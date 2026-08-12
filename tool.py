import time
import random
def timer(chinese):
    if chinese==True:
        print("歡迎")
        print("按Enter開始")
        number=input("輸入你要計時的秒數：")
        for i in range(int(number)):
            print(i+1)
            time.sleep(1)
        print("完成")
    else:
        print("Hello")
        print("Use enter start")
        number=input("Enter the number of seconds to time:")
        for i in range(int(number)):
            print(i+1)
            time.sleep(1)
        print("Done")
def game(chinese):
    if chinese==True:
        print("歡迎")
        print("按Enter開始")
        answer="0"
        player_enter="0"
        while True:
            player_enter=input("猜一個1至10數字（輸入out離開）:")
            answer=random.randint(1,10)
            if player_enter=="out":
                break
            if answer==int(player_enter):
                print("恭喜你猜對了")
                break
            else:
                print("再試一次")
    else:
        print("Wecome")
        print("Use enter start")
        answer="0"
        player_enter="0"
        while True:
            player_enter=input("Guess a number between 1 and 10 (enter 'out' to quit):")
            answer=random.randint(1,10)
            if player_enter=="out":
                break
            if answer==int(player_enter):
                print("Congratulations, you guessed correctly")
            else:
                print("Try again")