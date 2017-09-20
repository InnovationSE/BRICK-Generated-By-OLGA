from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_Start_Stop_Command import Supply_Fan_Start_Stop_Command
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Fan_Command import AHU_Discharge_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Fan_Command import AHU_Supply_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_Start_Stop_Command import Discharge_Fan_Start_Stop_Command


class AHU_Supply_Fan_Start_Stop_Command(Supply_Fan_Start_Stop_Command,AHU_Discharge_Fan_Command,AHU_Supply_Fan_Command,Discharge_Fan_Start_Stop_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Supply_Fan_Start_Stop_Command
	
	
