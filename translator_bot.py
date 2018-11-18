"""
Reddit bot for translation
"""
import praw
import schedule
from translator_api import *
import time



reddit = praw.Reddit('bot1',
                     user_agent='Windows:translationbot:v0 (by /u/translate-this)')

print(reddit.user.me())
