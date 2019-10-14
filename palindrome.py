def is_palindrome(text):
    strlen = len(list(text))
    pivot = int(strlen/2)
    if strlen%2 ==0:
        return  list(text)[:pivot] == list(reversed(list(text)[pivot:])) 
    else:
        return list(text)[:pivot] == list(reversed(list(text)[pivot+1:])) 

is_palindrome('nitin')
is_palindrome('aaaa')
is_palindrome('aaa')

def is_substring(subset,string):
    return True if string.find(subset)!=-1 else False



def get_palindrome(text):
    candidates = {}
    cursor = 0
    for i in range(0,len(text)):
        substr = ''.join(text[cursor:i+1])
        match = text.find(''.join(list(reversed(substr))),cursor)
        # print("reve rsed: ",''.join(list(reversed(text[cursor:i+1]))), cursor, match)
        # print(match- i)
        # print((match -i) in [0,1,2])
        if match == -1:
            cursor = cursor + 1
            i = cursor
            print(cursor)
        if is_palindrome(substr):
            if(len(substr) in candidates.keys()):
                candidates[len(substr)].append(substr)
            else:
                candidates[len(substr)] = [substr]
    #print(candidates)
    if len(candidates.keys())==0:
        return text[0]
    return list(set(candidates[max(candidates.keys())]))[0] if len(text)>0 else ""


get_palindrome('nitin')
get_palindrome('nan')
get_palindrome('aaakiranakaartsafdadanniittiinnnniittiinn')
# fails abcda
get_palindrome('abcda') # expected solution is "a"
get_palindrome('abacab')