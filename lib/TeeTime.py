from bs4 import BeautifulSoup 
import requests
import ipdb
import Course
import json


class TeeTime:
    
    all = []

    def __init__(self, date_time, avail_slots, holes):
        self.date_time = date_time
        self.avail_slots = avail_slots
        self.holes = holes

    def __str__(self):
        output = ''
        output += f'Date: {self.date_time}\nTime: {self.date_time}\nAvailable spots: {self.avail_slots}\nHoles: {self.holes}\n'
        output += '------------------'
        return output


    def get_page():
        # more code coming soon!
        doc =  BeautifulSoup(requests.get("https://app.membersports.com/tee-times/3660/4711/0/1/false").text, 'html.parser')
        return doc

TeeTime.get_page()