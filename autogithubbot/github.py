from apihelper import Api
import secret as s

class BadUser(Exception):
	pass

class BadRepo(Exception):
	pass

class GitHub:
	def __init__(self):
		self.api = Api('https://api.github.com',
			headers={'Authorization': 'token {}'.format(s.token)},
			user_agent='AutoGitHubBot by github.com/naiyt')

	def repo(self, username, repo):
		info = self.api.get('/repos/{}/{}'.format(username, repo))
		if info.status_code != 200:
			raise BadRepo('Repo {} does not exist'.format(repo))
		return Repo(info.json())

	def user(self, username):
		info = self.api.get('/users/{}'.format(username))
		if info.status_code != 200:
			raise BadUser('User {} does not exist'.format(username))
		return User(info.json())

class Repo:
	def __init__(self, repo_info):
		self.info = repo_info
		self.name = repo_info['name']
		self.url = repo_info['html_url']
		self.stars = repo_info['stargazers_count']
		self.forks = repo_info['forks']
		self.watchers = repo_info['watchers_count']
		self.language = repo_info['language']
		self.description = repo_info['description']
		self.clone_url = 'git clone {}'.format(repo_info['ssh_url'])
		self.author = repo_info['owner']['login']


class User:
	def __init__(self, user_info):
		self.info = user_info
		self.name = user_info['login']
		self.url = user_info['html_url']
		self.number_repos = user_info['public_repos']
		self.followers = user_info['followers']

