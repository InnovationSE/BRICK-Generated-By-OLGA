from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Water_System_Valve_Command import Water_System_Valve_Command
from brick.brickschema.org.schema._1_0_2.Brick.Perimeter_Heating_Valve_Command import Perimeter_Heating_Valve_Command


class Water_System_Perimeter_Heating_Valve_Command(Water_System_Valve_Command,Perimeter_Heating_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_System_Perimeter_Heating_Valve_Command
	
	
