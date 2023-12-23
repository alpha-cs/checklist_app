import tkinter as tk
from tkinter import ttk


def create_settings_tab(parent):
    tab_settings = ttk.Frame(parent)
    label = tk.Label(tab_settings, text="Settings Tab")
    label.pack(pady=10)
    return tab_settings
