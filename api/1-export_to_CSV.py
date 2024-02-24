#!/usr/bin/python3

"""
Script to fetch and export TODO list progress of an employee to a CSV file using a REST API.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches TODO list progress of an employee from the API.

    Args:
        employee_id (int): The ID of the employee whose progress needs to be fetched.

    Returns:
        list: A list of dictionaries containing task details.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('username', '')

        # Fetch todos
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        return employee_name, todos_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


def export_to_csv(employee_id, employee_name, todos_data):
    """
    Exports TODO list progress of an employee to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos_data (list): A list of dictionaries containing task details.
    """
    if todos_data:
        filename = f"{employee_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for todo in todos_data:
                writer.writerow({
                    'USER_ID': employee_id,
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': str(todo.get('completed')),
                    'TASK_TITLE': todo.get('title')
                })
        print(f"Data exported to {filename}")
    else:
        print("No data to export.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, todos_data = get_employee_todo_progress(employee_id)
    export_to_csv(employee_id, employee_name, todos_data)

