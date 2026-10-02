import time
import random
import glob
import os
import decorate
def timer(language):
    try:
        if language=="chinese":
            decorate.decorate_print("歡迎")
            decorate.decorate_input("按Enter開始")
            number=int(decorate.decorate_input("輸入你要計時的秒數（輸入out離開）："))
        else:
            decorate.decorate_print("Hello")
            decorate.decorate_input("Use enter start")
            number=int(decorate.decorate_input("Enter the number of seconds to time(enter 'out'to quit):"))
        if number=="out":
            return
        for i in range(number):
            print(i+1)
            time.sleep(1)
        if language=="chinese":
            decorate.decorate_print("完成")
        else:
            decorate.decorate_print("Done")
    except ValueError:
        decorate.decorate_print(f"Not find {number}")
def game(langauge):
    player_enter=0
    answer=0
    try:
        if langauge=="chinese":
            decorate.decorate_print("歡迎")
            decorate.decorate_input("按Enter開始")
        else:
            decorate.decorate_print("Wecome")
            decorate.decorate_input("Use enter start")
        while True:
            if langauge=="chinese":
                player_enter=int(decorate.decorate_input("猜一個1至10數字（輸入out離開）"))
            else:
                player_enter=int(decorate.decorate_input("Guess a number between 1 and 10(enter'out'to quit):"))
            answer=random.randint(1,10)
            if player_enter=="out":
                break
            if answer==player_enter:
                if langauge=="chinese":
                    decorate.decorate_print("恭喜你猜對了")
                else:
                    decorate.decorate_print("Congratulations, you guessed correctly")
                break
            else:
                if langauge=="chinese":
                    decorate.decorate_print("再試一次")
                else:
                    decorate.decorate_print("Try again")
    except ValueError:
        decorate.decorate_print(f"Not find {player_enter}")
def calculator(langauge):
    numerical_value1=0
    numerical_value2=0
    operator=0
    try:
        if langauge=="chinese":
            decorate.decorate_print("歡迎")
            decorate.decorate_input("按Enter開始")
            decorate.decorate_print("1.+\n2.-\n3.*\n4./")
            operator=decorate.decorate_input("輸入編號運算（輸入out離開）：")
            numerical_value1=int(decorate.decorate_input("1."))
            numerical_value2=int(decorate.decorate_input("2."))
        else:
            decorate.decorate_print("Hello")
            decorate.decorate_input("Use enter start")
            decorate.decorate_print("1.+\n2.-\n3.*\n4./")
            operator=decorate.decorate_input("Enter ID number to calculate(Enter'out'to quit):")
            numerical_value1=int(decorate.decorate_input("1."))
            numerical_value2=int(decorate.decorate_input("2."))
        if operator=="1":
            decorate.decorate_print(numerical_value1+numerical_value2)
        elif operator=="2":
            decorate.decorate_print(numerical_value1-numerical_value2)
        elif operator=="3":
            decorate.decorate_print(numerical_value1*numerical_value2)
        elif operator=="4":
            decorate.decorate_print(numerical_value1/numerical_value2)
        if operator.lower=="out":
            return
    except ValueError:
        decorate.decorate_print(f"Not find {operator}")
def text_editor(lanauge):
    user_enter=0
    flie=glob.glob("*.os.txt")
    try:
        if lanauge=="chinese":
            decorate.decorate_print("歡迎")
            decorate.decorate_input("按Enter開始")
            decorate.decorate_print("1.讀取檔案\n2.新建檔案\n3.刪除檔案")
            user_enter=decorate.decorate_input("輸入編號繼續(輸入out離開）：")
        else:
            decorate.decorate_print("Wecome")
            decorate.decorate_input("Use enter start")
            decorate.decorate_print("1.Read file\n2.Create new file\n3.Delete file")
            user_enter=decorate.decorate_input("Enter the number to continue(Enter'out'to quit):")
        if user_enter=="1":
                for n,t in enumerate(flie,start=1):
                    decorate.decorate_print(n,t.replace(".os.txt",""))
                if len(flie)==0:
                    return
                else:
                    if lanauge=="chinese":
                        choice=int(decorate.decorate_input("輸入編號開啟："))
                    else:
                        choice=int(decorate.decorate_input("Enter the ID to activate:"))
                    i=choice-1
                    open_file=flie[i]
                    with open(open_file,"r",encoding="utf-8")as f:
                        decorate.decorate_print(f.read())
        if user_enter=="2":
            if lanauge=="chinese":
                flie_name=decorate.decorate_input("輸入文件名稱：")
                content=decorate.decorate_input("輸入文件內容：")
            else:
                flie_name=decorate.decorate_input("Enter file name:")
                content=decorate.decorate_input("Input file content:")
            with open(f"{flie_name}.os.txt","w",encoding="utf-8")as f:
                f.write(content)
        if user_enter=="3":
            if len(flie)==0:
                return
            else:
                for n,t in enumerate(flie,start=1):
                    decorate.decorate_print(n,t.replace(".os.txt",""))
                if lanauge=="chinese":
                    delele=int(decorate.decorate_input("輸入編號刪除（輸入out取消）"))
                else:
                    delele=int(decorate.decorate_input("Enter the ID to delete (enter'out'to cancel)"))
                i=delele-1
                delele_file=flie[i]
                if lanauge=="chinese":
                    confirm=decorate.decorate_input(f"確定刪除檔案編號{delele}（yes/no）？")
                else:
                    confirm=decorate.decorate_input(f"Confirm deletion of file number{delele}?(yes/no)")
                if confirm=="yes":
                    os.remove(delele_file)
                else:
                    return
            if user_enter.lower or delele=="out":
                return
    except Exception:
        decorate.decorate_print(f"Not find{user_enter}")