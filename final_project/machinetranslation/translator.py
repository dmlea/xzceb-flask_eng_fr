'''module for english to french & french to english'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('6rS-dGqlctV0dU0z1jcPK8sRFYLgF3fW1mtKjRmQiqGd')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    '''function for english to french'''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    '''function for french to english'''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text
