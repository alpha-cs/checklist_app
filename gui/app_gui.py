import tkinter as tk
from tkinter import ttk
from gui.tab_main import create_main_tab
from gui.tab_user import create_user_tab
from gui.tab_timer import create_timer_tab
from gui.tab_stats import create_stats_tab
from gui.tab_settings import create_settings_tab


def initialize_gui():
    root = tk.Tk()
    root.title("Checklist Application")

    tab_control = ttk.Notebook(root)

    # Create each tab
    tab_main = create_main_tab(tab_control)
    tab_user = create_user_tab(tab_control)
    tab_timer = create_timer_tab(tab_control)
    tab_stats = create_stats_tab(tab_control)
    tab_settings = create_settings_tab(tab_control)

    # Add tabs to the tab control
    tab_control.add(tab_main, text='Main')
    tab_control.add(tab_user, text='User Account')
    tab_control.add(tab_timer, text='Timer')
    tab_control.add(tab_stats, text='Statistics')
    tab_control.add(tab_settings, text='Settings')

    tab_control.pack(expand=1, fill="both")

    return root
