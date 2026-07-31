from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):

    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "anshul@2006"
    app.config["MYSQL_DB"] = "career_ai"

    mysql.init_app(app)