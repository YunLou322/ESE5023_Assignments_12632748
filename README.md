# ESE5023_Assignments_12632748

Comments on HW1 Liyl(101/100)

You write your solving thoughts in detail in .pdf, good!(+2p)
Only .ipynb also is OK, you DON'T change into .py. Thanks.

1-2: A small error,"M3[i,j]=M1[i,k]*M2[k,j]" should be changed as M3[i,j]+=M1[i,k]*M2[k,j].
Need corrsponding rows and columns multiple and add. (-3p)

1-3: Good job!(+2p)

1-4: you listed all your calculated results ,that's right.
But there is a more smart method.Reverse thinking, for x, 
if x is even, divide by 2; if x is odd, make it even first(minus 1),
then divide. if Please reference:
    def Least_moves(x):
        moves = 0
        while x > 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = x - 1
            moves = moves + 1
        print(moves)
    print("Least_moves(10):")
    Least_moves(10)
    
1-5:
5.1 Good job! YOU ARE SO SMART!(+2p)
5.2 You don't plot.(-2p)

