# -*- coding: utf-8 -*-

"""
cerc_faux_finance
finance functions
balance - outstanding balance
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

All of these assume interest compounded at end of each month

"""
import math
debug = False


def unpaid(balance, annualInterestRate, monthlyPayment):
    ''' input a balance before payment before interest compounds at the end of
        the month, an annual interest rate in the form of 
        proportion expressed in decimal (eg 12% apr = .12), and a payment made
        during the month before the interest compounts.  Returns remaining
        balance after the payment is first deducted from the balance and then
        the balance is compounded.
        Assumes interest compounds once each month, and payment is made
        before the interest compounds.
    '''
    if debug is True:
        print('entering unpaid with balance:', balance, end='')
        print(', annualInterestRate:', annualInterestRate, 'monthlyPayment',
              monthlyPayment)
    unpaidbalance = balance - monthlyPayment
    newbalance = unpaidbalance * (1 + annualInterestRate/12)
    if debug is True: print('exit unpaid with newbalance', newbalance)
    return newbalance



def unpaidbyrate(balance, annualInterestRate, monthlyPaymentRate):
    '''
    input: a loan balance, and annualInterestRate, and minimum payment in
    terms of proportion of the balance (e.g. if you have to pay 2 dollars
    on 100 principle every year, you would enter .02).
    '''
    if debug is True:
        print('entering unpaidbyrate with balance:', balance,
              'annualInterestRate', annualInterestRate,
              'monthlyPaymentRate', monthlyPaymentRate)
    monthlyPayment = balance * monthlyPaymentRate
    unpaidamount = unpaid(balance, annualInterestRate, monthlyPayment)
    if debug is True: print('exit unpaidbyrate with unpaid:', unpaidamount)
    return unpaidamount

def oneyearminpaymentsrate(balance, annualInterestRate, monthlyPaymentRate):
    '''
    given a year of paying on a loan with starting balance, and an
    annualInterestRate compounded at the end of each month, paying the minimum
    monthly payment where that payment is specified as a monthlyPaymentRate of
    the balance, return the balance at the end of the year.
    '''
    for i in range(12):
        # if debug is True:
            # print('at oneyearminpayments begin iter', i, 'balance is', balance)
        balance = unpaidbyrate(balance, annualInterestRate, monthlyPaymentRate)
    return(round(balance, 2))



def oneyearpayx(balance, annualInterestRate, monthlyPayment):
    '''
    as oneyearminpaymentsrate, except the balance paid each month is specified
    as a constant, e.g. $240.
    '''
    if debug is True:
        print('oneyearpayx called with bal: ', balance, ', annualInterestRate',
              annualInterestRate, ', and monthlyPayment', monthlyPayment)
    
    for i in range(12):
        if debug is True:
            print('** at the start of onyearminpaymentsconstant iter', end='')
            print(i, ' balance', balance)
        balance = unpaid(balance, annualInterestRate, monthlyPayment)
    if debug is True: print('oneyearpayx about to return balance', balance)
    return balance
    


def payoffoneyearpayment(balance, annualInterestRate):
    '''
    given a balance and an annualInterestRate, compounded at the end of each
    month, find the smallest monthly
    which will pay off the balance.
    '''
    if debug is True: print('entering payoffoneyearpayment with balance', 
                             balance, 'and annualInterestRate',
                             annualInterestRate)
    guess = round(balance/11, 2)
    max = round(balance, 2)
    min = 0
    resultingbal = oneyearpayx(balance, annualInterestRate, guess)
    onelesscent = oneyearpayx(balance, annualInterestRate, guess - .01)
    while not (resultingbal < 0 and onelesscent > 0): 
        if debug is True:
            print('entering while loop with guess', guess, ', resultingbal',
                   resultingbal,
                  ', and onelessdolla', onelessdolla)
            print('max', max, ' min', min)
        if resultingbal < 0:
            max = guess
            guess = round((guess + min) / 2, 2)
        if resultingbal > 0:
            min = guess
            guess = round((guess + max) / 2, 2)
        resultingbal = oneyearpayx(balance, annualInterestRate, guess)
        onelesscent = oneyearpayx(balance, annualInterestRate, guess-.01)
    return guess    

balance = 320000
annualInterestRate = 0.2   
ans = payoffoneyearpayment(balance, annualInterestRate)
print('Lowest Payement:',
       payoffoneyearpayment(balance, annualInterestRate))
      
# print('balance', balance, ', annualInterestRate', annualInterestRate)
print('result of payment ', ans, oneyearpayx(balance, annualInterestRate, ans))
print('result of payment ', ans - .01, oneyearpayx(balance, annualInterestRate, ans-.01))        


