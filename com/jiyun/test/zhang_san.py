from com.jiyun.test import stu_info;
class ZhangSan(stu_info.StuInfo):
    def __init__(self):
        self.name="张三";
        self.ege=23;
        print("调用子类的构造方法")
