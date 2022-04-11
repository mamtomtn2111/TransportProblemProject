import tkinter as tk
from tkinter import *
from TPprograming import *

window = tk.Tk()
window.title("Bài toán vận tải")
window.geometry('1280x720')

def ConvertToMatrix(InputMatrix):
    StringMatrix = InputMatrix.split(";")
    listMatrix = []
    for i in StringMatrix:
        z = i.split(" ")
        listMatrix.append(list(map(int, z)))
    return listMatrix

def ConvertToList(Input):
    List = Input.split(" ")
    List = list(map(int, List))
    return List

def GetInput():
    demand = ConvertToList(str(ThuTextBox.get(1.0, END + "-1c")))
    supply = ConvertToList(str(PhatTextBox.get(1.0, END + "-1c")))
    cost = ConvertToMatrix(str(ChiPhiTextBox.get(1.0, END + "-1c")))
    return demand, supply, cost

def CalculateResult():
    KetQuaTextBox.delete("1.0", END)
    try:
        Thu, Phat, ChiPhi = GetInput()
        resultTable, s, d = main(ChiPhi, Phat, Thu)

        KetQuaTextBox.insert(END,"Ma trận chi phí ban đầu:\n")
        for i in ChiPhi:
            KetQuaTextBox.insert(END,str(i)+"\n")
        KetQuaTextBox.insert(END, "\nMa trận chi phí tối ưu:\n")
        for i in resultTable:
            KetQuaTextBox.insert(END, str(i) + "\n")

        KetQuaTextBox.insert(END, "\nChi phí tối ưu được tính:\n")
        ongkos = 0
        flag = 0
        for x in range(s):
            for y in range(d):
                if resultTable[x][y] == 0:
                    continue
                if flag == 1:
                    KetQuaTextBox.insert(END, " + ")
                KetQuaTextBox.insert(END, resultTable[x][y])
                KetQuaTextBox.insert(END, "x"+str(ChiPhi[x][y]))
                if x < s - 1 or y < d - 1:
                    flag = 1
                ongkos += resultTable[x][y] * ChiPhi[x][y]
        KetQuaTextBox.insert(END, " = " + str(ongkos))
    except:
        KetQuaTextBox.delete("1.0", END)
        KetQuaTextBox.insert(END, "Lỗi nhập liệu !!!\n")
        KetQuaTextBox.insert(END, "- Đối với ô thu phát cần phải điền các số nguyên và cách nhau bởi dấu cách !!!\n")
        KetQuaTextBox.insert(END, 'VD:\n [1, 2, 3] sẽ là "1 2 3"\n')
        KetQuaTextBox.insert(END, '- Đối với ô ma trận chi phí cần phải điền các số nguyên và cách nhau bởi dấu cách, Kết thúc một dòng 1 ma trận phải có dấu ";"!!!\nVD:')
        KetQuaTextBox.insert(END, "Ma trận [1, 2, 3]")
        KetQuaTextBox.insert(END, "[4, 5, 6]\n")
        KetQuaTextBox.insert(END, "Sẽ nhập là\n")
        KetQuaTextBox.insert(END, "1 2 3;\n")
        KetQuaTextBox.insert(END, "4 5 6;\n")
        KetQuaTextBox.insert(END, "hoặc 1 2 3;4 5 6 (không được để trống gần dấu ;)")

def ClearAllTextBox():
    ThuTextBox.delete("1.0", END)
    PhatTextBox.delete("1.0", END)
    ChiPhiTextBox.delete("1.0", END)
    KetQuaTextBox.delete("1.0", END)

def configureApp():
    for i in range(0, 3):
        window.columnconfigure(i, weight=2, minsize=50)
    for i in range(0, 5):
        window.rowconfigure(i, weight=2, minsize=50)

    GeneralLabel.grid(row=0, column=1)
    ThuLabel.grid(row=1, column=0)
    ThuTextBox.grid(row=1, column=1)
    PhatLabel.grid(row=2, column=0)
    PhatTextBox.grid(row=2, column=1)
    ChiPhiLabel.grid(row=3, column=0)
    ChiPhiTextBox.grid(row=3, column=1)
    Calculate.grid(row=4, column=1, pady=20)
    KetQua.grid(row=0, column=2, padx=20)
    KetQuaTextBox.grid(row=1, column=2, padx=20, rowspan=3)
    Clear.grid(row = 4, column = 2, pady = 20)
    Help.grid(row=1, column=3, padx=20)
    About.grid(row=2, column=3, padx=20)

def HelpEvent():
    HelpApp = tk.Tk()
    HelpApp.title("Trợ giúp sử dụng")
    #HelpApp.geometry('640x480')
    helpTextBox = Text(HelpApp,font=("bold", 14))
    helpTextBox.grid(row=0, column=0)
    HelpString = """
        Hướng dẫn sử dụng phần mềm:
        - Đối với ô thu và phát ta nhập các ô cách nhau một dấu cách, và bắt buộc phải 
        nhập số nguyên
        Ví dụ:
        [1, 2, 3] thì nhập là "1 2 3"
        - Đối với ma trận chi phí ta nhập các ô cách nhau một dấu cách, và sang một
        dòng ma trận mới thì ngăn cách bởi dầu ";" và bắt buộc toàn bộ là số nguyên.
        Ví dụ:
        [1 2 3]
        [4 5 6]
        [7 8 9]
        Chúng ta sẽ nhập liệu
        1 2 3;
        4 5 6;
        7 8 9;
        hoặc
        1 2 3;4 5 6;7 8 9
        Không được để khoảng trống gần dấu ";"
        - Khi nhập xong chúng ta click "Tính chi phí tối ưu", kết quả sẽ hiện thị ở ô 
        kết quả
        - Nhấn nút "Xóa các ô" để xóa hết nội dung của phiên tính toán trước
        Love from nhóm 3 - CNTT K18 CLC - 12/4/2022
    """
    helpTextBox.insert(END, HelpString)
    HelpApp.mainloop()

def AboutEvent():
    AboutApp = tk.Tk()
    AboutApp.title("Về chúng tôi")
    # HelpApp.geometry('640x480')
    AboutTextBox = Text(AboutApp, font=("bold", 14))
    AboutTextBox.grid(row=0, column=0)
    AboutString = """
            Đây là project được build bởi nhóm 3 gồm:
            - Nguyễn Vũ Hải - Lớp trưởng CNTT K18 CLC - ICTU (trưởng nhóm)
            - Vũ Quang Huy - Sinh viên CNTT K18 CLC - ICTU
            - Nguyễn Đức Thắng - Sinh viên CNTT K18 CLC - ICTU
            
            Phần mềm tính toán phương án tối ưu trong 
            bài toán vận tải bằng phương pháp chí phí 
            nhỏ nhất.
        """
    AboutTextBox.insert(END, AboutString)
    AboutApp.mainloop()


GeneralLabel = tk.Label(text="Tính toán theo chi phí cực tiểu", font=("bold", 22), padx=40, pady=50)

ThuLabel = tk.Label(text="Lượng thu", font=("bold", 14), padx=40, pady=50, width=20)
ThuTextBox = Text(window,height=3, width = 40,pady=10,font = ("bold", 20))

PhatLabel = tk.Label(text="Lượng phát", font=("bold", 14), padx=40, pady=50)
PhatTextBox = Text(window,height=3, width = 40, pady=10, font = ("bold", 20))

ChiPhiLabel = tk.Label(text="Ma trận \n chi phí", font=("bold", 14), padx=40, pady=50)
ChiPhiTextBox = Text(window,height=5, width = 40, pady=10, font = ("bold", 20))

Calculate = tk.Button(window, text="Tính chi phí tối ưu", font=("bold", 14), command = lambda:CalculateResult())

KetQua = tk.Label(text="Kết quả", font=("bold", 14), padx=40, pady=50)
KetQuaTextBox = Text(window,height=15, width = 45, pady=10, font= ("normal", 20))

Clear = tk.Button(window, text="Xóa các ô", font=("bold", 14), command = lambda:ClearAllTextBox())
Help = tk.Button(window, text="Trợ giúp", font=("bold", 14),  command = lambda:HelpEvent())
About = tk.Button(window, text="Về chúng tôi", font=("bold", 14),command = lambda:AboutEvent())

configureApp()

window.mainloop()