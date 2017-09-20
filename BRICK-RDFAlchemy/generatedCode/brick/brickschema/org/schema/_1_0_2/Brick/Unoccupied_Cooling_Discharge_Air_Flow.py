from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling import Cooling
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air


class Unoccupied_Cooling_Discharge_Air_Flow(Cooling,Discharge_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Unoccupied_Cooling_Discharge_Air_Flow
	
	
