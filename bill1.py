class Products:
    def __init__(self,product):
        self.products = product
        self.hoa_don = []

    def print_products(self):
        for product in self.products:              
            print(f'{product}:{self.products[product]} VND')

    def mua_hang(self):       
        quit = False
        while not quit:
            print('Nhap "N" neu muon huy mua hang')
            choice = input('Ban muon mua gi: ')
            check = 0
            for product in self.products:
                if choice == product:
                    so_luong = int(input('Ban muon mua bao nhieu: '))
                    thanh_tien = (hang_hoa[product]) * so_luong
                    self.hoa_don.append(product)
                    self.hoa_don.append(so_luong)
                    self.hoa_don.append(thanh_tien)
                    check = 1
            if check == 0:
                print('Hay nhap lai')
            if choice == 'N':
                quit = True
                print('Cam on da ung ho')
                check = 1   
    def print_bill(self):
        total = 0
        for i in range(0,len(self.hoa_don),3):
            print(f'{self.hoa_don[i]} * {self.hoa_don[i+1]} = {self.hoa_don[i+2]} VND')
            total += self.hoa_don[i+2]
        print(f'Ban can thanh toan : {total} VND')
        
                      
hang_hoa = {'keo' : 3000,'Kem' : 4000, 'tra sua' : 8000, 'hoa qua' : 15000}
customer = Products(hang_hoa)
print("----Menu----")
customer.print_products()
print("------------")
customer.mua_hang()
print("----Hoa Don Mua Hang----")
customer.print_bill()