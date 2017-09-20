from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Start_Stop_Command import VFD_Start_Stop_Command
from brick.brickschema.org.schema._1_0_2.Brick.Motor_Start_Stop_Command import Motor_Start_Stop_Command


class VFD_Motor_Start_Stop_Command(VFD_Start_Stop_Command,Motor_Start_Stop_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Motor_Start_Stop_Command
	
	
