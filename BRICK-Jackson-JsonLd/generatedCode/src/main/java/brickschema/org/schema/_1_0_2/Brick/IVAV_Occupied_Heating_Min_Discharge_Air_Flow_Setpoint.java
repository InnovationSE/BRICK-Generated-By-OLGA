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

import brickschema.org.schema._1_0_2.Brick.IOccupied_Heating_Min_Supply_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IVAV_Heating_Min_Discharge_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IOccupied_Heating_Discharge_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IVAV_Occupied_Heating_Supply_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IVAV_Occupied_Heating_Discharge_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IVAV_Heating_Min_Supply_Air_Flow_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IOccupied_Heating_Min_Discharge_Air_Flow_Setpoint;  


public interface IVAV_Occupied_Heating_Min_Discharge_Air_Flow_Setpoint extends IOccupied_Heating_Min_Supply_Air_Flow_Setpoint, IVAV_Heating_Min_Discharge_Air_Flow_Setpoint, IOccupied_Heating_Discharge_Air_Flow_Setpoint, IVAV_Occupied_Heating_Supply_Air_Flow_Setpoint, IVAV_Occupied_Heating_Discharge_Air_Flow_Setpoint, IVAV_Heating_Min_Supply_Air_Flow_Setpoint, IOccupied_Heating_Min_Discharge_Air_Flow_Setpoint {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
