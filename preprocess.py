import json
import re
import os

# Load Reddit posts from the JSON file
def load_reddit_posts(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Clean each post's text
def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)               # Replace multiple spaces/newlines with single space
    text = re.sub(r'http\S+', '', text)            # Remove URLs
    text = re.sub(r'[^\x00-\x7F]+', '', text)      # Remove emojis and non-ASCII chars
    return text.strip()

# Break post into 400-word chunks
def chunk_post(post, max_words=600):
    full_text = f"{post['title']}. {post['selftext']}"
    cleaned = clean_text(full_text)
    words = cleaned.split()
    chunks = [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
    return chunks

# Loop through all posts and chunk them
def preprocess_and_chunk(posts):
    all_chunks = []
    for post in posts:
        chunks = chunk_post(post)
        for chunk in chunks:
            all_chunks.append({
                'post_id': post['id'],
                'subreddit': post['subreddit'],
                'text': chunk
            })
    return all_chunks

# Main script
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    posts = load_reddit_posts("data/reddit_posts.json")
    chunks = preprocess_and_chunk(posts)

    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"✅ Preprocessing complete! Total chunks: {len(chunks)}")
