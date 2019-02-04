def decrypt(yourarr):
    a=list(map(int, yourarr.split()))
    print("\nThis is your encrypted array", a)
    i=0
    while i<len(a):
        a[i]=int((a[i]-4)/2)
        i+=1

    print("\nThis is your ascii array", a)

    p=0
    while p<len(a):
        a[p]=chr(a[p])
        p+=1
    print("\nThis is now your message in array form:", a)
    print("\nMESSAGE:", *a)



foo = input("Please enter an array in the format----0 0 0 SPACE IS NEEDED BETWEEN EACH DIGIT: ")
decrypt(foo)


