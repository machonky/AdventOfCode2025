import re

ID_RANGE_RE = re.compile(r",?(\d+)\-(\d+)")

#id_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#ranges = [m.groups() for m in ID_RANGE_RE.finditer(id_ranges)]
#print(ranges)

##open(0) -> powershell: Get-Content input.txt | python part1.py, bash: python part1.py < input.txt
id_ranges = open(0).readline().strip()
ranges = [m.groups() for m in ID_RANGE_RE.finditer(id_ranges)]

invalid_ids = []
for r_lower, r_upper in ranges:
    print(f"{r_lower}-{r_upper}")
    for id in range(int(r_lower), int(r_upper) + 1):
        idstr = str(id)
        #print(f"    c:'{idstr}'")
        id_length = len(idstr)
        split, splat = divmod(id_length,2)
        if (splat == 0):
            #print(f"    c:{idstr} split:{split}")
            leading = idstr[:split]
            #print(f"    l:{leading}")
            trailing = idstr[-split:]
            #print(f"    t:{trailing}")
            if (leading == trailing):
                print(f"    c:{idstr} split:{split}")
                print(f"****{idstr}")
                invalid_ids.append(int(idstr))
total = sum(invalid_ids)
print(total)