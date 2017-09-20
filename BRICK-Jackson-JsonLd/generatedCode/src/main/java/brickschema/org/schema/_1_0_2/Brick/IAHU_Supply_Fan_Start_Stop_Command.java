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

import brickschema.org.schema._1_0_2.Brick.ISupply_Fan_Start_Stop_Command;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Discharge_Fan_Command;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Supply_Fan_Command;  
import brickschema.org.schema._1_0_2.Brick.IDischarge_Fan_Start_Stop_Command;  


public interface IAHU_Supply_Fan_Start_Stop_Command extends ISupply_Fan_Start_Stop_Command, IAHU_Discharge_Fan_Command, IAHU_Supply_Fan_Command, IDischarge_Fan_Start_Stop_Command {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}