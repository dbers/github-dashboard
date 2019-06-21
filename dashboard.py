from flask import Flask, render_template, jsonify

from github import repo_stats

app = Flask(__name__, static_url_path="/static")

@app.route('/')
@app.route('/<organization>')
def index(organization=None):
    """Show the main dashboard"""
    return render_template('index.html', organization=organization)

@app.route('/githup-data/<organization>')
def get_orgs_github_data(organization):
    """Get the an organizations github information
    
    Arguments:
        name (string) -- Name of organization
        
    Return: Json data
    """
    data = repo_stats(organization)
    return jsonify(data)


