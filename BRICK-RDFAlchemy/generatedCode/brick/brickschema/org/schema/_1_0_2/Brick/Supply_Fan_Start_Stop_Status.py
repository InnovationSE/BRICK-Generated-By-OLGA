from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Start_Stop_Status import Fan_Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_Status import Supply_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_Status import Discharge_Fan_Status


class Supply_Fan_Start_Stop_Status(Fan_Start_Stop_Status,Supply_Fan_Status,Discharge_Fan_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Fan_Start_Stop_Status
	
	
