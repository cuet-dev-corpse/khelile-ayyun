from enum import Enum


class Type(Enum):
    PROGRAMMING, QUESTION = range(2)


class ParticipantType(Enum):
    CONTESTANT, PRACTICE, VIRTUAL, MANAGER, OUT_OF_COMPETITION = range(5)


class Verdict(Enum):
    FAILED, OK, PARTIAL, COMPILATION_ERROR, RUNTIME_ERROR, WRONG_ANSWER, PRESENTATION_ERROR, TIME_LIMIT_EXCEEDED, MEMORY_LIMIT_EXCEEDED, IDLENESS_LIMIT_EXCEEDED, SECURITY_VIOLATED, CRASHED, INPUT_PREPARATION_CRASHED, CHALLENGED, SKIPPED, TESTING, REJECTED = range(
        17)


class Testset(Enum):
    SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, TESTS2, TESTS3, TESTS4, TESTS5, TESTS6, TESTS7, TESTS8, TESTS9, TESTS10 = range(
        14)


class User:
    handle: str
    email: str | None
    first_name: str | None
    last_name: str | None
    country: str | None
    city: str | None
    organization: str | None
    contribution: int
    rank: str
    rating: int
    max_rank: str
    max_rating: int
    last_online_time_seconds: int
    registration_time_seconds: int
    friend_of_count: int
    avatar: str
    title_photo: str


class RatingChange:
    contest_id: int
    contest_name: str
    handle: str
    rank: int
    rating_update_time_seconds: int
    old_rating: int
    new_rating: int


class Member:
    handle: str
    name: str | None


class Party:
    contest_id: int | None
    members: list[Member]
    participant_type: ParticipantType
    team_id: int | None
    team_name: str | None
    ghost: bool
    room: int | None
    start_time_seconds: int | None


class Problem:
    contest_id: int | None
    problemset_name: str | None
    index: str
    name: str
    type: Type
    points: float | None
    rating: int | None
    tags: list[str]


class Submission:
    id: int
    contest_id: int | None
    creation_time_seconds: int
    relative_time_seconds: int
    problem: Problem
    author: Party
    programming_language: str
    verdict: Verdict | None
    testset: Testset
    past_test_count: int
    time_consumed_millis: int
    memory_consumed_bytes: int
    points: int
