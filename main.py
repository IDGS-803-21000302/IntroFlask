from flask import Flask, render_template, request, flash, Response

from flask_wtf.csrf import CSRFProtect
from flask import redirect

from flask import g

import forms

app = Flask(__name__)
app.secret_key='esta es la clave secreta'

@app.errorhandler(404)
def page_not_fund(e):
    return render_template('404.html'),404

#---------------------------
@app.before_request
def before_request():
    
    g.nombre='hola'
    # print('before_request')

#--------------------------
@app.after_request
def after_request(response):
    print('after_request')
    if 'Daniel' not in g.nombre and request.endpoint not in['/index']:
        return redirect('/index')
    return response

#--------------------------

@app.route("/index")
def index():
    g.nombre='Daniel'
    escuela="UTL!!!"
    alumnos=["mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    print('dentro de alumnos')
    print('hola {}'.format(g.nombre))
    nom=''
    apa=''
    ama=''
    mensaje=''
    alum_form= forms.UsersForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

        print("Nombre: {}".format(nom))
        print("Apa: {}".format(apa))
        print("Ama: {}".format(ama))
        
    return render_template("alumnos.html",form=alum_form,nom=nom,apa=apa,ama=ama)

@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde Hola !!  <br> Mundo</h1>"

@app.route("/user/<string:name>")
def  user(name):
    return "<h1> Hola "+ name

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {} Nombre: {}".format(id,name)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
    return "El valor de {} + {} = {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default<string:ab>")
def func1(ab="UTL"):
    return "El valor es " +ab


@app.route("/multiplicar",methods=["GET","POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2") 
        return "<h1>La multiplicacion es: {}<h1> ".format(str(int(num1)*int(num2)))
    else:
        return '''
                <form action="/multiplicar" method="POST">
                    <label>N1:</label>
                    <input type="text" name="n1"/><br>
                    <label>N2:</label>
                    <input type="text" name="n2"/><br>
                    <input type="submit"/>
                    
                </form>
            '''
    
@app.route("/formulario1")
def formulario1():
    return render_template("formulario1.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")


@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2") 
        return "<h1>La multiplicacion es: {}<h1> ".format(str(int(num1)*int(num2)))

if __name__== "__main__":
    app.run(debug=True)