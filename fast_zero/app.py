from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse, status_code=HTTPStatus.OK)
def ola_mundo_html():
    return """
    <html>
        <head>
            <title>Olá Mundo!</title>
            <body>
                <h1>Olá, Mundo!</h1>
            </body>
        </head>
    </html>
        """
