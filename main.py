from os import environ
from pyrogram import Client

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ.get("BOT_TOKEN")
session_string = environ.get("SESSION_STRING")
info = "Greetings from **Heroku**!"

if bot_token:
    app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
elif session_string:
    app = Client(session_string, api_id, api_hash)

print(info)

@app.on_message()
async def work(client, message):
    await app.send_message(message.chat.id, info)

app.run()
