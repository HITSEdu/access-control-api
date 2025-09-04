import secrets


async def generate_crypto_seed():
    return secrets.token_bytes(32).hex()
    
