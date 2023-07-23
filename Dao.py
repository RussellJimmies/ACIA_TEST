import psycopg2
import psycopg2.extras

class Dao:
    def __init__(self):
        self.cur = None

    def get_topN(self, connection, topN):
        try:
            self.cur = connection.connection.cursor()
            self.cur.execute(f"""
                            SELECT url FROM "{connection.DB_VIEW_SCHEMA}"."{connection.DB_VIEW_NAME}"
                            LIMIT {topN}
                            """)
            print("Row Count: " , self.cur.rowcount)

            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            connection.close_connection()