from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# get("/") mean operation mean get request to serve  in / endpoint
@app.get("/")
def index():
    return {"message": "i am mehran"}
    # retrun better to dict or json format

# for run at termianl use uvicorn main:app --reload in this command
# app : mean instance varibale -> app = FastAPI()

'''GET method overview'''

# this section of code more deatil of GET method in fastapi
'''
Path parameters
predefined values
Query parameters
'''

# path parameter
@app.get('/blog/{id}')
def get_post(id):
    return {"message": f"blog with id is {id}"}

# tyep validation
# this concept user just can INT type value to {id}
# when user get str or other type fastapi show he a ERROR :D
@app.get('/blog/{id}')
def gets(id: int):
    return {"message" : "this input in my path just you can int pass like {id}"}


# Pydantic and order is important (this fun create in top of /blog/{id})
"""
mean:
1. /blog
2. /blob/allpost
3. /blog/{id}
"""
@app.get("/blog/all")
def get_all_blog():
    return {"message" : "All blog provided"}


# Predefined path :F
# predefined values with <Enum>
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto =  'howto'

# you can not pass data in {type} else BlogType Enums :)
@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {"message" : f"Blog type: {type}"}