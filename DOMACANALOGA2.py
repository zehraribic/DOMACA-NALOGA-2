
print('Hello users! This program will convert km to miles.')


#vnasanje števila v km


number_km = int(input("Enter the number!"))
print ('Vrednost pretvorjena v milje:',
       0.621 * number_km )


#vprasaj uporabnika ce zeli nadaljevati


answer = "yes"
while answer == "yes":
    answer = input("Do You wAnt to coNtiNue? (Yes/No) ").lower()

    if answer == "yes":
        number_km = int(input("Vnesite željeno številko v kilometrih!"))
        print ('Vrednost pretvorjena v milje:',0.621 * number_km )

    else:
        print('Thank you! Have a nice day, bay!')









##domaca naloga st.: 2##


x=1
#fizz deljivo s 3
#buzz deljivo s 5
stevilo = int(input('Enter the number from 1 to 100:'))
while x <= stevilo:
    if x % 5 == 0 and x % 3 == 0:
        print ('fizz_buzz')
    elif x % 3 == 0:
        print ('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print (x)
    x= x + 1



