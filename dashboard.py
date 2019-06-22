from flask import Flask, render_template, jsonify
from flask_caching import Cache

from github_data import repo_stats

app = Flask(__name__, static_url_path="/static")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

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

    # first try to load from cache
    cache_key = "repos-{}".format(organization)
    data = cache.get( cache_key )
    if data is None:
        data = repo_stats(organization)
        cache.set(cache_key, data)
    
    # create return format DataTables needs
    datatables_data = {
        "data": data
    }
    return jsonify(datatables_data)


