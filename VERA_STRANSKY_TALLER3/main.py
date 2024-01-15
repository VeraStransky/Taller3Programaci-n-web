from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/formulariodenotas', methods=['GET', 'POST'])
def formularioDenotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular Promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Condiciones de Aprobación o Reprobación

        if 40<= promedio <=70 and asistencia >= 75:
            estado = 'APROBADO'
        elif promedio > 70:
            estado = 'ERROR: Nota superior a 70'
        else:
            estado = 'REPROBADO'


        # Definir la variable resultado

        resultado = True

        return render_template('formulariodenotas.html', promedio=promedio, estado=estado, resultado=resultado)

    return render_template('formulariodenotas.html')


@app.route('/formulariodenombres', methods=['GET', 'POST'])
def formularioDenombres():
    if request.method == 'POST':
        # Obtener nombres
        resultado = ''
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        # Comparar Longitud de nombres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_grande = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_grande)

        return render_template('formulariodenombres.html', nombre_mas_grande=nombre_mas_grande,
                               cantidad_caracteres=cantidad_caracteres)

    return render_template('formulariodenombres.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
