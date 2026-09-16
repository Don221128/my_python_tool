import time
import random
def timer(language):
    try:
        if language=="chinese":
            print("歡迎")
            input("按Enter開始")
            number=int(input("輸入你要計時的秒數（輸入out離開）："))
        else:
            print("Hello")
            input("Use enter start")
            number=int(input("Enter the number of seconds to time(enter 'out'to quit):"))
        if number=="out":
            return
        for i in range(number):
            print(i+1)
            time.sleep(1)
        if language=="chinese":
            print("完成")
        else:
            print("Done")
    except ValueError:
        print(f"Not find {number}")
def game(langauge):
    player_enter=0
    answer=0
    try:
        if langauge=="chinese":
            print("歡迎")
            input("按Enter開始")
        else:
            print("Wecome")
            input("Use enter start")
        while True:
            if langauge=="chinese":
                player_enter=int(input("猜一個1至10數字（輸入out離開）"))
            else:
                player_enter=int(input("Guess a number between 1 and 10(enter'out'to quit):"))
            answer=random.randint(1,10)
            if player_enter=="out":
                break
            if answer==player_enter:
                if langauge=="chinese":
                    print("恭喜你猜對了")
                else:
                    print("Congratulations, you guessed correctly")
                break
            else:
                if langauge=="chinese":
                    print("再試一次")
                else:
                    print("Try again")
    except ValueError:
        print(f"Not find {player_enter}")
def calculator(langauge):
    numerical_value1=0
    numerical_value2=0
    operator=0
    try:
        if langauge=="chinese":
            print("歡迎")
            input("按Enter開始")
            print("1.+\n2.-\n3.*\n4./")
            operator=input("輸入編號運算：")
            numerical_value1=int(input("1."))
            numerical_value2=int(input("2."))
        else:
            print("Hello")
            input("Use enter start")
            print("1.+\n2.-\n3.*\n4./")
            operator=input("Enter ID number to calculate:")
            numerical_value1=int(input("1."))
            numerical_value2=int(input("2."))
        if operator=="1":
            print(numerical_value1+numerical_value2)
        elif operator=="2":
            print(numerical_value1-numerical_value2)
        elif operator=="3":
            print(numerical_value1*numerical_value2)
        elif operator=="4":
            print(numerical_value1/numerical_value2)
    except ValueError:
        print(f"Not find {operator}")