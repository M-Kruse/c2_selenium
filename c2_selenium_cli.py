#!/usr/bin/env python3
#Quick sample work for cli interface of command and control selenium windows

from prompt_toolkit import prompt
from tabulate import tabulate

from c2_selenium import C2Selenium   

commands = ['list', 'stop', 'new', 'open', 'posts']
selenium_table_headers = ["Index", "Title"]

def wait_for_input():
    command = prompt('C2> ')
    return command

if __name__ == '__main__':
    c2 = C2Selenium()
    while True:
        table = []
        command = wait_for_input()
        command_list = command.split(" ")
        primary = command.split(" ")[0]
        if primary in commands:
            if primary == "list":
                if len(command_list) < 1:
                    print("[ERROR] Invalid input")
                    print("[INFO] Correct Syntax: list")
                else:
                    for idx, w in enumerate(c2.worker_list):
                        title = "None" if not w.title else w.title
                        title = title[:64]
                        table.append([idx, title])
                print(tabulate(table, selenium_table_headers))
            if primary == "new":
                if len(command_list) < 1:
                    print("[ERROR] Invalid input")
                    print("[INFO] Correct Syntax: new")
                else:
                    c2.spawn_worker()
            if primary == 'open':
                if len(command_list) < 3:
                    print("[ERROR] Invalid input")
                    print("[INFO] Correct Syntax: open <worker_idx> <url>")
                else:
                    c2.load_page(int(command_list[1]), command_list[2])
            if primary == 'posts':
                if len(command_list) < 2:
                    print("[ERROR] Invalid input")
                    print("[INFO] Correct Syntax: posts <worker_idx>")
                else:
                    c2.open_frontpage_comments(int(command_list[1]))
            if primary == 'stop':
                if len(command_list) < 2:
                    print("[ERROR] Invalid input")
                    print("[INFO] Correct Syntax: stop <worker_idx>")
                else:
                    c2.close_window(int(command_list[1]))