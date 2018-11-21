"""
Reddit bot for translation

Note: Interesting error when trying to do
if "translate-this" in unread.body and unread.is_root:
Python parses it as if we're trying to find "translate-this" str both in unread, and unread.is_root,
which obviously won't work, as unread.is_root is a bool. But this works
if "translate-this" in unread.body and not unread.is_root:
I guess the 'not' helps Python parse it better
"""
import praw
import schedule
from translator_api import *
import time



reddit = praw.Reddit('bot1',
                     user_agent='Windows:translationbot:v0 (by /u/translate-this)')

# for comment in reddit.subreddit('all').stream.comments():
#     if "translate-this" in comment.lower():
#         comment.reply("I see this")

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
            translation = translate(unread.parent().body, 'en')
            unread.reply(translation)

    # else:
    #     unread.reply("You are a root")

# user = reddit.redditor("GrassNova")
# print(user.comment_karma)

run_bot()
