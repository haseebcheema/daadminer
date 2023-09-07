from daadbot.daad import Daad
import time

with Daad() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    time.sleep(10)
