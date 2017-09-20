from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Auto_Cooling_Temperature_Setpoint import Auto_Cooling_Temperature_Setpoint


class AHU_Auto_Cooling_Temperature_Setpoint(Auto_Cooling_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Auto_Cooling_Temperature_Setpoint
	
	
