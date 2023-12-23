import tkinter as tk
from tkinter import ttk


def create_stats_tab(parent):
    tab_stats = ttk.Frame(parent)
    label = tk.Label(tab_stats, text="Statistics Tab")
    label.pack(pady=10)
    return tab_stats
