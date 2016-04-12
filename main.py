import re
from lettreToIntPY import parse

special = ["deux","trois","quatre","cinq","six","sept","huit","neuf"]

chaine = input("Entrez un calcul: ")
chaine = chaine.lower()
chaine = re.sub("0","o",chaine)
chaine = re.sub("1","i",chaine)
chaine = re.sub("2","r",chaine)
chaine = re.sub("3","e",chaine)
chaine = re.sub("4","a",chaine)
chaine = re.sub("5","s",chaine)
chaine = re.sub("6","g",chaine)
chaine = re.sub("7","t",chaine)
chaine = re.sub("8","b",chaine)
chaine = re.sub("9","g",chaine)
chaine = re.sub(" et "," ",chaine)
chaine = re.sub("dix-sept","dixsept",chaine)
chaine = re.sub("dix-huit","dixhuit",chaine)
chaine = re.sub("dix-neuf","dixneuf",chaine)
for i in range (len(special)):
    chaine = re.sub("vingt-"+special[i],"vingt ",chaine)
for i in range (len(special)):
    chaine = re.sub("trente-"+special[i],"trente ",chaine)
for i in range (len(special)):
    chaine = re.sub("quarante-"+special[i],"quarante ",chaine)
for i in range (len(special)):
    chaine = re.sub("cinquante-"+special[i],"cinquante ",chaine)
for i in range (len(special)):
    chaine = re.sub("soixante-"+special[i],"soixante ",chaine)
for i in range (len(special)):
    chaine = re.sub("quatre-vingt-"+special[i],"quatrevingt ",chaine)
chaine = re.sub("quatre-vingt","quatrevingt ",chaine)
chaine = re.sub('quatre vingt','quatrevingt',chaine)
chaine = re.sub('\-',' - ',chaine)
chaine = re.sub('\+',' + ',chaine)
chaine = re.sub('\%',' % ',chaine)
chaine = re.sub('\*',' * ',chaine)

signParse = []
for chaineC in range (len(chaine)):
    if chaine[chaineC] == "-" or chaine[chaineC] == "+" or chaine[chaineC] == "*" or chaine[chaineC] == "%":
        sign = chaine[chaineC]
        signParse.append(sign)
        chaine42 = re.sub("\-",'42',chaine)
        chaine42 = re.sub("\+",'42',chaine42)
        chaine42 = re.sub("\*",'42',chaine42)
        chaine42 = re.sub("\%",'42',chaine42)
signParse.append("")
chaineParse = chaine42.split("42")

tabFinal = []
for i in range (len(chaineParse)):
    value = parse(chaineParse[i])
    finalValue = value,signParse[i]
    tabFinal.append(finalValue)

lastTab = []
for i in range (len(tabFinal)):
    final = ','.join(map(str,tabFinal[i]))
    final = re.sub("\,","",final)
    lastTab.append(final)

print "".join(lastTab),"\n",eval("".join(lastTab))
