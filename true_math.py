from math import inf

def divide(first, second):
    global s
    for _ in range(1):
        if second == 0:
            s = inf
        else:
            s = first / second
    print(s)

    if __name__ == 'True_math':
        main()

