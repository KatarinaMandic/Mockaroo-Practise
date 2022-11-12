import mysql.connector as con

class DB:

    DATABASE = None

    @staticmethod
    def connect():
        if DB.DATABASE == None:
            DB.DATABASE = con.connect(
                host = 'localhost',
                port = 3306,
                user = 'pyadmin2',
                password = '1234',
                database = 'people_db'
            )
        return DB.DATABASE

    @staticmethod
    def select_distinct_countries():
        db = DB.connect()
        c = db.cursor()

        c.execute("SELECT DISTINCT country FROM people ORDER BY country ASC;")
        records = c.fetchall()

        countries = []

        for r in records:
            countries.append(r[0])
        
        return countries