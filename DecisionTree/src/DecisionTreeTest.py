# coding=utf-8
from tools import Tool
from Id3Util import *
from dec_tree_config import *
from functools import partial


class DecisionTreeTest:
    def __init__(self):
        self.tool = Tool()
        self.id3 = Id3Util()

    def testbench(self):
        dataset = self.tool.load_dataset(train_data_file)
        dataset_tags = map(lambda vec: vec[-1] == "no-lenses", dataset)
        print(dataset_tags)
        tree_root = self.id3.create_tree(dataset)
        self.tool.save_tree(tree_root)
        tree2_root = self.tool.load_tree()
        test_dataset = self.tool.load_dataset(test_data_file)
        sort_vec=partial(self.id3.sort_vector, dec_tree=tree2_root)

        zip_set=zip(map(sort_vec, test_dataset), map(lambda x: x[-1], test_dataset))
        right=reduce(sum, map(lambda x, y: 1 if x == y else 0, zip_set))
        right_rate = float(right)/len(test_dataset)
        print(test_dataset)
        print(right_rate)


if __name__ == "__main__":
    dt = DecisionTreeTest()
    dt.testbench()
