#create a function with input = new event csv and output = updated main newsletter list csv AND new customer csv

import pandas as pd


#automate download of eventbrite newest event here

#import new event csv
event = pd.read_csv(r'C:\Users\Kuma\Dropbox\_report_julienne.csv')
event_number = 11

#event = df of new event

def updatelist(event, event_number):
    """
    This function will call the main_mailing_list.csv and update it with the new customer info from the newest eventbrite event csv
    event = df of new event
    event_number = event number of new event
    """
    
    #change mailing list question column to string type and change column to "mailiing"
    event["mailing"] = event["Do you agree to receive future events and news from the event organizers?"].astype(str)
    #keep only customers that responded "yes" to mailing list
    yes_list = event[event["mailing"].str.contains("Yes")]
    #create a subset of data with the name and email of subscribers
    new_list = yes_list[["First Name", "Last Name", "Email"]]

    #read in the main mailing list 
    main = pd.read_csv("mailing_list_main.csv") 
    
    #concatenate new event list with main list
    concat = pd.concat([main, new_list])
    

    #identify only the newest subscribers from the new event
    new_subscr_raw = pd.merge(main, new_list, on='Email', how='outer', indicator=True).query('_merge == "right_only"').drop(columns=['_merge'])
    #select only first names and last names from "right" df
    new_subscr_raw = new_subscr_raw[["First Name_y", "Last Name_y", "Email"]]
    #change first and second column names to "First Name" and "Last Name"
    new_subscr = new_subscr_raw.rename({'First Name_y': 'First Name', 'Last Name_y': 'Last Name'}, axis = 1)
    
    #create new main mailing list
    new_mailing = pd.concat([main, new_subscr])

    #create a csv file of only the new subscribers
    new_subscr.to_csv('new_subscribers.csv', index = False) 
    #create a csv with the newest subsribers concatenated to the main list
    new_mailing.to_csv('new_mailing_list.csv', index=False)


updatelist(event, 11)
    