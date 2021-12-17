# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:16:38 2021

@author: kumarba
"""
import fitz
import re
import spacy
from spacy.matcher import Matcher
import nlp
#pip install PyMuPDF==1.14.20

path = raw_input()
output_location=raw_input()

class Redactor:
	@staticmethod
	def get_sensitive_data(lines):
	
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
		for line in lines:
		
			# matching the regex to each line
			if re.search(EMAIL_REG, line, re.IGNORECASE):
				search = re.search(EMAIL_REG, line, re.IGNORECASE)
				
				yield search.group(1)

	# constructor
	def __init__(self, path):
		self.path = path

	def redaction(self):
	
		""" main redactor code """
		
		# opening the pdf
		doc = fitz.open(self.path)
		
		# iterating through pages
		for page in doc:
			# getting the rect boxes which consists the matching email regex
			sensitive = self.get_sensitive_data(page.getText("text")
												.split('\n'))
			for data in sensitive:
				areas = page.searchFor(data)
				[page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		doc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
		print("Successfully redacted email id")

if __name__ == "__main__":

	# replace it with name of the pdf file
	redactor = Redactor(path)
	redactor.redaction()
