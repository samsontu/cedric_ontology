import sys
from owlready2 import *
onto = get_ontology("file:///Users/tu/Documents/Dropbox/CurrentProjects/CEDRIC/cedric_ontology/src/ontology/OMOP.owl").load()
omop = get_namespace("http://www.semanticweb.org/CEDRIC/OMOP/")
with onto:
	class hasPatient(ObjectProperty):
		range = [omop.PERSON]
		
onto.save(file = "/Users/tu/Documents/Dropbox/CurrentProjects/CEDRIC/cedric_ontology/src/ontology/OMOP.owl", format="rdfxml")