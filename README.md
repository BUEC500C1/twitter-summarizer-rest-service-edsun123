# video-edsun123
video-edsun123 created by GitHub Classroom

The goal of the this lab is to determine the number of processes working within your own comptuer and develop a queue system for tweet to video conversion.


This API receives the user name for a twitter page and returns a video summarizing the last 24 hours of tweets from that user's timeline.

Each tweet is converted to text on a frame, and any media is added to the frame as well. Each frame is shown for 3 seconds. The resulting video is returned to the requesting process.

If the specified user either does not exist or does not have any tweets on their timeline, the resulting video will be a single frame that has the text "This user has no tweets".

For each call, each tweet from the timeline is saved as a separate image in the directory. In order to keep the directory generally clean, the clean_old() function will scan all of the calls in the processes list, and will clear all .png files associated with calls that have already been completed. The clean_old() function is called every time the API receives a new incoming call.
