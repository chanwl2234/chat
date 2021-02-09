
def read_file(flies):
	
	with open(flies, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chats.append(line.strip())
		return chats


def convert(lines):
	name = None
	allen_wc = 0
	allen_sc = 0
	allen_img = 0
	viki_wc = 0
	viki_sc = 0
	viki_img = 0

	for line in chats:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sc += 1
			elif s[2] == '圖片':
				allen_img += 1
			else:
				for m in s[2:]:
					allen_wc += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sc += 1
			elif s[2] == '圖片':
				viki_img += 1
			else:
				for m in s[2:]:
					viki_wc += len(m)
	print(allen_wc, allen_sc, allen_img)
	print(viki_wc, viki_sc, viki_img)
	

def write_file(flies, chats):
	with open(flies, 'w', encoding = 'utf-8-sig') as f:
		for line in chats:
			f.write(line + '\n')

def main():
	chats = read_file('LINE-Viki.txt')
	chats = convert(chats)
	#write_file('output.txt', chats)

chats =[]
main()
