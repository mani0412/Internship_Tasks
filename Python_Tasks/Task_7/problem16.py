# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
result = ""

    k = k % 26

    for char in s:
        if char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            result += char

    return result
