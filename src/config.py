from envparse import env

env.read_envfile(".env")

BOT_TOKEN = env.str("BOT_TOKEN")
USER_ID = env.int("USER_ID")
