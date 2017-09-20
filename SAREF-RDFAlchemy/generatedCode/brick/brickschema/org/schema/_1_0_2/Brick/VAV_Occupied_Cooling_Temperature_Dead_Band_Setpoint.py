from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VAV_Occupied_Cooling_Temperature_Setpoint import VAV_Occupied_Cooling_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Cooling_Temperature_Dead_Band_Setpoint import Occupied_Cooling_Temperature_Dead_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Zone_Cooling_Temperature_Dead_Band_Setpoint import Zone_Cooling_Temperature_Dead_Band_Setpoint


class VAV_Occupied_Cooling_Temperature_Dead_Band_Setpoint(VAV_Occupied_Cooling_Temperature_Setpoint,Occupied_Cooling_Temperature_Dead_Band_Setpoint,Zone_Cooling_Temperature_Dead_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Occupied_Cooling_Temperature_Dead_Band_Setpoint
	
	
