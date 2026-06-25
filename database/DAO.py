from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeneri():
        conn=DBConnect.get_connection()
        result=[]
        cursor=conn.cursor(dictionary=True)
        query="""SELECT *
        FROM genre"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["genreId"])

        cursor.close()
        conn.close()
        return result