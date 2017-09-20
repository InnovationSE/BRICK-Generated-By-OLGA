from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heat_Exchanger_Valve_Command import Heat_Exchanger_Valve_Command


class HWS_Heat_Exchanger_Valve_Command(Heat_Exchanger_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Heat_Exchanger_Valve_Command
	
	
