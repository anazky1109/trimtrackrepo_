import pytest
from app.tracker import TrimTrack

@pytest.fixture
def tracker():
    return TrimTrack()

def test_add_log_success(tracker):
    res = tracker.add_log("Lari Pagi", 30)
    assert res["activity"] == "Lari Pagi"
    assert len(tracker.records) == 1

def test_invalid_activity(tracker):
    with pytest.raises(ValueError, match="Nama aktivitas harus diisi"):
        tracker.add_log("", 10)

def test_total_calculation(tracker):
    tracker.add_log("Coding", 60)
    tracker.add_log("Meeting", 30)
    assert tracker.get_total_duration() == 90