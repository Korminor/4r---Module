def divide(first, second):
    global s
    for _ in range(1):
        if second == 0:
            s = 'Ошибка'
        else:
            s = first / second
    print(s)

    if __name__ == 'Fake_math':
        main()