def promedio(s):
    c=0
    for i in range (len(s)):
     c+=s[i]
    d=len(s)
    return c/d
def main():
    s=[1,2,3,4,5,9]
    print (promedio(s))
if __name__=="__main__":
    main()
