def parenthese(string:str, openclose = tuple[str,str], amount:int = 0) -> bool:
    """Check les parenthèses"""
    vstring = pass_rule(string)
    if vstring == "":
        return amount == 0
    elif vstring[0] == openclose[0]:
        return parenthese(next_char(vstring[1:],*openclose),openclose,amount + 1)
    elif vstring[0] == openclose[1]:
        return parenthese(next_char(vstring[1:],*openclose),openclose,amount - 1)
    elif amount == 0:
        return True
    else:
        return parenthese(next_char(vstring[1:],*openclose),openclose,amount)

def next_char(string:str,*chars:str) -> str:
    """Retourne le string au prochain caractère"""
    if string == "":
        return ""
    elif string[0] in chars:
        return string[1:]
    else:
        return next_char(string[1:],*chars)

def next_patern(string:str,patern:str) -> str:
    """Retourne de manière similaire à 'next_char' mais sur un patern"""
    if string == "":
        return ""
    elif string[len(patern)] == patern:
        return string[len(patern):]
    else:
        return next_char(string[1:],patern)

def pass_rule(string:str) -> str:
    """Skip une partie du programme si non nécessaire"""
    if string == "":
        return ""
    if string[0] == '#':
        return next_char(string,"\n")
    if string[0:3] == '"""':
        return next_patern(string[3:],'"""')
    elif string[0:3] == "'''":
        return next_patern(string[3:],"'''")
    elif string[0] == "'":
        return next_char(string[1:],"'")
    elif string[0] == '"':
        return next_char(string[1:],'"')
    else:
        return string

def protocol(fileaspath):
    file = open(fileaspath,'r')
    lst = [line for line in file]
    file.close()
    return parenthese("".join(lst))

if "__main__"==__name__:
    string_parenthese = "((#))\n" + "a))"
    #print(parenthese(string_parenthese,("(",")")))
    #print(next_char("abcjdkefnrju","n","d"))
    print(protocol("main.py"))
