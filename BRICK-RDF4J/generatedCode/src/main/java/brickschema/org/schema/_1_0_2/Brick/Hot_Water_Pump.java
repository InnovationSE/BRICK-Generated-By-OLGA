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


import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Pump;
import brickschema.org.schema._1_0_2.Brick.HVAC;
import brickschema.org.schema._1_0_2.Brick.Equipment;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Hot_Water_Pump implements IHot_Water_Pump {

	IRI newInstance;
	
	public Hot_Water_Pump(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Hot_Water_Pump"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
