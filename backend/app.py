from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Store route
@app.route('/store')
def store():
    return render_template('store.html')

# Projects route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Login route
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Explore route
@app.route('/explore')
def explore():
    return render_template('explore.html')

# Recycle route (for Start Recycling button)
@app.route('/recycle')
def recycle():
    return render_template('recycle.html')

# Explore Items route
@app.route('/explore-items')
def explore_items():
    return render_template('explore-items.html')

if __name__ == '__main__':
    app.run(debug=True)
