import sanic
import sys

from pages.frontpage import show_frontpage

log_config = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'incremental' : False,
    'formatters' : {
        'simple': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'access': {
            'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: ' +
                    '%(request)s %(message)s %(status)d %(byte)d',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters' : {},
    'handlers' : {
        'consoleHandlerAccess' : {
            'class': 'logging.StreamHandler',
            'formatter': 'access',
            'stream': sys.stdout
        },
        'fileHandler' : {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter' : 'simple',
            'filename' : 'log.out',
            'when' : 'midnight',
            'backupCount' : 3
        }
    },
    'loggers' : {
        'sanic.root' : {
            'level' : 'INFO',
            'handlers' : ['fileHandler']
        },
        'sanic.access' : {
            'level' : 'INFO',
            'handlers' : ['consoleHandlerAccess']
        },
        'sanic.error' : {
            'level' : 'INFO',
            'handlers' : ['fileHandler']
        }
    }
}

app = sanic.Sanic("TestApp", log_config=log_config)
app.config.FORWARED_SECRET = "CookiesAreGreat"

@app.get("/")
async def frontpage(request):
    return sanic.response.html(show_frontpage())

if __name__ == "__main__":
    app.run('localhost', 8080, access_log=False)

