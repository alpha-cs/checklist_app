import tkinter as tk
from tkinter import ttk


def create_user_tab(parent):
    tab_user = ttk.Frame(parent)
    label = tk.Label(tab_user, text="User Account Tab")
    label.pack(pady=10)
    return tab_user
