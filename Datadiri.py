class datadiri : 
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama 
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan 
        self.fakultas = fakultas 
        self.kampus = kampus 
    
    def tampilkandata(self) : 
        print(f"nama = {self.nama}" )
        print(f"kelas = {self.kelas}")
        print(f"nim = {self.nim}")
        print(f"jurusan = {self.jurusan}")
        print(f"fakultas = {self.fakultas}")
        print(f"kampus = {self.kampus}")
        
data = datadiri ("Roaini alfiona widyanto", "2023D", "23091397111", "D4 Manajemen Informatika", "Vokasi", "Universitas Negeri Surabaya")

data.tampilkandata()
