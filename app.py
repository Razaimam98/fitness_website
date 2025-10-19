from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/motivation')
def motivation():
    return render_template('motivation.html')

@app.route('/supplements')
def supplements():
    return render_template('supplements.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    # In real projects, you would save this email in a database or email list
    print(f"New subscriber: {email}")
    return redirect(url_for('home'))

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
