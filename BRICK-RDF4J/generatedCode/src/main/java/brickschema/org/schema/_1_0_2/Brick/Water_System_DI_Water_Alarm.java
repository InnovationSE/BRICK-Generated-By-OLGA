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


import brickschema.org.schema._1_0_2.Brick.DI_Water_Alarm;
import brickschema.org.schema._1_0_2.Brick.Alarm;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.DI_Water;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Deionised_Water;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Deionised_Water_Alarm;
import brickschema.org.schema._1_0_2.Brick.Deionised_Water;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Alarm;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.DI_Water;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Water_System_DI_Water_Alarm implements IWater_System_DI_Water_Alarm {

	IRI newInstance;
	
	public Water_System_DI_Water_Alarm(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Water_System_DI_Water_Alarm"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
