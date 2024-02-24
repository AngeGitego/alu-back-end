#!/usr/bin/python3

"""
Script to fetch and display TODO list progress of an employee using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee whose progress needs to be fetched.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name', '')

        # Fetch todos
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Count completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))

        # Print progress
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo.get('completed'):
                print(f"\t{todo.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
