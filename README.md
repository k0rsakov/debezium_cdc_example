# CDC на примитивах

Пример создания CDC через Debezium.

[Статья на habr](https://habr.com/ru/articles/812797/).

Для создания виртуального окружения выполните:

```bash
python3.11 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt
```

Для запуска генератора записей в таблицу (добавление новых и изменение существующих пользователей) выполните:

```bash
python table_simulation.py
```

___

Если вам необходима консультация/менторство/мок-собеседование и другие вопросы по дата-инженерии, то вы можете
обращаться ко мне. Все контакты указаны по
[ссылке](https://www.notion.so/korsak0v/Data-Engineer-185c62fdf79345eb9da9928356884ea0).

