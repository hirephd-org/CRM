
def concatenate_events(): # function to load up the csv of event using the event name
    """this function is for concatenating all events (all csv event files in dropbox)"""
    li = []
    for i in events_test['event_name']:
        file_path = r'C:\Users\Kuma\Dropbox\_report_' + i + '.csv' #(use "r" before the path string to address special character, such as '\')
        df = pd.read_csv(file_path)   #read the csv file using the 'PATH' variable 
        li.append(df)
    

#for every event_name, load up the csv and save df in a new variable

def load_events(event_name): 
    """this function is to load up the csv of each event using the event name. Returns dataframe"""
    file_path = r'C:\Users\Kuma\Dropbox\_report_' + event_name + '.csv' #(use "r" before the path string to address special character, such as '\')
    read = pd.read_csv(file_path)   #read the csv file using the 'PATH' variable 
    df = DataFrame(read)
    return df

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
