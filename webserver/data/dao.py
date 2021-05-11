from webserver.data.models.models import User, Repositories

def save_new_user(db, username):
    try:
        new_user = User()
        new_user.username = username
        db.add(new_user)
        db.flush()
        db.commit()
    except Exception as error:
        print(error)
        return None


def get_user_data(db, username):
    try:
        return db.query(User).filter(User.username == username).first()
    except Exception as error:
        print(error)
        return None


def get_repo_data(db, username, repo_name):
    try:
        return db.query(Repositories).filter(Repositories.user_name == username).filter(Repositories.name == repo_name).first()
    except Exception as error:
        print(error)
        return None


def update_repo_details(db, username,repo_details):
    try:
        db.query(Repositories).filter(Repositories.user_name == username).filter(Repositories.name == repo_details["name"]).update(
            {
                "url": repo_details["html_url"],
                "name": repo_details["name"],
                "access_type": repo_details["is_private"],
                "created_at": repo_details["created_at"],
                "updated_at": repo_details["updated_at"],
                "size": repo_details["size"],
                "stargazers_count": repo_details["stargazers_count"],
                "watchers_count": repo_details["stargazers_count"]
            })
        db.flush()
        db.commit()
    except Exception as error:
        print(error)
        return None


def get_repos_from_user(db, username):
    repositories = []
    try:
        response = db.query(Repositories).filter(Repositories.user_id == get_user_data(db, username).id)
        for repo in response:
            repositories.append(repo.name)
        return repositories
    except Exception as error:
        print(error)
        return {"error":"Could not fint user locally."}


def save_new_repo(db, username, repo_details):
    if(get_user_data(db, username)==None):
        save_new_user(db, username)

    if(get_repo_data(db, username, repo_details["name"])):
        update_repo_details(db, username, repo_details)
    else:
        try:
            new_repo = Repositories()
            new_repo.user_id = get_user_data(db, username).id
            new_repo.user_name = username
            new_repo.url = repo_details["html_url"]
            new_repo.name = repo_details["name"]
            new_repo.is_private = repo_details["is_private"]
            new_repo.created_at = repo_details["created_at"]
            new_repo.updated_at = repo_details["updated_at"]
            new_repo.size = repo_details["size"]
            new_repo.stargazers_count = repo_details["stargazers_count"]
            new_repo.watchers_count = repo_details["watchers_count"]

            db.add(new_repo)
            db.flush()
            db.commit()
        except Exception as error:
            print(error)
            return None
