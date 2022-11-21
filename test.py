import random

ph = str(random.randint(500,900)/100)
pao2 = str(random.randint(60,190)/10)
paco2 = str(random.randint(30,90)/10)
hco3 = str((random.randint(10, 35)))

print("pH = " + ph, ", pO2 = " + pao2,",pCO2 = " + paco2,", HCO3- = " + hco3)

print()
continoue = input("INTERPRET ABG RESULTS, WHEN READY TO TEST TYPE 'YES': ")
print()

if continoue.upper() == 'YES':
    result = ["RESPIRATORY ACIDOSIS", "RESPIRATORY ACIDOSIS WITH METABOLIC COMPENSATION", "METABOLIC ACIDOSIS",
              "METABOLIC ACIDOSIS WITH RESPIRATORY COMPENSATION", "RESPIRATORY ALKALOSIS",
              "RESPIRATORY ALKALOSIS WITH METABOLIC COMPENSATION", "METABOLIC ALKALOSIS",
              "METABOLIC ALKALOSIS WITH RESPIRATORY COMPENSATION", "MIXED RESPIRATORY AND METABOLIC ACIDOSIS",
              "MIXED RESPIRATORY AND METABOLIC ALKALOSIS", "NONE OF THE ABOVE"]
    for i in range(0, len(result)):
        print(i + 1, result[i])
    print()
    student = input('WHAT IS YOUR INTERPRETATION?: ')
else:
    quit()

ph = float(ph)
paco2 = float(paco2)
pao2 = float(pao2)
hco3 = float(hco3)

if ph < 7.35 and paco2 >= 6 and 22 < hco3 < 26:
    answer = 1
elif ph < 7.35 and paco2 >= 6 and hco3 >= 26:
    answer = 2
elif ph < 7.35 and 4.7 < paco2 < 6 and hco3 <= 22:
    answer = 3
elif ph < 7.35 and paco2 <= 4.7 and hco3 <= 22:
    answer = 4
elif ph > 7.45 and paco2 <= 4.7 and 22 < hco3 < 26:
    answer = 5
elif ph > 7.45 and paco2 <= 4.7 and hco3 <= 22:
    answer = 6
elif ph > 7.45 and hco3 >= 26 and 4.7 < paco2 < 6:
    answer = 7
elif ph > 7.45 and hco3 >= 26 and paco2 >= 6:
    answer = 8
elif ph <= 7.35 and paco2 >= 6 and hco3 <= 22:
    answer = 9
elif ph >= 7.45 and paco2 <= 4.7 and hco3 >= 26:
    answer = 10
else:
    answer = 11

print()

if int(answer) == int(student):
    print('CORRECT !!')
else:
    print('GOOD TRY''\n'"UNFORTUNATELY THAT IS NOT CORRECT")
print()
info = input("WOULD YOU LIKE A BREAKDOWN OF THE ABG 'YES': ")
print()

if info.upper() != 'YES':
    quit()

print(result[answer - 1])

if ph <= 4 and 5.5 < pco2 < 6.8:
    print("Type 1 respiratory failure")
if pao2 <= 4 and pco2 >= 6.8:
    print("Type 2 respiratory failure")


if ph <= 7.35:
    print("pH IS ACIDIC ")
elif 17.351 < ph < 7.45:
    print("pH IS NORMAL")
else:
    print("pH IS ALKALOTIC")

if pao2 <= 11:
    print("O2 STATUS LOW - Hypxoemic ")
elif 11 < pao2 < 13:
    print("O2 STATUS NORMAL")
else:
    print("O2 STATUS HIGH")


if paco2 <= 4.7:
    print("CO2 STATUS LOW - Hypocapnic ")
elif 4.7 < paco2 < 6:
    print("CO2 STATUS NORMAL")
else:
    print("CO2 STATUS HIGH - Hypercapnic")


if hco3 <= 22:
    print("BICARBONATE LOW")
elif 22 < hco3 < 26:
    print("BICARBONATE NORMAL")
else:
    print("BICARBONATE HIGH")


