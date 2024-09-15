"""Test"""
from app.iso_check import ContainerValidator


ctn = ContainerValidator()


def test_length_of_container_number():
    """Test if the length of the container number is 11"""
    container_number = "MSFU8626370"  # A valid 11-character container number
    is_valid = ctn.validate_container_number(container_number)
    
    assert len(container_number) == 11
    assert is_valid is True
