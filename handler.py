import requests
import os
from pprint import pprint

accessToken = os.environ['TOKEN']

baseUrl = 'https://gitlab.com/api/v4'
# TODO: encript before commit
headers = {f"'Private-Token':{accessToken}"}
userId = '5937077'

def getUserProjects():
    projectIdList = []
    url = f'{baseUrl}/users/{userId}/projects'
    r = requests.get(url, headers=headers)
    userProjects = r.json()

    for project in userProjects:
        projectIdList.append(project['id'])

    return(projectIdList)


def getProjectCommits():
    commitsList = []
    for projectId in getUserProjects():
        url = f"{baseUrl}/projects/{projectId}/repository/commits"
        r = requests.get(url, headers=headers)
        commitsPerProjectList = r.json()
        commitsList.append(commitsPerProjectList)

    print(commitsList)

    # return()

print(getProjectCommits())