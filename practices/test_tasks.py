"""
Unit tests for TaskManagementSystem class.

This module contains comprehensive tests for the TaskManagementSystem,
validating task creation, listing, completion, and removal functionality.
""""""
        Test that task IDs are generated sequentially and uniquely.
        
        Verifies that:
        - The first task receives ID 1
        - The second task receives ID 2
        - Each new task increments the ID counter
        """
        

import unittest
from tasks import TaskManagementSystem

class TestTaskManagementSystem(unittest.TestCase):
    """
    Test suite for the TaskManagementSystem class.
    
    Tests all core functionality of the task management system including:
    - Task ID generation and uniqueness
    - Task creation with validation
    - Task listing and retrieval
    - Task status updates
    - Task removal
    """

    def test_id_add_task(self):
        """
        Test that ValueError is raised when adding an empty task description.
        
        Verifies that the system validates input and rejects empty strings
        as task descriptions.
        """
        tasks = TaskManagementSystem()
        id_task1 = tasks.add_task("Clean the dishes")
        id_task2 = tasks.add_task("Study Python")

        self.assertEqual(id_task1, 1)
        self.assertEqual(id_task2, 2)

    def test_add_task_exception(self):
        with self.assertRaises(ValueError):
            tasks = TaskManagementSystem()
            tasks.add_task("")

    def test_list_tasks(self):
        tasks = TaskManagementSystem()
        id_task1 = tasks.add_task("Clean the dishes")
        tasks_list = tasks.list_tasks()

        self.assertEqual(tasks_list[0]["id"], id_task1)
        self.assertEqual(tasks_list[0]["description"],"Clean the dishes")
        self.assertFalse(tasks_list[0]["completed"])

    def test_complete_task(self):
        tasks = TaskManagementSystem()
        id_task1 = tasks.add_task("Clean the dishes")
        tasks.complete_task(id_task1)
        tasks_list = tasks.list_tasks()


        self.assertTrue(tasks_list[0]["completed"])

    def test_remove_task(self):
        tasks = TaskManagementSystem()
        id_task1 = tasks.add_task("Clean the dishes")
        tasks.remove_task(id_task1)
        tasks_list = tasks.list_tasks()
        task_ids = [task["id"] for task in tasks_list]
        self.assertNotIn(id_task1, task_ids)

if __name__ == "__main__":
    unittest.main()
