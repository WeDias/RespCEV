from time import sleep
print('\033[1;34mContagem Regressiva\033[m')
contador = 0
for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print('\033[1;34mBOOM!\033[m')
