import os
import matplotlib
class App_pre:
    def __init__(self):
        self.mark_enum = {"didntLike": 0, "smallDoses": 1, "largeDoses": 2}
        self.ori_data_list=[]
    def read_set(self,file_name):
        """
        return List [] each element is ((fly_list,game_list,ice_list),markResult_list)
        return List [] each element is ((飞行常客里程数,玩视频游戏占比,消耗的冰激凌数量),标注结果-喜欢程度)
        :param file_name:
        :return:
        """
        try :
            f=open(file_name,"r",encoding="utf-8")
            fly_list =[]
            game_list=[]
            ice_list =[]
            mark_list=[]
            for line in f:
                elements=line.split()
                fly_list .append(float(elements[0]))
                game_list.append(float(elements[1]))
                ice_list .append(float(elements[2]))
                mark_list.append(self.mark_enum[elements[3]])
                self.ori_data_list=[fly_list,game_list,ice_list]
            return (self.ori_data_list,mark_list)
        except FileNotFoundError:
            print("ERROR 2901:file_name not found")
            os.system("pause")
    def rescale(self,rescale_lists):
        """
        inplace operation
        :param rescaled_lists:List[List[],]
        :return:
        """
        for i in rescale_lists:
            scale=max(i)-min(i)
            for val in i :
                val=val/scale



