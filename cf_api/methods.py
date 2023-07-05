from typing import Optional
import requests
from objects import Problem, Status
from exceptions import CFStatusFailed

BASE_URL = "https://codeforces.com/api"


def problemset_problems(tags: list[str] = [], problemset_name: Optional[str] = None) -> list[Problem]:
    params = {
        'tags': ';'.join(tags),
        'problemsetName': problemset_name
    }
    data = requests.get(
        url=BASE_URL + "/problemset.problems",
        params=params,
    ).json()
    if data['status'] == Status.FAILED:
        raise CFStatusFailed
    return [Problem(**prob) for prob in data.json()['result']['problems']]


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
