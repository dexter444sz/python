

def duplicate_encode(word):
    s = ''
    new_list = list(word.lower())
    for i in new_list:
        qty = new_list.count(i)
        if qty == 1:
            s += '('
        else:
            s += ')'
        
    return s
word = "(( @"
k = duplicate_encode(word)
print(k)
l=type(k)
print(l)

hello world




