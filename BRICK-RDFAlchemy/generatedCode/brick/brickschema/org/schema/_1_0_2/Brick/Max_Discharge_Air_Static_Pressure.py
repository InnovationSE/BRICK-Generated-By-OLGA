from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure import Discharge_Air_Static_Pressure
from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Max import Static_Pressure_Max


class Max_Discharge_Air_Static_Pressure(Discharge_Air_Static_Pressure,Static_Pressure_Max):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Max_Discharge_Air_Static_Pressure
	
	
