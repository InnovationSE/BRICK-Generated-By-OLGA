from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Damper_Min_Position_Setpoint import Economizer_Damper_Min_Position_Setpoint


class AHU_Economizer_Damper_Min_Position_Setpoint(Economizer_Damper_Min_Position_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Economizer_Damper_Min_Position_Setpoint
	
	
