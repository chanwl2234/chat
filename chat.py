
def read_file(flies):
	
	with open(flies, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chats.append(line.strip())
		return chats


def convert(lines):
	new = []
	name = None
	for line in chats:
		if line =='Allen':
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue

		new.append(name + ':' + line)
	return new

def write_file(flies, chats):
	with open(flies, 'w', encoding = 'utf-8-sig') as f:
		for line in chats:
			f.write(line + '\n')

def main():
	chats = read_file('input.txt')
	chats = convert(chats)
	write_file('output.txt', chats)

chats =[]
main()
