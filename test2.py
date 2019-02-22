#!/usr/bin/python3
# -*- coding: utf-8 -*-

#test2 和test差不多  只不过test放在一个类里了 不过好像没什么必要
#此文件为程序的入口


import tkinter as tk

import numpy as np

import gobang_2019_new


PIECE_SIZE = 10
chessboard = np.zeros((15, 15), dtype=np.int)
click_x = 0
click_y = 0
xofai=0
yofai=0

pieces_x = [i for i in range(32, 523, 35)]
pieces_y = [i for i in range(38, 529, 35)]

coor_black = []
coor_white = []

person_flag = 1
piece_color = "black"


# 右上方的棋子提示（工具）
def showChange(color):
    global piece_color
    piece_color = color
    side_canvas.delete("show_piece")
    side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                            110 + PIECE_SIZE, 25 + PIECE_SIZE,
                            fill=piece_color, tags=("show_piece"))


# 输赢的提示、游戏结束的提示（工具）
def pushMessage(mode):
    if mode == 1:
        var1.set("白棋赢")
    elif mode == -1:
        var1.set("黑棋赢")
    var2.set("游戏结束")


# 棋子的计数（工具）
def piecesCount(coor, pieces_count, t1, t2,mode):

    if mode==-1:

        for i in range(1, 5):
            (x, y) = (click_x + t1 * 35 * i, click_y + t2 * 35 * i) #因为这里是click_x所以只会为黑棋计数
            if (x, y) in coor:
                pieces_count += 1
            else:
                break
        return pieces_count
    else:
        for i in range(1, 5):
            (x, y) = (xofai + t1 * 35 * i, yofai + t2 * 35 * i) #为白棋
            if (x, y) in coor:
                pieces_count += 1
            else:
                break
        return pieces_count


# 事件监听处理
def coorBack(event):  # return coordinates of cursor 返回光标坐标
    global click_x, click_y
    click_x = event.x
    click_y = event.y
    coorJudge()


# 定义重置按钮的功能
def gameReset():
    global person_flag, coor_black, coor_white, piece_color,chessboard
    chessboard = np.zeros((15, 15), dtype=np.int)
    person_flag = 1  # 打开落子开关
    var.set("执黑棋")  # 还原提示标签
    var1.set("")  # 还原输赢提示标签
    var2.set("")  # 还原游戏结束提示标签
    showChange("black")  # 还原棋子提示图片
    canvas.delete("piece")  # 删除所有棋子
    coor_black = []  # 清空黑棋坐标存储器
    coor_white = []  # 清空白棋坐标存储器


'''判断输赢的逻辑'''


# preJudge调用realJudge0，realJudge0调用realJudge1和realJudge2；
# realJudge1负责横纵两轴的计数，realJudge2负责两斜线方向的计数
# realJudge0汇总指定颜色棋子结果，作出决策，判断是否游戏结束
# preJudge决定是判断黑棋还是判断白棋，对两种颜色的棋子判断进行导流
def preJudge(piece_color):
    if piece_color == "black":
        mode=-1
        realJudge0(coor_black,mode)
    elif piece_color == "white":
        mode = 1
        realJudge0(coor_white,mode)


def realJudge0(coor,mode):
    global person_flag, person_label

    if realJudge1(coor,mode) == 1 or realJudge2(coor,mode) == 1:
        pushMessage(mode)
        person_flag = 0


def realJudge1(coor,mode):
    pieces_count = 0
    pieces_count = piecesCount(coor, pieces_count, 1, 0,mode)  # 右边
    pieces_count = piecesCount(coor, pieces_count, -1, 0,mode)  # 左边

    if pieces_count >= 4:
        return 1
    else:
        pieces_count = 0
        pieces_count = piecesCount(coor, pieces_count, 0, -1,mode)  # 上边
        pieces_count = piecesCount(coor, pieces_count, 0, 1,mode)  # 下边

        if pieces_count >= 4:
            return 1
        else:
            return 0


def realJudge2(coor,mode):
    pieces_count = 0
    pieces_count = piecesCount(coor, pieces_count, 1, 1,mode)  # 右下角
    pieces_count = piecesCount(coor, pieces_count, -1, -1,mode)  # 左上角
    #print("计数器↘", pieces_count)
    if pieces_count >= 4:
        return 1
    else:
        pieces_count = 0
        pieces_count = piecesCount(coor, pieces_count, 1, -1,mode)  # 右上角
        pieces_count = piecesCount(coor, pieces_count, -1, 1,mode)  # 左下角
        #print("计数器↗", pieces_count)
        if pieces_count >= 4:
            return 1
        else:
            return 0


'''落子的逻辑'''


# 落子
def putPiece(piece_color):


    if(piece_color=="black"):
        canvas.create_oval(click_x - PIECE_SIZE, click_y - PIECE_SIZE,
                                click_x + PIECE_SIZE, click_y + PIECE_SIZE,
                           fill=piece_color, tags=("piece"))


        newAI=gobang_2019_new.AI(15, 1, 1)  #new AI执1

        chessboard[click_y//35-1][click_x//35]=-1 #实体棋盘即玩家执-1
        newAI.go(chessboard)
        #print(newAI.candidate_list)
        chessboard[newAI.candidate_list[0][0]][newAI.candidate_list[0][1]] = 1  # AI决策list结果填进去
        #上面的结果如何填满 防止再次调用
        global xofai, yofai
        xofai = (newAI.candidate_list[0][1])*35+32
        yofai = (newAI.candidate_list[0][0])* 35+38
        canvas.create_oval(xofai - PIECE_SIZE, yofai - PIECE_SIZE,
                                xofai + PIECE_SIZE, yofai + PIECE_SIZE,
                                fill="white", tags=("piece"))

        coor_white.append((xofai, yofai))
        coor_black.append((click_x, click_y))
        preJudge("black")

        preJudge("white")


        #print(coor_black,coor_white)










# 找出离鼠标点击位置最近的棋盘线交点，调用putPiece落子
def coorJudge():
    global click_x, click_y
    coor = coor_black + coor_white
    global person_flag, show_piece
    # print("x = %s, y = %s" % (click_x, click_y))
    item = canvas.find_closest(click_x, click_y)
    tags_tuple = canvas.gettags(item)
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
            (click_x, click_y) = coor_tuple
            # print("tags = ", tags_tuple, "coors = ", coor_tuple)
            if ((click_x, click_y) not in coor) and (click_x in pieces_x) and (click_y in pieces_y):
                # print("True")
                if person_flag != 0:
                    if person_flag == 1:
                        putPiece("black")
                        showChange("black")
                        var.set("执黑棋")
                    elif person_flag == -1:
                        putPiece("white")
                        showChange("black")
                        var.set("执黑棋")

            # else:
            # print("False")


"""窗口主体"""
root = tk.Tk()

root.title("Gobang")
root.geometry("760x560")

"""棋子提示"""
side_canvas = tk.Canvas(root, width=220, height=50)
side_canvas.grid(row=0, column=1)
side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                        110 + PIECE_SIZE, 25 + PIECE_SIZE,
                        fill=piece_color, tags=("show_piece"))
"""棋子提示标签"""
var = tk.StringVar()
var.set("执黑棋")
person_label = tk.Label(root, textvariable=var, width=12, anchor=tk.CENTER,
                        font=("Arial", 20))
person_label.grid(row=1, column=1)

"""输赢提示标签"""
var1 = tk.StringVar()
var1.set("")
result_label = tk.Label(root, textvariable=var1, width=12, height=4,
                        anchor=tk.CENTER, fg="red", font=("Arial", 25))
result_label.grid(row=2, column=1, rowspan=2)

"""游戏结束提示标签"""
var2 = tk.StringVar()
var2.set("")
game_label = tk.Label(root, textvariable=var2, width=12, height=4,
                      anchor=tk.CENTER, font=("Arial", 18))
game_label.grid(row=4, column=1)

"""重置按钮"""
reset_button = tk.Button(root, text="重新开始", font=20,
                         width=8, command=gameReset)
reset_button.grid(row=5, column=1)

"""棋盘绘制"""
# 背景
canvas = tk.Canvas(root, bg="saddlebrown", width=540, height=540)
canvas.bind("<Button-1>", coorBack)  # 鼠标单击事件绑定
canvas.grid(row=0, column=0, rowspan=6)
# 线条
for i in range(15):
    canvas.create_line(32, (35 * i + 38), 522, (35 * i + 38))
    canvas.create_line((35 * i + 32), 38, (35 * i + 32), 528)
# 点
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    canvas.create_oval(35 * point_x[i] + 28, 35 * point_y[i] + 33,
                       35 * point_x[i] + 36, 35 * point_y[i] + 41, fill="black")

# 透明棋子（设置透明棋子，方便后面落子的坐标定位到正确的位置）
for i in pieces_x:
    for j in pieces_y:
        canvas.create_oval(i - PIECE_SIZE, j - PIECE_SIZE,
                           i + PIECE_SIZE, j + PIECE_SIZE,
                           width=0, tags=(str(i), str(j)))

# 数字坐标
for i in range(15):
    label = tk.Label(canvas, text=str(i ), fg="black", bg="saddlebrown",
                     width=2, anchor=tk.E)
    label.place(x=2, y=35 * i + 28)
# 字母坐标
count = 0
for i in range(15):
    label = tk.Label(canvas, text=str(i ), fg="black", bg="saddlebrown",
                     width=2, anchor=tk.E)
    label.place(x=35 * count + 25, y=2)
    count += 1

"""
count = 0
for i in range(65, 81):
    label = tk.Label(canvas, text=chr(i), fg="black", bg="saddlebrown")
    label.place(x=35 * count + 25, y=2)
    count += 1
"""

"""窗口循环"""
root.mainloop()