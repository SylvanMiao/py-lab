if __name__=="__main__":
    print("More Mountain Game")
    print("Game Begin")
    pc=cc=0
    g=1

    while True:
        print("No.%2d game" %g)
        print("How many mountains are there?")
        n=int(input())
        if not n :
            break
        k=int(input("how many mountains are allowed to be moved each time?"))
        while (k>n or k<1):
            if k>n or k<1:
                print("repeat again")
        while n:
            x=int(input("how many mountains do you want to move this time?"))
            if (x>n or x>k or x<1):
                print("illegal,again please")
                continue
            n-=x
            print("there are %2d mountains left now" %n)
            if not n:
                print("you won i failed")
                print(" ")
                cc+=1
            else:
                y=(n-1)%(k+1)
                if not y:
                    y=1
                n-=y
                print("computer moved %2d mountains away" %y)

                if n:
                    print(" there are %2d mountains left now " %n)
                else:
                    print("i won you failed")
                    pc+=1
        g+=1
    print("total game times: %2d" %g)
    print("computer won %2d times, you won %2d times" %(pc,cc))
