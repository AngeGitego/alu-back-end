#!/usr/bin/python3
"""
This script fetches tasks owned by a specific user from an API
and exports the data in CSV format.

Requirements:
- Records all tasks owned by the specified user
- CSV format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name: USER_ID.csv
- Print the number of tasks written to the CSV file
"""

import csv
import requests
import sys

def fetch_user_tasks(user_id):
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        # Fetch tasks and user information
        tasks_response = requests.get(url_tasks, params={"userId": user_id})
        user_response = requests.get(url_user)

        tasks = tasks_response.json()
        user = user_response.json()

        return tasks, user

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def export_tasks_to_csv(tasks, user):
    user_id = user['id']
    username = user['username']
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            csv_writer.writerow([user_id, username, task["completed"], task["title"]])

    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    tasks, user = fetch_user_tasks(user_id)
    csv_filename = export_tasks_to_csv(tasks, user)

    print(f"Number of tasks in CSV: {len(tasks)}")
    print(f"CSV file '{csv_filename}' has been created successfully.")
