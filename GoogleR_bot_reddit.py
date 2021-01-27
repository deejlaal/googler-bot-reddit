from typing import List
import praw
import re
from configparser import ConfigParser

google_url_template = "https://www.google.com/search?q={0}"

reddit_configs_parser = ConfigParser()
reddit_configs_parser.read("praw.ini")

subreddit_name = reddit_configs_parser["reddit_configs"].get("subreddit_name")
bot_user_name = reddit_configs_parser["reddit_configs"].get("username")
bot_autoreply_header = ""
bot_autoreply_footer = "*GoogleR bot by u/dj_laaal. [Contact my Creator.](https://www.reddit.com/user/dj_laaal)*"
clickable_reddit_item_template = "**[{0}]({1})**"

def poll_comments_and_autoreply():
    print("Bot started...Looking for comments to respond to...")
    sub_reddit_instance = praw.Reddit("reddit_configs").subreddit(subreddit_name)
    for comment in sub_reddit_instance.stream.comments(skip_existing=True):
        print("-" * 60)
        # Prevent the bot from replying to itself and causing an endless loop
        if str.lower(comment.author.name) not in str.lower(bot_user_name):
            print("Comment by an actual user....Bot will auto-reply shortly....")
            print("Submission Title", comment.submission.title, sep = ":::")
            print("Subreddit", comment.subreddit.display_name, sep = ":::")
            if comment.author:
                print("Comment Author", comment.author.name, sep= ":::")  
            print("Comment Text", comment.body, sep= ":::")
            print("*" * 30)

            items_list = parse_and_itemize_search_terms(comment.body)
            if len(items_list) >0:
                auto_response_text = generate_autoreply_text(items_list)
                comment.reply(auto_response_text)
                print("Bot::Curly brackets found in the comment. Auto responded to the above comment.")
            else:
                print("Bot::No curly brackets found in the comment. Bot will not respond.")
    return
        
def parse_and_itemize_search_terms(comment_text: str):
    search_terms_list_itemized = list()
    regex_matches_iter = re.finditer('\{([^}]+)\}', comment_text)
    search_terms_list = [m.group().replace("{", "").replace("}", "") for m in regex_matches_iter]
    if len(search_terms_list) > 0:
        search_terms_list_itemized = [i for term in search_terms_list for i in term.split(",")]
    
    return search_terms_list_itemized

def generate_autoreply_text(terms_list: List = None):
    #l = ["Lorem space", "Ipsum", "Dolor"]
    formatted_reddit_comment  = bot_autoreply_header + "\n"
    for term in terms_list:
        strip_term = str.strip(term)
        google_url = google_url_template.format(strip_term)
        clickable_item = clickable_reddit_item_template.format(strip_term, google_url)
        formatted_reddit_comment += "- " + clickable_item + "\n\n"
    formatted_reddit_comment += "\n \n" + bot_autoreply_footer
    return formatted_reddit_comment

def main():
    pass


if __name__ == "__main__":
    poll_comments_and_autoreply()