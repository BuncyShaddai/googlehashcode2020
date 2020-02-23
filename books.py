#!/usr/bin/python3
from operator import itemgetter, attrgetter


class library:
    def __init__(self, num, nbook, nsignup, shipcount, books, tscr):
        self.num = num
        self.nbook = nbook
        self.nsignup = nsignup
        self.shipcount = shipcount
        self.books = books
        self.tscr = tscr

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def bubbleSort(books, scores):
    n = len(books)

    for i in range(n):
        for j in range(0, n - i - 1):

            if scores[books[j]] < scores[books[j + 1]]:
                books[j], books[j + 1] = books[j + 1], books[j]


def bksum(books, scores, shipcount):
    sum = 0
    tsr = []
    c = 0
    for bk in books:
        sum += scores[bk]
        if c % shipcount == 0:
            tsr.append(sum)
        c += 1
    return sum


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs



file = open("input5.txt", "r")

line1 = file.readline().strip()

nbooks, nlibs, d = map(int, line1.split())

scores = list(map(int, file.readline().strip().split()))
# print(scores)

scanned_books = [0] * nbooks

libs = []
for i in range(nlibs):
    nbook, nsignup, shipcount = map(int, file.readline().strip().split())
    books = list(map(int, file.readline().strip().split()))
    total = bksum(books, scores, shipcount)
    bubbleSort(books, scores)
    libs.append(library(i, nbook, nsignup, shipcount, books, total))
file.close()
# libs.multisort(key=lambda x: (x.nsignup, x.tscr))
multisort(libs, (("nsignup", False), ("tscr", True)))

# for k in libs:
# print(k)
outfile = open("output.txt", "w")

i = 0
while d > 0 and i < nlibs:
    libno = libs[i].num
    nbok = int(min(libs[i].nbook, d * libs[i].shipcount))
    # print(libno, nbook)
    outfile.write(str(libno))
    outfile.write(" ")
    outfile.write(str(nbok))
    outfile.write("\n")

    ll = []

    # for j in range(nbook):
    #     # print(libs[i].books[j], end=' ')
    #     t = libs[i].books[j]
    #     if ( t not in  scanned_books ):
    #         outfile.write(str(t))
    #         outfile.write(' ')
    #         scanned_books.add(t)
    #     else:
    #         ll.append(t)
    #         left += 1
    # # print()

    j = 0
    left = 0
    scanned = 0
    while scanned < nbok and j < libs[i].nbook:
        t = libs[i].books[j]
        if scanned_books[t] == 0:
            outfile.write(str(t))
            outfile.write(" ")
            scanned_books[t] += 1
            print(t, end=" ")
            scanned += 1
        else:
            ll.append(t)
            print("*", t, end=" ")
            left += 1
        j += 1
    if scanned != nbok:
        for j in range(nbok - scanned):
            outfile.write(str(ll[j]))
            outfile.write(" ")
            scanned_books[ll[j]]  += 1
            print(ll[j], end= ' ')
    print()
    outfile.write("\n")
    d -= libs[i].nsignup
    i += 1

outfile.close()
file = open("output.txt", "r")
data = file.readlines()
file.close()

outfile = open("output.txt", "w")
outfile.write(str(i))
outfile.write("\n")
outfile.writelines(data)

