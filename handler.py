import requests, os
from pprint import pprint

accessToken = os.environ.get('TOKEN')

baseUrl = 'https://gitlab.com/api/v4'
# TODO: encript before commit
headers = {"Private-Token": f"{accessToken}"}
userId = '5937077'

# print(headers)

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

    return()

print(getProjectCommits())