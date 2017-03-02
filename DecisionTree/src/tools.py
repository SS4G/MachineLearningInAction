# coding=utf-8
from dec_tree_config import *
from Id3Util import *
import pickle
class Tool:
    def __init__(self):
        self.tmpstr=""
    def load_dataset(self,datafile_path):
        """
        :param datafile_path:
         data fomat (attr0,attr1....,tag)
        :return dataset:
        """
        dataset=[]
        f=open(datafile_path,"r")
        for line in f :
            dataset.append(line.split())
        return dataset

    def save_tree(self,deci_tree):  # todo:save tree in file should be solved
        f=open(tree_save_file,"w")
        self.tmpstr=pickle.dumps(deci_tree)
        #f.write(pickle.dumps(deci_tree))
        f.close()
    def load_tree(self):
        f=open(tree_save_file,"r")
        line=f.readline()
        f.close()
        # return pickle.loads(line)
        return pickle.loads(self.tmpstr)


