from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Warm_Cool_Adjust_Sensor import Warm_Cool_Adjust_Sensor


class VAV_Warm_Cool_Adjust_Sensor(Warm_Cool_Adjust_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Warm_Cool_Adjust_Sensor
	
	
