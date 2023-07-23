from flask import Flask
from Connection import Connection

class Api:
    def connect(self):
        return Connection()

    def __init__(self):
        self.app = Flask(__name__)
        self.connection = self.connect()
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return "Home"

        
        @self.app.route('/topN/<string:topN>', methods=['GET'])
        def get_topN(topN):
            if topN < 1 or topN > 100:
                return "Invalid range: Value must be from 1 to 100."
            else:
                return topN

if __name__ == '__main__':
    api = Api()
    api.app.run()