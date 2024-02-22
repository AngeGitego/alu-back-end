import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = [task['title'] for task in todos_data if task['completed']]

        print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
        for task_title in done_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

