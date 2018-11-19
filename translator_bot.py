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

for unread in praw.models.util.stream_generator(reddit.inbox.unread):
    # This creates a generator that continuously returns unread messages in my inbox.
    print(unread)
    print(unread.body)
    unread.mark_read()
    if "translate-this" in unread.body and not unread.is_root:
        translation = translate(unread.parent().body, 'en')
        unread.reply(translation)

    # else:
    #     unread.reply("You are a root")


