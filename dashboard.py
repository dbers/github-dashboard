from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    """Show the main dashboard"""
    return render_template('index.html')

@app.route('/githup/<organization>')
def get_orgs_github_data(organization):
    """Get the an organizations github information
    
    Arguments:
        name (string) -- Name of organization
        
    Return: Json data
    """
    return 'Get info for %s' % organization