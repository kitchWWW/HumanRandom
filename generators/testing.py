#implemented as I read Andrej Karpathy's post on RNNs.
import pickle
from properNet import RNN
from properNet import path

def getPoem(sampleStart):

	with open('rnn.pkl','rb') as f:  # Python 3: open(..., 'rb')
		data = open(path, 'r').read() # should be simple plain text file
		data = list(data)
		data = ['{0} '.format(elem.lower()) for elem in data]
		chars = sorted(list(set(data)))
		data_size, vocab_size = len(data), len(chars)
		print( 'data has %d characters, %d unique.' % (data_size, vocab_size) )

		#make some dictionaries for encoding and decoding from 1-of-k
		char_to_ix = { ch:i for i,ch in enumerate(chars) }
		ix_to_char = { i:ch for i,ch in enumerate(chars) }

		print char_to_ix
		print ix_to_char

		rnn = pickle.load(f)
		sample_ix = rnn.sample(char_to_ix[sampleStart], 100)
		txt = ''.join([ix_to_char[n] for n in sample_ix])
		return txt

print(getPoem('1 '))