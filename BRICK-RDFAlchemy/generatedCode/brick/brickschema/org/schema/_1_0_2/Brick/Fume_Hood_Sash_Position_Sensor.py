from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper_Position_Sensor import Damper_Position_Sensor


class Fume_Hood_Sash_Position_Sensor(Damper_Position_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fume_Hood_Sash_Position_Sensor
	
	