# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
import zomatopy
#import send_mail
import json
import pandas as pd
from flask import Flask
from flask_mail import Mail,Message


app=Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='*******' # enter email id
app.config['MAIL_PASSWORD']='******' # enter user paswword
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'
    def run(self,dispatcher,tracker,domain):
        config={"user_key":"9d06cc654a2c2c45a41d36fcd5b84c23"}
        zomato=zomatopy.initialize_app(config)
        price = tracker.get_slot('price')
        price=price.lower()
        loc=tracker.get_slot('location')
        cuisine=tracker.get_slot('cuisine')
        cuisine=cuisine.lower()
        location_detail=zomato.get_location(loc,1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        budget_dict={'lesser than Rs. 300':1,'rs. 300 to 700':2,'more than 700':3,'lesser than 300':1,'300 to 700':2}
        cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
        d= json.loads(results)
        # dataframe for storing restaurants data
        res_df=pd.DataFrame()
        #index
        index=0
        if d['results_found']==0:
            dispatcher.utter_message("No_results")
        else:
            for restaurant in d['restaurants']:
                res_df.loc[index,'Name']=restaurant['restaurant']['name']
                res_df.loc[index,'location']=restaurant['restaurant']['location']['address']
                res_df.loc[index,'rating']=restaurant['restaurant']['user_rating']['aggregate_rating']
                res_df.loc[index,'price']=restaurant['restaurant']['average_cost_for_two']
                index+=1
            if budget_dict[price]==1:
                fil_df= res_df.loc[res_df['price']<=300]
            elif budget_dict[price]==2:
                fil_df=res_df.loc[((res_df['price']>=300 )&( res_df['price']<=700))]
            else:
                fil_df=res_df.loc[res_df['price']>700]
            fil_df=fil_df.sort_values(by=['rating'],ascending=False)
            dispatcher.utter_message("------ Here is the list of top "+cuisine+" restaurants in "+loc+" with average budget of "+price+" for 2 people " )
            for row in fil_df.head(5).iterrows():
                dispatcher.utter_message(row[1]['Name']+" in "+row[1]['location']+" has been rated "+row[1]['rating']+" with average cost for 2 people "+str(row[1]['price']))
        return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',price)]
class ValidateLocation(Action):
    def name(self):
        return 'validate_location'
    
    def location_list(self):
        # tier 1 cities
        cities=['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Ahmedabad', 'Pune','Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol','Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh','Coimbatore Nagpur', 'Cuttack', 
               'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 
               'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam', 'Kota', 
               'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik', 
               'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry','Purulia Allahabad', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 
               'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirupati', 
               'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Vellore', 'Warangal', 'Surat','Visakhapatnam']
        cities=[x.lower() for x in cities]
        return cities
    def run(self,dispatcher,tracker,domain):
        loc=tracker.get_slot('location')
        if loc.lower() not in self.location_list():
            dispatcher.utter_message("location is not in tier1 or tier2 cities")
            return [SlotSet('location_avl',"0")]
        else:
            dispatcher.utter_message('location found')
            return [SlotSet('location_avl',"1")]
#class ValidatePrice(Action):
#    def name(self):
#        return 'validate_price'
#    def price_list(self):
#        price_list=['lesser than Rs. 300','300 to 700','more than 700']
#        return price_list
#    def run(self,dispatcher,tracker,domain):
#        price=tracker.get_slot('price')
#        if price in self.price_list():
#            dispatcher.utter_message(" price range valid")
#            return [SlotSet('price_avl',"1")]
#        else:
#            dispatcher.utter_message(" PLease enter valid price range from the given list")
#            return [SlotSet('price_avl',"0")]
class SendMail(Action):
    def name(self):
        return 'action_mail_results'
    def run(self,dispatcher,tracker,domain):
        config={"user_key":"9d06cc654a2c2c45a41d36fcd5b84c23"}
        zomato=zomatopy.initialize_app(config)
        price = tracker.get_slot('price')
        price=price.lower()
        emailId=tracker.get_slot('emailId')
        loc=tracker.get_slot('location')
        cuisine=tracker.get_slot('cuisine')
        location_detail=zomato.get_location(loc,1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        budget_dict={'lesser than Rs. 300':1,'rs. 300 to 700':2,'more than 700':3,'lesser than 300':1,'300 to 700':2}
        cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), 20)
        d= json.loads(results)
        # dataframe for storing restaurants data
        res_df=pd.DataFrame()
        #index
        index=0
        if d['results_found']==0:
            dispatcher.utter_message("No_results")
        else:
            for restaurant in d['restaurants']:
                res_df.loc[index,'Name']=restaurant['restaurant']['name']
                res_df.loc[index,'location']=restaurant['restaurant']['location']['address']
                res_df.loc[index,'rating']=restaurant['restaurant']['user_rating']['aggregate_rating']
                res_df.loc[index,'price']=restaurant['restaurant']['average_cost_for_two']
                index+=1
            if budget_dict[price]==1:
                fil_df= res_df.loc[res_df['price']<=300]
            elif budget_dict[price]==2:
                fil_df=res_df.loc[((res_df['price']>=300) & (res_df['price']<=700))]
            else:
                fil_df=res_df.loc[res_df['price']>700]
            fil_df=fil_df.sort_values(by=['rating'],ascending=False)
        fil_df_html=fil_df.head(10)
        html_msg=''
        for row in fil_df_html.head(10).iterrows():
                html_msg+='\n'+(row[1]['Name']+" in "+row[1]['location']+" has been rated "+row[1]['rating']+" with average cost for 2 people "+str(row[1]['price']))
        msg = Message("Send Mail Tutorial!",
                      sender="****@gmail.com", # email id of the sender
                      recipients=[emailId])
        msg.body = "List of top restaurants"+html_msg           
        with app.app_context():
            mail.send(msg)
#        send_mail.mail_results(emailId,html_msg)
        

