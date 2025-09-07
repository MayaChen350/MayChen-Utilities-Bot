(import discord)
(import discord.ext.commands [Bot MissingRequiredArgument])
;; (import hyrule [doto])
(require hyrule [doto as->])
(require macros.core [setup-bot])

(defn run []
  (setv bot (Bot :command_prefix "!"
                  :intents (do 
                             (setv intents (discord.Intents.all)) 
                             (setv intents.message_content True)
                             intents)))

  (setup-bot bot
    (doto bot
      .wait_until_ready
      .tree.sync)
    (ctx.send
      (if (isInstance error MissingRequiredArgument)
        "Parameters are missing"
        error))))

