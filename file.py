# -*- coding:utf8 -*-
import os
import shutil

# 定义一个遍历文件的方法
class ErgodicFolder:

    folder = {'乡镇':['于田','南江','枚江','衙前','大坑','上坑','黄坑','草林','珠田','巾石','盆珠','堆前','滁洲','大汾','淋洋','左安','汤湖','碧洲','双桥','横岭','新江','扬芬','五江','西溪','戴家埔','营盘圩','禾源','高坪'],'县直':['中医院','人民医院','卫监','疾控中心','妇保','康复'],'民营':['光华','博爱','仁爱','众康','滨江','康宁','云岭']}
    root = ''
    putroot = ''

    def __init__(self,root):
        save = '\\save'
        if not os.path.exists(root+save):
            os.mkdir(root+save)
        self.putroot = os.path.join(root,'save')
        print('begin')
        self.root = root
        for key,value in self.folder.items():

            partpath = os.path.join(self.putroot,key)

            if not os.path.exists(partpath):
                os.mkdir(partpath)

            for xiashu in value:
                partpath2 = os.path.join(partpath,xiashu)
                if not os.path.exists(partpath2):
                    os.mkdir(partpath2)

                pass

    # 处理文件方法：针对不同文件类型做处理
    def process_file(self, file):
        
        FileName = file.split('.')[-2]

        for key,value in self.folder.items():
            
            partpath = os.path.join(self.putroot,key)
            
            for xiashu in value:
                partpath2 = os.path.join(partpath,xiashu)
                if xiashu in file:
                   
                    self.mycopyfile(file,partpath2+'\\')
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
            srcfpath,srcfname=os.path.split(srcfile)
        if not os.path.exists(fpath):
        
            os.mkdir(fpath)
       
       
        if not os.path.exists(dstfile+srcfname):
            print('正在保存...')
            print(dstfile+srcfname)
            shutil.copyfile(srcfile, dstfile+srcfname)

    def get_filelist(self, dir, Filelist):
        newDir = dir
        if os.path.isfile(dir):
            Filelist.append(dir)
        elif os.path.isdir(dir):
            if not os.listdir(dir): # 判断文件夹是否为空
                print(dir)
                # file = open(dir+'/gitee.txt','w')
                # file.close()
            for s in os.listdir(dir):
                newDir = os.path.join(dir, s)
                self.get_filelist(newDir, Filelist)
        return Filelist






dir = input('请输入文件目录:')
E = ErgodicFolder(dir)
E.ergodic_path_list(dir)
print('*'*50)
print('空文件夹：')
E.get_filelist(dir+'\\save',[])



