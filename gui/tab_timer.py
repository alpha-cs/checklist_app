import tkinter as tk
from tkinter import ttk


def create_timer_tab(parent):
    tab_timer = ttk.Frame(parent)
    label = tk.Label(tab_timer, text="Timer Tab")
    label.pack(pady=10)
    return tab_timer
