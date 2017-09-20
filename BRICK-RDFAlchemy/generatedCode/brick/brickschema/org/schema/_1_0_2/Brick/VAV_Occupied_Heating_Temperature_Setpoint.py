from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Heating_Temperature_Setpoint import Occupied_Heating_Temperature_Setpoint


class VAV_Occupied_Heating_Temperature_Setpoint(Occupied_Heating_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Occupied_Heating_Temperature_Setpoint
	
	
