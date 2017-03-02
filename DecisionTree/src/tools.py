# coding=utf-8
from dec_tree_config import *
from Id3Util import *
import cPickle as pickle
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
        f=open(tree_save_file,"wb")
        #self.tmpstr=pickle.dumps(deci_tree)
        pickle.dump(deci_tree,f)
        f.close()
    def load_tree(self):
        f=open(tree_save_file,"rb")
        tree=pickle.load(f)
        f.close()
        return tree
        #return pickle.loads(self.tmpstr)


