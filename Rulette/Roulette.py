from random import randint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Roulette:
    numbers = range(0, 37)
    reds = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
    blacks = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]


''' Netinka, nes užsifiksuoja ties ta pačia spalva, reikės paaiškinimo'''
# class Throw:
#     number = randint(0, 37)
#     color = ''
#     if number in Roulette.reds:
#         color = 'red'
#     elif number in Roulette.blacks:
#         color = 'black'
#     else:
#         color = 'green'

def get_color():
    number = randint(0, 37)
    if number in Roulette.reds:
        return 'red'
    elif number in Roulette.blacks:
        return 'black'
    else:
        return 'green'

class Bet:
    def __init__(self, bank, bet, color):
        self.bank = bank
        self.bet = bet
        self.color = color

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, new_bank):
        if new_bank > 0:
            self._bank = new_bank
        else:
            self._bank = 0
            print("Bank can't be negative")

    def play(self):
        bet_ammount = int(input("How much do you bet?: "))
        if bet_ammount < self.bank:
            color = input("Choose a color: ")
            # throw_result = Throw.color
            throw_result = get_color()
            if throw_result == color:
                self.bank += bet_ammount
                print('won')
            else:
                self.bank -= bet_ammount
                print('lost')
        else:
            print("Need more money or can't bet negative")


class Autobet:
    def __init__(self, bank, bet, color, max_bets):
        self._starting_bank = bank
        self._starting_bet = bet
        self.bank = bank
        self.bet = bet
        self.color = color
        self.max_bets = max_bets

    @property
    def starting_bank(self):
        return self._starting_bank

    @property
    def starting_bet(self):
        return self._starting_bet

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, new_bank):
        if new_bank > 0:
            self._bank = new_bank
        else:
            self._bank = 0
            print("Bank can't be negative")

    def play(self):
        times_played = 0
        while True:
            if times_played < self.max_bets:
                bet_ammount = self.bet
                if bet_ammount < self.bank:
                    color = self.color
                    throw_result = get_color()
                    if throw_result == color:
                        self.bank += bet_ammount
                        print('won')
                        self.bet = self.starting_bet
                        times_played += 1
                    else:
                        self.bank -= bet_ammount
                        self.bet += bet_ammount
                        print('lost')
                        print('Double or nothing!')
                        times_played += 1
                else:
                    print("Money is gone")
                    break
            else:
                print(f'Done playing. You have: {self.bank}')
                break


# bet1 = Bet(1000, 10, 'red')
#
# print(bet1._bank)

# while True:
#     bet1.play()
#     print(bet1.bank)

# autobet1 = Autobet(10000, 10, 'red', 10)
#
# autobet1.play()

def bet_tester(min, max, repeats, bank, bet_size):
    dict_of_finals = {}
    for trial_num in range(min, max+1):
        list_of_finals = []
        for i in range(repeats):
            autobet = Autobet(bank, bet_size, 'red', trial_num)
            autobet.play()
            list_of_finals.append(autobet.bank)
        dict_of_finals[trial_num] = list_of_finals
    analysis_dict = {}

    for key in dict_of_finals:
        average = sum(dict_of_finals[key]) / len(dict_of_finals[key])
        print(f'Maximum number of plays {key}, Average sum after {len(dict_of_finals[key])} separate trials: {average}')
        analysis_dict[key] = average

    dataframe = pd.DataFrame.from_dict(dict_of_finals)
    print(dataframe.shape)

    plt.bar(analysis_dict.keys(), analysis_dict.values(), color='g')
    plt.show()

bet_tester(1,100,1000, 100, 10)
