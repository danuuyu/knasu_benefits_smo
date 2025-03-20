import json
import os
import aiofiles

async def get_message(key_message):
    messages_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'messages.json')
    async with aiofiles.open(messages_path, 'r', encoding='utf-8') as file:
        messages = json.loads(await file.read())
        return messages[key_message]
    
