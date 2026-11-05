# Industries Common Resources Developer Guide 264 — sección: Omnistudio (121 artículos)

=== ARTICLE: apex_namespace_omnistudiocore.htm ===
---
page_id: apex_namespace_omnistudiocore.htm
title: omnistudiocore Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_namespace_omnistudiocore.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# omnistudiocore Namespace

Omnistudiocore namespace and its classes are for internal use only.

=== ARTICLE: connect_requests_calculation_procedure_step_input.htm ===
---
page_id: connect_requests_calculation_procedure_step_input.htm
title: Calculation Procedure Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_calculation_procedure_step_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Step Input

Input representation for the expression set version
    steps.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

#### 

                    

                    

                  

                  
                    

                    

                    
- 
- 
- 
- 
- 
- 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `calculationMatrixId` | String | The ID of the decision matrix record. | Optional Note This field is required when the step type is `MatrixLookup`. | 53.0 |
| `childStepId` | String[] | The IDs of the child steps in the parent expression set version record step. | Optional | 53.0 |
| `conditionsExpressionText` | String | The user-defined expression text used in a condition step. | Optional | 53.0 |
| `conditionsUiFormattedText` | String | Additional information required to render the condition expression text. For example, when the current step has a subset of `childStepIds` that is marked to bypass. Specify `"conditionsUiFormattedText":"{\"bypass\":[\"0mqx000000000f6AAA\"]}"` in the field to enable navigation outside the branch. | Optional | 53.0 |
| `description` | String | The description of the expression set version record step. | Optional | 53.0 |
| `formulaExpressionText` | String | The formula used in a calculation step. | Optional | 53.0 |
| `formulaUiFormattedText` | String | Reserved for future use. | Optional | 53.0 |
| `id` | String | The ID of the expression set version record step. | Required Note This field is required for the update request. | 53.0 |
| `inputVariablesFormatText` | String | The input variables in JSON format required to execute an expression set version record step. | Required | 53.0 |
| `isResultIncluded` | Boolean | Indicates whether the result of a step execution is returned to the user. The default is `false`. | Optional | 53.0 |
| `name` | String | The name of the expression set version record step. | Optional | 53.0 |
| `outputVariablesFormatText` | String | The output variables in JSON format returned by an expression set version record step. | Required | 53.0 |
| `outputVariablesMappingText` | String | The mapping between the output variable of a step and the input variable for a sub-calculation procedure version record or a sub-decision matrix record. | Optional Note This field is required when the step type is `MatrixLookup` or `ReferenceProcedure`. | 53.0 |
| `referenceCalculationProcedureId` | String | The ID of the sub-calculation procedure version record. | Optional Note This field is required when the step type is `ReferenceProcedure`. | 53.0 |
| `returnMessageValueSet` | String | User-configured messages for the result of the current step. | Optional | 53.0 |
| `stage` | String | Specify whether the expression set version step is a calculation or an aggregation. Note In version 53.0 and later, only calculation is supported. | Required | 53.0 |
| `stepType` | String | Specify the step type in the expression set version. Possible values are: `Condition` `Calculation` `MatrixLookup` `ReferenceProcedure` `Branch` `ConditionalGroup` | Required | 53.0 |

=== ARTICLE: connect_requests_calculation_procedure_version_definition_input.htm ===
---
page_id: connect_requests_calculation_procedure_version_definition_input.htm
title: Calculation Procedure Version Definition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_calculation_procedure_version_definition_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Version Definition Input

Input representation of the expression set version
    definition.

         

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

**JSON example**

: 
                  

Specify the version record ID or `CLONE` in
                     the `versionId` field to either update an
                     existing expression set version record or save the expression set version
                     record as a new expression set version record.

                  

```
{
   "calculationProcedureId":"0k0xx00000000HlAAI",
   "code":"200",
   "constants":{
      "details":[ {
         "apiName":"SENIOR_CITIZEN_AGE",
         "dataType":"Number",
         "defaultValue":"60",
         "isEditable":true,
         "isUserDefined":true,
         "name":"SENIOR_CITIZEN_AGE",
         "precision":2
      }.]
   },
   "enabled":false,
   "isSuccess":true,
   "message":"",
   "name":"rule3 V1",
   "rank":1,
   "root":{
      "steps":[
         "0mqxx00000000UfAAI"
      ]
   },
   "startDate":"2021-08-04T08:57:23.000Z",
   "step":{
      "details":{
         "0mqxx00000000UfAAI":{
            "childStepIds":[],
            "conditionsExpressionText":"age == SENIOR_CITIZEN_AGE",
            "conditionsUiFormattedText":"{\"bypass\":[]}",
            "id":"0mqxx00000000UfAAI",
            "inputVariablesFormatText":"[{\"name\":\"age\",\"dataType\":\"Number\",\"alias\":\"age\"}]",
            "isResultIncluded":false,
            "name":"Condition",
            "outputVariablesFormatText":"{\"name\":\"condition_output__1\",\"dataType\":\"Boolean\",\"alias\":\"condition_output__1\"}",
            "outputVariablesMappingText":"{\"condition_output__1\":\"condition_output__1\"}",
            "returnMessageValueSet":"{\"true\":\"\",\"false\":\"\"}",
            "stage":"Calculation",
            "stepType":"Condition"
         }
      }
   },
   "variables":{
      "details":[ {
         "apiName":"condition_output__1",
         "dataType":"Boolean",
         "defaultValue":"False",
         "id":"0kJxx00000000KzEAI",
         "isEditable":false,
         "isUserDefined":false,
         "name":"condition_output__1"
      }, {
         "apiName":"age",
         "dataType":"Number",
         "defaultValue":"60",
         "id":"0kJxx00000000L0EAI",
         "isEditable":true,
         "isUserDefined":true,
         "name":"age",
         "precision":2
      } ]
   },
   "versionId":"0k1xx00000000KzAAI",
   "versionNumber":1
}
```

               

**Properties**

: 

#### 

                              

                              

                              

                              

                              

                           

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `calculationProcedureId` | String | The ID of the expression-set record that you want to update the definition details for or save as a new version definition record. | Optional | 53.0 |
| `constants` | [Calculation Procedure Resource](./connect_requests_resource_input.htm.md)[] | The constant values passed in the expression set version record. | Optional | 53.0 |
| `description` | String | The description of the expression set version record. | Optional | 53.0 |
| `enabled` | Boolean | Indicates whether the expression set version record is active (`true`) for execution or not (`false`). The default is `false`. Note This field must be false with the update or save as request. | Optional | 53.0 |
| `endDate` | String | The date and time until when an active expression set version record is in effect. | Optional | 53.0 |
| `name` | String | The name of the expression set version record. | Optional | 53.0 |
| `rank` | Integer | The rank of the expression set version record. When multiple records are in effect, the record that’s ranked higher takes precedence. | Optional | 53.0 |
| `root` | String[] | The first steps defined in the expression set version record. | Optional | 53.0 |
| `startDate` | String | The start date and time from when an active expression set version record is in effect. | Optional | 53.0 |
| `step` | Map<String, [Calculation Procedure Step Input](./connect_requests_calculation_procedure_step_input.htm.md)> | The list of steps defined in the expression set version record. | Optional | 53.0 |
| `variables` | [Calculation Procedure Resource](./connect_requests_resource_input.htm.md)[] | The variable values passed in the expression set version record. | Optional | 53.0 |
| `versionId` | String | The ID of the expression set version record. | Required | 53.0 |
| `versionNumber` | Integer | The version number of the expression set record. | Optional | 53.0 |

=== ARTICLE: connect_requests_data_mapper_details.htm ===
---
page_id: connect_requests_data_mapper_details.htm
title: Data Mapper Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_data_mapper_details.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Details

Input representation of the data mapper details to clear the cache for.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "dataMappers": [
    {
      "dataMapperName": "DRWithLoad",
      "input": {
        "Name": "Get Account Details"
      }
    }
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `dataMapperName` | String | Name of the data mapper to clear the cache for. The execution cache is cleared for the storage that's specified in the `cacheStorageType` property. | Required | 64.0 |
| `input` | String | Custom JSON data to clear the cache. | Optional | 64.0 |

=== ARTICLE: connect_requests_data_mapper_execute_input_data.htm ===
---
page_id: connect_requests_data_mapper_execute_input_data.htm
title: Data Mapper Execute Input Data
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_data_mapper_execute_input_data.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execute Input Data

Input representation of the list of custom data for the execution of the data
    mapper.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": [
    {
      "Name": "Get Account Details"
    }
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | String[] | List of configuration details for executing the data mappers. | Required | 64.0 |

=== ARTICLE: connect_requests_data_mapper_execution_input.htm ===
---
page_id: connect_requests_data_mapper_execution_input.htm
title: Data Mapper Execution Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_data_mapper_execution_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execution Input

Input representation of the execution details of a data mapper.

**JSON example**

: 
            

```
{
  "dataMapperInput": {
    "inputs": [
      {
        "Name": "Get Account Details"
      }
    ]
  },
  "inputType": "JSON",
  "options": {
    "ignoreCache": false
  }
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `dataMapperInput` | [Data Mapper Execute Input Data](./connect_requests_data_mapper_execute_input_data.htm.md) | Details for executing the data mapper. | Required | 64.0 |
| `inputType` | String | Type of data mapper input. For example, JSON, XML, or custom class. | Required | 64.0 |
| `options` | [Data Mapper Execution Options](./connect_requests_data_mapper_execution_options.htm.md) | Optional parameters to refine the data mapper execution. | Optional | 64.0 |

=== ARTICLE: connect_requests_data_mapper_execution_options.htm ===
---
page_id: connect_requests_data_mapper_execution_options.htm
title: Data Mapper Execution Options
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_data_mapper_execution_options.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execution Options

Input representation of the optional parameters for the data mapper
    execution.

**JSON example**

: 
            

```
{
  "options": {
    "ignoreCache": false,
    "locale": "en-US"
  }
}
```

          

**Properties**

: 

                    

                    

                    

                    

                    

          

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `ignoreCache` | Boolean | Indicates whether to ignore the cache during the data mapper execution (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `ignore​MetadataCache` | Boolean | Indicates whether to ignore the metadata cache during the data mapper execution (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `ignoreMetadata​Permissions` | Boolean | Indicates whether to ignore the metadata permission during the data mapper execution (`true`) or elevate the metadata permission (`false`).The default value is `false`. | Optional | 64.0 |
| `locale` | String | Locale that's applied during the data mapper execution. | Optional | 64.0 |
| `resetCache` | Boolean | Indicates whether to reset the cache during the data mapper execution (`true`) or not (`false`).If set to `true`, data is fetched from the database instead of cache. The default value is `false`. | Optional | 64.0 |
| `shouldIgnore​Commit` | Boolean | Indicates whether to skip committing the transaction data to database (`true`)or not (`false`).The default value is `true`. | Optional | 64.0 |
| `shouldSend​LegacyResponse` | Boolean | Indicates whether response is displayed in the legacy Apex object format (`true`) or in generic format (`false`).The default value is `false`. | Optional | 64.0 |
| `withoutSharing` | Boolean | Indicates whether the Data Mapper must ignore the user sharing rules while executing the data (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |

=== ARTICLE: connect_requests_datamapper_cache_input_param.htm ===
---
page_id: connect_requests_datamapper_cache_input_param.htm
title: Data Mapper Clear Cache Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_datamapper_cache_input_param.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Clear Cache Input

Input representation of the details to clear the cache of the data mappers.

**JSON example**

          
: This is a sample example to clear the execution cache by using only the name of the
            data mapper.

: 

```
{
  "cacheStorageType": "Metadata",
  "dataMapperList": {
    "dataMappers": [
      {
        "dataMapperName": "DRWithLoad"
      }
    ]
  }
}
```

          
: This is a sample example to clear the execution cache by using the name of the data
            mapper along with additional inputs.

          
: 
            

```
{
  "cacheStorageType": "Session",
  "dataMapperList": {
    "dataMappers": [
      {
        "dataMapperName": "DRWithLoad",
        "input": {
          "Name": "Get Account Details"
        }
      }
    ]
  }
}
```

          

**Properties**

: 

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `cacheStorageType` | String | Storage type that's used for caching the data. Valid values are: `Session`—Cache is stored in the current user session. `Org`—Cache is shared across the entire organization. `All`—Refers to both session and org-level cache. | Required | 64.0 |
| `dataMapperList` | [Data Mapper Details](./connect_requests_data_mapper_details.htm.md)[] | List of data mappers to clear the cache for. | Required | 64.0 |

=== ARTICLE: connect_requests_decision_matrix_column.htm ===
---
page_id: connect_requests_decision_matrix_column.htm
title: Decision Matrix Column Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_column.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Column
    Input

Input representation of the information required to add, update, or
      delete columns in a decision matrix.

      
      
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    
- 
- 

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action` | String | The type of action you want to perform on a column.Possible values are: `delete` `update` | Required Note Leave this field blank if you’re adding a column in a decision matrix. | 53.0 |
| `apiName` | String | The API name of a column. | Optional | 53.0 |
| `columnType` | String | The type of a column.Possible values are: `Input` `Output` | Required | 53.0 |
| `dataType` | String | The data type of a column. | Optional | 53.0 |
| `displaySequence` | Integer | The display sequence of a column. | Optional | 53.0 |
| `id` | String | The ID of the column record to be updated or deleted. | Required Note Leave this field blank if you’re adding a column in a decision matrix. | 53.0 |
| `name` | String | The name of a column. | Required | 53.0 |
| `rangeValues` | String | The range values of a column. The range columns contain a sorted list of comma-separated values, which are updated whenever a row is added to the Decision Matrix Version. | Optional | 53.0 |

=== ARTICLE: connect_requests_decision_matrix_columns_input.htm ===
---
page_id: connect_requests_decision_matrix_columns_input.htm
title: Decision Matrix Columns Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_columns_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Columns Input

Input representation of the information to manage columns in relation
      to a decision matrix.

**JSON example**

: 
            

Add a column:

            

```
{
   "columns" : [ {
      "apiName" : "Name",
      "columnType" : "Input",
      "dataType" : "Text",
      "displaySequence" : 4,
      "name" : "Name"
   }]
}
```

          

          
: 
            

Delete a column:

            

```
{
   "columns" : [ {
      "action" : "delete",
      "id" : "0lJR0000000014bMAA"
   }]
}
```

          

          
: 
            

Update a column:

            

```
{
   "columns" : [ {
      "id" : "0lJR0000000014hMAA",
      "action" : "update",
      "columnType" : "Input",
      "name" : "First Name"
   }]
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `columns` | [Decision Matrix Column Input](./connect_requests_decision_matrix_column.htm.md)[] | List of columns to be added, updated, or deleted in a decision matrix. | Required | 53.0 |

=== ARTICLE: connect_requests_decision_matrix_row_input.htm ===
---
page_id: connect_requests_decision_matrix_row_input.htm
title: Decision Matrix Row Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_row_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Row Input

Input representation of the information required to add, update, or
      delete rows in a decision matrix version.

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    
- 
- 

                    

#### 

                    

                  

                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action` | String | Type of action you want to perform on a row.Possible values are: `delete` `update` | Required Note Leave this field blank if you’re adding a row in a decision matrix version. | 53.0 |
| `id` | String | The ID of the row record to be updated or deleted. | Required Note Leave this field blank if you’re adding a row to a decision matrix version. | 53.0 |
| `name` | String | Name of the row. | Optional | 53.0 |
| `rowData` | Map<String, Object> | The key-value pair for the row. All column values are required for update and delete operations. | Required | 53.0 |

=== ARTICLE: connect_requests_decision_matrix_rows_input.htm ===
---
page_id: connect_requests_decision_matrix_rows_input.htm
title: Decision Matrix Rows Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_rows_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Rows Input

Input representation of the information to manage rows in relation to
      the decision matrix version.

      
        
          

**JSON Example**

          
: 
            

Add a row:

            

```
{
  "rows": [
    {
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "2000"
      }
    }
  ]
}

```

          

          
: 
            

Delete a row:

            

```
{
  "rows": [
    {
      "id": "a1j5w000006D04uAAC",
      "action": "delete",
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "2000"
      }
    }
  ]
}

```

          

          
: 
            

Update a row:

            

```
{
  "rows": [
    {
      "id": "a1j5w000006D04uAAC",
      "action": "update",
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "1500"
      }
    }
  ]
}

```

          

          
: 
            

Add row using a CSV file:

          

          
: 
            

```
{
   "fileId" : "f1j5w000005D04uFGC"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fileId` | String | The ID of the [Content Document Version](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_contentversion.htm) that contains the rows details to be added or updated in a decision matrix version. | Optional Note This field is required if you’re using a CVS file to add or update rows. | 53.0 |
| `rows` | [Decision Matrix Row Input](./connect_requests_decision_matrix_row_input.htm.md)[] | List of rows to be added, updated, or deleted in a decision matrix version. | Required | 53.0 |

=== ARTICLE: connect_requests_integration_procedure_cache_input.htm ===
---
page_id: connect_requests_integration_procedure_cache_input.htm
title: Integration Procedure Clear Cache Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_cache_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Clear Cache Input

Input representation of the details to clear the execution cache of the integration
    procedures.

**JSON example**

          
: This is a sample example to clear the cache of an integration procedure by using the
            key that's associated with the integration procedure and cache storage type.

          
: 
            

```
{
  "cacheStorageType": "Metadata",
  "ipInput": {
    "inputs": [
      {
        "ipkey": "Account_GetAccountDetails"
      }
    ]
  }
}
```

          

          
: This is a sample example to clear the cache of an integration procedure by using the
            cache keys and cache storage type.

: 

```
{
  "cacheKeys": {
    "cacheKeys": [
      "IP06535636"
    ]
  },
  "cacheStorageType": "Metadata"
}
```

**Properties**

: 

- 
- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `cacheKeys` | [Integration Procedure Cache Keys](./connect_requests_integration_procedure_cache_keys_list.htm.md) | List of cache keys to clear the cache for. Cache keys are used to identify the cached data. | Optional | 64.0 |
| `cacheStorageType` | String | Storage type that's used for caching the data. Valid values are: `All`—Includes all cache types, such as metadata, session, and org-level caches. `Metadata`—Cache is used for configuration-related data such as schemas or field mappings. `Org`—Cache is shared across the entire organization. `Session`—Cache is stored in the current user session. | Required | 64.0 |
| `iPInput` | [Integration Procedure Details](./connect_requests_integration_procedure_cache_input_data.htm.md)[] | List of integration procedures to clear the cache for. | Optional | 64.0 |

=== ARTICLE: connect_requests_integration_procedure_cache_input_data.htm ===
---
page_id: connect_requests_integration_procedure_cache_input_data.htm
title: Integration Procedure Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_cache_input_data.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Details

Input representation of the details of the integration procedures to clear the cache
    for.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": [
    {
      "ipkey": "Account_GetAccountDetails",
      "inputData": "{\"Name\": \"Get Account Details\"}",
      "blockName": "Cache"
    }
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `blockName` | String | Block name of the integration procedure. | Optional | 64.0 |
| `iPKey` | String | Unique key that's associated with the integration procedure. The format of the value for this property is `Type_SubType`. | Required | 64.0 |
| `inputData` | String | Additional data to clear the cache. | Optional | 64.0 |

=== ARTICLE: connect_requests_integration_procedure_cache_keys_list.htm ===
---
page_id: connect_requests_integration_procedure_cache_keys_list.htm
title: Integration Procedure Cache Keys
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_cache_keys_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Cache Keys

Input representation of the cache keys to clear the execution cache.

    
      
        
          

**JSON example**

          
: 
            

```
{
    "cacheKeys": [
      "IP06535636"
    ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `cacheKeys` | String[] | List of cache keys to clear the cache for. | Optional | 64.0 |

=== ARTICLE: connect_requests_integration_procedure_service_run_input.htm ===
---
page_id: connect_requests_integration_procedure_service_run_input.htm
title: Integration Procedure Service Run
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_service_run_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Service Run

Input representation of the details to execute an integration procedure from
    Apex.

        
          

**JSON example**

          
: 
            

```
{
  "input": {
    "inputs": [
      "{\"Name\": \"Get Account Details\"}"
    ]
  },
  "options": {
    "ignoreCache": false
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `input` | [Integration Procedure Service Run Input](./connect_requests_integration_procedure_service_run_input_list.htm.md) | Details to execute the integration procedure. | Required | 64.0 |
| `options` | [Integration Procedure Service Run Options](./connect_requests_integration_procedure_service_run_options.htm.md) | Optional parameters to refine the execution of the integration procedure. | Optional | 64.0 |

=== ARTICLE: connect_requests_integration_procedure_service_run_input_list.htm ===
---
page_id: connect_requests_integration_procedure_service_run_input_list.htm
title: Integration Procedure Service Run Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_service_run_input_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Service Run Input

Input representation of the list of custom data to execute an integration procedure
    from Apex.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": [
    "{\"Name\": \"Get Account Details\"}"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | String[] | List of configuration details for executing the integration procedures. | Required | 64.0 |

=== ARTICLE: connect_requests_integration_procedure_service_run_options.htm ===
---
page_id: connect_requests_integration_procedure_service_run_options.htm
title: Integration Procedure Service Run Options
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_integration_procedure_service_run_options.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Service Run Options

Input representation of the optional parameters to customize and refine the execution of
    the integration procedure.

**JSON example**

: 
            

```
{
  "options": {
    "ignoreCache": false,
    "resetCache": true
  }
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `chainable` | Boolean | Indicates whether the integration procedure is executed in multiple chained calls (`true`) or as a single call (`false`).If the `chainable` property is set to `true`, the integration procedure automatically splits into smaller, sequentially executed pieces to avoid exceeding Salesforce governor limits or configured timeout thresholds. The default value is `false`. | Optional | 64.0 |
| `ignoreCache` | Boolean | Indicates whether to ignore the cache during the execution of the integration procedure (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `isDebug` | Boolean | Indicates whether to display the debugging details in the response (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `queueable​Chainable` | Boolean | Indicates whether the integration procedure executes the multiple chained calls asynchronously in the background as a queueable job (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `resetCache` | Boolean | Indicates whether to reset the cache during the execution of the integration procedure (`true`) or not (`false`).If set to `true`, data will be fetched from the database instead of the cache. The default value is `false`. | Optional | 64.0 |
| `shouldSend​LegacyResponse` | Boolean | Indicates whether response is displayed in the legacy Apex object format (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `useFuture` | Boolean | Indicates whether the integration procedure should run asynchronously as a fire-and-forget Apex job without returning a response (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `useQueueable` | Boolean | Indicates whether the integration procedure should run asynchronously by using a queueable Apex job that returns a job ID in the response (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `useQueueable​ApexRemoting` | Boolean | Indicates whether to run the operation in a queueable Apex job with no chaining (`true`) or not (`false`).The default value is `false`. | Optional | 64.0 |
| `vlcApex​Response` | Boolean | Indicates whether the response payload must be displayed (`true`) or not (`false`).If set to `true`, the response payload is displayed that contains the fields, such as `vlcStatus`, `vlcIPData`, and `vlcMessage` to manage and track the execution state of a chainable process. The default value is `false`. | Optional | 64.0 |
| `vlcIPData` | String | Unique key that represents the saved execution state of a chainable integration procedure.This key is included in the subsequent calls to resume processing from where the execution of the integration procedure left off. | Optional | 64.0 |
| `vlcMessage` | String | Contains error messages or additional information that's returned by the integration procedure. The value is `null` if there are no messages returned by the integration procedure. | Optional | 64.0 |
| `vlcStatus` | String | Current status of the execution process of the integration procedure. | Optional | 64.0 |

=== ARTICLE: connect_requests_resource_input.htm ===
---
page_id: connect_requests_resource_input.htm
title: Resource Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_resource_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resource Input

Input representation of the expression set resource (variable or
      constant).

         

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

**JSON example**

: 

```
{
   "variables":{
      "details":[ {
         "apiName":"condition_output__1",
         "dataType":"Boolean",
         "defaultValue":"False",
         "id":"0kJxx00000000KzEAI",
         "isEditable":false,
         "isUserDefined":false,
         "name":"condition_output__1"
      } ]
   }
}
"constants":{
   "details":[ {
      "apiName":"SENIOR_CITIZEN_AGE",
      "dataType":"Number",
      "defaultValue":"60",
      "isEditable":true,
      "isUserDefined":true,
      "name":"SENIOR_CITIZEN_AGE",
      "precision":2
   }.]
}
```

**Properties**

: 

- 
- 
- 
- 
- 
- 

#### 

#### 

#### 

#### 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | The API name of the variable or constant. | Required | 53.0 |
| `calculationMatrixName` | String | The name of the decision matrix used in the variable or constant. | Optional | 53.0 |
| `dataType` | String | The date type of the variable or constant.Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `Text` | Required | 53.0 |
| `defaultValue` | String | The default value of the variable or constant. | Optional | 53.0 |
| `displayName` | String | The display name of the variable or constant that appears in the user interface. | Optional | 53.0 |
| `id` | String | The ID of the variable or constant. | Required Note This field is required for the update request. | 53.0 |
| `isEditable` | Boolean | Indicates whether the variable or constant is editable. Note This field is for user-interface use only. | Optional | 53.0 |
| `isUserDefined` | Boolean | Indicates whether the variable or constant is user-defined. | Optional | 53.0 |
| `name` | String | The name of the variable or constant. | Required | 53.0 |
| `precision` | Integer | The floating-point precision of the variable or constant. | Required Note This field is required when the data type is `number`, `currency`, or `percentage`. | 53.0 |
| `uiDisplayOrder` | Integer | The display order of the variable or constant in the UI. Note Reserved for future use. | Optional | 53.0 |

=== ARTICLE: connect_requests_simulation_config_input.htm ===
---
page_id: connect_requests_simulation_config_input.htm
title: Simulation Config Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_simulation_config_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Config Input

Input information of the configuration version to run a
      simulation.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `versionInfo` | [Simulation Version Info Input](./connect_requests_simulation_version_info_input.htm.md) | The version information of the expression set. | Required | 53.0 |

=== ARTICLE: connect_requests_simulation_context_input.htm ===
---
page_id: connect_requests_simulation_context_input.htm
title: Simulation Context Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_simulation_context_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Context Input

Input representation of context details for
  simulation.

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `context​MappingId` | String | ID of the context mapping. | Optional | 62.0 |
| `name` | String | Name of the input context. | Required | 58.0 |
| `value` | Object | Value of the input context. | Required | 58.0 |

=== ARTICLE: connect_requests_simulation_eval_service_input.htm ===
---
page_id: connect_requests_simulation_eval_service_input.htm
title: Simulation Evaluation Service Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_simulation_eval_service_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Evaluation Service Input

Input representation to run simulation on an expression
      set.

         

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

            
               

**Root XML tag**

               
: `SimulationEvalServiceInput`

            
            
               

**JSON example**

               
: 
                  

```
{
   "input":{
      "variables":[
         {
            "name":"artEstimatedValue",
            "value":"301",
            "datatype":"number"
         },
         {
            "name":"quantity",
            "value":"301",
            "datatype":"number"
         }
      ]
   },
   "contextInput":{
      "name":"PensionFunds",
      "value":{
         "PolicyDetails":[
            {
               "PolicyName":"Policy1",
               "TotalMember":"100",
               "PrincipalAmout":"500",
               "Status":"Active",
               "TotalPremium":"0"
            },
            {
               "PolicyName":"Policy2",
               "TotalMember":"200",
               "PrincipalAmout":"100",
               "Status":"Inactive",
               "TotalPremium":"0"
            },
            {
               "PolicyName":"Policy3",
               "TotalMember":"300",
               "PrincipalAmout":"400",
               "Status":"Active",
               "TotalPremium":"0"
            }
         ]
      }
   },
   "config":{
      "versionInfo":{
         "configurationVersionId":"a1o5w000002EJPPAA4",
         "effectiveDate":"2019-02-13 00:00:00"
      }
   }
}
```

               

            
            
               

**Properties**

               
: 
                  

                        
                        
                        
                        
                        
                        
                           
                              

                              

                              

                              

                              

                           

                        

                        
                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `config` | [Simulation Config Input](./connect_requests_simulation_config_input.htm.md) | Configuration details for the simulation. | Required | 53.0 |
| `contextInput` | [Simulation Context Input](./connect_requests_simulation_context_input.htm.md) | Context details for the simulation. | Required | 58.0 |
| `input` | [Simulation Variable Input[]](./connect_requests_simulation_variable_input.htm.md) | List of input variables to run the simulation. | Required | 53.0 |

=== ARTICLE: connect_requests_simulation_variable_input.htm ===
---
page_id: connect_requests_simulation_variable_input.htm
title: Simulation Variable Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_simulation_variable_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Variable Input

Input information of the input variable and its
    value.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

**Properties**

: 

- 
- 
- 
- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `datatype` | String | The data type of the variable.Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `Text` | Required | 53.0 |
| `name` | String | The name of the variable. | Required | 53.0 |
| `value` | String | The value of the variable. | Required | 53.0 |

=== ARTICLE: connect_requests_simulation_version_info_input.htm ===
---
page_id: connect_requests_simulation_version_info_input.htm
title: Simulation Version Info Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_simulation_version_info_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Version Info Input

Input information of the version details to run
    simulation.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurationVersionId` | String | The ID of the expression set version record. | Required | 53.0 |
| `effectiveDate` | String | The expression set version that's active on this date is simulated. When multiple versions are active on the effective date, the version with higher priority is executed. | Optional | 53.0 |

=== ARTICLE: connect_resources_calculation_procedure.htm ===
---
page_id: connect_resources_calculation_procedure.htm
title: Calculation Procedure
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_calculation_procedure.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure

Retrieve the details for a given expression set (also known as
      calculation procedure) record.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

          

**Resource**

          
: 
            

```
/connect/omnistudio/evaluation-services/${id}
```

          

        
        
          

**Example**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/evaluation-services/0k0x000000000BQAAY
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET

**Response body for GET**

: [Calculation Procedure Detail Output](./connect_responses_calculation_procedure_detail_output.htm.md)

=== ARTICLE: connect_resources_calculation_procedures.htm ===
---
page_id: connect_resources_calculation_procedures.htm
title: Calculation Procedures
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_calculation_procedures.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedures

Get a list of expression sets (also known as calculation procedure)
      based on a search text. The API returns a maximum of ten expression set records that contain
      the specified keyword.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

**Resource**

: 

```
/connect/omnistudio/evaluation-services
```

        
          

**Example URI**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/evaluation-services?searchKey=Expression
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET

**Request parameters for GET**

: 

| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `searchKey` | String | The user-entered search text to retrieve a list of expression sets. | Required | 53.0 |

**Response body for GET**

: [Calculation Procedure List Output](./connect_responses_calculation_procedure_list_output.htm.md)

=== ARTICLE: connect_resources_data_mapper_clear_cache.htm ===
---
page_id: connect_resources_data_mapper_clear_cache.htm
title: Data Mapper Clear Cache (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_data_mapper_clear_cache.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Clear Cache (POST)

Clear the execution cache for the specified data mappers.

    
      

#### Note

When using the Data Mapper (DM) Connect API, HTTP callouts cannot
        be executed in the same transaction. This is because these APIs perform an implicit DML
        operation through the underlying Connect API framework. If a callout is required, it must be
        executed in a separate transaction, for example by using an asynchronous mechanism such as
        @future.

      
        
          

**Resource**

          
: 
            

```
/connect/omni-global/data-mapper/actions/clear-cache
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: This is a sample example to clear the execution cache by using only the name of the
            data mapper.

: 

```
{
  "cacheStorageType": "Metadata",
  "dataMapperList": {
    "dataMappers": [
      {
        "dataMapperName": "DRWithLoad"
      }
    ]
  }
}
```

          
: This is a sample example to clear the execution cache by using the name of the data
            mapper along with additional inputs.

          
: 
            

```
{
  "cacheStorageType": "Session",
  "dataMapperList": {
    "dataMappers": [
      {
        "dataMapperName": "DRWithLoad",
        "input": {
          "Name": "Get Account Details"
        }
      }
    ]
  }
}
```

          

**Properties**

: 

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `cacheStorageType` | String | Storage type that's used for caching the data. Valid values are: `Session`—Cache is stored in the current user session. `Org`—Cache is shared across the entire organization. `All`—Refers to both session and org-level cache. | Required | 64.0 |
| `dataMapperList` | [Data Mapper Details](./connect_requests_data_mapper_details.htm.md)[] | List of data mappers to clear the cache for. | Required | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Data Mapper Cache
              Details](./connect_responses_datamapper_clear_cache_output.htm.md)

=== ARTICLE: connect_resources_data_mapper_execution.htm ===
---
page_id: connect_resources_data_mapper_execution.htm
title: Data Mapper Execution (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_data_mapper_execution.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execution (POST)

Execute a data mapper from Apex classes by specifying the name of the data mapper along
    with additional inputs and options.

    
      

#### Note

When using the Data Mapper (DM) Connect API, HTTP callouts cannot
        be executed in the same transaction. This is because these APIs perform an implicit DML
        operation through the underlying Connect API framework. If a callout is required, it must be
        executed in a separate transaction, for example by using an asynchronous mechanism such as
        @future.

      
        
          

**Resource**

          
: 
            

```
/connect/omni-global/data-mapper/execute/name
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/omni-global/data-mapper/execute/Get Account Details
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
      

      
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | Name of the data mapper. | Required | 64.0 |

          

        
      

      
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 
            

```
{
  "dataMapperInput": {
    "inputs": [
      {
        "Name": "Get Account Details"
      }
    ]
  },
  "inputType": "JSON",
  "options": {
    "ignoreCache": false
  }
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `dataMapperInput` | [Data Mapper Execute Input Data](./connect_requests_data_mapper_execute_input_data.htm.md) | Details for executing the data mapper. | Required | 64.0 |
| `inputType` | String | Type of data mapper input. For example, JSON, XML, or custom class. | Required | 64.0 |
| `options` | [Data Mapper Execution Options](./connect_requests_data_mapper_execution_options.htm.md) | Optional parameters to refine the data mapper execution. | Optional | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Data Mapper Execution
              Details](./connect_responses_data_mapper_execution_output.htm.md)

=== ARTICLE: connect_resources_decision_matrices.htm ===
---
page_id: connect_resources_decision_matrices.htm
title: Decision Matrices
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_matrices.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrices

Get a list of decision matrices ( also known as calculation matrix)
      based on a search text. The API returns a maximum of ten decision matrices records that
      contain the specified keyword.

**Resource**

: 

```
/connect/omnistudio/decision-matrices
```

        
          

**Example URI**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/decision-matrices?searchKey=Test
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET

**Request parameters for GET**

: 

| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `searchKey` | String | The user-entered search text to retrieve a list of decision matrices. |  | 53.0 |

**Response body for GET**

: [Decision Matrix Result List](./connect_responses_decision_matrix_result_list.htm.md)

=== ARTICLE: connect_resources_decision_matrix.htm ===
---
page_id: connect_resources_decision_matrix.htm
title: Decision Matrix
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_matrix.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix

Retrieve the details for a given decision matrix record (also known as
      calculation matrix).

**Resource**

: 

```
/connect/omnistudio/decision-matrices/${matrixId}
```

        
          

**Example URI**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/decision-matrices/0lIx0000000000zEAA
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET

**Response body for GET**

: [Decision Matrix Result](./connect_responses_decision_matrix_result.htm.md)

=== ARTICLE: connect_resources_decision_matrix_columns.htm ===
---
page_id: connect_resources_decision_matrix_columns.htm
title: Decision Matrix Columns
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_matrix_columns.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Columns

Retrieve a list of or manage columns in a decision matrix. Use this
      resource to add new columns, or update or delete existing columns in a decision
    matrix.

**Resource**

: 

```
/connect/omnistudio/decision-matrices/${matrixId}/columns
```

        
          

**Example**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/decision-matrices/0lIR000000000u0MAA/columns
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET, POST

        
          

**Path parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `matrixId` | String | The ID of the decision matrix record. | Required | 53.0 |

          

        

**Response body for GET**

: [Decision Matrix Columns Output](./connect_responses_decision_matrix_columns_output.htm.md)

**Request body for POST**

: 
            

**JSON example**

: 
            

Add a column:

            

```
{
   "columns" : [ {
      "apiName" : "Name",
      "columnType" : "Input",
      "dataType" : "Text",
      "displaySequence" : 4,
      "name" : "Name"
   }]
}
```

          

          
: 
            

Delete a column:

            

```
{
   "columns" : [ {
      "action" : "delete",
      "id" : "0lJR0000000014bMAA"
   }]
}
```

          

          
: 
            

Update a column:

            

```
{
   "columns" : [ {
      "id" : "0lJR0000000014hMAA",
      "action" : "update",
      "columnType" : "Input",
      "name" : "First Name"
   }]
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `columns` | [Decision Matrix Column Input](./connect_requests_decision_matrix_column.htm.md)[] | List of columns to be added, updated, or deleted in a decision matrix. | Required | 53.0 |

**Response body for POST**

: [Decision Matrix Output](./connect_responses_decision_matrix_output.htm.md)

=== ARTICLE: connect_resources_decision_matrix_version_rows.htm ===
---
page_id: connect_resources_decision_matrix_version_rows.htm
title: Decision Matrix Version Rows
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_matrix_version_rows.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Version Rows

Retrieve a paginated list of or manage rows in a decision matrix
      version. Use this resource to add new rows, or update or delete existing rows in a decision
      matrix version.

**Resource**

: 

```
/connect/omnistudio/decision-matrices/${matrixId}/versions/${versionId}/rows
```

        
          

**Example**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/decision-matrices/0lIR000000000u0MAA
/versions/0lNR000000000rFMAQ/rows
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET, POST

        
          

**Path parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `matrixId` | String | The ID of the decision matrix record. | Required | 53.0 |
| `versionId` | String | The ID of the decision matrix version record. | Required | 53.0 |

          

        
        
          

**Query parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `file` | Boolean | Indicates whether to get the rows by generating a CSV file for downloading (`true`) or fetching the rows in JSON format (`false`). The default value is `false`. | Optional | 53.0 |

          

        

**Response body for GET**

: [Decision Matrix Rows Output](./connect_responses_decision_matrix_rows_output.htm.md)

**Request body for POST**

          
: 
            
        
          

**JSON Example**

          
: 
            

Add a row:

            

```
{
  "rows": [
    {
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "2000"
      }
    }
  ]
}

```

          

          
: 
            

Delete a row:

            

```
{
  "rows": [
    {
      "id": "a1j5w000006D04uAAC",
      "action": "delete",
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "2000"
      }
    }
  ]
}

```

          

          
: 
            

Update a row:

            

```
{
  "rows": [
    {
      "id": "a1j5w000006D04uAAC",
      "action": "update",
      "rowData": {
        "Age": "45",
        "Gender": "F",
        "Premium": "1500"
      }
    }
  ]
}

```

          

          
: 
            

Add row using a CSV file:

          

          
: 
            

```
{
   "fileId" : "f1j5w000005D04uFGC"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

#### 

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fileId` | String | The ID of the [Content Document Version](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_contentversion.htm) that contains the rows details to be added or updated in a decision matrix version. | Optional Note This field is required if you’re using a CVS file to add or update rows. | 53.0 |
| `rows` | [Decision Matrix Row Input](./connect_requests_decision_matrix_row_input.htm.md)[] | List of rows to be added, updated, or deleted in a decision matrix version. | Required | 53.0 |

          

        
      

          

**Response body for POST**

: [Decision Matrix Output](./connect_responses_decision_matrix_output.htm.md)

=== ARTICLE: connect_resources_get_activate_calc_procedure_version.htm ===
---
page_id: connect_resources_get_activate_calc_procedure_version.htm
title: Calculation Procedure Version Definition (Activate, Get)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_get_activate_calc_procedure_version.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Version Definition (Activate, Get)

Retrieve the definition of an expression set (also known as
      calculation procedure) version record. Activate an expression set version
    record.

    
      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Resource**

          
: 
            

```
/connect/omnistudio/evaluation-services/version-definitions/${id}
```

          

        
        
          

**Example**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/evaluation-services/
version-definitions/0lIxx000000001dEAA
```

          

        
        
          

**Available version**

          
: 53.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, PATCH

        
        
          

**Response body for GET**

          
: [Calculation Procedure Version Definition Output](./connect_responses_calculation_procedure_version_definition_output.htm.md)

        
        
          

**Response body for PATCH**

          
: [Calculation Procedure Activation Output](./connect_responses_calculation_procedure_activation_output.htm.md)

=== ARTICLE: connect_resources_integration_procedure.htm ===
---
page_id: connect_resources_integration_procedure.htm
title: Integration Procedure Execution (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_integration_procedure.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Execution (POST)

Execute an integration procedure by using the name or ID of the integration
    procedure.

    
      

#### Note

When using the Integration Procedure (IP) Connect API, HTTP
        callouts cannot be executed in the same transaction. This is because these APIs perform an
        implicit DML operation through the underlying Connect API framework. If a callout is
        required, it must be executed in a separate transaction, for example by using an
        asynchronous mechanism such as @future.

      
        
          

**Resource**

          
: 
            

```
/connect/omni-global/integration-procedure/execute/id
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/omni-global/integration-procedure/execute/0jNxx000000005rFCC
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
      

      
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | Name or ID of the integration procedure. | Required | 64.0 |

          

        
      

      
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "input": {
    "inputs": [
      "{\"Name\": \"Get Account Details\"}"
    ]
  },
  "options": {
    "ignoreCache": false
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `input` | [Integration Procedure Service Run Input](./connect_requests_integration_procedure_service_run_input_list.htm.md) | Details to execute the integration procedure. | Required | 64.0 |
| `options` | [Integration Procedure Service Run Options](./connect_requests_integration_procedure_service_run_options.htm.md) | Optional parameters to refine the execution of the integration procedure. | Optional | 64.0 |

          

        
      

       

        
        
          

**Response body for POST**

          
: [Integration Procedure
              Execution Details](./connect_responses_integration_procedure_service_run_output.htm.md)

=== ARTICLE: connect_resources_integration_procedure_clear_cache.htm ===
---
page_id: connect_resources_integration_procedure_clear_cache.htm
title: Integration Procedure Clear Cache (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_integration_procedure_clear_cache.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Clear Cache (POST)

Clear the execution cache for the specified integration procedures.

    
      

#### Note

When using the Integration Procedure (IP) Connect API, HTTP
        callouts cannot be executed in the same transaction. This is because these APIs perform an
        implicit DML operation through the underlying Connect API framework. If a callout is
        required, it must be executed in a separate transaction, for example by using an
        asynchronous mechanism such as @future.

      
        
          

**Resource**

          
: 
            

```
/connect/omni-global/integration-procedure/actions/clear-cache
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: This is a sample example to clear the cache of an integration procedure by using the
            key that's associated with the integration procedure and cache storage type.

          
: 
            

```
{
  "cacheStorageType": "Metadata",
  "ipInput": {
    "inputs": [
      {
        "ipkey": "Account_GetAccountDetails"
      }
    ]
  }
}
```

          

          
: This is a sample example to clear the cache of an integration procedure by using the
            cache keys and cache storage type.

: 

```
{
  "cacheKeys": {
    "cacheKeys": [
      "IP06535636"
    ]
  },
  "cacheStorageType": "Metadata"
}
```

**Properties**

: 

- 
- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `cacheKeys` | [Integration Procedure Cache Keys](./connect_requests_integration_procedure_cache_keys_list.htm.md) | List of cache keys to clear the cache for. Cache keys are used to identify the cached data. | Optional | 64.0 |
| `cacheStorageType` | String | Storage type that's used for caching the data. Valid values are: `All`—Includes all cache types, such as metadata, session, and org-level caches. `Metadata`—Cache is used for configuration-related data such as schemas or field mappings. `Org`—Cache is shared across the entire organization. `Session`—Cache is stored in the current user session. | Required | 64.0 |
| `iPInput` | [Integration Procedure Details](./connect_requests_integration_procedure_cache_input_data.htm.md)[] | List of integration procedures to clear the cache for. | Optional | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Integration Procedure
              Cache Details](./connect_responses_integration_procedure_cache_output.htm.md)

=== ARTICLE: connect_resources_save_update_calc_procedure_version.htm ===
---
page_id: connect_resources_save_update_calc_procedure_version.htm
title: Calculation Procedure Version Definition (Save As, Update)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_save_update_calc_procedure_version.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Version Definition (Save As, Update)

Update the details of an expression set (also known as calculation
      procedure) version record. Save an expression set version record as a new expression set
      version record.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

        
          

**Resource**

          
: 
            

```
/connect/omnistudio/evaluation-services/version-definitions
```

          

        
        
          

**Available version**

          
: 53.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 
                  

Specify the version record ID or `CLONE` in
                     the `versionId` field to either update an
                     existing expression set version record or save the expression set version
                     record as a new expression set version record.

                  

```
{
   "calculationProcedureId":"0k0xx00000000HlAAI",
   "code":"200",
   "constants":{
      "details":[ {
         "apiName":"SENIOR_CITIZEN_AGE",
         "dataType":"Number",
         "defaultValue":"60",
         "isEditable":true,
         "isUserDefined":true,
         "name":"SENIOR_CITIZEN_AGE",
         "precision":2
      }.]
   },
   "enabled":false,
   "isSuccess":true,
   "message":"",
   "name":"rule3 V1",
   "rank":1,
   "root":{
      "steps":[
         "0mqxx00000000UfAAI"
      ]
   },
   "startDate":"2021-08-04T08:57:23.000Z",
   "step":{
      "details":{
         "0mqxx00000000UfAAI":{
            "childStepIds":[],
            "conditionsExpressionText":"age == SENIOR_CITIZEN_AGE",
            "conditionsUiFormattedText":"{\"bypass\":[]}",
            "id":"0mqxx00000000UfAAI",
            "inputVariablesFormatText":"[{\"name\":\"age\",\"dataType\":\"Number\",\"alias\":\"age\"}]",
            "isResultIncluded":false,
            "name":"Condition",
            "outputVariablesFormatText":"{\"name\":\"condition_output__1\",\"dataType\":\"Boolean\",\"alias\":\"condition_output__1\"}",
            "outputVariablesMappingText":"{\"condition_output__1\":\"condition_output__1\"}",
            "returnMessageValueSet":"{\"true\":\"\",\"false\":\"\"}",
            "stage":"Calculation",
            "stepType":"Condition"
         }
      }
   },
   "variables":{
      "details":[ {
         "apiName":"condition_output__1",
         "dataType":"Boolean",
         "defaultValue":"False",
         "id":"0kJxx00000000KzEAI",
         "isEditable":false,
         "isUserDefined":false,
         "name":"condition_output__1"
      }, {
         "apiName":"age",
         "dataType":"Number",
         "defaultValue":"60",
         "id":"0kJxx00000000L0EAI",
         "isEditable":true,
         "isUserDefined":true,
         "name":"age",
         "precision":2
      } ]
   },
   "versionId":"0k1xx00000000KzAAI",
   "versionNumber":1
}
```

               

**Properties**

: 

#### 

                              

                              

                              

                              

                              

                           

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `calculationProcedureId` | String | The ID of the expression-set record that you want to update the definition details for or save as a new version definition record. | Optional | 53.0 |
| `constants` | [Calculation Procedure Resource](./connect_requests_resource_input.htm.md)[] | The constant values passed in the expression set version record. | Optional | 53.0 |
| `description` | String | The description of the expression set version record. | Optional | 53.0 |
| `enabled` | Boolean | Indicates whether the expression set version record is active (`true`) for execution or not (`false`). The default is `false`. Note This field must be false with the update or save as request. | Optional | 53.0 |
| `endDate` | String | The date and time until when an active expression set version record is in effect. | Optional | 53.0 |
| `name` | String | The name of the expression set version record. | Optional | 53.0 |
| `rank` | Integer | The rank of the expression set version record. When multiple records are in effect, the record that’s ranked higher takes precedence. | Optional | 53.0 |
| `root` | String[] | The first steps defined in the expression set version record. | Optional | 53.0 |
| `startDate` | String | The start date and time from when an active expression set version record is in effect. | Optional | 53.0 |
| `step` | Map<String, [Calculation Procedure Step Input](./connect_requests_calculation_procedure_step_input.htm.md)> | The list of steps defined in the expression set version record. | Optional | 53.0 |
| `variables` | [Calculation Procedure Resource](./connect_requests_resource_input.htm.md)[] | The variable values passed in the expression set version record. | Optional | 53.0 |
| `versionId` | String | The ID of the expression set version record. | Required | 53.0 |
| `versionNumber` | Integer | The version number of the expression set record. | Optional | 53.0 |

          

        
        
          

**Response body for POST**

          
: [Calculation Procedure Version Definition Output](./connect_responses_calculation_procedure_version_definition_output.htm.md)

=== ARTICLE: connect_resources_simulations.htm ===
---
page_id: connect_resources_simulations.htm
title: Simulations
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_simulations.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulations

Retrieve the input variables of an expression set that are required to
      run a simulation. Run a simulation. An expression set, also known as calculation
    procedure, is a group of steps that perform mathematical operations and
    transformations.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

**Resource**

: 

```
/connect/omnistudio/evaluation-services/version-definitions/${id}/simulation
```

        
          

**Example URI for GET**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/evaluation-services/version-definitions/a1o5w000002EJPPAA4/simulation
```

          

        
        
          

**Example URI for PATCH**

          
: 
            

```
/services/data/v53.0/connect/omnistudio/evaluation-services/version-definitions/a1o5w000002EJPPAA4/simulation
```

          

        

**Available version**

: 53.0

**Requires Chatter**

: No

**HTTP methods**

: GET, PATCH

        
          

**Query parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputVariables` | Boolean | Reserved for future use. | Optional | 53.0 |

          

        

**Response body for GET**

: [Simulation Input Variables Result List](./connect_responses_simulation_input_variables_result_list.htm.md)

**Request body for PATCH**

: 
            
            
               

**Root XML tag**

               
: `SimulationEvalServiceInput`

            
            
               

**JSON example**

               
: 
                  

```
{
   "input":{
      "variables":[
         {
            "name":"artEstimatedValue",
            "value":"301",
            "datatype":"number"
         },
         {
            "name":"quantity",
            "value":"301",
            "datatype":"number"
         }
      ]
   },
   "contextInput":{
      "name":"PensionFunds",
      "value":{
         "PolicyDetails":[
            {
               "PolicyName":"Policy1",
               "TotalMember":"100",
               "PrincipalAmout":"500",
               "Status":"Active",
               "TotalPremium":"0"
            },
            {
               "PolicyName":"Policy2",
               "TotalMember":"200",
               "PrincipalAmout":"100",
               "Status":"Inactive",
               "TotalPremium":"0"
            },
            {
               "PolicyName":"Policy3",
               "TotalMember":"300",
               "PrincipalAmout":"400",
               "Status":"Active",
               "TotalPremium":"0"
            }
         ]
      }
   },
   "config":{
      "versionInfo":{
         "configurationVersionId":"a1o5w000002EJPPAA4",
         "effectiveDate":"2019-02-13 00:00:00"
      }
   }
}
```

               

            
            
               

**Properties**

               
: 
                  

                        
                        
                        
                        
                        
                        
                           
                              

                              

                              

                              

                              

                           

                        

                        
                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `config` | [Simulation Config Input](./connect_requests_simulation_config_input.htm.md) | Configuration details for the simulation. | Required | 53.0 |
| `contextInput` | [Simulation Context Input](./connect_requests_simulation_context_input.htm.md) | Context details for the simulation. | Required | 58.0 |
| `input` | [Simulation Variable Input[]](./connect_requests_simulation_variable_input.htm.md) | List of input variables to run the simulation. | Required | 53.0 |

               

            
         

**Response body for PATCH**

: [Simulation Eval
              Service Output](./connect_responses_simulation_eval_service_output.htm.md)

=== ARTICLE: connect_responses_calculation_procedure_activation_output.htm ===
---
page_id: connect_responses_calculation_procedure_activation_output.htm
title: Calculation Procedure Activation Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_activation_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Activation Output

Output representation of the calculation procedure version record
      activation.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**JSON Response**

          
: 
            

```
{
   "code":"200",
   "isSuccess":true,
   "message":"Expression Set Version Activated",
   "versionId":"0k1xx00000000KzAAI"
}
```

          

        
      

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `versionId` | String | The ID of the activated calculation procedure version record. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_detail_output.htm ===
---
page_id: connect_responses_calculation_procedure_detail_output.htm
title: Calculation Procedure Detail Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_detail_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Detail Output

Output representation of the expression set details.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Response**

          
: 
            

```
{
   "code" : "200",
   "id" : "0k0x000000000BQAAY",
   "inputVariables" : [ {
      "dataType" : "Number",
      "name" : "var1"
   } ],
   "isSuccess" : true,
   "message" : "",
   "name" : "RuleWith100Conditions42",
   "outputVariables" : [ {
      "dataType" : "Number",
      "name" : "var2"
   } ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `description` | String | The description of the expression set. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the expression set record. | Small, 53.0 | 53.0 |
| `inputVariables` | [Calculation Procedure Variable Output[]](./connect_responses_calculation_procedure_variable_output.htm.md) | The list of input variables of the expression set. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `name` | String | The name of the expression set. | Small, 53.0 | 53.0 |
| `outputVariables` | [Calculation Procedure Variable Output[]](./connect_responses_calculation_procedure_variable_output.htm.md) | The list of output variables of the expression set. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_list_output.htm ===
---
page_id: connect_responses_calculation_procedure_list_output.htm
title: Calculation Procedure List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_list_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure List Output

Output representation of the expression set result
    list.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Response**

          
: 
            

```
{
   "calculationProcedures" : [ {
      "id" : "0k0x0000000008ZAAQ",
      "description" : "Test calculation set",
      "name" : "Expression_Set_1"
   },{
      "id" : "0k0x000000000BQAAY",
      "description" : "Test procedure set",
      "name" : "Expression_Set_2"
   } ],
   "code" : "200",
   "isSuccess" : true,
   "message" : ""
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `calculationProcedures` | [Calculation Procedure Output[]](./connect_responses_calculation_procedure_output.htm.md) | The list of the expression sets. | Small, 53.0 | 53.0 |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `success` | Boolean | Indicates whether the request was successful. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_output.htm ===
---
page_id: connect_responses_calculation_procedure_output.htm
title: Calculation Procedure Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Output

Output representation of the expression sets details.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Response**

          
: 
            

```
{
   "calculationProcedures" : [ {
      "id" : "0k0x0000000008ZAAQ",
      "description" : "Test calculation set",
      "name" : "Expression_Set_1"
   }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | The description of the expression set. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the expression set record. | Small, 53.0 | 53.0 |
| `name` | String | The name of the expression set. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_step_map_output.htm ===
---
page_id: connect_responses_calculation_procedure_step_map_output.htm
title: Calculation Procedure Step Map Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_step_map_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Step Map Output

Output representation of the step details of the expression set
      version record.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `details` | Map<String, [Calculation Procedure Step Output](./connect_responses_calculation_procedure_step_output.htm.md)> | The list that contains the step details of the expression set version record. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_step_output.htm ===
---
page_id: connect_responses_calculation_procedure_step_output.htm
title: Calculation Procedure Step Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Step Output

Output representation of the steps of the expression set version
      record.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

#### 

              

              

            

            
              

              

              

#### 

              

              

            

            
              

              

              
- 
- 
- 
- 
- 
- 

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `calculation​MatrixId` | String | The ID of the decision matrix record. | Small, 53.0 | 53.0 |
| `childStep​Ids` | String[] | The IDs of the child steps in the parent expression set version record step. | Small, 53.0 | 53.0 |
| `conditions​ExpressionText` | String | User-defined expression text used in a condition step. | Small, 53.0 | 53.0 |
| `conditionsUi​FormattedText` | String | Additional information required to render the condition expression text. For example, when the current step has a subset of `childStepIds` that is marked to bypass. The code `"conditionsUiFormattedText":"{\"bypass\":[\"0mqx000000000f6AAA\"]}"` specified in this field enables navigation outside the branch. | Small, 53.0 | 53.0 |
| `description` | String | The description of the expression set version record step. | Small, 53.0 | 53.0 |
| `failed​Explainer​TemplateId` | String | ID of the failed explainability message template in the Decision Table lookup procedure step. | Small, 56.0 | 56.0 |
| `failed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the failed explainability message template. | Small, 59.0 | 59.0 |
| `formula​Expression​Text` | String | The formula used in a calculation step. | Small, 53.0 | 53.0 |
| `formulaUi​FormattedText` | String | Reserved for future use. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the expression set version record step. | Small, 53.0 | 53.0 |
| `inputVariables​FormatText` | String | The input variables in JSON format required to execute an expression set version record step. | Small, 53.0 | 53.0 |
| `isResult​Included` | Boolean | Indicates whether the result of a step execution is returned to the user. The default is `false`. | Small, 53.0 | 53.0 |
| `name` | String | The name of the expression set version record step. | Small, 53.0 | 53.0 |
| `noResult​Explainer​TemplateId` | String | ID of the no result explainability message template in the Decision Table lookup procedure step. | Small, 59.0 | 59.0 |
| `noResult​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the no result explainability message template. | Small, 59.0 | 59.0 |
| `output​Variables​FormatText` | String | The output variables in JSON format returned by an expression set version record step. | Small, 53.0 | 53.0 |
| `output​Variables​MappingText` | String | The mapping between the output variable of a step and the input variable for a sub-calculation procedure version record or a sub-decision matrix record. | Small, 53.0 | 53.0 |
| `passed​Explainer​TemplateId` | String | ID of the passed explainability message template in the Decision Table lookup procedure step. | Small, 56.0 | 56.0 |
| `passed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the passed explainability message template. | Small, 59.0 | 59.0 |
| `reference​Calculation​ProcedureId` | String | The ID of the sub-calculation procedure version record. | Small, 53.0 | 53.0 |
| `return​Message​ValueSet` | String | User-configured messages for the result of the current step. Note This field is applicable when the step type is `Condition`. | Small, 53.0 | 53.0 |
| `stage` | String | Indicates whether the expression set version step is a calculation or an aggregation. Note In version 53.0 and later, only calculation is supported. | Small, 53.0 | 53.0 |
| `stepType` | String | Indicates whether the expression set version step type is mathematical or lookup. Possible values are: Condition Calculation MatrixLookup ReferenceProcedure Branch ConditionalGroup | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_variable_output.htm ===
---
page_id: connect_responses_calculation_procedure_variable_output.htm
title: Calculation Procedure Variable Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_variable_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Variable Output

Details of the variables of an expression set.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Response**

          
: 
            

```
{
      "dataType" : "Number",
      "name" : "var2"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dataType` | String | The data type of the variable. | Small, 53.0 | 53.0 |
| `name` | String | The name of the variable. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_calculation_procedure_version_definition_output.htm ===
---
page_id: connect_responses_calculation_procedure_version_definition_output.htm
title: Calculation Procedure Version Definition Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_calculation_procedure_version_definition_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Calculation Procedure Version Definition Output

Output representation of the expression set version
    definition.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**JSON Response**

          
: 
            

```
{
   "calculationProcedureId":"0k0xx00000000HlAAI",
   "code":"200",
   "constants":{
      "details":[
         {
            "apiName":"SENIOR_CITIZEN_AGE",
            "dataType":"Number",
            "defaultValue":"60",
            "isEditable":true,
            "isUserDefined":true,
            "name":"SENIOR_CITIZEN_AGE",
            "precision":2
         }
      ]
   },
   "enabled":false,
   "isSuccess":true,
   "message":"",
   "name":"rule3 V1",
   "rank":1,
   "root":{
      "steps":[
         "0mqxx00000000UfAAI"
      ]
   },
   "startDate":"2021-08-04T08:57:23.000Z",
   "step":{
      "details":{
         "0mqxx00000000UfAAI":{
            "childStepIds":[
            ],
            "conditionsExpressionText":"age == SENIOR_CITIZEN_AGE",
            "conditionsUiFormattedText":"{\"bypass\":[]}",
            "id":"0mqxx00000000UfAAI",
            "inputVariablesFormatText":"[{\"name\":\"age\",\"dataType\":\"Number\",\"alias\":\"age\"}]",
            "isResultIncluded":false,
            "name":"Condition",
            "outputVariablesFormatText":"{\"name\":\"condition_output__1\",\"dataType\":\"Boolean\",\"alias\":\"condition_output__1\"}",
            "outputVariablesMappingText":"{\"condition_output__1\":\"condition_output__1\"}",
            "returnMessageValueSet":"{\"true\":\"\",\"false\":\"\"}",
            "stage":"Calculation",
            "stepType":"Condition"
         }
      }
   },
   "variables":{
      "details":[
         {
            "apiName":"condition_output__1",
            "dataType":"Boolean",
            "defaultValue":"False",
            "id":"0kJxx00000000KzEAI",
            "isEditable":false,
            "isUserDefined":false,
            "name":"condition_output__1"
         },
         {
            "apiName":"age",
            "dataType":"Number",
            "defaultValue":"60",
            "id":"0kJxx00000000L0EAI",
            "isEditable":true,
            "isUserDefined":true,
            "name":"age",
            "precision":2
         }
      ]
   },
   "versionId":"0k1xx00000000KzAAI",
   "versionNumber":1
}
```

          

        
      

              

              

              

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `calculationProcedureId` | String | The ID of the expression set record. | Small, 53.0 | 53.0 |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `constants` | [Resource List Output](./connect_responses_resource_list_output.htm.md) | The constant definition of the expression set version record. | Small, 53.0 | 53.0 |
| `description` | String | The description of the expression set version record. | Small, 53.0 | 53.0 |
| `enabled` | Boolean | Indicates whether the expression set version record is active for execution. The default is `false`. | Small, 53.0 | 53.0 |
| `endDate` | String | The date and time until when an active expression set version record is in effect. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `name` | String | The name of the expression set version record. | Small, 53.0 | 53.0 |
| `rank` | Integer | The rank of the expression set version record. When multiple records are in effect, the record that’s ranked higher takes precedence. 1 denotes the highest rank. | Small, 53.0 | 53.0 |
| `root` | [Root Step List Output](./connect_responses_root_step_list_output.htm.md) | The first step defined in the expression set version record. If the first step is a branch, then the first steps in the record. | Small, 53.0 | 53.0 |
| `startDate` | String | The start date and time from when an active expression set version record is in effect. | Small, 53.0 | 53.0 |
| `step` | [Calculation Procedure Step Map Output](./connect_responses_calculation_procedure_step_map_output.htm.md) | The list of steps defined in the expression set version record. | Small, 53.0 | 53.0 |
| `variables` | [Resource List Output](./connect_responses_resource_list_output.htm.md) | The variable definition of the expression set version record. | Small, 53.0 | 53.0 |
| `versionId` | String | The ID of the expression set version record. | Small, 53.0 | 53.0 |
| `versionNumber` | Integer | The number of the expression set version record. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_data_mapper_execution_output.htm ===
---
page_id: connect_responses_data_mapper_execution_output.htm
title: Data Mapper Execution Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_data_mapper_execution_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execution Details

Output representation of the execution details of a data mapper.

        
          

**JSON example**

          
: 
            

```
{
  "response": [
    {
      "error": "Specify a Data Mapper name",
      "response": [
        {
          "status": false
        }
      ],
      "responseType": "JSON"
    }
  ],
  "status": "Success"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              
- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the execution fails. | Small, 64.0 | 64.0 |
| `response` | [Data Mapper Execution Response](./connect_responses_data_mapper_execution_response_output.htm.md) [] | List of responses corresponding to the custom inputs that are provided during the data mapper execution. | Small, 64.0 | 64.0 |
| `status` | String | Execution status of the data mapper. Valid values are: `Error`—Data mapper execution has failed due to an error. `Success`—Data mapper execution is successful. | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_data_mapper_execution_response_output.htm ===
---
page_id: connect_responses_data_mapper_execution_response_output.htm
title: Data Mapper Execution Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_data_mapper_execution_response_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Execution Response

Output representation of the response with error message, status, and response
    type.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "response": [
    {
      "error": "Specify a Data Mapper name",
      "response": [
        {
          "status": false
        }
      ],
      "responseType": "JSON"
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the execution fails for the input. | Small, 64.0 | 64.0 |
| `response` | String | Execution response corresponding to the custom input in JSON format. | Small, 64.0 | 64.0 |
| `responseType` | String | Format of the execution response, such as JSON, XML, or a custom class. | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_datamapper_clear_cache_output.htm ===
---
page_id: connect_responses_datamapper_clear_cache_output.htm
title: Data Mapper Cache Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_datamapper_clear_cache_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Cache Details

Output representation of the cache details that are cleared for the specified data
    mappers.

      
        
          

**JSON example**

          
: 
            

```
{
  "error": "Specify a Data Mapper name",
  "responseList": [
    {
      "error": "Specify a Data Mapper name",
      "status": false
    }
  ],
  "status": false
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the operation fails. | Small, 64.0 | 64.0 |
| `responseList` | [Data Mapper Clear Cache Response](./connect_responses_datamapper_clear_cache_response.htm.md)[] | List of responses that are generated during the clear cache process. | Small, 64.0 | 64.0 |
| `status` | Boolean | Indicates whether the cache is cleared successfully (`true`) or not (`false`). | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_datamapper_clear_cache_response.htm ===
---
page_id: connect_responses_datamapper_clear_cache_response.htm
title: Data Mapper Cache Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_datamapper_clear_cache_response.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper Cache Response

Output representation of the response with error message and status.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "responseList": [
    {
      "status": true
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the operation fails. | Small, 64.0 | 64.0 |
| `status` | Boolean | Indicates whether the cache is cleared successfully (`true`) or not (`false`). | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_decision_matrix_basic.htm ===
---
page_id: connect_responses_decision_matrix_basic.htm
title: Decision Matrix Basic
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_basic.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Basic

Output representation of the decision matrices
    details.

      
        
          

**Sample Response**

          
: 
            

```
{
   "decisionMatrices" : [ {
      "id" : "0lIx0000000001TEAQ",
      "name" : "Decision_Matrix_Test1"
   } ],
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | The description of the decision matrix. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the decision matrix record. | Small, 53.0 | 53.0 |
| `name` | String | The name of the decision matrix. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_column_output.htm ===
---
page_id: connect_responses_decision_matrix_column_output.htm
title: Decision Matrix Column Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_column_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Column Output

Representation of the details of a column in a decision
    matrix.

              

              

              

              

              

            

              

              

              

              

              

            

              

              

              
              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | The API name of a column. | Small, 53.0 | 53.0 |
| `columnType` | String | The type of column. | Small, 53.0 | 53.0 |
| `dataType` | String | The data type of a column. | Small, 53.0 | 53.0 |
| `displaySequence` | Integer | The display sequence of a column. | Small, 53.0 | 53.0 |
| `id` | String | The ID of a column. | Small, 53.0 | 53.0 |
| `name` | String | The name of a column. | Small, 53.0 | 53.0 |
| `rangeValues` | String | The range value of a column. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_columns_output.htm ===
---
page_id: connect_responses_decision_matrix_columns_output.htm
title: Decision Matrix Columns Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_columns_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Columns Output

Output representation of columns of a decision
    matrix.

      
        
          

**JSON example**

          
: 
            

```
{
   "columns" : [ {
      "apiName" : “Age”,
      "columnType" : "Input",
      "dataType" : "Number",
      "displaySequence" : 1,
      "id" : "0lJR0000000014aMAA",
      "name" : “Age”,
      "rangeValues" : null
   }, {
      "apiName" : “Gender”,
      "columnType" : "Input",
      "dataType" : "Text",
      "displaySequence" : 2,
      "id" : "0lJR0000000014bMAA",
      "name" : “Gender”,
      "rangeValues" : null
   }, {
      "apiName" : “Premium”,
      "columnType" : "Output",
      "dataType" : "Number",
      "displaySequence" : 3,
      "id" : "0lJR0000000014fMAA",
      "name" : "Premium",
      "rangeValues" : null
   } ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `columns` | [Decision Matrix Column Output](./connect_responses_decision_matrix_column_output.htm.md)[] | The list of columns in a decision matrix. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_output.htm ===
---
page_id: connect_responses_decision_matrix_output.htm
title: Decision Matrix Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Output

Output representation the action performed on a decision matrix
      version.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorFileId` | String | The ID of the error file containing failed records. | Small, 53.0 | 53.0 |
| `errors` | String[] | The request response error. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `success` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_result.htm ===
---
page_id: connect_responses_decision_matrix_result.htm
title: Decision Matrix Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Result

Output representation of the decision matrix details.

      
        
          

**Sample Response**

          
: 
            

```
{
   "code" : "200",
   "id" : "0lIx0000000000zEAA",
   "inputVariables" : [ {
      "dataType" : "Number",
      "id" : "0lJx0000000000zEAA",
      "name" : "IN1"
   }, {
      "dataType" : "Text",
      "id" : "0lJx00000000010EAA",
      "name" : "IN2"
   }, {
      "dataType" : "Text",
      "id" : "0lJx00000000011EAA",
      "name" : "IN3"
   }, {
      "dataType" : "Text",
      "id" : "0lJx00000000012EAA",
      "name" : "IN4"
   } ],
   "isSuccess" : true,
   "message" : "",
   "name" : "DescisionMatrix2",
   "outputVariables" : [ {
      "dataType" : "Text",
      "id" : "0lJx00000000013EAA",
      "name" : "OUT1"
   }, {
      "dataType" : "Text",
      "id" : "0lJx00000000014EAA",
      "name" : "OUT2"
   } ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `description` | String | The description of the decision matrix. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the decision matrix record. | Small, 53.0 | 53.0 |
| `inputVariables` | [Decision Matrix Variable[]](./connect_responses_decision_matrix_variable.htm.md) | The list of input variables of the decision matrix. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |
| `name` | String | The name of the decision matrix. | Small, 53.0 | 53.0 |
| `outputVariables` | [Decision Matrix Variable[]](./connect_responses_decision_matrix_variable.htm.md) | The list of output variables of the decision matrix. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_result_list.htm ===
---
page_id: connect_responses_decision_matrix_result_list.htm
title: Decision Matrix Result List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_result_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Result List

Output representation of the decision matrix result
    list.

      
        
          

**Sample Response**

          
: 
            

```
{
   "code" : "200",
   "decisionMatrices" : [ {
      "id" : "0lIx0000000001TEAQ",
      "name" : "Decision_Matrix_Test1"
   }, {
      "id" : "0lIx0000000000pEAA",
      "name" : "Decision_Matrix_Test2”
   }, {
      "id" : "0lIx0000000001OEAQ",
      "name" : "Decision_Matrix_Test3”
   } ],
   "isSuccess" : true,
   "message" : ""
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `decisionMatrices` | [Decision Matrix Basic[]](./connect_responses_decision_matrix_basic.htm.md) | The list of the decision matrices. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request was successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_row_output.htm ===
---
page_id: connect_responses_decision_matrix_row_output.htm
title: Decision Matrix Row Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_row_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Row Output

Representation of the details of a row in a decision matrix
      version.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | The ID of the row in a decision matrix version. | Small, 53.0 | 53.0 |
| `name` | String | The name of the row. | Small, 53.0 | 53.0 |
| `rowData` | Map<String, Object> | The key value pair of the row. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_rows_output.htm ===
---
page_id: connect_responses_decision_matrix_rows_output.htm
title: Decision Matrix Rows Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_rows_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Rows Output

Output representation of rows of a decision matrix
    version.

      
        
          

**JSON example**

          
: 
            

```

   "message" : null,
   "rows" : [ {
      "id" : "a1j5w000005D04uAAC",
      "name" : "303b5c8988601647873b4ffd247d83cb",
      "rowData" : {
         "Age" : 45,
         "Gender" : "F",
         "Premium" : 2000
      }
   } ],
   "totalRows" : 1
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | The error message in case of failure. | Small, 53.0 | 53.0 |
| `rows` | [Decision Matrix Row Output](./connect_responses_decision_matrix_row_output.htm.md)[] | The list of rows in a decision matrix version. | Small, 53.0 | 53.0 |
| `totalRows` | Integer | The total count of rows retrieved. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_decision_matrix_variable.htm ===
---
page_id: connect_responses_decision_matrix_variable.htm
title: Decision Matrix Variable
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_variable.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses_1.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Variable

Details of the input or output variables of a decision
    matrix.

      
        
          

**Sample Response**

          
: 
            

```
{
      "dataType" : "Text",
      "id" : "0lJx00000000010EAA",
      "name" : "IN2"
   }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dataType` | String | The data type of the variable. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the variable record. | Small, 53.0 | 53.0 |
| `name` | String | The name of the variable. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_integration_procedure_cache_output.htm ===
---
page_id: connect_responses_integration_procedure_cache_output.htm
title: Integration Procedure Cache Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_integration_procedure_cache_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Cache Details

Output representation of the cache that are cleared for the specified integration
    procedures.

      
        
          

**JSON example**

          
: 
            

```
{
  "error": "Specify a valid cache key.",
  "response": [
    {
      "status": false
    }
  ],
  "status": "Error"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the operation fails. | Small, 64.0 | 64.0 |
| `responseList` | [Integration Procedure Cache Response](./connect_responses_integration_procedure_cache_response.htm.md)[] | List of responses that are generated during the cache clearing process where each response corresponds to a specific cache key. | Small, 64.0 | 64.0 |
| `status` | Boolean | Indicates whether the cache is cleared successfully (`true`) or not (`false`) | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_integration_procedure_cache_response.htm ===
---
page_id: connect_responses_integration_procedure_cache_response.htm
title: Integration Procedure Cache Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_integration_procedure_cache_response.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Cache Response

Output representation of the response with error message and status.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "error": "Specify a valid cache key",
  "status": false
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the operation fails. | Small, 64.0 | 64.0 |
| `status` | Boolean | Indicates whether the cache is cleared successfully (`true`) or not (`false`). | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_integration_procedure_service_run_output.htm ===
---
page_id: connect_responses_integration_procedure_service_run_output.htm
title: Integration Procedure Execution Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_integration_procedure_service_run_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure Execution Details

Output representation of the execution details of the integration procedure.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "error": "Specify a valid IP name.",
  "response": [
    {
      "status": false
    }
  ],
  "status": "Error"
}
```

          

        
      

    

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | Error message if the execution of the integration procedure fails. | Small, 64.0 | 64.0 |
| `response` | String[] | List of responses for the execution of the integration procedures. | Small, 64.0 | 64.0 |
| `status` | String | Execution status of the integration procedure. Valid values are: `Error`—Execution has failed due to an error. `Success`—Execution is successful. | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_resource_list_output.htm ===
---
page_id: connect_responses_resource_list_output.htm
title: Resource List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_resource_list_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resource List Output

Output representation of the expression set version record resource
      list.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `details` | [Resource Output []](./connect_responses_resource_output.htm.md) | The constant or variable values passed to the expression set version record. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_resource_output.htm ===
---
page_id: connect_responses_resource_output.htm
title: Resource Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_resource_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resource Output

Output representation of variables or constants used in the
      calculation procedure version definition.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | The API name of the variable or constant. | Small, 53.0 | 53.0 |
| `calculationMatrixName` | String | The name of the decision matrix record used in the variable or constant. | Small, 53.0 | 53.0 |
| `dataType` | String | The data type of the variable or constant. | Small, 53.0 | 53.0 |
| `defaultValue` | String | The default value of the variable or constant. | Small, 53.0 | 53.0 |
| `displayName` | String | The display name of the variable or constant. | Small, 53.0 | 53.0 |
| `id` | String | The ID of the variable or constant. | Small, 53.0 | 53.0 |
| `isEditable` | Boolean | Indicates whether the variable or constant is editable. | Small, 53.0 | 53.0 |
| `isUserDefined` | Boolean | Indicates whether the variable or constant is user-defined. | Small, 53.0 | 53.0 |
| `name` | String | The name of the variable or constant. | Small, 53.0 | 53.0 |
| `precision` | Integer | The floating-point precision of the variable or constant. The value ranges from 0 to 16. | Small, 53.0 | 53.0 |
| `uiDisplayOrder` | Integer | Reserved for future use. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_root_step_list_output.htm ===
---
page_id: connect_responses_root_step_list_output.htm
title: Root Step List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_root_step_list_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Root Step List Output

Output representation of the first step of the expression set version
      record.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `steps` | String[] | The first step defined in the calculation procedure version record. If the first step is a branch, then the first steps in the record. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_error_output.htm ===
---
page_id: connect_responses_simulation_error_output.htm
title: Simulation Error Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_error_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Error Output

Error code and details.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code. | Small, 53.0 | 53.0 |
| `errorDetails` | String | The details of the error. | Small, 53.0 | 53.0 |
| `errorMsg` | String | The message stating the reason for error. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_eval_service_output.htm ===
---
page_id: connect_responses_simulation_eval_service_output.htm
title: Simulation Eval Service Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_eval_service_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Eval Service Output

Output representation of the simulation run on an expression
      set.

         

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Responses**

          
: 
                  

This is an example of a simulation run pass.

                  

```
{
   "executionId":"9QMRN00000004Sn4AI_20230112_091636_a091001d",
   "output":{
      "aggregationResults":{
         
      },
      "calculationResults":[
         {
            "res":25.00
         }
      ]
   },
   "simulationResults":[
      {
         "datatype":"Number",
         "name":"var1",
         "precision":2,
         "value":"25.00"
      },
      {
         "contextValue":{
            "PolicyDetails":[
               {
                  "PolicyName":"Policy1",
                  "TotalMember":"100",
                  "PrincipalAmout":"500",
                  "Status":"Active",
                  "TotalPremium":"1500"
               },
               {
                  "PolicyName":"Policy2",
                  "TotalMember":"200",
                  "PrincipalAmout":"100",
                  "Status":"Inactive",
                  "TotalPremium":"0"
               },
               {
                  "PolicyName":"Policy3",
                  "TotalMember":"300",
                  "PrincipalAmout":"400",
                  "Status":"Active",
                  "TotalPremium":"300"
               }
            ]
         },
         "datatype":"Context",
         "name":"PensionFunds",
         "precision":"",
         "value":""
      }
   ],
   "simulationStepResults":{
      "ListFilter":{
         "isDefaulted":false,
         "stepErrors":{
            
         },
         "stepInputs":[
            {
               "name":"PrincipalAmount",
               "contextValue":[
                  "500",
                  "100",
                  "400"
               ],
               "dataType":"Number",
               "value":""
            },
            {
               "name":"PolicyName",
               "contextValue":[
                  "Policy1",
                  "Policy2",
                  "Policy3"
               ],
               "dataType":"Text",
               "value":""
            },
            {
               "name":"TotalMembers",
               "contextValue":[
                  "100",
                  "200",
                  "300"
               ],
               "dataType":"Number",
               "value":""
            },
            {
               "name":"Status",
               "contextValue":[
                  "true",
                  "true",
                  "false"
               ],
               "dataType":"Boolean",
               "value":""
            }
         ]
      },
      "stepResults":[
         {
            "datatype":"Number",
            "name":"filter_output_total_items",
            "value":"3"
         },
         {
            "datatype":"Number",
            "name":"filter_output_filtered_items",
            "value":"2"
         },
         {
            "name":"filter_output",
            "datatype":"Boolean",
            "contextValue":[
               true,
               false,
               true
            ],
            "value":""
         }
      ]
   },
   "Calculation":{
      "explainabilityMessage":{
         "message":"Pass calculation msg",
         "showConditionDetails":false,
         "showOnlyExecutedPathMessage":true,
         "templateId":"8U8D20000004C9DKAU"
      },
      "isDefaulted":false,
      "stepErrors":{
         
      },
      "stepInputs":[
         {
            "name":"PrincipalAmount",
            "contextValue":[
               "500",
               "100"
            ],
            "dataType":"Number",
            "value":""
         },
         {
            "name":"TotalMembers",
            "contextValue":[
               "100",
               "200"
            ],
            "dataType":"Number",
            "value":""
         }
      ],
      "stepResults":[
         {
            "name":"TotalPremium",
            "contextValue":[
               "1500",
               "300"
            ],
            "dataType":"Number",
            "value":""
         }
      ]
   }
}
```

               

               
: 
                  

This is an example of a simulation run failure.

                  

```
{
   "error" : {
      "errorCode" : "",
      "errorMsg" : "localized error msg",
      "errorDetail" : "" // stacktrace
   }
}
```

               

        
      

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

               

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Simulation Error Output](./connect_responses_simulation_error_output.htm.md) | Error details of the simulation, if any. | Small, 53.0 | 53.0 |
| `executionId` | String | Execution ID generated after a successful request. | Small, 53.0 | 53.0 |
| `output` | [Simulation Runtime Output](./connect_responses_simulation_runtime_output.htm.md) | Results of the expression set from the simulation. | Small, 54.0 | 54.0 |
| `simulationResults` | [Simulation Variable Output](./connect_responses_simulation_variable_output.htm.md)[] | List of output variables of the simulation. | Small, 53.0 | 53.0 |
| `simulationStepResults` | Map<String, [Simulation Step Result Output](./connect_responses_simulation_step_result_output.htm.md)> | List of steps in the simulation including the inputs and results of each step. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_input_variable_basic.htm ===
---
page_id: connect_responses_simulation_input_variable_basic.htm
title: Simulation Input Variable Basic
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_input_variable_basic.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Input Variable Basic

Output representation of the details of an input variable of a
      simulation.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

              

              

              
- 
- 
- 
- 
- 
- 

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | The API name of the input variable. | Small, 53.0 | 53.0 |
| `dataType` | String | The data type of the input variable. Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `Text` | Small, 53.0 | 53.0 |
| `defaultValue` | String | The default value of the input variable. | Small, 53.0 | 53.0 |
| `lastSimulatedValue` | String | The value of the input variable in the previous simulation. | Small, 53.0 | 53.0 |
| `name` | String | The name of the input variable. | Small, 53.0 | 53.0 |
| `precision` | String | The floating point precision of the variable. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_input_variables_result_list.htm ===
---
page_id: connect_responses_simulation_input_variables_result_list.htm
title: Simulation Input Variables Result List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_input_variables_result_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Input Variables Result List

Output representation of the list of input variables of a
      simulation.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      
        
          

**Sample Response**

          
: 
            

```
{
   "code": "200",
   "message": "",
   "isSuccess": true
   "inputVariables": [
     {
         "DataType": "Number",
         "Name": "medicalPayment",
         "ApiName": "medicalPayment",
         "DefaultValue": "10",
         "LastSimulatedValue": "10",
         "Precision": "1"
      }, {
         "DataType": "Number",
         "ApiName": "dedWaiverFactor",
         "Name": "dedWaiverFactor",
         "DefaultValue": "10",
         "LastSimulatedValue": "15",
         "Precision": "1"
      }
   ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The request response code. | Small, 53.0 | 53.0 |
| `inputVariables` | [Simulation Input Variables Basic](./connect_responses_simulation_input_variable_basic.htm.md)[] | The list of input variables of a simulation. | Small, 53.0 | 53.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful. | Small, 53.0 | 53.0 |
| `message` | String | The request response message. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_runtime_output.htm ===
---
page_id: connect_responses_simulation_runtime_output.htm
title: Simulation Runtime Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_runtime_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Runtime Output

Output representation of the results of an expression set from the
      simulation.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `aggregationResults` | Map<String, String> | Aggregation results of the expression set from the simulation when the step type is `Aggregation`. | Small, 54.0 | 54.0 |
| `calculationResults` | Map<String, String>[] | Calculation results of the expression set from the simulation when the step type is `Calculation`. | Small, 54.0 | 54.0 |

=== ARTICLE: connect_responses_simulation_step_additional_info_output.htm ===
---
page_id: connect_responses_simulation_step_additional_info_output.htm
title: Simulation Step Additional Info Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_step_additional_info_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Step Additional Info Output

Information about the decision matrix or sub expression used in a
      step.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

              

              

              
- 
- 

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `stepType` | String | The type of the step.Possible values are: `DecisionMatrix` `SubProcedure` | Small, 53.0 | 53.0 |
| `versionName` | String | The name of the decision matrix version or the sub expression version. | Small, 53.0 | 53.0 |
| `versionNumber` | String | The version ID of the decision matrix or the sub expression. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_step_explainability_message_output.htm ===
---
page_id: connect_responses_simulation_step_explainability_message_output.htm
title: Simulation Step Explainability Message Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_step_explainability_message_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Step Explainability Message Output

Output representation of a decision explanation message for a step
      from the simulation.

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextTag​Messages` | String | Explainability messages of the step when context tags are used in the step. | Small, 60.0 | 60.0 |
| `message` | String | Decision explanation message of the step. | Small, 56.0 | 56.0 |
| `showCondition​Details` | Boolean | For the `Condition` step type, this property indicates whether the decision explanation includes the condition's details (`true`) or not (`false`). The default value for this field is `false`. | Small, 56.0 | 56.0 |
| `showOnly​ExecutedPath​Message` | Boolean | For the `Branch` step type, this property indicates whether the decision explanation includes information about the executed path only (`true`) or not (`false`). The default value for this field is `true`. | Small, 56.0 | 56.0 |
| `template​Id` | String | Decision explainer template ID of the step. | Small, 56.0 | 56.0 |

=== ARTICLE: connect_responses_simulation_step_result_output.htm ===
---
page_id: connect_responses_simulation_step_result_output.htm
title: Simulation Step Result Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_step_result_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Step Result Output

Output representation of the simulation results of a
    step.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additionalInfo` | [Simulation Step Additional Info Output](./connect_responses_simulation_step_additional_info_output.htm.md) | Additional information if the step type is decision matrix or sub expression. | Small, 53.0 | 53.0 |
| `explainabilityMessage` | [Simulation Step Explainability Message Output](./connect_responses_simulation_step_explainability_message_output.htm.md) | Decision explanation message for a step. | Small, 56.0 | 56.0 |
| `isDefaulted` | Boolean | Indicates whether the step has default values (`true`) or not (`false`). | Small, 57.0 | 57.0 |
| `stepErrors` | Map<String, String> | Errors occurred in a step. | Small, 54.0 | 54.0 |
| `stepInputs` | [Simulation Variable Output](./connect_responses_simulation_variable_output.htm.md)[] | Input variables of a step. | Small, 53.0 | 53.0 |
| `stepResults` | [Simulation Variable Output](./connect_responses_simulation_variable_output.htm.md)[] | Output variables of a step. | Small, 53.0 | 53.0 |

=== ARTICLE: connect_responses_simulation_variable_output.htm ===
---
page_id: connect_responses_simulation_variable_output.htm
title: Simulation Variable Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_simulation_variable_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Simulation Variable Output

Output representation of a simulation variable and its
    value.

      

#### Note

This API has been deprecated as of API version 55.0.
        In API version 55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

            
              

              

              
- 
- 
- 
- 
- 
- 

              

              

            

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextValue` | Object | Context details for running the simulation on an expression set. | Small, 58.0 | 58.0 |
| `datatype` |  | The data type of the variable.Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `Text` | Small, 53.0 | 53.0 |
| `name` | String | Name of the variable. | Small, 53.0 | 53.0 |
| `precision` | Integer | Precision of the variable. | Small, 54.0 | 54.0 |
| `value` | String | Value of the variable. | Small, 53.0 | 53.0 |

=== ARTICLE: meta_omnidatatransform.htm ===
---
page_id: meta_omnidatatransform.htm
title: OmniDataTransform
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omnidatatransform.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniDataTransform

Represents the header configuration of a DataRaptor.
	

	

	

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName field. 

	

## File Suffix and Directory Location

		
		

OmniDataTransform components have the suffix .omniDataTransform and are
				stored in the OmniDataTransforms folder.

	

	

## Version

		
		

OmniDataTransform components are available in API version 54.0 and later.

	

	

## Special Access Rules

		
			

To use this metadata type, you must have an Omnistudio license and the Discovery
				Framework feature enabled in your Salesforce org.

	

	

## Fields

		
		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

- 
- 
- 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| active | **Field Type** boolean **Description** Indicates whether the omni data transformation is active (`true`) or not (`false`). The default value is `false`. |
| assignmentRulesUsed | **Field Type** boolean **Description** Indicates whether Salesforce Assignment Rules must be used (`true`) or not (`false`). The default value is `false`. |
| deletedOnSuccess | **Field Type** boolean **Description** Indicates whether bulk records must be deleted after successfully processed on bulk loading (`true`) or not (`false`). |
| description | **Field Type** string **Description** The comment added in the Omni Data Transformation. |
| errorIgnored | **Field Type** boolean **Description** Indicates whether the Omni Data Transformation must continue processing if there are errors (`true`) or not (`false`). |
| expectedInputJson | **Field Type** string **Description** The expected JSON input payload format to assist in the Omni Data Transformation configuration. |
| expectedInputOtherData | **Field Type** string **Description** The expected custom input payload format to assist in the Omni Data Transformation configuration. |
| expectedInputXml | **Field Type** string **Description** The expected XML input payload format to assist in the Omni Data Transformation configuration. |
| expectedOutputJson | **Field Type** string **Description** The expected JSON output payload format to assist in the Omni Data Transformation configuration. |
| expectedOutputOtherData | **Field Type** string **Description** The expected custom output payload format to assist in the Omni Data Transformation configuration. |
| expectedOutputXml | **Field Type** string **Description** The expected XML output payload format to assist in the Omni Data Transformation configuration. |
| fieldLevelSecurityEnabled | **Field Type** boolean **Description** Indicates whether the Omni Data Transformation must check the user field-level access (`true`) or not (`false`). |
| inputParsingClass | **Field Type** string **Description** Custom class that's used to deserialize input to support any serialization format. |
| inputType | **Field Type** OmniDataTransformInputType (enumeration of type string) **Description** The data format in the input.Values are: `Custom` `JSON` `SObject` `XML` |
| isManagedUsingStdDesigner | **Field Type** boolean **Description** Indicates whether the Omni Data Transformation is managed using standard designer (`true`) or not (`false`). |
| name | **Field Type** string **Description** Required. The name that uniquely identifies a Omni Data Transformation. |
| namespace | **Field Type** string **Description** The namespace associated with the omni data transformation record. |
| nullInputsIncludedInOutput | **Field Type** boolean **Description** Indicates whether fields missing in the input (or null) must nullify the values in the record (`true`) or ignore the missing input and only update the fields that were provided in the input (`false`). |
| omniDataTransformItem | **Field Type** [OmniDataTransformItem[]](#OmniDataTransformItem) **Description** The configuration of a component inside a DataRaptor. |
| outputParsingClass | **Field Type** string **Description** Custom class that's used to serialize output to support any serialization format. |
| outputType | **Field Type** string **Description** The data format or object that's used in the output (JSON, XML, SObejct, PDF, Document). |
| overrideKey | **Field Type** string **Description** Reserved for future use. |
| preprocessorClassName | **Field Type** string **Description** The Apex class name to be executed before the Omni Data Transformation (acting as a before insert trigger/process). |
| previewJsonData | **Field Type** string **Description** The preview of input JSON. |
| previewOtherData | **Field Type** string **Description** The preview of input other data. |
| previewSourceObjectData | **Field Type** string **Description** The preview of input source object records. |
| previewXmlData | **Field Type** string **Description** The preview of input XML. |
| processSuperBulk | **Field Type** boolean **Description** Indicates whether the load Omni Data Transformation process the record upsert spread over multiple Salesforce Apex batch jobs (`true`) or not (`false`). |
| requiredPermission | **Field Type** string **Description** The list of custom permissions required to execute the Omni Data Transformation. |
| responseCacheTtlMinutes | **Field Type** double **Description** The number of minutes the Omni Data Transformation response must stay in the platform cache. |
| responseCacheType | **Field Type** string **Description** The platform cache used to store the Omni Data Transformation response, either org cache or session cache. |
| rollbackOnError | **Field Type** boolean **Description** Indicates whether the Omni Data Transformation must not commit if there is an error (`true`) or commit what has been executed (`false`). |
| sourceObject | **Field Type** string **Description** The SObject that's used as input in a Load Omni Data Transformation. |
| sourceObjectDefault | **Field Type** boolean **Description** Indicates whether it's the default Omni Data Transformation setting for the specified interface object (`true`) or not (`false`). |
| synchronousProcessThreshold | **Field Type** double **Description** The number of input records that can be processed synchronously in a Load Omni Data Transformation. If it's more than this number, then it uses a batch job. |
| targetOutputDocumentIdentifier | **Field Type** string **Description** The envelope ID of the document template. |
| targetOutputFileName | **Field Type** string **Description** The document name that receives the output of the Omni Data Transformation. |
| type | **Field Type** string **Description** Required. The definition of what the Omni Data Transformation performs: extract (SOQL), transform, or load (DML). |
| uniqueName | **Field Type** string **Description** The unique name for the Omni Data Transformation. |
| versionNumber | **Field Type** double **Description** A numeric version that's used with subtype, type, and language to create a unique identifier for Omni Data Transformation. |
| xmlDeclarationRemoved | **Field Type** boolean **Description** Indicates whether the XML declaration (e.g. <?xml version="1.0" encoding="UTF-8"?>) must be removed (`true`) or not (`false`). |
| xmlOutputTagsOrder | **Field Type** string **Description** The XML tag sequence to be used in the output. |

	

		

## OmniDataTransformItem

		
		

Represents the configuration of a component inside a DataRaptor.

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| defaultValue | **Field Type** string **Description** The default value that's used in output map. |
| disabled | **Field Type** boolean **Description** Indicates whether the output must not be generated (`true`) or is active and must be generated (`false`). |
| filterDataType | **Field Type** ODTItemFilterDataType (enumeration of type string) **Description** The field data type that's used in a Turbo Omni Data Transformation.Values are: `ADDRESS` `ANYTYPE` `BASE64` `BOOLEAN` `COMBOBOX` `CURRENCY` `DATACATEGORY` `DATE` `DATETIME` `DOUBLE` `EMAIL` `ENCRYPTEDSTRING` `GROUPREFERENCE` `ID` `INTEGER` `LONG` `MULTIPICKLIST` `PERCENT` `PHONE` `PICKLIST` `REFERENCE` `STRING` `TEXTAREA` `TIME` `URL` |
| filterGroup | **Field Type** double **Description** The grouping of WHERE clauses in the SOQL. |
| filterOperator | **Field Type** string **Description** The operator in the WHERE clause of the SOQL. |
| filterValue | **Field Type** string **Description** The field in the WHERE clause of the SOQL. |
| formulaConverted | **Field Type** string **Description** The reverse polish notation of the formula. |
| formulaExpression | **Field Type** string **Description** The formula that the user typed in. |
| formulaResultPath | **Field Type** string **Description** The variable name where the formula output is stored. |
| formulaSequence | **Field Type** double **Description** The sequence of execution of the formulas. |
| globalKey | **Field Type** string **Description** The globally unique identifier of the Omni Data Transformation Item that's used to identify the product across Salesforce orgs. |
| inputFieldName | **Field Type** string **Description** The field or variable path that's used in the configuration of the inputs. |
| inputObjectName | **Field Type** string **Description** The object that's used in the configuration of the inputs. |
| inputObjectQuerySequence | **Field Type** double **Description** The execution sequence of the inputs. |
| linkedFieldName | **Field Type** string **Description** The field name that's used to look up another object in a Load Omni Data Transformation. |
| linkedObjectSequence | **Field Type** double **Description** The UI number (sequence number) associated with the object that's used in the lookup in a Load Omni Data Transformation. |
| lookupByFieldName | **Field Type** string **Description** The field name that's used to look up a record in a Load Omni Data Transformation output. |
| lookupObjectName | **Field Type** string **Description** The object name that's used to look up a record in a Load Omni Data Transformation output. |
| lookupReturnedFieldName | **Field Type** string **Description** The field name that must be returned and used in the lookup in a Load Omni Data Transformation output. |
| migrationAttribute | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationCategory | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationGroup | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationKey | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationPattern | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationProcess | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationType | **Field Type** string **Description** Field that's used for DataPacks. |
| migrationValue | **Field Type** string **Description** Field that's used for DataPacks. |
| name | **Field Type** string **Description** Required. The Omni Data Transformation name where this configuration belongs to. |
| omniDataTransformation | **Field Type** string **Description** Omni Data Transformation associated with the item configuration |
| omniDataTransformationId | **Field Type** string **Description** The ID of the Omni Data Transformation associated with this item configuration. |
| outputCreationSequence | **Field Type** double **Description** The sequence of the output path items. |
| outputFieldFormat | **Field Type** string **Description** The data type of the field, node, or tag in the output path. |
| outputFieldName | **Field Type** string **Description** The field, node, or tag in the object that's used in the output path. |
| outputObjectName | **Field Type** string **Description** The name of the object that's used in the output path. |
| requiredForUpsert | **Field Type** boolean **Description** Indicates whether the field is mandatory for the upsert (`true`) or not (`false`). |
| transformValuesMappings | **Field Type** string **Description** The key-value pair JSON list that's used to convert output values into another value. |
| upsertKey | **Field Type** boolean **Description** Indicates whether the field is the key to find the records to upsert in the object (`true`) or is a value that's to be used during the upsert (`false`). |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of an OmniDataTransform component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniDataTransform xmlns="http://soap.sforce.com/2006/04/metadata">
    <active>false</active>
    <assignmentRulesUsed>false</assignmentRulesUsed>
    <deletedOnSuccess>false</deletedOnSuccess>
    <errorIgnored>false</errorIgnored>
    <fieldLevelSecurityEnabled>true</fieldLevelSecurityEnabled>
    <inputType>JSON</inputType>
    <isManagedUsingStdDesigner>false</isManagedUsingStdDesigner>
    <name>COODMtest</name>
    <nullInputsIncludedInOutput>false</nullInputsIncludedInOutput>
    <omniDataTransformItem>
        <disabled>false</disabled>
        <filterGroup>0.0</filterGroup>
        <globalKey>c7622d95-6995-4b57-8102-716e034e15e4</globalKey>
        <inputFieldName>Account:Type</inputFieldName>
        <inputObjectQuerySequence>0.0</inputObjectQuerySequence>
        <linkedObjectSequence>0.0</linkedObjectSequence>
        <name>COODMtest</name>
        <outputCreationSequence>1.0</outputCreationSequence>
        <outputFieldName>Type</outputFieldName>
        <outputObjectName>json</outputObjectName>
        <requiredForUpsert>false</requiredForUpsert>
        <transformValuesMappings>{ }</transformValuesMappings>
        <upsertKey>false</upsertKey>
    </omniDataTransformItem>
    <omniDataTransformItem>
        <disabled>false</disabled>
        <filterGroup>0.0</filterGroup>
        <filterOperator>&lt;&gt;</filterOperator>
        <filterValue>&apos;&apos;</filterValue>
        <globalKey>fffd4cd6-7ad8-4e90-adaa-d534a8f75dde</globalKey>
        <inputFieldName>Id</inputFieldName>
        <inputObjectName>Account</inputObjectName>
        <inputObjectQuerySequence>1.0</inputObjectQuerySequence>
        <linkedObjectSequence>0.0</linkedObjectSequence>
        <name>COODMtest</name>
        <outputCreationSequence>0.0</outputCreationSequence>
        <outputFieldName>Account</outputFieldName>
        <outputObjectName>json</outputObjectName>
        <requiredForUpsert>false</requiredForUpsert>
        <upsertKey>false</upsertKey>
    </omniDataTransformItem>
    <omniDataTransformItem>
        <disabled>false</disabled>
        <filterGroup>0.0</filterGroup>
        <globalKey>34b482a6-b64e-4d7f-9610-ef1c4f613b44</globalKey>
        <inputFieldName>Account:Id</inputFieldName>
        <inputObjectQuerySequence>0.0</inputObjectQuerySequence>
        <linkedObjectSequence>0.0</linkedObjectSequence>
        <name>COODMtest</name>
        <outputCreationSequence>1.0</outputCreationSequence>
        <outputFieldName>Id</outputFieldName>
        <outputObjectName>json</outputObjectName>
        <requiredForUpsert>false</requiredForUpsert>
        <transformValuesMappings>{ }</transformValuesMappings>
        <upsertKey>false</upsertKey>
    </omniDataTransformItem>
    <omniDataTransformItem>
        <disabled>false</disabled>
        <filterGroup>0.0</filterGroup>
        <globalKey>5e7ae38a-0cb1-4383-aab9-43e4d88caff2</globalKey>
        <inputFieldName>Account:Name</inputFieldName>
        <inputObjectQuerySequence>0.0</inputObjectQuerySequence>
        <linkedObjectSequence>0.0</linkedObjectSequence>
        <name>COODMtest</name>
        <outputCreationSequence>1.0</outputCreationSequence>
        <outputFieldName>Name</outputFieldName>
        <outputObjectName>json</outputObjectName>
        <requiredForUpsert>false</requiredForUpsert>
        <transformValuesMappings>{ }</transformValuesMappings>
        <upsertKey>false</upsertKey>
    </omniDataTransformItem>
    <omniDataTransformItem>
        <disabled>false</disabled>
        <filterGroup>0.0</filterGroup>
        <globalKey>1a6f7464-1157-4ec3-b62f-f795c5caceb2</globalKey>
        <inputFieldName>Account:BillingStreet</inputFieldName>
        <inputObjectQuerySequence>0.0</inputObjectQuerySequence>
        <linkedObjectSequence>0.0</linkedObjectSequence>
        <name>COODMtest</name>
        <outputCreationSequence>1.0</outputCreationSequence>
        <outputFieldName>BS</outputFieldName>
        <outputObjectName>json</outputObjectName>
        <requiredForUpsert>false</requiredForUpsert>
        <transformValuesMappings>{ }</transformValuesMappings>
        <upsertKey>false</upsertKey>
    </omniDataTransformItem>
    <outputType>JSON</outputType>
    <processSuperBulk>false</processSuperBulk>
    <responseCacheTtlMinutes>0.0</responseCacheTtlMinutes>
    <rollbackOnError>false</rollbackOnError>
    <sourceObjectDefault>false</sourceObjectDefault>
    <synchronousProcessThreshold>0.0</synchronousProcessThreshold>
    <type>Extract</type>
    <uniqueName>COODMtest_1</uniqueName>
    <versionNumber>1.0</versionNumber>
    <xmlDeclarationRemoved>false</xmlDeclarationRemoved>
</OmniDataTransform>

```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniDataTransform</name>
    </types>
    <version>67.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_omniexttrackingdef.htm ===
---
page_id: meta_omniexttrackingdef.htm
title: OmniExtTrackingDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniexttrackingdef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniExtTrackingDef

		Represents a connection between an OmniTrackingGroup in OmniAnalytics and a
			third-party Analytics system such as Google Analytics.

		
			

#### Note

This metadata type is part of Omnistudio Standard, not Omnistudio for Vlocity.

			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName field. 

	

## File Suffix and Directory Location

		
		

OmniExtTrackingDef components have the suffix .OmniExtTrackingDef and are stored in the OmniExtTrackingDefs folder.

	

	

## Version

		
		

OmniExtTrackingDef components are available in API version 60.0 and later.

	

	

## Special Access Rules

		
			

Using OmniAnalytics requires having an Omnistudio license and enabling OmniAnalytics in
				Setup.

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

#### 

#### 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

- 
- 

				

				

			
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** A description of the OmniExtTrackingDef. |
| developerName | **Field Type** string **Description** Required. The unique name of the OmniExtTrackingDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| isActive | **Field Type** boolean **Description** Required. Specifies whether the OmniExtTrackingDef is active. |
| masterLabel | **Field Type** string **Description** Required. The unique master label of the OmniExtTrackingDef. This internal label doesn’t get translated. |
| omniExtTrackingDefKey | **Field Type** string **Description** A UUID generated internally by Salesforce to uniquely identify an OmniExtTrackingDef record across all orgs. |
| omniExtTrackingEventDefs | **Field Type** [OmniExtTrackingEventDef[]](#OmniExtTrackingEventDef) **Description** The OmniExtTrackingEventDef objects related to this OmniExtTrackingDef. |
| trackingFrameworkInformation | **Field Type** string **Description** Required. JSON data containing information about an external service, such as the API call and input parameter names. |
| trackingServiceProvider | **Field Type** ExternalTrackingVendor (enumeration of type string) **Description** Required. The third-party Analytics system to which user interaction data is sent. Values are: `Google` `Mixpanel` |

	

		

## OmniExtTrackingEventDef

		
		

Represents a format for FlexCard or OmniScript user interaction data that a third-party
				Analytics system such as Google Analytics can accept.

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

- 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

#### 

#### 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| componentType | **Field Type** OmniAnalyticsComponentType (enumeration of type string) **Description** Required. The type of component for which user interactions are tracked. Values are: `Flexcard` `Omniscript` |
| description | **Field Type** string **Description** A description of the OmniExtTrackingEventDef. |
| developerName | **Field Type** string **Description** Required. The unique name of the OmniExtTrackingEventDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| inclusionRule | **Field Type** string **Description** Required. A true-or-false condition that determines whether an event is sent to the third-party Analytics system. |
| masterLabel | **Field Type** string **Description** Required. The unique master label of the OmniExtTrackingEventDef. This internal label doesn’t get translated. |
| omniExtTrackingDef | **Field Type** string **Description** The ID of the related OmniExtTrackingDef object. |
| omniExtTrackingEventDefKey | **Field Type** string **Description** A UUID generated internally by Salesforce to uniquely identify an OmniExtTrackingEventDef record across all orgs. |
| payloadTemplate | **Field Type** string **Description** Required. The payload template structure with placeholders for runtime data. This is used at runtime to generate the actual payload to be sent to the external Analytics service. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of an OmniExtTrackingDef component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniExtTrackingDef xmlns="http://soap.sforce.com/2006/04/metadata">
    <developerName>Purchase_Tracking_Google</developerName>
    <isActive>true</isActive>
    <masterLabel>Purchase_Tracking_Google</masterLabel>
    <trackingFrameworkInformation>{ "id": "GTM-XXXXXXX" }</trackingFrameworkInformation>
    <trackingServiceProvider>Google</trackingServiceProvider>
    <omniExtTrackingEventDefs>
        <componentType>Omniscript</componentType>
        <developerName>Purchase_Funnel_Google</developerName>
        <inclusionRule></inclusionRule>
        <masterLabel>Purchase_Funnel_Google</masterLabel>
        <payloadTemplate>
{
  "event": "promotionClick",
  "ecommerce": {
    "promoClick": {
      "promotions": [
        {
          "name": "%BusinessEvent%"
        }
      ]
    }
  }
}
        </payloadTemplate>
    </omniExtTrackingEventDefs>
</OmniExtTrackingDef>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniExtTrackingDef</name>
    </types>
    <version>60.0</version>
</Package>
```

		

		
		

## Wildcard Support in the Manifest File

			
			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_omniintegrationprocedure.htm ===
---
page_id: meta_omniintegrationprocedure.htm
title: OmniIntegrationProcedure
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniintegrationprocedure.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniIntegrationProcedure

		Represents an Omnistudio Integration Procedure for the
			Discovery Framework. It enables declarative, server-side processing to perform multiple
			actions in a single server call, supporting sales, service, and other business
			workflows. For Discovery Framework, the customization type is
				`discoveryframework`.
	

	

	

## Parent Type

			
			

 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field. 

		

	

## File Suffix and Directory Location

		
		

OmniIntegrationProcedure components have the suffix
					.omniIntegrationProcedure and are stored in the
					omnistudio/<Namespace>/omniIntegrationProcedures
				folder.

	

	

## Version

		
			

OmniIntegrationProcedure components are available in API version 56.0 and later.

	

		

## Special Access Rules

			
			

To use this metadata type, you must have an Omnistudio license and the Discovery
				Framework feature enabled in your Salesforce org.

		

	

## Fields

		
		
		
		
		

		
		
		
		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 
: 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| customHtmlTemplates | **Field Type** string **Description** The angular Omniscript template definitions. |
| customJavaScript | **Field Type** string **Description** The custom JavaScript used for integration procedure. |
| description | **Field Type** string **Description** The description of the integration procedure. |
| designerCustomizationType | **Field Type** string **Description** The Omnistudio designer customization type. |
| elementTypeComponentMapping | **Field Type** string **Description** Overrides all elements of one type with a custom Lightning web component by mapping the element type to the Custom LWC. |
| integrationProcedureInput | **Field Type** string **Description** The input for the integration procedure in JSON format. |
| integrationProcedureOutput | **Field Type** string **Description** The output for the integration procedure in JSON format. |
| isActive | **Field Type** boolean **Description** Indicates whether the integration procedure is active (`true`) or not (`false`). The default value is `false`. |
| isIntegProcdSignatureAvl | **Field Type** boolean **Description** Indicates whether the integration procedure has a signature (`true`) or not (`false`). The default value is `false`. |
| isIntegrationProcedure | **Field Type** boolean **Description** Indicates whether Omniscript is an Integration Procedure (`true`) or Omniscript metadata (`false`). |
| isManagedUsingStdDesigner | **Field Type** boolean **Description** Indicates whether the integration procedure is managed using standard designer (`true`) or not (`false`). |
| isMetadataCacheDisabled | **Field Type** boolean **Description** Indicates whether metadata cache for the integration procedure is disabled (`true`) or not (`false`). The default value is `false`. |
| isOmniScriptEmbeddable | **Field Type** boolean **Description** Indicates whether the Omniscript can be embedded in other Omniscripts (`true`) or not (`false`). The default value is `false` |
| isTestProcedure | **Field Type** boolean **Description** Indicates whether OmniIntegrationProcedure is a test procedure setting (`true`) or not (`false`). The default value is `false` |
| isWebCompEnabled | **Field Type** boolean **Description** Indicates whether web component Omniscript (not Angular) is enabled (`true`) or not (`false`). The default value is `false` |
| language | **Field Type** string **Description** Required. The language of the integration procedure. |
| lastPreviewPage | **Field Type** string **Description** The last page previewed in the Omniscript designer. |
| name | **Field Type** string **Description** Required. The name of the integration procedure. |
| nameSpace | **Field Type** string **Description** The namespace associated with the integration procedure record. |
| omniProcessElements | **Field Type** [OmniProcessElement[]](#OmniProcessElement) **Description** The OmniProcessElements associated with the OmniIntegrationProcedure. |
| omniProcessKey | **Field Type** string **Description** The integration procedure `Type_SubType` value. |
| omniProcessType | **Field Type** OmniProcessType (enumeration of type string) **Description** Required. Integration Procedure or Omniscript. Possible value is: `Integration Procedure` |
| overrideKey | **Field Type** string **Description** Reserved for future use. |
| propertySetConfig | **Field Type** string **Description** The configuration information associated with the OmniIntegrationProcedure. |
| requiredPermission | **Field Type** string **Description** The required permissions to execute the integration procedure. |
| responseCacheType | **Field Type** string **Description** Response cache used for the integration procedure (session or Org). |
| subType | **Field Type** string **Description** Required. The subtype value that's used with type and language to create a unique identifier for integration procedure. Integration Procedure subtype can contain only alphanumeric characters. |
| type | **Field Type** string **Description** Required. The type value that's used with subtype and language to create a unique identifier for integration procedure. Integration Procedure type can contain only alphanumeric characters. |
| uniqueName | **Field Type** string **Description** Required. The unique name for the integration procedure as Type_SubType_Language_VersionNumber. |
| versionNumber | **Field Type** string **Description** Required. A numeric version that's used with subtype, type, and language to create a unique identifier for integration procedure. |
| webComponentKey | **Field Type** string **Description** Internal unique key for the generated Lightning Web Components (LWC). |

	

		

## OmniProcessElement

		
			

Represents the Omnistudio Process Element associated with the Omnistudio Integration
				Procedure.

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 
: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| childElements | **Field Type** [OmniProcessElement[]](#OmniProcessElement) **Description** The child elements associated with the OmniProcessElement. |
| description | **Field Type** string **Description** The description of the OmniProcessElement. |
| designerCustomizationType | **Field Type** string **Description** The Omnistudio designer customization type. |
| discoveryFrameworkUsageType | **Field Type** string **Description** The usage type for industries that use the Discovery Framework. For example, the value for Health Cloud is `HcUsageType`. The value for no specific industry is `Default`. |
| embeddedOmniScriptKey | **Field Type** string **Description** The ID of the embedded Omniscript. |
| isActive | **Field Type** boolean **Description** Indicates whether the status of the OmniProcessElement is active (`true`) or not (`false`). |
| isOmniScriptEmbeddable | **Field Type** boolean **Description** Indicates whether the Omniscript with the OmniProcessElement can be embedded in other Omniscript (`true`) or not (`false`). |
| level | **Field Type** double **Description** The vertical level in which the OmniProcessElement occurs on the Omniscript. |
| name | **Field Type** string **Description** Required. The name of the OmniProcessElement. |
| omniProcessVersionNumber | **Field Type** double **Description** The version number of Omnistudio process element. |
| parentElementName | **Field Type** string **Description** The name of the parent OmniProcessElement. |
| parentElementType | **Field Type** string **Description** The type of the parent OmniProcessElement. |
| propertySetConfig | **Field Type** textarea **Description** The property set of the OmniProcessElement. |
| sequenceNumber | **Field Type** double **Description** The horizontal level in which the OmniProcessElement occurs on the Omniscript. |
| type | **Field Type** string **Description** The OmniProcessElement type. For example, `Text` and `TextArea`. |
| uniqueIndex | **Field Type** string **Description** A unique index number for the Omniscript. |

	

		

## Declarative Metadata Sample Definition

		
			
			

The following is an example of an OmniIntegrationProcedure component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniIntegrationProcedure xmlns="http://soap.sforce.com/2006/04/metadata">
    <customJavaScript>{&quot;salary&quot;:332}</customJavaScript>
    <elementTypeComponentMapping>{&quot;ElementTypeToHTMLTemplateList&quot;:[]}</elementTypeComponentMapping>
    <integrationProcedureInput>{
  &quot;properties&quot;: {
    &quot;salary&quot;: {
      &quot;type&quot;: &quot;integer&quot;
    }
  },
  &quot;type&quot;: &quot;object&quot;,
  &quot;title&quot;: &quot;Data&quot;,
  &quot;$schema&quot;: &quot;https://json-schema.org/draft/2020-12/schema&quot;
}</integrationProcedureInput>
    <integrationProcedureOutput>{
  &quot;properties&quot;: {
    &quot;tax&quot;: {
      &quot;type&quot;: &quot;double&quot;
    }
  },
  &quot;type&quot;: &quot;object&quot;,
  &quot;title&quot;: &quot;Data&quot;,
  &quot;$schema&quot;: &quot;https://json-schema.org/draft/2020-12/schema&quot;
}</integrationProcedureOutput>
    <isActive>true</isActive>
    <isIntegProcdSignatureAvl>true</isIntegProcdSignatureAvl>
    <isIntegrationProcedure>true</isIntegrationProcedure>
    <isManagedUsingStdDesigner>false</isManagedUsingStdDesigner>
    <isMetadataCacheDisabled>false</isMetadataCacheDisabled>
    <isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
    <isTestProcedure>false</isTestProcedure>
    <isWebCompEnabled>false</isWebCompEnabled>
    <language>English</language>
    <name>Calc</name>
    <omniProcessElements>
        <description>Response Action</description>
        <isActive>true</isActive>
        <isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
        <level>0.0</level>
        <name>Response</name>
        <omniProcessVersionNumber>0.0</omniProcessVersionNumber>
        <propertySetConfig>{
  &quot;responseJSONPath&quot; : &quot;&quot;,
  &quot;responseJSONNode&quot; : &quot;&quot;,
  &quot;executionConditionalFormula&quot; : &quot;&quot;,
  &quot;returnFullDataJSON&quot; : false,
  &quot;additionalOutput&quot; : {
    &quot;tax&quot; : &quot;=%salary%*0.3&quot;
  },
  &quot;returnOnlyAdditionalOutput&quot; : false,
  &quot;sendJSONPath&quot; : &quot;&quot;,
  &quot;responseFormat&quot; : &quot;&quot;,
  &quot;id&quot; : &quot;&quot;,
  &quot;isActive&quot; : true,
  &quot;restOptions&quot; : { },
  &quot;sendJSONNode&quot; : &quot;&quot;
}</propertySetConfig>
        <sequenceNumber>1.0</sequenceNumber>
        <type>Response Action</type>
    </omniProcessElements>
    <omniProcessKey>calc_calc</omniProcessKey>
    <omniProcessType>Integration Procedure</omniProcessType>
    <propertySetConfig>{
  &quot;transientValues&quot; : {
    &quot;deactivateConsent&quot; : false
  }
}</propertySetConfig>
    <subType>calc</subType>
    <type>calc</type>
    <uniqueName>calc_calc_English_1</uniqueName>
    <versionNumber>1.0</versionNumber>
</OmniIntegrationProcedure>

```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
    xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniIntegrationProcedure</name>
    </types>
    <version>67.0</version>
</Package>
```

		

		
		

## Wildcard Support in the Manifest File

			
			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

		

		

## Usage Type

			
			

Before you retrieve or deploy Discovery Framework OmniScripts, we recommend that you review
				this consideration.

			
				
- When deploying the OmniIntegrationProcedure of type Discovery Framework, enable
					Discovery Framework Metadata Enabled setting.

=== ARTICLE: meta_omniinteractionaccessconfig.htm ===
---
page_id: meta_omniinteractionaccessconfig.htm
title: OmniInteractionAccessConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniinteractionaccessconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniInteractionAccessConfig

Represents configuration settings for access to Omnistudio
      FlexCard caching and data sources.

    

## Parent Type

       This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm)
      metadata type and inherits its fullName field. 

    

## File Suffix and Directory Location

      
      

OmniInteractionAccessConfig components have the suffix
          .omniInteractionAccessConfig and are stored in the
          OmniInteractionAccessConfig folder.

    

    

## Version

      
      

OmniInteractionAccessConfig components are available in API version 53.0 and later.

    

    

## Special Access Rules

      
      

OmniInteractionAccessConfig is available if your org has the Omnistudio platform license
        and related addon and user licenses.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| configName | string | Not used. |
| isAsyncCardCachingEnabled | boolean | Required. If set to `true`, enables asynchronous FlexCard caching. The default is `false`. |
| isCardApexRemoteDisabled | boolean | Required. If set to `true`, disables remote Apex method calls for FlexCards. The default is `false`. |
| isCardCacheDisabled | boolean | Required. If set to `true`, disables FlexCard caching. The default is `false`. |
| isCardDataTfrmDisabled | boolean | Required. If set to `true`, disables Data Mapper data sources for FlexCards. The default is `false`. |
| isCardIntegrationProcDisabled | boolean | Required. If set to `true`, disables Integration Procedure data sources for FlexCards. The default is `false`. |
| isCardRestApiDisabled | boolean | Required. If set to `true`, disables REST calls for FlexCards. The default is `false`. |
| isCardSoqlDisabled | boolean | Required. If set to `true`, disables SOQL queries for FlexCards. The default is `false`. |
| isCardSoslDisabled | boolean | Required. If set to `true`, disables SOSL queries for FlexCards. The default is `false`. |
| isCardStreamingApiDisabled | boolean | Required. If set to `true`, disables Streaming API calls for FlexCards. The default is `false`. |
| isDataTfrmEncrpFieldsDisabled | boolean | Required. If set to `true`, disables Data Mapper field encryption for FlexCards. The default is `false`. |
| masterLabel | string | Required. The name of the setting. The value is `Profile_`ProfileId, `User_`UserId, or `Org_Wide`. |
| setupOwner | string | The ID of the profile, user, or org to which the settings apply. |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of an OmniInteractionAccessConfig component.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniInteractionAccessConfig xmlns="http://soap.sforce.com/2021/10/metadata">
   <isAsyncCardCachingEnabled>false</isAsyncCardCachingEnabled>
   <isCardApexRemoteDisabled>false</isCardApexRemoteDisabled>
   <isCardCacheDisabled>false</isCardCacheDisabled>
   <isCardDataTfrmDisabled>false</isCardDataTfrmDisabled>
   <isCardIntegrationProcDisabled>false</isCardIntegrationProcDisabled>
   <isCardRestApiDisabled>false</isCardRestApiDisabled>
   <isCardSoqlDisabled>false</isCardSoqlDisabled>
   <isCardSoslDisabled>false</isCardSoslDisabled>
   <isCardStreamingApiDisabled>false</isCardStreamingApiDisabled>
   <isDataTfrmEncrpFieldsDisabled>false</isDataTfrmEncrpFieldsDisabled>
   <masterLabel>Profile_00eB0000000ijOH</masterLabel>
   <setupOwner>00eB0000000ijOH</setupOwner>
</OmniInteractionAccessConfig>
```

      

The following is an example `package.xml` that references the previous
        definition.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2021/10/metadata">
    <types>
        <members>*</members>
        <name>OmniInteractionAccessConfig</name>
    </types>
    <version>53.0</version>
</Package>
```

    

    

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*`
        (asterisk) in the package.xml manifest file. For information about
        using the manifest file, see [Deploying and
          Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_omniinteractionconfig.htm ===
---
page_id: meta_omniinteractionconfig.htm
title: OmniInteractionConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniinteractionconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniInteractionConfig

Represents configuration settings for
    Omnistudio.

    

## Parent Type

       This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm)
      metadata type and inherits its fullName field. 

    

## File Suffix and Directory Location

      
      

OmniInteractionConfig components have the suffix
          .omniInteractionConfig and are stored in the
          OmniInteractionConfig folder.

    

    

## Version

      
      

OmniInteractionConfig components are available in API version 51.0 and later.

    

    

## Special Access Rules

      
      

OmniInteractionConfig is available if your org has the Omnistudio platform license and
        related add-on and user licenses.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| masterLabel | string | Required. The name of the setting. |
| value | string | Required. The value of the setting. |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of an OmniInteractionConfig component.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniInteractionConfig xmlns="http://soap.sforce.com/2021/10/metadata">
   <masterLabel>TheFirstInstalledOmniPackage</masterLabel>
   <value>omnistudio</value>
</OmniInteractionConfig>
```

      

The following is an example `package.xml` that references the previous
        definition.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2021/10/metadata">
    <types>
        <members>*</members>
        <name>OmniInteractionConfig</name>
    </types>
    <version>51.0</version>
</Package>
```

    

    

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*`
        (asterisk) in the package.xml manifest file. For information about
        using the manifest file, see [Deploying and
          Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

    

    

## Usage

      
      Settings configured using OmniInteractionConfig include:

#### Important

During the week of February 2, 2026, Salesforce enables the
            AdvancedOmnistudioAccessCheck,
          ApexClassCheckForIP, ApexClassCheck,
            EnforceDMFLSAndDataEncryption, and
            EnableQueryWithFLS settings by default to enhance org security.
          Review and prepare your configuration for a seamless transition and to prevent potential
          service interruptions.

      
        
- 
`AdvancedOmnistudioAccessCheck`—If set to `true`, performs advanced security checks for Omnistudio for
          Managed Packages to enhance data protection by enforcing stricter validation of access and
          permissions. These checks validate object-level access, field-level security, and Apex
          class permissions for all users, including guest, authenticated, and non-authenticated
          users, across Omnistudio components. See [Advanced Security Checks for Omnistudio for Managed
            Packages](https://help.salesforce.com/s/articleView?id=xcloud.os_advanced_security_updates_overview.htm&type=5&language=en_US).

        
- 
`ApexClassCheckForIP`—If set to `true`, strengthens security checks for Omnistudio for
          Managed Packages by enforcing Apex class access checks during Integration Procedure
          execution. This enhancement makes sure that users have the required permissions to run
          custom Apex classes referenced within Integration Procedures. See [Advanced Apex Class Check for Integration Procedures in
            Omnistudio for Managed Packages](https://help.salesforce.com/s/articleView?id=xcloud.os_ip_advanced_apex_class_check.htm&type=5&language=en_US).

        
- 
`ApexClassCheck`—Enable access to the` VlocityOpenInterface` Apex class that's used by remote
          action APIs for a user profile. Configure an Apex class permissions checker to make sure
          that users require explicit access to the Apex class that administers the remote action
          called from an Omniscript, Flexcard, or REST API. Checks Apex classes assigned to a
          profile and controls access. If the Omnistudio license isn’t available in your Salesforce
          org (for example, if you have installed Omnistudio as part of the CME or Insurance managed
          package), set the `ApexClassCheck` configuration to
            `true`. See [Add an Apex Class Permissions Checker](https://help.salesforce.com/s/articleView?id=xcloud.os_standard_add_an_apex_class_permissions_checker.htm&language=en_US&type=5).

        
- 
`CheckCachedMetadataRecordSecurity`—If set to `true`, performs a record-level security check for cached
          data in Data Mappers and Integration Procedures.

        
- 
`DefaultRequiredPermission`—The Custom Permission a
          user must have to run Data Mappers and Integration Procedures.

        
- 
`DocuSignAccountId`—The API Account ID from
          DocuSign's Apps and Keys page.

        
- 
`DocuSignNamedCredential`—The named credential for
          connecting to DocuSign. Set the value to `DocuSign`.

        
- 
`EnableQueryWithFLS`—Construct text-based search
          queries against the search index with Salesforce Object Search Language (SOSL). By using a
          single query, you can search text, email, and phone fields for multiple objects to which
          you have access, including custom objects. SOSL queries are encrypted so the query
          information isn’t visible on the client side. To enforce field-level security for an SOSL
          query, add the `EnableQueryWithFLS` Omni Interaction
          Configuration and set it to `true`. See [Set Up a Data Source on a Flexcard](https://help.salesforce.com/s/articleView?id=xcloud.os_configure_a_data_source_on_a_flexcard_35864.htm&language=en_US&type=5).

        
- 
`EnforceDMFLSAndDataEncryption`—If set to `true`, this setting enforces field-level security for all
          Data Mappers and displays encrypted fields in plain text only for users with the View
          Encrypted Data permission. This configuration also enforces object-level security. If set
          to true, Data Mappers run in the user context instead of the system context. The system
          respects the object and field-level permissions of the running user so that they only see
          the data they have access to. See [Security for Omnistudio Data Mappers and Integration
            Procedures](https://help.salesforce.com/s/articleView?id=xcloud.os_security_for_dataraptors_and_integration_procedures_48147.htm&language=en_US&type=5).

        
- 
`InstalledIndustryPackage`—If present, lists the namespace of the Salesforce
          Industries managed package that was installed. Values are `vlocity_cmt`, `vlocity_ins`, or `vlocity_ps`. Read-only.

        
- 
`newportZipUrl`—The relative URL (without the
          hostname) for the static resource that contains custom Newport styles for FlexCards.

        
- 
`OmniAnalyticsTrackingDebug`—If set to `true`, includes debugging data in Omnistudio Tracking
          Service records.

        
- 
`PerformAdvancedCheck`—If set to `true`, this configuration enables specific access to the
            `VlocityOpenInterface` Apex class used by remote
          action APIs for a user’s permission set or permission set group. This check is dependent
          on the `ApexClassCheck` and can only work if the
            `ApexClassCheck` setting is also set to `true`.

        
- 
`RetainDesignerSettingOnUpgrade`—If you're using the
          Standard Runtime and Package Designer, and you upgrade the package installation in your
          org, the designer switches to Standard Designer by default. To retain your preferred
          designer after the upgrade, set the `RetainDesignerSettingOnUpgrade` configuration to `true`.

#### Note

If you have enabled the Omnistudio standard designer by turning the
            Managed Package Designer setting off, you don’t require this configuration. This is only
            applicable to orgs that use the managed package designer with the standard
            runtime.

        
- 
`RollbackDRChanges`—If set to `true`, rolls back Data Mapper functionality changes. Use it
          if an upgrade causes some Data Mappers to stop working.

        
- 
`SkipUserProfileOnOSLoad`—If set to `true`, it doesn’t retrieve the user profile information when
          the Omniscript loads. If set to `false` or if the
          configuration is not available, it retrieves the user profile information when the
          Omniscript loads.

        
- 
`TheFirstInstalledOmniPackage`—Lists the namespace of
          the managed package that was installed first, which determines whether new or legacy
          Omnistudio features are available. Values are `omnistudio` for new features, or `vlocity_cmt`, `vlocity_ins`, or `vlocity_ps` for legacy features. Read-only.

        
- 
`Track_`component—If set to
            `true`, enables tracking for a component or component
          type in the Omnistudio Tracking Service.

        
- 
`TurnOffScaleCache`—If set to `true`, turns off the Scale Cache that Data Mappers and
          Integration Procedures use.

        
- 
`UserLocaleDateTime`—If set to `true`, processes date, time, and datetime field inputs using
          the user’s specific locale format rather than the standard list of predefined formats. Use
          it to ensure field inputs align with regional user expectations. See [Configure Date and Time Settings in Data
          Mappers](https://help.salesforce.com/s/articleView?id=xcloud.os_omni_interaction_config.htm&type=5&language=en_US).

        
- 
`EnableParentCompile`—If set to `true`, ensures metadata consistency and prevents migration
          failures for nested components. Use it to automate the compilation of parent elements and
          avoid manual rework during the migration process. See [Omnistudio Migration Prerequisites](https://help.salesforce.com/s/articleView?id=xcloud.os_migrate_oma_prereq.htm&type=5&language=en_US).

=== ARTICLE: meta_omniscript.htm ===
---
page_id: meta_omniscript.htm
title: OmniScript
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniscript.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniScript

Represents an OmniScript for the Discovery Framework, which
			guides users through sales, service, and other business processes. For Discovery
			Framework, the customization type is `discoveryframework`.
	

		
			

#### Important

Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations.

		

		

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName field. 

		

## File Suffix and Directory Location

			
			

OmniScript components have the suffix omniScript and are stored
				in the omniScripts folder.

		

		

## Version

			
			

OmniScript components are available in API version 56.0 and later.

		

		

## Special Access Rules

			
			

To use this metadata type, you must have an Omnistudio license and the Discovery Framework
				feature enabled in your Salesforce org.

		

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 
- 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| assessmentDefinitionMetadata | **Field Type** [AssessmentDefinitionMetadata[]](#AssessmentDefinitionMetadata) **Description** Metadata associated with an assessment definition. Available in API version 64.0 and later. |
| customHtmlTemplates | **Field Type** string **Description** The angular OmniScript template definitions. |
| customJavaScript | **Field Type** string **Description** The custom JavaScript used for an OmniScript. |
| designerCustomizationType | **Field Type** string **Description** The Omnistudio designer customization type. |
| elementTypeComponentMapping | **Field Type** string **Description** Overrides all elements of one type with a custom Lightning web component by mapping the element type to the Custom LWC. |
| isActive | **Field Type** boolean **Description** Indicates whether the OmniScript is active (`true`) or not (`false`). The default value is `false`. |
| isIntegrationProcedure | **Field Type** boolean **Description** Indicates whether OmniScript is an Integration Procedure (`true`) or OmniScript metadata (`false`). The default value is `false`. |
| isManagedUsingStdDesigner | **Field Type** boolean **Description** Indicates whether Omniscript is managed using standard designer (`true`) or not (`false`). Available in API version 64.0 and later. |
| isMetadataCacheDisabled | **Field Type** boolean **Description** Indicates whether metadata cache for the integration procedure is disabled (`true`) or not (`false`). The default value is `false`. |
| isOmniScriptEmbeddable | **Field Type** boolean **Description** Indicates whether the OmniScript can be embedded in other OmniScripts (`true`) or not (`false`). The default value is `false` |
| isTestProcedure | **Field Type** boolean **Description** Indicates whether OmniScript is a test procedure setting (`true`) or not (`false`). The default value is `false` |
| isWebCompEnabled | **Field Type** boolean **Description** Indicates whether web component OmniScript (not Angular) is enabled (`true`) or not (`false`). The default value is `false` |
| language | **Field Type** string **Description** Required. The language of the OmniScript. |
| lastPreviewPage | **Field Type** string **Description** The last page previewed in the OmniScript designer. |
| name | **Field Type** string **Description** Required. The name of the OmniScript. |
| namespace | **Field Type** string **Description** The namespace associated with this OmniScript record. |
| omniAssessmentTasks | **Field Type** [OmniAssessmentTaskMetadata](#subtype_OmniAssessmentTask)[] **Description** The omniAssessmentTasks associated with the OmniScript. Available in API version 63.0 and later. This field is available only if the Dynamic Assessment Access license is enabled. |
| omniProcessElements | **Field Type** [OmniProcessElement](#subtype_OmniProcessElement)[] **Description** The OmniProcessElements associated with the OmniScript. |
| omniProcessKey | **Field Type** string **Description** The integration procedure `Type_SubType` value. |
| omniProcessType | **Field Type** OmniProcessType (enumeration of type string) **Description** Required. Integration Procedure or OmniScript. Possible value is: `OmniScript` |
| overrideKey | **Field Type** string **Description** Reserved for future use. |
| propertySetConfig | **Field Type** string **Description** The configuration information associated with the OmniScript. |
| uniqueIndex | **Field Type** string **Description** The developer name of the assessment question in the OmniScript. This field is relevant only for Omniscripts with designerCustomizationType as `discoveryframework`. |
| requiredPermission | **Field Type** string **Description** The required permissions to execute the integration procedure. |
| responseCacheType | **Field Type** string **Description** Response cache used for the integration procedure (session or Org). |
| subType | **Field Type** string **Description** Required. The OmniScript sub type value. |
| type | **Field Type** string **Description** Required. The OmniScript type value. |
| uniqueName | **Field Type** string **Description** Required. The unique name for the OmniScript as Type_SubType_Language_VersionNumber. |
| versionNumber | **Field Type** string **Description** Required. The OmniScript version number. |
| webComponentKey | **Field Type** string **Description** Internal unique key for the generated Lightning Web Components (LWC). |

		

		

## AssessmentDefinitionMetadata

			
			

Represents the metadata associated with the assessment definition.

		

		

				
				
				
					
						

						

					

				

				
					
						

						

: 

: 

					

					
						

						

: 

: 

					

					
						

						

: 

: 

					

					
						

						

: 

: 

					

					
						

						

: 

: 

					

					
						

						

: 

: 

					

					
						

						

: 

: 

					

				

			
| Field Name | Description |
| --- | --- |
| approvalDateTime | **Field Type** dateTime **Description** The date and time when this version of the assessment definition was approved. |
| displayType | **Field Type** string **Description** The way this assessment is displayed in a user interface. |
| effectiveFromDate | **Field Type** dateTime **Description** The date and time from which the assessment definition becomes active and can be used. |
| effectiveToDate | **Field Type** dateTime **Description** The date and time until when this assessment definition is effective. |
| lastRevisedDateTime | **Field Type** dateTime **Description** The date and time when this assessment definition was last modified. |
| performerType | **Field Type** string **Description** The type of user, role, or system qualified or intended to complete the assessment. |
| purpose | **Field Type** string **Description** Reason for the assessment. |

		

## OmniAssessmentTaskMetadata

			
			

Represents the omni assessment tasks associated with the OmniScript.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 
: 
- 
- 
- 
- 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| name | **Field Type** string **Description** Required.The name of the omni assessment task. |
| status | **Field Type** picklist **Description** The status of the omni assessment task. Possible values are: `Completed` `InProgress`—In Progress `IsDefined`—Is Defined `NotStarted`—Not Started The default value is `IsDefined`. |
| uniqueName | **Field Type** string **Description** A unique name for the omni assessment task. |

		

		

## OmniProcessElement

			
			

Represents the OmniScript element associated with the OmniScript.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

					

				
| Field Name | Description |
| --- | --- |
| childElements | **Field Type** [OmniProcessElement](#subtype_OmniProcessElement)[] **Description** The child elements associated with the OmniProcessElement. |
| description | **Field Type** string **Description** The description of the OmniProcessElement. |
| designerCustomizationType | **Field Type** string **Description** The Omnistudio designer customization type. To create assessment questions using the Discovery Framework feature, use the customization type as `discoveryframework`. |
| discoveryFrameworkUsageType | **Field Type** string **Description** The usage type for industries that use the Discovery Framework. For example, the value for Health Cloud is `HcUsageType`. The value for no specific industry is `Default`. |
| embeddedOmniScriptKey | **Field Type** string **Description** The ID of the embedded OmniScript |
| isActive | **Field Type** boolean **Description** Indicates whether the status of the OmniProcessElement is active (`true`) or not (`false`). |
| isOmniScriptEmbeddable | **Field Type** boolean **Description** Indicates whether the OmniScript with the OmniProcessElement can be embedded in other OmniScripts (`true`) or not (`false`). |
| level | **Field Type** double **Description** The vertical level in which the OmniProcessElement occurs on the OmniScript. |
| name | **Field Type** string **Description** Required. The name of the OmniProcessElement. |
| omniProcessVersionNumber | **Field Type** double **Description** The related OmniProcess version. |
| parentElementName | **Field Type** string **Description** The name of the parent OmniProcessElement. |
| parentElementType | **Field Type** string **Description** The type of the parent OmniProcessElement. |
| propertySetConfig | **Field Type** textarea **Description** The property set of the OmniProcessElement. |
| sequenceNumber | **Field Type** double **Description** The horizontal level in which the OmniProcessElement occurs on the OmniScript. |
| type | **Field Type** string **Description** The OmniProcessElement type. For example, `Text` and `TextArea`. |
| uniqueIndex | **Field Type** string **Description** The developer name of the assessment question in the OmniScript. This field is relevant only for Omniscripts with designerCustomizationType as `discoveryframework`. |

		

		

## Declarative Metadata Sample Definition

			
			

Here’s an
				example
				of
				an
				Omniscript component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniScript
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<designerCustomizationType>Discovery Framework</designerCustomizationType>
	<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
	<elementTypeComponentMapping>{&quot;ElementTypeToHTMLTemplateList&quot;:[]}</elementTypeComponentMapping>
	<isActive>false</isActive>
	<isIntegrationProcedure>false</isIntegrationProcedure>
	<isManagedUsingStdDesigner>false</isManagedUsingStdDesigner>
	<isMetadataCacheDisabled>false</isMetadataCacheDisabled>
	<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
	<isTestProcedure>false</isTestProcedure>
	<isWebCompEnabled>true</isWebCompEnabled>
	<language>English</language>
	<name>Base Discovery Framework</name>
	<omniProcessElements>
		<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
		<isActive>true</isActive>
		<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
		<level>0.0</level>
		<name>Save-Responses</name>
		<omniProcessVersionNumber>0.0</omniProcessVersionNumber>
		<propertySetConfig>{&quot;controlWidth&quot;:12,&quot;label&quot;:&quot;Save&quot;,&quot;remoteClass&quot;:&quot;discoveryfrmwrk.StoreResponses&quot;,&quot;remoteMethod&quot;:&quot;invokeMethod&quot;,&quot;remoteOptions&quot;:{&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;},&quot;remoteTimeout&quot;:30000,&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;,&quot;sendJSONPath&quot;:&quot;&quot;,&quot;sendJSONNode&quot;:&quot;&quot;,&quot;responseJSONPath&quot;:&quot;&quot;,&quot;responseJSONNode&quot;:&quot;&quot;,&quot;extraPayload&quot;:{},&quot;inProgressMessage&quot;:&quot;In Progress&quot;,&quot;postMessage&quot;:&quot;Submitted Successfully&quot;,&quot;failureNextLabel&quot;:&quot;Continue&quot;,&quot;failureAbortLabel&quot;:&quot;Abort&quot;,&quot;failureGoBackLabel&quot;:&quot;Go Back&quot;,&quot;failureAbortMessage&quot;:&quot;Are you sure?&quot;,&quot;validationRequired&quot;:&quot;Step&quot;,&quot;redirectPageName&quot;:&quot;&quot;,&quot;redirectTemplateUrl&quot;:&quot;vlcAcknowledge.html&quot;,&quot;redirectNextLabel&quot;:&quot;Next&quot;,&quot;redirectNextWidth&quot;:3,&quot;redirectPreviousLabel&quot;:&quot;Previous&quot;,&quot;redirectPreviousWidth&quot;:3,&quot;showPersistentComponent&quot;:[true,false],&quot;show&quot;:null,&quot;HTMLTemplateId&quot;:&quot;&quot;,&quot;wpm&quot;:false,&quot;ssm&quot;:false,&quot;message&quot;:{},&quot;pubsub&quot;:false,&quot;svgSprite&quot;:&quot;&quot;,&quot;svgIcon&quot;:&quot;&quot;,&quot;errorMessage&quot;:{&quot;custom&quot;:[],&quot;default&quot;:null},&quot;enableDefaultAbort&quot;:false,&quot;enableActionMessage&quot;:false,&quot;useContinuation&quot;:false,&quot;businessCategory&quot;:&quot;&quot;,&quot;businessEvent&quot;:&quot;&quot;}</propertySetConfig>
		<sequenceNumber>1.0</sequenceNumber>
		<type>Remote Action</type>
	</omniProcessElements>
	<omniProcessElements>
		<childElements>
			<designerCustomizationType>Discovery Framework</designerCustomizationType>
			<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
			<isActive>true</isActive>
			<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
			<level>1.0</level>
			<name>Age</name>
			<omniProcessVersionNumber>0.0</omniProcessVersionNumber>
			<propertySetConfig>{&quot;controlWidth&quot;:12.0,&quot;label&quot;:&quot;Age v5&quot;,&quot;showInputWidth&quot;:false,&quot;inputWidth&quot;:12.0,&quot;required&quot;:false,&quot;repeat&quot;:false,&quot;repeatClone&quot;:false,&quot;repeatLimit&quot;:null,&quot;readOnly&quot;:false,&quot;defaultValue&quot;:null,&quot;help&quot;:false,&quot;helpText&quot;:&quot;&quot;,&quot;pattern&quot;:&quot;&quot;,&quot;ptrnErrText&quot;:&quot;&quot;,&quot;placeholder&quot;:&quot;&quot;,&quot;mask&quot;:null,&quot;show&quot;:null,&quot;conditionType&quot;:&quot;Hide if False&quot;,&quot;accessibleInFutureSteps&quot;:false,&quot;debounceValue&quot;:0.0,&quot;HTMLTemplateId&quot;:&quot;&quot;,&quot;hide&quot;:false,&quot;disOnTplt&quot;:false}</propertySetConfig>
			<sequenceNumber>2.0</sequenceNumber>
			<type>Number</type>
			<uniqueIndex>Age</uniqueIndex>
		</childElements>
		<childElements>
			<designerCustomizationType>Discovery Framework</designerCustomizationType>
			<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
			<isActive>true</isActive>
			<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
			<level>1.0</level>
			<name>First_Name</name>
			<omniProcessVersionNumber>0.0</omniProcessVersionNumber>
			<propertySetConfig>{&quot;controlWidth&quot;:12.0,&quot;label&quot;:&quot;First Name&quot;,&quot;showInputWidth&quot;:false,&quot;inputWidth&quot;:12.0,&quot;required&quot;:false,&quot;repeat&quot;:false,&quot;repeatClone&quot;:false,&quot;repeatLimit&quot;:null,&quot;readOnly&quot;:false,&quot;defaultValue&quot;:null,&quot;help&quot;:false,&quot;helpText&quot;:&quot;&quot;,&quot;mask&quot;:&quot;&quot;,&quot;pattern&quot;:&quot;&quot;,&quot;ptrnErrText&quot;:&quot;&quot;,&quot;minLength&quot;:0.0,&quot;maxLength&quot;:255.0,&quot;placeholder&quot;:&quot;&quot;,&quot;show&quot;:null,&quot;conditionType&quot;:&quot;Hide if False&quot;,&quot;accessibleInFutureSteps&quot;:false,&quot;debounceValue&quot;:0.0,&quot;HTMLTemplateId&quot;:&quot;&quot;,&quot;hide&quot;:false,&quot;disOnTplt&quot;:false}</propertySetConfig>
			<sequenceNumber>0.0</sequenceNumber>
			<type>Text</type>
			<uniqueIndex>First_Name</uniqueIndex>
		</childElements>
		<childElements>
			<designerCustomizationType>Discovery Framework</designerCustomizationType>
			<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
			<isActive>true</isActive>
			<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
			<level>1.0</level>
			<name>Last_Name</name>
			<omniProcessVersionNumber>0.0</omniProcessVersionNumber>
			<propertySetConfig>{&quot;controlWidth&quot;:12.0,&quot;label&quot;:&quot;Last Name&quot;,&quot;showInputWidth&quot;:false,&quot;inputWidth&quot;:12.0,&quot;required&quot;:false,&quot;repeat&quot;:false,&quot;repeatClone&quot;:false,&quot;repeatLimit&quot;:null,&quot;readOnly&quot;:false,&quot;defaultValue&quot;:null,&quot;help&quot;:false,&quot;helpText&quot;:&quot;&quot;,&quot;mask&quot;:&quot;&quot;,&quot;pattern&quot;:&quot;&quot;,&quot;ptrnErrText&quot;:&quot;&quot;,&quot;minLength&quot;:0.0,&quot;maxLength&quot;:255.0,&quot;placeholder&quot;:&quot;&quot;,&quot;show&quot;:null,&quot;conditionType&quot;:&quot;Hide if False&quot;,&quot;accessibleInFutureSteps&quot;:false,&quot;debounceValue&quot;:0.0,&quot;HTMLTemplateId&quot;:&quot;&quot;,&quot;hide&quot;:false,&quot;disOnTplt&quot;:false}</propertySetConfig>
			<sequenceNumber>1.0</sequenceNumber>
			<type>Text</type>
			<uniqueIndex>Last_Name</uniqueIndex>
		</childElements>
		<designerCustomizationType>Discovery Framework</designerCustomizationType>
		<discoveryFrameworkUsageType>0</discoveryFrameworkUsageType>
		<isActive>true</isActive>
		<isOmniScriptEmbeddable>false</isOmniScriptEmbeddable>
		<level>0.0</level>
		<name>Step1</name>
		<omniProcessVersionNumber>0.0</omniProcessVersionNumber>
		<propertySetConfig>{&quot;label&quot;:&quot;Base Discovery Framework&quot;,&quot;validationRequired&quot;:true,&quot;previousLabel&quot;:&quot;Previous&quot;,&quot;previousWidth&quot;:3,&quot;nextLabel&quot;:&quot;Enter&quot;,&quot;nextWidth&quot;:3,&quot;cancelLabel&quot;:&quot;Cancel&quot;,&quot;cancelMessage&quot;:&quot;Are you sure?&quot;,&quot;saveLabel&quot;:&quot;&quot;,&quot;saveMessage&quot;:&quot;&quot;,&quot;completeLabel&quot;:&quot;Complete&quot;,&quot;completeMessage&quot;:&quot;Are you sure you want to complete the script?&quot;,&quot;instruction&quot;:&quot;&quot;,&quot;showPersistentComponent&quot;:[true,false],&quot;remoteClass&quot;:&quot;&quot;,&quot;remoteMethod&quot;:&quot;&quot;,&quot;remoteTimeout&quot;:30000,&quot;remoteOptions&quot;:{},&quot;knowledgeOptions&quot;:{&quot;language&quot;:&quot;English&quot;,&quot;publishStatus&quot;:&quot;Online&quot;,&quot;keyword&quot;:&quot;&quot;,&quot;dataCategoryCriteria&quot;:&quot;&quot;,&quot;remoteTimeout&quot;:30000,&quot;typeFilter&quot;:&quot;&quot;},&quot;show&quot;:null,&quot;conditionType&quot;:&quot;Hide if False&quot;,&quot;HTMLTemplateId&quot;:&quot;&quot;,&quot;instructionKey&quot;:&quot;&quot;,&quot;chartLabel&quot;:null,&quot;allowSaveForLater&quot;:true,&quot;errorMessage&quot;:{&quot;custom&quot;:[],&quot;default&quot;:null},&quot;wpm&quot;:false,&quot;ssm&quot;:false,&quot;message&quot;:{},&quot;pubsub&quot;:false,&quot;businessCategory&quot;:&quot;&quot;,&quot;businessEvent&quot;:&quot;&quot;}</propertySetConfig>
		<sequenceNumber>0.0</sequenceNumber>
		<type>Step</type>
	</omniProcessElements>
	<omniProcessType>OmniScript</omniProcessType>
	<propertySetConfig>{&quot;persistentComponent&quot;:[{&quot;render&quot;:false,&quot;label&quot;:&quot;&quot;,&quot;remoteClass&quot;:&quot;&quot;,&quot;remoteMethod&quot;:&quot;&quot;,&quot;remoteTimeout&quot;:30000,&quot;remoteOptions&quot;:{&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;},&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;,&quot;sendJSONPath&quot;:&quot;&quot;,&quot;sendJSONNode&quot;:&quot;&quot;,&quot;responseJSONPath&quot;:&quot;&quot;,&quot;responseJSONNode&quot;:&quot;&quot;,&quot;id&quot;:&quot;vlcCart&quot;,&quot;itemsKey&quot;:&quot;cartItems&quot;,&quot;modalConfigurationSetting&quot;:{&quot;modalHTMLTemplateId&quot;:&quot;vlcProductConfig.html&quot;,&quot;modalController&quot;:&quot;ModalProductCtrl&quot;,&quot;modalSize&quot;:&quot;lg&quot;}},{&quot;render&quot;:false,&quot;dispOutsideOmni&quot;:false,&quot;label&quot;:&quot;&quot;,&quot;remoteClass&quot;:&quot;&quot;,&quot;remoteMethod&quot;:&quot;&quot;,&quot;remoteTimeout&quot;:30000,&quot;remoteOptions&quot;:{&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;},&quot;preTransformBundle&quot;:&quot;&quot;,&quot;postTransformBundle&quot;:&quot;&quot;,&quot;id&quot;:&quot;vlcKnowledge&quot;,&quot;itemsKey&quot;:&quot;knowledgeItems&quot;,&quot;modalConfigurationSetting&quot;:{&quot;modalHTMLTemplateId&quot;:&quot;&quot;,&quot;modalController&quot;:&quot;&quot;,&quot;modalSize&quot;:&quot;lg&quot;}}],&quot;allowSaveForLater&quot;:true,&quot;saveNameTemplate&quot;:null,&quot;saveExpireInDays&quot;:null,&quot;saveForLaterRedirectPageName&quot;:&quot;sflRedirect&quot;,&quot;saveForLaterRedirectTemplateUrl&quot;:&quot;vlcSaveForLaterAcknowledge.html&quot;,&quot;saveContentEncoded&quot;:false,&quot;saveObjectId&quot;:&quot;%ContextId%&quot;,&quot;saveURLPatterns&quot;:{},&quot;autoSaveOnStepNext&quot;:false,&quot;elementTypeToHTMLTemplateMapping&quot;:{},&quot;seedDataJSON&quot;:{},&quot;trackingCustomData&quot;:{},&quot;enableKnowledge&quot;:false,&quot;bLK&quot;:false,&quot;lkObjName&quot;:null,&quot;knowledgeArticleTypeQueryFieldsMap&quot;:{},&quot;timeTracking&quot;:false,&quot;hideStepChart&quot;:false,&quot;mergeSavedData&quot;:false,&quot;visualforcePagesAvailableInPreview&quot;:{},&quot;cancelType&quot;:&quot;SObject&quot;,&quot;allowCancel&quot;:true,&quot;cancelSource&quot;:&quot;%ContextId%&quot;,&quot;cancelRedirectPageName&quot;:&quot;OmniScriptCancelled&quot;,&quot;cancelRedirectTemplateUrl&quot;:&quot;vlcCancelled.html&quot;,&quot;consoleTabLabel&quot;:&quot;New&quot;,&quot;wpm&quot;:false,&quot;ssm&quot;:false,&quot;message&quot;:{},&quot;pubsub&quot;:false,&quot;autoFocus&quot;:false,&quot;currencyCode&quot;:&quot;&quot;,&quot;showInputWidth&quot;:false,&quot;rtpSeed&quot;:false,&quot;consoleTabTitle&quot;:null,&quot;consoleTabIcon&quot;:&quot;custom:custom18&quot;,&quot;errorMessage&quot;:{&quot;custom&quot;:[]},&quot;stylesheet&quot;:{&quot;newport&quot;:&quot;&quot;,&quot;lightning&quot;:&quot;&quot;,&quot;newportRtl&quot;:&quot;&quot;,&quot;lightningRtl&quot;:&quot;&quot;},&quot;stepChartPlacement&quot;:&quot;right&quot;,&quot;disableUnloadWarn&quot;:true,&quot;scrollBehavior&quot;:&quot;auto&quot;}</propertySetConfig>
	<subType>Framework</subType>
	<type>Discovery</type>
	<uniqueName>Discovery_Framework_English_1</uniqueName>
	<versionNumber>1.0</versionNumber>
</OmniScript>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
    xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniScript</name>
    </types>
    <version>63.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

		

		

## Usage Type

			
			

Before you retrieve or deploy Discovery Framework OmniScripts, we recommend that you
				review these considerations.

			
				
- If the DesignerCustomizationType of the OmniScript is
						`discoveryframework`, then the questions
					in the OmniScript must be within the <uniqueIndex> tag in
					the metadata definition file.

				
- When deploying the OmniScript of type Discovery Framework, enable Discovery
					Framework Metadata Enabled setting.

				
- OmniScripts of type Discovery Framework don't support IDX Workbench.

				
- If any question associated with the OmniScript doesn’t exist in the target org
					or, if the active version of that question doesn’t exist in the target org, then
					deploying the OmniScript fails.

=== ARTICLE: meta_omniscriptdefinition.htm ===
---
page_id: meta_omniscriptdefinition.htm
title: OmniscriptDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omniscriptdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniscriptDefinition

Represents the header configuration of an
      Omniscript. Each row represents an Omniscript's header configurations, such as its type,
      subtype, and name. An Omniscript helps build guided digital experiences. This object stores
      primary information about an Omniscript to render it at runtime.

    

    

## Parent Type

      
      

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm)
        metadata type and inherits its fullName field.

    

    

## File Suffix and Directory Location

      
      

OmniscriptDefinition components have the suffix .omniscriptDefinition
        and are stored in the omniscriptDefinitions folder.

      
    

    

## Version

      
      

OmniscriptDefinition components are available in API version 67.0 and later.

    

    

## Special Access Rules

      
      

To use this metadata type, you must have an Omnistudio license and the Discovery Framework
        feature enabled in your Salesforce org.

    

    

## Fields

      
      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

            

          

        
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** The user-defined text added to the Description field when creating an Omniscript. |
| designerCustomizationType | **Field Type** string **Description** The name of the customization applied to an Omniscript when used with Discovery Framework. |
| isActive | **Field Type** boolean **Description** Indicates whether the Omniscript is ready for use or in use on a Lightning or Experience Cloud page. The default value is `false`. |
| isManagedUsingStdDesigner | **Field Type** boolean **Description** Indicates whether the Omniscript or Integration Procedure is created or updated using the Omnistudio standard designer. The default value is `true`. |
| isOmniscriptReusable | **Field Type** boolean **Description** Indicates whether the Omniscript can be embedded in another Omniscript. The default value is `false`. |
| masterLabel | **Field Type** string **Description** The user-defined name of the Omniscript. |
| omniscriptDefinitionElement | **Field Type** [OmniscriptDefinitionElement](#OmniscriptDefinitionElement) **Description** The nested OmniScript definition element metadata associated with this OmniScript definition. Each row represents a configurable element of an Omniscript, such as a text block, an input field, or an action. These elements are the building blocks for creating an Omniscript. |
| omniscriptLanguage | **Field Type** string **Description** The language used in the Omniscript. Together with Type and Subtype, this forms the unique identifier of an Omniscript. |
| omniscriptName | **Field Type** string **Description** The user-defined name of the Omniscript. |
| overrideKey | **Field Type** string **Description** The unique name of the Omniscript that overrides the existing Omniscript. |
| propertySetConfig | **Field Type** [OmniScriptPropertySetConfig](#OmniScriptPropertySetConfig) **Description** The properties of an Omniscript configured via the Omniscript Designer, stored as a JSON. At runtime, this JSON is read to render the Omniscript as per its configurations. |
| references | **Field Type** string **Description** The references to related OmniScript resources or records. |
| subType | **Field Type** string **Description** The user-defined value, that together with Type and Language forms the unique identifier for an Omniscript. |
| type | **Field Type** string **Description** The user-defined value, that together with Subtype and Language forms the unique identifier for an Omniscript. |

    

    
    

## OmniscriptDefinitionElement

      
      
      
      
      

          
          
          
            
              

              

            

          

          
          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

: 

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

: 

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

            

          
          

        
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** The user-defined description added to the element. |
| designerCustomizationType | **Field Type** string **Description** The name of the customization applied to an Omniscript when used with features enabled outside of Omnistudio. |
| embeddedOmniscriptKey | **Field Type** string **Description** The key of the Omniscript embedded in the existing Omniscript. |
| isActive | **Field Type** boolean **Description** Indicates whether the element is used at runtime (`true`) or not (`false`). The default value is (`false`). |
| isOmniscriptReusable | **Field Type** boolean **Description** Indicates whether the Omniscript is reusable (`true`) or not (`false`) based on the user's selection of the Reuse checkbox in Omniscript Setup. The default value is (`false`). |
| level | **Field Type** double **Description** The depth of an element in the Omniscript configuration when it's nested within other elements. |
| omniScriptDefElementName | **Field Type** string **Description** The name of the element used in an Omniscript. |
| parentElementName | **Field Type** string **Description** The parent element name used to identify this OmniScript artifact in metadata. |
| parentElementType | **Field Type** OmniscriptElementType (enumeration of type string) **Description** The parent element type value that determines how this OmniScript setting is interpreted. **Values** Values are: `Aggregate` `Block` `Checkbox` `Currency` `Date` `Disclosure` `Email` `File` `Filter` `Formula` `Geolocation` `Headline` `Image` `Lookup` `Multi-select` `Number` `OmniScript` `Password` `Radio` `Range` `Select` `Signature` `Step` `Submit` `Telephone` `Text` `Time` `URL` `Validation` |
| propertySetConfig | **Field Type** [OmniScriptElementPropertySetConfig](#OmniScriptElementPropertySetConfig) **Description** The properties of an element within an Omniscript configured via the Omniscript Designer, stored as a JSON. At runtime, this JSON is read to render the element as per its configurations. |
| sequenceNumber | **Field Type** double **Description** The position of the element in relation to its sibling elements in the Omniscript's configuration. |
| type | **Field Type** OmniscriptElementType (enumeration of type string) **Description** The type of element added to the Omniscript. **Values** Values are: `Aggregate` `Block` `Checkbox` `Currency` `Date` `Disclosure` `Email` `File` `Filter` `Formula` `Geolocation` `Headline` `Image` `Lookup` `Multi-select` `Number` `OmniScript` `Password` `Radio` `Range` `Select` `Signature` `Step` `Submit` `Telephone` `Text` `Time` `URL` `Validation` |

      
    

    
    

## OmniScriptElementPropertySetConfig

      
      
      
      
      

          
          
          
            
              

              

            

          

          
          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
          

        
| Field Name | Description |
| --- | --- |
| BStandalone | **Field Type** boolean **Description** Indicates whether bstandalone is enabled for the OmniScript configuration. |
| accessibleInFutureSteps | **Field Type** boolean **Description** Indicates whether accessible in future steps is enabled for the OmniScript configuration. |
| allOrNone | **Field Type** boolean **Description** Indicates whether all or none is enabled for the OmniScript configuration. |
| allowClear | **Field Type** boolean **Description** Indicates whether the Clear action is available for the OmniScript element. |
| allowDelete | **Field Type** boolean **Description** Indicates whether the Delete action is available for the OmniScript element. |
| allowEdit | **Field Type** boolean **Description** Indicates whether the Edit action is available for the OmniScript element. |
| allowNegative | **Field Type** boolean **Description** Indicates whether negative values are allowed for the OmniScript element. |
| allowNew | **Field Type** boolean **Description** Indicates whether creating new records is allowed for the OmniScript element. |
| allowSaveChanges | **Field Type** boolean **Description** Indicates whether users can save changes made in the OmniScript element. |
| allowSaveForLater | **Field Type** boolean **Description** Indicates whether users can save progress and resume the OmniScript later. |
| applyIfError | **Field Type** boolean **Description** Indicates whether apply if error is enabled for the OmniScript configuration. |
| ariaLevel | **Field Type** int **Description** The ARIA level value used for accessibility semantics in the OmniScript interface. |
| attachmentList | **Field Type** string **Description** The attachment list collection that maps or groups related OmniScript data. |
| attachmentName | **Field Type** string **Description** The attachment name used to identify this OmniScript artifact in metadata. |
| attachmentParentId | **Field Type** string **Description** The attachment parent id used to reference related OmniScript resources or records. |
| autoSaveChanges | **Field Type** boolean **Description** Indicates whether auto save changes is enabled for the OmniScript configuration. |
| autoSaveLabel | **Field Type** string **Description** The auto save label text shown in the OmniScript user interface. |
| bundle | **Field Type** string **Description** The bundle used to configure OmniScript behavior. |
| businessCategory | **Field Type** string **Description** The business category value that determines how this OmniScript setting is interpreted. |
| businessEvent | **Field Type** string **Description** The business event value that determines how this OmniScript setting is interpreted. |
| callFrequency | **Field Type** int **Description** The call frequency setting that controls limits, layout, or processing behavior. |
| cancelLabel | **Field Type** string **Description** The cancel label text shown in the OmniScript user interface. |
| cancelMessage | **Field Type** string **Description** The cancel message text shown in the OmniScript user interface. |
| chartLabel | **Field Type** string **Description** The chart label text shown in the OmniScript user interface. |
| checkLabel | **Field Type** string **Description** The check label text shown in the OmniScript user interface. |
| clearValue | **Field Type** boolean **Description** Indicates whether clear value is enabled for the OmniScript configuration. |
| collapse | **Field Type** boolean **Description** Indicates whether collapse is enabled for the OmniScript configuration. |
| completeLabel | **Field Type** string **Description** The complete label text shown in the OmniScript user interface. |
| completeMessage | **Field Type** string **Description** The complete message text shown in the OmniScript user interface. |
| conditionType | **Field Type** string **Description** The condition type value that determines how this OmniScript setting is interpreted. |
| configurationErrorMessage | **Field Type** string **Description** The configuration error message text shown in the OmniScript user interface. |
| confirm | **Field Type** boolean **Description** Indicates whether confirm is enabled for the OmniScript configuration. |
| confirmationOnDelete | **Field Type** boolean **Description** Indicates whether confirmation on delete is enabled for the OmniScript configuration. |
| contentParentId | **Field Type** string **Description** The content parent id used to reference related OmniScript resources or records. |
| contentVersionList | **Field Type** string **Description** The content version list collection that maps or groups related OmniScript data. |
| controlWidth | **Field Type** int **Description** The control width setting that controls layout, limits, or processing order. |
| controllingField | **Field Type** string **Description** The controlling field that identifies the data source or target used by OmniScript. |
| customAttributes | **Field Type** string **Description** The custom attributes used to configure OmniScript behavior. |
| dataJSON | **Field Type** boolean **Description** Indicates whether data json is enabled for the OmniScript configuration. |
| dataJsonPath | **Field Type** string **Description** The data json path used to read or write runtime data. |
| dataProcessorFunction | **Field Type** string **Description** The data processor function logic expression used during OmniScript processing. |
| dataRaptorInputParameters | **Field Type** string **Description** The data raptor input parameters value used by OmniScript at runtime. |
| dataSource | **Field Type** string **Description** The data source that identifies the data source or target used by OmniScript. |
| dataType | **Field Type** string **Description** The data type value that determines how this OmniScript setting is interpreted. |
| dateFormat | **Field Type** string **Description** The date format value that determines how this OmniScript setting is interpreted. |
| dateTimeFormat | **Field Type** string **Description** The date time format value that determines how this OmniScript setting is interpreted. |
| dateType | **Field Type** string **Description** The date type value that determines how this OmniScript setting is interpreted. |
| debounceValue | **Field Type** int **Description** The debounce value setting that controls limits, layout, or processing behavior. |
| defaultMatrixResult | **Field Type** string **Description** The default matrix result setting that controls limits, layout, or processing behavior. |
| defaultValue | **Field Type** string **Description** The default value setting that controls limits, layout, or processing behavior. |
| deleteFailedMessage | **Field Type** string **Description** The delete failed message text shown in the OmniScript user interface. |
| deleteLabel | **Field Type** string **Description** The delete label text shown in the OmniScript user interface. |
| deleteSObject | **Field Type** string **Description** The delete sobject value used by OmniScript at runtime. |
| disOnTplt | **Field Type** boolean **Description** Indicates whether dis on tplt is enabled for the OmniScript configuration. |
| disableDataFilter | **Field Type** boolean **Description** Indicates whether disable data filter is enabled for the OmniScript configuration. |
| displayCurrencyCode | **Field Type** boolean **Description** Indicates whether display currency code is enabled for the OmniScript configuration. |
| displayHeight | **Field Type** int **Description** The display height setting that controls limits, layout, or processing behavior. |
| displayWidth | **Field Type** int **Description** The display width setting that controls layout, limits, or processing order. |
| docList | **Field Type** string **Description** The doc list collection that maps or groups related OmniScript data. |
| docuSignReturnUrl | **Field Type** string **Description** The docu sign return url value used by OmniScript at runtime. |
| docuSignTemplatesGroup | **Field Type** string **Description** The docu sign templates group reference used by OmniScript integrations or rendering. |
| docuSignTemplatesGroupSig | **Field Type** string **Description** The docu sign templates group sig reference used by OmniScript integrations or rendering. |
| dynamicProperties | **Field Type** string **Description** The dynamic properties used to configure OmniScript behavior. |
| editLabel | **Field Type** string **Description** The edit label text shown in the OmniScript user interface. |
| editMode | **Field Type** boolean **Description** Indicates whether edit mode is enabled for the OmniScript configuration. |
| elementErrorMap | **Field Type** string **Description** The element error map collection that maps or groups related OmniScript data. |
| elementName | **Field Type** string **Description** The element name used to identify this OmniScript artifact in metadata. |
| elementValueMap | **Field Type** string **Description** The element value map collection that maps or groups related OmniScript data. |
| emailBody | **Field Type** string **Description** The email body text shown to users in the OmniScript interface. |
| emailInformation | **Field Type** string **Description** The email information value used by OmniScript at runtime. |
| emailSubject | **Field Type** string **Description** The email subject text shown to users in the OmniScript interface. |
| emailTemplateInformation | **Field Type** string **Description** The email template information reference used by OmniScript integrations or rendering. |
| enableActionMessage | **Field Type** boolean **Description** Indicates whether action message is enabled for this OmniScript configuration. |
| enableCaption | **Field Type** boolean **Description** Indicates whether caption is enabled for this OmniScript configuration. |
| enableDefaultAbort | **Field Type** boolean **Description** Indicates whether default abort is enabled for this OmniScript configuration. |
| enableGoogleMapsAutocomplete | **Field Type** boolean **Description** Indicates whether google maps autocomplete is enabled for this OmniScript configuration. |
| enableLookup | **Field Type** boolean **Description** Indicates whether lookup is enabled for this OmniScript configuration. |
| entityIsDeletedMessage | **Field Type** string **Description** The entity is deleted message text shown in the OmniScript user interface. |
| errorMessage | **Field Type** string **Description** The error message text shown in the OmniScript user interface. |
| expression | **Field Type** string **Description** The expression logic expression used during OmniScript processing. |
| extraPayload | **Field Type** string **Description** The extra payload value used by OmniScript at runtime. |
| failureAbortLabel | **Field Type** string **Description** The failure abort label text shown in the OmniScript user interface. |
| failureAbortMessage | **Field Type** string **Description** The failure abort message text shown in the OmniScript user interface. |
| failureGoBackLabel | **Field Type** string **Description** The failure go back label text shown in the OmniScript user interface. |
| failureNextLabel | **Field Type** string **Description** The failure next label text shown in the OmniScript user interface. |
| fileAttachments | **Field Type** string **Description** The file attachments collection that maps or groups related OmniScript data. |
| googleAddressCountry | **Field Type** string **Description** The google address country value used by OmniScript at runtime. |
| googleMapsAPIKey | **Field Type** string **Description** The google maps apikey value used by OmniScript at runtime. |
| googleTransformation | **Field Type** string **Description** The google transformation value used by OmniScript at runtime. |
| headingLevel | **Field Type** int **Description** The heading level setting that controls layout, limits, or processing order. |
| help | **Field Type** boolean **Description** Indicates whether help is enabled for the OmniScript configuration. |
| helpText | **Field Type** string **Description** The help text text shown in the OmniScript user interface. |
| hide | **Field Type** boolean **Description** Indicates whether hide is enabled for the OmniScript configuration. |
| hideEditButton | **Field Type** boolean **Description** Indicates whether hide edit button is enabled for the OmniScript configuration. |
| hideGroupSep | **Field Type** boolean **Description** Indicates whether hide group sep is enabled for the OmniScript configuration. |
| hideLabel | **Field Type** boolean **Description** Indicates whether hide label is enabled for the OmniScript configuration. |
| hideMap | **Field Type** boolean **Description** Indicates whether hide map is enabled for the OmniScript configuration. |
| horizontalMode | **Field Type** boolean **Description** Indicates whether horizontal mode is enabled for the OmniScript configuration. |
| htmlTemplateId | **Field Type** string **Description** The html template id used to reference related OmniScript resources or records. |
| iconName | **Field Type** string **Description** The icon name used to identify this OmniScript artifact in metadata. |
| iconPosition | **Field Type** string **Description** The icon position value used by OmniScript at runtime. |
| iconVariant | **Field Type** string **Description** The icon variant value used by OmniScript at runtime. |
| ignoreCache | **Field Type** boolean **Description** Indicates whether ignore cache is enabled for the OmniScript configuration. |
| imageCountInRow | **Field Type** int **Description** The image count in row setting that controls layout, limits, or processing order. |
| inProgressMessage | **Field Type** string **Description** The in progress message text shown in the OmniScript user interface. |
| inputWidth | **Field Type** int **Description** The input width setting that controls layout, limits, or processing order. |
| instruction | **Field Type** string **Description** The instruction value used by OmniScript at runtime. |
| instructionKey | **Field Type** string **Description** The instruction key used to reference related OmniScript resources or records. |
| integrationProcedureKey | **Field Type** string **Description** The integration procedure key used to reference related OmniScript resources or records. |
| invalidIdMessage | **Field Type** string **Description** The invalid id message text shown in the OmniScript user interface. |
| invokeMode | **Field Type** string **Description** The invoke mode value that determines how this OmniScript setting is interpreted. |
| knowledgeOptions | **Field Type** string **Description** The knowledge options value used by OmniScript at runtime. |
| label | **Field Type** string **Description** The label text shown in the OmniScript user interface. |
| loginAction | **Field Type** string **Description** The login action value used by OmniScript at runtime. |
| lwcComponentOverride | **Field Type** string **Description** The lwc component override value used by OmniScript at runtime. |
| lwcName | **Field Type** string **Description** The lwc name used to identify this OmniScript artifact in metadata. |
| mask | **Field Type** string **Description** The mask value used by OmniScript at runtime. |
| matrixInputParameters | **Field Type** string **Description** The matrix input parameters value used by OmniScript at runtime. |
| max | **Field Type** string **Description** The max setting that controls limits, layout, or processing behavior. |
| maxDate | **Field Type** string **Description** The max date setting that controls limits, layout, or processing behavior. |
| maxDisplay | **Field Type** int **Description** The max display setting that controls limits, layout, or processing behavior. |
| maxLength | **Field Type** int **Description** The max length setting that controls layout, limits, or processing order. |
| maxTime | **Field Type** string **Description** The max time setting that controls limits, layout, or processing behavior. |
| message | **Field Type** string **Description** The message text shown in the OmniScript user interface. |
| messages | **Field Type** string **Description** The messages value used by OmniScript at runtime. |
| min | **Field Type** string **Description** The min setting that controls limits, layout, or processing behavior. |
| minDate | **Field Type** string **Description** The min date setting that controls limits, layout, or processing behavior. |
| minLength | **Field Type** int **Description** The min length setting that controls layout, limits, or processing order. |
| minTime | **Field Type** string **Description** The min time setting that controls limits, layout, or processing behavior. |
| mode | **Field Type** string **Description** The mode value that determines how this OmniScript setting is interpreted. |
| modelDateFormat | **Field Type** string **Description** The model date format value that determines how this OmniScript setting is interpreted. |
| modelTimeFormat | **Field Type** string **Description** The model time format value that determines how this OmniScript setting is interpreted. |
| multiple | **Field Type** boolean **Description** Indicates whether multiple is enabled for the OmniScript configuration. |
| namedCredential | **Field Type** string **Description** The named credential value used by OmniScript at runtime. |
| newItemLabel | **Field Type** string **Description** The new item label text shown in the OmniScript user interface. |
| newLabel | **Field Type** string **Description** The new label text shown in the OmniScript user interface. |
| nextLabel | **Field Type** string **Description** The next label text shown in the OmniScript user interface. |
| nextWidth | **Field Type** int **Description** The next width setting that controls layout, limits, or processing order. |
| objectAction | **Field Type** string **Description** The object action that identifies the data source or target used by OmniScript. |
| omniScriptRootConfig | **Field Type** [OmniScriptPropertySetConfig](#OmniScriptPropertySetConfig) **Description** The omniscript root config used to configure OmniScript behavior. |
| optionHeight | **Field Type** int **Description** The option height setting that controls limits, layout, or processing behavior. |
| optionSource | **Field Type** string **Description** The option source that identifies the data source or target used by OmniScript. |
| optionWidth | **Field Type** int **Description** The option width setting that controls layout, limits, or processing order. |
| options | **Field Type** string **Description** The options value used by OmniScript at runtime. |
| orgWideEmailAddress | **Field Type** string **Description** The org wide email address value used by OmniScript at runtime. |
| padding | **Field Type** int **Description** The padding value used by OmniScript at runtime. |
| pattern | **Field Type** string **Description** The pattern value used by OmniScript at runtime. |
| placeholder | **Field Type** string **Description** The placeholder text shown in the OmniScript user interface. |
| postMessage | **Field Type** string **Description** The post message text shown in the OmniScript user interface. |
| postTransformBundle | **Field Type** string **Description** The post transform bundle used to configure OmniScript behavior. |
| preTransformBundle | **Field Type** string **Description** The pre transform bundle used to configure OmniScript behavior. |
| previousLabel | **Field Type** string **Description** The previous label text shown in the OmniScript user interface. |
| previousWidth | **Field Type** int **Description** The previous width setting that controls layout, limits, or processing order. |
| ptrnErrText | **Field Type** string **Description** The ptrn err text text shown in the OmniScript user interface. |
| pubsub | **Field Type** boolean **Description** Indicates whether pubsub is enabled for the OmniScript configuration. |
| radioLabels | **Field Type** string **Description** The radio labels value used by OmniScript at runtime. |
| radioLabelsWidth | **Field Type** int **Description** The radio labels width setting that controls layout, limits, or processing order. |
| rangeHigh | **Field Type** int **Description** The range high value used by OmniScript at runtime. |
| rangeLow | **Field Type** int **Description** The range low value used by OmniScript at runtime. |
| readOnly | **Field Type** boolean **Description** Indicates whether read only is enabled for the OmniScript configuration. |
| recordAction | **Field Type** string **Description** The record action value used by OmniScript at runtime. |
| redirectNextLabel | **Field Type** string **Description** The redirect next label text shown in the OmniScript user interface. |
| redirectNextWidth | **Field Type** int **Description** The redirect next width setting that controls layout, limits, or processing order. |
| redirectPageName | **Field Type** string **Description** The redirect page name used to identify this OmniScript artifact in metadata. |
| redirectPreviousLabel | **Field Type** string **Description** The redirect previous label text shown in the OmniScript user interface. |
| redirectPreviousWidth | **Field Type** int **Description** The redirect previous width setting that controls layout, limits, or processing order. |
| redirectTemplateUrl | **Field Type** string **Description** The redirect template url reference used by OmniScript integrations or rendering. |
| remoteClass | **Field Type** string **Description** The remote class value used by OmniScript at runtime. |
| remoteConfirmMsg | **Field Type** string **Description** The remote confirm msg value used by OmniScript at runtime. |
| remoteMethod | **Field Type** string **Description** The remote method logic expression used during OmniScript processing. |
| remoteOptions | **Field Type** string **Description** The remote options value used by OmniScript at runtime. |
| remoteTimeout | **Field Type** int **Description** The remote timeout setting that controls limits, layout, or processing behavior. |
| repeat | **Field Type** boolean **Description** Indicates whether repeat is enabled for the OmniScript configuration. |
| repeatClone | **Field Type** boolean **Description** Indicates whether repeat clone is enabled for the OmniScript configuration. |
| repeatLimit | **Field Type** int **Description** The repeat limit value used by OmniScript at runtime. |
| replace | **Field Type** boolean **Description** Indicates whether replace is enabled for the OmniScript configuration. |
| required | **Field Type** boolean **Description** Indicates whether required is enabled for the OmniScript configuration. |
| responseJSONNode | **Field Type** string **Description** The response jsonnode value used by OmniScript at runtime. |
| responseJSONPath | **Field Type** string **Description** The response jsonpath used to read or write runtime data. |
| restMethod | **Field Type** string **Description** The rest method logic expression used during OmniScript processing. |
| restOptions | **Field Type** string **Description** The rest options value used by OmniScript at runtime. |
| restPath | **Field Type** string **Description** The rest path used to read or write runtime data. |
| restoreDefaultValuesOnCancel | **Field Type** boolean **Description** Indicates whether restore default values on cancel is enabled for the OmniScript configuration. |
| sanitize | **Field Type** boolean **Description** Indicates whether sanitize is enabled for the OmniScript configuration. |
| saveChangesLabel | **Field Type** string **Description** The save changes label text shown in the OmniScript user interface. |
| saveLabel | **Field Type** string **Description** The save label text shown in the OmniScript user interface. |
| saveMessage | **Field Type** string **Description** The save message text shown in the OmniScript user interface. |
| selectCheckBox | **Field Type** string **Description** The select check box value used by OmniScript at runtime. |
| selectMode | **Field Type** string **Description** The select mode value that determines how this OmniScript setting is interpreted. |
| selectSobject | **Field Type** string **Description** The select sobject value used by OmniScript at runtime. |
| sendJSONNode | **Field Type** string **Description** The send jsonnode value used by OmniScript at runtime. |
| sendJSONPath | **Field Type** string **Description** The send jsonpath used to read or write runtime data. |
| show | **Field Type** string **Description** The show value used by OmniScript at runtime. |
| showInputWidth | **Field Type** boolean **Description** Indicates whether show input width is enabled for the OmniScript configuration. |
| showPersistentComponent | **Field Type** string **Description** The show persistent component value used by OmniScript at runtime. |
| showPopup | **Field Type** boolean **Description** Indicates whether show popup is enabled for the OmniScript configuration. |
| signerInformation | **Field Type** string **Description** The signer information value used by OmniScript at runtime. |
| sobjectMapping | **Field Type** string **Description** The sobject mapping collection that maps or groups related OmniScript data. |
| ssm | **Field Type** boolean **Description** Indicates whether ssm is enabled for the OmniScript configuration. |
| staticDocList | **Field Type** string **Description** The static doc list collection that maps or groups related OmniScript data. |
| step | **Field Type** int **Description** The step value used by OmniScript at runtime. |
| subLabel | **Field Type** string **Description** The sub label text shown in the OmniScript user interface. |
| sumElement | **Field Type** string **Description** The sum element value used by OmniScript at runtime. |
| svgIcon | **Field Type** string **Description** The svg icon value used by OmniScript at runtime. |
| svgSprite | **Field Type** string **Description** The svg sprite value used by OmniScript at runtime. |
| targetFilter | **Field Type** string **Description** The target filter that identifies the data source or target used by OmniScript. |
| targetId | **Field Type** string **Description** The target id used to reference related OmniScript resources or records. |
| targetLWCLayout | **Field Type** string **Description** The target lwclayout that identifies the data source or target used by OmniScript. |
| targetType | **Field Type** string **Description** The target type value that determines how this OmniScript setting is interpreted. |
| templateName | **Field Type** string **Description** The template name used to identify this OmniScript artifact in metadata. |
| text | **Field Type** string **Description** The text text shown in the OmniScript user interface. |
| textKey | **Field Type** string **Description** The text key text shown in the OmniScript user interface. |
| timeFormat | **Field Type** string **Description** The time format value that determines how this OmniScript setting is interpreted. |
| timeInterval | **Field Type** int **Description** The time interval value used by OmniScript at runtime. |
| timeType | **Field Type** string **Description** The time type value that determines how this OmniScript setting is interpreted. |
| timezone | **Field Type** string **Description** The timezone value used by OmniScript at runtime. |
| type | **Field Type** string **Description** The type value that determines how this OmniScript setting is interpreted. |
| typeAheadKey | **Field Type** string **Description** The type ahead key used to reference related OmniScript resources or records. |
| uploadContDoc | **Field Type** boolean **Description** Indicates whether upload cont doc is enabled for the OmniScript configuration. |
| useContinuation | **Field Type** boolean **Description** Indicates whether use continuation is enabled for the OmniScript configuration. |
| useDataJson | **Field Type** boolean **Description** Indicates whether use data json is enabled for the OmniScript configuration. |
| useTemplate | **Field Type** boolean **Description** Indicates whether use template is enabled for the OmniScript configuration. |
| validateExpression | **Field Type** string **Description** The validate expression logic expression used during OmniScript processing. |
| validationRequired | **Field Type** string **Description** The validation required value used by OmniScript at runtime. |
| valueSvgMap | **Field Type** string **Description** The value svg map collection that maps or groups related OmniScript data. |
| variant | **Field Type** string **Description** The variant value used by OmniScript at runtime. |
| wpm | **Field Type** boolean **Description** Indicates whether wpm is enabled for the OmniScript configuration. |
| xmlPostTransformBundle | **Field Type** string **Description** The xml post transform bundle used to configure OmniScript behavior. |
| xmlPreTransformBundle | **Field Type** string **Description** The xml pre transform bundle used to configure OmniScript behavior. |

      
    

    
    

## OmniScriptPropertySetConfig

      
      
      
      
      

          
          
          
            
              

              

            

          

          
          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
            
              

              

: 

: 

            

          
          

        
| Field Name | Description |
| --- | --- |
| accessibilityToggle | **Field Type** boolean **Description** Indicates whether accessibility toggle is enabled for the OmniScript configuration. |
| allowCancel | **Field Type** boolean **Description** Indicates whether cancel is enabled for this OmniScript configuration. |
| allowSaveChanges | **Field Type** boolean **Description** Indicates whether users can save changes made in the OmniScript element. |
| allowSaveForLater | **Field Type** boolean **Description** Indicates whether users can save progress and resume the OmniScript later. |
| autoFocus | **Field Type** boolean **Description** Indicates whether auto focus is enabled for the OmniScript configuration. |
| autoSaveChanges | **Field Type** boolean **Description** Indicates whether auto save changes is enabled for the OmniScript configuration. |
| autoSaveOnStepNext | **Field Type** boolean **Description** Indicates whether auto save on step next is enabled for the OmniScript configuration. |
| bulk | **Field Type** boolean **Description** Indicates whether bulk is enabled for the OmniScript configuration. |
| cancelRedirectPageName | **Field Type** string **Description** The cancel redirect page name used to identify this OmniScript artifact in metadata. |
| cancelRedirectTemplateUrl | **Field Type** string **Description** The cancel redirect template url reference used by OmniScript integrations or rendering. |
| cancelSource | **Field Type** string **Description** The cancel source that identifies the data source or target used by OmniScript. |
| cancelType | **Field Type** string **Description** The cancel type value that determines how this OmniScript setting is interpreted. |
| consoleTabIcon | **Field Type** string **Description** The console tab icon value used by OmniScript at runtime. |
| consoleTabLabel | **Field Type** string **Description** The console tab label text shown in the OmniScript user interface. |
| consoleTabTitle | **Field Type** string **Description** The console tab title text shown in the OmniScript user interface. |
| currencyCode | **Field Type** string **Description** The currency code value used by OmniScript at runtime. |
| currentLanguage | **Field Type** string **Description** The current language value used by OmniScript at runtime. |
| disableUnloadWarn | **Field Type** boolean **Description** Indicates whether disable unload warn is enabled for the OmniScript configuration. |
| dynamicProperties | **Field Type** string **Description** The dynamic properties used to configure OmniScript behavior. |
| elementTypeToHTMLTemplateMapping | **Field Type** string **Description** The element type to htmltemplate mapping value that determines how this OmniScript setting is interpreted. |
| enableKnowledge | **Field Type** boolean **Description** Indicates whether knowledge is enabled for this OmniScript configuration. |
| errorMessage | **Field Type** string **Description** The error message text shown in the OmniScript user interface. |
| hideStepChart | **Field Type** boolean **Description** Indicates whether hide step chart is enabled for the OmniScript configuration. |
| knowledgeArticleTypeQueryFieldsMap | **Field Type** string **Description** The knowledge article type query fields map value that determines how this OmniScript setting is interpreted. |
| lkObjName | **Field Type** string **Description** The lk obj name used to identify this OmniScript artifact in metadata. |
| mergeSavedData | **Field Type** boolean **Description** Indicates whether merge saved data is enabled for the OmniScript configuration. |
| message | **Field Type** string **Description** The message text shown in the OmniScript user interface. |
| persistentComponent | **Field Type** string **Description** The persistent component value used by OmniScript at runtime. |
| pubsub | **Field Type** boolean **Description** Indicates whether pubsub is enabled for the OmniScript configuration. |
| rtpSeed | **Field Type** boolean **Description** Indicates whether rtp seed is enabled for the OmniScript configuration. |
| saveContentEncoded | **Field Type** boolean **Description** Indicates whether save content encoded is enabled for the OmniScript configuration. |
| saveExpireInDays | **Field Type** int **Description** The save expire in days value used by OmniScript at runtime. |
| saveForLaterRedirectPageName | **Field Type** string **Description** The save for later redirect page name used to identify this OmniScript artifact in metadata. |
| saveForLaterRedirectTemplateUrl | **Field Type** string **Description** The save for later redirect template url reference used by OmniScript integrations or rendering. |
| saveNameTemplate | **Field Type** string **Description** The save name template used to identify this OmniScript artifact in metadata. |
| saveObjectId | **Field Type** string **Description** The object ID used when saving OmniScript data. |
| saveURLPatterns | **Field Type** string **Description** The save urlpatterns value used by OmniScript at runtime. |
| scrollBehavior | **Field Type** string **Description** The scroll behavior value used by OmniScript at runtime. |
| seedDataJSON | **Field Type** string **Description** The seed data json value used by OmniScript at runtime. |
| showInputWidth | **Field Type** boolean **Description** Indicates whether show input width is enabled for the OmniScript configuration. |
| ssm | **Field Type** boolean **Description** Indicates whether ssm is enabled for the OmniScript configuration. |
| stepChartPlacement | **Field Type** string **Description** The step chart placement value used by OmniScript at runtime. |
| stylesheet | **Field Type** string **Description** The stylesheet value used by OmniScript at runtime. |
| timeTracking | **Field Type** boolean **Description** Indicates whether time tracking is enabled for the OmniScript configuration. |
| trackingCustomData | **Field Type** string **Description** The tracking custom data value used by OmniScript at runtime. |
| visualforcePagesAvailableInPreview | **Field Type** string **Description** The visualforce pages available in preview value used by OmniScript at runtime. |
| wpm | **Field Type** boolean **Description** Indicates whether wpm is enabled for the OmniScript configuration. |

      
    

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of the OmniscriptDefinition component.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniscriptDefinition xmlns="http://soap.sforce.com/2006/04/metadata">
    <isActive>true</isActive>
    <isManagedUsingStdDesigner>true</isManagedUsingStdDesigner>
    <isOmniscriptReusable>false</isOmniscriptReusable>
    <masterLabel>Simple_Os_English Updated</masterLabel>
    <omniscriptDefinitionElement>
        <isActive>true</isActive>
        <isOmniscriptReusable>false</isOmniscriptReusable>
        <level>1.0</level>
        <omniScriptDefElementName>TextBlock1</omniScriptDefElementName>
        <sequenceNumber>0.0</sequenceNumber>
        <type>Text Block</type>
    </omniscriptDefinitionElement>
    <omniscriptDefinitionElement>
        <isActive>true</isActive>
        <isOmniscriptReusable>false</isOmniscriptReusable>
        <level>0.0</level>
        <omniScriptDefElementName>Step1</omniScriptDefElementName>
        <sequenceNumber>0.0</sequenceNumber>
        <type>Step</type>
    </omniscriptDefinitionElement>
    <omniscriptLanguage>English</omniscriptLanguage>
    <omniscriptName>SimpleOs</omniscriptName>
    <references>[]</references>
    <subType>Os</subType>
    <type>Simple</type>
</OmniscriptDefinition>
```

      

The following is an example `package.xml` that references the previous definition.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniscriptDefinition</name>
    </types>
    <version>68.0</version>
</Package>
```

    

    
    

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*`
        (asterisk) in the package.xml manifest file. For information about
        using the manifest file, see [Deploying and
          Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_omnistudiosettings.htm ===
---
page_id: meta_omnistudiosettings.htm
title: OmniStudioSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omnistudiosettings.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniStudioSettings

Represents the settings that help administrators turn on
			specific Omnistudio features and capabilities at the organization level.
	

	

	

## Parent Type and Manifest	Access

		
			

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field. 

			

In the package manifest, all the settings metadata types for the org are accessed
				using the “Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

OmniStudioSettings values are stored in the .settings
				file in the settings folder. The .settings
				files are different from other named components, because there is only one settings
				file for each settings component.

	

	

## Version

		
		

OmniStudioSettings components are available in API version 64.0 and later.

	

	

## Special Access Rules

		
		
		
	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
							

							

: 

: 

						

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
							

							

: 

: 

						

				

			
| Field Name | Description |
| --- | --- |
| disableRollbackFlagsPref | **Field Type** boolean **Description** Indicates whether to turn on rollback flag preferences for Omnistudio settings (`true`) or not (`false`). The default value is`false`. When enabled, rollback flags are disabled to prevent automatic rollback of configuration changes. This setting helps retain designer settings during upgrades and provides control over rollback behavior for Omnistudio configurations. It works in conjunction with the `RetainDesignerSettingOnUpgrade` setting to manage upgrade behavior. |
| enableOaEventInternalWrites | **Field Type** boolean **Description** Indicates whether to turn on internal write operations for Omnistudio events (`true`) or not (`false`). The default value is`false`. This setting manages internal event handling, and controls how Omnistudio processes and stores event data. It also enables internal event persistence and processing capabilities for Omnistudio applications. |
| enableOaEventNotifications | **Field Type** boolean **Description** Indicates whether to turn on the Omnistudio event notification system (`true`) or not (`false`). The default value is `false`. This setting manages notifications for Omnistudio events, and enables real-time communication and alerts for application activities. It supports platform events, custom notifications, and integration with Salesforce notification systems. |
| enableOaForCore | **Field Type** boolean **Description** Indicates whether to turn on Omnistudio core builder functionality and the standard Omnistudio designer experience (`true`) or not (`false`). The default value is `false`. This setting is important for organizations that use managed packages with specific namespace requirements (omnistudio, vlocity_cmt, vlocity_ins, vlocity_ps) and version constraints that are greater than v63.0. |
| enableOmniGlobalAutoNumberPref | **Field Type** boolean **Description** Indicates whether to turn on global auto-numbering preferences for Omnistudio (`true`) or not (`false`). The default value is `false`. This setting controls the automatic generation and management of sequential numbers for Omnistudio components and records. It also provides centralized auto-numbering management for consistent record identification across all Omnistudio components. |
| enableOmniStudioContentTest | **Field Type** boolean **Description** Indicates whether to turn on Omnistudio content testing capabilities (`true`) or not (`false`). The default value is `false`. When enabled, users can test Omnistudio content and configurations within the platform. This setting supports testing of OmniScripts, Flexcards, DataRaptors, and Integration Procedures in a controlled environment. It’s typically used for development and quality assurance to validate content before deployment. Available in API version 65.0 and later. |
| enableOmniStudioDrVersion | **Field Type** boolean **Description** Indicates whether to turn on Omnistudio Data Mapper version functionality within Omnistudio (`true`) or not (`false`). The default value is `false`. Omnistudio Data Mapper version management features are essential for data transformation and integration workflows. This setting also enables version control for Omnistudio Data Mapper transformations, allowing organizations to maintain multiple versions of data mapping configurations. |
| enableOmniStudioMetadata | **Field Type** boolean **Description** Indicates whether to turn on metadata functionality in the organization (`true`) or not (`false`). The default value is `false`. When enabled, the organization can access and manage Omnistudio metadata components through the Metadata and Tooling API. This setting can’t be enabled if metadata component unique names contain spaces or special characters. After it’s enabled, the setting can’t be disabled. |
| enableStandardOmniStudioRuntime | **Field Type** boolean **Description** Indicates whether to enable the standard Omnistudio runtime environment (`true`) or not (`false`). The default value is `false`. When enabled, the standard runtime engine processes Omnistudio applications and content. This setting supports migration from managed-package Omnistudio runtimes to the standard runtime.This setting requires Omnistudio managed package to be properly configured. Available in API version 65.0 and later. |

	

		

## Declarative Metadata Sample Definition

		
			

This example shows a sample OmniStudioSettings component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniStudioSettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <enableOmniStudioMetadata>true</enableOmniStudioMetadata>
    <enableOmniStudioContentTest>false</enableOmniStudioContentTest>
    <enableStandardOmniStudioRuntime>false</enableStandardOmniStudioRuntime><enableOmniStudioDrVersion>false</enableOmniStudioDrVersion>
    <enableOaForCore>false</enableOaForCore>
    <enableOaEventNotifications>false</enableOaEventNotifications>
    <enableOaEventInternalWrites>false</enableOaEventInternalWrites>
    <enableOmniGlobalAutoNumberPref>true</enableOmniGlobalAutoNumberPref>
    <disableRollbackFlagsPref>false</disableRollbackFlagsPref>
</OmniStudioSettings>
```

			

Here's an example `package.xml` that references the
				previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?><Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>OmniStudio</members>
        <name>Settings</name>
    </types>
    <version>67.0</version>
</Package>

```

		

		

## Wildcard Support in the Manifest File

			
			

The wildcard character `*` (asterisk) in the
					package.xml manifest file doesn’t apply to metadata types
				for feature settings. The wildcard applies only when retrieving all settings, not
				for an individual setting. For details, see [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm). For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_omnitrackinggroup.htm ===
---
page_id: meta_omnitrackinggroup.htm
title: OmniTrackingGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omnitrackinggroup.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniTrackingGroup

Represents a group of FlexCard and OmniScript components that have
			their user interactions tracked together in OmniAnalytics.

		
			

#### Note

This metadata type is part of Omnistudio Standard, not Omnistudio for Vlocity.

			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName field. 

	

## File Suffix and Directory Location

		
		

OmniTrackingGroup components have the suffix .OmniTrackingGroup and are stored in the OmniTrackingGroups folder.

	

	

## Version

		
		

OmniTrackingGroup components are available in API version 60.0 and later.

	

	

## Special Access Rules

		
			

Using OmniAnalytics requires having an Omnistudio license and enabling OmniAnalytics in
				Setup.

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

#### 

#### 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

- 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** A description of the OmniTrackingGroup. |
| developerName | **Field Type** string **Description** Required. The unique name of the OmniTrackingGroup in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| endDate | **Field Type** date **Description** The date when the OmniTrackingGroup became inactive. |
| groupType | **Field Type** OmniTrackingGroupType (enumeration of type string) **Description** Required. Specifies whether this OmniTrackingGroup sends tracking data to a third-party Analytics system such as Google Analytics. Values are: `External`—A third-party Analytics system is used. `Internal`—No third-party Analytics system is used. |
| isActive | **Field Type** boolean **Description** Required. Specifies whether the OmniTrackingGroup is active. |
| masterLabel | **Field Type** string **Description** Required. The unique master label of the OmniTrackingGroup. This internal label doesn’t get translated. |
| maxAgeInDays | **Field Type** int **Description** The maximum number of days the group and its analytics data is active beyond which the data is deleted. |
| omniExtTrackingDef | **Field Type** string **Description** The ID of the related OmniExtTrackingDef object. Required if GroupType is set to `External`. |
| omniTrackingComponentDefs | **Field Type** [OmniTrackingComponentDef[]](#OmniTrackingComponentDef) **Description** The OmniTrackingComponentDef objects related to this OmniTrackingGroup. |
| omniTrackingGroupKey | **Field Type** string **Description** A UUID generated internally by Salesforce to uniquely identify an OmniTrackingGroup record across all orgs. |
| startDate | **Field Type** date **Description** The date when the OmniTrackingGroup became active. |

	

		

## OmniTrackingComponentDef

		
		

Represents a FlexCard or OmniScript that is a member of an OmniTrackingGroup, which tracks user
				interactions in OmniAnalytics.

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

- 
- 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

#### 

#### 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| componentType | **Field Type** OmniAnalyticsComponentType (enumeration of type string) **Description** Required. The type of component for which user interactions are tracked. Values are: `Flexcard` `Omniscript` |
| componentVersion | **Field Type** double **Description** Required. The version of the FlexCard or OmniScript. |
| developerName | **Field Type** string **Description** Required. The unique name of the OmniTrackingComponentDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| masterLabel | **Field Type** string **Description** Required. The unique master label of the OmniTrackingComponentDef. This internal label doesn’t get translated. |
| omniTrackingComponentDefKey | **Field Type** string **Description** A UUID generated internally by Salesforce to uniquely identify an OmniTrackingComponentDef record across all orgs. |
| omniTrackingGroup | **Field Type** string **Description** The ID of the related OmniTrackingGroup object. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of an OmniTrackingGroup component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OmniTrackingGroup xmlns="http://soap.sforce.com/2006/04/metadata">
    <developerName>Purchase_Tracking</developerName>
    <groupType>Internal</groupType>
    <isActive>true</isActive>
    <masterLabel>Purchase_Tracking</masterLabel>
    <omniTrackingComponentDefs>
        <componentType>Omniscript</componentType>
        <componentVersion>2</componentVersion>
        <developerName>Purchase_Funnel</developerName>
        <masterLabel>Purchase_Funnel</masterLabel>
    </omniTrackingComponentDefs>
</OmniTrackingGroup>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OmniTrackingGroup</name>
    </types>
    <version>60.0</version>
</Package>
```

		

		
		

## Wildcard Support in the Manifest File

			
			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: omnistudio_apex_reference.htm ===
---
page_id: omnistudio_apex_reference.htm
title: Omnistudio Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omnistudio Apex Reference

Apex is a strongly typed, object-oriented programming language that allows developers
    to execute flow and transaction control statements on the Salesforce Platform server, in
    conjunction with calls to the API. Omnistudio Apex reference includes built-in Apex classes and
    interfaces, grouped by namespace. 

- 
**[omnistudiocore Namespace](./apex_namespace_omnistudiocore.htm.md)**  

Omnistudiocore namespace and its classes are for internal use only.

=== ARTICLE: omnistudio_apis.htm ===
---
page_id: omnistudio_apis.htm
title: Omnistudio Business REST APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omnistudio Business REST APIs

Omnistudio Business APIs are RESTful APIs that are sometimes available as Apex classes
    and methods. You can access Omnistudio APIs using REST endpoints. These REST APIs follow similar
    conventions as Connect REST APIs.

    

#### Note

These APIs have been deprecated as of API version 55.0. In API version
        55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

    
      

OmniStudio provides a suite of services, components, and data model objects that combine to
        create Industry Cloud applications. Create guided interactions using data from your
        Salesforce org and external sources.

      

To understand the architecture, authentication, rate limits, and how the requests and
        responses work, see [Connect REST API Developer
          Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm).

    

  

- 
**[Expression Set](./omnistudio_calculation_procedure_apis_resources.htm.md)**  

An expression set allow complex math to be configured within       OmniStudio. Expression set is also known as calculation Procedure or evaluation     service.

- 
**[Decision Matrix](./omnistudio_decision_matrix_apis_resources.htm.md)**  

A decision matrix is a table that looks up information using multiple       input dimensions and returns the corresponding output value. Decision matrix is also known as       calculation matrix.

- 
**[Data Mapper](./omnistudio_data_mapper_apis.htm.md)**  

The Data Mapper is a mapping tool that you use to read, transform, and write Salesforce     data. Omnistudio Data Mapper is time-efficient and easier to maintain for data processing. Data     Mappers typically supply data to Omniscripts, Integration Procedures, Flexcards, and Apex     classes, and write the related updates to Salesforce.

- 
**[Integration Procedure](./omnistudio_integration_procedure_apis.htm.md)**  

Integration procedures can read and write data from Salesforce and external systems by     using the REST API calls and Apex classes. An Integration Procedure can be called from an     Omniscript, an API, or an Apex method, and can be a data source for a Flexcard. Integration     Procedures can handle multiple data sources to read and write data.

#### See Also

- [Omnistudio Foundation Guide](https://volt.my.salesforce.com/sfc/p/o0000000IKm8/a/3m000000nWyq/erXZ51SEaoeirtkzzlQnC5GehNzqvrSTTU3I1rOd3gs)

=== ARTICLE: omnistudio_apis_requests.htm ===
---
page_id: omnistudio_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_calculation_procedure_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Here’s a list of Expression Set API (also known as Calculation Procedure) request
    bodies.

    
      

#### Note

These APIs have been deprecated as of API version 55.0. In API version
        55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

    

  

- 
**[Calculation Procedure Version Definition Input](./connect_requests_calculation_procedure_version_definition_input.htm.md)**  

Input representation of the expression set version     definition.

- 
**[Calculation Procedure Step Input](./connect_requests_calculation_procedure_step_input.htm.md)**  

Input representation for the expression set version     steps.

- 
**[Resource Input](./connect_requests_resource_input.htm.md)**  

Input representation of the expression set resource (variable or       constant).

- 
**[Simulation Config Input](./connect_requests_simulation_config_input.htm.md)**  

Input information of the configuration version to run a       simulation.

- 
**[Simulation Evaluation Service Input](./connect_requests_simulation_eval_service_input.htm.md)**  

Input representation to run simulation on an expression       set.

- 
**[Simulation Context Input](./connect_requests_simulation_context_input.htm.md)**  

Input representation of context details for   simulation.

- 
**[Simulation Variable Input](./connect_requests_simulation_variable_input.htm.md)**  

Input information of the input variable and its     value.

- 
**[Simulation Version Info Input](./connect_requests_simulation_version_info_input.htm.md)**  

Input information of the version details to run     simulation.

=== ARTICLE: omnistudio_apis_requests_1.htm ===
---
page_id: omnistudio_apis_requests_1.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_requests_1.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_decision_matrix_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Here’s a list of Decision Matrix API (also known as Calculation Matrix) request
    bodies.

- 
**[Decision Matrix Columns Input](./connect_requests_decision_matrix_columns_input.htm.md)**  

Input representation of the information to manage columns in relation       to a decision matrix.

- 
**[Decision Matrix Column Input](./connect_requests_decision_matrix_column.htm.md)**  

Input representation of the information required to add, update, or       delete columns in a decision matrix.

- 
**[Decision Matrix Rows Input](./connect_requests_decision_matrix_rows_input.htm.md)**  

Input representation of the information to manage rows in relation to       the decision matrix version.

- 
**[Decision Matrix Row Input](./connect_requests_decision_matrix_row_input.htm.md)**  

Input representation of the information required to add, update, or       delete rows in a decision matrix version.

=== ARTICLE: omnistudio_apis_resources.htm ===
---
page_id: omnistudio_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_calculation_procedure_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Expression Set API (also known as Calculation Procedure)
    resources.

- 
**[Calculation Procedure](./connect_resources_calculation_procedure.htm.md)**  

Retrieve the details for a given expression set (also known as       calculation procedure) record.

- 
**[Calculation Procedures](./connect_resources_calculation_procedures.htm.md)**  

Get a list of expression sets (also known as calculation procedure)       based on a search text. The API returns a maximum of ten expression set records that contain       the specified keyword.

- 
**[Calculation Procedure Version Definition (Activate, Get)](./connect_resources_get_activate_calc_procedure_version.htm.md)**  

Retrieve the definition of an expression set (also known as       calculation procedure) version record. Activate an expression set version     record.

- 
**[Calculation Procedure Version Definition (Save As, Update)](./connect_resources_save_update_calc_procedure_version.htm.md)**  

Update the details of an expression set (also known as calculation       procedure) version record. Save an expression set version record as a new expression set       version record.

- 
**[Simulations](./connect_resources_simulations.htm.md)**  

Retrieve the input variables of an expression set that are required to       run a simulation. Run a simulation. An expression set, also known as calculation     procedure, is a group of steps that perform mathematical operations and     transformations.

=== ARTICLE: omnistudio_apis_resources_1.htm ===
---
page_id: omnistudio_apis_resources_1.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_resources_1.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_decision_matrix_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Decision Matrix API (also known as Calculation Matrix)
    resources.

- 
**[Decision Matrix](./connect_resources_decision_matrix.htm.md)**  

Retrieve the details for a given decision matrix record (also known as       calculation matrix).

- 
**[Decision Matrices](./connect_resources_decision_matrices.htm.md)**  

Get a list of decision matrices ( also known as calculation matrix)       based on a search text. The API returns a maximum of ten decision matrices records that       contain the specified keyword.

- 
**[Decision Matrix Columns](./connect_resources_decision_matrix_columns.htm.md)**  

Retrieve a list of or manage columns in a decision matrix. Use this       resource to add new columns, or update or delete existing columns in a decision     matrix.

- 
**[Decision Matrix Version Rows](./connect_resources_decision_matrix_version_rows.htm.md)**  

Retrieve a paginated list of or manage rows in a decision matrix       version. Use this resource to add new rows, or update or delete existing rows in a decision       matrix version.

=== ARTICLE: omnistudio_apis_responses.htm ===
---
page_id: omnistudio_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_calculation_procedure_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Expression Set API (also known as Calculation Procedure) response
    bodies.

    
      

#### Note

These APIs have been deprecated as of API version 55.0. In API version
        55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

    

  

- 
**[Calculation Procedure Detail Output](./connect_responses_calculation_procedure_detail_output.htm.md)**  

Output representation of the expression set details.

- 
**[Calculation Procedure List Output](./connect_responses_calculation_procedure_list_output.htm.md)**  

Output representation of the expression set result     list.

- 
**[Calculation Procedure Output](./connect_responses_calculation_procedure_output.htm.md)**  

Output representation of the expression sets details.

- 
**[Calculation Procedure Variable Output](./connect_responses_calculation_procedure_variable_output.htm.md)**  

Details of the variables of an expression set.

- 
**[Calculation Procedure Activation Output](./connect_responses_calculation_procedure_activation_output.htm.md)**  

Output representation of the calculation procedure version record       activation.

- 
**[Calculation Procedure Version Definition Output](./connect_responses_calculation_procedure_version_definition_output.htm.md)**  

Output representation of the expression set version     definition.

- 
**[Resource List Output](./connect_responses_resource_list_output.htm.md)**  

Output representation of the expression set version record resource       list.

- 
**[Resource Output](./connect_responses_resource_output.htm.md)**  

Output representation of variables or constants used in the       calculation procedure version definition.

- 
**[Root Step List Output](./connect_responses_root_step_list_output.htm.md)**  

Output representation of the first step of the expression set version       record.

- 
**[Calculation Procedure Step Map Output](./connect_responses_calculation_procedure_step_map_output.htm.md)**  

Output representation of the step details of the expression set       version record.

- 
**[Calculation Procedure Step Output](./connect_responses_calculation_procedure_step_output.htm.md)**  

Output representation of the steps of the expression set version       record.

- 
**[Simulation Error Output](./connect_responses_simulation_error_output.htm.md)**  

Error code and details.

- 
**[Simulation Eval Service Output](./connect_responses_simulation_eval_service_output.htm.md)**  

Output representation of the simulation run on an expression       set.

- 
**[Simulation Runtime Output](./connect_responses_simulation_runtime_output.htm.md)**  

Output representation of the results of an expression set from the       simulation.

- 
**[Simulation Step Explainability Message Output](./connect_responses_simulation_step_explainability_message_output.htm.md)**  

Output representation of a decision explanation message for a step       from the simulation.

- 
**[Simulation Input Variable Basic](./connect_responses_simulation_input_variable_basic.htm.md)**  

Output representation of the details of an input variable of a       simulation.

- 
**[Simulation Input Variables Result List](./connect_responses_simulation_input_variables_result_list.htm.md)**  

Output representation of the list of input variables of a       simulation.

- 
**[Simulation Step Additional Info Output](./connect_responses_simulation_step_additional_info_output.htm.md)**  

Information about the decision matrix or sub expression used in a       step.

- 
**[Simulation Step Result Output](./connect_responses_simulation_step_result_output.htm.md)**  

Output representation of the simulation results of a     step.

- 
**[Simulation Variable Output](./connect_responses_simulation_variable_output.htm.md)**  

Output representation of a simulation variable and its     value.

=== ARTICLE: omnistudio_apis_responses_1.htm ===
---
page_id: omnistudio_apis_responses_1.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_apis_responses_1.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_decision_matrix_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Decision Matrix API (also known as Calculation Matrix) response
    bodies.

- 
**[Decision Matrix Basic](./connect_responses_decision_matrix_basic.htm.md)**  

Output representation of the decision matrices     details.

- 
**[Decision Matrix Result](./connect_responses_decision_matrix_result.htm.md)**  

Output representation of the decision matrix details.

- 
**[Decision Matrix Result List](./connect_responses_decision_matrix_result_list.htm.md)**  

Output representation of the decision matrix result     list.

- 
**[Decision Matrix Variable](./connect_responses_decision_matrix_variable.htm.md)**  

Details of the input or output variables of a decision     matrix.

- 
**[Decision Matrix Columns Output](./connect_responses_decision_matrix_columns_output.htm.md)**  

Output representation of columns of a decision     matrix.

- 
**[Decision Matrix Column Output](./connect_responses_decision_matrix_column_output.htm.md)**  

Representation of the details of a column in a decision     matrix.

- 
**[Decision Matrix Rows Output](./connect_responses_decision_matrix_rows_output.htm.md)**  

Output representation of rows of a decision matrix     version.

- 
**[Decision Matrix Row Output](./connect_responses_decision_matrix_row_output.htm.md)**  

Representation of the details of a row in a decision matrix       version.

- 
**[Decision Matrix Output](./connect_responses_decision_matrix_output.htm.md)**  

Output representation the action performed on a decision matrix       version.

=== ARTICLE: omnistudio_calculation_procedure_apis_resources.htm ===
---
page_id: omnistudio_calculation_procedure_apis_resources.htm
title: Expression Set
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_calculation_procedure_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set

An expression set allow complex math to be configured within
      OmniStudio. Expression set is also known as calculation Procedure or evaluation
    service.

    
      

#### Note

These APIs have been deprecated as of API version 55.0. In API version
        55.0 and later, use the new [Business APIs in Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine_connect_apis.htm).

      

Sometimes you need more than a simple mathematical equation, and configuring expression set
        enables you to run just this kind of comprehensive and detailed set of mathematical
        processing steps. 

      

To handle many factors, values, and calculations, a expression set can call up one or more
        decision matrices. These are simply lookup tables that take a unique input or set of inputs
        and return an output or set of outputs. Use a decision matrix whenever you need to look up
        data.

    

  

- 
**[Resources](./omnistudio_apis_resources.htm.md)**  

Here’s a list of Expression Set API (also known as Calculation Procedure)     resources.

- 
**[Request Bodies](./omnistudio_apis_requests.htm.md)**  

Here’s a list of Expression Set API (also known as Calculation Procedure) request     bodies.

- 
**[Response Bodies](./omnistudio_apis_responses.htm.md)**  

Here’s a list of Expression Set API (also known as Calculation Procedure) response     bodies.

=== ARTICLE: omnistudio_data_mapper_apis.htm ===
---
page_id: omnistudio_data_mapper_apis.htm
title: Data Mapper
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_data_mapper_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Mapper

The Data Mapper is a mapping tool that you use to read, transform, and write Salesforce
    data. Omnistudio Data Mapper is time-efficient and easier to maintain for data processing. Data
    Mappers typically supply data to Omniscripts, Integration Procedures, Flexcards, and Apex
    classes, and write the related updates to Salesforce.

    
      

Omnistudio provides these types of Data Mappers.

      
        
- Extract—Read data from Salesforce objects and JSON output or XML with field
          mappings. Formulas are supported.

        
- Turbo Extract—Read data from a single Salesforce object type, with support for
          fields from related objects. Formulas aren’t supported.

        
- Transform—Perform intermediate data transformations without reading from or
          writing to Salesforce. Formulas are supported.

        
- Load—Create and update Salesforce data from JSON or XML input. Formulas are
          supported.

      

    

  

- 
**[Resources](./omnistudio_data_mapper_apis_resources.htm.md)**  

Learn more about the available Data Mapper API resources.

- 
**[Request Bodies](./omnistudio_data_mapper_apis_requests.htm.md)**  

Learn more about the available Data Mapper API request bodies.

- 
**[Response Bodies](./omnistudio_data_mapper_apis_responses.htm.md)**  

Learn more about the available Data Mapper API response bodies.

#### See Also

- [Omnistudio Data Mappers](https://help.salesforce.com/s/articleView?id=xcloud.os_omnistudio_dataraptors_45587.htm&language=en_US)

=== ARTICLE: omnistudio_data_mapper_apis_requests.htm ===
---
page_id: omnistudio_data_mapper_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_data_mapper_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available Data Mapper API request bodies.

- 
**[Data Mapper Clear Cache Input](./connect_requests_datamapper_cache_input_param.htm.md)**  

Input representation of the details to clear the cache of the data mappers.

- 
**[Data Mapper Details](./connect_requests_data_mapper_details.htm.md)**  

Input representation of the data mapper details to clear the cache for.

- 
**[Data Mapper Execution Input](./connect_requests_data_mapper_execution_input.htm.md)**  

Input representation of the execution details of a data mapper.

- 
**[Data Mapper Execute Input Data](./connect_requests_data_mapper_execute_input_data.htm.md)**  

Input representation of the list of custom data for the execution of the data     mapper.

- 
**[Data Mapper Execution Options](./connect_requests_data_mapper_execution_options.htm.md)**  

Input representation of the optional parameters for the data mapper     execution.

=== ARTICLE: omnistudio_data_mapper_apis_resources.htm ===
---
page_id: omnistudio_data_mapper_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_data_mapper_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Data Mapper API resources.

- 
**[Data Mapper Clear Cache (POST)](./connect_resources_data_mapper_clear_cache.htm.md)**  

Clear the execution cache for the specified data mappers.

- 
**[Data Mapper Execution (POST)](./connect_resources_data_mapper_execution.htm.md)**  

Execute a data mapper from Apex classes by specifying the name of the data mapper along     with additional inputs and options.

=== ARTICLE: omnistudio_data_mapper_apis_responses.htm ===
---
page_id: omnistudio_data_mapper_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_data_mapper_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_data_mapper_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available Data Mapper API response bodies.

- 
**[Data Mapper Cache Details](./connect_responses_datamapper_clear_cache_output.htm.md)**  

Output representation of the cache details that are cleared for the specified data     mappers.

- 
**[Data Mapper Cache Response](./connect_responses_datamapper_clear_cache_response.htm.md)**  

Output representation of the response with error message and status.

- 
**[Data Mapper Execution Details](./connect_responses_data_mapper_execution_output.htm.md)**  

Output representation of the execution details of a data mapper.

- 
**[Data Mapper Execution Response](./connect_responses_data_mapper_execution_response_output.htm.md)**  

Output representation of the response with error message, status, and response     type.

=== ARTICLE: omnistudio_decision_matrix_apis_resources.htm ===
---
page_id: omnistudio_decision_matrix_apis_resources.htm
title: Decision Matrix
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_decision_matrix_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix

A decision matrix is a table that looks up information using multiple
      input dimensions and returns the corresponding output value. Decision matrix is also known as
      calculation matrix.

- 
**[Resources](./omnistudio_apis_resources_1.htm.md)**  

Here’s a list of Decision Matrix API (also known as Calculation Matrix)     resources.

- 
**[Request Bodies](./omnistudio_apis_requests_1.htm.md)**  

Here’s a list of Decision Matrix API (also known as Calculation Matrix) request     bodies.

- 
**[Response Bodies](./omnistudio_apis_responses_1.htm.md)**  

Here’s a list of Decision Matrix API (also known as Calculation Matrix) response     bodies.

=== ARTICLE: omnistudio_flow_metadata_api.htm ===
---
page_id: omnistudio_flow_metadata_api.htm
title: Flow for Omnistudio
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Omnistudio

Represents the metadata associated with a flow. Use a flow to create an application
    that takes users through a series of pages to query and update records in the database. You can
    also execute logic and provide branching capability based on user input to build dynamic
    applications.

    

## FlowActionCall

      
      

Omnistudio exposes additional actionType values for the FlowActionCall Metadata type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid value only for Omnistudio include: `executeIntegrationProcedure`—Executes an Integration Procedure with Agentforce configured. Available in API version 64.0 and later. |

=== ARTICLE: omnistudio_integration_procedure_apis.htm ===
---
page_id: omnistudio_integration_procedure_apis.htm
title: Integration Procedure
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_integration_procedure_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Procedure

Integration procedures can read and write data from Salesforce and external systems by
    using the REST API calls and Apex classes. An Integration Procedure can be called from an
    Omniscript, an API, or an Apex method, and can be a data source for a Flexcard. Integration
    Procedures can handle multiple data sources to read and write data.

- 
**[Resources](./omnistudio_integration_procedure_apis_resources.htm.md)**  

Learn more about the available Integration Procedure API resources.

- 
**[Request Bodies](./omnistudio_integration_procedure_apis_requests.htm.md)**  

Learn more about the available Integration Procedure API request bodies.

- 
**[Response Bodies](./omnistudio_integration_procedure_apis_responses.htm.md)**  

Learn more about the available Integration Procedure API response bodies.

=== ARTICLE: omnistudio_integration_procedure_apis_requests.htm ===
---
page_id: omnistudio_integration_procedure_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_integration_procedure_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available Integration Procedure API request bodies.

- 
**[Integration Procedure Cache Keys](./connect_requests_integration_procedure_cache_keys_list.htm.md)**  

Input representation of the cache keys to clear the execution cache.

- 
**[Integration Procedure Clear Cache Input](./connect_requests_integration_procedure_cache_input.htm.md)**  

Input representation of the details to clear the execution cache of the integration     procedures.

- 
**[Integration Procedure Details](./connect_requests_integration_procedure_cache_input_data.htm.md)**  

Input representation of the details of the integration procedures to clear the cache     for.

- 
**[Integration Procedure Service Run](./connect_requests_integration_procedure_service_run_input.htm.md)**  

Input representation of the details to execute an integration procedure from     Apex.

- 
**[Integration Procedure Service Run Input](./connect_requests_integration_procedure_service_run_input_list.htm.md)**  

Input representation of the list of custom data to execute an integration procedure     from Apex.

- 
**[Integration Procedure Service Run Options](./connect_requests_integration_procedure_service_run_options.htm.md)**  

Input representation of the optional parameters to customize and refine the execution of     the integration procedure.

=== ARTICLE: omnistudio_integration_procedure_apis_resources.htm ===
---
page_id: omnistudio_integration_procedure_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_integration_procedure_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Integration Procedure API resources.

- 
**[Integration Procedure Clear Cache (POST)](./connect_resources_integration_procedure_clear_cache.htm.md)**  

Clear the execution cache for the specified integration procedures.

- 
**[Integration Procedure Execution (POST)](./connect_resources_integration_procedure.htm.md)**  

Execute an integration procedure by using the name or ID of the integration     procedure.

=== ARTICLE: omnistudio_integration_procedure_apis_responses.htm ===
---
page_id: omnistudio_integration_procedure_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_integration_procedure_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_integration_procedure_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available Integration Procedure API response bodies.

- 
**[Integration Procedure Cache Details](./connect_responses_integration_procedure_cache_output.htm.md)**  

Output representation of the cache that are cleared for the specified integration     procedures.

- 
**[Integration Procedure Cache Response](./connect_responses_integration_procedure_cache_response.htm.md)**  

Output representation of the response with error message and status.

- 
**[Integration Procedure Execution Details](./connect_responses_integration_procedure_service_run_output.htm.md)**  

Output representation of the execution details of the integration procedure.

=== ARTICLE: omnistudio_metadata_api_parent.htm ===
---
page_id: omnistudio_metadata_api_parent.htm
title: Omnistudio Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omnistudio Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Omnistudio](./omnistudio_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. Use a flow to create an application     that takes users through a series of pages to query and update records in the database. You can     also execute logic and provide branching capability based on user input to build dynamic     applications.

- 
**[OmniDataTransform](./meta_omnidatatransform.htm.md)**  

Represents the header configuration of a DataRaptor. 	

- 
**[OmniExtTrackingDef](./meta_omniexttrackingdef.htm.md)**  

 		Represents a connection between an OmniTrackingGroup in OmniAnalytics and a 			third-party Analytics system such as Google Analytics.

- 
**[OmniIntegrationProcedure](./meta_omniintegrationprocedure.htm.md)**  

 		Represents an Omnistudio Integration Procedure for the 			Discovery Framework. It enables declarative, server-side processing to perform multiple 			actions in a single server call, supporting sales, service, and other business 			workflows. For Discovery Framework, the customization type is 				`discoveryframework`. 	

- 
**[OmniInteractionAccessConfig](./meta_omniinteractionaccessconfig.htm.md)**  

Represents configuration settings for access to Omnistudio       FlexCard caching and data sources.

- 
**[OmniInteractionConfig](./meta_omniinteractionconfig.htm.md)**  

Represents configuration settings for     Omnistudio.

- 
**[OmniScript](./meta_omniscript.htm.md)**  

Represents an OmniScript for the Discovery Framework, which 			guides users through sales, service, and other business processes. For Discovery 			Framework, the customization type is `discoveryframework`. 	

- 
**[OmniscriptDefinition](./meta_omniscriptdefinition.htm.md)**  

Represents the header configuration of an       Omniscript. Each row represents an Omniscript's header configurations, such as its type,       subtype, and name. An Omniscript helps build guided digital experiences. This object stores       primary information about an Omniscript to render it at runtime.

- 
**[OmniStudioSettings](./meta_omnistudiosettings.htm.md)**  

Represents the settings that help administrators turn on 			specific Omnistudio features and capabilities at the organization level. 	

- 
**[OmniTrackingGroup](./meta_omnitrackinggroup.htm.md)**  

Represents a group of FlexCard and OmniScript components that have 			their user interactions tracked together in OmniAnalytics.

=== ARTICLE: omnistudio_overview.htm ===
---
page_id: omnistudio_overview.htm
title: Omnistudio
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_overview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omnistudio

Omnistudio provides a suite of services, components, and data model objects that combine
  to create Industry Cloud applications. Use Omnistudio to create guided interactions using data
  from your Salesforce org and external sources. Create Omniscripts to guide users through sales and
  service processes with fast, personalized responses. Get and post data with Omnistudio Data
  Mappers and Integration Procedures.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[Omnistudio Standard Objects](./omnistudio_standard_objects_parent.htm.md)**  

Omnistudio data model defines the foundational objects and fields used across Omnistudio   components. It enables consistent data access and management within guided experiences and process   automation. 

- 
**[Omnistudio Business REST APIs](./omnistudio_apis.htm.md)**  

Omnistudio Business APIs are RESTful APIs that are sometimes available as Apex classes     and methods. You can access Omnistudio APIs using REST endpoints. These REST APIs follow similar     conventions as Connect REST APIs.

- 
**[Omnistudio Metadata API Types](./omnistudio_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Omnistudio Apex Reference](./omnistudio_apex_reference.htm.md)**  

Apex is a strongly typed, object-oriented programming language that allows developers     to execute flow and transaction control statements on the Salesforce Platform server, in     conjunction with calls to the API. Omnistudio Apex reference includes built-in Apex classes and     interfaces, grouped by namespace.

=== ARTICLE: omnistudio_standard_objects_parent.htm ===
---
page_id: omnistudio_standard_objects_parent.htm
title: Omnistudio Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/omnistudio_standard_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omnistudio Standard Objects

Omnistudio data model defines the foundational objects and fields used across Omnistudio
  components. It enables consistent data access and management within guided experiences and process
  automation. 

- 
**[OmniComponentErrorLog](./sforce_api_objects_omnicomponenterrorlog.htm.md)**  

 		For internal use only.

- 
**[OmniDataPack](./sforce_api_objects_omnidatapack.htm.md)**  

 For internal use only.

- 
**[OmniDataTransform](./sforce_api_objects_omnidatatransform.htm.md)**  

 For internal use only.

- 
**[OmniDataTransformItem](./sforce_api_objects_omnidatatransformitem.htm.md)**  

 For internal use only.

- 
**[OmniESignature](./sforce_api_objects_omniesignature.htm.md)**  

 For internal use only.

- 
**[OmniExtTrackingDef](./sforce_api_objects_omniexttrackingdef.htm.md)**  

       Represents a connection between an OmniTrackingGroup in OmniAnalytics and a          third-party Analytics system such as Google Analytics. This object is available in API       version 60.0 and later. 

- 
**[OmniExtTrackingEventDef](./sforce_api_objects_omniexttrackingeventdef.htm.md)**  

       Represents a format for FlexCard or OmniScript user interaction data that a          third-party Analytics system such as Google Analytics can accept. This object is       available in API version 60.0 and later. 

- 
**[OmniInteractionAccessConfig](./sforce_api_objects_omniinteractionaccessconfig.htm.md)**  

 For internal use only.

- 
**[OmniInteractionConfig](./sforce_api_objects_omniinteractionconfig.htm.md)**  

 For internal use only.

- 
**[OmniProcess](./sforce_api_objects_omniprocess.htm.md)**  

 For internal use only.

- 
**[OmniProcessCompilation](./sforce_api_objects_omniprocesscompilation.htm.md)**  

 For internal use only.

- 
**[OmniProcessElement](./sforce_api_objects_omniprocesselement.htm.md)**  

 For internal use only.

- 
**[OmniProcessTransientData](./sforce_api_objects_omniprocesstransientdata.htm.md)**  

 For internal use only.

- 
**[OmniScriptSavedSession](./sforce_api_objects_omniscriptsavedsession.htm.md)**  

 For internal use only.

- 
**[OmniTrackingComponentDef](./sforce_api_objects_omnitrackingcomponentdef.htm.md)**  

       Represents a FlexCard or OmniScript that is a member of an OmniTrackingGroup,          which tracks user interactions in OmniAnalytics. This object is available in API       version 60.0 and later. 

- 
**[OmniTrackingGroup](./sforce_api_objects_omnitrackinggroup.htm.md)**  

       Represents a group of FlexCard and OmniScript components that have their user          interactions tracked together in OmniAnalytics. This object is available in API       version 60.0 and later. 

- 
**[OmniUiCard](./sforce_api_objects_omniuicard.htm.md)**  

 For internal use only.

=== ARTICLE: sforce_api_objects_omnicomponenterrorlog.htm ===
---
page_id: sforce_api_objects_omnicomponenterrorlog.htm
title: OmniComponentErrorLog
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnicomponenterrorlog.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniComponentErrorLog

		For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omnidatapack.htm ===
---
page_id: sforce_api_objects_omnidatapack.htm
title: OmniDataPack
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnidatapack.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniDataPack

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omnidatatransform.htm ===
---
page_id: sforce_api_objects_omnidatatransform.htm
title: OmniDataTransform
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnidatatransform.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniDataTransform

 For internal use only.

		
This object and associated records are only for internal
			use. Don't perform any create, edit, or delete operations on this object. Modifying or
			deleting this object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omnidatatransformitem.htm ===
---
page_id: sforce_api_objects_omnidatatransformitem.htm
title: OmniDataTransformItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnidatatransformitem.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniDataTransformItem

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniesignature.htm ===
---
page_id: sforce_api_objects_omniesignature.htm
title: OmniESignature
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniesignature.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniESignature

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniexttrackingdef.htm ===
---
page_id: sforce_api_objects_omniexttrackingdef.htm
title: OmniExtTrackingDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniexttrackingdef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniExtTrackingDef

      Represents a connection between an OmniTrackingGroup in OmniAnalytics and a
         third-party Analytics system such as Google Analytics. This object is available in API
      version 60.0 and later. 

      
         

#### Note

This object is part of OmniStudio Standard, not OmniStudio for Vlocity.

         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations. 

      

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Using OmniAnalytics requires having an OmniStudio license and enabling OmniAnalytics in
            Setup.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

#### 

#### 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 
- 

: 

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A description of the OmniExtTrackingDef. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the OmniExtTrackingDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Specifies whether the OmniExtTrackingDef is active. The default value is `true`. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language for the OmniExtTrackingDef. |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique master label of the OmniExtTrackingDef. This internal label doesn’t get translated. |
| OmniExtTrackingDefKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** A UUID generated internally by Salesforce to uniquely identify an OmniExtTrackingDef record across all orgs. |
| TrackingFrameworkInformation | **Type** textarea **Properties** Create, Update **Description** JSON data containing information about an external service, such as the API call and input parameter names. |
| TrackingServiceProvider | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The third-party Analytics system to which user interaction data is sent. Possible values are: `Google` The default value is `Google`. |

=== ARTICLE: sforce_api_objects_omniexttrackingeventdef.htm ===
---
page_id: sforce_api_objects_omniexttrackingeventdef.htm
title: OmniExtTrackingEventDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniexttrackingeventdef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniExtTrackingEventDef

      Represents a format for FlexCard or OmniScript user interaction data that a
         third-party Analytics system such as Google Analytics can accept. This object is
      available in API version 60.0 and later. 

      
         

#### Note

This object is part of OmniStudio Standard, not OmniStudio for Vlocity.

         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations. 

      

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Using OmniAnalytics requires having an OmniStudio license and enabling OmniAnalytics in
            Setup.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

: 

: 

: 
: 
- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

#### 

#### 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| ComponentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of component for which user interactions are tracked. Possible values are: `Flexcard` `Omniscript` |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A description of the OmniExtTrackingEventDef. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the OmniExtTrackingEventDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| InclusionRule | **Type** textarea **Properties** Create, Nillable, Update **Description** A true-or-false condition that determines whether an event is sent to the third-party Analytics system. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language for the OmniExtTrackingEventDef. |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique master label of the OmniExtTrackingEventDef. This internal label doesn’t get translated. |
| OmniExtTrackingDef | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the related OmniExtTrackingDef object. This field is a relationship field. **Relationship Name** OmniExtTrackingDef **Relationship Type** Lookup **Refers To** OmniExtTrackingDef |
| OmniExtTrackingEventDefKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** A UUID generated internally by Salesforce to uniquely identify an OmniExtTrackingEventDef record across all orgs. |
| PayloadTemplate | **Type** textarea **Properties** Create, Nillable, Update **Description** The payload template structure with placeholders for runtime data. This is used at runtime to generate the actual payload to be sent to the external Analytics service. |

=== ARTICLE: sforce_api_objects_omniinteractionaccessconfig.htm ===
---
page_id: sforce_api_objects_omniinteractionaccessconfig.htm
title: OmniInteractionAccessConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniinteractionaccessconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniInteractionAccessConfig

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniinteractionconfig.htm ===
---
page_id: sforce_api_objects_omniinteractionconfig.htm
title: OmniInteractionConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniinteractionconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniInteractionConfig

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniprocess.htm ===
---
page_id: sforce_api_objects_omniprocess.htm
title: OmniProcess
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniprocess.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniProcess

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniprocesscompilation.htm ===
---
page_id: sforce_api_objects_omniprocesscompilation.htm
title: OmniProcessCompilation
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniprocesscompilation.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniProcessCompilation

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniprocesselement.htm ===
---
page_id: sforce_api_objects_omniprocesselement.htm
title: OmniProcessElement
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniprocesselement.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniProcessElement

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniprocesstransientdata.htm ===
---
page_id: sforce_api_objects_omniprocesstransientdata.htm
title: OmniProcessTransientData
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniprocesstransientdata.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniProcessTransientData

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omniscriptsavedsession.htm ===
---
page_id: sforce_api_objects_omniscriptsavedsession.htm
title: OmniScriptSavedSession
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniscriptsavedsession.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniScriptSavedSession

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

=== ARTICLE: sforce_api_objects_omnitrackingcomponentdef.htm ===
---
page_id: sforce_api_objects_omnitrackingcomponentdef.htm
title: OmniTrackingComponentDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnitrackingcomponentdef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniTrackingComponentDef

      Represents a FlexCard or OmniScript that is a member of an OmniTrackingGroup,
         which tracks user interactions in OmniAnalytics. This object is available in API
      version 60.0 and later. 

      
         

#### Note

This object is part of OmniStudio Standard, not OmniStudio for Vlocity.

         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations. 

      

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Using OmniAnalytics requires having an OmniStudio license and enabling OmniAnalytics in
            Setup.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

: 

: 

: 
: 
- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

#### 

#### 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| ComponentType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of component for which user interactions are tracked. Possible values are: `Flexcard` `Omniscript` |
| ComponentVersion | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The version of the FlexCard or OmniScript. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the OmniTrackingComponentDef in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language for the OmniTrackingComponentDef. |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique master label of the OmniTrackingComponentDef. This internal label doesn’t get translated. |
| OmniTrackingComponentDefKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** A UUID generated internally by Salesforce to uniquely identify an OmniTrackingComponentDef record across all orgs. |
| OmniTrackingGroup | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the related OmniTrackingGroup object. This field is a relationship field. **Relationship Name** OmniTrackingGroup **Relationship Type** Lookup **Refers To** OmniTrackingGroup |

=== ARTICLE: sforce_api_objects_omnitrackinggroup.htm ===
---
page_id: sforce_api_objects_omnitrackinggroup.htm
title: OmniTrackingGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omnitrackinggroup.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniTrackingGroup

      Represents a group of FlexCard and OmniScript components that have their user
         interactions tracked together in OmniAnalytics. This object is available in API
      version 60.0 and later. 

      
         

#### Note

This object is part of OmniStudio Standard, not OmniStudio for Vlocity.

         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations. 

      

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

Using OmniAnalytics requires having an
            OmniStudio license and enabling OmniAnalytics in Setup.

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

#### 

#### 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 
- 
- 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A description of the OmniTrackingGroup. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the OmniTrackingGroup in the API. This name can contain only underscores and alphanumeric characters and must be unique in your organization. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. Limit: 80 characters. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Note Only users with View DeveloperName OR View Setup and Configuration permission can view, group, sort, and filter this field. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date when the OmniTrackingGroup became inactive. |
| GroupType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies whether this OmniTrackingGroup sends tracking data to a third-party Analytics system such as Google Analytics. Possible values are: `External`—A third-party Analytics system is used. `Internal`—No third-party Analytics system is used. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Specifies whether the OmniTrackingGroup is active. The default value is `false`. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language for the OmniTrackingGroup. |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique master label of the OmniTrackingGroup. This internal label doesn’t get translated. |
| MaxAgeInDays | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of days the group and its analytics data is active beyond which the data is deleted. |
| OmniExtTrackingDef | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the related OmniExtTrackingDef object. Required if GroupType is set to `External`. This field is a relationship field. **Relationship Name** OmniExtTrackingDef **Relationship Type** Lookup **Refers To** OmniExtTrackingDef |
| OmniTrackingGroupKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** A UUID generated internally by Salesforce to uniquely identify an OmniTrackingGroup record across all orgs. |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date when the OmniTrackingGroup became active. |

=== ARTICLE: sforce_api_objects_omniuicard.htm ===
---
page_id: sforce_api_objects_omniuicard.htm
title: OmniUiCard
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniuicard.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Omnistudio
parent_page: omnistudio_standard_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniUiCard

 For internal use only.

		

			

This object and associated records are only for internal use. Don't perform any
				create, edit, or delete operations on this object. Modifying or deleting this
				object’s records may result in errors with your implementation.

