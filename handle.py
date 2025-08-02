# handle.py
import snscrape.modules.twitter as sntwitter

def get_last_tweet(handle):
    scraper = sntwitter.TwitterUserScraper(handle)
    for tweet in scraper.get_items():
        print(f"[{handle}] → {tweet.content}")
        break  # Only the latest tweet

if __name__ == "__main__":
    twitter_handle = input("Enter Twitter handle (without @): ")
    try:
        get_last_tweet(twitter_handle)
    except Exception as e:
        print("❌ Failed to fetch tweets:", str(e))
