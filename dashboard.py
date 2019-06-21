from flask import Flask, render_template

app = Flask(__name__, static_url_path="static")

@app.route('/')
def index():
    """Show the main dashboard"""
    return render_template('index.html', name=name)


@app.route('/githup/<organization>')
def show_user_profile(organization):
    # show the user profile for that user
    return 'Get info for %s' % organization

@app.route('/githup/<organization>')
def show_user_profile(organization):
    # show the user profile for that user
    return 'Get info for %s' % organization