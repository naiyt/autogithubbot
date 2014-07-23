from bs4 import BeautifulSoup, SoupStrainer
from html import unescape
from urllib import parse
from github import GitHub, BadUser, BadRepo
import logging

class Parser:

    def __init__(self):
        pass

    def parse(self, message):
        soup = BeautifulSoup(unescape(message.body_html), parse_only=SoupStrainer('a'))
        for link in soup:
            repo_and_user = self._parse_path(link)
            if repo_and_user:
                return True, self._make_message(message, repo_and_user[0], repo_and_user[1])
        return False, ''

    def _parse_path(self, link):
        if link.has_attr('href'):
            url = parse.urlparse(link['href'])
            if self._check_url(url):
                return self._get_user_and_repo(url.path)
        return False

    def _check_url(self, url):
        return url.netloc == 'github.com' and url.path

    def _get_user_and_repo(self, path):
        path = path[1:] if path[0] == '/' else path
        path = path.split('/')
        if len(path) >= 2:
            return path[0], path[1]
        return False

    def _make_message(self, message, user, repo):
        github = GitHub()
        try:
            git_user = github.user(user)
        except BadUser:
            logging.error("Uh oh! {} doesn't seem to be a valid GitHub user.".format(user))
            return False
        try:
            git_repo = github.repo(user, repo)
        except BadRepo:
            logging.error("Uh oh! Can't connect to {}'s repo {}.".format(user, repo))
            return False
        # TODO - this is ugly, setup Jinja or some other templating here instead.
        message = """
**[{title}]({url})** - *A {language} repository written by [{author}]({author_url})*

> {description}

{stars} stars, {forks} forks

Clone this repository: `{clone}`

---
[I'm a bot](https://github.com/naiyt/autogithubbot) that posts info about GitHub repositories. [Create your own bot](https://github.com/naiyt/reddit-replier)! (Just be nice about it.)
    """.format(title=git_repo.name, url=git_repo.url, language=git_repo.language,
                   description=git_repo.description, author=git_repo.author,
                   author_url=git_user.url,
                   stars=git_repo.stars, forks=git_repo.forks, clone=git_repo.clone_url)
        return message

