#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    t = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        t += int(sys.argv[i])

    print(t)
