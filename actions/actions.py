from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class WorkExperienceDetails(Action):

    def name(self) -> Text:
            return "action_work_experience"
    
    async def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
            work_experience_text = """Here are the work experiences:
            1. Technical Support Engineer @ AMBOSS
            2. Technical Support Specialist @ PagerDuty
            3. Support Analyst @ WaveHQ
            """
            dispatcher.utter_message(text=work_experience_text)
            

            return [SlotSet("skill","Work Experience")]

class TechSkillsDetails(Action):

    def name(self) -> Text:
            return "action_tech_skills"
    
    async def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
            tech_skills_text = """Here are the tech skills:
            1. Programming languages: Python for scripting, Php for current work (monolith application), and GO for side projects
            2. Experience working with non-technical and technical customers or employees to solve problems using technical solutions
            3. General debugging / troubleshooting skillls
            """
            dispatcher.utter_message(text=tech_skills_text)
            

            return [SlotSet("skill","Tech Skills")]

class LeadershipDetails(Action):

    def name(self) -> Text:
            return "action_leadership"
    
    async def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
            leadership_text = """Here are the leadership experiences:
            1. First hire in a new role at a hyper growth start up --  "Technical McGuyver" (Technical Support Engineer) @ AMBOSS 
            2. Lead multiple internal projects and features for internal tools at AMBOSS 
            """
            dispatcher.utter_message(text=leadership_text)
            

            return [SlotSet("skill","Leadership Skills")]

class SoftDetailsDetails(Action):

    def name(self) -> Text:
            return "action_soft_skills"
    
    async def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
            soft_skills_text = """Here are the soft skills:
            1. Excellent communicator to all types of stakeholders (C-suite, internal support, non-technical customers etc)
            2. Skilled at discovering the root of an issue while providing immediate customer relief (whether it's solving the issue, providing a workaround, or outlining process moving forward)
            3. Experience providing technical and workflow solutions to multiple stakeholders, who sometimes had competing priorities
            """
            dispatcher.utter_message(text=soft_skills_text)
            

            return [SlotSet("skill","Soft Skills")]

class DeeperDetails(Action):

    def name(self) -> Text:
            return "action_deeper_details"
    
    async def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            skill = tracker.slots['skill']
            if skill == "Work Experience":
                dispatcher.utter_message(text="""
                * Multiple roles providing technical solutions to customer facing issues, by supporting customer facing teams and directly working with customers
                * Experience at hyper growth start ups wearing multiple hats
                """)
            elif skill == "Tech Skills":
                dispatcher.utter_message(text="""
                * Ability to independently learn a monolith application. Fix bugs and implement new features
                """)
            elif skill == "Leadership Skills":
                 dispatcher.utter_message(text="""
                 * Ability to push cross-functional projects and features to completion
                 * Capability to improve and scale cross-deparmental workflows
                 * Ability to work with little to no guidance
                 """)
            elif skill == "Soft Skills":
                 dispatcher.utter_message(text="""
                 * Enthusiastic, positive, and growth mindset orientated
                 * Experience communicating technical topics to a non-technical audience
                 """)


            return []