#this code will get the attendee list for the newest event from eventbrite, get the emails of those who said yes to receiving a newsletter, and upload into mailchimp
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
attendees = reports.json()['attendees'] #get attendee reports

#create a dataframe with attendee email, first name, last name and questions
df = pd.json_normalize(attendees, ['answers'], [['profile','email'], ['profile', 'first_name'], ['profile', 'last_name']], errors = 'ignore')

#subset only those rows with the mailing list question
df_mail = df[df['question'] == "Do you agree to receive future events and news from the event organizers?"]

#subset only those rows that say yes
df_yes = df_mail[df_mail["answer"].str.contains("Yes")]
new_yes_list = df_yes[['profile.first_name', 'profile.last_name', 'profile.email']]
new_yes_list

#next check how we can get the dictionaries out to dataframe