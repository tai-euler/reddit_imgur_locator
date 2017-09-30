# reddit_word_locator_scripts
written in python 2.7 with praw(The Python Reddit API Wrapper)

praw latest documentation: ```praw.readthedocs.io/en/latest/```
1. reddit_imgur_locator.py - locate imgur LINKS (in the comments!)
2. reddit_airdrop_locator.py - locate posts where the word "airdrop" is used(cryptocurrency) (in the post titles!)

<img src="https://steemitimages.com/0x0/https://s26.postimg.org/kt2mmrnkp/21434163_493613564331005_3460030575690121216_n.jpg" alt="wolfiecindysmile" style="width:304px;height:228px;">

## how to run: 
1. ```git clone https://github.com/tai-euler/reddit_word_locator.git```
2. ```cd reddit_word_locator/```

3. example script to run : ```python reddit_imgur_locator.py```

## Note: 
1. add your own  ```client_id='your_id'```,```client_secret="your_secret"```, ```password='your_pass'``` and  ```username='your_username' ```
in the python file.

You will find that in your reddit.com account when you create a script https://ssl.reddit.com/prefs/apps

2. add your own subreddit for example I add "naturepics": 
```subreddit = reddit.subreddit(“naturepics”)```

3. you can change the category and limit, how many topics should the script scrape by changing this line in the code:  ```hot_category = subreddit.hot(limit=120)```
you can change to: 
 ```new_category = subreddit.new(limit=30)```


### troubleshooting: 
1. ```pip3 install praw```
