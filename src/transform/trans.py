import pandas as pd

def apply_type2df(load_dt='20190101', path="~/data/2019movie"):
    df = pd.read_parquet(f'{path}/{load_dt}.parquet')
    df['rnum'] = pd.to_numeric(df['rnum'])
    assert str(df['rnum'].dtype) in ['int64']
    num_cols = ['salesAmt', 'salesShare', 'salesInten', 'salesChange', 'salesAcc', "audiCnt","audiInten","audiChange","audiAcc","scrnCnt","showCnt"] 

    df[num_cols] = df[num_cols].apply(pd.to_numeric)
    return df

def avg_month(path='~/data/2019movie/tmp.parquet'):
	col_selected = ['rank', 'movieCd', 'movieNm', 'openDt', 'salesAmt', 'salesAcc', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'load_dt']
	df_all = pd.read_parquet(path)
	df_new = df_all[col_selected]
	#일별 평균관객 수
	df_avgCnt = df_new.groupby(['load_dt'])['audiCnt'].mean().to_frame('avg_viewers').reset_index()
	df_avgCnt.sort_values('avg_viewers', ascending=False)
	#월별 평균관객 수
	df_monthadd = df_new
	df_monthadd.loc[:,'month'] = df_monthadd['load_dt'].str[4:6]
	month_avg = df_monthadd.groupby(['month'])['audiCnt'].mean().to_frame('avg_viewers').reset_index()
	month_avg = month_avg.sort_values('avg_viewers', ascending=False)
	month_avg.to_parquet('~/data/2019movie/month_avg.parquet')
	return month_avg
