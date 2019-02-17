import numpy as np


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
            print(i,j,totalmark)
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
                totalmark=totalmark+200
            elif numofm==4:
                totalmark=totalmark+200*-1
            elif numofe==3 :
                totalmark = totalmark + 40
            elif  numofm==3:
                totalmark = totalmark + 40*-1
        elif numofkeng==2:
            if numofe==3 :
                totalmark=totalmark+80
            elif  numofm==3:
                totalmark=totalmark+80*-1
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



chessboard = np.zeros((15, 15), dtype=np.int)

chessboard[7][6]=-1
chessboard[7][7]=-1
chessboard[7][8]=-1


chessboard[4][3]=1
chessboard[4][4]=1
chessboard[4][5]=1

print(suanfen(chessboard))