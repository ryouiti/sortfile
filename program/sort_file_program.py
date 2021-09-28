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
def select_mode(option = sys.argv[0])->int:
    option=option.lower()
    if option =="-n":
        mode  = 1
    else:
        mode = 2
    return mode

def select_dir(mode:int)->str:#ディレクトリをモードによって選ぶ
    selectdir =""
    if mode==1:
        selectdir = os.path.dirname(__file__)
    if mode==2:
        selectdir =os.path.abspath(os.path.join(__file__,os.pardir,os.pardir))#os.pardirは親ディレクトリを参照する文字列 os.path.joinを組み合わせることで親ディレクトリが得られる
    return selectdir

ROGO_RE = re.compile(r"\((.*)\)")
def sort_file_program():
    selectdir = select_dir(select_mode())
    for selectdir_list_name in os.listdir(selectdir):
        if rogolist:=ROGO_RE.findall(selectdir_list_name):
            for rogo in rogolist:
                rogo_split = rogo.replace(")("," ").split(" ")
                for rogo in rogo_split:
                    rogo_abspath = os.path.join(selectdir,rogo)
                    if not os.path.exists(rogo_abspath):
                        os.makedirs(rogo_abspath)
                    shutil.move(os.path.join(selectdir,selectdir_list_name),rogo_abspath)
                    selectdir = os.path.join(selectdir,rogo)
        selectdir = select_dir(select_mode())

if __name__=="__main__":
    sort_file_program()
