# imports
import pandas as pd

# custom imports
from config import engine, logger


def select(id):
    try:
        query = f'''
        select *
        from tb_messages
        where 1 = 1
        '''

        if id is not None:
            query += f' and id = {id}'

        df = pd.read_sql(query, con=engine)
        return df
    except Exception as e:
        logger.error('Erro')
        print(e)


def insert(message):
    try:
        df = pd.DataFrame([message.__dict__])
        df.to_sql('tb_messages', con=engine, if_exists='append', index=False)
    except Exception as e:
        logger.error('Erro')
        print(e)


def delete(id):
    query = f'''
    delete *
    from tb_messages
    where id = {id}
    '''
    engine.execute(query)
