from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Standby_Unit_On_Off import Standby_Unit_On_Off


class Standby_Glycool_Unit_On_Off(Standby_Unit_On_Off):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Standby_Glycool_Unit_On_Off
	
	
