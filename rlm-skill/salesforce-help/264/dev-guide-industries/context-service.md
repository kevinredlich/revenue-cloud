# Industries Common Resources Developer Guide 264 — sección: Context Service (131 artículos)

=== ARTICLE: actions_obj_build_context.htm ===
---
page_id: actions_obj_build_context.htm
title: Build Context Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_build_context.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Build Context Action

Build and cache context data associated with a context definition.

        
            

This action is available in API version 59.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`59.0`/actions/standard/buildContext`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextData | **Type** string **Description** Optional. JSON data that's used to build context data. |
| contextDefinitionId | **Type** string **Description** Required. The ID or developer name of the context definition record that's used to build context data. |
| contextMappingId | **Type** string **Description** Optional. The context mapping record ID or name that identifies which Salesforce object and mappings to use for building context data. |
| isTaggedData | **Type** boolean **Description** Optional. Indicates whether the associated context node is tagged with a key (`true`) or not (`false`). |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| contextDefinitionId | **Type** string **Description** The ID or Developer Name of the Context Definition record that was used to build context data. |
| contextId | **Type** string **Description** ID of the cached context data. |
| contextMappingId | **Type** string **Description** The Context Mapping record ID or Name that identifies which Salesforce object and mappings to use for building context data. |

        

        

## Usage

Build context invocable action is a wrapper over Build Context
            business API. The API fetches the data passed in request and saves the data to the
            cache. This is useful when the same data is required in multiple steps of the
            process.

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Build Context action. In this example, we
                            are inserting new records to hydrate input values (input hydration). To
                            use existing records instead, reference the IDs directly rather than
                            providing full record data.

                        

```
{
  "inputs": [
    {
      "contextDefinitionId": "AccountContextDef",
      "ContextData": {
        "Account": [
          {
            "id": "account1",
            "businessObjectType": "Account",
            "Name": "AcmeFlow",
            "Contact": [
              {
                "id": "contact1",
                "businessObjectType": "Contact",
                "FirstName": "John",
                "LastName": "Miller",
                "ParentReference": "account1"
              }
            ]
          }
        ]
      },
    "contextMappingId": "accountmap1",
    "isTaggedData": false
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Build Context action.

                        

```
{
  "actionName": "buildContext",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outputValues": {
    "contextDefinitionId": "11Oxx0000006PXVEA2",
    "contextId": "0000000a07da091002517526756248297be68492e6b442e8ad80182d518e45aa",
    "contextMappingId": "11jxx0000004L59AAE"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_delete_context_cache.htm ===
---
page_id: actions_obj_delete_context_cache.htm
title: Delete Context Cache Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_delete_context_cache.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Delete Context Cache Action

Delete the specified context instance from the in-memory context cache using the
        provided context ID. This action removes the cached data maintained by the context cache
        service without performing any database write operations.

        
            

This action is available in API version 63.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`59.0`/actions/standard/deleteContextCache`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextId | **Type** string **Description** Required. ID of the context instance. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Delete Context Cache action.

                        

```
{
  "inputs": [
    {
      "contextId": "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609"
    }
  ]
}
```

=== ARTICLE: actions_obj_delete_context_records.htm ===
---
page_id: actions_obj_delete_context_records.htm
title: Delete Context Records Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_delete_context_records.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Delete Context Records Action

Deletes one or more records from a context instance.

        
            

This action is available in API version 67.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`68.0`/actions/standard/deleteContextRecords`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextId | **Type** string **Description** Required. ID of the context instance from which records are deleted. |
| dataPaths | **Type** List<String> **Description** Required. A collection of data path objects that identify the records to delete from the context instance. Each object contains a `dataPath` field whose value is a list of strings representing the hierarchical path from the root to the target record in the context. |
| isPermanent​Delete | **Type** boolean **Description** Optional. Indicates whether the record is permanently deleted (`true`) or not (`false`). The default value is `false`. |

        

        

## Usage

            
            

Use this action to delete one or more records from a context instance. By default,
                records are soft deleted. To permanently delete the records, set `isPermanentDelete` to `true`.

        

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Delete Context Records action.

                        

```
{
  "inputs": [
    {
      "contextId": "0000000a07da091002517526756248297be68492e6b442e8ad80182d518e45aa",
      "dataPaths": [
        { "dataPath": ["001xx000003GbMhAAK", "003xx000004Wia5AAC"] }
      ],
      "isPermanentDelete": false
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Delete Context Records action.

                        

```
[
  {
    "actionName": "deleteContextRecords",
    "errors": null,
    "isSuccess": true,
    "outputValues": {}
  }
]
```

=== ARTICLE: actions_obj_persist_context_data.htm ===
---
page_id: actions_obj_persist_context_data.htm
title: Persist Context Data Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_persist_context_data.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Persist Context Data Action

Store cached context data associated with a context mapping ID in a Salesforce
        record.

        
            

This action is available in API version 59.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`59.0`/actions/standard/persistContextData`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextId | **Type** string **Description** Required. The ID of the context data record with cached data that's to be stored in the database. |
| contextMappingId | **Type** string **Description** Optional. The Context Mapping record ID or Name that's used to transform cached context data into the associated fields of the related Salesforce record. |
| trackingId | **Type** string **Description** Optional. The ID of a Context Mapping record that's used to transform cached context data into the associated fields of the related Salesforce record. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| referenceId | **Type** string **Description** The ID of a response event that's used to track the request processing status and to get the full request response. |

        

        

## Usage

Persist Context Data invocable action is a wrapper over Persist
            Context data Connect API. It provides the ability to store the context data present in
            cache to database. Any update in context data can be persisted in database, if
            required.

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Persist Context Data action.

                        

```
{
  "inputs": [
    {
      "contextId": "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609",
      "contextMappingId": "16Pxx0000004CCGEA2",
      "trackingId": "16Pxx0000004CCGEA2"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Persist Context Data action.

                        

```
{
  "actionName": "persistContextData",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outputValues": {
    "referenceId": "16Pxx0000004CAeEAM"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_query_context_tags.htm ===
---
page_id: actions_obj_query_context_tags.htm
title: Query Context Tags Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_query_context_tags.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Tags Action

Query the tag values from an instance that are associated with a context
        definition.

        
            

This action is available in API version 63.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`59.0`/actions/standard/queryContextTags`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextId | **Type** string **Description** Required. The ID of the context instance. |
| tagsList | **Type** string **Description** Required. A collection of tags to be queried. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| queryResult | **Type** string **Description** The output of the queried context instance. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Query Context Tags action.

                        

```
{
  "inputs": [
    {
      "contextId": "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609",
      "tagList": [
        "Account_Name",
        "Contact_LastName"
      ]
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Query Context Tags action.

                        

```
{
  "actionName": "queryContextTags",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outputValues": {
    "queryResult": {
      "Contact_LastName": [
        {
          "tagValue": "Miller",
          "dataPath": [
            "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609",
            "account1",
            "contact1"
          ],
          "eTag": "fba12e2955bf4a46354fee73ee8b238c",
          "weakEtag": 0
        }
      ],
      "Account_Name": [
        {
          "tagValue": "AcmeFlow",
          "dataPath": [
            "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609",
            "account1"
          ],
          "eTag": "fa0867f98939f191957687c1456715f7",
          "weakEtag": 0
        }
      ]
    }
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_update_context_attributes.htm ===
---
page_id: actions_obj_update_context_attributes.htm
title: Update Context Attributes Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_update_context_attributes.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Update Context Attributes Action

Update the attributes in the context instance using tags.

        
            

This action is available in API version 63.0 and later.

        

        

## Special Access Rules

            
            

Available in Developer, Enterprise, Professional, and Unlimited editions for
                Industries clouds where Context Service is enabled.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: 
`/services/data/v`59.0`/actions/standard/updateContextAttributes`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: POST

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
            

        

        

## Inputs

            
            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| contextId | **Type** string **Description** Required. ID of the context instance. |
| nodePathAndUpdatedValues | **Type** string **Description** Optional. The JSON containing the node path and its updated values. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Update Context Attributes action.

                        

```
{
  "inputs": [
    {
      "contextId": "0000000a07da09100251752497651022c35b6150a4d04cd6a84bf1a0439cc609",
      "NodePathAndUpdatedValues": [
        {
          "nodePath": {
            "dataPath": [
              "account1",
              "contact1"
            ]
          },
          "tagValues": [
            {
              "tagName": "Contact_LastName",
              "tagValue": "UPDATED_MILLER"
            }
          ]
        }
      ]
    }
  ]
}
```

=== ARTICLE: apex_class_Context_IndustriesContext.htm ===
---
page_id: apex_class_Context_IndustriesContext.htm
title: IndustriesContext Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_class_Context_IndustriesContext.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: apex_namespace_Context.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# IndustriesContext Class

Contains methods to create, query, persist, or delete a context. Also, query a record's
    status, query a context based on tags, or update context attributes by using the available
    methods.

## Namespace

[Context](#apex_class_Context_IndustriesContext)

- 
**[IndustriesContext Methods](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_methods)**  

Learn more about the available methods with the `IndustriesContext` class.

  

## IndustriesContext Methods

  
  
  
Learn more about the available methods with the `IndustriesContext` class.

    
      

The `IndustriesContext` class includes these methods.

    

    
  

- 
**[addRecordsToContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_addRecordsToContext)**  

Adds one or more records at a user-defined level in the hierarchy of the         context.

- 
**[buildContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_buildContext)**  

Creates a context.

- 
**[deleteContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_deleteContext)**  

Deletes a context.

- 
**[deleteRecords(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_deleteRecords)**  

Deletes one or more records from a context session identified by data         paths.

- 
**[evictContextDefinition(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_evictContextDefinition)**  

Removes the details of the context definition from cache.

- 
**[filteringContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_filteringContext)**  

Builds or queries a context based on a filter criteria.

- 
**[getContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_getContext)**  

Retrieves context details.

- 
**[getContextTranslation(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_getContextTranslation)**  

Retrieves context mappings based on a target mapping ID.

- 
**[leanerQueryTags(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_leanerQueryTags)**  

Queries context tags and returns an optimized, leaner result set compared to the standard     queryTags.

- 
**[persistContext(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_persistContext)**  

Persists the current data or state of context to the database.

- 
**[queryContextRecordsAndChildren(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_queryContextRecordsAndChildren)**  

Queries Context records and children based on the dataPath instead of         tags.

- 
**[queryRecordStatus(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_queryRecordStatus)**  

Queries the status of a record.

- 
**[queryTags(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_queryTags)**  

Queries a context by using tags.

- 
**[updateContextAttributes(input)](./apex_class_Context_IndustriesContext.htm.md#apex_Context_IndustriesContext_updateContextAttributes)**  

Updates the attributes of a context. 

    

### addRecordsToContext(input)

    
    
    
Adds one or more records at a user-defined level in the hierarchy of the
        context.

        

#### Signature

            
            

`public Map<String,Object>
                    addRecordsToContext(Map<String,Object> input)`

            

```
Context.IndustriesContext, addRecordsToContext, [Map<String,ANY>], Map<String,ANY>
```

        

        

#### Example

            
            

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();

Map<String, Object> inputAddRecord = new Map<String, Object>();
inputAddRecord.put('contextId', context.get('contextId').toString());
inputAddRecord.put('overWriteExistingRecords', true);
inputAddRecord.put('isTaggedData', false);
inputAddRecord.put('inputData', '{\"Account\":[{\"id\":\"synthetic\",\"businessObjectType\":\"Account\",\"Name\":\"test_account\"}]}');

Map<String, Object> ouputAddRecord = industriesContexts.addRecordsToContext(inputAddRecord);

```

        

        

#### Parameters

            
            
                
                    

**input**

                    
: Type: Map<String,Object>

                    
: 
                        
                            
                                

**contextId**

                                
: Type: String

                                
: ID of the Context to which record described in inputData is
                                    added.

                            
                            
                                

**overWriteExistingRecords**

                                
: Type: Boolean

                                
: Indicates if an already existing record with same ID as being
                                    added through inputData must be overriden.

                            
                            
                                

**inputData**

                                
: Type: String

                                
: Record data to be added to the context, hierarchical data in
                                    stringified format.

                            
                            
                                

**isTaggedData**

                                
: Type: Boolean

                                
: Describes if the inputData structure is using the taggedData
                                    Format.

                            
                        

                    

                
            

        

        

#### Return Value

            
            

Type: Map<String,Object>

        

    

### buildContext(input)

Creates a context.

    

#### Signature

      
      

`public Map<String,Object>
          buildContext(Map<String,Object> input)`

      

```
Context.IndustriesContext, buildContext, [Map<String,ANY>], Map<String,ANY>
```

    

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();

Map<String, Object> input = new Map<String, Object>(); 

Map<String, String> metadata = new Map<String, String>(); 
metadata.put('contextDefinitionId', '11Oxx0000006PinEAE');
metadata.put('mappingId','11jxx0000004LGRAA2');

String data = '{\'Account\':[{\'id\':\'001xx000003GYK0AAO\',\'businessObjectType\':\'Account\'}]}';
input.put('data', data);
input.put('metadata', metadata);

Map<String, Object> context = industriesContexts.buildContext(input);
System.debug(context.get('contextId'));
```

    

    

#### Parameters

      
      
        
          

**input**

          
: Type: Map<String,Object>

          
: Metadata about the context and payload data required to create a context.

        
      

    

    

#### Return Value

      
      

Type: Map<String,Object>

      

Details containing the context ID that’s created.

    

  

### deleteContext(input)

Deletes a context.

#### Signature

`public void deleteContext(Map<String,Object> input)`

```
Context.IndustriesContext, deleteContext, [Map<String,ANY>], void
```

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
input.put('contextId', '1f6ef0f4f9f361ef966d8a292db12ce90ce20bef22efb4afac431762ac71998d');
industriesContexts.deleteContext(input);
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details containing the ID of the context to be deleted.

#### Return Value

Type: void

    

### deleteRecords(input)

    
    
    
Deletes one or more records from a context session identified by data
        paths.

        

#### Signature

            
            

`public Map<String,Object>
                    deleteRecords(Map<String,Object> input)`

            

```
Context.IndustriesContext, deleteRecords, [Map<String,ANY>], Map<String,ANY>
```

        

        

#### Example

            
            

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();

Map<String, Object> input = new Map<String, Object>();
input.put('contextId', context.get('contextId').toString());

List<Map<String, Object>> dataPaths = new List<Map<String, Object>>();
Map<String, Object> dataPath1 = new Map<String, Object>();
dataPath1.put('dataPath', new List<String>{'001xx000003GbMhAAK', '003xx000004Wia5AAC'});
dataPaths.add(dataPath1);

input.put('dataPaths', dataPaths);
input.put('isPermanentDelete', false);

Map<String, Object> output = industriesContexts.deleteRecords(input);
System.debug('isSuccess: ' + output.get('isSuccess'));

```

        

        

#### Parameters

            
            
                
                    

**input**

                    
: Type: Map<String,Object>

                    
: 
                        
                            
                                

**contextId**

                                
: Type: String

                                
: Required. ID of the context session from which records are
                                    deleted.

                            
                            
                                

**dataPaths**

                                
: Type: List<Map<String,Object>>

                                
: Required. List of data path objects that identify records for
                                    deletion. Each object contains a `dataPath` key with record IDs that define the
                                    hierarchical path between the root and target record in the
                                    context.

                            
                            
                                

**isPermanentDelete**

                                
: Type: Boolean

                                
: Optional. Indicates whether the deletion is permanent (`true`) or not (`false`). If `false`, records are soft-deleted
                                    and marked as deleted within the context. If `true`, records are permanently
                                    removed from the context. The default value is `false`.

                            
                        

                    

                
            

        

        

#### Return Value

            
            

Type: Map<String,Object>

            
                
                    

**isSuccess**

                    
: Type: Boolean

                    
: Returns `true` if the delete operation
                        completed successfully.

                
            

        

    

### evictContextDefinition(input)

Removes the details of the context definition from cache.

    

#### Signature

      
      

`public void evictContextDefinition(Map<String,ANY>
          input)`

      

```
Context.IndustriesContext, evictContextDefinition, [Map<String,ANY>], void
```

    

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
input.put('contextDefinitionName', 'definitionName');
industriesContexts.evictContextDefinition(input);
```

    

    

#### Parameters

      
      
        
          

**input**

          
: Type: Map<String,ANY>

          
: API name of the context definition to remove the details of the context definition
            from cache.

        
      

    

    

#### Return Value

      
      

Type: void

    

  

    

### filteringContext(input)

    
    
    
Builds or queries a context based on a filter criteria.

        

#### Signature

            
            

`public Map<String, Object>
                    industriesContexts.filteringContext(buildWithFilter);`

        

        

#### Example

Type:
                BUILD

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> buildWithFilter = new Map<String, Object>();
Map<String, Object> input = new Map<String, Object>();

Map<String, String> metadata = new Map<String, String>();
metadata.put('contextDefinitionId', '11Oxx0000006PXVEA2');
metadata.put('mappingId','11jxx0000004L59AAE');

String data = '{\'Account\':[{\'id\':\'001xx000003GYiCAAW\',\'businessObjectType\':\'Account\'}]}';
input.put('data', data);
input.put('metadata', metadata);

buildWithFilter.put('type', 'BUILD');
buildWithFilter.put('build', input);
buildWithFilter.put('filter', '{ \"buildFilter\": {\"Contact\":[{\"filterType\":\"WHERE\",\"node\":\"Contact\",\"attribute\":\"Name\",\"dataType\":\"String\",\"operands\":[\"Howard Jones\"],\"operator\":\"Equals\"}]}}');

Map<String, Object> res = industriesContexts.filteringContext(buildWithFilter);

System.debug(res);

```

Type: QUERYRECORDANDCHILDREN or
                    QUERYRECORDS

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> queryWithFilter = new Map<String, Object>();
Map<String, Object> queryInput = new Map<String, Object>();

List<String> dataPath = new List<String>();
dataPath.add('001xx000003GYiCAAW');

Map<String, Object> contextDataPathInputRepresentation = new Map<String, Object>();
contextDataPathInputRepresentation.put('dataPath', dataPath);

List<Map<String, Object>> queryPaths = new List<Map<String, Object>>();
queryPaths.add(contextDataPathInputRepresentation);

queryInput.put('contextId', '44410fea80348668bebd58010279c579d611a8f686ebf71e6b2a6b1a6405160f');
queryInput.put('queryPaths', queryPaths);

queryWithFilter.put('type', 'QUERYRECORDANDCHILDREN');
queryWithFilter.put('query', queryInput);
queryWithFilter.put('filter', '{\"queryFilter\":[{\"filterType\":\"WHERE\",\"node\":\"Contact\",\"attribute\":\"Name\",\"dataType\":\"String\",\"operands\":[\"Howard Jones\"],\"operator\":\"Equals\"}]}');

Map<String, Object> res = industriesContexts.filteringContext(queryWithFilter);

System.debug(res);

```

        

#### Parameters

            
            
                
                    

**input**

                    
: Type: Enum

                    
: Object defining the type of operation. Operation Metadata along with filter
                        criteria to be applied on the operation. Valid values are:
                            BUILD,QUERYRECORDANDCHILDREN and
                            QUERYRECORDS

                
                
                    
: filter: String

                    
: Metadata about the filter object.

                
                
                    
: build: Map<String,Object>

                    
: Metadata to build the context. Only for type with value
                            BUILD. 

                
                
                    
: query: Map<String,Object>

                    
: Metadata to query records in the context. Only for type
                        with value QUERYRECORDANDCHILDREN and
                            QUERYRECORDS.

                
            

        

        

#### Return Value

            
            

Type: Map<String,Object>

            

Mapping of the contextId or queryResults with the requested operation type.

        

    

### getContext(input)

Retrieves context details.

#### Signature

`public Map<String,Object> getContext(Map<String,Object> input)`

```
Context.IndustriesContext, getContext, [Map<String,ANY>], Map<String,ANY>
```

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();

input.put('contextId', '03950312e509b6ae5c41653408fe4869efc931cc0ffd0e61f5599daa59a22309');
Map<String, Object> res = industriesContexts.getContext(input);

System.debug(res);
```

    

#### Parameters

**input**

: Type: Map<String,Object>

          
: Details containing the ID of the context to be retrieved.

#### Return Value

Type: Map<String,Object>

Details of the retrieved context.

### getContextTranslation(input)

Retrieves context mappings based on a target mapping ID.

#### Signature

`public Map<String,Object> getContextTranslation(Map<String,Object> input)`

```
Context.IndustriesContext, getContextTranslation, [Map<String,ANY>], Map<String,ANY>
```

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
input.put('contextId', '1f6ef0f4f9f361ef966d8a292db12ce90ce20bef22efb4afac431762ac71998d');
input.put('contextMappingId', '11jxx0000004LGRAA2');
List<String> persistAttibuteTypes = new List<String>();
persistAttibuteTypes.add('OUTPUT');
persistAttibuteTypes.add('INPUTOUTPUT');
input.put(‘persistAttibuteTypes’,  persistAttibuteTypes);
Boolean isDependenciesEstablished = false;
input.put(‘isDependenciesEstablished’, isDependenciesEstablished);
Boolean removeRestrictedFields = false;
input.put(‘removeRestrictedFields’, removeRestrictedFields);
Map<String, Object> res = industriesContexts.getContextTranslation(input);
System.debug(res);
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details of the request parameters to retrieve context mappings. The details include list of
            persisted attributes and settings to indicate whether any dependencies are established
            or restricted fields are removed.

#### Return Value

Type: Map<String,Object>

Details of the retrieved context mappings.

### leanerQueryTags(input)

  
Queries context tags and returns an optimized, leaner result set compared to the standard
    queryTags.

#### Signature

`public Map<String,Object> leanerQueryTags(Map<String,Object> input)`

    

#### Usage

      
      

Use the `leanerQueryTags` method to retrieve tag values
                from a context instance with optimized performance. This method returns a leaner
                result set.

      

Before calling this method, you must first create a context instance using the `buildContext` method and obtain the `contextId`.

    

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>(); 
Map<String, String> metadata = new Map<String, String>(); 
metadata.put('contextDefinitionName', 'SimpleDef');
metadata.put('mappingName','Mapping1');

String data = '{\'Account\':[{\'id\':\'001xx000003GYiBAAW\',\'businessObjectType\':\'Account\'}]}';
input.put('data', data);
input.put('metadata', metadata);                 

Map<String, Object> context = industriesContexts.buildContext(input);
System.debug(context.get('contextId'));

Map<String, Object> inputTag = new Map<String, Object>(); 
List<String> tag = new List<String>();
tag.add('Contact');
inputTag.put('contextId', (String)context.get('contextId'));
inputTag.put('tags', tag);
Map<String, Object> output = industriesContexts.leanerQueryTags(inputTag);

Map<String, Object> queryresult = (Map<String, Object>)output.get('leanerQueryTagResult');
List<String> recordIds = (List<String>)output.get('recordIds');

system.debug('Context id is: ' + output.get('contextId'));
system.debug('Record Ids list: ' + recordIds);

List<Object> contextTagDataLeanRepresentations= (List<Object>)queryresult.get('Contact_FirstName');
Map<String,Object> contextTagDataLeanRepresentation = (Map<String,Object>)contextTagDataLeanRepresentations.get(0);

for (String contextTagDataLeanRepresentationKey : contextTagDataLeanRepresentation.keySet()) {
    if(contextTagDataLeanRepresentationKey == 'tagValue'){
        if (contextTagDataLeanRepresentation.get(contextTagDataLeanRepresentationKey) instanceof Map<String, Object>) {
            Map<String, Object> accountData = (Map<String, Object>)contextTagDataLeanRepresentation.get(contextTagDataLeanRepresentationKey);

            for (String accountDataKey: accountData.keySet()) {
                Map<String, Object> attributeTagData = (Map<String, Object>)accountData.get(accountDataKey);
    
                system.debug('attributeTagData keys:: ' + attributeTagData.keySet());
                for (String attributeTagDataKey: attributeTagData.keySet()) {
                    system.debug('attributeTagDataKey:: ' + attributeTagDataKey);
                    system.debug('attributeTagDataValue:: ' + attributeTagData.get(attributeTagDataKey));
                    
                }
            }    
        } else {
            for (String key: contextTagDataLeanRepresentation.keySet()) {
                system.debug('key: ' + key);
                system.debug('value: ' +contextTagDataLeanRepresentation.get(key));
                
            }
        }
        
    }
}
```

    

#### Parameters

**input**

: Type: Map<String,Object>

          
: Input map that contains the parameters required to query the tags. Valid keys are:
              
- 
contextId: (String) — ID of the context to query[cite:
                223].

              
- 
tags: (List<String>) — List of tag names to query from
                the context instance. Tags serve as aliases for nodes and attributes in the context
                structure.

            

#### Return Value

Type: Map<String,Object>

      

Returns a map that contains the query results. The map includes these keys:

      
        
- 
`contextId` (String) — ID of the context
                    instance.

        
- 
`recordIds` (List<String>) — List of record IDs
                    associated with the queried tags.

        
- 
`leanerQueryTagResult` (Map<String,Object>) —
                    Map that contains the query results. Each key represents a tag name, and its
                    value contains the associated tag data with attribute information.

      

### persistContext(input)

Persists the current data or state of context to the database.

#### Signature

`public Map<String,Object> persistContext(Map<String,Object> input)`

```
Context.IndustriesContext, persistContext, [Map<String,ANY>], Map<String,ANY>
```

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
input.put('contextId', '5a42181d891c60f0097d50e0e1d52d6009ee3ef593d9ea145e1f4e05996a17c6');
input.put('targetMappingId', '');
Map<String, Object> output = industriesContexts.persistContext(input);
System.debug(output.get('referenceId'));
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details to persist context such as context ID and target mapping ID.

#### Return Value

Type: Map<String,Object>

Reference ID for the persisted context.

    

### queryContextRecordsAndChildren(input)

    
    
    
Queries Context records and children based on the dataPath instead of
        tags.

        

#### Signature

            
            

`Map<String, Object>
                    industriesContexts.queryContextRecordsAndChildren(input: Map<String,
                    Object>);`

        

        

#### Example

            
            

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();

List<String> dataPath = new List<String>();
dataPath.add('001xx000003GaX6AAK');

Map<String, Object> contextDataPathInputRepresentation = new Map<String, Object>();
contextDataPathInputRepresentation.put('dataPath', dataPath);

List<Map<String, Object>> queryPaths = new List<Map<String, Object>>();
queryPaths.add(contextDataPathInputRepresentation);

input.put('contextId', '7a823bc5f047b1b69aa059b05c3df0ccd69b1bc702e03b4f6c12740d0e277b7b');
input.put('queryPaths', queryPaths);

Map<String, Object> res = industriesContexts.queryContextRecordsAndChildren(input);

System.debug(res);

            
```

        

        

#### Parameters

            
            
                
                    

**input**

                    
: contextId: String

                    
: ID of the context to be queried.

                
                
                    
: queryPaths: Map<String,Object>

                    
: List of dataPath to be queried.

                
            

        

        

#### Return Value

            
            

queryResults: Map<String,Object>

            

Result containing the record data.

        

    

### queryRecordStatus(input)

Queries the status of a record.

#### Signature

`public Map<String,Object> queryRecordStatus(Map<String,Object> input)`

```
Context.IndustriesContext, queryRecordStatus, [Map<String,ANY>], Map<String,ANY>
```

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
input.put('contextId', '5a42181d891c60f0097d50e0e1d52d6009ee3ef593d9ea145e1f4e05996a17c6');
List<Map<String,Object>> queryPaths = new List<Map<String,Object>>();
Map<String,Object> queryPath = new Map<String,Object>();
List<String> dataPaths = new List<String>();
dataPaths.add('TestOrder123');
queryPath.put('dataPath', dataPaths);
queryPaths.add(queryPath);
input.put('queryPaths', queryPaths);
Map<String, Object> output = industriesContexts.queryRecordStatus(input);
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details containing the context ID and list of record paths for context data to query the status
            for.

#### Return Value

Type: Map<String,Object>

Details containing the results of the query.

### queryTags(input)

Queries a context by using tags.

#### Signature

`public Map<String,Object> queryTags(Map<String,Object> input)`

```
Context.IndustriesContext, queryTags, [Map<String,ANY>], Map<String,ANY>
```

    

#### Usage

      
      

The method works on the `tagNames` of the attribute or
        node.

    

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>(); 
List<String> tag = new List<String>();
tag.add('contactNameTag');
input.put('contextId', '967934fc3069c04bb17df94e526052d75ab99fd87393ffad008ed07d7ac54a13');
input.put('tags', tag);
Map<String, Object> output = industriesContexts.queryTags(input);
Map<String, Object> queryresult = (Map<String, Object>)output.get('queryResult');
List<Object> contextTagDataRepresentations= (List<Object>)queryresult.get('contactNameTag');
Map<String,Object> contextTagDataRepresentation = (Map<String,Object>)contextTagDataRepresentations.get(0);
System.debug(contextTagDataRepresentation.get('dataPath'));
System.debug(contextTagDataRepresentation.get('tagValue'));
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details containing the context ID and tags to be queried.

#### Return Value

Type: Map<String,Object>

      

Details containing the results of the query.

### updateContextAttributes(input)

Updates the attributes of a context. 

#### Signature

`public Map<String,Object> updateContextAttributes(Map<String,Object> input)`

```
Context.IndustriesContext, updateContextAttributes, [Map<String,ANY>], Map<String,ANY>
```

    

#### Usage

      
      

Use this method to update the attributes of a context.

      
        
-  This method works only with the names of the canonical structure, and not with
          tags.

        
-  The dataType of the values must match the dataType in the canonical structure. Also, it
          must match the dataType of the field if persistence is expected later. 

        
- The method supports attribute updates at different level. Pass an attributeMap
          corresponding to the given dataPath.

        
- The API works at the per-record level.

      

    

    

#### Example

      
      

```
Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
Map<String, Object> input = new Map<String, Object>();
Map<String, Object> contextAttributeValueInputRepresentation = new Map<String, Object>();
contextAttributeValueInputRepresentation.put('attributeName', 'Name');
contextAttributeValueInputRepresentation.put('attributeValue', 'Elon');

List<Map<String, Object>> attributes = new List<Map<String, Object>>();
attributes.add(contextAttributeValueInputRepresentation);

List<String> dataPath = new List<String>();
dataPath.add('001xx000003GaX6AAK');

Map<String, Object> contextDataPathInputRepresentation = new Map<String,Object>();
contextDataPathInputRepresentation.put('dataPath', dataPath);

Map<String, Object> nodePathAndAttributesInputRepresentation = new Map<String, Object>();
nodePathAndAttributesInputRepresentation.put('nodePath', contextDataPathInputRepresentation);
nodePathAndAttributesInputRepresentation.put('attributes', attributes);

List<Map<String, Object>> nodePathAndAttributes = new List<Map<String, Object>>();
nodePathAndAttributes.add(nodePathAndAttributesInputRepresentation);

input.put('contextId', 'f4fe20aa8ffb441998a3bba42c7a0452d9b104dcadd9907810cbacff4db7c39a');
input.put('nodePathAndAttributes', nodePathAndAttributes);

Map<String, Object> res = industriesContexts.updateContextAttributes(input);

System.debug(res.get('isSuccess'));
```

    

#### Parameters

**input**

: Type: Map<String,Object>

: Details containing the context ID and node path. The node path contains the path of the context
            record and list of attributes to be updated with their values.

#### Return Value

Type: Map<String,Object>

Details containing the updated attribute list.

=== ARTICLE: apex_namespace_Context.htm ===
---
page_id: apex_namespace_Context.htm
title: Context Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_namespace_Context.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Namespace

The `Context` namespace provides classes and methods to
    manage the sharing and consumption of business application data by using Context
    Service.

The `Context` namespace includes these classes.

- 
**[IndustriesContext Class](./apex_class_Context_IndustriesContext.htm.md#apex_class_Context_IndustriesContext)**  

Contains methods to create, query, persist, or delete a context. Also, query a record's     status, query a context based on tags, or update context attributes by using the available     methods.

=== ARTICLE: connect_requests_context_attr_hydration_details_input.htm ===
---
page_id: connect_requests_context_attr_hydration_details_input.htm
title: Context Attribute Hydration Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_attr_hydration_details_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Hydration Details Input

Input representation of context attribute hydration detail.

**Properties**

: 

                    

                    

                    

                    

                    

                  

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `childDetails` | Context Attribute Hydration Details Input[] | Child of hydration details. | Required | 59.0 |
| `contextAttrHydrationDetailId` | String | ID of the hydration detail record. This field is required for the update request. | Optional | 59.0 |
| `parentAttributeMappingId` | String | ID of the parent context attribute mapping record. | Required | 59.0 |
| `parentDetailId` | String | ID of the parent context attribute hydration detail record. | Required | 59.0 |
| `queryAttribute` | String | Query attribute. | Optional | 59.0 |
| `sObjectDomain` | String | SObject domain. | Optional | 59.0 |

=== ARTICLE: connect_requests_context_attribute_input.htm ===
---
page_id: connect_requests_context_attribute_input.htm
title: Context Attribute Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_attribute_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Input

Input representation for updating context attribute.

    
      
        
          

**JSON example**

          
: 
            

```
{
    "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
    "nodePathAndAttributes": [
        {
            "nodePath": {
                "dataPath": [
                    "TestOrder123"
                ]
            },
            "attributes": [
                {
                    "attributeName": "Status",
                    "attributeValue": "DISPATCHED"
                }
            ]
        }
    ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `updateContextAttributesInput` | Object | Input object for updating context attributes. | Required | 59.0 |

=== ARTICLE: connect_requests_context_attribute_mappings_input.htm ===
---
page_id: connect_requests_context_attribute_mappings_input.htm
title: Context Attribute Mappings Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_attribute_mappings_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Mappings Input

Input representation of context attribute mapping.

            
        
                    

**JSON example**

                    
: 
                        

```
{
    "contextAttributeMappings": [
        {
            "contextAttributeId": "11nxx000001hIgLAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Status"
                    }
                ]
            }
        },
        {
            "contextAttributeId": "11nxx000001hKiFAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Name"
                    }
                ]
            }
        }
    ]
}
```

                    

                    
: This example shows a JSON sample when context-to-context mappings
                        exist.

                    
: 
                        

```
{
  "contextMappings": [
    {
      "contextMappingId": "11jxx0000005UXnAAM",
      "contextNodeMappings": {
        "contextNodeMappings": [
          {
            "attributeMappings": {
              "contextAttributeMappings": [
                {
                  "hydrationDetails": {
                    "contextAttrContextHydrationDetails": [
                      {
                        "queryAttribute": "11nxx000001hGTFAA2",
                        "parentAttributeMappingId": "11Rxx00000058LcEAI"
                      }
                    ]
                  },
                  "contextAttributeId": "11nxx000001ihzFAAQ",
                  "contextInputAttributeName": "Node1A1"
                }
              ]
            },
            "contextNodeId": "11oxx000001HS0iAAG",
            "mappedContextNodeId": "11oxx000001G0mSAAS",
            "sObjectName": "Node1"
          }
        ]
      },
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ],
      "mappedContextDefinitionName": "11Oxx0000006PZ8EAM",
      "isDefault": false
    }
  ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the context attribute record. | Required | 59.0 |
| `contextAttributeMappingId` | String | ID of the context attribute mapping record. | Required | 59.0 |
| `contextInputAttributeName` | String | Context input attribute name. | Optional | 59.0 |
| `hydrationDetails` | [Context Attribute Hydration Details Input](./connect_requests_context_attr_hydration_details_input.htm.md)[] | List of context attribute hydration detail. | Optional | 59.0 |

=== ARTICLE: connect_requests_context_attributes_input.htm ===
---
page_id: connect_requests_context_attributes_input.htm
title: Context Attributes Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_attributes_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attributes Input 

Input representation of context attribute.

**JSON example**

: 

```
{
    "contextAttributes": [
        {
            "dataType": "STRING",
            "fieldType": "INPUT",
            "name": "Attribute_5",
            "tags": {
                "contextTags": [
                    {
                        "name": "Attribute_5_Tag"
                    }
                ]
            }
        },
        {
            "dataType": "NUMBER",
            "fieldType": "OUTPUT",
            "name": "Attribute_6"
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the attribute. | Required | 59.0 |
| `dataType` | String | Data type of the attribute. | Required | 59.0 |
| `domainSet` | String | Comma separated node names referenced by this attribute. | Optional | 59.0 |
| `fieldType` | String | Field type of the attribute. | Required | 59.0 |
| `isKey` | Boolean | Specifies if it used for transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `isValue` | Boolean | Specifies if it used for transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the attribute. | Required | 59.0 |
| `tags` | [Context Tag Input](./connect_requests_context_tag_input.htm.md)[] | List of tags for the attribute. | Optional | 59.0 |

=== ARTICLE: connect_requests_context_definition_filter_input.htm ===
---
page_id: connect_requests_context_definition_filter_input.htm
title: Context Definition Filter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_definition_filter_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filter Input

Input representation details of context definition filter.

        
          
: 
This example shows a sample request to
            create, get, or update a context definition filter.
            

```
{
      "description": "Updated",
      "filterApiName": "FilterAccount",
      "filterName":"FilterAccount",
      "filtersPerNode": "{\"Account\":{\"filterCondition\":{\"attribute\":\"City\",\"operator\":\"EQUALS\",\"operands\":[{\"value\":\"Bengaluru\",\"type\":\"STRING\"}],\"composite\":false},\"orderByConditions\":[{\"orderByAttribute\":\"Name\",\"ascending\":false,\"nullsFirst\":false}],\"limit\":5}}",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE"
    }
```

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionVersionId` | String | Unique identifier of the specific context definition version to which this filter belongs. | Required | 65.0 |
| `description` | String | Details of the context definition filter such as the purpose of the filter. Use this field to document the filter's business logic, intended use case, or any important implementation details for future reference. | Optional | 65.0 |
| `filterApiName` | String | Unique API name identifier for the context definition filter. | Required | 65.0 |
| `filterName` | String | Display name for the context definition filter. | Required | 65.0 |
| `filtersPerNode` | String | A JSON string representation of the filter condition logic that defines the filter criteria. This field contains the structured query conditions that's evaluated to determine which records match the filter. The JSON structure typically includes field names, operators, and values that form the filter expression. | Required | 65.0 |
| `inheritedFrom` | String | Source context definition if filter is inherited in the GET request. This field is not applicable for POST request. | Optional | 65.0 |

=== ARTICLE: connect_requests_context_definition_filter_list_input.htm ===
---
page_id: connect_requests_context_definition_filter_list_input.htm
title: Context Definition Filter List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_definition_filter_list_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filter List Input

Input representation for a list of Context Definition Filters

**JSON example**

: 

```
{
  "filters": [
    {
      "filterApiName": "FilterAccount",
      "filterName":"FilterAccount",
      "filtersPerNode": "{\"Account\":{\"filterCondition\":{\"attribute\":\"City\",\"operator\":\"EQUALS\",\"operands\":[{\"value\":\"Bengaluru\",\"type\":\"STRING\"}],\"composite\":false},\"orderByConditions\":[{\"orderByAttribute\":\"Name\",\"ascending\":false,\"nullsFirst\":false}],\"limit\":5}}",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `filters` | [Context Definition Filter Input](./connect_requests_context_definition_filter_input.htm.md)[] | List of context definition filter inputs. | Required | 65.0 |

=== ARTICLE: connect_requests_context_definition_upgrade.htm ===
---
page_id: connect_requests_context_definition_upgrade.htm
title: Context Definition Upgrade Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_definition_upgrade.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Upgrade Input

Input representation of context definition upgrade.

        
            
                
                    

**JSON example**

                    
: 
                        

```
{
  "contextDefinitions": [
    {
      "contextDefinitionId": "11Oxx0000006PfZEAU",
      "upgradeMode": "Sync"
    }
  ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        
- 
- 
- 

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionId` | String | ID of this context definition to be upgraded. | Required | 64.0 |
| `upgradeMode` | String | The upgrade mode enum. Possible values are: Sync Preview OverrideThe default value is Sync. | Optional | 64.0 |

=== ARTICLE: connect_requests_context_definitions_input.htm ===
---
page_id: connect_requests_context_definitions_input.htm
title: Context Definition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_definitions_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Input 

Input representation of the context definition.

**JSON example**

: 

```
{
   "name":"Example Definition",
   "description":"Example Description",
   "developerName":"John Doe",
   "startDate":"2023-06-02T00:00:00.000Z",
   "endDate":"2025-06-20T00:00:00.000Z",
   "isActive":false,
   "payload":"{\"contextDefinition\":{\"name\":\"ExampleDefinition\",\"description\":\"Example Description\",\"developerName\":\"ExampleDefinition\",\"contextDefinitionVersionList\":[{\"contextDefinitionVersion\":{\"isActive\":\"TRUE\",\"startDate\":\"2023-06-02T00:00:00.000Z\",\"endDate\":\"2025-06-20T00:00:00.000Z\",\"contextNodes\":[{\"name\":\"Claim\",\"isTransposable\":\"TRUE\",\"contextNodeId\":\"$param_claimId\",\"attributes\":[{\"dataType\":\"STRING\",\"type\":\"INPUT\",\"isFinal\":\"TRUE\",\"isKey\":\"false\",\"isValue\":\"true\",\"contextAttributeId\":\"$param_claimaccountId\",\"name\":\"Account\",\"contextTagList\":[{\"name\":\"ClaimAccount\"}]}],\"nodeChildren\":[{\"name\":\"ClaimItem\",\"isTransposable\":\"TRUE\",\"contextNodeId\":\"$param_claimItemId\",\"attributes\":[{\"dataType\":\"STRING\",\"type\":\"INPUT\",\"isFinal\":\"TRUE\",\"isKey\":\"FALSE\",\"isValue\":\"FALSE\",\"contextAttributeId\":\"$param_assetId\",\"name\":\"Asset\",\"contextTagList\":[{\"name\":\"ClaimItemAsset\"}]}],\"contextTagList\":[{\"contextNodeId\":\"$param_claimItemId\",\"name\":\"ClaimItem\"}]}],\"contextTagList\":[{\"contextNodeId\":\"$param_claimId\",\"name\":\"Claim\"}]}],\"contextMapping\":[{\"name\":\"Claim Order Mapping\",\"isDefault\":\"TRUE\",\"contextNodeMappings\":[{\"contextNodeId\":\"$param_claimId\",\"sObjectName\":\"Claim\",\"contextAttributeMappings\":[{\"contextAttributeId\":\"$param_claimaccountId\",\"hydrationSource\":\"SObject\",\"contextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Claim\",\"queryAttribute\":\"Account\",\"parentContextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Account\",\"queryAttribute\":\"Name\"}]}]}]},{\"contextNodeId\":\"$param_claimItemId\",\"sObjectName\":\"ClaimItem\",\"contextAttributeMappings\":[{\"contextAttributeId\":\"$param_assetId\",\"hydrationSource\":\"SObject\",\"contextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"ClaimItem\",\"queryAttribute\":\"Asset\",\"parentContextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Asset\",\"queryAttribute\":\"Name\"}]}]}]}]}]}}]}}",
   "sourceDefinitionId":"11Oxx0000007MnhEAE",
   "contextTtl":30
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextTtl` | Integer | Time to live (TTL) of context. | Optional | 59.0 |
| `description` | String | Short description of context definition. | Optional | 59.0 |
| `developerName` | String | Developer name. | Required | 59.0 |
| `endDate` | String | End date till context definition is valid. | Optional | 59.0 |
| `isActive` | Boolean | Specifies whether context is active (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the context definition. | Required | 59.0 |
| `payload` | String | JSON payload containing all the definitions and mappings. | Optional | 59.0 |
| `sourceDefinitionId` | String | Source context definition ID. | Optional | 59.0 |
| `startDate` | String | Start date from when context definition is valid. | Required | 59.0 |

=== ARTICLE: connect_requests_context_input.htm ===
---
page_id: connect_requests_context_input.htm
title: Context Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Input

Input representation for defining a context.

**JSON example**

: 

```
{
  "metadata": {
    "contextDefinitionId": "11Oxx0000006VjNEAU",
    "mappingId": "11jxx0000004Q83AAE"
  },
  "data": "{\"Order\":[{\"id\":\"TestOrder123\",\"businessObjectType\":\"Order\",\"Name\":\"Test Order\",\"Status\":\"SHIPPED\",\"AccountName\":\"Kroger\",\"OrderItems\":[{\"id\":\"TestOrderItem1\",\"businessObjectType\":\"OrderItem\",\"ProductName\":\"Coke\"},{\"id\":\"TestOrderItem2\",\"businessObjectType\":\"OrderItem\",\"ProductName\":\"Pepsi\"}]}]}"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | Payload containing context-specific information. | Required | 59.0 |
| `metadata` | [Context MetaData Input](./connect_requests_context_meta_data_input.htm.md) | Metadata information about context. | Required | 59.0 |

=== ARTICLE: connect_requests_context_mappings_input.htm ===
---
page_id: connect_requests_context_mappings_input.htm
title: Context Mappings Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_mappings_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mappings Input

Input representation of context mapping.

                    

**JSON example**

                    
: 
                        

```
{
  "contextMappings": [
    {
      "name": "ExampleMapping",
      "description": "Example Mapping Description",
      "isDefault": true,
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ]
    }
  ],
  "generateInputMappings": false,
  "generateSObjectMappings": false
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
| `contextMappingId` | String | ID of this context mapping. Required for update. | Required | 59.0 |
| `contextNodeMappings` | Context Node Mappings Input[] | List of context node mappings. | Optional | 59.0 |
| `description` | String | Description of context mapping. | Optional | 59.0 |
| `isDefault` | Boolean | Indicates whether to make a default mapping for the context definition (`true`) or not (`false`). | Optional | 59.0 |
| `intents` | List<String> | Purpose that's used to identify the type of required context mapping.Valid values are: `HYDRATION`—To load cache from a data source. `PERSISTENCE`—To load the sink objects from cache. Sink objects are the final destinations for the processed data. `ASSOCIATION`—To create a mapping without validating database relationships, attaching context structure nodes and their attributes with data source nodes and their attributes. `TRANSLATION`—To transform the data loaded in the cache to another representation defined by the mapping. | Optional | 61.0 |
| `name` | String | Name of the context mapping. | Required | 59.0 |

=== ARTICLE: connect_requests_context_meta_data_input.htm ===
---
page_id: connect_requests_context_meta_data_input.htm
title: Context Metadata Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_meta_data_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Metadata Input

Input representation of context metadata.

**JSON example**

: 

```
{
  "metadata": {
    "contextDefinitionId": "11Oxx0000006VjNEAU",
    "mappingId": "11jxx0000004Q83AAE"
  }
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionId` | String | The ID of the context definition to use for validating and creating the context record. | Required | 59.0 |
| `mappingId` | String | The ID of the context mapping to use for resolving the provided context data attributes. | Required | 59.0 |
| `taggedData` | Boolean | Parameter to return tagged attribute names instead of raw names in the created context record. | Optional | 59.0 |

=== ARTICLE: connect_requests_context_node_id_input.htm ===
---
page_id: connect_requests_context_node_id_input.htm
title: Context Node ID Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_node_id_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node ID Input

Input representation of the list of context node IDs to create the relationship nodes
    for.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "contextNodeIds": [
    "11oxx000001G3dtAAC",
    "11oxx000001G3duAAC"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextNodeIds` | String | List of context node IDs to create the relationship nodes by adding them as child nodes to the context node that’s specified in the endpoint. | Required | 61.0 |

=== ARTICLE: connect_requests_context_nodes_input.htm ===
---
page_id: connect_requests_context_nodes_input.htm
title: Context Nodes Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_nodes_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Nodes Input 

Input representation of context node.

**JSON example**

: 

```
{
    "contextNodes": [
        {
            "name": "Node_0",
            "attributes": {
                "contextAttributes": [
                    {
                        "dataType": "STRING",
                        "fieldType": "INPUT",
                        "name": "Attribute_1"
                    }
                ]
            },
            "childNodes": {
                "contextNodes": [
                    {
                        "name": "Node_1",
                        "attributes": {
                            "contextAttributes": [
                                {
                                    "dataType": "NUMBER",
                                    "fieldType": "INPUT",
                                    "name": "Attribute_2"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Context Attributes Input](./connect_requests_context_attributes_input.htm.md)[] | List of context attributes. | Optional | 59.0 |
| `childNodes` | [Context Nodes Input](#)[] | List of child context nodes. | Optional | 59.0 |
| `contextNodeId` | String | ID of the context node. | Required | 59.0 |
| `isTransposable` | Boolean | Specifies if the context node is used for the transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the context node. | Required | 59.0 |
| `parentNodeId` | String | ID of (parent) context node. | Optional | 59.0 |
| `tags` | [Context Tag Input](./connect_requests_context_tag_input.htm.md)[] | List of context tags. | Optional | 59.0 |

=== ARTICLE: connect_requests_context_tag_input.htm ===
---
page_id: connect_requests_context_tag_input.htm
title: Context Tag Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_tag_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag Input 

Input representation of the context tag.

        
          

**JSON example**

          
: 
            

```
{
    "contextTags": [
        {
            "name": "Attribute_Tag",
            "contextAttributeId": "11nxx000001hOozAAE"
        },
        {
            "name": "Node_Tag",
            "contextNodeId": "11oxx000001G9D2AAK"
        }
    ]
}
```

          

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the (parent) context attribute. | Required | 59.0 |
| `contextNodeId` | String | ID of the (parent) context node. | Required | 59.0 |
| `contextTagId` | String | ID of this Context tag. Required only for update. | Optional | 59.0 |
| `name` | String | Name of the context tag. | Required | 59.0 |

=== ARTICLE: connect_requests_node_path_and_tag_values.htm ===
---
page_id: connect_requests_node_path_and_tag_values.htm
title: Node Path and Tag Values Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_node_path_and_tag_values.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Node Path and Tag Values Input

Input representation of the node path which needs to update with tag
        details.

        
            
                
                    

**JSON example**

                    
: 
                        

```
{
            "nodePath": {
                "dataPath": [
                    "001xx000003GbQSAA0"
                ]
            },
            "tagValues": [
                {
                    "tagName": "Name",
                    "tagValue": "updatedAccount"
                },
                {
                    "tagName": "City",
                    "tagValue": "Bangalore"
                }
            ]
        }
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `nodePath` | String | Path of Context Data Record. | Required | 63.0 |
| `tagValues` | [List<Context​TagValueInput​Representation](./connect_requests_tag_values_input.htm.md) | List of Tag Names to be updated and their values. | Required | 63.0 |

=== ARTICLE: connect_requests_query_context_record_input.htm ===
---
page_id: connect_requests_query_context_record_input.htm
title: Query Context Record Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_query_context_record_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Record Input

Input representation of query context record.

**JSON example**

: 

```
{
  "contextId": "7bc695bc-f38b-4a94-8a95-0caa50f3da53"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | String[] | List of attributes to be retrieved. | Optional | 58.0 |
| `businessObjectTypeFilter` | String | Filter based on a business object type. | Optional | 58.0 |
| `contextId` | String | The ID of the context to be queried. | Required | 58.0 |
| `queryPath` | String[] | Path to the parent node. | Optional | 58.0 |

=== ARTICLE: connect_requests_query_data_input.htm ===
---
page_id: connect_requests_query_data_input.htm
title: Query Record Status Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_query_data_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Record Status Input

Input representation of status and related error messages of query data
    records.

    
      
        
          

**JSON example**

          
: 
            

```
{
    "queryRecordStatusInput": {
        "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
        "queryPaths": [
            {
                "dataPath": [
                    "TestOrder123"
                ]
            }
        ]
    }
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `queryRecordStatusInput` | Object | Input representation for context ID and the list of paths for querying the status. | Required | 59.0 |

=== ARTICLE: connect_requests_tag_values_input.htm ===
---
page_id: connect_requests_tag_values_input.htm
title: Tag Values Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_tag_values_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tag Values Input

Input representation of the list of Tag Names to be updated and their
        values.

        
            
                
                    

**JSON example**

                    
: 
                        

```

                {
                    "tagName": "Name",
                    "tagValue": "updatedAccount"
                },
                {
                    "tagName": "City",
                    "tagValue": "Bangalore"
                }
         
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `tagName` | String | Name of tag thats need to be updated. | Required | 63.0 |
| `tagValue` | String | Updated value of tags. | Required | 63.0 |

=== ARTICLE: connect_resources_attribute_mapping.htm ===
---
page_id: connect_resources_attribute_mapping.htm
title: Context Attribute Mapping (POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_attribute_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_attribute_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Mapping (POST, PATCH)

Create context attribute mapping. Update context attribute mapping.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-node-mappings/${contextNodeMappingId}/context-attribute-mappings
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-node-mappings/${contextNodeMappingId}/context-attribute-mappings
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-node-mappings/${contextNodeMappingId}/context-attribute-mappings
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST, PATCH

        
        
          

**Request body for POST**

          
: 
            
        
                    

**JSON example**

                    
: 
                        

```
{
    "contextAttributeMappings": [
        {
            "contextAttributeId": "11nxx000001hIgLAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Status"
                    }
                ]
            }
        },
        {
            "contextAttributeId": "11nxx000001hKiFAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Name"
                    }
                ]
            }
        }
    ]
}
```

                    

                    
: This example shows a JSON sample when context-to-context mappings
                        exist.

                    
: 
                        

```
{
  "contextMappings": [
    {
      "contextMappingId": "11jxx0000005UXnAAM",
      "contextNodeMappings": {
        "contextNodeMappings": [
          {
            "attributeMappings": {
              "contextAttributeMappings": [
                {
                  "hydrationDetails": {
                    "contextAttrContextHydrationDetails": [
                      {
                        "queryAttribute": "11nxx000001hGTFAA2",
                        "parentAttributeMappingId": "11Rxx00000058LcEAI"
                      }
                    ]
                  },
                  "contextAttributeId": "11nxx000001ihzFAAQ",
                  "contextInputAttributeName": "Node1A1"
                }
              ]
            },
            "contextNodeId": "11oxx000001HS0iAAG",
            "mappedContextNodeId": "11oxx000001G0mSAAS",
            "sObjectName": "Node1"
          }
        ]
      },
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ],
      "mappedContextDefinitionName": "11Oxx0000006PZ8EAM",
      "isDefault": false
    }
  ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the context attribute record. | Required | 59.0 |
| `contextAttributeMappingId` | String | ID of the context attribute mapping record. | Required | 59.0 |
| `contextInputAttributeName` | String | Context input attribute name. | Optional | 59.0 |
| `hydrationDetails` | [Context Attribute Hydration Details Input](./connect_requests_context_attr_hydration_details_input.htm.md)[] | List of context attribute hydration detail. | Optional | 59.0 |

                    

                
      

          

        
        
          

**Response body for POST**

          
: [Context Attribute Mapping List Output](./connect_responses_context_attribute_mapping_list.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
        
                    

**JSON example**

                    
: 
                        

```
{
    "contextAttributeMappings": [
        {
            "contextAttributeId": "11nxx000001hIgLAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Status"
                    }
                ]
            }
        },
        {
            "contextAttributeId": "11nxx000001hKiFAAU",
            "hydrationDetails": {
                "contextAttrHydrationDetails": [
                    {
                        "sObjectDomain": "Order",
                        "queryAttribute": "Name"
                    }
                ]
            }
        }
    ]
}
```

                    

                    
: This example shows a JSON sample when context-to-context mappings
                        exist.

                    
: 
                        

```
{
  "contextMappings": [
    {
      "contextMappingId": "11jxx0000005UXnAAM",
      "contextNodeMappings": {
        "contextNodeMappings": [
          {
            "attributeMappings": {
              "contextAttributeMappings": [
                {
                  "hydrationDetails": {
                    "contextAttrContextHydrationDetails": [
                      {
                        "queryAttribute": "11nxx000001hGTFAA2",
                        "parentAttributeMappingId": "11Rxx00000058LcEAI"
                      }
                    ]
                  },
                  "contextAttributeId": "11nxx000001ihzFAAQ",
                  "contextInputAttributeName": "Node1A1"
                }
              ]
            },
            "contextNodeId": "11oxx000001HS0iAAG",
            "mappedContextNodeId": "11oxx000001G0mSAAS",
            "sObjectName": "Node1"
          }
        ]
      },
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ],
      "mappedContextDefinitionName": "11Oxx0000006PZ8EAM",
      "isDefault": false
    }
  ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the context attribute record. | Required | 59.0 |
| `contextAttributeMappingId` | String | ID of the context attribute mapping record. | Required | 59.0 |
| `contextInputAttributeName` | String | Context input attribute name. | Optional | 59.0 |
| `hydrationDetails` | [Context Attribute Hydration Details Input](./connect_requests_context_attr_hydration_details_input.htm.md)[] | List of context attribute hydration detail. | Optional | 59.0 |

                    

                
      

          

        
        
          

**Response body for PATCH**

          
: [Context Attribute Mapping List](./connect_responses_context_attribute_mapping_list.htm.md)

=== ARTICLE: connect_resources_configure_relationship_node.htm ===
---
page_id: connect_resources_configure_relationship_node.htm
title: Context Node Relationship (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_configure_relationship_node.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_node_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Relationship (POST)

Configure a relationship node by adding child context nodes to a specific context
    node.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-nodes/contextNodeId/configurerelationship
```

          

          
: The contextNodeId specifies the ID of the context node to which you
            want to add the context nodes from the request body as child nodes.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-nodes/11oxx000001G3dtAAC/configurerelationship
```

          

        
        
          

**Available version**

          
: 61.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "contextNodeIds": [
    "11oxx000001G3dtAAC",
    "11oxx000001G3duAAC"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextNodeIds` | String | List of context node IDs to create the relationship nodes by adding them as child nodes to the context node that’s specified in the endpoint. | Required | 61.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Context Node List](./connect_responses_context_node_list.htm.md)

=== ARTICLE: connect_resources_context_attribute.htm ===
---
page_id: connect_resources_context_attribute.htm
title: Context Attribute (POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_attribute.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_attribute_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute (POST, PATCH)

Create a list of context attributes.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-nodes/${contextNodeId}/context-attributes
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-nodes/${contextNodeId}/context-attributes
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-nodes/${contextNodeId}/context-attributes
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST, PATCH

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
    "contextAttributes": [
        {
            "dataType": "STRING",
            "fieldType": "INPUT",
            "name": "Attribute_5",
            "tags": {
                "contextTags": [
                    {
                        "name": "Attribute_5_Tag"
                    }
                ]
            }
        },
        {
            "dataType": "NUMBER",
            "fieldType": "OUTPUT",
            "name": "Attribute_6"
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the attribute. | Required | 59.0 |
| `dataType` | String | Data type of the attribute. | Required | 59.0 |
| `domainSet` | String | Comma separated node names referenced by this attribute. | Optional | 59.0 |
| `fieldType` | String | Field type of the attribute. | Required | 59.0 |
| `isKey` | Boolean | Specifies if it used for transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `isValue` | Boolean | Specifies if it used for transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the attribute. | Required | 59.0 |
| `tags` | [Context Tag Input](./connect_requests_context_tag_input.htm.md)[] | List of tags for the attribute. | Optional | 59.0 |

          

        
        
          

**Response body for POST**

          
: 
[Context Attribute List](./connect_responses_context_attribute_list.htm.md)
          

        
        
          

**Request body for PATCH**

          
: 

              
                

**JSON example**

                
: 
                  

```
{
    "contextAttributes": [
        {
            "name": "Attribute_5_Updated",
            "contextAttributeId": "11nxx000001hOvRAAU"
        },
        {
            "name": "Attribute_6_Updated",
            "contextAttributeId": "11nxx000001hOvSAAU"
        }
    ]
}
```

                

              
            

        
        
          

**Response body for PATCH**

          
: 
[Context Attribute List](./connect_responses_context_attribute_list.htm.md)

=== ARTICLE: connect_resources_context_attribute_id.htm ===
---
page_id: connect_resources_context_attribute_id.htm
title: Context Attribute ID (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_attribute_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_attribute_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute ID (GET, DELETE)

Query and delete a context attribute using an ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-nodes/${contextNodeId}/context-attributes/${contextAttributeId}
```

          

        
        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-nodes/${contextNodeId}/context-attributes/${contextAttributeId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-nodes/${contextNodeId}/context-attributes/${contextAttributeId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Attribute Output](./connect_responses_context_attribute.htm.md)

=== ARTICLE: connect_resources_context_attribute_mapping_id.htm ===
---
page_id: connect_resources_context_attribute_mapping_id.htm
title: Context Attribute Mapping ID (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_attribute_mapping_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Mapping ID (GET, DELETE)

Query and delete a context attribute mapping using an ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-node-mappings/${contextNodeMappingId}/context-attribute-mappings/${contextAttributeMappingId}
```

          

        
        
          

**Example for GET **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-node-mappings/${contextNodeMappingId}/context-attribute-mappings/${contextAttributeMappingId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-node-mappings/${{contextNodeMappingId}/context-attribute-mappings/${contextAttributeMappingId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Attribute Mapping Output](./connect_responses_context_attribute_mapping.htm.md)

=== ARTICLE: connect_resources_context_definition.htm ===
---
page_id: connect_resources_context_definition.htm
title: Context Definition (GET, POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_context_definition_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition (GET, POST)

Create a context definition, clone an existing context definition, extend a standard
    definition (file based definition) or to persist entire context definition.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions
```

          

        
        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions
```

          

        
        
          

**Example for POST **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, POST

        
        
          

**Response body for GET**

          
: [Context Definition List](./connect_responses_context_definition_list.htm.md)

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
   "name":"Example Definition",
   "description":"Example Description",
   "developerName":"John Doe",
   "startDate":"2023-06-02T00:00:00.000Z",
   "endDate":"2025-06-20T00:00:00.000Z",
   "isActive":false,
   "payload":"{\"contextDefinition\":{\"name\":\"ExampleDefinition\",\"description\":\"Example Description\",\"developerName\":\"ExampleDefinition\",\"contextDefinitionVersionList\":[{\"contextDefinitionVersion\":{\"isActive\":\"TRUE\",\"startDate\":\"2023-06-02T00:00:00.000Z\",\"endDate\":\"2025-06-20T00:00:00.000Z\",\"contextNodes\":[{\"name\":\"Claim\",\"isTransposable\":\"TRUE\",\"contextNodeId\":\"$param_claimId\",\"attributes\":[{\"dataType\":\"STRING\",\"type\":\"INPUT\",\"isFinal\":\"TRUE\",\"isKey\":\"false\",\"isValue\":\"true\",\"contextAttributeId\":\"$param_claimaccountId\",\"name\":\"Account\",\"contextTagList\":[{\"name\":\"ClaimAccount\"}]}],\"nodeChildren\":[{\"name\":\"ClaimItem\",\"isTransposable\":\"TRUE\",\"contextNodeId\":\"$param_claimItemId\",\"attributes\":[{\"dataType\":\"STRING\",\"type\":\"INPUT\",\"isFinal\":\"TRUE\",\"isKey\":\"FALSE\",\"isValue\":\"FALSE\",\"contextAttributeId\":\"$param_assetId\",\"name\":\"Asset\",\"contextTagList\":[{\"name\":\"ClaimItemAsset\"}]}],\"contextTagList\":[{\"contextNodeId\":\"$param_claimItemId\",\"name\":\"ClaimItem\"}]}],\"contextTagList\":[{\"contextNodeId\":\"$param_claimId\",\"name\":\"Claim\"}]}],\"contextMapping\":[{\"name\":\"Claim Order Mapping\",\"isDefault\":\"TRUE\",\"contextNodeMappings\":[{\"contextNodeId\":\"$param_claimId\",\"sObjectName\":\"Claim\",\"contextAttributeMappings\":[{\"contextAttributeId\":\"$param_claimaccountId\",\"hydrationSource\":\"SObject\",\"contextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Claim\",\"queryAttribute\":\"Account\",\"parentContextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Account\",\"queryAttribute\":\"Name\"}]}]}]},{\"contextNodeId\":\"$param_claimItemId\",\"sObjectName\":\"ClaimItem\",\"contextAttributeMappings\":[{\"contextAttributeId\":\"$param_assetId\",\"hydrationSource\":\"SObject\",\"contextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"ClaimItem\",\"queryAttribute\":\"Asset\",\"parentContextSObjectHydrationInfoList\":[{\"sObjectDomain\":\"Asset\",\"queryAttribute\":\"Name\"}]}]}]}]}]}}]}}",
   "sourceDefinitionId":"11Oxx0000007MnhEAE",
   "contextTtl":30
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextTtl` | Integer | Time to live (TTL) of context. | Optional | 59.0 |
| `description` | String | Short description of context definition. | Optional | 59.0 |
| `developerName` | String | Developer name. | Required | 59.0 |
| `endDate` | String | End date till context definition is valid. | Optional | 59.0 |
| `isActive` | Boolean | Specifies whether context is active (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the context definition. | Required | 59.0 |
| `payload` | String | JSON payload containing all the definitions and mappings. | Optional | 59.0 |
| `sourceDefinitionId` | String | Source context definition ID. | Optional | 59.0 |
| `startDate` | String | Start date from when context definition is valid. | Required | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Context Definition Information](./connect_responses_context_definition_info.htm.md)

=== ARTICLE: connect_resources_context_definition_filter_by_id.htm ===
---
page_id: connect_resources_context_definition_filter_by_id.htm
title: Context Definition Filter By ID (DELETE, GET, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition_filter_by_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_context_definition_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filter By ID (DELETE, GET, PATCH)

Get, update, or delete a context definition filter for a specified context definition
    filter ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-filters/${contextDefinitionFilterId}
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-definitions/SimpleDef/context-filters/1Tlxx0000004DUuCAM
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: DELETE, GET, PATCH

        
        
          

**Response body for GET**

          
: [Context Definition Filter](./connect_responses_context_definition_filter.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
        
          
: 
This example shows a sample request to
            create, get, or update a context definition filter.
            

```
{
      "description": "Updated",
      "filterApiName": "FilterAccount",
      "filterName":"FilterAccount",
      "filtersPerNode": "{\"Account\":{\"filterCondition\":{\"attribute\":\"City\",\"operator\":\"EQUALS\",\"operands\":[{\"value\":\"Bengaluru\",\"type\":\"STRING\"}],\"composite\":false},\"orderByConditions\":[{\"orderByAttribute\":\"Name\",\"ascending\":false,\"nullsFirst\":false}],\"limit\":5}}",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE"
    }
```

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionVersionId` | String | Unique identifier of the specific context definition version to which this filter belongs. | Required | 65.0 |
| `description` | String | Details of the context definition filter such as the purpose of the filter. Use this field to document the filter's business logic, intended use case, or any important implementation details for future reference. | Optional | 65.0 |
| `filterApiName` | String | Unique API name identifier for the context definition filter. | Required | 65.0 |
| `filterName` | String | Display name for the context definition filter. | Required | 65.0 |
| `filtersPerNode` | String | A JSON string representation of the filter condition logic that defines the filter criteria. This field contains the structured query conditions that's evaluated to determine which records match the filter. The JSON structure typically includes field names, operators, and values that form the filter expression. | Required | 65.0 |
| `inheritedFrom` | String | Source context definition if filter is inherited in the GET request. This field is not applicable for POST request. | Optional | 65.0 |

          

        
        
          

**Response body for PATCH**

          
: [Context Definition Filter](./connect_responses_context_definition_filter.htm.md)

=== ARTICLE: connect_resources_context_definition_filters.htm ===
---
page_id: connect_resources_context_definition_filters.htm
title: Context Definition Filters (GET, POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition_filters.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_context_definition_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filters (GET, POST)

Create or get context filters associated with a specific context definition. Context
    filters are criteria or conditions that refine or limit data operations based on specific
    parameters.

    
      
        
          

**Resource**

          
: 

```
/connect/context-definitions/${contextDefinitionId}/context-filters
```

The
              `contextDefinitionId` property value is the unique
            identifier for the context definition whose filters you want to retrieve.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-definitions/SimpleDef/context-filters
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: GET, POST

        
        
          

**Response body for GET**

          
: [Context Definition Filter List](./connect_responses_context_definition_filter_list.htm.md)

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "filters": [
    {
      "filterApiName": "FilterAccount",
      "filterName":"FilterAccount",
      "filtersPerNode": "{\"Account\":{\"filterCondition\":{\"attribute\":\"City\",\"operator\":\"EQUALS\",\"operands\":[{\"value\":\"Bengaluru\",\"type\":\"STRING\"}],\"composite\":false},\"orderByConditions\":[{\"orderByAttribute\":\"Name\",\"ascending\":false,\"nullsFirst\":false}],\"limit\":5}}",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `filters` | [Context Definition Filter Input](./connect_requests_context_definition_filter_input.htm.md)[] | List of context definition filter inputs. | Required | 65.0 |

          

        
        
          

**Response body for POST**

          
: [Context Definition Filter List](./connect_responses_context_definition_filter_list.htm.md)

=== ARTICLE: connect_resources_context_definition_id.htm ===
---
page_id: connect_resources_context_definition_id.htm
title: Context Definition Id (GET, PATCH, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_context_definition_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Id (GET, PATCH, DELETE)

Query, update, and delete a context definition using an ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}
```

          

        
        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}
```

          

        
        
          

**Example for PATCH **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, PATCH, DELETE

        
        
          

**Response body for GET**

          
: [Context Definition Output](./connect_responses_context_definition.htm.md)

        
        
          

**Request body for PATCH**

          
: 

              
                

**JSON example**

                
: 
                  

```
{
"definition": "Example Defintion patch",
"description": "Example Description patch"
}
```

                

              
            

        
        
          

**Response body for PATCH**

          
: [Context Definition Information](./connect_responses_context_definition_info.htm.md)

=== ARTICLE: connect_resources_context_definition_upgrades.htm ===
---
page_id: connect_resources_context_definition_upgrades.htm
title: Context Definition Upgrade (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition_upgrades.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_context_definition_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Upgrade (PATCH)

Upgrade a context definition. Once an extended definition is created from a base
        standard definition, use this API to reflect any updates made to the base standard
        definition in the extended definition.

        
            
                
                    

**Resource**

                    
: 
                        

```
/connect/context-definitions/upgrades
```

                    

                
                
                    

**Example for PATCH **

                    
: 
                        

```
https://yourInstance.salesforce.com/services/data/v64.0/connect/context-definitions/upgrades
```

                    

                
                
                    

**Available version**

                    
: 64.0

                
                
                    

**HTTP methods**

                    
: PATCH

                
                
                    

**Request body for PATCH**

                    
: 
                        
                
                    

**JSON example**

                    
: 
                        

```
{
  "contextDefinitions": [
    {
      "contextDefinitionId": "11Oxx0000006PfZEAU",
      "upgradeMode": "Sync"
    }
  ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        
- 
- 
- 

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionId` | String | ID of this context definition to be upgraded. | Required | 64.0 |
| `upgradeMode` | String | The upgrade mode enum. Possible values are: Sync Preview OverrideThe default value is Sync. | Optional | 64.0 |

                    

                
            

                    

                
                
                    

**Response body for PATCH**

                    
: [Context Definition Information](./connect_responses_context_definition_info.htm.md)

=== ARTICLE: connect_resources_context_mapping.htm ===
---
page_id: connect_resources_context_mapping.htm
title: Context Mapping (POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mapping (POST, PATCH)

Create and update context mappings.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-mappings
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-mappings
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-mappings
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST, PATCH

        
        
          

**Request body for POST**

          
: 
            
                    

**JSON example**

                    
: 
                        

```
{
  "contextMappings": [
    {
      "name": "ExampleMapping",
      "description": "Example Mapping Description",
      "isDefault": true,
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ]
    }
  ],
  "generateInputMappings": false,
  "generateSObjectMappings": false
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
| `contextMappingId` | String | ID of this context mapping. Required for update. | Required | 59.0 |
| `contextNodeMappings` | Context Node Mappings Input[] | List of context node mappings. | Optional | 59.0 |
| `description` | String | Description of context mapping. | Optional | 59.0 |
| `isDefault` | Boolean | Indicates whether to make a default mapping for the context definition (`true`) or not (`false`). | Optional | 59.0 |
| `intents` | List<String> | Purpose that's used to identify the type of required context mapping.Valid values are: `HYDRATION`—To load cache from a data source. `PERSISTENCE`—To load the sink objects from cache. Sink objects are the final destinations for the processed data. `ASSOCIATION`—To create a mapping without validating database relationships, attaching context structure nodes and their attributes with data source nodes and their attributes. `TRANSLATION`—To transform the data loaded in the cache to another representation defined by the mapping. | Optional | 61.0 |
| `name` | String | Name of the context mapping. | Required | 59.0 |

                    

                

          

        
        
          

**Response body for POST**

          
: [Context Mapping List Output](./connect_responses_context_mapping_list.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
    "contextMappings": [
      {
        "contextMappingId": "11jxx0000005UXnAAM",
        "contextNodeMappings": {
          "contextNodeMappings": [
            {
              "attributeMappings": {
                "contextAttributeMappings": [
                  {
                    "hydrationDetails": {
                      "contextAttrHydrationDetails": []
                    },
                    "contextAttributeId": "11nxx000001ihzFAAQ",
                    "contextInputAttributeName": "Node1A1"
                  }
                ]
              },
              "contextNodeId": "11oxx000001HS0iAAG",
              "sObjectName": "Node1"
            }
          ]
        }
      }
    ]
  }
```

                

              
            

          

        
        
          

**Response body for PATCH**

          
: [Context Mapping List Output](./connect_responses_context_mapping_list.htm.md)

=== ARTICLE: connect_resources_context_mapping_id.htm ===
---
page_id: connect_resources_context_mapping_id.htm
title: Context Mapping Id (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_mapping_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mapping Id (GET, DELETE)

Query and delete a context mapping using an Id.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-mappings/${contextMappingId}
```

          

        
        
          

**Example for GET **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-mappings/${contextMappingId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-mappings/${contextMappingId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Mapping Output](./connect_responses_context_mapping.htm.md)

=== ARTICLE: connect_resources_context_node.htm ===
---
page_id: connect_resources_context_node.htm
title: Context Node (POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_node.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_node_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node (POST, PATCH)

Create and update context node.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-nodes
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-nodes
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-nodes
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST, PATCH

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
    "contextNodes": [
        {
            "name": "Node_0",
            "attributes": {
                "contextAttributes": [
                    {
                        "dataType": "STRING",
                        "fieldType": "INPUT",
                        "name": "Attribute_1"
                    }
                ]
            },
            "childNodes": {
                "contextNodes": [
                    {
                        "name": "Node_1",
                        "attributes": {
                            "contextAttributes": [
                                {
                                    "dataType": "NUMBER",
                                    "fieldType": "INPUT",
                                    "name": "Attribute_2"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Context Attributes Input](./connect_requests_context_attributes_input.htm.md)[] | List of context attributes. | Optional | 59.0 |
| `childNodes` | [Context Nodes Input](./connect_requests_context_nodes_input.htm.md)[] | List of child context nodes. | Optional | 59.0 |
| `contextNodeId` | String | ID of the context node. | Required | 59.0 |
| `isTransposable` | Boolean | Specifies if the context node is used for the transposable feature (`true`) or not (`false`). | Optional | 59.0 |
| `name` | String | Name of the context node. | Required | 59.0 |
| `parentNodeId` | String | ID of (parent) context node. | Optional | 59.0 |
| `tags` | [Context Tag Input](./connect_requests_context_tag_input.htm.md)[] | List of context tags. | Optional | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Context Node List Output](./connect_responses_context_node_list.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
    "contextNodes": [
        {
            "name": "Node_0_patch",
            "contextNodeId": "11oxx000001G9D2AAK"
        }
    ]
}
```

                

              
            

          

        
        
          

**Response body for PATCH**

          
: [Context Node List Output](./connect_responses_context_node_list.htm.md)

=== ARTICLE: connect_resources_context_node_id.htm ===
---
page_id: connect_resources_context_node_id.htm
title: Context Node Id (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_node_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_node_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Id (GET, DELETE)

Query and delete a context node using an Id.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-nodes/${contextNodeId}
```

          

        
        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-nodes/${contextNodeId}
```

          

        
        
          

**Example for POST **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-nodes/${contextNodeId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Node
            Output](./connect_responses_context_node.htm.md)

=== ARTICLE: connect_resources_context_node_mapping_id.htm ===
---
page_id: connect_resources_context_node_mapping_id.htm
title: Context Node Mapping Id (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_node_mapping_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_node_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Mapping Id (GET, DELETE)

Query and delete a context node mapping using an ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-mappings/${contextMappingId}/context-node-mappings/${contextNodeMappingId}
```

          

        
        
          

**Example for GET **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-mappings/${contextMappingId}/context-node-mappings/${contextNodeMappingId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-mappings/${contextMappingId}/context-node-mappings/${contextNodeMappingId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Node Mapping Output](./connect_responses_context_node_mapping.htm.md)

=== ARTICLE: connect_resources_context_query_lean_tag.htm ===
---
page_id: connect_resources_context_query_lean_tag.htm
title: Context Query Tags Leaner (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_query_lean_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Query Tags Leaner (POST)

Query tags and return a memory-optimized (leaner) result suitable for Apex and low-heap
    clients. Eliminate redundant metadata to reduce heap usage and payload size.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/query-tags-leaner
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-tags-leaner
```

          

        
        
          

**Available version**

          
: 67.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**Root XML tag**

          
: `<LeanerQueryTagsInputRepresentation>`

        
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "0000000s07fm061002917633740427233ff03037a8fe48048696667781ec824c",
  "tags": [
    "Contact_FirstName",
    "Contact_Email"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of the context to query. | Required | 66.0 |
| `tags` | String[] | List of tag names to query from the context. Tags can include both attribute-level and node-level. | Required | 66.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Leaner Query Tags Result](./connect_responses_leaner_query_tags_result.htm.md)

=== ARTICLE: connect_resources_context_runtime_schema.htm ===
---
page_id: connect_resources_context_runtime_schema.htm
title: Context Runtime Schema (DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_runtime_schema.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Runtime Schema (DELETE)

Clear runtime schema cache for context definitions and their associated mappings. 

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-runtime-schema/clear
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-runtime-schema/clear?contextDefinitionDevlName=CustomerProfile&contextMappingNames=StandardMapping,CustomMapping
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: DELETE

        
        
          

**Request parameters for DELETE**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionDevlName` | String | Developer name of the context definition whose runtime schema is to be cleared. | Required | 65.0 |
| `contextMappingNames` | String[] | Comma-separated list of mapping names to clear. If not provided, the default mapping for the definition is cleared. | Optional | 65.0 |

          

        
        
          

**Response body for DELETE**

          
: 
            

This resource uses query parameters only and returns HTTP 204 No Content on
              success.

=== ARTICLE: connect_resources_context_service_runtime.htm ===
---
page_id: connect_resources_context_service_runtime.htm
title: Context Service (DELETE, GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_service_runtime.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service (DELETE, GET)

Retrieve the context details using a context ID. Delete a context record using a
    context ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/${contextId}
```

          

        
        
          

**Example **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/c4c69a9a-3841-4fc3-a10d-a52779ade3d8
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: DELETE, GET

        
        
          

**Response body for GET**

          
: [Context Info](./connect_responses_context_info.htm.md)

        
        
          

**Response body for DELETE**

          
: None.

=== ARTICLE: connect_resources_context_tag.htm ===
---
page_id: connect_resources_context_tag.htm
title: Context Tag (GET, POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_tag_managament.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag (GET, POST, PATCH)

Query, create, and update context tag.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-tags
```

          

        
        
          

**Example for GET **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-tags
```

          

        
        
          

**Example for POST **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-tags
```

          

        
        
          

**Example for PATCH **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-tags
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, POST, PATCH 

        
        
          

**Response body for GET**

          
: 
[Context Tag List Output](./connect_responses_context_tag_list.htm.md)

#### Note

              

When the `includeReferencedDefinitionTag` query
                parameter is set to `true` in a GET request, the
                response will include the name of the context tag in the format `ContextDeveloperName.tagName`.

            

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
    "contextTags": [
        {
            "name": "Attribute_Tag",
            "contextAttributeId": "11nxx000001hOozAAE"
        },
        {
            "name": "Node_Tag",
            "contextNodeId": "11oxx000001G9D2AAK"
        }
    ]
}
```

          

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of the (parent) context attribute. | Required | 59.0 |
| `contextNodeId` | String | ID of the (parent) context node. | Required | 59.0 |
| `contextTagId` | String | ID of this Context tag. Required only for update. | Optional | 59.0 |
| `name` | String | Name of the context tag. | Required | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Context Tag List Output](./connect_responses_context_tag_list.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
    "contextTags": [
        {
            "name": "Updated_ATag",
            "contextTagId": "11kxx00000ZzcDpAAJ"
        }
    ]
}
```

                

              
            

          

        
        
          

**Response body for PATCH**

          
: [Context Tag List Output](./connect_responses_context_tag_list.htm.md)

=== ARTICLE: connect_resources_context_tag_id.htm ===
---
page_id: connect_resources_context_tag_id.htm
title: Context Tag ID (GET, DELETE)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_tag_id.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_tag_managament.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag ID (GET, DELETE)

Query and delete a context tag.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definitions/${contextDefinitionId}/context-tags/${contextTagId}
```

          

        
        
          

**Example for GET **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-tags/${contextTagId}
```

          

        
        
          

**Example for DELETE **

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-definitions/${contextDefinitionId}/context-tags/${contextTagId}
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET, DELETE

        
        
          

**Response body for GET**

          
: [Context Attribute Tag Output](./connect_responses_context_attribute_tag.htm.md)

=== ARTICLE: connect_resources_create_context.htm ===
---
page_id: connect_resources_create_context.htm
title: Context Service (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_create_context.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service (POST)

Create new context records by submitting metadata and associated JSON data. After
    validating the data, the system generates a new context ID. Context objects created using this
    API apply only to a single request. They cannot be used to pass data across multiple
    requests.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts
```

          

        
        
          

**Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "metadata": {
    "contextDefinitionId": "11Oxx0000006VjNEAU",
    "mappingId": "11jxx0000004Q83AAE"
  },
  "data": "{\"Order\":[{\"id\":\"TestOrder123\",\"businessObjectType\":\"Order\",\"Name\":\"Test Order\",\"Status\":\"SHIPPED\",\"AccountName\":\"Kroger\",\"OrderItems\":[{\"id\":\"TestOrderItem1\",\"businessObjectType\":\"OrderItem\",\"ProductName\":\"Coke\"},{\"id\":\"TestOrderItem2\",\"businessObjectType\":\"OrderItem\",\"ProductName\":\"Pepsi\"}]}]}"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | Payload containing context-specific information. | Required | 59.0 |
| `metadata` | [Context MetaData Input](./connect_requests_context_meta_data_input.htm.md) | Metadata information about context. | Required | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Context
              Info](./connect_responses_context_info.htm.md)

=== ARTICLE: connect_resources_create_query_tag.htm ===
---
page_id: connect_resources_create_query_tag.htm
title: Query Tags (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_create_query_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Tags (POST)

Create query tags within a defined context

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/query-tags
```

          

        
        
          

**Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-tags
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
  "tags": [
    "Order"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of the context record. | Required | 59.0 |
| `tags` | String[] | List of query tags to be queried within this context. | Required | 59.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Query Tags
              Result](./connect_responses_query_tags_result.htm.md)

=== ARTICLE: connect_resources_create_update_query_data_record_status.htm ===
---
page_id: connect_resources_create_update_query_data_record_status.htm
title: Query Record Status (PATCH, POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_create_update_query_data_record_status.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Record Status (PATCH, POST)

Update the processing status and related error messages of query data records. Create
    the processing status and related error messages of query data records

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/query-record-status
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-record-status/18732dfd
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-record-status/18732dfd
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: PATCH, POST

        
        
          

**Response body for PATCH**

          
: [Context
            Output](./connect_responses_context_output.htm.md)

        
        
          

**Request body for POST**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
    "queryRecordStatusInput": {
        "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
        "queryPaths": [
            {
                "dataPath": [
                    "TestOrder123"
                ]
            }
        ]
    }
}

```

                

              
              
                

**Properties**

                
: 
                  

                      
                      
                      
                      
                      
                      
                        
                          

                          

                          

                          

                          

                        

                      

                      
                        
                          

                          

                          

                          

                          

                        

                      

                    
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `queryRecordStatusInput` | Object | Input representation for context ID and the list of paths for querying the status. | Required | 59.0 |

                

              
            

          

        
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
  "queryPaths": [
    {
      "dataPath": [
        "TestOrder123"
      ]
    }
  ]
}
```

          

        
        
          

**Response body for POST**

          
: [Query
              Record Status Result](./connect_responses_query_record_status_result.htm.md)

=== ARTICLE: connect_resources_node_mapping.htm ===
---
page_id: connect_resources_node_mapping.htm
title: Context Node Mapping (POST, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_node_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_node_mapping_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Mapping (POST, PATCH)

Create and update context node mappings.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-mappings/${contextMappingId}/context-node-mappings
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-mappings/${contextMappingId}/context-node-mappings
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v59.0/connect/context-mappings/${contextMappingId}/context-node-mappings
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST, PATCH

        
        
          

**Request body for POST**

          
: 
            
                
                    

**JSON example**

                    
: 
                        

```
{
    "contextNodeMappings": [
        {
            "contextNodeId": "11oxx000001G31BAAS",
            "sObjectName": "Order"
        },
        {
            "contextNodeId": "11oxx000001G31CAAS",
            "sObjectName": "OrderItem"
        }
    ]
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributeMappings` | [Context Attribute Mappings Input](./connect_requests_context_attribute_mappings_input.htm.md)[] | List of context attribute mappings. | Required | 59.0 |
| `contextNodeId` | String | Reference to context node. | Optional | 59.0 |
| `contextNodeMappingId` | String | ID of this context node mapping. Required for update. | Required | 59.0 |
| `sObjectName` | String | SObject name. | Optional | 59.0 |

                    

                
            

          

        
        
          

**Response body for POST**

          
: [Context Node Mapping List Output](./connect_responses_context_node_mapping_list.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
    "contextNodeMappings": [
        {
            "contextNodeMappingId": "11bxx000000YZipAAG",
            "sObjectName": "Quote"
        },
        {
            "contextNodeMappingId": "11bxx000000YZiqAAG",
            "sObjectName": "QuoteItem"
        }
    ]
}
```

                

              
            

          

        
        
          

**Response body for PATCH**

          
: [Context Node Mapping List Output](./connect_responses_context_node_mapping_list.htm.md)

=== ARTICLE: connect_resources_persist_context.htm ===
---
page_id: connect_resources_persist_context.htm
title: Persist Context (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_persist_context.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: persistence_context_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Persist Context (POST)

Persist a context by passing the context ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/persist-records
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/persist-records
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "contextPersistInput": {
    "contextId": "384fdcef-36e2-4bbb-82ed-2e7bc4e670c7",
    "targetMappingId": "11jxx0000004Q83AAE"
  }
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextPersistInput` | Object | Contains contextId and targetMappingId for persisting context. | Required | 59.0 |

          

        
      

          

        
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "384fdcef-36e2-4bbb-82ed-2e7bc4e670c7",
  "targetMappingId": "11jxx0000004Q83AAE"
}
```

          

        
        
          

**Response body for POST**

          
: 
[Persist
              Context Output](./connect_responses_persist_context_output.htm.md)

#### Note

              

When updating reference fields within a context and attempting to persist the
                context, changes to the reference field itself may not be persisted. This is because
                reference fields point to related entities, and the persist operation primarily
                focuses on the attributes of the main entity within the context. 

              

For example, if you have an Order context with a reference field to an Account,
                updating the Account reference within the Order context and then calling the persist
                API may not save the updated Account reference. Other attributes of the Order might
                be persisted, but the relationship to the Account might not be.

=== ARTICLE: connect_resources_query_context_interface_by_name.htm ===
---
page_id: connect_resources_query_context_interface_by_name.htm
title: Query Context Definition Interface By Name (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_query_context_interface_by_name.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Definition Interface By Name (GET)

Get the details of a context definition interface by using the context definition
    interface name.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definition-interfaces/contextDefinitionInterfaceName
```

          

        
        
          
: The contextDefinitionInterfaceName path parameter is the API name
            of the context definition interface.

        
        
          

**Resource example**

          
: 

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-definition-interfaces/exampleDefinitionInterface
```

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Response body for GET**

          
: [Context Definition
              Interface](./connect_responses_context_definition_interface.htm.md)

=== ARTICLE: connect_resources_query_context_interfaces.htm ===
---
page_id: connect_resources_query_context_interfaces.htm
title: Query Context Definition Interfaces (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_query_context_interfaces.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Definition Interfaces (GET)

Get the lists of metadata associated with context definition interfaces.

    
      
        
          

**Resource**

          
: 
            

```
/connect/context-definition-interfaces
```

          

        
        
          

**Resource example**

          
: 

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/context-definition-interfaces
```

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Response body for GET**

          
: [Context Definition
              Interface Metadata List](./connect_responses_context_definition_interface_metadata_list.htm.md)

=== ARTICLE: connect_resources_query_context_record.htm ===
---
page_id: connect_resources_query_context_record.htm
title: Query Context Record (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_query_context_record.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Record (POST)

Query a context record, with the option to retrieve child records.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/query-record
```

          

        
        
          

**Examples**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-record
```

          

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/query-record?children=false
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request parameters for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `children` | Boolean | Indicates whether to retrieve child records `true` or not `false`. | Optional | 59.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "contextId": "7bc695bc-f38b-4a94-8a95-0caa50f3da53"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | String[] | List of attributes to be retrieved. | Optional | 58.0 |
| `businessObjectTypeFilter` | String | Filter based on a business object type. | Optional | 58.0 |
| `contextId` | String | The ID of the context to be queried. | Required | 58.0 |
| `queryPath` | String[] | Path to the parent node. | Optional | 58.0 |

          

        
        
          

**Response body for POST**

          
: [Query
              Context Record Result](./connect_responses_query_context_record_result.htm.md)

=== ARTICLE: connect_resources_update_context_attribute.htm ===
---
page_id: connect_resources_update_context_attribute.htm
title: Context Attribute (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_update_context_attribute.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute (PATCH)

Update attributes of a context record.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/attributes
```

          

        
        
          

**Example for PATCH**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/contexts/attributes
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: PATCH

        
        
        
          

**Request body for PATCH**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
    "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
    "nodePathAndAttributes": [
        {
            "nodePath": {
                "dataPath": [
                    "TestOrder123"
                ]
            },
            "attributes": [
                {
                    "attributeName": "Status",
                    "attributeValue": "DISPATCHED"
                }
            ]
        }
    ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `updateContextAttributesInput` | Object | Input object for updating context attributes. | Required | 59.0 |

          

        
      

          

          
: 
            

#### Note

 When a context definition is mapped to Account and a field is mapped to `Account.RecordType.Name`, updating the RecordType's ID
              does not update the mapped field. This is because updating the RecordType ID does not
              cause updates to other fields of the RecordType record.

          

        
        
          

**Response body for PATCH**

          
: [Context
            Output](./connect_responses_context_output.htm.md)

=== ARTICLE: connect_resources_write_through_tags.htm ===
---
page_id: connect_resources_write_through_tags.htm
title: Write Through Tags (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_write_through_tags.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: runtime_context_intance_management.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Write Through Tags (PATCH)

Update Context Attributes through tags.

    
      
        
          

**Resource**

          
: 
            

```
/connect/contexts/write-through-tags
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: PATCH

        
        
          

**Request body for PATCH**

          
: 
            

```
{
    "contextId": "3ec8da809ebd6cef79f685239fb005e8c7cffa075a0d3d7b1d8d17ec22bxxxxd",
    "nodePathAndTagValues": [
        {
            "nodePath": {
                "dataPath": [
                    "001xx000003GbQSAA0"
                ]
            },
            "tagValues": [
                {
                    "tagName": "Name",
                    "tagValue": "updatedAccount"
                },
                {
                    "tagName": "City",
                    "tagValue": "Bangalore"
                }
            ]
        }
    ]
}
```

          

        
        
          

**Request parameters for PATCH**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of context which will get updated. | Required | 63.0 |
| `nodePath​And​TagValues` | [List<Node​PathAndTag​ValuesInput​Representation>](./connect_requests_node_path_and_tag_values.htm.md) | Node path which needs to update with tag details. | Required | 63.0 |

          

        
        
          

**Response body for PATCH**

          
: [ContextOutputRepresentation](./connect_responses_context_output.htm.md)

=== ARTICLE: connect_responses_context_attr_hydration_detail.htm ===
---
page_id: connect_responses_context_attr_hydration_detail.htm
title: Context Attribute Hydration Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attr_hydration_detail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Hydration Detail

Output representation of context attribute hydration detail.

              

              

              

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `childDetails` | [Context Attribute Hydration Detail](#connect_responses_context_attr_hydration_detail)[] | List of parent context attribute hydration detail. | Small, 59.0 | 59.0 |
| `contextAttrHydrationDetailId` | String | ID of this context attribute hydration detail record. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `mappedAttributeDataTypeInfo` | [Mapped Attribute Data Type](./connect_responses_mapped_attribute_data_type_info.htm.md)[] | Data type of the attribute mapped field. | Small, 59.0 | 59.0 |
| `parentMappingAttributeId` | String | ID of the parent context attribute mapping record. | Small, 59.0 | 59.0 |
| `queryAttribute` | String | Query attribute. | Small, 59.0 | 59.0 |
| `sObjectDomain` | String | sObject domain. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_attribute.htm ===
---
page_id: connect_responses_context_attribute.htm
title: Context Attribute Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attribute.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Output

Output representation of the context attribute.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributeTags` | [Context Attribute Tag](./connect_responses_context_attribute_tag.htm.md)[] | List of context attribute tags. | Small, 59.0 | 59.0 |
| `contextAttributeId` | String | ID of this context attribute. | Small, 59.0 | 59.0 |
| `dataType` | String | Data type of the context attribute. | Small, 59.0 | 59.0 |
| `domainSet` | String | Comma separated node names referenced by this attribute. | Small, 59.0 | 59.0 |
| `fieldType` | String | Field type of the attribute. | Small, 59.0 | 59.0 |
| `isKey` | Boolean | Specifies if it used for transposable feature (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isValue` | Boolean | Specifies if it used for transposable (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `name` | String | Name of the attribute. | Small, 59.0 | 59.0 |
| `parentNodeId` | String | ID of (parent) context node. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_attribute_list.htm ===
---
page_id: connect_responses_context_attribute_list.htm
title: Context Attribute List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attribute_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute List Output

Output representation of list of context attributes.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Context Attribute Output](./connect_responses_context_attribute.htm.md)[] | List of attributes. | Small, 59.0 | 59.0 |
| `contextAttributeListId` | String | Unique ID. Required for LDS | Small, 59.0 | 59.0 |
| `contextNodeId` | String | ID of context node. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Success | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_attribute_mapping.htm ===
---
page_id: connect_responses_context_attribute_mapping.htm
title: Context Attribute Mapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attribute_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Mapping

Output representation of the context attribute mapping.

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| contextAttr​ContextHydration​DetailList | Context Attribute Hydration Detail[] | List of the context attribute hydration records when context-to-context mappings exist. | Small, 61.0 | 61.0 |
| `context​AttrHydration​DetailList` | Context Attribute Hydration Detail[] | Details of the context attribute hydration. | Small, 59.0 | 59.0 |
| `context​AttributeId` | String | ID of the context attribute record. | Small, 59.0 | 59.0 |
| `contextAttribute​MappingId` | String | ID of the context attribute mapping record. | Small, 59.0 | 59.0 |
| `contextInput​AttributeName` | String | Input attribute name. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `parentNode​MappingId` | String | ID of the parent context node mapping record. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_attribute_mapping_list.htm ===
---
page_id: connect_responses_context_attribute_mapping_list.htm
title: Context Attribute Mapping List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attribute_mapping_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Mapping List

Output representation of list of context attribute mappings.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeMappingListId` | String | Unique ID. Required for LDS. | Small, 59.0 | 59.0 |
| `contextAttributeMappings` | [Context Attribute Mapping](./connect_responses_context_attribute_mapping.htm.md)[] | List of context attribute mappings. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_attribute_tag.htm ===
---
page_id: connect_responses_context_attribute_tag.htm
title: Context Attribute Tag Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_attribute_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute Tag Output

Output representation of context attribute tag.

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

```

```

```

```

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextAttributeId` | String | ID of (parent) context attribute. | Small, 59.0 | 59.0 |
|  |  |  |  |  |
| `contextTagId` | String | ID of this context tag. | Small, 59.0 | 59.0 |
| `dynamic` | Boolean | Indicates if the attribute tag is dynamic (true ) or not (false ). | Small, 59.0 | 59.0 |
|  |  |  |  |  |
| `name` | String | Name of the context attribute tag. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_data_record.htm ===
---
page_id: connect_responses_context_data_record.htm
title: Context Data Record
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_data_record.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Data Record

Output representation of context data record, including its attributes, type, associated
    child objects, and other relevant metadata.

      
        
          

**Sample Response**

          
: 
            

```
{
            "childQueryRecords": [
                {
                    "childQueryRecords": [],
                    "record": {
                        "attributesAndValues": {
                            "Name": "Acme Corp",
                            "BillingAddress": "{city:New York,country:USA,geocodeAccuracy:null,latitude:null,longitude:null,postalCode:31349,state:NY,street:10 Main Rd.}",
                            "Industry": "Manufacturing",
                            "Type": "Prospect"
                        },
                        "businessObjectType": "Account",
                        "childBusinessObjectTypes": [
                            "OpportunityItem",
                            "OrderItem"
                        ],
                        "contextDataRecordId": "003xx000004WhFsAAK",
                        "currentState": "CREATED",
                        "lastUpdatedTimeStamp": "2023-10-11 04:46:13.804"
                    }
                }
            ]
        }
    ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributesAndValues` | Map<String, Object> | Mapping of attributes to their corresponding values within the context. | Small, 59.0 | 59.0 |
| `businessObjectType` | String | Type of business object. | Small, 59.0 | 59.0 |
| `childBusinessObjectTypes` | String[] | List indicating types of child business objects. | Small, 59.0 | 59.0 |
| `contextDataRecordId` | String | Unique ID of the context data record. | Small, 59.0 | 59.0 |
| `currentState` | String | The current status of the context data record. | Small, 59.0 | 59.0 |
| `lastUpdatedTimeStamp` | String | The last updated time stamp of context data record. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_data_record_status.htm ===
---
page_id: connect_responses_context_data_record_status.htm
title: Context Data Record Status
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_data_record_status.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Data Record Status

Output representation of context data record status.

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextErrors` | [Context Error](./connect_responses_context_error.htm.md)[] | List of context errors. | Small, 59.0 | 59.0 |
| `dataPath` | String[] | Path of the data. | Small, 59.0 | 59.0 |
| `processingStatus` | String | Processing status of the context data record. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_definition.htm ===
---
page_id: connect_responses_context_definition.htm
title: Context Definition Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Output

Output representation of context definition.

            
              

              

              

              

              

            

- 
- 
- 

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `activeVersionId` | String | ID of the active context definition version. | Small, 59.0 | 59.0 |
| `canBeReferenceDefinition` | Boolean | Specifies if the context definition can be used as a reference definition to other context definitions (`true`) or not (`false`). | Small, 63.0 | 63.0 |
| `contextDefinitionId` | String | ID of the context definition. | Small, 59.0 | 59.0 |
| `contextDefinitionVersionList` | [Context Definition Version](./connect_responses_context_definition_version.htm.md)[] | List of context definition versions. | Small, 59.0 | 59.0 |
| `contextTtl` | Integer | TTL of the context. | Small, 59.0 | 59.0 |
| `definition` | String | Definition. | Small, 59.0 | 59.0 |
| `definitionType` | String | Type of definition. Possible values are: `standard_executable` `standard_nonexecutable` `custom_nonexecutable` | Small, 60.0 | 60.0 |
| `developerName` | String | Developer name. | Small, 59.0 | 59.0 |
| `hasSystemTags` | String | Specifies if the context definition has system node and tags attached (`true`) or not (`false`). | Small, 63.0 | 63.0 |
| `interfaces` | String | List of implemented Context Definition Interfaces for this context definition. | Small, 62.0 | 62.0 |
| `isActive` | Boolean | Specifies if the context definition is active (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isEditable` | Boolean | Specifies if the context definition is editable (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `referenceContextDefinitions` | [ContextDefinitionReference[]](./connect_responses_context_definition_reference.htm.md) | List of reference defintions this definition is referencing . | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_context_definition_filter.htm ===
---
page_id: connect_responses_context_definition_filter.htm
title: Context Definition Filter
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_filter.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filter

Output representation details of a context definition filter.

      
        
          

**JSON example**

          
: This example shows a sample response for the Context Definition Filter by ID (GET)
            request.

```
{
  "contextDefinitionFilterId": "1Tlxx0000004DUuCAM",
  "contextDefinitionVersionId": "11pxx0000004VmmAAE",
  "filterName": "FilterAccount2",
  "filterApiName": "FilterAccount2",
  "filtersPerNode": "{&quot;Account&quot;:{&quot;filterCondition&quot;:{&quot;attribute&quot;:&quot;City&quot;,&quot;operator&quot;:&quot;EQUALS&quot;,&quot;operands&quot;:[{&quot;value&quot;:&quot;Bengaluru&quot;,&quot;type&quot;:&quot;STRING&quot;}],&quot;composite&quot;:false},&quot;orderByConditions&quot;:[{&quot;orderByAttribute&quot;:&quot;Name&quot;,&quot;ascending&quot;:false,&quot;nullsFirst&quot;:false}],&quot;limit&quot;:5}}"
  "isSuccess": true
}
```

          
: This example shows a sample response for the Context Definition Filter By ID (PATCH)
            request.

```
{
  "contextDefinitionFilterId": "1Tlxx0000004DUuCAM",
  "contextDefinitionVersionId": "11pxx0000004VmmAAE",
  "description": "Updated",
  "filterName": "FilterAccount2",
  "filterApiName": "FilterAccount2",
  "filtersPerNode": "{&quot;Account&quot;:{&quot;filterCondition&quot;:{&quot;attribute&quot;:&quot;City&quot;,&quot;operator&quot;:&quot;EQUALS&quot;,&quot;operands&quot;:[{&quot;value&quot;:&quot;Bengaluru&quot;,&quot;type&quot;:&quot;STRING&quot;}],&quot;composite&quot;:false},&quot;orderByConditions&quot;:[{&quot;orderByAttribute&quot;:&quot;Name&quot;,&quot;ascending&quot;:false,&quot;nullsFirst&quot;:false}],&quot;limit&quot;:5}}",
  "isSuccess": true
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionFilterId` | String | ID of the context definition filter. | Small, 65.0 | 65.0 |
| `contextDefinitionVersionId` | String | Unique identifier of the specific context definition version to which this filter belongs. | Small, 65.0 | 65.0 |
| `description` | String | Details of the context definition filter such as the purpose of the filter. Use this field to document the filter's business logic, intended use case, or any important implementation details for future reference. | Small, 65.0 | 65.0 |
| `filterApiName` | String | Unique API name identifier for the context definition filter. | Small, 65.0 | 65.0 |
| `filterName` | String | Display name for the context definition filter. | Small, 65.0 | 65.0 |
| `filtersPerNode` | String | A JSON string representation of the filter condition logic that defines the filter criteria. This field contains the structured query conditions that's evaluated to determine which records match the filter. The JSON structure typically includes field names, operators, and values that form the filter expression. | Small, 65.0 | 65.0 |
| `inheritedFrom` | String | Source context definition if filter is inherited in the GET request. This field is not applicable for POST request. | Small, 65.0 | 65.0 |
| `isSuccess` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_context_definition_filter_list.htm ===
---
page_id: connect_responses_context_definition_filter_list.htm
title: Context Definition Filter List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_filter_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Filter List

Output representation details of context definition filter list.

        
          

**JSON example**

          
: 
            

```
{
  "contextDefinitionFilterList": [
    {
      "contextDefinitionFilterId": "1Tlxx0000004DRgCAM",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE",
      "filterApiName": "FilterAccount"
      "filterName": "FilterAccount",
      "filtersPerNode": "{\n    &quot;Account&quot;: {\n      &quot;filterCondition&quot;: {\n        &quot;attribute&quot;: &quot;Name&quot;,\n        &quot;operator&quot;: &quot;EQUALS&quot;,\n        &quot;operands&quot;: [\n          {\n            &quot;value&quot;: &quot;Acme&quot;,&quot;type&quot;: &quot;STRING&quot;\n          }\n        ]\n      },\n      &quot;orderByConditions&quot;: [\n        {\n          &quot;orderByAttribute&quot;: &quot;Name&quot;,\n          &quot;ascending&quot;: false,\n          &quot;nullsFirst&quot;: false\n        }\n      ],\n      &quot;limit&quot;: 10\n    }\n  }"
    },
    {
      "contextDefinitionFilterId": "1Tlxx0000004DTICA2",
      "contextDefinitionVersionId": "11pxx0000004VmmAAE",
      "filterName": "FilterContact",
      "filterApiName": "FilterContact",
      "filtersPerNode": "{\n    &quot;Contact&quot;: {\n      &quot;filterCondition&quot;: {\n        &quot;attribute&quot;: &quot;FirstName&quot;,\n        &quot;operator&quot;: &quot;EQUALS&quot;,\n        &quot;operands&quot;: [\n          {\n            &quot;value&quot;: &quot;Howard&quot;,&quot;type&quot;: &quot;STRING&quot;\n          }\n        ]\n      }\n  }\n  }"
    }
  ],
  "contextDefinitionFilterListId": "4dd6fda2-3fa0-4075-8f03-33a1288ef009",
  "contextDefinitionId": "SimpleDef",
  "isSuccess": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionFilterList` | [Context Definition Filter](./connect_responses_context_definition_filter.htm.md)[] | List of context definition filters. | Small, 65.0 | 65.0 |
| `contextDefinitionFilterListId` | String | ID of the context definition filter list. | Small, 65.0 | 65.0 |
| `contextDefinitionId` | String | ID of the context definition. | Small, 65.0 | 65.0 |
| `isSuccess` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_context_definition_info.htm ===
---
page_id: connect_responses_context_definition_info.htm
title: Context Definition Information
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_info.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Information 

Output representation of context definition information.

      
        
          

**Sample Response**

          
: 
            

```
{
  "activeVersionId": "11pxx0000004cLEAAY",
  "contextDefinitionId": "11Oxx0000006XWfEAM",
  "contextTtl": 30,
  "createdBy": "Admin User",
  "createdDate": "2024-10-17T14:34:26.000Z",
  "definition": "ExampleDefinition",
  "description": "Example Description",
  "developerName": "ExampleDevelopername",
  "isActive": false,
  "isEditable": true,
  "isSuccess": true,
  "lastModifiedBy": "Admin User",
  "lastModifiedDate": "2024-10-17T14:34:26.000Z",
  "startDate": "2024-10-17T14:34:26.000Z"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `activeVersionId` | String | Active context definition version ID. | Small, 59.0 | 59.0 |
| `contextDefinitionId` | String | ID of the context definition. | Small, 59.0 | 59.0 |
| `contextTtl` | Integer | TTL of the context. | Small, 59.0 | 59.0 |
| `createdBy` | String | User who created the context definition. | Small, 59.0 | 59.0 |
| `createdDate` | String | Date on which the context definition was created. | Small, 59.0 | 59.0 |
| `definition` | String | Name of the context definition. | Small, 59.0 | 59.0 |
| `description` | String | Short description of context definition. | Small, 59.0 | 59.0 |
| `developerName` | String | Developer name associated with the definition. | Small, 59.0 | 59.0 |
| `isActive` | Boolean | Specifies if the context definition list is active (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isEditable` | Boolean | Specifies if the context definition list is editable (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `lastModifiedBy` | String | User who last modified the definition. | Small, 59.0 | 59.0 |
| `lastModifiedDate` | String | Date on which the definition was modified last. | Small, 59.0 | 59.0 |
| `startDate` | String | Start date from when context definition is valid. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_definition_interface.htm ===
---
page_id: connect_responses_context_definition_interface.htm
title: Context Definition Interface
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_interface.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Interface

Output representation of the details of the context definition interface.

        
          

**JSON example**

          
: 
            

```
{
  "contextDefinitionInterfaceMetadata": {
    "createdBy": "Automated Process",
    "createdDate": "2024-05-15T00:00:00.000Z",
    "description": "Test Interface",
    "developerName": "TestBaseInterface",
    "interfaceName": "TestBaseInterface",
    "lastModifiedBy": "Automated Process",
    "parentInterfaces": [
      "TestBaseInterface1"
    ],
    "version": "62.1"
  },
  "contextDefinitionInterfaceNodeTagList": [
    {
      "attributeTags": [
        {
          "dataType": "STRING",
          "isMappingRequired": true,
          "isNodeTag": false,
          "tagName": "id_attr_tag"
        }
      ],
      "childNodeTags": [
        {
          "attributeTags": [
            {
              "dataType": "STRING",
              "isMappingRequired": false,
              "isNodeTag": false,
              "tagName": "contactId_attr_tag"
            },
            {
              "dataType": "STRING",
              "isMappingRequired": true,
              "isNodeTag": false,
              "tagName": "contactName_attr_tag"
            }
          ],
          "childNodeTags": [],
          "isMappingRequired": false,
          "isNodeTag": true,
          "tagName": "Contact_node_tag"
        }
      ],
      "isMappingRequired": true,
      "isNodeTag": true,
      "tagName": "Account_node_tag"
    }
  ],
  "isSuccess": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinition​InterfaceMetadata` | [Context Definition Interface Metadata](./connect_responses_context_definition_interface_metadata.htm.md) | Metadata details associated with the context definition interface. | Small, 62.0 | 62.0 |
| `contextDefinition​Interface​NodeTagList` | [Context Definition Interface Node Tag](./connect_responses_context_definition_interface_node_tag.htm.md)[] | List of tags associated with the context definition interface. | Small, 62.0 | 62.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_definition_interface_attribute_tag.htm ===
---
page_id: connect_responses_context_definition_interface_attribute_tag.htm
title: Context Definition Interface Attribute Tag
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_interface_attribute_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Interface Attribute Tag

Output representation of the attribute tags associated with the context definition
    interface.

        
          

**JSON example**

          
: 
            

```
{
  "attributeTags": [
    {
      "dataType": "REFERENCE",
      "isMappingRequired": false,
      "isNodeTag": false,
      "domainName": "Account",
      "tagName": "AccountRef_attr_tag"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dataType` | String | Data type of the attribute associated with the context definition interface. | Small, 62.0 | 62.0 |
| `domainName` | String | Domain name of the attribute associated with the context definition interface. | Small, 62.0 | 62.0 |
| `isMappingRequired` | Boolean | Indicates whether the attribute tag must be mapped in the context definition (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `isNodeTag` | Boolean | Indicates whether the attribute tag is a node tag (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `isOptional` | Boolean | Indicates whether validation must be done for the attribute tag (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `tagName` | String | Name of the attribute tag. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_definition_interface_metadata.htm ===
---
page_id: connect_responses_context_definition_interface_metadata.htm
title: Context Definition Interface Metadata
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_interface_metadata.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Interface Metadata

Output representation of the metadata associated with the context definition
    interface.

        
          

**JSON example**

          
: 
            

```
{
  "contextDefinitionInterfaceMetadata": {
    "createdBy": "Automated Process",
    "createdDate": "2024-05-15T00:00:00.000Z",
    "description": "Test Interface",
    "developerName": "TestBaseInterface",
    "interfaceName": "TestBaseInterface",
    "lastModifiedBy": "Automated Process",
    "parentInterfaces": [
      "TestBaseInterface1"
    ],
    "version": "62.1"
  }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `createdBy` | String | User, system, or object that created the context definition interface. | Small, 62.0 | 62.0 |
| `createdDate` | String | Date when the context definition interface was created. | Small, 62.0 | 62.0 |
| `description` | String | Description of the context definition interface. | Small, 62.0 | 62.0 |
| `developerName` | String | Developer name of the context definition interface. | Small, 62.0 | 62.0 |
| `interfaceName` | String | Title of the context definition interface. | Small, 62.0 | 62.0 |
| `lastModifiedBy` | String | User, system, or object that last updated the context definition interface. | Small, 62.0 | 62.0 |
| `parentInterfaces` | String[] | List of parent context definition interfaces that this interface is inherited from. | Small, 62.0 | 62.0 |
| `version` | String | Version number of the context definition interface. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_definition_interface_metadata_list.htm ===
---
page_id: connect_responses_context_definition_interface_metadata_list.htm
title: Context Definition Interface Metadata List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_interface_metadata_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Interface Metadata List

Output representation of the metadata list associated with the context definition
    interfaces.

        
          

**JSON example**

          
: 
            

```
{
  "contextDefinitionInterfaceMetadataList": [
    {
      "createdBy": "Automated Process",
      "createdDate": "2024-05-15T00:00:00.000Z",
      "description": "Test Interface",
      "developerName": "TestBaseInterface",
      "interfaceName": "TestBaseInterface",
      "lastModifiedBy": "Automated Process",
      "parentInterfaces": [
        "TestBaseInterface1"
      ],
      "version": "62.1"
    }
  ],
  "contextDefinitionInterfaceMetadataListId": "43db7f18-9dd7-40a2-9a34-a2b3a1cff9e5",
  "isSuccess": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinition​Interface​MetadataList` | [Context Definition Interface Metadata](./connect_responses_context_definition_interface_metadata.htm.md)[] | List of metadata associated with the context definition interfaces. | Small, 62.0 | 62.0 |
| `contextDefinition​Interface​MetadataListId` | String | Unique ID of the metadata list associated with the context definition interfaces. Required for Lightning Data Service (LDS). | Small, 62.0 | 62.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_definition_interface_node_tag.htm ===
---
page_id: connect_responses_context_definition_interface_node_tag.htm
title: Context Definition Interface Node Tag
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_interface_node_tag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Interface Node Tag

Output representation of the tags associated with the context definition
    interface.

        
          

**JSON example**

          
: 
            

```
{
  "contextDefinitionInterfaceNodeTagList": [
    {
      "attributeTags": [
        {
          "dataType": "STRING",
          "isMappingRequired": true,
          "isNodeTag": false,
          "tagName": "id_attr_tag"
        }
      ],
      "childNodeTags": [
        {
          "attributeTags": [
            {
              "dataType": "STRING",
              "isMappingRequired": false,
              "isNodeTag": false,
              "tagName": "contactId_attr_tag"
            },
            {
              "dataType": "STRING",
              "isMappingRequired": true,
              "isNodeTag": false,
              "tagName": "contactName_attr_tag"
            }
          ],
          "childNodeTags": [],
          "isMappingRequired": false,
          "isNodeTag": true,
          "tagName": "Contact_node_tag"
        }
      ],
      "isMappingRequired": true,
      "isNodeTag": true,
      "tagName": "Account_node_tag"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributeTags` | [Context Definition Interface Attribute Tag](./connect_responses_context_definition_interface_attribute_tag.htm.md)[] | List of attribute tags associated with the context definition interface. | Small, 62.0 | 62.0 |
| `childNodeTags` | [Context Definition Interface Node Tag](#)[] | List of child node tags associated with the context definition interface. | Small, 62.0 | 62.0 |
| `isMappingRequired` | Boolean | Indicates whether the context tags must be mapped in the context definition (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `isNodeTag` | Boolean | Indicates whether the context tag is a node tag (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `isOptional` | Boolean | Indicates whether validation must be done for the context tag (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `tagName` | String | Name of the context tag. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_definition_list.htm ===
---
page_id: connect_responses_context_definition_list.htm
title: Context Definition List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition List 

Output representation of list of context definitions.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionList` | [Context Definition Information](./connect_responses_context_definition_info.htm.md)[] | List of context definitions. | Small, 59.0 | 59.0 |
| `contextDefinitionListId` | String | Unique ID. Required for LDS. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the output is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_definition_reference.htm ===
---
page_id: connect_responses_context_definition_reference.htm
title: Context Definition Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_reference.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Reference

Output representation of context definition reference.

        
            

                    
                    
                    
                    
                    
                    
                        
                            

                            

                            

                            

                            

                        

                    

                    
                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                    

                
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionReferenceId` | String | ID of the ContextDefinitionReference. | Small, 63.0 | 63.0 |
| `referenceContextDefinition` | String | ID of the reference context definition. | Small, 63.0 | 63.0 |
| `inheritedFrom` | String | Represents inherited reference definition in the definition. | Small, 63.0 | 63.0 |
| `contextDefinition` | String | ID or name of the current context defintion. | Small, 63.0 | 63.0 |
| `referenceContextDefinitionName` | String | Reference context definition name. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_context_definition_version.htm ===
---
page_id: connect_responses_context_definition_version.htm
title: Context Definition Version
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_version.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Version 

Output representation of context definition version.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionId` | String | ID of context definition. | Small, 59.0 | 59.0 |
| `contextDefinitionVersionId` | String | ID of context definition version. | Small, 59.0 | 59.0 |
| `contextMappings` | [Context Mapping[]](./connect_responses_context_mapping.htm.md) | List of context mappings. | Small, 59.0 | 59.0 |
| `contextNodes` | [Context Node[]](./connect_responses_context_node.htm.md) | List of context nodes. | Small, 59.0 | 59.0 |
| `endDate` | String | End date till context definition version is valid. | Small, 59.0 | 59.0 |
| `isActive` | Boolean | Specifies if the context definition version is active (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isEditable` | Boolean | Specifies if the context definition version is editable (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `startDate` | String | Start date from when context definition version is valid. | Small, 59.0 | 59.0 |
| `versionNumber` | Integer | Version number. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_error.htm ===
---
page_id: connect_responses_context_error.htm
title: Context Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_error.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Error Response

Output representation of context error.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code for the context error. | Small, 59.0 | 59.0 |
| `errorMessage` | String | Error message for the context error. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_info.htm ===
---
page_id: connect_responses_context_info.htm
title: Context Information
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_info.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Information

Output representation containing detailed information about a context.

      
        
          

**Sample Response**

          
: 
            

```
{
  "childBusinessObjectTypes": [
    "Order"
  ],
  "contextDefinitionId": "11Oxx0000006VjNEAU",
  "contextId": "3729ed60-d16d-41b8-8951-9ad4f6407ad2",
  "contextMappingId": "11jxx0000004Q83AAE",
  "isSuccess": true
}
```

          

        
      

              

              

              

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `childBusinessObjectTypes` | String[] | List of associated child business object types. | Small, 59.0 | 59.0 |
| `contextDefinitionId` | String | ID of the context definition record. | Small, 59.0 | 59.0 |
| `contextId` | String | Unique ID of the context. | Small, 59.0 | 59.0 |
| `contextMappingId` | String | Identifier for the context's mapping structure. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the request was successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_mapping.htm ===
---
page_id: connect_responses_context_mapping.htm
title: Context Mapping Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mapping Output

Output representation of context mapping.

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionVersionID` | String | ID of the context definition version. | Small, 59.0 | 59.0 |
| `contextMappingID` | String | ID of the context mapping. | Small, 59.0 | 59.0 |
| `contextNodeMappings` | [Context Node Mapping](./connect_responses_context_node_mapping.htm.md)[] | List of context node mappings. | Small, 59.0 | 59.0 |
| `description` | String | Description of context mapping. | Small, 59.0 | 59.0 |
| `isDefault` | Boolean | Specifies if you want to make it the default mapping for context definition (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isInputMapped` | Boolean | Indicates whether the specified context mapping details are mapped with the source (`true`) or not (`false`). | Small, 61.0 | 61.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `intents` | List<String> | Context mapping that’s associated with the usage of the `intents`. | Small, 61.0 | 61.0 |
| `mappedContext​DefinitionName` | String | API name of the context definition when context-to-context mappings exist. | Small, 61.0 | 61.0 |
| `name` | String | Name of the context mapping. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_mapping_list.htm ===
---
page_id: connect_responses_context_mapping_list.htm
title: Context Mapping List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_mapping_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mapping List Output

Output representation
    of
    a
    list of context mappings.

      
        
          

**Sample Response**

          
: 
            

```
{
  "contextMappingListId": "915c3ffc-65e6-47fd-b9c1-3fdfa92421c1",
  "contextMappings": [
    {
      "contextDefinitionVersionId": "11pxx0000004UcCAAU",
      "contextMappingId": "11jxx0000004LYBAA2",
      "contextNodeMappings": [],
      "description": "mappingDescription",
      "intents": [
        "ASSOCIATION",
        "HYDRATION",
        "PERSISTENCE",
        "TRANSLATION"
      ],
      "isDefault": false,
      "isInputMapped": false,
      "name": "mappingName"
    }
  ],
  "isSuccess": true
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextMappingListId` | String | Unique ID of the context mapping list. | Small, 59.0 | 59.0 |
| `contextMappings` | [Context Mapping Output[]](./connect_responses_context_mapping.htm.md) | List of context mappings. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_node.htm ===
---
page_id: connect_responses_context_node.htm
title: Context Node
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_node.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node

Output representation of the details of context nodes.

      
        
          

**JSON Example**

          
: 
            

```
{
  "contextNodes": [
    {
      "attributes": [],
      "baseReference": "11oxx000001G1DTPP88",
      "canonicalNodeId": "11oxx000001G1CGAA0",
      "childNodes": [],
      "contextDefinitionVersionId": "11pxx0000004UvYAAU",
      "contextNodeId": "11oxx000001G3xEAAS",
      "displayName": "Mobile_Contact_AccountSibRef",
      "isSuccess": true,
      "isTransposable": false,
      "name": "Mobile_Contact_AccountSibRef",
      "parentNodeId": "11oxx000001G1AeAAK",
      "tags": []
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Context Attribute List](./connect_responses_context_attribute_list.htm.md)[] | List of attributes. | Small, 59.0 | 59.0 |
| `baseReference` | String | Identifies the context node ID of the parent context definition that this context node is inherited from. | Small, 60.0 | 60.0 |
| `canonicalNodeId` | String | ID of the canonical node that’s used as a reference to create this context node. | Small, 61.0 | 61.0 |
| `childNodes` | [Context Node Output](#)[] | List of child context nodes. | Small, 59.0 | 59.0 |
| `contextDefinition​VersionID` | String | ID of context definition version. | Small, 59.0 | 59.0 |
| `contextNodeID` | String | ID of this context node. | Small, 59.0 | 59.0 |
| `displayName` | String | Name of the context node that appears on the UI. | Small, 61.0 | 61.0 |
| `isSuccess` | Boolean | Specifies if the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `isTransposable` | Boolean | Specifies if the context node is used for the transposable feature (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `name` | String | Name of the context node. | Small, 59.0 | 59.0 |
| `parentNodeId` | String | ID of (parent) context node. | Small, 59.0 | 59.0 |
| `tags` | [Context Attribute Tag Output](./connect_responses_context_attribute_tag.htm.md)[] | List of tags. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_node_list.htm ===
---
page_id: connect_responses_context_node_list.htm
title: Context Node List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_node_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node List

Output representation of the list of context nodes.

    
      
        
          

**JSON Example**

          
: 
            

```
{
  "contextNodeListId": "ebaf2554-88f2-4cb2-8418-cd3c250a9535",
  "contextNodes": [
    {
      "attributes": [
        {
          "attributeTags": [],
          "contextAttributeId": "11nxx000001hJm5AAE",
          "dataType": "REFERENCE",
          "domainSet": "Contact_AccountSibRef",
          "fieldType": "INPUT",
          "isKey": false,
          "isValue": false,
          "name": "ParentReference",
          "parentNodeId": "11oxx000001G3xEAAS"
        }
      ],
      "canonicalNodeId": "11oxx000001G1CGAA0",
      "childNodes": [],
      "contextDefinitionVersionId": "11pxx0000004UvYAAU",
      "contextNodeId": "11oxx000001G3xEAAS",
      "displayName": "Mobile_Contact_AccountSibRef",
      "isTransposable": false,
      "name": "Mobile_Contact_AccountSibRef",
      "parentNodeId": "11oxx000001G1AeAAK",
      "tags": []
    }
  ],
  "isSuccess": true
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextNode​ListId` | String | Unique ID of the context node list, which is required for Salesforce Lightning Design System (LDS). | Small, 59.0 | 59.0 |
| `contextNodes` | [Context Node []](./connect_responses_context_node.htm.md) | List of context nodes. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_node_mapping.htm ===
---
page_id: connect_responses_context_node_mapping.htm
title: Context Node Mapping Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_node_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Mapping Output

Output representation of the context node mapping.

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributeMappings` | [Context Attribute Mapping](./connect_responses_context_attribute_mapping.htm.md)[] | List of the context attribute mappings. | Small, 59.0 | 59.0 |
| `contextMappingID` | String | ID of the context mapping. | Small, 59.0 | 59.0 |
| `contextNodeID` | String | ID of the context node. | Small, 59.0 | 59.0 |
| `contextNodeMappingID` | String | ID of this context node mapping. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `mappedContext​NodeId` | String | Node ID in the source context definition. | Small, 61.0 | 61.0 |
| `sObjectName` | String | SObject name. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_node_mapping_list.htm ===
---
page_id: connect_responses_context_node_mapping_list.htm
title: Context Node Mapping List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_node_mapping_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Mapping List Output

Output representation of list of context node mappings.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextNodeMappingListId` | String | Unique ID. Required for LDS. | Small, 59.0 | 59.0 |
| `contextNodeMappings` | [Context Node Mapping Output[]](./connect_responses_context_node_mapping.htm.md) | List of context node mappings | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Specifies if the operation is success (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_output.htm ===
---
page_id: connect_responses_context_output.htm
title: Context Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Output

Output Representation of attributes associated with defined context.

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `isSuccess` | Boolean | Indicates whether the attributes update is successful `(true)` or not `(false)`. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_query_record.htm ===
---
page_id: connect_responses_context_query_record.htm
title: Context Query Record
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_query_record.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Query Record

Output representation of context query record, including primary and associated child
    records.

      
        
          

**Sample Response**

          
: 
            

```
{
   "childQueryRecords":[
      {
         "childQueryRecords":[
            
         ],
         "record":{
            "attributesAndValues":{
               "Name":"Acme Corp",
               "BillingAddress":"{city:New York,country:USA,geocodeAccuracy:null,latitude:null,longitude:null,postalCode:31349,state:NY,street:10 Main Rd.}",
               "Industry":"Manufacturing",
               "Type":"Prospect"
            },
            "businessObjectType":"Account",
            "childBusinessObjectTypes":[
               "OpportunityItem",
               "OrderItem"
            ],
            "contextDataRecordId":"003xx000004WhFsAAK",
            "currentState":"CREATED",
            "lastUpdatedTimeStamp":"2023-10-11 04:46:13.804"
         }
      }
   ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `childQueryRecords` | [Context Query Record](#connect_responses_context_query_record) | List of child query records derived from the main context query. | Small, 59.0 | 59.0 |
| `record` | [Context Data Record](./connect_responses_context_data_record.htm.md) | The context data record obtained from the query. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_tag_data.htm ===
---
page_id: connect_responses_context_tag_data.htm
title: Context Tag Data
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_tag_data.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag Data

Output representation of context tag data.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dataPath` | String[] | The path in the context data structure to the tag's location. | Small, 59.0 | 59.0 |
| `tagValue` | [Object](./connect_responses_query_tags.htm.md) | The value of the tag, which can be nested if the tag corresponds to an object with multiple attributes. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_context_tag_data_leaner.htm ===
---
page_id: connect_responses_context_tag_data_leaner.htm
title: Context Tag Data Leaner
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_tag_data_leaner.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag Data Leaner

Output representation of the leaner context tag data. It stores only the metadata
    required to reconstruct tag values and the index references instead of full path
    strings.

        
          

**JSON example**

          
: 
            

```
{
  "nodeLevelTag": false,
  "recordIdIndexesForPath": [
    0,
    2
  ],
  "tagValue": "Blue"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `nodeLevel​Tag` | Boolean | Indicates whether the tag is at node level (`true`) or not. (`false`) | Small, 66.0 | 66.0 |
| `recordId​IndexesForPath` | Integer[] | List of integer indexes referencing the recordIds array to reconstruct the data path.For example, if `recordIds` is ["r4", "r2", "r10", "r1"] and `recordIdIndexesForPath` is [3, 1], the reconstructed path would be contextId/r1/r2 (where r1 is at index 3 and r2 is at index 1). | Small, 66.0 | 66.0 |
| `tagValue` | Object | Value of the tag. For attribute-level tags, this is a primitive value. For node-level tags, this is a map containing nested tag data. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_context_tag_list.htm ===
---
page_id: connect_responses_context_tag_list.htm
title: Context Tag List Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_tag_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag List Output

Output representation of list of context tags.

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDefinitionId` | String | ID of the context definition created. | Small, 59.0 | 59.0 |
| `contextTagListId` | String | Unique ID. Required for LDS. | Small, 59.0 | 59.0 |
| `contextTags` | [Context Attribute Tag Output](./connect_responses_context_attribute_tag.htm.md)[] | List of context tags. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_leaner_query_tags_result.htm ===
---
page_id: connect_responses_leaner_query_tags_result.htm
title: Leaner Query Tags Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_leaner_query_tags_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Leaner Query Tags Result

Output representation of the leaner query tags result. The result includes compact tag
    data mapped to tag names and a shared list of record IDs.

        
          

**JSON example**

          
: 
            

```
{
  "contextId": "0000000s07fm061002917633740427233ff03037a8fe48048696667781ec824c",
  "isSuccess": true,
  "errorMessage": null,
  "recordIds": [
    "001xx000003GYiBAAW",
    "003xx000004WhFpAAK",
    "003xx000004WhFqAAK",
    "003xx000004WhFoAAK"
  ],
  "queryResultLeanerRepresentation": {
    "Contact_FirstName": [
      {
        "nodeLevelTag": false,
        "recordIdIndexesForPath": [
          0,
          1
        ],
        "tagValue": "Carole"
      },
      {
        "nodeLevelTag": false,
        "recordIdIndexesForPath": [
          0,
          2
        ],
        "tagValue": "Jon"
      },
      {
        "nodeLevelTag": false,
        "recordIdIndexesForPath": [
          0,
          3
        ],
        "tagValue": "Geoff"
      }
    ]
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of context to be queried. | Small, 66.0 | 66.0 |
| `errorMessage` | String | Error message when `isSuccess` is false. | Small, 66.0 | 66.0 |
| `isSuccess` | Boolean | Indicates whether the query was successful (`true`) or not (`true`). | Small, 66.0 | 66.0 |
| `queryResult​LeanerRepresentation` | [Context Tag Data Leaner](./connect_responses_context_tag_data_leaner.htm.md) | Map of tag name and list of lean tag data. Each entry contains tag values and compact indexes for record path construction. | Small, 66.0 | 66.0 |
| `recordIds` | String[] | List of all record IDs present in the context that are included in the tag result. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_mapped_attribute_data_type_info.htm ===
---
page_id: connect_responses_mapped_attribute_data_type_info.htm
title: Mapped Attribute Data Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_mapped_attribute_data_type_info.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Mapped Attribute Data Type

Output representation of the context attribute mapping data type information.

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dataType` | String | Data type of attribute mapped field. | Small, 59.0 | 59.0 |
| `supportedPicklistValues` | String[] | Supported picklist values of attribute mapped field. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_persist_context_output.htm ===
---
page_id: connect_responses_persist_context_output.htm
title: Persist Context Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_persist_context_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Persist Context Output

Output Representation to persist context data.

      
        
          

**Sample Response**

          
: 
            

```
{
  "referenceId": "95Txx0000004CCG"
}

```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `referenceId` | String | The reference ID that maps to the response. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_query_context_record_result.htm ===
---
page_id: connect_responses_query_context_record_result.htm
title: Query Context Record Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_query_context_record_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Context Record Result

Output representation of query result context record.

      
        
          

**Sample Response**

          
: 
            

```
{
   "contextId":"7bc695bc-f38b-4a94-8a95-0caa50f3da53",
   "isDone":true,
   "isSuccess":true,
   "queryRecords":[
      {
         "childQueryRecords":[
            
         ],
         "record":{
            "attributesAndValues":{
               "Name":"Acme Corp",
               "BillingAddress":"{city:New York,country:USA,geocodeAccuracy:null,latitude:null,longitude:null,postalCode:31349,state:NY,street:10 Main Rd.}",
               "Industry":"Manufacturing",
               "Type":"Prospect"
            },
            "businessObjectType":"Account",
            "childBusinessObjectTypes":[
               "OpportunityItem",
               "OrderItem"
            ],
            "contextDataRecordId":"003xx000004WhFsAAK",
            "currentState":"CREATED",
            "lastUpdatedTimeStamp":"2023-10-11 04:46:13.804"
         }
      }
   ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID for the context record that is queried. | Small, 59.0 | 59.0 |
| `isDone` | Boolean | Indicates whether the query operation is complete `(true)` or not `(false)`. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the status of query is successful `(true)` or not `(false)`. | Small, 59.0 | 59.0 |
| `queryRecords` | [Context Query Record](./connect_responses_context_query_record.htm.md)[] | List of the retrieved context query records. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_query_record_status_result.htm ===
---
page_id: connect_responses_query_record_status_result.htm
title: Query Record Status Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_query_record_status_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Record Status Result

Output representation of query result status of context data records. 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextRecordStatusListId` | String | Unique ID associated with the list of context record status required for Lightning Data Service. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the status retrieval of context data query records was successful `(true)` or not `(false)`. | Small, 59.0 | 59.0 |
| `queryResult` | [Context Data Record Status](./connect_responses_context_data_record_status.htm.md)[] | List containing the status of the queried context data records. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_query_tags.htm ===
---
page_id: connect_responses_query_tags.htm
title: Query Tags
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_query_tags.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Tags

Output representation of query tags result.

        
            
                
                    

**Sample Response**

                    
: 
                        

```
{
                "tagValue": {
                    "Industry": {
                        "contextDataPathBuilder": {
                            "pathTokens": [
                                "6ba44bdce01b138f7cfdf9c7ab414312bf76f4b75362e47adb6ab368714fb5bf",
                                "001SB00000M9i21YAB"
                            ]
                        },
                        "dmlStatus": "CREATED",
                        "nodeLevelTag": false,
                        "tagPath": {
                            "pathTokens": []
}
```

                    

                
            

            

                    
                    
                    
                    
                    
                    
                        
                            

                            

                            

                            

                            

                        

                    

                    
                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                    

                
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDataPathBuilder` | Map<String, Object> | Indicates whether the query operation is complete | Small, 59.0 | 59.0 |
| `pathTokens` | String [] | List of paths indicating the tag data path. | Small, 59.0 | 59.0 |
| `dmlStatus` | String | DML status of the tag value. | Small, 59.0 | 59.0 |
| `nodeLevelTag` | Boolean | Indicates if the tag is at the node level `true`) or not (`false`. | Small, 59.0 | 59.0 |
| `tagPath` | Map<String, Object> | The path to the tag containing a list of paths indicating the tag path. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_query_tags_result.htm ===
---
page_id: connect_responses_query_tags_result.htm
title: Query Tags Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_query_tags_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Query Tags Result

Output representation of the results when querying context tags.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `isDone` | Boolean | Indicates whether the tag query process is complete `(true)` or not `(false)`. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates if the query was successful `(true)` or not `(false)`. | Small, 59.0 | 59.0 |
| `queryResult` | [Map<String, ContextTagDataRepresentation>>](./connect_responses_context_tag_data.htm.md) | Contains a mapping of each queried tag to its results. | Small, 59.0 | 59.0 |

=== ARTICLE: context_attribute_management.htm ===
---
page_id: context_attribute_management.htm
title: Context Attribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_attribute_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Attribute

 Create new attributes, update existing ones, retrieve or query attribute details,
        and delete attributes.

- 
**[Context Attribute (POST, PATCH)](./connect_resources_context_attribute.htm.md)**  

Create a list of context attributes.

- 
**[Context Attribute ID (GET, DELETE)](./connect_resources_context_attribute_id.htm.md)**  

Query and delete a context attribute using an ID.

- 
**[Context Attribute Mapping (POST, PATCH)](./connect_resources_attribute_mapping.htm.md)**  

Create context attribute mapping. Update context attribute mapping.

=== ARTICLE: context_mapping_management.htm ===
---
page_id: context_mapping_management.htm
title: Context Mapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_mapping_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Mapping

 Create new context mappings, update existing mappings, retrieve or query mapping
        details, and delete mappings.

- 
**[Context Mapping (POST, PATCH)](./connect_resources_context_mapping.htm.md)**  

Create and update context mappings.

- 
**[Context Mapping Id (GET, DELETE)](./connect_resources_context_mapping_id.htm.md)**  

Query and delete a context mapping using an Id.

- 
**[Context Attribute Mapping ID (GET, DELETE)](./connect_resources_context_attribute_mapping_id.htm.md)**  

Query and delete a context attribute mapping using an ID.

=== ARTICLE: context_node_management.htm ===
---
page_id: context_node_management.htm
title: Context Node
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_node_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node

 Create new nodes, update existing nodes, retrieve or query node details, and delete
        nodes.

- 
**[Context Node (POST, PATCH)](./connect_resources_context_node.htm.md)**  

Create and update context node.

- 
**[Context Node Id (GET, DELETE)](./connect_resources_context_node_id.htm.md)**  

Query and delete a context node using an Id.

=== ARTICLE: context_node_mapping_management.htm ===
---
page_id: context_node_mapping_management.htm
title: Context Node Mapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_node_mapping_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Mapping

 Create new node mappings, update existing ones, retrieve or query mapping details,
        and delete node mappings.

- 
**[Context Node Mapping Id (GET, DELETE)](./connect_resources_context_node_mapping_id.htm.md)**  

Query and delete a context node mapping using an ID.

- 
**[Context Node Mapping (POST, PATCH)](./connect_resources_node_mapping.htm.md)**  

Create and update context node mappings.

- 
**[Context Node Relationship (POST)](./connect_resources_configure_relationship_node.htm.md)**  

Configure a relationship node by adding child context nodes to a specific context     node.

=== ARTICLE: context_service_apex_reference.htm ===
---
page_id: context_service_apex_reference.htm
title: Context Service Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Apex Reference

Use the built-in Apex class to manage the processes of a context
      service.

- 
**[Context Namespace](./apex_namespace_Context.htm.md)**  

The `Context` namespace provides classes and methods to     manage the sharing and consumption of business application data by using Context     Service.

=== ARTICLE: context_service_apis.htm ===
---
page_id: context_service_apis.htm
title: Context Service Business REST APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Business REST APIs

Context Service Business APIs are RESTful APIs that are sometimes
         available as Apex classes and methods. You can access the Context Service APIs using
      REST endpoints. These REST APIs follow similar conventions as Connect REST APIs.

      
         

To understand the architecture, authentication, rate limits, and how the requests and
            responses work, see [Connect REST API Developer
               Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm).

      

   

- 
**[Resources](./context_service_apis_resources.htm.md)**  

Here’s a list of Context Service API resources.

- 
**[Request Bodies](./context_service_apis_requests.htm.md)**  

Here’s a list of Context Service API request bodies.

- 
**[Response Bodies](./context_service_apis_responses.htm.md)**  

Here’s a list of Context Service response bodies.

#### See Also

- [*Connect REST API Developer Guide*: Connect REST API Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: context_service_apis_requests.htm ===
---
page_id: context_service_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Here’s a list of Context Service API request bodies.

- 
**[Context Attribute Mappings Input](./connect_requests_context_attribute_mappings_input.htm.md)**  

Input representation of context attribute mapping.

- 
**[Context Attribute Hydration Details Input](./connect_requests_context_attr_hydration_details_input.htm.md)**  

Input representation of context attribute hydration detail.

- 
**[Context Attributes Input](./connect_requests_context_attributes_input.htm.md)**  

Input representation of context attribute.

- 
**[Context Definition Input](./connect_requests_context_definitions_input.htm.md)**  

Input representation of the context definition.

- 
**[Context Definition Upgrade Input](./connect_requests_context_definition_upgrade.htm.md)**  

Input representation of context definition upgrade.

- 
**[Context Definition Filter Input](./connect_requests_context_definition_filter_input.htm.md)**  

Input representation details of context definition filter.

- 
**[Context Definition Filter List Input](./connect_requests_context_definition_filter_list_input.htm.md)**  

Input representation for a list of Context Definition Filters

- 
**[Context Input](./connect_requests_context_input.htm.md)**  

Input representation for defining a context.

- 
**[Context Mappings Input](./connect_requests_context_mappings_input.htm.md)**  

Input representation of context mapping.

- 
**[Context Metadata Input](./connect_requests_context_meta_data_input.htm.md)**  

Input representation of context metadata.

- 
**[Context Node ID Input](./connect_requests_context_node_id_input.htm.md)**  

Input representation of the list of context node IDs to create the relationship nodes     for.

- 
**[Context Node Mapping Id (GET, DELETE)](./connect_resources_context_node_mapping_id.htm.md)**  

Query and delete a context node mapping using an ID.

- 
**[Context Nodes Input](./connect_requests_context_nodes_input.htm.md)**  

Input representation of context node.

- 
**[Context Tag Input](./connect_requests_context_tag_input.htm.md)**  

Input representation of the context tag.

- 
**[Context Query Tags Leaner (POST)](./connect_resources_context_query_lean_tag.htm.md)**  

Query tags and return a memory-optimized (leaner) result suitable for Apex and low-heap     clients. Eliminate redundant metadata to reduce heap usage and payload size.

- 
**[Node Path and Tag Values Input](./connect_requests_node_path_and_tag_values.htm.md)**  

Input representation of the node path which needs to update with tag         details.

- 
**[Query Context Record Input](./connect_requests_query_context_record_input.htm.md)**  

Input representation of query context record.

- 
**[Query Record Status Input](./connect_requests_query_data_input.htm.md)**  

Input representation of status and related error messages of query data     records.

- 
**[Tag Values Input](./connect_requests_tag_values_input.htm.md)**  

Input representation of the list of Tag Names to be updated and their         values.

=== ARTICLE: context_service_apis_resources.htm ===
---
page_id: context_service_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Context Service API resources.

- 
**[Context Definition](./context_service_context_definition_management.htm.md)**  

 Create a context definition, clone an existing context definition, extend a standard         definition (file based definition) or persist entire context definition.

- 
**[Context Node](./context_node_management.htm.md)**  

 Create new nodes, update existing nodes, retrieve or query node details, and delete         nodes.

- 
**[Context Attribute](./context_attribute_management.htm.md)**  

 Create new attributes, update existing ones, retrieve or query attribute details,         and delete attributes.

- 
**[Context Tag](./context_tag_managament.htm.md)**  

Create tags for attributes or nodes, update existing context tags, retrieve or query         specific tags, list all context tags, and delete tags.

- 
**[Context Node Mapping](./context_node_mapping_management.htm.md)**  

 Create new node mappings, update existing ones, retrieve or query mapping details,         and delete node mappings.

- 
**[Context Mapping](./context_mapping_management.htm.md)**  

 Create new context mappings, update existing mappings, retrieve or query mapping         details, and delete mappings.

- 
**[Context Service Runtime](./runtime_context_intance_management.htm.md)**  

Create new runtime context instances, query data from context instances, and delete         context instances.

- 
**[Context Persistence](./persistence_context_management.htm.md)**  

Persist context data to Salesforce database entities.

- 
**[Context Query Tags Leaner (POST)](./connect_resources_context_query_lean_tag.htm.md)**  

Query tags and return a memory-optimized (leaner) result suitable for Apex and low-heap     clients. Eliminate redundant metadata to reduce heap usage and payload size.

=== ARTICLE: context_service_apis_responses.htm ===
---
page_id: context_service_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Context Service response bodies.

- 
**[Context Attribute Output](./connect_responses_context_attribute.htm.md)**  

Output representation of the context attribute.

- 
**[Context Attribute Mapping](./connect_responses_context_attribute_mapping.htm.md)**  

Output representation of the context attribute mapping.

- 
**[Context Attribute Mapping List](./connect_responses_context_attribute_mapping_list.htm.md)**  

Output representation of list of context attribute mappings.

- 
**[Context Attribute Hydration Detail](./connect_responses_context_attr_hydration_detail.htm.md)**  

Output representation of context attribute hydration detail.

- 
**[Context Attribute Tag Output](./connect_responses_context_attribute_tag.htm.md)**  

Output representation of context attribute tag.

- 
**[Context Attribute List Output](./connect_responses_context_attribute_list.htm.md)**  

Output representation of list of context attributes.

- 
**[Context Data Record](./connect_responses_context_data_record.htm.md)**  

Output representation of context data record, including its attributes, type, associated     child objects, and other relevant metadata.

- 
**[Context Data Record Status](./connect_responses_context_data_record_status.htm.md)**  

Output representation of context data record status.

- 
**[Context Definition Filter](./connect_responses_context_definition_filter.htm.md)**  

Output representation details of a context definition filter.

- 
**[Context Definition Filter List](./connect_responses_context_definition_filter_list.htm.md)**  

Output representation details of context definition filter list.

- 
**[Context Definition Information](./connect_responses_context_definition_info.htm.md)**  

Output representation of context definition information.

- 
**[Context Definition Interface](./connect_responses_context_definition_interface.htm.md)**  

Output representation of the details of the context definition interface.

- 
**[Context Definition Interface Attribute Tag](./connect_responses_context_definition_interface_attribute_tag.htm.md)**  

Output representation of the attribute tags associated with the context definition     interface.

- 
**[Context Definition Interface Metadata](./connect_responses_context_definition_interface_metadata.htm.md)**  

Output representation of the metadata associated with the context definition     interface.

- 
**[Context Definition Interface Metadata List](./connect_responses_context_definition_interface_metadata_list.htm.md)**  

Output representation of the metadata list associated with the context definition     interfaces.

- 
**[Context Definition Interface Node Tag](./connect_responses_context_definition_interface_node_tag.htm.md)**  

Output representation of the tags associated with the context definition     interface.

- 
**[Context Definition Output](./connect_responses_context_definition.htm.md)**  

Output representation of context definition.

- 
**[Context Definition List](./connect_responses_context_definition_list.htm.md)**  

Output representation of list of context definitions.

- 
**[Context Definition Version](./connect_responses_context_definition_version.htm.md)**  

Output representation of context definition version.

- 
**[Context Definition Reference](./connect_responses_context_definition_reference.htm.md)**  

Output representation of context definition reference.

- 
**[Context Error Response](./connect_responses_context_error.htm.md)**  

Output representation of context error.

- 
**[Context Information](./connect_responses_context_info.htm.md)**  

Output representation containing detailed information about a context.

- 
**[Context Mapping Output](./connect_responses_context_mapping.htm.md)**  

Output representation of context mapping.

- 
**[Context Mapping List Output](./connect_responses_context_mapping_list.htm.md)**  

Output representation     of     a     list of context mappings.

- 
**[Context Node Mapping Output](./connect_responses_context_node_mapping.htm.md)**  

Output representation of the context node mapping.

- 
**[Context Node Mapping List Output](./connect_responses_context_node_mapping_list.htm.md)**  

Output representation of list of context node mappings.

- 
**[Context Node List](./connect_responses_context_node_list.htm.md)**  

Output representation of the list of context nodes.

- 
**[Context Node](./connect_responses_context_node.htm.md)**  

Output representation of the details of context nodes.

- 
**[Context Output](./connect_responses_context_output.htm.md)**  

Output Representation of attributes associated with defined context.

- 
**[Context Query Record](./connect_responses_context_query_record.htm.md)**  

Output representation of context query record, including primary and associated child     records.

- 
**[Context Tag Data](./connect_responses_context_tag_data.htm.md)**  

Output representation of context tag data.

- 
**[Context Tag Data Leaner](./connect_responses_context_tag_data_leaner.htm.md)**  

Output representation of the leaner context tag data. It stores only the metadata     required to reconstruct tag values and the index references instead of full path     strings.

- 
**[Context Tag List Output](./connect_responses_context_tag_list.htm.md)**  

Output representation of list of context tags.

- 
**[Leaner Query Tags Result](./connect_responses_leaner_query_tags_result.htm.md)**  

Output representation of the leaner query tags result. The result includes compact tag     data mapped to tag names and a shared list of record IDs.

- 
**[Mapped Attribute Data Type](./connect_responses_mapped_attribute_data_type_info.htm.md)**  

Output representation of the context attribute mapping data type information.

- 
**[Persist Context Output](./connect_responses_persist_context_output.htm.md)**  

Output Representation to persist context data.

- 
**[Query Context Record Result](./connect_responses_query_context_record_result.htm.md)**  

Output representation of query result context record.

- 
**[Query Record Status Result](./connect_responses_query_record_status_result.htm.md)**  

Output representation of query result status of context data records. 

- 
**[Query Tags](./connect_responses_query_tags.htm.md)**  

Output representation of query tags result.

- 
**[Query Tags Result](./connect_responses_query_tags_result.htm.md)**  

Output representation of the results when querying context tags.

=== ARTICLE: context_service_context_definition_management.htm ===
---
page_id: context_service_context_definition_management.htm
title: Context Definition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_context_definition_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition

 Create a context definition, clone an existing context definition, extend a standard
        definition (file based definition) or persist entire context definition.

- 
**[Context Definition (GET, POST)](./connect_resources_context_definition.htm.md)**  

Create a context definition, clone an existing context definition, extend a standard     definition (file based definition) or to persist entire context definition.

- 
**[Context Definition Id (GET, PATCH, DELETE)](./connect_resources_context_definition_id.htm.md)**  

Query, update, and delete a context definition using an ID.

- 
**[Context Definition Upgrade (PATCH)](./connect_resources_context_definition_upgrades.htm.md)**  

Upgrade a context definition. Once an extended definition is created from a base         standard definition, use this API to reflect any updates made to the base standard         definition in the extended definition.

- 
**[Context Definition Filters (GET, POST)](./connect_resources_context_definition_filters.htm.md)**  

Create or get context filters associated with a specific context definition. Context     filters are criteria or conditions that refine or limit data operations based on specific     parameters.

- 
**[Context Definition Filter By ID (DELETE, GET, PATCH)](./connect_resources_context_definition_filter_by_id.htm.md)**  

Get, update, or delete a context definition filter for a specified context definition     filter ID.

=== ARTICLE: context_service_flow_metadata_api.htm ===
---
page_id: context_service_flow_metadata_api.htm
title: Flow for Context Service
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Context Service

Represents the metadata associated with a flow. Use a flow to create an application
    that takes users through a series of pages to query and update records in the database. You can
    also execute logic and provide branching capability based on user input to build dynamic
    applications.

    

## FlowActionCall

      
      

Context Service exposes additional actionType values for the FlowActionCall Metadata
        type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid value only for Context Service include: `deleteContextCache`—Deletes the context instance from the context cache using specified context ID. This value is available in API version 64.0 and later. `queryContextTags`—Queries context instance tags associated with a context definition. This value is available in API version 64.0 and later. `updateContextAttributes`—Updates attributes on the context instance using context tags. This value is available in API version 64.0 and later. |

=== ARTICLE: context_service_invocable_actions_parent.htm ===
---
page_id: context_service_invocable_actions_parent.htm
title: Context Service Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Standard Invocable Actions

Learn more about the standard invocable actions available with Context
    Service.

- 
**[Build Context Action](./actions_obj_build_context.htm.md)**  

Build and cache context data associated with a context definition.

- 
**[Delete Context Cache Action](./actions_obj_delete_context_cache.htm.md)**  

Delete the specified context instance from the in-memory context cache using the         provided context ID. This action removes the cached data maintained by the context cache         service without performing any database write operations.

- 
**[Delete Context Records Action](./actions_obj_delete_context_records.htm.md)**  

Deletes one or more records from a context instance.

- 
**[Persist Context Data Action](./actions_obj_persist_context_data.htm.md)**  

Store cached context data associated with a context mapping ID in a Salesforce         record.

- 
**[Query Context Tags Action](./actions_obj_query_context_tags.htm.md)**  

Query the tag values from an instance that are associated with a context         definition.

- 
**[Update Context Attributes Action](./actions_obj_update_context_attributes.htm.md)**  

Update the attributes in the context instance using tags.

=== ARTICLE: context_service_metadata_api_parent.htm ===
---
page_id: context_service_metadata_api_parent.htm
title: Context Service Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[ContextDefinition](./meta_contextdefinition.htm.md)**  

Represents the details of a context definition that 			describe the relationship between the node structures within a context.

- 
**[Flow for Context Service](./context_service_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. Use a flow to create an application     that takes users through a series of pages to query and update records in the database. You can     also execute logic and provide branching capability based on user input to build dynamic     applications.

=== ARTICLE: context_service_overview.htm ===
---
page_id: context_service_overview.htm
title: Context Service
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_overview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service

Simplify the sharing and consumption of business application data using Context Service.
  Acting as a generic module, Context Service forms a layer between applications and procedures,
  enabling easy retrieval and use of data across various industry clouds at every step of the
  process.

- 
**[Context Service Metadata API Types](./context_service_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Context Service Tooling API Objects](./context_service_tooling_api_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

- 
**[Context Persistence Platform Event](./contextpersistenceevent_platform_event.htm.md)**  

Use the ContextPersistence event to notify subscribers after a context persistence     event has completed its execution is processed.

- 
**[Context Service Standard Invocable Actions](./context_service_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Context     Service.

- 
**[Context Service Business REST APIs](./context_service_apis.htm.md)**  

Context Service Business APIs are RESTful APIs that are sometimes          available as Apex classes and methods. You can access the Context Service APIs using       REST endpoints. These REST APIs follow similar conventions as Connect REST APIs.

- 
**[Context Service Apex Reference](./context_service_apex_reference.htm.md)**  

Use the built-in Apex class to manage the processes of a context       service.

- 
**[Context Attribute Input](./connect_requests_context_attribute_input.htm.md)**  

Input representation for updating context attribute.

=== ARTICLE: context_service_tooling_api_parent.htm ===
---
page_id: context_service_tooling_api_parent.htm
title: Context Service Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_service_tooling_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

  

For more information about Tooling API objects and to find a complete reference of all the
   supported objects, see [Introducing Tooling
    API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

 

- 
**[ContextAttrHydrationDetail](./tooling_api_objects_contextattrhydrationdetail.htm.md)**  

       Represents the SOQL (database) queries that fetch data for a chosen attribute          from the input schema. This object is available in API version 59.0 and later. 

- 
**[ContextAttribute](./tooling_api_objects_contextattribute.htm.md)**  

       Represents information about an attribute used to describe a context node.          Each node can have one or many attributes associated with it.  This object is       available in API version 59.0 and later. 

- 
**[ContextAttributeMapping](./tooling_api_objects_contextattributemapping.htm.md)**  

       Represents the relationship between the attribute defined in the context and          the values in the related objects. This object is available in API version 59.0 and       later. 

- 
**[ContextDefinition](./tooling_api_objects_contextdefinition.htm.md)**  

       Represents information about a context definition. The context definition          describes the relationship between the node structures within a context. This object       is available in API version 59.0 and later. 

- 
**[ContextDefinitionReference](./tooling_api_objects_contextdefinitionreference.htm.md)**  

       Represents information about reference from one Context Definition to another          Context Definition.  This object is available in API version 60.0 and       later.

- 
**[ContextDefinitionSync](./tooling_api_objects_contextdefinitionsync.htm.md)**  

Stores information for the sync operation of the custom definition          with the standard definition. This object is available in API version 62.0 and       later.

- 
**[ContextDefinitionVersion](./tooling_api_objects_contextdefinitionversion.htm.md)**  

       Represents information about the context definition version. Only one version          can be active at a time. This object is available in API version 59.0 and later. 

- 
**[ContextMapping](./tooling_api_objects_contextmapping.htm.md)**  

       Represents the mapping of both attributes and nodes to related objects.       This object is available in API version 59.0 and later. 

- 
**[ContextMappingIntent](./tooling_api_objects_contextmappingintent.htm.md)**  

       Represents the purpose associated to a context mapping. This object is       available in API version 61.0 and later. 

- 
**[ContextNode](./tooling_api_objects_contextnode.htm.md)**  

       Represents information about the structure of the nodes within the context.          Within a structure, each node can have other nodes related to them and attributes to          describe the object. A hierarchy for the nodes can also be defined here. This object       is available in API version 59.0 and later. 

- 
**[ContextNodeAttrDictionary](./tooling_api_objects_contextnodeattrdictionary.htm.md)**  

Represents          the          relationship between          the          ContextNodeMapping and ContextDictionary          objects          as a junction table. This object is available in API version 62.0       and later.

- 
**[ContextNodeMapping](./tooling_api_objects_contextnodemapping.htm.md)**  

       Represents the relationship between the node in the context and values in the          input schema. This object is available in API version 59.0 and later. 

- 
**[ContextTag](./tooling_api_objects_contexttag.htm.md)**  

       Represents a shortened name of an attribute or node instead of its fully          qualified tag structure name. This object is available in API version 59.0 and later. 

- 
**[CtxAttrHydrationCtx](./tooling_api_objects_ctxattrhydrationctx.htm.md)**  

       Represents the queries that fetch the data for a chosen attribute from the          input schema for context-to-context mapping This object is available in API version       61.0 and later.

=== ARTICLE: context_tag_managament.htm ===
---
page_id: context_tag_managament.htm
title: Context Tag
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/context_tag_managament.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Tag

Create tags for attributes or nodes, update existing context tags, retrieve or query
        specific tags, list all context tags, and delete tags.

- 
**[Context Tag (GET, POST, PATCH)](./connect_resources_context_tag.htm.md)**  

Query, create, and update context tag.

- 
**[Context Tag ID (GET, DELETE)](./connect_resources_context_tag_id.htm.md)**  

Query and delete a context tag.

=== ARTICLE: contextpersistenceevent_platform_event.htm ===
---
page_id: contextpersistenceevent_platform_event.htm
title: Context Persistence Platform Event
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/contextpersistenceevent_platform_event.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Persistence Platform Event

Use the ContextPersistence event to notify subscribers after a context persistence
    event has completed its execution is processed.

    

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in Salesforce orgs when the admin settings for Context Service and for the product related to the use case are enabled. The Salesforce org must have the ContextService license. |

  

  

- 
**[ContextPersistenceEvent](./sforce_api_objects_contextpersistenceevent.htm.md)**  

Notifies subscribers when the Context Persistence event, initiated by the Context 		Persistence API has completed its execution. This event is designed to inform 		customers/clients about the success or failure of their Context Persistence request. This 		object is available in API version 59.0 and later.

=== ARTICLE: meta_contextdefinition.htm ===
---
page_id: meta_contextdefinition.htm
title: ContextDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_contextdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDefinition

Represents the details of a context definition that
			describe the relationship between the node structures within a context.

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type
			and inherits its fullName field. 

		

## File Suffix and Directory Location

			
			

ContextDefinition components have the suffix .contextDefinition
				and are stored in the contextDefinitions folder.

		

		

## Version

			
			

ContextDefinition components are available in API version 59.0 and later.

		

		

## Special Access Rules

			
			

Enable the organization preference ContextDefinitionsEnabled to access the
				ContextDefinition metadata type.

		

		

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

						

					

				
| Field Name | Description |
| --- | --- |
| canBeReferenceDefinition | **Field Type** boolean **Description** Indicates whether the context definition can be referred by other context definitions (`true`) or not (`false`). Available in API version 63.0 and later. The default value is `false`. |
| clonedFrom | **Field Type** string **Description** The name of the context definition that's used to clone the current context definition. |
| contextDefinitionReferences | **Field Type** [ContextDefinitionReference](#ContextDefinitionReference)[] **Description** References of the context definition. |
| contextDefinitionVersions | **Field Type** [ContextDefinitionVersion[]](#ContextDefinitionVersion) **Description** Version of the context definition. |
| contextTtl | **Field Type** int **Description** Duration to persist the data, which is loaded in the run-time context instances created by this context definition, in the cache. The default value is 10 minutes. |
| description | **Field Type** string **Description** Description of the context definition. |
| hasSystemTags | **Field Type** boolean **Description** Indicates whether the context definition has system tags (`true`) or not (`false`). Available in API version 63.0 and later. The default value is `false`. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context definition that's used to derive the current context definition. |
| inheritedFromVersion | **Field Type** string **Description** Version number of the parent definition that's used to derive the current context definition. |
| isProtected | **Field Type** boolean **Description** Auto-generated value that doesn’t impact the behavior of the metadata type. |
| masterLabel | **Field Type** string **Description** Required. User-friendly name for the context definition, which is defined when the context definition is created. |
| title | **Field Type** string **Description** Required. Name of the context definition. |

		

		

## ContextDefinitionReference

			
			

Represents details about the context definition reference.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| inheritedFrom | **Field Type** string **Description** ID of the parent context definition reference that's used to derive the current context definition reference. |
| referenceContextDefinition | **Field Type** string **Description** Required. ID or name of the referred context definition. |

		

		

## ContextDefinitionVersion

			
			

Represents details about the context definition version. Only one version can be
				active at a time.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

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
| contextMappings | **Field Type** [ContextMapping[]](#ContextMapping) **Description** Mapping of attributes and nodes to related objects. |
| contextNodes | **Field Type** [ContextNode[]](#ContextNode) **Description** Details of the structure of the nodes within the context. |
| endDate | **Field Type** string **Description** Date and time when the context definition version becomes inactive. |
| isActive | **Field Type** boolean **Description** Indicates whether the context definition version is active (`true`) or not (`false`). The default value is `false`. |
| startDate | **Field Type** string **Description** Required. Date and time when the context definition version becomes active. |
| versionNumber | **Field Type** int **Description** Required. Version number of the context definition. |

		

		

## ContextMapping

			
			

Represents the mapping of attributes and nodes to related objects.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

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
| contextMappingIntents | **Field Type** [ContextMappingIntent[]](#ContextMappingIntent) **Description** Purpose associated to a context mapping. |
| contextNodeMappings | **Field Type** [ContextNodeMapping[]](#ContextNodeMapping) **Description** Mapping of the node in the context and values in the input schema. |
| default | **Field Type** boolean **Description** Indicates whether the mapping for a context definition version is default (`true`) or not (`false`). The default value is `false`. |
| description | **Field Type** string **Description** Description of the context mapping. |
| inheritedFrom | **Field Type** string **Description** Name of the parent mapping that's used to derive the current mapping. |
| title | **Field Type** string **Description** Required. Name of the context mapping. |

		

		

## ContextMappingIntent

			
			

Represents the purpose associated to a context mapping.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

- 
- 
- 
- 

						

					

				
| Field Name | Description |
| --- | --- |
| mappingIntent | **Field Type** ContextMappingIntentType (enumeration of type string) **Description** Required. Specifies the purpose that's used to identify the type of context mapping required. Valid values are: `hydration` `association` `persistence` `translation` |

		

		

## ContextNodeMapping

			
			

Represents the relationship between the node in the context and values in the input
				schema.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

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
| contextAttributeMappings | **Field Type** [ContextAttributeMapping[]](#ContextAttributeMapping) **Description** Mapping of the attribute defined in the context and the values in the related objects. |
| contextNode | **Field Type** string **Description** Context node record associated with the context node mapping. |
| contextNodeAttrDictionaries | **Field Type** [ContextNodeAttrDictionary[]](#ContextNodeAttrDictionary) **Description** Facilitates relationships between context node mapping and context dictionary. Additionally, it records the relationship between context node and context dictionary. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context node mapping that's used to derive the current context node mapping. |
| mappedContextDefinition | **Field Type** string **Description** API name of the context definition for existing context-to-context mappings. |
| object | **Field Type** string **Description** Name of the object used for the mapping. |

		

		

## ContextAttributeMapping

			
			

Represents the relationship between the attributes defined in the context and the
				values in the related objects.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

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
| contextAttrHydrationDetails | **Field Type** [ContextAttrHydrationDetail[]](#ContextAttrHydrationDetail) **Description** Details of the SOQL (database) queries that fetch data for a chosen attribute from the input schema. |
| contextAttribute | **Field Type** string **Description** Context attribute record associated with the context attribute mapping. |
| contextInputAttributeName | **Field Type** string **Description** Required. Name of the input attribute. |
| ctxAttrHydrationCtxs | **Field Type** [CtxAttrHydrationCtx[]](#CtxAttrHydrationCtx) **Description** Query that fetches data for a chosen attribute from the input schema for context-to-context mapping. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context attribute mapping that's used to derive the current context attribute mapping. |

		

		

## ContextAttrHydrationDetail

			
			

Represents the SOQL (database) queries that fetch data for a chosen attribute from
				the input schema.

			

					
					
					
						
							

							

						

					

					
						
							

							

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
| contextAttrHydrationDetails | **Field Type** [ContextAttrHydrationDetail[]](#ContextAttrHydrationDetail) **Description** Details of the query that fetches the data for the specific query attribute. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context attribute hydration detail that's used to derive the current context attribute hydration detail. |
| objectName | **Field Type** string **Description** Required. Name of the object used for the attribute hydration detail. |
| queryAttribute | **Field Type** string **Description** Required. The SOQL query that is the source of the hydration. |

		

		

## CtxAttrHydrationCtx

			
			

Represents the queries that fetch data for a chosen attribute from the input schema
				for context-to-context mapping.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| contextQueryAttribute | **Field Type** string **Description** Required. Attribute in context definition that's the source of context hydration. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context attribute hydration detail that's used to derive the current context attribute. |

		

		

## ContextNodeAttrDictionary

			
			

Represents the relationship between a context node and the context attribute
				dictionary.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| contextAttrDictIdentifier | **Field Type** string **Description** Required. Developer name of the context attribute dictionary. |
| contextNodeTagPrefix | **Field Type** string **Description** Required. Tag prefix of the context node that's used to create the unique identifier of the parent context node. |

		

		

## ContextNode

			
			

Represents details of the structure of the nodes within the context. Each node can
				have other nodes related to them and attributes to describe the object. You can also
				define a hierarchy for the nodes.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
						
							

							

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
| canonicalNode | **Field Type** string **Description** Canonical node that's associated with the context node. |
| contextAttributes | **Field Type** [ContextAttribute[]](#ContextAttribute) **Description** Details of the attribute used to describe the context node. |
| contextNodeAttrDictionaries | **Field Type** [ContextNodeAttrDictionary[]](#ContextNodeAttrDictionary) **Description** Facilitates relationships between context node and context dictionary. Additionally, it records the relationship between context node and context dictionary. |
| contextTags | **Field Type** [ContextTag[]](#ContextTag) **Description** Unique identifier of the attribute or node. |
| displayName | **Field Type** string **Description** Display name of the context node. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context node that's used to derive the current context node. |
| title | **Field Type** string **Description** Required. Name of the context node. |
| transposable | **Field Type** boolean **Description** Indicates whether the data in the Context Node record can be converted to field names (`true`) or not (`false`). The default value is `false`. |

		

		

## ContextAttribute

			
			

Represents details of an attribute used to describe a context node. Each node can
				have one or many associated attributes.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Field Name | Description |
| --- | --- |
| contextTags | **Field Type** [ContextTag[]](#ContextTag) **Description** Shortened name of the attribute or node. |
| dataType | **Field Type** ContextAttributeDataType (enumeration of type string) **Description** Required. Type of data that's stored in the context attribute. Valid values are: `boolean` `currency` `date` `datetime` `number` `percent` `picklist` `reference` `string` `selfreference`—Available in API version 63.0 and later. |
| description | **Field Type** string **Description** Description of the context attribute. |
| displayName | **Field Type** string **Description** Display name of the context attribute. |
| domainSet | **Field Type** string **Description** List of node references to show the parent-child relationship between the nodes in a definition. |
| fieldType | **Field Type** ContextAttributeFieldType (enumeration of type string) **Description** Required. List of node references to depict the parent-child relation between the nodes in a definition. Valid values are: `aggregate` `input` `inputoutput` `output` |
| inheritedFrom | **Field Type** string **Description** Name of the parent attribute that's used to derive the current attribute. |
| key | **Field Type** boolean **Description** Indicates whether the attribute is a key attribute in the node (`true`) or not (`false`). The default value is `false`. |
| title | **Field Type** string **Description** Required. Name of the context attribute. |
| transient | **Field Type** boolean **Description** Indicates if an attribute is skipped in context persistence (`true`) or not (`false`). Available in API version 63.0 and later. The default value is `false`. |
| value | **Field Type** boolean **Description** Indicates whether the attribute identifies as a value in a node (`true`) or not (`false`). The default value is `false`. |

		

		

## ContextTag

			
			

Represents a unique identifier of an attribute or node instead of a fully qualified
				tag structure name.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| title | **Field Type** string **Description** Required. Name of the context tag. |
| inheritedFrom | **Field Type** string **Description** Name of the parent context tag that's used to derive the current context tag. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of a ContextDefinition component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ContextDefinition xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Test</fullName>
    <contextDefinitionVersions>
        <contextMappings>
            <contextNodeMappings>
                <contextNodeAttrDictionaries>
                    <contextAttrDictIdentifier>Context Attribute Dictionary Name</contextAttrDictIdentifier>
                    <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>
                </contextNodeAttrDictionaries>
                <contextAttributeMappings>
                    <contextAttrHydrationDetails>
                        <objectName>CustomAccount__c</objectName>
                        <queryAttribute>Name</queryAttribute>
                        <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName/hydrationInfo-1</inheritedFrom>
                    </contextAttrHydrationDetails>
                    <ctxAttrHydrationCtxs>
                        <contextQueryAttribute>StandardDefinition</contextQueryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>
                    </ctxAttrHydrationCtxs>
                    <contextAttribute>AccountName</contextAttribute>
                    <contextInputAttributeName>AccountName</contextInputAttributeName>
                    <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName</inheritedFrom>
                </contextAttributeMappings>
                <contextAttributeMappings>
                    <contextAttrHydrationDetails>
                        <objectName>CustomAccount__c</objectName>
                        <queryAttribute>CustomAccountName__c</queryAttribute>
                        <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>
                    </contextAttrHydrationDetails>
                    <ctxAttrHydrationCtxs>
                        <contextQueryAttribute>StandardDefinition</contextQueryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>
                    </ctxAttrHydrationCtxs>
                    <contextAttribute>CustomAccountName</contextAttribute>
                    <contextInputAttributeName>CustomAccountName</contextInputAttributeName>
                    <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName</inheritedFrom>
                </contextAttributeMappings>
                <contextNode>Praneeth</contextNode>
                <object>CustomAccount__c</object>
                <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth</inheritedFrom>
                <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>
            </contextNodeMappings>
            <contextMappingIntents>
                <mappingIntent>hydration</mappingIntent>
            </contextMappingIntents>
            <default>true</default>
            <title>CustomAccountMapping</title>
            <inheritedFrom>StandardDefinition/version/CustomAccountMapping</inheritedFrom>
        </contextMappings>
        <contextMappings>
            <contextNodeMappings>
                <contextNodeAttrDictionaries>
                    <contextAttrDictIdentifier>Context Attribute Dictionary Name</contextAttrDictIdentifier>
                    <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>
                </contextNodeAttrDictionaries>
                <contextAttributeMappings>
                    <contextAttrHydrationDetails>
                        <objectName>Account</objectName>
                        <queryAttribute>Name</queryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName/hydrationInfo-1</inheritedFrom>
                    </contextAttrHydrationDetails>
                    <ctxAttrHydrationCtxs>
                        <contextQueryAttribute>StandardDefinition</contextQueryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>
                    </ctxAttrHydrationCtxs>
                    <contextAttribute>AccountName</contextAttribute>
                    <contextInputAttributeName>AccountName</contextInputAttributeName>
                    <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName</inheritedFrom>
                </contextAttributeMappings>
                <contextAttributeMappings>
                    <contextAttrHydrationDetails>
                        <objectName>Account</objectName>
                        <queryAttribute>CustomAccountName__c</queryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>
                    </contextAttrHydrationDetails>
                    <ctxAttrHydrationCtxs>
                        <contextQueryAttribute>StandardDefinition</contextQueryAttribute>
                        <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>
                    </ctxAttrHydrationCtxs>
                    <contextAttribute>CustomAccountName</contextAttribute>
                    <contextInputAttributeName>CustomAccountName</contextInputAttributeName>
                    <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName</inheritedFrom>
                </contextAttributeMappings>
                <contextNode>Praneeth</contextNode>
                <object>Account</object>
                <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth</inheritedFrom>
                <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>
            </contextNodeMappings>
             <contextMappingIntents>
                <mappingIntent>persistence</mappingIntent>
             </contextMappingIntents>
            <description>Account Mapping</description>
            <default>false</default>
            <title>AccountMapping</title>
            <inheritedFrom>StandardDefinition/version/AccountMapping</inheritedFrom>
        </contextMappings>
        <contextNodes>
            <contextNodeAttrDictionaries>
                <contextAttrDictIdentifier>Context Attribute Dictionary Name</contextAttrDictIdentifier>
                <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>
            </contextNodeAttrDictionaries>
            <contextAttributes>
                <contextTags>
                    <title>AccountName</title>
                    <inheritedFrom>StandardDefinition/version/Praneeth/AccountName/AccountName</inheritedFrom>
                </contextTags>
                <dataType>string</dataType>
                <fieldType>inputoutput</fieldType>
                <key>false</key>
                <title>AccountName</title>
                <displayName>AccountName</displayName>
                <description>Test Description</description>
                <value>false</value>
                <inheritedFrom>StandardDefinition/version/Praneeth/AccountName</inheritedFrom>
            </contextAttributes>
            <contextAttributes>
                <dataType>string</dataType>
                <fieldType>inputoutput</fieldType>
                <key>false</key>
                <title>CustomAccountName</title>
                <value>false</value>
                <displayName>CustomAccountName</displayName>
                <description>Test Description</description>
                <inheritedFrom>StandardDefinition/version/Praneeth/CustomAccountName</inheritedFrom>
            </contextAttributes>
            <contextTags>
                <title>Praneeth</title>
                <inheritedFrom>StandardDefinition/version/Praneeth/Praneeth</inheritedFrom>
            </contextTags>
            <title>Praneeth</title>
            <transposable>false</transposable>
            <inheritedFrom>StandardDefinition/version/Praneeth</inheritedFrom>
            <canonicalNode></canonicalNode>
            <displayName>Praneeth</displayName>
        </contextNodes>
        <endDate>2097-05-10 00:00:00</endDate>
        <startDate>2023-05-10 00:00:00</startDate>
        <versionNumber>1</versionNumber>
        <isActive>true</isActive>
    </contextDefinitionVersions>
    <description>Test Description</description>
    <contextTtl>10</contextTtl>
    <inheritedFrom>StandardDefinition</inheritedFrom>
    <inheritedFromVersion>1.0</inheritedFromVersion>
    <clonedFrom>OriginalDefinition</clonedFrom>
    <isProtected>false</isProtected>
    <masterLabel>Test Label</masterLabel>
    <title>TestTitle</title>
    <displayName>TestTitle</displayName>
</ContextDefinition>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>Test</members>
        <name>ContextDefinition</name>
    </types>
    <types>
        <members>Account.CustomAccountName__c</members>
        <name>CustomField</name>
    </types>
    <types>
        <members>CustomAccount__c</members>
        <name>CustomObject</name>
    </types>
    <version>64.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving
					Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: persistence_context_management.htm ===
---
page_id: persistence_context_management.htm
title: Context Persistence
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/persistence_context_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Persistence

Persist context data to Salesforce database entities.

- 
**[Persist Context (POST)](./connect_resources_persist_context.htm.md)**  

Persist a context by passing the context ID.

=== ARTICLE: runtime_context_intance_management.htm ===
---
page_id: runtime_context_intance_management.htm
title: Context Service Runtime
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/runtime_context_intance_management.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Service Runtime

Create new runtime context instances, query data from context instances, and delete
        context instances.

- 
**[Context Service (POST)](./connect_resources_create_context.htm.md)**  

Create new context records by submitting metadata and associated JSON data. After     validating the data, the system generates a new context ID. Context objects created using this     API apply only to a single request. They cannot be used to pass data across multiple     requests.

- 
**[Context Service (DELETE, GET)](./connect_resources_context_service_runtime.htm.md)**  

Retrieve the context details using a context ID. Delete a context record using a     context ID.

- 
**[Context Attribute (PATCH)](./connect_resources_update_context_attribute.htm.md)**  

Update attributes of a context record.

- 
**[Context Runtime Schema (DELETE)](./connect_resources_context_runtime_schema.htm.md)**  

Clear runtime schema cache for context definitions and their associated mappings. 

- 
**[Query Context Definition Interfaces (GET)](./connect_resources_query_context_interfaces.htm.md)**  

Get the lists of metadata associated with context definition interfaces.

- 
**[Query Context Definition Interface By Name (GET)](./connect_resources_query_context_interface_by_name.htm.md)**  

Get the details of a context definition interface by using the context definition     interface name.

- 
**[Query Context Record (POST)](./connect_resources_query_context_record.htm.md)**  

Query a context record, with the option to retrieve child records.

- 
**[Query Record Status (PATCH, POST)](./connect_resources_create_update_query_data_record_status.htm.md)**  

Update the processing status and related error messages of query data records. Create     the processing status and related error messages of query data records

- 
**[Query Tags (POST)](./connect_resources_create_query_tag.htm.md)**  

Create query tags within a defined context

- 
**[Write Through Tags (PATCH)](./connect_resources_write_through_tags.htm.md)**  

Update Context Attributes through tags.

=== ARTICLE: sforce_api_objects_contextpersistenceevent.htm ===
---
page_id: sforce_api_objects_contextpersistenceevent.htm
title: ContextPersistenceEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_contextpersistenceevent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: contextpersistenceevent_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextPersistenceEvent

Notifies subscribers when the Context Persistence event, initiated by the Context
		Persistence API has completed its execution. This event is designed to inform
		customers/clients about the success or failure of their Context Persistence request. This
		object is available in API version 59.0 and later.

		

## Supported Calls

			
			

`describeSObjects()`

		

		

## Supported Subscribers

			
			

					
					
					
						
							

							

						

					

					
						
							

							

						

						
							

							

						

						
							

							

						

						
							

							

						

					

				
| Subscriber | Supported? |
| --- | --- |
| Apex Triggers |  |
| Flows |  |
| Processes |  |
| Streaming API (CometD) |  |

		

		

## Streaming API Subscription Channel

			
			

`/event/ContextPersistenceEvent`

		

		

## Special Access Rules

			
			

The ContextPersistenceEvent is available when IndustriesContextService Org permission is
				enabled.

		

		

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

						

					

				
| Field | Details |
| --- | --- |
| Correlation Id | **Type** string **Properties** Nillable **Description** The unique identifier of the parent request that this request belongs to. |
| EventUuid | **Type** string **Properties** Create **Description** Required. A universally unique identifier (UUID) that identifies a platform event message. |
| HasErrors | **Type** boolean **Properties** Nillable **Description** Indicates whether the context persistence service is a failure (`true`) or a success (`false`). |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| Request Identifier | **Type** string **Properties** Nillable **Description** The identifier of asynchronous or synchronous request associated with the event. |

=== ARTICLE: tooling_api_objects_contextattrhydrationdetail.htm ===
---
page_id: tooling_api_objects_contextattrhydrationdetail.htm
title: ContextAttrHydrationDetail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextattrhydrationdetail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextAttrHydrationDetail

      Represents the SOQL (database) queries that fetch data for a chosen attribute
         from the input schema. This object is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ContextAttributeMappingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context attribute mapping record that's associated with the attribute hydration detail. This field is a relationship field. **Relationship Name** ContextAttributeMapping **Relationship Type** Lookup **Refers To** ContextAttributeMapping |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| ObjectName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the object used for the attribute hydration detail. |
| ParentHydrationDetailId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The parent hydration detail attribute. Based on the attribute mapping, there can be more than one hydration information sources. This field is a relationship field. **Relationship Name** ParentHydrationDetail **Relationship Type** Lookup **Refers To** ContextAttrHydrationDetail |
| QueryAttribute | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The SOQL or query that is the source of the hydration. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context attribute hydration detail that's used to derive the current context attribute hydration detail.This field is available in API version 60.0 and later. |

=== ARTICLE: tooling_api_objects_contextattribute.htm ===
---
page_id: tooling_api_objects_contextattribute.htm
title: ContextAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextattribute.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextAttribute

      Represents information about an attribute used to describe a context node.
         Each node can have one or many attributes associated with it.  This object is
      available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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
| ContextNodeId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context node record that's associated with the context attribute. This field is a relationship field. **Relationship Name** ContextNode **Relationship Type** Lookup **Refers To** ContextNode |
| DataType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of data that's stored in the context attribute. Possible values are: `boolean`Boolean `currency`—Currency `date`—Date `datetime`—Datetime `lookup`—Lookup `number`—Number `percent`—Percent `picklist`—Picklist `reference`—Reference `string`—String The default value is `string`. |
| DomainSet | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The list of node references to show a parent-child relationship between nodes in a definition. |
| FieldType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** List of node references to depict parent/child relation between the nodes in a definition Possible values are: `input`—INPUT `inputoutput`—INPUTOUTPUT `output`—OUTPUT The default value is `input`. |
| IsKey | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the attribute is a key attribute in the node (true) or not (false). The default value is `false`. |
| IsLocalizationDisabled | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the context attribute is to be localized or not The default value is `false`. This field is available in API version 68.0 and later. |
| IsTransient | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if an attribute must be skipped in context persistence. The default value is `false`. |
| IsValue | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates the attribute that identifies as a value in a node. The default value is `false`. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| Title | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the context attribute. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent attribute that's used to derive the current attribute.This field is available in API version 60.0 and later. |

=== ARTICLE: tooling_api_objects_contextattributemapping.htm ===
---
page_id: tooling_api_objects_contextattributemapping.htm
title: ContextAttributeMapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextattributemapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextAttributeMapping

      Represents the relationship between the attribute defined in the context and
         the values in the related objects. This object is available in API version 59.0 and
      later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ContextAttributeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context attribute record associated with this context attribute mapping. This field is a relationship field. **Relationship Name** ContextAttribute **Relationship Type** Lookup **Refers To** ContextAttribute |
| ContextInputAttributeName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Stores the name of input attribute. |
| ContextNodeMappingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context node mapping record that's associated with the context attribute mapping. This field is a relationship field. **Relationship Name** ContextNodeMapping **Relationship Type** Lookup **Refers To** ContextNodeMapping |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context attribute mapping that's used to derive the current context attribute mapping.This field is available in API version 60.0 and later. |

=== ARTICLE: tooling_api_objects_contextdefinition.htm ===
---
page_id: tooling_api_objects_contextdefinition.htm
title: ContextDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDefinition

      Represents information about a context definition. The context definition
         describes the relationship between the node structures within a context. This object
      is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

: 

: 
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

                  

               

            
| Field | Details |
| --- | --- |
| CanBeReferenceDefinition | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the context definition can be referred by other context definitions (`true`) or not (`false`). The default value is `false`. This field is available in API version 63.0 and later. |
| ClonedFrom | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the context definition that's used to clone the current context definition. |
| ContextTtl | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Displays how long you’d like the data that’s loaded in the runtime context instances created by this context definition to stay in the cache. The default value is 10 minutes. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the context definition. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the context definition. |
| DisplayName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The display name of the context definition. |
| HasSystemTags | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the context definition has system tags (`true`) or not (`false`). The default value is `false`. This field is available in API version 63.0 and later. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context definition that's used to derive the current context definition.This field is available in API version 60.0 and later. |
| InheritedFromVersion | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The version number of the parent definition that's used to derive the current context definition.This field is available in API version 60.0 and later. |
| IsTransformationEnabled | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether transformations are enabled for the context definition. The default value is `false`. This field is available in API version 68.0 and later. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the context definition. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The UI label of the context definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the namespacePrefix__componentName notation. |
| Title | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the context definition. |

=== ARTICLE: tooling_api_objects_contextdefinitionreference.htm ===
---
page_id: tooling_api_objects_contextdefinitionreference.htm
title: ContextDefinitionReference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextdefinitionreference.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDefinitionReference

      Represents information about reference from one Context Definition to another
         Context Definition.  This object is available in API version 60.0 and
      later.

      
      

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

                  

               

            
| Field | Details |
| --- | --- |
| ContextDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context definition record that's associated with the context definition reference. This field is a relationship field. **Relationship Name** ContextDefinition **Relationship Type** Master-detail **Refers To** ContextDefinition |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context definition that's used to derive the current context definition.This field is available in API version 60.0 and later. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| ReferenceContextDefinition | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the referred context definition. |

=== ARTICLE: tooling_api_objects_contextdefinitionsync.htm ===
---
page_id: tooling_api_objects_contextdefinitionsync.htm
title: ContextDefinitionSync
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextdefinitionsync.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDefinitionSync

Stores information for the sync operation of the custom definition
         with the standard definition. This object is available in API version 62.0 and
      later.

      
      

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
- 
- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ContextDefinitionName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The context definition the sync is running for. |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the synchronization ends. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the context definition sync record. This is a default field created for a platform entity. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the synchronization starts. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the sync operation. Valid values are: `failed` `in_progress` `success` |
| SynchronizationInformation | **Type** textarea **Properties** Create, Nillable, Update **Description** The details of the context definition synchronization. |

=== ARTICLE: tooling_api_objects_contextdefinitionversion.htm ===
---
page_id: tooling_api_objects_contextdefinitionversion.htm
title: ContextDefinitionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextdefinitionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDefinitionVersion

      Represents information about the context definition version. Only one version
         can be active at a time. This object is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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
| ContextDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context definition record associated with the context definition version. This field is a relationship field. **Relationship Name** ContextDefinition **Relationship Type** Lookup **Refers To** ContextDefinition |
| EndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the context definition version becomes inactive. |
| InheritedApexVersion | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The version of the Apex class generated from the context definition version. It is null when no Apex class is generated, 0.0 when an Apex class is generated for a custom definition, and equal to the value in InheritedVersionNumber when an Apex class is generated from an extended definition. This field is available in API version 68.0 and later. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the context definition version is active (true) or not (false). The default value is `false`. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| StartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the context definition version becomes active. |
| VersionNumber | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The context definition version number. |

=== ARTICLE: tooling_api_objects_contextmapping.htm ===
---
page_id: tooling_api_objects_contextmapping.htm
title: ContextMapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextmapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextMapping

      Represents the mapping of both attributes and nodes to related objects.
      This object is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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
| ContextDefinitionVersionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context definition version record that's associated with the context mapping. This field is a relationship field. **Relationship Name** ContextDefinitionVersion **Relationship Type** Lookup **Refers To** ContextDefinitionVersion |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the context mapping. |
| IsDefault | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the mapping for a context definition version is default (true) or not (false). The default value is `false`. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| Title | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the context mapping. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent mapping that's used to derive the current mapping.This field is available in API version 60.0 and later. |

=== ARTICLE: tooling_api_objects_contextmappingintent.htm ===
---
page_id: tooling_api_objects_contextmappingintent.htm
title: ContextMappingIntent
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextmappingintent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextMappingIntent

      Represents the purpose associated to a context mapping. This object is
      available in API version 61.0 and later. 

      
      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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
- 
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| ContextMappingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context mapping that's associated with usage intent. This field is a relationship field. **Relationship Name** ContextMapping **Relationship Type** Master-detail **Refers To** ContextMapping (the master object) |
| MappingIntent | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the purpose to identify the type of context mapping required. Possible values are: `association`—Association `hydration`—Hydration `persistence`—Persistence `translation`—Translation |

=== ARTICLE: tooling_api_objects_contextnode.htm ===
---
page_id: tooling_api_objects_contextnode.htm
title: ContextNode
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextnode.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextNode

      Represents information about the structure of the nodes within the context.
         Within a structure, each node can have other nodes related to them and attributes to
         describe the object. A hierarchy for the nodes can also be defined here. This object
      is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CanonicalNodeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The canonical node associated with the context node. This field is a relationship field. This field is available in API version 61.0 and later. **Relationship Name** CanonicalNode **Refers To** ContextNode |
| ContextDefinitionVersionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context definition version record associated with the context node. This field is a relationship field. **Relationship Name** ContextDefinitionVersion **Relationship Type** Lookup **Refers To** ContextDefinitionVersion |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** The description of the context node. |
| DisplayName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The display name of the context node.This field is available in API version 61.0 and later. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context node that's used to derive the current context node.This field is available in API version 60.0 and later. |
| IsCustomMappingAllowed | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the attribute can be mapped to a source attribute in an extended context definition (`true`) or not (`false`). The default value is `false`. |
| IsTransposable | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the data in the Context Node record can be converted to field names (true) or not (false). The default value is `false`. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| Title | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the context node. |

=== ARTICLE: tooling_api_objects_contextnodeattrdictionary.htm ===
---
page_id: tooling_api_objects_contextnodeattrdictionary.htm
title: ContextNodeAttrDictionary
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextnodeattrdictionary.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextNodeAttrDictionary

Represents
         the
         relationship between
         the
         ContextNodeMapping and ContextDictionary
         objects
         as a junction table. This object is available in API version 62.0
      and later.

      
      

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

                  

               

            
| Field | Details |
| --- | --- |
| ContextAttrrDictIdentifier | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The developer name of the context attribute dictionary. |
| ContextNodeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the context node. This field is a relationship field. **Relationship Name** ContextNode **Relationship Type** Lookup **Refers To** ContextNode |
| ContextNodeMapingId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the context node mapping. This field is a relationship field. **Relationship Name** ContextNodeMapping **Relationship Type** Lookup **Refers To** ContextNodeMapping |
| ContextNodeTagPrefix | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The tag prefix of the context node that's used to create the unique identifier of the parent context node. |

=== ARTICLE: tooling_api_objects_contextnodemapping.htm ===
---
page_id: tooling_api_objects_contextnodemapping.htm
title: ContextNodeMapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contextnodemapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextNodeMapping

      Represents the relationship between the node in the context and values in the
         input schema. This object is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ContextMappingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context mapping record that's associated with the context node mapping. This field is a relationship field. **Relationship Name** ContextMapping **Relationship Type** Lookup **Refers To** ContextMapping |
| ContextNodeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context node record associated with this context node mapping. This field is a relationship field. **Relationship Name** ContextNode **Relationship Type** Lookup **Refers To** ContextNode |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| Object | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the object used for the mapping. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context node mapping that's used to derive the current context node mapping.This field is available in API version 60.0 and later. |
| MappedContextDefinition | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the context definition when context-to-context mappings exist.This field is available in API version 61.0 and later. |

=== ARTICLE: tooling_api_objects_contexttag.htm ===
---
page_id: tooling_api_objects_contexttag.htm
title: ContextTag
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_contexttag.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextTag

      Represents a shortened name of an attribute or node instead of its fully
         qualified tag structure name. This object is available in API version 59.0 and later. 

      
      

## Supported SOAP API Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ContextAttributeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context attribute record that's associated with the context tag. This field is a relationship field. **Relationship Name** ContextAttribute **Relationship Type** Lookup **Refers To** ContextAttribute |
| ContextNodeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context node record that's associated with the context tag. This field is a relationship field. **Relationship Name** ContextNode **Relationship Type** Lookup **Refers To** ContextNode |
| Title | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the context tag. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent context tag that's used to derive the current context tag.This field is available in API version 60.0 and later. |

=== ARTICLE: tooling_api_objects_ctxattrhydrationctx.htm ===
---
page_id: tooling_api_objects_ctxattrhydrationctx.htm
title: CtxAttrHydrationCtx
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_ctxattrhydrationctx.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Context Service
parent_page: context_service_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CtxAttrHydrationCtx

      Represents the queries that fetch the data for a chosen attribute from the
         input schema for context-to-context mapping This object is available in API version
      61.0 and later. 

      
      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ContextAttributeMappingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The context attribute mapping record that's associated with the attribute hydration detail. This field is a relationship field. **Relationship Name** ContextAttributeMapping **Relationship Type** Master-detail **Refers To** ContextAttributeMapping (the master object) |
| ContextQueryAttribute | **Type** string **Properties** Create, Filter, Sort, Update **Description** The attribute in context definition that's the source of context hydration. |
| InheritedFrom | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The name of the parent CtxAttrCtxHydrationDetail that's used to derive the current CtxAttrCtxHydrationDetail. |

