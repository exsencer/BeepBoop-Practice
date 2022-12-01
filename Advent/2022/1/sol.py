with open('input.txt') as f:
    cur_elf = 0
    max_elf = 0
    while True:
        cal = f.readline()
        if not cal:
            if cur_elf > max_elf:
                max_elf = cur_elf
            #print(cur_elf)
            break

        if cal == '\n':
            #print(cur_elf)
            if cur_elf > max_elf:
                max_elf = cur_elf
            cur_elf = 0
        else:
            cur_elf += int(cal.strip())
    
    print(max_elf)