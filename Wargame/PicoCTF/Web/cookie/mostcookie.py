# cookie 후보들 중 하나 걸리길 바라야지..
# 일단 get 으로 받아와서 data 중 아무거나 걸리길..!

from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
import requests

s = requests.Session()
s.get("http://mercury.picoctf.net:44693/search")

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

cookie = s.cookies["session"] #session 이름에 cookie 들이...
s_value = s.get("very_auth")

