
#!/usr/bin/python3
"""Returns info for employee using rest API"""

import requests
import json
from sys import argv


if __name__ == "__main__":

    sR = requests.Session()

    id = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sR.get(idURL)
    employeeName = sR.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for a in json_req:
        if a['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for a in json_req:
        if a['completed']:
            print("\t " + a.get('title'))

