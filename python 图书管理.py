import json
import os
save_path="c:/books.txt"

#加载本地数据
def load_books():
    #判断文件是否存在
    if not os.path.exists(save_path):
        return []
    else:
        f=open(save_path,'r')
        content=f.read()
        f.close()
        if len(content)==0:
            return []
        else:
            return json.loads(content)

books=load_books()

def save_books():
    f=open(save_path,'w')
    content=json.dumps(books)
    f.write(content)
    f.close()

def add_book():
    a=input("名称：")
    b=input("编号：")
    c=input("价格：")
    book={"name":a,"id":b,"price":c}
    books.append(book)
    save_books()

def find_book():
    name=input("输入查找名称：")
    #result=[]
    for book in books:
        if book["name"]==name:
           # result.append(book)
            print("名称:%s"%book["name"])
            print("编号:%s"%book["id"])
            print("价格:%s"%book["price"])


def delete_book():
    id=input("输入删除id：")
    for book in books:
        if book["id"]==id:
            books.remove(book)
    save_books()


def show_all_book():
    for book in books:
        print("名称:%s"%book["name"])
        print("编号:%s"%book["id"])
        print("价格:%s"%book["price"])


print("**************************************")
print("       欢迎来到***图书管理系统")
print("1、添加图书")
print("2、根据书名查找图书")
print("3、根据编号删除图书")
print("4、显示所有图书信息")
print("输入不同数字，使用不同功能")
print("**************************************")


while 1:
    a=int(input("请输入数字："))
    if a==1:
        add_book()
    elif a==2:
        find_book()
    elif a==3:
        delete_book()
    elif a==4:
        show_all_book()
    else:
        save_books()
        exit()
