from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/pintura', methods=['GET', 'POST'])
def formularioCompra():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        total_sin_descuento = tarros_pintura * 9000

        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0

        monto_descuento = total_sin_descuento * porcentaje_descuento

        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template('pintura.html', nombre=nombre, total_sin_descuento=total_sin_descuento, monto_descuento=monto_descuento, total_con_descuento=total_con_descuento)

    return render_template('pintura.html')

@app.route('/login', methods=['GET', 'POST'])
def formularioLogin():
    mensaje = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario == 'juan' and contraseña == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and contraseña == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('login.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
