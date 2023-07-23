from flask import Flask
from Connection import Connection
from Dao import Dao
import psycopg2

class Api:

    def __init__(self):
        self.app = Flask(__name__)
        self.dao = Dao()
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return f"""
            <pre>
            Welcome to my API!

            <u>Endpoints:</u> 

            <b>/topN/int from 1 - 100</b>
            Returns json of topN documents from the crawl table, sorted by score (descending)
            </pre>
            """
        
        @self.app.route('/topN/<string:topN>', methods=['GET'])
        def get_topN(topN):
            json = None
            try:
                self.connection = Connection()
                json = self.dao.get_topN(self.connection, topN)

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally: 
                self.connection.close_connection()
                return json

if __name__ == '__main__':
    api = Api()
    api.app.run(debug=True)