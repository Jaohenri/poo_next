"""
Module for the TaskManagementSystem class.
This module defines a simple system to add, list,
mark as completed and remove tasks.
"""

class TaskManagementSystem:
    """
    Manages a collection of tasks, allowing addition, listing,
    status update and removal.

    Attributes:
        _tasks (dict): A dictionary where keys are task IDs
                       (integers) and values are dictionaries representing
                       each task (e.g., {'description': 'Study Python', 'completed': False}).
        _next_id (int): The next available ID for a new task,
                        ensuring uniqueness.
    """

    def __init__(self):
        """
        Initializes the task management system with an empty list.
        """
        self._tasks = {}
        self._next_id = 1

    def add_task(self, description: str) -> int:
        """
        Adds a new task to the system.

        Args:
            description (str): The description of the task to be added.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If the task description is empty or not a string.
        """
        if not isinstance(description, str) or not description.strip():
            raise ValueError("The task description cannot be empty.")

        task = {
            'description': description.strip(),
            'completed': False
        }
        self._tasks[self._next_id] = task
        self._next_id += 1
        return self._next_id - 1 # Returns the ID of the task that was just added

    def list_tasks(self) -> list:
        """
        Lists all tasks currently in the system.

        Returns:
            list: A list of dictionaries, where each dictionary represents a task
                  and includes its 'id', 'description' and 'completed'.
        """
        complete_list = []
        for task_id, details in self._tasks.items():
            complete_list.append({
                'id': task_id,
                'description': details['description'],
                'completed': details['completed']
            })
        return complete_list

    def complete_task(self, task_id: int) -> bool:
        """
        Marks a specific task as completed.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if the task was marked as completed, False if it was already completed.

        Raises:
            ValueError: If the task ID is not found.
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")

        if self._tasks[task_id]['completed']:
            return False # Already was completed

        self._tasks[task_id]['completed'] = True
        return True

    def remove_task(self, task_id: int) -> None:
        """
        Removes a task from the system.

        Args:
            task_id (int): The ID of the task to be removed.

        Raises:
            ValueError: If the task ID is not found.
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        del self._tasks[task_id]

if __name__ == '__main__':
    ...
