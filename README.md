# Task Management System using Design Patterns

A Task Management System developed for a small design team, demonstrating the application of three core Object-Oriented Design Patterns in Python: Factory Method, Observer and Singleton.

---

##  Project Goal

To create a flexible, maintainable, and robust task management system that supports dynamic task creation, assignment and real-time user notification of status changes.

---

## Design Patterns Implemented

1.  **Factory Method Pattern:**
    * **Purpose:** To dynamically create different types of tasks (e.g., 'Design', 'Review', 'Deployment') without specifying the exact class of the task object to be created.
2.  **Observer Pattern:**
    * **Purpose:** To notify users (observers, e.g., 'Jordan' or 'Alex') automatically whenever there is a change in the status of their assigned tasks.
3.  **Singleton Pattern:**
    * **Purpose:** To ensure that only **one instance** of the central `TaskManager` exists and is responsible for managing all tasks across the entire system.

---

## System Functionality

The program demonstrates the following core requirements:

* Creation of at least three distinct task types.
* Dynamic assignment of tasks to multiple users.
* Changing task statuses (e.g., from "Not Started" to "Completed").
* Automatic notification of users upon task status changes.

---

## How to Run

1.  Ensure you have Python installed.
2.  Execute the main program file (e.g., `task_manager.py`).
    ```bash
    python task_manager.py
    ```
3.  [cite_start]The output will show task creation, assignment, status updates, and the resulting user notifications (e.g., "Jordan has been notified...")[cite: 156].
