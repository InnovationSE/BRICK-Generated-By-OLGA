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


import brickschema.org.schema._1_0_2.Brick.Mixed_Air;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Air;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Air_Damper_Position;
import brickschema.org.schema._1_0_2.Brick.Damper_Position;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Mixed_Air_Damper_Position implements IMixed_Air_Damper_Position {

	IRI newInstance;
	
	public Mixed_Air_Damper_Position(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Mixed_Air_Damper_Position"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
