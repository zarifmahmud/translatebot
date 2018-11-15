import requests
from yandex_key import * #Contains my API key for Yandex translations.
import urllib.parse

yandexurl = "https://translate.yandex.net/api/v1.5/tr/translate?key={}&options=1".format(yandexkey)

def translation_params(text: str, lang: str):
    """
    Need to add user given parameters to yandexurl, so this takes them in, and URL encodes them to make them URL
    friendly.
    """
    encode_dict = {"text": text, "lang": lang}
    print(urllib.parse.urlencode(encode_dict))

translation_params("This is a test", "French")

