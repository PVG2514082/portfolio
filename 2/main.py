from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    abc = sqlite3.connect('resume.sqlite')
    abc.row_factory = sqlite3.Row
    return abc


@app.route('/')
def index():
    return render_template('123.html')


@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search')
    return render_template('search_results.html', search_term=search_term)


@app.route('/resume', methods=['GET', 'POST'])
def create_resume():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        salary = request.form.get('salary')
        experience = request.form.get('experience')
        place = request.form.get('location')
        resume = request.form.get('resumee')
        db_lp = sqlite3.connect('resume.sqlite')
        cursor_db = db_lp.cursor()
        print(experience, salary)
        a = len(db_lp.cursor().execute("SELECT * FROM res").fetchall())

        s = db_lp.cursor().execute("""INSERT INTO res VALUES (?, ?, ?, ?, ?, ?, ?)""", (a, name, email, resume, place, experience, salary)).fetchall()

        cursor_db.close()

        db_lp.commit()
        db_lp.close()

        return render_template('123.html')
    return render_template('create_resume.html')


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('wer.sqlite')
        cursor_db = db_lp.cursor()
        cursor_db.execute('SELECT password FROM aut WHERE login = ?', (Login,))
        pas = cursor_db.fetchall()

        cursor_db.close()
        try:
            if pas[0][0] != Password:
                return render_template('auth_bad.html')
        except:
            return render_template('auth_bad.html')

        db_lp.close()
        return render_template('aut.html')

    return render_template('authorization.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_registration():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('wer.sqlite')
        cursor_db = db_lp.cursor()
        a = len(db_lp.cursor().execute("SELECT * FROM aut").fetchall())
        s = db_lp.cursor().execute("""INSERT INTO aut VALUES (?, ?, ?)""", (a + 1, Login, Password,)).fetchall()

        cursor_db.close()

        db_lp.commit()
        db_lp.close()

        return render_template('successregis.html')

    return render_template('registration.html')

@app.route('/catalog')
def resume_list():
    conn = sqlite3.connect('resume.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM res')
    resume_data = cursor.fetchall()
    conn.close()
    return render_template('catalog.html', resume_data=resume_data)


if __name__ == '__main__':
    app.run(debug=True)