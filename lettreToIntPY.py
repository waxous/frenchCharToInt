lettre = ["un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dixsept","dixhuit","dixneuf","vingt","trente","quarante","cinquante","soixante","quatrevingt","cent","mille"]
nombre = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","30","40","50","60","80","100","1000"]

def parse(operand):
    leftValue = 0
    rightValue = 0
    leftCentValue = 0
    middleOrRightCentValue = 0
    rightCentValue = 0
    rightMaxCentValue = 0
    centAfter = 0
    centAfterAfter = 0
    centAfterAfterAfter = 0
    strWithoutMille = 0
    strWithoutMilleIndexZero = 0
    strWithoutMilleIndexUn = 0
    strWithoutMilleIndexDeux = 0
    result = 0

    find = operand.find(lettre[26])

    #Calcule si il y a mille
    if find != -1:
        listWithoutMille = operand.split(lettre[26])
        prevMille = listWithoutMille[0].split()
        afterMille = listWithoutMille[1].split()
        #Ici on calcule toute les possibilite a gauche de mille
        if len(prevMille) <= 1 or prevMille[0] == lettre[19] or prevMille[0] == lettre[20] or prevMille[0] == lettre[21] or prevMille[0] == lettre[22] or prevMille[0] == lettre[23] or prevMille[0] == lettre[24] or prevMille[0] == lettre[25]:
            for i in range (len(lettre)):
                for y in prevMille:
                    if lettre[i] == y:
                        leftValue += int(nombre[i])
                for z in afterMille:
                    if lettre[i] == z:
                        rightValue += int(nombre[i])

        if len(prevMille) == 0:
            leftValue = 1

        if len(prevMille) > 1:
            rightValue = 0
            listValueCent1 = prevMille[0].split()
            listValueCent2 = prevMille[1].split()
            for i in range (len(lettre)):
                for y in listValueCent1:
                    if lettre[i] == y:
                        leftCentValue += int(nombre[i])
                for z in listValueCent2:
                    if lettre[i] == z:
                        middleOrRightCentValue += int(nombre[i])
                for w in afterMille:
                    if lettre[i] == w:
                        rightValue += int(nombre[i])

            if len(prevMille) > 2:
                listValueCent3 = prevMille[2].split()
                for i in range (len(lettre)):
                    for y in listValueCent3:
                        if lettre[i] == y:
                            rightCentValue += int(nombre[i])

            if len(prevMille) > 3:
                listValueCent4 = prevMille[3].split()
                for i in range (len(lettre)):
                    for y in listValueCent4:
                        if lettre[i] == y:
                            rightMaxCentValue += int(nombre[i])

            #Fin du calcule de toute les possibilite a gauche de mille

        if len(afterMille) > 1:
            if afterMille[1] == lettre[25]:
                rightValue = 0
                centAfterMille = afterMille[0].split()
                for i in range (len(lettre)):
                    for y in centAfterMille:
                        if lettre[i] == y:
                            centAfter += int(nombre[i])
                            rightValue += centAfter*100

                if len(afterMille) > 2:
                    valueAfterCentAfterMille = afterMille[2].split()
                    for i in range (len(lettre)):
                        for y in valueAfterCentAfterMille:
                            if lettre[i] == y:
                                centAfterAfter += int(nombre[i])
                                rightValue += centAfterAfter

                if len(afterMille) > 3:
                    valueAfterCentAfterMilleAfter = afterMille[3].split()
                    for i in range (len(lettre)):
                        for y in valueAfterCentAfterMilleAfter:
                            if lettre[i] == y:
                                centAfterAfterAfter += int(nombre[i])
                                rightValue += centAfterAfterAfter

    #Fin du calcule si il y a mille


        if len(prevMille) <= 1 or prevMille[0] == lettre[19] or prevMille[0] == lettre[20] or prevMille[0] == lettre[21] or prevMille[0] == lettre[22] or prevMille[0] == lettre[23] or prevMille[0] == lettre[24] or prevMille[0] == lettre[25]:
            return (int(leftValue)*1000)+(int(rightValue))
        if len(prevMille) == 2 :
            return ((int(leftCentValue)*int(middleOrRightCentValue))*1000)+(int(rightValue))
        if len(prevMille) == 3:
            return (((int(leftCentValue)*int(middleOrRightCentValue))+rightCentValue)*1000)+(int(rightValue))
        if len(prevMille) == 4:
            return (((int(leftCentValue)*int(middleOrRightCentValue))+rightCentValue+rightMaxCentValue)*1000)+(int(rightValue))


    #Calcul si chaine ne contien pas mille
    if find == -1:
        tabSplit = operand.split()
        if len(tabSplit) == 1:
            for i in range (len(lettre)):
                for y in operand.split():
                    if lettre[i] == y:
                        strWithoutMille += int(nombre[i])
            rightValue += strWithoutMille
        if len(tabSplit) > 1:
            if tabSplit[1] != lettre[25]:
                for i in range (len(lettre)):
                    for y in operand.split():
                        if lettre[i] == y:
                            strWithoutMilleIndexZero += int(nombre[i])
                rightValue += strWithoutMilleIndexZero
            if tabSplit[1] == lettre[25]:
                marre = tabSplit[0].split()
                marre1 = tabSplit[1].split()
                for i in range (len(lettre)):
                    for y in marre:
                        if lettre[i] == y:
                            strWithoutMille += int(nombre[i])
                    for z in marre1:
                        if lettre[i] == z:
                            strWithoutMilleIndexZero += int(nombre[i])
                rightValue = strWithoutMille*strWithoutMilleIndexZero

            if len(tabSplit) > 2 and tabSplit[1] == lettre[25]:
                marre2 = tabSplit[2].split()
                for i in range (len(lettre)):
                    for y in marre2:
                        if lettre[i] == y:
                            strWithoutMilleIndexUn += int(nombre[i])
                rightValue += strWithoutMilleIndexUn

            if len(tabSplit) > 3:
                marre3 = tabSplit[3].split()
                for i in range (len(lettre)):
                    for y in marre3:
                        if lettre[i] == y:
                            strWithoutMilleIndexDeux += int(nombre[i])
                rightValue += strWithoutMilleIndexDeux
    #Fin du calcul si il n'y a pas cent

        for i in range (len(tabSplit)):
            if tabSplit[i] != lettre[26]:
                return rightValue
