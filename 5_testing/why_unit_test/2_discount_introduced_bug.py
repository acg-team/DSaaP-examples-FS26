def discounted_price(price: float, percentage: float) -> float:
    return price - percentage

if __name__ == "__main__":
    print(discounted_price(100, 20)) # expected output: 80.0

    print(discounted_price(200, 20)) # expected output: 160.0, but will print 180.0 due to the bug in the discount function