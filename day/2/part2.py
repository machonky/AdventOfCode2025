import re

ID_RANGE_RE = re.compile(r",?(\d+)\-(\d+)")

#id_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#ranges = [m.groups() for m in ID_RANGE_RE.finditer(id_ranges)]
#print(ranges)

##open(0) -> powershell: Get-Content input.txt | python part2.py, bash: python part2.py < input.txt
id_ranges = open(0).readline().strip()
ranges = [m.groups() for m in ID_RANGE_RE.finditer(id_ranges)]

invalid_ids = set()
for r_lower, r_upper in ranges:
    print(f"{r_lower}-{r_upper}")
    for id in range(int(r_lower), int(r_upper) + 1):
        idstr = str(id)
        #print(f"    c:'{idstr}'")
        id_length = len(idstr)
        split, splat = divmod(id_length,2)
        for sub_id_size in range(split, 0, -1):
            #print(f"    sub_id_size:{sub_id_size}")
            leading = idstr[:sub_id_size]
            #print(f"    leading:'{leading}'")
            positions = [] # find non-overlapping occurrances of leading
            start = 0
            while True:
                idx = idstr.find(leading, start)
                if (idx == -1):
                    break
                positions.append(idx)
                start = idx + len(leading)
            if  len(positions) > 1 and \
                len(idstr)//len(leading) == len(positions) and \
                len(idstr)%len(leading) == 0:
                #print(f"        {positions}")
                #print(f"****{idstr}") # testing shows 3 successful results for 222222 (2,22,222) so we must store id's in a set
                invalid_ids.add(int(idstr))
            
total = sum(invalid_ids)
print(f"Total: {total}")