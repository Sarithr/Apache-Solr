import pysolr
import logging
import json

logging.basicConfig(level = logging.DEBUG)

class SolrConnector:
	def __init__(self, adminUrl):
		self.adminUrl = adminUrl
		self.solr = pysolr.Solr(self.adminUrl)

	def addData(self, data):
		isDataInserted = False
		responseMessage = ''
		try:
			if (len(data) != 0):
				self.solr.add(data)
				logging.debug("Data added")
				isDataInserted = True
				responseMessage = "Data Inserted Successfully"
			else:
			 	responseMessage = "Provide valid values to insert"			
		except:
			logging.exception("Unable to insert the Data")
		return isDataInserted, responseMessage	

	def selectData(self, query):
		isDataInserted = False
		responseMessage = ''
		try:
			if (len(query) != 0):
				searchResult = self.solr.search(query)
				logging.debug(searchResult)
				logging.debug("Data searched")
				isDataInserted = True
				responseMessage = "Data Filtered Successfully"
			else: 
				responseMessage = "Provide valid values to filter"
		except:
			logging.exception("Unable to filter the Data")
		return isDataInserted, responseMessage
				
	#def updateData(self, updation):
		#self.solr(updation)
		#logging.debug("Data updated")	

	def deleteData(self, deletion):
		isDataInserted = False
		responseMessage = ''
		try:
			if (deletion != ""):
				self.solr.delete(deletion)
				logging.debug("Data deleted")	
				isDataInserted = True
				responseMessage = "Data Deleted Successfully"
			else:
				responseMessage = "Provide valid values to delete"	
		except:
			logging.exception("Unable to delete the Data")
		return isDataInserted, responseMessage	


