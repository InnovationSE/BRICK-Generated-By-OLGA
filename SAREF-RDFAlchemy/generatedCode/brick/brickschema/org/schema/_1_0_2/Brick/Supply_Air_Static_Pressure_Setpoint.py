from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Setpoint import Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air


class Supply_Air_Static_Pressure_Setpoint(Static_Pressure_Setpoint,Discharge_Air,Supply_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Air_Static_Pressure_Setpoint
	
	
