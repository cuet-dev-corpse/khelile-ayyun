from constants import TOP_25_TAGS
from services.cf_api.methods import problemset_problems
from services.db import get_handle


def print_top_25_tags():
    tags = {}
    for problem in problemset_problems():
        for tag in problem.tags or []:
            tags[tag] = tags.get(tag, 0) + 1

    top_25_tags = []
    for k, v in tags.items():
        top_25_tags.append((v, k))
    for tag in sorted(top_25_tags)[-25:]:
        print(f'"{tag[1]}",')
    print("\nIGNORED TAGS:")
    for tag in sorted(top_25_tags)[:-25]:
        print(f'"{tag}",')


# print_top_25_tags()
# print(len(TOP_25_TAGS))
# print(get_handle(123))