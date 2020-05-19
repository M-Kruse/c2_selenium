#!/usr/bin/env python3
#Quick sample work for command and control of multiple selenium windows
#For demonstration purposes, this is tooled specifically for reddit

from selenium import webdriver

class C2Selenium(object):
	"""docstring for C2Selenium"""
	def __init__(self):
		super(C2Selenium, self).__init__()
		self.worker_list = []

	def get_worker_by_handle(self, handle):
		for worker in self.worker_list:
			if worker.current_window_handle == handle:
				return worker

	def spawn_worker(self):
		self.worker = webdriver.Firefox()
		self.worker_list.append(self.worker)
		return self.worker

	def load_page(self, worker_idx, url):
		worker = self.worker_list[worker_idx]
		worker.get(url)

	def open_frontpage_comments(self, worker_idx):
		worker = self.worker_list[worker_idx]
		worker.get("https://old.reddit.com")
		elements = worker.find_elements_by_xpath("//div[contains(@data-context, 'listing')]")
		for i in range(0, 2):
			e = elements[i]
			worker = self.spawn_worker()
			worker.get("https://old.reddit.com" + e.get_attribute("data-permalink"))

	def focus_window(self, worker_idx):
		worker = self.worker_list[worker_idx]
		worker.maximize_window()

	def close_window(self, worker_idx):
		worker = self.worker_list[worker_idx]
		worker.close()
		del self.worker_list[worker_idx]