import twint
import json
import os
import requests

c = twint.Config()
c.Username = "" # how to get user input to this script?

tweets = []

c.Limit = 20
c.Images = True
c.Store_object = True
c.Store_object_tweets_list = tweets


