from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Setpoint import Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Flow_Setpoint import Supply_Air_Flow_Setpoint


class Heating_Discharge_Air_Flow_Setpoint(Discharge_Air_Flow_Setpoint,Supply_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Discharge_Air_Flow_Setpoint
	
	
