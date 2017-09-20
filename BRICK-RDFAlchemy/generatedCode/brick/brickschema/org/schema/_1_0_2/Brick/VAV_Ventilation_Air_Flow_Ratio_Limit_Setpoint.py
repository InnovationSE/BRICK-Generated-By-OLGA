from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Ventilation_Air_Flow_Ratio_Limit_Setpoint import Ventilation_Air_Flow_Ratio_Limit_Setpoint


class VAV_Ventilation_Air_Flow_Ratio_Limit_Setpoint(Ventilation_Air_Flow_Ratio_Limit_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Ventilation_Air_Flow_Ratio_Limit_Setpoint
	
	
