"""
@author Gleb Tcivie
An application that checks from the list of the products if some price or aviability has changed and notifies via Telegram bot
"""

import asyncio
import telegram
import json


async def main():
    with open('Credentials', 'r') as file:
        credentials = json.load(file)
        bot = telegram.Bot(credentials['TOKEN'])
        async with bot:
            print((await bot.get_updates())[0])


if __name__ == '__main__':
    asyncio.run(main())
