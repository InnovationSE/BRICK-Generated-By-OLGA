from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Static_Pressure_Cutout_Limit_Setpoint import High_Static_Pressure_Cutout_Limit_Setpoint


class VAV_High_Static_Pressure_Cutout_Limit_Setpoint(High_Static_Pressure_Cutout_Limit_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_High_Static_Pressure_Cutout_Limit_Setpoint
	
	
