import os


def calculate_points(amount: float) -> int:
    return int(amount * 0.1)


def save_user_token(token: str):
    # Secure: Fetch secret from environment variables instead of hardcoding
    secret_key = os.getenv("SECRET_KEY")
    print(f"Token saved with key present: {secret_key is not None}")
