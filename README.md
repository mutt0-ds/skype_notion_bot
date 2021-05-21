# Skype Bot (README WIP)

This is a small project I've worked with during my free time, while trying to optimize my Notion database using [their new API](https://developers.notion.com/docs/getting-started) and send daily reminders about the task I have planned for a specific day, based on my Notion notes.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements. I've been using the [skpy](https://pypi.org/project/SkPy/) library for automatizing Skype notifications: please check out their documentations for retrieving the CHAT_ID required in the .env file.

```bash
pip install requirements.txt
```

## Notion Data

![my To-Do page](https://github.com/mutt0-ds/skype_notion_bot/blob/main/media/home.png)
I've been storing my tasks in my To-Do page 

![my To-Do page](https://github.com/mutt0-ds/skype_notion_bot/blob/main/media/message.png)
The bot send me every day my tasks

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
