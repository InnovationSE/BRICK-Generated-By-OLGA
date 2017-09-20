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

import brickschema.org.schema._1_0_2.Brick.IAHU_Discharge_Air_Temperature_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IEconomizer_Supply_Air_Temperature_Dead_Band_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Supply_Air_Temperature_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IEconomizer_Discharge_Air_Temperature_Dead_Band_Setpoint;  


public interface IAHU_Economizer_Discharge_Air_Temperature_Dead_Band_Setpoint extends IAHU_Discharge_Air_Temperature_Setpoint, IEconomizer_Supply_Air_Temperature_Dead_Band_Setpoint, IAHU_Supply_Air_Temperature_Setpoint, IEconomizer_Discharge_Air_Temperature_Dead_Band_Setpoint {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
