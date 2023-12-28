
def get_position_size(balance, position_risk):
    account_risk = 0.20
    position_risk = position_risk / 100
    return balance * account_risk / position_risk
     
def get_leverage(position_size, balance):
    return position_size / balance

try:
    balance = float(input("Balance($): "))
    position_risk = float(input("Risk(%): "))
except ValueError:
    print("Enter a Number:")

position_size = get_position_size(balance, position_risk)
leverage = round(get_leverage(position_size, balance))

size = leverage * balance

print(f"Position Size: {size}\nLeverage: {leverage}.00x")
