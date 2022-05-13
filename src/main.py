import sanic
import dominate
from dominate.tags import *

app = sanic.Sanic("TestApp")
app.config.FORWARED_SECRET = "CookiesAreGreat"

@app.get("/")
async def frontpage(request):
    doc = dominate.document(title='Velkommen')

    with doc.head:
        link(rel="stylesheet", href="style.css")

    with doc:
        h1("Hello, world!")

    return sanic.response.html(doc.render())

if __name__ == "__main__":
    app.run('localhost', 8080)
