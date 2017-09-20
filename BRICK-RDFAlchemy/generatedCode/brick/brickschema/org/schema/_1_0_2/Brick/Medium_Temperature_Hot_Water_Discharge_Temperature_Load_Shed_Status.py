from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water import Medium_Temperature_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Differential_Pressure_Load_Shed_Status import Differential_Pressure_Load_Shed_Status


class Medium_Temperature_Hot_Water_Discharge_Temperature_Load_Shed_Status(Medium_Temperature_Hot_Water,Differential_Pressure_Load_Shed_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Discharge_Temperature_Load_Shed_Status
	
	
