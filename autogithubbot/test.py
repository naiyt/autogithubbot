import unittest
from github import GitHub, BadUser, BadRepo
from parser import parser
from replier import replier

class Message:
    def __init__(self, body):
        self.body_html = body

class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_message_success(self):
        message1 = Message(
            'You should properly reply to: <a href="https://github.com/naiyt/trello-rss">Trello-RSS</a>'
        )
        message2 = Message(
            'You should properly reply w/trailing slash: <a href="https://github.com/naiyt/trello-rss/">Trello-RSS</a>'
        )
        message3 = Message(
            'Please reply if given extra info after user/repo: <a href="https://github.com/naiyt/trello-rss/README.md'
        )
        self.assertEquals(parser(message1), ('naiyt', 'trello-rss'))
        self.assertEquals(parser(message2), ('naiyt', 'trello-rss'))
        self.assertEquals(parser(message3), ('naiyt', 'trello-rss'))


    def test_message_failure_without_github_link(self):
        message = Message(
            'Do not reply to me! <a href="https://natecollings.com">Nate</a>'
        )
        self.assertFalse(parser(message))

    def test_message_failure_with_github_link_no_repo(self):
        message1 = Message(
            'Do not reply! No repo! <a href="https://github.com/naiyt">Naiyt</a>'
        )
        message2 = Message(
            'Do not reply! No user! <a href="https://github.com">Naiyt</a>'
        )
        self.assertFalse(parser(message1))
        self.assertFalse(parser(message2))


class TestReplier(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.replied_message = """
[trello-rss](https://github.com/naiyt/trello-rss)
A Python repository written by [naiyt](https://github.com/naiyt)
Creates an RSS feed to keep track of updates from Trello boards you belong to
10 watchers, 10 stars, 0 forks
Clone this repository: git clone git@github.com:naiyt/trello-rss.git

[I'm a bot](https://github.com/naiyt/autogithubbot) that posts info about GitHub repositories. [Create your own bot](https://github.com/naiyt/reddit-replier)!
"""
        self.message = Message(
            'You should properly reply to: <a href="https://github.com/naiyt/trello-rss">Trello-RSS</a>'
        )

    def test_message_creation(self):
        reply = replier(self.message, 'naiyt', 'trello-rss')
        self.assertEquals(reply, self.replied_message)

    def test_parser_replier_integration(self):
        result = parser(self.message)
        args = [self.message]
        args.extend(result)
        reply = replier(*args)
        self.assertEquals(reply, self.replied_message)

    def test_parser_with_bad_user(self):
        self.assertRaises(BadUser, replier, self.message, 'naiytfds', 'trello-rss')

    def test_parser_with_bad_repo(self):
        self.assertRaises(BadRepo, replier, self.message, 'naiyt', 'trellofdsfds-rss')


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


if __name__ == '__main__':
    unittest.main(warnings='ignore')