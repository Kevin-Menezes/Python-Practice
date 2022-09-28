import justpy as jp

def app():
    wp = jp.QuasarPage() # Creating main page...Quasar is a framework from JS

    h1 = jp.QDiv(a=wp,text="Analysis of Course Reviews", classes="text-h2 text-center q-pa-md")
    p1 = jp.QDiv(a=wp,text="These graphs represent course review analysis")
    return wp

jp.justpy(app) # Calling the function
