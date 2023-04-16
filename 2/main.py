from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

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
        phone = request.form.get('phone')
        resume = request.form.get('resume')
        # Create resume functionality here
        return render_template('resume_confirmation.html', name=name)
    else:
        return render_template('create_resume.html')

@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(('''SELECT password FROM login_passwords.db
                                                   WHERE login = '{}';
                                                   ''').format(Login))
        pas = cursor_db.fetchall()

        cursor_db.close()
        try:
            if pas[0][0] != Password:
                return render_template('auth_bad.html')
        except:
            return render_template('auth_bad.html')

        db_lp.close()
        return render_template('successfulauth.html')

    return render_template('authorization.html')

if __name__ == '__main__':
    app.run(debug=True)