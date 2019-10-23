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
    i = 0
    sequence_len = len(text)
    if is_palindrome(text) or text=="":
        return text
    elif len(set(text))==sequence_len:
        return text[0]
    while(i<sequence_len):
        match = text.find(''.join(list(reversed(text[cursor:i+1]))),cursor+1)
        if match == -1:
            if len(candidates.keys())>0:
                max_len = max(candidates.keys())
                if len(text[cursor:sequence_len])<max_len:
                    return list(set(candidates[max_len]))[0] 
            substr = ''.join(text[cursor:i+1])
            if is_palindrome(substr):
                # if(len(substr) in candidates.keys()):
                #     candidates[len(substr)].append(substr)
                # else:
                candidates[len(substr)] = [substr]
            cursor = cursor + 1
            i = cursor
        elif((match - i) in [0,1,]):
            # if len(text[cursor:(match+(i+1-cursor))]) in candidates.keys():
            #     candidates[len(text[cursor:(match+(i+1-cursor))])].append(text[cursor:(match+(i+1-cursor))])
            # else:
            candidates[len(text[cursor:(match+(i+1-cursor))])] = [text[cursor:(match+(i+1-cursor))]]
        i+=1
    if len(candidates.keys())==0:
        return text[0]
    return list(set(candidates[max(candidates.keys())]))[0]


get_palindrome('nitin')
get_palindrome('nan')
get_palindrome('aaakiranakaartsafdadanniittiinnnniittiinn')
# fails abcda
get_palindrome('abcda') # expected solution is "a"
get_palindrome('abacab')


def get_shortest_palindrome(text):
    """
    Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
    Find and return the shortest palindrome you can find by performing this transformation.

    Example 1:

    Input: "aacecaaa"
    Output: "aaacecaaa"
    Example 2:

    Input: "abcd"
    Output: "dcbabcd"
    """
    strlen = len(text)
        unique_chars = len(set(text))
        print(set(text))
        if unique_chars == strlen:
            return ("".join(list(reversed(text[1:])))+text)
        if text=="" or strlen==1 or unique_chars==1:
            return text
        if is_palindrome(text):
            return text
        if strlen//unique_chars > 100:
            d = {}
            for char in set(text):
                            
        left_pad = []
        #print(strlen)
        i = strlen-1
        while(i!=0):
            left_pad.append(text[i])
            #print(left_pad)
            #print("text[:i-1]: ",text[:i],i)
            if is_palindrome(text[:i]):
              #  print("".join(left_pad)+text)
                return ("".join(left_pad)+text)
            i = i -1    

get_shortest_palindrome('abcd')
get_shortest_palindrome('cbabcd')