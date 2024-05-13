# CDC Debezium

Пример создания CDC через Debezium

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