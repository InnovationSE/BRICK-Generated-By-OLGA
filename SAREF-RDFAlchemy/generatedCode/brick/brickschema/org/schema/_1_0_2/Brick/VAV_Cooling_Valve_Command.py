from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VAV_Cooling_Command import VAV_Cooling_Command
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Valve_Command import Cooling_Valve_Command


class VAV_Cooling_Valve_Command(VAV_Cooling_Command,Cooling_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Cooling_Valve_Command
	
	
