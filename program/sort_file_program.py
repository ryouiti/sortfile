'''ファイル名の先頭に()がついたファイルを対象とする。
自動的に()の中にある名前のディレクトリを作成して、()のついたファイルをディレクトリに移動するプログラム
例1
(sample)sample.text
sampleディレクトリが作られて、sample.textがsampleディレクトリに移動する
例2
(sample)(method)sample_method.text
(1)sampleディレクトリが作られる
(2)sampleディレクトリの中にmethodディレクトリが作られる
(3)sample_method.textがmethodディレクトリに移動する
'''
import os
import re
import shutil
import sys
import tkinter.filedialog
# def select_mode(option = sys.argv[0])->int:
#     option=option.lower()
#     if option =="-n":
#         mode  = 1
#     else:
#         mode = 2
#     return mode

# def select_dir_bymode(mode:int)->str:#ディレクトリをモードによって選ぶ
#     nowdir =""
#     if mode==1:
#         nowdir = os.path.dirname(__file__)
#     if mode==2:
#         nowdir =os.path.abspath(os.path.join(__file__,os.pardir,os.pardir))#os.pardirは親ディレクトリを参照する文字列 os.path.joinを組み合わせることで親ディレクトリが得られる
#     return nowdir


def GUI_select_directory()->str:
    iDir = os.path.abspath(os.path.dirname(__file__))
    selected_file_path = tkinter.filedialog.askdirectory(initialdir = iDir)
    return  selected_file_path

def rogo_deployment(rogolist):
    rogo_split=""
    for rogo in rogolist:
        rogo_split=rogo.replace(")("," ").split(" ")
    return rogo_split


ROGO_RE = re.compile(r"\((.*)\)")
def sort_file_program():
    user_selectdir = GUI_select_directory()
    nowdir = user_selectdir
    for selectdir_list_name in os.listdir(nowdir):
        if rogolist:=ROGO_RE.findall(selectdir_list_name):
            rogo_split = rogo_deployment(rogolist)
            for rogo in rogo_split:
                rogo_abspath = os.path.join(nowdir,rogo)
                if not os.path.exists(rogo_abspath):
                    os.makedirs(rogo_abspath)
                shutil.move(os.path.join(nowdir,selectdir_list_name),rogo_abspath)
                nowdir = os.path.join(nowdir,rogo)
        nowdir = user_selectdir

if __name__=="__main__":
    sort_file_program()
