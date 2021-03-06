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


import brickschema.org.schema._1_0_2.Brick.Yearly_Steam_Usage_Meter;
import brickschema.org.schema._1_0_2.Brick.Steam_Usage_Meter;
import brickschema.org.schema._1_0_2.Brick.Meter;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Steam_System_Yearly_Steam_Usage_Meter implements ISteam_System_Yearly_Steam_Usage_Meter {

	IRI newInstance;
	
	public Steam_System_Yearly_Steam_Usage_Meter(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Steam_System_Yearly_Steam_Usage_Meter"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
