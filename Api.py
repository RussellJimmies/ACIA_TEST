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
            Bienvenue à mon API!

            <u>Endpoints:</u> 

            <b>/topN/int from 1 - 100</b>
            Retourne un document JSON des topN documents de la table crawl, selon leur score (décroissant).
            </pre>
            """
        
        @self.app.route('/topN/<string:topN>', methods=['GET'])

        
        def get_topN(topN: int):
            """
                Retourne un document JSON des topN documents de la table crawl, selon leur score (décroissant).

                Paramètres :
                    topN (int) : Le nombre d'éléments à récupérer depuis la base de données.

                Retour :
                    json : Les données récupérées au format JSON.
            """
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
    api.app.run()