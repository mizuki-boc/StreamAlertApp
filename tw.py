from twitchio.ext import commands
import twitchio


if __name__ == "__main__":
    user_id = "kato_junichi0817"

    print(twitchio.webhook.StreamChanged(user_id).as_uri())