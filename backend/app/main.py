from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a Gastos Claros"}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola {nombre}"}


@app.get("/doble/{numero}")
def calcular_doble(numero: int):
    return {"doble": 2 * numero}
