from flask import Flask 
from flask import render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index(): 

    return render_template('index.html',display='',pageTital='Calulator page')

@app.route('/over',methods=["POST","GET"])
def over():
        if request.method=="POST":
            form = request.form
            Loan_amount=float(form["money"])
            payments_per_year=float(form["payments_per_year"])
            number_of_years=float(form["years"])
            annual_rate=float(form["the annual rate"])
            number_of_payment_periods=float(form["the number of payment periods"])

            N=payments_per_year*number_of_years
            I=annual_rate / number_of_payment_periods
            D=((1+I)**N-1)/(I*(1+I)**N)
            
            calc = Loan_amount/D

            estimate = "The loan payment is ${0:,.2f}".format(calc)

            return render_template('index.html', display = estimate,pageTital='Calulator page')





        return redirect("/")






if __name__ == '__main__':     
    app.run(debug=True, host='0.0.0.0')