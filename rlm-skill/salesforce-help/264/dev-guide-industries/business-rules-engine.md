# Industries Common Resources Developer Guide 264 — sección: Business Rules Engine (183 artículos)

=== ARTICLE: actions_obj_decision_matrix.htm ===
---
page_id: actions_obj_decision_matrix.htm
title: Decision Matrix Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_decision_matrix.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_invocable_actions.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Actions

Invoke a decision matrix in a flow with the Decision Matrix
      Actions. A decision matrix is a user-defined table where you can look up an output based
    on the inputs you provide. 

    
      

For example, you can look up a candidate’s eligibility to avail medical insurance in a
        decision matrix based on the candidate’s age and gender.

    

    
      

These actions are available in API version 55.0 and later.

    

    

## Supported REST HTTP Methods

      
      
        
          
            

**URI**

            
: 
`/services/data/v55.0/actions/custom/runDecisionMatrix/{UniqueName}`

#### Note

The
                value of UniqueName is the unique identifier of the record, which is sourced from
                the name of a decision matrix.

          
          
            

**Formats**

            
: JSON

          
          
            

**HTTP Methods**

            
: POST

          
          
            

**Authentication**

            
: `Authorization: Bearer
                  token`

          
        

      

    

    

## Inputs

      
      

Vary depending on the selected decision matrix.

    

    

## Outputs

      
      

Vary depending on the inputs of the selected decision matrix.

    

    

## Usage

      
      
        
          

**Sample Request**

          
: 
            

Here’s an example POST request that has the inputs, such as, age and state:

            

```
{
   "inputs":[
      {
         "age":"25",
         "state":"NY"
      },
      {
         "age":"25",
         "state":"CA"
      },
      {
         "age":"",
         "state":"WA"
      }
   ]
}
```

          

        
        
          

**Sample Response**

          
: 
            

Here’s an example response that has the premium and tax values based on the inputs
              provided in the example request.

            

```
[
   {
      "actionName":"premiumTaxLookup",
      "errors":null,
      "isSuccess":true,
      "outputValues":{
         "premium":2400.0,
         "tax":200.0
      }
   },
   {
      "actionName":"premiumTaxLookup",
      "errors":null,
      "isSuccess":true,
      "outputValues":{
         "premium":2400.0,
         "tax":200.0
      }
   },
   {
      "actionName":"premiumTaxLookup",
      "errors":[
         {
            "statusCode":"REQUIRED_FIELD_MISSING",
            "message":"Missing required input parameter: age",
            "fields":[
            ]
         }
      ],
      "isSuccess":false,
      "outputValues":null
   }
]
```

=== ARTICLE: actions_obj_expression_set.htm ===
---
page_id: actions_obj_expression_set.htm
title: Expression Set Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_expression_set.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_invocable_actions.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Actions

Invoke an active expression set. An expression set is a user-defined
      rule that accepts an input and returns the output based on the configured
    function.

    
      

The configured function of an expression set can be a simple decision matrix lookup, a
        calculation based on a mathematical formula, a condition, or another expression set.

      

When a Flow is invoked using Batch management (for example, for processing 200 records),
        the calls to expression sets are automatically bulkified, which allows the execution of
        multiple inputs in a single request.

      

These actions are available in API version 55.0 and later.

    

  

## Supported REST HTTP Methods

      
      
        
          
            

**URI**

            
: 
`/services/data/v55.0/actions/custom/runExpressionSet/{ApiName}`

#### Note

The
                API name of an expression set is unique within your Salesforce instance.

          
          
            

**Formats**

            
: JSON

          
          
            

**HTTP Methods**

            
: POST

          
          
            

**Authentication**

            
: `Authorization: Bearer token`

          
        

      

    

    

## Inputs

      
      

Inputs vary depending on the selected expression set. For expression sets tied to a context
        definition, you can build and persist context data using additional inputs.

      

          
          
          
            
              

              

            

          

          
            
              

              

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
| __<ContextNode>​RecordIds | **Type** List<String> **Description** Optional. A collection of context node record IDs to be built. |
| __mappingName | **Type** String **Description** Optional. The default context mapping available in the context definition. |
| __persist​ContextData | **Type** Boolean **Description** Optional. Indicates whether to save context data to the database (`true`) or not (`false`). |
| __buildContext | **Type** String **Description** Optional. Indicates whether to build the context using the IDs of context definition records in the database. |

      

For context-based expression sets, provide either the context ID or the build context
        parameters. If both are provided and `__buildContext` is
          `true`, the context ID is ignored and the context is
        built from the input record IDs.

    

    

## Outputs

      
      

Vary depending on the inputs of the selected expression set.

    

    

## Usage

        
          

**When the expression set is not linked with a context**

          
: 
            

This section has the sample request and response for invoking an expression set with
              these steps.

            
              
1. Find the tax percentage and the premium corresponding to specific age and salary
                using a decision matrix lookup.

              
2. Check the age criterion to calculate the total tax.

              
3. Calculate the total tax to be paid based on the age group, salary, and the tax
                percentage.

            

            
              
                

**Sample request**

                
: 
                  

Here’s an example POST request that has the inputs, such as, age and
                    salary.

                  

```
{
  "inputs": [
    {
      "Age": "25.00",
      "Salary": "50000.00"
    },
    {
      "Age": "30.00",
      "Salary": "70000.00"
    },
    {
      "Age": "40.00",
      "Salary": "90000.00"
    }
  ]
}
```

                

              
              
                

**Sample response**

                
: 
                  

Here’s an example response that has the premium and tax values based on the
                    inputs provided in the example request.

                  

```
[
  {
    "actionName": "TaxPremiumES",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "TaxPremium__Premium": 1000,
      "TaxPremium__Tax": 10,
      "TaxToBePaid": 1050,
      "condition_output__2": "false",
      "condition_output__1": "true"
    }
  },
  {
    "actionName": "TaxPremiumES",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "TaxPremium__Premium": 1500,
      "TaxPremium__Tax": 12,
      "TaxToBePaid": 1512,
      "condition_output__2": "true",
      "condition_output__1": "false"
    }
  },
  {
    "actionName": "TaxPremiumES",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "TaxPremium__Premium": 2000,
      "TaxPremium__Tax": 15,
      "TaxToBePaid": 2015,
      "condition_output__2": "false",
      "condition_output__1": "true"
    }
  }
]
```

                

              
            

          

        
        
          

**When the expression set is linked with a context**

          
: 
            

An expression set can be configured with a context definition. In this case, the
              expression set runs using context data that is either provided directly or built at
              runtime.

            
              
                

**Sample request when context ID is available**

                
: 
                  

Here's an example request that runs a context-based expression set using an
                    existing context ID.

                  

```
{
  "inputs": [
    {
      "Claim2Id": "55304396580d20ffbae5111a641ab0a747ffbe47dfab2b16df35df9ac87184fc",
      "inputVar1": 10
    }
  ]
}
```

                

              
              
                

**Sample response**

                
: 
                  

Here's an example response for a context-based expression set execution.

                  

```
[
  {
    "actionName": "ClaimProcessingES",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "Claim2Id": "55304396580d20ffbae5111a641ab0a747ffbe47dfab2b16df35df9ac87184fc",
      "inputVar1": 10
    }
  }
]
```

                

              
            

            
              
                

**Sample request when context ID is not available**

                
: 
                  

When an expression set is tied to a context definition and a context ID isn't
                    available, use the `__buildContext` parameter
                    to build the context before the expression set runs. You can also persist the
                    context data to the database after execution by setting `__persistContextData` to `true`.

                  

Here's an example POST request that builds the context, runs the expression
                    set, and persists the context data.

                  

```
{
  "inputs": [
    {
      "inputVar1": 10,
      "__buildContext": true,
      "__StudentRecordIds": ["a02xx000001nf9nAAA"],
      "__mappingName": "Default Mapping",
      "__persistContextData": true
    }
  ]
}
```

                

              
              
                

**Sample response**

                
: 
                  

Here's an example response that includes the context ID that was built during
                    execution.

                  

```
[
  {
    "actionName": "StudentEligibilityES",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "StudentId": "55304396580d20ffbae5111a641ab0a747ffbe47dfab2b16df35df9ac87184fc",
      "inputVar1": 10
    }
  }
]
```

=== ARTICLE: apex_ConnectAPI_DecisionTable_execute_1.htm ===
---
page_id: apex_ConnectAPI_DecisionTable_execute_1.htm
title: execute(decisionTableId, DecisionTableInput)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_ConnectAPI_DecisionTable_execute_1.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_methods.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# execute(decisionTableId, DecisionTableInput)

Execute an active decision table.

    

## API Version

      
      

51.0

    

    

## Requires Chatter

      
      

No

    

    

## Signature

      
      

`public static ConnectApi.DecisionTableOutcome execute(String
          decisionTableId, ConnectApi.DecisionTableInput DecisionTableInput)`

      
    

    

## Parameters

      
      
        
          

**decisionTableId**

          
: Type: String

          
: ID of the decision table.

        
        
          

**DecisionTableInput**

          
: Type: [`ConnectApi.DecisionTableInput`](./apex_connectapi_input_decision_table.htm.md)

          
: A `ConnectApi.DecisionTableInput` object with a
            list of conditions.

        
      

    

    

## Return Value

      
      

Type: [`ConnectApi.DecisionTableOutcome`](./apex_connectapi_output_decision_table_outcome.htm.md)

    

    

## Example

      
      
        

```

ConnectApi.DecisionTableInput input = new ConnectApi.DecisionTableInput();
input.datasetLinkName = ‘DSL1’;//Optional,if you want to use a dataset link mapping definition
input.conditions = new List<ConnectApi.DecisionTableCondition>();
ConnectApi.DecisionTableCondition condition = new ConnectApi.DecisionTableCondition();
condition.fieldName = 'Brand__c';
condition.value = 'Cloud Kicks';
input.conditions.add(condition);
ConnectApi.DecisionTableOutcome output = ConnectApi.DecisionTable.execute('0lDxxxj23444', input);

```

=== ARTICLE: apex_class_BusinessRule_CalculationMatrixMigrationService.htm ===
---
page_id: apex_class_BusinessRule_CalculationMatrixMigrationService.htm
title: CalculationMatrixMigrationService Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_class_BusinessRule_CalculationMatrixMigrationService.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: apex_namespace_BusinessRule.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationMatrixMigrationService Class

Contains methods for migrating calculation matrices from the Vlocity
      package to the Business Rules Engine as decision matrices.

## Namespace

[BusinessRule](./apex_namespace_BusinessRule.htm.md)

## Example

      This example converts a list of calculation matrix IDs to decision matrix IDs and logs the
        result in the debug log.

```

List<String> ids = new List<String>();
ids.add('a03xx000004WhvkAAC');
ids.add('a03xx000004WhxMAAS');
ids.add('a03xx000004WhyyAAC');

System.debug('TO MIGRATE A LIST OF CALCULATION MATRICES');
System.debug(BusinessRule.CalculationMatrixMigrationService.migrate(ids, 'vlocity_ins'));

```

      This example converts a calculation matrix ID to a decision matrix ID and logs the result
        in the debug log.

```

System.debug('TO MIGRATE A CALCULATION MATRIX');
System.debug(BusinessRule.CalculationMatrixMigrationService.migrate('a03xx000004Wi0aAAC', 'vlocity_ins'));

```

- 
**[CalculationMatrixMigrationService Methods](./apex_class_BusinessRule_CalculationMatrixMigrationService.htm.md#apex_BusinessRule_CalculationMatrixMigrationService_methods)**  

## CalculationMatrixMigrationService Methods

The following are methods for `CalculationMatrixMigrationService`.

- 
**[migrate(calculationMatrixIds, namespace)](./apex_class_BusinessRule_CalculationMatrixMigrationService.htm.md#apex_BusinessRule_CalculationMatrixMigrationService_migrate)**  

Migrate calculation matrices from the Vlocity package to the Business       Rules Engine as decision matrices.

- 
**[migrate(calculationMatrixId, namespace)](./apex_class_BusinessRule_CalculationMatrixMigrationService.htm.md#apex_BusinessRule_CalculationMatrixMigrationService_migrate_2)**  

Migrate a calculation matrix from the Vlocity package as a decision       matrix to the Business Rules Engine.

### migrate(calculationMatrixIds, namespace)

Migrate calculation matrices from the Vlocity package to the Business
      Rules Engine as decision matrices.

#### Signature

`public static Map<String,Object> migrate(List<String> calculationMatrixIds, String namespace)`

#### Parameters

**calculationMatrixIds**

: Type: List<String>

: The 18-character IDs of the calculation matrices in the Vlocity managed package to be migrated
            to the Business Rules Engine as decision matrices.

**namespace**

: Type: String

: The namespace in which Vlocity is deployed as a managed package. For example,
                `vlocity_ins`. This contains the calculation
              matrix custom objects.

#### Return Value

Type: Map<String,Object>

### migrate(calculationMatrixId, namespace)

Migrate a calculation matrix from the Vlocity package as a decision
      matrix to the Business Rules Engine.

#### Signature

`public static Map<String,Object> migrate(String calculationMatrixId, String namespace)`

#### Parameters

**calculationMatrixId**

: Type: String

: The 18-character ID of the calculation matrix in the Vlocity managed package to be migrated to
            the Business Rules Engine as a decision matrix.

**namespace**

: Type: String

          
: The namespace in which Vlocity is deployed as a managed package. For example, `vlocity_ins`. This contains the calculation matrix
            custom objects.

#### Return Value

Type: Map<String,Object>

=== ARTICLE: apex_class_BusinessRule_CalculationProcedureMigrationService.htm ===
---
page_id: apex_class_BusinessRule_CalculationProcedureMigrationService.htm
title: CalculationProcedureMigrationService Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_class_BusinessRule_CalculationProcedureMigrationService.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: apex_namespace_BusinessRule.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationProcedureMigrationService Class

Contains methods for migrating calculation procedures from the Vlocity
      package to the Business Rules Engine as expression sets.

## Namespace

[BusinessRule](./apex_namespace_BusinessRule.htm.md)

    

## Usage

      
      Consider these guidelines before migrating a calculation procedure that uses a calculation matrix.
          
- Migrate the calculation matrix first. This creates a decision matrix.

          
- Add data to the decision matrix and activate it.

        

    

## Example

      This example converts a list of calculation procedure IDs to expression set IDs and logs
        the result in the debug log.

```

List<String> calcProcIds = new List<String>();
calcProcIds.add('a00xx000000boy5AAA');
calcProcIds.add('a00xx000000bozhAAA');
calcProcIds.add('a00xx000000bp1JAAQ');

System.debug('TO MIGRATE A LIST OF CALCULATION PROCEDURES');
System.debug(BusinessRule.CalculationProcedureMigrationService.migrate(calcProcIds, 'vlocity_ins'));

```

      This example converts a calculation procedure ID to an expression set ID and logs the
        result in the debug log.

```

System.debug('TO MIGRATE A CALCULATION PROCEDURE');
System.debug(BusinessRule.CalculationProcedureMigrationService.migrate('a00xx000000bp2vAAA', 'vlocity_ins'));

```

- 
**[CalculationProcedureMigrationService Methods](./apex_class_BusinessRule_CalculationProcedureMigrationService.htm.md#apex_BusinessRule_CalculationProcedureMigrationService_methods)**  

## CalculationProcedureMigrationService Methods

The following are methods for `CalculationProcedureMigrationService`.

- 
**[migrate(calcProcedureIds, namespace)](./apex_class_BusinessRule_CalculationProcedureMigrationService.htm.md#apex_BusinessRule_CalculationProcedureMigrationService_migrate)**  

Migrate calculation procedures from the Vlocity package as expression       sets to the Business Rules Engine.

- 
**[migrate(calcProcedureId, namespace)](./apex_class_BusinessRule_CalculationProcedureMigrationService.htm.md#apex_BusinessRule_CalculationProcedureMigrationService_migrate_2)**  

Migrate a calculation procedure from the Vlocity package as an       expression set to the Business Rules Engine.

### migrate(calcProcedureIds, namespace)

Migrate calculation procedures from the Vlocity package as expression
      sets to the Business Rules Engine.

#### Signature

`public static Map<String,Object> migrate(List<String>
          calcProcedureIds, String namespace)`

#### Parameters

**calcProcedureIds**

: Type: List<String>

: The 18-character IDs of the calculation procedures in the Vlocity managed package to be migrated
                        to the Business Rules Engine as expression sets.

18 character ID.

                    

**namespace**

                    
: Type: String

                    
: The namespace in which Vlocity is deployed as a
                            managed package. For example, `vlocity_ins`. This contains the calculation procedure
                            custom objects.

                

#### Return Value

Type: Map<String,Object>

### migrate(calcProcedureId, namespace)

Migrate a calculation procedure from the Vlocity package as an
      expression set to the Business Rules Engine.

#### Signature

`public static Map<String,Object> migrate(String
          calcProcedureId, String namespace)`

#### Parameters

**calcProcedureId**

: Type: String

: The 18-character ID of the calculation procedure in the Vlocity managed package to be migrated
            to the Business Rules Engine as an expression set.

**namespace**

: Type: String

: The namespace in which Vlocity is deployed as a managed package. For example, `vlocity_ins`. This contains the calculation procedure
            custom objects.

#### Return Value

Type: Map<String,Object>

=== ARTICLE: apex_connectapi_input_decision_table.htm ===
---
page_id: apex_connectapi_input_decision_table.htm
title: ConnectApi.DecisionTableInput
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_connectapi_input_decision_table.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.DecisionTableInput

Input representation of the decision table.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `conditions` | List<[`ConnectApi.​DecisionTableCondition`](./apex_connectapi_input_decision_table_condition_representatio.htm.md)> | List of decision table conditions on which the decision table executes. | Required | 51.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 51.0 |

=== ARTICLE: apex_connectapi_input_decision_table_condition_representatio.htm ===
---
page_id: apex_connectapi_input_decision_table_condition_representatio.htm
title: ConnectApi.DecisionTableCondition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_connectapi_input_decision_table_condition_representatio.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.DecisionTableCondition

Input representation of the decision table condition.

- 
- 
- 
- 
- 
- 
- 
- 
- 

            
              

              

              

              

              

            

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fieldName` | String | The field name that is selected as an input for the decision table. | Required | 51.0 |
| `operator` | String | The operator used for the input field. Valid values are: `DoesNotExistIn`—Use to check if the input value doesn’t exist in a multi-select picklist. `Equals`—Use to check if the input value equals to the configured value in the rule. `ExistsIn`—Use to check if the input value exists in a multi-select picklist. `GreaterOrEqual`—Use to check if the input value is greater than or equal to the configured value in the rule. `GreaterThan`—Use to check if the input value is greater than the configured value in the rule. `LessOrEqual`—Use to check if the input value is less than or equal to the configured value in the rule. `LessThan`—Use to check if the input value is less than the configured value in the rule. `Matches`—Use to check if the input value is a substring of the value in the rule. `NotEquals`— The operator specified here overrides the operator defined in Decision Table. | Optional | 51.0 |
| `sourceObject` | String | The name of source object for the input field. The source object field is not mandatory if the dataset link is configured with a single source object.The source object field is required only when the dataset link definition contains multiple source objects. | Optional | 52.0 |
| `value` | Object | The value of the data type that is selected as an input. | Required | 51.0 |

=== ARTICLE: apex_connectapi_output_decision_table_outcome.htm ===
---
page_id: apex_connectapi_output_decision_table_outcome.htm
title: ConnectApi.DecisionTableOutcome
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_connectapi_output_decision_table_outcome.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.DecisionTableOutcome

Output representation of the decision table
    execution.

#### 

- 
- 
- 

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errorCode` | Integer | The error code if transaction fails for any reason. | 51.0 |
| `errorMessage` | String | The error message if transaction fails for any reason. | 51.0 |
| `outcomeList` | List<[`ConnectApi.​DecisionTableOutcomeItem`](./apex_connectapi_output_decision_table_outcome_item.htm.md)> | The outcome list that stores two or more outcomes provided by the decision table. Note A decision table that is invoked by the Decision Table custom invocable action can provide up to 50 outcomes. | 51.0 |
| `outcomeType` | String | The outcome type after the request is successful. Valid values are: `MultipleMatch`—Outcome returns multiple matches. `NoMatch`—Outcome returns no match. `SingleMatch`—Outcome returns single match. | 51.0 |
| `successStatus` | Boolean | Indicates the status of the decision table execution. | 51.0 |

=== ARTICLE: apex_connectapi_output_decision_table_outcome_item.htm ===
---
page_id: apex_connectapi_output_decision_table_outcome_item.htm
title: ConnectApi.DecisionTableOutcomeItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_connectapi_output_decision_table_outcome_item.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.DecisionTableOutcomeItem

Output representation of the decision table outcome
    item.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `values` | Map<String, Object> | The list of outcomes provided by the decision table. If the decision table is configured to sort outcomes based on an input field or the output field, then the outcomes are provided based on the selected sort order. | 51.0 |

=== ARTICLE: apex_namespace_BusinessRule.htm ===
---
page_id: apex_namespace_BusinessRule.htm
title: BusinessRule Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/apex_namespace_BusinessRule.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BusinessRule Namespace

The `BusinessRule` namespace provides classes for
    migrating calculation matrices and calculation procedures from Vlocity to the Business Rules
    Engine in Salesforce.

The following are the classes in the `BusinessRule`
                            namespace.

- 
**[CalculationMatrixMigrationService Class](./apex_class_BusinessRule_CalculationMatrixMigrationService.htm.md#apex_class_BusinessRule_CalculationMatrixMigrationService)**  

Contains methods for migrating calculation matrices from the Vlocity       package to the Business Rules Engine as decision matrices.

- 
**[CalculationProcedureMigrationService Class](./apex_class_BusinessRule_CalculationProcedureMigrationService.htm.md#apex_class_BusinessRule_CalculationProcedureMigrationService)**  

Contains methods for migrating calculation procedures from the Vlocity       package to the Business Rules Engine as expression sets.

#### See Also

- [*Apex Developer Guide*: Getting Started with Apex](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/apex_intro_get_started.htm)

=== ARTICLE: business_rules_engine.htm ===
---
page_id: business_rules_engine.htm
title: Business Rules Engine
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business Rules Engine

Business Rules Engine is a suite of services, components, and objects that can be used to
  create business rules that perform complex lookups and calculations. The key components of
  Business Rules Engine are expression sets, decision matrices, and decision tables.

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

- 
**[Expression Set](./expression_set_parent.htm.md)**  

Expression sets consist of a series of steps connected in a logical flow built from         variables, constants, conditions, calculations, lookups, and aggregations.

- 
**[Decision Table](./decision_table.htm.md)**  

A decision table provides outcomes for one or more fields of a standard or custom     object based on the business rules that you define. The business rules can be part of a standard     or custom object, or a custom metadata type.

- 
**[Decision Explainer for Expression Set](./decision_explainer_bre_parent.htm.md)**  

Decision Explainer is an audit-like service that can be used by applications to store         their application data to explain past events. The stored data can be retrieved later for         reporting through custom-built user interfaces.         

- 
**[Lookup Tables](./lookup_tables_parent.htm.md)**  

Business Rules Engine has two types of lookup tables—decision matrices and decision         tables. Learn more about the developer resources of lookup tables for integration with         Flows, Omniscripts, or any third-party custom tools.

#### See Also

- [*Salesforce Help*: Permission Sets for Business Rules Engine](https://help.salesforce.com/s/articleView?id=ind.bre_permission_sets.htm&type=5&language=en_US)

=== ARTICLE: connect_requests_business_rules_input.htm ===
---
page_id: connect_requests_business_rules_input.htm
title: Business Rules Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_business_rules_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business Rules Input

Input representation of an expression set.

        
          

**JSON example 1**

          
: 
            

```
{
  "inputs": [
    {
      "age": "25",
      "state": "CA",
      "PatientId": "001xx000003GYjnAAG"
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z",
    "useDatesOnly": "true",
    "actionContextCode": "9QLxx0000004C92GAE",
    "explainabilitySpecName": "ES_One_Explainability"
  }
}
```

          

        
        
          

**JSON example 2**

          
: 
            

```
{
  "inputs": [
    {
      "age": "25",
      "state": "CA",
      "PatientId":"001xx000003GYjnAAG",
      "__actionContextCode":"001xx000003GYjnAAG"
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z",
    "useDatesOnly": "true"
  }
}

```

            

#### Note

You can use more than one `actionContextCode`
              for multiple sets of inputs, passed in a single API call. 

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

#### 

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | Map<String, Object>[] | List of inputs passed to an expression set. An input may contain multiple variables. Note If the expression set uses a field alias as a variable, append Id to the object alias to which the field alias belongs, and pass the ID of the source object linked to the object alias. If the expression set uses a context definition, append Id to the context definition developer name and pass the context ID as the value. | Required | 55.0 |
| `options` | [Expression Set Options Input](./connect_requests_options.htm.md) | The options for executing an expression set. | Optional | 55.0 |

=== ARTICLE: connect_requests_context_definition_input.htm ===
---
page_id: connect_requests_context_definition_input.htm
title: Context Definition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_context_definition_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Input

Input representation of the context definitions in an expression
      set.

**Root XML tag**

: `<ContextDefinitionInput>`

**JSON example**

: 
            

```

  "contextDefinitionList": {
      "contextDefinitions":[{
      "id":"11Oxx0000006PcLEAU"
      }]
  }
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the context definition. | Required | 58.0 |
| `name` | String | Developer name of the context definition. | Optional | 58.0 |

=== ARTICLE: connect_requests_decision_matrix_input.htm ===
---
page_id: connect_requests_decision_matrix_input.htm
title: Decision Matrix Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Input

Input representation of the inputs passed to a decision matrix for
      lookup.

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `input` | [Decision Matrix Variable List](./connect_requests_decision_matrix_variable.htm.md) | List of variables in an input. | Required | 55.0 |

=== ARTICLE: connect_requests_decision_matrix_lookup.htm ===
---
page_id: connect_requests_decision_matrix_lookup.htm
title: Decision Matrix Lookup Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_lookup.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Lookup Input

Input representation of the input for a decision matrix
    lookup.

      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": [
    {
      "input": [
        {
          "name": "Premium",
          "value": "2400"
        }
      ]
    },
    {
      "input": [
        {
          "name": "Tenure",
          "value": "10"
        }
      ]
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z"
  }
}
```

          

        
        
          
: Here, `Premium` and `Tenure` are column
            headers in the matrix, and `2400` and `10` are
            values of a cell in the column.

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | [Decision Matrix Input](./connect_requests_decision_matrix_input.htm.md) | List of inputs passed to a decision matrix. An input may contain multiple variables. | Required | 55.0 |
| `options` | [Decision Matrix Options Input](./connect_requests_decision_matrix_options.htm.md) | The lookup options for a decision matrix. | Optional | 55.0 |

=== ARTICLE: connect_requests_decision_matrix_options.htm ===
---
page_id: connect_requests_decision_matrix_options.htm
title: Decision Matrix Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_options.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Options Input

Input representation of the options used to look up a decision
      matrix.

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `effectiveDate` | String | The date from when a decision matrix version comes into effect. The date format is yyyy-mm-dd’T’hh:mm:ss’Z. | Optional | 55.0 |
| `useDatesOnly` | String | Specifies that only the date portion (yyyy-mm-dd) of the value of the effectiveDate field be used at the time of execution. | Optional | 55.0 |

=== ARTICLE: connect_requests_decision_matrix_variable.htm ===
---
page_id: connect_requests_decision_matrix_variable.htm
title: Decision Matrix Variable Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_matrix_variable.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Variable Input

Input representation of the variables in an input passed to a decision
      matrix lookup.

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | The name of the variable. | Required | 55.0 |
| `value` | Object | The value assigned to the variable. | Required | 55.0 |

=== ARTICLE: connect_requests_decision_model_export_input.htm ===
---
page_id: connect_requests_decision_model_export_input.htm
title: Decision Model Export Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_model_export_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Model Export Input

Input representation of the request to export decision matrix
      data.

**JSON example**

: 

```
{
   "decisionModelEntityIds":[
      “0lNRO00000004f72AA”,
      “0lNRO000000rfn27AA”
   ]
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `decision​Model​EntityIds` | String[] | A list of decision matrix version IDs to export data from. | Required | 58.0 |

=== ARTICLE: connect_requests_decision_table_bulk_input.htm ===
---
page_id: connect_requests_decision_table_bulk_input.htm
title: Decision Table Bulk Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_bulk_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Bulk Input

Input representation of the Decision Table bulk
      lookup.

      
         
            
               

**JSON example**

               
: 
                  

```
{
   "datasetLinkName" : "transactionMapping",
   “conditions” :[
      {
        “conditionsList”: [
          {
              "fieldName": "Product__c",
              "value": "Nike",
              "operator": "Matches" //Operator is optional
          },
          {
              "fieldName": "Price__c",
              "value": 1000,
              "operator": "GreaterThan"
          }
        ]
      },
      {
        “conditionsList”: [
          {
              "fieldName": "Product__c",
              "value": "Adidas",
              "operator": "Matches" //Operator is optional
          },
          {
              "fieldName": "Price__c",
              "value": 1500,
              "operator": "GreaterThan"
          }
        ]

```

               

            
            
               

**Properties**

               
: 
                  

                        
                        
                        
                        
                        
                        
                           
                              

                              

                              

                              

                              

                           

                        

                        
                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `conditions` | [Decision Table Condition List](./connect_requests_decision_table_condition_list_input.htm.md) | The list of decision table conditions on which the decision table executes and provides outcomes. | Required | 58.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 58.0 |

=== ARTICLE: connect_requests_decision_table_condition.htm ===
---
page_id: connect_requests_decision_table_condition.htm
title: Decision Table Condition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_condition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Condition Input

Input representation of the decision table condition.

    
      

#### Note

        

IsDeleted and LastModifiedDate are not supported in Decision Table Condition Input.

      

    

**Properties**

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

#### 

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

#### 

                                        

                                    

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fieldName` | String | The field name that is selected as an input for the decision table. | Required | 55.0 |
| `value` | String | The value of the data type that is selected as an input. Specify the value of a decision table’s group-by field in double quotes, which is also applicable for numeric or integer type fields. For example, specify `"value": "1000"` for a Price numeric type field, and `"value" : "102.0"` for a Number integer type field. | Required | 55.0 |
| `operator` | String | The operator used for the input field. Valid values are: `DoesNotExistIn`—Use to check if the input value doesn’t exist in a multi-select picklist. `Equals`—Use to check if the input value equals to the configured value in the rule. `ExistsIn`—Use to check if the input value exists in a multi-select picklist. `GreaterOrEqual`—Use to check if the input value is greater than or equal to the configured value in the rule. `GreaterThan`—Use to check if the input value is greater than the configured value in the rule. `LessOrEqual`—Use to check if the input value is less than or equal to the configured value in the rule. `LessThan`—Use to check if the input value is less than the configured value in the rule. `Matches`—Use to check if the input value is a substring of the value in the rule. `NotEquals`—Use to check if the input value doesn’t equal to the configured value in the rule. Note The operator specified here overrides the operator defined in Decision Table. | Optional | 55.0 |
| `sourceObject` | String | The name of the source object for the input field. If the dataset link is configured with a single source object, the source object field isn’t mandatory. | Optional Note This field is required only when the dataset link definition contains multiple source objects. | 55.0 |

#### See Also

- [Supported Data Types and Operators](https://help.salesforce.com/s/articleView?id=ind.reference_decision_table_data_type_operator.htm&type=5&language=en_US)

=== ARTICLE: connect_requests_decision_table_condition_list_input.htm ===
---
page_id: connect_requests_decision_table_condition_list_input.htm
title: Decision Table Condition List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_condition_list_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Condition List Input

Input representation of the Decision Table condition
      list.

      
         
            
               

**Properties**

               
: 
                  

                        
                        
                        
                        
                        
                        
                           
                              

                              

                              

                              

                              

                           

                        

                        
                           
                              

                              

                              

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `conditions` | [Decision Table Condition](./connect_requests_decision_table_condition.htm.md)[] | The details of the decision table conditions on which the decision table executes and provides outcomes. | Required | 58.0 |

=== ARTICLE: connect_requests_decision_table_definition_input.htm ===
---
page_id: connect_requests_decision_table_definition_input.htm
title: Decision Table Definition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_definition_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Definition Input

Input representation of a decision table
      definition.

      
         
            
               

**Properties**

               
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

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `collectOperator` | String | Operator to apply a filter to outputs. Valid values are: `Count` `Maximum` `Minimum` `None` `Sum` | Optional | 58.0 |
| `condition​Criteria` | String | Custom logic applied on the decision table columns to decide how the input fields are processed. | OptionalRequired when the condition type is `Custom`. | 58.0 |
| `conditionType` | String | Condition logic for input fields. Valid values are: `All` `Any` `Custom` | Optional | 58.0 |
| `description` | String | Description of the decision table. | Optional | 58.0 |
| `decision​Result​Policy` | String | Results policy to filter results of the decision table. Valid values are: `AnyValue` `CollectOperator—For internal use only` `FirstMatch` `OutputOrder` `Priority—For internal use only` `RuleOrder—For internal use only` `UniqueValues—For internal use only` | Optional | 58.0 |
| `doesConsider​NullValue` | Boolean | Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is `false`. | Optional | 60.0 |
| `fullName` | String | Unique name of the rule definition. | Required | 58.0 |
| `isSet​Collect​Operator` | Boolean | For internal use only.Indicates whether the `collectOperator` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Criteria` | Boolean | For internal use only. Indicates whether the `conditionCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Type` | Boolean | For internal use only. Indicates whether the `conditionType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Description` | Boolean | For internal use only. Indicates whether the `description` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Decision​ResultPolicy` | Boolean | For internal use only. Indicates whether the `DecisionResultPolicy` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetFullName` | Boolean | For internal use only. Indicates whether the `FullName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetParameters` | Boolean | For internal use only. Indicates whether the `parameters` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetSetupName` | Boolean | For internal use only. Indicates whether the `setupName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​conditionLogic` | Boolean | For internal use only. Indicates whether the `sourceConditionLogic` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Criteria` | Boolean | For internal use only. Indicates whether the `sourceCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Object` | Boolean | For internal use only. Indicates whether the `sourceObject` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Type` | Boolean | For internal use only. Indicates whether the `sourceType` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetType` | Boolean | For internal use only. Indicates whether the `type` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetUsageType` | Boolean | For internal use only. Indicates whether the `UsageType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `parameters` | [Decision Table Parameter Input](./connect_requests_decision_table_parameter_input.htm.md)[] | Array of input and output fields for the decision table. | Optional | 58.0 |
| `setupName` | String | Name of the decision table. | Required | 58.0 |
| `source​condition​Logic` | String | Custom logic to filter the decision table rows. | Optional | 58.0 |
| `sourceCriteria` | [Decision Table Source Criteria Input](./connect_requests_decision_table_source_criteria_input.htm.md)[] | Output array representation of source filters for the decision table rows, such as, `fieldName`, `operators`, `valueType`, and more. | Optional | 58.0 |
| `sourceObject` | String | Object containing business rules for the decision table to read. | Required | 58.0 |
| `sourceType` | String | Type of source to obtain decision table data. Valid values are: `CsvUpload` `MultipleSobjects` `SingleSobject` | Required | 58.0 |
| `status` | String | Status of the decision table. Valid values are: `ActivationInProgress` `ActivationInProgress` `Draft` `Inactive` | Required | 58.0 |
| `type` | String | Type of the decision table. Valid values are: `HighVolume` `LowVolume` | Optional | 58.0 |
| `usageType` | String | Process type that uses the decision table. Valid values are: `Pricing` `ProductEligibility` | Optional | 58.0 |

=== ARTICLE: connect_requests_decision_table_input.htm ===
---
page_id: connect_requests_decision_table_input.htm
title: Decision Table Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Input

Input representation of a decision table.

      
         
            
               

**JSON example**

               
: 
                  

```
{
   "conditions":[
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Nike",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1000,
               "operator":"GreaterThan"
            }
         ]
      },
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Adidas",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1500,
               "operator":"GreaterThan"
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
| `conditions` | [Decision Table Condition](./connect_requests_decision_table_condition.htm.md)[] | The list of decision table conditions on which the decision table executes and provides outcomes. | Required | 55.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 55.0 |

=== ARTICLE: connect_requests_decision_table_parameter_input.htm ===
---
page_id: connect_requests_decision_table_parameter_input.htm
title: Decision Table Parameter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_parameter_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Parameter Input

Input representation of parameters defined for the decision
      table.

**Root XML tag**

: 

**Properties**

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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `columnMapping` | String | Source object path for mapping to the column of an entity.Use this field to specify input and output fields from multiple source objects. | Optional | 58.0 |
| `dataType` | String | Data type of the field used. Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `String` | Optional | 58.0 |
| `decimalScale` | Integer | Precision of the field used. | Optional | 58.0 |
| `domainEntity` | String | Entity domain the field is mapped to. | Optional | 58.0 |
| `fieldName` | String | Name of the field to be used in the decision table. | Required | 58.0 |
| `isGroupByField` | Boolean | Indicates whether the field is used to group the business rules of the decision table (`true`) or not (`false`). | Optional | 58.0 |
| `isPriority` | Boolean | Indicates whether it’s a priority field (`true`) or not (`false`). | Optional | 58.0 |
| `maxlength` | Integer | Maximum length of the field used. | Optional | 58.0 |
| `operator` | String | Valid operators for a field based on its usage. Possible values are: `Between` `DoesNotExistIn` `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `LessOrEqual` `LessThan` `Matches` `NotEquals` | Optional | 58.0 |
| `sequence` | Integer | Sequence in which input fields are processed. | Optional | 58.0 |
| `sortType` | String | Type of sorting to be done on the rows of a decision table. Possible values are: `AscNullFirst`- Sort row values in ascending order, showing null values first. `AscNullLast`- Sort row values in ascending order, showing null values last. `DescNullFirst`- Sort row values in descending order, showing null values first. `DescNullLast`- Sort row values in descending order, showing null values last. `None` - Show rows as they are without sorting. | Optional | 58.0 |
| `usage` | String | Usage type for a field. Possible values are: `Input` `Output` | Required | 58.0 |

=== ARTICLE: connect_requests_decision_table_row_list_input.htm ===
---
page_id: connect_requests_decision_table_row_list_input.htm
title: Decision Table Row List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_row_list_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Row List Input

Input representation of the data for a row in the CSV based decision
      table that has to be added or updated.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "id": "1FIxx0000004CSOGA2",
  "rowData": {
    "City": "City3",
    "AssetLevel": "300"
  },
  "action": "update"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action` | String | Action to perform on this row.Valid values are: `Create` `Update` | Optional | 62.0 |
| `id` | String | ID of the decision table tow. | Optional | 62.0 |
| `rowdata` | Map<String, Object> | Key value pair of the decision table row. | Required | 62.0 |

=== ARTICLE: connect_requests_decision_table_rows_list_input.htm ===
---
page_id: connect_requests_decision_table_rows_list_input.htm
title: Decision Table Rows List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_rows_list_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Rows List Input

Input representation of the request to update rows in a CSV based
      decision table.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "rows": [
    {
      "id": "1FIxx0000004CSOGA2",
      "rowData": {
        "City": "City3",
        "AssetLevel": "300"
      },
      "action": "update"
    }
  ]
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `rows` | [Decision Table Row Input](./connect_requests_decision_table_row_list_input.htm.md)[] | List of rows to be updated or added. | Required | 62.0 |

=== ARTICLE: connect_requests_decision_table_source_criteria_input.htm ===
---
page_id: connect_requests_decision_table_source_criteria_input.htm
title: Decision Table Source Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_decision_table_source_criteria_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Source Criteria Input

Input representation of source criteria for the decision
    table.

**Root XML tag**

: 

**Properties**

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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `operator` | String | Operator used in the filter criteria. Possible values are: `Contains` `DoesNotContain` `Equals` `GreaterThan` `GreaterThanOrEqual` `IsNotNull` `IsNull` `LessThan` `LessThanOrEqual` `NotEqual` | Required | 58.0 |
| `sequenceNumber` | Integer | Sequence number of the filter criteria in the associated decision table source condition. | Optional | 58.0 |
| `sourceFieldName` | String | Name of the field in the filter criteria. | Required | 58.0 |
| `value` | String | Expected value of the field. | Optional | 58.0 |
| `valueType` | String | Type of a filter value. Possible values are: `Formula` `Literal` `Lookup` `Parameter` `PickList` | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_advanced_condition_step.htm ===
---
page_id: connect_requests_expression_set_advanced_condition_step.htm
title: Expression Set Advanced Condition Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_advanced_condition_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Advanced Condition Step Input

Input representation of an advanced condition step in an expression
      set.

**Root XML tag**

: `<ExpressionSetAdvancedConditionStepInput>`

**JSON example**

: 

```
"advancedCondition" : {
            "conditionLogic" : "1",
              "criteria" : [ {
                "operator" : "Equals",
                "sequenceNumber" : 1,
                "sourceFieldName" : "a",
                "value" : "0",
                "valueType" : "Literal"
              } ],
            "resultParameter" : "condition_output__1"
          }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `condition​Logic` | String | Condition that’s defined for the advanced condition. For example, if all conditions are met or any of the conditions are met. | Required | 58.0 |
| `criteria` | [Expression Set Condition Criteria Input](./connect_requests_expression_set_condition_criteria.htm.md)[] | List of condition criteria in an expression set. | Required | 58.0 |
| `result​Parameter` | String | Expression set definition version variable associated with the result of the step. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_aggregation_step.htm ===
---
page_id: connect_requests_expression_set_aggregation_step.htm
title: Expression Set Aggregation Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_aggregation_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Aggregation Step Input

Input representation of an aggregation step in an expression
    set.

**Root XML tag**

: `<ExpressionSetAggregationStepInput>`

**JSON example**

: 

```
"aggregation" : {
"aggergatedParameter" : "v1",
"aggregateFunction" : "Sum",
"expression" : "SUM ( v2 )"
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
| `aggergated​Parameter` | String | Expression set version variable that’s present on the right side of the aggregation step. | Required | 58.0 |
| `aggregate​Function` | String | Aggregation function of the expression set.Valid values are: `Avg` `Max` `Min` `Sum` | Required | 58.0 |
| `expression` | String | Expression that’s present on the left side of the aggregation step. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_assignment_step.htm ===
---
page_id: connect_requests_expression_set_assignment_step.htm
title: Expression Set Assignment Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_assignment_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Assignment Step Input

Input representation of an assignment step in an expression
    set.

**Root XML tag**

: `<ExpressionSetAssignmentStepInput>`

**JSON example**

: 

```
"assignment" : {
            "assignedParameter" : "b",
            "expression" : "100"
          }
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assigned​Parameter` | String | Expression set version variable that’s present on the right side of the calculation step. | Required | 58.0 |
| `expression` | String | Expression that’s present on the left side of the calculation step. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_condition_criteria.htm ===
---
page_id: connect_requests_expression_set_condition_criteria.htm
title: Expression Set Condition Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_condition_criteria.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Condition Criteria Input

Input representation of a condition criteria in an expression
      set.

**Root XML tag**

: `<ExpressionSetConditionCriteriaInput>`

**JSON example**

: 

```
"criteria" : [ {
                "operator" : "Equals",
                "sequenceNumber" : 1,
                "sourceFieldName" : "a",
                "value" : "0",
                "valueType" : "Literal"
              } ]
```

**Properties**

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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `operator` | String | Condition operator of the expression set.Valid values are: `Contains` `DoesNot​Contain` `Equals` `GreaterThan​OrEquals` `Greater​Than` `IsNot​Null` `IsNull` `LessThan` `LessThan​OrEquals` `NotEqual​To` | Required | 58.0 |
| `sequence​Number` | Integer | The sequence number of the condition in the advanced condition. | Required | 58.0 |
| `sourceField​Name` | String | The expression set version variable associated with the condition criteria. | Required | 58.0 |
| `value` | String | The right-hand side of the condition is specified in this field. | Required | 58.0 |
| `valueType` | String | Criteria value type of the expression set.Valid values are: `Formula` `Literal` `Parameter` | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_condition_expression_step.htm ===
---
page_id: connect_requests_expression_set_condition_expression_step.htm
title: Expression Set Condition Expression Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_condition_expression_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Condition Expression Step

Input representation of an expression set condition
    step.

**Root XML tag**

: `<ExpressionSetConditionExpressionStepInput>`

**JSON example**

: 
            

```
"conditionExpression": {
                "expression": "productName == 'iPhone' && City == 'Los Angeles'",
                "resultParameter": "condition_output__1"
              }
```

          

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `expression` | String | Expression that’s defined for the step. | Required | 58.0 |
| `result​Parameter` | String | Expression set version variable associated with the result of the step. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_custom_element_parameter.htm ===
---
page_id: connect_requests_expression_set_custom_element_parameter.htm
title: Expression Set Custom Element Parameter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_custom_element_parameter.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Custom Element Parameter Input

Input representation of a custom element parameter in an expression
      set.

**Root XML tag**

: `<ExpressionSetCustomElementParameterInput>`

**JSON example**

: 

```
"parameters": [
              {
                "input": true,
                "name": "Divisor",
                "output": false,
                "value": "v1",
                "type": "Parameter"
              },
              {
                "input": true,
                "name": "Dividend",
                "output": false,
                "value": "v2",
                "type": "Parameter"
              },
              {
                "input": false,
                "name": "Answer",
                "output": true,
                "value": "v3",
                "type": "Parameter"
              }
            ]
```

**Properties**

: 

                  
                    

                    

                    
- 
- 
- 
- 
- 

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `input` | Boolean | Indicates whether the custom element parameter is an input parameter (`true`) or not (`false`). | Required | 58.0 |
| `name` | String | Name of the custom element parameter. | Required | 58.0 |
| `output` | Boolean | Indicates whether the custom element parameter is an output parameter (`true`) or not (`false`). | Required | 58.0 |
| `type` | String | Type of custom element parameter. Valid values are: `Formula` `Literal` `Lookup` `Parameter` `Picklist` The default value is `Parameter`. | Optional | 58.0 |
| `value` | String | Name of the expression set variable. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_custom_element_step.htm ===
---
page_id: connect_requests_expression_set_custom_element_step.htm
title: Expression Set Custom Element Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_custom_element_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Custom Element Step Input

Input representation of a custom element step in an expression
      set.

**Root XML tag**

: `<ExpressionSetCustomElementStepInput>`

**JSON example**

: 

```
 "customElement": {
            "parameters": [
              {
                "input": true,
                "name": "Divisor",
                "output": false,
                "value": "v1"
              },
              {
                "input": true,
                "name": "Dividend",
                "output": false,
                "value": "v2"
              },
              {
                "input": false,
                "name": "Answer",
                "output": true,
                "value": "v3"
              }
            ]
          },
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `parameters` | [Expression Set Custom Element Parameter Input](./connect_requests_expression_set_custom_element_parameter.htm.md)[] | List of parameters in a custom element. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_des_token_mapping.htm ===
---
page_id: connect_requests_expression_set_des_token_mapping.htm
title: Expression Set DES Token Mapping Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_des_token_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set DES Token Mapping Input

Input representation of the DES token mapping in an expression set
      version step.

**Root XML tag**

: `<ExpressionSetDesTokenMappingInput>`

**JSON example**

: 

```
"passedMessageTokenMappings": [
{
"expressionSetMessageToken": "price",
"resourceReference": "DM1__Price"
}
],
"failedMessageTokenMappings": [
{
"expressionSetMessageToken": "model",
"resourceReference": "Model"
}
],

"noResultMessageTokenMappings": [
{
"expressionSetMessageToken": "year",
"resourceReference": "Year"
}
]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `resource​Reference` | String | Name of the expression set resource that’s mapped to a token, such as Variable, Constant, or FiledAlias. | Required | 59.0 |
| `expressionSet​MessageToken` | String | Name of the explainability message template token. | Required | 59.0 |

=== ARTICLE: connect_requests_expression_set_input.htm ===
---
page_id: connect_requests_expression_set_input.htm
title: Expression Set Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Input

Input representation of the expression set create and update
      request.

**Root XML tag**

: `<ExpressionSetInput>`

**JSON example**

: 

```
{
  "name": "CTX Mapping ES",
  "apiName": "CTX_Mapping_ES_1",
  "description": "...",
  "usageType": "Bre",
  "contextDefinitions": [
    {
      "id": "11Oxx0000006PcLEAU"
    }
  ],
  "versions": [
    {
      "name": "CTX_Mapping_ES_1 V1",
      "apiName": "CTX_Mapping_ES_1_V1",
      "description": "Sample CTX Mapping",
      "startDate": "2022-11-14T20:31:47.000+0000",
      "endDate": "2022-11-14T20:31:47.000+0000",
      "versionNumber": 1,
      "rank": 1,
      "enabled": true,
      "showExplExternally": false,
      "steps": [
        {
          "name": "Condition1",
          "description": "Condition step for conditions w.r.t product",
          "sequenceNumber": 1,
          "resultIncluded": true,
          "stepType": "Condition",
          "conditionExpression": {
            "expression": "productName == 'iPhone' && productColor == 'Red'",
            "resultParameter": "condition_output__1"
          }
        }
      ],
      "variables": [
        {
          "name": "productName",
          "collection": false,
          "dataType": "Text",
          "description": "productName",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "productColor",
          "collection": false,
          "dataType": "Text",
          "description": "productColor",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "condition_output__1",
          "dataType": "Boolean",
          "description": "condition_output__1",
          "input": false,
          "output": true,
          "resultStep": "Condition1",
          "type": "Variable"
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
| `apiName` | String | Unique name of the expression set. | Required | 58.0 |
| `context​Definitions` | [Context Definition Input](./connect_requests_context_definition_input.htm.md) | List of context definitions in an expression set. | Optional | 58.0 |
| `description` | String | Description of the expression set. | Optional | 58.0 |
| `name` | String | Name of the expression set. | Required | 58.0 |
| `usage​Type` | String | Usage type of the expression set. Valid value is `Bre`. The default value is `Bre`. When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. | Required | 58.0 |
| `versions` | [Expression Set Version Input](./connect_requests_expression_set_version.htm.md)[] | List of the expression set versions. | Optional | 58.0 |

=== ARTICLE: connect_requests_expression_set_lookup_table_step.htm ===
---
page_id: connect_requests_expression_set_lookup_table_step.htm
title: Expression Set Lookup Table Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_lookup_table_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Lookup Table Step Input

Input representation of a lookup table step in an expression
    set.

**Root XML tag**

: `<ExpressionSetLookupTableStepInput>`

**JSON example**

: 

```

              "lookupTable": {
                "lookupTableName": "DM_for_test",
                "type": "DecisionMatrix"
              }
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `lookup​TableName` | String | Decision matrix or decision table name that’s used in the lookup table step. | Required | 58.0 |
| `type` | String | Lookup table type of the expression set.Valid values are: `DecisionMatrix` `DecisionTable` | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_sub_expression_step.htm ===
---
page_id: connect_requests_expression_set_sub_expression_step.htm
title: Expression Set SubExpression Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_sub_expression_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set SubExpression Step Input

Input representation of a subexpression step in an expression
      set.

**Root XML tag**

: `<ExpressionSetSubExpressionStepInput>`

**JSON example**

: 

```

              "subExpression": {
                "expressionSet": "EPC_ExpressionSet_NoVersions"
              }
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `expression​Set` | String | Expression set name that’s used in the subexpression set step. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_version.htm ===
---
page_id: connect_requests_expression_set_version.htm
title: Expression Set Version Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_version.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Input

Input representation of an expression set version.

**Root XML tag**

: `<ExpressionSetVersionInput>`

**JSON example**

: 

```
"versions": [
    {
      "description": null,
      "endDate": "2023-03-29T13:08:36.000+0000",
      "name": "ExpressionSet DM V1",
      "apiName": "ExpressionSet_DM_V1",
      "showExplExternally": false,
      "startDate": "2023-02-16T13:08:36.000+0000",
      "enabled": false,
      "steps": [
        {
          "actionType": null,
          "advancedCondition": null,
          "aggregation": null,
          "assignment": null,
          "conditionExpression": {
            "expression": "productName == 'iPhone' && City == 'Los Angeles",
            "resultParameter": "condition_output__1"
          },
          "customElement": null,
          "lookupTable": null,
          "description": "Condition step for conditions w.r.t product",
          "failedExplainerTemplate": null,
          "name": "Condition1",
          "parentStep": null,
          "passedExplainerTemplate": null,
          "resultIncluded": true,
          "sequenceNumber": 1,
          "shouldExposeExecPathMsgOnly": false,
          "shouldExposeConditionDetails": false,
          "shouldShowExplExternally": false,
          "stepType": "Condition",
          "subExpression": null
        },
        {
          "actionType": "GetOutputsFromDecisionMatrix",
          "advancedCondition": null,
          "aggregation": null,
          "assignment": null,
          "conditionExpression": null,
          "customElement": null,
          "lookupTable": {
            "lookupTableName": "DM_for_test",
            "type": "DecisionMatrix"
          },
          "description": null,
          "failedExplainerTemplate": null,
          "name": "DM_for_test",
          "parentStep": null,
          "passedExplainerTemplate": null,
          "resultIncluded": true,
          "sequenceNumber": 2,
          "shouldExposeExecPathMsgOnly": true,
          "shouldExposeConditionDetails": false,
          "shouldShowExplExternally": false,
          "stepType": "BusinessKnowledgeModel",
          "subExpression": null
        }
      ],
      "variables": [
        {
          "collection": false,
          "dataType": "Text",
          "decimalPlaces": 2,
          "description": null,
          "input": true,
          "lookupName": "DM_for_test",
          "lookupType": "DecisionMatrix",
          "name": "City",
          "objectName": null,
          "output": false,
          "resultStep": null,
          "type": "Variable",
          "value": null
        },
        {
          "collection": false,
          "dataType": "Text",
          "decimalPlaces": null,
          "description": null,
          "input": false,
          "lookupName": "DM_for_test",
          "lookupType": "DecisionMatrix",
          "name": "DM_for_test__State",
          "objectName": null,
          "output": true,
          "resultStep": null,
          "type": "Variable",
          "value": null
        },
        {
          "collection": false,
          "dataType": "Text",
          "decimalPlaces": null,
          "description": "productName",
          "input": true,
          "lookupName": null,
          "lookupType": null,
          "name": "productName",
          "objectName": null,
          "output": false,
          "resultStep": null,
          "type": "Variable",
          "value": null
        },
        {
          "collection": false,
          "dataType": "Boolean",
          "decimalPlaces": null,
          "description": "condition_output__1",
          "input": false,
          "lookupName": null,
          "lookupType": null,
          "name": "condition_output__1",
          "objectName": null,
          "output": true,
          "resultStep": "Condition1",
          "type": "Variable",
          "value": null
        }
      ],
      "versionNumber": 1
    }
  ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | API name of the version. | Required | 58.0 |
| `description` | String | Description of the version. | Optional | 58.0 |
| `enabled` | Boolean | Indicates whether the version is active (`true`) or inactive (`false`). | Required | 58.0 |
| `endDate` | String | Effective end date of the version. | Required | 58.0 |
| `id` | String | ID of expression set version. | Optional | 58.0 |
| `name` | String | Name of the version. | Required | 58.0 |
| `rank` | Integer | Rank of the version. | Optional | 58.0 |
| `show​Expl​Externally` | Boolean | Indicates whether the decision explanation is exposed to community users (`true`) or not (`false`). | Required | 58.0 |
| `start​Date` | String | Effective start date of the version. | Required | 58.0 |
| `steps` | [Expression Set Version Step Input](./connect_requests_expression_set_version_step.htm.md)[] | List of steps in an expression set. | Optional | 58.0 |
| `variables` | [Expression Set Version Variable Input](./connect_requests_expression_set_version_variable.htm.md)[] | List of variables in an expression set. | Optional | 58.0 |
| `version​Number` | Integer | Version number of the expression set version. | Required | 58.0 |

=== ARTICLE: connect_requests_expression_set_version_step.htm ===
---
page_id: connect_requests_expression_set_version_step.htm
title: Expression Set Version Step Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_version_step.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Step Input

Input representation of a step in an expression set
    version.

**Root XML tag**

: `<ExpressionSetVersionStepInput>`

**JSON example**

: 

```
"steps": [
            {
              "actionType": null,
              "advancedCondition": null,
              "aggregation": null,
              "assignment": null,
              "conditionExpression": {
                "expression": "productName == 'iPhone' && City == 'Los Angeles'",
                "resultParameter": "condition_output__1"
              },
              "customElement": null,
              "lookupTable": null,
              "description": "Condition step for conditions w.r.t product",
              "failedExplainerTemplate": "FailureTemplate",
              "failedMessageTokenMappings": [
              {
              "expressionSetMessageToken": "model",
              "resourceReference": "Model"
              }],
              "name": "Condition1",
              "noResultExplainerTemplate": "NoResultTemplate",
              "noResultMessageTokenMappings": [
              {
              "expressionSetMessageToken": "year",
              "resourceReference": "Year"
              }],
              "parentStep": null,
              "passedExplainerTemplate": "SuccessTemplate",
              "passedMessageTokenMappings": [
              {
              "expressionSetMessageToken": "price",
              "resourceReference": "DM1__Price"
              }],
              "resultIncluded": true,
              "sequenceNumber": 1,
              "shouldExposeExecPathMsgOnly": false,
              "shouldExposeConditionDetails": false,
              "shouldShowExplExternally": false,
              "stepType": "Condition",
              "subExpression": null
            }
          ]

```

**Properties**

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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action​Type` | String | Business Knowledge Model of the expression set.Valid values are: `AiAccelerator​SubscriberChurn​Prediction` `AssignBadge​ToMember` `AssignParameter​Values` `Automated​Claims​Processing​Validation` `BreAggregator` `BreAggregator​Assignment` `ChangeMember​Tier` `CheckMember​BadgeAssignment` `CreditPoints` `Crud` `DebitPoints` `Evaluate​Qualification` `Evaluate​Disqualification` `GetMember​Attributes​Values` `GetMember​PointBalance` `GetMember​Promotions` `GetMemberTier` `GetOutputs​FromDecision​Matrix` `GetOutputs​FromDecision​Table` `GetUser​Data` `IncreaseUsage​ForCumulative​Promotion` `IssueVoucher` `List​Group​Calculation` `PriceAdjustmentMatrix` `PriceList` `RecordAlert` `Redeem​Voucher` `RunFlow` `RunProgram​Process` `SampleBusiness​ElementWith​Context` `SampleDynamic​Custom​Element` `SendMail` `TestCustom​Element` `UpdateCurrent​ValueFor​MemberAttribute` `UpdatePoint​Balance` `UpdateUsage​ForCumulative​Promotion` `VolumeDiscount` | Optional | 58.0 |
| `advanced​Condition` | [Expression Set Advanced Condition Step Input](./connect_requests_expression_set_advanced_condition_step.htm.md) | Details of the advanced condition if the step is an advanced condition step. | Optional | 58.0 |
| `aggregation` | [Expression Set Aggregation Step Input](./connect_requests_expression_set_aggregation_step.htm.md) | Aggregation details if the step is an aggregation step. | Optional | 58.0 |
| `assignment` | [Expression Set Assignment Step Input](./connect_requests_expression_set_assignment_step.htm.md) | Assignment details if the step is an assignment step. | Optional | 58.0 |
| `condition​Expression` | [Expression Set Condition Expression Step Input](./connect_requests_expression_set_condition_expression_step.htm.md) | Details of the condition if the step is a condition step. | Optional | 58.0 |
| `custom​Element` | [Expression Set Custom Element Step Input](./connect_requests_expression_set_custom_element_step.htm.md) | Details of the custom element if the step is a custom element step. | Optional | 58.0 |
| `description` | String | Description of the step. | Optional | 58.0 |
| `failed​Explainer​Template` | String | Name of the failed explainability message template. | Optional | 58.0 |
| `failed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_requests_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the failed explainability message template. | Optional | 59.0 |
| `lookup​Table` | [Expression Set Lookup Table Step Input](./connect_requests_expression_set_lookup_table_step.htm.md) | Details of the lookup table for a decision matrix or decision table step. | Optional | 58.0 |
| `name` | String | Unique name of the step in the expression set version. | Required | 58.0 |
| `noResult​Explainer​Template` | String | Name of the explainability message template that’s used when the evaluation result of the selected element type is No Result. This field is applicable for a Decision Table only. | Optional | 59.0 |
| `noResult​MessageToken​Mappings` | [Expression Set DES Token Mapping](./connect_requests_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the no result explainability message template. | Optional | 59.0 |
| `parent​Step` | String | Unique name of the parent step in the expression set version. | Optional | 58.0 |
| `passed​Explainer​Template` | String | Name of the passed explainability message template. | Optional | 58.0 |
| `passed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_requests_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the passed explainability message template. | Optional | 59.0 |
| `result​Included` | Boolean | Indicates whether to include the step output in the expression set result (`true`) or not (`false`). | Optional | 58.0 |
| `sequence​Number` | Integer | Sequence number of the step in the expression set version. | Required | 58.0 |
| `shouldExpose​ExecPathMsg​Only` | Boolean | Indicates whether the decision explanation includes information about the executed path only (`true`) or not (`false`) for the Branch element type. | Optional | 58.0 |
| `should​ExposeCondition​Details` | Boolean | Indicates whether the decision explanation includes the condition details (`true`) or not (`false`) for the Condition element type. | Optional | 58.0 |
| `shouldShow​Expl​Externally` | Boolean | Indicates whether the decision explanation is exposed to community users for the step (`true`) or not (`false`). | Optional | 58.0 |
| `step​Type` | String | Step type of the expression set.Valid values are: `Advanced​Condition` `Advanced​ListFilter`—Available in version 59.0 and later. `Branch` `Business​Knowledge​Model` `Condition` `DefaultPath` `ListFilter`—Available in version 59.0 and later. `ListGroup`—Available in version 59.0 and later. `SubExpression` | Required | 58.0 |
| `sub​Expression` | [Expression Set Sub Expression Step Input](./connect_requests_expression_set_sub_expression_step.htm.md) | Details of the subexpression if the step is a subexpression step. | Optional | 58.0 |

=== ARTICLE: connect_requests_expression_set_version_variable.htm ===
---
page_id: connect_requests_expression_set_version_variable.htm
title: Expression Set Version Variable Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_expression_set_version_variable.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Variable Input

Input representation of a variable in an expression set
    version.

**Root XML tag**

: `<ExpressionSetVersionVariableInput>`

**JSON example**

: 

```
          "variables": [
            {
              "collection": false,
              "dataType": "Text",
              "decimalPlaces": 2,
              "description": null,
              "input": true,
              "lookupName": "DM_for_test",
              "lookupType": "DecisionMatrix",
              "name": "City",
              "objectName": null,
              "output": false,
              "resultStep": null,
              "type": "Variable",
              "value": null
            },
            {
              "collection": false,
              "dataType": "Text",
              "decimalPlaces": null,
              "description": null,
              "input": false,
              "lookupName": "DM_for_test",
              "lookupType": "DecisionMatrix",
              "name": "DM_for_test__State",
              "objectName": null,
              "output": true,
              "resultStep": null,
              "type": "Variable",
              "value": null
            },
            {
              "collection": false,
              "dataType": "Text",
              "decimalPlaces": null,
              "description": "productName",
              "input": true,
              "lookupName": null,
              "lookupType": null,
              "name": "productName",
              "objectName": null,
              "output": false,
              "resultStep": null,
              "type": "Variable",
              "value": null
            },
            {
              "collection": false,
              "dataType": "Boolean",
              "decimalPlaces": null,
              "description": "condition_output__1",
              "input": false,
              "lookupName": null,
              "lookupType": null,
              "name": "condition_output__1",
              "objectName": null,
              "output": true,
              "resultStep": "Condition1",
              "type": "Variable",
              "value": null
            }
          ]
```

**Properties**

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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `collection` | Boolean | Indicates whether the variable is a collection (`true`) or not (`false`). | Optional | 58.0 |
| `data​Type` | String | Data type of the variable in an expression set version.Valid values are: `Action​Output` `Boolean` `Currency` `Date` `Date​Time` `Decision​Matrix` `Decision​Table` `Numeric` `Percent` `Sobject` `Sub​Expression` `Text` | Required | 58.0 |
| `decimal​Places` | Integer | Number of decimal places allowed for the value of the variable. | Optional | 58.0 |
| `description` | String | Description of the variable. | Optional | 58.0 |
| `input` | Boolean | Indicates whether the variable is an input of an expression set version (`true`) or not (`false`). | Optional | 58.0 |
| `lookup​Name` | String | API name of the decision matrix, decision table, or subexpression. | Optional | 58.0 |
| `lookup​Type` | String | Lookup type of the variable in an expression set version.Valid values are: `Decision​Matrix` `Decision​Table` `Sub​Expression` | Optional | 58.0 |
| `name` | String | Name of the variable. | Required | 58.0 |
| `object​Name` | String | Name of the object when the variable is of the sObject type. | Optional | 58.0 |
| `output` | Boolean | Indicates whether the variable is output of an expression set version (`true`) or not (`false`). | Optional | 58.0 |
| `result​Step` | String | Name of the step that’s assigning the value to this variable. | Optional | 58.0 |
| `type` | String | Type of the variable in an expression set.Valid values are: `Constant` `Formula` `Variable` | Required | 58.0 |
| `value` | String | Represents a value for a constant variable type and represents a formula for a formula variable type. | Optional | 58.0 |

=== ARTICLE: connect_requests_options.htm ===
---
page_id: connect_requests_options.htm
title: Expression Set Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_options.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Options Input

Input representation of the options for executing an expression
      set.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": [
    {
      "age": "25",
      "state": "CA",
      "PatientId": "001xx000003GYjnAAG"
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z",
    "useDatesOnly": "true",
    "actionContextCode": "9QLxx0000004C92GAE",
    "explainabilitySpecName": "ES_One_Explainability"
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

#### 

                    

                    

                  

                  
                    

                    

                    

#### 

                    

                    

                  

                  
                    

                    

                    

#### 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `actionContext​Code` | String | The code of the action context used to log explainability for a specific execution of an expression set. Note To exclude decision explanations for expression set version steps from action logs, ensure that you exclude the `actionContextCode` and `explainabilitySpecName` properties from the payload. | Optional | 55.0 |
| `effectiveDate` | String | The date from which an expression set comes into effect. The date format is yyyy-mm-dd’T’hh:mm:ss’Z. Note Multiple versions of an expression set can exist with different date ranges. For example, Version 1 is effective before December 2019, and Version 2 is effective from January 2020 to the present. If you specify `effectiveDate` as "2019-03-15T00:00:00Z", Version 1 is executed. If you do not specify `effectiveDate`, the currently active version, Version 2, is executed. | Optional | 55.0 |
| `explainability​Spec​Name` | String | The name of the explainability specification that is used to log explainability for a specific execution of an expression set. Note To exclude decision explanations for expression set version steps from action logs, ensure that you exclude the `actionContextCode` and `explainabilitySpecName` properties from the payload. | Optional | 55.0 |
| `useDatesOnly` | String | Specifies that only the date portion (yyyy-mm-dd) of the value of effectiveDate field is to be used at the time of execution. | Optional | 55.0 |
| `versionNumber` | String | The version number of the expression set version record. | Optional | 55.0 |

=== ARTICLE: connect_resources_bre_create_expression_set.htm ===
---
page_id: connect_resources_bre_create_expression_set.htm
title: Expression Set (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_create_expression_set.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set (POST)

Creates an expression set in Business Rules Engine. An expression
      set performs a series of calculations by using lookup tables and user-defined variables and
      constants.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/expression-set
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect
/business-rules/expression-set
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**Root XML tag**

: `<ExpressionSetInput>`

**JSON example**

: 

```
{
  "name": "CTX Mapping ES",
  "apiName": "CTX_Mapping_ES_1",
  "description": "...",
  "usageType": "Bre",
  "contextDefinitions": [
    {
      "id": "11Oxx0000006PcLEAU"
    }
  ],
  "versions": [
    {
      "name": "CTX_Mapping_ES_1 V1",
      "apiName": "CTX_Mapping_ES_1_V1",
      "description": "Sample CTX Mapping",
      "startDate": "2022-11-14T20:31:47.000+0000",
      "endDate": "2022-11-14T20:31:47.000+0000",
      "versionNumber": 1,
      "rank": 1,
      "enabled": true,
      "showExplExternally": false,
      "steps": [
        {
          "name": "Condition1",
          "description": "Condition step for conditions w.r.t product",
          "sequenceNumber": 1,
          "resultIncluded": true,
          "stepType": "Condition",
          "conditionExpression": {
            "expression": "productName == 'iPhone' && productColor == 'Red'",
            "resultParameter": "condition_output__1"
          }
        }
      ],
      "variables": [
        {
          "name": "productName",
          "collection": false,
          "dataType": "Text",
          "description": "productName",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "productColor",
          "collection": false,
          "dataType": "Text",
          "description": "productColor",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "condition_output__1",
          "dataType": "Boolean",
          "description": "condition_output__1",
          "input": false,
          "output": true,
          "resultStep": "Condition1",
          "type": "Variable"
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
| `apiName` | String | Unique name of the expression set. | Required | 58.0 |
| `context​Definitions` | [Context Definition Input](./connect_requests_context_definition_input.htm.md) | List of context definitions in an expression set. | Optional | 58.0 |
| `description` | String | Description of the expression set. | Optional | 58.0 |
| `name` | String | Name of the expression set. | Required | 58.0 |
| `usage​Type` | String | Usage type of the expression set. Valid value is `Bre`. The default value is `Bre`. When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. | Required | 58.0 |
| `versions` | [Expression Set Version Input](./connect_requests_expression_set_version.htm.md)[] | List of the expression set versions. | Optional | 58.0 |

          

        
        
          

**Response body for POST**

          
: [Expression Set Output](./connect_responses_expression_set_output.htm.md)

=== ARTICLE: connect_resources_bre_decision_matrix.htm ===
---
page_id: connect_resources_bre_decision_matrix.htm
title: Decision Matrix Lookup (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_decision_matrix.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Lookup (POST)

Performs a lookup on decision matrix rows based on the input values
      provided, and returns the row’s output.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-matrices/${matrixName}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/vXX.X/connect
/business-rules/decision-matrices/InsurancePremium
```

          

        
        
          

**Available version**

          
: 55.0

        
        
          

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
  "inputs": [
    {
      "input": [
        {
          "name": "Premium",
          "value": "2400"
        }
      ]
    },
    {
      "input": [
        {
          "name": "Tenure",
          "value": "10"
        }
      ]
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z"
  }
}
```

          

        
        
          
: Here, `Premium` and `Tenure` are column
            headers in the matrix, and `2400` and `10` are
            values of a cell in the column.

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | [Decision Matrix Input](./connect_requests_decision_matrix_input.htm.md) | List of inputs passed to a decision matrix. An input may contain multiple variables. | Required | 55.0 |
| `options` | [Decision Matrix Options Input](./connect_requests_decision_matrix_options.htm.md) | The lookup options for a decision matrix. | Optional | 55.0 |

          

        
      

          

        
      

      
        
          

**Response body for POST**

          
: [Decision Matrix Lookup Result](./connect_responses_bre_decision_matrix_lookup_result.htm.md)

=== ARTICLE: connect_resources_bre_decision_model_entity.htm ===
---
page_id: connect_resources_bre_decision_model_entity.htm
title: Decision Model Notation Export (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_decision_model_entity.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Model Notation Export (POST)

Export decision matrix data to a file in the DMN (Decision Model
      Notation) format, an easily readable format for business rules designed by Object Management
      Group.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-models/export
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-models/export
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

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
   "decisionModelEntityIds":[
      “0lNRO00000004f72AA”,
      “0lNRO000000rfn27AA”
   ]
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `decision​Model​EntityIds` | String[] | A list of decision matrix version IDs to export data from. | Required | 58.0 |

          

        
        
          

**Response body for POST**

          
: [Decision Model Export Output](./connect_responses_decision_model_export_output.htm.md)

        
      

    

  

#### See Also

- [DMN (Decision Model Notation)](https://www.omg.org/dmn/#:~:text=DMN%20is%20a%20modeling%20language,monitor%20their%20application%3B%20business%20analysts.)

=== ARTICLE: connect_resources_bre_decision_table.htm ===
---
page_id: connect_resources_bre_decision_table.htm
title: Decision Table Lookup (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_decision_table.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Lookup (POST)

Performs a lookup on a decision table.

      
         
            
               

**Resource**

               
: 
                  

```
/connect/business-rules/decision-table/${decisionTableId}
```

               

            
            
               

**Resource Example**

               
: 
                  

```
https://yourInstance.salesforce.com/services/data/v55.0/connect
/decision-table/0lDB0000000TNQzMAO
```

               

            
            
               

**Available version**

               
: 55.0

            
            
               

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
   "conditions":[
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Nike",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1000,
               "operator":"GreaterThan"
            }
         ]
      },
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Adidas",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1500,
               "operator":"GreaterThan"
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
| `conditions` | [Decision Table Condition](./connect_requests_decision_table_condition.htm.md)[] | The list of decision table conditions on which the decision table executes and provides outcomes. | Required | 55.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 55.0 |

               

            
         

               

            
            
               

**Response body for POST**

               
: [Decision Table Outcome](./connect_responses_decision_table_outcome.htm.md)

=== ARTICLE: connect_resources_bre_expression_set.htm ===
---
page_id: connect_resources_bre_expression_set.htm
title: Expression Set Invocation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_expression_set.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Invocation (POST)

Invokes expression sets in Business Rule Engine.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/expressionSet/${expressionSetName}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/vXX.X/connect
/business-rules/expressionSet/${expressionSetName}
```

            
            
          

        
        
          

**Available version**

          
: 55.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example 1**

          
: 
            

```
{
  "inputs": [
    {
      "age": "25",
      "state": "CA",
      "PatientId": "001xx000003GYjnAAG"
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z",
    "useDatesOnly": "true",
    "actionContextCode": "9QLxx0000004C92GAE",
    "explainabilitySpecName": "ES_One_Explainability"
  }
}
```

          

        
        
          

**JSON example 2**

          
: 
            

```
{
  "inputs": [
    {
      "age": "25",
      "state": "CA",
      "PatientId":"001xx000003GYjnAAG",
      "__actionContextCode":"001xx000003GYjnAAG"
    }
  ],
  "options": {
    "effectiveDate": "2022-12-03T10:15:30Z",
    "useDatesOnly": "true"
  }
}

```

            

#### Note

You can use more than one `actionContextCode`
              for multiple sets of inputs, passed in a single API call. 

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

#### 

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | Map<String, Object>[] | List of inputs passed to an expression set. An input may contain multiple variables. Note If the expression set uses a field alias as a variable, append Id to the object alias to which the field alias belongs, and pass the ID of the source object linked to the object alias. If the expression set uses a context definition, append Id to the context definition developer name and pass the context ID as the value. | Required | 55.0 |
| `options` | [Expression Set Options Input](./connect_requests_options.htm.md) | The options for executing an expression set. | Optional | 55.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Business Rules Result](./connect_responses_business_rules_result.htm.md)

=== ARTICLE: connect_resources_bre_expression_set_id_delete_get.htm ===
---
page_id: connect_resources_bre_expression_set_id_delete_get.htm
title: Expression Set (DELETE, GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_expression_set_id_delete_get.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set (DELETE, GET)

Read or delete expression set for a specified expression set
      ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/expression-set/${expressionSetId}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/expression-set/$11Oxx0000006PcLEAU
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: DELETE, GET

        
        
          

**Response body for GET**

          
: [Expression Set Output](./connect_responses_expression_set_output.htm.md)

        
        
          

**Response body for DELETE**

          
: None.

=== ARTICLE: connect_resources_bre_expression_set_id_patch.htm ===
---
page_id: connect_resources_bre_expression_set_id_patch.htm
title: Expression Set (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_expression_set_id_patch.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set (PATCH)

Endpoint to update expression set.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/expression-set/${expressionSetId}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/expression-set/$11Oxx0000006PcLEAU
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: PATCH

        
        
          

**Request body for PATCH**

          
: 
            

**Root XML tag**

: `<ExpressionSetInput>`

**JSON example**

: 

```
{
  "name": "CTX Mapping ES",
  "apiName": "CTX_Mapping_ES_1",
  "description": "...",
  "usageType": "Bre",
  "contextDefinitions": [
    {
      "id": "11Oxx0000006PcLEAU"
    }
  ],
  "versions": [
    {
      "name": "CTX_Mapping_ES_1 V1",
      "apiName": "CTX_Mapping_ES_1_V1",
      "description": "Sample CTX Mapping",
      "startDate": "2022-11-14T20:31:47.000+0000",
      "endDate": "2022-11-14T20:31:47.000+0000",
      "versionNumber": 1,
      "rank": 1,
      "enabled": true,
      "showExplExternally": false,
      "steps": [
        {
          "name": "Condition1",
          "description": "Condition step for conditions w.r.t product",
          "sequenceNumber": 1,
          "resultIncluded": true,
          "stepType": "Condition",
          "conditionExpression": {
            "expression": "productName == 'iPhone' && productColor == 'Red'",
            "resultParameter": "condition_output__1"
          }
        }
      ],
      "variables": [
        {
          "name": "productName",
          "collection": false,
          "dataType": "Text",
          "description": "productName",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "productColor",
          "collection": false,
          "dataType": "Text",
          "description": "productColor",
          "input": true,
          "output": false,
          "type": "Variable"
        },
        {
          "name": "condition_output__1",
          "dataType": "Boolean",
          "description": "condition_output__1",
          "input": false,
          "output": true,
          "resultStep": "Condition1",
          "type": "Variable"
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
| `apiName` | String | Unique name of the expression set. | Required | 58.0 |
| `context​Definitions` | [Context Definition Input](./connect_requests_context_definition_input.htm.md) | List of context definitions in an expression set. | Optional | 58.0 |
| `description` | String | Description of the expression set. | Optional | 58.0 |
| `name` | String | Name of the expression set. | Required | 58.0 |
| `usage​Type` | String | Usage type of the expression set. Valid value is `Bre`. The default value is `Bre`. When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. | Required | 58.0 |
| `versions` | [Expression Set Version Input](./connect_requests_expression_set_version.htm.md)[] | List of the expression set versions. | Optional | 58.0 |

          

        
        
          

**Response body for PATCH**

          
: [Expression Set Output](./connect_responses_expression_set_output.htm.md)

=== ARTICLE: connect_resources_bre_guardrail.htm ===
---
page_id: connect_resources_bre_guardrail.htm
title: Guardrails (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_guardrail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guardrails (GET)

Fetches guardrails from the Business Rules Engine (BRE) to manage rate limits for BRE
    components.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/guardrails
```

          

        
        
          

**Example POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/guardrails
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

- 
- 
- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `componentNames` | String | BRE component to fetch the guardrails. It contains a comma-separated list of predefined components. Valid component values are: `ExpressionSet` `DecisionTable` `DecisionMatrix` `Explainability` `DynamicRules` If no values are provided, guardrails for all components accessible to the user are returned. | Optional | 63.0 |
| `isNotification​Enabled` | Boolean | Indicates whether to return only the guardrails with enabled notifications (`true`) or not (`false`). | Optional | 63.0 |

          

        
        
          

**Response body for GET**

          
: [BRE Guardrails](./connect_responses_bre_guardrails.htm.md)

=== ARTICLE: connect_resources_bre_search_lookup_tables.htm ===
---
page_id: connect_resources_bre_search_lookup_tables.htm
title: Lookup Tables (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_bre_search_lookup_tables.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables (GET)

Retrieve lookup tables.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/lookup-tables
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/lookup-tables?searchKey=D&usageType=Bre&lookupTypes=DecisionTable,DecisionMatrix
```

          

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/lookup-tables?searchKey=D&usageType=Bre
```

          

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/lookup-tables?searchKey=D&usageType=Bre&lookupTypes=DecisionTable&businessKnowledgeModelName=ManualDiscount
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `lookupTypes` | String | Type of lookup table. Valid values are: `DecisionMatrix` `DecisionTable` | Optional | 59.0 |
| `searchKey` | String | The search text entered by the user to retrieve a list of lookup tables. | Required | 59.0 |
| `usageType` | String | Usage type of the lookup table. Valid value is `Bre`. The default value is `Bre`. When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. | Required | 59.0 |

          

        
        
          

**Response body for GET**

          
: [Lookup Tables Result
              List](./connect_responses_lookup_tables_result_list.htm.md)

=== ARTICLE: connect_resources_decisionTableId.htm ===
---
page_id: connect_resources_decisionTableId.htm
title: Decision Table Invocation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decisionTableId.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Invocation (POST)

Invoke a decision table by passing multiple input conditions within
      the same request.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-table/lookup/${decisionTableId}
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect
/business-rules/decision-table/lookup/${0lDD2000000004NMAQ}
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

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
   "datasetLinkName" : "transactionMapping",
   “conditions” :[
      {
        “conditionsList”: [
          {
              "fieldName": "Product__c",
              "value": "Nike",
              "operator": "Matches" //Operator is optional
          },
          {
              "fieldName": "Price__c",
              "value": 1000,
              "operator": "GreaterThan"
          }
        ]
      },
      {
        “conditionsList”: [
          {
              "fieldName": "Product__c",
              "value": "Adidas",
              "operator": "Matches" //Operator is optional
          },
          {
              "fieldName": "Price__c",
              "value": 1500,
              "operator": "GreaterThan"
          }
        ]

```

               

            
            
               

**Properties**

               
: 
                  

                        
                        
                        
                        
                        
                        
                           
                              

                              

                              

                              

                              

                           

                        

                        
                           
                              

                              

                              

                              

                              

                           

                           
                              

                              

                              

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `conditions` | [Decision Table Condition List](./connect_requests_decision_table_condition_list_input.htm.md) | The list of decision table conditions on which the decision table executes and provides outcomes. | Required | 58.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 58.0 |

               

            
         

          

        
        
          

**Response body for POST**

          
: [Decision Table Bulk Outcome](./connect_responses_decision_table_bulk_outcome.htm.md)

=== ARTICLE: connect_resources_decision_table_csv_based_dt.htm ===
---
page_id: connect_resources_decision_table_csv_based_dt.htm
title: CSV Based Decision Table (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_table_csv_based_dt.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CSV Based Decision Table (GET)

Fetch paginated data from a CSV based decision table. This resource is responsible for
    managing rows in a Decision Table.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-table/${decisionTableId}/data
```

          

        
        
          

**Example for GET**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-table/0lDxx0000000001EAA/data?filter=AssetLevel:101
```

          

        
        
          

**Example for POST**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-table/0lDxx0000000001EAA/data
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET POST

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `filter` | String | Filters applied to rows based on column criteria. | Optional | 62.0 |
| `limit` | Integer | Limits the number of records viewed at a time. The default value is `20`. | Optional | 62.0 |
| `offset` | Integer | Token that represents the page offset for pagination. Use this value with the pageSize parameter to indicate where the page starts. The maximum offset is `100` and the default is `0`. | Optional | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Decision Table Rows List](./connect_responses_decision_table_rows_list_output.htm.md)

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "rows": [
    {
      "id": "1FIxx0000004CSOGA2",
      "rowData": {
        "City": "City3",
        "AssetLevel": "300"
      },
      "action": "update"
    }
  ]
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `rows` | [Decision Table Row Input](./connect_requests_decision_table_row_list_input.htm.md)[] | List of rows to be updated or added. | Required | 62.0 |

          

        
      

          

        
        
          

**Request parameters for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `rows​Input` | Object |  |  | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Decision Table Data](./connect_responses_decision_table_data_output.htm.md)

=== ARTICLE: connect_resources_decision_table_definition_details.htm ===
---
page_id: connect_resources_decision_table_definition_details.htm
title: Decision Table Definitions (DELETE, GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_table_definition_details.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Definitions (DELETE, GET)

Get details of a decision table definition. Delete a decision table
      definition associated with a decision table.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-table/definitions/${decisionTableId}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-table/definitions/0lDxx00000002Ur
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: DELETE, GET

        
      

      
        
          

**Response body for DELETE**

          
: [Decision Table
              Output](./connect_responses_decision_table_output.htm.md)

        
        
          

**Response body for GET**

          
: [Decision Table Output](./connect_responses_decision_table_output.htm.md)

=== ARTICLE: connect_resources_decision_table_definition_details_patch.htm ===
---
page_id: connect_resources_decision_table_definition_details_patch.htm
title: Decision Table Definitions (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_table_definition_details_patch.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Definitions (PATCH)

Update a decision table definition associated with a decision
      table.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-table/definitions/${decisionTableId}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-table/definitions/0lDxx00000002Ur
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: PATCH

        
      

      
        
          

**JSON example**

          
: 
            

```
{
   "setupName":"Product Qualificiation eligibility",
   "fullName":"ProductQualificationEligibility",
   "description":"Eligiblity of Products using Qualification Rules",
   "usageType":"ProductEligibility",
   "sourceType":"SingleSobject",
   "sourceObject":"AccountFeed",
   "status":"Draft",
   "decisionResultPolicy":"UniqueValues",
   "doesConsiderNullValue": true,
   "collectOperator":"Count",
   "conditionType":"Any",
   "conditionCriteria":"1 OR 2 OR 3",
   "parameters":[
      {
         "fieldName":"IsDeleted",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"1"
      },
      {
         "fieldName":"Id",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"2"
      },
      {
         "fieldName":"Title",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"3"
      },
      {
         "fieldName":"CreatedById",
         "usage":"OUTPUT"
      }
   ]
}
```

          

        
      

      
        
          

**Request body for PATCH**

          
: 
            
            
               

**Properties**

               
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

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `collectOperator` | String | Operator to apply a filter to outputs. Valid values are: `Count` `Maximum` `Minimum` `None` `Sum` | Optional | 58.0 |
| `condition​Criteria` | String | Custom logic applied on the decision table columns to decide how the input fields are processed. | OptionalRequired when the condition type is `Custom`. | 58.0 |
| `conditionType` | String | Condition logic for input fields. Valid values are: `All` `Any` `Custom` | Optional | 58.0 |
| `description` | String | Description of the decision table. | Optional | 58.0 |
| `decision​Result​Policy` | String | Results policy to filter results of the decision table. Valid values are: `AnyValue` `CollectOperator—For internal use only` `FirstMatch` `OutputOrder` `Priority—For internal use only` `RuleOrder—For internal use only` `UniqueValues—For internal use only` | Optional | 58.0 |
| `doesConsider​NullValue` | Boolean | Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is `false`. | Optional | 60.0 |
| `fullName` | String | Unique name of the rule definition. | Required | 58.0 |
| `isSet​Collect​Operator` | Boolean | For internal use only.Indicates whether the `collectOperator` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Criteria` | Boolean | For internal use only. Indicates whether the `conditionCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Type` | Boolean | For internal use only. Indicates whether the `conditionType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Description` | Boolean | For internal use only. Indicates whether the `description` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Decision​ResultPolicy` | Boolean | For internal use only. Indicates whether the `DecisionResultPolicy` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetFullName` | Boolean | For internal use only. Indicates whether the `FullName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetParameters` | Boolean | For internal use only. Indicates whether the `parameters` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetSetupName` | Boolean | For internal use only. Indicates whether the `setupName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​conditionLogic` | Boolean | For internal use only. Indicates whether the `sourceConditionLogic` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Criteria` | Boolean | For internal use only. Indicates whether the `sourceCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Object` | Boolean | For internal use only. Indicates whether the `sourceObject` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Type` | Boolean | For internal use only. Indicates whether the `sourceType` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetType` | Boolean | For internal use only. Indicates whether the `type` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetUsageType` | Boolean | For internal use only. Indicates whether the `UsageType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `parameters` | [Decision Table Parameter Input](./connect_requests_decision_table_parameter_input.htm.md)[] | Array of input and output fields for the decision table. | Optional | 58.0 |
| `setupName` | String | Name of the decision table. | Required | 58.0 |
| `source​condition​Logic` | String | Custom logic to filter the decision table rows. | Optional | 58.0 |
| `sourceCriteria` | [Decision Table Source Criteria Input](./connect_requests_decision_table_source_criteria_input.htm.md)[] | Output array representation of source filters for the decision table rows, such as, `fieldName`, `operators`, `valueType`, and more. | Optional | 58.0 |
| `sourceObject` | String | Object containing business rules for the decision table to read. | Required | 58.0 |
| `sourceType` | String | Type of source to obtain decision table data. Valid values are: `CsvUpload` `MultipleSobjects` `SingleSobject` | Required | 58.0 |
| `status` | String | Status of the decision table. Valid values are: `ActivationInProgress` `ActivationInProgress` `Draft` `Inactive` | Required | 58.0 |
| `type` | String | Type of the decision table. Valid values are: `HighVolume` `LowVolume` | Optional | 58.0 |
| `usageType` | String | Process type that uses the decision table. Valid values are: `Pricing` `ProductEligibility` | Optional | 58.0 |

               

            
         

          

        
        
          

**Response body for PATCH**

          
: [Decision Table Output](./connect_responses_decision_table_output.htm.md)

=== ARTICLE: connect_resources_decision_table_definition_details_post.htm ===
---
page_id: connect_resources_decision_table_definition_details_post.htm
title: Decision Table Definitions (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_table_definition_details_post.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_table_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Definitions (POST)

Create a decision table definition. A decision table definition
    contains all the details required to create a decision table.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/decision-table/definitions
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect/business-rules/decision-table/definitions
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

        
      

      
        
          

**JSON example for a single object source**

          
: 
            

```
{
   "setupName":"Product Qualificiation eligibility",
   "fullName":"ProductQualificationEligibility",
   "description":"Eligiblity of Products using Qualification Rules",
   "usageType":"ProductEligibility",
   "sourceType":"SingleSobject",
   "sourceObject":"AccountFeed",
   "status":"Draft",
   "decisionResultPolicy":"FirstMatch",
   "doesConsiderNullValue": true,
   "collectOperator":"Count",
   "conditionType":"Any",
   "conditionCriteria":"1 OR 2 OR 3",
   "parameters":[
      {
         "fieldName":"IsDeleted",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"1"
      },
      {
         "fieldName":"Id",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"2"
      },
      {
         "fieldName":"Title",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"3"
      },
      {
         "fieldName":"CreatedById",
         "usage":"OUTPUT"
      }
   ]
}

```

          

        
      

      
        
          

**JSON example for a multi-object source**

          
: 
            

```
{
   "setupName":"Jumbo Pricing Definition",
   "fullName":"JumboPricingDefinition",
   "description":"Join all the DT definitions into one jumbo pricing definition",
   "usageType":"ProductEligibility",
   "type":"LowVolume",
   "sourceType":"MultipleSobjects",
   "sourceObject":"AccountFeed",
   "status":"Draft",
   "decisionResultPolicy":"OutputOrder",
   "doesConsiderNullValue": true,
   "collectOperator":"Count",
   "sourceconditionLogic":"1 AND 2 AND 3",
   "conditionType":"Any",
   "conditionCriteria":"1 OR 2 OR 3 OR 4 OR 5",
   "parameters":[
      {
         "fieldName":"IsDeleted",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"1",
         "columnMapping":"IsDeleted"
      },
      {
         "fieldName":"Id",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"2",
         "columnMapping":"Id"
      },
      {
         "fieldName":"Title",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"3",
         "columnMapping":"Title"
      },
      {
         "fieldName":"OldvalNumber",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"4",
         "columnMapping":"AccountHistory.OldvalNumber"
      },
      {
         "fieldName":"OldvalString",
         "usage":"INPUT",
         "operator":"Equals",
         "sequence":"5",
         "columnMapping":"AccountHistory.OldvalString"
      },
      {
         "fieldName":"CreatedById",
         "usage":"OUTPUT",
         "columnMapping":"CreatedById"
      },
      {
         "fieldName":"NewvalNumber",
         "usage":"OUTPUT",
         "columnMapping":"AccountHistory.NewvalNumber"
      },
      {
         "fieldName":"NewvalString",
         "usage":"OUTPUT",
         "columnMapping":"AccountHistory.NewvalString"
      }
   ]
   "sourceCriteria":[
      {
         "sourceFieldName":"OldvalString",
         "value":"5",
         "operator":"Equals",
         "valueType":"Parameter",
         "sequenceNumber":"1"
      }
   ]
}
```

          

        
      

      
        
          

**Request body for POST**

          
: 
            
            
               

**Properties**

               
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

                              

                              

                           

                        

                     
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `collectOperator` | String | Operator to apply a filter to outputs. Valid values are: `Count` `Maximum` `Minimum` `None` `Sum` | Optional | 58.0 |
| `condition​Criteria` | String | Custom logic applied on the decision table columns to decide how the input fields are processed. | OptionalRequired when the condition type is `Custom`. | 58.0 |
| `conditionType` | String | Condition logic for input fields. Valid values are: `All` `Any` `Custom` | Optional | 58.0 |
| `description` | String | Description of the decision table. | Optional | 58.0 |
| `decision​Result​Policy` | String | Results policy to filter results of the decision table. Valid values are: `AnyValue` `CollectOperator—For internal use only` `FirstMatch` `OutputOrder` `Priority—For internal use only` `RuleOrder—For internal use only` `UniqueValues—For internal use only` | Optional | 58.0 |
| `doesConsider​NullValue` | Boolean | Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is `false`. | Optional | 60.0 |
| `fullName` | String | Unique name of the rule definition. | Required | 58.0 |
| `isSet​Collect​Operator` | Boolean | For internal use only.Indicates whether the `collectOperator` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Criteria` | Boolean | For internal use only. Indicates whether the `conditionCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Condition​Type` | Boolean | For internal use only. Indicates whether the `conditionType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Description` | Boolean | For internal use only. Indicates whether the `description` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Decision​ResultPolicy` | Boolean | For internal use only. Indicates whether the `DecisionResultPolicy` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetFullName` | Boolean | For internal use only. Indicates whether the `FullName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetParameters` | Boolean | For internal use only. Indicates whether the `parameters` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetSetupName` | Boolean | For internal use only. Indicates whether the `setupName` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​conditionLogic` | Boolean | For internal use only. Indicates whether the `sourceConditionLogic` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Criteria` | Boolean | For internal use only. Indicates whether the `sourceCriteria` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Object` | Boolean | For internal use only. Indicates whether the `sourceObject` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSet​Source​Type` | Boolean | For internal use only. Indicates whether the `sourceType` is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetType` | Boolean | For internal use only. Indicates whether the `type` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `isSetUsageType` | Boolean | For internal use only. Indicates whether the `UsageType` field is enabled (`true`) or not (`false`). | Optional | 58.0 |
| `parameters` | [Decision Table Parameter Input](./connect_requests_decision_table_parameter_input.htm.md)[] | Array of input and output fields for the decision table. | Optional | 58.0 |
| `setupName` | String | Name of the decision table. | Required | 58.0 |
| `source​condition​Logic` | String | Custom logic to filter the decision table rows. | Optional | 58.0 |
| `sourceCriteria` | [Decision Table Source Criteria Input](./connect_requests_decision_table_source_criteria_input.htm.md)[] | Output array representation of source filters for the decision table rows, such as, `fieldName`, `operators`, `valueType`, and more. | Optional | 58.0 |
| `sourceObject` | String | Object containing business rules for the decision table to read. | Required | 58.0 |
| `sourceType` | String | Type of source to obtain decision table data. Valid values are: `CsvUpload` `MultipleSobjects` `SingleSobject` | Required | 58.0 |
| `status` | String | Status of the decision table. Valid values are: `ActivationInProgress` `ActivationInProgress` `Draft` `Inactive` | Required | 58.0 |
| `type` | String | Type of the decision table. Valid values are: `HighVolume` `LowVolume` | Optional | 58.0 |
| `usageType` | String | Process type that uses the decision table. Valid values are: `Pricing` `ProductEligibility` | Optional | 58.0 |

               

            
         

          

        
        
          

**Response body for POST**

          
: [Decision Table Output](./connect_responses_decision_table_output.htm.md)

=== ARTICLE: connect_resources_decision_table_execution.htm ===
---
page_id: connect_resources_decision_table_execution.htm
title: Decision Table Execution
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_decision_table_execution.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Execution

Execute an active decision table.

        
          

**Resource**

          
: 
            

```
services/data/vXX.X/connect/business-rules/decision-table/lookup/${decisionTableId}
```

          

        
        
          

**Available version**

          
: 51.0

        
        
          

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
   "conditions":[
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Nike",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1000,
               "operator":"GreaterThan"
            }
         ]
      },
      {
         "conditionsList":[
            {
               "fieldName":"Product__c",
               "value":"Adidas",
               "operator":"Matches"
            },
            {
               "fieldName":"Price__c",
               "value":1500,
               "operator":"GreaterThan"
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
| `conditions` | [Decision Table Condition](./connect_requests_decision_table_condition.htm.md)[] | The list of decision table conditions on which the decision table executes and provides outcomes. | Required | 55.0 |
| `datasetLinkName` | String | The API name of the dataset link provided as an input for the decision table execution. | Optional | 55.0 |

               

            
         

          

        
        
          

**Response body for POST**

          
: [Decision Table Outcome](./connect_responses_decision_table_outcome.htm.md)

        
        
          

**Sample Response body**

          
: 
            

```
{
   “outcomeType” : “Single Match”,
   "outcomeList" : [
      {
         “values” : {
            “Discount_c”: 5
         }
      }
   ]
}

```

=== ARTICLE: connect_resources_expression_set_dependencies.htm ===
---
page_id: connect_resources_expression_set_dependencies.htm
title: Expression Set Version Dependencies (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_expression_set_dependencies.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Dependencies (GET)

Retrieve expression set version dependencies.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/expression-set/version/${expressionSetVersionId}/dependencies
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v58.0/connect/business-rules/expression-set/version/9QARN000000016v4AA/dependencies
```

          

        
        
          

**Available version**

          
: 58.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Response body for GET**

          
: [Expression Set Version Dependency](./connect_responses_expression_set_version_dependency_output.htm.md)

=== ARTICLE: connect_resources_rules_engine_explainability_logs.htm ===
---
page_id: connect_resources_rules_engine_explainability_logs.htm
title: Explainability Logs (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_rules_engine_explainability_logs.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Logs (GET)

Retrieves explainability logs for expression step elements for which
      explanation messages are configured.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/explainability/logs
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect
/business-rules/explainability/logs?actionContextCode=001x0000005DmI3AAK
```

          

        
        
          

**Available version**

          
: 56.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action​Context​Code` | String | The record ID within the context of the associated application's action that’s used to retrieve action logs. | Optional | 56.0 |
| `application​SubType` | String | The subtype of the associated application for which the explainability log is generated. This matches one of the valid values in the ExplainabilityActionDef . `ApplicationSubtype` field. | Optional | 56.0 |
| `application​Type` | String | The name of the application for which the explainability service is run. This matches one of the valid values in the ExplainabilityActionDef .`ApplicationType` field. | Optional | 56.0 |
| `createdAfter` | String | A valid date time after which the explainability log records are returned. | Optional | 56.0 |
| `createdBefore` | String | A valid date time before which the explainability log records are returned. | Optional | 56.0 |
| `pageSize` | Integer | The number of explainability log records to return. The value can range from 200 to 500. | Optional | 56.0 |
| `processType` | String | The process type of the associated application for which the explainability action log is generated. This matches one of the valid values in the ExplainabilityActionDef `ProcessType` field. | Optional | 56.0 |
| `queryMore` | String | A string returned from the previous request, which you must pass to the next request to get the next page. | Optional | 56.0 |

          

        
        
          

**Response body for GET**

          
: [Explainability Logs](./connect_responses_explainability_logs.htm.md)

=== ARTICLE: connect_resources_rules_engine_message_template_detail.htm ===
---
page_id: connect_resources_rules_engine_message_template_detail.htm
title: Explainability Message Template Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_rules_engine_message_template_detail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Message Template Details (GET)

Retrieves the details of an explainability message template for a
      specified template ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/explainability/message-templates/${messageTemplateId}
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect
/business-rules/explainability/message-templates/8U8x00000000027CAA
```

          

        
        
          

**Available version**

          
: 56.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Response body for GET**

          
: [Message Template Details](./connect_responses_message_template_detail_output.htm.md)

=== ARTICLE: connect_resources_rules_engine_message_templates_list.htm ===
---
page_id: connect_resources_rules_engine_message_templates_list.htm
title: Explainability Message Templates (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_rules_engine_message_templates_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Message Templates (GET)

Retrieves a list of explainability message templates that matches
      the given search parameters. 

    
      
        
          

**Resource**

          
: 
            

```
/connect/business-rules/explainability/message-templates
```

          

        
        
          

**Resource Example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/connect
/business-rules/explainability/message-templates?messageType=Passed
```

          

        
        
          

**Available version**

          
: 56.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

#### Note

You must specify at least one parameter as part of the GET request.

            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 
- 
- 
- 
- 
- 

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `isDefault` | Boolean | Specifies whether the message in the explainability message template for an expression set step type is default (`true`) or not (`false`). | Optional | 56.0 |
| `messageType` | String | The message defined for a step when the step result is either passed or failed. | Optional | 56.0 |
| `searchKey` | String | The keyword used to retrieve the list of templates. | Optional | 56.0 |
| `stepType` | String | The type of expression set step element. Pass one of these values for this field: Calculation Branch Condition Decision Matrix Lookup Decision Table Lookup Aggregation Sub Expression Business Element | Optional | 56.0 |

          

        
        
          

**Response body for GET**

          
: [Message Templates List](./connect_responses_message_templates_list_output.htm.md)

=== ARTICLE: connect_responses_bre_decision_matrix_lookup_result.htm ===
---
page_id: connect_responses_bre_decision_matrix_lookup_result.htm
title: Decision Matrix Lookup Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_bre_decision_matrix_lookup_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Lookup Result

Output representation of the individual output of a decision matrix
      version lookup.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "outputs": [
    {
      "results": [],
      "error": "Input Data is Missing"
    },
    {
      "results": [
        {
          "name": "premium",
          "value": "2400"
        },
        {
          "name": "tax",
          "value": "300"
        }
      ]
    },
    {
      "results": [],
      "error": "There is no output for the given input data"
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `outputs` | [Decision Matrix Lookup Basic Result](./connect_responses_decision_matrix_lookup_basic_result.htm.md)[] | List of outputs returned by a decision matrix. An output may contain multiple variables. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_bre_guardrails.htm ===
---
page_id: connect_responses_bre_guardrails.htm
title: BRE Guardrails
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_bre_guardrails.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BRE Guardrails

Output representation of the BRE
    guardrails
    for each component.

        
          

**JSON Sample**

          
: 
            

```
{
  "result": [
    {
      "componentName": "DecisionTable",
      "guardrails": [
        {
          "name": "MaxProcessLimit",
          "guardrailType": "RateLimit",
          "limitValue": "100",
          "currentValue": "50",
          "notificationSupported": true
        }
      ]
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `result` | [BRE Guardrails Result](./connect_responses_bre_guardrails_result.htm.md)[] | Guardrails associated with the specified BRE component. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_bre_guardrails_result.htm ===
---
page_id: connect_responses_bre_guardrails_result.htm
title: BRE Guardrails Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_bre_guardrails_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BRE Guardrails Result

Output representation of the BRE Guardrails result.

        
          

**JSON Sample**

          
: 
            

```
{
  "result": [
    {
      "componentName": "DecisionTable",
      "guardrails": [
        {
          "name": "MaxProcessLimit",
          "guardrailType": "RateLimit",
          "limitValue": "100",
          "currentValue": "50",
          "notificationSupported": true
        }
      ]
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `component​Name` | String | Name of the BRE component that the guardrail is fetched for. | Small, 63.0 | 63.0 |
| `guardrails` | [Guardrails](./connect_responses_guardrails.htm.md)[] | Specify the guardrails for the provided BRE component. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_business_rule_aggregation_results_output.htm ===
---
page_id: connect_responses_business_rule_aggregation_results_output.htm
title: Business Rules Aggregation Results
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_business_rule_aggregation_results_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business Rules Aggregation Results

Output representation of expression set results.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Error Result](./connect_responses_error_result.htm.md) | The details of the error. | Small, 55.0 | 55.0 |
| `results` | [Variable Map Output](./connect_responses_variable_map_output.htm.md) | The result of the aggregation step in an expression set. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_business_rules_result.htm ===
---
page_id: connect_responses_business_rules_result.htm
title: Business Rules Results
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_business_rules_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business Rules Results

Output representation of executing an expression set.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "outputs": [
    {
      "result": {
        "Premium": "1200",
        "Tax": "100"
      },
      "variables": {
        "age": "25",
        "state": "CA"
      },
      "error": {
        "stepId": "<stepId>",
        "errorMessage": "The rule is missing inputs: ['var1', 'var2'] and 3 more steps have 5 error"
      }
    },
    {
      "result": {
        "Premium": "2400",
        "Tax": "300"
      }
    },
    {
      "result": {
        "Premium": "500",
        "Tax": "25"
      }
    }
  ],
  "aggregationResults": {
    "result": {
      "TotalPremium": "4100",
      "TotalTax": "425"
    },
    "error": {
      "stepId": "<stepId>",
      "errorMessage": "The rule is missing inputs: ['var1', 'var2'] and 3 more steps have 5 error"
    }
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `aggregationResults` | [Business Rule Aggregation Results Output](./connect_responses_business_rule_aggregation_results_output.htm.md) | The result of the aggregation step in an expression set. | Small, 55.0 | 55.0 |
| `outputs` | [Rule Result](./connect_responses_rule_result.htm.md)[] | List of outputs returned by an expression set. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_context_definition_output.htm ===
---
page_id: connect_responses_context_definition_output.htm
title: Context Definition Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_context_definition_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Definition Output

Output representation of the context definitions in an expression
      set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the context definition. | Small, 58.0 | 58.0 |
| `name` | String | Developer name of the context definition. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_current_value.htm ===
---
page_id: connect_responses_current_value.htm
title: Current Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_current_value.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Current Value

Output representation of the current value of the guardrail at a row level.

      

```
{
  "values": {
    "currentValue": "50"
  }
}
```

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `currentValue` | String | Current value at a row-level. | Small, 63.0 | 63.0 |
|  | String | Unique identifier name of the sObject that the current value is provided from. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_decision_matrix_lookup_basic_result.htm ===
---
page_id: connect_responses_decision_matrix_lookup_basic_result.htm
title: Decision Matrix Lookup Basic Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_matrix_lookup_basic_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Lookup Basic Result

Results from a Decision Matrix lookup using a single
  input.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | String | The message stating the reason for the error. | Small, 55.0 | 55.0 |
| `results` | [Variable Output](./connect_responses_variable_output.htm.md)[] | The list of outputs for the specified input variable values. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_decision_model_export_error.htm ===
---
page_id: connect_responses_decision_model_export_error.htm
title: Decision Model Export Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_model_export_error.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Model Export Error

Error representation of a failed DMN (Decision Model Notation) export
      request.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code corresponding to the failed export request. | Small, 58.0 | 58.0 |
| `errorMessage` | String | Error message corresponding to the failed export request. | Small, 58.0 | 58.0 |
| `recordId` | String | Version ID of the decision matrix for which the data export request failed. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_model_export_output.htm ===
---
page_id: connect_responses_decision_model_export_output.htm
title: Decision Model Export Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_model_export_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Model Export Output

Output representation of a completed DMN (Decision Model Notation)
      export request.

      
        
          

**JSON example**

          
: 
            

```
{
   "message":"OK",
   "success":true,
   "errors":[
      {
         "errorCode":"BAD_REQUEST",
         "errorMessage":"We couldn’t find this record. Specify a valid ID for decisionModelEntityIds parameter.",
         "recordId":"0lNRO00000004fsdfAA"
      }
   ]
}
```

          

        
      

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Decision Model Export Error](./connect_responses_decision_model_export_error.htm.md)[] | List of errors corresponding to a failed export request. | Small, 58.0 | 58.0 |
| `message` | String | Response message from the completed export request. | Small, 58.0 | 58.0 |
| `success` | Boolean | Indicates whether the export request was successful (`true`) or not (`false`). | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_table_bulk_outcome.htm ===
---
page_id: connect_responses_decision_table_bulk_outcome.htm
title: Decision Table Bulk Outcome
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_bulk_outcome.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Bulk Outcome

Output representation of the decision table bulk
    look-up.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `outputs` | [Decision Table Outcome](./connect_responses_decision_table_outcome.htm.md) | List of the output of the Decision Table bulk lookup. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_table_data_output.htm ===
---
page_id: connect_responses_decision_table_data_output.htm
title: Decision Table Data
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_data_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Data

Output representation of the status of an action performed.

        
          

**Sample Output**

          
: 
            

```
{
  "errors": [],
  "errorFileId": "string_value"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​FileId` | String | Error code if transaction failed for any reason. | Small, 62.0 | 62.0 |
| `errors` | String[] | List of error messages if transaction failed for any reason. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_decision_table_definition_output.htm ===
---
page_id: connect_responses_decision_table_definition_output.htm
title: Decision Table Definition Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_definition_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Definition Output

Output representation of a decision table definition associated with a
      decision table.

              

              

              
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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `collectOperator` | String | Operator applied to outputs. Valid values are: `Count` `Maximum` `Minimum` `None` `Sum` | Small, 58.0 | 58.0 |
| `conditionCriteria` | String | Custom logic for deciding how the input fields are processed. | Small, 58.0 | 58.0 |
| `conditionType` | String | Condition logic for input fields. Valid values are: `All` `Any` `Custom` | Small, 58.0 | 58.0 |
| `decision​Result​Policy` | String | Results policy to specify the result of the decision table. Valid values are: `AnyValue` `CollectOperator—For internal use only` `FirstMatch` `OutputOrder` `Priority—For internal use only` `RuleOrder—For internal use only` `UniqueValues—For internal use only` | Small, 58.0 | 58.0 |
| `description` | String | Description of the decision table. | Small, 58.0 | 58.0 |
| `doesConsider​NullValue` | Boolean | Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is `false`. | Small, 60.0 | 60.0 |
| `fullName` | String | Unique name of the rule definition. | Small, 58.0 | 58.0 |
| `id` | String | ID of the decision table. | Small, 58.0 | 58.0 |
| `parameters` | [Decision Table Parameter Output](./connect_responses_decision_table_parameter_output.htm.md)[] | Array of input fields defined for the decision table. | Small, 58.0 | 58.0 |
| `setupName` | String | Name of the decision table. | Small, 58.0 | 58.0 |
| `sourceCriteria` | [Decision Table Source Criteria Output](./connect_responses_decision_table_source_criteria_output.htm.md)[] | Output array representation of source filters. | Small, 58.0 | 58.0 |
| `sourceObject` | String | Object containing business rules for the decision table to read. | Small, 58.0 | 58.0 |
| `sourceType` | String | Type of source used to obtain decision table data. Valid values are: `CsvUpload` `MultipleSobjects` `SingleSobject` | Small, 58.0 | 58.0 |
| `sourceconditionLogic` | String | Custom logic for deciding how criteria on source is applied. | Small, 58.0 | 58.0 |
| `status` | String | Status of the decision table. Valid values are: `ActivationInProgress` `ActivationInProgress` `Draft` `Inactive` | Small, 58.0 | 58.0 |
| `usageType` | String | Process type that uses the decision table. Valid values are: `Pricing` `ProductEligibility` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_table_outcome.htm ===
---
page_id: connect_responses_decision_table_outcome.htm
title: Decision Table Outcome
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_outcome.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Outcome

Output representation of the decision table
      execution.

      
         
            
               

**JSON example**

               
: 
                  

```
{
  "errorCode" : null,
  "errorMessage" : null,
  "outcomeList" : [ {
    "values" : {
      "amount__c" : "399",
      "Name" : "MH 005"
    }
  }, {
    "values" : {
      "amount__c" : "499",
      "Name" : "MH 006"
    }
  }, {
    "values" : {
      "amount__c" : "379",
      "Name" : "MH 007"
    }
  }, {
    "values" : {
      "amount__c" : "1498",
      "Name" : "MH 008"
    }
  }, {
    "values" : {
      "amount__c" : "98",
      "Name" : "MH 009"
    }
  }, {
    "values" : {
      "amount__c" : "251",
      "Name" : "MH 010"
    }
  } ],
  "outcomeType" : "Multiple Matches",
  "successStatus" : true
}

```

               

            
         

         

               
               
               
               
               
               
                  
                     

                     

                     

                     

                     

                  

               

               
                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                  

               

            
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | Integer | The error code if transaction fails for any reason. | Small, 55.0 | 55.0 |
| `errorMessage` | String | The error message if transaction fails for any reason. | Small, 55.0 | 55.0 |
| `outcomeList` | [Decision Table Outcome Item](./connect_responses_decision_table_outcome_item.htm.md)[] | Outcome list that stores two or more outcomes provided by the decision table. | Small, 55.0 | 55.0 |
| `outcomeType` | String | The outcome type after the request is successful. | Small, 55.0 | 55.0 |
| `successStatus` | Boolean | Indicates the status of the decision table execution. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_decision_table_outcome_item.htm ===
---
page_id: connect_responses_decision_table_outcome_item.htm
title: Decision Table Outcome Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_outcome_item.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Outcome Item

Output representation of the decision table outcome
    item.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `values` | Map<String, Object> | The list of outcomes provided by the decision table. If the decision table is configured to sort outcomes based on an input field or the output field, then the outcomes are provided based on the selected sort order. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_decision_table_output.htm ===
---
page_id: connect_responses_decision_table_output.htm
title: Decision Table Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Output

Output representation of the decision table details.

    
      
        
          

**JSON example for GET, POST, and PATCH**

          
: 
            

```
{
   "code":"200",
   "decisionTable":{
      "collectOperator":"Count",
      "conditionCriteria":"1 OR 2 OR 3",
      "conditionType":"Any",
      "decisionResultPolicy":"FirstMatch",
      "doesConsiderNullValue": true,
      "description":"Eligiblity of Products using Qualification Rules",
      "id":"0lDxx00000000BJ",
      "parameters":[
         {
            "fieldName":"IsDeleted",
            "isGroupByField":false,
            "isPriority":false,
            "operator":"Equals",
            "sequence":1,
            "usage":"Input"
         },
         {
            "fieldName":"CreatedById",
            "isGroupByField":false,
            "isPriority":false,
            "usage":"Output"
         },
         {
            "fieldName":"Title",
            "isGroupByField":false,
            "isPriority":false,
            "operator":"Equals",
            "sequence":3,
            "usage":"Input"
         },
         {
            "fieldName":"Id",
            "isGroupByField":false,
            "isPriority":false,
            "operator":"Equals",
            "sequence":2,
            "usage":"Input"
         }
      ],
      "setupName":"Product Qualification eligibility3",
      "sourceCriteria":[
         
      ],
      "sourceObject":"AccountFeed",
      "sourceType":"SingleSobject",
      "sourceconditionLogic":"1 AND 2 AND 3",
      "status":"Draft"
   },
   "isSuccess":true,
   "message":""
}
```

          

        
        
          

**JSON example for DELETE**

          
: 
            

```
{
   "code":"200",
   "isSuccess":true,
   "message":""
}
```

          

        
      

    

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Response code from the API request. | Small, 58.0 | 58.0 |
| `decisionTable` | [Decision Table Definition Output](./connect_responses_decision_table_definition_output.htm.md) | Details of the decision table definition associated with the decision table. | Small, 58.0 | 58.0 |
| `isSuccess` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `message` | String | Error message when the API request fails. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_table_parameter_output.htm ===
---
page_id: connect_responses_decision_table_parameter_output.htm
title: Decision Table Parameter Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_parameter_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Parameter Output 

Output representation of a decision table parameter.

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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `columnMapping` | String | Source object path for mapping to the column of an entity. | Small, 58.0 | 58.0 |
| `dataType` | String | Data type of the field used. Possible values are: `Boolean` `Currency` `Date` `Number` `Percent` `String` | Small, 58.0 | 58.0 |
| `decimalScale` | Integer | Precision of the field used. | Small, 58.0 | 58.0 |
| `domainEntity` | String | Entity domain the field is mapped to. | Small, 58.0 | 58.0 |
| `fieldName` | String | Name of the field to be used in the decision table. | Small, 58.0 | 58.0 |
| `isGroupByField` | Boolean | Indicates whether the field is used to group the business rules of the decision table (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `isPriority` | Boolean | Indicates whether it is a priority field (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `maxlength` | Integer | Maximum length of the field used. | Small, 58.0 | 58.0 |
| `operator` | String | Valid operators for a field based on its usage. Possible values are: `Between` `DoesNotExistIn` `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `LessOrEqual` `LessThan` `Matches` `NotEquals` | Small, 58.0 | 58.0 |
| `sequence` | Integer | Sequence in which input fields are processed. | Small, 58.0 | 58.0 |
| `sortType` | String | Type of sorting done on the rows of a decision table. Possible values are: `AscNullFirst` `AscNullLast` `DescNullFirst` `DescNullLast` `None` | Small, 58.0 | 58.0 |
| `usage` | String | Usage type for a field. Possible values are: `Input` `Output` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_decision_table_row_output.htm ===
---
page_id: connect_responses_decision_table_row_output.htm
title: Decision Table Row
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_row_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Row

Output representation to describe the output of a decision table row.

        
          

**Sample Output**

          
: 
            

```
{
  "rows": {
    "id": "1FIxx0000004CCG",
    "rowData": {
      "AssetLevel": "101",
      "City": "city1"
    }
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the decision table row. | Small, 62.0 | 62.0 |
| `rowData` | Map<String, Object> | Key value pair of the decision table row. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_decision_table_rows_list_output.htm ===
---
page_id: connect_responses_decision_table_rows_list_output.htm
title: Decision Table Rows List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_rows_list_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Rows List

Output representation of the rows in relation to the decision table, including current
    state of pagination.

        
          

**Sample Output**

          
: 
            

```
{
  "rows": [
    {
      "id": "1FIxx0000004CCG",
      "rowData": {
        "AssetLevel": "101",
        "City": "city1"
      }
    }
  ],
  "totalRows": 3
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `rows` | [Decision Table Row](./connect_responses_decision_table_row_output.htm.md)[] | List of rows returned in response to the API request. | Small, 62.0 | 62.0 |
| `totalRows` | Integer | Total number of rows. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_decision_table_source_criteria_output.htm ===
---
page_id: connect_responses_decision_table_source_criteria_output.htm
title: Decision Table Source Criteria Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_source_criteria_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Source Criteria Output

Output representation of the decision table source
    criteria.

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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `operator` | String | Operator used in the filter criteria. Possible values are: `Contains` `DoesNotContain` `Equals` `GreaterThan` `GreaterThanOrEqual` `IsNotNull` `IsNull` `LessThan` `LessThanOrEqual` `NotEqual` | Small, 58.0 | 58.0 |
| `sequenceNumber` | Integer | Sequence number of the filter criteria in the associated decision table source condition. | Small, 58.0 | 58.0 |
| `sourceFieldName` | String | Name of the field in the filter criteria. | Small, 58.0 | 58.0 |
| `value` | String | Expected value of the field. | Small, 58.0 | 58.0 |
| `valueType` | String | Type of filter value. Possible values are: `Formula` `Literal` `Lookup` `Parameter` `PickList` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_dependency_detail_output.htm ===
---
page_id: connect_responses_dependency_detail_output.htm
title: Dependency Detail Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_dependency_detail_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dependency Detail Output

Output representation of the  expression set version
      dependencies.

#### 

- 
- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | Name of the expression set version dependency detail API. | Small, 58.0 | 58.0 |
| `id` | String | ID of the expression set version dependency. Note This ID can be used as the ID of the expression set, decision matrix, or decision table. | Small, 58.0 | 58.0 |
| `lastModifiedDate` | String | Date on which the dependency was modified last. | Small, 58.0 | 58.0 |
| `name` | String | Expression set version dependency name. | Small, 58.0 | 58.0 |
| `type` | String | Type of the expression set version dependencies.Possible values: `DecisionMatrix` `DecisionTable` `ExpressionSet` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_error_result.htm ===
---
page_id: connect_responses_error_result.htm
title: Error Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_error_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Result

Output representation of the errors in the execution of an expression
      set.

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorMessage` | String | The message that provides details of the error in executing an expression set. | Small, 55.0 | 55.0 |
| `stepId` | String | The ID of a step in an expression set version that resulted in an error. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_explainability_log_detail.htm ===
---
page_id: connect_responses_explainability_log_detail.htm
title: Explainability Log Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_log_detail.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Log Detail

Output representation of the list of  explainability
    logs.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `action​Context​Code` | String | The record ID within the context of the associated application's action that can be used to retrieve the log. | Small, 56.0 | 56.0 |
| `actionLog` | String | The contents of the explainability log as a JSON string. | Small, 56.0 | 56.0 |
| `application​LogDate` | String | The date and time at which the explainability log is generated by the application's action. | Small, 56.0 | 56.0 |
| `application​Subtype` | String | The subtype of the associated application for which the explainability log is generated. This matches one of the valid values in the ExplainabilityActionDef `ApplicationSubtype` field. | Small, 56.0 | 56.0 |
| `application​Type` | String | The name of the application for which the explainability service is run. This matches one of the valid values in the ExplainabilityActionDef `ApplicationType` field. | Small, 56.0 | 56.0 |
| `name` | String | A name to identify the explainability log record. | Small, 56.0 | 56.0 |
| `processType` | String | The process type of the associated application for which the explainability action log is generated. This matches one of the valid values in the `ProcessType` field. | Small, 56.0 | 56.0 |

=== ARTICLE: connect_responses_explainability_logs.htm ===
---
page_id: connect_responses_explainability_logs.htm
title: Explainability Logs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_explainability_logs.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Explainability Logs

Output representation of the list of explainability action
    logs.

      
        
          

**JSON example**

          
: 
            

```
{
  "actionLogs": [
    {
      "actionContextCode": "001x0000005SdzIAAS",
      "actionLog": "{This is a sample action log data.}",
      "applicationLogDate": "Mon Aug 01 10:29:35 GMT 2022",
      "applicationSubtype": "ASD1",
      "applicationType": "0",
      "name": "EAD1",
      "processType": "BPT1"
    }
  ],
  "queryMore": " "
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `actionLogs` | [Explainability Log Detail](./connect_responses_explainability_log_detail.htm.md)[] | The list of explainability logs that matches the search criteria. | Small, 56.0 | 56.0 |
| `queryMore` | String | A string that can be passed to the next call to fetch the next batch of explainability log records. | Small, 56.0 | 56.0 |

=== ARTICLE: connect_responses_expression_set_advanced_condition_step_output.htm ===
---
page_id: connect_responses_expression_set_advanced_condition_step_output.htm
title: Expression Set Advanced Condition Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_advanced_condition_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Advanced Condition Step

Output representation of an advanced condition step in an expression
      set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `condition​Logic` | String | Condition that’s defined for the advanced condition. For example, all conditions are met or any of the conditions are met. | Small, 58.0 | 58.0 |
| `criteria` | [Expression Set Condition Criteria](./connect_responses_expression_set_condition_criteria_output.htm.md) | List of condition criteria in an expression set. | Small, 58.0 | 58.0 |
| `result​Parameter` | String | Expression set definition version variable associated with the result of this step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_aggregation_step_output.htm ===
---
page_id: connect_responses_expression_set_aggregation_step_output.htm
title: Expression Set Aggregation Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_aggregation_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Aggregation Step

Output representation of the expression set aggregation
    step.

- 
- 
- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `aggergated​Parameter` | String | Expression set version variable that’s present on the right side of the aggregation step. | Small, 58.0 | 58.0 |
| `aggregate​Function` | String | Aggregation function of the expression set.Valid values are: `Avg` `Max` `Min` `Sum` | Small, 58.0 | 58.0 |
| `expression` | String | Expression that’s present on the left side of the aggregation step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_assignment_step_output.htm ===
---
page_id: connect_responses_expression_set_assignment_step_output.htm
title: Expression Set Assignment Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_assignment_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Assignment Step

Output representation of an assignment step in an expression
    set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `assigned​Parameter` | String | Expression set version variable that’s present on the right side of the calculation step. | Small, 58.0 | 58.0 |
| `expression` | String | Expression that’s present on the left side of the calculation step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_condition_criteria_output.htm ===
---
page_id: connect_responses_expression_set_condition_criteria_output.htm
title: Expression Set Condition Criteria
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_condition_criteria_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Condition Criteria

Output representation of a condition criteria in an expression
      set.

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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `operator` | String | Condition operator of the expression set.Valid values are: `Contains` `DoesNotContain` `Equals` `GreaterThan​OrEquals` `GreaterThan` `IsNotNull` `IsNull` `LessThan` `LessThan​OrEquals` `NotEqualTo` | Small, 58.0 | 58.0 |
| `sequence​Number` | Integer | Sequence number of the condition in the advanced condition. | Small, 58.0 | 58.0 |
| `source​Field​Name` | String | Expression set version variable associated with the condition criteria. | Small, 58.0 | 58.0 |
| `value` | String | Value specified in the right-hand side of the condition. | Small, 58.0 | 58.0 |
| `value​Type` | String | Criteria value type of the expression set.Valid values are: `Formula` `Literal` `Parameter` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_condition_expression_step_output.htm ===
---
page_id: connect_responses_expression_set_condition_expression_step_output.htm
title: Expression Set Condition Expression Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_condition_expression_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Condition Expression Step

Output representation of a condition step in an expression
    set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `expression` | String | Expression that’s defined for the step. | Small, 58.0 | 58.0 |
| `result​Parameter` | String | Expression set version variable associated with the result of the step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_custom_element_parameter_output.htm ===
---
page_id: connect_responses_expression_set_custom_element_parameter_output.htm
title: Expression Set Custom Element Parameter
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_custom_element_parameter_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Custom Element Parameter

Output representation of a custom element parameter in an expression
      set.

            
              

              

              
- 
- 
- 
- 
- 

              

              

            

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `input` | Boolean | Indicates whether the custom element parameter is an input parameter (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `name` | String | Name of the custom element parameter. | Small, 58.0 | 58.0 |
| `output` | Boolean | Indicates whether the custom element parameter is an output parameter (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `type` | String | Type of custom element parameter. Valid values are: `Formula` `Literal` `Lookup` `Parameter` `Picklist` The default value is `Parameter`. | Small, 58.0 | 58.0 |
| `value` | String | Name of the expression set variable. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_custom_element_step_output.htm ===
---
page_id: connect_responses_expression_set_custom_element_step_output.htm
title: Expression Set Custom Element Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_custom_element_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Custom Element Step

Output representation of a custom element step in an expression
      set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `parameters` | [Expression Set Custom Element Parameter](./connect_responses_expression_set_custom_element_parameter_output.htm.md) | List of parameters in a custom element. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_des_token_mapping.htm ===
---
page_id: connect_responses_expression_set_des_token_mapping.htm
title: Expression Set DES Token Mapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_des_token_mapping.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set DES Token Mapping

Output representation of the DES token mapping in an expression set
      version step.

    
      
        
          

**JSON example**

          
: 
            

```
"passedMessageTokenMappings": [
{
"expressionSetMessageToken": "price",
"resourceReference": "DM1__Price"
}
],
"failedMessageTokenMappings": [
{
"expressionSetMessageToken": "model",
"resourceReference": "Model"
}
],

"noResultTokenMappings": [
{
"expressionSetMessageToken": "year",
"resourceReference": "Year"
}
]
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `resource​Reference` | String | Name of the expression set resource that’s mapped to a token, such as Variable, Constant, or FiledAlias. | Small, 59.0 | 59.0 |
| `expressionSet​MessageToken` | String | Name of the explainability message template token. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_expression_set_error.htm ===
---
page_id: connect_responses_expression_set_error.htm
title: Expression Set Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_error.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Error

Representation of the expression set errors.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | Error message in the creation of the expression set. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_lookup_table_step_output.htm ===
---
page_id: connect_responses_expression_set_lookup_table_step_output.htm
title: Expression Set Lookup Table Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_lookup_table_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Lookup Table Step

Output representation of a lookup table step in an expression
      set.

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `lookup​Table​Name` | String | Decision matrix or decision table name that’s used in the lookup table step. | Small, 58.0 | 58.0 |
| `type` | String | Lookup table type of the expression set.Valid values are: `DecisionMatrix` `DecisionTable` | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_output.htm ===
---
page_id: connect_responses_expression_set_output.htm
title: Expression Set Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Output

Output representation of the expression set
      create,
      update and delete request.

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `api​Name` | String | Unique name of the expression set. | Small, 58.0 | 58.0 |
| `context​Definitions` | [Context ​Definition Output](./connect_responses_context_definition_output.htm.md) | List of context definitions in an expression set. | Small, 58.0 | 58.0 |
| `description` | String | Description of the expression set. | Small, 58.0 | 58.0 |
| `error` | [Expression Set​ Error](./connect_responses_expression_set_error.htm.md) | Details of the error message in the case of failure of the expression set create request. | Small, 58.0 | 58.0 |
| `id` | String | ID of the expression set. | Small, 58.0 | 58.0 |
| `name` | String | Name of the expression set. | Small, 58.0 | 58.0 |
| `status` | String | Response status of the expression set.Valid values are: `Failed` `Success` | Small, 58.0 | 58.0 |
| `usage​Type` | String | Usage type of the expression set. Valid value is `Bre`. The default value is `Bre`. When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. | Small, 58.0 | 58.0 |
| `versions` | [Expression Set​ Version Output](./connect_responses_expression_set_version_output.htm.md) | List of the expression set versions. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_sub_expression_step_output.htm ===
---
page_id: connect_responses_expression_set_sub_expression_step_output.htm
title: Expression Set SubExpression Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_sub_expression_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set SubExpression Step

Output representation of a subexpression step in an expression
      set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `expression​Set` | String | Expression set name that’s used in the subexpression set step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_version_dependency_output.htm ===
---
page_id: connect_responses_expression_set_version_dependency_output.htm
title: Expression Set Version Dependency
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_version_dependency_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Dependency

Output representation for the expression set version
    dependency.

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `dependencies` | [Dependency Detail Output](./connect_responses_dependency_detail_output.htm.md)[] | Dependent components of the expression set version. | Small, 58.0 | 58.0 |
| `id` | String | Expression set dependency version ID. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_version_output.htm ===
---
page_id: connect_responses_expression_set_version_output.htm
title: Expression Set Version Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_version_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Output

Output representation of an expression set version.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `api​Name` | String | API name of the expression set version. | Small, 58.0 | 58.0 |
| `description` | String | Description of the expression set version. | Small, 58.0 | 58.0 |
| `enabled` | Boolean | Indicates whether the expression set version is active (`true`) or inactive (`false`). | Small, 58.0 | 58.0 |
| `end​Date` | String | Effective end date of the expression set version. | Small, 58.0 | 58.0 |
| `id` | String | ID of the expression set version. | Small, 58.0 | 58.0 |
| `name` | String | Name of the expression set version. | Small, 58.0 | 58.0 |
| `rank` | Integer | Rank of the expression set version. | Small, 58.0 | 58.0 |
| `show​Expl​Externally` | Boolean | Indicates whether the decision explanation is exposed to community users (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `start​Date` | String | Effective start date of the expression set version. | Small, 58.0 | 58.0 |
| `steps` | [Expression Set Version Step](./connect_responses_expression_set_version_step_output.htm.md) | List of steps in an expression set. | Small, 58.0 | 58.0 |
| `variables` | [Expression Set Version Variable](./connect_responses_expression_set_version_variable_output.htm.md) | List of variables in an expression set. | Small, 58.0 | 58.0 |
| `version​Number` | Integer | Version number of the expression set version. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_version_step_output.htm ===
---
page_id: connect_responses_expression_set_version_step_output.htm
title: Expression Set Version Step
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_version_step_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Step

Output representation of a step in an expression set
    version.

                        
                            

                            

                            

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

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `action​Type` | String | Business Knowledge Model of the expression set.Valid values are: `AiAccelerator​SubscriberChurn​Prediction` `AssignBadge​ToMember` `AssignParameter​Values` `Automated​Claims​Processing​Validation` `BreAggregator` `BreAggregator​Assignment` `ChangeMember​Tier` `CheckMember​BadgeAssignment` `CreditPoints` `Crud` `DebitPoints` `Evaluate​Qualification` `Evaluate​Disqualification` `GetMember​Attributes​Values` `GetMember​PointBalance` `GetMember​Promotions` `GetMemberTier` `GetOutputs​FromDecision​Matrix` `GetOutputs​FromDecision​Table` `GetUser​Data` `IncreaseUsage​ForCumulative​Promotion` `IssueVoucher` `List​Group​Calculation` `PriceList` `RecordAlert` `Redeem​Voucher` `Redeem​Voucher` `RunFlow` `RunProgram​Process` `SampleBusiness​ElementWith​Context` `SampleDynamic​Custom​Element` `SendMail` `TestCustom​Element` `UpdateCurrent​ValueFor​MemberAttribute` `UpdatePoint​Balance` `UpdateUsage​ForCumulative​Promotion` `VolumeDiscount` | Small, 58.0 | 58.0 |
| `advanced​Condition` | [Expression Set Advanced Condition Step](./connect_responses_expression_set_advanced_condition_step_output.htm.md) | Details of the advanced condition in case of an advanced condition step. | Small, 58.0 | 58.0 |
| `aggregation` | [Expression Set Aggregation Step](./connect_responses_expression_set_aggregation_step_output.htm.md) | Details of the aggregation step in case of an aggregation step. | Small, 58.0 | 58.0 |
| `assignment` | [Expression Set Assignment Step](./connect_responses_expression_set_assignment_step_output.htm.md) | Details of the assignment step in case of an assignment step. | Small, 58.0 | 58.0 |
| `condition​Expression` | [Expression Set Condition Expression Step](./connect_responses_expression_set_condition_expression_step_output.htm.md) | Details of the condition step in case of a condition step. | Small, 58.0 | 58.0 |
| `custom​Element` | [Expression Set Custom Element Step](./connect_responses_expression_set_custom_element_step_output.htm.md) | Details of the custom element step in case of a custom element step. | Small, 58.0 | 58.0 |
| `description` | String | Description of the step in expression set version. | Small, 58.0 | 58.0 |
| `failed​Explainer​Template` | String | Name of the failed explainability message template. | Small, 58.0 | 58.0 |
| `failed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the failed explainability message template. | Optional | 59.0 |
| `lookup​Table` | [Expression Set Lookup Table Step](./connect_responses_expression_set_lookup_table_step_output.htm.md) | Details of the lookup table in case of a decision matrix or decision table step. | Small, 58.0 | 58.0 |
| `name` | String | Unique name of the step in expression set version. | Small, 58.0 | 58.0 |
| `noResult​Explainer​Template` | String | Name of the explainability message template that’s used when the evaluation result of the selected element type is No Result. This field is applicable for a Decision Table only. | Small, 59.0 | 59.0 |
| `noResult​MessageToken​Mappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the no result explainability message template. | Small, 59.0 | 59.0 |
| `parent​Step` | String | Unique name of the parent step of this step in the expression set version. | Small, 58.0 | 58.0 |
| `passed​Explainer​Template` | String | Name of the passed explainability message template. | Small, 58.0 | 58.0 |
| `passed​Message​TokenMappings` | [Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md) | List of the token resource mappings of the passed explainability message template. | Small, 59.0 | 59.0 |
| `result​Included` | Boolean | Indicates whether to include the step output in the expression set result (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `sequence​Number` | Integer | Sequence number of the step in the expression set version. | Small, 58.0 | 58.0 |
| `shouldExpose​Condition​Details` | Boolean | Indicates whether the decision explanation includes the condition details (`true`) or not (`false`) for the condition element type. | Small, 58.0 | 58.0 |
| `should​ExposeExec​PathMsg​Only` | Boolean | Indicates whether the decision explanation includes details of the executed path only (`true`) or not (`false`) for the branch element type. | Small, 58.0 | 58.0 |
| `should​ShowExpl​Externally` | Boolean | Indicates whether the decision explanation is exposed to community users for the step (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `step​Type` | String | Step type of the expression set.Valid values are: `Advanced​Condition` `Branch` `Business​Knowledge​Model` `Condition` `DefaultPath` `SubExpression` | Small, 58.0 | 58.0 |
| `sub​Expression` | [Expression Set SubExpression Step](./connect_responses_expression_set_sub_expression_step_output.htm.md) | Details of the subexpression set in case of a subexpression step. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_expression_set_version_variable_output.htm ===
---
page_id: connect_responses_expression_set_version_variable_output.htm
title: Expression Set Version Variable
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_expression_set_version_variable_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Version Variable

Output representation of a variable in an expression set
    version.

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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `collection` | Boolean | Indicates whether the variable is a collection (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `data​Type` | String | Variable data type for the expression set. `Action​Output` `Boolean` `Currency` `Date` `Date​Time` `Decision​Matrix` `Decision​Table` `Numeric` `Percent` `Sobject` `Sub​Expression` `Text` | Small, 58.0 | 58.0 |
| `decimal​Places` | Integer | Number of decimal places allowed for the value of the variable. | Small, 58.0 | 58.0 |
| `description` | String | Description of the variable. | Small, 58.0 | 58.0 |
| `input` | Boolean | Indicates whether the variable is the input of an expression set version (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `lookup​Name` | String | API name of the decision matrix, decision table, or subexpression. | Small, 58.0 | 58.0 |
| `lookup​Type` | String | Variable lookup type of the expression set.Valid values are: `Decision​Matrix` `Decision​Table` `Sub​Expression` | Small, 58.0 | 58.0 |
| `name` | String | Name of the variable. | Small, 58.0 | 58.0 |
| `object​Name` | String | Name of the object when the variable is of sObject type. | Small, 58.0 | 58.0 |
| `output` | Boolean | Indicates whether the variable is the output of an expression set version (`true`) or not (`false`). | Small, 58.0 | 58.0 |
| `result​Step` | String | Name of the step that’s producing the value to the variable. | Small, 58.0 | 58.0 |
| `type` | String | Variable type of the expression set.Valid values are: `Constant` `Formula` `Variable` | Small, 58.0 | 58.0 |
| `value` | String | Represents a value in case of a constant variable type and a formula in case of a formula variable type. | Small, 58.0 | 58.0 |

=== ARTICLE: connect_responses_guardrail_current_value.htm ===
---
page_id: connect_responses_guardrail_current_value.htm
title: Guardrail Current Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_guardrail_current_value.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guardrail Current Value

Output representation of the current values of the guardrails along with the resource
    type.

      

```
{
  "currentValues": {
    "resourceType": "ExampleResource",
    "values": {
      "currentValue": "50",
      "resourceName": "Resource1"
    }
  }
}
```

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `resource​Type` | String | Name of the sObject that the current value of the guardrail is determined from. | Small, 63.0 | 63.0 |
| `values` | [Current Value[]](./connect_responses_current_value.htm.md) | Row-level current values of the guardrail. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_guardrails.htm ===
---
page_id: connect_responses_guardrails.htm
title: Guardrails
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_guardrails.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guardrails

Output representation of each guardrail that includes information to manage system
    thresholds and notifications in BRE components.

        
          

**JSON Sample**

          
: 
            

```
{
  "guardrails": {
    "name": "MaxProcessLimit",
    "guardrailType": "RateLimit",
    "limitValue": "100",
    "currentValue": "50",
    "notificationSupported": true
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `currentValue` | String | Current value of the guardrail. | Small, 63.0 | 63.0 |
|  | [Guardrail Current Value](./connect_responses_guardrail_current_value.htm.md) | Resource type and the row-level current values of the guardrail. For future use only. | Small, 63.0 | 63.0 |
| `guardrail​Type` | Guardrail Type (enumeration of type string) | Type of guardrail. Valid values are: `RateLimit` `OrgValueLimit` | Small, 63.0 | 63.0 |
| `limitValue` | String | Default or configured value of the given guardrail | Small, 63.0 | 63.0 |
|  | String | Maximum value of the given guardrail. For future use only. | Small, 63.0 | 63.0 |
| `multiValue` | Boolean | Specifies details if the current values are determined by an org level or aggregation of row levels. | Small, 63.0 | 63.0 |
| `name` | String | Name of the guardrail. | Small, 63.0 | 63.0 |
| `notification​Supported` | Boolean | Indicates whether the guardrail supports notifications (`true`) or not (`false`). | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_lookup_table_details.htm ===
---
page_id: connect_responses_lookup_table_details.htm
title: Lookup Table Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_lookup_table_details.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Table Details

Output representation of the basic details of a lookup
    table.

      
        
          

**JSON example**

          
: 
            

```

  "lookupTables":[{
    "apiName":"DM_1",
    "id":"0lIxx0000000001EAA",
    "lookupTableDefinitionId":"9QNxx0000004C92GAE",
    "lookupTableType":"DecisionMatrix",
    "name":"DM_1"
  },
  {
    "apiName":"DT_2",
    "id":"0lIxx000000003FEAQ",
    "lookupTableDefinitionId":"0lDxx000000001dEAA",
    "lookupTableType":"DecisionTable",
    "name":"DT_2"
  }]
```

          

        
      

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiName` | String | Unique developer name of the Decision Table or Decision Matrix. | Small, 59.0 | 59.0 |
| `id` | String | ID of the lookup table record. | Small, 59.0 | 59.0 |
| `lookupTable​DefinitionId` | String | ID of the Decision Table or Decision Matrix record. | Small, 59.0 | 59.0 |
| `lookupTable​Type` | String | Type of the lookup table, such as Decision Table or Decision Matrix. | Small, 59.0 | 59.0 |
| `name` | String | Name of the Decision Table or Decision Matrix. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_lookup_tables_result_list.htm ===
---
page_id: connect_responses_lookup_tables_result_list.htm
title: Lookup Tables Result List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_lookup_tables_result_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Result List

Output representation of the result of a lookup table search
      request.

      
        
          

**JSON example**

          
: 
            

```
{
  "code": "200",
  "isSuccess": true,
  "lookupTables": [
    {
      "id": "0lIxx000000003FEAQ",
      "lookupTableDefinitionId": "0lDxx000000001dEAA",
      "lookupTableType": "DecisionTable",
      "name": "DT_Apr27_2",
      "apiName": "DT_Apr27_2"
    }
  ],
  "message": ""
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Response code of the API request. | Small, 59.0 | 59.0 |
| `isSuccess` | Boolean | Indicates whether the request is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |
| `lookupTables` | [Lookup Table Details](./connect_responses_lookup_table_details.htm.md)[] | List of the retrieved lookup tables. | Small, 59.0 | 59.0 |
| `message` | String | API response message if the request fails. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_message_template_detail_output.htm ===
---
page_id: connect_responses_message_template_detail_output.htm
title: Message Template Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_message_template_detail_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Message Template Detail

Output representation of explainability message template
    details.

      
        
          

**JSON example**

          
: 
            

```
{
  "expressionSetStepType": "Branch",
  "id": "8U8x00000000027CAA",
  "isDefault": true,
  "message": "This is Branch Passing Message",
  "name": "BranchMessageTemplate",
  "resultType": "Passed"
}
```

          

        
      

              

              

              

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

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `expression​SetStep​Type` | String | The step type in an expression set version that uses the explainability message template.Possible values: Calculation Branch Condition Decision Matrix Lookup Decision Table Lookup Aggregation Sub Expression Business Element | Small, 56.0 | 56.0 |
| `id` | String | The record ID of the explainability message template. | Small, 56.0 | 56.0 |
| `isDefault` | Boolean | Indicates whether the decision explainer template for a specified step type is default (`true`) or not (`false`). | Small, 56.0 | 56.0 |
| `message` | String | The explanation message in the explainability message template for a specific expression set step type. | Small, 56.0 | 56.0 |
| `name` | String | The name that identifies the explainability message template. | Small, 56.0 | 56.0 |
| `resultType` | String | The type of result for which the message template can be used. The step type for which the result is evaluated can be a condition, conditional group, or branch. Possible Values: `Passed` `Failed` | Small, 56.0 | 56.0 |

=== ARTICLE: connect_responses_message_templates_list_output.htm ===
---
page_id: connect_responses_message_templates_list_output.htm
title: Message Templates List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_message_templates_list_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Message Templates List

Output representation of the list of explainability message
      templates.

      
        
          

**JSON example**

          
: 
            

```
{
  "messageTemplates" : [ {
    "expressionSetStepType" : "Branch",
    "id" : "8U8x00000000027CAA",
    "isDefault" : true,
    "message" : "This is Branch Passing Message",
    "name" : "BranchMessageTemplate",
    "resultType" : "Passed"
  }, {
    "expressionSetStepType" : "Calculation",
    "id" : "8U8x00000000022CAA",
    "isDefault" : true,
    "message" : "CalcMessageTemplate PASS",
    "name" : "CalcMessageTemplate",
    "resultType" : "Passed"
  }, {
    "expressionSetStepType" : "Condition",
    "id" : "8U8x0000000002CCAQ",
    "isDefault" : false,
    "message" : "This is Condition Passing Message",
    "name" : "ConditionMessageTemplate",
    "resultType" : "Passed"
  }, {
    "expressionSetStepType" : "MatrixLookup",
    "id" : "8U8x0000000002HCAQ",
    "isDefault" : true,
    "message" : "This is DM passing message",
    "name" : "DMMessageTemplate",
    "resultType" : "Passed"
  }, {
    "expressionSetStepType" : "ReferenceProcedure",
    "id" : "8U8x0000000002MCAQ",
    "isDefault" : true,
    "message" : "This is SubExpression Passing Message",
    "name" : "SubExpressionMessageTemplate",
    "resultType" : "Passed"
  } ]
}

```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | The API response code when there’s a failure in retrieving the list of explainability message templates. | Small, 56.0 | 56.0 |
| `isSuccess` | Boolean | Identifies whether the request is successful (`true`) or not (`false`). | Small, 56.0 | 56.0 |
| `message` | String | The error message when there’s a failure in retrieving the list of explainability message templates. | Small, 56.0 | 56.0 |
| `message​Templates` | [Message Template Detail](./connect_responses_message_template_detail_output.htm.md) [] | The list of explainability message templates. | Small, 56.0 | 56.0 |

=== ARTICLE: connect_responses_rule_result.htm ===
---
page_id: connect_responses_rule_result.htm
title: Rule Results
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_rule_result.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rule Results

Output representation of the result of executing a single input in an
      expression set.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Error Result](./connect_responses_error_result.htm.md) | The details of the error resulting from executing a single input in an expression set. | Small, 55.0 | 55.0 |
| `results` | [Variable Map Output](./connect_responses_variable_map_output.htm.md) | The result of the aggregation step in an expression set. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_variable_map_output.htm ===
---
page_id: connect_responses_variable_map_output.htm
title: Variable Map Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_variable_map_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variable Map Output

Output representation of the input variables in an expression set
      version.

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `variableMap` | Map<String, Object> | A map of input variables and their corresponding values. | Small, 55.0 | 55.0 |

=== ARTICLE: connect_responses_variable_output.htm ===
---
page_id: connect_responses_variable_output.htm
title: Variable Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_variable_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variable Output

Output representation of the input variables in an expression
      set.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | The name of the variable. | Small, 55.0 | 55.0 |
| `value` | Object | The value of the variable. | Small, 55.0 | 55.0 |

=== ARTICLE: decision_explainer_bre_connect_apis.htm ===
---
page_id: decision_explainer_bre_connect_apis.htm
title: Decision Explainer Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_connect_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Business APIs

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce
        software and UIs.

The Decision Explainer runtime service for Business Rules Engine is exposed through
            Connect APIs.

#### Note

            

Use the Decision Explainer resources when your Salesforce instance has Business Rules
                Engine and Decision Explainer, and you want to show explanations of the results of
                an expression set step to external users.

        

With Decision Explainer connect APIs, you can:

            
- [Retrieve a list of explainability message
                        templates](./connect_resources_rules_engine_message_templates_list.htm.md)

            
- [Retrieve details of a specific explainability message
                        template](./connect_resources_rules_engine_message_template_detail.htm.md)

            
- [Retrieve explainability logs for expression step
                        elements that have explanations configured](./connect_resources_rules_engine_explainability_logs.htm.md)

        

- 
**[Resources](./decision_explainer_bre_resources.htm.md)**  

Decision Explainer API includes these resources.

- 
**[Response Bodies](./decision_explainer_bre_responses.htm.md)**  

Decision Explainer API includes these response bodies.

=== ARTICLE: decision_explainer_bre_metadata_api_parent.htm ===
---
page_id: decision_explainer_bre_metadata_api_parent.htm
title: Decision Explainer Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[ExplainabilityMsgTemplate](./meta_explainabilitymsgtemplate.htm.md)**  

Represents information about the template 			that contains the decision explanation message for a specified expression set step 			type.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: decision_explainer_bre_parent.htm ===
---
page_id: decision_explainer_bre_parent.htm
title: Decision Explainer for Expression Set
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: business_rules_engine.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer for Expression Set

Decision Explainer is an audit-like service that can be used by applications to store
        their application data to explain past events. The stored data can be retrieved later for
        reporting through custom-built user interfaces.
        

- 
**[Decision Explainer Standard Objects](./decision_explainer_bre_standard_objects.htm.md)**  

Use standard objects to create, update, and activate Decision Explainer     components.

- 
**[Decision Explainer Business APIs](./decision_explainer_bre_connect_apis.htm.md)**  

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce         software and UIs.

- 
**[Decision Explainer Metadata API Types](./decision_explainer_bre_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Decision Explainer Tooling API Objects](./decision_explainer_bre_tooling_objects_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

#### See Also

- [*Salesforce Help*: Decision Explainer for Expression Sets](https://help.salesforce.com/s/articleView?id=ind.decision_explainer.htm&type=5&language=en_US)

=== ARTICLE: decision_explainer_bre_resources.htm ===
---
page_id: decision_explainer_bre_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Decision Explainer API includes these resources.

- 
**[Explainability Message Templates (GET)](./connect_resources_rules_engine_message_templates_list.htm.md)**  

Retrieves a list of explainability message templates that matches       the given search parameters. 

- 
**[Explainability Message Template Details (GET)](./connect_resources_rules_engine_message_template_detail.htm.md)**  

Retrieves the details of an explainability message template for a       specified template ID.

- 
**[Explainability Logs (GET)](./connect_resources_rules_engine_explainability_logs.htm.md)**  

Retrieves explainability logs for expression step elements for which       explanation messages are configured.

=== ARTICLE: decision_explainer_bre_responses.htm ===
---
page_id: decision_explainer_bre_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Decision Explainer API includes these response bodies.

- 
**[Explainability Logs](./connect_responses_explainability_logs.htm.md)**  

Output representation of the list of explainability action     logs.

- 
**[Explainability Log Detail](./connect_responses_explainability_log_detail.htm.md)**  

Output representation of the list of  explainability     logs.

- 
**[Message Template Detail](./connect_responses_message_template_detail_output.htm.md)**  

Output representation of explainability message template     details.

- 
**[Message Templates List](./connect_responses_message_templates_list_output.htm.md)**  

Output representation of the list of explainability message       templates.

=== ARTICLE: decision_explainer_bre_standard_objects.htm ===
---
page_id: decision_explainer_bre_standard_objects.htm
title: Decision Explainer Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Standard Objects

Use standard objects to create, update, and activate Decision Explainer
    components.

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

- 
**[ExplainabilityMsgTemplateLocalization](./sforce_api_objects_explainabilitymsgtemplatelocalization.htm.md)**  

       Represents the translated value of the message in an explainability message          template for an expression set step element. This object is available in API version       56.0 and later.

=== ARTICLE: decision_explainer_bre_tooling_objects_parent.htm ===
---
page_id: decision_explainer_bre_tooling_objects_parent.htm
title: Decision Explainer Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_explainer_bre_tooling_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Explainer Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

  

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[ExplainabilityMsgTemplate](./tooling_api_objects_explainabilitymsgtemplate.htm.md)**  

Represents the template that contains the decision explanation          message for a specified element type. This object is available in API version 56.0 and       later.

- 
**[ExpressionSetMessageToken](./tooling_api_objects_expressionsetmessagetoken.htm.md)**  

Represents a token that's used in an explainability message template.          The token can be replaced with an expression set version resource that the template is used          in. This object is available in API version 59.0 and later.

#### See Also

- [*Developer Guide*: Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

=== ARTICLE: decision_table.htm ===
---
page_id: decision_table.htm
title: Decision Table
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: business_rules_engine.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table

A decision table provides outcomes for one or more fields of a standard or custom
    object based on the business rules that you define. The business rules can be part of a standard
    or custom object, or a custom metadata type.

    

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: Decision Table is available with Enterprise, Unlimited, and Performance Editions with Loyalty Management or Rebate Management |

  

    

Information about decision tables are contained in Tooling API objects. Tooling API objects
      let you interact with metadata for declarative development. For example, you can create your
      own version of Setup.

  

- 
**[Decision Table REST APIs](./decision_table_apis.htm.md)**  

Decision table APIs are RESTful APIs that are sometimes available as Apex classes and     methods. You can access Decision Table APIs using REST endpoints. These REST APIs follow similar     conventions as Connect REST APIs.

- 
**[Decision Table Metadata API](./decision_table_metadata_api.htm.md)**  

You can create, edit, and activate a decision table using a Metadata API.

- 
**[Decision Table Invocable Actions](./dt_actions_parent.htm.md)**  

Invoke a decision table or refresh business rules for an active       decision table. For more information on standard and custom invocable actions, see         **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

=== ARTICLE: decision_table_apex_input_classes.htm ===
---
page_id: decision_table_apex_input_classes.htm
title: Input Classes
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apex_input_classes.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Input Classes

These are Decision Table Apex input classes.

- 
**[ConnectApi.DecisionTableInput](./apex_connectapi_input_decision_table.htm.md)**  

Input representation of the decision table.

- 
**[ConnectApi.DecisionTableCondition](./apex_connectapi_input_decision_table_condition_representatio.htm.md)**  

Input representation of the decision table condition.

=== ARTICLE: decision_table_apex_methods.htm ===
---
page_id: decision_table_apex_methods.htm
title: DecisionTable Methods
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apex_methods.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTable Methods

This is a `DecisionTable` method.

- 
**[execute(decisionTableId, DecisionTableInput)](./apex_ConnectAPI_DecisionTable_execute_1.htm.md)**  

Execute an active decision table.

=== ARTICLE: decision_table_apex_output_classes.htm ===
---
page_id: decision_table_apex_output_classes.htm
title: Output Classes
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apex_output_classes.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Output Classes

These are Decision Table Apex output classes.

- 
**[ConnectApi.DecisionTableOutcome](./apex_connectapi_output_decision_table_outcome.htm.md)**  

Output representation of the decision table     execution.

- 
**[ConnectApi.DecisionTableOutcomeItem](./apex_connectapi_output_decision_table_outcome_item.htm.md)**  

Output representation of the decision table outcome     item.

=== ARTICLE: decision_table_apex_reference.htm ===
---
page_id: decision_table_apex_reference.htm
title: Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apex Reference

This Apex reference goes into detail about the built-in Apex `ConnectApi` classes and interfaces.

        

For Apex-related SOAP API calls, see [Apex-Related Calls](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/call_apex_list.htm) in
            the SOAP API Developer Guide. For Apex-related objects, see [Standard Objects](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_list.htm) in the
                Salesforce Object Reference.

    

- 
**[DecisionTable Methods](./decision_table_apex_methods.htm.md)**  

This is a `DecisionTable` method.

- 
**[Input Classes](./decision_table_apex_input_classes.htm.md)**  

These are Decision Table Apex input classes.

- 
**[Output Classes](./decision_table_apex_output_classes.htm.md)**  

These are Decision Table Apex output classes.

=== ARTICLE: decision_table_apis.htm ===
---
page_id: decision_table_apis.htm
title: Decision Table REST APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table REST APIs

Decision table APIs are RESTful APIs that are sometimes available as Apex classes and
    methods. You can access Decision Table APIs using REST endpoints. These REST APIs follow similar
    conventions as Connect REST APIs.

    

To understand the architecture, authentication, rate limits, and how the requests and
      responses work, see [Connect REST API Developer
        Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/).

  

- 
**[Resources](./decision_table_apis_resources.htm.md)**  

Here’s a list of Decision Table API resources.

- 
**[Request Bodies](./decision_table_apis_requests.htm.md)**  

Here’s a list of Decision Table API request bodies.

- 
**[Response Bodies](./decision_table_apis_responses.htm.md)**  

Here’s a list of Decision Table API response bodies.

=== ARTICLE: decision_table_apis_requests.htm ===
---
page_id: decision_table_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Here’s a list of Decision Table API request bodies.

- 
**[Decision Table Input](./connect_requests_decision_table_input.htm.md)**  

Input representation of a decision table.

- 
**[Decision Table Condition Input](./connect_requests_decision_table_condition.htm.md)**  

Input representation of the decision table condition.

- 
**[Decision Table Row List Input](./connect_requests_decision_table_row_list_input.htm.md)**  

Input representation of the data for a row in the CSV based decision       table that has to be added or updated.

- 
**[Decision Table Rows List Input](./connect_requests_decision_table_rows_list_input.htm.md)**  

Input representation of the request to update rows in a CSV based       decision table.

=== ARTICLE: decision_table_apis_resources.htm ===
---
page_id: decision_table_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Decision Table API resources.

- 
**[CSV Based Decision Table (GET)](./connect_resources_decision_table_csv_based_dt.htm.md)**  

Fetch paginated data from a CSV based decision table. This resource is responsible for     managing rows in a Decision Table.

- 
**[Decision Table Execution](./connect_resources_decision_table_execution.htm.md)**  

Execute an active decision table.

=== ARTICLE: decision_table_apis_responses.htm ===
---
page_id: decision_table_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Decision Table API response bodies.

- 
**[Decision Table Data](./connect_responses_decision_table_data_output.htm.md)**  

Output representation of the status of an action performed.

- 
**[Decision Table Outcome](./connect_responses_decision_table_outcome.htm.md)**  

Output representation of the decision table       execution.

- 
**[Decision Table Outcome Item](./connect_responses_decision_table_outcome_item.htm.md)**  

Output representation of the decision table outcome     item.

- 
**[Decision Table Row](./connect_responses_decision_table_row_output.htm.md)**  

Output representation to describe the output of a decision table row.

- 
**[Decision Table Rows List](./connect_responses_decision_table_rows_list_output.htm.md)**  

Output representation of the rows in relation to the decision table, including current     state of pagination.

=== ARTICLE: decision_table_data_model.htm ===
---
page_id: decision_table_data_model.htm
title: Decision Table Data Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_data_model.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Data Model

Before you start using the Decision Table Tooling API objects, here's a representation
  of the data model.

  

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: Decision Table is available with Enterprise, Unlimited, and Performance Editions with Loyalty Management or Rebate Management |

=== ARTICLE: decision_table_metadata_api.htm ===
---
page_id: decision_table_metadata_api.htm
title: Decision Table Metadata API
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/decision_table_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Metadata API

You can create, edit, and activate a decision table using a Metadata API.

  

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: Decision Table is available with Enterprise, Unlimited, and Performance Editions with Loyalty Management or Rebate Management |

  

 

- 
**[DecisionTable](./meta_decisiontable.htm.md)**  

Represents the information about a decision     table.

- 
**[DecisionTableDatasetLink](./meta_decisiontabledatasetlink.htm.md)**  

Represents the information about a dataset link       associated with a decision table. In a dataset link, select an object for whose records, the       decision table must provide an outcome. This type extends the       Metadata metadata type and inherits its fullName field.

=== ARTICLE: dt_actions_parent.htm ===
---
page_id: dt_actions_parent.htm
title: Decision Table Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dt_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Invocable Actions

Invoke a decision table or refresh business rules for an active
      decision table. For more information on standard and custom invocable actions, see
        **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

- 
**[Decision Table Actions](./dt_actions_run_decision_table.htm.md)**  

Invoke a decision table.

- 
**[Decision Table Refresh Action](./dt_actions_refresh_decision_table.htm.md)**  

Refresh business rules for an active decision table.

=== ARTICLE: dt_actions_refresh_decision_table.htm ===
---
page_id: dt_actions_refresh_decision_table.htm
title: Decision Table Refresh Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dt_actions_refresh_decision_table.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Refresh Action

Refresh business rules for an active decision table.

  
   

For more information about refreshing an active decision table, see [Refresh Decision Tables in Flows](https://help.salesforce.com/articleView?id=task_refresh_decision_table_flow.htm&language=en_US) in Salesforce Help. This
    object is available in API version 51.0 and later.

  

  

## Supported REST HTTP Methods

   
   
    
     

**URI**

     
: ``/services/data/vXX.X/`actions/standard/refreshDecisionTable`

    
    
     

**Formats**

     
: JSON

    
    
     

**HTTP Methods**

     
: GET, POST

    
    
     

**Authentication**

     
: `Authorization: Bearer token`

    
   

  

  

## Inputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

      
       

       

: 

: 

      

     

    
| Input | Details |
| --- | --- |
| decisionTable​ApiName | **Type** string **Description** Required. API name of an active decision table that you want to refresh. |
| isDecisionTable​Incremental | **Type** boolean **Description** Specifies whether to trigger an incremental refresh (`true`) or not (`false`). If set to true, this field triggers an update only on changes made to the recent sObject data instead of performing a full refresh. The default value is `false`. This feature requires a full refresh to be performed initially. After a full refresh is done, you can proceed with incremental refreshes. However, if the changes exceed 2,000 records, the incremental refresh fails. In such cases, a full refresh is necessary to update the Decision Table with the latest sObject data. An incremental refresh updates `LastIncrementalSyncDate` only. A full refresh updates `LastRefreshedDate` and `LastSyncDate`. |

  

  

## Outputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

      
       

       

: 

: 

      

     

    
| Output | Details |
| --- | --- |
| errorMessage | **Type** string **Description** Error message to indicate why the request wasn't successful. |
| status | **Type** string **Description** Indicates whether the decision table is queued for refresh. Valid values are `Queued` or `Failed`. |

  

  

## Usage

   
   

**Sample Request**

   
    

```
{
  "inputs": [
    {
      "decisionTableApiName": "Points_to_Redeem_Based_on_Product_and_Order_Channel",
      "isDecisionTableIncremental": true
    }
  ]
}
```

   

   

**Sample Response**

   
    

```

{
   "status":"Queued",//Queued or Failed
   "errorMessage":"" //in case any failure
}

```

=== ARTICLE: dt_actions_run_decision_table.htm ===
---
page_id: dt_actions_run_decision_table.htm
title: Decision Table Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dt_actions_run_decision_table.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Actions

Invoke a decision table.

  
   

Decision tables provide outcomes based on your business rules. For more information about
    invoking decision tables, see [Invoke a Decision Table](https://help.salesforce.com/articleView?id=concept_decision_table_run.htm&language=en_US) in Salesforce Help.

   

This object is available in API version 51.0 and later.

  

  

## Supported REST HTTP Methods

         
            
               

**Formats**

               
: JSON

            
            
               

**HTTP Methods**

               
: GET, POST

            
            
               

**Authentication**

               
: `Authorization: Bearer token`

            
         

The specific URI endpoint and the structure
    of the JSON payload depend on whether a dataset link is configured for your decision table. To
    check if a dataset link is enabled for your decision table, you can query the
    DecisionTableDataLink table. If an entry for your decision table exists in this table, a dataset
    link is active. For more information about dataset links, see [DecisionTableDatasetLink](https://developer.salesforce.com/docs/atlas.en-us.264.0.psc_api.meta/psc_api/tooling_api_objects_decisiontabledatasetlink.htm).

  

## Decision Table Without Dataset Link

If your `decisionTableId` isn't found in the `DecisionTableDatasetLink` table, you must append `_Default` to your decision table's API name to construct the endpoint URI.

    
     

**URI without dataset link**

     
: ``/services/data/vXX.X/`actions/custom/decisionTableAction/dtapi_Default`

    
   

  

## Decision Table With Dataset Link

If your decisionTableId is present in the
    DecisionTableDatasetLink table, the endpoint URI uses the API name of the dataset link.

    
     

**URI with dataset link**

     
: ``/services/data/vXX.X/`actions/custom/decisionTableAction/dslapiname`

    
   

  

## Inputs

   
   

You can choose to invoke a decision table with or without dataset link.

   To execute a default Decision Table without dataset link, specify the input fields that were
    defined at the time of the Decision Table creation in the flow. The input fields are optional.
    However, you must specify at least one field as the input parameter. Use the GET method to
    retrieve input parameters of a Decision Table definition.

#### Note

For example, to decide discount
     percentage for products, you can pass the input parameters, including Brand__c,
     Highest_Price_Point_c, and Lowest_Price_Point_c.

   

To execute a Decision Table with dataset link, specify the list that contains the source
    object and its corresponding field to be used in the dataset link that is associated with the
    decision table.

   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

     

    
| Input | Details |
| --- | --- |
| sObjectType | **Type** sObject **Description** The name of the dataset link’s object whose records, the decision table must provide an outcome for. |

  

  

## Outputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

#### 

      

      
       

       

: 

: 
- 
- 
- 

      

      
       

       

: 

: 

      

     

    
| Output | Details |
| --- | --- |
| outcomeList | **Type** sObject **Description** Outcome list that stores two or more outcomes provided by the decision table. Note A decision table that is invoked by the Decision Table custom invocable action can provide up to 50 outcomes. |
| outcomeType | **Type** string **Description** Indicates the type of outcome provided by the decision table after the request is successful. Valid values are: `Multiple Match—Outcome returns multiple matches.` `No Match`—Outcome returns no match. `Single Match`—Outcome returns single match. |
| singleOutcome | **Type** sObject **Description** Stores the outcome in case a single outcome is provided by the decision table. In case multiple outcomes are provided, it stores one of the outcomes. |

  

  

## Usage

**JSON Sample Request without dataset link**

When you invoke a decisionTableAction without a dataset link, the request contains an array of
            input objects.

    

```

{
   "inputs" : [
      {
        "Product__c": "Cloud Kicks",
        "Price__c": 1000
      }
   ]
}
```

   

**JSON Sample Request with dataset Link**

When you invoke a decisionTableAction
    with a dataset link, the input objects in the request are nested within another object, which is
    typically the name of the transaction object.

    

```

{
   "inputs" : [
      {
         "Transaction__c" : {
            "Product__c": "Cloud Kicks",
            "Price__c": 1000
         }
      }
   ]
}
```

   

**JSON Sample Request with dataset Link containing multiple source objects**

    

```

{
   "inputs" : [
      {
         "Transaction__c" : {
            "Product__c": "Cloud Kicks",
            "Price__c": 1000
         }
      }
      {
         "Catalog__c" : {
            "name": "Highest_Price_Point_c",
            "value": "500",
         }
      }
   ]
}
```

   

**JSON Sample Response**

    

```

[{
   “outcomeType” : “SINGLE MATCH”,
   “singleOutcome”: { “Points”: 100 },
   "outcomeList" : [
      {
         “Points”: 100
      }
   ]
}]

```

=== ARTICLE: dt_setup_objects.htm ===
---
page_id: dt_setup_objects.htm
title: Decision Table Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dt_setup_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Tooling API Objects

Use Tooling API objects to create, update, and activate decision tables. Dataset links
    can also be created and associated with decision tables using Tooling API objects.

    

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: Decision Table is available with Enterprise, Unlimited, and Performance Editions with Loyalty Management or Rebate Management |

  

  

- 
**[Decision Table Data Model](./decision_table_data_model.htm.md)**  

Before you start using the Decision Table Tooling API objects, here's a representation   of the data model.

- 
**[DecisionTable](./tooling_api_objects_decisiontable.htm.md)**  

Represents the information about a decision table. This object is     available in API version 51.0 and later.

- 
**[DecisionTableDatasetLink](./tooling_api_objects_decisiontabledatasetlink.htm.md)**  

     Represents a dataset link associated with a decision table. Use dataset links       in a decision table to select an object whose records the decision table must evaluate and       provide outcomes for. This object is available in API version 51.0 and later. 

- 
**[DecisionTableParameter](./tooling_api_objects_decisiontableparameter.htm.md)**  

Represents an input or output field in a decision table. An input       field is a field in the business rule object or custom metadata type that contains values used       by the decision table to evaluate records and values. An output field is a field in the       business rule object or custom metadata type that contains the values provided as outcomes for       a rule. This object is available in API version 51.0 and later.

- 
**[DecisionTblDatasetParameter](./tooling_api_objects_decisiontbldatasetparameter.htm.md)**  

     Represents the mapping between a decision table parameter and a field of the       object selected in the dataset link. This mapping allows the decision table to know which       object fields from the dataset link must be evaluated by the input fields of the decision       table. This object is available in API version 51.0 and later.

- 
**[DecisionTableSourceCriteria](./tooling_api_objects_decisiontablesourcecriteria.htm.md)**  

Represents the fields and values from a data source that are used to          define the condition logic of the data that's used in a decision table. This object is       available in API version 59.0 and later.

=== ARTICLE: expression_set_connect_apis.htm ===
---
page_id: expression_set_connect_apis.htm
title: Expression Set Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_connect_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Business APIs

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce
        software and UIs.

The runtime service for Expression Set is exposed through Connect APIs.

With Expression Set Connect APIs, you can:

                
- 
[Invoke an expression set](./connect_resources_bre_expression_set.htm.md).

            
- 
[Create an expression set](./connect_resources_bre_create_expression_set.htm.md).

        

- 
**[Resources](./expression_set_resources.htm.md)**  

Expression Set API includes these resources.

- 
**[Request Bodies](./expression_set_requests.htm.md)**  

Expression Set API includes these request bodies.

- 
**[Response Bodies](./expression_set_responses.htm.md)**  

Expression Set API includes these response bodies.

=== ARTICLE: expression_set_flow_metadata_api.htm ===
---
page_id: expression_set_flow_metadata_api.htm
title: Flow for Expression Set
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Expression Set

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Business Rules Engine exposes additional actionType values for the FlowActionCall Metadata
        type. For more information on Flow and FlowActionCall metadata type, see [Flow](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_visual_workflow.htm).

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Expression Set include: `runExpressionSet`—Invoke an active expression set. This value is available in API version 55.0 and later. |

=== ARTICLE: expression_set_invocable_actions.htm ===
---
page_id: expression_set_invocable_actions.htm
title: Expression Set Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_invocable_actions.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Invocable Actions

Use actions to invoke Expression Set actions in a flow.

    
      

#### Note

        

You can also use the Invocable namespace, which contains the classes and methods required
          to invoke the Decision Matrix and Expression Set invocable actions from Apex. See [Invocable Namespace](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_Invocable.htm).

      

    

  

- 
**[Expression Set Actions](./actions_obj_expression_set.htm.md)**  

Invoke an active expression set. An expression set is a user-defined       rule that accepts an input and returns the output based on the configured     function.

=== ARTICLE: expression_set_metadata_api_parent.htm ===
---
page_id: expression_set_metadata_api_parent.htm
title: Expression Set Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[ExpressionSetDefinition](./meta_expressionsetdefinition.htm.md)**  

Represents an expression set definition. 	

- 
**[ExpressionSetMessageToken](./meta_expressionsetmessagetoken.htm.md)**  

Represents an interface to retrieve, deploy, 			create, update, or delete information on Expression Set Message Token.

- 
**[ExpressionSetObjectAlias](./meta_expressionsetobjectalias.htm.md)**  

Represents information about the alias of the source 			object that’s used in an expression set. 	

- 
**[Flow for Expression Set](./expression_set_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: expression_set_parent.htm ===
---
page_id: expression_set_parent.htm
title: Expression Set
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: business_rules_engine.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set

Expression sets consist of a series of steps connected in a logical flow built from
        variables, constants, conditions, calculations, lookups, and aggregations.

- 
**[Expression Set Standard Objects](./expression_set_standard_objects.htm.md)**  

Use standard objects to create, update, and activate Expression Set     components.

- 
**[Expression Set Business APIs](./expression_set_connect_apis.htm.md)**  

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce         software and UIs.

- 
**[Expression Set Invocable Actions](./expression_set_invocable_actions.htm.md)**  

Use actions to invoke Expression Set actions in a flow.

- 
**[Expression Set Metadata API Types](./expression_set_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Expression Set Tooling API Objects](./expression_set_tooling_objects_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

#### See Also

- [*Salesforce Help*: Expression Sets](https://help.salesforce.com/s/articleView?id=ind.expression_sets.htm&type=5&language=en_US)

=== ARTICLE: expression_set_requests.htm ===
---
page_id: expression_set_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Expression Set API includes these request bodies.

- 
**[Business Rules Input](./connect_requests_business_rules_input.htm.md)**  

Input representation of an expression set.

- 
**[Context Definition Input](./connect_requests_context_definition_input.htm.md)**  

Input representation of the context definitions in an expression       set.

- 
**[Expression Set Advanced Condition Step Input](./connect_requests_expression_set_advanced_condition_step.htm.md)**  

Input representation of an advanced condition step in an expression       set.

- 
**[Expression Set Aggregation Step Input](./connect_requests_expression_set_aggregation_step.htm.md)**  

Input representation of an aggregation step in an expression     set.

- 
**[Expression Set Assignment Step Input](./connect_requests_expression_set_assignment_step.htm.md)**  

Input representation of an assignment step in an expression     set.

- 
**[Expression Set Condition Criteria Input](./connect_requests_expression_set_condition_criteria.htm.md)**  

Input representation of a condition criteria in an expression       set.

- 
**[Expression Set Condition Expression Step](./connect_requests_expression_set_condition_expression_step.htm.md)**  

Input representation of an expression set condition     step.

- 
**[Expression Set Custom Element Parameter Input](./connect_requests_expression_set_custom_element_parameter.htm.md)**  

Input representation of a custom element parameter in an expression       set.

- 
**[Expression Set Custom Element Step Input](./connect_requests_expression_set_custom_element_step.htm.md)**  

Input representation of a custom element step in an expression       set.

- 
**[Expression Set DES Token Mapping Input](./connect_requests_expression_set_des_token_mapping.htm.md)**  

Input representation of the DES token mapping in an expression set       version step.

- 
**[Expression Set Input](./connect_requests_expression_set_input.htm.md)**  

Input representation of the expression set create and update       request.

- 
**[Expression Set Lookup Table Step Input](./connect_requests_expression_set_lookup_table_step.htm.md)**  

Input representation of a lookup table step in an expression     set.

- 
**[Expression Set Options Input](./connect_requests_options.htm.md)**  

Input representation of the options for executing an expression       set.

- 
**[Expression Set SubExpression Step Input](./connect_requests_expression_set_sub_expression_step.htm.md)**  

Input representation of a subexpression step in an expression       set.

- 
**[Expression Set Version Input](./connect_requests_expression_set_version.htm.md)**  

Input representation of an expression set version.

- 
**[Expression Set Version Step Input](./connect_requests_expression_set_version_step.htm.md)**  

Input representation of a step in an expression set     version.

- 
**[Expression Set Version Variable Input](./connect_requests_expression_set_version_variable.htm.md)**  

Input representation of a variable in an expression set     version.

=== ARTICLE: expression_set_resources.htm ===
---
page_id: expression_set_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Expression Set API includes these resources.

- 
**[Expression Set (POST)](./connect_resources_bre_create_expression_set.htm.md)**  

Creates an expression set in Business Rules Engine. An expression       set performs a series of calculations by using lookup tables and user-defined variables and       constants.

- 
**[Expression Set (DELETE, GET)](./connect_resources_bre_expression_set_id_delete_get.htm.md)**  

Read or delete expression set for a specified expression set       ID.

- 
**[Expression Set (PATCH)](./connect_resources_bre_expression_set_id_patch.htm.md)**  

Endpoint to update expression set.

- 
**[Expression Set Invocation (POST)](./connect_resources_bre_expression_set.htm.md)**  

Invokes expression sets in Business Rule Engine.

- 
**[Expression Set Version Dependencies (GET)](./connect_resources_expression_set_dependencies.htm.md)**  

Retrieve expression set version dependencies.

- 
**[Guardrails (GET)](./connect_resources_bre_guardrail.htm.md)**  

Fetches guardrails from the Business Rules Engine (BRE) to manage rate limits for BRE     components.

=== ARTICLE: expression_set_responses.htm ===
---
page_id: expression_set_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Expression Set API includes these response bodies.

- 
**[Current Value](./connect_responses_current_value.htm.md)**  

Output representation of the current value of the guardrail at a row level.

- 
**[BRE Guardrails](./connect_responses_bre_guardrails.htm.md)**  

Output representation of the BRE     guardrails     for each component.

- 
**[BRE Guardrails Result](./connect_responses_bre_guardrails_result.htm.md)**  

Output representation of the BRE Guardrails result.

- 
**[Guardrails](./connect_responses_guardrails.htm.md)**  

Output representation of each guardrail that includes information to manage system     thresholds and notifications in BRE components.

- 
**[Guardrail Current Value](./connect_responses_guardrail_current_value.htm.md)**  

Output representation of the current values of the guardrails along with the resource     type.

- 
**[Business Rules Aggregation Results](./connect_responses_business_rule_aggregation_results_output.htm.md)**  

Output representation of expression set results.

- 
**[Business Rules Results](./connect_responses_business_rules_result.htm.md)**  

Output representation of executing an expression set.

- 
**[Context Definition Output](./connect_responses_context_definition_output.htm.md)**  

Output representation of the context definitions in an expression       set.

- 
**[Dependency Detail Output](./connect_responses_dependency_detail_output.htm.md)**  

Output representation of the  expression set version       dependencies.

- 
**[Error Result](./connect_responses_error_result.htm.md)**  

Output representation of the errors in the execution of an expression       set.

- 
**[Expression Set Output](./connect_responses_expression_set_output.htm.md)**  

Output representation of the expression set       create,       update and delete request.

- 
**[Expression Set Advanced Condition Step](./connect_responses_expression_set_advanced_condition_step_output.htm.md)**  

Output representation of an advanced condition step in an expression       set.

- 
**[Expression Set Aggregation Step](./connect_responses_expression_set_aggregation_step_output.htm.md)**  

Output representation of the expression set aggregation     step.

- 
**[Expression Set Assignment Step](./connect_responses_expression_set_assignment_step_output.htm.md)**  

Output representation of an assignment step in an expression     set.

- 
**[Expression Set Condition Criteria](./connect_responses_expression_set_condition_criteria_output.htm.md)**  

Output representation of a condition criteria in an expression       set.

- 
**[Expression Set Condition Expression Step](./connect_responses_expression_set_condition_expression_step_output.htm.md)**  

Output representation of a condition step in an expression     set.

- 
**[Expression Set Custom Element Parameter](./connect_responses_expression_set_custom_element_parameter_output.htm.md)**  

Output representation of a custom element parameter in an expression       set.

- 
**[Expression Set Custom Element Step](./connect_responses_expression_set_custom_element_step_output.htm.md)**  

Output representation of a custom element step in an expression       set.

- 
**[Expression Set DES Token Mapping](./connect_responses_expression_set_des_token_mapping.htm.md)**  

Output representation of the DES token mapping in an expression set       version step.

- 
**[Expression Set Error](./connect_responses_expression_set_error.htm.md)**  

Representation of the expression set errors.

- 
**[Expression Set Lookup Table Step](./connect_responses_expression_set_lookup_table_step_output.htm.md)**  

Output representation of a lookup table step in an expression       set.

- 
**[Expression Set SubExpression Step](./connect_responses_expression_set_sub_expression_step_output.htm.md)**  

Output representation of a subexpression step in an expression       set.

- 
**[Expression Set Version Dependency](./connect_responses_expression_set_version_dependency_output.htm.md)**  

Output representation for the expression set version     dependency.

- 
**[Expression Set Version Output](./connect_responses_expression_set_version_output.htm.md)**  

Output representation of an expression set version.

- 
**[Expression Set Version Step](./connect_responses_expression_set_version_step_output.htm.md)**  

Output representation of a step in an expression set     version.

- 
**[Expression Set Version Variable](./connect_responses_expression_set_version_variable_output.htm.md)**  

Output representation of a variable in an expression set     version.

- 
**[Rule Results](./connect_responses_rule_result.htm.md)**  

Output representation of the result of executing a single input in an       expression set.

- 
**[Variable Map Output](./connect_responses_variable_map_output.htm.md)**  

Output representation of the input variables in an expression set       version.

- 
**[Variable Output](./connect_responses_variable_output.htm.md)**  

Output representation of the input variables in an expression       set.

=== ARTICLE: expression_set_standard_objects.htm ===
---
page_id: expression_set_standard_objects.htm
title: Expression Set Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Standard Objects

Use standard objects to create, update, and activate Expression Set
    components.

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

- 
**[ExpressionSet](./sforce_api_objects_expressionset.htm.md)**  

Represents information about an expression set. An expression set          performs a series of calculations using lookups and user-defined variables and          constants. This object is available in API version 55.0 and later.

- 
**[ExpressionSetDefinitionContextDefinition](./sforce_api_objects_expressionsetdefinitioncontextdefinition.htm.md)**  

Represents a relationship between an expression set definition and a          context definition. This object is available in API version 58.0 and       later.

- 
**[ExpressionSetVersion](./sforce_api_objects_expressionsetversion.htm.md)**  

Represents information about a specific version of an expression set.          This object is also accessible through the UI API, which enables its use in components like          Lightning Web Components (LWC). This object is available in API version 55.0 and       later.

- 
**[ExpressionSetView](./sforce_api_objects_expressionsetview.htm.md)**  

Represents a virtual object that provides a consolidated view of          file-based expression set. File-based expression sets are read-only templates. To be able          to modify file-based expression sets, you must clone them first.  This object is       available in API version 55.0 and later.

- 
**[ExpsSetObjectAliasFieldVw](./sforce_api_objects_expssetobjectaliasfieldvw.htm.md)**  

Represents the virtual object that provides a consolidated view of          source object and its alias, and the source object fields and their aliases that are used          in an expression set. This object is used to check the permission level required to access          the underlying object fields associated with their field aliases. This object is       available in API version 56.0 and later.

=== ARTICLE: expression_set_tooling_objects_parent.htm ===
---
page_id: expression_set_tooling_objects_parent.htm
title: Expression Set Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/expression_set_tooling_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Expression Set Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

  

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[ExpressionSetDefinition](./tooling_api_objects_expressionsetdefinition.htm.md)**  

Represents information about an expression set definition. This       object is available in API version 55.0 and later.

- 
**[ExpressionSetDefinitionVersion](./tooling_api_objects_expressionsetdefinitionversion.htm.md)**  

Represents information about an expression set definition          version. This object is available in API version 55.0 and later.

- 
**[ExpressionSetObjectAlias](./tooling_api_objects_expressionsetobjectalias.htm.md)**  

Represents the alias of the source object that's used in an          expression set. This object is available in API version 56.0 and later.

#### See Also

- [*Developer Guide*: Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

=== ARTICLE: lookup_table_resources.htm ===
---
page_id: lookup_table_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_table_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Lookup Table API includes these resources.

- 
**[Decision Matrix Lookup (POST)](./connect_resources_bre_decision_matrix.htm.md)**  

Performs a lookup on decision matrix rows based on the input values       provided, and returns the row’s output.

- 
**[Decision Model Notation Export (POST)](./connect_resources_bre_decision_model_entity.htm.md)**  

Export decision matrix data to a file in the DMN (Decision Model       Notation) format, an easily readable format for business rules designed by Object Management       Group.

- 
**[Decision Table Definitions (POST)](./connect_resources_decision_table_definition_details_post.htm.md)**  

Create a decision table definition. A decision table definition     contains all the details required to create a decision table.

- 
**[Decision Table Definitions (DELETE, GET)](./connect_resources_decision_table_definition_details.htm.md)**  

Get details of a decision table definition. Delete a decision table       definition associated with a decision table.

- 
**[Decision Table Definitions (PATCH)](./connect_resources_decision_table_definition_details_patch.htm.md)**  

Update a decision table definition associated with a decision       table.

- 
**[Decision Table Lookup (POST)](./connect_resources_bre_decision_table.htm.md)**  

Performs a lookup on a decision table.

- 
**[Decision Table Invocation (POST)](./connect_resources_decisionTableId.htm.md)**  

Invoke a decision table by passing multiple input conditions within       the same request.

- 
**[Lookup Tables (GET)](./connect_resources_bre_search_lookup_tables.htm.md)**  

Retrieve lookup tables.

- 
**[CSV Based Decision Table (GET)](./connect_resources_decision_table_csv_based_dt.htm.md)**  

Fetch paginated data from a CSV based decision table. This resource is responsible for     managing rows in a Decision Table.

- 
**[Decision Table Execution](./connect_resources_decision_table_execution.htm.md)**  

Execute an active decision table.

=== ARTICLE: lookup_tables_connect_apis.htm ===
---
page_id: lookup_tables_connect_apis.htm
title: Lookup Tables Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_connect_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Business APIs

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce
        software and UIs.

The runtime service for Lookup Table components is exposed through Connect APIs.

With Lookup Table Connect APIs, you can:

            
- 
[Perform a lookup on a decision matrix](./connect_resources_bre_decision_matrix.htm.md).

            
- 
[Perform a lookup on a decision table](./connect_resources_bre_decision_table.htm.md).

            
- 
[Retrieve lookup tables](./connect_resources_bre_search_lookup_tables.htm.md).

        

- 
**[Resources](./lookup_table_resources.htm.md)**  

Lookup Table API includes these resources.

- 
**[Request Bodies](./lookup_tables_requests.htm.md)**  

Lookup Table API includes these request bodies.

- 
**[Response Bodies](./lookup_tables_responses.htm.md)**  

Lookup Table API includes these response bodies.

=== ARTICLE: lookup_tables_decision_matrix_data_model.htm ===
---
page_id: lookup_tables_decision_matrix_data_model.htm
title: Decision Matrix Data Model Overview
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_decision_matrix_data_model.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Matrix Data Model Overview

Learn about the objects and relationships within the Decision Matrix data
    model.

   

The Decision Matrix data model provides a set of objects and fields that you can refer to
    implement and extend decision matrices.

   
    
   

   

To view a larger version, right-click or Ctrl+click the image and select **Open Image
     in New Tab**.

=== ARTICLE: lookup_tables_flow_metadata_api.htm ===
---
page_id: lookup_tables_flow_metadata_api.htm
title: Flow for Lookup Tables
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Lookup Tables

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Business Rules Engine exposes additional actionType values for the FlowActionCall Metadata
        type. For more information on Flow and FlowActionCall metadata type, see [Flow](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_visual_workflow.htm).

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Lookup Tables include: `runDecisionMatrix`—Invoke a decision matrix in a flow. This value is available in API version 55.0 and later. |

=== ARTICLE: lookup_tables_invocable_actions.htm ===
---
page_id: lookup_tables_invocable_actions.htm
title: Lookup Tables Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_invocable_actions.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Invocable Actions

Use actions to invoke Lookup Table actions in a flow.

    
      

#### Note

        

You can also use the Invocable namespace, which contains the classes and methods required
          to invoke the Decision Matrix and Expression Set invocable actions from Apex. See [Invocable Namespace](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_Invocable.htm).

      

    

  

- 
**[Decision Matrix Actions](./actions_obj_decision_matrix.htm.md)**  

Invoke a decision matrix in a flow with the Decision Matrix       Actions. A decision matrix is a user-defined table where you can look up an output based     on the inputs you provide. 

- 
**[Decision Table Refresh Action](./dt_actions_refresh_decision_table.htm.md)**  

Refresh business rules for an active decision table.

- 
**[Decision Table Actions](./dt_actions_run_decision_table.htm.md)**  

Invoke a decision table.

=== ARTICLE: lookup_tables_metadata_api_parent.htm ===
---
page_id: lookup_tables_metadata_api_parent.htm
title: Lookup Tables Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[DecisionMatrixDefinition](./meta_decisionmatrixdefinition.htm.md)**  

Represents a definition of a decision matrix. 	

- 
**[Flow for Lookup Tables](./lookup_tables_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

- 
**[DecisionTable](./meta_decisiontable.htm.md)**  

Represents the information about a decision     table.

- 
**[DecisionTableDatasetLink](./meta_decisiontabledatasetlink.htm.md)**  

Represents the information about a dataset link       associated with a decision table. In a dataset link, select an object for whose records, the       decision table must provide an outcome. This type extends the       Metadata metadata type and inherits its fullName field.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: lookup_tables_parent.htm ===
---
page_id: lookup_tables_parent.htm
title: Lookup Tables
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: business_rules_engine.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables

Business Rules Engine has two types of lookup tables—decision matrices and decision
        tables. Learn more about the developer resources of lookup tables for integration with
        Flows, Omniscripts, or any third-party custom tools.

- 
**[Decision Matrix Data Model Overview](./lookup_tables_decision_matrix_data_model.htm.md)**  

Learn about the objects and relationships within the Decision Matrix data     model.

- 
**[Lookup Tables Standard Objects](./lookup_tables_standard_objects.htm.md)**  

Use standard objects to create, update, and activate Lookup Table     components.

- 
**[Lookup Tables Business APIs](./lookup_tables_connect_apis.htm.md)**  

Connect REST APIs help customers, partners, and ISVs integrate with Salesforce         software and UIs.

- 
**[BusinessRule Namespace](./apex_namespace_BusinessRule.htm.md)**  

The `BusinessRule` namespace provides classes for     migrating calculation matrices and calculation procedures from Vlocity to the Business Rules     Engine in Salesforce.

- 
**[Lookup Tables Invocable Actions](./lookup_tables_invocable_actions.htm.md)**  

Use actions to invoke Lookup Table actions in a flow.

- 
**[Lookup Tables Metadata API Types](./lookup_tables_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Lookup Tables Tooling API Objects](./lookup_tables_tooling_objects_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

- 
**[Decision Table Tooling API Objects](./dt_setup_objects.htm.md)**  

Use Tooling API objects to create, update, and activate decision tables. Dataset links     can also be created and associated with decision tables using Tooling API objects.

- 
**[Apex Reference](./decision_table_apex_reference.htm.md)**  

This Apex reference goes into detail about the built-in Apex `ConnectApi` classes and interfaces.

#### See Also

- [*Salesforce Help*: Decision Matrices](https://help.salesforce.com/s/articleView?id=ind.decision_matrices.htm&type=5&language=en_US)

- [*Salesforce Help*: Decision Tables](https://help.salesforce.com/s/articleView?id=ind.decision_tables.htm&type=5&language=en_US)

=== ARTICLE: lookup_tables_requests.htm ===
---
page_id: lookup_tables_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Lookup Table API includes these request bodies.

- 
**[Decision Matrix Input](./connect_requests_decision_matrix_input.htm.md)**  

Input representation of the inputs passed to a decision matrix for       lookup.

- 
**[Decision Matrix Lookup Input](./connect_requests_decision_matrix_lookup.htm.md)**  

Input representation of the input for a decision matrix     lookup.

- 
**[Decision Matrix Options Input](./connect_requests_decision_matrix_options.htm.md)**  

Input representation of the options used to look up a decision       matrix.

- 
**[Decision Matrix Variable Input](./connect_requests_decision_matrix_variable.htm.md)**  

Input representation of the variables in an input passed to a decision       matrix lookup.

- 
**[Decision Model Export Input](./connect_requests_decision_model_export_input.htm.md)**  

Input representation of the request to export decision matrix       data.

- 
**[Decision Table Bulk Input](./connect_requests_decision_table_bulk_input.htm.md)**  

Input representation of the Decision Table bulk       lookup.

- 
**[Decision Table Condition Input](./connect_requests_decision_table_condition.htm.md)**  

Input representation of the decision table condition.

- 
**[Decision Table Condition List Input](./connect_requests_decision_table_condition_list_input.htm.md)**  

Input representation of the Decision Table condition       list.

- 
**[Decision Table Input](./connect_requests_decision_table_input.htm.md)**  

Input representation of a decision table.

- 
**[Decision Table Definition Input](./connect_requests_decision_table_definition_input.htm.md)**  

Input representation of a decision table       definition.

- 
**[Decision Table Parameter Input](./connect_requests_decision_table_parameter_input.htm.md)**  

Input representation of parameters defined for the decision       table.

- 
**[Decision Table Source Criteria Input](./connect_requests_decision_table_source_criteria_input.htm.md)**  

Input representation of source criteria for the decision     table.

- 
**[Decision Table Row List Input](./connect_requests_decision_table_row_list_input.htm.md)**  

Input representation of the data for a row in the CSV based decision       table that has to be added or updated.

- 
**[Decision Table Rows List Input](./connect_requests_decision_table_rows_list_input.htm.md)**  

Input representation of the request to update rows in a CSV based       decision table.

=== ARTICLE: lookup_tables_responses.htm ===
---
page_id: lookup_tables_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Lookup Table API includes these response bodies.

- 
**[Decision Matrix Lookup Basic Result](./connect_responses_decision_matrix_lookup_basic_result.htm.md)**  

Results from a Decision Matrix lookup using a single   input.

- 
**[Decision Matrix Lookup Result](./connect_responses_bre_decision_matrix_lookup_result.htm.md)**  

Output representation of the individual output of a decision matrix       version lookup.

- 
**[Decision Model Export Error](./connect_responses_decision_model_export_error.htm.md)**  

Error representation of a failed DMN (Decision Model Notation) export       request.

- 
**[Decision Model Export Output](./connect_responses_decision_model_export_output.htm.md)**  

Output representation of a completed DMN (Decision Model Notation)       export request.

- 
**[Decision Table Bulk Outcome](./connect_responses_decision_table_bulk_outcome.htm.md)**  

Output representation of the decision table bulk     look-up.

- 
**[Decision Table Definition Output](./connect_responses_decision_table_definition_output.htm.md)**  

Output representation of a decision table definition associated with a       decision table.

- 
**[Decision Table Outcome](./connect_responses_decision_table_outcome.htm.md)**  

Output representation of the decision table       execution.

- 
**[Decision Table Outcome Item](./connect_responses_decision_table_outcome_item.htm.md)**  

Output representation of the decision table outcome     item.

- 
**[Decision Table Output](./connect_responses_decision_table_output.htm.md)**  

Output representation of the decision table details.

- 
**[Decision Table Parameter Output](./connect_responses_decision_table_parameter_output.htm.md)**  

Output representation of a decision table parameter.

- 
**[Decision Table Source Criteria Output](./connect_responses_decision_table_source_criteria_output.htm.md)**  

Output representation of the decision table source     criteria.

- 
**[Decision Table Data](./connect_responses_decision_table_data_output.htm.md)**  

Output representation of the status of an action performed.

- 
**[Decision Table Row](./connect_responses_decision_table_row_output.htm.md)**  

Output representation to describe the output of a decision table row.

- 
**[Decision Table Rows List](./connect_responses_decision_table_rows_list_output.htm.md)**  

Output representation of the rows in relation to the decision table, including current     state of pagination.

- 
**[Lookup Table Details](./connect_responses_lookup_table_details.htm.md)**  

Output representation of the basic details of a lookup     table.

- 
**[Lookup Tables Result List](./connect_responses_lookup_tables_result_list.htm.md)**  

Output representation of the result of a lookup table search       request.

=== ARTICLE: lookup_tables_standard_objects.htm ===
---
page_id: lookup_tables_standard_objects.htm
title: Lookup Tables Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Standard Objects

Use standard objects to create, update, and activate Lookup Table
    components.

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

- 
**[CalculationMatrix](./sforce_api_objects_calculationmatrix.htm.md)**  

Matches input values to a table row and returns the row's output          values. The label for this object is Decision Matrix. This object is available in API       version 53.0 and later.

- 
**[CalculationMatrixColumn](./sforce_api_objects_calculationmatrixcolumn.htm.md)**  

       Defines a column in a Decision Matrix. The label for this object is Decision          Matrix Column. This object is available in API version 53.0 and later. 

- 
**[CalcMatrixColumnRange](./sforce_api_objects_calcmatrixcolumnrange.htm.md)**  

Represents information about a value in a decision matrix column when          the column is of the type number range or text range. This object is available in API       version 59.0 and later.

- 
**[CalculationMatrixRow](./sforce_api_objects_calculationmatrixrow.htm.md)**  

       Defines a row in a Decision Matrix. The label for this object is Decision          Matrix Row. This object is available in API version 53.0 and later. 

- 
**[CalculationMatrixVersion](./sforce_api_objects_calculationmatrixversion.htm.md)**  

Defines a version of a Decision Matrix. The label for this object is          Decision Matrix Version. This object is available in API version 53.0 and       later.

=== ARTICLE: lookup_tables_tooling_objects_parent.htm ===
---
page_id: lookup_tables_tooling_objects_parent.htm
title: Lookup Tables Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/lookup_tables_tooling_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Tables Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

  

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Professional**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[DecisionMatrixDefinition](./tooling_api_objects_decisionmatrixdefinition.htm.md)**  

Represents information about a decision matrix definition. This       object is available in API version 55.0 and later.

- 
**[DecisionMatrixDefinitionVersion](./tooling_api_objects_decisionmatrixdefinitionversion.htm.md)**  

Represents information about a decision matrix definition          version. This object is available in API version 55.0 and later.

#### See Also

- [*Developer Guide*: Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

=== ARTICLE: meta_decisionmatrixdefinition.htm ===
---
page_id: meta_decisionmatrixdefinition.htm
title: DecisionMatrixDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_decisionmatrixdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionMatrixDefinition

Represents a definition of a decision matrix.
	

		
			

#### Note

Before deploying a decision matrix or a decision matrix version to a target org,
				review these [decision matrix migration considerations](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US).

		

		This type extends the Metadata metadata type and inherits its
					fullName field.

		

## File Suffix and Directory Location

			
			

DecisionMatrixDefinition components have the suffix
					.decisionMatrixDefinition and are stored in the
					decisionMatrixDefinition folder.

		

		

## Version

			
			

DecisionMatrixDefinition components are available in API version 55.0 and later.

		

		
		

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
- 
- 
- 
- 
- 
- 
- 
- 

: 

#### 

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

						

					

				
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** Describes a decision matrix definition. |
| groupKey | **Field Type** string **Description** A key for grouping matrix rows in different versions, such as a geographic region or a product code. |
| label | **Field Type** string **Description** Required. The UI label of a decision matrix definition. |
| processType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** The process type that uses the expression set rule. Valid values are: `Bre` `GpaCalculation` `InsuranceClaimProcessing`—Available in API version 65.0 and later. `ItServiceManagement`—Available in API version 65.0 and later. `PlanCostCalculation` `RatingDiscovery` `StudentInformationSystem`—Available in API version 65.0 and later. `StudentSuccess` Note When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other usage types may be available to you depending on your industry solution and permission sets. Available in API version 59.0 and later. |
| subGroupKey | **Field Type** string **Description** A subgroup key for grouping matrix rows in different versions, such as a geographic region or a product code. For example, if the groupKey is `Country`, the subGroupKey can be `State` or `Province`. |
| type | **Field Type** DecisionMatrixType (enumeration of type string) **Description** The type of a decision matrix. Valid values are: `Grouped` `Standard` |
| versions | **Field Type** [DecisionMatrixDefinitionVersion](#DMDV)[] **Description** Represents an array of decision matrix version definitions in a decision matrix. This array must contain at least one version. |

		

		

## DecisionMatrixDefinitionVersion

			
			

Represents a definition of a decision matrix version.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

: 

						

						
							

							

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

						

						
							

							

: 

: 

						

						
							

							

: 

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| columns | **Field Type** [DecisionMatrixDefinitionVersionColumn​​](#DMDVcolumn)[] **Description** Represents an array of columns in a decision matrix definition version. |
| decisionMatrixDefinition | **Field Type** string **Description** The full name of a decision matrix version. |
| endDate | **Field Type** dateTime **Description** The date until which a decision matrix definition version is available for use. |
| groupKeyValue | **Field Type** string **Description** The value of the groupKey for a decision matrix definition version. For example, if the groupKey is `Country`, the groupKeyValue can be `United States`. |
| label | **Field Type** string **Description** Required. The UI label of a decision matrix definition version. |
| rank | **Field Type** int **Description** The rank of the Decision Matrix Definition Version. When more than one enabled version matches a decision matrix call, and the start date time to end date time spans overlap, the version with the highest rank is chosen. Available in API version 64.0 and later. |
| startDate | **Field Type** dateTime **Description** Required. The date from when a decision matrix definition version is available for use. |
| status | **Field Type** DecisionMatrixDefStatus (enumeration of type string) **Description** Required. Specifies the status of a decision matrix definition version. Valid values are: `Active` `Draft` `Inactive` `InvalidDraft` `Obsolete` |
| subGroupKeyValue | **Field Type** string **Description** The value of the subgroup key for a decision matrix definition version. For example, if the subGroupKey is `State` or `Province`, the subGroupKeyValue can be `California`. |
| versionNumber | **Field Type** int **Description** Required. The version number of a decision matrix definition. |

		

		

## DecisionMatrixDefinitionVersionColumn​​

			
			

Represents a definition of a column in a decision matrix definition version.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Field Name | Description |
| --- | --- |
| columnType | **Field Type** DecisionMatrixColumnType (enumeration of type string) **Description** Required. Specifies whether a column is for an input or output. Valid values are: `Input` `Output` |
| dataType | **Field Type** DecisionMatrixDataType (enumeration of type string) **Description** Required. The type of data that’s stored in a column. Valid values are: `Boolean` `Currency` `Number` `NumberRange` `Percent` `Text` `TextRange` |
| displaySequence | **Field Type** int **Description** Required. Represents the position of a column in the column order. |
| isWildcardColumn | **Field Type** boolean **Description** Required. Specifies whether a column stores a wildcard value (`true`) or not (`false`). The default value is `false`. |
| name | **Field Type** string **Description** Required. The full name of a decision matrix definition version column. |
| rangeValue | **Field Type** string **Description** A list of values that define range boundaries. |
| wildcardValue | **Field Type** string **Description** The wildcard value such as `ALL`. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of a DecisionMatrixDefinition component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<DecisionMatrixDefinition
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<label>HealthCloudUM_ValidRegions</label>
	<type>Standard</type>
	<versions>
		<fullName>HealthCloudUM_ValidRegions_V1</fullName>
		<columns>
			<columnType>Input</columnType>
			<dataType>Text</dataType>
			<displaySequence>2</displaySequence>
			<isWildcardColumn>false</isWildcardColumn>
			<name>State</name>
		</columns>
		<columns>
			<columnType>Input</columnType>
			<dataType>Text</dataType>
			<displaySequence>1</displaySequence>
			<isWildcardColumn>false</isWildcardColumn>
			<name>City</name>
		</columns>
		<columns>
			<columnType>Output</columnType>
			<dataType>Boolean</dataType>
			<displaySequence>3</displaySequence>
			<isWildcardColumn>false</isWildcardColumn>
			<name>IsValid</name>
		</columns>
		<decisionMatrixDefinition>HealthCloudUM_ValidRegions</decisionMatrixDefinition>
		<label>HealthCloudUM_ValidRegions V1</label>
		<startDate>2022-05-02T13:04:06.000Z</startDate>
		<status>Draft</status>
		<versionNumber>1</versionNumber>
	</versions>
</DecisionMatrixDefinition>
```

			

The following is an example `package.xml` that references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>DecisionMatrixDefinition</name>
	</types>
	<version>67.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based.htm).

=== ARTICLE: meta_decisiontable.htm ===
---
page_id: meta_decisiontable.htm
title: DecisionTable
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_decisiontable.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_metadata_api.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTable

Represents the information about a decision
    table.

    

      

#### Important

 Where possible, we changed noninclusive terms to
        align with our company value of Equality. We maintained certain terms to avoid any effect on
        customer implementations. 

    

    

## Parent Type

       This type extends the Metadata metadata type and inherits its fullName field. 

    

## File Suffix and Directory Location

      
      

DecisionTable components have the suffix .decisionTable and are stored
        in the decisionTables folder.

    

    

## Version

      
      

DecisionTable components are available in API version 51.0 and later.

    

    

## Special Access Rules

      
      

To use this metadata type, your Salesforce org must have the Loyalty Management or the
        Rebate Management license.

    

    

## Fields

      
      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

- 
- 
- 
- 
- 

            

            
              

              

: 

: 

            

            
              

              

: 

: 

- 
- 
- 

            

            
              

              

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

- 
- 
- 

            

            
              

              

: 

: 

- 
- 
- 
- 
- 

            

            
              

              

: 

: 

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

- 
- 
- 
- 
- 
- 

            

            
              

              

: 

: 

- 
- 
- 
- 

            

            
              

              

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

            

          

        
| Field Name | Description |
| --- | --- |
| collectOperator | **Field Type** DecisionTable​CollectOperator (enumeration of type string) **Description** Specifies the operator that's used when the result is filtered by the Collect operator.Valid values are: `Count` `Maximum` `Minimum` `None` `Sum` |
| condition​Criteria | **Field Type** string **Description** Logic that's used to decide how the input fields are processed. |
| conditionType | **Field Type** DecisionTable​ConditionType (enumeration of type string) **Description** Condition logic that's used for input fields.Valid values are: `All` `Any` `Custom` |
| dataSource​Type | **Field Type** DecisionTable​DataSourceType (enumeration of type string) **Description** Specifies the type of data source that's used to create a decision table.Valid values are: `ContextDefinition` `CsvUpload` `MultipleSobjects` `SingleSobject` |
| decisionTable​FileImportVersions | **Field Type** [DecisionTableFileImportVersion](#DecisionTableFileImportVersion)[] **Description** Versions of the decision table that were imported from a CSV file. Each version captures a separate import iteration with its own activation window, rank, and refresh status. Available in API version 67.0 and later. |
| decisionTable​Parameters | **Field Type** [DecisionTableParameter[]](#DecisionTableParameter) **Description** Parameters that you specify in a decision table. |
| decisionTable​SourceCriterias | **Field Type** [DecisionTableSourceCriteria[]](#DecisionTableSourceCriteria) **Description** The fields and values from a data source that are used to define the condition logic of the data that's used in a decision table. |
| description | **Field Type** string **Description** Description of the decision table. |
| doesConsider​NullValue | **Field Type** boolean **Description** Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is false. |
| downloadStatus | **Field Type** DecisionTableDownloadStatus (enumeration of type string) **Description** Specifies the progress status of a CSV download from a CSV-based lookup table. Available in API version 64.0 and later.Valid values are: `Completed` `DownloadInProgress` `Failed` |
| executionType | **Field Type** DecisionTableExecutionType (enumeration of type string) **Description** Indicates the backing storage for the Decision Table. Valid values are: `DLO`—Available in API version 67.0 and later. Replaces `DMO`. `HBASE` `HBPO` `SOLR` `SOQL` |
| filterResultBy | **Field Type** DecisionTableHitPolicy (enumeration of type string) **Description** Specifies how the results of a decision table are filtered if a set of inputs returns multiple matching outputs.Valid values are: `AnyValue` `CollectOperator` `FirstMatch` `OutputOrder` `Priority` `RuleOrder` `UniqueValues` |
| hasIncremental​SyncFailed | **Field Type** boolean **Description** Indicates if the last incremental refresh failed. |
| isIncremental​SyncEnabled | **Field Type** boolean **Description** Indicates if incremental refresh is enabled for the Decision Table. |
| isVersioned | **Field Type** boolean **Description** Indicates whether the CSV based decision table supports multiple file-import versions (`true`) or not (`false`). When set to `true`, the decisionTableFileImportVersions collection captures each version. The default value is `true`. Available in API version 67.0 and later. |
| lastIncremental​SyncDate | **Field Type** string **Description** The date and time on which the last incremental refresh occured for the decision table. |
| lastSyncDate | **Field Type** string **Description** Latest date on which the decision table was refreshed. |
| refresh​FailureReason | **Field Type** string **Description** Reason why the refresh of the decision table data failed. |
| refreshStatus | **Field Type** DecisionTableRefreshStatus (enumeration of type string) **Description** Specifies the refresh status of the cached data in the decision table.Valid values are: `Completed` `CompletedWithWarnings`—Available in API version 67.0 and later. `Failed` `InProgress` `Initiated` |
| setupName | **Field Type** string **Description** Required. Name of the decision table, which appears in Salesforce Setup. |
| sourceCondition​Logic | **Field Type** string **Description** The condition logic that's used to define the decision table from the source data. |
| sourceObject | **Field Type** string **Description** Required. Object that contains the rules based on which the decision table must provide outcomes. |
| status | **Field Type** DecisionTableStatus (enumeration of type string) **Description** Required. Status of the decision table. Valid values are: `ActivationInProgress` `Active` `Draft` `Inactive` |
| type | **Field Type** DecisionTableType (enumeration of type string) **Description** Stores the type of decision table.Valid values are: `Advanced` `HighScaleExecution` `HighVolume` `LowVolume` `MediumVolume` `RealTime` |
| uploadStatus | **Field Type** DecisionTableUploadStatus (enumeration of type string) **Description** Specifies the progress status of the CSV upload for a CSV based Lookup table.Valid values are: `Completed` `CompletedWithErrors` `Failed` `UploadInProgress` |
| usageType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** Type of industry or the application within the industry that's using a decision table.Valid values are: `Bre` `ComplianceControl` `DecompositionEnrichmentMapping` `DefaultPricing` `DefaultRating` `EventOrchestration` `FinancialServicesCloud` `FulfillmentCondition` `GpaCalculation` `InsuranceClaimProcessing`—Available in API version 65.0 and later. `ItServiceManagement`—Available in API version 65.0 and later. `PlanCostCalculation` `PriceProtection` `PricingDiscovery` `ProductCategoryQualification` `ProductQualification` `RatingDiscovery` `RecordAlert` `ShipAndDebit` `StudentInformationSystem`—Available in API version 65.0 and later. `StudentSuccess` `TestProcess` `WarrantyClaim` When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other usage types are available to you depending on your industry solution and permission sets. |

    

    

## DecisionTableFileImportVersion

      
      

Represents a version of a CSV file-import for a CSV-based decision table. Each version
        captures a separate import iteration with its own activation window, rank, and refresh
        status. Available in API version 67.0 and later.

      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

            

            
              

              

: 

: 

            

            
              

              

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

- 
- 
- 

            

          

        
| Field Name | Description |
| --- | --- |
| endDate | **Field Type** string **Description** The date and time when the decision table version becomes inactive. |
| lastIncremental​SyncDate | **Field Type** string **Description** The date and time on which the last incremental refresh occured for the decision table version. |
| lastSyncDate | **Field Type** string **Description** The date and time on which the last refresh occured for the decision table version. |
| rank | **Field Type** int **Description** Required. The current rank of the decision table version that’s used to determine when it can get chosen for processing. |
| refresh​FailedReason | **Field Type** string **Description** The reason the most recent refresh of the decision table version data failed. |
| refreshStatus | **Field Type** DecisionTable​RefreshStatus (enumeration of type string) **Description** Specifies the refresh status of the cached data in the decision table version.Valid values are: `Completed` `CompletedWithWarnings` `Failed` `InProgress` `Initiated` |
| startDate | **Field Type** string **Description** Required. The date and time when the decision table version becomes active. |
| uploadStatus | **Field Type** DecisionTable​UploadStatus (enumeration of type string) **Description** Specifies the progress status of the CSV upload for the decision table version.Valid values are: `Completed` `CompletedWithErrors` `Failed` `UploadInProgress` |
| versionName | **Field Type** string **Description** Required. The name of the decision table version. The maximum length is 120 characters. |
| versionNumber | **Field Type** int **Description** Required. The decision table version number. The combination of decisionTable and versionNumber must be unique. |
| versionStatus | **Field Type** DecisionTableStatus (enumeration of type string) **Description** Required. The status of the decision table version.Valid values are: `ActivationInProgress` `Active` `Inactive` |

    

    

## DecisionTableParameter

      
      

Represents an input or output field of a decision table.

      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

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

- 
- 
- 
- 
- 

            

            
              

              

: 

: 

- 
- 
- 

            

          

        
| Field Name | Description |
| --- | --- |
| dataType | **Field Type** DTParameterDataType (enumeration of type string) **Description** The data type of the field used in a decision table.Valid values are: `Boolean` `Currency` `Date` `DateTime` `Number` `Percent` `String` |
| decimalScale | **Field Type** int **Description** The number of digits to the right of the decimal point. |
| domainObject | **Field Type** string **Description** For polymorhpic fields, indicates the domain object in the field hierarchy. |
| fieldName | **Field Type** string **Description** Required. API name of the fields that selected as an input or output for the decision table. |
| fieldPath | **Field Type** string **Description** The path of the field used in a decision table in relation to the object that the field belongs to. |
| isGroup​ByField | **Field Type** boolean **Description** Indicates whether an input field is used to group the business rules of the decision table. |
| isPriority​Field | **Field Type** boolean **Description** Indicates whether a field is given priority. |
| isRequired | **Field Type** boolean **Description** Indicates whether a field is required to be used for lookups. |
| length | **Field Type** int **Description** The maximum number of characters supported for a field that's used in a decision table. |
| operator | **Field Type** DecisionTableOperator (enumeration of type string) **Description** Operator used for the input field.Valid values are: `Contains` `DoesNotExistIn` `DoesNotMatch` `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `IsNotNull` `IsNull` `LessOrEqual` `LessThan` `Matches` `NotEquals` |
| sequence | **Field Type** int **Description** The sequence in which input fields are processed. This field is available in API version 52.0 and later. |
| sortType | **Field Type** DecisionTableSortType (enumeration of type string) **Description** Sort outputs of a decision table based on the values of the input or output parameter field. This field is available in API version 56.0 and later.Valid values are: `AscNullFirst` `AscNullLast` `DescNullFirst` `DescNullLast` `None` |
| usage | **Field Type** DecisionTableParameterType (enumeration of type string) **Description** Required. Usage type of a field. Valid values are: `INPUT` `OUTPUT` `ROWCRITERIA` |

    

    

## DecisionTableSourceCriteria

      
      

Represents the fields and values from a data source that are used to define the condition
        logic of the data that's used in a decision table.

      

          
          
          
            
              

              

            

          

          
            
              

              

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

            

          

        
| Field Name | Description |
| --- | --- |
| operator | **Field Type** DTSourceCriteriaOperator (enumeration of type string) **Description** Required. The operator that’s applied to an associated decision table’s field to filter the data. Valid values are: `Contains` `DoesNotExistIn` `DoesNotMatch` `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `IsNotNull` `IsNull` `LessOrEqual` `LessThan` `Matches` `NotEquals` |
| sequenceNumber | **Field Type** int **Description** Required. The sequence number used in the associated decision table's source condition logic. |
| sourceField​Name | **Field Type** string **Description** Required. The name of the field that's used in the decision table. |
| value | **Field Type** string **Description** The value that’s expected in the source field used in the decision table. |
| valueType | **Field Type** DTSourceCriteriaValueType (enumeration of type string) **Description** Required. The type of the value that’s used to filter the source data. Valid values are: `Formula` `Literal` `Lookup` `Parameter` `Picklist` |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of a DecisionTable component.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<DecisionTable xmlns="http://soap.sforce.com/2006/04/metadata">
    <collectOperator>None</collectOperator>
    <conditionCriteria>1 and 2 and 3 and 4</conditionCriteria>
    <conditionType>All</conditionType>
    <dataSourceType>SingleSobject</dataSourceType>
    <decisionTableParameters>
        <fieldName>IsDeleted</fieldName>
        <operator>Equals</operator>
        <usage>INPUT</usage>
        <sequence>1</sequence>
        <isGroupByField>true</isGroupByField>
        <sortType>AscNullFirst</sortType>
        <dataType>Number</dataType>
        <fieldPath>AccountFeed.CommentsCount</fieldPath>
        <domainObject>AccountFeed</domainObject>
        <isPriorityField>false</isPriorityField>
        <decimalScale>2</decimalScale>
        <length>14</length>
        <isRequired>false</isRequired>
    </decisionTableParameters>
    <decisionTableParameters>
        <fieldName>IsActive</fieldName>
        <usage>OUTPUT</usage>
    </decisionTableParameters>
    <decisionTableParameters>
        <fieldName>LimitNumber</fieldName>
        <operator>Equals</operator>
        <usage>INPUT</usage>
        <sequence>2</sequence>
        <isGroupByField>false</isGroupByField>
    </decisionTableParameters>
    <decisionTableParameters>
        <fieldName>LimitStartDate</fieldName>
        <usage>OUTPUT</usage>
    </decisionTableParameters>
    <decisionTableParameters>
        <fieldName>GivenBadgeCount</fieldName>
        <operator>Equals</operator>
        <usage>INPUT</usage>
        <sequence>3</sequence>
        <isGroupByField>false</isGroupByField>
    </decisionTableParameters>
    <decisionTableParameters>
        <fieldName>Name</fieldName>
        <operator>Equals</operator>
        <usage>INPUT</usage>
        <sequence>4</sequence>
        <isGroupByField>false</isGroupByField>
    </decisionTableParameters>
    <decisionTableSourceCriterias>
        <sourceFieldName>IsDeleted</sourceFieldName>
        <operator>Equals</operator>
        <value>false</value>
        <sequenceNumber>1</sequenceNumber>
        <valueType>Literal</valueType>
    </decisionTableSourceCriterias>
    <description>Sample DT created for md-common tests</description>
    <filterResultBy>UniqueValues</filterResultBy>
    <setupName>Sample DT</setupName>
    <sourceObject>WorkBadgeDefinition</sourceObject>
    <sourceConditionLogic>1</sourceConditionLogic>
    <status>Draft</status>
    <type>LowVolume</type>
    <usageType>Bre</usageType>
    <doesConsiderNullValue>false</doesConsiderNullValue>
    <refreshStatus>Failed</refreshStatus>
    <refreshFailureReason>Failed due to limit violation.</refreshFailureReason>
    <executionType>Hbpo</executionType>
    <lastIncrementalSyncDate>""</lastIncrementalSyncDate>
    <uploadStatus>Completed</uploadStatus>
    <isIncrementalSyncEnabled>false</isIncrementalSyncEnabled>
    <hasIncrementalSyncFailed>false</hasIncrementalSyncFailed>
</DecisionTable>
```

      

The following is an example `package.xml` that
        references the previous definition.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
   <fullName>Sample DT Package</fullName>
   <description>Package created for md-common tests</description>
   <types>
      <members>Sample_DT</members>
      <name>DecisionTable</name>
   </types>
   <types>
      <members>DSL_Sample</members>
      <members>Sample_DT_Default</members>
      <name>DecisionTableDatasetLink</name>
   </types>
   <version></version>
</Package>
```

=== ARTICLE: meta_decisiontabledatasetlink.htm ===
---
page_id: meta_decisiontabledatasetlink.htm
title: DecisionTableDatasetLink
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_decisiontabledatasetlink.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_table_metadata_api.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTableDatasetLink

Represents the information about a dataset link
      associated with a decision table. In a dataset link, select an object for whose records, the
      decision table must provide an outcome. This type extends the
      Metadata metadata type and inherits its fullName field.

    
      

#### Note

Dataset links are supported only for Standard decision
        tables.

    

    

## File Suffix and Directory Location

      
      
      

DecisionTableDatasetLink components have the suffix
          .decisionTableDatasetLink and are stored in the
          decisionTableDatasetLinks folder.

    

    

## Version

      
      

DecisionTableDatasetLink components are available in API version 51.0 and later.

    

    

## Special Access Rules

      
      

To use this metadata type, your Salesforce org must have the Loyalty Management or the
        Rebate Management license.

    

    

## Fields

      
      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| decisionTableName | string | Required. The name of the associated decision table. |
| decisionTblDatasetParameters | [DecisionTblDatasetParameters](#dtparametersID) | Mapping between a decision table parameter and a field of the object selected in the dataset link. |
| description | string | The description of the dataset link. |
| isDefault | boolean | Indicates whether a dataset link is the default dataset link for a decision table. |
| setupName | string | Required. The name of the decision table dataset link, which appears in Setup. |
| sourceObject | string | Required. The name of the object being evaluated. |

    

    

## DecisionTblDatasetParameters

      
    

    
      

Represents the mapping between a decision table parameter and a field of
          the object selected in the dataset link.

      

The mapping allows the decision table to know which object fields must be compared to the
        input-output fields of the decision table.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| datasetFieldName | string | Required. Name of the dataset field whose value must be compared against an Input type decision table parameter when providing the outcome. |
| fieldName | string | Required. The API name of the decision table field that is selected as an input or output for the decision table dataset link. |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of a DecisionTableDatasetLink component.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">
   <decisionTableName>Sample_DT</decisionTableName>
   <decisionTblDatasetParameters>
      <fieldName>IsDeleted</fieldName>
      <datasetFieldName>IsDeleted</datasetFieldName>
   </decisionTblDatasetParameters>
   <decisionTblDatasetParameters>
      <fieldName>LimitNumber</fieldName>
      <datasetFieldName>CallDurationInSeconds</datasetFieldName>
   </decisionTblDatasetParameters>
   <decisionTblDatasetParameters>
      <fieldName>Name</fieldName>
      <datasetFieldName>Subject</datasetFieldName>
   </decisionTblDatasetParameters>
   <description>DSL created for md-common tests</description>
   <isDefault>false</isDefault>
   <sourceObject>Task</sourceObject>
   <setupName>DSL Sample</setupName>
</DecisionTableDatasetLink>
```

      

The following is an example of a default DecisionTableDatasetLink component.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">
   <decisionTableName>Sample_DT</decisionTableName>
   <isDefault>true</isDefault>
   <sourceObject>WorkBadgeDefinition</sourceObject>
   <setupName>Default DSL Sample</setupName>
</DecisionTableDatasetLink>
```

      

The following is an example `package.xml` that
        references the previous definition.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
   <fullName>Sample DT Package</fullName>
   <description>Package created for md-common tests</description>
   <types>
      <members>Sample_DT</members>
      <name>DecisionTable</name>
   </types>
   <types>
      <members>DSL_Sample</members>
      <members>Sample_DT_Default</members>
      <name>DecisionTableDatasetLink</name>
   </types>
   <version>51.0</version>
</Package>
```

=== ARTICLE: meta_explainabilitymsgtemplate.htm ===
---
page_id: meta_explainabilitymsgtemplate.htm
title: ExplainabilityMsgTemplate
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_explainabilitymsgtemplate.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityMsgTemplate

Represents information about the template
			that contains the decision explanation message for a specified expression set step
			type.

		
		

## Parent Type

			 This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ExplainabilityMsgTemplate components have the suffix
					.explainabilityMsgTemplate and are stored in the
					ExplainabilityMsgTemplates folder.

		

		

## Version

			
			

ExplainabilityMsgTemplate components are available in API version 56.0 and later.

		

		
		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

						

						
							

							

: 

: 

- 
- 
- 

						

						
							

							

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
|  |  |
| evaluationResult | **Field Type** EvaluationResult (enumeration of type string) **Description** Required. The type of result for which the message template can be used. The step type for which the result is evaluated can be a condition, conditional group, or branch.Valid values are: `Failed` `Passed` `NoResult` |
| expressionSetStepType | **Field Type** ExpressionSetStepType (enumeration of type string) **Description** Required. The step type in an expression set that uses the explainability message template.Valid values are: `Aggregation` `Branch` `BusinessElement` `Calculation` `Condition` `DecisionTableLookup` `ListEnabledGroup` `ListFilter` `MatrixLookup` `ReferenceProcedure` |
| expsSetProcessType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** Required. The type of industry that’s using the expression set.Valid values are: `Bre` `GpaCalculation` `InsuranceClaimProcessing`—Available in API version 65.0 and later. `ItServiceManagement`—Available in API version 65.0 and later. `PlanCostCalculation` `RatingDiscovery` `StudentInformationSystem`—Available in API version 65.0 and later. `StudentSuccess` When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other process types are available to you depending on your industry solution and permission sets. |
| isDefault | **Field Type** boolean **Description** Indicates whether the decision explainer template for a specified step type is default (true) or not (false). |
| masterLabel | **Field Type** string **Description** Required. Master label the for ExplainabilityMsgTemplate. |
| message | **Field Type** string **Description** Required. The message associated with the template for a specific expression set step type. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExplainabilityMsgTemplate component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ExplainabilityMsgTemplate
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<evaluationResult>Passed</evaluationResult>
	<expressionSetStepType>Condition</expressionSetStepType>
	<expsSetProcessType>ProductQualification</expsSetProcessType>
	<isDefault>false</isDefault>
	<masterLabel>ML EMT testDM</masterLabel>
	<message>EMT Testing</message>
</ExplainabilityMsgTemplate>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ExplainabilityMsgTemplate</name>
	</types>
	<version>67.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based.htm).

=== ARTICLE: meta_expressionsetdefinition.htm ===
---
page_id: meta_expressionsetdefinition.htm
title: ExpressionSetDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_expressionsetdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetDefinition

Represents an expression set definition.
	

		
			

#### Note

Before deploying an expression set or an expression set version to a target org, review
				these [Expression Set Migration Considerations](https://help.salesforce.com/s/articleView?id=ind.considerations_for_migrating_expression_sets.htm&type=5&language=en_US).

		

		

## Parent Type

 This type extends the Metadata metadata type and inherits its
				fullName field.

		

## File Suffix and Directory Location

			
			

ExpressionSetDefinition components have the suffix
					.expressionSetDefinition and are stored in the
					expressionSetDefinition folder.

		

		

## Version

			
			

ExpressionSetDefinition components are available in API version 55.0 and later.

		

		
		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

						

						
							

							

: 

: 

						

						
							

							

: 

: 

- 
- 

						

						
							

							

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

- 
- 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
|  |  |
| description | **Field Type** string **Description** The description of an expression set definition. |
| executionMode | **Field Type** ExpsSetExecutionMode (enumeration of type string) **Description** Specifies the execution mode for the expression set definition.Valid values are: `Cloud` `Local` |
| executionScale | **Field Type** ExpsSetExecutionScale (enumeration of type string) **Description** Specifies the scale of the inputs that an expression set processes. The scale determines where the expression set is executed. Valid values are: `High` `Low` Available in API version 61.0 and later. |
| interfaceSource​Type | **Field Type** ExpsSetInterfaceSourceType (enumeration of type string) **Description** The interface source type designed by the consuming cloud that's making a customized expression set builder available to its users. Valid values are: `Bre` `Constraint` (Available in API version 62.0 and later). `DiscoveryProcedure` (Available in API version 61.0 and later). `EventOrchestration` (Available in API version 61.0 and later). `GpaCalculationProcedure` (Available in API version 67.0 and later). `IntelligentDecisionStudio` (Available in API version 67.0 and later). `ItServiceManagement` (Available in API version 65.0 and later). `PricingProcedure` `QualificationProcedure` `RatingDiscoveryProcedure` (Available in API version 61.0 and later). `RatingProcedure` (Available in API version 67.0 and later). `Sample` Available in API version 59.0 and later. |
| label | **Field Type** string **Description** Required. The UI label of an expression set definition. |
| processType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** The process type that uses the expression set rule. Valid values are: `AssetRefreshEligibility`—Available in API version 67.0 and later. `Bre` `GpaCalculation` `InsuranceClaimProcessing`—Available in API version 65.0 and later. `ItServiceManagement`—Available in API version 65.0 and later. `PlanCostCalculation` `Program`—Available in API version 67.0 and later. `RatingDiscovery` `StockRotation`—Available in API version 67.0 and later. `StudentInformationSystem`—Available in API version 65.0 and later. `StudentSuccess` When Business Rules Engine is enabled for a Salesforce instance, the default value is `Bre`. Other process types are available to you depending on your industry solution and permission sets. |
| resource​InitializationType | **Field Type** ResourceInitializationType (enumeration of type string) **Description** Indicates whether the initial value of expression set variables and context tags is null or a default value. Valid values are: `Default` `Off` Available in API version 64.0 and later. |
| template | **Field Type** boolean **Description** Defines whether an expression set is a template or not. |
| type | **Field Type** ExpsSetType (enumeration of type string) **Description** The type of the expression set definition.Valid values are: `Custom` `Standard` |
| usageSubType | **Field Type** ExpsSetUsageSubType (enumeration of type string) **Description** The subtype of the industry that's using the expression set definition. If no value is specified, the field defaults to null. |
| versions | **Field Type** [ExpressionSetDefinitionVersion](#ExpSetDefVer)[] **Description** Represents an array of expression set version definitions in an expression set.This array must contain at least one version. |

		

		

## ExpressionSetDefinitionVersion​​

			
			

Represents a definition of an expression set version.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

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

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

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

						

						
							

							

: 

: 

						

						
							

							

: 

: 

#### 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 

						

					

				
| Field Name | Description |
| --- | --- |
| decimalScale | **Field Type** integer **Description** Number of decimal places to be used in the results of calculation steps that involve context variables. |
| description | **Field Type** string **Description** Describes the version of an expression set definition. |
| endDate | **Field Type** dateTime **Description** The date until which the expression set definition is available for use. |
| expressionSet​Definition | **Field Type** string **Description** The full name of an expression set definition. |
| interface​SourceType | **Field Type** ExpsSetInterfaceSourceType (enumeration of type string) **Description** The interface source type designed by the consuming cloud that's making a customized expression set builder available to its users. Valid values are: `Bre` `Constraint` `DiscoveryProcedure` `EventOrchestration` `GpaCalculationProcedure` `IntelligentDecisionStudio` `ItServiceManagement` `PricingProcedure` `QualificationProcedure` `RatingDiscoveryProcedure` `RatingProcedure` `Sample` Available in API version 67.0 and later. |
| label | **Field Type** string **Description** Required. The UI label of an expression set definition. |
| processType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** The process type that uses the expression set rule. Available in API version 67.0 and later. |
| rank | **Field Type** int **Description** The rank of the Expression Set Definition Version. When more than one enabled version matches an expression set call, and the start date time to end date time spans overlap, the version with the highest rank is chosen. Available in API version 62.0 and later. |
| shouldShow​ExplExternally | **Field Type** boolean **Description** Indicates whether the decision explanation is exposed to external users (`true`) or not (`false`). The default value is `false`. Available in API version 56.0 and later. |
| startDate | **Field Type** dateTime **Description** Required. The date from when the expression set definition is available for use. |
| status | **Field Type** ExpsSetStatus (enumeration of type string) **Description** Required. The status of an expression set definition. Valid values are: `Active` `Draft` `Inactive` `InvalidDraft` `Obsolete` |
| steps | **Field Type** [ExpressionSetStep](#ExpSetStep)[] **Description** Represents an array of steps created in an expression set version. |
| uiTier | **Field Type** boolean **Description** Indicates whether the API call originated from the design time builder or a package. Note This field is for internal use only. |
| variables | **Field Type** [ExpressionSet​​Variable](#ExpSetVar)[] **Description** Represents an array of variables in an expression set version. |
| versionNumber | **Field Type** int **Description** Required. The version number of an expression set definition. |

		

		

## ExpressionSet​​Step

			
			

Represents a step in an expression set version.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

: 

						

						
							

							

: 

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

						

						
							

							

: 

: 

```

```

```

```

						

						
							

							

: 

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

						

					

				
| Field Name | Description |
| --- | --- |
| actionType | **Field Type** BusinessKnowledgeModel (enumeration of type string) **Description** Specifies the type of action this step executes.Valid values are: `AiAcceleratorSubscriberChurnPrediction` `ApexAction` `ApexListAction` (Available in API version 64.0 and later.) `AssetDiscovery` `AssignBadgeToMember` `AssignParameterValues` `AssignmentElement` `AssignmentRuleCustomQueue` (Available in API version 65.0 and later.) `AssignmentRuleCustomUser` (Available in API version 65.0 and later.) `AteprlRecordCreator` (Available in API version 65.0 and later.) `AttributeAdjustmentMatrix` `AttributeDiscount` `AutomatedClaimsProcessingValidation` `BaseRate` `BindingObjectRateAdjustmentResolution` (Available in API version 64.0 and later.) `BindingObjectRateCardEntryResolution` (Available in API version 64.0 and later.) `BreAggregator` `BreAggregatorAssignment` `BreakdownLineMapping` (Available in API version 64.0 and later.) `BundleDiscount` `CalculateQuantity` (Available in API version 64.0 and later.) `ChangeMemberTier` `CheckMemberBadgeAssignment` `CommercePricing` (Available in API version 62.0 and later.) `CommitmentAdjustment` (Available in API version 65.0 and later.) `ComplianceCheck` `ComplianceControlLog` (Available in API version 62.0 and later.) `Constraint` (Available in API version 64.0 and later.) `CreditPoints` `Crud` `DebitPoints` `DerivedPricing` `DiscountDistributionService` `DiscoverySettings` (Available in API version 64.0 and later.) `DynamicRulesExecutor` (Available in API version 65.0 and later.) `EvaluateCategoryDisqualification` (Available in API version 62.0 and later.) `EvaluateCategoryQualification` (Available in API version 62.0 and later.) `EvaluateDisqualification` `EvaluateQualification` `FormulaBasedPricing` `FormulaBasedRating` (Available in API version 62.0 and later.) `GetCustomerPromotionAttrValue` (Available in API version 64.0 and later.) `GetMemberAttributesValues` `GetMemberPartnerLinkageStatus` `GetMemberPointBalance` `GetMemberPromotions` `GetMemberTier` `GetOutputsFromDecisionMatrix` `GetOutputsFromDecisionTable` `GetUserData` `GroupingAndAggregatePricing` `GroupingAndAggregateRating` (Available in API version 62.0 and later.) `IncreaseUsageForCumulativePromotion` `IntegrationOrchestration` `InterNodeDataCopy` `IssueExtendedReward` (Available in API version 64.0 and later.) `IssueVoucher` `ListGroup` `ListGroupCalculation` `ListPrice` `ManualDiscount` `ManualRatingDiscount` (Available in API version 62.0 and later.) `MapProduct` `MinimumPrice` (Available in API version 62.0 and later.) `MultiRecipientProductQualification` (Available in API version 64.0 and later.) `NegotiatedBaseRate` (Available in API version 64.0 and later.) `NegotiatedRateCardEntryResolution` (Available in API version 64.0 and later.) `NegotiatedTierAdjustment` (Available in API version 64.0 and later.) `NegotiatedVolumeAdjustment` (Available in API version 64.0 and later.) `PredictiveAI` `PriceAdjustmentMatrix` `PriceGuidance` (Available in API version 64.0 and later.) `PriceRevision` (Available in API version 65.0 and later.) `PricingPropagation` (Available in API version 65.0 and later.) `PricingSettings` `PromotionExecution` (Available in API version 65.0 and later.) `PromotionsDiscount` `Proration` `RateAdjustmentByAttributeResolution` (Available in API version 62.0 and later.) `RateAdjustmentByTierResolution` (Available in API version 62.0 and later.) `RateAdjustmentMatrix` (Available in API version 62.0 and later.) `RateAssignment` (Available in API version 62.0 and later.) `RateCardEntryResolution` (Available in API version 62.0 and later.) `RateCardResolution` (Available in API version 62.0 and later.) `RatingAttributeDiscount` `RatingBreakdownLineMapping` (Available in API version 65.0 and later.) `RatingRoundingValues` (Available in API version 62.0 and later.) `RatingSetting` `RatingTierDiscount` `RatingVolumeDiscount` `RecordAction` `RecordAlert` `RedeemVoucher` `RoundingValues` `RuleFetch` `RunFlow` `RunProgramProcess` `SampleBusinessElementWithContext` `SampleCustomElementWithExpressionAndListFilter` `SampleDynamicCustomElement` `SampleJavaBasedTaxCalculatorCustomElement` `SampleTaxCalculatorCustomElement` `SendMail` `StopPricing` `StopRating` (Available in API version 62.0 and later.) `SubscriptionPricing` `TermGpaCalculation` (Available in API version 64.0 and later.) `TermGpaReporting` (Available in API version 64.0 and later.) `TestCustomElement` `UpdateCurrentValueForMemberAttribute` `UpdateCustomerPromotionAttrValue` (Available in API version 64.0 and later.) `UpdatePointBalance` `UpdateUsageForCumulativePromotion` `UpsertRecord` (Available in API version 64.0 and later.) `VolumeDiscount` `VolumeTierDiscount` |
| advancedCondition | **Field Type** [ExpressionSetAdvancedCondition](#ExpSetAdvCon) **Description** Represents an advanced condition step. |
| aggregation | **Field Type** [ExpressionSetAggregation](#ExpSetAggregate) **Description** Represents an aggregation step. |
| assignment | **Field Type** [ExpressionSetAssignment](#ExpSetAssignment) **Description** Represents an assignment step. |
| conditionExpression | **Field Type** [ExpressionSetConditionExpression](#ExpSetConExp) **Description** Represents a condition step. |
| customElement | **Field Type** [ExpressionSetCustomElement](#ExpSetCustomElement) **Description** Represents a custom element step that contains the input and output mappings. Available in API version 56.0 and later. |
| decisionTable | **Field Type** [ExpressionSetDecisionTable](#ExpSetDecisionTbl) **Description** Represents a decision matrix or decision table step. |
| description | **Field Type** string **Description** Describes an expression set definition version step. |
| failed​ExplainerTemplate | **Field Type** string **Description** The explainability message template that’s used when the result type of a condition step in an expression set is Failed. |
| failedMessage​TokenMappings | **Field Type** ExplainabilityMessageTemplateTokenMapping (enumeration of type string) **Description** List of the token resource mappings of the failed explainability message template. Valid values are: `expressionSetMessageToken` `resourceReference` Available in API version 59.0 and later. |
| hasNested​Explainability | **Field Type** boolean **Description** Indicates whether the step has nested explainability (true ) or not (false ). Available in API version 67.0 and later. |
| label | **Field Type** string **Description** Required. The UI label of an expression set definition version step. |
| name | **Field Type** string **Description** Required. The full name of an expression set definition version step. |
| noResult​ExplainerTemplate | **Field Type** string **Description** The explainability message template that’s used when the result type of a condition step in an expression set is No Result. Available in API version 59.0 and later. |
| noResultMessage​TokenMappings | **Field Type** ExplainabilityMessageTemplateTokenMapping (enumeration of type string) **Description** List of the token resource mappings of the no result explainability message template. Valid values are: `expressionSetMessageToken` `resourceReference` Available in API version 59.0 and later. |
| parentStep | **Field Type** string **Description** The name of the parent step in an expression set definition version that’s associated with a step. |
| passedExplainer​Template | **Field Type** string **Description** The explainability message template that’s used when the result type of a condition step in an expression set is Passed. |
| passedMessage​TokenMappings | **Field Type** ExplainabilityMessageTemplateTokenMapping (enumeration of type string) **Description** List of the token resource mappings of the passed explainability message template. Valid values are: `expressionSetMessageToken` `resourceReference` Available in API version 59.0 and later. |
| resultIncluded | **Field Type** boolean **Description** Indicates whether the step output must be included in the expression result (true) or not (false). |
| sequenceNumber | **Field Type** int **Description** Required. The sequence number of a step in an expression set definition version. |
| shouldExposExecPathMsgOnly | **Field Type** boolean **Description** Indicates whether the message in the explainability message template is exposed for only the branch path that was run. |
| shouldExposeConditionDetails | **Field Type** boolean **Description** Indicates whether the details of the condition are shown in the decision explanation. |
| shouldShowExplExternally | **Field Type** boolean **Description** Indicates whether the decision explanations are shown to external users. |
| stepType | **Field Type** ExpsSetStepType (enumeration of type string) **Description** Required. Specifies the type of step in an expression set definition version. Valid values are: `AdvancedCondition` `AdvancedListFilter` (Available in API version 67.0 and later). `Branch` `BusinessKnowledgeModel` `Condition` `DefaultPath` `ListFilter` (Available in API version 67.0 and later). `ListGroup` (Available in API version 67.0 and later). `SubExpression` |
| subExpression | **Field Type** [ExpressionSetSubExpression](#ExpSetSubExp) **Description** Represents a sub expression step. |

		

		

## ExpressionSetAdvancedCondition

			
			

Represents an advanced condition step.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 
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
| conditionLogic | **Field Type** string **Description** Required. The condition that’s defined for an advanced condition. |
| criteria | **Field Type** [ExpressionSetConditionCriteria](#ExpSetConCriteria) [] **Description** Represents an array of criteria defined in the advanced condition. |
| errorMessage | **Field Type** string **Description** An error message for a failed advanced condition. |
| resultParameter | **Field Type** string **Description** An expression set definition version variable associated with the result of a step. |
| successMessage | **Field Type** string **Description** A success message for a successful advanced condition. |

		

		

## ExpressionSetConditionCriteria

			
			

Represents a criterion defined in an advanced condition.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

: 
: 
- 
- 
- 
- 
- 

						

					

				
| Field Name | Description |
| --- | --- |
| operator | **Field Type** ExpsSetConditionOperator (enumeration of type string) **Description** Required. Specifies the operator for evaluating an expression. Valid values are: `Contains` `DoesNotContain` `Equals` `GreaterThan` `GreaterThanOrEquals` `IsNull` `IsNotNull` `LessThan` `LessThanOrEquals` `NoEquals` |
| sequenceNumber | **Field Type** int **Description** Required. The position of the condition in a step that contains multiple conditions. |
| sourceFieldName | **Field Type** string **Description** Required. The expression set definition version variable associated with the result of a condition criterion. |
| value | **Field Type** string **Description** Specifies the condition of a criterion. |
| valueType | **Field Type** ExpsSetValueType (enumeration of type string) **Description** Specifies the type of value. Valid values are: `Formula` `Literal` `Lookup` `Parameter` `Picklist` |

		

		

## ExpressionSetAggregation

			
			

Represents an aggregation step.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Field Name | Description |
| --- | --- |
| aggregatedParameter | **Field Type** string **Description** Required. The expression set definition version variable associated with the result of a condition criterion. |
| aggregateFunction | **Field Type** ExpsSetAggregationFunction (enumeration of type string) **Description** Required. Specifies the aggregation function used in a step. Valid values are: `Avg` `Max` `Min` `Sum` |
| expression | **Field Type** string **Description** Required. Specifies the expression of an aggregation. |

		

		

## ExpressionSetAssignment

			
			

Represents an assignment step.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

					

				
| Field Name | Description |
| --- | --- |
| aggregatedParameter | **Field Type** string **Description** Required. The expression set definition version variable associated with a step detail. |
| expression | **Field Type** string **Description** Required. The expression that’s defined for a step. |

		

		

## ExpressionSetConditionExpression

			
			

Represents a condition in a condition step.

			

					
					
					
						
							

							

						

					

					
						
							

							

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
| errorMessage | **Field Type** string **Description** An error message for a failed condition. |
| expression | **Field Type** string **Description** Required. The expression that’s defined for a step. |
| resultParameter | **Field Type** string **Description** The expression set definition version variable associated with the result of a step. |
| successMessage | **Field Type** string **Description** A success message for a successful condition. |

		

		

## ExpressionSetCustomElement

			
			

Represents a custom element in an expression set. Available in API version 56.0 and
				later.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| parameters | **Field Type** [ExpressionSetElementParameter](#ExpressionSetElementParameter)[] **Description** Represents the list of parameters in the custom element. |

		

		

## ExpressionSetElementParameter

			
			

Represents a parameter within a custom element of an expression set. Available in API
				version 56.0 and later.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

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

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| input | **Field Type** boolean **Description** Required. Indicates whether the custom element parameter is input (`true`) or not (`false`). The default value is `true`. |
| name | **Field Type** string **Description** Required. The name of the custom element parameter. |
| output | **Field Type** boolean **Description** Required. Indicates whether the custom element parameter is output (`true`) or not (`false`). The default value is `true`. |
| type | **Field Type** ExpsSetValueType (enumeration of type string) **Description** The type of custom element parameter.Values are: `Formula` `Literal` `Lookup` `Parameter` `PickList` The default value is `Parameter`. |
| value | **Field Type** string **Description** Required. The name of the expression set variable. |

		

		

## ExpressionSetDecisionTable

			
			

Represents a decision table or decision matrix in a step.

			

					
					
					
						
							

							

						

					

					
						
							

							

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
| decisionTableName | **Field Type** string **Description** Required. The decision matrix or decision table name used in a step. |
| mappings | **Field Type** [ExpressionSetElementParameter[]](#ExpressionSetElementParameter) **Description** The mapping information between various parameters in an ExpressionSetDecisionTable. Available in API version 59.0 and later. |
| type | **Field Type** string **Description** Required. The type in a step. It can be a decision table or decision matrix. |

		

		

## ExpressionSetSubExpression

			
			

Represents a sub expression in a step.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

					

				
| Field Name | Description |
| --- | --- |
| expressionSet | **Field Type** string **Description** Required. The sub expression name used in a step. |
| mappings | **Field Type** [ExpressionSetElementParameter[]](#ExpressionSetElementParameter) **Description** The mapping information between various parameters in an ExpressionSetDecisionTable. Available in API version 61.0 and later. |

		

		

## ExpressionSet​​Variable

			
			

Represents a definition of an expression set variable.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

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
- 
- 
- 
- 
- 

						

						
							

							

: 

: 
: 

#### 

						

					

				
| Field Name | Description |
| --- | --- |
| collection | **Field Type** boolean **Description** Indicates whether a variable stores a collection of values (`true`) or not (`false`). |
| dataType | **Field Type** ExpsSetDataType (enumeration of type string) **Description** Required. The data type of an expression set variable. Valid values are: `ActionOutput` `Boolean` `Currency` `Date` `DateTime` `DecisionMatrix` `DecisionTable` `Numeric` `Percent` `Sobject` `SubExpression` `Text` |
| decimalPlaces | **Field Type** int **Description** The decimal digits in the currency, number, or percent data type for an expression set variable. |
| description | **Field Type** string **Description** The description of the variable used in an expression set. |
| fields | **Field Type** [ExpressionSetVariableField](#ExpSetVarFld) [] **Description** Represents an array of fields in an object that's used as a variable in an expression set. |
| input | **Field Type** boolean **Description** Indicates whether an expression set variable is used as an input (`true`) in an expression or not (`false`). |
| lookupName | **Field Type** string **Description** The API name of a decision matrix, a decision table, or a sub expression. |
| lookupType | **Field Type** ExpsSetVariableLookupType (enumeration of type string) **Description** The type of the lookup used in an expression set definition. Valid values are: `DecisionMatrix` `DecisionTable` `SubExpression` |
| name | **Field Type** string **Description** Required. The full name of the variable used in an expression set definition. |
| objectName | **Field Type** string **Description** The name of the sObject. |
| output | **Field Type** boolean **Description** Indicates whether an expression set variable is used as an output in an expression(`true`) or not (`false`). |
| resultStep | **Field Type** string **Description** The step that produces the expression set variable. |
| type | **Field Type** ExpsSetVariableType (enumeration of type string) **Description** Required. The type of variable in an expression set definition. Valid values are: `Constant` `ContextDynamicAttributeTag` (Available in API version 62.0 and later.) `ExecutableContextDefinitionTag` (Available in API version 62.0 and later.) `Formula` `Variable` |
| value | **Field Type** string **Description** Represents a constant value or a formula. Note It stores the default value of a variable. |

		

		

## ExpressionSetVariableField

			
			

Represents a definition of a field in an object that's used as a variable in an expression
				set.

			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

						
							

							

: 

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

						

					

				
| Field Name | Description |
| --- | --- |
| dataType | **Field Type** ExpsSetDataType (enumeration of type string) **Description** Required. Specifies the type of data stored in an expression set variable. Valid values are: `ActionOutput` `Boolean` `Currency` `Date` `DateTime` `DecisionMatrix` `DecisionTable` `Numeric` `Percent` `Sobject` `SubExpression` `Text` |
| decimalPlaces | **Field Type** int **Description** The decimal digits in the currency, number, or percent data type for an expression set variable. |
| fields | **Field Type** [ExpressionSetVariableField](#ExpSetVarFld) [] **Description** Represents an array of fields in an object that's used as a variable in an expression set. |
| lookupName | **Field Type** string **Description** The API name of a decision matrix, a decision table, or a sub expression. |
| lookupType | **Field Type** ExpsSetVariableLookupType (enumeration of type string) **Description** Required. The type of lookup used in an expression set definition. Valid values are: `DecisionMatrix` `DecisionTable` `SubExpression` |
| name | **Field Type** string **Description** Required. The full name of the field used in an expression set variable. |
| objectName | **Field Type** string **Description** The name of the sObject. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExpressionSetDefinition component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ExpressionSetDefinition xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>ExpSetWithAllSteps</label>
    <processType>Bre</processType>
    <template>false</template>
    <description></description>
    <interfaceSourceType>Sample</interfaceSourceType>
    <executionScale>Low</executionScale>
    <versions>
        <fullName>ExpSetWithAllSteps_V1</fullName>
        <expressionSetDefinition>ExpSetWithAllSteps</expressionSetDefinition>
        <label>ExpSetWithAllSteps V1</label>
        <shouldShowExplExternally>false</shouldShowExplExternally>
        <startDate>2022-08-09T22:04:56.000Z</startDate>
        <endDate>2023-08-09T22:04:56.000Z</endDate>
        <status>Draft</status>
        <uiTier>false</uiTier>
        <rank>1</rank>
        <description>ExpSetWithAllSteps_V1</description>
        <steps>
            <description>Aggregate</description>
            <actionType>BreAggregator</actionType>
            <aggregation>
                <aggergatedParameter>result</aggergatedParameter>
                <aggregateFunction>Avg</aggregateFunction>
                <expression>AVG ( result )</expression>
            </aggregation>
            <label>Aggregate</label>
            <name>Aggregate</name>
            <resultIncluded>true</resultIncluded>
            <sequenceNumber>5</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <label>Branch</label>
            <name>Branch</name>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>4</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>Branch</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>b</assignedParameter>
                <expression>SUM ( a , 10 )</expression>
            </assignment>
            <label>Calculation</label>
            <name>Calculation</name>
            <resultIncluded>true</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>result</assignedParameter>
                <expression>b * 100</expression>
            </assignment>
            <label>Calculation</label>
            <name>Calculation10</name>
            <parentStep>DefaultLane</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>result</assignedParameter>
                <expression>b * 1</expression>
            </assignment>
            <label>Calculation</label>
            <name>Calculation3</name>
            <parentStep>Condition</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>result</assignedParameter>
                <expression>SUM ( b , 10 )</expression>
            </assignment>
            <label>Calculation</label>
            <name>Calculation5</name>
            <parentStep>Condition4</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>result</assignedParameter>
                <expression>b * 10</expression>
            </assignment>
            <label>Calculation</label>
            <name>Calculation8</name>
            <parentStep>Condition7</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <steps>
            <conditionExpression>
                <successMessage>success</successMessage>
                <errorMessage>error</errorMessage>
                <expression>IS10 == b</expression>
                <resultParameter>condition_output__1</resultParameter>
            </conditionExpression>
            <label>Condition</label>
            <name>Condition</name>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>2</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>Condition</stepType>
        </steps>
        <steps>
            <advancedCondition>
                <successMessage>success</successMessage>
                <errorMessage>error</errorMessage>
                <conditionLogic>1</conditionLogic>
                <criteria>
                    <operator>Equals</operator>
                    <sequenceNumber>1</sequenceNumber>
                    <sourceFieldName>condition_output__1</sourceFieldName>
                    <value>true</value>
                    <valueType>Literal</valueType>
                </criteria>
                <resultParameter>condition_output__3</resultParameter>
            </advancedCondition>
            <label>Condition</label>
            <name>Condition4</name>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>3</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>AdvancedCondition</stepType>
        </steps>
        <steps>
            <conditionExpression>
                <expression>IS10 == b</expression>
                <resultParameter>condition_output__2</resultParameter>
            </conditionExpression>
            <label>Condition</label>
            <name>Condition7</name>
            <parentStep>Branch</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>Condition</stepType>
        </steps>
        <steps>
            <label>Default Lane</label>
            <name>DefaultLane</name>
            <parentStep>Branch</parentStep>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>2</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>false</shouldShowExplExternally>
            <stepType>DefaultPath</stepType>
        </steps>
        <steps>
            <actionType>AssignParameterValues</actionType>
            <assignment>
                <assignedParameter>a</assignedParameter>
                <expression>3</expression>
            </assignment>
            <failedExplainerTemplate>CalculationFailure</failedExplainerTemplate>
            <failedMessageTokenMappings>
                <expressionSetMessageToken>y2</expressionSetMessageToken>
                <resourceReference>a</resourceReference>
            </failedMessageTokenMappings>
            <label>CalculationStepWithTokensAndMappings</label>
            <name>CalculationStepWithTokensAndMappings</name>
            <passedExplainerTemplate>CalculationSuccess</passedExplainerTemplate>
            <passedMessageTokenMappings>
                <expressionSetMessageToken>y1</expressionSetMessageToken>
                <resourceReference>a</resourceReference>
            </passedMessageTokenMappings>
            <resultIncluded>false</resultIncluded>
            <sequenceNumber>1</sequenceNumber>
            <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>
            <shouldExposeConditionDetails>false</shouldExposeConditionDetails>
            <shouldShowExplExternally>true</shouldShowExplExternally>
            <stepType>BusinessKnowledgeModel</stepType>
        </steps>
        <variables>
            <collection>false</collection>
            <dataType>Boolean</dataType>
            <description>condition_output__3</description>
            <input>false</input>
            <name>condition_output__3</name>
            <output>false</output>
            <resultStep>Condition4</resultStep>
            <type>Variable</type>
            <value>False</value>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Numeric</dataType>
            <decimalPlaces>2</decimalPlaces>
            <description>a</description>
            <input>true</input>
            <name>a</name>
            <output>false</output>
            <type>Variable</type>
            <value>10</value>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Boolean</dataType>
            <description>condition_output__1</description>
            <input>false</input>
            <name>condition_output__1</name>
            <output>false</output>
            <resultStep>Condition</resultStep>
            <type>Variable</type>
            <value>False</value>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Boolean</dataType>
            <description>condition_output__2</description>
            <input>false</input>
            <name>condition_output__2</name>
            <output>false</output>
            <resultStep>Condition7</resultStep>
            <type>Variable</type>
            <value>False</value>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Numeric</dataType>
            <decimalPlaces>2</decimalPlaces>
            <description>IS10</description>
            <input>false</input>
            <name>IS10</name>
            <output>false</output>
            <type>Constant</type>
            <value>10</value>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Numeric</dataType>
            <decimalPlaces>2</decimalPlaces>
            <description>b</description>
            <input>false</input>
            <name>b</name>
            <output>true</output>
            <type>Variable</type>
        </variables>
        <variables>
            <collection>false</collection>
            <dataType>Numeric</dataType>
            <decimalPlaces>2</decimalPlaces>
            <description>result</description>
            <input>false</input>
            <name>result</name>
            <output>true</output>
            <type>Variable</type>
        </variables>
        <versionNumber>1</versionNumber>
    </versions>
</ExpressionSetDefinition>
```

			

The following is an example `package.xml` that references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ExpressionSetDefinition</name>
	</types>
	<version>67.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based.htm).

=== ARTICLE: meta_expressionsetmessagetoken.htm ===
---
page_id: meta_expressionsetmessagetoken.htm
title: ExpressionSetMessageToken
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_expressionsetmessagetoken.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetMessageToken

Represents an interface to retrieve, deploy,
			create, update, or delete information on Expression Set Message Token.

		
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

		

## Parent Type

			 This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ExpressionSetMessageToken components have the suffix
					expressionSetMessageToken and are stored in the
					ExpressionSetMessageToken folder.

		

		

## Version

			
			

ExpressionSetMessageToken components are available in API version 59.0 and later.

		

		

## Special Access Rules

			
			

InteractionCalculation.orgHasBREandDESAccess Org permission set license is required
				for users to access this metadata type.

		

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** Required. Description of the expression set message token. |
| developerName | **Field Type** string **Description** Required. Developer name of the expression set message token. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for ExpressionSetMessageToken, which is defined when the ExpressionSetMessageToken is created. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExpressionSetMessageToken component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ExpressionSetMessageToken xmlns="http://soap.sforce.com/2006/04/metadata">
    <developerName>token</developerName>
    <description>Description</description>
    <masterLabel>token</masterLabel>
</ExpressionSetMessageToken>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>ExpressionSetMessageToken</name>
    </types>
    <version>59.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving
					Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_expressionsetobjectalias.htm ===
---
page_id: meta_expressionsetobjectalias.htm
title: ExpressionSetObjectAlias
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_expressionsetobjectalias.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetObjectAlias

Represents information about the alias of the source
			object that’s used in an expression set.
	

		

## Parent Type

			 This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

ExpressionSetObjectAlias components have the suffix
					.expressionSetObjectAlias and are stored in the
					expressionSetObjectAlias folder.

		

		

## Version

			
			

ExpressionSetObjectAlias components are available in API version 56.0 and later.

		

		
		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

- 
- 
- 
- 
- 
- 
- 
- 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| dataType | **Field Type** ExpsSetObjectDataType (enumeration of type string) **Description** Required. The data type of the object alias.Values are: `JSON` `sObject` |
| mappings | **Field Type** [ExpressionSetObjectAliasField[]](#ExpressionSetObjectAliasField) **Description** The mapping between a source field and its corresponding field alias. |
| objectApiName | **Field Type** string **Description** Required. The API name of the top-level object, when the data type is sObject. The key of the top-level object, when the data type is JSON. |
| usageType | **Field Type** ExpsSetProcessType (enumeration of type string) **Description** Required. The type of application associated with the industry that's using an expression set. Your Salesforce org admin can define the values.Valid values are: `Bre` `GpaCalculation` `InsuranceClaimProcessing`—Available in API version 65.0 and later. `ItServiceManagement`—Available in API version 65.0 and later. `PlanCostCalculation` `RatingDiscovery` `StudentInformationSystem`—Available in API version 65.0 and later. `StudentSuccess` When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other usage types are available to you depending on your industry solution and permission sets. |

		

		

## ExpressionSetObjectAliasField

			
			
			

The fields associated with the source object for which the object
				alias is created.

			

					
					
					
						
							

							

						

					

					
						
						
						
							

							

: 

: 

: 

						

						
							

							

: 

: 

: 

						

					

				
| Field Name | Description |
| --- | --- |
| fieldAlias | **Field Type** string **Description** Required. The field alias associated with the source field name. |
| sourceFieldName | **Field Type** string **Description** Required. The name of the source field for which the field alias is created. The source field name under an object alias must be unique. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an ExpressionSetObjectAlias component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ExpressionSetObjectAlias xmlns="http://soap.sforce.com/2006/04/metadata">
    <dataType>sObject</dataType>
    <mappings>
        <fieldAlias>dum2</fieldAlias>
        <sourceFieldName>CreatedBy.Contact.Name</sourceFieldName>
    </mappings>
    <mappings>
        <fieldAlias>dum3</fieldAlias>
        <sourceFieldName>CreatedBy.Name</sourceFieldName>
    </mappings>
    <mappings>
        <fieldAlias>dum1</fieldAlias>
        <sourceFieldName>Owner.Contact.Name</sourceFieldName>
    </mappings>
    <objectApiName>Account</objectApiName>
    <usageType>Bre</usageType>
</ExpressionSetObjectAlias>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>ExpressionSetObjectAlias</name>
	</types>
	<version>67.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
					File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based.htm).

=== ARTICLE: sforce_api_objects_calcmatrixcolumnrange.htm ===
---
page_id: sforce_api_objects_calcmatrixcolumnrange.htm
title: CalcMatrixColumnRange
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_calcmatrixcolumnrange.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalcMatrixColumnRange

Represents information about a value in a decision matrix column when
         the column is of the type number range or text range. This object is available in API
      version 59.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| CalculationMatrixColumnId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the decision matrix column associated with the column range value. This field is a relationship field. **Relationship Name** CalculationMatrixColumn **Relationship Type** Lookup **Refers To** CalculationMatrixColumn |
| CalculationMatrixVersionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The decision matrix version ID asociated with the column range value. This field is a relationship field. **Relationship Name** CalculationMatrixVersion **Relationship Type** Lookup **Refers To** CalculationMatrixVersion |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the decision matrix column. |
| Occurrence | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The number of times a range value is used in a decision matrix version. |
| RangeStartValue | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The value that defines the start of a range. |

=== ARTICLE: sforce_api_objects_calculationmatrix.htm ===
---
page_id: sforce_api_objects_calculationmatrix.htm
title: CalculationMatrix
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_calculationmatrix.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationMatrix

Matches input values to a table row and returns the row's output
         values. The label for this object is Decision Matrix. This object is available in API
      version 53.0 and later.

      
         

 Decision Matrices are useful for implementing complex rules in a systematic, readable
            way. There are two types: Standard and Grouped. A Grouped Decision Matrix groups rows in
            different versions by one or two keys such as geographic region or product code.

      

      

## Supported Calls

      
      

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,` search(),`
            `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

Access to Decision Matrices requires Omnistudio
            licenses.

      

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

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 
: 
- 

                  

               

            
| Field | Details |
| --- | --- |
| DecisionMatrixDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The decision matrix definition record associated with this calculation matrix. This field is a polymorphic relationship field. **Relationship Name** DecisionMatrixDefinition **Relationship Type** Lookup **Refers To** DecisionMatrixDefinition, DecisionTable |
| DecisionMatrixType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of lookup table. Possible values are: `DecisionMatrix` `DecisionTable` The default value is `DecisionMatrix`. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** A text description of the Decision Matrix. |
| GroupKey | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A key for grouping matrix rows in different versions, such as geographic region or product code. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, it's possible the user only accessed this record or list view (LastReferencedDate) but didn't view it. |
| MigrationStatus | **Type** textarea **Properties** Nillable **Description** The status of migrating the data from the Calculation Matrix object to the Decision Matrix Definition object. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The Decision Matrix name. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who currently owns this matrix. Default value is the user logged in to the API to perform the create action. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| SubGroupKey | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A subkey for grouping matrix rows in different versions, such as geographic region or product code. For example, if the GroupKey is `Country`, the SubGroupKey can be `State` or `Province`. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The Decision Matrix type. A Standard Decision Matrix has no special features. A Grouped Decision Matrix groups rows by one or two keys (GroupKey and SubGroupKey) such as geographic region or product code. Possible values are: `Grouped` `Standard` |
| UniqueName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier of the record, which is sourced from the value in the Name field of CalculationMatrix (decision matrix). For example, if the name of the calculation matrix is sample matrix, its UniqueName would be sample_matrix. |
| UsageType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** A decision matrix’s usage type. Available in API version 59.0 and later. Possible value is: `Bre`-Default When Business Rules Engine is enabled on your Salesforce org, the default value is Bre. Other usage types may be available to you depending on your industry solution and permission sets. |

      

      

## Usage

        
        

Expression Sets, OmniScripts, and Integration Procedures can call Decision Matrices.

=== ARTICLE: sforce_api_objects_calculationmatrixcolumn.htm ===
---
page_id: sforce_api_objects_calculationmatrixcolumn.htm
title: CalculationMatrixColumn
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_calculationmatrixcolumn.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationMatrixColumn

      Defines a column in a Decision Matrix. The label for this object is Decision
         Matrix Column. This object is available in API version 53.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Access to Decision Matrices requires Omnistudio licenses.

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

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
| ApiName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the column. |
| CalculationMatrixId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the Decision Matrix to which this column belongs. This is a relationship field. **Relationship Name** CalculationMatrix **Relationship Type** Lookup **Refers To** CalculationMatrix |
| ColumnType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the column matches matrix input or is returned as output. Possible values are: `Input` `Output` |
| DataType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of data in the column. Possible values are: `Boolean` `Currency` `Number` `NumberRange` `Percent` `Text` `TextRange` |
| DisplaySequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The position of this column in the column order. |
| IsWildcardColumn | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Specifies that this column can contain a wildcard value such as `ALL`. The default value is `false`. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The column name. |
| RangeValues | **Type** textarea **Properties** Create, Nillable, Update **Description** A list of values that define range boundaries. |
| WildcardColumnValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value that indicates a wildcard, for example `ALL`. Applicable if IsWildcardColumn is `true`. |

=== ARTICLE: sforce_api_objects_calculationmatrixrow.htm ===
---
page_id: sforce_api_objects_calculationmatrixrow.htm
title: CalculationMatrixRow
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_calculationmatrixrow.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationMatrixRow

      Defines a row in a Decision Matrix. The label for this object is Decision
         Matrix Row. This object is available in API version 53.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`, 
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Access to Decision Matrices requires Omnistudio licenses.

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CalculationMatrixVersionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the Decision Matrix Version to which this row belongs. This is a relationship field. **Relationship Name** CalculationMatrixVersion **Relationship Type** Lookup **Refers To** CalculationMatrixVersion |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The last date on which this row version is active. Applicable if IsVersionEnabled is `true`. |
| InputData | **Type** textarea **Properties** Create, Nillable, Update **Description** The input columns and associated values for this row of the matrix. |
| IsVersionEnabled | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Specifies whether the associated matrix version is active. Derived from the associated Decision Matrix Version (CalculationMatrixVersion object). The default value is `false`. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The row name. |
| OutputData | **Type** textarea **Properties** Create, Nillable, Update **Description** The output columns and associated values for this row of the matrix. |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The first date on which this row version is active. Applicable if IsVersionEnabled is `true`. |

=== ARTICLE: sforce_api_objects_calculationmatrixversion.htm ===
---
page_id: sforce_api_objects_calculationmatrixversion.htm
title: CalculationMatrixVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_calculationmatrixversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculationMatrixVersion

Defines a version of a Decision Matrix. The label for this object is
         Decision Matrix Version. This object is available in API version 53.0 and
      later.

      

## Supported Calls

      
      

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

Access to Decision Matrices requires Omnistudio licenses.

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

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
| ApiName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the decision matrix version. This field is available in API version 56.0 and later. |
| CalculationMatrixId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the Decision Matrix to which this version belongs. This is a relationship field. **Relationship Name** CalculationMatrix **Relationship Type** Lookup **Refers To** CalculationMatrix |
| DecisionMatrixDefinitionVerId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The decision matrix definition version associated with this calculation matrix version. This field is a relationship field. **Relationship Name** DecisionMatrixDefinitionVer **Relationship Type** Lookup **Refers To** DecisionMatrixDefinitionVersion |
| DscnModelNoteExportStatus | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** Indicates the export status of a decision matrix version in the Decision Model and Notation (DMN) format. Possible values are: `Initiated` `InProgress` `Complete` `Failed` |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The last date on which this matrix version is active. |
| GroupKey | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** A key for grouping matrix rows in different versions, such as geographic region or product code. Derived from the associated Decision Matrix (CalculationMatrix object). |
| GroupKeyValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the GroupKey for this version. For example, if the GroupKey is `Country`, the GroupKeyValue can be `United States`. |
| IsEnabled | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Specifies whether this version is active. The default value is `false`. |
| LoadProcessStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of a data upload from a .csv file. Possible values are: `Completed` `CompletedWithErrors` `Failed` `InProgress` `Pending` |
| MatrixType | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The matrix type, either `Standard` or `Grouped`. A Grouped Decision Matrix groups rows in different Decision Matrix Versions by one or two keys such as geographic region or product code. Derived from the associated Decision Matrix (CalculationMatrix object). |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The matrix version name. |
| Rank | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** When the invocation time of a matrix call is between the StartDateTime and EndDateTime of more than one enabled matrix version, the version with the highest Rank is chosen. |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The first date on which this matrix version is active. |
| SubGroupKey | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** A subkey for grouping matrix rows in different versions, such as geographic region or product code. For example, if the GroupKey is `Country`, the SubGroupKey can be `State or Province`. Derived from the associated Decision Matrix (CalculationMatrix object). |
| SubGroupKeyValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the SubGroupKey for this version. For example, if the SubGroupKey is `State or Province`, the SubGroupKeyValue can be `California`. |
| VersionNumber | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The version number. |

=== ARTICLE: sforce_api_objects_explainabilitymsgtemplatelocalization.htm ===
---
page_id: sforce_api_objects_explainabilitymsgtemplatelocalization.htm
title: ExplainabilityMsgTemplateLocalization
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_explainabilitymsgtemplatelocalization.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityMsgTemplateLocalization

      Represents the translated value of the message in an explainability message
         template for an expression set step element. This object is available in API version
      56.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Users need the System Administrator permission set to access this object.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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

                  

            

            
| Field | Details |
| --- | --- |
| Language | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort **Description** The language of the translated explainability message template. Possible values are: `af`—Afrikaans `am`—Amharic `ar`—Arabic `ar_AE`—Arabic (United Arab Emirates) `ar_BH`—Arabic (Bahrain) `ar_DZ`—Arabic (Algeria) `ar_EG`—Arabic (Egypt) `ar_IQ`—Arabic (Iraq) `ar_JO`—Arabic (Jordan) `ar_KW`—Arabic (Kuwait) `ar_LB`—Arabic (Lebanon) `ar_LY`—Arabic (Libya) `ar_MA`—Arabic (Morocco) `ar_OM`—Arabic (Oman) `ar_QA`—Arabic (Qatar) `ar_SA`—Arabic (Saudi Arabia) `ar_SD`—Arabic (Sudan) `ar_SY`—Arabic (Syria) `ar_TN`—Arabic (Tunisia) `ar_YE`—Arabic (Yemen) `bg`—Bulgarian `bn`—Bengali `bs`—Bosnian `ca`—Catalan `cs`—Czech `cy`—Welsh `da`—Danish `de`—German `de_AT`—German (Austria) `de_BE`—German (Belgium) `de_CH`—German (Switzerland) `de_LU`—German (Luxembourg) `el`—Greek `el_CY`—Greek (Cyprus) `en_AE`—English (United Arab Emirates) `en_AU`—English (Australian) `en_BE`—English (Belgium) `en_CA`—English (Canadian) `en_CY`—English (Cyprus) `en_DE`—English (Germany) `en_GB`—English (UK) `en_HK`—English (Hong Kong) `en_IE`—English (Ireland) `en_IL`—English (Israel) `en_IN`—English (Indian) `en_MT`—English (Malta) `en_MY`—English (Malaysian) `en_NL`—English (Netherlands) `en_NZ`—English (New Zealand) `en_PH`—English (Phillipines) `en_SG`—English (Singapore) `en_US`—English `en_ZA`—English (South Africa) `eo`—Esperanto (Pseudo) `es`—Spanish `es_AR`—Spanish (Argentina) `es_BO`—Spanish (Bolivia) `es_CL`—Spanish (Chile) `es_CO`—Spanish (Colombia) `es_CR`—Spanish (Costa Rica) `es_DO`—Spanish (Dominican Republic) `es_EC`—Spanish (Ecuador) `es_GT`—Spanish (Guatemala) `es_HN`—Spanish (Honduras) `es_MX`—Spanish (Mexico) `es_NI`—Spanish (Nicaragua) `es_PA`—Spanish (Panama) `es_PE`—Spanish (Peru) `es_PR`—Spanish (Puerto Rico) `es_PY`—Spanish (Paraguay) `es_SV`—Spanish (El Salvador) `es_US`—Spanish (United States) `es_UY`—Spanish (Uruguay) `es_VE`—Spanish (Venezuela) `et`—Estonian `eu`—Basque `fa`—Farsi `fi`—Finnish `fr`—French `fr_BE`—French (Belgium) `fr_CA`—French (Canadian) `fr_CH`—French (Switzerland) `fr_LU`—French (Luxembourg) `fr_MA`—French (Morocco) `ga`—Irish `gu`—Gujarati `haw`—Hawaiian `hi`—Hindi `hmn`—Hmong `hr`—Croatian `ht`—Haitian Creole `hu`—Hungarian `hy`—Armenian `in`—Indonesian `is`—Icelandic `it`—Italian `it_CH`—Italian (Switzerland) `iw`—Hebrew `iw_EO`—Esperanto RTL (Pseudo) `ja`—Japanese `ji`—Yiddish `ka`—Georgian `kk`—Kazakh `kl`—Greenlandic `km`—Khmer `kn`—Kannada `ko`—Korean `lb`—Luxembourgish `lt`—Lithuanian `lv`—Latvian `mi`—Te reo `mk`—Macedonian `ml`—Malayalam `mr`—Marathi `ms`—Malay `mt`—Maltese `my`—Burmese `nl_BE`—Dutch (Belgium) `nl_NL`—Dutch `no`—Norwegian `pa`—Punjabi `pl`—Polish `pt_BR`—Portuguese (Brazil) `pt_PT`—Portuguese (European) `rm`—Romansh `ro`—Romanian `ro_MD`—Romanian (Moldova) `ru`—Russian `ru_AM`—Russian (Armenia) `ru_BY`—Russian (Belarus) `ru_KG`—Russian (Kyrgyzstan) `ru_KZ`—Russian (Kazakhstan) `ru_LT`—Russian (Lithuania) `ru_MD`—Russian (Moldova) `ru_PL`—Russian (Poland) `ru_UA`—Russian (Ukraine) `sh`—Serbian (Latin) `sh_ME`—Montenegrin `sk`—Slovak `sl`—Slovene `sm`—Samoan `sq`—Albanian `sr`—Serbian (Cyrillic) `sv`—Swedish `sw`—Swahili `ta`—Tamil `te`—Telugu `th`—Thai `tl`—Tagalog `tr`—Turkish `uk`—Ukrainian `ur`—Urdu `vi`—Vietnamese `xh`—Xhosa `zh_CN`—Chinese (Simplified) `zh_HK`—Chinese (Hong Kong) `zh_MY`—Chinese (Malaysia) `zh_SG`—Chinese (Singapore) `zh_TW`—Chinese (Traditional) `zu`—Zulu |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the namespacePrefix__componentName notation. This is a required field.The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The Id of the related explainability message template. This field is a relationship field. **Relationship Name** Parent **Relationship Type** Lookup **Refers To** ExplainabilityMsgTemplate |
| Value | **Type** textarea **Properties** Create, Filter, Sort, Update **Description** The translated label of the explainability message template. |

=== ARTICLE: sforce_api_objects_expressionset.htm ===
---
page_id: sforce_api_objects_expressionset.htm
title: ExpressionSet
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_expressionset.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSet

Represents information about an expression set. An expression set
         performs a series of calculations using lookups and user-defined variables and
         constants. This object is available in API version 55.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      
      

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
- 
- 

                  

                  
                     

                     

: 

: 

: 
: 
- 

: 

#### 

                  

               

            
| Field | Details |
| --- | --- |
| ApiName | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The API name of the expression set. This field is unique within your organization. This is a required field. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the expression set. |
| ExecutionScale | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the scale of the input that an expression set processes. The scale determines where the expression set is executed. Possible values are: `High` `Low` |
| ExpressionSetDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The expression set definition record associated with this expression set. This is a required field. This is a relationship field. **Relationship Name** ExpressionSetDefinition **Relationship Type** Lookup **Refers To** ExpressionSetDefinition |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, it's possible the user only accessed this record or list view (LastReferencedDate) but didn't view it. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the expression set. This is a required field. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who currently owns this expression set. Default value is the user logged in to the API to perform the create action This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| Type | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of the expression set. Possible values are: `Custom` `Standard` |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of industry that’s using the expression set. Possible values are: `Bre` Note When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other usage types may be available to you depending on your industry solution and permission sets. |

=== ARTICLE: sforce_api_objects_expressionsetdefinitioncontextdefinition.htm ===
---
page_id: sforce_api_objects_expressionsetdefinitioncontextdefinition.htm
title: ExpressionSetDefinitionContextDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_expressionsetdefinitioncontextdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetDefinitionContextDefinition

Represents a relationship between an expression set definition and a
         context definition. This object is available in API version 58.0 and
      later.

      

#### Note

You can’t add records to this object.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ContextDefinitionApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** API name of the context definition. |
| ContextDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the context definition. This field is a relationship field. **Relationship Name** ContextDefinition **Relationship Type** Lookup **Refers To** ContextDefinition |
| ExecutableContextDefinition | **Type** string **Properties** Create, Filter, Group, Nillable, Sort **Description** Developer name of the file-based context definition. |
| ExpressionSetApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** API name of the expression set. |
| ExpressionSetDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the expression set definition. This field is a relationship field. **Relationship Name** ExpressionSetDefinition **Relationship Type** Lookup **Refers To** ExpressionSetDefinition |

=== ARTICLE: sforce_api_objects_expressionsetversion.htm ===
---
page_id: sforce_api_objects_expressionsetversion.htm
title: ExpressionSetVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_expressionsetversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetVersion

Represents information about a specific version of an expression set.
         This object is also accessible through the UI API, which enables its use in components like
         Lightning Web Components (LWC). This object is available in API version 55.0 and
      later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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
| ApiName | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The API name of the expression set version. This is a required field and it requires a unique value. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the expression set version, |
| DecimalScale | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of decimal places to apply to non-local resources such as context tags. |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the expression set version becomes inactive. |
| ExpressionSetDefinitionVerId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The expression set definition version associated with this expression set version. This is a required field. This is a relationship field. **Relationship Name** ExpressionSetDefinitionVer **Relationship Type** Lookup **Refers To** ExpressionSetDefinitionVersion |
| ExpressionSetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the parent expression set record that’s associated with this expression set version. This is a required field. This is a relationship field. **Relationship Name** ExpressionSet **Relationship Type** Lookup **Refers To** ExpressionSet |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the expression set version is active (`true`) or not (`false`). This is a required field. The default value is `false`. |
| IsLoopingEnabled | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether looping is active for this expression set version (`true`) or not (`false`). The default value is `false`. |
| LatestSimulationResult | **Type** textarea **Properties** Create, Nillable, Update **Description** The result of the simulation service that processes the input variables defined for the expression set version, in JSON format. |
| LoopEndVariableName | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the resource that’s used to determine which resource can be processed last in the loop. |
| LoopIncrementVariableName | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the variable that’s used to determine which resource can be processed next in the loop. |
| LoopStartVariableName | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the variable that’s processed when the loop starts. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the expression set version. This is a required field. |
| Rank | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rank of the expression set version. An expression set version's rank is used to determine when the version is chosen for processing. When more than one enabled version matches an expression set call, and the start and end date time periods overlap, the version with the highest rank is chosen. |
| ShouldShowExplExternally | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the decision explanation is exposed to external users (true) or not (false). The default value for this field is `false`. This field is available in API version 56.0 and later. |
| StartDateTime | **Type** dateTime **Properties** Create, Defaulted on create, Filter, Nillable, Sort, Update **Description** The date and time when the expression set version becomes active. |
| VersionNumber | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The version number of this expression set. This is a required field. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later

         
            
               

**[ExpressionSetVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[ExpressionSetVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_expressionsetview.htm ===
---
page_id: sforce_api_objects_expressionsetview.htm
title: ExpressionSetView
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_expressionsetview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetView

Represents a virtual object that provides a consolidated view of
         file-based expression set. File-based expression sets are read-only templates. To be able
         to modify file-based expression sets, you must clone them first.  This object is
      available in API version 55.0 and later.

      

## Supported Calls

      
      

         `describeSObjects()`, 
         `query()`
      

      

      

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

- 
- 

                  

                  
                     

                     

: 

: 

: 

- 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The description of an expression set. |
| DurableId | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ID of the expression set. |
| ExpressionSetDetails | **Type** textarea **Properties** Nillable **Description** The details of the expression set in JSON format, which includes information such as name, version, created date, and elements contained in the expression set. |
| HasContextDefinitionRef | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the executable expression set template references an executable context definition (`true`) or not (`false`). The default value is False.Available in API version 60.0 and later. The default value is `false`. |
| IsExecutable | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the expression set template is executable (`true`) or not (`false`). Available in API version 60.0 and later. The default value is `false`. |
| IsTemplate | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the expression set is a template (`true`) or not (`false`). When installed from managed packages, expression sets can’t be viewed or cloned by subscribers because of intellectual property (IP) protection. But when those expression sets are templates, subscribers can open them in a builder, clone them, and customize the clones. The default value is `false`. |
| LastModifiedBy | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the user that last updated the expression set view. |
| Name | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the file-based or database expression set. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| UsageType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of industry or the application within the industry that's using the template.Available in API version 60.0 and later. Possible value is: Bre—Business Rules Engine When Business Rules Engine is enabled for a Salesforce instance, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. |
| UsageTypeLabel | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Specifies the label of the usage type that's associated with an expression set template |

      

      

## Usage

        
        

Use expression set templates as reference to build your own expression sets. Expression
            set templates are read-only files that contain rules that can run end-to-end. Save a
            template as an expression set to use it as-is, or modify the expression set for your
            business requirement.

=== ARTICLE: sforce_api_objects_expssetobjectaliasfieldvw.htm ===
---
page_id: sforce_api_objects_expssetobjectaliasfieldvw.htm
title: ExpsSetObjectAliasFieldVw
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_expssetobjectaliasfieldvw.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpsSetObjectAliasFieldVw

Represents the virtual object that provides a consolidated view of
         source object and its alias, and the source object fields and their aliases that are used
         in an expression set. This object is used to check the permission level required to access
         the underlying object fields associated with their field aliases. This object is
      available in API version 56.0 and later.

      

## Supported Calls

         
         

            `describeSObjects()`, `query()`
         

      

      

## Special Access Rules

         
         

To view this object, users need access to the source object, the usage type, and the
            field level security associated with the object field aliases in the object.

      

      

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
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| DurableId | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier for the field. Always retrieve this value before using it, as the value isn’t guaranteed to stay the same from one release to the next. Simplify queries by using this field instead of making multiple queries. |
| ExpsSetDefVerVarField | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Identifies the variable to which this field belongs. This is a required field. |
| FieldAlias | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The alias associated with the object field that's used in the expression set. The field alias can be up to 30 characters in length. This is a required field. |
| InstalledPackageName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the package used to add the record to the org. This is a required field. |
| LastModifiedBy | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the user who modified the alias last. This is a required field. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. This is a required field. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the namespacePrefix__componentName notation. This is a required field.The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| ObjectAlias | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The alias that corresponds to the source object whose fields are used in an expression set. In the context of an expression set, this alias is a group that contains the aliases for fields from the source object. This is a required field. |
| ObjectApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The API name of the source object associated with the object field aliases that are used in an expression set. |
| SourceFieldDataType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The data type of the source object for which the object alias is defined. This is a required field. Possible values are: `ActionOutput` `Boolean` `Currency` `Date` `DateTime` `DecisionMatrix` `DecisionTable` `Numeric` `Percent` `Sobject` `SubExpression` `Text` The default value is `Text`. |
| SourceFieldDecimalScale | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of decimal places applied to the value in the source field that's of the type Currency, Percent, or Number. |
| SourceFieldName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the source object field associated with a field alias that's used in an expression set. This is a required field. |
| UsageType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of application associated with the industry that's using an expression set. Possible values are: `Bre`–Default When Business Rules Engine is enabled for a Salesforce org, the default value is '`Bre`’. Other usage types may be available to you depending on your industry solution and permission sets. |

=== ARTICLE: tooling_api_objects_decisionmatrixdefinition.htm ===
---
page_id: tooling_api_objects_decisionmatrixdefinition.htm
title: DecisionMatrixDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisionmatrixdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionMatrixDefinition

Represents information about a decision matrix definition. This
      object is available in API version 55.0 and later.

      
      

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
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the decision matrix definition. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** Full name of the associated metadata type in Metadata API. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which this decision matrix definition is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the decision matrix definition. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Decision matrix definition metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |

=== ARTICLE: tooling_api_objects_decisionmatrixdefinitionversion.htm ===
---
page_id: tooling_api_objects_decisionmatrixdefinitionversion.htm
title: DecisionMatrixDefinitionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisionmatrixdefinitionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: lookup_tables_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionMatrixDefinitionVersion

Represents information about a decision matrix definition
         version. This object is available in API version 55.0 and later.

      
      

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
- 
- 
- 
- 
- 

: 

                  

                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| DecisionMatrixDefinitionId | **Type** reference **Properties** Filter, Group, Sort **Description** The decision matrix definition associated with this decision matrix definition version. This is a required field. This field is a relationship field. **Relationship Name** DecisionMatrixDefinition **Relationship Type** Lookup **Refers To** DecisionMatrixDefinition |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the decision matrix definition version. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** Full name of the associated metadata type in Metadata API. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which this decision matrix definition version is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the decision matrix definition version. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Decision matrix definition version metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of this decision matrix definition version. Possible values are: `Active` `Draft` `Inactive` `InvalidDraft` `Obsolete` The default value is `Draft`. |
| VersionNumber | **Type** int **Properties** Filter, Group, Sort **Description** The version number of this decision matrix definition version. This is a required field. |

=== ARTICLE: tooling_api_objects_decisiontable.htm ===
---
page_id: tooling_api_objects_decisiontable.htm
title: DecisionTable
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisiontable.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTable

Represents the information about a decision table. This object is
    available in API version 51.0 and later.

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## Supported SOAP API Calls

      
      

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`,
          `update()`, `upsert()`

    

    

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
- 
- 
- 

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
- 
- 
- 

            

            
              

              

: 

: 

: 

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

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

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
- 
- 
- 
- 
- 
- 

            

            
              

              

: 

: 

: 

- 
- 
- 
- 

            

          

        
| Field | Details |
| --- | --- |
| CollectOperator | **Type** string **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** For internal use only. |
| ConditionCriteria | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Custom logic that's used to decide how the input fields are processed. |
| ConditionType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Condition logic that's used for input fields. Possible values are: `All`—All conditions are met (AND) `Any`—Any condition is met (OR) `Custom`—Custom Logic The default value is 'All'. |
| DataSourceType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Type of data source that’s used to create a decision table. Available in API version 59.0 and later. Valid values are: `ContextDefinition` `CsvUpload` `MultipleSobjects` `SingleSobject` The default value is `SingleSobject`. |
| DecisionTableParameters | **Type** [QueryResult](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_queryresult.htm) **Properties** Nillable **Description** Input or output field in a decision table. |
| DecisionTableSourceCriterias | **Type** [QueryResult](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_queryresult.htm) **Properties** Nillable **Description** Filter criteria that’s associated with the decision table condition. Available in API version 59.0 and later. |
| Description | **Type** textarea **Properties** Filter, Nillable, Sort **Description** Description of the decision table. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** Developer name of the decision table. |
| DoesConsiderNullValue | **Type** boolean **Properties** Defaulted on create, Filter, Group, Nillable, Sort **Description** Indicates whether a column that has a null value is considered for lookup (`true`) or not (`false`). The default value is `false`. Available in API version 60.0 and later. |
| DownloadStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the progress status of a CSV download from a CSV-based lookup table. Available in API version 64.0 and later. Valid values are: `Completed` `DownloadInProgress` `Failed` |
| executionType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the backing storage for the Decision Table. Valid values are: `Dmo` `Hbase` `Hbpo` `Solr` `Soql` |
| FilterResultBy | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** If a collection of inputs returns multiple matching outputs, then the FilterResultBy field specifies how the results of a decision table are filtered. Available in API version 59.0 and later. Valid values are: `AnyValue` `CollectOperator` `FirstMatch` `OutputOrder` `Priority` `RuleOrder` `UniqueValues` |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** Name of the decision table. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| IsVersioned | **Type** boolean **Properties** Filter, Group, Nillable, Sort **Description** Indicates whether the CSV based decision table has multiple versions (`true`) or not (`false`). The default value is `false`. Available in API version 60.0 and later. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Language in which the decision table is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| LastSyncDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Latest date on which the decision table was refreshed. |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** Label of the decision table. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Metadata of the decision table. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Namespace prefix that’s associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| PricingElementDecisionTables | **Type** [QueryResult](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_queryresult.htm) **Properties** Nillable **Description** Reserved for future use. |
| RefreshFailureReason | **Type** string **Properties** Filter, Nillable, Sort **Description** Reason for the refresh of the decision table data to fail. Available in API version 60.0 and later. |
| RefreshStatus | **Type** string **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Refresh status of the cached data in the decision table. Available in API version 60.0 and later. Valid values are: `Initiated` `Failed` `Completed` `CompletedWithWarnings` `In Progress` |
| RowLevelOverrideType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the row-level criteria that overrides the Decision Table column criteria. Valid values are: `Both` `Condition` `None` `Operator` The default value is `None`. |
| SetupName | **Type** string **Properties** Filter, Group, Sort **Description** Required. Name of the decision table, which appears in Setup. |
| SourceConditionLogic | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Condition logic that's used to define the decision table from the source data. Available in API version 59.0 and later. |
| SourceObject | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Required. Object that contains the rules based on which the decision table must provide outcomes. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. Status of the decision table. Valid values are: `ActivationInProgress` `Active` `Draft` `Inactive` |
| Type | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Determine whether a decision table’s data volume is high or low. Available in API version 59.0 and later. Valid values are: `Advanced` `HighScaleExecution` `HighVolume`–Reserved for future use `LowVolume` `MediumVolume` `RealTime` The default value is `LowVolume`. |
| UsageType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Usage type of the decision table. Available in API version 59.0 and later. `Bre`–Default `ProductCategoryQualification` `ProductQualification` `RecordAlert` When Business Rules Engine is enabled for a Salesforce org, the default value is `Bre`. Other usage types may be available to you depending on your industry solution and permission sets. |

=== ARTICLE: tooling_api_objects_decisiontabledatasetlink.htm ===
---
page_id: tooling_api_objects_decisiontabledatasetlink.htm
title: DecisionTableDatasetLink
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisiontabledatasetlink.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTableDatasetLink

    Represents a dataset link associated with a decision table. Use dataset links
      in a decision table to select an object whose records the decision table must evaluate and
      provide outcomes for. This object is available in API version 51.0 and later. 

    
      

#### Note

Dataset links are supported only for Standard decision
        tables.

    

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## Supported SOAP API Calls

      
      

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`,
          `update()`, `upsert()`

    

    

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
| DecisionTableId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The unique identifier of the associated decision table. This is a relationship field. **Relationship Name** DecisionTable **Relationship Type** Lookup **Refers To** DecisionTable |
| Description | **Type** textarea **Properties** Filter, Nillable, Sort **Description** The description of the dataset link. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the dataset link. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** The name of the decision table dataset link. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| IsDefault | **Type** boolean **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates whether a dataset link is the default dataset link for a decision table. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which the dataset link is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the dataset link. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Decision table dataset link metadata. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| SetupName | **Type** string **Properties** Filter, Group, Sort **Description** Required. The name of the dataset link, which appears in Setup. |
| SourceObject | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the dataset link's source object. |

=== ARTICLE: tooling_api_objects_decisiontableparameter.htm ===
---
page_id: tooling_api_objects_decisiontableparameter.htm
title: DecisionTableParameter
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisiontableparameter.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTableParameter

Represents an input or output field in a decision table. An input
      field is a field in the business rule object or custom metadata type that contains values used
      by the decision table to evaluate records and values. An output field is a field in the
      business rule object or custom metadata type that contains the values provided as outcomes for
      a rule. This object is available in API version 51.0 and later.

    

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

: 

            

            
              

              

: 

: 

: 
: 
- 
- 
- 

            

          

        
| Field | Details |
| --- | --- |
| DecisionTableId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The unique identifier of the associated decision table. This is a relationship field. **Relationship Name** DecisionTable **Relationship Type** Lookup **Refers To** DecisionTable |
| DomainObject | **Type** string **Properties** Create, Filter, Group, Sort **Description** For polymorhpic fields, indicates the domain object in the field hierarchy. This field is available in API version 59.0 and later. |
| FieldName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the field that’s selected as an input or output for the decision table. |
| FieldPath | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The path of the field used in a decision table in relation to the object that the field belongs to. This field is available in API version 59.0 and later. |
| IsGroupByField | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether an input field is used to group the business rules of the decision table (`true`) or not (`false`). The default value is `false`'. This field is available in API version 55.0 and later. |
| IsRequired | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether a field is required to have input values when a look up is performed on the decision table (`true`) or not (`false`). The default value is `false`'. This field is available in API version 59.0 and later. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| Operator | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The operator used for the input field. Possible values are: `Contains` `DoesNotExistsIn` `DoesNotMatch` `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `IsNotNull` `IsNull` `LessOrEqual` `LessThan` `Matches` `NotEquals` |
| Sequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The sequence in which input fields are processed. |
| SortType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Sort outputs of a decision table based on the values of the input or output parameter field. This field is available in API version 56.0 and later. Possible values are: `AscNullFirst` `AscNullLast` `DescNullFirst` `DescNullLast` `None` The default value is `None`. Outputs can’t be sorted based on picklist and multi-select picklist fields. |
| Usage | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The usage type of a field. Possible values are: `INPUT` `OUTPUT` `ROWCRITERIA` |

=== ARTICLE: tooling_api_objects_decisiontablesourcecriteria.htm ===
---
page_id: tooling_api_objects_decisiontablesourcecriteria.htm
title: DecisionTableSourceCriteria
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisiontablesourcecriteria.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTableSourceCriteria

Represents the fields and values from a data source that are used to
         define the condition logic of the data that's used in a decision table. This object is
      available in API version 59.0 and later.

      
      

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
- 
- 
- 
- 
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| DecisionTableId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the decision table that’s associated with the source criteria. This field is a relationship field. **Relationship Name** DecisionTable **Relationship Type** Lookup **Refers To** DecisionTable |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| Operator | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The operator that’s applied to an associated decision table’s field to filter the data. Possible values are: `Contains`—Available in API version 64.0 and later. `DoesNotExistIn` `DoesNotMatch`—Available in API version 64.0 and later. `Equals` `ExistsIn` `GreaterOrEqual` `GreaterThan` `IsNotNull` `IsNull` `LessOrEqual` `LessThan` `Matches` `NotEquals` The default value is `Equals`. |
| SequenceNumber | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The sequence number used in the associated decision table's source condition logic. |
| SourceFieldName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the field that's used in the decision table. |
| Value | **Type** textarea **Properties** Create, Nillable, Update **Description** The value that’s expected in the source field used in the decision table. |
| ValueType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of the value that’s used to filter the source data. Possible values are: `Formula` `Literal` `Lookup` `Parameter` `Picklist` The default value is `Literal`. |

=== ARTICLE: tooling_api_objects_decisiontbldatasetparameter.htm ===
---
page_id: tooling_api_objects_decisiontbldatasetparameter.htm
title: DecisionTblDatasetParameter
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_decisiontbldatasetparameter.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: dt_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DecisionTblDatasetParameter

    Represents the mapping between a decision table parameter and a field of the
      object selected in the dataset link. This mapping allows the decision table to know which
      object fields from the dataset link must be evaluated by the input fields of the decision
      table. This object is available in API version 51.0 and later.

    

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
- 
- 
- 
- 
- 
- 
- 
- 

            

          

        
| Field | Details |
| --- | --- |
| DatasetFieldName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The name of the field whose value must be compared against an input type decision table parameter when providing the outcome. |
| DatasetSourceObject | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The object whose field values are evaluated by the associated decision table to provide outcomes. |
| DecisionTableDatasetLinkId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The unique identifier of the associated decision table dataset link. This is a relationship field. **Relationship Name** DecisionTableDatasetLink **Relationship Type** Lookup **Refers To** DecisionTableDatasetLink |
| DecisionTableParameterId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The unique identifier of the associated decision table parameter. This is a relationship field. **Relationship Name** DecisionTableParameter **Relationship Type** Lookup **Refers To** DecisionTableParameter |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |

=== ARTICLE: tooling_api_objects_explainabilitymsgtemplate.htm ===
---
page_id: tooling_api_objects_explainabilitymsgtemplate.htm
title: ExplainabilityMsgTemplate
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_explainabilitymsgtemplate.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExplainabilityMsgTemplate

Represents the template that contains the decision explanation
         message for a specified element type. This object is available in API version 56.0 and
      later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`
         

      

      

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
- 
- 
- 
- 

: 

#### 

                  

                  
                     

                     

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

                  

                  
                     

                     

: 

: 

: 
: 
- 
- 
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name for the ExplainabilityMsgTemplate object. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. This field is automatically generated, but you can supply your own value if you create the record using the API. |
| EmtUsageType | **Type** Picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** A explainability message template’s usage type. This field is available from API version 60.0 and later. Possible values are: `Bre`–Default `ProductCategoryQualification` `ProductQualification` `RecordAlert` Note When Business Rules Engine is enabled for a Salesforce instance, the default value is '`Bre`’. Other usage types may be available to you depending on your industry solution and permission sets. |
| ExpressionSetStepType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The step type in an expression set that uses the explainability message template. This is a required field. Possible values are: `Aggregation` `Branch` `BusinessElement` `Calculation` `Condition` `DecisionTableLookup` `ListFilter`—This value is available from API version 59.0 and later. `ListEnabledGroup`—This value is available from API version 59.0 and later. `MatrixLookup` `PredictiveAI` `ReferenceProcedure` The default value is `Calculation`. |
| IsDefault | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the explainability message template for a specified step type is default (`true`) or not (`false`). The default value is `false`. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language in which the message in the explainability message template is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The label for ExplainabilityMsgTemplate. In the UI, this field id Explainability Message Template. |
| Message | **Type** textarea **Properties** Create, Filter, Sort, Update **Description** The message associated with the template for a specific expression set step type. This is a required field. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |
| ResultType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of result for which the message template can be used. The step type for which the result is evaluated can be a condition, conditional group, or branch. This is a required field. Possible values are: `Failed` `NoResult`—This value is available from API version 59.0 and later. `Passed` The default value is `Passed`. |

=== ARTICLE: tooling_api_objects_expressionsetdefinition.htm ===
---
page_id: tooling_api_objects_expressionsetdefinition.htm
title: ExpressionSetDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_expressionsetdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetDefinition

Represents information about an expression set definition. This
      object is available in API version 55.0 and later.

      
      

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
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the expression set definition. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** Full name of the associated metadata type in Metadata API. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| ExecutionScale | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the scale of the input that an expression set processes. The scale determines where the expression set is executed. Possible values are: `High` `Low` |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which the expression set definition is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the expression set definition. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Expression set definition metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |
| Type | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of the expression set definition. Possible values are: `Custom` `Standard` |

=== ARTICLE: tooling_api_objects_expressionsetdefinitionversion.htm ===
---
page_id: tooling_api_objects_expressionsetdefinitionversion.htm
title: ExpressionSetDefinitionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_expressionsetdefinitionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetDefinitionVersion

Represents information about an expression set definition
         version. This object is available in API version 55.0 and later.

      
      

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
- 
- 
- 
- 
- 

: 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the expression set definition version. |
| ExpressionSetDefinitionId | **Type** reference **Properties** Filter, Group, Sort **Description** The expression set definition record associated with this expression set definition version. This field is a relationship field. **Relationship Name** ExpressionSetDefinition **Relationship Type** Lookup **Refers To** ExpressionSetDefinition |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** Full name of the associated metadata type in Metadata API. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which this expression set definition version is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the expression set definition version. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Expression set definition version metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the status of the expression set definition version. Possible values are: `Active` `Draft` `Inactive` `InvalidDraft` `Obsolete` The default value is `Draft`. |
| VersionNumber | **Type** int **Properties** Filter, Group, Sort **Description** The version number of the expression set definition version. This is a required field. |

=== ARTICLE: tooling_api_objects_expressionsetmessagetoken.htm ===
---
page_id: tooling_api_objects_expressionsetmessagetoken.htm
title: ExpressionSetMessageToken
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_expressionsetmessagetoken.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: decision_explainer_bre_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetMessageToken

Represents a token that's used in an explainability message template.
         The token can be replaced with an expression set version resource that the template is used
         in. This object is available in API version 59.0 and later.

      
      
         

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

- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** The description of an expression set message token record. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name for the ExpressionSetMessageToken object. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. This field is automatically generated, but you can supply your own value if you create the record using the API. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language in which the expression set message token is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The label for the ExpressionSetMessageToken. In the UI, this field is Expression Set Message Token. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |

=== ARTICLE: tooling_api_objects_expressionsetobjectalias.htm ===
---
page_id: tooling_api_objects_expressionsetobjectalias.htm
title: ExpressionSetObjectAlias
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_expressionsetobjectalias.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Business Rules Engine
parent_page: expression_set_tooling_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetObjectAlias

Represents the alias of the source object that's used in an
         expression set. This object is available in API version 56.0 and later.

      
      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

## Special Access Rules

         
         

To use this object, users must have the Modify All Data permission, and the
            orgHasExpressionSet org permission.

      

      

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
- 
- 
- 
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| DataType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Specifies the data type of the object alias. This is a required field. Possible values are: `JSON` `sObject` The default value is `sObject`. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the expression set object alias. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** The name of the expression set object alias. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which the expression set object alias is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the expression set object alias. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Expression set object alias metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |
| ObjectAlias | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The alias that corresponds to the source object that's used in an expression set. In the context of an expression set, this alias in a group that contains the aliases of fields from the source object. The length of the object alias can’t exceed 40 characters. This is a required field. |
| ObjectApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The API name of the source object associated with the alias that's being used in an expression set. |
| UsageType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of application associated with the industry that's using an expression set. Possible values are: `Bre`–Default `ProductCategoryQualification` `ProductQualification` `RecordAlert` When Business Rules Engine is enabled for a Salesforce org, the default value is '`Bre`’. Other usage types may be available to you depending on your industry solution and permission sets. |

