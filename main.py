from pynput import keyboard


class Stock():
    def __init__(self, name, symbol, price, industry, per, cap, volume):
        self.name = name
        self.price = price
        self.industry = industry
        self.symbol = symbol
        self.per = per
        self.cap = cap
        self.volume = volume
        return

    def __str__(self):
        return str(self.name, "(" + self.symbol + ") $" + self.price)

if __name__ == "__main__":
    print("Hello World!")
