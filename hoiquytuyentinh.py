from __future__ import division, print_function, unicode_literals
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold, RepeatedKFold

from numpy import *
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import BaggingRegressor


df = pd.read_csv("data.csv", delimiter=',')
#define predictor and response variables
X = df[['bedrooms', 'bathrooms', 'sqft_living','floors']].values.reshape(-1,4)
Y = df['price']
#Splitting the data into Train and Test
model = LinearRegression()
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.3, random_state=0)
model.fit(xtrain, ytrain)
pred = model.predict(xtest)
master= tk.Tk()
master.title("Bài tập lớn")
master.geometry("600x400",)
tk.Label(master, text="Nhập thông số liên quan để dự đoán: ").grid(row=0, column=0)
tk.Label(master, text="Số phòng ngủ").grid(row=1, column=0)
tk.Label(master, text="Số phòng tắm").grid(row=2, column=0)
tk.Label(master, text="Dien tich ").grid(row=3, column=0)
tk.Label(master, text="so tang").grid(row=4, column=0)
tk.Label(master, text="Ket qua du doan: ").grid(row=5, column=0)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master,state='disabled')
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
tk.Label(master, text="Chọn chức năng:").grid(row=6,column=0)


def duDoan():
    
    check1=e1.get()
    check2=e2.get()
    check3=e3.get()
    check4=e4.get()
    check5=e5.get()
    if(check1 == "" or check2 == "" or check3== "" or check4== "" or float(check1) <=0 or float(check2) <=0 or float(check3) <=0 or float(check4) <=0):
        messagebox.showerror("Error", "Vui long nhập đúng thông số.")
    else:
        bien1 = float(check1)
        bien2 = float(check2)
        bien3 = float(check3)
        bien4 = float(check4)
        kqDuDoan = model.predict([[bien1,bien2,bien3,bien4]])
        e5.configure(state=tk.NORMAL)
        e5.insert(0,str(kqDuDoan))
    #messagebox.showinfo( "Kết quả dự đoán","Dự đoán giá của căn chung cư có "+str(bien1)+" phòng ngủ,"+str(bien2)+"phong tam,co dien tich la"+str(bien3)+"m^2 , co"+str(bien4)+"tang,co ket qua du doan la: "+str(kqDuDoan)+" tỷ VND")
tk.Button(master, 
          text='Dự đoán', 
          command=duDoan).grid(row=7, column=0, sticky=tk.W,pady=4)


tk.Button(master, 
          text='Thoát', 
          command=quit).grid(row=7, 
                                    column=4, 
                                    sticky=tk.W,
                                    pady=4)
def pthoiquy():
    a=model.coef_
    b=model.intercept_
    messagebox.showinfo( "Phương trình hồi quy","PT hồi quy có dạng: y = "+str(a[0])+" * x1 + "+str(a[1])+" * x2 + "+str(a[2])+" * x3 +"+str(a[3])+" * x4 +"+str(b))
tk.Button(master, 
          text='PT hồi quy', 
          command=pthoiquy).grid(row=7, 
                                column=1, 
                                sticky=tk.W,
                                pady=4)
def reset():
    check1=e1.get()
    check2=e2.get()
    check3=e3.get()
    check4=e4.get()
    check5=e5.get()
    if(check1 == "" and check2 == "" and check3== "" and check4== "" and check5== ""):
        messagebox.showinfo("reset","Cac o da reset")
    else:
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')
        e5.configure(state=tk.DISABLED)
         
tk.Button(master, 
          text='Reset', 
          command=reset).grid(row=7, 
                                column=2, 
                                sticky=tk.W,
                                pady=4)   

master.mainloop()
