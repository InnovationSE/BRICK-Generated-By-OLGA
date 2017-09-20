from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fault_Indicator_Status import Fault_Indicator_Status
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Fault_Status import VFD_Fault_Status


class VFD_Fault_Indicator_Status(Fault_Indicator_Status,VFD_Fault_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Fault_Indicator_Status
	
	
