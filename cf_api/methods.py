from typing import Optional
import requests
from objects import Problem

BASE_URL = "https://codeforces.com/api"


def problemset_problems(tags: list[str] = [], problemset_name: Optional[str] = None) -> list[Problem]:
    params = {
        'tags': ';'.join(tags),
        'problemsetName': problemset_name
    }
    response = requests.get(
        url=BASE_URL + "/problemset.problems",
        params=params,
    )
    return [Problem(**prob) for prob in response.json()['result']['problems']]


def problemset_reset_status(count, problemset_name):
    pass


def user_info(handles):
    pass


def user_rating(handle):
    pass


def user_status(handle, _from, count):
    pass


if __name__ == '__main__':
    print(problemset_problems())
