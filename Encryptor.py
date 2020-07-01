# Encryption Side 

def encrypt(yourstr):
        a=list(yourstr)
        print("\n", a)
        i = 0
        while i<len(yourstr):
                a[i]=(ord(yourstr[i]))
                i+=1
        print("This is your ascii list\n", a)

        b=a
        p=0
        while p<len(yourstr):
                b[p]=((a[p]*2)+4)
                p+=1
        print("\nThis is your encrypted string\n", b)

        print("\nTHIS IS YOUR FINAL ENCRYPTED MESSAGE\n", *b)




enc1 = input("Please enter something you want to encrypt:")
encrypt(enc1)









