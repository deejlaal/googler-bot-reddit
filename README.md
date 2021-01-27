# googler-bot-reddit
A simple reddit bot that polls new comments posted to a subreddit, parses comment text looking for any words specified within a pair of curly brackets (e.g {gravity, mission to mars}) and posts an auto-reply to the comment by listing Google links for those words. 

Here is an example of the bot in action: https://www.reddit.com/r/bottesting/comments/kw68gb/test_post_for_googler_bot/?sort=new

## Pre-Requisites
The bot program is essentially a Python script that will need to be hosted on a local computer or a server where the program can continuously run uninterrupted. Also, the python program leverages a handful of "python packages" that will need to be installed prior to starting the bot. Here are the pre-requisites for the bot to be used successfully:-
1. A server where the bot program can be run
2. Python 3.x run-time. If you are not fully familiar with Python ecosystem, the simplest way would be to install the Anaconda distribution on your server. Instructions here: https://docs.anaconda.com/anaconda/install/
3. Python packages needed for the program to function. The ones needed are praw, re and configparser. 
