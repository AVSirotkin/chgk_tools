# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:16:10 2019

@author: avsirotkin
"""
import requests
import re
import datetime
import dateparser



def get_announcement(strings_to_remove = 0, extra_message = "", ljurl = "https://chgk-spb.livejournal.com/2046721.html"):
    resp = requests.get(ljurl)
    announce = "Sorry"
    if resp.ok:
        announce = resp.text
        announce = re.findall("<article.*?</article.*?>", announce)[0]
        announce = re.sub("<article.*?>", "", announce)
        announce = re.sub("</article.*?>", "", announce)
        announce = re.sub("<div.*", "", announce)
        announce = re.sub("<p>", "", announce)
        announce = re.sub("</p>", "\n\n", announce)
        announce = re.sub("<br.*?>", "\n", announce)   


        announce_strings = announce.split("\n")
        if len(announce_strings) > strings_to_remove:
            announce_strings = announce_strings[strings_to_remove:]

        #clear old infos 
        announce_strings_cleared = []
        too_old = False
        for s in announce_strings:
            
            if len(s) > 7:
                date_string = dateparser.parse(s[3:-4], languages = ["ru"])
            else:
                date_string = None
            if date_string:
                if date_string.date() < datetime.date.today():
                    too_old = True
                else:
                    too_old = False
            if not too_old:
                announce_strings_cleared.append(s)        
        
        announce =  "\n".join(announce_strings_cleared)               
        
        if extra_message != "":
            extra_message = extra_message + "\n"

        announce = "Продолжаем вести список синхронов в Санкт-Петербурге. Пост обновлён "+datetime.date.today().strftime("%d.%m.%Y")+".\n\n" + extra_message + announce   

    return(announce)
    
    
#my_test_post_orig = '''<article class="b-singlepost-body entry-content e-content   ng-scope" lj-sale-entry="" lj-discovery-tags="" lj-embed-resizer=""> <p>Продолжаем вести список синхронов в Санкт-Петербурге. Информация дублируется в <a href="https://t.me/WeekChgkSPB" rel="nofollow" target="_self">телеграм-канал</a>.</p><b>11 февраля (пн)</b><br><a href="https://chgk-spb.livejournal.com/2064993.html" rel="nofollow" target="_self">Кубок Сигулды - AnyDay (19:30)</a><br><br><b>12 февраля (вт)</b><br><a href="https://chgk-spb.livejournal.com/2059936.html" rel="nofollow" target="_self">Синхрон-lite - Форпост (19:15)</a><br><a href="https://chgk-spb.livejournal.com/2058288.html" rel="nofollow" target="_self">Синхрон-lite - Xren (19:30)</a><br><br><b>15 февраля (пт)</b><br><a href="https://chgk-spb.livejournal.com/2067370.html" rel="nofollow" target="_self">Открытый Синхронный кубок Беларуси - Any day (19:30)</a><br><a href="https://chgk-spb.livejournal.com/2069030.html" rel="nofollow" target="_self">Открытый Синхронный кубок Беларуси - Xren (19:30)</a><br><br><b>17 февраля (вс)</b><br><a href="https://chgk-spb.livejournal.com/2066034.html" rel="nofollow" target="_self">ОВСЧ-6 - Форпост (12:00)</a><br><a href="https://chgk-spb.livejournal.com/2070368.html" rel="nofollow" target="_self">Славянка без раздаток-2 - Чайковский (13:00)</a><br><a href="https://chgk-spb.livejournal.com/2069295.html" rel="nofollow" target="_self">Славянка без раздаток-2 - Xren (13:00)</a><br><a href="https://chgk-spb.livejournal.com/2070736.html" rel="nofollow" target="_self">ОВСЧ-6 - Чайковский (15:45)</a><br><a href="https://chgk-spb.livejournal.com/2069688.html" rel="nofollow" target="_self">Честный Эйб - Xren (16:00)</a><br><br><b>18 февраля (пн)</b><br><a href="https://chgk-spb.livejournal.com/2070916.html" rel="nofollow" target="_self">Честный Эйб - Чайковский (19:25)</a><br><a href="https://chgk-spb.livejournal.com/2067048.html" rel="nofollow" target="_self">Зимний Варан - Any day (19:30)</a><br><br><b>19 февраля (вт)</b><br><a href="https://chgk-spb.livejournal.com/2066288.html" rel="nofollow" target="_self">Парное ЧГК "Chgk is..." - Форпост (19:19)</a><br><a href="https://chgk-spb.livejournal.com/2071251.html" rel="nofollow" target="_self">Эврика-11 - Чайковский (19:25)</a><br><a href="https://chgk-spb.livejournal.com/2069787.html" rel="nofollow" target="_self">ОВСЧ-6 - Xren (19:30)</a>  <div class="mqe67p"></div></article>'''
#
#
#
##my_test_post = '''Продолжаем вести список синхронов в Санкт-Петербурге. Информация дублируется в <a href="https://t.me/WeekChgkSPB" rel="nofollow" target="_self">телеграм-канал</a>.<b>11 февраля (пн)</b><br><a href="https://chgk-spb.livejournal.com/2064993.html" rel="nofollow" target="_self">Кубок Сигулды - AnyDay (19:30)</a><br><br><b>12 февраля (вт)</b><br><a href="https://chgk-spb.livejournal.com/2059936.html" rel="nofollow" target="_self">Синхрон-lite - Форпост (19:15)</a><br><a href="https://chgk-spb.livejournal.com/2058288.html" rel="nofollow" target="_self">Синхрон-lite - Xren (19:30)</a><br><br><b>15 февраля (пт)</b><br><a href="https://chgk-spb.livejournal.com/2067370.html" rel="nofollow" target="_self">Открытый Синхронный кубок Беларуси - Any day (19:30)</a><br><a href="https://chgk-spb.livejournal.com/2069030.html" rel="nofollow" target="_self">Открытый Синхронный кубок Беларуси - Xren (19:30)</a><br><br><b>17 февраля (вс)</b><br><a href="https://chgk-spb.livejournal.com/2066034.html" rel="nofollow" target="_self">ОВСЧ-6 - Форпост (12:00)</a><br><a href="https://chgk-spb.livejournal.com/2070368.html" rel="nofollow" target="_self">Славянка без раздаток-2 - Чайковский (13:00)</a><br><a href="https://chgk-spb.livejournal.com/2069295.html" rel="nofollow" target="_self">Славянка без раздаток-2 - Xren (13:00)</a><br><a href="https://chgk-spb.livejournal.com/2070736.html" rel="nofollow" target="_self">ОВСЧ-6 - Чайковский (15:45)</a><br><a href="https://chgk-spb.livejournal.com/2069688.html" rel="nofollow" target="_self">Честный Эйб - Xren (16:00)</a><br><br><b>18 февраля (пн)</b><br><a href="https://chgk-spb.livejournal.com/2070916.html" rel="nofollow" target="_self">Честный Эйб - Чайковский (19:25)</a><br><a href="https://chgk-spb.livejournal.com/2067048.html" rel="nofollow" target="_self">Зимний Варан - Any day (19:30)</a><br><br><b>19 февраля (вт)</b><br><a href="https://chgk-spb.livejournal.com/2066288.html" rel="nofollow" target="_self">Парное ЧГК "Chgk is..." - Форпост (19:19)</a><br><a href="https://chgk-spb.livejournal.com/2071251.html" rel="nofollow" target="_self">Эврика-11 - Чайковский (19:25)</a><br><a href="https://chgk-spb.livejournal.com/2069787.html" rel="nofollow" target="_self">ОВСЧ-6 - Xren (19:30)</a>'''
#
#my_test_post = re.sub("<article.*?>", "", my_test_post_orig)
#my_test_post = re.sub("</article.*?>", "", my_test_post)
#my_test_post = re.sub("<div.*", "", my_test_post)
#my_test_post = re.sub("<p>.*?</p>", "", my_test_post)
#my_test_post = re.sub("<br>", "\n", my_test_post)   
#print(my_test_post)
#print(get_announcement("https://chgk-spb.livejournal.com/2046721.html"))
#ljurl = "https://chgk-spb.livejournal.com/2046721.html"
#resp
#announce
get_announcement()
#dateparser.parse("27 сентября (пт)", languages = ["ru"])
