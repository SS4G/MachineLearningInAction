# coding=utf-8
import matplotlib.pyplot as plt
import json
class TreePloter:
    """
    标准的json表示的树的节点 每个json对象应该只有一个键 切这个键是这个节点的值
    """
    def __init__(self,level_height=10):
        self.figure_name="default tree"

    def get_tree_depth(self,json_obj):
        """
        tree is in json format object
        :param json_tree:
        :return: depth of the tree
        """
        for key in json_obj:  # only one key in each json obj
            next_objs=json_obj[key]  # get list of next level json objs
            if next_objs==None:
                return 0
            else :
                next_level_depth=[]
                for next_obj in next_objs:
                    next_level_depth.append(self.get_tree_depth(next_obj))
                return 1+max(next_level_depth)

    def get_tree_width(self,json_obj):
        """
        只是一个大概的宽度 以一颗树的所有叶子节点之和作为一颗树的宽度
        :param json_tree:
        :return:amount of leaf node num
        """
        for key in json_obj:  # only one key in each json obj
            next_objs = json_obj[key]  # get list of next level json objs
            if next_objs==None:
                return 1  #if the json obj is leaf
            else:
                sums=0
                for next_obj in next_objs:
                    sums+=self.get_tree_width(next_obj)
                return sums

    def get_this_level_width(self,json_obj,level):
        """
        返回指定层级的节点数目 根节点在第零层
        :param json_obj:
        :return:
        """
        json_obj_keys = json_obj.keys()
        for key in json_obj_keys:  # only one key in each json obj
            next_objs = json_obj[key]
            if next_objs==None:
                return 0
            if level==0:
                return len(next_objs)
            else :
                sums=0
                for next_obj in next_objs:
                    sums+=self.get_this_level_width(next_obj,level-1)
                return sums

    def plot_main(self,json_obj):
        depth=self.get_tree_depth(json_obj)
        width=self.get_tree_width(json_obj)
        plt.figure(self.figure_name,figsize=(10,10))
        plt.subplot(111)
        plt.axis([0,depth,0,width])
if __name__=="__main__":
    tree_json=a="""
                {"n00": [
                    {"n10": [
                        {"n20": null},
                        {"n21": null}
                    ]
                    },

                    {"n11": [
                        {"n22": null},
                        {"n23": null}
                    ]
                    },

                    {"n12": [
                        {"n24": null},
                        {"n25": null}
                    ]
                    }

                ]
                }
                """
    tree_root=json.loads(tree_json)
    tp=TreePloter()
    tree_depth=tp.get_tree_depth(tree_root)
    tree_width=tp.get_tree_width(tree_root)
    each_level_width=[]
    for level in range(tree_depth+1):
        each_level_width.append(tp.get_this_level_width(tree_root,level))
    print("tree_depth      =",tree_depth        )
    print("tree_width      =",tree_width        )
    print("each_level_width=",each_level_width)