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


import brickschema.org.schema._1_0_2.Brick.Preheat_Coil_Entering_Air_Temperature_Sensor;
import brickschema.org.schema._1_0_2.Brick.Entering_Water_Temperature_Sensor;
import brickschema.org.schema._1_0_2.Brick.Temperature_Sensor;
import brickschema.org.schema._1_0_2.Brick.Sensor;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Entering_Water_Temperature_Sensor;
import brickschema.org.schema._1_0_2.Brick.Temperature_Sensor;
import brickschema.org.schema._1_0_2.Brick.Sensor;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class AHU_Preheat_Coil_Entering_Air_Temperature_Sensor implements IAHU_Preheat_Coil_Entering_Air_Temperature_Sensor {

	IRI newInstance;
	
	public AHU_Preheat_Coil_Entering_Air_Temperature_Sensor(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#AHU_Preheat_Coil_Entering_Air_Temperature_Sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
