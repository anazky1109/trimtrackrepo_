import json
import os

class BarberTracker:
    def __init__(self, filename='bookings.json'):
        self.filename = filename
        self.bookings = self._load_data()

    def _load_data(self):
        """Dyvta: Mengambil data dari file JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save_data(self):
        """Dyvta: Menyimpan data ke file JSON"""
        with open(self.filename, 'w') as f:
            json.dump(self.bookings, f, indent=4)

    def add_booking(self, name, time):
        # ... (Logika dari Reza akan masuk di sini) ...
        new_entry = {"name": name, "time": time}
        self.bookings.append(new_entry)
        self._save_data() # Simpan otomatis
        return "Berhasil!"
    def add_booking(self, customer_name, service_time):
        """Logika dari Reza: Validasi Bentrok & Jam Operasional"""
        if not customer_name:
            raise ValueError("Nama pelanggan tidak boleh kosong")
        
        # Validasi Jam Operasional
        if service_time < self.open_time or service_time >= self.close_time:
            raise ValueError(f"Barber tutup. Buka: {self.open_time}:00 - {self.close_time}:00")
        
        # Validasi Anti-Collision (Cek jadwal bentrok)
        for b in self.bookings:
            if b["time"] == service_time:
                return "FAILED: Jadwal sudah terisi, cari jam lain."

        # Jika lolos validasi, simpan data
        new_booking = {
            "id": len(self.bookings) + 1,
            "name": customer_name,
            "time": service_time
        }
        self.bookings.append(new_booking)
        self._save_data() # Memanggil fungsi Dyvta
        return f"SUCCESS: Booking untuk {customer_name} jam {service_time}:00"