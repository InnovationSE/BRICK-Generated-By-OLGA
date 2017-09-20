from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Discharge_Air_Flow_Setpoint import Cooling_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Flow_Setpoint import Supply_Air_Flow_Setpoint


class Unoccupied_Cooling_Discharge_Air_Flow_Setpoint(Cooling_Discharge_Air_Flow_Setpoint,Supply_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Unoccupied_Cooling_Discharge_Air_Flow_Setpoint
	
	
