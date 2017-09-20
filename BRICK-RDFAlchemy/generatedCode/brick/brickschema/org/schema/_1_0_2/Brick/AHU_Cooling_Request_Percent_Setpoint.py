from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Demand_Setpoint import Demand_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Cooling_Request_Setpoint import AHU_Cooling_Request_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Request_Percent_Setpoint import Cooling_Request_Percent_Setpoint


class AHU_Cooling_Request_Percent_Setpoint(Demand_Setpoint,AHU_Cooling_Request_Setpoint,Cooling_Request_Percent_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Cooling_Request_Percent_Setpoint
	
	
