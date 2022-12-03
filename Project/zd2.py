#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    print("Введите две строки:\n")

    x = set(input())
    y = set(input())

    r = x.intersection(y)
    print(f"Общие символы: {r}")
