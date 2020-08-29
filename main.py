from os import environ
from pyrogram import Client

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

with Client(":memory:", api_id, api_hash, bot_token=bot_token) as app:
    info = "Greetings from **Heroku**!"
    user_id = int(environ.get("USER_ID"))
    if user_id:
        app.send_message(user_id, info)
    else:
        print(info)
