#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    gl = set("aeyuioаеёиоуыэюя")

    s = input("Введите строку:\n").lower()

    x = sum(i in gl for i in s)
    print(f"Кол-во гласных в строке: {x}")
