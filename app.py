from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'guests.db'

# Initialize database
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT DEFAULT 'pending'
            )
        ''')
        conn.commit()
        conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM guests')
    guests = [dict(id=row[0], name=row[1], status=row[2]) for row in c.fetchall()]
    conn.close()
    return render_template('index.html', guests=guests)

@app.route('/add', methods=['POST'])
def add_guest():
    name = request.form['name']
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO guests (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', added='true'))

@app.route('/update/<int:guest_id>/<status>')
def update_guest(guest_id, status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE guests SET status = ? WHERE id = ?', (status, guest_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:guest_id>')
def delete_guest(guest_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM guests WHERE id = ?', (guest_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)