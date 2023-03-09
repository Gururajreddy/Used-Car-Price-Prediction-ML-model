from flask import Flask,render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('clean_cars.csv')

@app.route('/')
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique(),reverse = True)
    fuel_type = df['fuel_type'].unique()
    return render_template('index.html',companies = companies, car_models = car_models, years = year,fule_types= fuel_type)


@app.route('/predict',methods = ['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kiol_driven'))
    print(comapny,car_model,year,fuel_type,kms_driven)
    return ""


if __name__ == "__main__":
    app.run(debug=True)