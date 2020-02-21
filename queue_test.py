import _thread as thread, queue, time

import tweepy
import time
import io
import os
from flask import Flask
import pytest
import subprocess

from google.cloud import vision
from google.cloud.vision import types

import io
import os
from google.cloud import vision
from google.cloud.vision import types
import urllib
import urllib.request

import tweepy
import datetime
import sys

numconsumers = 2
numproducers = 1
nummessages = 1

Consumer_key= 'oneBlZdM0AaWQzuutkVxQJZ3g'
Consumer_secret= 'vsTzdyO3jHgiCQglgX1nqo8VaylxFpn0u93XEseBbALRCR9g5F'
Access_key= '1222946005336936449-bS53klLdH43Bi71nSQyVWPhD6cdrSA'
Access_secret= 'Dybso4U2NA3ibzd6nZtcNrCarvpqsYCFgoGEAAh4lxeAS'

auth=tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

credential_path = r"twittervision-eb2dfdbe7250.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

FILE_NAME = 'last_seen_id.txt'
username = "Edwin86888730"
startDate = datetime.datetime(2020, 2, 20, 0, 0, 0)
endDate =   datetime.datetime(2021, 2, 21, 0, 0, 0)
 
# Create a lock so that only one thread writes to the console at a time
safeprint = thread.allocate_lock()
 
# Create a queue object
dataQueue = queue.Queue()
# Function called by the producer thread

count = 0


def call_back(string):
    print("Finished converting {}".format(string))
    return 1
    
def convert_str2slide(slidestring):
    global count
    count=count+1
    file_name="output{num}.mp4".format(num = count)
    print(file_name)
    os.system('ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \ "drawtext=fontfile=/path/to/font.ttf:fontsize=30: \ fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text={str1}" \{str2}'.format(str1 = slidestring, str2=file_name))
    
    file_obj = open("list.txt","a")
    file_obj.write('file ./'+file_name+'\n')
    file_obj.close()
    
    call_back(slidestring)

    if call_back:
        call_back(slidestring)
        
    return 1
    
def retrieve_one_tweet():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        str = mention.full_text
        return str
        
def retrieve_all_tweets():
    tweets = []
    tmpTweets = api.user_timeline(username, tweet_mode='extended')
    for tweet in tmpTweets:
        
        if tweet.created_at < endDate and tweet.created_at > startDate:
#            print(tweet.full_text)
            str=tweet.full_text
            print(tweet.full_text)
            tweets.append(str)
    return tweets
    
def wait_for_tweet():
    while(True):
        retrieve_one_tweet();
        time.sleep(5)
        
def producer(idnum):
#    tweet_str = retrieve_tweet()
    tweet_list = []
    tweet_list=retrieve_all_tweets()
#    print("hello")
    for tweet in tweet_list:
#        print("adding" + tweet)
        dataQueue.put(tweet)
# Produce 4 messages to place on the queue
#    for msgnum in range(nummessages):
#        # Simulate a delay
#        time.sleep(idnum)
#
#        # Put a String on the queue
#        dataQueue.put('[producer id={}, count={}]'.format(idnum, msgnum))
 
# Function called by the consumer threads
def consumer(idnum):
    # Create an infinite loop
    while True:
        # Simulate a delay
        time.sleep(0.1)
        try:
            # Attempt to get data from the queue. Note that
            # dataQueue.get() will block this thread's execution
            # until data is available
            data = dataQueue.get()
            convert_str2slide(data)
            
        except queue.Empty:
            pass
#        else:
#            # Acquire a lock on the console
#            with safeprint:
#                # Print the data created by the producer thread
#                print('consumer ', idnum, ' got => ', data)

def create_slideshow():
    os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy mergedfile.mp4')
    return 1
 
if __name__ == '__main__':
    # Create consumers
#    open('list.txt', 'w').close()
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
    # Create producers
    for i in range(numproducers):
#        print("hello")
        thread.start_new_thread(producer, (i,))
        
#    os.system('ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \ "drawtext=fontfile=/path/to/font.ttf:fontsize=30: \ fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text={str1}" \ {str2}'.format(str1 = "hello" , str2="output1.mp4"))
#    wait_for_tweet()
#    retrieve_all_tweets()
    # Simulate a delay
#    os.system("xargs rm < list.txt")

    time.sleep(((numproducers) * numconsumers) + 1)
    create_slideshow()
    # Exit the program
    print('Main thread exit')
#    os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy mergedfile.mp4')
    
#    create_slideshow()
    for i in range(1, count+1):
           print("removing")
           os.system("rm {str1}.mp4".format(str1="output"+str(i)))

    os.system("> list.txt")

    #import queue
    #
    ## From class queue, Queue is
    ## created as an object Now L
    ## is Queue of a maximum
    ## capacity of 20
    #L = queue.Queue(maxsize=20)
    #
    ## Data is inserted into Queue
    ## using put() Data is inserted
    ## at the end
    #L.put(5)
    #L.put(9)
    #L.put(1)
    #L.put(7)
    #
    ## get() takes data out from
    ## the Queue from the head
    ## of the Queue
    #print(L.get())
    #print(L.get())
    #print(L.get())
    #print(L.get())

    # Specify the number of consumer and producer threads
