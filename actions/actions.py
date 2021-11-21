# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from logging import NullHandler
from typing import Any, Text, Dict, List
import os
import math
import random
import smtplib
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser
import mysql.connector
from mysql.connector import errorcode

from rasa_sdk.events import AllSlotsReset

login_user='root'
database_password = "vaibhav"

class takeType(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["types"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]



class symptomClass(Action):

    def name(self) -> Text:
        return "action_symptom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city=tracker.get_slot("city")
        symptom=tracker.get_slot("symptom")
        print(city,symptom)
        
        cnx = mysql.connector.connect(user='root',password=database_password, database='optum')
        cursor = cnx.cursor()


        query = ("")

        cursor.execute(query, ())
        uid = -1
        for (a,b) in cursor:
            
            uid = a
        cursor.close()
        cnx.close() 

        dispatcher.utter_message("submitted")
        



class symptomClass(Action):

    def name(self) -> Text:
        return "action_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city=tracker.get_slot("city")
        speciality=tracker.get_slot("speciality")
        time=tracker.get_slot("time")
        print(city,speciality,time)
        
        cnx = mysql.connector.connect(user='root',password=database_password, database='optum')
        cursor = cnx.cursor()


        query = ("")

        cursor.execute(query, ())
        uid = -1
        for (a,b) in cursor:
            
            uid = a
        cursor.close()
        cnx.close() 

        dispatcher.utter_message("submitted")
        
        
