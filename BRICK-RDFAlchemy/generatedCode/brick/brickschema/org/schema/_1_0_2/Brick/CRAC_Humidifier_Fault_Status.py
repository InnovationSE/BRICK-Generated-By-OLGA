from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidifier_Fault_Status import Humidifier_Fault_Status


class CRAC_Humidifier_Fault_Status(Humidifier_Fault_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Humidifier_Fault_Status
	
	
