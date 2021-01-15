# sales
sales = input("\nEnter total sales:")
print("Input data type is string = {}".format(isinstance(sales,str)))
# input validation
if not sales.isnumeric():
    raise Exception("The input entered should be numeric")
sales = float(sales)
# average price
average_price = 2100
print(average_price)
# sales usd
annual_gross_revenue = sales * average_price
print(annual_gross_revenue)
# cogs_percentage
cogs_percentage = 0.59
print(cogs_percentage)
# cogs
cogs = annual_gross_revenue * cogs_percentage
print(cogs)
#annual net revenue
annual_net_revenue = annual_gross_revenue - cogs
print(annual_net_revenue)
# quaterly net revenue
quarterly_net_revenue = annual_net_revenue / 4
print(quarterly_net_revenue)
# monthly net revenue
monthly_net_revenue = annual_net_revenue / 4
# quarterly gross revenue
quarterly_gross_revenue = annual_gross_revenue / 4
print(quarterly_gross_revenue)
# monthy groos revenue
monthly_gross_revenue = annual_gross_revenue / 12
print(monthly_gross_revenue)
# print summary
print("\n")
print("-"*30)
print("Total sales: {}".format(sales))
print("Average price: {}".format(average_price))
print("COGS %: {}".format(cogs_percentage))
print("COGS: {}".format(cogs))
print("-"*30)
print("-"*30)
print("Gross Revenue")
print("..... annual: ${:.2f}".format(annual_gross_revenue))
print(".. quarterly: ${:.2f}".format(quarterly_gross_revenue))
print(".... monthly: ${:.2f}".format(monthly_gross_revenue))
print("-"*30)
print("-"*30)
print("Net Revenue")
print("..... annual: ${:.2f}".format(annual_net_revenue))
print(".. quarterly: ${:.2f}".format(quarterly_net_revenue))
print(".... monthly: ${:.2f}".format(monthly_net_revenue))
print("-"*30)