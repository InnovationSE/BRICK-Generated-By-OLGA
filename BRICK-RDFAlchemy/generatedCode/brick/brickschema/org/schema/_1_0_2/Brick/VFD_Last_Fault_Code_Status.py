from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Fault_Status import VFD_Fault_Status
from brick.brickschema.org.schema._1_0_2.Brick.Last_Fault_Code_Status import Last_Fault_Code_Status


class VFD_Last_Fault_Code_Status(VFD_Fault_Status,Last_Fault_Code_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Last_Fault_Code_Status
	
	
