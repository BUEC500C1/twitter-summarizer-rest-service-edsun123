# Edwin Sun's Twitter-Video Converter
video-edsun123 created by GitHub Classroom

Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day
1) Convert text into an image in a frame
2) Do a sequence of all texts and images in chronological order.
3) Display each video frame for 3 seconds

# Overview

This API retrieves tweets from the last 24 hours of tweets from that user's timeline then returns a video of all tweets in that timeline.

Each text from the tweet is converted to text on a frame which is shown for 3 seconds. Then each is saved as a 3 second video in the current directory and a text_file keeps track of those video filenames. Note: before each call, the program will clean out the current directory and the text file to prepare for writing more mp4 files in the next call.
