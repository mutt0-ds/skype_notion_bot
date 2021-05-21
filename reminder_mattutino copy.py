
from numpy import datetime64
from skpy import Skype
from datetime import datetime, date
import notion_api_call
from decouple import config

#skype access
EMAIL = config('EMAIL')
PSW = config('PSW')
ID_CHAT = config('ID_CHAT')

#notion access
NOTION_TOKEN = config('NOTION_TOKEN')
DB_ID = config('DB_ID')

#mapping with emojis makes the message shorter
DICT_TASK = {'⚠\xa0ASAP ⚠':"⚠",
               'Urgenti': "🏎️",
               'Medie':'👌',
               'Remoti':'🍿'}

def daily_reminder(NOTION_TOKEN,DB_ID): 
    request = notion_api_call.API_call(NOTION_TOKEN,DB_ID)
    results = notion_api_call.retrieve_data_from_req(request)

    text = f"Today is {date.today().strftime('%A')} (party)\n"

    notion_text=""
    for index,row in results.iterrows():
        if isinstance(row["Alert_parsed"], datetime):
            if row["Alert_parsed"].date() == date.today():
                
                symbol= DICT_TASK.get(row["Status"])
                name_task=row["Name"]
                
                if row["Alert_parsed"].hour !=0:
                        time=row["Alert_parsed"].strftime("%h:%S%M")
                else:   time="9:00" #if I didn't select an hour, let's say it's in the morning

                notion_text+= f"\n{symbol} {name_task} - {time}"

    if notion_text=="":  text+="Nothing to do today (sun)!" 
    else:                text+=f"Here's what you have to do:\n{notion_text}"
    return text   

def skype_message(EMAIL,PSW,ID_CHAT,content):
    sk = Skype(EMAIL, PSW)
    ch = sk.chats[ID_CHAT] 
    msg = ch.sendMsg(content)

if __name__=="__main__":
    data = daily_reminder(NOTION_TOKEN,DB_ID)
    skype_message(EMAIL,PSW,ID_CHAT,data)
    print("All done!")