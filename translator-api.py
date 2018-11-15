import requests
from yandex_key import * #Contains my API key for Yandex translations.
import urllib.parse

yandexurl = "https://translate.yandex.net/api/v1.5/tr/translate?key={}&options=1&".format(yandexkey)


def translation_params(text: str, lang: str):
    """
    Need to add user given parameters to yandexurl, so this takes them in, and URL encodes them to make them URL
    friendly.

    >>> translation_params("This is a test", "en-fr")
    text=This+is+a+test&lang=en-fr

    """
    encode_dict = {"text": text, "lang": lang}
    return urllib.parse.urlencode(encode_dict)

# print(translation_params("This is a test", "en-fr"))

def translate(text: str, lang: str) -> str:
    """
    The actual translation
    """
    urlext = translation_params(text, lang)
    yan = yandexurl
    yan += urlext
    r = requests.get(yan)
    textyan = r.text
    print(textyan)

translate("Cheese", "fr")


