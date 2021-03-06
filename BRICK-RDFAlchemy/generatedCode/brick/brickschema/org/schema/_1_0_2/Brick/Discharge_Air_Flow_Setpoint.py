from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air
from brick.brickschema.org.schema._1_0_2.Brick.Air_Flow_Setpoint import Air_Flow_Setpoint


class Discharge_Air_Flow_Setpoint(Supply_Air,Discharge_Air,Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Discharge_Air_Flow_Setpoint
	
	
