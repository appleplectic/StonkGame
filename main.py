#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# main.py

"""main.py"""

#from pynput import keyboard

class Stock():
    def __init__(self, name, symbol, price, industry, per, cap, volume):
        self.name = name
        self.price = price
        self.industry = industry
        self.symbol = symbol
        self.per = per
        self.cap = cap
        self.volume = volume
    def __str__(self):
        return f"{self.name} ({self.symbol}) ${self.price}"

if __name__ == "__main__":
    stock = Stock("Banana Inc.", "BAN", 135.98, "Technology", 29.04, 2280000000000, 94369347)
    print(stock)