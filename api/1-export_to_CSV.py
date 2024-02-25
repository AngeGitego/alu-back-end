#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Fetch TODOs for the employee
        response_todos = requests.get(url_todos)
        response_user = requests.get(url_user)

        if response_todos.status_code != 200 or response_user.status_code != 200:
            print("Failed to fetch data from the API")
            sys.exit(1)

        todos_data = response_todos.json()
        user_data = response_user.json()

        if not todos_data:
            print("Employee has no tasks")
            sys.exit(0)

        # Create CSV file
        filename = f"{employee_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write header row
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write task data
            for task in todos_data:
                csv_writer.writerow([task["userId"], user_data["username"], task["completed"], task["title"]])

        print(f"CSV file '{filename}' generated successfully.")

    except Exception as e:
        print("An error occurred:", str(e))
