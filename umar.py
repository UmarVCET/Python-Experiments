def find_a(s):
    for i in range(len(s)):
        if s[i] == 'a':
            a_index = i
        else: pass
    return a_index


def checkString (s : str) -> bool:
    if len(s) == 0:
        return True
    else:
        if 'a' not in s:
            return True
        elif 'b' not in s:
            return False
        a_index = find_a(s)
        if a_index < s.index('b'):
            return True
        else:
            return False

checkString("aabaa")
checkString("bbb")
     
True
