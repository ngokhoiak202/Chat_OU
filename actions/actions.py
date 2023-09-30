# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa.shared.core.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


# class FallbackClass(Action):
#
#     def name(self) -> Text:
#         return "fallback_action"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]):
#         # Kiểm tra xem câu hỏi đó có phải là một trường hợp "fallback" hay không
#         if tracker.active_loop_name == "fallback":
#             # Thực hiện các hành động cần thiết
#             dispatcher.utter_message(text="Xin lỗi, tôi không hiểu câu hỏi của bạn. Bạn có thể thử lại không?")
#
#         return []
#
#
# class FallbackAction(Action):
#
#     def name(self) -> Text:
#         return "fallback_action"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> None:
#         # Trả về một thông báo cho người dùng
#         dispatcher.utter_message("Xin lỗi, tôi không hiểu câu hỏi của bạn.")
