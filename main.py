import logging
from database.db_setup import setup_database
from utils.config_loader import load_settings
from gui.app_gui import initialize_gui
from errors.error_handler import setup_logging, log_detailed_exception


def main():
    try:
        # Set up logging
        setup_logging()

        logging.info("Starting the application")

        # Set up the database connection
        session = setup_database()

        # Load application settings
        load_settings()

        # Initialize and start the GUI
        root = initialize_gui()
        root.mainloop()

    except Exception as e:
        log_detailed_exception()
        raise  # Optionally re-raise the exception after logging


if __name__ == '__main__':
    main()
