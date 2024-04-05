import re

def remove_repeated_events(event_list_values, key):
    if not isinstance(event_list_values, list):
        raise ValueError("event_list_values must be a list")
    
    if not event_list_values:
        return []
    
    unique_values_set = set()

    unique_events = []

    for event in event_list_values:
        value = event.get(key)
        if value is not None and value not in unique_values_set:
            unique_values_set.add(value)
            unique_events.append(event)

    return unique_events

def check_keywords_in_title(title, keywords):
    for keyword in keywords:
        if keyword.lower() in title.lower():
            return True
    return False

def extract_numbers_with_regex(input_string):
    return re.findall(r'\d+', input_string)