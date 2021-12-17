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





class Redactor:

	# static methods work independent of class object
	@staticmethod
	def get_sensitive_data(lines):
	
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?"
		for line in lines:
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
		
		for page in doc:
			##page._wrapContents()
			sensitive = self.get_sensitive_data(page.getText("text")
												.split('\n'))
			for data in sensitive:
				areas = page.searchFor(data)
				
				# drawing outline over sensitive datas
				[page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
		print("Successfully redacted phone number")

# driver code for testing
if __name__ == "__main__":

	# replace it with name of the pdf file
	#path = 'C:/Users/kumarba/Desktop/CV Clean/Suhas.pdf'
	redactor = Redactor(path)
	redactor.redaction()




def remove_img_on_pdf(idoc, page):
    #img_list = idoc.getPageImageList(page)
    img_list = idoc.get_page_images(page)
    con_list = idoc[page].get_contents()

    for i in con_list:
        c = idoc.xref_stream(i)
        if c != None:
            for v in img_list:
                arr = bytes(v[7], 'utf-8')
                r = c.find(arr)
                if r != -1:
                    cnew = c.replace(arr, b"")
                    idoc.update_stream(i, cnew)
                    c = idoc.xref_stream(i)
    return idoc


doc = fitz.open(path)
rdoc = remove_img_on_pdf(doc, 0)
rdoc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
# Succesfully removed image


# In[10]:


class Redactor:
	@staticmethod
	def get_sensitive_data(lines):
	
		""" Function to get all the lines """
		
		# email regex
        #\bMale\b|\bGirl\b|\bBoy\b|\bMen\b|\bWomen\b|\bFemale\b
		EMAIL_REG = r"(M(ale)|F(emale)|Mr|M(en)|W(omen))"
		for line in lines:
		
			# matching the regex to each line
			if re.search(EMAIL_REG, line, re.IGNORECASE):
				search = re.search(EMAIL_REG, line, re.IGNORECASE)
				
				# yields creates a generator
				# generator is used to return
				# values in between function iterations
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
		
			##page._wrapContents()
			

			sensitive = self.get_sensitive_data(page.getText("text")
												.split('\n'))
			for data in sensitive:
				areas = page.searchFor(data)
				
				# drawing outline over sensitive datas
				[page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
		print("Successfully redacted Gender related details")

# driver code for testing
if __name__ == "__main__":

	# replace it with name of the pdf file
	#path = 'C:/Users/kumarba/Desktop/CV Clean/Suhas.pdf'
	redactor = Redactor(path)
	redactor.redaction()


# In[ ]:


class Redactor:
	@staticmethod
	def get_sensitive_data(lines):
	
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"(INDIA|USA|Uk)"
		for line in lines:
		
			# matching the regex to each line
			if re.search(EMAIL_REG, line, re.IGNORECASE):
				search = re.search(EMAIL_REG, line, re.IGNORECASE)
				
				# yields creates a generator
				# generator is used to return
				# values in between function iterations
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
		
			##page._wrapContents()
			

			sensitive = self.get_sensitive_data(page.getText("text")
												.split('\n'))
			for data in sensitive:
				areas = page.searchFor(data)
				
				# drawing outline over sensitive datas
				[page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
		print("Successfully redacted location(Country)")

# driver code for testing
if __name__ == "__main__":

	# replace it with name of the pdf file
	#path = 'C:/Users/kumarba/Desktop/CV Clean/Suhas.pdf'
	redactor = Redactor(path)
	redactor.redaction()


# In[ ]:


class Redactor:
	@staticmethod
	def get_name(lines):
		for line in lines:
			nlp_text = nlp(line)
			pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
			matcher.add('NAME', [pattern])
			matches = matcher(nlp_text)
			for match_id, start, end in matches:
				span = nlp_text[start:end]
				return span.text
    
	@staticmethod
	def get_sensitive_data(lines):
		replaceThis = Redactor.get_name(lines)
		EMAIL_REG = "(" + replaceThis + ")"  
		
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
		
			##page._wrapContents()
			sensitive = self.get_sensitive_data(page.getText("text")
												.split('\n'))
			for data in sensitive:
				areas = page.searchFor(data)
				
				# drawing outline over sensitive datas
				[page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save(output_location,incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
		print("Successfully redacted Name")

# driver code for testing
if __name__ == "__main__":
	# replace it with name of the pdf file
	nlp = spacy.load('en_core_web_sm')
	matcher = Matcher(nlp.vocab)
	#path = 'C:/Users/kumarba/Desktop/CV Clean/Suhas.pdf'
	redactor = Redactor(path)
	redactor.redaction()
