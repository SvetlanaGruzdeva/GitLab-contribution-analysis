import requests, os
from pprint import pprint
from collections import Counter

accessToken = os.environ.get('TOKEN')

baseUrl = 'https://gitlab.com/api/v4'
headers = {"Private-Token": f"{accessToken}"}
userId = '5937077'

def getUserProjects():
    projectsDict = {}
    url = f'{baseUrl}/users/{userId}/projects'
    r = requests.get(url, headers=headers)
    userProjects = r.json()

    for project in userProjects:
        # projectIdList.append(project['id'])
        projectsDict[project['id']] = project['name']

    return(projectsDict)


def getProjectCommits():
    rawStatsList = []
    
    for projectId, projectName in getUserProjects().items():
        url = f"{baseUrl}/projects/{projectId}/repository/commits"
        r = requests.get(url, headers=headers)
        commitsPerProjectList = r.json()
        print('Project ID: ', projectId,', Project Name: ', projectName)

        for commit in commitsPerProjectList:
            commitsPerProject = {}
            commitsPerProject['title'] = commit['title']
            commitsPerProject['committed_date'] = commit['committed_date']
            commitsPerProject['author_email'] = commit['author_email']

            rawStatsList.append(commitsPerProject)

        pprint(rawStatsList)


    return()

print(getProjectCommits())

# def handler(event, context):
#     print(getProjectCommits())
