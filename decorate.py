def decorate_print(text):
    text=str(text)
    lines=text.split('\n')
    for line in lines:
        print(f"|{line}")
def decorate_input(text,type=str):
    text=str(text)
    lines=text.split('\n')
    for line in lines[:-1]:
        print(f"|{line}")
    if type==str:
        variable=input(f"|{lines[-1]}")
    elif type==int:
        variable=int(input(f"|{lines[-1]}"))
    else:
        print("Error!")
    return variable