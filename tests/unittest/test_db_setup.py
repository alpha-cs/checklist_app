# tests/test_db_setup.py
import unittest
from database.db_setup import setup_database


class TestDatabaseSetup(unittest.TestCase):

    def test_database_connection(self):
        """Test if the database connection is established successfully."""
        session = setup_database()
        self.assertIsNotNone(session)  # Check if session is not None


if __name__ == '__main__':
    unittest.main()
