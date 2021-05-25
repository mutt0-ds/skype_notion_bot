# Skype + Notion Notification Bot
![logo](https://github.com/mutt0-ds/skype_notion_bot/blob/main/media/logo.png)

This is a small project I've worked on during my free time, while trying to optimize my Notion database using [their new API](https://developers.notion.com/docs/getting-started) and send daily reminders about the tasks/reminders I have scheduled for a specific day, based on my Notion notes.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements. I've been using the unofficial [skpy](https://pypi.org/project/SkPy/) library for automatizing Skype notifications: please check out their documentations for retrieving the CHAT_ID required in the .env file.

Additionally, I used dateparser for parsing the different dates of the alerts and python-decouple for reading the .env variables.

```bash
pip install requirements.txt
```

## Descriptioon
Here's an example of my To-Do Notion Page:

![my To-Do page](https://github.com/mutt0-ds/skype_notion_bot/blob/main/media/home.png)

I'm storing my tasks in 4 different categories, depending on their urgency, and sometimes I set up a reminder using the "Alert" subproperty. 
I decided to connect this database to my Skype Account because Notion's notification system only works through emails or mobile.

![my To-Do page](https://github.com/mutt0-ds/skype_notion_bot/blob/main/media/message.png)

Every day, the bot sends me the tasks/reminders I've assigned to that day through Skype.

## Usage
This code is based on my personal database, you will have to edit the env. variables and the API call. 
I hope you will find it useful. Pull requests are welcome. 
