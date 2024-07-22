import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor

class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.task_count = 1
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List App")
        self.setGeometry(300, 300, 500, 400)

        layout = QVBoxLayout()

        self.task_entry = QLineEdit()
        self.task_entry.setStyleSheet(" border: 1px solid #ccc;")
        layout.addWidget(self.task_entry)

        add_button = QPushButton("Add Task")
        add_button.setStyleSheet("background-color: #4CAF50; color: #fff; border: none; border-radius: 5px; padding: 5px 10px;")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        self.task_list = QListWidget()
        self.task_list.setStyleSheet(" border: 1px solid #ccc;")
        layout.addWidget(self.task_list)

        remove_button = QPushButton("Remove Task")
        remove_button.setStyleSheet("background-color: #f44336; padding: 5px 10px;")
        remove_button.clicked.connect(self.remove_task)
        layout.addWidget(remove_button)

        complete_button = QPushButton("Complete Task")
        complete_button.setStyleSheet("background-color: #8bc34a; padding: 5px 10px;")
        complete_button.clicked.connect(self.complete_task)
        layout.addWidget(complete_button)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_entry.text()
        if task:
            item = QListWidgetItem(f"{self.task_count}. {task}")
            item.setBackground(QColor("white"))
            self.task_list.addItem(item)
            self.task_entry.clear()
            self.task_count += 1

    def remove_task(self):
        selected_task_index = self.task_list.currentRow()
        if selected_task_index!= -1:
            self.task_list.takeItem(selected_task_index)

    def complete_task(self):
        selected_task_index = self.task_list.currentRow()
        if selected_task_index!= -1:
            completed_task = self.task_list.takeItem(selected_task_index)
            completed_task.setText(f"[Done] {completed_task.text()}")
            completed_task.setBackground(QColor("green"))
            self.task_list.addItem(completed_task)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoListApp()
    todo_app.show()
    sys.exit(app.exec_())
