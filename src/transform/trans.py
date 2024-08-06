import pandas as pd

def apply_type2df(load_dt='20190101', path="~/data/2019movie"):
    df = pd.read_parquet(f'{path}/{load_dt}')
    df['rnum'] = pd.to_numeric(df['rnum'])
    assert str(df['rnum'].dtype) in ['int64']
    num_cols = ['rnum', 'audiAcc']

    df[num_cols] = df[num_cols].apply(pd.to_numeric)
    return df
