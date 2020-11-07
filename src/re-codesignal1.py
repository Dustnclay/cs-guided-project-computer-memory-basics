def csBinaryToASCII(binary):
    saved = binary
    letterlist = []
    collected = ""

    for i in range (0,len(saved),8):
        letterlist.append(saved[i:i+8])

    for binnum in letterlist:
        collected += chr(int(binnum,2))

    print('letterlist:',letterlist)
    print("collected",collected)


csBinaryToASCII("011011000110000101101101011000100110010001100001")

    # firstletter = ""
    # second = ""
    # index = 0
    # saved = binary
    # for item in saved:
    # print(saved[i])
    # print()
        # if index < 8:
        # print(saved[i:i+8])

        #     firstletter += item
        #     index += 1 
        #     print(index)
        # else:
        #     letterlist.append(firstletter)
            # saved.pop(0)
            # saved.pop(1)
            # saved.pop(2)
            # saved.pop(3)
            # saved.pop(4)
            # saved.pop(5)
            # saved.pop(6)
            # saved.pop(7)
    
    # print(firstletter)