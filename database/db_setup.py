# database/db_setup.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
import datetime


def setup_database():
    engine = create_engine('mysql+mysqlconnector://root:5662@localhost/windb')
    metadata = MetaData()

    # Define the tasks table
    tasks_table = Table('tasks', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('description', String(255)),
                        Column('frequency', String(50)),
                        Column('points', Integer),
                        Column('negative_points', Integer),
                        Column('creation_date', DateTime,
                               default=datetime.datetime.utcnow)
                        )

    # Define the task_log table
    task_log_table = Table('task_log', metadata,
                           Column('log_id', Integer, primary_key=True),
                           Column('task_id', Integer, ForeignKey('tasks.id')),
                           Column('date_completed', DateTime,
                                  default=datetime.datetime.utcnow),
                           Column('points_awarded', Integer)
                           )

    # Create tables if they don't exist
    metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()
