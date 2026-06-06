import pytest
from unittest.mock import mock_open

from src import calc

class FakeDictReader:
    def __init__(self, data):
        self.data = getattr(self, '_test_data', [])
    def __iter__(self):
        return iter(self.data)
    @classmethod
    def set_test_data(cls, data):
        cls._test_data = data

def test_load_data(monkeypatch):
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        },
        {
            'date': '2026-01-01',
            'time': '18:00',
            'period': 'evening',
            'systolic': 130,
            'diastolic': 90,
            'weight': 72.0
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('builtins.open', mock_open(read_data='dummy data'))
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    assert calc.load_data('nothing') == fake_data

def test_load_data_when_data_is_imported_correctly(capsys, monkeypatch):
    '''Confirmation of data import for 3 rows, including 2 consecutive error rows.'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 'abc',
            'diastolic': 80,
            'weight': 70.5
        },
        {
            'date': '2026-01-01',
            'time': '18:00',
            'period': 'night',
            'systolic': 130,
            'diastolic': 90,
            'weight': 72.0
        },
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 99,
            'weight': 72.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert data == [fake_data[2]]
    out = capsys.readouterr().out
    assert "Error converting numerical value(systolic) at line 1" in out
    assert "Invalid period: night at line 2" in out

def test_load_data_when_required_column_does_not_exist(capsys, monkeypatch):
    '''When a required column does not exist'''
    fake_data = [
        {
            'date': '2026-01-01',
            # 'time': '10:00', required column does not exist
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert "Required columns are missing at line 1" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_systolic_cannot_be_converted_to_int(capsys, monkeypatch):
    '''When systolic cannot be converted to int'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 'abc',
            'diastolic': 80,
            'weight': 70.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert "Error converting numerical value(systolic) at line 1" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_diastolic_cannot_be_converted_to_int(capsys, monkeypatch):
    '''When diastolic cannot be converted to int'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 'abc',
            'weight': 70.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert "Error converting numerical value(diastolic) at line 1" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_weight_cannot_be_converted_to_float(capsys, monkeypatch):
    '''When weight cannot be converted to float'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 'abc'
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert "Error converting numerical value(weight) at line 1" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_period_is_neither_morning_nor_evening(capsys, monkeypatch):
    '''When period is neither morning nor evening'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'afternoon',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('data/health_data.csv')
    assert "Invalid period: afternoon at line 1" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_the_file_is_not_found(capsys, monkeypatch):
    '''When the file is not found'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        }
    ]
    FakeDictReader.set_test_data(fake_data)
    monkeypatch.setattr('csv.DictReader', FakeDictReader)
    data = calc.load_data('nothing')
    assert "File not found" in capsys.readouterr().out
    assert len(data) == 0

def test_load_data_when_an_unknown_error_occurs(capsys, monkeypatch):
    '''When an unknown error occurs'''
    mock = mock_open()
    mock.side_effect = Exception('Unknown error')
    monkeypatch.setattr('builtins.open', mock)
    data = calc.load_data('data/health_data.csv')
    assert "Error loading data" in capsys.readouterr().out
    assert len(data) == 0

def test_is_data_empty_when_the_data_is_empty():
    '''When the data is empty'''
    fake_data = []
    assert calc.is_data_empty(fake_data)

def test_is_data_empty_when_the_data_is_not_empty():
    '''When the data is not empty'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        }
    ]
    assert not calc.is_data_empty(fake_data)

def test_filter_data_by_period_when_the_period_is_morning():
    '''When the period is morning'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        },
        {
            'date': '2026-01-01',
            'time': '18:00',
            'period': 'evening',
            'systolic': 130,
            'diastolic': 90,
            'weight': 72.0
        }
    ]
    data = calc.filter_data_by_period(fake_data, 'morning')
    assert data == [fake_data[0]]

def test_filter_data_by_period_when_the_period_is_evening():
    '''When the period is evening'''
    fake_data = [
        {
            'date': '2026-01-01',
            'time': '10:00',
            'period': 'morning',
            'systolic': 120,
            'diastolic': 80,
            'weight': 70.5
        },
        {
            'date': '2026-01-01',
            'time': '18:00',
            'period': 'evening',
            'systolic': 130,
            'diastolic': 90,
            'weight': 72.0
        }
    ]
    data = calc.filter_data_by_period(fake_data, 'evening')
    assert data == [fake_data[1]]

def test_calc_stats():
    '''The average, maximum, and minimum should be calculated correctly.'''
    fake_data = [120, 130, 120]
    data = calc.calc_stats(fake_data)
    assert data == {
        'average': 123.33,
        'maximum': 130,
        'minimum': 120
    }

def test_calc_weight_stats():
    '''The average, maximum, and minimum should be calculated correctly.'''
    fake_data = [
        {
            'weight': 70.5
        },
        {
            'weight': 72.0
        }
    ]
    data = calc.calc_weight_stats(fake_data)
    assert data == {
        'average': 71.25,
        'maximum': 72.0,
        'minimum': 70.5
    }

def test_calc_blood_pressure_stats():
    '''The average, maximum, and minimum should be calculated correctly.'''
    fake_data = [
        {
            'systolic': 120,
            'diastolic': 80
        },
        {
            'systolic': 130,
            'diastolic': 90
        }
    ]
    data = calc.calc_blood_pressure_stats(fake_data)
    assert data == {
        'systolic': {
            'average': 125,
            'maximum': 130,
            'minimum': 120
        },
        'diastolic': {
            'average': 85,
            'maximum': 90,
            'minimum': 80
        }
    }
