## data format for this tool
### tree plot tool
we use JSON format to describe a tree 
if a tree logic is below:

![tree](http://note.youdao.com/yws/public/resource/fc1de53b6446c9f6c2210ece757e5ff9/xmlnote/WEBRESOURCE679220f4af7a472762ff83f367ba5945/14056)
#### Json obj=dict{str:list(Json obj)}
```JSON
{"node0_0":[
    {"node1_0":[
        {"node2_0":null},
        {"node2_1":null}
        ]    
    },
    
    {"node1_1":[
        {"node2_2":null},
        {"node2_3":null}
        ]    
    },
    
    {"node1_2":[
        {"node2_4":null},
        {"node2_5":null}
        ]    
    }
    
    ]
}
```
