# googler-bot-reddit
A simple reddit bot that polls new comments posted to a subreddit, parses comment text looking for any words specified within a pair of curly brackets (e.g {gravity, mission to mars}) and posts an auto-reply to the comment by listing Google links for those words. 

Here is an example of the bot in action: https://www.reddit.com/r/bottesting/comments/kw68gb/test_post_for_googler_bot/?sort=new

## Pre-Requisites
The bot program is essentially a Python script that will need to be hosted on a local computer or a server where the program can continuously run uninterrupted. Also, the python program leverages a handful of "python packages" that will need to be installed prior to starting the bot. Here are the pre-requisites for the bot to be used successfully:-
1. A server where the bot program can be run
2. Python 3.x run-time. If you are not fully familiar with Python ecosystem, the simplest way would be to install the Anaconda distribution on your server. Instructions here: https://docs.anaconda.com/anaconda/install/
3. Python packages needed for the program to function. The ones needed are praw, re and configparser. 


### Note: If you have installed Anaconda, you'll only need to install "praw" package manually since rest of the required packages are available in Anaconda by default.


## Configuring the bot
Open "praw.ini" file in any text editor and specify the necessary values as decribed in the file itself. There are additional comments in the file that provide additional details. Please read through them and configure accordingly.

## Running the bot
Once the praw.ini configuration has been completed, simply launch command prompt (Windows) or Terminal/Shell (Mac/Unix) and execute the following command:

python path/to/bot/code/googleR_bot_reddit.py

### Note: DONOT close the command window after executing the above command. In order for the bot to run continuously, the window needs to remain open. If you don't like to see a window being open all the time, use this help guide to run the python script in background: https://www.geeksforgeeks.org/running-python-program-in-the-background/
