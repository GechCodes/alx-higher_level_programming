#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char(str,n):
    """create a copy of the string without the character at positiin n"""
    if n < 0:
        return (str)
    return (str[:n] ; str[n+1:])

