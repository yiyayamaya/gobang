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


        bigdic={}
        for i in range(15):
            for j in range(15):
                if chessboard[i][j]==0:
                    chessboardmoni=chessboard.copy()
                    chessboardmoni[i][j]=1 #第一次模拟 下白棋
                    #biglist.append({(i,j):suanfen(chessboardmoni)})
                    bigdic[(i,j)]=suanfen(chessboardmoni)
        #print(bigdic)

        print(bigdic)
        erzilist=[]
        erzilistfen=[]

        for i in range(3):
            amax=max(bigdic,key=bigdic.get)
            #print(amax)
            erzilistfen.append(bigdic[amax])
            del bigdic[amax]
            erzilist.append(amax)


        print(erzilist,erzilistfen)

        chessboardson1 = chessboard.copy()
        chessboardson2 = chessboard.copy()
        chessboardson3 = chessboard.copy()
        chessboardson1[erzilist[0][0]][erzilist[0][1]] = 1
        chessboardson2[erzilist[1][0]][erzilist[1][1]] = 1
        chessboardson3[erzilist[2][0]][erzilist[2][1]] = 1

        print(chessboardson1)
        print(chessboardson2)
        print(chessboardson3)

        bigdic1 = {}
        for i in range(15):
            for j in range(15):
                if chessboardson1[i][j] == 0:
                    chessboardson1moni = chessboardson1.copy()
                    chessboardson1moni[i][j] = -1  # 第二次模拟 下黑棋
                    bigdic1[(i, j)] = suanfen(chessboardson1moni)


        son1sunzilist = []
        #print(bigdic1)
        for i in range(3):
            amin = min(bigdic1, key=bigdic1.get)

            son1sunzilist.append(bigdic1[amin])

            del bigdic1[amin]
            son1sunzilist.append(amin)

        print(son1sunzilist)

        bigdic2 = {}
        for i in range(15):
            for j in range(15):
                if chessboardson2[i][j] == 0:
                    chessboardson2moni = chessboardson2.copy()
                    chessboardson2moni[i][j] = -1  # 第二次模拟 下黑棋
                    bigdic2[(i, j)] = suanfen(chessboardson2moni)

        son2sunzilist = []
        # print(bigdic2)
        for i in range(3):
            amin = min(bigdic2, key=bigdic2.get)

            son2sunzilist.append(bigdic2[amin])

            del bigdic2[amin]
            son2sunzilist.append(amin)

        print(son2sunzilist)

        bigdic3 = {}
        for i in range(15):
            for j in range(15):
                if chessboardson3[i][j] == 0:
                    chessboardson3moni = chessboardson3.copy()
                    chessboardson3moni[i][j] = -1  # 第二次模拟 下黑棋
                    bigdic3[(i, j)] = suanfen(chessboardson3moni)

        son3sunzilist = []
        # print(bigdic3)
        for i in range(3):
            amin = min(bigdic3, key=bigdic3.get)
            son3sunzilist.append(bigdic3[amin])

            del bigdic3[amin]
            son3sunzilist.append(amin)

        print(son3sunzilist)


        bijiaoerzi=[]
        bijiaoerzi.append(son1sunzilist[0])
        bijiaoerzi.append(son2sunzilist[0])
        bijiaoerzi.append(son3sunzilist[0])

        print(bijiaoerzi)
        indexoferzi=bijiaoerzi.index(max(bijiaoerzi))
        print(erzilist[indexoferzi])
        self.candidate_list.clear()
        self.candidate_list.append((erzilist[indexoferzi][0],erzilist[indexoferzi][1]))
    






























def suanfen(chessboard): #此方法只用于得到棋盘上三处最大value以及位置 不应修改外部变量


    #print("算一下局面分")
    global totalmark
    totalmark = 0


    for i in range(15):
        for j in range(15):


            #print((i,j))

            jugby5(i, j, chessboard,"heng")
            jugby5(i, j, chessboard, "shu")
            jugby5(i, j, chessboard, "xie")
            jugby5(i, j, chessboard, "fanxie")
    #print(totalmark)
    return totalmark




def jugby5(x,y,chessboard,mode):

    m=1 #模拟在此下一个1; m=me e=enemy
    e=-1

    fuhao=1
    global totalmark
    if mode=="heng":
        detx=0
        dety=1
    elif mode=="shu":
        detx=1
        dety=0
    elif mode=="xie":
        detx=1
        dety=1
    elif mode=="fanxie":
        detx=1
        dety=-1
    result=[]
    #print((x+detx,y+dety),(x+detx*2,y+dety*2),(x+detx*3,y+dety*3),(x+detx*4,y+dety*4))
    if sizeok(x+detx,y+dety,15) and sizeok(x+2*detx,y+2*dety,15) and sizeok(x+3*detx,y+3*dety,15) \
            and sizeok(x+4*detx,y+4*dety,15):

        result.append(chessboard[x][y])
        result.append(chessboard[x+detx][y+dety])
        result.append(chessboard[x+2*detx][y+2*dety])
        result.append(chessboard[x+3*detx][y+3*dety])
        result.append(chessboard[x+4*detx][y+4*dety])
    elif sizeok(x+detx,y+dety,15) and sizeok(x+2*detx,y+2*dety,15) and sizeok(x+3*detx,y+3*dety,15):

        result.append(chessboard[x][y])
        result.append(chessboard[x + detx][y + dety])
        result.append(chessboard[x + 2 * detx][y + 2 * dety])
        result.append(chessboard[x + 3 * detx][y + 3 * dety])
    elif sizeok(x+detx,y+dety,15) and sizeok(x+2*detx,y+2*dety,15):

        result.append(chessboard[x][y])
        result.append(chessboard[x + detx][y + dety])
        result.append(chessboard[x + 2 * detx][y + 2 * dety])
    elif sizeok(x+detx,y+dety,15):

        result.append(chessboard[x][y])
        result.append(chessboard[x + detx][y + dety])

    #print(result)
    numofe=result.count(1)
    numofm=result.count(-1) #m是黑棋 黑棋会导致负分
    numofkeng=result.count(0)
    #print(numofe,numofm,numofkeng)

    if len(result)==5:
        if numofkeng==0:
            if numofe==5 :
                totalmark=totalmark+1000
            elif numofm==5:
                totalmark = totalmark + 1000 * -1
            elif numofe==4 :
                totalmark = totalmark + 50
            elif numofm == 4:
                totalmark = totalmark + 50 * -1
            elif numofe==3 :
                totalmark = totalmark + 20
            elif numofm==3:
                totalmark = totalmark + 20 * -1
        elif numofkeng == 1:
            if numofe==4:
                totalmark=totalmark+400
            elif numofm==4:
                totalmark=totalmark+400*-1
            elif numofe==3 :
                totalmark = totalmark + 40
            elif  numofm==3:
                totalmark = totalmark + 40*-1
        elif numofkeng==2:
            if numofe==3 :
                totalmark=totalmark+140
            elif  numofm==3:
                totalmark=totalmark+200*-1
            elif numofe==2 :
                totalmark = totalmark + 30
            elif numofm==2:
                totalmark = totalmark + 30*-1
        elif numofkeng == 3:
            if numofe == 2 :
                totalmark = totalmark + 30
            if  numofm == 2:
                totalmark = totalmark + 30*-1
        elif numofkeng==4:
            if numofe == 1 :
                totalmark = totalmark + 10
            elif numofm == 1 :
                totalmark = totalmark + 10*-1




        #print(mode,totalmark)

def sizeok(x,y,size):
    if x>=0 and x<=size-1 and y>=0 and y<=size-1:
        return True
    else:
        return False




