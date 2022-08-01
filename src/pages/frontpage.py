import dominate
from dominate.tags import *

def show_frontpage():
    doc = dominate.document(title='Velkommen')

    with doc.head:
        link(rel="stylesheet", href="style.css")

    with doc:
        with div(cls="contents"):
            with div(cls="header"):
                h1("Programmering")
                h2("H.C. Ørsted Gymnasium, Frederiksberg")
            with div(cls="body"):
                p("Velkommen til hjemmesiden for programmeringsklasserne på H.C. Ørsted Gymnasium, Frederiksberg.")

                h3("Nyttige links")
                with div(cls="two-col"):
                    with ul(cls="link-lst"):
                        with li():
                            a("Python", href="https://www.python.org/")
                            p("Her kan man downloade den nyeste version af Python.")
                        with li():
                            a("Object-Oriented Programming in Python", href="https://python-textbok.readthedocs.io/en/1.0/index.html")
                            p("Bog om Python-programmering på engelsk.")
                        with li():
                            a("Sanic dokumentation", href="https://sanic.dev/en/guide/getting-started.html")
                            p("Sanic er et web-framework til Python, som vi bruger i programmeringstimerne når vi arbejder med web-udvikling. På ovenstående link finder du den officielle dokumentation.")
                        with li():
                            a("Dear PyGui dokumentation", href="https://dearpygui.readthedocs.io/en/latest/")
                            p("Dear PyGui er et moderne GUI-framework til Python, som vi bruger når vi gerne vil lave desktop-programmer.")
                        with li():
                            a("Dominate", href="https://github.com/Knio/dominate")
                            p("Dominate er et Python-bibliotek, som gør det nemt at konstruere HTML-sider. På ovenstående link findes dokumentation og eksempler.")
                        with li():
                            a("SQLite3 til Python", href="https://docs.python.org/3/library/sqlite3.html")
                            p("SQLite3 er et simpelt fil-baseret database-bibliotek. Når man installerer Python, får man automatisk et Python-bibliotek til SQLite3 med. På ovenstående link findes dokumentation og eksempler.")
                        with li():
                            a("MDN Web Docs", href="https://developer.mozilla.org/en-US/")
                            p("Mozilla Foundation har lavet nogle virkelig gode sider med dokumentation og tutorials for alt hvad der har med HTML, CSS, og JavaScript at gøre. Dem finder du på ovenstående link.")
                        with li():
                            a("jsfiddle", href="https://jsfiddle.net/")
                            p("På jsfiddle kan man hurtigt og nemt eksperimentere med HTML, CSS, og JavaScript. Nyttigt til at undersøge hvordan man får et lille element på sin hjemmeside til at se rigtigt ud, inden man integrerer det i resten af koden.")

                h3("Elevsider")
                p("Her vil man senere kunne finde links til hjemmesider, som eleverne har lavet.")

    return doc.render()
