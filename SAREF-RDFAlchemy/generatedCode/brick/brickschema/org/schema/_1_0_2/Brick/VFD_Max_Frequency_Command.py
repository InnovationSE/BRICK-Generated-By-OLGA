from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Frequency_Command import VFD_Frequency_Command
from brick.brickschema.org.schema._1_0_2.Brick.Max_Frequency_Command import Max_Frequency_Command


class VFD_Max_Frequency_Command(VFD_Frequency_Command,Max_Frequency_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Max_Frequency_Command
	
	
