from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan import Discharge_Fan
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_Differential_Speed import Return_Fan_Differential_Speed


class Return_Discharge_Fan_Differential_Speed(Discharge_Fan,Return_Fan_Differential_Speed):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Discharge_Fan_Differential_Speed
	
	
