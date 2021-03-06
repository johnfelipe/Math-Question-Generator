#Worksheet headers for Automatic Question Generation

class Header_File:
	def __init__(self,filename, title,author,date,timestamp):
		self.Title = title
		self.Date = date
		self.Author = author
		self.FileName = filename
		self.TimeStamp = timestamp
		self.Text = "\def\XCfileversion{v0.1}%\n"
		self.Text +="\def\XCfiledate{"+self.Date+"}%\n"
		self.Text +="\documentclass[letter]{article}\n"
		self.Text +="\usepackage{array,multicol,multido,textcomp,amsmath,graphicx,hyperref,subfigure,underscore,parskip}\n"
		self.Text +="\usepackage{xcolor}[2005/03/24]\n"
		self.Text +="\usepackage[normalem]{ulem}\n"
		self.Text +="\usepackage[hmargin={1.25cm,.75cm},vmargin=1.25cm,footskip=.5cm,nohead]{geometry}\n"
		self.Text +="\\begin{document}\n"
		self.Text +="\\title{"+self.Title+"}\n"
		self.Text +="\\author{"+self.Author+"\\thanks{This file was generated by an \\textsf{Open Source} mathematics worksheet program which can be downloaded at \\texttt{www.metaciv.org}. Please send error reports and suggestions for improvements to \\texttt{wneal@lia-edu.ca}.}}\n"
		self.Text +="\date{\XCfileversion{} (\XCfiledate)}\n"
		self.Text +="\maketitle\n"
		self.Text +="\\setlength{\\parskip}{12mm plus 4mm minus 4mm}"
		self.Text += "\\setlength{\\parindent}{0cm}"
		
	def Write_Header(self):
		f = open(self.FileName,"w")
		f.write(self.Text)
		f.close()
