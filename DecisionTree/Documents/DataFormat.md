## data format

1. data_vector (一个条目的数据向量 单条的训练或者测试数据):  
  data_vector的最后一项是一个元组 表示标记结果  
List[attrA,attrB,attrC,...Tag_attr0]
2. dataset (多个数据向量构成的集合 表示一个数据集或者一个训练集):   
List[ data_vectorA,data_vectorB,data_vectorC...]
