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
    commitsList = []
    commiterNameList = []
    uniqueCommiterNameList = []
    
    for projectId, projectName in getUserProjects().items():
        url = f"{baseUrl}/projects/{projectId}/repository/commits"
        r = requests.get(url, headers=headers)
        commitsPerProjectList = r.json()
        commitsList.append(commitsPerProjectList)
        print('Project ID: ', projectId,', Project Name: ', projectName)

        for commits in commitsList:
            for i in range(len(commits)):
                commiterNameList.append(commits[i]['committer_name'])

        counter = Counter(commiterNameList)

        print(counter.keys())

    return()

print(getProjectCommits())

# def handler(event, context):
#     print(getProjectCommits())
