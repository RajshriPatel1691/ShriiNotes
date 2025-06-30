# from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
# import os, sqlite3

# app = Flask(__name__)
# app.secret_key = 'secret'
# DATABASE = 'users.db'

# def init_db():
#     with sqlite3.connect(DATABASE) as conn:
#         conn.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
#         conn.commit()

# @app.route('/')
# def index():
#     return redirect('/login')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         try:
#             with sqlite3.connect(DATABASE) as conn:
#                 conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
#                 conn.commit()
#             return redirect('/login')
#         except:
#             return "User already exists!"
#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         with sqlite3.connect(DATABASE) as conn:
#             cur = conn.cursor()
#             cur.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
#             if cur.fetchone():
#                 session['email'] = email
#                 return redirect('/home')
#             else:
#                 return "Invalid credentials!"
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     if 'email' not in session:
#         return redirect('/login')
#     return render_template('home.html', email=session['email'])

# @app.route('/notes/<subject>')
# def notes(subject):
#     if 'email' not in session:
#         return redirect('/login')
#     path = os.path.join('notes', subject)
#     files = os.listdir(path)
#     return render_template('notes.html', subject=subject, notes=files)

# @app.route('/download/<subject>/<filename>')
# def download_note(subject, filename):
#     return send_from_directory(os.path.join('notes', subject), filename, as_attachment=True)

# @app.route('/logout')
# def logout():
#     session.pop('email', None)
#     return redirect('/login')

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os, sqlite3

app = Flask(__name__)
app.secret_key = 'secret'
DATABASE = 'users.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
        conn.commit()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            with sqlite3.connect(DATABASE) as conn:
                conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
                conn.commit()
            return redirect('/login')
        except:
            return "User already exists!"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
            if cur.fetchone():
                session['email'] = email
                return redirect('/home')
            else:
                return "Invalid credentials!"
    return render_template('login.html')

@app.route('/home')
def home():
    if 'email' not in session:
        return redirect('/login')
    return render_template('home.html', email=session['email'])

@app.route('/notes/<subject>')
def notes(subject):
    if 'email' not in session:
        return redirect('/login')
    path = os.path.join('notes', subject)
    if not os.path.exists(path):
        return "Subject folder not found!"
    files = os.listdir(path)
    return render_template('notes.html', subject=subject, notes=files)

@app.route('/download/<subject>/<filename>')
def download_note(subject, filename):
    return send_from_directory(os.path.join('notes', subject), filename, as_attachment=True)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

