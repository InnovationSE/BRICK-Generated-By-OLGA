from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Temperature_Setpoint import Economizer_Temperature_Setpoint


class Economizer_Disable_Differential_Temperature_Setpoint(Economizer_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Disable_Differential_Temperature_Setpoint
	
	
