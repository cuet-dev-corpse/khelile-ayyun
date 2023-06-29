import requests
from objects import Problem

def problemset_problems(tags: list[str] = None, problemset_name: str = None):
    params = {
        'tags': ';'.join(tags),
        'problemsetName': problemset_name
    }
    response = requests.get(f"https://codeforces.com/api/problemset.problems", params=params)
    return [Problem() for prob in response.json()]

def problemset_reset_status(count, problemset_name):
    pass

def user_info(handles):
    pass

def user_rating(handle):
    pass

def user_status(handle, _from, count):
    pass


if __name__ == '__main__':
    problemset_problems(tags=["implementation"])