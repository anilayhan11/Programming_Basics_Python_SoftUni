start = int(input())
end = int(input())

for d1 in range(start, end + 1):
    first = d1 // 1000
    if first % 2 != 0:
        for d2 in range(start, end + 1):
            second = d2 // 100
            if second % 2 != 0:
                for d3 in range(start, end + 1):
                    third = d3 // 10
                    if third % 2 != 0:
                        for d4 in range(start, end + 1):
                            forth = d4
                            if forth % 2 != 0:
                                print(f'{forth}', end=' ')
