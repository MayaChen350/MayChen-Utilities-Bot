(import discord)
(import discord.ext.commands [Bot, MissingRequiredArgument])
(import hyrule [

(defn run []
  (setv intents 
        (setv (. (discord.Intents.all) message_content) True)
  (setv bot (Bot (:command_prefix "!")))

  (defn :async [bot.event] on_ready []
    (doto bot
      (.wait_until_ready)
      (.sync (. tree)))

  
  (defn :async [bot.event] on_command_error [ctx error]
    (ctx.send
      (if (isInstance error MissingRequiredArgument)
        "Parameters are missing"
        error)))


