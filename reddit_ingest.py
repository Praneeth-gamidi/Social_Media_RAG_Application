import praw
import json

# Initialize Reddit API with credentials (use a Reddit dev app)
reddit = praw.Reddit(
    client_id='95m7TR5lWieiBTk2JQZ5eg',
    client_secret='fGFAwL2tOo12Y2Y8Ar34spzZuDRhiQ',
    user_agent='social-media-rag'
)

def fetch_posts(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        if not post.stickied:
            posts.append({
                'id': post.id,
                'title': post.title,
                'selftext': post.selftext,
                'created_utc': post.created_utc,
                'subreddit': subreddit_name,
                'url': post.url
            })
    return posts

# Save to JSON
if __name__ == "__main__":
    subreddits = ['news', 'technology', 'memes']
    all_posts = []
    for sub in subreddits:
        posts = fetch_posts(sub, limit=50)
        all_posts.extend(posts)

    with open("data/reddit_posts.json", "w", encoding='utf-8') as f:
        json.dump(all_posts, f, indent=2)
