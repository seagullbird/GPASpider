# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import re

class Gpa:
	def __init__(self):
		self.session = requests.Session()
		self.url = 'http://jwxt.bupt.edu.cn'
		self.headers = { 
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
			}
		self.labels = ['Course No.', 'Course Seq.', 'Course Name', 'English Course Name', 'Credit', 'Course Attr.', 'Grade']

	def getIndexHtml(self):
		try:
			self.index = self.session.get(self.url)
			return self.index
		except Exception as e:
			print('getIndexHtml Error:', e)

	def getVerifyCodePic(self):
		vCodeJpg = open('vCode.png', 'wb')
		vCodeJpg.write(self.session.get(self.url + BeautifulSoup(self.index.text, 'html.parser').img['src']).content)
		vCodeJpg.close()

	def getVerifyCode(self, vCode):
		self.vCode = vCode

	def login(self, username, password):
		data = {
			'type' : 'sso',
			'zjh' : username,
			'mm' : password,
			'v_yzm': self.vCode
		}
		try:
			self.session.post(self.url + '/jwLoginAction.do', data=data, headers=self.headers)
		except Exception as e:
			print('login Error:', e)

	def getGradePage(self):
		try:
			self.gradePage = self.session.get(self.url + '/gradeLnAllAction.do?type=ln&oper=qbinfo').text
			fw = open('allGrade.html', 'w')
			fw.write(self.gradePage)
			fw.close()
			self.gradePage = ''.join(self.gradePage.split())
			return self.gradePage
		except Exception as e:
			print('getGradePage Error:', e)
			return ''

	def getGradeTable(self):
		pat = r'<trclass="odd"onMouseOut="this.className=\'even\';"onMouseOver="this.className=\'evenfocus\';"><tdalign="center">(.*?)</td><tdalign="center">(.*?)</td><tdalign="center">(.*?)</td><tdalign="center">(.*?)</td><tdalign="center">(.*?)</td><tdalign="center">(.*?)</td><tdalign="center"><palign="center">(.*?)&nbsp;</P></td></tr>'

		self.courseTable = re.findall(pat, self.gradePage)
		return self.courseTable

	def calcGpa(self):
		totalCredits = 0
		totalGrades = 0
		# gradeConverter = lambda x : (90<= x < 100 and 4) or \
		# 							(80 <= x < 90 and 3) or \
		# 							(70 <= x < 79 and 2) or \
		# 							(60 <= x < 69 and 1) or \
		# 							(x < 60 and 0)
		for course in self.courseTable:
			try:
				totalCredits += float(course[self.labels.index('Credit')])
				totalGrades += float(course[self.labels.index('Grade')]) * float(course[self.labels.index('Credit')])
			except Exception as e:
				print('calc error:', e)
		self.gpa = (totalGrades * 4) / (totalCredits * 100)
		return self.gpa 

	def getMyGpa(self):
		self.getIndexHtml()
		self.getVerifyCodePic()
		self.getVerifyCode()
		self.login()
		self.getGradePage()
		self.getGradeTable()
		self.calcGpa()
		return float('%.2f' % self.gpa)



