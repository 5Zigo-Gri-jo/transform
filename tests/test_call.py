from src.transform.trans import apply_type2df
import pandas as pd

def test_apply_type2df():
    df = apply_type2df()
    assert isinstance(df, pd.DataFrame)
    assert str(df['rnum'].dtype) in ['int64']
    assert str(df['audiAcc'].dtype) in ['int64']
    
    num_cols = [
            'salesAmt', 'salesShare', 'salesInten',
            'salesChange', 'salesAcc', "audiCnt","audiInten",
            "audiChange","audiAcc","scrnCnt","showCnt","load_dt"
            ]

    for c in num_cols:
        assert df[c].dtype in ['int64', 'float64']
    print(df)
