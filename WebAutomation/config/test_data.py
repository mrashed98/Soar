import uuid

class TestData:
    # Base URLs
    BASE_URL = "https://juice-shop.herokuapp.com/#"
    LOGIN_URL = f"{BASE_URL}/login"
    REGISTERATION_URL = f"{BASE_URL}/register"
    HOME_URL = f"{BASE_URL}/"
    BASKET_URL = f"{BASE_URL}/basket"
    
    # Test Users
    EMAIL = f"{uuid.uuid4()}@example.com"
    PASSWORD = str(uuid.uuid4())
    SECURITY_ANSWER = str(uuid.uuid4())
    
    # Dummy Address
    ADDRESS = {
        "country": "United States",
        "name": "John Doe",
        "mobile": "1234567890",
        "address": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }

    # Dummy Card
    CARD = {
        "cardNumber": "4242424242424242",
        "cardExpiryMonth": "12",
        "cardExpiryYear": "2025",
        "cardCvc": "123"
    }
