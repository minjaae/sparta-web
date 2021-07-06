from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 한 개 찾기 - 예시
matrix = db.movies.find_one({'title':'매트릭스'})
matrix_star = matrix['star']
print(matrix_star)

sameMovies = list(db.movies.find({'star':matrix_star},{'_id':False}))

for movie in sameMovies:
    print(movie['title'])

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})