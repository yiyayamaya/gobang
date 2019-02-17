import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(0)
cengshu=0


#don't change the class name
class AI(object):
#chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
#You are white or black
        global COLOR_BLACK
        global COLOR_WHITE

        self.color = color
        if self.color==COLOR_BLACK:
            COLOR_BLACK = -1
            COLOR_WHITE = 1
        else:
            COLOR_BLACK=1
            COLOR_WHITE =-1


 #the max time you should use, your algorithm's run time must not exceed the timelimit.
        self.time_out = time_out
 # You need add your decision into your candidate_list. System will get the end ofyour candidate_list as your decision .
        self.candidate_list = []


 # The input is current chessboard.
    def go(self, chessboard):

        print("新的一步")
        #print("刚刚执行go\n",chessboard)

        self.candidate_list.clear()

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))  # 以上2行获取空的位置

        pos_idx = random.randint(0, len(idx) - 1)
        new_pos = idx[pos_idx]
        self.candidate_list.append(new_pos)  # 最最最开始随便空位置下一个



        global max1,max2,max3,max1i,max1j,max2i,max2j,max3i,max3j #极值 不一定是极大还是极小
        goonce(self, chessboard,-1,1) #AI的第一人称 本AI是1 敌人是-1

        print("在外面",max1,max2,max3,max1i,max1j,max2i,max2j,max3i,max3j)

        #print(chessboard)#此时ai走的步还未出现在棋盘




        chessboardson1=chessboard.copy()
        chessboardson2=chessboard.copy()
        chessboardson3=chessboard.copy()

        chessboardson1[max1i][max1j] = 1
        chessboardson2[max2i][max2j] = 1
        chessboardson3[max3i][max3j] = 1
        erzilist=[]
        print("儿子1",chessboardson1)
        goonce(self, chessboardson1,1,-1)
        print(max1, max2, max3, max1i, max1j, max2i, max2j, max3i, max3j)
        chessboardson1_1 = chessboardson1.copy()
        chessboardson1_2 = chessboardson1.copy()
        chessboardson1_3 = chessboardson1.copy()
        chessboardson1_1[max1i][max1j] = -1
        chessboardson1_2[max2i][max2j] = -1
        chessboardson1_3[max3i][max3j] = -1
        sunzilist=[]
        print("孙子1_1\n",chessboardson1_1)
        goonce(self, chessboardson1_1, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子1_2\n",chessboardson1_2)
        goonce(self, chessboardson1_2, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子1_3\n",chessboardson1_3)
        goonce(self, chessboardson1_3, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子list",sunzilist,sunzilist.index(max(sunzilist)))
        indexofsunzi=sunzilist.index(max(sunzilist))
        erzilist.append(sunzilist[indexofsunzi])



        print("儿子2",chessboardson2)
        goonce(self, chessboardson2,1,-1)
        print( max1, max2, max3, max1i, max1j, max2i, max2j, max3i, max3j)
        chessboardson2_1 = chessboardson2.copy()
        chessboardson2_2 = chessboardson2.copy()
        chessboardson2_3 = chessboardson2.copy()
        chessboardson2_1[max1i][max1j] = -1
        chessboardson2_2[max2i][max2j] = -1
        chessboardson2_3[max3i][max3j] = -1
        sunzilist = []
        print("孙子2_1\n", chessboardson2_1)
        goonce(self, chessboardson2_1, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子2_2\n", chessboardson2_2)
        goonce(self, chessboardson2_2, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子2_3\n", chessboardson2_3)
        goonce(self, chessboardson2_3, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子list", sunzilist, sunzilist.index(max(sunzilist)))
        indexofsunzi = sunzilist.index(max(sunzilist))
        erzilist.append(sunzilist[indexofsunzi])

        print("儿子3",chessboardson3)
        goonce(self, chessboardson3,1,-1)
        print( max1, max2, max3, max1i, max1j, max2i, max2j, max3i, max3j)
        chessboardson3_1 = chessboardson3.copy()
        chessboardson3_2 = chessboardson3.copy()
        chessboardson3_3 = chessboardson3.copy()
        chessboardson3_1[max1i][max1j] = -1
        chessboardson3_2[max2i][max2j] = -1
        chessboardson3_3[max3i][max3j] = -1
        sunzilist = []
        print("孙子3_1\n", chessboardson3_1)
        goonce(self, chessboardson3_1, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子3_2\n", chessboardson3_2)
        goonce(self, chessboardson3_2, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子3_3\n", chessboardson3_3)
        goonce(self, chessboardson3_3, -1, 1)
        print(max1)
        sunzilist.append(max1)
        print("孙子list", sunzilist, sunzilist.index(max(sunzilist)))
        indexofsunzi = sunzilist.index(max(sunzilist))
        erzilist.append(sunzilist[indexofsunzi])

        print(erzilist)
        indexoferzi=erzilist.index(min(erzilist))
        print(indexoferzi)

        goonce(self, chessboard, -1, 1)

        self.candidate_list.clear()
        if indexoferzi==0:
            self.candidate_list.append((max1i,max1j))
        elif indexoferzi==1:
            self.candidate_list.append((max2i, max2j))
        elif indexoferzi==2:
            self.candidate_list.append((max3i, max3j))
        self.candidate_list
        print(self.candidate_list)























def goonce(self, chessboard,enemycolor,mycolor): #此方法只用于得到棋盘上三处最大value以及位置 不应修改外部变量


    print("新的一个value判断")
    valueboard=np.zeros((self.chessboard_size, self.chessboard_size), dtype=np.int)


    idx2 = np.where(chessboard == enemycolor)#得到敌人的点
    idx2 = list(zip(idx2[0], idx2[1]))


    idx3 = np.where(chessboard == mycolor)#得到自己的点
    idx3 = list(zip(idx3[0], idx3[1]))


    #print(idx2,idx3)

    for i in idx2:#扫描敌人棋子



        #一个子也堵 1分

        danyi(-1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(-1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(-1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(0, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)
        danyi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size,enemycolor)

        daner(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)


        daner(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        daner(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)








        dansan(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansan(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansan(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansan(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)


        tiaosan(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(0, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(-2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(-2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        tiaosan(-2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)

        dansi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)
        dansi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, enemycolor,mycolor,enemycolor)

    for i in idx3:#扫描自己棋子

        daner(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)

        daner(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        daner(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)







        dansan(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansan(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansan(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansan(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)

        tiaosan(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(0, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(-2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(-2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        tiaosan(-2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)

        dansi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)
        dansi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, mycolor,mycolor,enemycolor)



    print("valueboard:\n",valueboard)


    global max1,max2,max3,max1i,max1j,max2i,max2j,max3i,max3j
    if enemycolor==1:
        max1, max2, max3, max1i, max1j, max2i, max2j, max3i, max3j=getmaxofvalueboard(valueboard)
    elif enemycolor==-1:
        max1, max2, max3, max1i, max1j, max2i, max2j, max3i, max3j = getminofvalueboard(valueboard)






def getmaxofvalueboard(valueboard):

    maxyi=0# 第一大
    maxyii=0
    maxyij=0

    maxer=0
    maxeri = 0
    maxerj = 0

    maxsan=0
    maxsani = 0
    maxsanj = 0
    for i in range(15):
        for j in range(15):
            if valueboard[i][j]>maxyi:
                maxyi=valueboard[i][j]
                maxyii=i
                maxyij=j
    valueboard2=valueboard.copy()
    valueboard2[maxyii][maxyij]=0
    for i in range(15):
        for j in range(15):
            if valueboard2[i][j]>maxer:
                maxer=valueboard[i][j]
                maxeri=i
                maxerj=j
    valueboard3 = valueboard2.copy()
    valueboard3[maxeri][maxerj] = 0
    for i in range(15):
        for j in range(15):
            if valueboard3[i][j]>maxsan:
                maxsan=valueboard3[i][j]
                maxsani=i
                maxsanj=j




    return maxyi,maxer,maxsan,maxyii,maxyij,maxeri,maxerj,maxsani,maxsanj



def getminofvalueboard(valueboard):

    maxyi=0# 第一小
    maxyii=0
    maxyij=0

    maxer=0
    maxeri = 0
    maxerj = 0

    maxsan=0
    maxsani = 0
    maxsanj = 0
    for i in range(15):
        for j in range(15):
            if valueboard[i][j]<maxyi:
                maxyi=valueboard[i][j]
                maxyii=i
                maxyij=j
    valueboard2=valueboard.copy()
    valueboard2[maxyii][maxyij]=0
    for i in range(15):
        for j in range(15):
            if valueboard2[i][j]<maxer:
                maxer=valueboard[i][j]
                maxeri=i
                maxerj=j
    valueboard3 = valueboard2.copy()
    valueboard3[maxeri][maxerj] = 0
    for i in range(15):
        for j in range(15):
            if valueboard3[i][j]<maxsan:
                maxsan=valueboard3[i][j]
                maxsani=i
                maxsanj=j




    return maxyi,maxer,maxsan,maxyii,maxyij,maxeri,maxerj,maxsani,maxsanj


def sizeok(x,y,size):
    if x>=0 and x<=size-1 and y>=0 and y<=size-1:
        return True
    else:
        return False


def bijiao(dian,candidate_list,  valueboard):
    c = candidate_list[0]
    if valueboard[dian[0]][dian[1]] > valueboard[c[0]][c[1]]:
        candidate_list.pop()
        candidate_list.append(dian)


def danyi(changeofx,changeofy,valueboard,i,chessboard,candidate_list,chessboard_size,enemycolor):
    a=(i[0]+changeofx,i[1]+changeofy)
    if sizeok(a[0],a[1], chessboard_size) and chessboard[a[0]][a[1]] == 0:
        valueboard[a[0]][a[1]] += 1*enemycolor
        #bijiao( a, candidate_list, valueboard)



def daner(changeofx,changeofy,valueboard,i,chessboard,candidate_list,chessboard_size,curcolor,color,enemycolor):


    if curcolor==color:
        fenshu=12
    else:
        fenshu=10

    a=(i[0]+changeofx,i[1]+changeofy)

    if changeofy==2:
        changeofy=1


    if changeofx==2:
        changeofx=1

    if changeofy==-2:
        changeofy=-1


    if changeofx==-2:
        changeofx=-1



    a1 = (a[0] + changeofx, a[1] + changeofy)
    a2 = (i[0] - changeofx, i[1] - changeofy)




    if sizeok(a[0],a[1], chessboard_size)and chessboard[a[0]][a[1]] == curcolor:


        if sizeok(a1[0],a1[1],chessboard_size) and chessboard[a1[0]][a1[1]] == 0:

            valueboard[a1[0]][a1[1]] += fenshu*enemycolor
            #bijiao(a1, candidate_list, valueboard)

        if sizeok(a2[0],a2[1],chessboard_size)and chessboard[a2[0]][a2[1]] == 0:

            valueboard[a2[0]][a2[1]] += fenshu*enemycolor
            #bijiao(a2, candidate_list, valueboard)


def dansan(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color,enemycolor):

    if curcolor==color:
        fenshu=50
        mianfenshu=20
    else:
        fenshu=30
        mianfenshu=11
    a = (i[0] + changeofx, i[1] + changeofy)
    a1=(a[0] + changeofx, a[1] + changeofy)
    a2=(a1[0] + changeofx, a1[1] + changeofy)
    a3=(i[0] - changeofx, i[1] - changeofy)

    if sizeok(a[0], a[1], chessboard_size) and chessboard[a[0]][a[1]] == curcolor \
            and sizeok(a1[0], a1[1], chessboard_size) and chessboard[a1[0]][a1[1]] == curcolor:



        if sizeok(a2[0],a2[1],chessboard_size) and chessboard[a2[0]][a2[1]] == 0:

            if sizeok(a3[0],a3[1],chessboard_size)and chessboard[a3[0]][a3[1]] == 0:

                valueboard[a2[0]][a2[1]] += fenshu*enemycolor
                #bijiao(a2, candidate_list, valueboard)

            if sizeok(a3[0], a3[1], chessboard_size) and chessboard[a3[0]][a3[1]] == curcolor*-1:

                valueboard[a2[0]][a2[1]] += mianfenshu*enemycolor
                #bijiao(a2, candidate_list, valueboard)

        if sizeok(a3[0],a3[1],chessboard_size)and chessboard[a3[0]][a3[1]] == 0:

            if sizeok(a2[0], a2[1], chessboard_size) and chessboard[a2[0]][a2[1]] == 0:
                valueboard[a3[0]][a3[1]] += fenshu*enemycolor
                #bijiao(a3, candidate_list, valueboard)

            if sizeok(a2[0], a2[1], chessboard_size) and chessboard[a2[0]][a2[1]] == curcolor * -1:
                valueboard[a3[0]][a3[1]] += mianfenshu*enemycolor
                #bijiao(a3, candidate_list, valueboard)

def tiaosan(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color,enemycolor):

    if curcolor==color:
        fenshu=50

    else:
        fenshu=30

    a = (i[0] + changeofx, i[1] + changeofy)


    if changeofy==2:
        changeofy=1


    if changeofx==2:
        changeofx=1


    if changeofy==-2:
        changeofy=-1


    if changeofx==-2:
        changeofx=-1


    a1=(a[0] + changeofx, a[1] + changeofy)
    a2=(i[0] + changeofx, i[1] + changeofy)


    if sizeok(a[0], a[1], chessboard_size) and chessboard[a[0]][a[1]] == curcolor \
            and sizeok(a1[0], a1[1], chessboard_size) and chessboard[a1[0]][a1[1]] == curcolor:



        if sizeok(a2[0],a2[1],chessboard_size) and chessboard[a2[0]][a2[1]] == 0:



            valueboard[a2[0]][a2[1]] += fenshu*enemycolor
            #bijiao(a2, candidate_list, valueboard)




def dansi(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color,enemycolor):

    if curcolor==color:
        fenshu=1000

    else:
        fenshu=90


    a = (i[0] + changeofx, i[1] + changeofy)
    a1 = (a[0] + changeofx, a[1] + changeofy)
    a2 = (a1[0] + changeofx, a1[1] + changeofy)
    a3 = (a2[0] + changeofx, a2[1] + changeofy)
    a4 = (i[0] - changeofx, i[1] - changeofy)

    if sizeok(a[0], a[1], chessboard_size) and chessboard[a[0]][a[1]] == curcolor \
            and sizeok(a1[0], a1[1], chessboard_size) and chessboard[a1[0]][a1[1]] == curcolor \
            and sizeok(a2[0], a2[1], chessboard_size) and chessboard[a2[0]][a2[1]] == curcolor :

        if sizeok(a3[0],a3[1],chessboard_size) and chessboard[a3[0]][a3[1]] == 0:

            valueboard[a3[0]][a3[1]] += fenshu*enemycolor
            #bijiao(a3, candidate_list, valueboard)

        if sizeok(a4[0],a4[1],chessboard_size)and chessboard[a4[0]][a4[1]] == 0:

            valueboard[a4[0]][a4[1]] += fenshu*enemycolor
            #bijiao(a4, candidate_list, valueboard)



