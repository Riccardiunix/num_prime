import time
import sys
import math
import bitarray
import base64
import zlib


def find_next(p, sqrt, a, u):
    while p < u and a[p] == 1:
        p += 1

    if p < u:
        p += 1
        k = 3 * p + 1
        if k % 2 == 0:
            k += 1
        d = (p << 1) + 1
        i = int(round(k * (5.0 / 6.0)))
        i1 = (6 * i) - 1
        i2 = i1 + 2
        s = (i << 1) - 1
        if i1 % k == 0:
            s -= 1
        del i, i1, i2
        return k, d, s, p
    return sqrt, sqrt, sqrt, p


if __name__ == "__main__":
    n = 100000000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    start = time.time()

    sys.stdout.write("Array... "), sys.stdout.flush()
    u = n // 3 + 1
    a = bitarray.bitarray(u)
    a.setall(False)
    sys.stdout.write("done\n")
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
            except IndexError:
                i = False
                del mi
        # Multipli di 7
        if j:
            try:
                for y in range(13):
                    a[mj] = 1
                    a[mj + 5] = 1
                    mj += 14
            except IndexError:
                j = False
                del mj
        # Multipli di 11
        if k:
            try:
                for y in range(8):
                    a[mk] = 1
                    a[mk + 7] = 1
                    mk += 22
            except IndexError:
                k = False
                del mk
        # Multipli di 13
        if h:
            try:
                for y in range(7):
                    a[mh] = 1
                    a[mh + 9] = 1
                    mh += 26
            except IndexError:
                h = False
                del mh
        # Multipli di 17
        if p:
            try:
                for y in range(6):
                    a[mp] = 1
                    a[mp + 11] = 1
                    mp += 34
            except IndexError:
                p = False
                del mp
        # Multipli di 19
        if l:
            try:
                for y in range(5):
                    a[ml] = 1
                    a[ml + 13] = 1
                    ml += 38
            except IndexError:
                l = False
                del ml
        # Multipli di 23
        if r:
            try:
                for y in range(4):
                    a[mr] = 1
                    a[mr + 15] = 1
                    mr += 46
            except IndexError:
                r = False
                del mr
        # Multipli di 29
        if o:
            try:
                for y in range(3):
                    a[mo] = 1
                    a[mo + 19] = 1
                    mo += 58
            except IndexError:
                o = False
                del mo
        iter += 1
    del i, j, k, h, p, l, r, o
    sys.stdout.write("done (%d)\n" % iter)

    sqrt = int(round(math.sqrt(n))) + 1
    usqrt = sqrt // 3 + 1

    k = 31
    d = 21
    s = 50

    k2 = 37
    d2 = 25
    s2 = 60

    k3 = 41
    d3 = 27
    s3 = 67

    p = 13

    while s3 != u and s2 != u and s != u:
        try:
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
        except IndexError:
            k3o = k3
            po = p+1
            k3, d3, s3, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k3 >= sqrt:
                print("%d... done" % k3o)
                s3 = u
            else:
                print("%d -> %d" % (k3o, k3))
                a[s3] = 1
                a[s3 + d3] = 1
                s3 += k3 << 1
            del k3o, po

        try:
            a[s2] = 1
            a[s2 + d2] = 1
            s2 += k2 << 1
            a[s2] = 1
            a[s2 + d2] = 1
            s2 += k2 << 1
        except IndexError:
            k2o = k2
            po = p + 1
            k2, d2, s2, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k2 >= sqrt:
                print("%d... done" % k2o)
                s2 = u
            else:
                print("%d -> %d" % (k2o, k2))
                a[s2] = 1
                a[s2 + d2] = 1
                s2 += k2 << 1
            del k2o, po

        try:
            a[s] = 1
            a[s + d] = 1
            s += k << 1
            a[s] = 1
            a[s + d] = 1
            s += k << 1
        except IndexError:
            ko = k
            po = p + 1
            k, d, s, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k >= sqrt:
                print("%d... done" % ko)
                s = u
            else:
                print("%d -> %d" % (ko, k))
                a[s] = 1
                a[s + d] = 1
                s += k << 1
            del ko, po
        iter += 1

    if s3 == u:
        s3 = s2
        d3 = d2
        k3 = k2
        s2 = s
        d2 = d
        k2 = k
    elif s2 == u:
        s2 = s
        d2 = d
        k2 = k
    del s, d, k

    while s3 != u and s2 != u:
        try:
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
        except IndexError:
            k3o = k3
            po = p + 1
            k3, d3, s3, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k3 >= sqrt:
                print("%d... done" % k3o)
                s3 = u
            else:
                print("%d -> %d" % (k3o, k3))
                a[s3] = 1
                a[s3 + d3] = 1
                s3 += k3 << 1
            del k3o, po

        try:
            a[s2] = 1
            a[s2 + d2] = 1
            s2 += k2 << 1
            a[s2] = 1
            a[s2 + d2] = 1
            s2 += k2 << 1
        except IndexError:
            k2o = k2
            po = p + 1
            k2, d2, s2, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k2 >= sqrt:
                print("%d... done" % k2o)
                s2 = u
            else:
                print("%d -> %d" % (k2o, k2))
                a[s2] = 1
                a[s2 + d2] = 1
                s2 += k2 << 1
            del k2o, po
        iter += 1

    if s2 != u and s3 == u:
        s3 = s2
        d3 = d2
        k3 = k2
    del s2, d2, k2

    while s3 != u:
        try:
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
            a[s3] = 1
            a[s3 + d3] = 1
            s3 += k3 << 1
        except IndexError:
            k3o = k3
            po = p + 1
            k3, d3, s3, p = find_next(p, sqrt, a, usqrt)
            iter += p - po
            if k3 >= sqrt:
                print("%d... done" % k3o)
                s3 = u
            else:
                print("%d -> %d" % (k3o, k3))
                a[s3] = 1
                a[s3 + d3] = 1
                s3 += k3 << 1
            del k3o, po
        iter += 1

    del s3, d3, k3

    print("\n%15d %5.5f %20d\n" % (n, time.time() - start, iter))

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
    compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15)
    out = open("soluz2.txt", "w")
    if gb == 1:
        a = compress.compress((open("soluz.txt", "r").read()).encode()) + compress.flush()
        out.write("1\n" + base64.b64encode(a).decode())
    else:
        inp = open("soluz.txt", "r")
        out.write(str(gb) + "\n")
        div = s // gb
        for i in range(gb - 1):
            st = ""
            for j in range(div):
                st += inp.readlines(div)
            out.write(base64.b64encode(compress.compress(st.replace("\n", ",").encode()) + compress.flush()).decode() + "\n")

        st = ""
        a = inp.readline()
        while a != "":
            st += a
            a = inp.readline()
        out.write(base64.b64encode(compress.compress(st.replace("\n", ",").encode()) + compress.flush()).decode() + "\n")
    sys.stdout.write("done\n")