# Implement modulo without using the (%) operator.
def modulo(a, b):
    return (a - b * (a // b))

print(modulo(5, 3))

# Take an input string and determine if exactly 3 question marks
# exist between every pair of numbers that add up to 10.
# If so, return true, otherwise return false.
def exists_three_question_marks(s):
    return s.count('?') == 3

def question_mark(s):
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i+1, len(s)):
                if s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
                    if not exists_three_question_marks(s[i:j]):
                        return False
    return True
print(question_mark('1asdf???asdfa9')) # True
print(question_mark('1asdf???asdfa91')) # False
