from datetime import datetime, timedelta
import requests


URL_SEARCH_REPOSITORIES = 'https://api.github.com/search/repositories'
TIME_DELTA = 7
TOP_SIZE = 20


def get_params_request():
    time_start = datetime.utcnow().date() - timedelta(days=TIME_DELTA)
    time_start_str = time_start.strftime('%Y-%m-%d')
    return {
        'q': 'created:>{}'.format(time_start_str),
        'sort': 'stars',
        'per_page': TOP_SIZE
    }


def get_trending_repositories():
    params = get_params_request()
    response = requests.get(URL_SEARCH_REPOSITORIES, params)
    return response.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    pass


def main():
    template_response = '''
    Name: {}
    URL: {}
    Stars: {}
    Open issues: {}
    '''
    trending_repositories = get_trending_repositories()
    for repo in trending_repositories:
        print(template_response.format(repo['name'],
                                       repo['html_url'],
                                       repo['stargazers_count'],
                                       repo['open_issues_count']))


if __name__ == '__main__':
    main()
