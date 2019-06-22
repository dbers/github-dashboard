from github import Github
import asyncio

from .constants import GITHUB_ACCESS_TOKEN


REPO_DATA = []

def repo_stats(name, sort=None):
    """
    Get stats for a given organization
    """
    g = Github(GITHUB_ACCESS_TOKEN)
    github_org = g.get_organization(name)
    all_repos = github_org.get_repos()

    # build list of [ {name, stars, forks, contributors}, ''' ]
    REPO_DATA = []
    loop = asyncio.new_event_loop()
    for repo in all_repos:
        task = _get_stats(repo)
        future = loop.create_task(task)
    
    loop.run_until_complete(future)
    return REPO_DATA


async def _get_stats(repo):
    """
    Async function that will fetch stats needed. 
    Contributors takes to long.  only way to make this useable
    """
    # lack of better way to get this, make another call
    all_contributors = repo.get_stats_contributors()
    if all_contributors is None:
        total_contributors = 0
    else:
        total_contributors = len(all_contributors)

    data = {
        "name" : repo.name,
        "stars" : repo.stargazers_count,
        "forks" : repo.forks,
        "contributors" : total_contributors
    }
    # not ideal but having issues returning data from async functions and time is an issue
    REPO_DATA.append(data)
