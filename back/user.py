from db import mysql

def register_user(name,email,password):

    cursor = mysql.connection.cursor()

    query = """
    INSERT INTO users(name,email,password)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (name,email,password)
    )

    mysql.connection.commit()

    cursor.close()