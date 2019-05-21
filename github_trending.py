from datetime import datetime, timedelta
import requests


def get_request_params(time_delta, top_size):
    time_start = datetime.utcnow().date() - timedelta(days=time_delta)
    time_start_str = time_start.strftime('%Y-%m-%d')
    return {
        'q': 'created:>{}'.format(time_start_str),
        'sort': 'stars',
        'per_page': top_size
    }


def get_trending_repositories(url, time_delta, top_size):
    params = get_request_params(time_delta, top_size)
    response = requests.get(url, params)
    return response.json()['items']


def get_open_issues(repo_owner, repo_name):
    url_template = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    params = {
        'state': 'open',
        'per_page': '100',
    }
    page = 0
    while True:
        page += 1
        params['page'] = page
        response = requests.get(url_template, params=params)
        issues = response.json()
        if issues:
            yield from issues
        else:
            return False


def get_open_issues_amount(repo_owner, repo_name):
    issues_amount = 0
    for issue in get_open_issues(repo_owner, repo_name):
        if 'id' in issue and not 'pull_request' in issue:
            issues_amount += 1
    return issues_amount


def main():
    url_search_repositories = 'https://api.github.com/search/repositories'
    time_delta = 7
    top_size = 20

    template_response = '''
    Name: {}
    URL: {}
    Stars: {}
    Open issues: {}
    '''
    trending_repositories = get_trending_repositories(
        url_search_repositories,
        time_delta,
        top_size
    )
    for repo in trending_repositories:
        print(template_response.format(
            repo['name'],
            repo['html_url'],
            repo['stargazers_count'],
            get_open_issues_amount(repo['owner']['login'], repo['name'])
        ))


if __name__ == '__main__':
    main()
