from apscheduler.schedulers.background import BackgroundScheduler
from getlist import get_event_list
from datetime import datetime

def start():
    print("scheduler!")
    listScheduler = BackgroundScheduler()
    listScheduler.add_job(get_event_list, 'interval', minutes = 1, start_date = datetime.now())
    listScheduler.start()

    # detailScheduler = BackgroundScheduler()
    # detailScheduler.add_job(getlist.get_detail_info, 'interval', minutes = 2, start_date = datetime.now())
    # detailScheduler.start()
   
    start_date=datetime.now()
start()