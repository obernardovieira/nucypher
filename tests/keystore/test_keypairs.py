import pytest
import sha3
from nkms.keystore import keypairs
from umbral.keys import UmbralPrivateKey, UmbralPublicKey


def test_gen_keypair_if_needed():
    new_enc_keypair = keypairs.EncryptingKeypair()
    assert new_enc_keypair.privkey != None
    assert new_enc_keypair.pubkey != None

    new_sig_keypair = keypairs.SigningKeypair()
    assert new_sig_keypair.privkey != None
    assert new_sig_keypair.pubkey != None


def test_keypair_with_umbral_keys():
    umbral_privkey = UmbralPrivateKey.gen_key()
    umbral_pubkey = umbral_privkey.gen_pubkey()

    new_keypair_from_priv = Keypair(umbral_privkey)
    assert new_keypair_from_priv.privkey == umbral_privkey
    assert new_keypair_from_priv.pubkey == umbral_pubkey

    new_keypair_from_pub = Keypair(umbral_pubkey)
    assert new_keypair_from_pub.pubkey == umbral_pubkey
    with pytest.raises(AttributeError):
        new_keypair_from_pub.privkey


def test_keypair_serialization():
    umbral_pubkey = UmbralPrivateKey.gen_key().get_pubkey()
    new_keypair = Keypair(umbral_pubkey)

    pubkey_bytes = new_keypair.serialize_pubkey()
    assert pubkey_bytes == bytes(umbral_pubkey)

    pubkey_b64 = new_keypair.serialize_pubkey(as_b64=False)
    assert pubkey_b64 == umbral_pubkey.to_bytes()


def test_keypair_fingerprint():
    umbral_pubkey = UmbralPrivateKey.gen_key().get_pubkey()
    new_keypair = Keypair(umbral_pubkey)

    fingerprint = new_keypair.get_fingerprint()
    assert fingerprint != None

    umbral_fingerprint = sha3.keccak_256(bytes(umbral_pubkey)).hexdigest().encode()
    assert fingerprint == umbral_fingerprint


def test_signing():
    umbral_privkey = UmbralPrivateKey.gen_key()
    sig_keypair = Keypair(umbral_privkey)

    msg = b'attack at dawn'
    signature = sig_keypair.sign(msg)

def test_ecdsa_keypair_signing(self):
    msghash = API.keccak_digest(b'hello world!')

    sig = self.ecdsa_keypair.sign(msghash)
    self.assertEqual(bytes, type(sig))
    self.assertEqual(65, len(sig))

def test_ecdsa_keypair_verification(self):
    msghash = API.keccak_digest(b'hello world!')

    sig = self.ecdsa_keypair.sign(msghash)
    self.assertEqual(bytes, type(sig))
    self.assertEqual(65, len(sig))

    is_valid = self.ecdsa_keypair.verify(msghash, sig)
    self.assertTrue(is_valid)
