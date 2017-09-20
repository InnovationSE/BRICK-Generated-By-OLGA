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


import brickschema.org.schema._1_0_2.Brick.Bypass_Air_Flow_Sensor;
import brickschema.org.schema._1_0_2.Brick.Air_Flow_Sensor;
import brickschema.org.schema._1_0_2.Brick.Flow_Sensor;
import brickschema.org.schema._1_0_2.Brick.Sensor;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class AHU_Bypass_Air_Flow_Sensor implements IAHU_Bypass_Air_Flow_Sensor {

	IRI newInstance;
	
	public AHU_Bypass_Air_Flow_Sensor(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#AHU_Bypass_Air_Flow_Sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
