#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "b", "f", "g", "i"}
    b = {"c", "f", "g", "i", "s", "v"}
    c = {"a", "g", "h", "i"}
    d = {"f", "w", "x"}

    an = u - a
    bn = u - b

    x = (a & b) | c
    print(f"x = {x}")

    y = (a & bn) | (c - d)
    print(f"y = {y}")