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