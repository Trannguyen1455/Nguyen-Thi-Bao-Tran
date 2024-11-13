from Bai130.utils.FuncUtils import tinh_khau_hao
gia_mua_moi=120000000
phi_van_chuyen=5000000
phi_lap_dat=1000000
so_nam_du_kien=10
nguyen_gia,khauhao_nam,khauhao_thang=tinh_khau_hao(gia_mua_moi,phi_lap_dat,phi_van_chuyen,so_nam_du_kien)
print("Nguyen gia tscd =", nguyen_gia)
print("Khau hao nam = ",khauhao_nam)
print('Khau hao thang = ',khauhao_thang)
