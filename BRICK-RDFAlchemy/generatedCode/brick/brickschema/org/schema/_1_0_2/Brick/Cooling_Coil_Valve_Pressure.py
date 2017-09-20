from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Valve import Cooling_Valve


class Cooling_Coil_Valve_Pressure(Cooling_Valve):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Coil_Valve_Pressure
	
	
