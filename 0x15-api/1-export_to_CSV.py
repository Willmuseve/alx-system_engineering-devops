#!/usr/bin/python3
"""Exports the data in CSV Fformat"""

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

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, eName, task.get('completed'),
                               task.get('title')))
