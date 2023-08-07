import sanic
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=False)

app = sanic.Sanic("ProgrammingWebsite")

@app.get("/")
async def frontpage(request):
    template = env.get_template("index.html")
    return sanic.response.html(template.render())

