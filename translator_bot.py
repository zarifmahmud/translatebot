"""
Reddit bot for translation

Note: Interesting error when trying to do
if "translate-this" in unread.body and unread.is_root:
Python parses it as if we're trying to find "translate-this" str both in unread, and unread.is_root,
which obviously won't work, as unread.is_root is a bool. But this works
if "translate-this" in unread.body and not unread.is_root:
I guess the 'not' helps Python parse it better

TODO
-Implement author check (prevent people from using it too much)
"""
import praw
import schedule
from translator_api import *
import time
import re

reddit = praw.Reddit('bot1',
                     user_agent='Windows:translationbot:v0 (by /u/translate-this)')

user_dict = {}


def karma_check(username) -> bool:
    """
    Checks if a given user has enough link and comment karma.
    """
    user = reddit.redditor(username)
    return user.link_karma > 10 and user.comment_karma > 350



def run_bot():
    """
    This is the function that runs the Reddit bot. It creates a generator that continuously returns unread messages
    to the bot's inbox, checks if "translate-this" is mentioned in the message (like in /u/translate-this), if the
    comment isn't a top-level comment, and if the user has enough karma to call the bot.
    """
    for unread in praw.models.util.stream_generator(reddit.inbox.unread):
        print(unread)
        print(unread.body)
        print(unread.author)
        unread.mark_read()
        if "translate-this" in unread.body and not unread.is_root and karma_check(str(unread.author)):
            if "translate-back" in unread.body:
                lang_detected = re.search(r'<.+>', unread.body).group(0).lstrip('<').rstrip('>')
                print(lang_detected)
                translation = translate(unread.parent().body, lang_detected)
            else:
                translation = translate(unread.parent().body, 'en')
            unread.reply(translation)
            if unread.author in user_dict:
                user_dict[unread.author] += 1
            else:
                user_dict[unread.author] = 1



# user = reddit.redditor("translate-bot")
# print(user.comment_karma)

run_bot()
