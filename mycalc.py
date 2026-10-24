
#there could be some comments helping the dev so ignore them

print ("calculator for my dad") #prints the title
print ("choose an action")
print ("1. add")
print ("2. subtract")
print ("3. multiply")#action thingi

main = input ()

if main == "1":
    print ("first digit plz")
    a = float(input())
    print ("bro forgot the second digit")
    b = float(input())
    print ("answer:", a + b)

elif main == "2":
    print ("first digit plz")
    c = float(input())
    print ("second digit as always")
    d = float(input())
    print ("answer:", c - d)

elif main == "3":
    print ("first digit plz")
    e = float(input())
    print ("second digit as always")
    f = float(input())
    print ("answer:", e * f)

else:
    print ("bro chose an invalid action 💀")
