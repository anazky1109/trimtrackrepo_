import json
import os

class BarberTracker:
    def __init__(self, filename='bookings.json'):
        self.filename = filename
        self.bookings = self._load_data()
        
      
        self.open_time = 9
        self.close_time = 21

    def _load_data(self):
        """Dyvta: Memuat data dari JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except: return []
        return []

    def _save_data(self):
        """Dyvta: Menyimpan data ke JSON"""
        with open(self.filename, 'w') as f:
            json.dump(self.bookings, f, indent=4)

    def add_booking(self, customer_name, service_time):
        """Reza: Validasi Bentrok & Jam Operasional"""
        if not customer_name:
            raise ValueError("Nama pelanggan tidak boleh kosong")
        
        # Sekarang self.open_time sudah ada, tidak akan error lagi
        if service_time < self.open_time or service_time >= self.close_time:
            raise ValueError(f"Barber tutup. Buka: {self.open_time}:00 - {self.close_time}:00")
        
        for b in self.bookings:
            if b["time"] == service_time:
                return "FAILED: Jadwal sudah terisi"

        new_booking = {
            "id": len(self.bookings) + 1,
            "name": customer_name,
            "time": service_time
        }
        self.bookings.append(new_booking)
        self._save_data()
        return f"SUCCESS: {customer_name} jam {service_time}:00"

    def get_schedule_report(self):
        """Talitha: Standarisasi Output"""
        if not self.bookings:
            return "Belum ada jadwal hari ini."
        
        sorted_list = sorted(self.bookings, key=lambda x: x["time"])
        report = "=== JADWAL BARBER HARI INI ===\n"
        for b in sorted_list:
            report += f"[{b['time']}:00] - ID: {b['id']} - {b['name']}\n"
        return report

    def delete_log(self, booking_id):
        for i, b in enumerate(self.bookings):
            if b["id"] == booking_id:
                del self.bookings[i]
                self._save_data()
                return True
        raise ValueError(f"Booking dengan ID {booking_id} tidak ditemukan.")