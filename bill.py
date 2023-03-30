class Hang_hoa:
    def __init__(self):
        self.hanghoa = {}
    def them_hang_hoa(self):
        so_luong = int(input('nhập số lượng hàng muốn thêm:'))
        for i in range(so_luong):
            name = input('nhập tên hàng: ')
            price = float(input('nhập số tiền hàng: '))
            self.hanghoa[name] = price
    def xoa_hang_hoa(self):
        so_luong = int(input('nhập số lượng loại mặt hàng muốn xóa:'))
        for i in range(so_luong):
            name = input('nhập tên hàng: ')
            if name in self.hanghoa:
                del self.hanghoa[name]
                print(f'Đã xóa hàng {name}')
            else:
                print('tên hàng bạn nhập không chính xác! ')
    def In_hang_hoa(self):
        for i in self.hanghoa:
            print(f'{i} : {self.hanghoa[i]} vnd')
class Hoa_don(Hang_hoa):
    def __init__(self):
        self.so_luong = {}
        self.so_tien = {}
        self.tong_tien = 0 
    def mua_hang_hoa(self):
        check = int(input('nhập số loại mặt hàng bạn muốn mua'))
        for i in range(check):
            check2 = 0
            while (check2 == 0):
                name = input('nhập tên hàng: ')
                for hang in self.hanghoa:
                    if name == hang:                    
                        so_luong = int(input("nhập số lượng: "))
                        self.so_luong[name] = so_luong
                        self.so_tien[name] = so_luong * self.hanghoa[name]
                        check2 = 1
                        break
                if check2 == 0:
                    print('tên hàng bạn nhập không chính xác,vui lòng nhập lại ')
                   
    def thanh_tien(self):
        tong= 0
        for tien in self.so_tien:
            tong += self.so_tien[tien]
        self.tong_tien = tong 
    def In_hoa_don(self):
        for thong_tin in self.so_tien:
            print(f'{thong_tin} -- số lượng: {self.so_luong[thong_tin]} -- thành tiền: {self.so_tien[thong_tin]} ')
        print(f'Tổng tiền hàng: {self.tong_tien} vnd')

t = Hoa_don()
t.hanghoa = menu = {'cơm': 5000, 'canh': 6000, 'rau': 7000, 'cá': 8000}
t.In_hang_hoa()
print("--------------------------------")
'''
t.them_hang_hoa()
t.xoa_hang_hoa()
t.In_hang_hoa()
'''
print("--------------------------------")

t.mua_hang_hoa()
t.thanh_tien()
t.In_hoa_don()



