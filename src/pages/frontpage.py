import dominate
from dominate.tags import *

def show_frontpage():
    doc = dominate.document(title='Velkommen')

    with doc.head:
        link(rel="stylesheet", href="style.css")

    with doc:
        with div(cls="contents"):
            with div(cls="header"):
                h1("Programmering B")
                h2("H.C. Ørsted Gymnasium, Frederiksberg")
            with div(cls="body"):
                p("Velkommen til hjemmesiden for programmeringsklasserne på H.C. Ørsted Gymnasium, Frederiksberg.")

    return doc.render()
