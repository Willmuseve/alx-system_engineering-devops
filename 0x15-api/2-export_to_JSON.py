#!/usr/bin/python3
"""Export to JSON"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    eName = response.json().get('username')

    link_t = url + "/todos"
    response = requests.get(link_t)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": eName
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
