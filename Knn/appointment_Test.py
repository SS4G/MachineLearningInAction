from KnnUtil import *
from config  import *
from App_pre import *
from random  import *
class AppointmentTest:
    def __init__(self):
        self.knntool=KnnUtil()
        self.pre=App_pre()
        pass
    def main_test(self):
        #读取原始的标记数据
        ori_data_set, mark_result=self.pre.read_set(original_data_set)

        #归一化处理数据讲三个`部分的数据都变成一样的权重
        self.pre.rescale(ori_data_set)#原地归一化操作

        ori_marked_length = len(ori_data_set)
        test_length = ori_marked_length // 5

        f=open(rescale_result_file,"w",encoding="utf-8")
        for i in range(test_length):#randomly get 20% for test
            rand_index=randint(0,ori_marked_length)
            f.write("\t".join((ori_data_set[0][rand_index], ori_data_set[1][rand_index], ori_data_set[2][rand_index],mark_result[rand_index])))
            #save the test data
        f.close()

        #构建好标记点向量
        marked_points = []
        for i in range(ori_marked_length):
            marked_points.append((ori_data_set[0][i], ori_data_set[1][i], ori_data_set[2][i]))

        #测试过程
        right=0
        for line in f:
            x = line.split("\t")
            test_point=(float(x[0]),float(x[1]),float(x[2]))
            test_mark =int(x[4])
            judge_type=self.knntool.find_NearestTag_KthNearst(point_a=test_point,point_list=marked_points,point_tag_list=mark_result,dims=3,K=K)
            if judge_type==test_mark:
                right+=1
        print("total test case:",test_length)
        print("total right:",right)
        print("right rate: ",100*right/test_length,"%")


if __name__ == "__main__":
    print()