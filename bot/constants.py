"""
Contains all the constants in one file so that we can change it without altering the main code
"""
from discord import Color

PRIMARY_COLOR = Color.from_rgb(65, 135, 235)

ABOUT_TITLE = "About খেলিলি আইয়ুন"
ABOUT_DESCRIPTION = (
    "খেলিলি আইয়ুন is a discord bot created to work as a helping hand for CP communities\n"
    "The name of the bot was inspired by মেজ্জান হাইলে আইয়ুন\n\n"
    ":point_right: Check out our GitHub repo [here](https://github.com/cuet-dev-corpse/khelile-ayyun)\n"
    ":construction: The bot is currently under construction. All features may not work properly"
)
ABOUT_FOOTER = "Made with 💖 by CUET Dev Corpse"

IGNORE_FIELDS = [
    "lastOnlineTimeSeconds",
    "registrationTimeSeconds",
    "avatar",
    "titlePhoto",
]

TOP_25_TAGS = [
    "hashing",
    "interactive",
    "probabilities",
    "shortest paths",
    "divide and conquer",
    "dsu",
    "geometry",
    "*special",
    "two pointers",
    "bitmasks",
    "combinatorics",
    "number theory",
    "strings",
    "trees",
    "dfs and similar",
    "binary search",
    "sortings",
    "graphs",
    "brute force",
    "constructive algorithms",
    "data structures",
    "dp",
    "greedy",
    "implementation",
    "math",
]

EMOJI_WARNING = ":warning:"
EMOJI_SUCCESS = ":white_check_mark:"