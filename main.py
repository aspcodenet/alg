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

arrayen = [ Player("Stefan",50),Player("Kalle",13), Player("Lisa",28), Player("Anna",52), Player("Oliver",14) ]

# Göra n antal genomgångar av listan: n = 10
# i = for i in range(0,n)
# För varje par element i och i+1 i listan:
# 12 4 16 7      indewx = 0
# 4  12 16 7 indewx = 1
# Om listan[index] < listan[index+1]:
# Byta plats på listan[i] och listan[i+1]
# Varje element “bubblar upp” till rätt plats
def bubbleSort(arrayen):
    for index in range(0,len(arrayen)):
        print(arrayen)    
        for pairStart in range(0,len(arrayen)-1-index):
            firstObject = arrayen[pairStart]
            secondObject = arrayen[pairStart+1]
            if firstObject.Age > secondObject.Age:
                temp = arrayen[pairStart]
                arrayen[pairStart] = arrayen[pairStart+1]
                arrayen[pairStart+1] = temp
                #arrayen[pairStart], arrayen[pairStart+1] = arrayen[pairStart+1],arrayen[pairStart]

def main():
    bubbleSort(arrayen)
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