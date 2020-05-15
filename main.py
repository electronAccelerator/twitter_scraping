import twint
import json
import os
import requests

usernames = ['littleulvar']

for name in usernames:

    tweets = []

    c = twint.Config()
    c.Username=name
    c.Store_object=True
    c.Store_object_tweets_list=tweets
    c.Images=True
    c.Limit=10

    twint.run.Search(c)

    if (len(tweets)):

        os.makedirs(os.path.dirname(f'/images/{name}/'), exist_ok=True)
        i = 0

        for tweet in tweets:

            for pic in tweet.photos:

                img = requests.get(pic).content
                filename = f'{i}.{pic[-3:]}'

                print(f'Outputting: images/{name}/{filename}')

                with open(f'/images/{name}/{filename}', 'wb+') as file:
                    file.write(img)

                i += 1

print('All Done')