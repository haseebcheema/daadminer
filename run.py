from daadbot.daad import Daad
import time

with Daad() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_language()
    time.sleep(10)
