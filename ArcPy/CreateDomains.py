import fmeobjects
import arcpy
import os

class FeatureCreator(object):
    """Template Class Interface:
    When using this class, make sure its name is set as the value of the 'Class to Process Features'
    transformer parameter.
    """
    
    def __init__(self):
        """Base constructor for class members."""
        pass
        
    def input(self, feature):
        """This method is called once by FME to initiate feature creation.
        Any number of features can be created and emitted by the self.pyoutput() method.
        The initial feature argument is a placeholder and can be ignored.
        """
        # Set workspace environment to geodatabase
        ws = FME_MacroValues['DataConnection']
        arcpy.env.workspace = ws

        # Set local parameters
        domName = "Material6"
        gdb = FME_MacroValues['DataConnection']
        inFeatures = FME_MacroValues['DataConnection'] + "/SAN_CASING"
        inField = "SEWERID"

        # Process: Create the coded value domain
        arcpy.management.CreateDomain(FME_MacroValues['DataConnection'], domName, "Valid pipe materials", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key" 
        # and the domain description as the "value" (domDict[code])
        domDict = {"CI":"Cast iron", "DI": "Ductile iron", "PVC": "PVC", "ACP": "Asbestos concrete", "COP": "Copper"}
    
        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary
        for code in domDict:        
            arcpy.management.AddCodedValueToDomain(gdb, domName, code, domDict[code])
    
        # Process: Constrain the material value of distribution mains
        arcpy.management.AssignDomainToField(inFeatures, inField, domName)

        newFeature = fmeobjects.FMEFeature()
        self.pyoutput(newFeature)
        
    def close(self):
        """This method is called at the end of the class."""
        pass
