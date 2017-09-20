from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Temperature import Cooling_Temperature


class Unoccupied_Cooling_Temperature(Cooling_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Unoccupied_Cooling_Temperature
	
	
