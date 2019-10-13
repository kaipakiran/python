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
        match = text.find(''.join(list(reversed(text[cursor:i+1]))),cursor)
        if match == -1:
            substr = ''.join(text[cursor:i+1])
            if is_palindrome(substr):
                if(len(substr) in candidates.keys()):
                    candidates[len(substr)].append(substr)
                else:
                    candidates[len(substr)] = [substr]
            cursor = i
        elif((match - i) in [0,1,2]):
            if len(text[cursor:(match+(i+1-cursor))]) in candidates.keys():
                candidates[len(text[cursor:(match+(i+1-cursor))])].append(text[cursor:(match+(i+1-cursor))])
            else:
                candidates[len(text[cursor:(match+(i+1-cursor))])] = [text[cursor:(match+(i+1-cursor))]]
    return list(set(candidates[max(candidates.keys())]))[0]


get_palindrome('nitin')
get_palindrome('nan')
get_palindrome('aaakiranakaartsafdadanniittiinnnniittiinn')
# fails abcda
get_palindrome('abcda') # expected solution is "a"
