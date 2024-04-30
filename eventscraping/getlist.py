import time
from datetime import datetime
from get_list_lib.get_list_luma import get_list_luma
from get_list_lib.get_list_eventbrite import get_list_eventbrite
import requests

def get_event_list():   
    event_list = []
    event_list.extend(get_list_luma())
    # event_list.extend(get_list_eventbrite())
    # time.sleep(5)
    # print("1112:", datetime.now())    
    
    print(event_list)
    # print(len(event_list))

    

# if __name__ == "__get_event_list__":
#     get_event_list()
    # return event_list

# def get_detail_info():
#     print("21221:", datetime.now())


#     return get_event_list()

# get_event_list()
