from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.FCU_VFD_Speed_Command import FCU_VFD_Speed_Command
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_VFD_Speed_Command import Supply_Fan_VFD_Speed_Command
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_VFD_Speed_Command import Discharge_Fan_VFD_Speed_Command


class FCU_Supply_Fan_VFD_Speed_Command(FCU_VFD_Speed_Command,Supply_Fan_VFD_Speed_Command,Discharge_Fan_VFD_Speed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Supply_Fan_VFD_Speed_Command
	
	
