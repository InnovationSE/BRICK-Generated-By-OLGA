from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Valve_Status import Valve_Status


class Heat_Exchanger_Valve_Status(Valve_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heat_Exchanger_Valve_Status
	
	
