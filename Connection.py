from dotenv import load_dotenv
import os
import psycopg2

class Connection:
    def __init__(self):
        load_dotenv()  
        self.DB_HOST = os.getenv('DB_HOST')  
        self.DB_NAME = os.getenv('DB_NAME')  
        self.DB_USER = os.getenv('DB_USER')  
        self.DB_PW = os.getenv('DB_PW')  
        self.DB_VIEW_NAME = os.getenv('DB_VIEW_NAME')  
        self.DB_VIEW_SCHEMA = os.getenv('DB_VIEW_SCHEMA')  
        self.connection = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PW, host=self.DB_HOST)

    def close_connection(self):
        self.connection.close()