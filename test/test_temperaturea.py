def test_invalid_temperature():
    with pytest.raises(ValueError):
        is_overheating(-5)
