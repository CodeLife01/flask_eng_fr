#!/usr/bin/env python3
# Author : Arthur Thouvenin
# Contact : athouvenin [at] outlook.fr
# Created : 09/09/2021
# Last update : 09/09/2021
"""
This is the presentation of the module

"""

# Import dependencies
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

LANGUAGE_TRANSLATOR_APIKEY = os.getenv('LANGUAGE_TRANSLATOR_APIKEY')
LANGUAGE_TRANSLATOR_IAM_APIKEY = os.getenv('LANGUAGE_TRANSLATOR_IAM_APIKEY')
LANGUAGE_TRANSLATOR_URL = os.getenv('LANGUAGE_TRANSLATOR_URL')
LANGUAGE_TRANSLATOR_AUTH_TYPE = os.getenv('LANGUAGE_TRANSLATOR_AUTH_TYPE')

# Authenticate
authenticator = IAMAuthenticator(LANGUAGE_TRANSLATOR_APIKEY)
lt = LanguageTranslatorV3(version="2018-05-01",authenticator=authenticator)
lt.set_service_url(LANGUAGE_TRANSLATOR_URL)

def english_to_french(request):
    """
    translate english to french
    """
    if request is None:
        return None
    response = lt.translate(text=request,model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation

def french_to_english(request):
    """
    translate french to english
    """
    if request is None:
        return None
    response = lt.translate(text=request,model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation
