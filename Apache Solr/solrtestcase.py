import unittest, logging
from solrclass import SolrConnector
import socket

class SolrTestCase(unittest.TestCase):
	def setup(self):
		logging.basicConfig(level = logging.DEBUG)
		socket.getaddrinfo('localhost', 8080)

	def testSaveData(self):
		data = [{"id" : "06", "name" : "rakshana"}]
		insertData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = insertData.addData(data)	
		self.assertTrue(isDataInserted)
		self.assertEquals(responseMessage, "Data Inserted Successfully")

	def testSelectData(self):
		query = "aparna"
		filterData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = filterData.selectData(query)	
		self.assertTrue(isDataInserted)
		self.assertEquals(responseMessage, "Data Filtered Successfully")
	
	def testDeleteData(self):
		deletion = id = "doc1"
		deleteData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = deleteData.deleteData(deletion)	
		self.assertTrue(isDataInserted)
		self.assertEquals(responseMessage, "Data Deleted Successfully")
	
	def testSaveDataWithoutData(self):
		data = []
		insertData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = insertData.addData(data)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage, "Provide valid values to insert"	)

	def testSelectDataWithoutQuery(self):
		query = ""
		filterData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = filterData.selectData(query)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage,"Provide valid values to filter")

	def testDeleteDataWithoutDeletion(self):
		deletion = ""
		deleteData = SolrConnector('http://localhost:8983/solr/solr_sample')
		isDataInserted, responseMessage = deleteData.deleteData(deletion)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage, "Provide valid values to delete")
	
