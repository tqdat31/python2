class Student:
    
    def __init__(self,ID,ten):
        self.ID = ID
        self.ten = ten
        self.diem = {}
        self.gpa = 0
    def tinh_gpa(self):
        tong = 0
        for diem in self.diem.values():
            tong += diem
        self.gpa = tong/ len(self.diem) + self.gpa 
    def print_sv(self):
        print(f'ID : {self.ID} \n tên sv: {self.ten} \n điểm học phần:    ')
        for diem_mon in self.diem :
            print(f"điểm môn {diem_mon}: {self.diem[diem_mon]} ")
        print(f"GPA : {self.gpa}")
    def dk_tot_nghiep(self):
        if self.gpa /10 *4 >= 2.5:
            print('bạn đậu')
        else:
            print('bạn tạch')
    def them_mon(self) :
        so_mon = int(input('nhập số môn bạn muốn thêm: '))
        for i in range(so_mon) :
            nhap_mon  = input('nhập tên môn ')
            self.diem[nhap_mon] = float(input(f'nhập điểm môn {nhap_mon}'))

i = Student(1,'vu')
i.diem= {'python':9 , 'wed': 5 , 'english': 8}

i.tinh_gpa()
i.print_sv()
i.dk_tot_nghiep()
i.them_mon()
i.tinh_gpa()
i.print_sv()