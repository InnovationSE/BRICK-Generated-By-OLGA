from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidity_Setpoint import Humidity_Setpoint


class CRAC_Humidity_Setpoint(Humidity_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Humidity_Setpoint
	
	
