import tool
print("Hello")
print("Choose your language")
player_language=input("中文輸入1，English enter 2: ")
language=None
if player_language=="1":
    language="chinese"
else:
    language="english"
while True:
    try:
        if language=="chinese":
            print("\n1.計時器\n2.遊戲")
            open_tool=input("輸入工具編號開啟（輸入out離開）：")
        else:
            print("\n1.Timer\n2.Game")
            open_tool=input("Enter tool ID open(enter 'out' to quit): ")
        if open_tool=="1":
            tool.timer(language)
        elif open_tool=="2":
            tool.game(language)
        else:
            break
    except ValueError:
        print(f"Not find {open_tool}")