package com.campfhir.service.conversion;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;

import org.hl7.fhir.dstu3.model.Address;
import org.hl7.fhir.dstu3.model.Bundle;
import org.hl7.fhir.dstu3.model.CodeableConcept;
import org.hl7.fhir.dstu3.model.Coding;
import org.hl7.fhir.dstu3.model.DecimalType;
import org.hl7.fhir.dstu3.model.Extension;
import org.hl7.fhir.dstu3.model.StringType;
import org.hl7.fhir.dstu3.model.Enumerations.AdministrativeGender;
import org.hl7.fhir.exceptions.FHIRException;
import org.xml.sax.SAXException;

import com.campfhir.model.Patient;


/**
*
* @author  James Champion
* @version 1.0
* @since   2019-08-20 
*/
public class PatientConversion 
{
    
	public org.hl7.fhir.dstu3.model.Patient Patients(Patient patient) throws ParseException, IOException, ParserConfigurationException, SAXException
	{
			org.hl7.fhir.dstu3.model.Patient n = new org.hl7.fhir.dstu3.model.Patient(); 
			
			
			
			/******************** PNT_IDENTIFIER ******************************************************************************** 
			 * PNT_IDENTIFIER maps to Patient / identifier
			 ********************************************************************************************************************/
			n.setId(patient.getPNT_IDENTIFIER());
			
			/******************** PNT_GENDER ************************************************************************************ 
			 * PNT_GENDER maps to Patient / gender
			 */
			try 
			{
				n.setGender(AdministrativeGender.fromCode(patient.getPNT_GENDER()));
			} 
			catch (FHIRException e) 
			{
				e.printStackTrace();
			}
				
			/******************** PNT_BIRTHDATE *********************************************************************************
			 * PNT_BIRTHDATE maps to Patient / birthDate 
			 ********************************************************************************************************************/
			if(patient.getPNT_BIRTHDATE() != null)
			{
			    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-M-dd hh:mm:ss");
			    SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM");
			    Date date;
			    try {
				date = sdf.parse(patient.getPNT_BIRTHDATE());
				n.setBirthDate(date);
			    } catch (ParseException e) {
				try {
				    date = sdf2.parse(patient.getPNT_BIRTHDATE());
				    n.setBirthDate(date);
				} catch (ParseException e) {
				    e.printStackTrace();
				}
			    }
			}
			
			CodeableConcept ms = new CodeableConcept();
			
			Coding c = new Coding();
			


			/******************** PNT_MARITAL_STATUS_CODE ***********************************************************************
			 * PNT_MARITAL_STATUS_CODE  maps to Patient / maritalStatus / coding / code
			 ********************************************************************************************************************/
			c.setCode(patient.getPNT_MARITAL_STATUS_CODE());
			
			/******************** PNT_MARITAL_STATUS_SYSTEM *********************************************************************
			 * PNT_MARITAL_STATUS_SYSTEM maps to Patient / maritalStatus / coding / system
			 ********************************************************************************************************************/
			c.setSystem("http://terminology.hl7.org/CodeSystem/v3-MaritalStatus");//patient.getPNT_MARITAL_STATUS_SYSTEM());
			
			List<Coding> theCoding = new ArrayList<Coding>();
			
			theCoding.add(c);
			
			ms.setCoding(theCoding);
			n.setMaritalStatus(ms);	
		
			/******************** PNT_RACE **************************************************************************************
			 * PNT_RACE maps to Patient / extension / race / coding / code
			 ********************************************************************************************************************/
			Extension race = new Extension().setUrl("http://terminology.hl7.org/ValueSet/v3-Race").setValue(new StringType(patient.getPNT_RACE())); 
			n.addExtension(race);
			
			/******************** PNT_ETHNICITY *********************************************************************************
			 * PNT_ETHNICITY maps to Patient / extension / ethnicity / coding / code
			 ********************************************************************************************************************/
			Extension ethnicity = new Extension().setUrl("http://hl7.org/fhir/v3/Ethnicity").setValue(new StringType(patient.getPNT_ETHNICITY())); 
			n.addExtension(ethnicity);

			
			Address addrResource = n.addAddress();
			if(patient.getPNT_ADDRESS_EXT_LAT_VALUE()!=null && patient.getPNT_ADDRESS_EXT_LONG_VALUE() != null)
			{
				Extension geolocation = addrResource.addExtension();
				
				/******************** PNT_ADDRESS_EXT_LAT_VALUE ****************************************************************
				 * PNT_ADDRESS_EXT_LAT_VALUE maps to Patient / address / extension / latitude / value
				 ***************************************************************************************************************/
			    geolocation.addExtension("Latitude", new DecimalType(patient.getPNT_ADDRESS_EXT_LAT_VALUE()));
			    
				/******************** PNT_ADDRESS_EXT_LONG_VALUE ***************************************************************
				 * PNT_ADDRESS_EXT_LONG_VALUE maps to Patient / address / extension / longitude / value
				 ***************************************************************************************************************/
			    geolocation.addExtension("Longitude", new DecimalType(patient.getPNT_ADDRESS_EXT_LONG_VALUE()));
			}

		  return n;
	}
}
