import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '0f6a786d1adab8450cb9486c44c6179b1a61e91a'
    
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')        
        return response.json()
    
    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    secim = input("1-Find User\n 2- Get Repository 3- Create Repository \n 4- Exit\n Seçim: ")

    if secim =='4':
        break
    else:
        if secim == '1':
            username =input("username: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepository(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input("repository name : ")
            result = github.createRepository(name)
            print(result)
            print("Succeed!!!!")
        else:
            print('Yanlış')
