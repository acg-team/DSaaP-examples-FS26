def discounted_price(price: float, percentage: float) -> float:
    return price - price * percentage / 100

if __name__ == "__main__":
    print(discounted_price(100, 200))