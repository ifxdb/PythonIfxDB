# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_066_TableObjects(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_066)

  def run_test_066(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    result = ifx_db.tables(conn, None, config.user.lower(), 'animals')
      
#    NOTE: This is a workaround
#    function fetch_object() to be implemented...
#    row = ifx_db.fetch_object(result)
#    JS: check .lower() functionatily  
  
    class Row:
        pass

    data = ifx_db.fetch_assoc(result)
    while ( data ):
      row = Row()
      row.table_schem = data['TABLE_SCHEM']
      row.table_name = data['TABLE_NAME']
      row.table_type = data['TABLE_TYPE']
      row.remarks = data['REMARKS']
          
      print "Schema:  %s" % row.table_schem
      print "Name:    %s" % row.table_name
      print "Type:    %s" % row.table_type
      print "Remarks: %s\n" % row.remarks
#      row = ifx_db.fetch_object(result)
      data = ifx_db.fetch_assoc(result)

    result = ifx_db.tables(conn, None, config.user.lower(), 'animal_pics')
    
#    row = ifx_db.fetch_object(result)
    data = ifx_db.fetch_assoc(result)
    while (data ):
      row = Row()
      row.table_schem = data['TABLE_SCHEM']
      row.table_name = data['TABLE_NAME']
      row.table_type = data['TABLE_TYPE']
      row.remarks = data['REMARKS']
        
      print "Schema:  %s" % row.table_schem
      print "Name:    %s" % row.table_name
      print "Type:    %s" % row.table_type
      print "Remarks: %s\n" % row.remarks
      data = ifx_db.fetch_assoc(result)
      
    result = ifx_db.tables(conn, None, config.user.lower(), 'anime_cat')
    
#    row = ifx_db.fetch_object(result)
    data = ifx_db.fetch_assoc(result)
    while ( data ): 
      row = Row()
      row.table_schem = data['TABLE_SCHEM']
      row.table_name = data['TABLE_NAME']
      row.table_type = data['TABLE_TYPE']
      row.remarks = data['REMARKS']
        
      print "Schema:  %s" % row.table_schem
      print "Name:    %s" % row.table_name
      print "Type:    %s" % row.table_type
      print "Remarks: %s\n" % row.remarks
#      row = ifx_db.fetch_object(result)
      data = ifx_db.fetch_assoc(result)
    
    ifx_db.free_result(result)
    ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#Schema:  %s
#Name:    ANIMALS
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    ANIMAL_PICS
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    ANIME_CAT
#Type:    VIEW
#Remarks: None
#__ZOS_EXPECTED__
#Schema:  %s
#Name:    ANIMALS
#Type:    TABLE
#Remarks: 
#
#Schema:  %s
#Name:    ANIMAL_PICS
#Type:    TABLE
#Remarks: 
#
#Schema:  %s
#Name:    ANIME_CAT
#Type:    VIEW
#Remarks: 
#__SYSTEMI_EXPECTED__
#Schema:  %s
#Name:    ANIMALS
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    ANIMAL_PICS
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    ANIME_CAT
#Type:    VIEW
#Remarks: None
#__IDS_EXPECTED__
#Schema:  %s
#Name:    animals
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    animal_pics
#Type:    TABLE
#Remarks: None
#
#Schema:  %s
#Name:    anime_cat
#Type:    VIEW
#Remarks: None
