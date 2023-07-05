from typing import Optional
import requests
from objects import Problem, RatingChange, Status, Submission, User
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
        raise CFStatusFailed(data['comment'])
    return [Problem(**problem) for problem in data['result']['problems']]


def problemset_recent_status(count: int) -> list[Submission]:
    params = {
        'count': count
    }
    data = requests.get(
        url=BASE_URL + "/problemset.recentStatus",
        params=params,
    ).json()
    if data['status'] == Status.FAILED:
        raise CFStatusFailed(data['comment'])
    return [Submission(**submission) for submission in data['result']]


def user_info(handles: list[str]) -> list[User]:
    params = {
        'handles': ';'.join(handles)
    }
    data = requests.get(
        url=BASE_URL + "/user.info",
        params=params,
    ).json()
    if data['status'] == Status.FAILED:
        raise CFStatusFailed(data['comment'])
    return [User(**user) for user in data['result']]


def user_rating(handle: str) -> list[RatingChange]:
    params = {
        'handle': handle
    }
    data = requests.get(
        url=BASE_URL + "/user.rating",
        params=params,
    ).json()
    if data['status'] == Status.FAILED:
        raise CFStatusFailed(data['comment'])
    return [RatingChange(**rating_change) for rating_change in data['result']]


def user_status(handle: str, _from: int, count: int):
    params = {
        'handle': handle,
        'from': _from,
        'count': count
    }
    data = requests.get(
        url=BASE_URL + "/user.status",
        params=params,
    ).json()
    if data['status'] == Status.FAILED:
        raise CFStatusFailed(data['comment'])
    return [Submission(**submission) for submission in data['result']]
