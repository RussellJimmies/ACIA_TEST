import psycopg2
from flask import jsonify

class Dao:
    def __init__(self):
        self.cur = None

    def get_topN(self, connection, topN):
        try:
            if int(topN) < 1 or int(topN) > 100:
                resp = jsonify("Value must be from 1 to 100.")
                resp.status_code = 400
            else:
                self.cur = connection.connection.cursor()
                self.cur.execute(f"""
                                SELECT url 
                                FROM "{connection.DB_VIEW_SCHEMA}"."{connection.DB_VIEW_NAME}"
                                LIMIT {topN}
                                """)
                #print(self.cur.fetchall())
                resp = jsonify(self.cur.fetchall())

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            return resp