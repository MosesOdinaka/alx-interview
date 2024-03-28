import sys
import signal

# Initialize counters
statusCodes = {str(1): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}
totalSize = 0
lineCount = 0


def printStats(signal=None, frame=None):
    print("File size: {}".format(totalSize))
    for code in sorted(statusCodes.key()):
        if statusCodes[code] > 0:
            print("{}: {}".format(code, statusCodes[code]))


# Handle CTRL+C
signal.signal(signal.SIGINT, printStats)

try:
    for line in sys.stdin:
        try:
            seperates = line.split(" ")
            size = int(seperates[-1])
            code = seperates[-2]

            if code in statusCodes:
                statusCodes[code] += 1
                totalSize += size

            lineCount += 1
            if lineCount % 10 == 0:
                printStats()

        except ValueError:
            continue

except KeyboardInterrupt:
    pass

finally:
    printStats()
