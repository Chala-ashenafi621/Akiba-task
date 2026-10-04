# TASK 9 — Currency Exchange Desk
exchange_rate = float(input("Enter exchange rate: "))
usd_amount = float(input("Enter amount in USD: "))
etb_amount = usd_amount * exchange_rate
print("\n==============================")
print("      CURRENCY EXCHANGE")
print("==============================")

print("USD Amount:", usd_amount)
print("Exchange Rate: 1 USD =", exchange_rate, "ETB")
print("ETB Amount:", f"{etb_amount:,.2f}", "ETB")

print("==============================")