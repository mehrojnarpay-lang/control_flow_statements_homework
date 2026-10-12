def main(a):

    x=abs(a)
    teskari=(x % 10)*10+x//10
    return teskari<=x
print(main(57)) 
print(main(21)) 