import pytest

from eth2._utils.bls import bls


@pytest.fixture
def sample_bls_private_key():
    return 42


@pytest.fixture
def sample_bls_public_key(sample_bls_private_key):
    return bls.privtopub(sample_bls_private_key)


@pytest.fixture
def sample_bls_key_pair(sample_bls_private_key, sample_bls_public_key):
    return (sample_bls_public_key, sample_bls_private_key)
