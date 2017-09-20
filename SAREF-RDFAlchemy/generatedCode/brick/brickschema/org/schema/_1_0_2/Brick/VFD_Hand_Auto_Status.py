from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Status import VFD_Status
from brick.brickschema.org.schema._1_0_2.Brick.Hand_Auto_Status import Hand_Auto_Status
from brick.brickschema.org.schema._1_0_2.Brick.Manual_Auto_Status import Manual_Auto_Status


class VFD_Hand_Auto_Status(VFD_Status,Hand_Auto_Status,Manual_Auto_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Hand_Auto_Status
	
	
