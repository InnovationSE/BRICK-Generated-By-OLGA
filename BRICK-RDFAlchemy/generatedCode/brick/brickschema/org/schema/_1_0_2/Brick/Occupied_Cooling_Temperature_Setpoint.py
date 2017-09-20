from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Temperature import Cooling_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Temperature_Setpoint import Cooling_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Occupied import Occupied


class Occupied_Cooling_Temperature_Setpoint(Cooling_Temperature,Cooling_Temperature_Setpoint,Occupied):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Occupied_Cooling_Temperature_Setpoint
	
	
