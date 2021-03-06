from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Status import Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Status import VFD_Status
from brick.brickschema.org.schema._1_0_2.Brick.On_Off_Status import On_Off_Status


class VFD_On_Off_Status(Start_Stop_Status,VFD_Status,On_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_On_Off_Status
	
	
