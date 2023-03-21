"""
    llmapi_cli

    llmapi is open api for Large Language Models
    llmapi_cli is llmapi's client

    :date:      03/08/2023
    :author:    llmapi <llmapi@163.com>
    :homepage:  https://llmapi.io/
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2023 llmapi. All rights reserved
"""
from threading import Thread
import sys
import json
import os
import argparse as ap
from argparse import RawTextHelpFormatter
import getpass
import requests
import time
def _make_post(url,content):
    try:
        res = requests.post(url, data = json.dumps(content))
        rep = res.json()
        return rep
    except Exception:
        return {'code':-1,'msg':'request failed'}

class LLMClient():
    def __init__(self, host:str = 'https://api.llmapi.io', apikey:str = '', bot_type:str = 'mock'):
        self.host = host
        self.apikey = apikey
        self.bot_type = bot_type
        self.session = self._start_session()
        if self.session == 0:
            print('start session failed')
            exit()

    def _start_session(self):
        url = self.host + '/v1/chat/start'
        content = {'apikey':self.apikey, 'bot_type':self.bot_type}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            return rep['session']
        else:
            print("error message : ", rep['msg'])
            return 0

    def _end_session(self):
        try:
            url = self.host + '/v1/chat/end'
            content = {'apikey':self.apikey, 'session':self.session}
            r = _make_post(url,content)
            return r
        except Exception:
            return None

    def ask(self, prompt:str):
        url = self.host + '/v1/chat/ask'
        content = {'apikey':self.apikey, 'session':self.session, 'content':prompt, 'timeout':60}
        rep = _make_post(url,content)

        if rep['reply'] == 'None':
            return -1,'timeout'
        if rep['code'] == 0:
            return rep['code'],rep['reply']
        else:
            return rep['code'],rep['msg']

    def __str__(self):
        print(f"| [host]:{self.host}")
        print(f"| [session]:{self.session}")
        print(f"| [bot_type]:{self.bot_type}")
        return ""
