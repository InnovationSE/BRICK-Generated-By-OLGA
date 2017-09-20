from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On_Off_Status import On_Off_Status


class Humidification_On_Off_Status(On_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Humidification_On_Off_Status
	
	
