from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Request_Setpoint import Heating_Request_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Demand_Setpoint import Demand_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Heating_Demand_Setpoint import Heating_Demand_Setpoint


class VAV_Heating_Request_Setpoint(Heating_Request_Setpoint,Demand_Setpoint,Heating_Demand_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Heating_Request_Setpoint
	
	
