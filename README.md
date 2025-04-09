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
