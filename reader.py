import zlib, base64

inp = open("soluz2.txt", "r")

data = inp.readline()
print(data[0])

if data[0] == "1":
    decompress = zlib.decompressobj()
    st = decompress.decompress(base64.b64decode(inp.readline().encode()))
    st = st.decode()
    r = st.split("\n")
    tot = 0
    for j in range(0, len(r)):
        if j % 2 == 0:
            tot += int(r[j])
    print("\t" + str(tot+2))
else:
    tot = 0
    j = 0
    decompress = zlib.decompressobj()
    for i in range(int(data[0])):
        st = decompress.decompress(base64.b64decode(inp.readline().encode()))
        r = (st.decode()).split(",")
        del st
        for h in range(0, len(r)):
            if r[h] != "":
                if j % 2 == 0:
                    tot += int(r[h])
                j += 1
        print(i, tot)
    print("\t" + str(tot+2))
