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

import brickschema.org.schema._1_0_2.Brick.IHWS_Heat_Exchanger_Supply_Water_Temperature_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.ISupply_Water_Temperature_Proportional_Band_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IHeat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IHWS_Heat_Exchanger_Discharge_Water_Temperature_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IHeat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint;  


public interface IHWS_Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint extends IHWS_Heat_Exchanger_Supply_Water_Temperature_Setpoint, ISupply_Water_Temperature_Proportional_Band_Setpoint, IHeat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint, IHWS_Heat_Exchanger_Discharge_Water_Temperature_Setpoint, IHeat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
