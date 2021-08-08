from progressbar import ProgressBar
name = input('имя пользователя: ')
f = open(name + '/' + name + '.txt', encoding='utf-8')
lines = f.readlines()
pbar = ProgressBar(maxval=len(lines))
pbar.start()
for i in range(0,len(lines)):
	pbar.update(i)
	if lines[i].lower()[-5:-1] == '.jpg':
		f_2 = open(name + '/' + name + '_jpg.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.png':
		f_2 = open(name + '/' + name + '_png.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.doc':
		f_2 = open(name + '/' + name + '_doc.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-6:-1] == '.docx':
		f_2 = open(name + '/' + name + '_docx.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.xls':
		f_2 = open(name + '/' + name + '_xls.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.xlsx':
		f_2 = open(name + '/' + name + '_xlsx.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.ppt':
		f_2 = open(name + '/' + name + '_ppt.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-6:-1] == '.pptx':
		f_2 = open(name + '/' + name + '_pptx.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.pdf':
		f_2 = open(name + '/' + name + '_pdf.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.zip':
		f_2 = open(name + '/' + name + '_zip.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.rar':
		f_2 = open(name + '/' + name + '_rar.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-4:-1] == '.7z':
		f_2 = open(name + '/' + name + '_7z.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
	elif lines[i].lower()[-5:-1] == '.txt':
		f_2 = open(name + '/' + name + '_txt.txt', 'a' , encoding='utf-8')
		f_2.write(lines[i] + '\n')
		f_2.close()
pbar.finish()