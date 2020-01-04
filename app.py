from model import InputForm
from flask import Flask, render_template, request
from compute import compute

template_name = 'view0.html'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        bedrooms = float(form.bedrooms.data)
        sqft_living = float(form.sqft_living.data)
        waterfront = float(form.waterfront.data)
        view = float(form.view.data)
        grade=float(form.grade.data)
        yob = float(form.yob.data)
        zipcode = form.zipcode.data


        result, df = compute(bedrooms, sqft_living,  waterfront,
                         view,  grade,  yob , zipcode)

        return render_template(template_name,
                           form=form, df = df , result='$'+str(int(result)))

    else:
        result = None
        df = None
        return render_template(template_name,
                           form=form, df = df , result=result)

if __name__ == '__main__':
    app.run()
