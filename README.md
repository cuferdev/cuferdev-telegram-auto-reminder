# cuferdev-telegram-auto-reminder

A simple bot that sends a message to a Telegram chat on behalf of the user at a specified interval.
Created in Python using the Telethon library.

## What it does
- Logs in to Telegram using your phone number
- Sends a specified message to a designated chat at a set interval
- Runs infinitely in the background (until closed)

## Technologies used
- Python 3.10+
- Telethon

## How to use
- Upon the first run, the program will ask you to enter your api_id and api_hash, which you can obtain from https://my.telegram.org, then enter your phone number, confirmation code (which will be sent via 
- Telegram), password (if any), chat id or @username where the message will be sent, the interval (in seconds), and the message itself.
- After the first run, several session files will be created. On subsequent launches, you will only need to enter the chat id or @username, the interval (in seconds), and the message.
- If you delete the session files, you will need to repeat the initial setup process.
- If something doesn’t work, try deleting the session files and restarting the program.

## Use cases
- Self-organization: reminders to yourself

- Bots without hosting — just run it on your computer

- Auto-reports, ritual reminders, commands

## Contact
If you want to order a similar bot or another simple program — feel free to contact me: Telegram: @cufeer

** Original README in Russian below **

# cuferdev-telegram-auto-reminder

Простой бот, который отправляет сообщение в Telegram-чат от имени пользователя с заданным интервалом.  
Создан на Python с использованием библиотеки [Telethon](https://github.com/LonamiWebs/Telethon).

## Что делает
- Авторизуется в Telegram по номеру телефона
- С определенным интервалом отправляет заданное сообщение в указанный чат
- Работает бесконечно в фоне (до закрытия)

## Используемые технологии
- Python 3.10+
- Telethon

## Как использовать
- При первом запуске программа попросит вас ввести свой api_id и api_hash которые вы можете узнать на сайте https://my.telegram.org , после чего вам нужно ввести свой номер телефона, код подтверждения ( придет в телеграмм ), пароль ( если есть ) chat id или @username в который будет отправляться сообщение, интервал ( в секундах ), и само сообщение. 
- После первого запуска создадутся несколько файлов ( это ваша сессия ) при следущем запуске вам нужно будет ввести только chat id или @username в который будет отправляться сообщение, интервал ( в секундах ), и само сообщение.
- При удалении файлов с вашей сессией вам придется делать все то, что вы делали при первом запуске.
- Если что-то не работает попробуйте удалить файлы с сессией и перезапустить программу.

## Применение
- Самоорганизация: напоминалки самому себе

- Боты без хостинга — просто запусти у себя на компе

- Автоотчёты, ритуальные напоминания, команды

## Связь
Если хочешь заказать подобный бот или другую простую программу — пиши:
Telegram: @cufeer
