from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Motor_Power_Meter import Motor_Power_Meter
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Power_Meter import VFD_Power_Meter


class VFD_Motor_Power_Meter(Motor_Power_Meter,VFD_Power_Meter):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Motor_Power_Meter
	
	
