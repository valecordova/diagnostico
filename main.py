from days import highest_days
from hashtags import highest_hastags
from retweeted import highest_retweeted
from users import highest_users
import pandas as pd

if __name__ == "__main__":
    tweets_df = pd.read_json(
        'farmers-protest-tweets-2021-03-5.json', lines=True)
    highest_days(tweets_df)
    highest_hastags(tweets_df)
    highest_retweeted(tweets_df)
    highest_users(tweets_df)
