import praw
reddit = praw.Reddit(client_id='your_id',
                     client_secret="your_secret", password='your_pass',
                     user_agent='Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                     username='your_username')


redditSubreddits = ['dogs', 'dogpictures' ]


# iterate through every subreddit from the array
# and find imgur URLs in the comments
for oneSubreddit in redditSubreddits:

                        subreddit = reddit.subreddit(oneSubreddit)
                        print('subreddit: ' + oneSubreddit)

                        hot_category = subreddit.hot(limit=50)
                        # we can print out he options to this object
                        # ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
                        # print(dir(hot_category))

                        for submission in hot_category:
                            # we can print out he options to this object
                            # [ 'created_utc', 'likes', 'delete', 'edit', ...
                            # print(dir(submission))


                            # we skip the stickied posts on the beginning of the page
                            if not submission.stickied:
                                #print(submission.title)
                                # this gives us the comments and subcomments from the posts
                               # print (dir(submission))
                                comments = submission.comments.list()
                                for comment in comments:
                                    # find just the comments that contains an imgur link
                                    try:
                                        if 'imgur' in comment.body:
                                            # give us title and url from post with imgur.com link from the comments
                                            print (submission.title + ' : ')
                                            print (submission.url)
                                            print (submission.shortlink)
                                            print(comment.body)
                                            print(20*'-')
                                    except Exception as msg:
                                        print msg
