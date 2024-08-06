# Transform_package
이 레파지토리는 https://github.com/5Zigo-Gri-jo/airflow_dags.git 레포지토리의 하위속성 패키지입니다.
해당 레포지토리는 영화 박스오피스 데이터를 변환하는 Transform 패키지입니다.



## 목차

- [필요 조건](#필요-조건)
- [설치 방법](#설치-방법)
- [모듈 기능](#모듈-기능)

## 필요 조건

- Python 3.x
- `requests` 라이브러리
- `pandas` 라이브러리
- `pyarrow` 라이브러리 (Parquet 파일 저장을 위해 필요)

## 설치 방법
1. 레포지토리 클론  
```
$ git clone git@github.com:5Zigo-Gri-jo/transform.git
```

2. 클론한 디렉토리로 이동  
```
$ cd transform
```

3. 설치 이후 환경설정 
```
$ source .venv/bin/activate
$ pdm init
$ pdm install
```

## 모듈 기능
```trans.py```
- 영화진흥위원회에서 추출한  일별 박스 오피스 Parquet 파일을 정제하고 가공합니다.
- 이 파일은  2019년의 데이터를 일별로 추출하여 각각 365개의 parquet 파일을 정제하는 함수를 담고 있습니다.  

```apply_type2df```
- 지정된 경로와 날짜의 Parquet 파일을 읽어와 rnum과 audiAcc 열의 데이터를 숫자형으로 변환한 후 반환합니다.
- 데이터 변환 중 rnum 열이 'int64'인지 확인합니다.



