"""
My Reddit translate bot

TODO
- Find way of getting translation from the output without the other XML stuff
- Open new Reddit account, get it karma so you can test it out, and integrate with PRAW.
"""
import requests
from yandex_key import *  # Contains my API key for Yandex translations.
import urllib.parse

yandexurl = "https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&options=1&".format(yandexkey)
# We're using Yandex's option to return content in a JSON format rather than XML because the requests package
# has a built in way of dealing with JSON.


def translation_params(text: str, lang: str):
    """
    Need to add user given parameters to yandexurl, so this takes them in, and URL encodes them to make them URL
    friendly, and returns a completed URL.

    >>> translation_params("This is a test", "en-fr")
    text=This+is+a+test&lang=en-fr

    """
    encode_dict = {"text": text, "lang": lang}
    urlext = urllib.parse.urlencode(encode_dict)
    return yandexurl + urlext

# print(translation_params("This is a test", "en-fr"))


def translate(text: str, lang: str) -> str:
    """
    The actual translation
    """
    yanurl = translation_params(text, lang)
    r = requests.get(yanurl)
    output_dict = r.json()  # Returns dictionary with translated text, and otheri info.
    return output_dict["text"][0]

#{'code': 200, 'detected': {'lang': 'en'}, 'lang': 'en-fr', 'text': ['Ceci est un test']}



print(translate("This is a test", "fr"))


