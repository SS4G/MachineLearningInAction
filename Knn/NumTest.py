# coding=utf-8
from KnnUtil   import *
from NumberPre import *
import NumberConfig as n_cfg
class NumTest:
    def __init__(self):
        self.Npre=NumberPre()
        self.KnnTool=KnnUtil()
    def testbench(self):
        train_tag_list=[]
        train_vec_list=[]
        test_tag_list=[]
        print("load data finished!")
        for case in self.Npre.train_cases:
            train_tag_list.append(case[1])
            train_vec_list.append(case[0])
        for case in self.Npre.test_cases:
            test_tag_list.append(case[1])
        length=len(self.Npre.test_cases)
        print("test vector and tran vector constructed!")
        error=0
        print(len(self.Npre.test_cases))
        print(len(self.Npre.train_cases))
        for index in xrange(length):
            print(index," case tested","error",error)
            res=self.KnnTool.find_NearestTag_KthNearst(self.Npre.test_cases[index][0],train_vec_list, train_tag_list, dims=1024,K=n_cfg.K )
            if res!=self.Npre.test_cases[index][1]:
                error+=1
        #print(error/length)
        return float(error)/float(length)
if __name__=="__main__":
    s=NumTest()
    print(s.testbench())
