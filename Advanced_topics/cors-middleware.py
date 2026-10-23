from fastapi import FastAPI, Response, Request
#from fastapi.middleware.cors import CORSMiddleware
#from fastapi.middleware.gzip import GZipMiddleware
#from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

class testMiddleware(BaseHTTPMiddleware):
     async def dispatch(self, request: Request, call_next):
        print("Request received")

        response = await call_next(request)

        print("Response generated")

        return response

app=FastAPI()

app.add_middleware(testMiddleware)

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=[
#        'https://varunsharma.com',
#        "https://www.google.com"
#    ],
#    allow_credentials=True,
#    allow_methods=['GET','POST','PUT','DELETE'],
#    allow_headers=['*']
#)

#app.add_middleware(GZipMiddleware, 
#                    minimum_size=500,
#                    compresslevel=9)


#app.add_middleware(HTTPSRedirectMiddleware)


@app.get('/')
def hello():
    print('111')
    return {'message','hi from hellp method'}


