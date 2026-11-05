lazy from time import sleep
lazy from random import randint
lazy from glob import glob
lazy from os import system,remove
import edo
edo.set_theme(only_decorate="start")
def timer(language):
    try:
        if language=="chinese":
            edo.decorate_print("歡迎","|")
            edo.decorate_input("按Enter開始","|")
            number=int(edo.decorate_input("輸入你要計時的秒數（輸入out離開）：","|"))
        else:
            edo.decorate_print("Hello","|")
            edo.decorate_input("Use enter start","|")
            number=int(edo.decorate_input("Enter the number of seconds to time(enter 'out'to quit):","|"))
        if number=="out":
            system("clear")
            return
        for i in range(number):
            print(i+1)
            sleep(1)
        if language=="chinese":
            edo.decorate_print("完成","|")
        else:
            edo.decorate_print("Done,","|")
        input()
        system("clear")
    except ValueError:
        print(f"Not find {number}")
def game(langauge):
    player_enter=0
    answer=0
    try:
        if langauge=="chinese":
            edo.decorate_print("歡迎","|")
            edo.decorate_input("按Enter開始","|")
        else:
            edo.decorate_print("Wecome","|")
            edo.decorate_input("Use enter start","|")
        while True:
            if langauge=="chinese":
                player_enter=int(edo.decorate_input("猜一個1至10數字（輸入out離開）","|"))
            else:
                player_enter=int(edo.decorate_input("Guess a number between 1 and 10(enter'out'to quit):","|"))
            answer=randint(1,10)
            if player_enter=="out":
                system("clear")
                break
            if answer==player_enter:
                if langauge=="chinese":
                    edo.decorate_print("恭喜你猜對了","|")
                else:
                    edo.decorate_print("Congratulations, you guessed correctly","|")
                break
            else:
                if langauge=="chinese":
                    edo.decorate_print("再試一次","|")
                else:
                    edo.decorate_print("Try again","|")
        system("clear")
    except ValueError:
        print(f"Not find {player_enter}")
def calculator(langauge):
    numerical_value1=0
    numerical_value2=0
    operator=0
    try:
        if langauge=="chinese":
            edo.decorate_print("歡迎","|")
            edo.decorate_input("按Enter開始","|",only_decorate="start")
            edo.decorate_print("1.+\n2.-\n3.*\n4./","|")
            operator=edo.decorate_input("輸入編號運算（輸入out離開）：","|")
            numerical_value1=int(edo.decorate_input("1.","|"))
            numerical_value2=int(edo.decorate_input("2.","|"))
        else:
            edo.decorate_print("Hello","|")
            edo.decorate_input("Use enter start","|")
            edo.decorate_print("1.+\n2.-\n3.*\n4./","|")
            operator=edo.decorate_input("Enter ID number to calculate(Enter'out'to quit):","|")
            numerical_value1=int(edo.decorate_input("1.","|"))
            numerical_value2=int(edo.decorate_input("2.","|"))
        if operator=="1":
            edo.decorate_print(numerical_value1+numerical_value2,"|")
            input()
        elif operator=="2":
            edo.decorate_print(numerical_value1-numerical_value2,"|")
            input()
        elif operator=="3":
            edo.decorate_print(numerical_value1*numerical_value2,"|")
            input()
        elif operator=="4":
            edo.decorate_print(numerical_value1/numerical_value2,"|")
            input()
        if operator.lower()=="out":
            system("clear")
            return
        system("clear")
    except ValueError:
        print(f"Not find {operator}")
def text_editor(lanauge):
    user_enter=0
    flie=glob.glob("*.os.txt")
    try:
        if lanauge=="chinese":
            edo.decorate_print("歡迎","|")
            edo.decorate_input("按Enter開始","|")
            edo.decorate_box("1.讀取檔案\n2.新建檔案\n3.刪除檔案","|",title="選單")
            user_enter=edo.decorate_input("輸入編號繼續(輸入out離開）：","|",only_decorate="start")
        else:
            edo.decorate_print("Wecome","|")
            edo.decorate_input("Use enter start","|")
            edo.decorate_box("1.Read file\n2.Create new file\n3.Delete file","|",title="Menu")
            user_enter=edo.decorate_input("Enter the number to continue(Enter'out'to quit):","|",only_decorate="start")
        if user_enter=="1":
                for n,t in enumerate(flie,start=1):
                    edo.decorate_print(n,t.replace(".os.txt",""),"|")
                if len(flie)==0:
                    system("clear")
                    return
                else:
                    if lanauge=="chinese":
                        choice=int(edo.decorate_input("輸入編號開啟：","|"))
                    else:
                        choice=int(edo.decorate_input("Enter the ID to activate:","|"))
                    i=choice-1
                    open_file=flie[i]
                    with open(open_file,"r",encoding="utf-8")as f:
                        edo.decorate_print(f.read(),"|")
        if user_enter=="2":
            if lanauge=="chinese":
                flie_name=edo.decorate_input("輸入文件名稱：","|")
                content=edo.decorate_input("輸入文件內容：","|")
            else:
                flie_name=edo.decorate_input("Enter file name:","|")
                content=edo.decorate_input("Input file content:","|")
            with open(f"{flie_name}.os.txt","w",encoding="utf-8")as f:
                f.write(content)
        if user_enter=="3":
            if len(flie)==0:
                return
            else:
                for n,t in enumerate(flie,start=1):
                    edo.decorate_print(n,t.replace(".os.txt"),"|")
                if lanauge=="chinese":
                    delele=int(edo.decorate_input("輸入編號刪除（輸入out取消）","|"))
                else:
                    delele=int(edo.decorate_input("Enter the ID to delete (enter'out'to cancel)","|"))
                i=delele-1
                delele_file=flie[i]
                if lanauge=="chinese":
                    confirm=edo.decorate_input(f"確定刪除檔案編號{delele}（yes/no）？","|")
                else:
                    confirm=edo.decorate_input(f"Confirm deletion of file number{delele}?(yes/no)","|")
                if confirm=="yes":
                    remove(delele_file)
                else:
                    return
            if user_enter.lower()=="out" or delele=="out":
                return
            system("clear")
    except Exception:
        print(f"Not find{user_enter}")