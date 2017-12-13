from com.jiyun.test import stu_info,zhang_san;

stu=stu_info.StuInfo("王五",56);
# stu1=stu_info.StuInfo("赵六",23);
# stu1.dis_stu_info();
# stu1.display_stu_count();
stu.sex="女";
stu.sex="男";

# del stu.sex;
# print(stu.sex)
stu_name=getattr(stu,"name");
print(stu_name)
print(hasattr(stu, 'age'))

print ("Employee.__doc__:", stu_info.StuInfo.__doc__)
print ("Employee.__name__:", stu_info.StuInfo.__name__)
print ("Employee.__module__:", stu_info.StuInfo.__module__)
print ("Employee.__bases__:", stu_info.StuInfo.__bases__)
print ("Employee.__dict__:", stu_info.StuInfo.__dict__)

# del stu

zhang_san_info=zhang_san.ZhangSan();

zhang_san_info.dis_stu_info();

print(issubclass(zhang_san.ZhangSan,stu_info.StuInfo));

print(isinstance(zhang_san_info,stu_info.StuInfo))
