lazy from rich.console import Console
lazy from rich.text import Text
lazy from rich.panel import Panel
lazy from rich.style import Style
console=Console()
theme_color="white"
theme_decorate=None
def decorate_print(text,decorate,only_decorate=None,color=None):
    try:
        global theme_color
        global theme_decorate
        text=str(text)
        if only_decorate is None:
            only_decorate=theme_decorate
        if color is None:
            color=theme_color
        lines=text.split('\n')
        for line in lines:
            if only_decorate=="start":
                string=f"{decorate}{line}"
            elif only_decorate=="end":
                string=f"{line}{decorate}"
            else:
                string=f"{decorate}{line}{decorate}"
            if color!=None:
                string=f"[{color}]{string}[/]"
            console.print(string)
    except Exception:
        print("Error!")
def decorate_input(text,decorate,only_decorate=None,color=None):
    try:
        global theme_color
        global theme_decorate
        if only_decorate is None:
            only_decorate=theme_decorate
        text=str(text)
        if color is None:
            color=theme_color
        lines=text.split('\n')
        for _ in lines[:-1]:
            if only_decorate=="start":
                string=f"{decorate}{lines[-1]}"
            elif only_decorate=="end":
                string=f"{lines[-1]}{decorate}"
            else:
                string=f"{decorate}{lines[-1]}{decorate}"
            console.print(Text(string,style=color))
        late_line=lines[-1]
        if only_decorate=="start":
            result=f"{decorate}{late_line}"
        elif only_decorate=="end":
            result=f"{late_line}{decorate}"
        else:
            result=f"{decorate}{late_line}{decorate}"
        variable=console.input(Text(result,style=color))
        return variable
    except Exception:
        print("Error!")
def decorate_box(text,decorate,title,only_decorate=None,size=None,color=None):
    try:
        global theme_color
        global theme_decorate
        text=str(text)
        title=str(title)
        if only_decorate is None:
            only_decorate=theme_decorate
        if color is None:
            color=theme_color
        lines=text.split('\n')
        result=[]
        for line in lines:
            if only_decorate=="start":
                string=f"{decorate}{line}"
            elif only_decorate=="end":
                string=f"{line}{decorate}"
            else:
                string=f"{decorate}{line}{decorate}"
            result.append(string)
        final_text="\n".join(result)
        if size is not None:
            width=max(3,size[0])
            height=max(3,size[1])
        else:
            width,height=150,5
        box=Panel(final_text,title=title,width=width,height=height,border_style=color)
        console.print(box)
    except Exception as e:
        print(f"Error!{e}")
def set_theme(only_decorate=None,color=None):
    global theme_color
    global theme_decorate
    if only_decorate==None:
        theme_decorate=None
    else:
        theme_decorate=only_decorate
    if color==None:
        theme_color="white"
    else:    
        Style.parse(color)
        theme_color=color