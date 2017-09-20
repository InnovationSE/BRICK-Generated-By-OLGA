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


import brickschema.org.schema._1_0_2.Brick.Water_System;
import brickschema.org.schema._1_0_2.Brick.Equipment;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Hot_Water_System implements IHot_Water_System {

	IRI newInstance;
	
	public Hot_Water_System(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Hot_Water_System"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
