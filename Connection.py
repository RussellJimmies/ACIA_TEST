from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

class Connection:
    def __init__(self):
        load_dotenv()  
        DB_HOST = os.getenv('DB_HOST')  
        DB_NAME = os.getenv('DB_NAME')  
        DB_USER = os.getenv('DB_USER')  
        DB_PW = os.getenv('DB_PW')  
        self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)