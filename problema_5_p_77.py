'''Într-un fişier sunt înscrise caractere arbitrare. Elaboraţi un program
care afişează pe ecran numărul vocalelor din fişier.
'''
a=open('C:/Users/moonb/OneDrive/Desktop/file.txt', 'r')
b=a.read()
c=[]
d=0
a.close()
for i in range(0,len(b)):
    if b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u' or b[i]=='A' or b[i]=='E' or b[i]=='I' or b[i]=='O' or b[i]=='U':
      c.append(b[i])
      d+=1

print('sunt',d,'vocale: ',c)
