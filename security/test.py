import mysql.connector

def check_user_in_db(db_name, db_user, db_password, user_email, db_host='localhost'):
    try:
        # Connexion à la base de données
        db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = db.cursor()

        # Requête pour vérifier l'utilisateur
        query = f"SELECT * FROM order_client WHERE email = '{user_email}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print(f"User {user_email} exists in the database.")
        else:
            print(f"User {user_email} does not exist in the database.")

        db.close()
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

# Paramètres de connexion
db_user = 'root'
db_password = 'root'
db_name = 'fruiticart'
user_email = 'louise.ferreira@edu.devinci.fr'

# Vérification de l'utilisateur dans la base de données
check_user_in_db(db_name, db_user, db_password, user_email)
