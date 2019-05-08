from datetime import datetime, timedelta
import requests
import json
import argparse


URL_SEARCH_REPOSITORIES = 'https://api.github.com/search/repositories'
URL_GET_ISSUES = 'https://api.github.com/issues'
DEFAULT_DAY = 7
DEFAULT_AMOUNT = 20


def valid_params(string=None, *args):
    value_param = int(string)
    print(args)
    if not value_param or 1 > value_param > 1000:
        msg = '{} is min 1 or bolshe 1000'
        raise argparse.ArgumentTypeError(msg)
    return value_param


def get_params_cmd():
    parser = argparse.ArgumentParser(description='Getting popular projects on github')
    parser.add_argument('-d', '--days', default=DEFAULT_DAY, type=valid_params(minv=1, maxv=1000), help='Repository age in days')
    parser.add_argument('-a', '--amt', default=DEFAULT_AMOUNT, type=valid_params(minv=1, maxv=1000),
                        help='Amount of repositories 1..1000')
    params = parser.parse_args()

    #TODO test amt <=1000

    return params


def get_params_request(days):
    day_max_created = datetime.utcnow().date() - timedelta(days=days)
    date_for_parameter = day_max_created.strftime('%Y-%m-%d')
    return {
        'q': 'created>{}'.format(date_for_parameter),
        'sort': 'stars'
            }


def get_repositories():
    #params[page] = page
    response = requests.get(URL_SEARCH_REPOSITORIES, params)


def get_trending_repositories(top_size):
    trending_repositories = []
    while len(trending_repositories) < top_size:
        pass


    return

def get_open_issues_amount(repo_owner, repo_name):
    pass


def main():
    params = get_params_cmd()
    days, amount = params['days'], params['amt']
    trending_repositories = get_trending_repositories(days, amount)


if __name__ == '__main__':
    '''header = {'User-Agent': 'mamedovvms'}
    response = requests.get('https://api.github.com/search/repositories',
                            params={'q': 'created:>=2019-05-07', 'page': 35, 'sort': 'stars'})
    #+created_at:2016-12-20T12:26:11Z
    decode_json = response.json()
    print(json.dumps(decode_json, indent=4, ensure_ascii=False))
    #print(len(decode_json['items']))
    #main()'''
    params = get_params_cmd()
    print(params)
