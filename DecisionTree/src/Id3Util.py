# coding=utf-8
from math import log
from operator import itemgetter
class DecisionNode:
    def __init__(self,nodetype="Tag",tag="XX",split_attr_index=-1,split_attr_dict
    =None):
        """
        :param treetype: Leaf or Tree  Tag is leaf of the decision
        :param tag: only valid when Node is Leaf
        :param split_attr_index:
        :param split_attr_vals:
        """
        self.nodetype=nodetype# end of the tree Tag or tree
        self.tag=tag
        self.split_attr_index=split_attr_index
        self.split_attr_dict=split_attr_dict#type {attr_val:DecisionTree}
class Id3Util:
    """
    this class is used for Id3 decision Tree
    """
    def __init__(self):
        pass
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
            self.addbykey(tag_dict,vector[-1])
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

    def split_data_set(self, dataset, attr=None,val=None):
        """
        return dataset which attr==val
        :param dataset :wh
        :param attr: 信息增益最大的属性的下标
        :param val : 对应的下标的值
        :return:
        """
        # x= map(lambda vec:vec[:attr].extend(vec[attr+1:]),filter(lambda vec:vec[attr]==val,dataset))
        x = map(lambda vec: vec[:attr]+vec[attr+1:], filter(lambda vec:vec[attr]==val,dataset))
        # todo very low performance
        return x

    def is_data_set_pure(self, dataset):

        datataga = dataset[0]
        datatagb = datataga[-1]
        dataset_tags = map(lambda vec:vec[-1] == datatagb, dataset)
        return reduce(lambda x, y: x and y, dataset_tags)  # 所有标签都一致返回True 否则返回 False

    def create_tree(self, dataset):
        """
        retrun handler of the Decision Tree
        :param dataset:
        :return:
        """

        if self.is_data_set_pure(dataset):  # 递归结束条件 - 所有数据集处于一个类别的tag中
            return DecisionNode(nodetype="Leaf", tag=dataset[0][-1])
        elif len(dataset[0]) == 1:   # 所有的特征都消耗完了
            return DecisionNode(nodetype="Leaf", tag=dataset[0][-1])  # ---Todo 需要实现多数表决
        # 从数据集中选出当前信息增益最大的属性的下标
        best_split_attr = self.choose_best_attr(dataset)
        attr_set = set([vec[best_split_attr] for vec in dataset])
        new_datasets = []
        attr_val_dict = {}
        for attr_val in attr_set:
            new_datasets.append((self.split_data_set(dataset, attr=best_split_attr, val=attr_val),attr_val))
        for new_set in new_datasets:
            attr_val_dict[new_set[1]] = self.create_tree(new_set[0])  # 将用对应attr_val生成的树添加到当前树的字典中
        return DecisionNode(nodetype="Tree",split_attr_index=best_split_attr,split_attr_dict=attr_val_dict)

    def sort_vector(self, vector, dec_tree=None):
        tmp_tree=dec_tree
        vector_copy=[]
        vector_copy[:]=vector[:]#创建一个原始向量的副本 不要修改他
        while tmp_tree.nodetype!="Leaf":
            tmp_tree=tmp_tree.split_attr_dict[vector_copy[tmp_tree.split_attr_index]]
            vector_copy[:tmp_tree.split_attr_index].extend(vector_copy[tmp_tree.split_attr_index+1:])
        return tmp_tree.tag

    def show_tree(self,indent,tree_root):
        if tree_root.nodetype=="Leaf":
            print(indent*"\t"+tree_root.tag)
        else:
            for key in tree_root.split_attr_dict:
                print(indent*"\t"+str(tree_root.split_attr_index))
                self.show_tree(indent+1,tree_root.split_attr_dict[key])
if __name__ == '__main__':
    test_set=[
               ["a","1","^","tag0"],
               ["b","2","^","tag1"],
               ["c","3","%","tag2"],
               ["d","3","%","tag3"],
               ["d","3",")","tag4"],
             ]
    t = Id3Util()
    result=t.split_data_set(dataset=test_set, attr=0, val="d")
    print result