#!/usr/bin/python3
"""
Using a REST API and an EMP_ID, save info about their TODO list in a csv file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <EMP_ID>")
        sys.exit(1)

    EMP_ID = sys.argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee data
    employee_response = requests.get(BASE_URL + f'/users/{EMP_ID}')
    if employee_response.status_code != 200:
        print(f"Failed to retrieve employee data: {employee_response.status_code}")
        sys.exit(1)
    
    employee_data = employee_response.json()
    EMPLOYEE_NAME = employee_data.get("username")

    # Retrieve employee's TODO list
    todos_response = requests.get(BASE_URL + f'/todos?userId={EMP_ID}')
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO list: {todos_response.status_code}")
        sys.exit(1)

    todos_data = todos_response.json()

    # Write data to CSV file
    csv_filename = f"{EMP_ID}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            csv_writer.writerow([EMP_ID, EMPLOYEE_NAME, str(todo["completed"]), todo["title"]])

    print(f"CSV file '{csv_filename}' has been created.")
