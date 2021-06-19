# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:36:57 2021

@author: Kuma
"""

#Update tables for mySQL database

import pandas as pd

#read csvs of tables
allevents=pd.read_csv(r'concat_events.csv')

events=pd.read_csv(r'events.csv')
customer=pd.read_csv(r'customer.csv', encoding="utf-8")
email=pd.read_csv(r'email.csv')
mailing=pd.read_csv(r'mailing.csv')
paid=pd.read_csv(r'paid.csv')
acpss_attendance=pd.read_csv(r'acpss_attendance.csv')
customer_type=pd.read_csv(r'customer_type.csv')


#read csv of new event
new_event=pd.read_csv(r'report_creative.csv')
new_event=new_event.rename(columns={'First Name':'firstname', 
                                            'Last Name':'lastname', 
                                            'Email':'email',
                                            'Order Date':'date',
                                            'Order #':'order_id',
                                            'Do you agree to receive future events and news from the event organizers?':'mailing_list'})




#1. Add new event to 'events' table; event number, title and date
#new_row={'acpss_id':, 'acpss_name':'', 'acpss_date':''}
new_row={'acpss_id':5, 'acpss_name':'Pathways into Creative Industries', 'acpss_date':'2021/06/16'}
events=events.append(new_row, ignore_index=True)
events.to_csv(r'events.csv', index=False) #save csv


#2. Add new email info into 'email' table
new_event_email=new_event[['email', 'date']] #subset email columns
concat_email=pd.concat([email, new_event_email])#concatenate original customers with new event customers
concat_email=concat_email.drop_duplicates(['email'], keep='first')#drop duplicate names from new event
last_email_id=email['email_id'].iloc[-1]#store the last email_id value from original email file
#grab only the rows with nas to generate new email_id s
nas=concat_email[concat_email['email_id'].isna()].reset_index(drop=True)
nas['email_id']=nas.index+last_email_id+1 #add new email_ids
nas['customer_id']=nas.index+last_email_id+1 #add new customer ids
new_email=pd.concat([email, nas]) #concatenate old email list with new emails
new_email.to_csv(r'email.csv')

#----------------------------------------
#3. Add new customer info into 'customer' table
#rename First Name, Last Name columns in newevent df
new_event_customers=new_event[['firstname', 'lastname', 'email']] #subset firstname, lastname, email columns
new_event_customers_email=pd.merge(new_email, new_event_customer, on='email')
sub_new_event_customers=new_event_customers_email[['customer_id','firstname', 'lastname']]
new_customers=pd.concat([customer, sub_new_event_customers]).drop_duplicates(['customer_id'], keep='first').reset_index(drop=True)
new_customers.to_csv(r'customer.csv')#save csv

