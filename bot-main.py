import sys
import time
import telepot
import random

stef_responses = ["I'm not wifed", "Jason is a simp", "God Olga is so brass", ""]

def handle(msg):
    print "CONSUMING!"
    content_type, chat_type, chat_id = telepot.glance(msg)
    print "Message from " + str(chat_id)
    command = msg['text']
    if command is not None and command.startswith("/simulate"):
        bot.sendMessage(chat_id, stef_responses[random.randint(0, len(stef_responses)-1)])

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)