from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Differential_Pressure import Chilled_Water_Differential_Pressure


class Chilled_Water_Differential_Pressure_Proportional_Band(Chilled_Water_Differential_Pressure):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Differential_Pressure_Proportional_Band
	
	
