# 13:00 onsdag 24/8
# 0.5 Skapa projekt
# 0.55 ;) Med objekt - HockeyPlayer ju
# 0.6 Kör upp på github
# 1. Branch -> skapa bubbleSort
# 2. Branch -> skapa selSort
# ev 3. Branch -> skapa insertionSort
# 4. Gå tillbaka till bubbleSort och lägg till tajming
# 5. Gå tillbaka till selSort och lägg till tajming
# Vi kör denna kodsession MAX till 14:30 !!

class Player:
    def __init__(self, namn, age):
        self.Namn = namn
        self.Age = age

    def __repr__(self):
        return f"{self.Namn} {self.Age}"

arrayen = [ Player("Stefan",50), Player("Kalle",13), Player("Lisa",28), Player("Anna",52), Player("Oliver",14) ]

# Enkel algoritm:
# Gå igenom alla element X i listan:
# Om X är mindre än elementet till vänster om den:
# Ta ut X ur listan
# Leta till vänster till vi hittar något mindre än X
# Göra en “insert” på X på det nya platsen
# [ 5, 14, 50,  33  ]
#   0   1   2   3   
# index = 3
def insertionSort(arrayen):
    for index in range(1,len(arrayen)):
        vardeInnan = arrayen[index-1] # Stefan 50
        x = arrayen[index] # Kalle 13
        if x.Age < vardeInnan.Age:
            del arrayen[index]
            indexOfLower = 0
            for  leftLoopIndex in range(index-1,0,-1):
                if arrayen[leftLoopIndex].Age < x.Age:
                    indexOfLower = leftLoopIndex + 1
                    break
            arrayen.insert(indexOfLower,x)


def main():
    insertionSort(arrayen)
    print(arrayen)

if __name__ == "__main__":
    main()




#          0 1 2 3 4 5 6 7 8 9   POSITION

# Göra n antal genomgångar av listan: n = 10
# i = for i in range(0,n)
# För varje par element i och i+1 i listan:
# Om listan[i] < listan[i+1]:
# Byta plats på listan[i] och listan[i+1]
# Varje element “bubblar upp” till rätt plats



# En förbättring över bubble sort:
# Göra n antal genomgångar av listan:
# Leta efter den minsta element i listan:
# Flytta den till först platsen
# Sedan näst-minst, näst-näst-minst osv




# # # NÄR TAR VI KOSTNADEN?
# # - lägenhet 
# # 1. Casha hela insatsen 500000
# # - per månad  avgiften 1100

# # 2. Casha 100000
# #     - per månad avgift 1100 + ränta/amt 2000 (400000)


# #         1  2   3   4    5   6   7    8     9    10  11
# #Start läser in data från fil
# array = [11231232,3345,500,600,73216,1111,1112,1113,1114,2000,3099]
# sort array - ta lång tid!!!!! 

# BINÄRSÖK = SJUKT SNABBT !!! Skalar bra!!
# #for O(n) 