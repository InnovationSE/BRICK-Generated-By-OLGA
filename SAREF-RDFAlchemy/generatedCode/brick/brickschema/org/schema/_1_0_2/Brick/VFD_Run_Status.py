from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Status import VFD_Status
from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Status import Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.Run_Status import Run_Status


class VFD_Run_Status(VFD_Status,Start_Stop_Status,Run_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Run_Status
	
	
