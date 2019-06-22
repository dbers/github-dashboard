# Github Dashboard

Currently Supports loading up an organizations repos and sotrting by:
- name
- stars
- forks
- contributors

Do to the slowness of computing `contributors`, the data is cached when fetching from services.

## Installation 
Use the following steps to run project (in shell)
```
git clone git@github.com:dbers/github-dashboard.git
cd github-dashboard
pipenv install
```

## Running Project 
Requires GITHUB_TOKEN is set.  Then just run:
```

pipenv shell
./run.sh
```

in browser go to `http://127.0.0.1:5000`

