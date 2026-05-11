import pytest
from unittest.mock import patch
import os
import json
from bank import load_db, save_db, deposit, withdraw, read_amount, transfer

@pytest.fixture
def temp_db(tmp_path):
    db_file = tmp_path / "test_db.json"
    initial_data = {
        "users": {
            "testuser": {
                "password": "123",
                "balance": 100.0,
                "transactions": []
            },
            "recipient": {
                "password": "456",
                "balance": 50.0,
                "transactions": []
            }
        }
    }
    with open(db_file, "w") as f:
        json.dump(initial_data, f)
    
    with patch("bank.DB_FILE", str(db_file)):
        yield db_file


def test_read_amount():
    with patch("builtins.input", side_effect=["50"]):
        assert read_amount("Prompt: ") == 50.0

    with patch("builtins.input", side_effect=["abc", "10"]):
        assert read_amount("Prompt: ") is None

def test_deposit(temp_db):
    with patch("builtins.input", return_value="50"):
        deposit("testuser")
    
    db = load_db()
    assert db["users"]["testuser"]["balance"] == 150.0
    assert len(db["users"]["testuser"]["transactions"]) == 1
    assert db["users"]["testuser"]["transactions"][0]["type"] == "deposit"

def test_transfer(temp_db):
    with patch("builtins.input", side_effect =["recipient", "50"]):
        transfer("testuser")

    db = load_db()
    assert db["users"]["testuser"]["balance"] == 50.0
    assert db["users"]["recipient"]["balance"] == 100.0

    assert len(db["users"]["testuser"]["transactions"]) ==1
    assert db["users"]["testuser"]["transactions"][0]["type"] == "transfer_out"


def test_withdraw_success(temp_db):
    with patch("builtins.input", return_value="40"):
        withdraw("testuser")
    
    db = load_db()
    assert db["users"]["testuser"]["balance"] == 60.0

def test_withdraw_insufficient(temp_db):
    with patch("builtins.input", return_value="200"):
        withdraw("testuser")
    
    db = load_db()
    assert db["users"]["testuser"]["balance"] == 100.0