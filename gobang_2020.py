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
        arr = [0, 0, 0]
        goonce(self, chessboard)














def goonce(self, chessboard):





    #print(self.color,'走了一步') 2019年注释
    valueboard=np.zeros((self.chessboard_size, self.chessboard_size), dtype=np.int)




    self.candidate_list.clear()

    idx = np.where(chessboard == COLOR_NONE)
    idx = list(zip(idx[0], idx[1])) #以上2行获取空的位置


    pos_idx = random.randint(0, len(idx)-1)
    new_pos = idx[pos_idx]
    self.candidate_list.append(new_pos)#最最最开始随便空位置下一个


    o=(self.chessboard_size//2,self.chessboard_size//2)

    if chessboard[o[0]][o[1]]==0:

        valueboard[o[0]][o[1]]+=0.1

        self.candidate_list.pop()
        self.candidate_list.append(o)



    idx2 = np.where(chessboard == COLOR_WHITE)#得到敌人的点
    idx2 = list(zip(idx2[0], idx2[1]))

    idx3 = np.where(chessboard == COLOR_BLACK)#得到自己的点
    idx3 = list(zip(idx3[0], idx3[1]))

    for i in idx2:#扫描敌人棋子



        #一个子也堵 1分

        danyi(-1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(-1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(-1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(0, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)
        danyi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size)

        daner(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)


        daner(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        daner(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)








        dansan(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansan(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansan(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansan(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)


        tiaosan(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        tiaosan(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        tiaosan(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        tiaosan(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        tiaosan(0, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE, self.color)
        tiaosan(-2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE, self.color)
        tiaosan(-2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE, self.color)
        tiaosan(-2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)

        dansi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)
        dansi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_WHITE,self.color)

    for i in idx3:#扫描自己棋子

        daner(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)

        daner(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        daner(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)







        dansan(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansan(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansan(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansan(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)

        tiaosan(0, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        tiaosan(2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        tiaosan(2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        tiaosan(2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        tiaosan(0, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK, self.color)
        tiaosan(-2, 2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK, self.color)
        tiaosan(-2, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK, self.color)
        tiaosan(-2, -2, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,
                self.color)

        dansi(0, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansi(1, 1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansi(1, 0, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)
        dansi(1, -1, valueboard, i, chessboard, self.candidate_list, self.chessboard_size, COLOR_BLACK,self.color)

    x=self.candidate_list[0]


    monichessboard=np.copy(chessboard)


    monichessboard[x[0],x[1]]=self.color#假设我方下了一步

    #print(monichessboard) 2019年注释
    """
    global cengshu
    print(cengshu)
    if cengshu>=1:
        return
    cengshu = cengshu + 1
    AI.__init__(self,self.chessboard_size, self.color*-1, self.time_out)#机器很单纯的在模拟板下了一步
    AI.go(self, monichessboard)
    print('ok')
    """

    assert chessboard[new_pos[0],new_pos[1]]== COLOR_NONE





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


def danyi(changeofx,changeofy,valueboard,i,chessboard,candidate_list,chessboard_size):
    a=(i[0]+changeofx,i[1]+changeofy)
    if sizeok(a[0],a[1], chessboard_size) and chessboard[a[0]][a[1]] == 0:
        valueboard[a[0]][a[1]] += 1
        bijiao( a, candidate_list, valueboard)



def daner(changeofx,changeofy,valueboard,i,chessboard,candidate_list,chessboard_size,curcolor,color):


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

            valueboard[a1[0]][a1[1]] += fenshu
            bijiao(a1, candidate_list, valueboard)

        if sizeok(a2[0],a2[1],chessboard_size)and chessboard[a2[0]][a2[1]] == 0:

            valueboard[a2[0]][a2[1]] += fenshu
            bijiao(a2, candidate_list, valueboard)


def dansan(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color):

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

                valueboard[a2[0]][a2[1]] += fenshu
                bijiao(a2, candidate_list, valueboard)

            if sizeok(a3[0], a3[1], chessboard_size) and chessboard[a3[0]][a3[1]] == curcolor*-1:

                valueboard[a2[0]][a2[1]] += mianfenshu
                bijiao(a2, candidate_list, valueboard)

        if sizeok(a3[0],a3[1],chessboard_size)and chessboard[a3[0]][a3[1]] == 0:

            if sizeok(a2[0], a2[1], chessboard_size) and chessboard[a2[0]][a2[1]] == 0:
                valueboard[a3[0]][a3[1]] += fenshu
                bijiao(a3, candidate_list, valueboard)

            if sizeok(a2[0], a2[1], chessboard_size) and chessboard[a2[0]][a2[1]] == curcolor * -1:
                valueboard[a3[0]][a3[1]] += mianfenshu
                bijiao(a3, candidate_list, valueboard)

def tiaosan(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color):

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



            valueboard[a2[0]][a2[1]] += fenshu
            bijiao(a2, candidate_list, valueboard)




def dansi(changeofx, changeofy, valueboard, i, chessboard, candidate_list, chessboard_size, curcolor,color):

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

            valueboard[a3[0]][a3[1]] += fenshu
            bijiao(a3, candidate_list, valueboard)

        if sizeok(a4[0],a4[1],chessboard_size)and chessboard[a4[0]][a4[1]] == 0:

            valueboard[a4[0]][a4[1]] += fenshu
            bijiao(a4, candidate_list, valueboard)



