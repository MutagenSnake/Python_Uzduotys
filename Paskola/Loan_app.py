from tabulate import tabulate
from abc import ABC, abstractmethod
import pickle
import csv

class Loan:
    def __init__(self, loan_sum: int, term: int, interest: float):
        self.loan_sum = loan_sum
        self.term = term
        self.interest = interest

    def interest_calculator(self) -> float:
        total_interest = 0
        total = self.loan_sum
        monthly = self.loan_sum/(self.term * 12)
        while total > 0:
            total_interest += total * self.interest
            total = total - monthly
        return total_interest

    def __str__(self):
        return f'Paskolos dydis: {self.loan_sum}\n' \
               f'Terminas: {self.term} metai\n' \
               f'Palūkanų norma: {self.interest}\n' \
               f'Mokėtinos palūkanos: {Loan.interest_calculator(self)}\n' \
               f'Bendra mokėtina suma: {self.loan_sum + Loan.interest_calculator(self)}'

    def payment_graph(self):
        term_months = self.term * 12
        monthly_payment = self.loan_sum / term_months
        loan_sum_left = self.loan_sum
        index = 0
        list_for_print = [['Month', 'Monthly Payment', 'Loan left', 'Interest', 'Full Payment']]

        while loan_sum_left > 0:
            interest = loan_sum_left * self.interest
            full_payment = monthly_payment + interest
            index += 1
            list_to_add = [index, monthly_payment, loan_sum_left, interest, full_payment]
            list_for_print.append(list_to_add)
            loan_sum_left -= monthly_payment

        csv_file_name = str(input('Name a csv file: '))

        with open(f'{csv_file_name}.csv', 'w') as f:
            writer = csv.writer(f)
            for line in list_for_print:
                writer.writerow(line)

        print(tabulate(list_for_print, headers="firstrow"))

class ILoanInterface(ABC):

    @abstractmethod
    def get_loan(self) -> Loan:
        pass

    @abstractmethod
    def give_loan_info(self, loan: Loan):
        pass

    @abstractmethod
    def give_graph(self, loan: Loan):
        pass

class ConsoleLoanInterface(ILoanInterface):

    def get_loan(self) -> Loan:
        loan_sum = int(input("Paskolos suma: "))
        if loan_sum <= 0:
            raise ValueError('Paskolos suma turi būti didesnė nei nulis!')
        interest = float(input("Mėnesinė palūkanų norma: "))
        term = int(input("Paskolos terminas (metai): "))

        return Loan(loan_sum, term, interest)

    def give_loan_info(self, loan: Loan):
        print(loan)

    def give_graph(self, loan: Loan):
        print(loan.payment_graph())

class FileLoanInterface(ILoanInterface):
    def get_loan(self) -> Loan:
        # Take from file
        raise NotImplementedError

    def give_loan_info(self, loan: Loan):
        # Whrite to a file
        raise NotImplementedError

def main():
    while True:
        with open('loans.pkl', 'rb') as file:
            try:
                loans = pickle.load(file)
            except Exception:
                print(Exception)
        choice = int(input('Enter new loan: 1\nPick a loan from a list: 2\nGet info of all loans: 3\nQuit the program: 9\n'))
        if choice == 1:
            interface = ConsoleLoanInterface()
            loan = interface.get_loan()
            interface.give_loan_info(loan)
            loans.append(loan)
            with open('loans.pkl', 'wb') as file:
                pickle.dump(loans, file)
        elif choice == 2:
            index = 0
            list_for_print = [['Index', 'Sum', 'Term', 'Interest']]
            for loan in loans:
                index += 1
                list_to_add = [index, loan.loan_sum, loan.term, loan.interest]
                list_for_print.append(list_to_add)
            print(tabulate(list_for_print, headers="firstrow"))
            list_index = int(input('Choose loan index: '))
            true_index = list_index - 1
            choice_2 = int(input('Get info: 1\nGet table: 2\nModify data: 3\n'))
            if choice_2 == 1:
                print(loans[true_index])
            elif choice_2 == 2:
                loans[true_index].payment_graph()
            elif choice_2 == 3:
                loans[true_index].loan_sum = int(input(f'Change sum from {loans[true_index].loan_sum} to :'))
                loans[true_index].term = int(input(f'Change term from {loans[true_index].term} to :'))
                loans[true_index].interest = float(input(f'Change interest from {loans[true_index].interest} to :'))
            with open('loans.pkl', 'wb') as file:
                pickle.dump(loans, file)
        elif choice == 9:
            break

if __name__ == '__main__':
    main()



# paskola = Loan(10000, 10, 0.002)
#
# print(paskola.payment_graph())