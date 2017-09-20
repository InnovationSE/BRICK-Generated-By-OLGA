from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Thermal_Power_Meter import Thermal_Power_Meter


class Heating_Thermal_Power_Meter(Thermal_Power_Meter):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Thermal_Power_Meter
	
	
