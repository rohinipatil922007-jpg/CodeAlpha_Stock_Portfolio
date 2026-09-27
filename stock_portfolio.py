# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

print("================================")
print("   STOCK PORTFOLIO TRACKER")
print("================================")

portfolio = {}
total_investment = 0

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock} x {quantity} = ₹{investment}")

    total_investment += investment

print("--------------------------------")
print(f"Total Investment: ₹{total_investment}")
print("================================")

# Save the result to a text file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock} x {quantity} = ₹{investment}\n")

    file.write("-----------------------\n")
    file.write(f"Total Investment: ₹{total_investment}\n")

print("\n✅ Portfolio saved to portfolio.txt")