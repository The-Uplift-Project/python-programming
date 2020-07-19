# converting Hex to Base64: the preferred way
# base 64 index table
b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# In process of completion
def convert(input_hex):

	# encoded string object to be returned
	encoded = ""

	# converting hex to binary
	binary = [bin(byte) for byte in input_hex]

	# removing the preceeding '0b' from binary strings
	binary = [b[2:] for b in binary]

	# since preceeding zeros are removed, ensure that 
	# the length is strictly 8 bits
	binary = [b.zfill(8) for b in binary]

convert(bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
