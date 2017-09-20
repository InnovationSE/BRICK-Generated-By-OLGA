from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Push_Button_Status import Emergency_Push_Button_Status


class Fume_Hood_Emergency_Push_Button_Status(Emergency_Push_Button_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fume_Hood_Emergency_Push_Button_Status
	
	
