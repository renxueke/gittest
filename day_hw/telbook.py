# 实现一个通讯录，实现增删改查的功能

record_list=[]
record_id=0

def input_record():
    name=input("请输入您的姓名：")
    phone_number=input("请输入您的电话号码：")
    record={"name":name,"phone_number":phone_number}
    return record


# 定义增加号码

def add_record():
    record=input_record()
    global record_id
    record_id+=1
    record["record_id"]=record_id
    record_list.append(record)
    return "添加成功"


# 定义修改号码
def query_record(name):
    query_result=[]
    query_ids=[]
    for record in record_list:
        if record["name"]==name:
          query_ids.append(record["record_id"])
          query_result.append(record)
    return query_ids,query_result

# 定义删除号码

# def del_record():



if __name__=="__main__":
    while True:
        menu="""
        通讯录
        1.添加
        """
        print(menu)
        s=input("请选择操作：")
        if s in ["1","2","3","4","5"]:

            if s=="1":
                msg=add_record()
                print(msg)
