from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Max_Return_Air_CO2_Setpoint import Max_Return_Air_CO2_Setpoint


class AHU_Max_Return_Air_CO2_Setpoint(Max_Return_Air_CO2_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Max_Return_Air_CO2_Setpoint
	
	
