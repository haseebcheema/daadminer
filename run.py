from daadbot.daad import Daad
import time

with Daad() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_language()
    bot.go_to_international_programs()
    bot.choose_programme('Computer Science')
    bot.apply_filters()
    bot.filter_amount_on_page()
    bot.go_to_next_page()
    time.sleep(30)
