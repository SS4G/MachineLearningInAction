from KnnUtil import *
from config  import *
from App_pre import *
class AppointmentTest:
    def __init__(self):
        self.knntool=KnnUtil()
        self.pre=App_pre()
        pass
    def main_test(self):
        ori_data_set, mark_result=self.pre.read_set(original_data_set)
        self.pre.rescale(ori_data_set)#rescale the ori data
        ori_marked_length = len(ori_data_set)
        f=open(rescale_result_file,"w",encoding="utf-8")
        for i in range(ori_marked_length//5):#randomly get 20% for test
            f.write("\t".join((ori_data_set[0][i], ori_data_set[1][i], ori_data_set[2][i])))
        f.close()

        f=open(rescale_result_file,"r",encoding="utf-8")




        #read the test data
        ori_test_set, mark_test_result = self.pre.read_set(original_data_set)

        test_length = len(ori_test_set)

        # reshape the ori data to list[(fly,game,ice),]
        marked_points = []
        for i in range(ori_marked_length):
            marked_points.append((ori_data_set[0][i], ori_data_set[1][i], ori_data_set[2][i]))
        # reshape the ori data to list[(fly,game,ice),]
        test_points = []
        for i in range(ori_marked_length):
            test_points.append((ori_test_set[0][i], ori_test_set[1][i], ori_test_set[2][i]))


        #test
        right=0
        for j in range(test_length):
            judge_type=self.knntool.find_NearestTag_KthNearst(point_a=test_points[j],point_list=marked_points,point_tag_list=mark_result,dims=3,K=K)
            if judge_type==mark_test_result[j]:
                right+=1
        print("total testcase:",test_length)
        print("total right:",right)
        print("right rate: ",100*right/test_length,"%")


if __name__ == "__main__":
    print()