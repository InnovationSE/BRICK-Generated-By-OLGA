from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Heating_Supply_Air_Flow import Occupied_Heating_Supply_Air_Flow
from brick.brickschema.org.schema._1_0_2.Brick.Heating_Max_Supply_Air_Flow import Heating_Max_Supply_Air_Flow


class Occupied_Heating_Max_Supply_Air_Flow(Occupied_Heating_Supply_Air_Flow,Heating_Max_Supply_Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Occupied_Heating_Max_Supply_Air_Flow
	
	
