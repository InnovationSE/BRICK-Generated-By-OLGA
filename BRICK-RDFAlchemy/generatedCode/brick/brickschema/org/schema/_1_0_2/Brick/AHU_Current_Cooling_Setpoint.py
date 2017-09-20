from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Current_Cooling_Setpoint import Current_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Temperature_Setpoint import Cooling_Temperature_Setpoint


class AHU_Current_Cooling_Setpoint(Current_Cooling_Setpoint,Cooling_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Current_Cooling_Setpoint
	
	
