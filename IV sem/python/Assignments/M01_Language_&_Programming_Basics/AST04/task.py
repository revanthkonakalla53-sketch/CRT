def Reverse_String(s: str) -> str:
    result = ""
    for ch in s:
        result = ch + result
    return result


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))