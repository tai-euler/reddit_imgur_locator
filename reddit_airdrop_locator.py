# locate all the posts in cryptocurrency subreddits, where in the title the word "airdrop" is used


import praw
reddit = praw.Reddit(client_id='your_id',
                     client_secret="your_secret", password='your_pass',
                     user_agent='Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                     username='your_username')
                     
                     
cryptoSubreddits = ['icocrypto', 'CryptoCurrency', 'CryptoMarkets' ]

print('try to visit ' + 'https://airdropalert.com/')

# iterate through the subreddits in the array
for oneSubreddit in cryptoSubreddits:

                    print(' Subreddit: ' + oneSubreddit)
                    subreddit = reddit.subreddit(oneSubreddit)
                        # we can un/subscribe to the subreddit with
                        # subreddit.subscribe() or subreddit.unsubscribe()

                        # or upvote, downvote, reply etc.
                        # subreddit.upvote(),
                        # subreddit.downvote(),
                        # subreddit.reply()
                    hot_category = subreddit.hot(limit=350)
                    # we can print out he options to this object
                    # ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
                    # print(dir(hot_category))

                    for submission in hot_category:
                        # we can print out he options to this object
                        # [ 'created_utc', 'likes', 'delete', 'edit', ...
                        #print(dir(submission))
                        #break
                        # we skip the stickied posts on the beginning of the page
                        if not submission.stickied:

                                try:
                                        if 'Airdrop' in submission.title or 'airdrop' in submission.title or 'AirDrop' in submission.title or 'airdropped' in submission.title:
                                        # give us title and url from post with imgur.com link from the comments
                                            print (submission.title + ' : ')
                                            print (submission.url)
                                            time = submission.created
                                            timeConverted = datetime.fromtimestamp(time)
                                            timeConvertedStr = str(timeConverted)

                                           # if '2017-09' in timeConvertedStr:
                                           #     print 'true'

                                            print (timeConverted)
                                            print (submission.title)
                                            print (submission.shortlink)
                                            print(20*'-')
                                except Exception as msg:
                                        print msg
