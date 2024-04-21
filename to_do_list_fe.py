# Import the tkinter module
import tkinter as tk

# Define the ToDoList class
class ToDoList(tk.Tk):
  # Initialize the ToDoList class
  def __init__(self):
    # Call the __init__ method of the parent class (tk.Tk)
    super().__init__()

    # Set the window title
    self.title('To-Do List')

    # Set the window size
    self.geometry('300x200')

    # Initialize the tasks list
    self.tasks = []

    # Create a Label widget for the tasks label
    self.task_label = tk.Label(self, text='Tasks:', font=('Courier', 25, 'italic', 'bold'),fg='tan', bg=None)

    # Add the Label widget to the window using the pack method
    self.task_label.pack()

    # Create an Entry widget for the task input
    self.task_entry = tk.Entry(self)

    # Add the Entry widget to the window using the pack method
    self.task_entry.pack(padx=10, pady=10)

    # Create a Listbox widget for the to-do list
    self.task_list = tk.Listbox(self, height=10)

    # Add the Listbox widget to the window using the pack method
    self.task_list.pack()

    # Create a Button widget for the add task button
    self.add_button = tk.Button(self, text='Add Task', command=self.add_task, font=('Courier', 16, 'italic', 'bold'), fg='black', bg=None)

    # Add the Button widget to the window using the pack method
    self.add_button.pack(padx=10, pady=10)

    # Create a Button widget for the remove task button
    self.remove_button = tk.Button(self, text='Remove Task', command=self.remove_task, font=('Courier', 16, 'italic', 'bold'), fg='black', bg=None)

    # Add the Button widget to the window using the pack method
    self.remove_button.pack(padx=10, pady=10)

    # Set the background color of the window and the widgets to beige
    self.config(bg='antiquewhite')
    self.task_entry.config(bg='grey')
    self.task_list.config(bg='grey')
   

  # Define the add_task method
  def add_task(self):
    # Get the text from the Entry widget
    task = self.task_entry.get()

    # Add the text to the tasks list
    self.tasks.append(task)

    # Insert the text into the Listbox widget
    self.task_list.insert(tk.END, task)

    # Clear the Entry widget
    self.task_entry.delete(0, tk.END)

  # Define the remove_task method
  def remove_task(self):
    # Get the selected task from the Listbox widget
    selected_task = self.task_list.get(tk.ACTIVE)

    # Remove the selected task from the tasks list
    self.tasks.remove(selected_task)

    # Delete the selected task from the Listbox widget
    self.task_list.delete(tk.ACTIVE)

# Create an instance of the ToDoList class
app = ToDoList()

# Start the tkinter event loop
app.mainloop()