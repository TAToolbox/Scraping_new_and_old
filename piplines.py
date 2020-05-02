# import os
# import csv
from pymongo import MongoClient

client = MongoClient()
db = 'whatever'
collection = 'other_whatever'

def do_stuff():
    #do stuff
    # return dict(something)
    pass

collection.replace_one(do_stuff(), do_stuff(), upsert=True)

# with open('./csv.csv', mode='rw+') as f:
#     reader = csv.DictReader(f)

#     # do stuff to reader

#     writer = csv.DictWriter(f)
