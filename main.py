from jwt import algorithms
from django.utils import formats
from rsa import cli
from feedparser import feedparser
from requests import sessions
from lib.Crypto.PublicKey import ElGamal
if __name__ == '__main__':
    formats.get_format()
    algorithms.HMACAlgorithm.prepare_key()
    cli.VerifyOperation.perform_operation()
    feedparser.parse()
    sessions.SessionRedirectMixin.resolve_redirects()
    ElGamal.generate()
