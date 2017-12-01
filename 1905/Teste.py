f = open("labirintos_sem_espaco.txt", "r")

labirinto = []

i = 0
while i < 5:
    try:
        for x in range(5):
            labirinto.append(f.readline().split())
    except:
        break

    i += 1

print labirinto