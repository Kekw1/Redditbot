import praw


subreddit = reddit.subreddit("meme")

top = subreddit.top(limit = 1)

for submission in top:
    print(submission.title)