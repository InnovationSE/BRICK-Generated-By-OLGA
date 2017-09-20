from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Temperature import Heating_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Occupied import Occupied
from brick.brickschema.org.schema._1_0_2.Brick.Heating_Temperature_Setpoint import Heating_Temperature_Setpoint


class Occupied_Heating_Temperature_Setpoint(Heating_Temperature,Occupied,Heating_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Occupied_Heating_Temperature_Setpoint
	
	
