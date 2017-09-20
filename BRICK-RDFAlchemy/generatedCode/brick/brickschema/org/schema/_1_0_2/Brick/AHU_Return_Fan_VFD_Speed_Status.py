from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Return_Fan_Status import AHU_Return_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.AHU_VFD_Status import AHU_VFD_Status
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_VFD_Speed_Status import Return_Fan_VFD_Speed_Status


class AHU_Return_Fan_VFD_Speed_Status(AHU_Return_Fan_Status,AHU_VFD_Status,Return_Fan_VFD_Speed_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Fan_VFD_Speed_Status
	
	
