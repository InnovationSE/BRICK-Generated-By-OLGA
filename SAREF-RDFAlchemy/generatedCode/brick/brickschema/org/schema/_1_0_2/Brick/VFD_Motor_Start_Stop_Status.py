from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Motor_Start_Stop_Status import Motor_Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Start_Stop_Status import VFD_Start_Stop_Status


class VFD_Motor_Start_Stop_Status(Motor_Start_Stop_Status,VFD_Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Motor_Start_Stop_Status
	
	
