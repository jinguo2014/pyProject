class StuInfo:
    '学生类'
    stu_count=0;

    def __init__(self,name,ege):
        self.name=name;
        self.ege=ege;
        StuInfo.stu_count+=1;
    def display_stu_count(self):
        print("学生个数：",StuInfo.stu_count);

    def dis_stu_info(self):
        print("学生姓名：",self.name,"学生年龄：",self.ege);

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
