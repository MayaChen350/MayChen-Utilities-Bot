(defmacro setup-bot [bot ready command_error]
      `(do 
         (defn :async [bot.event] on_ready []
            ~ready 
            None)
         (defn :async [bot.event] on_command_error [ctx error]
            ~command_error
            None)))

(defn smth []
  (print "hi")
  (setup-bot {"event" 3}
             (do (print "heyo") (print ":3"))
             (print "oh no there was an error D:"))
  None)
