from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Cooling_Supply_Air_Flow import Occupied_Cooling_Supply_Air_Flow
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Max_Supply_Air_Flow import Cooling_Max_Supply_Air_Flow


class Occupied_Cooling_Max_Supply_Air_Flow(Occupied_Cooling_Supply_Air_Flow,Cooling_Max_Supply_Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Occupied_Cooling_Max_Supply_Air_Flow
	
	
