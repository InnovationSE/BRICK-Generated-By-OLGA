from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Run_Direction_Status import Run_Direction_Status
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Run_Status import VFD_Run_Status


class VFD_Run_Direction_Status(Run_Direction_Status,VFD_Run_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Run_Direction_Status
	
	
