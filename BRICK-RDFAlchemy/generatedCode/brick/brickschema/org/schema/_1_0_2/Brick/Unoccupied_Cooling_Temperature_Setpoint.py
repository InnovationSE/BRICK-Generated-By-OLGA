from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Temperature_Setpoint import Cooling_Temperature_Setpoint


class Unoccupied_Cooling_Temperature_Setpoint(Cooling_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Unoccupied_Cooling_Temperature_Setpoint
	
	
