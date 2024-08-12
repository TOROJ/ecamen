
def elementosRep(s):

    for i in range (len(s)):
     print(s.count(s[i]))
     if (s.count(s[i])==1):
        return "no se repite"
     else:
        return"se repite"

def main():
    s=[1,2,3,4,5,9]
    print (elementosRep(s))
if __name__=="__main__":
    main()
