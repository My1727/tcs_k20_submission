ma_quan_sat = str(input("Nhap ma quan sat: "))
ten_dai_luong = str(input("Nhap ten dai luong: "))
gia_tri_do = float(input("Nhap gia tri do: "))
don_vi = str(input("Nhap don vi: "))
# 5.2. Gan thoi diem hien tai
from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
# 5.3. Xuat ban ghi bang f-string
print(f"Ma quan sat : {ma_quan_sat}")
print(f"Dai luong : {ten_dai_luong}")
print(f"Gia tri : {gia_tri_do:.2f}{don_vi}")
print(f"Thoi diem : {thoi_diem_text}")