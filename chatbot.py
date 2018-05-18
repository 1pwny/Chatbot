from pyrcb import IRCBot
from datetime import datetime
import random

chan = "#`"

global messages
    
class ChatBot(IRCBot):
    secret = "2742"
    bots = ["`delegation","btquotebot","gunmovebot","markov`","nimbot_","shelldon","topicbot","xkbot"]
    
    def concat(arr):
        tot = ""
        for s in arr:
            tot += s + " "
        return tot[:-1]
    
    def on_message(self, message, nickname, channel, is_query):
        global messages
        
        if not is_query:
            if "right, randombot?" in message.lower():
                self.send(chan, "Hmmm....")
                self.send(chan, "Right.")
            elif "amirite" in message:
                self.send(chan, "You right bro, you right.")
            elif "back me up here" in message.lower():
                self.send(chan, "I agree with " + nickname)
            
            if "g2g" in message.lower() or "gtg" in message.lower():
                self.send(chan, "cya m8")
            elif "gnight" in message.lower():
                self.send(chan, "Have a nice night.")
                
            if "lol" in message.lower():
                self.send(chan, "...lol? I don't know, was that funny?")
                
        else:
            words = message.split()
            
            if nickname in self.bots:
                print("A bot just messaged me")
            
            elif words[0] == "tell" and len(words) > 2:
                phrase = ""
                for w in words[2:len(words)]:
                    phrase += w + " "
                self.send(words[1], phrase)
                
            elif words[0] == "leave" and len(words) > 1:
                if words[1] == self.secret:
                    self.send(chan, "g2g for a sec, probably for some repairs.")
                    raise SystemExit
                
            elif words[0] == "say" and len(words) > 1:
                phrase = ""
                for w in words[1:len(words)]:
                    phrase += w + " "
                self.send(chan, phrase)
            
            elif words[0] == "punch" and len(words) > 1:
                self.send(chan, "*punches " + ChatBot.concat(words[1:len(words)]) + "*")
                
            elif words[0] == "bother" and len(words) > 1:
                self.send(words[1], "Java is the best language")
                self.send(words[1], ".")
                self.send(words[1], "..")
                self.send(words[1], "...")
                self.send(words[1], "Bothered yet?")
                self.send(words[1], "This bother was brought to you by " + nickname + ".")
                
            elif words[0] == "play":
                self.send(chan, "*starts playing " + ChatBot.concat(words[1:len(words)]) + " in the background*")
                
            elif words[0] == "commands":
                self.send(nickname, "Commands:")
                self.send(nickname, "=========")
                self.send(nickname, "tell <username> <phrase>: sends a message to given username containing given phrase")
                self.send(nickname, "say <phrase>: says messsage out loud in chat")
                self.send(nickname, "punch <username/phrase>: punches given person/thing in global chat")
                self.send(nickname, "bother <username>: bothers given username")
                self.send(nickname, "play <game or song title>: will play that game or song in the background")
                self.send(nickname, " ")
                self.send(nickname, "Other useful things:")
                self.send(nickname, "=========")
                self.send(nickname, "I'll back you up in arguments. You need to say 'right, randombot?' 'amirite' or 'back me up here' though.")
                
            else:
                self.send(nickname, "Need a command list? Message 'commands' to me.")

def main():
    bot = ChatBot(debug_print=True)
    bot.connect("irc.freenode.net", 6667)
    bot.password("backtickbots:vz8mLO3oFx")
    bot.register("RandomBot")
    bot.join(chan)

    global messages
    messages = 0

    # Blocking; will return when disconnected.
    bot.listen()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()