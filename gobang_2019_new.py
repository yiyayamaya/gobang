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

        starttime = time.time()

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


                    if calusurround(chessboard, i, j) != 0:

                        chessboardmoni=chessboard.copy()
                        chessboardmoni[i][j]=1 #第一次模拟 下白棋
                        #biglist.append({(i,j):suanfen(chessboardmoni)})
                        bigdic[(i,j)]=suanfen(chessboardmoni)
        

        #print("bigdic\n",bigdic)
        erzilist=[]
        erzilistfen=[]

        starttime2 = time.time()


        for i in range(8):#第一层模拟次数
            amax=max(bigdic,key=bigdic.get)

            erzilistfen.append(bigdic[amax])
            del bigdic[amax]
            erzilist.append(amax)


        print(erzilist,erzilistfen)
        chessboardlist = []
        bijiaoerzi = []

        starttime3 = time.time()

        for i in range(len(erzilist)):

            chessboardson = chessboard.copy()

            chessboardson[erzilist[i][0]][erzilist[i][1]] = 1


            chessboardlist.append(chessboardson)
        starttime4 = time.time()

        for index in range(len(erzilist)):
            bigdicerzi = {}
            for i in range(15):
                for j in range(15):
                    if chessboardlist[index][i][j] == 0:
                        if calusurround(chessboard, i, j) !=0:
                            chessboardsonmoni = chessboardlist[index].copy()
                            chessboardsonmoni[i][j] = -1  # 第二次模拟 下黑棋
                            bigdicerzi[(i, j)] = suanfen(chessboardsonmoni)


            sunzilist = []

            for i in range(3): #这个3并无意义 实际黑棋不会看分最低的三个 只会选分最低的一个
                amin = min(bigdicerzi, key=bigdicerzi.get)

                sunzilist.append(bigdicerzi[amin])

                del bigdicerzi[amin]
                sunzilist.append(amin)

            print(sunzilist)
            bijiaoerzi.append(sunzilist[0])

        starttime5 = time.time()





        print(bijiaoerzi)
        indexoferzi=bijiaoerzi.index(max(bijiaoerzi))
        print("白下",erzilist[indexoferzi])
        self.candidate_list.clear()
        self.candidate_list.append((erzilist[indexoferzi][0],erzilist[indexoferzi][1]))

        starttime6 = time.time()


        print(starttime2-starttime,starttime3-starttime2,starttime4-starttime3,starttime5-starttime4
              ,starttime6-starttime5)























def calusurround(chessboard,x,y):#计算一个棋子周围的棋子数(无论颜色) 若为0 则不值得在这里模拟并算分
    neighboor=0
    if sizeok(x-1,y-1,15) and chessboard[x-1][y-1]!=0:
        neighboor=neighboor+1
    if sizeok(x-1,y,15) and chessboard[x-1][y]!=0:
        neighboor=neighboor+1
    if sizeok(x-1,y+1,15) and chessboard[x-1][y+1]!=0:
        neighboor=neighboor+1
    if sizeok(x,y-1,15) and chessboard[x][y-1]!=0:
        neighboor=neighboor+1
    if sizeok(x,y+1,15) and chessboard[x][y+1]!=0:
        neighboor=neighboor+1
    if sizeok(x+1,y-1,15) and chessboard[x+1][y-1]!=0:
        neighboor=neighboor+1
    if sizeok(x+1,y,15) and chessboard[x+1][y]!=0:
        neighboor=neighboor+1
    if sizeok(x+1,y+1,15) and chessboard[x+1][y+1]!=0:
        neighboor=neighboor+1
    return neighboor




def suanfen(chessboard): #此方法只用于得到棋盘上三处最大value以及位置 不应修改外部变量


    
    global totalmark
    totalmark = 0


    for i in range(15):
        for j in range(15):


            

            jugby5(i, j, chessboard,"heng")
            jugby5(i, j, chessboard, "shu")
            jugby5(i, j, chessboard, "xie")
            jugby5(i, j, chessboard, "fanxie")
   
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

   
    numofe=result.count(1)
    numofm=result.count(-1) #m是黑棋 黑棋会导致负分
    numofkeng=result.count(0)
   
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




        

def sizeok(x,y,size):
    if x>=0 and x<=size-1 and y>=0 and y<=size-1:
        return True
    else:
        return False




