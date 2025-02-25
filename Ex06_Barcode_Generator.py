start = int(input())
end = int(input())

for i in range(a, e + 1):
    for j in range(b, f + 1):
        for k in range(c, g + 1):
            for l in range(d, h + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")