import requests
from datetime import datetime, timedelta
import data
import config


# This function is pretty unnecessary and was made just for practice (and fun). Yay!
# It takes today's date, adds 1 day to it, then converts it into a str and slices to (yyyy-mm-dd) format
def tomorrow_maker():
    tomorrow_raw = datetime.today() + timedelta(days=1)
    tomorrow = str(tomorrow_raw)[:10]
    return tomorrow


# This function is, also, pretty unnecessary and was made just for practice (and fun). Yay!
# It takes the template body for a new order, replaces its deliveryDate with tomorrow's date from tomorrow_maker func
# and returns the modified body
def new_order_body_modifier():
    tomorrow = tomorrow_maker()
    modified_body = data.new_order_body
    modified_body['deliveryDate'] = tomorrow
    return modified_body


# This functions creates a new order and returns the created order's tracking number
def create_order():
    modified_body = new_order_body_modifier()
    response = requests.post(config.SITE_URL + config.CREATE_ORDER,
                             json=modified_body,
                             headers=data.headers)
    track = response.json()['track']
    return track


# This function check the specified order in the database (don't forget to supply the track number)
# and returns the response
def check_track(track):
    track_param = {'t': track}
    response = requests.get(config.SITE_URL + config.CHECK_ORDER,
                            params=track_param)
    return response
