# coding=utf-8
import NumberConfig as n_cfg
import os
class NumberPre:
    """
    一次性装载数据以及测试用例
    """
    def __init__(self):
        self.test_cases =self.load_data(n_cfg.testcase_dir   )
        self.train_cases=self.load_data(n_cfg.train_dir      )
    def tointlist(self,str0):
        return [0 if y == "0" else 1 for y in str0]
    def load_data(self,cases_path):
        """
            case                   case-tag
        [ (str<1024characters>,numtag),... ] cases
        :param cases_path:
        :return:
        """
        marked_files=os.listdir(cases_path)
        whole_cases=[]
        for filename in marked_files:
            numtag=int(filename.split("_")[0])#获取数字的真实值
            one_case=[]#一个文件的向量
            marked_handle=open(cases_path+filename,"r")
            lines=marked_handle.readlines()
            for line in lines:
                if len(line)>3:
                    one_case.append(line.strip())
            whole_cases.append((self.tointlist("".join(one_case)),numtag))#将一个case及其标签都添加到一个元祖中
        return whole_cases


