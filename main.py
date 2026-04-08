
from app.tracker import BarberTracker
import sys

def main():
    barber = BarberTracker()
    
    while True:
        print("\n" + "="*30)
        print("   TRIMTRACK BARBER BOOKING   ")
        print("="*30)
        print("1. Tambah Booking Baru")
        print("2. Lihat Jadwal Hari Ini")
        print("3. Hapus/Batal Booking")
        print("4. Keluar")
        
        pilihan = input("\nPilih menu (1-4): ")

        if pilihan == '1':
            nama = input("Masukkan Nama Pelanggan: ")
            try:
                jam = int(input("Masukkan Jam Booking (9-20): "))

                hasil = barber.add_booking(nama, jam)
                print(f"\n[SISTEM]: {hasil}")
            except ValueError as e:
                print(f"\n[ERROR]: {e}")

        elif pilihan == '2':
            print("\n" + barber.get_schedule_report())

        elif pilihan == '3':
            try:
                id_booking = int(input("Masukkan ID Booking yang akan dihapus: "))
                if hasattr(barber, 'delete_log'): 
                    try:
                        barber.delete_log(id_booking)
                        print("\n[SISTEM]: Booking berhasil dihapus.")
                    except ValueError as e:
                        print(f"\n[ERROR]: {e}")
                else:
                    print("\n[SISTEM]: Fitur hapus belum diimplementasi.")
            except ValueError:
                print("\n[ERROR]: Masukkan ID dalam bentuk angka.")

        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan TrimTrack Barber!")
            sys.exit()

        else:
            print("\n[ERROR]: Pilihan tidak valid.")

if __name__ == "__main__":
    main()