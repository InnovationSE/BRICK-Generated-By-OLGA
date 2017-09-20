from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Max_Chilled_Water_Differential_Pressure_Setpoint import Max_Chilled_Water_Differential_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.CWS_Chilled_Water_Differential_Pressure_Setpoint import CWS_Chilled_Water_Differential_Pressure_Setpoint


class CWS_Max_Chilled_Water_Differential_Pressure_Setpoint(Max_Chilled_Water_Differential_Pressure_Setpoint,CWS_Chilled_Water_Differential_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CWS_Max_Chilled_Water_Differential_Pressure_Setpoint
	
	
