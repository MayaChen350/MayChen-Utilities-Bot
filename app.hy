(import discord)
(import discord.ext.commands [Bot MissingRequiredArgument])
;; (import hyrule [doto])
(require hyrule [doto as->])
(require macros.core [setup-bot])

(setv commands #())

(defn run []
  (setv bot (Bot :command_prefix "!"
                 :intents (do 
                            (setv intents (discord.Intents.all)) 
                            (setv intents.message_content True)
                             intents)))
  (setup-bot bot
    (do
      (await bot.wait_until_ready)
      (await bot.tree.sync))
    (ctx.send
      (if (isInstance error MissingRequiredArgument)
        "Parameters are missing"
        error)))
  
  (map bot.add_command commands)
  (bot.run settings.DISCORD_API_SECRET :root_logger True))

(when (= __name__ "__main__") (run))
