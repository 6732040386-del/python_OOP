# FnClassObject
# ฟังก์ชั้นที่ทำงานร่วมกับ class และ object
from oop1 import Employee

# isinstance และ  ฟังก์ชั้นที่ทำงานร่วมกับ class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก c lass ที่เรานิยามหรือไม่
# die => แสดง attribute  และ object
# __class__ =>
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

emp1 = Employee('วิบูลย์', 50000, 'วิชาการ')
emp2 = Employee('เรณู', 25000, 'กิจการ')
emp3 = Employee('alther', 10000, 'อาคาร')
emp4 = Employee('lim',20000,'HR')


print(isinstance(emp1, Employee)) #ตรวจสอบว่า obj ถูกสร้างจาก class ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)
