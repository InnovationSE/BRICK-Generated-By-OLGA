from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Booster_Fan_Air_Flow_Setpoint import Booster_Fan_Air_Flow_Setpoint


class VAV_Booster_Fan_Air_Flow_Setpoint(Booster_Fan_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Booster_Fan_Air_Flow_Setpoint
	
	
