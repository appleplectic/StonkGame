#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# main.py

"""main.py"""

#from pynput import keyboard

class Stock:
    '''Stock class.'''
    def __init__(self, name: str, symbol: str, price: int, industry: str, per: str, cap: int, volume: int) -> None:
        self.name = name
        self.price = price
        self.industry = industry
        self.symbol = symbol
        self.per = per
        self.cap = cap
        self.volume = volume

    def __str__(self) -> str:
        return str(self.name, "(" + self.symbol + ") $" + self.price)

if __name__ == "__main__":
    print("Hello World!")
