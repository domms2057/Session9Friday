fp = open("text.txt", "r")
print(fp.read())
fp.close() # close is good practice, not needed

with open("text.txt", "r") as fp:
    for line in fp:
        print(line, end="")
        print(line.rstrip())

with open("text.txt", "r") as fp:
    line_number = 1
    for line in fp:
        # print(line, end="
        print(f"{line_number}): {line.rstrip()}")
        line_number += 1