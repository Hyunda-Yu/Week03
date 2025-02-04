import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.dbmoviescrapping

def date_rank(date):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date='+date,headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')
  movies=soup.select('#old_content>table>tbody>tr')

# movies (tr들) 의 반복문을 돌리기
  for movie in movies:
     a_tag=movie.select_one('td.title>div>a')
     if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text # td 태그 사이의 텍스트를 가져오기
        each_movie= {'rank':rank,'title':title,'star':star}
        collection = 'movie_' + date
        db[collection].insert_one(each_movie)

date_rank('20190705')

