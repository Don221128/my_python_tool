def decorate_print(text):
    text=str(text)
    lines=text.split('\n')
    for line in lines:
        print(f"|{line}")
def decorate_input(text):
    text=str(text)
    lines=text.split('\n')
    for line in lines[:-1]:
        print(f"|{line}")
    variable=input(f"|{lines[-1]}")
    return variable