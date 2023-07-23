from flask import Flask
from Connection import Connection
from Dao import Dao
import psycopg2
import psycopg2.extras


class Api:

    def __init__(self):
        self.app = Flask(__name__)
        self.dao = Dao()
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return "Home"

        
        @self.app.route('/topN/<string:topN>', methods=['GET'])
        def get_topN(topN):
            if int(topN) < 1 or int(topN) > 100:
                return "Invalid range: Value must be from 1 to 100."
            else:
                # create sql query demanding N results try/except/finally
                # jsonify
                try:
                    self.connection = Connection()
                    self.dao.get_topN(self.connection, topN)

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally: 
                    self.connection.close_connection()
                    return topN

if __name__ == '__main__':
    api = Api()
    api.app.run(debug=True)