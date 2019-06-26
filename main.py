import time, sys, math, bitarray, base64, zlib


def findIndex(s):
    n = (s + 1) // 6
    if (s > n * 6):
        return (n << 1) - 1
    return (n << 1) - 2


def n_primi8(n):
    start = time.time()

    sys.stdout.write("Array... "), sys.stdout.flush()
    u = n // 3
    a = bitarray.bitarray(u)
    a.setall(False)
    sys.stdout.write("done\n")
    itertot = 0
    sys.stdout.write("5, 7, 11, 13, 17, 19, 23, 29... "), sys.stdout.flush()
    iter = 0
    mi, i = 7, 1
    mj, j = 10, 1
    mk, k = 17, 1
    mh, h = 20, 1
    mp, p = 27, 1
    ml, l = 30, 1
    mr, r = 37, 1
    mo, o = 47, 1
    while i or j or k or h or p or l or r or o:
        # Multipli di 5
        if i:
            try:
                for y in range(18):
                    a[mi] = 1
                    a[mi + 3] = 1
                    mi += 10
            except:
                i = False
                del mi
        # Multipli di 7
        if j:
            try:
                for y in range(13):
                    a[mj] = 1
                    a[mj + 5] = 1
                    mj += 14
            except:
                j = False
                del mj
        # Multipli di 11
        if k:
            try:
                for y in range(8):
                    a[mk] = 1
                    a[mk + 7] = 1
                    mk += 22
            except:
                k = False
                del mk
        # Multipli di 13
        if h:
            try:
                for y in range(7):
                    a[mh] = 1
                    a[mh + 9] = 1
                    mh += 26
            except:
                h = False
                del mh
        # Multipli di 17
        if p:
            try:
                for y in range(6):
                    a[mp] = 1
                    a[mp + 11] = 1
                    mp += 34
            except:
                p = False
                del mp
        # Multipli di 19
        if l:
            try:
                for y in range(5):
                    a[ml] = 1
                    a[ml + 13] = 1
                    ml += 38
            except:
                l = False
                del ml
        # Multipli di 23
        if r:
            try:
                for y in range(4):
                    a[mr] = 1
                    a[mr + 15] = 1
                    mr += 46
            except:
                r = False
                del mr
        # Multipli di 29
        if o:
            try:
                for y in range(3):
                    a[mo] = 1
                    a[mo + 19] = 1
                    mo += 58
            except:
                o = False
                del mo
        iter += 1
    del i, j, k, h, p, l, r, o
    sys.stdout.write("done (%d)\n" % iter)

    itertot += iter

    k = 31
    d = 21
    p = 10
    sqrt = int(math.sqrt(n)) + 1

    while k < sqrt:
        iter = 0
        while k < sqrt and a[findIndex(k)] != 0:
            d += 2
            p += 1
            k = int(3 * p + 1.5)
            if k % 2 == 0:
                k += 1
            iter += 1

        if k < sqrt:
            i = int(round((k * 5) / 6.0))
            i1 = (6 * i) - 1
            i2 = (6 * i) + 1
            if i1 % k == 0:
                s = findIndex(i1)
            else:
                s = findIndex(i2)
            del i, i1, i2

            d2 = d + 2
            p += 1
            k2 = int(3 * p + 1.5)
            if k2 % 2 == 0:
                k2 += 1
            while k2 < sqrt and a[findIndex(k2)] != 0:
                d2 += 2
                p += 1
                k2 = int(3 * p + 1.5)
                if k2 % 2 == 0:
                    k2 += 1
                iter += 1

            if k2 < sqrt:
                ii = int(round((k2 * 5) / 6.0))
                ii1 = (6 * ii) - 1
                ii2 = (6 * ii) + 1
                if ii1 % k2 == 0:
                    s2 = findIndex(ii1)
                else:
                    s2 = findIndex(ii2)
                del ii, ii1, ii2

                d3 = d2 + 2
                p += 1
                k3 = int(3 * p + 1.5)
                if k3 % 2 == 0:
                    k3 += 1
                while k3 < sqrt and a[findIndex(k3)] != 0:
                    d3 += 2
                    p += 1
                    k3 = int(3 * p + 1.5)
                    if k3 % 2 == 0:
                        k3 += 1
                    iter += 1

                if k3 < sqrt:
                    sys.stdout.write(str(k) + ", " + str(k2) + ", " + str(k3) + "... "), sys.stdout.flush()
                    iii = int(round((k3 * 5) / 6.0))
                    iii1 = (6 * iii) - 1
                    iii2 = (6 * iii) + 1
                    if iii1 % k3 == 0:
                        s3 = findIndex(iii1)
                    else:
                        s3 = findIndex(iii2)
                    del iii, iii1, iii2

                    while s3 < u:
                        a[s3] = 1
                        a[s2] = 1
                        a[s] = 1
                        if s3 + d3 < u:
                            a[s3 + d3] = 1
                            a[s2 + d2] = 1
                            a[s + d] = 1
                        elif s2 + d2 < u:
                            a[s2 + d2] = 1
                            a[s + d] = 1
                        elif s + d < u:
                            a[s + d] = 1
                        s += k << 1
                        s2 += k2 << 1
                        s3 += k3 << 1
                        iter += 1

                    del s3

                    while s2 < u:
                        a[s2] = 1
                        a[s] = 1
                        if s2 + d2 < u:
                            a[s2 + d2] = 1
                            a[s + d] = 1
                        elif s + d < u:
                            a[s + d] = 1
                        s += k << 1
                        s2 += k2 << 1
                        iter += 1

                    del s2

                    while s < u:
                        a[s] = 1
                        if s + d < u:
                            a[s + d] = 1
                        s += k << 1
                        iter += 1

                    del s
                    d = d3 + 2
                    sys.stdout.write("done (%d)\n" % iter)

                else:
                    sys.stdout.write(str(k) + ", " + str(k2) + "... "), sys.stdout.flush()

                    while s2 < u:
                        a[s2] = 1
                        a[s] = 1
                        if s2 + d2 < u:
                            a[s2 + d2] = 1
                            a[s + d] = 1
                        elif s + d < u:
                            a[s + d] = 1
                        s += k << 1
                        s2 += k2 << 1
                        iter += 1

                    del s2

                    while s < u:
                        a[s] = 1
                        if s + d < u:
                            a[s + d] = 1
                        s += k << 1
                        iter += 1

                    del s
                    d = d2 + 2
                    sys.stdout.write("done (%d)\n" % iter)

            else:
                sys.stdout.write(str(k) + "... "), sys.stdout.flush()

                while s < u:
                    a[s] = 1
                    if s + d < u:
                        a[s + d] = 1
                    s += k << 1
                    iter += 1

                del s
                sys.stdout.write("done (%d)\n" % iter)

        itertot += iter
        p += 1
        k = int(3 * p + 1.5)
        if k % 2 == 0:
            k += 1

    print("\n%15d %5.5f %20d\n" % (n, time.time() - start, itertot))

    sys.stdout.write("Scrittura... "), sys.stdout.flush()
    s = 1
    out = open("soluz.txt", "w")
    cont1 = 0
    cont0 = 0
    for i in range(u):
        if a[i] == 0:
            if cont1 == 0:
                if cont0 != 0:
                    out.write(str(cont0) + "\n")
                    s += 1
                cont0 = 0
            cont1 += 1
        else:
            if cont0 == 0:
                out.write(str(cont1) + "\n")
                s += 1
                cont1 = 0
            cont0 += 1

    if cont0 == 0:
        out.write(str(cont1))
    if cont0 == 1:
        out.write(str(cont0))
    out.close()
    del n, cont0, cont1
    del a
    sys.stdout.write("done\n")

    sys.stdout.write("Compressione... "), sys.stdout.flush()
    gb = (s // 536870912) + 1
    out = open("soluz2.txt", "w")
    if gb == 1:
        compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15)
        a = compress.compress((open("soluz.txt", "r").read()).encode()) + compress.flush()
        out.write("1\n" + base64.b64encode(a).decode())
    else:
        inp = open("soluz.txt", "r")
        out.write(str(gb) + "\n")
        div = s // gb
        for i in range(gb - 1):
            st = ""
            for j in range(div):
                st += inp.readline()
            compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15)
            out.write(base64.b64encode(compress.compress(st.replace("\n", ",").encode()) + compress.flush()).decode() + "\n")

        st = ""
        a = inp.readline()
        while a != "":
            st += a
            a = inp.readline()
        compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15)
        out.write(base64.b64encode(compress.compress(st.replace("\n", ",").encode()) + compress.flush()).decode() + "\n")
    sys.stdout.write("done\n")


if len(sys.argv) > 1:
    n_primi8(int(sys.argv[1]))
else:
    n_primi8(100000000)
