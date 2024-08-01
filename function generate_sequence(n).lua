from time import sleep

palabra = 'hello world'
j = 0
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
txt = ''

while True:
    for i in range(len(abc)):
        print(txt + abc[i])
        if abc[i] == palabra[j]:
            txt += abc[i]
            break
        sleep(0.02)
    if txt == palabra:
        break
    j += 1