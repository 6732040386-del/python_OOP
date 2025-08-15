# ClassInstanceVariable

# ClassInstanceVarble คือ ตัวแปรที่ทำงานภายใน class
# ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribีะำ)
# โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

# instance Veriable คือ ตัวแปรที่อยู่ภาคใน
# สามารถเข้าถึงข้อมูลส่วนนี้โดยจ้องสร้าง Object ขึ้นมา

# class Variable
class Employee:
    # class variable
    _minSalary = 12000
    _maxSalary = 50000
    _companyMame = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # instance Variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)


emp1 = Employee('ฝน', 50000, 'วิชาการ')
#print('เงินเดือนขั้นต่ำ = '+str(Employee._minSalary))
print(Employee._companyMame)