#this code will get the attendee list from eventbrite, get the emails of those who said yes to receiving a newsletter, and upload into mailchimp
import requests
import json
from configparser import ConfigParser
import pandas as pd


config = ConfigParser()
config.read(r'C:\Users\Kuma\Documents\Python\HirePhD\eventbrite\config.cfg')

eventbrite_token = config['user_info']['eventbrite_token']

event_id = config['eventbrite_ids']['event_id']#update event_id for each event

response = requests.get("https://www.eventbriteapi.com/v3/users/me/?token=" + eventbrite_token) #log into eventbrite

reports = requests.get( "https://www.eventbriteapi.com/v3/events/" +event_id+ "/attendees/?token=" + eventbrite_token) #get event details
attendees = reports.json()['attendees']


df = pd.json_normalize(attendees)
df1 = df['answers']
df1


#next check how we can get the dictionaries out to dataframe