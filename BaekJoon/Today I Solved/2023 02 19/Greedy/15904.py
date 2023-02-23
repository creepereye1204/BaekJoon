m=input()
UCPC=['U','C','P','C']
for i in m:
 if len(UCPC)>0:
     if i==UCPC[0]:
        UCPC=UCPC[1:]
if len(UCPC)==0:
    print('I love UCPC')
else:
    print('I hate UCPC')