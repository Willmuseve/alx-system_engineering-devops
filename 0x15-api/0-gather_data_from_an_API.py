#!/usr/bin/python3
"""A python script that uses a REST API for a given employeeID
 and returns a todo list progress"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    eName = response.json().get('name')

    link_t = url + "/todos"
    response = requests.get(link_t)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(eName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
