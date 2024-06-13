from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors 
import MySQLdb

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123456789987654321mM."
app.config["MYSQL_DB"] = "sonic"
app.config["MYSQL_PORT"] = 9500

mysql = MySQL(app)

@app.route("/")
def index():
  return "<h1>Hello index</h1>"

@app.route("/add_user", methods=["POST"])
def add_user():
  data = request.json
  username = data.get("username")
  email = data.get("email")
  password = data.get("password")
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  try:
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.connection.commit()
    response = {"status": "Success", "message": "User added successfully"}
    status_code = 200
  except MySQLdb.IntegrityError:
    response = {"status": "Error", "message": "Email already exists"}
    status_code = 400
  cursor.close()
  return jsonify(response), status_code

@app.route("/check_user", methods=["POST"])
def check_user():
  data = request.json
  username = data.get("username")
  email = data.get("email")
  password = data.get("password")

  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute("SELECT * FROM users WHERE email=%s AND password = %s AND username = %s;", 
                 (username, email, password))
  user = cursor.fetchone()
  cursor.close()
  if user:
    return jsonify({"status": "success", "message": "User exists", "user": user}), 200
  else:
    return jsonify({"status": "error", "message": "Invalid email or password", "user": user}), 400

@app.route("/delete_user", methods=["DELETE"])
def delete_user():
  data = request.get_json()
  if not data or 'user_id' not in data:
    return jsonify({"error": "Invalid input"}), 400
  
  user_id = data["user_id"]
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  try:
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id, ))
    mysql.connection.commit()
    if cursor.rowcount == 0:
      return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
  except MySQLdb.Error as e:
    mysql.connection.rollback()
    return jsonify({"error": str(e)}), 500
  finally:
    cursor.close()
    

if __name__ == "__main__":
  app.run(port=3000, debug=True) # http://127.0.0.1:3000