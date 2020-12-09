# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import requests
from requests.exceptions import HTTPError
import re

from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    ActionExecuted,
    UserUttered,
)

from actions.config_reader import ConfigReader


class SetName(Action):
    def name(self):
        return "action_set_name"

    def run(self, dispatcher, tracker, domain):
        name = tracker.latest_message.get('text')

        return [SlotSet("name", name)]


class News(Action):
    # get covid news from api
    # actions/config.ini for change api_url and api_key
    def name(self) -> Text:
        return "action_news_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        try:
            self.config_reader = ConfigReader()
            self.configuration = self.config_reader.read_config()
            url = self.configuration['NEWS_API_URL'] + \
                self.configuration['NEWS_API_KEY']
            res = requests.get(url)
            jsonRes = res.json()
            articles = jsonRes["articles"]
            list_news = list()
            for index_article in range(len(articles)):
                title = articles[index_article]["title"]
                author = articles[index_article]["author"]
                news_final = str(index_article + 1) + ". " + \
                    str(title) + " - " + str(author)
                list_news.append(news_final)
            dispatcher.utter_message("\n\n".join(list_news))

        except HTTPError as http_err:
            dispatcher.utter_message(f"actions.py | class News | line 41:  HTTP error occurred: {http_err}")
        except Exception as err:
            dispatcher.utter_message(f"actions.py | class News | line 41: occurred: {err}")

        return []

class TotalGlobalCases(Action):

    def name(self) -> Text:
        return "action_global_cases_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        
        try:
            print("action_global_cases_covid")
            self.config_reader = ConfigReader()
            self.configuration = self.config_reader.read_config()

            url =  self.configuration['GLOBAL_CASES_API_URL']
            res = requests.get(url)
            jsonRes = res.json()
            totalGlobalCases = jsonRes["Global"]
            total_confirmed = str(totalGlobalCases["TotalConfirmed"])
            total_recovered = str(totalGlobalCases["TotalRecovered"])
            total_deaths = str(totalGlobalCases["TotalDeaths"])

            dispatcher.utter_message(
                f"Confirmados: {total_confirmed} \n\nRecuperados: {total_recovered} \n\nÓbitos: {total_deaths}")

        except HTTPError as http_err:
            dispatcher.utter_message(f"HTTP error occurred: {http_err}")
        except Exception as err:
            dispatcher.utter_message(f"Other error occurred: {err}")

        return []