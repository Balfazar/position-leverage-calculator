import random
from decimal import Decimal, getcontext

def simulate_trades(winrate, starting_balance, risk_per_trade, risk_to_reward_ratio, num_trades):
    account_balance = Decimal(str(starting_balance))
    risk_per_trade_percentage = Decimal(str(risk_per_trade)) / Decimal('100')
    risk_to_reward_ratio = max(Decimal('1.0'), Decimal(str(risk_to_reward_ratio)))

    for _ in range(num_trades):
        if random.uniform(0, 1) < winrate:
            # Win
            risk_amount = account_balance * risk_per_trade_percentage
            reward_amount = risk_amount * risk_to_reward_ratio
            account_balance += reward_amount - risk_amount
        else:
            # Loss
            risk_amount = account_balance * risk_per_trade_percentage
            account_balance -= risk_amount

    return account_balance

def main():
    # Set precision for Decimal
    getcontext().prec = 28

    # Parameters
    winrate = Decimal('0.75')  # 75% winrate
    starting_balance = Decimal('2000')
    risk_per_trade = Decimal('20')  # 20% risk per trade
    risk_to_reward_ratio = Decimal('1.5')  # Risk to reward ratio
    num_trades = 100  # Number of trades to simulate

    # Simulate trades
    final_balance = simulate_trades(winrate, starting_balance, risk_per_trade, risk_to_reward_ratio, num_trades)

    # Display results
    print(f"Initial Balance: ${starting_balance}")
    print(f"Final Balance: ${str(final_balance)}")
    print(f"Profit/Loss: ${str(final_balance - starting_balance)}")

if __name__ == "__main__":
    main()
