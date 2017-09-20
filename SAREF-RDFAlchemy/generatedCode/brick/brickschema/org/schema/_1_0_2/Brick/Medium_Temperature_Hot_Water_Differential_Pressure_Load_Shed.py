from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Differential_Pressure import Medium_Temperature_Hot_Water_Differential_Pressure
from brick.brickschema.org.schema._1_0_2.Brick.Load_Shed import Load_Shed


class Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed(Medium_Temperature_Hot_Water_Differential_Pressure,Load_Shed):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed
	
	
