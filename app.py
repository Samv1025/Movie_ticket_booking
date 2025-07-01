from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 movie TEXT,
                 seats TEXT)''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Registration successful'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    username = data['username']
    movie = data['movie']
    seats = ','.join(data['seats'])
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (username, movie, seats) VALUES (?, ?, ?)", (username, movie, seats))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Booking successful'})

@app.route('/bookings/<username>', methods=['GET'])
def get_bookings(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT movie, seats FROM bookings WHERE username=?", (username,))
    bookings = [{'movie': row[0], 'seats': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(bookings)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
