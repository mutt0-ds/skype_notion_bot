import os
import pandas as pd
import requests
import dateparser

def API_call(NOTION_TOKEN,DB_ID):
    DB_URL = f'https://api.notion.com/v1/databases/{DB_ID}/query'
    CONT_TYPE = 'application/json'
    HEAD = {'Authorization': "Bearer "+NOTION_TOKEN, 
                'Content-Type': CONT_TYPE,
                'Notion-Version': '2021-05-13'}
    FILTER="""{
        "filter": {
            "or": [
            {
                "property": "Status",
                "select": {"equals": "⚠\xa0ASAP ⚠"}
            },
            {
                "property": "Status",
                "select": {"equals": "Urgenti"}
            },
            {
                "property": "Status",
                "select": {"equals": "Medie"}
            },
            {
                "property": "Status",
                "select": {"equals": "Remoti"}
            }
                ]
                }
            }""".encode('utf-8')

    r = requests.post(DB_URL, headers=HEAD,data=FILTER)
    assert(r.status_code == 200),"Notion API (or DB) Issue!\n"+r.json()["message"]
    return r

def retrieve_data_from_req(r):
    #I care about name, status and annotation
    column_list=[]
    for obj in r.json()['results']:
        name_list = obj["properties"].get("Name").get("title")
        name= " ".join([i.get("plain_text") for i in name_list])

        status = obj["properties"].get("Status").get("select").get("name")
        
        reminder = obj["properties"].get("Alert").get("rich_text")
        
        alert = "" #it could be empty
        for i in reminder:
            if i.get("type") == "mention": 
                if "date" in list(i.get("mention").keys()):
                    alert = i.get("mention").get("date").get("start")

        column_list.append([name,status,alert])

    #creating the final df
    df = pd.DataFrame(column_list,columns=["Name","Status","Alert"])
    df["Alert_parsed"] = df.Alert.apply(lambda x: dateparser.parse(x,settings={'DATE_ORDER': 'YMD'}))
    return df
