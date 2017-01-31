def taxation(purchaseAmount):
    countyTax = purchaseAmount * .025
    stateTax = purchaseAmount * .05
    totalTax = countyTax + stateTax
    return countyTax, stateTax, totalTax
