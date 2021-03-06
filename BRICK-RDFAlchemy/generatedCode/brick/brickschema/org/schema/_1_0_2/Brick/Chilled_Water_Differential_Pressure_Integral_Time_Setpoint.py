from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Differential_Pressure_Setpoint import Chilled_Water_Differential_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Integral_Time_Setpoint import Integral_Time_Setpoint


class Chilled_Water_Differential_Pressure_Integral_Time_Setpoint(Chilled_Water_Differential_Pressure_Setpoint,Integral_Time_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Differential_Pressure_Integral_Time_Setpoint
	
	
