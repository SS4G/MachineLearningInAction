# coding=utf-8
from math import log
from operator import itemgetter
class Id3Util:
    """
    this class is used for Id3 decision Tree
    """
    def addbykey(self,dict0,key):
        """
        向对应字典的对应键的位置加1
        如果这个键不存在那么就在字典中创建这个键后操作
        :param dict0:
        :param key:
        :return:
        """
        if key not in dict0:
            dict0[key]=1
        else :
            dict0[key]+=1
    def __init__(self):
        pass
    def calc_shannon_entropy(self,data_set,attr_index=None,attr_val=None):
        """
        以tag计算香侬熵
        :param data_set:
        :param attr_index:需要计算的属性的索引位置 即哪一个属性
        :param attr_val:  对应索引的值
        若attr_index以及attr_val均不为None 那么就在 符合vector[attr_index]==attr_val 的向量中计算香侬熵
        若都是用默认参数 那么就是计算所有传入数据集的香侬熵
        :return: value of Shanon Entropy
        """
        if attr_index!=None and attr_val!=None:
            data_set=filter(lambda vector:vector[attr_index]==attr_val,data_set)#筛选出符合要求的dataset

        tag_dict={}
        data_set_size=len(data_set)
        entropy=0.0
        for vector in data_set:
            self.addbykey(tag_dict,data_set[-1])
        for tag in tag_dict:
            pn=float(tag_dict[tag])/data_set_size
            entropy+= -pn*log(pn,2)#以2为底
        return entropy

    def choose_best_attr(self,data_set):
        attr_amount=len(data_set[0])-1#获取单个向量的属性个数
        data_set_amount=len(data_set)
        Hx=self.calc_shannon_entropy(data_set)
        entropy_promotes=[]
        for attr_i in range(attr_amount):#对向量剩余的属性依次迭代
            attr_vals=[vector[attr_i] for vector in data_set]
            attr_i_val_set=set(attr_vals)
            y_entropy=0.0 #H(X|Y)
            for attr_i_val in attr_i_val_set:
                p_yi=len(filter(lambda vector:vector[attr_i]==attr_i_val,data_set))/float(data_set_amount)#calculate P(Y=yi)
                y_entropy+=p_yi*self.calc_shannon_entropy(data_set, attr_index=attr_i, attr_val=attr_i_val)
            entropy_promotes.append((Hx-y_entropy,attr_i))
        max_promote=sorted(entropy_promotes,key=itemgetter(0),reverse=True)
        best_attr=max_promote[0][1]
        return best_attr
        #返回划分后的数据集 以及最终划分所选的索引
    def split_data_set(self,dataset,attr=None,val=None):
        """
        return dataset which attr==val
        :param attr:
        :param val:
        :return:
        """
        return filter(lambda vec:vec[attr]==val,dataset)

    def create_tree(self,dataset):
        dataset_tags=[vector[-1] for vector in dataset]
        diff_tag_amount=len(set(dataset_tags))
        if diff_tag_amount==1:
            pass#stop
        else:
            dataset
