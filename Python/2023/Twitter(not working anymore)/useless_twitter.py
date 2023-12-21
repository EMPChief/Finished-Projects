import tweepy
from tweepy import User, Tweet
import twitter_config
import pyjokes


joke = pyjokes.get_joke()


def about_me(client: tweepy.Client) -> None:
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


def get_my_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    emp = client.get_user(username="ItsMeArtur")
    response = client.get_user_tweets(id=emp.id)
    return response.data


if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=twitter_config.BEARER_TOKEN,
        consumer_key=twitter_config.API_KEY,
        consumer_secret=twitter_config.API_SECRET,
        access_token=twitter_config.ACCESS_TOKEN,
        access_token_secret=twitter_config.ACCESS_SECRET,
    )

    print("=== About Me ===")
    about_me(client)
    print()
    print("=== EMP Tweets ===")
    print(joke)
    for tweet in get_my_tweets(client):
        print(tweet, end="\n\n")
