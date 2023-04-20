# Import libraries
from flask import Flask, render_template, request, redirect, url_for
from model import DataModel
from logic import calculate_result

app = Flask(__name__, template_folder='pages', static_url_path='/static')

# แสดงหน้าแรก
@app.route('/')
def home():
    data_list = DataModel.get_all()
    result = request.args.get('result', '')  # retrieve result from query parameter
    return render_template('home.html', data_list=data_list, result=result)

# สร้างแถว
@app.route('/create', methods=['POST'])
def create():
    pregnancies = request.form['pregnancies']
    glucose = request.form['glucose']
    skin_thickness = request.form['skin_thickness']
    BMI = request.form['BMI']
    age = request.form['age']
    result, last_insert_id = calculate_result(pregnancies, glucose, skin_thickness, BMI, age)
    return redirect(url_for('home', result=result))

if __name__ == '__main__':
    app.run(debug=True)
