from utils.FuncUtils import tinh_chi_tiet_khau_hao
gia_mua_moi=120000000
phi_van_chuyen=5000000
phi_lap_dat=1000000
so_nam_du_kien=10
chitiet=tinh_chi_tiet_khau_hao(
    gia_mua_moi,phi_van_chuyen,phi_lap_dat, so_nam_du_kien)
print("Chi tiết khấu hao:")
print(chitiet)