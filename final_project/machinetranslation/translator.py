import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

VERSION = '2022-07-04'

authenticator = IAMAuthenticator(f'{API_KEY}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{URL}')

def english_to_french(english_text):
    """
    translate from english to french
    """

    french_text = language_translator.translate(text=english_text,source="en",target="fr").get_result()['translations'][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    translate from french to english
    """
    
    english_text = language_translator.translate(text=french_text,source="fr",target="english").get_result()['translations'][0]["translation"]
    return english_text
