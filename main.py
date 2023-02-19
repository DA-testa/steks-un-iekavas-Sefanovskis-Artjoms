# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    brackets_stack = []
    counters = {'(': 0, ')': 0, '[': 0, ']': 0,'{': 0, '}': 0}
    for i, next in enumerate(text):
        if next in "([{)]}":
            bracket = Bracket(next,i)
            brackets_stack.append(bracket)
            counters[next] = counters[next] + 1
    
    roundBrack = counters["("] - counters[")"]
    squareBrack = counters["["] - counters["]"]
    curlyBrack = counters["{"] - counters["}"]

    if roundBrack == 0 and squareBrack == 0 and curlyBrack == 0:
        return False

    elif roundBrack < 0 or squareBrack < 0 or curlyBrack < 0:


        for i in brackets_stack[::-1]:
            brackCounter = roundBrack if i.char == ")" else squareBrack if i.char == "]" else curlyBrack

            if(i.char in ")]}" and brackCounter < 0):
                return i.position
    else:
        for i in brackets_stack:
            brackCounter = roundBrack if i.char == "(" else squareBrack if i.char == "[" else curlyBrack

            if(i.char in "([{" and brackCounter > 0):
                return i.position
        
def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch == False):
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()





