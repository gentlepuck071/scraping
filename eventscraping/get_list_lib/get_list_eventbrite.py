from get_list_lib.cities import web3event_cities
from get_list_lib.tags import web3event_tags
from get_list_lib.get_event_list import get_event_list
from common.utils import remove_repeated_events
from get_list_lib.event_detail_info_eventbrite import get_detail_info_eventbrite


def get_list_eventbrite():
    eventbrite_url = "https://www.eventbrite.com"
    list_eventbrite = []
    for city in web3event_cities:
        for tag in web3event_tags:
            url = eventbrite_url + "/d/" + city + "/" +tag
            list_eventbrite.extend(get_event_list(url))
    
    filtered_event_list = remove_repeated_events(list_eventbrite, "href")

    print("count:", len(filtered_event_list))

    