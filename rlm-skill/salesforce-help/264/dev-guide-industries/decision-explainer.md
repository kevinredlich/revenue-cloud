# Industries Common Resources Developer Guide 264 — sección: Decision Explainer (22 artículos)

=== ARTICLE: connect_requests_explainability_action_log_input.htm ===
---
page_id: connect_requests_explainability_action_log_input.htm
title: Explainability Action Log Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_explainability_action_log_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Action Log Input

Input representation of Explainability action logs.

    
      
        
          

**Root XML tag**

          
: `ExplainabilityActionLog`

        
        
          

**JSON example**

          
: 
            

```
{
"specificationName" : "EAD1",
"name" : "testEAL1",
"actionLog" : "{\"input\":{\"input\":{\"input\":2}},\"ruledefinition\":{\"calculationProcedureId\":\"0k0xx00000000JNAAY\",
\"variables\":{\"details\":[{\"apiName\":\"total\",\"isEditable\":true,\"defaultValue\":null,\"displayName\":null,\"dataType\"
:\"Number\",\"precision\":2,\"calculationMatrixName\":null,\"name\":\"total\",\"isUserDefined\":true,\"uiDisplayOrder\":null,
\"id\":\"0kJxx000000018zEAA\"},{\"apiName\":\"input\",\"isEditable\":true,\"defaultValue\":\"10\",\"displayName\":null,\"dataType\"
:\"Number\",\"precision\":2,\"calculationMatrixName\":null,\"name\":\"input\",\"isUserDefined\":true,\"uiDisplayOrder\":null,\"id\"
:\"0kJxx00000001AbEAI\"}]},\"code\":null,\"endDate\":null,\"description\":null,\"message\":null,\"enabled\":true,\"versionNumber\":2,
\"versionId\":\"0k1xx00000000knAAA\",\"root\":{\"steps\":[\"0mqxx00000001TxAAI\"]},\"name\":\"es1 V1 CLONE\",\"rank\":2,\"step\":
{\"details\":{\"0mqxx00000001TxAAI\":{\"inputVariablesFormatText\":\"[{\\\"name\\\":\\\"input\\\",\\\"dataType\\\":\\\"Number\\\",
\\\"alias\\\":\\\"input\\\"}]\",\"stepType\":\"Calculation\",\"outputVariablesFormatText\":\"{\\\"name\\\":\\\"total\\\",\\\"dataType\\\":
\\\"Number\\\",\\\"alias\\\":\\\"total\\\"}\",\"conditionsUiFormattedText\":\"{\\\"bypass\\\":{},\\\"stepNumber\\\":3}\",
\"formulaUiFormattedText\":null,\"description\":null,\"outputVariablesMappingText\":\"{\\\"total\\\":\\\"total\\\"}\",
\"conditionsExpressionText\":null,\"calculationMatrixId\":null,\"isResultIncluded\":true,\"formulaExpressionText\":\"10 * input\",\"stage\":
\"Calculation\",\"name\":\"Calculation\",\"childStepIds\":[],\"referenceCalculationProcedureId\":null,\"id\":\"0mqxx00000001TxAAI\",
\"returnMessageValueSet\":\"{\\\"true\\\":\\\"\\\",\\\"false\\\":\\\"\\\"}\"}}},\"constants\":{\"details\":[]},\"startDate\":1637684784000,
\"isSuccess\":null},\"runtime\":{\"output\":[{\"aggregationResults\":{},\"calculationResults\":[{\"total\":20,\"ID\":\"input\"}]}],\"simulate\"
:{\"0mqxx00000001TxAAI\":{\"stepInputs\":{\"input\":2},\"stepResults\":{\"total\":20}}}}}",
"actionLogDate" : "2021-09-15T03:18:30.081Z",
"actionContextCode" : "0f0xx0000000001AAA"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action​Context​Code` | String | The valid Salesforce record ID that’s used to retrieve the explainability action logs. | Required | 54.0 |
| `actionLog` | String | The contents of the explainability action log. | Required | 54.0 |
| `action​LogDate` | String | The date and time when the explainability action log was generated by the application’s action. | Required | 54.0 |
| `actionLog​OwnerId` | String | The ID of the user who owns the action log. | No | 54.0 |
| `additional​Filter` | String | The string that’s used as an additional filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `name` | String | A name to identify the explainability action log record. | No | 54.0 |
| `primary​Filter` | String | The string that’s used as the primary filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `secondary​Filter` | String | The string that’s used as the secondary filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `specification​Name` | String | A unique name that identifies an active explainability action log record. | Required | 54.0 |

=== ARTICLE: connect_resources_explainability_detailed_action_log.htm ===
---
page_id: connect_resources_explainability_detailed_action_log.htm
title: Explainability Detailed Action Log (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_explainability_detailed_action_log.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Detailed Action Log (GET)

Retrieve detailed action logs and combine log segments to generate a consolidated
    explainability action log.

    
      
        
          

**Resource**

          
: 
            

```
/connect/decision-explainer/detailed-action-log
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/decision-explainer/detailed-action-log?actionContextCode=001xx000003GYiCAAW&applicationType=0&applicationSubType=BREDES&processType=BREDES&actionLogDateTime=2024-03-06T05:09:32.000Z&uniqueIdentifier=f89eff41-94ed-4fe7-9b72-f6df2bb5f4aa
```

          

        
        
          

**Available version**

          
: 61.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `actionContextCode` | String | Record ID within the context of the associated application's action that can be used to retrieve the action log | Required | 61.0 |
| `actionLogDateTime` | String | Date and time when the explainability action log records are to be returned Date format - yyyy-MM-ddTHH:mm:ss.SSSZ. | Required | 61.0 |
| `applicationSubType` | String | Subtype of the associated application for which the explainability log is generated. | Required | 61.0 |
| `applicationType` | String | Name of the application for which the explainability service is run. | Required | 61.0 |
| `processType` | String | Type of business process associated with the explainability action. | Required | 61.0 |
| `uniqueIdentifier` | String | A unique ID that's associated with a specific explainability action log. | Required | 61.0 |

          

        
        
          

**Response body for GET**

          
: [Explainability Detailed Action Log Detail](./connect_responses_explainability_detailed_action_log_detail.htm.md)

=== ARTICLE: connect_resources_get_create_action_logs.htm ===
---
page_id: connect_resources_get_create_action_logs.htm
title: Action Logs (GET, POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_get_create_action_logs.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Action Logs (GET, POST)

Retrieve a paginated list of Explainability action logs. Create an
      Explainability action log.

**Resource**

: 

```
/connect/decision-explainer/action-logs
```

        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/vXX.X/connect​​/
decision-explainer/action-logs?actionContextCode=001x0000005DmI3AAK
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/vXX.X/connect​​/
decision-explainer/action-logs
```

          

        

**Available version**

: 54.0

**Requires Chatter**

: No

**HTTP methods**

: GET, POST

**Query parameters for GET**

: 

| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `actionContextCode` | String | The record ID within the context of the associated application's action that’s used to retrieve action logs. | Required | 54.0 |
| `applicationSubType` | String | The subtype of the associated application for which the explainability log is generated. This matches one of the valid values in the ExplainabilityActionDef `ApplicationSubtype` field. | Optional | 54.0 |
| `applicationType` | String | The name of the application for which the explainability service is run. This matches one of the valid values in the ExplainabilityActionDef `ApplicationType` field. | Optional | 54.0 |
| `createdAfter` | String | A valid date time after which the explainability action log records are returned. | Optional | 54.0 |
| `createdBefore` | String | A valid date time before which the explainability action log records are returned. | Optional | 54.0 |
| `pageSize` | Integer | The number of explainability action log records to return. The value can range from 200 to 500. | Optional | 54.0 |
| `processType` | String | The process type of the associated application for which the explainability action log is generated. This matches one of the valid values in the ExplainabilityActionDef `ProcessType` field. | Optional | 54.0 |
| `queryMore` | String | A string returned from the previous request, which you must pass to the next request to get the next page. | Optional | 54.0 |

**Response body for GET**

: [Explainability Action Logs](./connect_responses_explainability_action_logs.htm.md)

**Request body for POST**

: 
            
        
          

**Root XML tag**

          
: `ExplainabilityActionLog`

        
        
          

**JSON example**

          
: 
            

```
{
"specificationName" : "EAD1",
"name" : "testEAL1",
"actionLog" : "{\"input\":{\"input\":{\"input\":2}},\"ruledefinition\":{\"calculationProcedureId\":\"0k0xx00000000JNAAY\",
\"variables\":{\"details\":[{\"apiName\":\"total\",\"isEditable\":true,\"defaultValue\":null,\"displayName\":null,\"dataType\"
:\"Number\",\"precision\":2,\"calculationMatrixName\":null,\"name\":\"total\",\"isUserDefined\":true,\"uiDisplayOrder\":null,
\"id\":\"0kJxx000000018zEAA\"},{\"apiName\":\"input\",\"isEditable\":true,\"defaultValue\":\"10\",\"displayName\":null,\"dataType\"
:\"Number\",\"precision\":2,\"calculationMatrixName\":null,\"name\":\"input\",\"isUserDefined\":true,\"uiDisplayOrder\":null,\"id\"
:\"0kJxx00000001AbEAI\"}]},\"code\":null,\"endDate\":null,\"description\":null,\"message\":null,\"enabled\":true,\"versionNumber\":2,
\"versionId\":\"0k1xx00000000knAAA\",\"root\":{\"steps\":[\"0mqxx00000001TxAAI\"]},\"name\":\"es1 V1 CLONE\",\"rank\":2,\"step\":
{\"details\":{\"0mqxx00000001TxAAI\":{\"inputVariablesFormatText\":\"[{\\\"name\\\":\\\"input\\\",\\\"dataType\\\":\\\"Number\\\",
\\\"alias\\\":\\\"input\\\"}]\",\"stepType\":\"Calculation\",\"outputVariablesFormatText\":\"{\\\"name\\\":\\\"total\\\",\\\"dataType\\\":
\\\"Number\\\",\\\"alias\\\":\\\"total\\\"}\",\"conditionsUiFormattedText\":\"{\\\"bypass\\\":{},\\\"stepNumber\\\":3}\",
\"formulaUiFormattedText\":null,\"description\":null,\"outputVariablesMappingText\":\"{\\\"total\\\":\\\"total\\\"}\",
\"conditionsExpressionText\":null,\"calculationMatrixId\":null,\"isResultIncluded\":true,\"formulaExpressionText\":\"10 * input\",\"stage\":
\"Calculation\",\"name\":\"Calculation\",\"childStepIds\":[],\"referenceCalculationProcedureId\":null,\"id\":\"0mqxx00000001TxAAI\",
\"returnMessageValueSet\":\"{\\\"true\\\":\\\"\\\",\\\"false\\\":\\\"\\\"}\"}}},\"constants\":{\"details\":[]},\"startDate\":1637684784000,
\"isSuccess\":null},\"runtime\":{\"output\":[{\"aggregationResults\":{},\"calculationResults\":[{\"total\":20,\"ID\":\"input\"}]}],\"simulate\"
:{\"0mqxx00000001TxAAI\":{\"stepInputs\":{\"input\":2},\"stepResults\":{\"total\":20}}}}}",
"actionLogDate" : "2021-09-15T03:18:30.081Z",
"actionContextCode" : "0f0xx0000000001AAA"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action​Context​Code` | String | The valid Salesforce record ID that’s used to retrieve the explainability action logs. | Required | 54.0 |
| `actionLog` | String | The contents of the explainability action log. | Required | 54.0 |
| `action​LogDate` | String | The date and time when the explainability action log was generated by the application’s action. | Required | 54.0 |
| `actionLog​OwnerId` | String | The ID of the user who owns the action log. | No | 54.0 |
| `additional​Filter` | String | The string that’s used as an additional filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `name` | String | A name to identify the explainability action log record. | No | 54.0 |
| `primary​Filter` | String | The string that’s used as the primary filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `secondary​Filter` | String | The string that’s used as the secondary filter criteria to fetch the explainability action logs. | Optional | 57.0 |
| `specification​Name` | String | A unique name that identifies an active explainability action log record. | Required | 54.0 |

          

        
      

**Response body for POST**

: [Explainability Action Log Create](./connect_responses_explainability_action_log_create.htm.md)

=== ARTICLE: connect_responses_explainability_action_log_create.htm ===
---
page_id: connect_responses_explainability_action_log_create.htm
title: Explainability Action Log Create
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_action_log_create.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Action Log Create

Output representation of the create Explainability action log
      request.

      
        
          

**JSON example**

          
: 
            

```
{
   "sequenceNumber" : 1,
   "uniqueIdentifier" : "de3b62ae-410b-419a-b75e-1d2d5cb24b88"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `sequenceNumber` | Integer | The sequence number of the explainability action log. | Small, 54.0 | 54.0 |
| `uniqueIdentifier` | String | The unique ID of the explainability action log created after a successful create request. | Small, 54.0 | 54.0 |

=== ARTICLE: connect_responses_explainability_action_log_detail.htm ===
---
page_id: connect_responses_explainability_action_log_detail.htm
title: Explainability Action Log Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_action_log_detail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Action Log Detail

Output representation of the Explainability action log
    details.

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `actionContextCode` | String | The record ID within the context of the associated application's action that’s used to retrieve the action log. | Small, 54.0 | 54.0 |
| `actionLog` | String | The contents of the explainability action log. | Small, 54.0 | 54.0 |
| `additionalFilter` | String | The string that’s used as an additional filter criteria to fetch the explainability action logs. | Small, 57.0 | 57.0 |
| `applicationLogDate` | String | The date and time when the explainability action log was generated by the application's action. | Small, 54.0 | 54.0 |
| `applicationSubtype` | String | The subtype of the associated application for which the explainability log is generated.This matches one of the valid values in the ExplainabilityActionDef `ApplicationSubType` field. | Small, 54.0 | 54.0 |
| `applicationType` | String | The name of the application for which the explainability service is run.This matches one of the valid values in the ExplainabilityActionDef `ApplicationType` field. | Small, 54.0 | 54.0 |
| `explainabilitySpecName` | String | The name that identifies the explainability specification. | Small, 57.0 | 57.0 |
| `name` | String | A name to identify the explainability action log record. | Small, 54.0 | 54.0 |
| `primaryFilter` | String | The string that’s used as the primary filter criteria to fetch the explainability action logs. | Small, 57.0 | 57.0 |
| `processType` | String | The process type of the associated application for which the explainability action log is generated.This matches one of the valid values in the ExplainabilityActionDef `ProcessType` field. | Small, 54.0 | 54.0 |
| `secondaryFilter` | String | The string that’s used as the secondary filter criteria to fetch the explainability action logs. | Small, 57.0 | 57.0 |

=== ARTICLE: connect_responses_explainability_action_logs.htm ===
---
page_id: connect_responses_explainability_action_logs.htm
title: Explainability Action Logs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_action_logs.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Action Logs

Output representation of the list of Explainability action
    logs.

      
        
          

**JSON example**

          
: 
            

```
{
   "actionLogs" : [ {
      "actionContextCode" : "001x0000005DmI3AAK",
      "actionLog" : “{This is a sample action log data.}”,
      "applicationLogDate" : "Mon Dec 06 10:29:35 GMT 2021",
      "applicationSubtype" : "AST1",
      "applicationType" : "0",
      "name" : "EAD1",
      "processType" : "BPT1"
   }, {
      "actionContextCode" : "001x0000005DmI3AAK",
      "actionLog" : “{This is a sample action log data.}”,
      "applicationLogDate" : "Mon Dec 06 15:21:09 GMT 2021",
      "applicationSubtype" : "AST1",
      "applicationType" : "0",
      "name" : "EAD1",
      "processType" : "BPT1"
   } ],
   "queryMore" : ""
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `actionLogs` | [Explainability Action Log Detail](./connect_responses_explainability_action_log_detail.htm.md)[] | Represents the list of explainability action logs. | Small, 54.0 | 54.0 |
| `queryMore` | String | A string that can be passed to the next call to fetch the next batch of explainability action log records. | Small, 54.0 | 54.0 |

=== ARTICLE: connect_responses_explainability_detailed_action_log_detail.htm ===
---
page_id: connect_responses_explainability_detailed_action_log_detail.htm
title: Explainability Detailed Action Log Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_detailed_action_log_detail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Detailed Action Log Detail

Output representation of explainability action log in detail.

      
        
          

**JSON example**

          
: 
            

```
{
    "actionContextCode": "001xx000003GYiCAAW",
    "actionLog": "{&quot;input&quot;:{&quot;calcInput&quot;:10},&quot;ruledefinition&quot;:{&quot;interfaceSourceType&quot;:null,&quot;calculationProcedureId&quot;:&quot;9QLxx0000004C92GAE&quot;,&quot;variables&quot;:{&quot;details&quot;:[{&quot;apiName&quot;:&quot;calInt&quot;,&quot;isEditable&quot;:true,&quot;defaultValue&quot;:null,&quot;displayName&quot;:null,&quot;dataType&quot;:&quot;Number&quot;,&quot;precision&quot;:2,&quot;calculationMatrixName&quot;:null,&quot;name&quot;:&quot;calInt&quot;,&quot;isUserDefined&quot;:true,&quot;uiDisplayOrder&quot;:null,&quot;id&quot;:null},{&quot;apiName&quot;:&quot;calcInput&quot;,&quot;isEditable&quot;:true,&quot;defaultValue&quot;:null,&quot;displayName&quot;:null,&quot;dataType&quot;:&quot;Number&quot;,&quot;precision&quot;:2,&quot;calculationMatrixName&quot;:null,&quot;name&quot;:&quot;calcInput&quot;,&quot;isUserDefined&quot;:true,&quot;uiDisplayOrder&quot;:null,&quot;id&quot;:null}]},&quot;code&quot;:null,&quot;endDate&quot;:null,&quot;contextDefinition&quot;:null,&quot;description&quot;:null,&quot;message&quot;:null,&quot;enabled&quot;:true,&quot;versionNumber&quot;:1,&quot;aliasGroupList&quot;:{&quot;aliasGroupList&quot;:[]},&quot;versionId&quot;:&quot;0k1xx0000004C92GAE&quot;,&quot;showExplExternally&quot;:false,&quot;root&quot;:{&quot;steps&quot;:[&quot;Calculation&quot;]},&quot;executionScale&quot;:&quot;Low&quot;,&quot;name&quot;:&quot;ExpDes V1&quot;,&quot;rank&quot;:1,&quot;step&quot;:{&quot;details&quot;:{&quot;Calculation&quot;:{&quot;inputVariablesFormatText&quot;:&quot;[{&#92;&quot;dataType&#92;&quot;:&#92;&quot;Number&#92;&quot;,&#92;&quot;name&#92;&quot;:&#92;&quot;calcInput&#92;&quot;,&#92;&quot;alias&#92;&quot;:&#92;&quot;calcInput&#92;&quot;}]&quot;,&quot;exposeExecPathMsgOnly&quot;:true,&quot;stepType&quot;:&quot;Calculation&quot;,&quot;lookupTableName&quot;:null,&quot;outputVariablesFormatText&quot;:&quot;{&#92;&quot;name&#92;&quot;:&#92;&quot;calInt&#92;&quot;}&quot;,&quot;customElementName&quot;:null,&quot;passedExplainerTemplateId&quot;:null,&quot;conditionsUiFormattedText&quot;:&quot;&quot;,&quot;description&quot;:null,&quot;inputVariablesMappingText&quot;:null,&quot;outputVariablesMappingText&quot;:&quot;{&#92;&quot;calInt&#92;&quot;:&#92;&quot;calInt&#92;&quot;}&quot;,&quot;calculationMatrixId&quot;:null,&quot;failedExplainerTemplateId&quot;:null,&quot;exposeConditionDetails&quot;:false,&quot;referenceCalculationProcedureId&quot;:null,&quot;id&quot;:&quot;Calculation&quot;,&quot;returnMessageValueSet&quot;:&quot;{&#92;&quot;true&#92;&quot;:&#92;&quot;&#92;&quot;,&#92;&quot;false&#92;&quot;:&#92;&quot;&#92;&quot;}&quot;,&quot;passedMessageTokenMappings&quot;:[],&quot;failedMessageTokenMappings&quot;:[],&quot;lookupTableError&quot;:null,&quot;noResultMessageTokenMappings&quot;:[],&quot;formulaUiFormattedText&quot;:null,&quot;noResultExplainerTemplateId&quot;:null,&quot;conditionsExpressionText&quot;:null,&quot;isResultIncluded&quot;:true,&quot;formulaExpressionText&quot;:&quot;100 + calcInput&quot;,&quot;showExplExternally&quot;:false,&quot;stage&quot;:&quot;Calculation&quot;,&quot;name&quot;:&quot;Calculation&quot;,&quot;childStepIds&quot;:[]}}},&quot;constants&quot;:{&quot;details&quot;:[]},&quot;allowNullInputsInSimulation&quot;:false,&quot;startDate&quot;:1709616068000,&quot;isSuccess&quot;:true,&quot;usageType&quot;:&quot;Bre&quot;},&quot;simulation&quot;:{&quot;simulationStepResults&quot;:{&quot;Calculation&quot;:{&quot;stepInputs&quot;:[{&quot;datatype&quot;:&quot;Number&quot;,&quot;precision&quot;:2,&quot;name&quot;:&quot;calcInput&quot;,&quot;value&quot;:&quot;10.00&quot;}],&quot;stepResults&quot;:[{&quot;datatype&quot;:&quot;Number&quot;,&quot;precision&quot;:2,&quot;name&quot;:&quot;calInt&quot;,&quot;value&quot;:&quot;110.00&quot;}],&quot;isDefaulted&quot;:false}},&quot;simulationResults&quot;:[{&quot;datatype&quot;:&quot;Number&quot;,&quot;precision&quot;:2,&quot;name&quot;:&quot;calInt&quot;,&quot;value&quot;:&quot;110.00&quot;}]}}",
    "additionalFilter": "undef",
    "applicationLogDate": "Wed Mar 06 05:09:32 GMT 2024",
    "applicationSubtype": "BREDES",
    "applicationType": "0",
    "explainabilitySpecName": "BREDES",
    "name": "BREDES",
    "primaryFilter": "undef",
    "processType": "BREDES",
    "secondaryFilter": "undef",
    "uniqueIdentifier": "f89eff41-94ed-4fe7-9b72-f6df2bb5f4aa"
}
```

          

        
      

              

              

              

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `actionContextCode` | String | Record ID within the context of the associated application action that's used to retrieve the action log. | Small, 62.0 | 62.0 |
| `actionLog` | String | Contents of the explainability action log as a JSON string. | Small, 62.0 | 62.0 |
| `additionalFilter` | String | Additional filter that's used to retrieve the results. | Small, 62.0 | 62.0 |
| `applicationLogDate` | String | Date and time at which the explainability action log was generated by the application's action. | Small, 62.0 | 62.0 |
| `applicationSubtype` | String | Subtype of the associated application for which the explainability log is generated. It matches one of the valid values for Explainability Action Specification table's ApplicationSubtype field. | Small, 62.0 | 62.0 |
| `applicationType` | String | Name of the application for which the explainability service is run. It must match one of the valid values in the applicationType field of the Explainability Action Specification table. | Small, 62.0 | 62.0 |
| `explainabilitySpecName` | String | Name of the explainability specification associated with the action log. | Small, 62.0 | 62.0 |
| `name` | String | Name to identify the explainability action log record to be created. | Small, 62.0 | 62.0 |
| `primaryFilter` | String | Primary filter that's used to retrieve the results. | Small, 62.0 | 62.0 |
| `processType` | String | Type of business process associated with the application for which the explainability action log is generated. It must match with one of the valid values in the processType field of the Explainability Action Specification table. | Small, 62.0 | 62.0 |
| `secondaryFilter` | String | Secondary filter that's used to retrieve the results. | Small, 62.0 | 62.0 |
| `uniqueIdentifier` | String | Unique ID associated with the specific Explainability action log. | Small, 62.0 | 62.0 |

=== ARTICLE: decision_explainer.htm ===
---
page_id: decision_explainer.htm
title: Decision Explainer
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer

Decision Explainer is an audit-like service that can be used by applications to store
    their application data to explain past events. The stored data can be retrieved later for
    reporting through custom-built user interfaces.
    

- 
**[Decision Explainer Business APIs](./decision_explainer_business_apis.htm.md)**  

Use the Decision Explainer Business APIs to give users a seamless API experience for     applications to audit their past events.

- 
**[Decision Explainer Tooling API Objects](./decision_explainer_tooling_api_parent.htm.md)**  

Decision Explainer objects store and locate the metadata         associated with every business rule.

- 
**[Decision Explainer Metadata API Types](./decision_explainer_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

=== ARTICLE: decision_explainer_apis_requests.htm ===
---
page_id: decision_explainer_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Here’s a list of Decision Explainer API request bodies.

- 
**[Explainability Action Log Input](./connect_requests_explainability_action_log_input.htm.md)**  

Input representation of Explainability action logs.

=== ARTICLE: decision_explainer_apis_resources.htm ===
---
page_id: decision_explainer_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Decision Explainer API resources.

- 
**[Action Logs (GET, POST)](./connect_resources_get_create_action_logs.htm.md)**  

Retrieve a paginated list of Explainability action logs. Create an       Explainability action log.

- 
**[Explainability Detailed Action Log (GET)](./connect_resources_explainability_detailed_action_log.htm.md)**  

Retrieve detailed action logs and combine log segments to generate a consolidated     explainability action log.

=== ARTICLE: decision_explainer_apis_responses.htm ===
---
page_id: decision_explainer_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Decision Explainer API response bodies.

- 
**[Explainability Action Logs](./connect_responses_explainability_action_logs.htm.md)**  

Output representation of the list of Explainability action     logs.

- 
**[Explainability Action Log Create](./connect_responses_explainability_action_log_create.htm.md)**  

Output representation of the create Explainability action log       request.

- 
**[Explainability Action Log Detail](./connect_responses_explainability_action_log_detail.htm.md)**  

Output representation of the Explainability action log     details.

- 
**[Explainability Detailed Action Log Detail](./connect_responses_explainability_detailed_action_log_detail.htm.md)**  

Output representation of explainability action log in detail.

=== ARTICLE: decision_explainer_business_apis.htm ===
---
page_id: decision_explainer_business_apis.htm
title: Decision Explainer Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_business_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Business APIs

Use the Decision Explainer Business APIs to give users a seamless API experience for
    applications to audit their past events.

- 
**[Resources](./decision_explainer_apis_resources.htm.md)**  

Here’s a list of Decision Explainer API resources.

- 
**[Request Bodies](./decision_explainer_apis_requests.htm.md)**  

Here’s a list of Decision Explainer API request bodies.

- 
**[Response Bodies](./decision_explainer_apis_responses.htm.md)**  

Here’s a list of Decision Explainer API response bodies.

=== ARTICLE: decision_explainer_metadata_api_parent.htm ===
---
page_id: decision_explainer_metadata_api_parent.htm
title: Decision Explainer Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

    
      

For more information about Metadata API and to find a complete reference of existing metadata types, see [Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm).

    

    
  

- 
**[ApplicationSubtypeDefinition](./meta_applicationsubtypedefinition.htm.md)**  

Represents a subtype of an application. Create 			application subtype definitions to define the types of applications used in your 			Decision Explainer entities. 

- 
**[BusinessProcessTypeDefinition](./meta_businessprocesstypedefinition.htm.md)**  

Represents the definition of the business process 			type within an application domain.

- 
**[ExplainabilityActionDefinition](./meta_explainabilityactiondefinition.htm.md)**  

Represents the definition of the explainability 			action log that is generated by the associated application's action.

- 
**[ExplainabilityActionVersion](./meta_explainabilityactionversion.htm.md)**  

Represents the explainability action version of the 			explainability action log that is generated by the associated application's 		action.

=== ARTICLE: decision_explainer_tooling_api_parent.htm ===
---
page_id: decision_explainer_tooling_api_parent.htm
title: Decision Explainer Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_tooling_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Tooling API Objects

Decision Explainer objects store and locate the metadata
        associated with every business rule.

        
            

Tooling API exposes metadata used in developer tooling that you can access through
                REST or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to
                retrieve smaller pieces of metadata. For more information about Tooling API objects
                and to find a complete reference of all the supported objects, see **[Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)**.

        

    

- 
**[ApplicationSubtypeDefinition](./tooling_api_objects_applicationsubtypedefinition.htm.md)**  

       Represents a subtype of an application within an application domain.       Available in API version 54.0 and later. 

- 
**[BusinessProcessTypeDef](./tooling_api_objects_businessprocesstypedef.htm.md)**  

       Represents a type of business process within an application domain.       Available in API version 54.0 and later. 

- 
**[ExplainabilityActionDef](./tooling_api_objects_explainabilityactiondef.htm.md)**  

       Represents the explainability definition of the explainability action log          that's generated by the associated application's action. Available in API version 54.0       and later. 

- 
**[ExplainabilityActionVersion](./tooling_api_objects_explainabilityactionversion.htm.md)**  

       Represents the explainability action version of the explainability action log          that's generated by the associated application's action. Available in API version 54.0       and later.

=== ARTICLE: meta_applicationsubtypedefinition.htm ===
---
page_id: meta_applicationsubtypedefinition.htm
title: ApplicationSubtypeDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_applicationsubtypedefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ApplicationSubtypeDefinition

Represents a subtype of an application. Create
			application subtype definitions to define the types of applications used in your
			Decision Explainer entities. 

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ApplicationSubtypeDefinition components have the suffix
					.applicationSubtypeDefinition and are stored in the
					applicationSubtypeDefinition folder.

		

		

## Version

			
			

ApplicationSubtypeDefinition components are available in API version 57.0 and
				later.

		

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

- 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| applicationUsageType | **Field Type** AppDomainUsageType (enumeration of type string) **Description** Required. The application's domain that defines the application's subtype. Possible value: `ExplainabilityService` |
| description | **Field Type** string **Description** The description of the application subtype definition. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for ApplicationSubtypeDefinition, which is defined when the ApplicationSubtypeDefinition is created. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ApplicationSubtypeDefinition component.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<ApplicationSubtypeDefinition
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<masterLabel>ApplicationSubtype1</masterLabel>
	<description>Application Subtype 1</description>
	<applicationUsageType>ExplainabilityService</applicationUsageType>
</ApplicationSubtypeDefinition>
```

			The following is an example `package.xml` that references
				the previous
				definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ApplicationSubtypeDefinition</name>
	</types>
	<version>57.0</version>
</Package>
```

=== ARTICLE: meta_businessprocesstypedefinition.htm ===
---
page_id: meta_businessprocesstypedefinition.htm
title: BusinessProcessTypeDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_businessprocesstypedefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BusinessProcessTypeDefinition

Represents the definition of the business process
			type within an application domain.

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			 This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

BusinessProcessTypeDefinition components have the suffix
					.businessProcessTypeDefinition and are stored in the
					businessProcessTypeDefinition
				folder.

		

		

## Version

			
			

BusinessProcessTypeDefinition components are available in API version 57.0 and
				later.

		

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

- 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| applicationUsageType | **Field Type** AppDomainUsageType (enumeration of type string) **Description** Required. The application's domain that defines the business process type definition. Possible value: `ExplainabilityService` |
| description | **Field Type** string **Description** The description of the business process type definition. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for BusinessProcessTypeDefinition, which is defined when the BusinessProcessTypeDefinition is created. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of a BusinessProcessTypeDefinition component.

			

```

<?xml version="1.0" encoding="UTF-8"?>

<BusinessProcessTypeDefinition
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<masterLabel>ProcessType1</masterLabel>
	<description>Process Type 1</description>
	<applicationUsageType>ExplainabilityService</applicationUsageType>
</BusinessProcessTypeDefinition>
```

			The following is an example `package.xml` that references
				the previous
				definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>BusinessProcessTypeDefinition</name>
	</types>
	<version>57.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
        File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_explainabilityactiondefinition.htm ===
---
page_id: meta_explainabilityactiondefinition.htm
title: ExplainabilityActionDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_explainabilityactiondefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityActionDefinition

Represents the definition of the explainability
			action log that is generated by the associated application's action.

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ExplainabilityActionDefinition components have the suffix
					.explainabilityActionDefinition and are stored in the
					explainabilityActionDefinition
				folder.

		

		

## Version

			
			

ExplainabilityActionDefinition components are available in API version 57.0 and
				later.

		

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

- 
- 

						

						
							

							

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
| actionLogSchemaType | **Field Type** ActionLogSchemaType (enumeration of type string) **Description** Required. The action log schema type of the application.Possible values are: `ExpressionSet` `Other` |
| applicationSubtype | **Field Type** string **Description** Required. The subtype of the associated application for which the explainability log is generated. |
| applicationType | **Field Type** EASAppType (enumeration of type string) **Description** Required. The type of the application for which the explainability log is generated. Possible values are: `ActionableEventOrch` (Available in API version 61.0 and later). `Compliance` (Available in API version 64.0 and later). `EducationCloud` (Available in API version 64.0 and later). `HealthCloud` `IndustriesDroOrderProcess` (Available in API version 61.0 and later). `IndustriesPricing` `IndustryServiceExcellence` `Loyalty` `OmniAnalytics` (Available in API version 61.0 and later). `PatientServicesProgram` `PublicSector` The default value is `PublicSector`. Other application types are available to you depending on your industry solution and permission sets. |
| description | **Field Type** string **Description** The description of the explainability action definition record. |
| internal | **Field Type** boolean **Description** Required. Indicates whether the explainability action definition record is created internally by the Salesforce platform (`true`) or not (`false`). The default value is `false.` |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for ExplainabilityActionDefinition, which is defined when the ExplainabilityActionDefinition is created. |
| processType | **Field Type** string **Description** Required. The process type of the explainability action definition. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExplainabilityActionDefinition component.

			

```

<?xml version="1.0" encoding="UTF-8"?>

<ExplainabilityActionDefinition
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<masterLabel>ActionDefinition1</masterLabel>
	<description>Action Definition 1</description>
	<applicationType>PublicSector</applicationType>
	<applicationSubtype>testType</applicationSubtype>
	<processType>testType</processType>
	<actionLogSchemaType>ExpressionSet</actionLogSchemaType>
	<internal>true</internal>
</ExplainabilityActionDefinition>
```

			The following is an example `package.xml` that references
				the previous
				definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ApplicationSubtypeDefinition</name>
	</types>
	<types>
		<members>*</members>
		<name>BusinessProcessTypeDefinition</name>
	</types>
	<types>
		<members>*</members>
		<name>ExplainabilityActionDefinition</name>
	</types>
	<version>57.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
        File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_explainabilityactionversion.htm ===
---
page_id: meta_explainabilityactionversion.htm
title: ExplainabilityActionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_explainabilityactionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityActionVersion

Represents the explainability action version of the
			explainability action log that is generated by the associated application's
		action.

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ExplainabilityActionVersion components have the suffix
					.explainabilityActionVersion and are stored in the
					explainabilityActionVersion
				folder.

		

		

## Version

			
			

ExplainabilityActionVersion components are available in API version 57.0 and
				later.

		

		

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

						

					

				
| Field Name | Description |
| --- | --- |
| actionLogMessageTemplate | **Field Type** string **Description** The custom message template that is registered by the application. |
| actionSpecification | **Field Type** string **Description** Required. The explainability specification of the application's action log that's generated at runtime and stored as a JSON file. |
| active | **Field Type** boolean **Description** Required. Indicates whether the explainability action version is active and can be used as a specification in the application's action logs. |
| definitionVersion | **Field Type** int **Description** Required. The version of the explainability action definition. |
| description | **Field Type** string **Description** The description of the explainability action version record. |
| explainabilityActionDef | **Field Type** string **Description** Required. The explainability definition of the explainability action log that's generated by the associated application's action. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for ExplainabilityActionVersion, which is defined when the ExplainabilityActionVersion is created. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExplainabilityActionVersion component.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<ExplainabilityActionVersion
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<masterLabel>ActionVersion1</masterLabel>
	<explainabilityActionDef>ActionDef</explainabilityActionDef>
	<description>Version Description</description>
	<actionSpecification>Test action specification</actionSpecification>
	<active>false</active>
	<actionLogMessageTemplate>Test template</actionLogMessageTemplate>
	<definitionVersion>1</definitionVersion>
</ExplainabilityActionVersion>
```

			The following is an example `package.xml` that references
				the previous
				definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ApplicationSubtypeDefinition</name>
	</types>
	<types>
		<members>*</members>
		<name>BusinessProcessTypeDefinition</name>
	</types>
	<types>
		<members>*</members>
		<name>ExplainabilityActionDefinition</name>
	</types>
	<types>
		<members>*</members>
		<name>ExplainabilityActionVersion</name>
	</types>
	<version>57.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
        File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: tooling_api_objects_applicationsubtypedefinition.htm ===
---
page_id: tooling_api_objects_applicationsubtypedefinition.htm
title: ApplicationSubtypeDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_applicationsubtypedefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ApplicationSubtypeDefinition

      Represents a subtype of an application within an application domain.
      Available in API version 54.0 and later. 

      
         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

                  

               

            
| Field | Details |
| --- | --- |
| ApplicationUsageType | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the application's domain that defines the application's subtype. Possible values are: `Explainability Service` The default value is `ExplainabilityService`. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the application subtype definition record. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique name of the application subtype definition. |
| Language | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the application subtype definition. |
| ManageableState | **Type** string **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The UI label of the application subtype definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. |

=== ARTICLE: tooling_api_objects_businessprocesstypedef.htm ===
---
page_id: tooling_api_objects_businessprocesstypedef.htm
title: BusinessProcessTypeDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_businessprocesstypedef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BusinessProcessTypeDef

      Represents a type of business process within an application domain.
      Available in API version 54.0 and later. 

      
         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

                  

               

            
| Field | Details |
| --- | --- |
| ApplicationUsageType | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the application's domain that defines the business process type definition. Possible values are: `Explainability Service` The default value is `ExplainabilityService`. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the business process type definition. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique name of the business process type definition. |
| Language | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the business process type definition. |
| ManageableState | **Type** string **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The UI label of the business process type definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. |

=== ARTICLE: tooling_api_objects_explainabilityactiondef.htm ===
---
page_id: tooling_api_objects_explainabilityactiondef.htm
title: ExplainabilityActionDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_explainabilityactiondef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityActionDef

      Represents the explainability definition of the explainability action log
         that's generated by the associated application's action. Available in API version 54.0
      and later. 

      
         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
| ActionLogSchemaType | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the action log schema type of the application. Possible values are: `ExpressionSet` `Other` The default value is `Other`. |
| ApplicationSubtypeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the subtype of the associated application for which the explainability log is generated. This is a relationship field. **Relationship Name** ApplicationSubtype **Relationship Type** Lookup **Refers To** ApplicationSubtypeDefinition |
| ApplicationType | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of the application for which the explainability log is generated. Possible values are: `ActionableEventOrch` (Available in API version 61.0 and later). `Compliance` (Available in API version 64.0 and later). `EducationCloud` (Available in API version 64.0 and later). `HealthCloud` `IndustriesDroOrderProcess` (Available in API version 61.0 and later). `IndustriesPricing` `IndustryServiceExcellence` `Loyalty` `OmniAnalytics` (Available in API version 61.0 and later). `PatientServicesProgram` `PublicSector` The default value is `PublicSector`. Other application types are available to you depending on your industry solution and permission sets. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the explainability action definition record. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique name of the explainability action definition record. |
| IsInternal | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Nillable, Sort, Update **Description** Indicates whether the explainability action definition record is created internally by the Salesforce platform (`true`) or not (`false`). The default value is `false`. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the explainability action definition. |
| ManageableState | **Type** string **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The UI label of the explainability action definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. |
| ProcessTypeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The process type of the explainability action definition. This is a relationship field. **Relationship Name** ProcessType **Relationship Type** Lookup **Refers To** BusinessProcessTypeDef |

=== ARTICLE: tooling_api_objects_explainabilityactionversion.htm ===
---
page_id: tooling_api_objects_explainabilityactionversion.htm
title: ExplainabilityActionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_explainabilityactionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Decision Explainer
parent_page: decision_explainer_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityActionVersion

      Represents the explainability action version of the explainability action log
         that's generated by the associated application's action. Available in API version 54.0
      and later. 

      
         

#### Important

 Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ActionLogMessageTemplate | **Type** string **Properties** Create, Nillable, Update **Description** The custom message template that is registered by the application. |
| ActionSpecification | **Type** string **Properties** Create, Nillable, Update **Description** The explainability specification of the application's action log that's generated at runtime and stored as a JSON file. |
| DefinitionVersion | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The version of the explainability action definition. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the explainability action version record. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique name of the explainability action version record. |
| ExplainabilityActionDefId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The explainability action definition of which this record is one of the versions. This is a relationship field. **Relationship Name** ExplainabilityActionDef **Relationship Type** Lookup **Refers To** ExplainabilityActionDef |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Nillable, Sort, Update **Description** Indicates whether the explainability action version is active and can be used as a specification in the application's action logs (`true`) or not (`false`). The default value is `false`. |
| Language | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the explainability action version. |
| ManageableState | **Type** string **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, NIllable, Sort, Update **Description** The UI label of the explainability action version. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. |

