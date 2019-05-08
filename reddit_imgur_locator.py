# python3
# locate all imgur links in the comments


import os
import argparse
import requests
import praw
import re
from random import randint
from time import sleep


reddit = praw.Reddit(client_id='your_id',
                     client_secret="your_secret", password='your_pass',
                     user_agent='Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                     username='your_username')


subredditList = ['dogs', 'dogpictures' ]


# the requests, loops and iterations
# iterate through every subreddit from 'subredditList'
# and find imgur URLs in the comments

# arrays for all the imgur links
body_urls = []


for actualSubreddit in subredditList:

                        # make a subreddit praw class instance by handing the actualSubreddit over to the reddit object
                        subreddit = reddit.subreddit(actualSubreddit)
                        print(40*'-')
                        print('Processing subreddit: ' + actualSubreddit)
                        print(40*'-')
                        
                        type(subreddit)
                        # <class 'praw.models.reddit.subreddit.Subreddit'>
                        
                        # example for 'display_name'
                        subreddit.display_name
                        
                        
                        # limit how deep you want to scrape the HOT category of submissions
                        hot_category = subreddit.hot(limit=15)
                        type(hot_category)
                        # <class 'praw.models.listing.generator.ListingGenerator'>
                        
                        # to avoid a ban, sleep randomly between 1 and 7 seconds in every loop
                        sleep(randint(1,7))
                        
                        for submission in hot_category:
                          
                              # we skip the stickied posts on the beginning of the page
                            if not submission.stickied:
                                    body_urls.append(submission.url)
                                
                                    for comment in subreddit.comments(limit=125):
                                    # find just the comments that contains an imgur link
                                    
                                        try:
                                            if 'imgur' in comment.body:

                                                # skip bot content
                                                if 'I am a bot' in comment.body:
                                                    continue
                                                    
                                                # encode bytes as UTF-8
                                                string_comment = comment.body.encode('utf-8')
                                                # make comment a string
                                                string_comment2 = str(comment.body)
                                               # string_comment2 = str(string_comment)
                                                # remove white space and save in a list
                                               
                                                string_comment3 = string_comment2.split(" ")
                                                
                                                chars_to_remove = ["\\n","\\r","<",">","#","%","^","*","=",")","(",",","?","-","_","&","[","]","{","}","'"]
                                                
                                                # iterate through elements in list
                                                for element in string_comment3:
    
                                                    if 'imgur' in element:
            
                                                        # iterate through elmement string to remove chars
                                                        for char in chars_to_remove:
                                                            # remove some unnecessary chars from the string 
                                                            element = element.replace(char,"")
                                                        
                                                        # still messy links, so find imgur links in element
                                                        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', element)
                                                        # urls is a list, so iterate through and save urls
                                                        for x in urls:
                                                            body_urls.append(x)
                                   
                                        except Exception as msg:
                                                    print (msg)

# removing duplicates by converting a list to set()                                              
body_urls3 = set(body_urls) # remove duplicates

# generate html file to display images in iframes
f= open("new_file.html","w+") 
f.write("<!DOCTYPE html><html>")

for element in body_urls3:
    f.write('<div <a href="{}" target="_blank">{}</a></div> <div style="position:relative;padding-top:56.25%;" id="{}"><iframe width="1100em" height="1100em" name="{}" src="{}" frameborder="0" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe></div>'.format(element,element,element,element,element))

f.write("<html>")
f.close()

print("** Done! **")

