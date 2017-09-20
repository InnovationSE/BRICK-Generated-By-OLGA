/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/

package brickschema.org.schema._1_0_2.Brick;

import java.util.ArrayList;
import java.util.List;

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

import brickschema.org.schema._1_0_2.Brick.IEmergency_Power_Off_System_Enable_Status;  
import brickschema.org.schema._1_0_2.Brick.ICRAC_Emergency_Power_Off_Enable_Status;  


public interface ICRAC_Emergency_Power_Off_System_Enable_Status extends IEmergency_Power_Off_System_Enable_Status, ICRAC_Emergency_Power_Off_Enable_Status {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}