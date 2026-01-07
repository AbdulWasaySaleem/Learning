#Best time to buy and Sell Stock
#Prices array each index represent the price on that day
#Find the best time to buy and sell the stock example [7,1,5,3,6,4] reurn 1(since cheapest) and 5(since max profit)

def timeToBuyAndSell(prices):
  cheapest = prices[0]
  profit = 0
  
  for i in range(len(prices)):
    if prices[i]< cheapest:
      cheapest = prices[i]
    else:
      profit = max(profit, prices[i]-cheapest)
      
  print("Buy at day",cheapest, "Sell at day",profit, "to maximize profit")
  
prices = [7,1,5,3,6,4]

timeToBuyAndSell(prices)
