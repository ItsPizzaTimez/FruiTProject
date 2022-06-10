from time import sleep
timer = 0
check = True
while check:
    timer += 1
    sleep(300)
    print("test : {}".format(timer))