import pytest
import os
from app.tracker import BarberTracker

@pytest.fixture
def temp_tracker():
    """Setup tracker dengan file JSON sementara khusus testing"""
    test_file = "test_db.json"
    tracker = BarberTracker(filename=test_file)
    yield tracker
    if os.path.exists(test_file):
        os.remove(test_file)

def test_reza_validation(temp_tracker):
    # Tes Anti-Collision Reza
    temp_tracker.add_booking("Anazky", 10)
    result = temp_tracker.add_booking("Dyvta", 10)
    assert "FAILED" in result

def test_dyvta_storage(temp_tracker):
    # Tes JSON Storage Dyvta
    temp_tracker.add_booking("Reza", 14)
    assert os.path.exists("test_db.json")

def test_talitha_report(temp_tracker):
    # Tes Standarisasi Talitha
    temp_tracker.add_booking("Z", 15)
    temp_tracker.add_booking("A", 9)
    report = temp_tracker.get_schedule_report()
    assert "[9:00] - A" in report # Pastikan A (jam 9) muncul duluan