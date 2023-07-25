# import datetime
# import isodate
# import requests
# import pprint
# import pandas as pd
from googleapiclient.discovery import build

from urllib.parse import urlparse

YOUTUBE_API_KEY = 'AIzaSyAem-ptyr8RMcY3l-r2fnodMvQrnvlrwDI'

youtube = build('youtube','V3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.serch().list(
    part='snippet',
    q='KOG',
    order='viewVount',
    type='video',
).execute()

search_response['items'][0]

# class youtube_list_scv:
#     def __init__(self):
#         # APIから取得できる時間が標準時なので時差用の変数を用意
#         self.JST = datetime.timedelta(hours=9)
        
#         # 過去のCSVからpandas.Dataframeを用意、ない場合新しいものを用意
#         try:
#             self.csvData = pd.read_csv('videos_csv.csv', comment='*')
#         except:
#             colname = ['id','channel','title','url','state','start','end']
#             self.csvData = pd.DataFrame(index=[], columns=colname)

#         # Youtube search APIにおいて、いちどのリクエストでいくつ取得するか
#         self.NumList = 5

#     def timetrans(self, strtime):
#         '''
#         日時のフォーマットがグリニッジ標準時かつisoformatの文字列で返されるため、
#         日本時間のdate型に直して返します
#         '''
#         stime = datetime.datetime.fromisoformat(strtime[:-1]) + self.JST
#         return stime.replace(microsecond=0)
    
#     def YouTubelist(self, nPt, channel):


