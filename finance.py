#imports yfinance
# from tkinter import Y
import yfinance as yf

#grabs the data from specific stock based on stock sticker
#Apple intrinsic value calculation
# apple = yf.ticker("aapl")
# msft = yf.Ticker("aapl")
netflix = yf.Ticker('nflx')
# ourstandingshare = apple.info['sharesOutstanding'] #fetch number of shares
# ourstandingshare = apple.info
# ourstandingshares = msft.info #fetch number of shares

#gets all info from specific stock
ourStandingShares = netflix.info
# print(ourstandingshares)

# for key,value in ourstandingshares.items():
#     print(key, ":", value)
# for key,value in ourStandingShares.items():
#     print(key, ":", value)

#grabs specific info from a specific stock
# numShares = msft.info['sharesOutstanding']
numShares = netflix.info['sharesOutstanding']
moneyCashFlow = netflix.info['freeCashflow']
# print(moneyCashFlow)

# Assumptions
required_rate = 0.07
perpetual_rate = 0.02
cashflowgrowthrate = 0.03

#years that will be linked to free cashflow array
years = [1, 2, 3, 4]

freecashflow = [50803000, 64121000, 58896000, 73365000] #last 4 years in 1000s of $

futurefreecashflow = []
discountfactor = []
discountedfuturefreecashflow = []

#calculates terminal value of stock basedon free cashflow, perpetual rate and required perpetual rate
# terminalvalue = freecashflow [-1] * (1 + perpetual_rate)/(required_rate-perpetual_rate)
# print(terminalvalue)
netflixTerminalValue = moneyCashFlow * (1 + perpetual_rate)/(required_rate-perpetual_rate)


#uses a for loop to calculate future cash flow which is then appended to array
# for year in years:
#     cashflow = freecashflow[-1] *(1 + cashflowgrowthrate)**year
#     futurefreecashflow.append(cashflow)
#     discountfactor.append((1 + required_rate)**year)
cashFlow = moneyCashFlow * (1 + cashflowgrowthrate)**1
futurefreecashflow.append(cashFlow)
discountfactor.append((1 + required_rate)**1)



# print(discountfactor)
# print(futurefreecashflow)

#calculates the discounted future cash flow and appends it to the array
# for i in range(0, len(years)):
#     discountedfuturefreecashflow.append(futurefreecashflow[i]/discountfactor[i])
calcResult = (futurefreecashflow[0] / discountfactor[0])
discountedfuturefreecashflow.append(calcResult)



# print(discountedfuturefreecashflow)

#calculates discounted terminaal value based on required rate and terminal value
#it is then appended to the discounted future cash flow array

# discountedterminalevalue = terminalvalue/(1 + required_rate)**4
# discountedfuturefreecashflow.append(discountedterminalevalue)
discountedTerminalValue = netflixTerminalValue/(1 + required_rate)**1
discountedfuturefreecashflow.append(discountedTerminalValue)

#calculates current value based on sum of discoutned future cash flow 
# todaysvalue = sum(discountedfuturefreecashflow)
netflixCurrentValue = sum(discountedfuturefreecashflow)

#calculates stock's fair value based on stock's current value*1000 divided by number of shares
#it is then printed to output fair value price of a specific stock
netflixFairValue = netflixCurrentValue*1000/numShares
print("The fair value of AAPL is ${}".format(round(netflixFairValue, 2)))

# fairvalue = todaysvalue*1000/numShares

#print("The fair value of AAPL is ${}".format(round(fairvalue, 2)))