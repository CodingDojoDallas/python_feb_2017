#part 1
# def draw_stars(x):
#     newArr = []
#     for i in x:
#         newArrSub = []
#         count = 1
#         while count <= i:
#             newArrSub.append("*")
#             count += 1
#         print newArrSub
# y = [4,6,1,3,5,7,25]
# draw_stars(y)
# #part 2
def drawStars2(x):
    newArr = []
    for i in x:
        newArrSub = []
        if isinstance(i, str):
            i = i.lower()
            count = 1
            while count <= len(i):
                count += 1
                newArrSub.append(i[0])
            print newArrSub
        elif isinstance(i, int):
            count = 1
            while count <= i :
                count +=1
                newArrSub.append("*")
            print newArrSub


x = [4,"Tom",1,"Micheal",5,7,"Jimmy Smith"]
drawStars2(x)
