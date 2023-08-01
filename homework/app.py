from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    email = request.form['email']

    # Создаем cookie с данными пользователя
    response = make_response(redirect('/welcome'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)

    return response

@app.route('/welcome')
def welcome():
    # Получаем данные пользователя из cookie
    name = request.cookies.get('user_name')
    email = request.cookies.get('user_email')

    if name and email:
        return render_template('welcome.html', name=name, email=email)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    # Удаляем cookie с данными пользователя
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')

    return response

if __name__ == '__main__':
    app.run(debug=True)
