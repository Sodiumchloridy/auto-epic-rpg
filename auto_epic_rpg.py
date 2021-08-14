import time
import discum
import os
from datetime import datetime
from threading import Thread

#Install Discum module using pip, other modules should come with python.

bot = discum.Client(token='YOUR_DISCORD_TOKEN', log={"console":True, "file":False})
target_channel = "YOUR_DISCORD_CHANNEL_ID" #Use a private server with Epic RPG bot just in case anything happens and you can monitor it.
work = "rpg chainsaw" #Your desired work command.
guild_id = "YOUR_DISCORD_SERVER_ID"

def autorpg():
    print("Starting bot")
    time.sleep(1)
    bot.sendMessage(target_channel, "rpg heal")
    time.sleep(1)
    while True:
        bot.sendMessage(target_channel, "rpg hunt")
        time.sleep(60)
        if x % 2 == 0:
            bot.sendMessage(target_channel, "rpg heal")
            time.sleep(1)
            continue
        if x % 5 == 0:
            bot.sendMessage(target_channel, work)
            time.sleep(1)
            continue
        if x % 10 == 0:
            bot.sendMessage(target_channel, "rpg farm")
            time.sleep(1)
            continue
        if x % 60 == 0:
            bot.sendMessage(target_channel, "rpg heal")
            time.sleep(1)
            bot.sendMessage(target_channel, "rpg adventure")
            time.sleep(1)
            bot.sendMessage(target_channel, "rpg heal")
            time.sleep(1)
            continue
        if x % 180 == 0:
            bot.sendMessage(target_channel, "rpg buy ed lb")
            x = 0
            continue
        x += 1

#This is to force quit the bot when you're in epic rpg jail so you can manually solve the captcha, if not you can get banned for 24 hrs.
@bot.gateway.command
def antiguard(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['guild_id'] == guild_id and m['channel_id'] == target_channel:
            if 'rpg jail' in m['content']:
                os._exit(0)

def antiguard():
    bot.gateway.run(auto_reconnect=True)

        
thread_rpg = Thread(target=autorpg)
thread_antiguard = Thread(target=antiguard)

if __name__ == '__main__':
    thread_rpg.start()
    time.sleep(1)
    thread_antiguard.start()
    time.sleep(1)
    thread_antiguard.join()