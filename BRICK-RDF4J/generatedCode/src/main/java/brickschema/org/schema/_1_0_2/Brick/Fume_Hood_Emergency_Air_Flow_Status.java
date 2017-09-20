/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/
package brickschema.org.schema._1_0_2.Brick;

import brick.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;

import java.math.BigDecimal;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.Date;


import brickschema.org.schema._1_0_2.Brick.Emergency_Air_Flow_Status;
import brickschema.org.schema._1_0_2.Brick.Status;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Fume_Hood_Emergency_Air_Flow_Status implements IFume_Hood_Emergency_Air_Flow_Status {

	IRI newInstance;
	
	public Fume_Hood_Emergency_Air_Flow_Status(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Fume_Hood_Emergency_Air_Flow_Status"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
