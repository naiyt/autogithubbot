import unittest
from github import GitHub

'''
class TestGitHubRepo(unittest.TestCase):
    def setUp(self):
        self.github = GitHub()

    def test_getting_repo_name(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.name, 'reddit-replier')

    def test_getting_repo_link(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.url, 'https://github.com/naiyt/reddit-replier')

    def test_getting_repo_stars(self):
        repo = self.github.repo('naiyt', 'fireemblem')
        self.assertEqual(repo.stars, 0)

    def test_getting_repo_forks(self):
        repo = self.github.repo('naiyt', 'fireemblem')
        self.assertEqual(repo.forks, 0)

    def test_getting_repo_watchers(self):
        repo = self.github.repo('naiyt', 'fireemblem')
        self.assertEqual(repo.watchers, 0)

    def test_getting_repo_language(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.language, 'Python')

    def test_getting_repo_desc(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.description, 'Easily create Reddit bots that reply to comments based on specific criteria')

    def test_getting_repo_author(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.author, 'naiyt')

    def test_getting_cloning_info(self):
        repo = self.github.repo('naiyt', 'reddit-replier')
        self.assertEqual(repo.clone_url, 'git clone git@github.com:naiyt/reddit-replier.git')

class TestGitHubUser(unittest.TestCase):
    def setUp(self):
        self.github = GitHub()
        self.user = self.github.user('naiyt')

    def test_user_name(self):
        self.assertEqual(self.user.name, 'naiyt')

    def test_user_url(self):
        self.assertEqual(self.user.url, 'https://github.com/naiyt')

    def test_user_number_of_repos(self):
        self.assertEqual(self.user.number_repos, 28)

    def test_user_number_of_followers(self):
        self.assertEqual(self.user.followers, 4)
'''

if __name__ == '__main__':
    unittest.main(warnings='ignore')