import mysql.connector
from mysql.connector import Error

class ToDoListApp:
    def __init__(self):
        self.db_url = "localhost"
        self.user = "root"
        self.password = "WJ28@krhps"
        self.database = "mydb"

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host=self.db_url,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def add_task(self, task):
        """Add a new task to the database."""
        query = "INSERT INTO tasks (description) VALUES (%s)"
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, (task,))
                connection.commit()
                print("Task added successfully")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def view_tasks(self):
        """View all tasks in the database."""
        query = "SELECT * FROM tasks"
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                print("\n===== All Tasks =====")
                for (id, description, is_completed) in result:
                    status = "Completed" if is_completed else "Pending"
                    print(f"{id}: {description} [{status}]")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def mark_task_as_complete(self, task_id):
        """Mark a specified task as complete."""
        query = "UPDATE tasks SET is_completed=true WHERE id=%s"
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, (task_id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Task marked as complete")
                else:
                    print("Task not found")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def delete_task(self, task_id):
        """Delete a specified task from the database."""
        query = "DELETE FROM tasks WHERE id=%s"
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, (task_id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def run(self):
        """Run the to-do list application."""
        while True:
            print("\n===== To-Do List Application =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                task = input("Enter task description: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                complete_id = int(input("Enter task ID to mark as complete: "))
                self.mark_task_as_complete(complete_id)
            elif choice == '4':
                delete_id = int(input("Enter task ID to delete: "))
                self.delete_task(delete_id)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
