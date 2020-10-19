"""
Your friend is making a text editor for programmers.
He is currently working on a feature that will find errors in the usage of different types of brackets.
Code can contain any brackets from the set []{}(), where the opening brackets are
[,{, and ( and the closing brackets corresponding to them are ],}, and ).

Input Format. Input contains one string 𝑆 which consists of big and small latin letters,
digits, punctuation marks and brackets from the set []{}().

Constraints. The length of 𝑆 is at least 1 and at most 105 .

Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes).
Otherwise, output the 1-based index of the first unmatched closing bracket,
and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
"""

# python3
from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    # used to test if closing bracket from string matches
    # opening bracket at top of the stack
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []

    # if opening bracket, push to top of stack
    # we use enumerate to track element and index

    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))

        # if closing bracket, stack should not be empty!
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1

            # Check top of stack.
            for j in range(len(opening_brackets_stack) - 1, -1, -1):
                # confirm that top of stack is opening bracket
                if opening_brackets_stack[j][1] in "([{":
                    # confirm it's the correct opening breacket
                    if are_matching(opening_brackets_stack[j][1], next):
                        opening_brackets_stack.pop(j)
                        break
                    else:
                        # Return index of where error is
                        # Note - this problem uses 1-indexing
                        return i + 1

    if len(opening_brackets_stack) == 1:
        return opening_brackets_stack[0][0] + 1
    return 0

def main():
    text = input()
    mismatch = find_mismatch(text)

    if mismatch != 0:
        print(mismatch)
        return 0
    print("Success")
    return 0

if __name__ == "__main__":
    main()
