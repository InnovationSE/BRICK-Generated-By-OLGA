from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heat_Exchanger_Valve_Status import Heat_Exchanger_Valve_Status


class HVAC_Heat_Exchanger_Valve_Status(Heat_Exchanger_Valve_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HVAC_Heat_Exchanger_Valve_Status
	
	
