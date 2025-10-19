from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Nutrition page
@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

# Motivation page
@app.route('/motivation')
def motivation():
    return render_template('motivation.html')

# Supplements page
@app.route('/supplements')
def supplements():
    return render_template('supplements.html')

# Workout page
@app.route('/workout')
def workout():
    return render_template('workout.html')

# Blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Privacy Policy page
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

# Email subscription (dummy)
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    # Here you can add code to save email in database or send to mailing list
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
