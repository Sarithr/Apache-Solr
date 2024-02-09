import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/solr_sample')
solr.add([{"id": "04", "name": "gayathri"}])

print("Data added")

searchResults = solr.search("03")
print(searchResults)

solr.delete(id="doc_1")
print("Data deleted")