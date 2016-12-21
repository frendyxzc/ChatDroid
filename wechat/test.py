#!/usr/bin/env python
# coding: utf-8
import requests

info = {'input': '鲜闻'}
r = requests.post("http://127.0.0.1:5000/chat", data=info)

print r.text