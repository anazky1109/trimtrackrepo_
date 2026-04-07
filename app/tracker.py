class TrimTrack:
    def __init__(self):
        self.records = []

    def add_log(self, activity, duration):
        if not activity:
            raise ValueError("Nama aktivitas harus diisi")
        if duration <= 0:
            raise ValueError("Durasi harus lebih dari 0")
        entry = {"activity": activity, "duration": duration}
        self.records.append(entry)
        return entry

    def get_total_duration(self):
        return sum(item["duration"] for item in self.records)

    def reset(self):
        self.records = []
        return True