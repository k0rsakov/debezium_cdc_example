# CDC Debezium

Пример создания CDC через Debezium.

[Статья на habr](https://github.com/k0rsakov/debezium_cdc_example).

Для создания виртуального окружения выполните:

```bash
python3.11 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt
```

Для активации виртуального окружения выполните:

```bash
source venv/bin/activate
```

Для запуска генератора записей в таблицу (добавление новых и изменение существующих пользователей) выполните:

```bash
python table_simulation.py
```