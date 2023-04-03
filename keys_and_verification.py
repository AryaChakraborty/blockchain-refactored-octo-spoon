from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sign(message, private_key):
    message = message.encode('utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature


def verify(message, signature, public_key):
    message = message.encode('utf-8')
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        return True
    except InvalidSignature:
        return False
    except:
        print("error executing public key")
        return False


if __name__ == '__main__':
    pr, pu = generate_keys()  # A
    pr1, pu1 = generate_keys()  # B
    message = "Hi I am Arya"
    signature = sign(message, pr)
    if verify(message, signature, pu1):
        print('success')
    else :
        # this block will execute
        print('failed')