import sanic
import sys

from pages.frontpage import show_frontpage

app = sanic.Sanic("ProgrammingWebsite")
app.config.FORWARED_SECRET = "CookiesAreGreat"

@app.get("/")
async def frontpage(request):
    return sanic.response.html(show_frontpage())

if __name__ == "__main__":
    app.run('localhost', 8080, access_log=False)

