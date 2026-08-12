import os
import sqlite3
import hashlib
import time
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init_db():
    conn = sqlite3.connect('foro.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            parent_id INTEGER DEFAULT NULL,
            fecha TEXT NOT NULL,
            imagen TEXT DEFAULT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_user_id():
    user_ip = request.remote_addr or "127.0.0.1"
    return hashlib.md5(user_ip.encode()).hexdigest()[:6]

@app.route('/')
def index():
    conn = sqlite3.connect('foro.db')
    c = conn.cursor()
    
    c.execute('SELECT id, user_id, mensaje, fecha, imagen FROM posts ORDER BY id ASC')
    posts_raw = c.fetchall()
    
    c.execute('SELECT parent_id, id, user_id FROM posts WHERE parent_id IS NOT NULL')
    replies_raw = c.fetchall()
    conn.close()

    replies_map = {}
    for parent_id, reply_id, user_id in replies_raw:
        if parent_id not in replies_map:
            replies_map[parent_id] = []
        replies_map[parent_id].append({'id': reply_id, 'user_id': user_id})

    posts = []
    for p in posts_raw:
        posts.append({
            'id': p[0],
            'user_id': p[1],
            'mensaje': p[2],
            'fecha': p[3],
            'imagen': p[4],
            'replies': replies_map.get(p[0], [])
        })

    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def new_post():
    mensaje = request.form.get('mensaje', '').strip()
    file = request.files.get('imagen')
    filename = None

    if file and allowed_file(file.filename):
        filename = f"{int(time.time())}_{secure_filename(file.filename)}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if not mensaje and not filename:
        return redirect(url_for('index'))

    user_id = get_user_id()
    fecha = time.strftime("%d/%m/%y(%a)%H:%M:%S")
    parent_id = None

    if mensaje.startswith('>>'):
        try:
            first_word = mensaje.split()[0]
            parent_id = int(first_word.replace('>>', ''))
        except ValueError:
            pass

    conn = sqlite3.connect('foro.db')
    c = conn.cursor()
    c.execute('INSERT INTO posts (user_id, mensaje, parent_id, fecha, imagen) VALUES (?, ?, ?, ?, ?)',
              (user_id, mensaje, parent_id, fecha, filename))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
