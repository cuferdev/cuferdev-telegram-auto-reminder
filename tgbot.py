import logging
import asyncio
import os
from telethon import TelegramClient

CONFIG_FILE = "config.txt"

def save_config(api_id, api_hash, phone):
    with open(CONFIG_FILE, "w") as file:
        file.write(f"{api_id}\n{api_hash}\n{phone}")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            lines = file.read().splitlines()
            if len(lines) == 3:
                return lines[0], lines[1], lines[2]
    return None

async def main():
    config = load_config()
    
    if config is None:
        api_id = input("Введите API ID: ")
        api_hash = input("Введите API HASH: ")
        phone_number = input("Введите номер телефона: ")

        save_config(api_id, api_hash, phone_number)
    else:
        api_id, api_hash, phone_number = config

    client = TelegramClient("my_session", int(api_id), api_hash)

    async with client:
        await client.start(phone_number)

        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input("Введите код подтверждения: ")
            await client.sign_in(phone_number, code)

        chat_id = input("Введите ID чата (или @username): ")
        interval = int(input("Введите интервал отправки сообщений (в секундах): "))
        message = input("Введите сообщение: ")

        print("✅ Бот запущен! Используйте Ctrl+C для остановки.")

        while True:
            try:
                entity = await client.get_input_entity(chat_id)
                await client.send_message(entity, message)
                print(f"✅ Сообщение отправлено в {chat_id}")
            except Exception as e:
                print(f"❌ Ошибка: {e}")
            
            await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.run(main())
