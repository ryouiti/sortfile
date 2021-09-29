import os
import random
from typing import List
import tkinter.filedialog
import sort_file_program
sample_rogo = ["(sample)","(test)","(exam)","(example)","(specimen)","(evaluation)","(flag)"]

def random_rogo(sample_rogo:List[str])->str:
    rogo_num=random.randint(1,len(sample_rogo))
    rogo_sample = random.sample(sample_rogo,rogo_num)
    return "".join(rogo_sample)


def GUI_select_directory()->str:
    iDir = os.path.abspath(os.path.dirname(__file__))
    selected_file_path = tkinter.filedialog.askdirectory(initialdir = iDir)
    return  selected_file_path

user_select_dir = GUI_select_directory()
os.chdir(user_select_dir)

for i in  (str(i) for i in range(1000)):
    rogo= random_rogo(sample_rogo)
    dirname = rogo+"test" + i+".txt"
    if not os.path.exists(dirname):
        with open(dirname,"w") as f:
            f.write("")
sort_file_program.sort_file_program(user_select_dir)