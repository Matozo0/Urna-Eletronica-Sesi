from flask import request, render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required

from app import app, login_manager
from app.modelos import Urna, Mesario

@app.route('/', methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        urna = Urna.query.filter_by(login=login).first()
        mesario = Mesario.query.filter_by(login=login).first()

        if urna and urna.verificar_senha(senha):
            login_user(urna)
            return redirect(url_for('index'))        
        
        if mesario and mesario.verificar_senha(senha):
            login_user(mesario)
            return redirect(url_for('mesario'))
        
        if (not mesario or not mesario.verificar_senha(senha)) and (not urna or not urna.verificar_senha(senha)):
            return redirect(url_for('login'))        

    return render_template('login.html')

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/mesario')
@login_required
def mesario():
    return render_template('mesario.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')