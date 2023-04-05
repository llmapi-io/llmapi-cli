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

from typing import Optional
import json
import requests
import numpy


class LLMClient():
    """
    A client for the llmapi.
    """

    def __init__(self, host: str = 'https://api.llmapi.io', bot_type: str = 'mock', apikey: Optional[str] = None, system: str = None):
        """
        Initializes the LLMClient.

        Args:
        - host (str): The url of llmapi server. Default is 'https://api.llmapi.io'.
        - bot_type (str): The type of bot to start. Default is 'mock'.
        - apikey (Optional[str]): The apikey to use for authentication. If None, no authentication is used. Default is None.

        Returns:
        - None.
        """
        self.host = host
        self.apikey = apikey
        self.bot_type = bot_type
        self.session_id = None
        self.system = system

    def _make_post(self, url: str, content: dict) -> dict:
        """
        Makes a post request to the llmapi server

        Args:
        - url (str): The url to post the request to.
        - content (dict): The content to include in the post request.

        Returns:
        - (dict): The response from the server.
        """
        try:
            headers = {'Content-Type': 'application/json'}
            if self.apikey is not None:
                content['apikey'] = self.apikey
            res = requests.post(url, headers=headers, json=content)
            rep = res.json()
            return rep
        except Exception:
            return {'code': -1, 'msg': 'request failed'}

    def start_session(self) -> bool:
        """
        Starts a new chat session.

        Args:
        - None.

        Returns:
        - (bool): True if the session was started successfully, False otherwise.
        """
        url = f"{self.host}/v1/chat/start"
        content = {'bot_type': self.bot_type, 'settings': {}}
        if self.system is not None:
            content['settings']['system'] = self.system
        rep = self._make_post(url, content)
        if 'code' in rep and rep['code'] == 0:
            self.session_id = rep['session']
            return True
        else:
            print(rep)
            return False

    def end_session(self) -> None:
        """
        Ends the current chat session.

        Args:
        - None.

        Returns:
        - None.
        """
        if self.session_id is None:
            return False
        url = f"{self.host}/v1/chat/end"
        content = {'session': self.session_id}
        self._make_post(url, content)
        self.session_id = None

    def ask(self, prompt: str, timeout: int = 60) -> tuple:
        """
        Asks a question to the llmapi and gets a response.

        Args:
        - prompt (str): The question to ask the llmapi.

        Returns:
        - (tuple[int,str]): A tuple with two values: the result code (0 for success, -1 for failure) and the response from the llmapi.
        """
        if self.session_id is None:
            return -1, 'session invalid'
        url = f"{self.host}/v1/chat/ask"
        content = {'session': self.session_id,
                   'content': prompt, 'timeout': timeout}
        rep = self._make_post(url, content)
        if 'code' in rep and rep['code'] == 0:
            if bot_type == 'gpt-embedding':
                return rep['code'], json.loads(rep['reply'])
            return rep['code'], rep['reply']
        elif 'code' in rep:
            return rep['code'], rep['msg']
        else:
            return -1, 'request failed'

    def similarity(self, embedding1: dict, embedding2: dict) -> float:
        a = embedding1
        b = embedding2
        dot_product = np.dot(a, b)
        a_norm = np.linalg.norm(a)
        b_norm = np.linalg.norm(b)
        cosine_sim = dot_product / (a_norm * b_norm)
        return cosine_sim

    def __str__(self):
        """
        Returns a string representation of the LLMClient.

        Args:
        - None.

        Returns:
        - (str): The string representation of the LLMClient.
        """
        s = ""
        s += f"| host     | {self.host}\n"
        s += f"| session  | {self.session_id}\n"
        s += f"| bot_type | {self.bot_type}\n"
        if self.apikey is not None:
            s += f"| apikey   | {self.apikey[0:3]+'*'*(len(self.apikey)-6)+self.apikey[-3:]}\n"
        else:
            s += f"| apikey   | None\n"
        return s
