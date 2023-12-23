import tkinter as tk
from tkinter import ttk
import datetime


def create_main_tab(parent):
    tab_main = ttk.Frame(parent)

    # Create a PanedWindow
    paned_window = ttk.PanedWindow(tab_main, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=True)

    # Create Left and Right Frames
    create_left_side(paned_window)
    create_right_side(paned_window)

    return tab_main


def create_left_side(paned_window):
    left_frame = ttk.Frame(paned_window)
    paned_window.add(left_frame, weight=2)

    days_frame = ttk.Frame(left_frame)
    days_frame.pack(fill=tk.BOTH, expand=True)

    for i in range(-2, 3):
        day = datetime.date.today() + datetime.timedelta(days=i)
        day_frame = create_day_frame(days_frame, day)
        day_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def create_right_side(paned_window):
    right_frame = ttk.Frame(paned_window)
    paned_window.add(right_frame, weight=1)

    # Points Display
    points_label = tk.Label(right_frame, text="Total Points: 0")
    points_label.pack(pady=20)

    # Add Task Section
    add_task_label = tk.Label(right_frame, text="Add a Task:")
    add_task_label.pack(pady=10)

    task_entry = tk.Entry(right_frame)
    task_entry.pack(pady=10)

    add_task_button = tk.Button(
        right_frame, text="Add Task", command=lambda: add_task(task_entry.get()))
    add_task_button.pack(pady=10)


def create_day_frame(parent, day):
    frame = ttk.Frame(parent, borderwidth=1, relief=tk.SUNKEN)
    label = tk.Label(frame, text=day.strftime(
        '%A\n%Y-%m-%d'), font=('Arial', 12, 'bold'))
    label.pack(pady=5)

    task_listbox = tk.Listbox(frame)
    task_listbox.pack(fill=tk.BOTH, expand=True)

    return frame


def add_task(task):
    print(f"Task to add: {task}")
