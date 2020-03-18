import sys
import os
import random

def getID():
    out = ''
    options = \
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTTUVWXYZ'
    out += options[random.randint(0, 62)]
    out += options[random.randint(0, 62)]
    out += options[random.randint(0, 62)]
    out += options[random.randint(0, 62)]
    out += options[random.randint(0, 62)]
    out += options[random.randint(0, 62)]
    return out

def push(result1, result2, result3):       
    rows = 0
    results = []
    randomID = getID()
    for input in ["1st: "+result1,
                  "2nd: "+result2,
                  "3rd: "+result3]:
        output = ''
        while len(input) > 32:
            rows = rows + 1
            lastSpace = str.rindex(input, beg=0, end=32)
            if lastSpace != -1 and 32 - lastSpace < 5:
                if str.rindex(input, beg=33, end=33) != -1:
                    output += input[0:32] + '\n'
                    input = input[33:len(input)]
                else:
                    output += input[0:lastSpace] + '\n'
                    input = input[lastSpace + 1:len(input)]
            else:
                output += input[0:31] + '-'
                input = input[32:len(input)]

        output += input
        results.append(output)

    os.system("echo \"" + chr(0x7F) + (" " * 12) + randomID + (" " * 12)
              + chr(0x7F) + "\n\" > /dev/serial0")
    rows += 1

    os.system("echo \"" + results[0] + "\n\" > /dev/serial0")
    rows += 2

    os.system("echo \"" + results[1] + "\n\" > /dev/serial0")
    rows += 2

    os.system("echo \"" + results[2] + "\n\" > /dev/serial0")
    rows += 2

    os.system("echo \"" + chr(0x7F) + (" " * 12) + randomID + (" " * 12)
              + chr(0x7F) + "\n\" > /dev/serial0")
    rows += 1

    os.system('echo \"Thank you for voting. Hold on to'
              + 'this reciept and insert it to\n'
              + 'the scanning unit to cast your\n'
              + 'Vote. Thank you for voting.\n\" > /dev/serial0')
    rows += 5
    os.system('echo "This system has been brought to\n'
              + 'you by Team 26: DemocraSafe." > /dev/serial0')
    rows += 2
    while rows < 28:  # about 10.5CM
        os.system('echo "" > /dev/serial0')
        rows = rows + 1
