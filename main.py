import tool
import decorate
decorate.decorate_print("Hello\nChoose your language")
user_language=decorate.decorate_input("中文輸入1，English enter 2:")
if user_language=="1":
    language="chinese"
else:
    language="english"
while True:
    try:
        if language=="chinese":
            decorate.decorate_print("\n1.計時器\n2.遊戲\n3.計算機\n4.文字編輯器")
            open_tool=decorate.decorate_input("輸入工具編號開啟（輸入out離開）：")
        else:
            decorate.decorate_print("\n1.Timer\n2.Game\n3.Calculator\n4.Text editor")
            open_tool=decorate.decorate_input("Enter tool ID open(enter'out'to quit):")
        if open_tool=="1":
            tool.timer(language)
        elif open_tool=="2":
            tool.game(language)
        elif open_tool=="3":
            tool.calculator(language)
        elif open_tool=="4":
            tool.text_editor(language)
        elif open_tool=="out":
            break
        else:
            if language=="chinese":
                raise ValueError(f"Traceback (most recent call last):\n   File 'main.py', line 14, in <module>\n     open_tool=input('輸入工具編號開啟（輸入out離開）：')\nValueError: {open_tool} not in list")
            else:
                raise ValueError(f"Traceback (most recent call last) :\n   File 'main.py', line 17, in <module> \n     open_tool=input/('Enter tool ID open(enter'out'to quit):')\nValueError:{open_tool} not in list")
    except Exception as e:
        print(f"Not find {open_tool}.Detailed Information:\n{e}")