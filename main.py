#1-misol
xarajatlar = []

def qoshish(sana, kategoriya, summa):
    xarajatlar.append({"sana": sana, "kategoriya": kategoriya, "summa": summa})

def statistika():
    jami = {}
    for x in xarajatlar:
        jami[x["kategoriya"]] = jami.get(x["kategoriya"], 0) + x["summa"]
    print("Kategoriya bo‘yicha xarajatlar:", jami)

qoshish("2026-01-01", "Oziq-ovqat", 50000)
qoshish("2026-01-02", "Transport", 20000)
statistika()

#2-misol
def tekshir(s):
    for i in range(9):
        if len(set(s[i])) != 9:
            return False
        if len(set(s[j][i] for j in range(9))) != 9:
            return False
    return True

sudoku = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

print("To‘g‘ri" if tekshir(sudoku) else "Noto‘g‘ri")

#3-misol
from collections import Counter

matn = input("Matn kiriting: ").lower()
sozlar = matn.split()
jumlalar = matn.split(".")

print("So‘zlar soni:", len(sozlar))
print("O‘rtacha so‘z uzunligi:", sum(len(s) for s in sozlar)/len(sozlar))
print("Eng ko‘p ishlatilgan so‘zlar:", Counter(sozlar).most_common(3))

#4-misol
javoblar = {
    "salom": "Salom! Qanday yordam beray?",
    "isming": "Men mini chatbotman",
    "xayr": "Xayr! Omad!"
}

while True:
    savol = input("Siz: ").lower()
    if savol == "xayr":
        print("Bot:", javoblar["xayr"])
        break
    print("Bot:", javoblar.get(savol, "Tushunmadim"))

#5-misol
doska = [" "] * 9

def chiz():
    print(doska[0:3])
    print(doska[3:6])
    print(doska[6:9])

def yutdi(b):
    g = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[c]==b[d]!=" " for a,c,d in g)

for i in range(9):
    chiz()
    p = "X" if i % 2 == 0 else "O"
    joy = int(input(f"{p} joy (0-8): "))
    doska[joy] = p
    if yutdi(doska):
        chiz()
        print(p, "yutdi!")
        break
