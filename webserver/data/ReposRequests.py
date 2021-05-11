import requests

from webserver.data.database import local_session
from webserver.data.dao import get_repos_from_user
from webserver.data.dao import save_new_repo


def get_repos(username, from_local):
    repositories = []
    if (from_local):
        repositories = get_repos_from_user(local_session(), username)
    else:
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        if (response.status_code == requests.codes.ok):
            for repo in response.json():
                repositories.append(repo["name"])

    return repositories


def get_repo_details(username, repo_name, save_data):
    response = requests.get(f'https://api.github.com/repos/{username}/{repo_name}')
    if (response.status_code == requests.codes.ok):
        response_json = {
            "name": response.json()["name"],
            "html_url": response.json()["html_url"],
            "is_private": response.json()["private"],
            "created_at": response.json()["created_at"],
            "updated_at": response.json()["updated_at"],
            "size": response.json()["size"],
            "stargazers_count": response.json()["stargazers_count"],
            "watchers_count": response.json()["watchers_count"],
        }

    if(save_data):
        save_new_repo(local_session(), username, response_json)

    return response_json
