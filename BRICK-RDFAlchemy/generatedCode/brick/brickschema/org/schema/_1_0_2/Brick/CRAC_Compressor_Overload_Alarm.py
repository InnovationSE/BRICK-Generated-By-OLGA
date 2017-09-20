from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Compressor_Overload_Alarm import Compressor_Overload_Alarm


class CRAC_Compressor_Overload_Alarm(Compressor_Overload_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Compressor_Overload_Alarm
	
	
