import numpy  as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os,sys

## nead reformatted_band.dat and KPOINTS

os.chdir(sys.path[0]) #使得在vscode中也可以使用相对路径

class Ansys():
    def __init__(self):
        self.name = ''
        self.x_axis = 'K-Path'
        self.y_axis = 'Energy (eV)'
        self.tick = []
        self.tick_label =[]
        self.sep = 0
        self.xlim = 0
        self.row_num = 0

    def set_tick(self):
        df = pd.read_csv('KPOINTS',sep='\s+', header=None)
        self.sep = int(df.loc[1,0])
        label = list(df[3])[4:]
        self.tick_label = [label[i] for i in range(0,len(label),2)]

    def read(self):  ##读取文件
        df = pd.read_csv('./REFORMATTED_BAND.dat',sep='\s+',header=None,skiprows=1)  
        x_list = list(df[0])
        self.xlim = x_list[-1]
        self.tick = [x_list[i] for i in range(0,len(x_list),self.sep)]
        self.row_num = df.shape[1]
        return df

    def plot(self,df):  #画图
        fig = plt.figure()
        ax1 = fig.add_subplot(111) ##共2*2有4张图，第一个
        for i in range(1,self.row_num):
            ax1.plot(df[0],df[i])
        ax1.set_ylim(-2,2)
        ax1.set_xlim(0,self.xlim)
        ax1.set_xticks(self.tick)
        ax1.set_xticklabels(self.tick_label)
        # add vertical lines at node positions
        ax1.axhline(0,linewidth=0.5,color='k')
        ax1.set_xlabel(self.x_axis)
        ax1.set_ylabel(self.y_axis)
        for i in self.tick:
            ax1.axvline(i,linewidth=0.5, color='k')
        plt.savefig('band_structure.png',dpi=600)
        plt.clf()

    def run(self):  #执行部分
        self.set_tick()
        data1 = self.read()
        self.plot(data1)
    
if __name__ == '__main__':  
    a = Ansys()
    # a.test()
    a.run()