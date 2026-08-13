import time
import random
def timer(chinese):
    try:
        if chinese==True:
            print("歡迎")
            input("按Enter開始")
            number=input("輸入你要計時的秒數（輸入out離開）：")
            if number=="out":
                return
            for i in range(int(number)):
                print(i+1)
                time.sleep(1)
            print("完成")
        else:
            print("Hello")
            input("Use enter start")
            number=input("Enter the number of seconds to time(enter 'out'to quit):")
            if number=="out":
                return
            for i in range(int(number)):
                print(i+1)
                time.sleep(1)
            print("Done")
    except ValueError:
        print(f"Not find {number}")
def game(chinese):
    try:
        if chinese==True:
            print("歡迎")
            input("按Enter開始")
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
            input("Use enter start")
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
    except ValueError:
        print(f"Not find {player_enter}")