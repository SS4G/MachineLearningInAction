# coding=utf-8
import math
import operator
import os
import datetime
#from numpy import *
class KnnUtil:
    def __init__(self):
        pass
    def get_us(self,time_pointa,time_pointb):
            return time_pointa.second*1000000+time_pointa.microsecond-time_pointb.second*1000000-time_pointb.microsecond
    def distance_calculator(self, point_a, point_b, dims=2):
        """
        calculate distance between 2 points
        point_a:tuple with dims
        point_b:tuple with dims
        dims:  how many dimension
        eg: dims=3
        point_a=(1,2,3)
        point_b=(4,5,6)
        """
        dis_sum = 0.0
        for dim in range(dims):
            dis_sum += (point_a[dim] - point_b[dim]) ** 2
        return dis_sum

    def find_NearestTag_KthNearst(self, point_a, point_list, point_tag_list, dims=2, K=10):
        """
        point_a:    需要判定的点
        point_list: 已经标注过的点
        point_tag_list:已经标注过的点的标注结果 与point_list按照索引一一对应 tag 应当是一个可比较的对象
        """
        points_amounts = len(point_list)
        res_tuple_list = [None] * points_amounts
        if points_amounts != len(point_tag_list):
            print("ERROR 000: 标注长度与样本点长度不一致")
            os.system("pause")
            raise RuntimeError

        for i in range(points_amounts):
            #tick0 = datetime.datetime.now()
            res_tuple_list[i] = (
            point_list[i], point_tag_list[i], self.distance_calculator(point_a, point_list[i], dims=dims))
            #tick1 = datetime.datetime.now()
        point_sorted_list = sorted(res_tuple_list, key=operator.itemgetter(2))

            #tick2 = datetime.datetime.now()
        # reduce by key
        tag_cnt_dict = {}
        for j in range(K):  # 进行最近k个元素的类别统计
            tag = point_sorted_list[j][1]
            if tag not in tag_cnt_dict:
                tag_cnt_dict[tag] = 1
            else:
                tag_cnt_dict[tag] += 1
        key_cnt_list = []
        for key in tag_cnt_dict:
            key_cnt_list.append((key, tag_cnt_dict[key]))
        key_cnt_list = sorted(key_cnt_list, key=operator.itemgetter(1), reverse=True)

        #print(self.get_us(tick1,tick0),self.get_us(tick2,tick1))
        return key_cnt_list[0][0]  # 返回距离最近的k个元素的 类别标签作为结果
#self test
if __name__ == "__main__":
    point0 = (1, 2)
    points = [(1, 2), (3, 4), (4, 5), (100, 300)]
    point_tag = ["A", "B", "A", "B"]
    tool = KnnUtil()
    type_final = tool.find_NearestTag_KthNearst(point0, points, point_tag, K=3)
    print(type_final)


