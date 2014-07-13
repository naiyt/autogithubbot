from github import GitHub

def replier(message, username, repo):
    github = GitHub()
    user = github.user(username)
    repo = github.repo(username, repo)
    message = """
[{title}]({url})
A {language} repository written by [{author}]({author_url})
{description}
{watchers} watchers, {stars} stars, {forks} forks
Clone this repository: {clone}

[I'm a bot](https://github.com/naiyt/autogithubbot) that posts info about GitHub repositories. [Create your own bot](https://github.com/naiyt/reddit-replier)!
""".format(title=repo.name, url=repo.url, language=repo.language,
               description=repo.description, author=repo.author,
               author_url=user.url, watchers=repo.watchers,
               stars=repo.stars, forks=repo.forks, clone=repo.clone_url)
    return message