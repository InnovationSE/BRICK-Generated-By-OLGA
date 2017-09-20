from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Duct_Pressure_Status import Supply_Air_Duct_Pressure_Status
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Duct_Pressure_Status import Discharge_Air_Duct_Pressure_Status


class VAV_Supply_Air_Duct_Pressure_Status(Supply_Air_Duct_Pressure_Status,Discharge_Air_Duct_Pressure_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Supply_Air_Duct_Pressure_Status
	
	
