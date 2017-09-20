from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Valve_Command import Heating_Valve_Command
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Heating_Command import VAV_Heating_Command


class VAV_Heating_Valve_Command(Heating_Valve_Command,VAV_Heating_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Heating_Valve_Command
	
	
