def Mediana(s):
    c=int(len (s)/2)
    return s[c:c+1]
def main():
    s=[1,2,3,4,5,9,10]
    print (Mediana(s))
if __name__=="__main__":
    main()
