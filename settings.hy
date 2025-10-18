(import os)
(import dotenv [load_dotenv])

(load_dotenv)
(setv DISCORD_API_SECRET (os.getenv "DISCORD_API_TOKEN"))
