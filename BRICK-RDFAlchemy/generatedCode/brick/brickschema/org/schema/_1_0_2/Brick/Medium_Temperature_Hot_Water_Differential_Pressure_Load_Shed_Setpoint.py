from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Differential_Pressure_Setpoint import Hot_Water_Differential_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Load_Shed_Differential_Pressure_Setpoint import Load_Shed_Differential_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water import Medium_Temperature_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint import Temperature_Setpoint


class Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint(Hot_Water_Differential_Pressure_Setpoint,Load_Shed_Differential_Pressure_Setpoint,Medium_Temperature_Hot_Water,Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint
	
	
