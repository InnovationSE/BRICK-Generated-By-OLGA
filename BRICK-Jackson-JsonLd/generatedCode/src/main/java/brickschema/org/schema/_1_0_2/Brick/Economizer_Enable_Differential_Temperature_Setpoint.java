/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/
package brickschema.org.schema._1_0_2.Brick;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;

import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldId;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldProperty;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldType;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldLink;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldPropertyType;

import brick.jsonld.util.RefId;

import brickschema.org.schema._1_0_2.Brick.Economizer_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;






public  class Economizer_Enable_Differential_Temperature_Setpoint implements IEconomizer_Enable_Differential_Temperature_Setpoint {

	Map<String, List<RefId>> relations;
	
	public Economizer_Enable_Differential_Temperature_Setpoint(String id) {
		super();
		this.id = "https://brickschema.org/schema/1.0.2/Brick#" + id;
		relations = new HashMap<String, List<RefId>>();
		
	}

	@JsonldId
	public String id;
	
	@JsonIgnore
	public RefId getRefId()
	{
		return new RefId(id);
	}
	
	@JsonInclude(Include.NON_NULL)
	@JsonProperty("@type")
	public String getType()
	{
		return "https://brickschema.org/schema/1.0.2/Brick#Economizer_Enable_Differential_Temperature_Setpoint";
	}
	
	
	
	
	
	
}
