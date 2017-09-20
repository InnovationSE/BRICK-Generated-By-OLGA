from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.FCU_Fan_Status import FCU_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_VFD_Speed_Status import Discharge_Fan_VFD_Speed_Status
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_VFD_Speed_Status import Supply_Fan_VFD_Speed_Status


class FCU_Discharge_Fan_VFD_Speed_Status(FCU_Fan_Status,Discharge_Fan_VFD_Speed_Status,Supply_Fan_VFD_Speed_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Discharge_Fan_VFD_Speed_Status
	
	
