with open('input.txt') as f:
    cur_elf = 0
    max_elfs = [0, 0, 0]
    while True:
        cal = f.readline()
        
        if not cal:
            lowest_elf = max_elfs.index(min(max_elfs))
            if cur_elf > max_elfs[lowest_elf]:
                max_elfs[lowest_elf] = cur_elf
            break

        if cal == '\n':
            lowest_elf = max_elfs.index(min(max_elfs))
            if cur_elf > max_elfs[lowest_elf]:
                max_elfs[lowest_elf] = cur_elf
            cur_elf = 0
        else:
            cur_elf += int(cal.strip())
    
    print(max_elfs)
    print(sum(max_elfs))
