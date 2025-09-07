(defmacro setup-bot [ready command_error]
      `(do 
         (defn :async [] on_ready []
            ~ready 
            None)
         (defn :async [] on_command_error [ctx error]
            ~command_error
            None)))

(defn smth []
  (print "hi")
  (setup-bot (do (print "heyo") (print ":3"))
             (print "oh no there was an error D:"))
  None)
