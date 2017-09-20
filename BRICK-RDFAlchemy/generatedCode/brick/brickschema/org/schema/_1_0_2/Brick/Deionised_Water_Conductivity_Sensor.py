from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Deionised_Water import Deionised_Water
from brick.brickschema.org.schema._1_0_2.Brick.Conductivity_Sensor import Conductivity_Sensor


class Deionised_Water_Conductivity_Sensor(Deionised_Water,Conductivity_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Deionised_Water_Conductivity_Sensor
	
	
