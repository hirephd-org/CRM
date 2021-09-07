import pandas as pd
from pandas.core.frame import DataFrame

events = pd.read_csv(r'C:\Users\Kuma\Dropbox\event_id.csv')

events_test = events.iloc[1:] #testing without first event "MLA" without csv associated with it

#for every event_name, load up the csv and save df in a new variable

def load_events(event_name): # function to load up the csv of each event using the event name
    file_path = r'C:\Users\Kuma\Dropbox\_report_' + event_name + '.csv' #(use "r" before the path string to address special character, such as '\')
    read = pd.read_csv(file_path)   #read the csv file using the 'PATH' variable 
    df = DataFrame(read)
    return df

for i in events_test['event_name']: #calls each event name under events_name in events dataframe
    globals()["event_%s" %i] = load_events(i) #dataframes for each event can be called as example: "event_" + "biotech" = event_biotech
print(event_biotech) #test to see if it works

#note: apparently using globals() is bad practice?

#-----funciton for concatenating all events into one dataframe-------

def concatenate_events(): # function to load up the csv of event using the event name
    """this function is for concatenating all events (all csv event files in dropbox)"""
    li = []
    for i in events_test['event_name']:
        file_path = r'C:\Users\Kuma\Dropbox\_report_' + i + '.csv' #(use "r" before the path string to address special character, such as '\')
        df = pd.read_csv(file_path)   #read the csv file using the 'PATH' variable 
        li.append(df)
    
    all_events = pd.concat(li, axis = 0, ignore_index = True)
    print(all_events)
    
    












