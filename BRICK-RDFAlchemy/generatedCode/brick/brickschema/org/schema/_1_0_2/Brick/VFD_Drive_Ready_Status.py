from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Status import VFD_Status
from brick.brickschema.org.schema._1_0_2.Brick.Drive_Ready_Status import Drive_Ready_Status


class VFD_Drive_Ready_Status(VFD_Status,Drive_Ready_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Drive_Ready_Status
	
	
