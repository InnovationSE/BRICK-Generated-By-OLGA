from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Setpoint import Discharge_Air_Flow_Setpoint


class Cooling_Discharge_Air_Flow_Setpoint(Discharge_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Discharge_Air_Flow_Setpoint
	
	
