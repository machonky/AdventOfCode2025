totalOutputJoltage = 0
with open(0) as f:
    for batteryLabel in [line.strip() for line in f]:
        print(f"batteryLabel:{batteryLabel}")
        maxMagnitude = 11
        magnitude = maxMagnitude
        magnitudeDigit = 0
        cellJolts = []
        batteryLabelLen = len(batteryLabel)
        #print(f"    batteryLabelLen:{batteryLabelLen}")
        i = 0
        foundIndex = 0
        while i < batteryLabelLen:
            if magnitude == -1:
                break

            cellKey = batteryLabel[i]
            #print(f"    cellKey: {cellKey} magnitude:{magnitude} i:{i}")

            if int(cellKey) > magnitudeDigit:
                magnitudeDigit = int(cellKey)
                foundIndex = i # we might need this position if we don't find anything larger
                #print(f"    found '{magnitudeDigit}'")

            # position limit of the string for this O.O.M
            if i == batteryLabelLen - magnitude - 1:
                #print(f"    collect '{magnitudeDigit}' i:{i}")
                cellJolts.append(magnitudeDigit*10**magnitude)
                magnitudeDigit = 0
                magnitude -= 1
                i = foundIndex + 1 # jump back just after where we found the best jolt
                continue           

            if int(cellKey) == 9:
                magnitudeDigit = int(cellKey)
                #collect
                #print(f"    collect '{magnitudeDigit}'")
                cellJolts.append(magnitudeDigit*10**magnitude)
                magnitudeDigit = 0
                magnitude -= 1

            i += 1

        batteryJolts = sum(cellJolts)
        totalOutputJoltage += batteryJolts
        print(f"    batteryJolts:{batteryJolts}")
print(f"totalOutputJoltage:{totalOutputJoltage}")


