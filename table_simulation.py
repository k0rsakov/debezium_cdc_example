import uuid
import json
import time
import random
import requests

import pandas as pd
from connectors_to_databases import PostgreSQL

pg = PostgreSQL(
    host='localhost',
    port=5432,
    login='postgres',
    password='postgres',
)


def insert_user():
    r = requests.get(url='https://randomuser.me/api/')

    d = json.loads(r.text)
    dict_user = d['results'][0]

    d_ = {
        'first_name': [dict_user['name']['first']],
        'last_name': [dict_user['name']['last']],
        'email': [dict_user['email']],
    }

    df = pd.DataFrame(d_)

    try:
        pg.insert_df(
            df=df,
            pg_table_schema='inventory',
            pg_table_name='customers',
        )
    except Exception as ex:
        pass

    time.sleep(2)


def update_user():
    df_id = pg.execute_to_df(
        '''
        SELECT id FROM inventory.customers
        '''
    )

    len_list = len(df_id.id)

    random_user = random.randint(0, len_list)

    try:
        pg.execute_script(
            f'''
            UPDATE
                inventory.customers
            SET
                first_name = '{str(uuid.uuid4())}',
                last_name = '{str(uuid.uuid4())}'
            WHERE
                id = {df_id.id[random_user]}
            '''
        )
    except Exception as ex:
        pass

    time.sleep(2)


while True:
    if random.randint(1, 1000) % 2 == 0:
        print('INSERT new USER')
        insert_user()
    else:
        print('UPDATE current USER')
        update_user()
