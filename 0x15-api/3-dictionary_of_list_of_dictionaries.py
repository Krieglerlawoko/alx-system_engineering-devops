#!/usr/bin/python3
"""
returns info about employee todo list progress
given ID using rest API
"""

import requests
import json
from sys import argv


if __name__ == "__main__":

    import requests
    import json
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for a in todos:
            if a.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": a.get('title'),
                            "completed": a.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as fil:
        json.dump(todoAll, fil)
