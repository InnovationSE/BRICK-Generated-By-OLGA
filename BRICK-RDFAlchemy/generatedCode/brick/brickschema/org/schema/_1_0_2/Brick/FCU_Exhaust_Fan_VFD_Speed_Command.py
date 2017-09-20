from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_VFD_Speed_Command import Exhaust_Fan_VFD_Speed_Command
from brick.brickschema.org.schema._1_0_2.Brick.FCU_VFD_Speed_Command import FCU_VFD_Speed_Command


class FCU_Exhaust_Fan_VFD_Speed_Command(Exhaust_Fan_VFD_Speed_Command,FCU_VFD_Speed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Exhaust_Fan_VFD_Speed_Command
	
	
