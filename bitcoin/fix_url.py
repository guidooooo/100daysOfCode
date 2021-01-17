#http://mainnet.programmingbitcoin.com is a 404
#http://testnet.programmingbitcoin.com is a 503

#As a result a bunch of code examples can't be followed.

#For the time being I'm using Blockstream's block explorer API like so:

def get_url(cls, testnet=False):
        if testnet:
            return 'https://blockstream.info/testnet/api/'
        else:
            return 'https://blockstream.info/api/'
#And a slightly modified fetch method (notice the / before hex as opposed to .hex as it was initially:

@classmethod
def fetch(cls, tx_id, testnet=False, fresh=False):
	if fresh or (tx_id not in cls.cache):
		url = '{}/tx/{}/hex'.format(cls.get_url(testnet), tx_id)