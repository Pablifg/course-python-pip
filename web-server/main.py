import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # Crear instancia

@app.get("/") #Ruta por la cual desde la web podrá ingresar
def get_list():
    return [1,2,3]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
        <h1>I'm a page</h1>
        <p>I'm a paragraph</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()