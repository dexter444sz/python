

def alphabet_position(text):
    s = ''
    new_list = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_text = list(text.lower())
    for i in alphabet_text:
        symbol = i
        for k in new_list:
                symbol2 = k
                if symbol == symbol2:
                    s = s + ' ' + str(new_list.index(k)+1)    
    s = s.replace(' ', '', 1)
    return s
text = "The sunset sets at twelve o' clock."
k = alphabet_position(text)
print(k)
l=type(k)
print(l)




