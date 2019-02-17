

import tkinter as tk

import numpy as np

import gobang_2019
class myUI:
    def __init__(self):

        self.chessboard = np.zeros((15, 15), dtype=np.int)

        self.PIECE_SIZE = 10

        self.click_x = 0
        self.click_y = 0

        self.pieces_x = [i for i in range(32, 523, 35)]
        self.pieces_y = [i for i in range(38, 529, 35)]

        self.coor_black = []
        self.coor_white = []

        self.person_flag = 1
        self.piece_color = "black"

        self.realx=0
        self.realy=0

        """窗口主体"""
        self.root = tk.Tk()

        self.root.title("Gobang")
        self.root.geometry("760x560")

        """棋子提示"""
        self.side_canvas = tk.Canvas(self.root, width=220, height=50)
        self.side_canvas.grid(row=0, column=1)
        self.side_canvas.create_oval(110 - self.PIECE_SIZE, 25 - self.PIECE_SIZE,
                                110 + self.PIECE_SIZE, 25 + self.PIECE_SIZE,
                                fill=self.piece_color, tags=("show_piece"))
        """棋子提示标签"""
        self.var = tk.StringVar()
        self.var.set("执黑棋")
        self.person_label = tk.Label(self.root, textvariable=self.var, width=12, anchor=tk.CENTER,
                                font=("Arial", 20))
        self.person_label.grid(row=1, column=1)

        """输赢提示标签"""
        self.var1 = tk.StringVar()
        self.var1.set("")
        self.result_label = tk.Label(self.root, textvariable=self.var1, width=12, height=4,
                                anchor=tk.CENTER, fg="red", font=("Arial", 25))
        self.result_label.grid(row=2, column=1, rowspan=2)

        """游戏结束提示标签"""
        self.var2 = tk.StringVar()
        self.var2.set("")
        self.game_label = tk.Label(self.root, textvariable=self.var2, width=12, height=4,
                              anchor=tk.CENTER, font=("Arial", 18))
        self.game_label.grid(row=4, column=1)


        """
        
        reset_button = tk.Button(self.root, text="重新开始", font=20,
                                 width=8, command=gameReset(self))
        reset_button.grid(row=5, column=1)
        """





        """棋盘绘制"""
        # 背景
        self.canvas = tk.Canvas(self.root, bg="saddlebrown", width=540, height=540)
        self.canvas.bind("<Button-1>", coorBackAdaptor(coorBack,self=self))  # 鼠标单击事件绑定
        self.canvas.grid(row=0, column=0, rowspan=6)
        #print(add(1,2))
        # 线条
        for i in range(15):
            self.canvas.create_line(32, (35 * i + 38), 522, (35 * i + 38))
            self.canvas.create_line((35 * i + 32), 38, (35 * i + 32), 528)
        # 点
        point_x = [3, 3, 11, 11, 7]
        point_y = [3, 11, 3, 11, 7]
        for i in range(5):
            self.canvas.create_oval(35 * point_x[i] + 28, 35 * point_y[i] + 33,
                               35 * point_x[i] + 36, 35 * point_y[i] + 41, fill="black")

        # 透明棋子（设置透明棋子，方便后面落子的坐标定位到正确的位置）
        for i in self.pieces_x:
            for j in self.pieces_y:
                self.canvas.create_oval(i - self.PIECE_SIZE, j - self.PIECE_SIZE,
                                   i + self.PIECE_SIZE, j + self.PIECE_SIZE,
                                   width=0, tags=(str(i), str(j)))

        # 数字坐标
        for i in range(15):
            self.label = tk.Label(self.canvas, text=str(i + 1), fg="black", bg="saddlebrown",
                             width=2, anchor=tk.E)
            self.label.place(x=2, y=35 * i + 28)
        # 字母坐标
        self.count = 0
        for i in range(65, 81):
            self.label = tk.Label(self.canvas, text=chr(i), fg="black", bg="saddlebrown")
            self.label.place(x=35 * self.count + 25, y=2)
            self.count += 1



        """窗口循环"""
        self.root.mainloop()




# 右上方的棋子提示（工具）
def showChange(self,color):

    self.piece_color = color
    self.side_canvas.delete("show_piece")
    self.side_canvas.create_oval(110 - self.PIECE_SIZE, 25 - self.PIECE_SIZE,
                            110 + self.PIECE_SIZE, 25 + self.PIECE_SIZE,
                            fill=self.piece_color, tags=("show_piece"))


# 输赢的提示、游戏结束的提示（工具）
def pushMessage(self):
    if self.person_flag == -1:
        self.var1.set("白棋赢")
    elif self.person_flag == 1:
        self.var1.set("黑棋赢")
    self.var2.set("游戏结束")


# 棋子的计数（工具）
def piecesCount(self,coor, pieces_count, t1, t2):
    for i in range(1, 5):
        (x, y) = (self.click_x + t1 * 35 * i, self.click_y + t2 * 35 * i)
        if (x, y) in coor:
            pieces_count += 1
        else:
            break
    return pieces_count


# 事件监听处理
def coorBack(event,self):  # return coordinates of cursor 返回光标坐标


    self.click_x = event.x
    self.click_y = event.y
    coorJudge(self)

def coorBackAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)



#定义重置按钮的功能
def gameReset(self):

    self.person_flag = 1       #打开落子开关
    self.var.set("执黑棋")      #还原提示标签
    self.var1.set("")          #还原输赢提示标签
    self.var2.set("")          #还原游戏结束提示标签
    showChange(self,"black")   #还原棋子提示图片
    self.canvas.delete("piece")#删除所有棋子
    self.coor_black = []       #清空黑棋坐标存储器
    self.coor_white = []       #清空白棋坐标存储器



def gameResetAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)


'''判断输赢的逻辑'''


# preJudge调用realJudge0，realJudge0调用realJudge1和realJudge2；
# realJudge1负责横纵两轴的计数，realJudge2负责两斜线方向的计数
# realJudge0汇总指定颜色棋子结果，作出决策，判断是否游戏结束
# preJudge决定是判断黑棋还是判断白棋，对两种颜色的棋子判断进行导流
def preJudge(self,piece_color):
    if piece_color == "black":
        realJudge0(self,self.coor_black)
    elif piece_color == "white":
        realJudge0(self,self.coor_white)


def realJudge0(self,coor):


    if realJudge1(self,coor) == 1 or realJudge2(self,coor) == 1:
        pushMessage(self)
        self.person_flag = 0


def realJudge1(self,coor):
    pieces_count = 0
    pieces_count = piecesCount(self,coor, pieces_count, 1, 0)  # 右边
    pieces_count = piecesCount(self,coor, pieces_count, -1, 0)  # 左边
    if pieces_count >= 4:
        return 1
    else:
        pieces_count = 0
        pieces_count = piecesCount(self,coor, pieces_count, 0, -1)  # 上边
        pieces_count = piecesCount(self,coor, pieces_count, 0, 1)  # 下边
        if pieces_count >= 4:
            return 1
        else:
            return 0


def realJudge2(self,coor):
    pieces_count = 0
    pieces_count = piecesCount(self,coor, pieces_count, 1, 1)  # 右下角
    pieces_count = piecesCount(self,coor, pieces_count, -1, -1)  # 左上角
    if pieces_count >= 4:
        return 1
    else:
        pieces_count = 0
        pieces_count = piecesCount(self,coor, pieces_count, 1, -1)  # 右上角
        pieces_count = piecesCount(self,coor, pieces_count, -1, 1)  # 左下角
        if pieces_count >= 4:
            return 1
        else:
            return 0


'''落子的逻辑'''


# 落子
def putPiece(self,piece_color):

    if(piece_color=="black"):
        print("人执黑，下在了",self.click_y//35-1,self.click_x//35 ,"图像位置=",self.click_x,self.click_y)
        self.canvas.create_oval(self.click_x - self.PIECE_SIZE, self.click_y - self.PIECE_SIZE,
                                self.click_x + self.PIECE_SIZE, self.click_y + self.PIECE_SIZE,
                           fill=piece_color, tags=("piece"))


        newAI=gobang_2019.AI(15, 1, 1)  #new AI执1
        self.chessboard[self.click_y//35-1][self.click_x//35]=-1 #实体棋盘即玩家执-1
        newAI.go(self.chessboard)
        print(newAI.candidate_list)
        self.chessboard[newAI.candidate_list[0][0]][newAI.candidate_list[0][1]] = 1  # AI决策list结果填进去
        #上面的结果如何填满 防止再次调用

        xofai = (newAI.candidate_list[0][1])*35+32
        yofai = (newAI.candidate_list[0][0])* 35+38
        self.canvas.create_oval(xofai - self.PIECE_SIZE, yofai - self.PIECE_SIZE,
                                xofai + self.PIECE_SIZE, yofai + self.PIECE_SIZE,
                                fill="white", tags=("piece"))

        self.coor_white.append((xofai, yofai))
        self.coor_black.append((self.click_x, self.click_y))
        preJudge(self, piece_color)










# 找出离鼠标点击位置最近的棋盘线交点，调用putPiece落子
def coorJudge(self):

    coor = self.coor_black + self.coor_white


    item = self.canvas.find_closest(self.click_x, self.click_y)

    tags_tuple = self.canvas.gettags(item)
    if len(tags_tuple) > 1:
        tags_list = list(tags_tuple)
        coor_list = tags_list[:2]
        try:
            for i in range(len(coor_list)):
                coor_list[i] = int(coor_list[i])
        except ValueError:
            pass
        else:
            coor_tuple = tuple(coor_list)
            (self.click_x, self.click_y) = coor_tuple
            # print("tags = ", tags_tuple, "coors = ", coor_tuple)
            if ((self.click_x, self.click_y) not in coor) and (self.click_x in self.pieces_x) and (self.click_y in self.pieces_y):
                # print("True")
                if self.person_flag != 0:

                    if self.person_flag == 1:
                        putPiece(self,"black")
                        showChange(self,"black")
                        self.var.set("执黑棋")

                    elif self.person_flag == -1:
                        putPiece(self,"white")
                        showChange(self,"black")
                        self.var.set("执黑棋")
                    #self.person_flag *= -1
            # else:
            # print("False")






myUI1=myUI()