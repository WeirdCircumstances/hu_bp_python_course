from random import randint

x = int(raw_input("Rate eine Zahl zwischen 0 und 100: ")) 

n = randint(0,100)
i = randint(0,10)
j = randint(0,10)
#k = randint(0,10)
#l = randint(0,10)

while x!=n:
    print 'Leider falsch. Versuche es erneut. Hint: Die Zahl lieg in diesem Bereich: '+ str(n-i) +'-'+ str(n+j)
    x = int(raw_input("Please enter an integer: "))
else:
    print 'Wow! Du solltest Lotto spielen! Das Ergebnis ist richtig.'

