from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CRAC_On_Off_Status import CRAC_On_Off_Status
from brick.brickschema.org.schema._1_0_2.Brick.Dehumidification_On_Off_Status import Dehumidification_On_Off_Status


class CRAC_Dehumidification_On_Off_Status(CRAC_On_Off_Status,Dehumidification_On_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Dehumidification_On_Off_Status
	
	
