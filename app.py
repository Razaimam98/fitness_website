from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --------- Home Page ---------
@app.route('/')
def home():
    return render_template('home.html')

# --------- About Page ---------
@app.route('/about')
def about():
    return render_template('about.html')

# --------- Privacy Policy Page ---------
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

# --------- Blog Pages ---------
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

# --------- Sitemap Route ---------
@app.route('/sitemap.xml')
def sitemap():
    """Serve sitemap.xml from the project root"""
    return send_from_directory(os.path.join(app.root_path), 'sitemap.xml')

# --------- Run App ---------
if __name__ == '__main__':
    # Use debug=True only for local development
    app.run(debug=True)
