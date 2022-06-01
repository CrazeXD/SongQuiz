import random
import json
import os
from pytube import Youtube

class ChooseSong:
    def __init__(self):
        self.song_list = []
        self.song_list_path = "song_list.json"
        self.song_list_json = self.load_json()
        

