from flask import Flask, render_template, request, redirect
import csv
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Loan(db.Model):
    __tablename__ = 'Loans'
    id = db.Column(db.Integer, primary_key = True)
    lsum = db.Column(db.Integer)
    term = db.Column(db.Integer)
    interest = db.Column(db.Float)

    def __init__(self, lsum, term, interest):
        self.lsum = lsum
        self.term = term
        self.interest = interest

    def __repr__(self):
        return f'{self.lsum}, {self.term}, {self.interest}'

db.create_all()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        loan_sum = request.form['lsum']
        loan_term = request.form['term']
        loan_interest = request.form['interest']
        new_loan = Loan(lsum=loan_sum, term=loan_term, interest=loan_interest)
        try:
            db.session.add(new_loan)
            db.session.commit()
            return redirect('/')
        except:
            return 'no work, no add loan'
    else:
        loans = Loan.query.order_by(Loan.id).all()
        return render_template('home.html', loans=loans)

@app.route('/delete/<int:id>')
def delete(id):
    loan_to_delete = Loan.query.get_or_404(id)
    try:
        db.session.delete(loan_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as exp:
        return exp

@app.route('/table/<int:id>')
def table(id):
    loan = Loan.query.get(id)
    term_months = loan.term * 12
    monthly_payment = loan.lsum / term_months
    loan_sum_left = loan.lsum
    index = 0
    list_for_print = [['Month', 'Monthly Payment', 'Loan left', 'Interest', 'Full Payment']]

    while loan_sum_left > 0:
        interest = loan_sum_left * loan.interest
        full_payment = monthly_payment + interest
        index += 1
        list_to_add = [index, monthly_payment, loan_sum_left, interest, full_payment]
        list_for_print.append(list_to_add)
        loan_sum_left -= monthly_payment

    csv_file_name = f'loan_{loan.id}'

    with open(f'{csv_file_name}.csv', 'w') as f:
        writer = csv.writer(f)
        for line in list_for_print:
            writer.writerow(line)

    data = pd.read_csv(f'loan_{loan.id}.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    loan = Loan.query.get_or_404(id)

    if request.method == 'POST':
        loan.lsum = request.form['lsum']
        loan.term = request.form['term']
        loan.interest = request.form['interest']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your loan'
    else:
        return render_template('update.html', loan=loan)

@app.route('/plot/<int:id>', methods=['GET', 'POST'])
def plot(id):
    loan = Loan.query.get(id)
    term_months = loan.term * 12
    monthly_payment = loan.lsum / term_months
    loan_sum_left = loan.lsum
    index = 0
    list_for_print = [['Month', 'Monthly Payment', 'Loan left', 'Interest', 'Full Payment']]

    while loan_sum_left > 0:
        interest = loan_sum_left * loan.interest
        full_payment = monthly_payment + interest
        index += 1
        list_to_add = [index, monthly_payment, loan_sum_left, interest, full_payment]
        list_for_print.append(list_to_add)
        loan_sum_left -= monthly_payment

    csv_file_name = f'loan_{loan.id}'

    with open(f'{csv_file_name}.csv', 'w') as f:
        writer = csv.writer(f)
        for line in list_for_print:
            writer.writerow(line)

    data = pd.read_csv(f'loan_{loan.id}.csv')
    sns.lineplot(data=data, x='Month', y='Full Payment')
    plt.savefig(f'loan_{loan.id}.png')
    return render_template('plot.html', image=f'loan_{loan.id}.png')

if __name__ == "__main__":
    app.run(debug=True)