import os.path
dict={}
def showMenu():#显示主菜单函数（10分）
    print('-'*30)
    print("   学生通讯录管理系统    v1.0")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生")
    print("4. 查询学生")
    print("5. 获取所有学生通讯信息")
    print("6. 保存信息")
    print("7. 退出系统")
    print("-"*30)

def saveToFile():#将dict中的信息保存信息到backup.data文件中（10分）
    f=open('backup.data','w',encoding='utf-8')# 打开backup.data文件
    f.write(str(dict))# 将字典写入backup.data文件
    f.close()# 关闭文件


def recoverData():#从backup.data文件中导入信息到dict中。（10分）
    global dict# 全局变量
    if os.path.exists('backup.data'):# 如果当前路径下存在backup.data
        f=open("backup.data",'r',encoding='utf-8')# 则打开backup.data
        content=f.read()# 读取backup.data
        dict=eval(content)# 将内容传输给全局定义的字典
        f.close()# 关闭文件


def getSelcet() :#选择功能号（5分）
    try:
        selectNum=int(input("请输入选择的序号："))# 捕获一个序号
    except:
        return 0
    return selectNum# 返回这个序号



def addstuInfo():#添加学生（10分）
    name = input("你当前是做添加操作，请输入要添加的名片信息---姓名:")
    sex = input("请输入要添加的名片信息---性别:")
    telphone = input("请输入要添加的名片信息---手机号码：")
    dict[name]={"性别":sex,"电话":telphone} # 给每个学生添加信息
    print(dict)# 展示数据



    
def delstuInof():#删除学生（10分）
    name = input("你当前是做删除学生操作，接下来请输入要删除人的姓名：")
    if name not in dict.keys():# 如果字典中没有该学生信息输出提示
        print("没有找到要删除的学生")
        return 0
    del dict[name] # 删除字典中该学生信息
    print("删除成功，当前剩下的学生名片还有：")
    for i in dict.keys():# 对字典的键进行遍历
        print("姓名"+":"+i,end=' ')# 输出姓名
        for k in dict[i]:
            print(k+':'+dict[i][k],end=' ')# 输出其他信息
        print()



def modifystuInfo():#修改学生（10分）
    name = input("你当前是做修改学生操作，接下来请输入要修改人的姓名：")
    sex_new=input("请输入新的性别为：")
    number_new=input("请输入新手机号码为：")
    dict[name]['性别']=sex_new# 修改性别信息
    dict[name]['电话']=number_new# 修改电话信息
    print("学生 "+name+' 信息被修改为：')
    print(dict[name])



    
def seckstuInfo():#查询学生（5分）
   name=input("你当前是做查询学生操作，接下来请输入要查询人的姓名：")
   if name not in dict.keys():# 如果字典中没有该学生
       print("查无此学生")
       return 0
   else:
       for i in dict[name].values():# 输出该学生的信息
           print(i)


   
def showstuInfo():#获取所有学生通讯信息函数（10分）
    print("当前的名片有：")
    for i in dict.keys():
        print(i,end='')
        print(dict[i])

    
def exitSystem():#退出系统函数(5分)
    print("系统已退出")
    return 0



def main():#(5分)
    recoverData()#从backup.data文件中导入信息到dict中
    while True:
        showMenu()#显示主菜单函数
        num = getSelcet()  #选择功能号函数
        if num == 1:
            addstuInfo()#添加学生
        elif num == 2:
            delstuInof()#删除学生
        elif num == 3:
            modifystuInfo()#修改学生
        elif num == 4:
            seckstuInfo()#查询学生
        elif num == 5:
            showstuInfo()#获取所有学生通讯信息
        elif num == 6:
            saveToFile()#将dict中的信息保存信息到backup.data文件中
        elif num == 7:
            exitSystem()#退出系统
            break
        else:
            print("你的输入有误，请重新输入..")
main()