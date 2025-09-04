import secrets


def generate_crypto_seed():
    """
    Генерирует криптографически безопасный сид на 32 байта
    используя модуль secrets (рекомендуется для безопасности)
    """
    return secrets.token_bytes(32)
    
