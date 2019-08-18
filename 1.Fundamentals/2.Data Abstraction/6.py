def is_circular_rotation(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if len(s) != len(t):
            return False
        if s.find(t[0:len(t) - i]) != -1:
            new_s = t[0:len(t) - i] + s[0:i]
            if new_s != t:
                return True
    return False


s = 'ACTGACG'
t = 'TGACGAC'
print(is_circular_rotation(s, t))