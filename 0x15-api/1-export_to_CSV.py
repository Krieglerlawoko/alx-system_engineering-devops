#!/usr/bin/python3
"""
returns info about employee todo list using 
rest API
"""

import json
import csv
import requests
from sys import argv


if __name__ == "__main__":

    sR = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sR.get(idURL)
    employeeName = sR.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for a in json_req:
        if a['completed']:
            totalTasks += 1

    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for a in json_req:
            write.writerow([idEmp, usr, a.get('completed'), a.get('title')])
