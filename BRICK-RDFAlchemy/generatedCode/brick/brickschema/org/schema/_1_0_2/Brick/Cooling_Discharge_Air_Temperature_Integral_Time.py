from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Cooling import Discharge_Air_Temperature_Cooling


class Cooling_Discharge_Air_Temperature_Integral_Time(Discharge_Air_Temperature_Cooling):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Discharge_Air_Temperature_Integral_Time
	
	
