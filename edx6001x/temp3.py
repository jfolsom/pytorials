debug = False
balance = 42
annualInterestRate = .2
monthlyPaymentRate = .04
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

def paymentbyrate(balance, monthlyPaymentRate):
    if debug is True:
        print('entering paymentbyrate with balance:', balance,
               'monthlyPaymentRate:', monthlyPaymentRate)
    payment = balance * monthlyPaymentRate
    if debug is True: print('exit paymentbyrate with payment', payment)
    return payment

def unpaidbyrate(balance, annualInterestRate, monthlyPaymentRate):
    if debug is True:
        print('entering unpaidbyrate with balance:', balance,
              'annualInterestRate', annualInterestRate,
              'monthlyPaymentRate', monthlyPaymentRate)
    monthlyPayment = paymentbyrate(balance, monthlyPaymentRate)
    unpaidamount = unpaid(balance, annualInterestRate, monthlyPayment)
    if debug is True: print('exit unpaidbyrate with unpaid:', unpaidamount)
    return unpaidamount

def oneyearminpayments(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        if debug is True:
            print('\n')
            print('******at begin iter', i, 'balance is', balance)
        balance = unpaidbyrate(balance, annualInterestRate, monthlyPaymentRate)
    return(round(balance, 2))

print('Remaining balance: ', oneyearminpayments(balance,annualInterestRate,monthlyPaymentRate))