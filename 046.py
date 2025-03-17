from time import sleep

import emoji


for i in range(10, 0, -1):
    sleep(1)
    print(i)
sleep(1)
print(emoji.emojize('\U0001f31f'))