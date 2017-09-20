from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Alarm import VFD_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Maintenance_Required_Alarm import Maintenance_Required_Alarm


class VFD_Maintenance_Required_Alarm(VFD_Alarm,Maintenance_Required_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Maintenance_Required_Alarm
	
	
