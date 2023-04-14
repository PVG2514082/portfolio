from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('123.html')

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search')
    # Perform search functionality here
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

if __name__ == '__main__':
    app.run(debug=True)