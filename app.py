from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/pagina1", methods=["GET", "POST"])
def pagina1():

    if request.method == "POST":

        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 4.0 and asistencia >= 75:
            resultado = "APROBADO"
        else:
            resultado = "DESAPROBADO"

        return render_template(
            "pagina1.html",
            promedio=round(promedio, 1),
            resultado=resultado
        )

    return render_template("pagina1.html")

@app.route("/pagina2", methods=["GET", "POST"])
def pagina2():

    if request.method == "POST":

        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        nombres = [nombre1, nombre2, nombre3]

        mayor = max(len(nombre1), len(nombre2), len(nombre3))

        nombres_mayores = []

        for nombre in nombres:
            if len(nombre) == mayor:
                nombres_mayores.append(nombre)

        if len(nombres_mayores) == 1:

            nombre_mayor = nombres_mayores[0]
            cantidad_caracteres = len(nombre_mayor)

            resultado = "El nombre con mayor cantidad de caracteres es: " + nombre_mayor

        else:

            nombre_mayor = ""
            cantidad_caracteres = 0

            resultado = "ERROR: Hay más de un nombre con la misma cantidad de caracteres."

        return render_template(
            "pagina2.html",
            resultado=resultado,
            nombre_mayor=nombre_mayor,
            cantidad_caracteres=cantidad_caracteres
        )

    return render_template("pagina2.html")

if __name__ == "__main__":
    app.run(debug=True)