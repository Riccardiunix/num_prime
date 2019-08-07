import time
import sys
import math
import bitarray
import base64
import zlib


def find_value(it, a4, a5, a7):
    h = int(round(it))
    if a4 == 0 or a5 == 0 or a7 == 0:
        h -= 2
    if h % 2 == 0:
        return h + 1
    return h


def fix_data(k, i, iter_t):
    data = [round(k * 1.6), round((k << 3) / 3.0), round(k * 3.2), round(k * (704.0 / 165.0)), round(k * 4.8),
            round(k * (968.0 / 165.0)), round(k * (24673.0 / 3300.0)), k << 3]
    lpos = 0
    inte = 6
    for l in range(8):
        pos = data[l] + i
        inte += const * (pos - lpos)
        lpos = pos
        res4 = (pos - 4) % 8
        res5 = (pos - 5) % 8
        res7 = (pos - 7) % 8
        j = find_value(inte, res4, res5, res7)
        if j % k != 0:
            intep = inte + const
            jp = find_value(intep, (res4 + 1) % 8, (res5 + 1) % 8, (res7 + 1) % 8)
            intel = inte - const
            jl = find_value(intel, (res4 - 1) % 8, (res5 - 1) % 8, (res7 - 1) % 8)
            if jl % k == 0:
                data[l] -= 1
            elif jp % k == 0:
                data[l] += 1
            else:
                st = True
                sp = int(round(k / 100.0)) - 3
                intep += (sp - 1) * const
                res4p = (res4 + sp) % 8
                res5p = (res5 + sp) % 8
                res7p = (res7 + sp) % 8
                intel -= (sp - 1) * const
                res4l = (res4 - sp) % 8
                res5l = (res5 - sp) % 8
                res7l = (res7 - sp) % 8
                while st:
                    jp = find_value(intep, res4p, res5p, res7p)
                    jl = find_value(intel, res4l, res5l, res7l)
                    if jl % k == 0:
                        st = False
                        data[l] -= sp
                    elif jp % k == 0:
                        st = False
                        data[l] += sp
                    else:
                        sp += 1
                        intep += const
                        res4p = (res4p + 1) % 8
                        res5p = (res5p + 1) % 8
                        res7p = (res7p + 1) % 8
                        intel -= const
                        res4l = (res4l - 1) % 8
                        res5l = (res5l - 1) % 8
                        res7l = (res7l - 1) % 8
                    iter_t[0] += 1
        iter_t[0] += 1
        try:
            a[data[l] + i] = 1
        except IndexError:
            l = 8
    return data


if __name__ == "__main__":
    const = 3.749999999999999

    try:
        u = int(sys.argv[1])
    except IndexError:
        u = 100000
    n = int((u << 2) / 15.0) + 1

    sys.stdout.write("Array... "), sys.stdout.flush()
    a = bitarray.bitarray(n)
    a.setall(0)
    sys.stdout.write("done\n")

    iter_tot = [0]
    start = time.time()

    s7, i7 = 0, 1
    s11, i11 = 1, 1
    s13, i13 = 2, 1
    s17, i17 = 3, 1
    s19, i19 = 4, 1
    s23, i23 = 5, 1
    s29, i29 = 6, 1
    s31, i31 = 7, 1

    sys.stdout.write("7, 11, 13, 17, 19, 23, 29, 31... "), sys.stdout.flush()
    while i7 or i11 or i13 or i17 or i23 or i29 or i31:
        if i7:
            try:
                for i in range(18):
                    a[s7+12] = 1
                    a[s7+19] = 1
                    a[s7+23] = 1
                    a[s7+30] = 1
                    a[s7+34] = 1
                    a[s7+41] = 1
                    a[s7+53] = 1
                    a[s7+56] = 1
                    s7 += 56
            except IndexError:
                del s7
                i7 = 0
        if i11:
            try:
                for i in range(12):
                    a[s11+18] = 1
                    a[s11+30] = 1
                    a[s11+36] = 1
                    a[s11+47] = 1
                    a[s11+53] = 1
                    a[s11+65] = 1
                    a[s11+83] = 1
                    a[s11+88] = 1
                    s11 += 88
            except IndexError:
                del s11
                i11 = 0
        if i13:
            try:
                for i in range(10):
                    a[s13+21] = 1
                    a[s13+35] = 1
                    a[s13+42] = 1
                    a[s13+55] = 1
                    a[s13+62] = 1
                    a[s13+76] = 1
                    a[s13+97] = 1
                    a[s13+104] = 1
                    s13 += 104
            except IndexError:
                del s13
                i13 = 0
        if i17:
            try:
                for i in range(8):
                    a[s17+27] = 1
                    a[s17+45] = 1
                    a[s17+54] = 1
                    a[s17+73] = 1
                    a[s17+82] = 1
                    a[s17+100] = 1
                    a[s17+127] = 1
                    a[s17+136] = 1
                    s17 += 136
            except IndexError:
                del s17
                i17 = 0
        if i19:
            try:
                for i in range(7):
                    a[s19+30] = 1
                    a[s19+50] = 1
                    a[s19+60] = 1
                    a[s19+81] = 1
                    a[s19+91] = 1
                    a[s19+111] = 1
                    a[s19+141] = 1
                    a[s19+152] = 1
                    s19 += 152
            except IndexError:
                del s19
                i19 = 0
        if i23:
            try:
                for i in range(6):
                    a[s23+36] = 1
                    a[s23+61] = 1
                    a[s23+73] = 1
                    a[s23+98] = 1
                    a[s23+110] = 1
                    a[s23+135] = 1
                    a[s23+171] = 1
                    a[s23+184] = 1
                    s23 += 184
            except IndexError:
                del s23
                i23 = 0
        if i29:
            try:
                for i in range(5):
                    a[s29+47] = 1
                    a[s29+78] = 1
                    a[s29+93] = 1
                    a[s29+124] = 1
                    a[s29+139] = 1
                    a[s29+170] = 1
                    a[s29+217] = 1
                    a[s29+232] = 1
                    s29 += 232
            except IndexError:
                del s29
                i29 = 0
        if i31:
            try:
                for i in range(4):
                    a[s31+49] = 1
                    a[s31+82] = 1
                    a[s31+99] = 1
                    a[s31+132] = 1
                    a[s31+149] = 1
                    a[s31+182] = 1
                    a[s31+231] = 1
                    a[s31+248] = 1
                    s31 += 248
            except IndexError:
                del s31
                i31 = 0
        iter_tot[0] += 1
    del i7, i11, i13, i17, i19, i23, i29, i31
    sys.stdout.write("done (%d)\n" % iter_tot[0])

    sqtn = int(round(math.sqrt(u)))
    sqt = ((sqtn << 2) / 15.0) - 1

    k = 37
    data = [60, 99, 119, 158, 178, 217, 277, 296]
    s = 8 + data[-1]

    k1 = 41
    data1 = [66, 110, 132, 175, 197, 241, 307, 328]
    s1 = 9 + data1[-1]

    k2 = 43
    data2 = [69, 115, 138, 183, 206, 252, 321, 344]
    s2 = 10 + data2[-1]

    i = 10
    il = 10
    inter = 43.49999999999999
    r4 = 6
    r5 = 5
    r7 = 3

    while s != sqtn and s1 != sqtn and s2 != sqtn:
        try:
            for add in data:
                a[s + add] = 1
            s += data[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += (i - il)
            if i < sqt:
                ko = k
                inter += (i - il) * const
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k))
                data = fix_data(k, i, iter_tot)
                s = i + data[-1]
                il = i
            else:
                s = sqtn

        try:
            for add in data1:
                a[s1 + add] = 1
            s1 += data1[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += (i - il)
            if i < sqt:
                ko = k1
                inter += (i - il) * const
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k1 = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k1))
                data1 = fix_data(k1, i, iter_tot)
                s1 = i + data1[-1]
                il = i
            else:
                s1 = sqtn

        try:
            for add in data2:
                a[s2 + add] = 1
            s2 += data2[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += (i - il)
            if i < sqt:
                ko = k2
                inter += (i - il) * const
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k2 = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k2))
                data2 = fix_data(k2, i, iter_tot)
                s2 = i + data2[-1]
                il = i
            else:
                s2 = sqtn
        iter_tot[0] += 1

    if s1 == sqtn:
        s1 = s2
        data1 = data2
    if s == sqtn:
        s = s2
        data = data2
    del s2, data2

    while s != sqtn and s1 != sqtn:
        try:
            for add in data:
                a[s + add] = 1
            s += data[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += i - il
            if i < sqt:
                ko = k
                inter += (i - il) * const
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k))
                data = fix_data(k, i, iter_tot)
                s = i + data[-1]
                il = i
            else:
                s = sqtn

        try:
            for add in data1:
                a[s1 + add] = 1
            s1 += data1[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += (i - il)
            if i < sqt:
                ko = k1
                inter += (i - il) * const
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k1 = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k1))
                data1 = fix_data(k1, i, iter_tot)
                s1 = i + data1[-1]
                il = i
            else:
                s1 = sqtn
        iter_tot[0] += 1

    if s == sqtn:
        s = s1
        data = data1
    del s1, data1

    while s != sqtn:
        try:
            for add in data:
                a[s + add] = 1
            s += data[-1]
        except IndexError:
            i += 1
            while i < sqt and a[i] != 0:
                i += 1
            iter_tot[0] += (i - il)
            if i < sqt:
                ko = k
                inter += (i - il) * const
                k = int(round(inter))
                r4 = (r4 + i - il) % 8
                r5 = (r5 + i - il) % 8
                r7 = (r7 + i - il) % 8
                k = find_value(inter, r4, r5, r7)
                print("%d -> %d" % (ko, k))
                data = fix_data(k, i, iter_tot)
                il = i
            else:
                s = sqtn
        iter_tot[0] += 1

    print("\n%15d %5.5f %20d\n" % (u, (time.time() - start), iter_tot[0]))
    del data

    sys.stdout.write("Scrittura... "), sys.stdout.flush()
    s = 1
    tot = 3
    out = open("soluz.txt", "w")
    cont1 = 0
    cont0 = 0
    for i in range(n):
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
                tot += cont1
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

    print("\t %d" % tot)

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