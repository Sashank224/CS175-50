print("Hi Joe Welcome to the Stock Program")

COMMISSION_RATE = float(input("How much commission rate before the sale\n"))

sellingCommission= float(input("How much commission rate after the sale\n"))

NUM_SHARES= float(input("How many stocks were bought\n"))

stockSoldFor = float(input("How many stocks were sold\n"))


PURCHASE_PRICE  = float(input("Whats the stock's price per share?\n"))

SELLING_PRICE  = float(input("How whats the stock's price after sale\n"))

amountPaidForStock =(NUM_SHARES*PURCHASE_PRICE)
print("total amount paid : $", amountPaidForStock)

purchaseCommission = (COMMISSION_RATE*amountPaidForStock)
print(" Commission Paid:  $", purchaseCommission)

totalPaid = (amountPaidForStock + purchaseCommission)

stockSoldFor = (NUM_SHARES*SELLING_PRICE)
print("Amount the stock sold for $", stockSoldFor)

sellingCommission = (COMMISSION_RATE*stockSoldFor)
print("the commission paid on sale $", sellingCommission)

totalReceived = (stockSoldFor - sellingCommission)

profit = (totalReceived-totalPaid)
print("The profit is \n $", profit)

