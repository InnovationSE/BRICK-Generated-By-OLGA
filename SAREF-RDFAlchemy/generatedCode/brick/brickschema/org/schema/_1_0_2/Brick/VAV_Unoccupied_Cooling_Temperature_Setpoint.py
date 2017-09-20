from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Unoccupied_Cooling_Temperature_Setpoint import Unoccupied_Cooling_Temperature_Setpoint


class VAV_Unoccupied_Cooling_Temperature_Setpoint(Unoccupied_Cooling_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Unoccupied_Cooling_Temperature_Setpoint
	
	
