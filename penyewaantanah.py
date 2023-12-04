
class FSA:
    def __init__(self):
        self.current_state = 'start'
        self.customer_data = {}  # Dictionary untuk menyimpan data pelanggan

    def start(self):
        print("SISTEM PENYEWAAN TANAH & BANGUNAN")
        self.current_state = 'input_data'
        self.input_data()

    def input_data(self):
        print("Masukkan data pelanggan:")
        
        self.customer_data['nama'] = input("Nama: ")
        self.customer_data['alamat'] = input("Alamat: ")
        self.customer_data['nomer_hp'] = input("Nomor HP: ")
        self.customer_data['nik'] = input("NIK: ")
        self.current_state = 'choose_type'

    def choose_type(self):
        print("Pilih jenis sewa:")
        print("1. Tanah")
        print("2. Tanah + Bangunan")
        print("3. Bangunan")
        choice = int(input("Pilih jenis sewa (1/2/3): "))
        if choice == 1:
            self.customer_data['jenis_sewa'] = 'Tanah'
            self.current_state = 'choose_duration'
        elif choice == 2:
            self.customer_data['jenis_sewa'] = 'Tanah + Bangunan'
            self.current_state = 'choose_duration'
        elif choice == 3:
            self.customer_data['jenis_sewa'] = 'Bangunan'
            self.current_state = 'choose_duration'
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            self.choose_type()

    def choose_duration(self):
        print("Pilih durasi sewa:")
        print("1. Perhari")
        print("2. Perminggu")
        print("3. Perbulan")
        print("4. Pertahun")
        choice = int(input("Pilih durasi sewa (1/2/3/4): "))
        if choice == 1:
            self.customer_data['durasi_sewa'] = 'Perhari'
            self.current_state = 'negotiation_process'
        elif choice == 2:
            self.customer_data['durasi_sewa'] = 'Perminggu'
            self.current_state = 'negotiation_process'
        elif choice == 3:
            self.customer_data['durasi_sewa'] = 'Perbulan'
            self.current_state = 'negotiation_process'
        elif choice == 4:
            self.customer_data['durasi_sewa'] = 'Pertahun'
            self.current_state = 'negotiation_process'
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            self.choose_duration()

    def negotiation_process(self):
        print("Proses negosiasi...")
        # Di sini bisa dimasukkan kode untuk proses negosiasi, perjanjian harga, dll.
        self.current_state = 'rent_active'

    def rent_active(self):
        print(f"Sewa {self.customer_data['jenis_sewa']} selama {self.customer_data['durasi_sewa']} telah aktif.")
        self.current_state = 'finish'

    def finish(self):
        print("proses telah selesai.")
        self.current_state = 'end'

    def run(self):
        while self.current_state != 'end':
            if self.current_state == 'start':
                self.start()
            elif self.current_state == 'input_data':
                self.input_data()
            elif self.current_state == 'choose_type':
                self.choose_type()
            elif self.current_state == 'choose_duration':
                self.choose_duration()
            elif self.current_state == 'negotiation_process':
                self.negotiation_process()
            elif self.current_state == 'rent_active':
                self.rent_active()
            elif self.current_state == 'finish':
                self.finish()
            else:
                print("Terjadi kesalahan.")
                self.current_state = 'end'


# Inisiasi objek FSA
fsa = FSA()
# Menjalankan FSA
fsa.run()
