# -*- coding:utf8 -*-
import os
import shutil

# 定义一个遍历文件的方法
class ErgodicFolder:

    folder = {'乡镇':['于田','南江','枚江','衙前','大坑','上坑','黄坑','草林','珠田','巾石','盆珠','堆前','滁洲','大汾','淋洋','左安','汤湖','碧洲','双桥','横岭','新江','扬芬','五江','西溪','戴家埔','营盘圩','禾源','高坪'],'县直':['中医院','人民医院','卫监','疾控中心','妇保','康复'],'民营':['光华','博爱','仁爱','众康','滨江','康宁','云岭']}
    root = r'C:\laragon\www\pyenv\filemanage\testdata'

    def __init__(self):
        print('begin')
        for key,value in self.folder.items():
            print(key)
            partpath = os.path.join(self.root,key)
            print('-'+partpath)
            if not os.path.exists(partpath):
                os.mkdir(partpath)
                print('创建目录')
            for xiashu in value:
                partpath2 = os.path.join(partpath,xiashu)
                if not os.path.exists(partpath2):
                    os.mkdir(partpath2)
                    print('创建目录')
                pass

    # 处理文件方法：针对不同文件类型做处理
    def process_file(self, file):
        FileName = file.split('.')[-2]

        for key,value in self.folder.items():
            
            partpath = os.path.join(self.root,key)
            
            for xiashu in value:
                partpath2 = os.path.join(partpath,xiashu)
                if xiashu in file:
                    print(2)
                    self.mycopyfile(file,partpath2)
                pass

    def ergodic_path_list(self, path):
        os.chdir(path)  # 进入到目标路径，类似命令行中的cd命令
        file_lists = os.listdir()  # 获取当前目录中所有文件夹和文件列表
        for file in file_lists:  # 遍历当前路径中的所有文件
            if os.path.isfile(file):  # 处理文件
                self.process_file(file)
            if os.path.isdir(file):  # 如果是文件夹，则调用函数自身再次遍历该文件夹
                self.ergodic_path_list(file)
        # 当前文件夹遍历结束，返回上级目录继续遍历
        os.chdir('..')


    def mycopyfile(self,srcfile,dstfile):
        if not os.path.isfile(srcfile):
            print("%s not exit!" % (srcfile))
        else:
            fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
            shutil.copyfile(srcfile,dstfile)
         #print("copy %s" % (srcfile,dstfile))

if __name__ == '__main__':
    path = r'C:\laragon\www\pyenv\filemanage\testdata'
    E = ErgodicFolder()
    E.ergodic_path_list(path)





