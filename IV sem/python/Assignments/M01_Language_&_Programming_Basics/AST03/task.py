def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    # truncate instead of round
    avg = int(avg * 100) / 100

    # ensure at least one decimal place
    if avg == int(avg):
        avg_str = f"{avg:.1f}"
    else:
        avg_str = str(avg)

    if avg >= 40:
        status = "Pass"
    else:
        status = "fail"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))