const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const db = new sqlite3.Database('database.db');

app.use(cors());
app.use(bodyParser.json());

// Initialize DB
function initDb() {
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    movie TEXT,
    seats TEXT
  )`);
}

// Register
app.post('/register', (req, res) => {
  const { username, password } = req.body;
  const stmt = db.prepare('INSERT INTO users (username, password) VALUES (?, ?)');
  stmt.run(username, password, err => {
    if (err) return res.status(400).json({ message: 'Username already exists' });
    res.status(201).json({ message: 'Registration successful' });
  });
  stmt.finalize();
});

// Login
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  db.get('SELECT * FROM users WHERE username=? AND password=?', [username, password], (err, row) => {
    if (row) {
      res.json({ message: 'Login successful' });
    } else {
      res.status(401).json({ message: 'Invalid credentials' });
    }
  });
});

// Book tickets
app.post('/book', (req, res) => {
  const { username, movie, seats } = req.body;
  const seatList = seats.join(',');
  const stmt = db.prepare('INSERT INTO bookings (username, movie, seats) VALUES (?, ?, ?)');
  stmt.run(username, movie, seatList, err => {
    if (err) return res.status(500).json({ message: 'Booking failed' });
    res.json({ message: 'Booking successful' });
  });
  stmt.finalize();
});

// Get user bookings
app.get('/bookings/:username', (req, res) => {
  const username = req.params.username;
  db.all('SELECT movie, seats FROM bookings WHERE username=?', [username], (err, rows) => {
    if (err) return res.status(500).json([]);
    res.json(rows);
  });
});

app.listen(port, () => {
  initDb();
  console.log(`Server running at http://localhost:${port}`);
});
