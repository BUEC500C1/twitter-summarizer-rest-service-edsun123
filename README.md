# Edwin Sun's Twitter-Video Converter
video-edsun123 created by GitHub Classroom

Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day
1) Convert text into an image in a frame
2) Do a sequence of all texts and images in chronological order.
3) Display each video frame for 3 seconds

# Overview

This API retrieves tweets from the last 24 hours of tweets from that user's timeline then returns a video of all tweets in that timeline.

Each text from the tweet is converted to text on a frame which is shown for 3 seconds. Then each is saved as a 3 second video in the current directory and a text_file keeps track of those video filenames. The text file is necessary to concatenate all the files into a mega video called mergedfile.mp4. Note: before each call, the program will clean out the current directory and the text file to prepare for writing more mp4 files in the next call.

For the queueing system, I have 1 consumer process that retrieves the tweets and 2 producer processes that convert those tweets to videos. Using the module queue helps lock the processes so that current tasks are finished and also facilitates adding and removing tasks from the queue task system.

# Files
1) Main program is run in queue_test.py
To run...
```
python3 queue_test.py
```
2) Video file names are stored in list.txt
3) Keys for authentication is stored in separate keys file called keys.py
```
TWITTER_API_KEY = XXXXXXXXX
TWITTER_API_SECRET_KEY = XXXXXXXXXXXXXXXXXX
TWITTER_ACCESS_TOKEN = XXXXXXXXX
TWITTER_ACCESS_TOKEN_SECRET = XXXXXXXXXXXXXXXXXXXXXXXXXXX

```
# Threads
Normally you would expect on thread is assigned to each core. Given a mac computer with 4 cores, it should handle 4 threads of tweet-video conversion. However, I've found that the performance jumps around 30-40% in cpu usage instead of 25%. Then it is found that by default, each thread for frame conversion is ~1.5 threads per core. So for performance reasons, I've had at most 2 producers or 2 threads to do the video-thread conversion
