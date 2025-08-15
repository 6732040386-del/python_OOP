# เขียนโปรแกมสร้าง clacc ชื่อ people โดยมี attribute และ method ดังนี้
# attributr
# name เป็นชื่อบุคคล
# ade เป็นอายูของบุคคล
# method
#    Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ
#    my name is <name>.  I'm <age> year old

class people:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def Introduce(self):
        print("my name is {}. i'm {} year old.".format(self.name ,self.age))
person = people("ฝน", 20)
person.Introduce()


