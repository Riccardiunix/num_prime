import zlib, base64

inp = open("soluz2.txt", "r")

data = inp.readline()

def find_value(it, a4, a5, a7):
    h = int(round(it))
    if a4 == 0 or a5 == 0 or a7 == 0:
        h -= 2
    if h % 2 == 0:
        return h + 1
    return h

if data[0] == "1":
    decompress = zlib.decompressobj()
    st = decompress.decompress(base64.b64decode(inp.readline().encode()))
    st = st.decode()
    r = st.split("\n")
    tot = 0
    totn = 0
    for j in range(0, len(r)):
        if j % 2 == 0:
            for k in range(int(r[j])):
                l = (totn+k+1) * 3.749999999999 + 2.249999999999
                print(find_value(l, (totn+k-4) % 8, (totn+k-5) % 8, (totn+k-7) % 8))
            tot += int(r[j])
        if r[j] != '':
            totn += int(r[j])
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
