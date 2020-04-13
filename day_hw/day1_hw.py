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


# 定义查询号码
def query_record(name):
    query_result=[]
    query_ids=[]
    for record in record_list:
        if record["name"]==name:
          query_ids.append(record["record_id"])
          query_result.append(record)
    return query_ids,query_result

# 定义删除号码

def del_record(name):
    query_ids,query_result=query_record(name)
    if len(query_ids) == 0:
        print("不存在")
    else:
        if len(query_result)>1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id=input("请输入要删除的id：")
            if int(record_id)in query_ids:
                for record in record_list:
                    if int(record_id)==record["record_id"]:
                        record_list.remove(record)
            else:
                print("输入错误！")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
            while True:
                s=input("请问是否确认删除？（y/n）")
                if s in ["y","n"]:
                    if s=="y":
                        record_list.remove(query_result[0])
                    else:
                        pass
                    break
                else:
                    print("输入错误")


# 定义修改函数

def change_record(name):
    query_ids,query_result=query_record(name)
    if len(query_ids)==0:
        print("没有数据可以修改！")
    else:
        if len(query_result)>1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id =input("请输入要修改的信息：")
            if int(record_id)in query_ids:
                for record in record_list:
                    if int(record_id)==record["record_id"]:
                        phone_number=input("请输入修改的手机号：")
                        record["phone_number"]=phone_number
                        print("修改成功")
                        break
            else:
                print("输入错误")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
            phone_number=input("请输入修改的手机号：")
            query_result[0]["phone_number"]=phone_number
            print("修改成功")



if __name__=="__main__":
    while True:
        menu="""
        通讯录
        1.添加
        2.查询
        3.删除
        4.修改
        5.退出
        """
        print(menu)
        s=input("请选择操作：")
        if s in ["1","2","3","4","5"]:

            if s=="1":
                msg=add_record()
                print(msg)
            if s=="2":
                name=input("请输入您要查询的姓名：")
                query_ids,query_result=query_record(name)
                if len(query_ids)==0:
                    print("不存在")
                else:
                    for record in  query_result:
                        print("{}\t{}\t{}".format(record["record_id"],record["name"],record["phone_number"]))

            if s=="3":
                name=input("请输入要删除的姓名：")
                del_record(name)
            if s=="4":
                name=input("请输入要修改的姓名：")
                change_record(name)
            if s=="5":
                break
        else:
            print("输入有误")
            continue