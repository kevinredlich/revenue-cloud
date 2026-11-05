# Revenue Management Developer Guide 264 — sección: Product Configurator (135 artículos)

=== ARTICLE: actions_obj_run_config_rules.htm ===
---
page_id: actions_obj_run_config_rules.htm
title: Run Config Rules Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_run_config_rules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Run Config Rules Action

Run rules for a specific quote or order based on a context ID or
            transaction ID, and process other steps that are part of the configuration directly
            within a Flow. This action decouples rule execution from configurations to enable
            independent execution of rules and for easier retrieval of responses.

        
            

This action is available in API version 65.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/runConfigRules`

                    
: If you’re calling this invocable action from an external website, include
                        the site name in the URI.

                    
: `<siteName>/services/data/v68.0/actions/standard/runConfigRules`

                
                
                    

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
| transactionContextId | **Type** string **Description** Unique identifier for the transaction context. |
| transactionId | **Type** string **Description** Required. Unique identifier for the transaction. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| configRuleResult | **Type** Apex-defined **Description** An `runtime_industries_cpq.ConfigRuleResult` record that contains the configuration rule execution results including validation messages, product recommendations, visibility rules, and errors from rule processing. |
| transactionContextId | **Type** string **Description** Unique identifier for the transaction context. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This example shows a sample request to run rules for the specified quote
                            based on the transaction context ID and transaction ID.

                        

```
{
  "inputs": [
    {
      "transactionContextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
      "transactionId": "0Q0DU0000005tJh0AI"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
[
  {
    "actionName": "runConfigRules",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "transactionContextId": "0000000p18dq18g0029175793402786243c3d5ea94c241f09c11388ac1b865f9",
      "configRuleResult": {
        "visibilityRules": [
          {
            "stiId": "0QLxx0000004CU0GAM",
            "prcId": "PRC1",
            "attributeId": "Color",
            "attributePicklistValueId": "Red",
            "target": "Attribute",
            "scope": "Product",
            "type": "Hide"
          },
          {
            "stiId": "0QLxx0000004CU0GAM",
            "prcId": "PRC2",
            "attributeId": "Size",
            "attributePicklistValueId": "Large",
            "target": "Attribute",
            "scope": "Bundle",
            "type": "Disable"
          }
        ],
        "transactionContextId": "0000000p18dq18g0029175793402786243c3d5ea94c241f09c11388ac1b865f9",
        "productRecommendationRules": [
          {
            "referenceId": "CORE_BUNDLE_001",
            "productIds": [
              "01t000000001234",
              "01t000000005678"
            ]
          }
        ],
        "messageRules": [
          {
            "stiId": "0QLxx0000004CU0GAM",
            "severity": "INFO",
            "messages": [
              "Product configuration validated successfully"
            ]
          },
          {
            "stiId": "0QLxx0000004CU0GAM",
            "severity": "INFO",
            "messages": [
              "All required attributes are configured"
            ]
          },
          {
            "stiId": "0QLxx0000004CU0GAM",
            "severity": "INFO",
            "messages": [
              "Bundle compatibility check passed"
            ]
          }
        ],
        "errors": []
      }
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

                    

                    
: 
                        

Here's a sample input to call this invocable action by using `transactionContextId` property from Apex
                            code.

                        

```
// Create the invocable action with namespace
Invocable.Action action = Invocable.Action.createStandardAction('runConfigRules');
            
// Set input parameters using setInvocationParameter
String contextId = '008d27d7-e004-4906-a949-ee7d7c323c77';
System.debug('Setting transactionContextId parameter with value: ' + contextId);
            
// Use the exact parameter name format from the debug output
action.setInvocationParameter('transactionContextId', contextId);
            
// Debug the action parameters
System.debug('Action parameters: ' + action);
            
// Execute the action
System.debug('Invoking action...');
List<Invocable.Action.Result> results = action.invoke();
            
System.debug('Number of results: ' + results.size());
```

=== ARTICLE: cml_about_the_apex_debugging_log_file.htm ===
---
page_id: cml_about_the_apex_debugging_log_file.htm
title: About the Apex Debugging Log File
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_about_the_apex_debugging_log_file.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_debugging_cml.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# About the Apex Debugging Log File

The Apex debugging log file contains three sections: RLM_CONFIGURATOR_BEGIN,
    RLM_CONFIGURATOR_STATS, and RLM_CONFIGURATOR_END.

    

## RLM_CONFIGURATOR_BEGIN

      
      

JSON representation of the request payload to ExecuteConstraintsRESTService.

      

```
"contextProperties" : { },
"rootLineItems" : [ {
  "attributes" : { },
  "properties" : {  },
  "ruleActions" : null,
  "attributeDomains" : { },
  "portDomainsToHide" : { },
  "lineItems" : [ {} ]
} ],
"orgId" : "00Dxx0000006H2F"
}
```

    

    

## RLM_CONFIGURATOR_STATS

      
      

Key statistics of the request execution by the constraint engine, as in this example.

      

```
"rootId" : "0QLxx0000004D1uGAE",  //Root ID that is being configured
"Product" : "SFDC License",  //Root product name
"Total Execution Time" : "2ms",  //Total solver time
"Constraints Execution Stats" : "Distinct: 18 Total: 70",  //Number of distinct and total constraint satisfaction attempts
"Solving goal AndGoal([ConfigureComponentGoal(RootProduct RootProduct_0)]) took " : "2ms",  //Total solver time for the goal
"Configurator Stats" : "Total Time 2ms",  //Total time
"Number of Component" : "6",  //Number of components instantiated
"Number of Variables" : "42",  //Number of variables instantiated
"Number of Constraints" : "13",  //Number of constraints instantiated
"Number of Backtracks" : "0",  //Number of backtracks solver did for the last choice point
"Constraints Violation Stats" : "Distinct: 0 Total: 0",  //Distinct and total number of constraint violations followed by a list of top 10
"ChoicePoint Backtracking Stats" : "Distinct: 0 Total: 0"  // Distinct and total number of backtracked choice points followed by a list of top 10
}
```

    

    

## RLM_CONFIGURATOR_END

      
      

JSON representation of the response payload from ExecuteConstraintsRESTService.

      

```
"id" : "0QLxx0000004D1uGAE",
"rootId" : null,
"parentId" : null,
"cfgStatus" : "User",
"name" : "RootProduct",
"relation" : null,
"source" : "SalesTransaction.SalesTransactionItem",
"qty" : 1,
"actionCode" : null,
"modelName" : "Support_instance_variable_in_CML",
"productId" : "01txx0000006iP2AAI",
"productRelatedComponentId" : null,
"attributes" : {},  "properties" : {},
"ruleActions" : [ {} ],   "attributeDomains" : {},  "portDomainsToHide" : {},
"lineItems" : [ {} ]
}
```

=== ARTICLE: cml_action_rule.htm ===
---
page_id: cml_action_rule.htm
title: Action Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_action_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Action Rule

The CML Action Rule is defined using the rule() keyword. Its primary purpose is to
    execute a designated action, specified as a string literal, when a condition is met.

    
      

This action is typically handled by external systems, such as the Product Configurator API
        or custom code, to manage business processes, workflows, or complex constraints that fall
        outside the constraint engine's primary scope.

      

Action rules have this syntax.

      

```
rule(condition, action, arg, ..., arg)
rule(<condition>, <action>, "attribute", <attribute>);
rule(<condition>, <action>, "attribute", <attribute>, "value", [<attribute values>]);
rule(<condition>, <action>, "relation", <relation>, "type", <type>);

```

      

`condition` is any logic expression such as a constraint
        in CML.

      

`action` is a string literal that specifies an action
        that can be interpreted by the Product Configurator API. The Product Configurator API
        supports these actions.

      
        
- Hide: hide attribute, attribute value, product option

        
- Disable: disable attribute, attribute value, product option

        
- args are a list of arguments needed to execute the action. An argument is a pair
          including a string literal and an identifier, a literal, or a domain, enclosed in brackets
          [ ] to specify multiple values. The string literal specifies what kind of argument
          follows. The identifier attribute can be defined in the type. The engine retrieves the
          argument value and passes it to the caller to execute the action.

=== ARTICLE: cml_annotation_example_closeRelation.htm ===
---
page_id: cml_annotation_example_closeRelation.htm
title: closeRelation Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_closeRelation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# closeRelation Annotation

closeRelation is a CML annotation that controls addition of new line items to the
    relationship by the engine.

    
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Annotation | `closeRelation` |
| --- | --- |
| Applicable to | Relationship |
| Value Type/Values | true, false |
| Description | If `closeRelation` is not specified, the engine sets it implicitly as false for the relationship. If `closeRelation` is specified as true, the engine prevents the addition of new line items to the relationship. If `closeRelation` is specified as false, the engine allows the addition of new line items to the relationship. |

    

    

## Example 1

      
      

In this example, the `closeRelation` annotation isn’t
        specified for the relationship (`mainalternatorclassification`). The model contains the constraint.

      

```
type LineItem;
type GeneratorSet : LineItem { 
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    relation mainalternatorclassification : MainAlternatorClassification;
    constraint(dutyRating == "Continuous Power (COP)" -> mainalternatorclassification[Alternator_240] >= 1);
}
type MainAlternatorClassification : LineItem;
type Alternator_220 : MainAlternatorClassification;
type Alternator_440 : MainAlternatorClassification;
type Alternator_240 : MainAlternatorClassification;
```

    

    

## Example 2

      
      

In this example, the `closeRelation`annotation is
        defined as `false` for the relationship (`mainalternatorclassification`). The model contains the
        constraint.

      

```
type LineItem;
type GeneratorSet : LineItem {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(closeRelation = false)    
    relation mainalternatorclassification : MainAlternatorClassification;
    constraint(dutyRating == "Continuous Power (COP)" -> mainalternatorclassification[Alternator_240] >= 1);
}
type MainAlternatorClassification : LineItem;
type Alternator_220 : MainAlternatorClassification;
type Alternator_440 : MainAlternatorClassification;
type Alternator_240 : MainAlternatorClassification;
```

    

    

## Example Description and Configurator Result

      
      

In example 1, the `mainalternatorclassification`
        relation is not specified with the `closeRelation`
        annotation, but the system considers it as `false` by
        default. In example 2, the relation is explicitly defined with `false`. As a result, if the user updates the `dutyRating` variable to `"Continuous Power
          (COP)"`, the system adds the `Alternator_240` product according to annotation and constraint logic and allows
        addition of other products from the `mainalternatorclassification` relation (`Alternator_220,Alternator_440`). The system does not allow to unselect the
          `Alternator_240` product specified in the constraint
        while the `"Continuous Power (COP)"` is
        selected. If the user updates the `dutyRating` variable
        to another value (For example, `Emergency Standby Power
          (ESP)"`), the engine removes the `Alternator_240
        `product, but the user can add/select/unselect all products from the relationship
        manually.

    

    

## Example 3

      
      

In this example, the `closeRelation` annotation is
        specified as `true` for the relationship (`mainalternatorclassification`). The model contains the
        constraint

      

```
type LineItem;
type GeneratorSet : LineItem {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(closeRelation = true)    
    relation mainalternatorclassification : MainAlternatorClassification;
    constraint(dutyRating == "Continuous Power (COP)" -> mainalternatorclassification[Alternator_240] >= 1);
}
type MainAlternatorClassification : LineItem;
type Alternator_220 : MainAlternatorClassification;
type Alternator_440 : MainAlternatorClassification;
type Alternator_240 : MainAlternatorClassification;
```

      

In example 3, the `mainalternatorclassification`
        relation is specified with the `closeRelation` annotation
        as `true`. As a result, if a user updates the dutyRating
        variable to `"Continuous Power (COP)"`, the
        engine resets it back to `"Emergency Standby Power
          (ESP)"` to prevent adding the `Alternator_240` product according to the annotation. The user can add all `mainalternatorclassification` products manually (including the
          `Alternator_240` product specified in the
        constraint).

    

    

Table 1. closeRelation Configuration Settings
        
        
        
        
        
        
        
        
          
            

            

            

            

            

            

            

          

        

        
          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

        

      
| Associated Example | Product Group Structure | Applicable to | "closeRelation" annotation | User Action | Engine Action | UI Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| N/A | Individual product | Relationship | not specified | Change variable value specified in constraint condition | Add the product according to the constraint. Allow addition of other products to the relationship | Display product specified in constraint as pre-selected: if a User unselects it, the product returns back to selected state. User can select other products from the relationship |
| N/A | Individual product | Relationship | TRUE | Change variable value specified in constraint condition | Reset the variable value back to the default value to avoid addition the relation product specified in the constraint | Products from the relation are not added or selected (including the product specified in constraint). User can manually select any products from the relationship |
| N/A | Individual product | Relationship | FALSE | Change variable value specified in constraint condition | Add the product according to the constraint. Allow addition of other products to the relationship | Display product specified in constraint as pre-selected: if a User unselects it, the product returns back to selected state. User can select other products from the relationship |
| Example 1 | Product Classification | Relationship | not specified | Change variable value specified in constraint condition | Add the product according to the constraint. Allow addition of other products to the relationship from browse products pop up | Display product specified in constraint as pre-selected: if a User unselects it, the product returns back to selected state. User can add other products from the relationship in browse products pop up |
| Example 2 | Product Classification | Relationship | FALSE | Change variable value specified in constraint condition | Add the product according to the constraint. Allow addition of other products to the relationship from browse products pop up | Display product specified in constraint as pre-selected: if a User unselects it, the product returns back to selected state. User can add other products from the relationship in browse products pop up |
| Example 3 | Product Classification | Relationship | TRUE | Change variable value specified in constraint condition | Reset the variable value back to the default value to avoid addition the relation product specified in the constraint | Products from the relation are not added or selected (including the product specified in constraint). User can manually browse and add any products from the relationship |

=== ARTICLE: cml_annotation_example_configurable.htm ===
---
page_id: cml_annotation_example_configurable.htm
title: configurable Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_configurable.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# configurable Annotation

`configurable` is a CML annotation that controls whether
    a model element can be configured.

    
      

`configurable` annotation specification: Variable

      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `configurable` |
| --- | --- |
| Applicable to | Variable |
| Value Type/Values | true, false |
| Description | If the `configurable` annotation is not explicitly specified, the engine sets it implicitly as true for the variable. If the `configurable` annotation is explicitly specified as true, the variable is indicated as configurable. The engine sets the value to the variable. If the `configurable` annotation is explicitly specified as false, the engine doesn't set a value to the variable. |

    

    

## Example 1

In this example, the `configurable` annotation is not specified for the variable (Cable Entry) of the
        VoltageConnection child products. The `defaultValue` is
        not defined.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

In this example, the `configurable` annotation is not
        explicitly specified for the variable `cableEntry`, but
        the system considers it as `configurable = true` by
        default. As a result, the system sets the `"Top
          Entry"` (the first value in the `["Top
          Entry", "Bottom Entry", "Side Entry"]` CML domain) as the
        initial value for the configurable `Cable Entry`
        variable.

    

    

## Example 2

In this example, the `configurable` annotation is specified as `true` for the variable (Cable Entry) of the VoltageConnection child products. The
          `defaultValue` is not
      specified.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    @(configurable = true)
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

In this example, the `configurable` annotation is
          `true` for the variable. As a result, the system
        specifies the variable as configurable and sets the `"Top
          Entry"` (the first value in the `["Top
          Entry", "Bottom Entry", "Side Entry"]` CML domain) as the
        initial value for the `Cable Entry`.

    

    

## Example 3

In this example, the `configurable` annotation is specified as `false` for the variable (Cable Entry) of the VoltageConnection child products.
        The `defaultValue` is not
      specified

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    @(configurable = false)
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

In this example, the `configurable` annotation is
          `false` for the variable. As a result, the engine
        doesn't configure the variable with an initial value, and it is displayed empty on the
        Product Configuration UI.

    

    

## Example 4

In this example, the `configurable` is `false` and `defaultValue` annotation is `true` for the variable (Cable Entry) of the VoltageConnection child
      products.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    @(configurable = true, defaultValue = "Side Entry")
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

In this example, the system indicates the variable as `configurable` and sets the `"Side
          Entry"` as the initial value for the `Cable
          Entry` defined in the `defaultValue`
        annotation.

    

    

## Example 5

In this example, the `configurable` and `defaultValue` annotations
        are specified for the variable (Cable Entry) of the VoltageConnection child
      products.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    @(configurable = false, defaultValue = "Side Entry")
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

In this example, the system sets the `"Side
          Entry"` as the initial value for the `Cable
          Entry` according to the `defaultValue`
        annotation.

    

    

Table 1. configurable Configuration Settings
        
        
        
        
        
        
        
        
          
            

            

            

            

            

            

            

          

        

        
          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

          
            

            

            

            

            

            

            

          

        

      
| Associated Example | Product Group Structure | Applicable to | "CONFIGURABLE" annotation | User Action | Engine Action | UI Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Example 1 | Individual product | Variable | not specified | Configure the product containing variable | Set the first value from the variable domain as initial value. If the User changes the variable value manually, reset it back to the first value from the variable domain. If the default value is defined in PCM, reset it back to the first value from the variable domain | Display defined by engine variable value as the default value |
| Example 2 Example 4 | Individual product | Variable | TRUE | Configure the product containing variable | Set the first value from the variable domain as initial value If the User changes the variable value manually, reset it back to the first value from the variable domain. If the default value is defined in PCM, reset it back to the first value from the variable domain If the defaultValue annotation is specified for the variable, set it as initial value | Display defined by engine variable value as the default value |
| Example 3 Example 5 | Individual product | Variable | FALSE | Configure the product containing variable | Set emptiness for the variable as initial value (If the default value is specified in PCM for the variable, set it as initial value instead of emptiness). If the defaultValue annotation is specified for the variable, set it as initial value (despite of the PCM default value) | Display defined by engine or PCM variable value as the default value |

=== ARTICLE: cml_annotation_example_defaultValue.htm ===
---
page_id: cml_annotation_example_defaultValue.htm
title: defaultValue Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_defaultValue.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# defaultValue Annotation

The `defaultValue` annotation is used on a variable to
    define the value it should start with when configuration begins.

    
      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `defaultValue` |
| --- | --- |
| Applicable to | Variable |
| Value Type/Values | Literal |
| Description | The configurator uses the default value defined in PCM (Product Attribute Definition). If no PCM default is available, the configurator uses the first value in the variable domain as the initial value. If no default value is defined in PCM and a defaultValue is specified in CML, the configurator uses the value defined in CML as the initial value of the variable. |

    

    

## Example 1

In this example, neither PCM nor CML defines a default value
        for the Cable Entry
      variable.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
type VoltageConnection {
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

The configurator sets `"Top Entry"` as the initial value
        for `Cable Entry`, because it is the first value in the
        variable domain `["Top Entry", "Bottom
          Entry", "Side Entry"`.

    

    

## Example 2

In this example, PCM (Product Attribute Definition) defines
          `"Bottom Entry"` as the default value for `Cable Entry`, and no `defaultValue` annotation is defined for this variable in
      CML.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}
// This annotation is added automatically if PCM has a default before the product is added to CML. If the product already exists in CML, the annotation is added or updated only after running Sync.
@(defaultValue = "Bottom Entry") 
type VoltageConnection {
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

The configurator sets the `"Bottom Entry"` as
        the initial value for the `Cable Entry` of the `VoltageConnection` child products.

      

As a best practice, define the default value in PCM and use the Sync function in CML to keep the model aligned whenever PCM settings are updated.

    

    

## Example 3

In this example, a `defaultValue` annotation with `"Side Entry"` is defined in CML, and no default value is defined in PCM
        for the `Cable Entry`
      variable.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[1..999999];
}

type VoltageConnection {
    @(defaultValue = "Side Entry")
    string cableEntry = ["Top Entry", "Bottom Entry", "Side Entry"];
}
```

    

## Example Description and Configurator Result

      
      

The configurator sets the `"Side Entry"`
        annotation value as the initial value for Cable Entry.

      

#### Note

We recommend that you define default values in PCM (Product Attribute
        Definition) whenever possible, as this approach promotes consistency across products and
        simplifies maintenance.

      

The defaultValue annotation in CML should be used only when a default value is not suitable
        to be defined in PCM due to specific modeling requirements.

      

When a default value is defined in PCM but the CML model has not been synced, the
        configurator still applies the PCM default. However, the value displayed in the CML model
        may become inconsistent with PCM.

      

To avoid such inconsistencies, it is recommended to run the Sync action in CML after
        updating default values in PCM, so that the CML model remains aligned with the latest PCM
        settings.

    

    

## defaultValue Configuration Settings

      
      

Table 1. defaultValue Configuration Settings
          
          
          
          
          
          
          
            
              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

            

            
              

              

              

              

              

              

            

            
              

              

              

              

              

              

            

            
              

              

              

              

              

              

            

            
              

              

              

              

              

              

            

          

        
| Associated Example | Configurable Specified | Configurable Value | defaultValue Specified | Initial Value Behavior | Example UI Result |
| --- | --- | --- | --- | --- | --- |
| Example 1 | No | default = TRUE | No | Uses the first value in the domain | Automatically set to "Top Entry" |
| Example 2 | Yes | TRUE | No | Uses the first value in the domain | Automatically set to "Bottom Entry" |
| Example 3 | Yes | FALSE | No | No initial value is set | Field remains empty |
| N/A | Yes | TRUE | Yes | Uses the value defined in defaultValue | Automatically set to "Side Entry" |
| N/A | Yes | FALSE | Yes | Still uses the value defined in defaultValue | Automatically set to "Side Entry" |

=== ARTICLE: cml_annotation_example_domainComputation.htm ===
---
page_id: cml_annotation_example_domainComputation.htm
title: domainComputation Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_domainComputation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# domainComputation Annotation

`domainComputation` is a CML annotation that specifies
    how the domain of a model element is determined, either by using a fixed domain or by
    computing the domain dynamically during configuration.

    
      

`domainComputation` annotation specification: Variable
        and Relationship

      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `domainComputation` |
| --- | --- |
| Applicable to | Variable and Relationship |
| Value Type/Values | true, false |
| Description | `If domainComputation annotation is not explicitly specified, the engine sets it implicitly as false for the variable, and true for a relationship`If the `domainComputation` annotation is specified as `true`, the variable or relationship domain is dynamically determined based on the configuration and constraint logic. If the `domainComputation` annotation is specified as `false`, the variable domain is fixed. |

    

    

## Example 1

In this example, the `domainComputation` annotation is not specified for the variable (voltage) of the
          `GeneratorSet` type. The model contains the
        constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"]
    constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380");
    constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440");
}

```

    

## Example 2

In this example, the `domainComputation` annotation is explicitly specified as false for the variable
        (voltage) of the `GeneratorSet` type. The model contains
        the constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(domainComputation = false)
    string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"];
    constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380");
    constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440");
}
```

    

## Example Description and Configurator Result

      
      

In example 1, the `domainComputation` annotation is not
        explicitly specified for the `voltage` variable, but the
        system considers it as `false` by default. In example 2,
        the `domainComputation` annotation is explicitly defined
        as `false`. As a result, the system remains the variable
        domain unchanged `(["220/380", "240/416",
          "347/600", "255/440", "277/480", "2400/4160",
          "7200/12470", "7621/13200", "7976/13800"])` and
        executes the constraints:

      

If the `dutyRating` is selected with the `"Continuous Power (COP)"` value, the `voltage` is pre-populated with the next possible value from
        the variable domain `("240/416")` to satisfy
        the constraint.

      

If the `dutyRating` is selected with the `"Data Center Continuous (DCC)"` value, the `voltage` is pre-populated with the `"255/440"` value to satisfy the constraint.

    

    

## Example 3

In this example, the `domainComputation` annotation is explicitly specified as `true` for the variable (`voltage`) of the `GeneratorSet` type. The
        model contains the
      constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(domainComputation = true)
    string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"];
    constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380");
    constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440");
}
```

    

## Example Description and Configurator Result

      
      

In example 3, the `domainComputation` annotation is
        explicitly specified as `true` for the `voltage` variable. As a result, the system updates the
        variable domain based on the constraint logic.

      

If the `dutyRating` is selected with the `"Continuous Power (COP)"` value, the voltage is
        pre-populated with the next possible value from the variable domain `("240/416")` to satisfy the constraint. The variable
        domain is updated to exclude the `"220/380"`
        value.

      

If the `dutyRating` is selected with the `"Data Center Continuous (DCC)"` value, the `voltage` is pre-populated with the `"255/440"` value to satisfy the constraint. The variable domain is
        updated to contain only the `"255/440"`
        value.

    

    

## Example 4

In this example, the `domainComputation` annotation is not specified for the relationship
        (temperatureSensors). The model contains the
      constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    relation temperatureSensors : TemperatureSensor[0..1];
    constraint(dutyRating == "Continuous Power (COP)" -> temperatureSensors[BearingTemperatureSensor] == 0);
    constraint(dutyRating == "Data Center Continuous (DCC)" -> temperatureSensors[StatorTemperatureSensor] == 0);
}
type TemperatureSensor;
type BearingTemperatureSensor : TemperatureSensor;
type StatorTemperatureSensor : TemperatureSensor;
```

    

## Example 5

In this example, the `domainComputation` annotation is explicitly specified as `true` for the relationship (temperatureSensors). The model
        contains the constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(domainComputation = true)
    relation temperatureSensors : TemperatureSensor[0..1];
    constraint(dutyRating == "Continuous Power (COP)" -> temperatureSensors[BearingTemperatureSensor] == 0);
    constraint(dutyRating == "Data Center Continuous (DCC)" -> temperatureSensors[StatorTemperatureSensor] == 0);
}
type TemperatureSensor;
type BearingTemperatureSensor : TemperatureSensor;
type StatorTemperatureSensor : TemperatureSensor;
```

    

## Example Description and Configurator Result

      
      

In example 4, the `domainComputation` annotation is not
        explicitly specified for the `temperatureSensors`
        relationship, but the system considers it as `true` by
        default. In example 5, the `domainComputation` annotation
        is explicitly specified as `true` for the relationship.
        As a result, the system updates the relationship domain based on the constraint logic.

      

- If the `dutyRating` is selected with the `"Continuous Power (COP)"` value, the system
          re-computes the relationship domain and excludes the `BearingTemperatureSensor` product to satisfy the constraint. The `StatorTemperatureSensor` product remains and can be selected
          in scope of the `GeneratorSet` bundle product;

- If the `dutyRating` is selected with the `"Data Center Continuous (DCC)"` value: the system
          re-computes the relationship domain and excludes the `StatorTemperatureSensor` product to satisfy the constraint. The `BearingTemperatureSensor` product remains and can be
          selected in scope of the `GeneratorSet` bundle
          product.

    

    

## Example 6

In this example, the `domainComputation` annotation is explicitly specified as `false` for the relationship (`temperatureSensors`). The model contains the
      constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    @(domainComputation = false)
    relation temperatureSensors : TemperatureSensor[0..1];
    constraint(dutyRating == "Continuous Power (COP)" -> temperatureSensors[BearingTemperatureSensor] == 0);
    constraint(dutyRating == "Data Center Continuous (DCC)" -> temperatureSensors[StatorTemperatureSensor] == 0);
}
type TemperatureSensor;
type BearingTemperatureSensor : TemperatureSensor;
type StatorTemperatureSensor : TemperatureSensor;
```

    

## Example Description and Configurator Result

      
      

In example 6, the `domainComputation` annotation is
        explicitly specified as `false` for the relationship. As
        a result, the system remains the relationship domain unchanged and executes the
        constraints:

      

If the `dutyRating` is selected with the `"Continuous Power (COP)"` value, the system displays
        both `BearingTemperatureSensor` and `StatorTemperatureSensor` products in scope of the `GeneratorSet` bundle product. The `BearingTemperatureSensor` product cannot be selected based on the constraint.

      

If the `dutyRating` is selected with the `"Data Center Continuous (DCC)"` value, the system
        displays both `BearingTemperatureSensor` and `StatorTemperatureSensor` products in scope of the GeneratorSet
        bundle product. The `StatorTemperatureSensor` product
        cannot be selected based on the constraint.

    

    

## domainComputation Configuration Settings

      
      

Table 1. defaultValue Configuration Settings
          
          
          
          
          
          
          
            
              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

```

```

            

            
              

              

              

              

              

              

```

```

            

            
              

              

              

              

              

              

```

```

            

          

        
| Applicable to | "domainComputation" annotation | User Action | Actual UI Behavior | Actual Engine Behavior | Constraint Model |
| --- | --- | --- | --- | --- | --- |
| string voltage | not specified | Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • Initial value for the voltage = the value specified in the @defaultValue annotation ("220/380") • The user can select a different voltage value (e.g. "240/416", "255/440" etc.). The system remains User selected voltage • The user can save the configuration with both values: initial voltage or user-selected voltage Case 2: Duty Rating = "Continuous Power (COP)" • Initial value for the voltage = next possible value from the domain to satisfy the constraint ("240/416") • Warning: If the user selects a different voltage (e.g. "220/380", "255/440", "2400/4160" etc.), the system reverts it to the initial value ("240/416") • The user can save the configuration with the initial voltage value (the configuration cannot be saved with other voltage due to reverting) Case 3: Duty Rating = "Data Center Continuous (DCC)" • Initial value for the voltage = specified value in constraint that comes first in the domain ("220/380") • The user can select a different vaild voltage specified in constraint ("255/440"). The system remains User selected voltage • If the user selects a voltage that not vaild in the constraint (e.g. "240/416", "2400/4160" etc.), the system will revert it to one of the values defined in constraint ("220/380" or "255/440") • The user can save the configuration with the specified in constraint voltage value (the configuration cannot be saved with other voltage due to reverting) | Always show the full voltage domain regardless of the Duty Rating selection. | Remain the full voltage domain. Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • If the configuration is saved with initial (default) voltage value ("220/380"): attributeName":"voltage","cfgStatus":"Default" • If the configuration is saved with User selected voltage value (e.g. "255/440"): attributeName":"voltage","cfgStatus":"Default" Case 2: Duty Rating = "Continuous Power (COP)" • If the configuration is saved with initial/reverted to initial voltage value ("240/416"): "attributeName":"voltage","cfgStatus":"Engine" Case 3: Duty Rating = "Data Center Continuous (DCC)" • If the configuration is saved with initial ("220/380")/other constraint specified("255/440")/reverted to constraint specified voltage values ("220/380", "255/440"): "attributeName":"voltage","cfgStatus":"Default" | type GeneratorSet { @(defaultValue = "Emergency Standby Power (ESP)") string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"]; @(defaultValue = "220/380") string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"]; constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380"); constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440" || voltage == "220/380"); } |
| string voltage | TRUE | Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • Display the full voltage domain • Initial value for the voltage = the value specified in the @defaultValue annotation ("220/380") • The user can select a different voltage value (e.g. "240/416", "255/440" etc.). The system remains User selected voltage • The user can save the configuration with both values: initial voltage or User selected voltage Case 2: Duty Rating = "Continuous Power (COP)" • Display updated voltage domain according to the constraint (the "220/380" is not shown) • Initial value for the voltage = next possible value from the domain to satisfy the constraint ("240/416") • Warning: If the user selects a different voltage (e.g. "255/440", "2400/4160" etc.), the system reverts it to the initial value ("240/416") • The user can save the configuration with the initial ("240/416") voltage value (the configuration cannot be saved with other voltage due to reverting) Case 3: Duty Rating = "Data Center Continuous (DCC)" • Display updated voltage domain according to the constraint (only "220/380" and "255/440" are shown, other values are excluded) • Initial value for the voltage = specified value in constraint that comes first in the domain ("220/380") • Warning: If the user selects a different voltage specified in constraint ("255/440"), the system reverts it to the initial value ("220/380") • The user can save the configuration with the initial voltage value (the configuration cannot be saved with the "255/440" voltage due to reverting) | Show updated voltage domain based on Duty Rating selection and constraint logic. | Update voltage domain based on Duty Rating selection and constraint logic. Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • Remain the full voltage domain • If the configuration is saved with initial (default) voltage value ("220/380"): attributeName":"voltage","cfgStatus":"Default" • If the configuration is saved with User selected voltage value (e.g. "255/440"): attributeName":"voltage","cfgStatus":"Default" Case 2: Duty Rating = "Continuous Power (COP)" • Update voltage domain according to the constraint (exclude the "220/380" value) • If the configuration is saved with initial/reverted voltage value ("240/416"): "attributeName":"voltage","cfgStatus":"Engine" Case 3: Duty Rating = "Data Center Continuous (DCC)" • If the configuration is saved with initial ("220/380")/reverted to "220/380" constraint specified voltage value: "attributeName":"voltage","cfgStatus":"Engine" | type GeneratorSet { @(defaultValue = "Emergency Standby Power (ESP)") string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"]; @(defaultValue = "220/380", domainComputation = true) string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"]; constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380"); constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440" || voltage == "220/380"); } |
| string voltage | FALSE | Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • Initial value for the voltage = the value specified in the @defaultValue annotation ("220/380") • The user can select a different voltage value (e.g. "240/416", "255/440" etc.). The system remains User selected voltage • The user can save the configuration with both values: initial voltage or User selected voltage Case 2: Duty Rating = "Continuous Power (COP)" • Initial value for the voltage = next possible value from the domain to satisfy the constraint ("240/416") • Warning: If the user selects a different voltage (e.g. "220/380", "255/440", "2400/4160" etc.), the system reverts it to the initial value ("240/416") • The user can save the configuration with the initial voltage value (the configuration cannot be saved with other voltage due to reverting) Case 3: Duty Rating = "Data Center Continuous (DCC)" • Initialvalue for the voltage = specified value in constraint that comes first in the domain ("220/380") • The user can select a different voltage specified in constraint ("255/440"). The system remains User selected voltage • If the user selects a voltage that not specified in the constraint (e.g. "240/416", "2400/4160" etc.), the system will revert it to one of the values defined in constraint ("220/380" or "255/440") • The user can save the configuration with the specified in constraint voltage value (the configuration cannot be saved with other voltage due to reverting) | Same as not specified Always show the full voltage domain regardless of the Duty Rating selection. | Same as not specified Remain the full voltage domain. Case 1: Duty Rating = any except specified in constraints (e.g. "Prime Power (PRP)", "Emergency Standby Power (ESP)"): • If the configuration is saved with initial (default) voltage value ("220/380"): attributeName":"voltage","cfgStatus":"Default" • If the configuration is saved with User selected voltage value (e.g. "255/440"): attributeName":"voltage","cfgStatus":"Default" Case 2: Duty Rating = "Continuous Power (COP)" • If the configuration is saved with initial/reverted to initial voltage value ("240/416"): "attributeName":"voltage","cfgStatus":"Engine" Case 3: Duty Rating = "Data Center Continuous (DCC)" • If the configuration is saved with initial ("220/380")/other constraint specified("255/440")/reverted to constraint specified voltage values ("220/380", "255/440"): "attributeName":"voltage","cfgStatus":"Default" | type GeneratorSet { @(defaultValue = "Emergency Standby Power (ESP)") string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"]; @(defaultValue = "220/380", domainComputation = false) string voltage = ["220/380", "240/416", "347/600", "255/440", "277/480", "2400/4160", "7200/12470", "7621/13200", "7976/13800"]; constraint(dutyRating == "Continuous Power (COP)" -> voltage != "220/380"); constraint(dutyRating == "Data Center Continuous (DCC)" -> voltage == "255/440" || voltage == "220/380"); } |

=== ARTICLE: cml_annotation_example_guardrails.htm ===
---
page_id: cml_annotation_example_guardrails.htm
title: guardrails Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_guardrails.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# guardrails Annotation

guardrails is a CML annotation that prevent the constraint engine from changing
    specified attributes or relations when it resolves the constraint.

    
      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

- 
- 

      

      

| Annotation | `guardrails` |
| --- | --- |
| Applicable to | Constraint |
| Value Type/Values | String. A comma-separated list of the attribute or relation names to protect. |
| Description | Prevents the constraint engine from altering the listed attributes or relations to satisfy the constraint. Defines protections at the constraint level instead of on individual attributes and relations, which avoids conflicts with other constraints that share the same elements. When you guard an attribute, the engine can't change its domain values. When you guard a relation, the engine can't change its cardinality. |

    

    

## Example 1: Guard an Attribute

      
      

In this generator set model, the UL 2200 compliance constraint requires a secondary voltage
        of 600V or less. The `Voltage` attribute is guarded, so
        the engine can't change its domain values to satisfy the constraint.

      

```
type GeneratorSet : LineItem {
    @(configurable = false)
    int requiredKW = [101..10000];
    string Voltage = ["220/380", "240/416", "277/480", "7976/13800"];
    string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];

    int Voltage3 = strtoint(regexpreplace(Voltage, VOLTAGE_REGEX, "$2"), 0);

    // Guard Voltage so the engine resolves the rule by adjusting the
    // compliance standard, not the domain values of Voltage.
    @(guardrails = "Voltage")
    constraint(standardsAndCompliance == "Listing-UL 2200" -> Voltage3 <= 600,
       "The UL 2200 standard covers stationary engine generator assemblies rated at 600 volts or less.");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 1, the `guardrails` annotation set to
          "`Voltage`". As a result, if the user selects
        the "`Listing-UL 2200`" standard, the engine
        can't change the domain values of the `Voltage`
        attribute to resolve the conflict. Instead, the engine either satisfies the constraint by
        changing an unguarded element, such as `standardsAndCompliance`, or displays a conflict error message. Without the
          `guardrails` annotation, the engine restricts the
        domain values of `Voltage` to satisfy the constraint.

=== ARTICLE: cml_annotation_example_peelable.htm ===
---
page_id: cml_annotation_example_peelable.htm
title: peelable Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_peelable.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# peelable Annotation

The `peelable` annotation is used to create soft
    selection values and allow the engine to modify these selections to satisfy a
    constraint.

    
      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

- 
- 

      

      

| Annotation | `peelable` |
| --- | --- |
| Applicable to | Variable |
| Value Type/Values | true, false |
| Description | Indicates whether the constraint engine can override the variable's value (whether set by default or user selection) to resolve a conflict. If `peelable` annotation is set to `true`, the engine treats the value as a "soft selection." When a configuration conflict occurs, the engine attempts to "peel" (unbind) this variable and retry the solution. If a valid configuration is found, the engine automatically changes the value to satisfy constraints rather than displaying an error message. If `peelable` annotation is set to `false`, the engine treats the value as a "hard selection." If the value causes a conflict with a constraint, the engine will not attempt to change it automatically. Instead, it will stop and display a conflict error message to the user, requiring manual intervention to resolve the issue. |

    

    

## Example 1: peelable = true (Soft Selection)

      
      

In this scenario, the `ServiceLevel` defaults to `"Standard"`. Because it is marked `peelable = true`, the Constraint Engine treats this value as a
        "soft pick." It is authorized to override this value automatically if a conflict
        arises with another selection.

      

```
type CloudSubscription {
    
    // User adds 5TB of storage
    int storageTB = [1..3]; 

    /* 
     * peelable=true: The engine acts as a "negotiator." 
     * If a constraint needs to change this value, the engine is allowed 
     * to "peel" (remove) the user's selection and apply the required value.
     */
    @(defaultValue = "Standard", peelable = true)
    string ServiceLevel = ["Standard", "Premium"];

    // Constraint: 5TB or more requires Premium Service
    constraint(storageTB >= 5 -> ServiceLevel == "Premium", "High storage requires Premium service");
}
```

    

    

## Example 2: peelable = false (Hard Selection)

      
      

In this scenario, `peelable` is omitted (defaulting to
          `false`) or explicitly set to `false`. The engine treats the value `"Standard"` as a "hard constraint" or a
        firm user commitment. It is not authorized to change it automatically.

      

```
type CloudSubscription {
    
    // User adds 5TB of storage
    int storageTB = [1..3]; 

    /* 
     * peelable=false (Default): The engine acts as a "validator."
     * It respects the current value as a hard fact. 
     * It cannot change "Standard" to "Premium" on its own.
     */
    @(defaultValue = "Standard", peelable = false)
    string ServiceLevel = ["Standard", "Premium"];

    // Constraint: 5TB or more requires Premium Service
    constraint(storageTB >= 5 -> ServiceLevel == "Premium", "High storage requires Premium service");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 1, the `ServiceLevel` attribute is specified
        with the `peelable` annotation set to `true`. In example 2, the annotation is not specified, so the
        system considers it as false by default. As a result, if the user updates the `storageTB` variable to 5, the system automatically changes the
          `ServiceLevel` to `"Premium"` in example 1 according to constraint logic, effectively
        "peeling" the default `"Standard"`
        value to resolve the conflict. The system allows this override without displaying an error
        message to the user. In example 2, the system does not allow the engine to override the
        default `"Standard"` value automatically.
        Consequently, the system displays a conflict error message, and the user must manually
        update the `ServiceLevel` to `"Premium"` to satisfy the constraint.

    

    

## Example 3: System-Driven Soft Selection (configurable = false, peelable = true)

      
      

In this example, the `Voltage` is set to a high voltage
        (" `2400/4160`") by default. The annotation
          `configurable = false` prevents the user from manually
        changing this value in the UI. However, `peelable = true`
        is added to allow the constraint engine to override this default if a specific compliance
        standard is selected.

      

```
type GeneratorSet {
    
    string standardsAndCompliance = ["None", "Listing-UL 2200"];

    /* 
     * configurable=false: The user cannot change this directly.
     * peelable=true: The engine is authorized to change the default 
     * to resolve conflicts with the standardsAndCompliance selection.
     */
    @(defaultValue = "2400/4160", configurable = false, peelable = true)
    string Voltage = ["220/380", "277/480", "2400/4160"];

    // Constraint: UL 2200 listing requires a specific low voltage (277/480)
    constraint(standardsAndCompliance == "Listing-UL 2200" -> Voltage == "277/480");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 3, the `Voltage` is specified with
        configurable set to `false`, preventing user interaction,
        but peelable is set to `true`. Initially, the system sets
        the voltage to "`2400/4160`". If the user
        updates the `standardsAndCompliance` variable to
          "`Listing-UL 2200`", the system detects a
        conflict with the default voltage. Because the variable is peelable, the system
        automatically "peels" the default "`2400/4160`" value and changes it to "`277/480`" to satisfy the constraint. The transition happens silently without
        a conflict error, even though the user cannot manually edit the field.

    

    

## Example 4: System-Driven Hard Constraint (configurable = false, peelable = false)

      
      

In this example, the `EmissionsTier` is set to
          "`Tier 3`" by default. It is marked `configurable = false` (system-controlled) and `peelable` is omitted (defaults to false), treating the default
        value as a hard constraint.

      

```
type GeneratorSet {

    string Location = ["US", "International"];

    /*
     * configurable=false: The user cannot change this.
     * peelable=false (Default): The engine treats "Tier 3" as a hard fact.
     */
    @(defaultValue = "Tier 3", configurable = false)
    string EmissionsTier = ["Tier 3", "Tier 4 Final"];

    // Constraint: US Location requires Tier 4 Final
    constraint(Location == "US" -> EmissionsTier == "Tier 4 Final", "US requires Tier 4 Final emissions");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 4, the `EmissionsTier` is specified with
        configurable set to `false`, and `peelable` is not specified (defaulting to `false`). As a result, the system considers the default value
          "`Tier 3`" as a hard constraint that cannot
        be overridden. If the user updates the Location variable to "`US`", the constraint engine attempts to enforce
          "`Tier 4 Final`" but finds it cannot
        overwrite the fixed "`Tier 3`" value.
        Consequently, the system displays a conflict error message stating "`US requires Tier 4 Final emissions`," and the
        configuration enters an invalid state because the user cannot manually change the
        EmissionsTier to resolve it.

    

    

## Example 5: Auto-Correcting User Input (`configurable = true`, `peelable = true`)

      
      

In this example, the ``EnclosureType`` is
        user-selectable (``configurable = true``) and defaults to
        "Standard". It is marked with `peelable = true`. This allows the engine to
        override even an explicit user selection if a subsequent choice makes the enclosure
        invalid.

      

```
type GeneratorAccessories {
    /* 
     * configurable=true: User explicitly selects 'Standard'.
     * peelable=true: Grants permission to override the User's selection 
     * to resolve conflicts with the Environment.
     */
    @(defaultValue = "Standard", configurable = true, peelable = true)
    string EnclosureType = ["Standard", "Heated", "Reinforced"];

    string Environment = ["Indoor", "Arctic"];

    // Constraint: Arctic requires Heated Enclosure
    constraint(Environment == "Arctic" -> EnclosureType == "Heated");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 5, the ``EnclosureType`` is specified with
          ``configurable`` set to ``true`` and ``peelable`` set to ``true``. Initially, the system allows the user to confirm the
        selection of "`Standard`". If the user
        subsequently updates the ``Environment`` variable to
          "`Arctic`", the system detects that
          "`Standard`" is invalid. Typically, the
        engine protects user selections and would throw an error. However, because ``EnclosureType`` is peelable, the system treats the user's
        choice as a "soft pick." It automatically "peels" the "`Standard`" selection and changes it to "`Heated`" to satisfy the logic. The user sees their
        previous selection update automatically to match the new environment requirement, preventing
        a "dead end" configuration state.

    

    

## Example 6: Upstream Correction (`sequence`, `peelable = true`)

      
      

In this example, the ``Voltage`` is configured early in
        the process (Sequence 1) with a default value of "`Low`". It is marked with ``peelable =
          true`` to allow downstream selections to override this initial setting.

      

```
type GeneratorSet {
    /* 
     * sequence=1: Evaluated first. Defaults to 'Low'.
     * peelable=true: Allows 'Application' (seq=2) to force a change to this value.
     */
    @(defaultValue = "Low", sequence = 1, peelable = true)
    string Voltage = ["Low", "Medium", "High"];

    /* 
     * sequence=2: Evaluated after Voltage is set.
     * The user picks 'DataCenter', which requires High Voltage.
     */
    @(sequence = 2)
    string Application = ["Residential", "DataCenter"];

    // Constraint: DataCenter application forces High Voltage
    constraint(Application == "DataCenter" -> Voltage == "High");
}
```

    

    

## Example Description and Configurator Result

      
      

In example 6, the ``Voltage`` attribute is specified
        with ``sequence`` set to `1` and ``peelable`` set to ``true``. As a result, the system initially sets the value to
          "`Low`" before evaluating the ``Application`` attribute. If the user updates the ``Application`` variable to "`DataCenter`" (which runs at sequence 2), the system detects a conflict
        between the established "`Low`" voltage and the
        constraint requirement for "`High`" voltage.
        Because ``Voltage`` is peelable, the system automatically
        "peels" the default "`Low`" value and
        changes it to "`High`" to satisfy the
        constraint. The transition happens silently without a conflict error, effectively allowing a
        later user choice to correct an earlier default assumption.

    

    

## Example 7: Guided Fallback (‘strategy`, `peelable = true`)

      
      

In this example, the ``ServiceTier`` defaults to
          "`Bronze`" (the lowest value). It is marked
        with ``peelable = true`` and ``strategy = "descending`"`. If a constraint forces a change from the
        default, the strategy directs the engine to try the highest possible valid values first.

      

```
type ServicePlan {
    /* 
     * defaultValue="Bronze": Start cheap.
     * peelable=true: Allow upgrade if needed.
     * strategy="descending": If peeled, try 'Platinum' next (Max value), 
     * instead of creeping up to 'Silver'.
     */
    @(defaultValue = "Bronze", strategy = "descending", peelable = true)
    string ServiceTier = ["Bronze", "Silver", "Gold", "Platinum"];

    int UserCount = [1..1000];

    // Constraint: > 100 users requires Premium tiers (Gold or Platinum)
    constraint(UserCount > 100 -> ServiceTier in ["Gold", "Platinum"]);
}
```

    

    

## Example Description and Configurator Result

      
      

In example 7, the ``ServiceTier`` is specified with
          ``strategy`` set to "`descending`" and ``peelable`` set to
          ``true``. Initially, the system sets the value to
          "`Bronze`". If the user updates the ``UserCount`` variable to 150, the constraint requires ``ServiceTier`` to be either "`Gold`" or "`Platinum`". Because
        the variable is peelable, the system removes the "`Bronze`" selection. Instead of testing the next closest value ("`Silver`"), the "`descending`" strategy instructs the engine to attempt resolution starting
        from the top of the domain. Consequently, the system automatically selects "`Platinum`" (the highest valid option) rather than
          "`Gold`". The user sees the plan upgrade
        immediately to the highest tier without an error message.

=== ARTICLE: cml_annotation_example_productField.htm ===
---
page_id: cml_annotation_example_productField.htm
title: productField Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_productField.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# productField Annotation

productField is a CML annotation that defines the Product2 field on a variable.
  productField loads the value from Product Catalog Management (PCM) during constraint model
  activation.

  
   

     
     
     
      
       

       

      

     

     
      
       

       

      

      
       

       

      

      
       

       

      

     

    
| Annotation | `productfield` |
| --- | --- |
| Applicable to | Variable |
| Value Type/Values | Literal (case sensitive) |
| Description | Used to load the value from the corresponding Product2 field defined in Product Catalog Management(PCM). Defined under either a type or supertype. If defined under a supertype, the types, which inherit from the supertype, load the Product2 field value for the corresponding product. Supports a maximum of 50 Product2 fields. Loads product field values for a maximum of 20,000 products. Read-only. Doesn't support a null value. |

  

  

## Example 1

In this example, `RatedPowerOutput__c` is a custom field defined on the Product2 object. The constraint
    rules engine loads the value of `RatedPowerOutput__c` for the
    GeneratorSet product during constraint model
    activation.

```
type GeneratorSet {
    @(productField = "RatedPowerOutput__c")
    int ratedPowerOutput;
}
```

  

## Example 2

In this example, the product field variable `productName` is defined under a supertype `EquipmentItem`. Any type that inherits the supertype loads the
    value of `Name` for the corresponding product during
    constraint model
    activation.

```
type EquipmentItem {
    @(productField = "Name")
    string productName;
}

type GeneratorSet : EquipmentItem;
type GeneralModel : EquipmentItem;
```

  

## Example 3

In this example, the product field variable `productCode` is defined under the parent type `GeneratorSet`. `GeneralModel`
    is a child of `GeneratorSet`, and it can access the `productCode` variable from its parent by using the `parent()`
    function.

```
type GeneratorSet {
    @(productField = "ProductCode")
    string productCode;

    relation generalModels : GeneralModel[1..999999];
}

type GeneralModel {
    string parentProductCode = parent(productCode);
}
```

=== ARTICLE: cml_annotation_example_propagateUp.htm ===
---
page_id: cml_annotation_example_propagateUp.htm
title: propagateUp Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_propagateUp.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# propagateUp Annotation

`propagateUp` is a Constraint Modeling Language
    (CML) annotation that controls aggregation propagation between children and parent
    elements.

    
      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

- 
- 

      

      

| Annotation | `propagateUp` |
| --- | --- |
| Applicable to | Relationship |
| Value Type/Values | true, false |
| Description | If propagateUp is not specified, the engine sets it implicitly as false for the relationship. If the propagateUp annotation is specified as true, the engine aggregates values from children to parent elements (upward propagation). The engine cannot modify this value from the parent level (e.g. via constraint), so the children relation domain will not be affected. If the propagateUp is specified as false, both upward and downward propagations are applicable. The engine aggregates values from children to parent elements (upward propagation). Meanwhile the engine can modify this value (e.g. via constraint) from the parent level. The value is propagated downward and might affect the relation domain (downward propagation). |

    

    

## Example 1

In this example, the `propagateUp` annotation is not specified for the relationship (`warranties`). The model contains technical variable (`coverageDays`) and
      constraint.

```
type GeneratorSet {

        relation warranties : Warranty {
        totalDays = sum(coverageDays);
    }
    constraint(warranties.totalDays <= 299);
}

type Warranty {
    int coverageDays = 100;
}

type Warranty_PRP : Warranty;

type Warranty_DCC : Warranty;

type Warranty_ESP : Warranty;

```

    

## Example 2

In this example, the `propagateUp` annotation is defined as `false`
        for the relationship (`warranties`). The model contains
        technical variable (coverageDays) and
      constraint.

```
type GeneratorSet {

        @(propagateUp = false)
        relation warranties : Warranty {
        totalDays = sum(coverageDays);
    }
    constraint(warranties.totalDays <= 299);
}

type Warranty {
    int coverageDays = 100;
}

type Warranty_PRP : Warranty;

type Warranty_DCC : Warranty;

type Warranty_ESP : Warranty;
```

    

## Example Description and Configurator Result

      
      

In example 1, the `warranties` relation is not specified
        with the propagateUp annotation, and the system considers it as `false` by default. In example 2, the relation is explicitly defined with a
          `false` annotation value. Each product of the `warranties` relation is assigned with the technical `coverageDays` variable equalled to 100. The `totalDays` calculates the `coverageDays` sum of selected `warranties`
        products. As a result, the system validates the constraint and relation domain in the
        following way:

      

- The user selects one `warranties` product (e.g. `Warranty_PRP`). The system calculates the `totalDays` aggregated value for the relation (equal to 100).
          The system validates the constraint on the parent based on the calculated aggregation
          variable. The constraint is satisfied (100<= 299). The system also verifies the
          possibility to add extra products to the relation. The capacity of the constraint allows
          to add one more product to the relation, so the system will not reduce the relation
          domain.

- The user selects the second `warranties` product (e.g.
            `Warranty_DCC`). The system calculates the `totalDays` aggregated value for the relation (equal to 200).
          The system validates the constraint on the parent based on the calculated aggregation
          variable. The constraint is satisfied (200<= 299). The system verifies the possibility
          to add extra products to the relation. The capacity of the constraint (300<= 299) does
          not allow to add one more product to the relation, so the system will reduce the relation
          domain.

- The user unselects one of the selected `warranties` products
          (e.g. `Warranty_PRP`). The system calculates the
            `totalDays` aggregated value for the relation (equal
          to 100). The system validates the constraint on the parent based on the calculated
          aggregation variable. The constraint is satisfied (100<= 299). The system verifies the
          possibility to add extra products to the relation. The capacity of the constraint allows
          to add one more product to the relation, so the system will not reduce the relation domain
          (both `Warranty_DCC` and `Warranty_ESP` products are available for selection).

    

    

## Example 3

In this example, the `propagateUp` annotation is specified for the relationship (`warranties`) as `true`. The
        model contains technical variable (`coverageDays`) and
        constraint.

```
type GeneratorSet {

        @(propagateUp = true)
        relation warranties : Warranty {
        totalDays = sum(coverageDays);
    }
    constraint(warranties.totalDays <= 299);
}

type Warranty {
    int coverageDays = 100;
}

type Warranty_PRP : Warranty;

type Warranty_DCC : Warranty;

type Warranty_ESP : Warranty;
```

    

## Example Description and Configurator Result

      
      

In example 3, the relation is specified with `propagateUp` annotation as `true` value. Each
        product of the `warranties` relation is assigned with the
        technical `coverageDays` variable equalled to 100. The
          `totalDays` calculates the `coverageDays` sum of selected `warranties`
        products. As a result, the system validates the constraint and relation domain in the
        following way:

      

The user selects one `warranties` product (e.g. `Warranty_PRP`). The system calculates the `totalDays` aggregated value for the relation (equal to 100).
        The system validates the constraint on the parent based on the calculated aggregation
        variable. The constraint is satisfied (100<=299);

      

The user selects the second `warranties` product (e.g.
          `Warranty_DCC`). The system calculates the `totalDays` aggregated value for the relation (equal to 200).
        The system validates the constraint on the parent based on the calculated aggregation
        variable. The constraint is satisfied (200<=299);

      

The user selects the third `warranties` product (e.g.
          `Warranty_ESP`). The system calculates the `totalDays` aggregated value for the relation (equal to 300).
        The system validates the constraint on the parent based on the calculated aggregation
        variable. The constraint is not satisfied (300<=299). The system rejects the selection of
        one of the warranties products to satisfy the constraint.

      

As a best practice, use the `propagateUp = true` for
        models with few relationships and rare constraint violations, since it minimizes propagation
        work and avoids extra domain updates. Meanwhile, set the `propagateUp = false` for large product structures or frequent violations, since
        bidirectional propagation prevents invalid states early and reduces expensive
        backtracking.

    

    

## propagateUp Configuration Settings

      
      

Table 1. propagateUp Configuration Settings
          
          
          
          
          
          
          
          
            
              

              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

          

        
| Associated Example | Product Group Structure | Applicable to | "propagateUp" annotation | User Action | Engine Action | UI Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Example 1 | Individual product | Relationship | not specified | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint, limitation of the relation domain when the constraint capacity is used up | Displays the selected products. When constraint capacity is used up, in addition to the selected products the limited list of the available to be added products will be displayed(if any) |
| Example 2 | Individual product | Relationship | FALSE | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint, limitation of the relation domain when the constraint capacity is used up | Displays the selected products. When constraint capacity is used up, in addition to the selected products the limited list of the available to be added products will be displayed(if any) |
| Example 3 | Individual product | Relationship | TRUE | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint, rejection of the user selection when the constraint validation is failed | Displays the selected products. No limitations for the list of available products |
| N/A | Product Classification | Relationship | not specified | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint. The engine might replace one of the previously selected products with a newly selected | Displays the selected products. No limitations for the list of available products in the browse popup for the classification |
| N/A | Product Classification | Relationship | FALSE | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint. The engine might replace one of the previously selected products with a newly selected | Displays the selected products. No limitations for the list of available products in the browse popup for the classification |
| N/A | Product Classification | Relationship | TRUE | Selects or deselects the products | Calculates the aggregation variable value on the relation, validation of the constraint, rejection of the user selection when the constraint validation is failed | Displays the selected products. No limitations for the list of available products in the browse popup for the classification |

=== ARTICLE: cml_annotation_example_relatedAttributes.htm ===
---
page_id: cml_annotation_example_relatedAttributes.htm
title: relatedAttributes Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_relatedAttributes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# relatedAttributes Annotation

`relatedAttributes` is a Constraint Modeling
    Language (CML) annotation that resets the domain to the original one for
    domainComputation.

    
      

`relatedAttributes` annotation specification:
        Variable

      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `relatedAttributes` |
| --- | --- |
| Applicable to | Variable and Relationship |
| Value Type/Values | String |
| Description | For Variables If `relatedAttributes` annotation is not specified, the engine updates the variable domain according to domainComputation and constraint logic. If the `relatedAttributes` annotation is specified with one or multiple values (separated by comma), the variable domain is reset to the original domain. For relationships If `domainComputation` is not explicitly specified, the engine sets it implicitly as true for the relationship. If the `domainComputation` is specified as `true`, the relationship domain is dynamically determined based on the configuration and constraint logic. If the `domainComputation` is specified as `false`, the relationship domain is fixed. |

    

    

## Example 1

In this example, the `relatedAttributes` annotation is not specified for the variables (`controlLanguage`, `controlPlacement`, `commissioningScope`) of
        the `Control` type. The `domainComputation` annotation is defined for the variables. The model contains
        the constraints.

```
type GeneratorSet {
    relation controls : Control;
}

type Control {
    @(domainComputation = true, defaultValue = "English")
    string controlLanguage = ["English", "Danish", "French"];

    @(domainComputation = true, defaultValue = "Left")
    string controlPlacement = ["Left", "Right", "Top"];

    @(domainComputation = true, defaultValue = "None")
    string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

    constraint(controlPlacement == "Right" -> commissioningScope != "Remote Support");

    constraint(controlLanguage == "Danish" -> commissioningScope != "On-site Commissioning");

```

    

## Example Description and Configurator Result

      
      

In example 1, the variables of the `Control` type are
        not specified with the `relatedAttributes` annotation,
        but defined with the `domainComputation` annotation. As a
        result, the system updates the variable domain based on the constraint logic.

      

If the `controlPlacement` is selected with the
          "`Right`" value, the `commissioningScope` variable domain is updated to exclude the
          "`Remote Support`" value;

      

If the `controlLanguage` is selected with the “`Danish`" value, the `commissioningScope` variable domain is updated to exclude the "`On-site Commissioning`" value.

    

    

## Example 2

In this example, the `relatedAttributes` annotation is specified for the variable with one value. The
          `domainComputation` annotation is defined for the
        variables. The model contains the
      constraints.

```
type GeneratorSet {
    relation controls : Control;
}

type Control {
    @(domainComputation = true, defaultValue = "English")
    string controlLanguage = ["English", "Danish", "French"];

    @(domainComputation = true, defaultValue = "Left")
    string controlPlacement = ["Left", "Right", "Top"];

     @(domainComputation = true, defaultValue = "None", relatedAttributes = "controlPlacement")
    string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

    constraint(controlPlacement == "Right" -> commissioningScope != "Remote Support");

    constraint(controlLanguage == "Danish" -> commissioningScope != "On-site Commissioning");
}
```

    

## Example 3

In this example, the `relatedAttributes` annotation is specified for the variable with one value. The
          `domainComputation` annotation is defined for the
        variables. The model contains the
      constraints.

```
type GeneratorSet {
    relation controls : Control;
}

type Control {
    @(domainComputation = true, defaultValue = "English")
    string controlLanguage = ["English", "Danish", "French"];

    @(domainComputation = true, defaultValue = "Left")
    string controlPlacement = ["Left", "Right", "Top"];

    @(domainComputation = true, defaultValue = "None", relatedAttributes = "controlLanguage")
    string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

    constraint(controlPlacement == "Right" -> commissioningScope != "Remote Support");

    constraint(controlLanguage == "Danish" -> commissioningScope != "On-site Commissioning");
}
```

    

## Example Description and Configurator Result

      
      

In Example 2, the `relatedAttributes` annotation is
        defined with the "`controlPlacement`" value for
        the `commissioningScope` variable. As a result, the
        system controls the domain for the `commissioningScope`
        differently depending on `controlPlacement` or `controlLanguage` variable selection.

      

If the `controlPlacement` is selected with the
          "`Right`" value, the `commissioningScope` variable domain remains unchanged, because
        the `controlPlacement` is listed in the `relatedAttributes` annotation.

      

If the controlLanguage is selected with the “`Danish`" value, the `commissioningScope`
        variable domain is updated to exclude the "`On-site
          Commissioning`" value according to the constraint, because the `controlLanguage` is not listed in the `relatedAttributes` annotation.

      

In example 3, the `relatedAttributes` annotation is
        defined with the "`controlLanguage`" value for
        the `commissioningScope` variable. As a result, the
        system controls the domain for the `commissioningScope`
        differently depending on `controlPlacement` or `controlLanguage` variable selection.

      

If the `controlPlacement` is selected with the
          "`Right`" value, the `commissioningScope` variable domain is updated to exclude the
          "`Remote` Support" value according to the
        constraint, because the `controlPlacement` is not listed
        in the `relatedAttributes` annotation.

      

If the `controlLanguage` is selected with the
          "`Danish`" value, the `commissioningScope` variable domain remains unchanged, because
        the `controlLanguage` is listed in the `relatedAttributes` annotation.

    

    

## Example 4

In this example, the `relatedAttributes` annotation is specified for the variable with several values
        (separated by comma). The domainComputation annotation is defined for the variables. The
        model contains the
      constraints.

```
type GeneratorSet {
    relation controls : Control;
}

type Control {
    @(domainComputation = true, defaultValue = "English")
    string controlLanguage = ["English", "Danish", "French"];

    @(domainComputation = true, defaultValue = "Left")
    string controlPlacement = ["Left", "Right", "Top"];

    @(domainComputation = true, defaultValue = "None", relatedAttributes = "controlPlacement, controlLanguage")
    string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

    constraint(controlPlacement == "Right" -> commissioningScope != "Remote Support");

    constraint(controlLanguage == "Danish" -> commissioningScope != "On-site Commissioning");
}
```

    

## Example Description and Configurator Result

      
      

In example 4, the `relatedAttributes` annotation is
        defined with the "`controlPlacement`" and
          "`controlLanguage`" values for the
        commissioningScope variable. As a result, the system remains the `commissioningScope` variable domain unchanged.

      

If the `controlPlacement` is selected with the
          "`Right`" value, the `commissioningScope` variable domain remains unchanged, because
        the `controlPlacement` is listed in the `relatedAttributes` annotation.

      

If the controlLanguage is selected with the "`Danish`" value, the `commissioningScope`
        variable domain remains unchanged, because the `controlLanguage` is listed in the `relatedAttributes` annotation.

    

    

## Example 5

In this example, the `relatedAttributes` annotation is not specified for the relationship (`temperatureSensors`). The `domainComputation` annotation is defined for the relationship. The model contains
        the constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    
    @(domainComputation = true)
    relation temperatureSensors : TemperatureSensor[0..1];

    constraint(dutyRating == "Continuous Power (COP)" -> temperatureSensors[BearingTemperatureSensor] == 0);

    constraint(dutyRating == "Data Center Continuous (DCC)" -> temperatureSensors[StatorTemperatureSensor] == 0);
}

type TemperatureSensor;

type BearingTemperatureSensor : TemperatureSensor;

type StatorTemperatureSensor : TemperatureSensor;
```

    

## Example Description and Configurator Result

      
      

In example 5, the `temperatureSensors` relation is not
        specified with the `relatedAttributes` annotation, but
        defined with the `domainComputation` as true. As a
        result, the system updates the relationship domain based on the constraint logic.

      

If the `dutyRating` is selected with the "`Continuous Power (COP)`" value, the system re-computes
        the relationship domain and excludes the `BearingTemperatureSensor` product to satisfy the constraint. The `StatorTemperatureSensor` product remains and can be selected
        in scope of the `GeneratorSet` bundle product.

      

If the `dutyRating` is selected with the "`Data Center Continuous (DCC)`" value, the system
        re-computes the relationship domain and excludes the `StatorTemperatureSensor` product to satisfy the constraint. The `BearingTemperatureSensor` product remains and can be selected
        in scope of the `GeneratorSet` bundle product.

    

    

## Example 6

In this example, the `relatedAttributes` annotation is specified for the relationship (`temperatureSensors`). The `domainComputation` annotation is defined for the relationship. The model contains
        the constraints.

```
type GeneratorSet {
    @(defaultValue = "Emergency Standby Power (ESP)")
    string dutyRating = ["Emergency Standby Power (ESP)", "Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)"];
    
    @(domainComputation = true, relatedAttributes = 'dutyRating')
    relation temperatureSensors : TemperatureSensor[0..1];

    constraint(dutyRating == "Continuous Power (COP)" -> temperatureSensors[BearingTemperatureSensor] == 0);

    constraint(dutyRating == "Data Center Continuous (DCC)" -> temperatureSensors[StatorTemperatureSensor] == 0);
}

type TemperatureSensor;

type BearingTemperatureSensor : TemperatureSensor;

type StatorTemperatureSensor : TemperatureSensor;
```

    

## Example Description and Configurator Result

      
      

In example 6, the `temperatureSensors` relation is
        specified with the `relatedAttributes` annotation
        containing the `dutyRating` value, the `domainComputation` annotation is defined as `true`. As a result, the system remains the relationship domain
        unchanged and executes the constraints.

      

If the `dutyRating` is selected with the "`Continuous Power (COP)`" value, the system displays both
          `BearingTemperatureSensor` and `StatorTemperatureSensor` products in scope of the `GeneratorSet` bundle product. The `BearingTemperatureSensor` product cannot be selected based on the constraint.

      

If the `dutyRating` is selected with the “`Data Center Continuous (DCC)`" value, the system displays
        both `BearingTemperatureSensor` and `StatorTemperatureSensor` products in scope of the `GeneratorSet` bundle product. The `StatorTemperatureSensor` product cannot be selected based on the constraint.

    

    

## relatedAttributes Configuration Settings

      
      

Table 1. relatedAttributes Configuration Settings
          
          
          
          
          
          
          
          
          
            
              

              

              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

            

          

        
| Associated Example | Product Group Structure | Applicable to | "relatedAttributes" annotation | "domainComputation" annotation | User Action | Engine Action | UI Behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Example 1 | Individual product | Variable | not specified | TRUE | Change variable value specified in constraint condition | Update the variable (specified with domainComputation) domain based on domainComputation and constraint logic | Display updated variable domain |
| Example 2 Example 3 | Individual product | Variable | specified (with one variable) | TRUE | Change variable value specified in constraint condition and relatedAttributes | Reset variable (specified in relatedAttributes) domain to the original domain | Display original variable domain |
| Example 4 | Individual product | Variable | specified (with several variables) | TRUE | Change variable values specified in constraint conditions and relatedAttributes | Reset variable (specified in relatedAttributes) domain to the original domain | Display original variable domain |
| Example 5 | Individual product | Relationship | not specified | TRUE | Change variable value specified in constraint condition | Update the relationship (specified with domainComputation) domain based on domainComputation and constraint logic | Display updated relationship domain |
| Example 6 | Individual product | Relationship | specified | TRUE | Change variable value specified in constraint condition and relatedAttributes | Reset relationship domain to the original domain | Display original relationship domain (products). If the product is allowed according to constraint: the product can be selected If the product is not allowed according to constraint: selected product returns back to unselected state |
| N/A | Product Classification | Relationship | not specified | TRUE | • Change variable value specified in constraint condition > Add products on browse popup from product classification • Add products on browse popup from product classification > Change variable value specified in constraint condition | Update the relationship (specified with domainComputation) domain based on domainComputation and constraint logic | Display updated relationship domain. If the variable is changed again by the User, the value is reverted to the initial value |
| N/A | Product Classification | Relationship | specified | TRUE | • Change variable value specified in constraint condition > Add products on browse popup from product classification •Add products on browse popup from product classification > Change variable value specified in constraint condition | • If the variable of constraint condition is changed first: update the relationship (specified with domainComputation) domain based on constraint logic • if products are added first from browse popup: remain the relationship domain unchanged | • If the variable of constraint condition is changed first: display updated relationship domain. If the variable is changed again by the user, the value is reverted to the initial value • if products are added first from browse popup: display added products as selected. If constraint variable is changed again by the user, the value is reverted to the initial value |

=== ARTICLE: cml_annotation_example_sequence.htm ===
---
page_id: cml_annotation_example_sequence.htm
title: sequence Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_sequence.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# sequence Annotation

The `sequence` annotation defines the execution and
    configuration order of elements in a Constraint Modeling Language (CML) model.

    
      

`sequence` annotation specification: Variable and
        Relationship

      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `sequence` |
| --- | --- |
| Applicable to | Variable and Relationship |
| Value Type/Values | integer Example: 1, 2, 10 |
| Description | If a sequence value is not explicitly defined, the configurator implicitly determines the order based on the variable or relationship declaration order in the CML model. If a sequence value is explicitly defined, the configurator uses the sequence number to control the order in which variables or relationships are configured. Variables or Relationships with lower sequence values are assigned first. |

    

    

## Example 1

In this example, the `sequence` annotation is not explicitly specified. The `defaultValue` is defined for 3 variables (`controlPlacement`, `commissioningScope`, and
          `controlLanguage`) of the `Control` products. The model contains a
      constraint.

```
type GeneratorSet {
    relation controls : Control[1..999999];
}

type Control {
	@(defaultValue = "Left")
	string controlPlacement = ["Left", "Right", "Top"];

	@(defaultValue = "None")
	string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

	@(defaultValue = "English")
	string controlLanguage = ["English", "Danish", "French"];

	constraint(controlPlacement == "Left" && controlLanguage == "English" -> commissioningScope == "Remote Support");
}
```

    

## Example Description and Configurator Result

      
      

The model defines 3 variables with `defaultValue`
        annotation.

      

```
controlPlacement = "Left"
commissioningScope = "None"
controlLanguage = "English"

```

      

Even when sequence is not explicitly specified for the variables, the engine assigns it implicitly based on the variable declaration order in the CML type. For this example, the sequence for the variables is:

      

```
controlPlacement: sequence = 1 (highest priority)
commissioningScope: sequence = 2
controlLanguage: sequence = 3 (lowest priority)

```

      

The constraint specifies that a type with `controlPlacement ==
          "Left"` and `controlLanguage ==
          "English"` will have a `commissioningScope ==
          "Remote Support":`.

      

```
constraint(controlPlacement == "Left" && controlLanguage == "English" -> commissioningScope == "Remote Support");
```

      

For any constraint, the engine enforces logical equivalence between the left-hand side
        (before ->) and the right-hand side (after ->): if the left side evaluates to true,
        the right side must also be true (and vice versa).

      

In this example, the engine resolves the true -> false constraint (to be false -> false): it modifies the controlLanguage with the highest sequence.

      

As a result, the Product Configurator will have next values for the variables:

      

```
controlPlacement = "Left"
commissioningScope = "None"
controlLanguage = "Danish"

```

    

    

## Example 2

In this example, the `sequence` annotation is explicitly specified and the defaultValue is defined for
        3 variables (`controlPlacement`, `controlLanguage`, `commissioningScope`) of the `Control`
        products. The model contains a
      constraint.

```
type GeneratorSet {
    relation controls : Control[1..999999];
}

type Control{

@(defaultValue = "Left", sequence = 1)
string controlPlacement = ["Left", "Right", "Top"];

@(defaultValue = "English", sequence = 3)
string controlLanguage = ["English", "Danish", "French"];

@(defaultValue = "None", sequence = 2)
string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

constraint(controlPlacement == "Left" && controlLanguage == "English" -> commissioningScope == "Remote Support");
}
```

    

## Example Description and Configurator Result

      
      

This example is similar to Example 1, but the `sequence`
        annotation is specified explicitly for the variables to control solver priority:

      

```
controlPlacement: sequence = 1 (highest priority)
controlLanguage: sequence = 3 (lowest priority)
commissioningScope: sequence = 2

```

      

The constraint specifies that a type with `controlPlacement ==
          "Left"` and `controlLanguage ==
          "English"` will have a `commissioningScope ==
          "Remote Support":`.

      

```
constraint(controlPlacement == "Left" && controlLanguage == "English" -> commissioningScope == "Remote Support");
```

      

- Following the same logical equivalence for constraints described in Example 1 and considering
          the default values specified in the Example 2, the left side of the constraint is true
            (`controlPlacement = "Left"` and `controlLanguage = "English"`), while the right
          side is false (`commissioningScope =
          "None"`).

- Because the `commissioningScope` has higher priority than the
            `controlLanguage`, the engine avoids changing the
            `commissioningScope` and instead resolves the
          constraint by making the left side false.

- The `controlPlacement` has the highest priority sequence than
          the `controlLanguage`, so the engine modifies the
          controlLanguage as the most efficient way to satisfy the constraint.

      

Available values for the `controlLanguage: ["English",
          "Danish", "French"]`. To make the left side of the constraint
        false, the engine selects the first non-matching value (specified in CML domain): `"Danish"`.

      

As a result, the Product Configurator will have next values for the variables.

      

```
controlPlacement = "Left"
controlLanguage = "Danish"
commissioningScope = "None"

```

    

    

## Example 3

In this example, the `sequence` annotation is explicitly specified and the defaultValue is defined for
        3 variables (`controlPlacement`, `controlLanguage`, and `commissioningScope`) of the `Control`
        products. The model contains a
      constraint.

```
type GeneratorSet {
    relation controls : Control[1..999999];
}

type Control{
    
@(defaultValue = "Left", sequence = 1)
string controlPlacement = ["Left", "Right", "Top"];

@(defaultValue = "English", sequence = 2)
string controlLanguage = ["English", "Danish", "French"];

@(defaultValue = "None", sequence = 3)
string commissioningScope = ["None", "Remote Support", "On-site Commissioning"];

constraint(controlPlacement == "Left" && controlLanguage == "English" -> commissioningScope == "Remote Support");
}
```

    

## Example Description and Configurator Result

      
      

This example is similar to Example 2, but the lowest priority sequence is specified for the
          `commissioningScope`. This is a trigger for the engine
        to modify the `commissioningScope` first to resolve the
        true -> false constraint to be true -> true).

      

As a result, the Product Configurator will have next values for the variables:

      

```
controlPlacement = "Left"
controlLanguage = "English"
commissioningScope = "Remote Support"
```

    

    

## Example 4

In this example, the sequence annotation is not explicitly
        specified for 3 relations (`voltageConnections`, `controls`, and  `alternators`). The model contains a
      constraint.

```
type GeneratorSet {
    relation voltageConnections : VoltageConnection[0..999999];
    relation controls : Control[1..999999];
    relation alternators : Alternator[1..999999];

    int alternatorsQty = controls[Control] + voltageConnections[VoltageConnection];
    constraint(alternators[Alternator] > 0 -> alternators[Alternator] == alternatorsQty, "alternators[Alternator] = controls[Control] + voltageConnections[VoltageConnection]");
}

type Alternator;

type VoltageConnection;

type Control;
```

    

## Example Description and Configurator Result

      
      

Even when sequence is not explicitly specified for the relations, the engine sets it implicitly based on the relation declaration order in the CML type. For this example, the sequence for the relations is:

      

```
relation voltageConnections: sequence = 1 (highest priority)
relation controls: sequence = 2
relation alternators: sequence = 3 (lowest priority)
```

      

#### Note

Use mindful sequencing in CML for variables and relations to avoid
        backtracking issues. Define them in the order you expect the engine to modify them during
        constraint resolution.

      

In this example, the CML model works without conflicts because the relations are implicitly
        defined with the correct sequence. The `voltageConnections` and controls relations are evaluated first, then the `alternatorsQty` is calculated from their quantities. Finally,
        the `alternators` relation is adjusted based on that
        result. Because the `alternators` is processed last, the
        engine avoids backtracking and errors.

    

    

## Example 5

In this example, the `sequence` annotation is explicitly specified for 3 relations (`voltageConnections`, `controls`, and `alternators`). The model
        contains a constraint.

```
type GeneratorSet {
	@(sequence=3)
    relation alternators : Alternator[1..999999];
    @(sequence=1)
    relation voltageConnections : VoltageConnection[0..999999];
	@(sequence=2)
    relation controls : Control[1..999999];

    int alternatorsQty = controls[Control] + voltageConnections[VoltageConnection];
    constraint(alternators[Alternator] > 0 -> alternators[Alternator] == alternatorsQty, "alternators[Alternator] = controls[Control] + voltageConnections[VoltageConnection]");
}
type Alternator;

type VoltageConnection;

type Control;
```

    

## Example Description and Configurator Result

      
      

This example is similar to Example 4, but the `sequence`
        is explicitly specified for the relations to control the processing priority and ensure the
        engine evaluates and modifies them in the correct order during configuration.

    

    

## sequence Configuration Settings

      
      

Table 1. sequence Configuration Settings
          
          
          
          
          
          
          
          
            
              

              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

            

          

        
| Associated Example | Product Group Structure | Applicable to | "sequence" annotation | User Action | Engine Action | UI Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Example 1 | N/A | Variable | not specified | Configure the product containing variables | Assign the sequence for the variables based on the variable declaration order in the type. Enforce logical equivalence between left-hand side and right-hand side for the constraint by modifying the variable with the highest sequence | Display appropriate variable values based on sequence and constraint logic |
| Example 2 Example 3 | N/A | Variable | specified | Configure the product containing variables | Assign the sequence for the variables based on defined sequence annotation. Enforce logical equivalence between left-hand side and right-hand side for the constraint by modifying the variable with the highest sequence | Display appropriate variable values based on sequence and constraint logic |
| Example 4 | Individual product | Relationship | not specified | Configure the bundle product containing relationship products | Assign the sequence for the relationships based on the relation declaration order in the type. Execute the constraint (according to assigned sequence) | Display adjusted relationships based on the relationship sequence and constraint logic |
| Example 5 | Individual Product | Relationship | specified | Configure the bundle product containing relationship products | Assign the sequence for the relationships based on defined sequence annotation. Execute the constraint (according to specified sequence) | Display adjusted relationships based on the relationship sequence and constraint logic |
| N/A | Product Classification | Relationship | not specified | Configure the bundle product containing relationship products | Assign the sequence for the relationships based on the relation declaration order in the type. Execute the constraint (according to assigned sequence) | Display adjusted relationships based on the relationship sequence and constraint logic |
| N/A | Product Classification | Relationship | specified | Configure the bundle product containing relationship products | Assign the sequence for the relationships based on defined sequence annotation. Execute the constraint (according to specified sequence) | Display adjusted relationships based on the relationship sequence and constraint logic |

=== ARTICLE: cml_annotation_example_split.htm ===
---
page_id: cml_annotation_example_split.htm
title: split Annotation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_example_split.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_annotation_examples.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# split Annotation

`split` is a Constraint Modeling Language (CML)
    annotation that specifies whether the instances of the type should be split or not.

    
      

      
      
      

      

      

      

      
      

      

      

      
      

      

      

      
      

      

      

      

| Annotation | `split` |
| --- | --- |
| Applicable to | Type |
| Value Type/Values | true, false |
| Description | If split isn’t specified, there are multiple instances of the same type in the relationship with different quantities. If the split is specified as `true`, there can be multiple instances of the type, and the quantity of each instance is always 1. If the split is specified as `false`, there is only one instance in the relationship. If the user adds more instances, the engine adds more quantity to the existing instance. |

    

    

## Example 1

In this example, the split annotation isn’t specified for the type (Model).

```
type FESBAGeneratorSet {
    relation models : Model;
}
type Model;
```

    

## Example Description and Configurator Result

      
      

In this example, the system allows the multiple instances of the Model type with different quantities defined by the user.

    

    

## Example 2

In this example, the split annotation is specified as
          `true` for the type
      (Model).

```
type FESBAGeneratorSet {
    relation models : Model;
}
@(split = true)
type Model;
```

    

## Example Description and Configurator Result

      
      

In this example, the annotation `split = true` specifies
        that the multiple Model instances are split into individual items with fixed quantity 1.

    

    

## Example 3

In this example, the split annotation is specified as
          `false` for the type
        (Model).

```
type FESBAGeneratorSet {
    relation models : Model;
}
@(split = false)
type Model;
```

Use `@(split=false)` when the
        line item record must persist across configuration changes and record continuity matters for
        your business process. The `@(split=false)` annotation
        prevents the configurator from deleting and recreating existing line item records when the
        quantity or selection changes. When you apply `@(split=false)`, the configurator updates the quantity on the existing record
        instead of replacing it with a new one. This preserves the record ID and any data associated
        with it.

    

## Example Description and Configurator Result

      
      

In this example, the system allows one instance of the Model type with different quantity defined by the user.

      

#### Note

If there are multiple products of type Model (for example, `FESBA 900kW` and `FESBA
          1500kW`), the user can add both models to the configuration and adjust the
        quantity for each one. However, the user can’t add additional separate instances of the same
        product (for example, to configure unique instances with different variable values).

    

    

## split Configuration Settings

      
      

Table 1. split Configuration Settings
          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Product Group Structure | "split" annotation | Engine Action | user Action | UI Behavior |
| --- | --- | --- | --- | --- |
| Product Classification | TRUE | Add multiple products | N/A | N/A |
| Product Classification | TRUE | N/A | Selecting or adding the product multiple times manually | Multiple instances created (qty = 1 each). User can add more instances, but can't change quantity per instance. |
| Product Classification | FALSE | Add multiple products | N/A | One instance created with qty > 1. User can change the quantity of this instance, but can't add more instances. |
| Product Classification | FALSE | N/A | Selecting or adding the product multiple times manually | One instance created with qty = 1. User can change the quantity of this instance, but can't add more instances. |
| Product Classification | (empty) | Add multiple products | N/A | One instance created with qty > 1. User can change quantity and can add more instances. |
| Product Classification | (empty) | N/A | Selecting or adding the product multiple times manually | One instance created with qty = 1. User can change quantity and can add more instances. |
| Individual Product | TRUE | Add multiple products | N/A | Multiple line items created, but Configurator displays only one instance. Users cannot modify quantity for that instance. |
| Individual Product | TRUE | N/A | Selecting or adding the product manually | One instance created with qty = 1. Users cannot change quantity. |
| Individual Product | FALSE | Add multiple products |  | One instance created with qty > 1. Users can't modify quantity for that instance. |
| Individual Product | FALSE | N/A | Selecting or adding the product manually | One instance created with qty = 1. Users can modify quantity for that instance. |
| Individual Product | (empty) | Add multiple products |  | One instance created with qty > 1. Users can't modify quantity for that instance. |
| Individual Product | (empty) | N/A | Selecting or adding the product manually | One instance created with qty = 1. Users can modify quantity for that instance. |

=== ARTICLE: cml_annotation_examples.htm ===
---
page_id: cml_annotation_examples.htm
title: Annotation Examples
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_annotation_examples.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Annotation Examples

Constraint Modeling Language (CML) annotations are labels that you add to parts of a
    model, such as types, variables, relationships, and constraints. Annotations control how these
    elements are shown and how they behave in the configurator. Annotations help fine-tune the
    configurator and the constraint engine without changing the actual structure of the
    model.

    
      

The examples explain what each annotation does, where it can be used in the model, what
        kinds of values it supports, and how it behaves when the configurator runs and evaluates
        constraints. CML code samples show how the annotation works in practice.

    

  

- 
**[closeRelation Annotation](./cml_annotation_example_closeRelation.htm.md)**  

closeRelation is a CML annotation that controls addition of new line items to the     relationship by the engine.

- 
**[configurable Annotation](./cml_annotation_example_configurable.htm.md)**  

`configurable` is a CML annotation that controls whether     a model element can be configured.

- 
**[defaultValue Annotation](./cml_annotation_example_defaultValue.htm.md)**  

The `defaultValue` annotation is used on a variable to     define the value it should start with when configuration begins.

- 
**[domainComputation Annotation](./cml_annotation_example_domainComputation.htm.md)**  

`domainComputation` is a CML annotation that specifies     how the domain of a model element is determined, either by using a fixed domain or by     computing the domain dynamically during configuration.

- 
**[guardrails Annotation](./cml_annotation_example_guardrails.htm.md)**  

guardrails is a CML annotation that prevent the constraint engine from changing     specified attributes or relations when it resolves the constraint.

- 
**[peelable Annotation](./cml_annotation_example_peelable.htm.md)**  

The `peelable` annotation is used to create soft     selection values and allow the engine to modify these selections to satisfy a     constraint.

- 
**[productField Annotation](./cml_annotation_example_productField.htm.md)**  

productField is a CML annotation that defines the Product2 field on a variable.   productField loads the value from Product Catalog Management (PCM) during constraint model   activation.

- 
**[propagateUp Annotation](./cml_annotation_example_propagateUp.htm.md)**  

`propagateUp` is a Constraint Modeling Language     (CML) annotation that controls aggregation propagation between children and parent     elements.

- 
**[relatedAttributes Annotation](./cml_annotation_example_relatedAttributes.htm.md)**  

`relatedAttributes` is a Constraint Modeling     Language (CML) annotation that resets the domain to the original one for     domainComputation.

- 
**[sequence Annotation](./cml_annotation_example_sequence.htm.md)**  

The `sequence` annotation defines the execution and     configuration order of elements in a Constraint Modeling Language (CML) model.

- 
**[split Annotation](./cml_annotation_example_split.htm.md)**  

`split` is a Constraint Modeling Language (CML)     annotation that specifies whether the instances of the type should be split or not.

=== ARTICLE: cml_appendix_model_structure.htm ===
---
page_id: cml_appendix_model_structure.htm
title: Model Structure
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_appendix_model_structure.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Model Structure

The tables on the following pages show the structure for the constraint model in Core
    Concept Examples.

    

See [Core Concept Examples](./cml_core_concept_examples.htm.md).

    
      

          
          
          
          
          
          
          
          
          
          
            
              

              

              

              

              

              

              

              

              

            

          

          
            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

            
              

              

              

              

              

              

              

              

              

            

          

        
| Level | Product Group | Product | Product Type Name | Product Attribute | API Name OR CML Variable | Configurable or Static | Type | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Bundle | Generator Set | GeneratorSet |  |  |  |  |  |
|  |  |  |  | Required KW | requiredKW | CONFIGURABLE | int |  |
|  |  |  |  | Surge Load KW | surgeLoadKW | EXPRESSION | decimal | requiredKW * 1.25 |
|  |  |  |  | Reserve Capacity KW | reserveCapacityKW | EXPRESSION | decimal | surgeLoadKW - requiredKW |
|  |  |  |  | Voltage | voltage | CONFIGURABLE | Picklist Voltage ["220/380","240/416","255/440","277/480","347/600","2400/4160","7200/12470","7621/13200","7976/13800"] |  |
|  |  |  |  | Duty Rating | dutyRating | CONFIGURABLE | Picklist DutyRating ["Prime Power", "Continuous Power", "Data Center Continuous", "Emergency Standby Power"] |  |
|  |  |  |  | Standards and Compliance | standardsAndCompliance |  | Picklist standardsAndCompliance ["Certification-CSA", "Listing-UL 2200"] |  |
|  |  |  |  | max dB level | dBMax | CONFIGURABLE | int |  |
|  |  |  |  | Nominal Power Output | nominalPowerOutput |  | Picklist Power Output Picklist ["100 kW", "300 kW", "500 kW", "700 kW"] |  |
| 1 | General |  |  |  |  |  |  |  |
| 2 | General - Model |  | GeneralModel |  |  |  |  |  |
|  |  |  |  | Power KW | powerKW | STATIC | Picklist powerKW [900, 1750, 2500] | powerKW >= Needs.requiredKW |
|  |  |  |  | dB | dB | STATIC | Picklist dB [78, 90, 94] |  |
|  |  | General Model 900 | GeneralModel900 |  |  |  |  |  |
|  |  | General Model 1750 | GeneralModel1750 |  |  |  |  |  |
|  |  | General Model 2500 | GeneralModel2500 |  |  |  |  |  |
| 2 | General - Voltage Connection |  | VoltageConnection |  |  |  |  |  |
|  |  |  |  | Voltage | voltage | STATIC | Picklist voltage ["220/380", "240/416", "255/440"] | voltage == Needs.voltage |
|  |  |  |  | Cable Entry | cableEntry | CONFIGURABLE | Picklist cableEntry ["Top Entry", "Bottom Entry", "Side Entry"] |  |
|  |  | 220/380,3 Phase,Wye,4 Wire | VoltageConnection_220_380 |  |  |  |  |  |
|  |  | 240/416,3 Phase,Wye,4 Wire | VoltageConnection_240_416 |  |  |  |  |  |
|  |  | 255/440,3 Phase,Wye,4 Wire | VoltageConnection_255_440 |  |  |  |  |  |
| 1 | Alternator |  |  |  |  |  |  |  |
| 2 | Alternator - Main Alternator |  | MainAlternator |  |  |  |  |  |
|  |  |  |  |  | voltage | STATIC | Picklist Voltage | Needs.voltage == voltage |
|  |  |  |  |  | PRP | STATIC | boolean | constraint(Needs.dutyRating=="Prime Power"->PRP==true) |
|  |  |  |  |  | COP | STATIC | boolean | constraint(Needs.dutyRating=="Continuous Power"->COP==true) |
|  |  |  |  |  | DCC | STATIC | boolean | constraint(Needs.dutyRating=="Data Center Continuous"->DCC==true) |
|  |  |  |  |  | ESP | STATIC | boolean | constraint(Needs.dutyRating=="Emergency Standby Power"->ESP==true) |
|  |  | Alt-60Hz,Wye,220/380V,150/125/105C-SD/P/C,40C amb | FESBA_B595_2 |  |  |  |  |  |
|  |  | Alternator-60Hz,Wye,240/416 Volt,105/80C-StbyPrm | FESBA_B715_2 |  |  |  |  |  |
|  |  | Alt-60Hz,Wye,440V,150/125SP,40C amb | FESBA_B691_2 |  |  |  |  |  |
| 2 | Alternator - Heater |  |  |  |  |  |  |  |
| 2 | Alternator - Temperature Sensors |  | TemperatureSensor |  |  |  |  |  |
|  |  |  |  | Max Operating KW | maxOperatingKW | STATIC |  |  |
|  |  |  |  | Parent Required KW | parentRequiredKW | EXPRESSION |  |  |
|  |  | Temp Sens-Stator, 2 RTD/Ph | StatorTemperatureSensor |  |  |  |  |  |
|  |  | Bearing,1 RTD NDE | BearingTemperatureSensor |  |  |  |  |  |
| 2 | Alternator - Output Terminals |  | OutputTerminal |  |  |  |  |  |
|  |  | Output Terminals-2-Hole Lug, NEMA | OutputTerminals2HoleLugNEMA |  |  |  |  |  |
| 1 | Engine |  |  |  |  |  |  |  |
| 2 | Engine - Engine Model |  | EngineModel |  |  |  |  |  |
|  |  | Engine - QSK60-G6 | FESBA_2940 |  |  |  |  |  |
| 2 | Engine - Starter Motor |  | StarterMotor |  |  |  |  |  |
|  |  | Electric Starter Motor - 24V DC | FESBA_A334-2 |  |  |  |  |  |
| 2 | Engine - Fuel Filter |  | FuelFilter |  |  |  |  |  |
|  |  | Fuel Filters-Engine, Standard | FESBA_3090 |  |  |  |  |  |
|  |  | Fuel Filters-Engine, Duplex | FESBA_C278-2 |  |  |  |  |  |
| 1 | Control |  |  |  |  |  |  |  |
| 2 | Control - Control Main |  | Control |  |  |  |  |  |
|  |  |  |  | Control Placement | controlPlacement | CONFIGURABLE | Picklist ["Left", "Right", "Top"] |  |
|  |  |  |  | Commissioning Scope | commissioningScope | CONFIGURABLE | Picklist ["None", "Remote Support", "On-site Commissioning"] |  |
|  |  |  |  | Control Language | controlLanguage | CONFIGURABLE | Picklist ["English", "Danish", "French"] |  |
|  |  | PowerCommand 3.3 | FESBA_H704_2 |  |  |  |  |  |
|  |  | PowerCommand 3.3 with MLD | FESBA_KX21_2 |  |  |  |  |  |
| 2 | Control - Control Cabinet Heater |  | ControlCabinetHeater |  |  |  |  |  |
|  |  | 120/240VAC compatible | FESBA_A460_2 |  |  |  |  |  |
| 1 | Services |  |  |  |  |  |  |  |
| 2 | Services - Warranty |  | Warranty |  |  |  |  |  |
|  |  | Warranty PRP | Warranty_PRP |  |  |  |  |  |
|  |  | Warranty DCC | Warranty_DCC |  |  |  |  |  |
|  |  | Warranty ESP | Warranty_ESP |  |  |  |  |  |
| 2 | Services - Maintenance |  | Maintenance |  |  |  |  |  |
|  |  |  |  | Maintenance Duration | maintenanceDuration | CONFIGURABLE | int [12..60] |  |
|  |  |  |  | Coverage Level | coverageLevel | CONFIGURABLE | Picklist ["Standard", "Premium"] |  |
|  |  | Standard Maintenance Kit | StandardMaintenanceKit |  |  |  |  |  |
| 2 | Services - Testing |  | Test |  |  |  |  |  |
|  |  | Test - Standard Factory | StandardFactoryTest |  |  |  |  |  |
|  |  | Test Record-Certified | TestRecord |  |  |  |  |  |
|  |  | Test-Independent Laboratory | IndependentLaboratoryTest |  |  |  |  |  |
|  |  | Test - Witness | WitnessTest |  |  |  |  |  |
|  |  | Test-Extended, Standby Load, 2 | WitnessTestService |  |  |  |  |  |
| 1 | Accessories |  |  |  |  |  |  |  |
| 2 | Accessories - Main |  | Accessory |  |  |  |  |  |
|  |  |  |  | Category | category | CONFIGURABLE | Picklist |  |
|  |  |  |  | Weight | weight |  |  |  |
| 2 | Accessories - Enclosure |  | Enclosure |  |  |  |  |  |
|  |  |  |  | dB Reduction | dBReduction | STATIC | Picklist dBReduction [0, 1, 3, 6, 9] |  |
|  |  | Enclosure None | Enclosure_None |  |  |  |  |  |
|  |  | Enclosure Weather | Enclosure_Weather |  |  |  |  |  |
|  |  | Enclosure SA1 | Enclosure_SA1 |  |  |  |  |  |
|  |  | Enclosure SA2 | Enclosure_SA2 |  |  |  |  |  |
|  |  | Enclosure SA3 | Enclosure_SA3 |  |  |  |  |  |
| 1 | Install & Misc |  |  |  |  |  |  |  |
| 2 | Install & Misc - Installation |  | install |  |  |  |  |  |

=== ARTICLE: cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm ===
---
page_id: cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm
title: Business-Centric Constraint Modeling Language (CML) Guidelines
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business-Centric Constraint Modeling Language (CML) Guidelines

Constraint Modeling Language (CML) must accurately calculate the total sum or aggregate
    of specific attributes like quantity or userCount across child components, especially in complex
    configurations requiring group-level aggregation

    
      

The main modeling obstacles when performing aggregation in CML involve:

      

- Initialization Errors: Preventing runtime errors, such as `NullPointerException`, which can occur if derived aggregate attributes lack
          explicit domains.

- Circular Dependencies: Avoiding calculation loops where the parent and children mutually rely on
          aggregated totals, often involving the `total()`
          function. If these loops are not broken, the aggregated variable becomes "not
          bound", which causes the solution to fail.

    

    

## User Workflow

      
      

As a sales representative, when I am configuring a bundle product in the Configurator window, I modify the quantities or specific attributes of the individual child components. I expect the constraint engine to immediately and accurately calculate the overall aggregated totals for the parent product, such as the totalItemCount or sumOfUsers.

    

  

- 
**[Business-Centric CML Examples](./cml_business_centric_cml_examples.htm.md)**  

These Constraint Modeling Language (CML) structures implement quantity aggregation and     resolve calculation dependencies.

=== ARTICLE: cml_business_centric_cml_examples.htm ===
---
page_id: cml_business_centric_cml_examples.htm
title: Business-Centric CML Examples
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_business_centric_cml_examples.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Business-Centric CML Examples

These Constraint Modeling Language (CML) structures implement quantity aggregation and
    resolve calculation dependencies.

    

## Example 1: Derived Aggregates (Total Quantity or Sum)

      
      

This CML example shows how to model bundle rollups by separating aggregation from validation, ensuring correct calculation order, solver stability, and business-rule consistency

      

```
type LineItem;
type GeneratorSet : LineItem {
  int totalItemPowerKW = modelclassification.totalPowerKW;
  // Aggregate `powerKW`
  relation modelclassification : ModelClassification[0..10] {
    totalPowerKW = sum(powerKW);
  }
  message(true, "GeneratorSet totalItemPowerKW = {} kW (calculated roll-up). Sum of selected ModelClassification powerKW values = {} kW.", totalItemPowerKW, modelclassification.totalPowerKW);
}
type ModelClassification : LineItem {
  int powerKW = [900, 1750, 2500];
}
type GeneralModel1750 : ModelClassification {
  int powerKW = 1750;
}
type GeneralModel2500 : ModelClassification {
  int powerKW = 2500;
}
type GeneralModel900 : ModelClassification {
  int powerKW = 900;
}
```

    

    

## Example Description and Configurator Result

      
      

In example 1, the `GeneratorSet` type contains the
          `totalItemPowerKW` variable that is assigned with the
          `totalPowerKW`. The model specifies a relationship
        based on the product classification (`modelClassification`). This relationship includes aggregation using the sum()
        function that calculates the `totalPowerKW` from the
        products selected in the `modelClassification` during
        bundle configuration. The model contains a message for displaying the `totalItemPowerKW` with the `modelClassification.totalPowerKW` on the Product Configuration.

      

```
message(true, "GeneratorSet totalItemPowerKW = {} kW (calculated roll-up). Sum of selected ModelClassification powerKW values = {} kW.", totalItemPowerKW, modelclassification.totalPowerKW);
```

      

As a result, the engine calculates the `totalPowerKW` of
        user selected products in the `modelClassification` and
        assigns this value to the `totalItemPowerKW`. The system
        displays both values in the information message on the Product Configuration.

    

    

## Example 2: Resolving Circular Dependencies

      
      

This pattern breaks unsolvable loops by enforcing unidirectional data flow (Parent dictates Child quantity based on Child aggregates).

      

```
type LineItem;
type GeneratorSet : LineItem {
  // RELATION: THE "READ" PHASE
  // Data flows UP from children to the parent via the port attribute
  relation voltageclassification : VoltageClassification[1..10] {
    sumOfChildPower = total(power);
  }
  // Explicit domain ensures the solver initializes correctly for calculations
  decimal(2) totalDistributionValue = [0.00..1000.00];
  // CONSTRAINT 1: THE "CALCULATION" PHASE
  // @(sequence = 1) ensures the engine reads child data and calculates first
  @(sequence = 1)
  constraint calcTotalDistribution(totalDistributionValue == voltageclassification.sumOfChildPower / 100);
  // CONSTRAINT 2: THE "WRITE/ENFORCE" PHASE
  // @(sequence = 2) ensures this happens last to push values DOWN to children
  @(sequence = 2)
  constraint setChildQuantity(voltageclassification[VoltageClassification] == totalDistributionValue * 2);
}
type VoltageClassification : LineItem {
  int power = [1..100];
}
type VoltageConnection_220_380 : VoltageClassification;
type VoltageConnection_240_416 : VoltageClassification;
type VoltageConnection_255_440 : VoltageClassification;
```

    

    

## Example Description and Configurator Result

      
      

In example 2, the relationship includes aggregation using the `total()` function that calculates the `sumOfChildPower` from the selected products in the `voltageclassification`. The `GeneratorSet`
        type contains the `totalDistributionValue` with the
        explicit domain ([0.00..1000.00]). The model contains two constraints with corresponding
          `@sequence` annotation to enforce the logical order for
        calculation of the `calcTotalDistribution` (using child
        products data) and defining the quantity for the `voltageclassification` child items.

    

    

## Example 3: Grouped Aggregation (Sum of Users Across Regions)

      
      

This advanced pattern uses the `@(groupBy=attribute)`
        annotation to create virtual components (`RegionGroup`)
        for aggregation, referencing the source data relation in the parent type (`SubscriptionOrder.licenses`) using the `sourceContextNode` annotation.

      

```
// 1. Base Product Type (e.g., Regional License)
type RegionalLicense {
  int regionId = [0..100]; // Attribute for grouping
  int userCount = [0..100];
}
// 2. Virtual Group Type (Performs grouping and user sum)
@(split=true, virtual=true, groupBy=regionId)
type RegionGroup {
  int regionId;
  int groupTotalUsers; // Sum of userCount for this region
  // Relation to licenses matching this region group
  @(sourceContextNode="SubscriptionOrder.licenses")
  relation licenses: RegionalLicense[0..100];
  // Constraint: Calculate the aggregate user count within this group
  constraint(groupTotalUsers == licenses.sum(userCount));
}
// 3. Parent Order Management (Aggregates all region totals)
@(virtual=true)
type SubscriptionOrder {
  // Overall total users is calculated by referencing the group totals
  int totalUsers = regionGroups.groupTotalUsers;
  relation licenses: RegionalLicense[0..500];
  relation regionGroups: RegionGroup[1..10];
}
```

    

    

## Example Description and Configurator Result

      
      

In example 3, the `licenses` relationship that is
        brought as an external source by `@(sourceContextNode="SubscriptionOrder.licenses")`, includes an aggregation using
        the `sum()` function that calculates the `groupTotalUsers` from the selected products in the `RegionalLicense`. The `RegionGroup` type contains the `groupTotalUsers` variable that serves the aggregation. The `SubscriptionOrder` type contains the aggregate metric `totalUsers` which is calculated by summing all `groupTotalUsers`. The model contains one core constraint on
          `RegionGroup` to enforce that `groupTotalUsers` equals the sum of all `userCount` from its member licenses.

=== ARTICLE: cml_cml_best_practices.htm ===
---
page_id: cml_cml_best_practices.htm
title: Constraint Modeling Language (CML) Best Practices
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_cml_best_practices.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Constraint Modeling Language (CML) Best Practices

To prevent performance degradation or unexpected behaviors when the constraint engine
    executes CML code, follow these practices when writing code.

    

For tips on troubleshooting, see [Debugging Constraint Modeling Language (CML)](./cml_debugging_cml.htm.md).

    

## Relationship Cardinality: Specify the Smallest Range Required

      
      

In a relationship, cardinality is the quantity of instances of the same type. Specify the
        smallest required cardinality for a variable, to avoid testing unneeded combinations of
        values. If you specify a higher cardinality than required, or don't specify cardinality, the
        constraint engine tests more combinations, which impacts performance.

      

This example doesn't specify cardinality. The constraint engine tries to set a quantity
        with 1, 2, 3, all the way up to 9,999:

      

```
relation engine : Engine;
```

      

This example specifies minimum and maximum cardinality as 0 and 1, so the constraint engine
        sets the quantity to 1. The engine tests fewer combinations to find a solution.

      

```
relation engine : Engine[0..1];
```

    

    

## Decimals and Doubles: Consider the Impact of Scale on Performance

      
      

In a decimal or double, scale is the number of digits that follow the decimal point. Using
        decimals and doubles in expressions can cause performance problems due to the number of
        permutations.

      

In this example, myNumber is a double with a scale of 2. The value can be 0.00, 0.01, 0.02,
        all the way up to 2.99, which can impact constraint engine performance:

      

```
double(2) myNumber = [0..3];
```

      

In this example, myNumber is an integer. The value can only be 0, 1, 2 or 3, which has less
        impact on constraint engine performance:

      

```
int myNumber = [0..3];
```

    

    

## Variable Domains: Keep Domains as Small as Possible

      
      

A variable domain is the set of all possible values that the variable can take. In this
        example, the variable color has a domain with three values:

      

```
string color = ["Red", "Yellow", "Green"];
```

      

The larger the domain, the more possible values for the variable, which means more
        combinations for the engine to test. A large domain can impact performance and lead to
        slower searches, errors, or unexpected behaviors.

    

    

## Calculating Values: Put Calculations Inside of Constraints

      
      

To calculate a value, put the calculation inside of a constraint, instead of in an inline
        expression.

      

For example, to calculate area, use this constraint:

      

```
constraint(area == length * width)
```

      

Avoid this example, which calculates the area with an inline expression, and can impact
        performance:

      

```
area = length * width.
```

    

    

## Relationships: Combine Relationships to Reduce Performance Impact

      
      

Creating multiple relationships on a type can impact performance. When possible, combine
        relationships to improve performance.

      

When possible, avoid this example, which includes separate relationships for Mouse and
        Keyboard, two accessories in a product bundle:

      

```
relation mouse : Mouse;
relation keyboard : Keyboard;
```

      

Follow this example, which uses one relationship for Accessories, which can include Mouse,
        Keyboard, and other accessories.

      

```
relation accessories : Accessories;
```

    

    

## Sequence: Use the Sequence Variable Annotation to Specify the Order of
        Execution

      
      

If a constraint model includes multiple attributes and relationships that should follow a
        certain order of execution, use the sequence variable annotation to specify the order. The
        constraint engine follows sequence designations in satisfying constraint requirements and
        resolving constraint violations.

      

In this example, for the Desktop type, the sequence annotation directs the constraint
        engine to set the default values for attributes in this order:

      
        
- Display: sequence=1

        
- Windows_Processor: sequence=2

        
- Display_Size: sequence=3

      

      

```
type Desktop {
    @(defaultValue = "1080p Built-in Display", sequence=1)
    string Display = ["1080p Built-in Display", "4k Built-in Display", "2k Built-in Display"];
    
    @(defaultValue = "15 Inch", sequence=3)
    string Display_Size = ["15 Inch", "24 Inch", "13 Inch", "27 Inch"];
    
    @(defaultValue = "i5-CPU 4.4GHz", sequence=2)
    string Windows_Processor = ["i5-CPU 4.4GHz", "i7-CPU 4.7GHz", "Intel Core i9 5.2 GHz"];

    constraint(Display == "1080p Built-in Display" && Display_Size == "15 Inch" -> Windows_Processor == "i7-CPU 4.7GHz");
}
```

      

For Desktop, Display is set to 1080p, Windows_Processor to i5-CPU, and Display_Size to 15
        Inch.

      

The constraint specifies that a type with Display of 1080p and Display_Size of 15 Inch must
        have a Windows_Processor of i7-CPU.

      

```
constraint(Display == "1080p Built-in Display" && Display_Size == "15 Inch" -> Windows_Processor == "i7-CPU 4.7GHz");
```

      

The Windows_Processor default value of i5-CPU for Desktop violates the constraint. In order
        to satisfy the constraint and resolve the violation, the constraint engine uses a different
        Display_Size for Desktop, such as 24 Inch.

      

If the user manually updates Display_Size for Desktop to 15 Inch in the Product
        Configurator, the constraint engine updates Windows_Processor to i7-CPU to satisfy the
        constraint.

    

    

## Sequence and Configurable

      
      

Using the `configurable` property with the `sequence` variable affects how the solver handles attributes.
        When configurable is set to `true`, the user can set
        attribute values, and the solver doesn't override user input unless no other solution
        exists. When `configurable` is set to `false`, the solver sets attribute values.

      

In this example for type A, `attribute1` is set to
          `configurable = true`. The user can set the value, and
        the solver doesn't override the user input unless no other solution exists. When the
        left-hand side of the rule is true, the constraint doesn't change `attribute1` to "`Enum3`".

      

```
type A : System {
    @(defaultValue = "Enum1", domainComputation = "true", configurable = true, sequence = 48)
    string attribute1 = ["Enum1", "Enum2", "Enum3"];

  @(configurable = false, defaultValue = "0", sequence = 30)
    decimal(2) attribute2 = f(x, y, z);
    constraint((attribute2 > 3 && attribute2 <= 5) -> attribute1 == "Enum3", "message");
}
```

      

In this example for type B, `attribute1` is set to
          `configurable = false`. The solver propagates values to
        satisfy constraints. When the left-hand side of the rule is true, the constraint
        automatically sets `attribute1` to "`Enum3`".

      

```
type B : System {
    @(defaultValue = "Enum1", domainComputation = "true", configurable = false, sequence = 48)
    string attribute1 = ["Enum1", "Enum2", "Enum3"];

  @(configurable = false, defaultValue = "0", sequence = 30)
    decimal(2) attribute2 = f(x, y, z);
    constraint((attribute2 > 3 && attribute2 <= 5) -> attribute1 == "Enum3", "message");
```

      

Use mindful sequencing in CML to avoid backtracking by the solver when looking for a
        solution, as in this example.

      

```
type LaptopProBundle {

    //relation mouse : Mouse[1..20]; 
    //The relation mouse has the highest sequence
    relation warranty : Warranty[0..10];
    relation software : Software;
    relation printerBundle : PrinterBundle;
    relation laptop : Laptop[1..10];
    relation mouse : Mouse[1..20];
    //Put highest sequence last to avoid backtracking

    int mouseQty = laptop[Laptop] + warranty[Warranty];

    constraint(mouse[Mouse] > 0 -> mouse[Mouse] == mouseQty,
               "mouse[Mouse] = laptop[Laptop] + warranty[Warranty]");
```

    

    

## Automatically Add a Product: Define as a Separate Constraint

      
      

If you need to automatically add a product, and also set attributes on the product, define
        these procedures as separate constraints, as in this example.

      

```
constraint(laptop[Laptop] > 0, warranty[Warranty] > 0);
constraint(warranty[Warranty] > 0, warranty[Warranty].type == “Premium”);
```

      

Avoid this example, which automatically adds a product and sets attributes on the product,
        in the same constraint.

      

```
constraint(laptop[Laptop] > 0, warranty[Warranty] > 0 && warranty[Warranty].type == "Premium");
```

    

    

## Access Quantity in CML: Cardinality and Attribute Constraints

      
      

There are two ways to access quantity in CML:

      

A cardinality constraint creates or validates the presence of components. The constraint
        engine adds or removes instances to satisfy the conditions of the constraint.

      

An attribute constraint, such as lineItemQuantity or ItemEndQuantity, only reads or
        validates. The constraint engine validates the expression, but doesn't configure to satisfy
        the conditions of the constraint

      

For best performance, follow these guidelines:

      
        
- Use a cardinality constraint whenever possible. Use `lineItemQuantity` or `ItemEndQuantity` only
          when a cardinality constraint can't meet the business need.

        
- Treat `lineItemQuantity` and `ItemEndQuantity` as read-only. Use only in calculation or
          evaluation rules.

        
- Keep scope in mind. When a product can have multiple instances, read `lineItemQuantity` or `ItemEndQuantity` per instance. Avoid reading the attribute at a parent or
          aggregate scope where it can be unbound or ambiguous.

        
- Don't use `lineItemQuantity` or `ItemEndQuantity` to create components. Drive component
          creation by cardinality, not by attribute references.

      

      

Use constraint patterns similar to these examples. Do this.

      

```
constraint(mouse[Mouse] == warranty[Warranty])
```

      

Avoid this.

      

```
constraint(mouse[Mouse].lineItemQuantity == warranty[Warranty].lineItemQuantity)
```

      

Do this.

      

```
constraint(mouse[Mouse] == 3)
```

      

Avoid this.

      

```
constraint(mouse[Mouse].lineItemQuantity == 3)
```

    

    

## Pricing Fields Not Supported in CML

      
      

Pricing fields, such as ListPrice, NetUnitPrice, and others, are not supported in CML and
        should not be used in constraint models. CML is designed to enforce configuration logic for
        products, not to perform pricing calculations. Attempting to reference or manipulate pricing
        fields in CML code leads to errors and unexpected behaviors in the constraint engine. Use
        dedicated pricing or calculation mechanisms outside of the CML constraint model for such
        functionality.

    

    

## Configure Child or Grandchild Products Based on Parent Product

      
      

Use the `parent` keyword to configure child and
        grandchild products dynamically based on the parent product. Control visibility or
        availability for the child or grandchild using the keyword.

      

#### Note

The `parent` keyword isn't supported with
        Group Type.

      

In this example, grandchild products are excluded based on which parent product they belong
        to.

      

```
type LineItem;

/* 
 * Parent 1: Industrial Bundle 
 * Sets the context 'ApplicationType' to "Industrial"
 */
type IndustrialGeneratorBundle : LineItem {
    relation enclosurePackage : EnclosurePackage[1..999];
    
    relation enclosurePackage1 : EnclosurePackage[1..999];
    
    relation enclosurePackage2 : EnclosurePackage;

    string ApplicationType = "Industrial";
}

/* 
 * Parent 2: Residential Bundle 
 * Sets the context 'ApplicationType' to "Residential"
 */
type ResidentialGeneratorBundle : LineItem {
    relation enclosurePackage3 : EnclosurePackage[1..999];
    
    relation enclosurePackage4 : EnclosurePackage;

    string ApplicationType = "Residential";
}

/* 
 * Shared Component: Enclosure Package 
 * Uses parent() to read the ApplicationType and excludes items accordingly.
 */
type EnclosurePackage : LineItem {
    relation soundInsulation : SoundInsulation[0..999];
    relation weatherProofing : WeatherProofing[0..999];
    relation heater : Heater[0..999];                   
    relation lighting : InternalLighting[0..999];      
    
// Retrieve the context tag from the parent bundle
    string parentApp = parent(ApplicationType);

    message(true, parentApp);

    // Logic 1: Exclude Lighting and Heater for BOTH bundles
    exclude(parentApp == "Industrial" || parentApp == "Residential", lighting[InternalLighting]);
    exclude(parentApp == "Industrial" || parentApp == "Residential", heater[Heater]);

    // Logic 2: Residential (Basic) excludes Sound Insulation
    exclude(parentApp == "Residential", soundInsulation[SoundInsulation]);

    // Logic 3: Industrial (Pro) excludes Weather Proofing
    exclude(parentApp == "Industrial", weatherProofing[WeatherProofing]);
}

// --- Sub-components ---

type SoundInsulation : LineItem {
    @(defaultValue = "Foam")
    string Material = ["Foam", "Fiberglass"];
}

type WeatherProofing : LineItem {
    @(defaultValue = "Standard")
    string Grade = ["Standard", "Marine"];
}

type Heater : LineItem;

type InternalLighting : LineItem;
```

    

    

## PCG Group Relations: Follow Order in Constraints

      
      

Order the Product Component Group (PCG) group relations in the way they appear in the
        constraints. Specify the groups used in the LHS of the constraints first, followed by those
        in the RHS.

      

In this example, the order of PCG groups is incorrect as `Test1Group` is part of the LHS and should be declared first. 

      

```
type TestParent : LineItem {
    Test2Group test2group;

    Test1Group test1group;

    constraint(test1group.testchild1[TestChild1] > 0 -> test2group.testchild2[TestChild2] == test1group.testchild1[TestChild1]);

}
```

      

This example shows the correct order of PCG groups, where `Test1Group` is declared first because it is part of the LHS.

      

```
type Test20260204Parent : LineItem {
    
    Test1Group test1group;
    Test2Group test2group;

    constraint(test1group.testchild1[TestChild1] > 0 -> test2group.testchild2[TestChild2] == test1group.testchild1[TestChild1]);

}
```

    

    

## Relations Without PCG: Follow Order in Constraints

      
      

Order of relations matter for constraint evaluation. Specify the relations used in the LHS
        of the constraints first, followed by those in the RHS.

    

    

## Relation Aggregates: Stabilize Preferences Using Staged
        Variables

To improve solver stability and prevent backtracking, avoid referencing
        relation aggregates directly within preferences when the preferences also influence the same
        relation. Instead, stage these aggregates through local variables and state
        anchors.

In this example, the preferences and the calculated quantity depend directly
        on live relation
        aggregates.

```
relation ml : ModelTraining {
   totalNumSubscriptions = total(NumSubscriptions);
   subCount = count(Sublicense == true);
}
preference(ml[ModelTraining] > 0 && ml.subCount == 0 -> ml[ModelTraining] == parentQty);
preference(ml[ModelTraining] > 0 && ml.subCount > 0 -> ml[ModelTraining] == calculatedQuantity);
constraint(calculatedQuantity == ((ml.totalNumSubscriptions + 99) / 100) * 100);
```

When
        the solver evaluates preferences that depend directly on a relation's own aggregates, it
        creates a tight feedback loop:

Relation Quantity ⟶ Relation Aggregates ⟶ Preference
        Guards/Targets ⟶ Relation Quantity (loop repeats)

The feedback loop can cause the
        solver to oscillate or backtrack repeatedly before finding a stable solution.

This
        example shows the stabilized pattern. It introduces staged variables that act as anchors to
        separate the relation aggregates from the preference
        logic.

```
relation ml : ModelTraining {
    totalNumSubscriptions = total(NumSubscriptions);
    subCount = count(Sublicense == true);
}

// Stage 1: Convert relation conditions into stable booleans
boolean hasSub;
constraint(hasSub <-> (ml.subCount > 0));

// Stage 2: Copy relation aggregates into local variables
int localTotalNumSubscriptions;
constraint(localTotalNumSubscriptions == ml.totalNumSubscriptions);

// Stage 3: Perform calculations by using the local variables
int calculatedQuantity;
constraint(calculatedQuantity == ((localTotalNumSubscriptions + 99) / 100) * 100);

// Stage 4: Use the staged variables in the preferences
preference(ml[ModelTraining] > 0 && hasSub == false -> ml[ModelTraining] == parentQty);
preference(ml[ModelTraining] > 0 && hasSub == true -> ml[ModelTraining] == calculatedQuantity);
```

With
        this pattern, instead of solving everything simultaneously, the solver logic processes a
        pipeline:

Relation ⟶ Aggregates ⟶ Anchored State/Local Variables ⟶ Derived
        Calculations ⟶ Preferences

This process reduces oscillation and makes the solving path
        more deterministic.

    

## Dependent Logic: Use Configurable Variable Annotation
        to Prevent Premature Default Assignment

To ensure preference rules correctly set
        target attributes based on calculated values, use the `@(configurable=false)` annotation on the target attribute. This prevents a race
        condition where the engine assigns a default value during initialization before your
        calculation and preference rules execute.

When an inline expression is used, CML
        evaluates the model top-down. If the target attribute is declared before the inline
        calculation, the engine immediately assigns a default value to the attribute. As a result,
        any subsequent `preference()` rules are ignored because
        the engine treats the existing default value as an established selection and avoids
        overwriting it with the calculated value. Annotating the target attribute with `@(configurable=false)`) forces the engine to leave the
        variable as `null` until the calculation and preference
        rules are executed.

In this example, the engine processes `ShippingMethod` first and immediately assigns the default value "Standard" to it.
        Later, when the calculation for `totalWeight` returns a
        value high enough to require the “Freight” shipping method, the engine ignores this
        preference rule because the `ShippingMethod` variable is
        already bound to
        "Standard".

```
type Order : LineItem {
    int quantity = [1..100];
    int weightPerUnit = [10..50];

    // Problem: Engine assigns "Standard" immediately during initialization
    @(defaultValue = "Standard")
    string ShippingMethod = ["Standard", "Freight"];

    // Calculated Attribute via Inline Expression

    // The calculation happens after the default is already set
    int totalWeight = quantity * weightPerUnit;

    // This rule is ignored because ShippingMethod is already bound to "Standard"
    preference(totalWeight > 1000 -> ShippingMethod == "Freight");
}
```

In this example, using the `@(configurable=false)` annotation ensures the `ShippingMethod` attribute remains as `null`
        until the calculation completes and the rules execute.

#### Note

Provide a second preference rule for the fallback condition (else) to ensure a value is
        always
      set.

```
ype Order : LineItem {
    int quantity = [1..100];
    int weightPerUnit = [10..50];

    // Solution: Prevent premature default assignment 
    @(configurable=false)
    string ShippingMethod = ["Standard", "Freight"]; 

    // Calculated Attribute via Inline Expression 
    int totalWeight = quantity * weightPerUnit;

    // Rule 1: Handle the specific condition (high weight)
    preference(totalWeight > 1000 -> ShippingMethod == "Freight");

    // Rule 2: Handle the fallback (low weight)
    preference(totalWeight <= 1000 -> ShippingMethod == "Standard");
}
```

    

## Consolidate Multiple Default Configurations

Apply dynamic, overridable default quantities to a single component based on
        multiple possible states of a driving attribute. This process avoids rule conflicts where
        only the last rule evaluates.

When multiple `setdefault` rules target the same assignment in the RHS,  evaluations can
        conflict. For example,  a conflict can result when the rule targets the same relation and
        type, such as `accessories[Accessory] == ...`. The
        condition side can use different expressions, but if the rules resolve to the same target on
        the assignment side, behavior can become order-dependent and lead to inconsistent
        outcomes.

For example, if you want to set a default for the quantity of `Accessories` based on the selected `DutyRating` of a Generator Set, writing three separate `setdefault` rules causes inconsistent behavior depending on
        the quantity changes of the accessories.

To prevent the conflict, consolidate the
        conditional logic into a single derived variable using nested ternary expressions, such as
          `? :`. Then, apply a single `setdefault` rule using that newly derived variable to drive the relation's
        quantity.

This example shows the recommended process, consolidating the logic into a
        single variable and rule.

```
type GeneratorSet : LineItem {
    string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];

    relation accessories : Accessory[1..99] {
        default Accessory(1);
    }

    // 1. Consolidate the conditional logic into a single integer variable
    int defaultAccessoryQty = (DutyRating == "Prime Power (PRP)") ? 2 : ((DutyRating == "Continuous Power (COP)") ? 4 : 6);

    // 2. Create a dynamic informational message
    string infoMsg = DutyRating + " accessory default overridden";

    // 3. Apply a single setdefault rule using the derived variable
    setdefault(
        DutyRating in ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"],
        accessories[Accessory] == defaultAccessoryQty,
        infoMsg
    );
}

```

Avoid the process shown in this example, which includes multiple conflicting
          `setdefault`
      rules.

```
type GeneratorSet : LineItem {
    string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];

    relation accessories : Accessory[1..99] {
        default Accessory(1);
    }

    // X AVOID: Multiple setdefault rules targeting the same relation.
    // Only the last rule will reliably evaluate.
    setdefault(DutyRating == "Prime Power (PRP)", accessories[Accessory] == 2, "PRP error");
    setdefault(DutyRating == "Continuous Power (COP)", accessories[Accessory] == 4, "COP error");
    setdefault(DutyRating == "Emergency Standby Power (ESP)", accessories[Accessory] == 6, "ESP error");
}

```

=== ARTICLE: cml_cml_core_concepts.htm ===
---
page_id: cml_cml_core_concepts.htm
title: Core Concepts
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_cml_core_concepts.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Core Concepts

Constraint Modeling Language (CML) includes components that cover high-level global
        configurations to specific data types and constraints.

    
    

See these topics for information on each core concept and the ways they work together.

    

#### Note

CML supports single-line code comments with // and block comments with /*
        */.

            
    

  

- 
**[Global Properties and Settings](./cml_global_properties_and_settings.htm.md)**  

Header-level declarations define the global properties and settings for a model, including     constants, properties, and external values that set up the foundation of the CML code.

- 
**[Variables](./cml_variables.htm.md)**  

Variables are the properties or characteristics defined within a type. Variables can hold     different types of data and can be calculated from other values.

- 
**[Types](./cml_types.htm.md)**  

In Constraint Modeling Language (CML), you define types to represent entities or     objects in the model. Types are the foundational building blocks of CML. A type encapsulates the     property, relationships, constraint, and rules for the entity.

- 
**[Relationships](./cml_relationships.htm.md)**  

Relationships in Constraint Modeling Language (CML) define how different product types     are associated with each other, forming the structural hierarchy of a product bundle.     Relationships are also referred to as ports.

- 
**[Constraints](./cml_constraints.htm.md)**  

Constraints enforce rules and conditions on types, variables, and relationships. Use     constraints to define logical restrictions and ensure consistency within the     model.

=== ARTICLE: cml_constraint_model_example_modeling_a_generator_set.htm ===
---
page_id: cml_constraint_model_example_modeling_a_generator_set.htm
title: Modeling a Generator Set
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_constraint_model_example_modeling_a_generator_set.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Modeling a Generator Set

The Constraint Model for a Generator Set examples use CML to define a technical power
    configuration, illustrating concepts such as calculated variables, enforcement of external
    standards, and component selection based on requirements.

    

The [examples](./cml_core_concept_examples.htm.md) correspond to the [CML core concepts](./cml_cml_core_concepts.htm.md) linked here. See the Generator Set
      examples for code samples that use the core concepts.

    

- Global Properties and Settings—`VOLTAGE_REGEX` is a
        global constant that defines a fixed regular expression pattern used for validation or
        parsing throughout the model.

      
- Types—`GeneratorSet` is the root type that
        represents the main entity. `GeneralModel` represents a
        related component type.

      
- Variables—The `GeneratorSet` type defines
        variables like `requiredKW` (the user's power
        requirement), `Voltage`, and calculated variables like
          `surgeLoadKW` and `Voltage3` (derived from parsing the `Voltage`
        string).

      
- Relationships—The `GeneralModels` relation
        connects the `GeneratorSet` type to its possible
        configurations (`GeneralModel`).

      
- Constraints—Constraints enforce critical business rules and safety standards, such
        as ensuring the selected generator model's power meets the required threshold, or
        restricting configuration options (such as `Voltage`)
        based on the specified compliance standards (`Listing-UL
          2200`).

=== ARTICLE: cml_constraints.htm ===
---
page_id: cml_constraints.htm
title: Constraints
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_constraints.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_cml_core_concepts.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Constraints

Constraints enforce rules and conditions on types, variables, and relationships. Use
    constraints to define logical restrictions and ensure consistency within the
    model.

    
      

For more information about the supported constraints, see:

      
        
- [Logical
            Constraints](./cml_logical_constraints.htm.md)

        
- [Table
            Constraints](./cml_table_constraints.htm.md)

        
- [Using Proxy Variables with Constraints on Types and Relationships](./cml_using_proxy_variables_constraints.htm.md)

        
- [Group Type](./cml_group_type.htm.md)

        
- [Message Rule](./cml_message_rule.htm.md)

        
- [Preference Rule](./cml_preference_rule.htm.md)

        
- [Require Rule](./cml_require_rule.htm.md)

        
- [Require Rule vs Constraint](./cml_require_rule_vs_constraint.htm.md)

        
- [SetDefault Rule](./cml_setdefault_rule.htm.md)

        
- [Exclude Rule](./cml_exclude_rule.htm.md)

        
- [Action Rule](./cml_action_rule.htm.md)

        
- [Hide/Disable Rule](./cml_hide_disable_rule.htm.md)

        
- [Recommendation Rule](./cml_recommendation_rule.htm.md)

        
- [Set Product Selling Model in a Constraint](./cml_set_product_selling_model_constraint.htm.md)

      

    

    

## Supported Logic Operators

      
      

These logic operators are supported in CML.

    

    

## Arithmetic Operators

      
      
        
- Multiplication (*)

        
- Division (/)

        
- Remainder (%)

        
- Addition (+)

        
- Subtraction (-)

      

    

    

## Relational Operators

      
      
        
- Greater than (>)

        
- Greater than or equal to (>=)

        
- Less than (<)

        
- Less than or equal to (<=)

      

    

    

## Equality Operators

      
      
        
- Equal (==)

        
- Not equal (!=)

      

    

    

## Logic Operators

      
      
        
- Not  (!)

        
- And  (&&)

        
- XOR/Exclusive or (^)

        
- Or (||)

        
- Bi-conditional (<->)

        
- Conditional (?:)

        
- Implication (->)

      

    

    

## Operator Precedence

      
      

In resolving equations, operator precedence determines the order in which operations are performed. Operators in CML have precedence in this order:

      
        
- Arithmetic operators have the first precedence.

        
- Relational operators have the second precedence.

        
- Equality operators have the third precedence.

        
- Logic operators have a lower precedence than equality operators, in decreasing order as listed, with Implication having the lowest precedence.

      

    

    

## Constraint Annotation

      
      

Here are the details of `abort`, a constraint
        annotation.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

          

        
| Annotation | Possible Values | Description |
| --- | --- | --- |
| abort | true, false | Specifies that, if this constraint fails, abort search and return `false` for configuration. |

    

  

- 
**[Logical Constraints](./cml_logical_constraints.htm.md)**  

A logical constraint defines a statement that must hold true logically. The constraint     can be any logical expression by using a logical operator.

- 
**[Table Constraints](./cml_table_constraints.htm.md)**  

The table constraint in Constraint Modeling Language (CML) is used to define a set of     valid combinations of values for two or more attributes. These combinations are specified in     rows within the constraint definition.

- 
**[Proxy Variables with Constraints on Types and Relationships](./cml_using_proxy_variables_constraints.htm.md)**  

Use proxy variables to reference the variables of related types, including parent,     root, and sibling types.

- 
**[Message Rule](./cml_message_rule.htm.md)**  

The message rule displays a message to users based on specified conditions.

- 
**[Preference Rule](./cml_preference_rule.htm.md)**  

The preference rule encourages the constraint solver to satisfy the condition, but     doesn't enforce it if the condition can't be met.

- 
**[Require Rule](./cml_require_rule.htm.md)**  

The require rule requires certain components to be included in a relationship when     specified conditions are met.

- 
**[Require Rule vs Constraint](./cml_require_rule_vs_constraint.htm.md)**  

In Constraint Modeling Language (CML), constraint() and require() can both enforce     behavior, but they operate differently: constraint focuses on logical consistency, require     focuses on physical presence of products.

- 
**[Setdefault Rule](./cml_setdefault_rule.htm.md)**  

The setdefault rule allows component selection with attribute values and quantity,     similar to the require rule.

- 
**[Exclude Rule](./cml_exclude_rule.htm.md)**  

The exclude rule automatically removes a specific type in a relationship if a certain     condition is true.

- 
**[Action Rule](./cml_action_rule.htm.md)**  

The CML Action Rule is defined using the rule() keyword. Its primary purpose is to     execute a designated action, specified as a string literal, when a condition is met.

- 
**[Hide or Disable Rule](./cml_hide_disable_rule.htm.md)**  

The Hide or Disable Rule uses the rule() keyword to conditionally remove an element     from the selection menu (hide) or preserve it in the menu while preventing user selection     (disable).

- 
**[Recommendation Rule](./cml_recommendation_rule.htm.md)**  

The recommend keyword is used within a Constraint Modeling Language (CML) rule to     display suggestions for related products in the Product Configurator. The rule defines the     condition under which a specific product type or relation should be suggested to the     user.

- 
**[Set Product Selling Model in a Constraint](./cml_set_product_selling_model_constraint.htm.md)**  

Use the productSellingModel tagname to write a constraint that sets the Product Selling     Model (PSM) for a type. You can define a PSM as one time, time-deferred (subscription with end     date), or evergreen (recurring subscription with no preset end date). The PSM is updated for new     line items at runtime, based on the constraint.

=== ARTICLE: cml_core_concept_examples.htm ===
---
page_id: cml_core_concept_examples.htm
title: Core Concept Examples
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_core_concept_examples.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Core Concept Examples

These examples illustrate core Constraint Modeling Language (CML) concepts including
    type, relationships, constraints, and so on.

    

For an explanation of the constraint model structure in these examples, see [Model
          Structure](./cml_appendix_model_structure.htm.md).

    

## Example 1: Use Regex Global Variable

      
      

```
// Global Constant: Regex used to parse voltage strings
define VOLTAGE_REGEX "^([11-19]+)/([11-19]+)$" 

type LineItem;
type GeneratorSet : LineItem {
   // Core attributes
   @(configurable = false)
   int requiredKW = [101..10000]; // Required power capacity
   string Voltage = ["220/380", "240/416", "277/480", "7976/13800"]; 
   string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];

   // Calculated attributes
   // Surge load is 1.25 times the required KW
   decimal(2) surgeLoadKW = requiredKW * 1.25; 
   // Voltage3 extracts the secondary voltage (e.g., 380 or 416) for checks
   int Voltage3 = strtoint(regexpreplace(Voltage, VOLTAGE_REGEX, "$2"), 0); 

   // Relation to model components 
   relation GeneralModels : GeneralModel[11]; 

   // Constraint 1: Ensure model capacity meets the required KW
   constraint(GeneralModels[GeneralModel].powerKW >= requiredKW, 
      "Selected Generator Model is insufficient for the required power."); 
   
   // Constraint 2: UL 2200 standard restricts voltage to 600V or less (Implication rule)
   constraint(standardsAndCompliance == "Listing-UL 2200" -> Voltage3 <= 600, 
      "The UL 2200 standard covers stationary engine generator assemblies rated at 600 volts or less.");
}

// Component type definition (GeneralModel is a product component)
type GeneralModel : LineItem {
   int powerKW = [900, 1200, 1500, 1750, 2500];
   int dB = [20..23];
}
```

    

    

## Key Technical Details

      
      

- The `GeneratorSet` type is related to the `GeneralModel` type through a single relation.

              
              
              
              
              
              
                
                  

                  

                  

                  

                  

                

              

              
                
                  

                  

                  

                  

                  

                

              

            
| Parent Type | Relation Name | Child Type | Cardinality | Key Attribute Usage |
| --- | --- | --- | --- | --- |
| `GeneratorSet` | `GeneralModels` | `GeneralModel` | Not Applicable | Constrained by `requiredKW` on the parent type. |

      

- Parent Type (`GeneratorSet`): Defined as a `LineItem` component, the `GeneratorSet` holds configuration parameters such as the user's power
          requirement (`requiredKW`), the specified voltage
            (`Voltage`), and compliance standards (`standardsAndCompliance`). It also includes calculated
          attributes like `surgeLoadKW` and `Voltage3`.

- Child Type (`GeneralModel`): Defined as a `LineItem` component, the `GeneralModel` specifies the technical attributes of the selected generator
          configuration, including its power output (`powerKW`)
          and noise rating (`dB`).

- Cardinality: The relation `GeneralModels : GeneralModel`
          specifies the quantity bounds for the component, indicating that exactly 11 instances of
          the `GeneralModel` type must be included in this
          configuration.

    

    

## Example 2: Use Groupby Annotation to Create Virtual Group

      
      

Using Groupby annotation for types, this model creates a virtual `VoltageGroup` for every unique voltage (for example,
        "220/380", "480/277") found in the transaction.

      

```
// 1. The physical product type
type GeneratorSet {
   @(configurable = false)
   int requiredKW = [101..10000];

   string Voltage = ["220/380", "240/416", "255/440", "277/480"];

   // Calculation with explicit domain for best practice
   decimal(2) surgeLoadKW = [126.25..12500.00];
   constraint(surgeLoadKW == requiredKW * 1.25);
}

// 2. The virtual container grouped by the "Voltage" attribute
@(split=true, virtual=true, groupBy=Voltage)
type VoltageGroup {
   string Voltage; // The attribute used for grouping
   decimal(2) groupTotalSurgeKW = [0.00..99999.99];

   // Map instances to this group from the transaction line items
   @(sourceContextNode="SalesTransaction.SalesTransactionItem")
   relation generators : GeneratorSet[0..50];

   // Aggregation: Sum only the surge load of generators in THIS voltage group
   constraint(groupTotalSurgeKW == generators.sum(surgeLoadKW));

   // Business Rule: Limit total surge load per voltage branch
   message(groupTotalSurgeKW > 10000, "Warning: Surge load for Voltage {} exceeds branch capacity!", Voltage);
}

// 3. The top-level system managing the groups
@(virtual = true)
type GeneratorSystem {
   relation generators : GeneratorSet[0..100];
   relation voltageGroups : VoltageGroup[1..10];

   decimal(2) systemTotalKW = voltageGroups.sum(groupTotalSurgeKW);
}
```

    

    

## Key Technical Details

      
      

- 
`groupBy=Voltage`: The engine scans all `GeneratorSet` instances and creates one virtual `VoltageGroup` for each unique voltage value detected (for
          example, one group for all "220/380" units, another for all "277/480"
          units).

- 
`sourceContextNode`: This tells the virtual group to pull its
          "children" (the generators) from the specific path in the Salesforce context
          where quote line items are stored.

- Bottom-Up Aggregation: Each `VoltageGroup` independently
          calculates its `groupTotalSurgeKW` based strictly on
          the generators assigned to it by the groupBy logic.

- Explicit Domains: Following best practices, the `surgeLoadKW`
          and `groupTotalSurgeKW` use explicit domains (for
          example, [0.00..99999.99]) to prevent "NullPointer" or initialization errors
          during solving.

    

    

## Example 3: Use Sharingcount Annotation to Reuse Accessory Instances

      
      

In this example, we apply sharingcount annotation to the `Accessory` type to allow the engine to reuse accessory instances across the
        configuration up to a specified limit.

      

```
// 1. Define the component type with split and sharingCount
// split=true enables parallel solving by splitting quantity into multiple instances
// sharingCount=5 allows a single Accessory instance to be reused 5 times in the model
@(split = true, sharingCount = 5)
type Accessory {
   string category;
   decimal(2) weight;
}

type GeneratorSet {
   @(configurable = false)
   int requiredKW = [101..10000];

   // 2. Define the relationship with the sharing annotation
   // @(sharing = true) allows the engine to satisfy this relation by 
   // "pointing" to existing instances instead of creating new ones 
   @(sharing = true)
   relation Accessories : Accessory[1..99];
}
```

    

    

## Key Technical Details

      
      

- Parallel Solving: By setting `split = true`, the engine can
          process the 99 possible accessories in parallel rather than sequentially, which is
          critical for large-scale generator configurations.

- Resource Management: The `sharingCount = 5` tells the solver
          that it doesn't need to instantiate 99 unique `Accessory` objects; it can reuse the same object definition up to five times
          across different parts of the configuration graph.

- Relationship Requirement: For `sharingCount` to take effect,
          the Relation (the port) must also be annotated with `@(sharing
            = true)` to grant the engine permission to reuse instances.

    

    

## Example 4: Use contextPath and tagName Annotations

      
      

```
// 1. GLOBAL EXTERN DECLARATIONS
// Unifying contextPath (header field) and tagName (context identifier)
@(contextPath = "SalesTransaction.ShippingCountry", tagName = "Region_Identifier")
extern string ShippingCountry = "International";

@(contextPath = "SalesTransaction.ProjectUrgency", tagName = "Priority_Level")
extern string ProjectUrgency = "Standard";

// 2. PHYSICAL PRODUCT TYPE
type GeneratorSet {
   // Core technical attributes
   @(configurable = false)
   int requiredKW = [101..10000];

   string DutyRating = ["Prime Power (PRP)", "Emergency Standby Power (ESP)"];
   
   // Technical calculation with explicit domain (Best Practice)
   decimal(2) surgeLoadKW = [126.25..12500.00]; 
   constraint(surgeLoadKW == requiredKW * 1.25);

   // 3. LOGIC INTEGRATING EXTERNAL DATA
   // Using contextPath/tagName data to drive technical warnings
   message(ShippingCountry == "US", 
           "Regional Notice: Generator must comply with US-specific UL 2200 standards.");

   message(ProjectUrgency == "Critical" && requiredKW > 5000, 
           "High Priority Alert: Large scale power requirement in a Critical project requires site inspection.", 
           requiredKW, "Warning"); 
}
```

    

    

## Key Technical Details

      
      

- External Variable (`extern`): These are declared outside of
          any type to hold values supplied by the environment (Salesforce).

- 
`contextPath` Annotation: This maps the variable directly to
          a header-level field in the Sales Transaction.

- 
`tagName` Annotation: This links the variable to a specific
          Context Tag identifier within the Salesforce Context Definition.

      

#### Note

Rules depending on these external variables (such as the `ShippingCountry` message) only re-evaluate when a Line Item
        change occurs (For example, updating `requiredKW`), not
        solely when the header field changes.

    

    

## Example 5: Use Format Specifiers (%s, %d) and Dates in Constraints

      
      

In this example, we define a generator configuration that validates the required power
          (`requiredKW`) against the duty rating and voltage,
        providing specific feedback when a mismatch occurs.

      

```
type GeneratorSet  {
   // 1. Core Technical Attributes with explicit domains
   @(configurable = true)
   int requiredKW = [101..10000];

   string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)",
                        "Data Center Continuous (DCC)", "Emergency Standby Power (ESP)"];

   string Voltage = ["220/380", "277/480", "347/600", "2400/4160"];

   string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];

   // Date Attribute Definition
   // Date variables represent a specific day.
   // You can define a fixed domain for a date as a range between two dates.
   date requestedDeliveryDate = ["2024-01-01".."2025-12-31"];

   // Message Rule with Multiple Arguments using placeholders
   message(requiredKW > 5000 && DutyRating == "Emergency Standby Power (ESP)",
           "High Capacity Alert: The %s rating for %d kW requires an additional cooling system.",
           DutyRating, requiredKW, "Warning");

   // Constraint with Multiple Arguments using placeholders
   constraint(Voltage == "2400/4160" && standardsAndCompliance == "Listing-UL 2200",
              "Configuration Error: Voltage %s cannot be used with %s standards due to safety limits.",
              Voltage, standardsAndCompliance);

   // Dates can be used in logical expressions with comparison operators like < or >=.
   message(requestedDeliveryDate < "2024-09-01" && requiredKW > 7000,
           "Schedule Warning: Delivery for %d kW units on %s may require expedited manufacturing.",
           requiredKW, requestedDeliveryDate, "Info");
}
```

    

    

## Key Technical Details

      
      

- Multiple Arguments: You can pass several variables after the string literal. The engine maps them to the placeholders in the exact order they appear.

- Format Specifiers

- 
`%s` is used for string variables (for example, `DutyRating` or `Voltage`).

- 
`%d` is used for integer variables (for example, `requiredKW`).

- Placeholder Usage: Alternatively, you can use the {} syntax, which the constraint engine automatically replaces with the actual argument values during runtime evaluation.

- Comparison Logic with Dates: You can treat dates as comparable values in `constraint` or `message`
          rules to enforce scheduling logic (for example, ensuring a delivery date is not too early
          for a complex build).

    

    

## Example 6: Use Arithmetic Calculations and Functions

      
      

This example demonstrates using aggregate functions (a virtual type for transaction-level
        aggregation) and mathematical functions within the `GeneratorSet` type for precise quantity calculation.

      

```
// --- Component Definition —
type GeneratorSet  {
    int requiredKW = [101..10000];
    int quantity = [1..10]; 
    // BEST PRACTICE: Define derived attributes with an explicit domain
    decimal(2) surgeLoadKW = [0.00..12500.00]; 
    // BEST PRACTICE: Put calculations inside of constraints
    constraint(surgeLoadKW == requiredKW * 1.25);
}
// --- Accessory Definition ---
type Accessory  {
    int weight_kg = [1..100];
}
// --- Virtual System Type (Aggregation Context) ---
@(virtual = true)
type System {
    @(sourceContextNode = "SalesTransaction.SalesTransactionItem")
    relation generators : GeneratorSet[0..10];
	relation shipmentbatch : ShipmentBatch [0..10];
    // BEST PRACTICE: Attributes must have explicit domains
    decimal(2) totalQuotedLoad = [0.00..125000.00];
    int highPowerCount = [0..10];
    // Aggregate calculations in separate constraints
    constraint(totalQuotedLoad == generators.sum(surgeLoadKW));
    // VARIATION: Condition-based count
    // count() requires a logical expression 
    constraint(highPowerCount == generators.count(requiredKW > 5000));
    // Ensuring Shipment batch crates are similar to the number of generators
    message(
        shipmentbatch.requiredCrates != generators[GeneratorSet], 
        "The Shipment items ({}) must match the number of Generators ({})", 
        shipmentbatch.requiredCrates, generators[GeneratorSet], 
        "Error"
    );
}
type ShipmentBatch {
    int totalItems = [1..100];
    int itemsPerCrate = 10;
    // BEST PRACTICE: Define derived attributes for the relation in the parent type
    int totalWeight = [0..1000];
    int accessoryCount = [0..10];
    // Aggregates within the relation block
    relation accessories : Accessory[0..10] {
        accessoryWeight = sum(weight_kg); 
        accessoryCount = count(weight_kg > 0); 
    }
    // Mapping relation attributes to parent variables via constraints
    constraint(totalWeight == accessories.accessoryWeight);
    constraint(accessoryCount == accessories.accessoryCount);
    int requiredCrates = [0..100];
    // Mathematical Function Example: CEIL
    constraint calculateCeil(requiredCrates == ceil(totalItems / itemsPerCrate));
}
```

    

    

## Key Considerations for Calculations and Aggregations

      
      

When implementing these functions in CML, follow these architectural best practices for robustness and performance.

      

- Explicit domains are required: All the derived attributes that result from a calculation or aggregation must have an explicit variable domain definition. This practice ensures accurate aggregation and helps prevent runtime errors.

- Separate calculation from declaration: Define the aggregation or calculation in a separate
          constraint rather than using an inline derived attribute declaration (for example, `int total = items.sumPrice;`). This separation helps avoid
          issues where domains may not initialize correctly.

- Correct Pattern: Define the relation aggregate (`totalQty =
            sum(quantity);`) and then enforce the result via a constraint (`constraint(totalItemCount == items.totalQty);`).

    

    

## Example 7: Use Asset-Based Constraints Across Transaction and Installed Base

      
      

This example shows how to enforce quantity rules that span both in-flight items on the
        current sales transaction and products the customer already owns (the installed base). The
          `sourceContextNode="Asset"` annotation on a relation
        pulls existing asset records into the model as read-only data, so that a `require()` rule can combine those asset quantities with
        in-transaction quantities to drive configuration logic.

      

```
// 1. Top-level virtual type that organizes generator sets by fuel type
@(virtual=true)
type ServiceOrder {
  relation groups : GeneratorGroup;
}

// 2. Virtual group type: the engine creates one GeneratorGroup instance
// for each unique FuelType value found in the sales transaction
@(virtual=true, groupby=FuelType)
type GeneratorGroup {

  // In-flight generator sets on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation generators : GeneratorSet;
  constraint(generators[GeneratorSet] < 10, "Generator qty should be less than 10");
  constraint(generators[GeneratorSet].Discount > 10 && generators[GeneratorSet].Discount < 20,
             "Discount should be between 10 and 20");

  // In-flight heaters on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation heaters : Heater;

  // Existing heaters retrieved from the customer's installed base (Assets)
  // closerelation=true prevents the engine from adding new records to this relation
  @(sourceContextNode="Asset", closerelation=true)
  relation heaterAssets : Heater;

  // Asset-based require rule: when combined in-flight and installed heater
  // quantity exceeds 10, exactly 100 generator sets are required
  require(heaters[Heater] + heaterAssets[Heater] > 10, generators[GeneratorSet] == 100);
}

// 3. Physical product types
type GeneratorSet {
  string FuelType = ["Natural Gas", "Diesel", "Propane"];
  decimal Discount = [0..100];
}

type Heater {
  boolean AutoIgnition;
}
```

    

    

## Key Technical Details

      
      
        
- 
`sourceContextNode="SalesTransaction.SalesTransactionItem"`:
          Binds the relation to line items on the current quote or order. The engine reads and writes
          these instances during configuration.

        
- 
`sourceContextNode="Asset"`: Binds the relation to
          asset records that represent products the customer already owns from prior transactions.
          These records exist outside the current transaction and are treated as read-only context
          data.

        
- 
`closerelation=true`: Required on asset-sourced
          relations to prevent the engine from attempting to add new instances to the installed base.
          Without this annotation, the engine may try to create asset records to satisfy cardinality
          or require rules.

        
- Asset-based `require()`: The rule `require(heaters[Heater] + heaterAssets[Heater] > 10,
            generators[GeneratorSet] == 100)` combines cardinality from two separate
          relations — one sourced from the transaction and one from the installed base — in a single
          logical expression. This lets the model enforce quantity thresholds that account for what
          the customer is buying now and what they already have.

        
- Virtual grouping: The `groupby=FuelType` annotation
          on `GeneratorGroup` ensures that the asset-based
          constraint is evaluated independently per fuel type, so heaters and generator sets of
          different fuel types do not count toward each other's totals.

      

    

    

## Example 8: Use Asset Scope to Drive Auto-Add Logic

      
      

These examples show how to use the installed base (existing customer assets) as a condition
        in a `require()` rule to automatically add products to
        the current quote. The positive asset check triggers an auto-add when the customer already
        owns a product. The negative asset check enforces a prerequisite product when the customer
        does not yet own it.

      

Positive asset check: if the customer already owns at least one `GeneratorSet` in their installed base, the engine automatically adds a `MaintenanceKit` to the current quote.

      

```
@(virtual=true)
type ServiceOrder {
  // In-flight generator sets on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation generators : GeneratorSet;

  // Existing generator sets from the customer's installed base (read-only)
  @(sourceContextNode="Asset", closeRelation=true)
  relation generatorAssets : GeneratorSet;

  // In-flight maintenance kits on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation maintenanceKits : MaintenanceKit;

  // Positive asset check: customer already owns a GeneratorSet,
  // so automatically require a MaintenanceKit on the quote
  require(generatorAssets[GeneratorSet] >= 1, maintenanceKits[MaintenanceKit]);
}

type GeneratorSet;
type MaintenanceKit;
```

      

Negative asset check: if the customer does not yet own a `GeneratorSet` in their installed base but is adding more than one `MaintenanceKit` to the quote, the engine requires a `GeneratorSet` to also be added to the quote.

      

```
@(virtual=true)
type ServiceOrder {
  // In-flight generator sets on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation generators : GeneratorSet;

  // Existing generator sets from the customer's installed base (read-only)
  @(sourceContextNode="Asset", closeRelation=true)
  relation generatorAssets : GeneratorSet;

  // In-flight maintenance kits on the current sales transaction
  @(sourceContextNode="SalesTransaction.SalesTransactionItem")
  relation maintenanceKits : MaintenanceKit;

  // Negative asset check: customer does not own a GeneratorSet yet,
  // but is adding more than one MaintenanceKit, so require a GeneratorSet on the quote
  require(generatorAssets[GeneratorSet] < 1 && maintenanceKits[MaintenanceKit] > 1, generators[GeneratorSet]);
}

type GeneratorSet;
type MaintenanceKit;
```

    

    

## Key Technical Details

      
      
        
- Positive asset check (`generatorAssets[GeneratorSet] >=
            1`): Evaluates to true when the installed base contains at least one matching
          asset. Use this pattern to trigger upsell or companion-product logic for existing
          customers.

        
- Negative asset check (`generatorAssets[GeneratorSet] <
            1`): Evaluates to true when the customer has no matching asset. Use this pattern
          to enforce a prerequisite product for net-new buyers.

        
- Auto-add result: When the `require()` condition is
          met, the engine adds the specified product to the relation automatically. Passing only the
          relation and type without a quantity (`maintenanceKits[MaintenanceKit]`) requires exactly one instance. Append `== N` to require a specific quantity.

        
- 
`closeRelation=true` is required on the asset
          relation to prevent the engine from attempting to write back to the installed base when
          evaluating the condition.

=== ARTICLE: cml_debugging_cml.htm ===
---
page_id: cml_debugging_cml.htm
title: Debugging Constraint Modeling Language (CML)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_debugging_cml.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_what_is_constraint_modeling_language.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Debugging Constraint Modeling Language (CML)

To debug constraint models and troubleshoot performance issues, enable debug logging in
    Apex and set the debug log level to FINE.

    

For more information on debug logging in Salesforce, see these topics in Salesforce Help:

    

- [Set Up Debug Logging](https://help.salesforce.com/s/articleView?id=xcloud.code_add_users_debug_log.htm&language=en_US)

      
- [Debug Log](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/apex_debugging_debug_log.htm)

      
- [Debug Log Levels](https://help.salesforce.com/s/articleView?id=platform.code_setting_debug_log_levels.htm&language=en_US)

    

Use the Apex log to get information about configurator engine performance when running a constraint model, including performance degradation or unexpected behavior. To improve performance, modify the constraint model based on information in the log.

    

For tips on writing trouble-free CML, see [Constraint Modeling Language (CML) Best
        Practices](./cml_cml_best_practices.htm.md).

  

- 
**[About the Apex Debugging Log File](./cml_about_the_apex_debugging_log_file.htm.md)**  

The Apex debugging log file contains three sections: RLM_CONFIGURATOR_BEGIN,     RLM_CONFIGURATOR_STATS, and RLM_CONFIGURATOR_END.

- 
**[Use the Apex Debugging Log File](./cml_use_the_apex_debugging_log_file.htm.md)**  

To find possible reasons for the performance problems and identify solutions, look at     the RLM_CONFIGURATOR_STATS section of the log file.

=== ARTICLE: cml_exclude_rule.htm ===
---
page_id: cml_exclude_rule.htm
title: Exclude Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_exclude_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Exclude Rule

The exclude rule automatically removes a specific type in a relationship if a certain
    condition is true.

    
      

The exclude rule has this syntax.

      

```
exclude(logic expression, relationship[type],"Explanation message");
```

      

The type must be leaf type, a node without children.

      

In the exclude rule, if a user sets attribute values in Product Catalog Management (PCM)
        that violate the rule requirements, the constraint engine overrides the user input in order
        to validate the constraint. This behavior is different than other constraints, in which the
        constraint engine doesn't override user input, but displays an error if user input
        violates the constraint. See How User Input Order Affects Constraint Engine Behavior section
        in [Logical Constraints](./cml_logical_constraints.htm.md).

      

In this example, the exclude rule automatically removes the `Heater_120` heater from the type `GeneratorSet` if the `Voltage3` is greater
        than or equal to `4160`.

      

```
type GeneratorSet {
int Voltage3 = [120..13800];
relation Heaters : Heater_120 [1..3];
exclude(Voltage3 >= 4160, Heaters[Heater_120]);
}
type Heater_120 {}
```

    

    

## Exclude a Child Product Based on Another Child
        Product's Attribute

When a bundle contains multiple child products, you can
        exclude one child product based on an attribute value set on a sibling child product. To
        evaluate a child product's attributes from the parent scope, use the `count()` aggregate function on the parent's relation. The
          `count()` function inspects instances within a relation
        and counts those that match a given condition. When the count is greater than zero, at least
        one child instance satisfies the condition, and the exclude rule acts on that
        result.

Use this
        pattern.

```
exclude(<relation>.count(<ChildType>.<attribute> == <value>) > 0, <otherRelation>[<OtherChildType>], "Explanation message");
```

In
        this example, the `GeneratorSet` bundle contains both
          `Heater` and `StandardCooler` child products. If any `Heater` in the configuration has an `outputClass` of `High-Output`, the `StandardCooler` is automatically excluded because high-output
        heaters require an industrial-grade
      cooler.

```
type Heater {
string outputClass = ["Standard-Output", "High-Output"];
}
type StandardCooler {}
type GeneratorSet {
relation Heaters : Heater[0..10];
relation Coolers : StandardCooler[0..5];
exclude(Heaters.count(Heater.outputClass == "High-Output") > 0, Coolers[StandardCooler],
  "High-output heaters require an industrial cooler, not a standard cooler.");
}

```

=== ARTICLE: cml_external_variables.htm ===
---
page_id: cml_external_variables.htm
title: External Variables
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_external_variables.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# External Variables

External variables are global Constraint Modeling Language (CML) variables defined
    within a virtual CML type.

See virtual in [Type Annotations](./cml_type_annotations.htm.md). The values for external variables are usually set by the
        environment that launches the constraint solver engine. Use external variables to import
        runtime data from the context header (such as Quote or Sales Transaction) into the
        configuration model, with the contextPath annotation to denote header fields, or with
        tagName annotation to denote lineItem fields. See External Variable Annotations section.

If the external variable isn't mapped to any
        external data source, it must have a default value. Otherwise, it may remain unbound and
        cause errors.

Here's a basic declaration
      syntax.

```
extern int MAX_VALUE = 9999;
extern decimal(2) threshold = 1.5;
```

    

## Example: Using External Variables with Context Path Annotation

      
      

In this example, the constraint engine needs access to the quote header (Sales Transaction)
        field, which defines the shipping location to enforce region-specific compliance
        requirements. The `contextPath` annotation is used to map
        the field (`SalesTransaction.ShippingCountry`) to an
        external CML variable (`ShippingCountry`).

      

#### Note

The CML variable name can be different from the context path value.

      

```
// External variable declaration with context path annotation
@(contextPath = "SalesTransaction.ShippingCountry")
extern string ShippingCountry; // ShippingCountry Value is pulled from the Quote/Order header
```

      

See the full example in [Using ContextPath and tagName annotations](./cml_core_concept_examples.htm.md).

    

    

## External Variable Annotations

      
      

Here are the details of external variable annotations.

    

    

        
        
        
        
          
            

            

            

          

        

        
          
            

            

            

          

        

      
| Annotation | Possible Value | Description |
| --- | --- | --- |
| contextPath | "SalesTransaction.<ST_FIELD>", where the sales transaction field is pulled directly from the context definition. | References sales transaction values directly from their context definition, such as account name, sales transaction total, or address. The contextPath annotation can only be used for header fields. To create a variable linked to a SalesTransactionItem, use the tagName annotation to reference context tags on SalesTransactionItem within a type. See tagName in [Variable Annotations](./cml_variable_annotations.htm.md). |

=== ARTICLE: cml_global_properties_and_settings.htm ===
---
page_id: cml_global_properties_and_settings.htm
title: Global Properties and Settings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_global_properties_and_settings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_cml_core_concepts.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Global Properties and Settings

Header-level declarations define the global properties and settings for a model, including
    constants, properties, and external values that set up the foundation of the CML code.

    

Use these declarations to create reusable components and configuration settings that you can
      reference throughout the model.

    

## Global Constants

      
      

Use global constants to define values that remain fixed throughout the model. These
        constants can be numeric values, strings, lists, or other supported data types. Use
        constants to create standardized settings or options that you can reference multiple times.
        See [Example 1: Use Regex Global Variable](./cml_cml_core_concepts.htm.md).

      

In the example, `MAX_COUNT` is a global constant that is
        hard-coded to `100: define MAX_COUNT 100`.

      

Regex (regular expressions) can be used to define global constants. The generalized
        abstract syntax structure for regex expressions is define `<CONSTANT_NAME> "^<REGEX_PATTERN_STRING>$"`.

    

    

## Regex Pattern Components

      
      

This table lists regex components and their details.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Regex Component | Description | Generalization |
| --- | --- | --- |
| ^ and $ | Anchors that ensure the pattern matches the entire string, from the beginning (^) to the end ($). | Ensures strict adherence to the required format. |
| () | Capturing Groups used to isolate portions of the matched string. You can reference the captured parts later by using $1, $2, and so on, in functions such as regexpreplace. See [String Variable Functions and Operators](./cml_string_variable_functions_and_operators.htm.md). | Allows extraction of specific data fields from a string. |
| + | Character Class and Quantifier that matches one or more (+) digits or characters. | Defines the permitted characters and minimum occurrences for the data fields. |
| / | Literal Character matching the forward slash separator present in the input data. | Matches fixed delimiters in the input string. |

      

In the example, `VOLTAGE_REGEX` is a global constant
        that defines a fixed regular expression pattern used for validation or parsing throughout
        the model define `VOLTAGE_REGEX
        "^([0-9]+)/([0-9]+)$"`.

      

For more on the usage of global properties, see [External
        Variables](./cml_external_variables.htm.md).

=== ARTICLE: cml_group_type.htm ===
---
page_id: cml_group_type.htm
title: Group Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_group_type.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_types.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Group Type

In Constraint Modeling Language (CML), a Group Type is used to logically containerize
    related components within a bundle configuration, primarily when product component groups are
    imported from Product Catalog Management (PCM).

    
      

The Group Type uses specific annotations to control the total quantity of components
        selected from that group, regardless of the individual component type.

      

Bundles and Group Types (also known as Product Component Groups or PCGs) represent different levels of a product hierarchy and serve distinct functional roles in configuration logic.

    

    

## Conceptual Hierarchy

      
      
        
- Bundles are high-level parent products that contain multiple child products sold together as a package. In CML, they are defined as "root types" that encapsulate the properties, relationships, and constraints for the entire entity.

        
- Group Types are structural containers within a bundle. They act as intermediate folders that organize related components imported from Product Catalog Management (PCM). Instances of these Group Types are declared as variables inside the root Bundle type.

      

    

    

## Role in Cardinality and Selection

      
      
        
- Bundles establish the primary relationship between a root product and its broad categories of components.

        
- Group Types are specifically designed to enforce cardinality rules for a collection of
          products. They use the `@(minInstanceQty)` and `@(maxInstanceQty)` annotations to control exactly how many
          instances can be selected from a specific set of options (for example, "select at
          least 1 but no more than 2 accessories"). While the selected component can have a
          high quantity, the Group Type restricts the number of unique instances chosen from that
          group.

      

    

    

## Syntactic Implementation

      
      
        
- Accessing Components: For standard bundles, you reference components directly via their
          relation name. For components within a Group Type, you must use dot notation starting with
          the group variable name defined in the root type (for example, `accessoryGroup.mouse.Wireless == true`).

        
- Constraint Limitations: You cannot write a constraint directly on a Group Type's attribute to apply it to all components within that group; constraints must reference the specific child components.

        
- Identification: Group Types are automatically identified by a Group suffix and the presence of instance cardinality annotations during the import from PCM.

      

      

#### Note

The following examples are partial. See the complete code in the final CML
        code sample.

    

    

## Example 1: Defining Generator Set Group Types

      
      

We can define two group types for a Generator Set configuration: `CoreModelGroup` (mandatory selection of a primary generator
        model) and `EnclosureGroup` (optional selection of a
        specific enclosure type).

      

For the `CoreModelGroup`, setting `minInstanceQty` to 1 and `maxInstanceQty` to 1 means that at least 1 is required, and a maximum of 1 is
        permitted.

      

```
@(minInstanceQty=1, maxInstanceQty=1)
type CoreModelGroup {
// Relation holds the actual Generator Model products
relation generalModel : GeneralModel[0..9999];
}
type GeneralModel : LineItem {
int powerKW;
}
```

      

For the `EnclosureGroup`, setting `minInstanceQty` to 0 and `maxInstanceQty` to 1 means that selecting an enclosure is optional, but if
        selected, the user can add at most one instance of an enclosure component (such as
        WeatherproofEnclosure).

      

```
@(minInstanceQty=0, maxInstanceQty=1)
type EnclosureGroup {
relation enclosure : Enclosure;
relation cabinetHeater : ControlCabinetHeater;
}
type Enclosure : LineItem;
type ControlCabinetHeater : LineItem;
```

    

    

## Example 2: Referencing Group Types in the Root Bundle

      
      

Once defined, instances of these group types are used as variables within the root type,
        which represents the entire bundle. In this example, the `coreModelGroup` and `enclosureGroup` are
        instances of the respective group types, defined within the root type `GeneratorSetBundle`.

      

```
type GeneratorSetBundle {
CoreModelGroup coreModelGroup;
EnclosureGroup enclosureGroup;
}
```

    

    

## Example 3: Writing Constraints on Group Components

      
      

To write constraints or rules that reference components inside a group, use dot notation starting with the group variable name defined in the root type.

      

This example shows how a constraint might be defined within the `GeneratorSetBundle` type to enforce business logic on components within the
        groups.

      

```
// If the selected generator model has a powerKW greater than 1500,
// then a Control Cabinet Heater must be included in the Enclosure Group.
constraint(coreModelGroup.generalModel.powerKW > 1500 ->
enclosureGroup.cabinetHeater[ControlCabinetHeater] == 1);
// Require an Enclosure component if the set requires seismic certification.
require(seismicCertification == "IBC Seismic Certification",
enclosureGroup.enclosure[Enclosure],
"Enclosure required for seismic certification");
```

    

    

## Final CML Code Sample with Group Types

      
      

This structure defines the complete model, showing the component hierarchy and the relationship constraints.

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Parent Type | Relation Name | Child Type | Cardinality | Key Attribute Usage |
| --- | --- | --- | --- | --- |
| `GeneratorSetBundle` | `coreModelGroup` (Group Instance) | `CoreModelGroup` | Group Cardinality: 1 | The group type defined by `@minInstanceQty=1, maxInstanceQty=1`. This enforces that exactly one component choice must be made from the internal generalModel relation. |
| `GeneratorSetBundle` | `enclosureGroup` (Group Instance) | `EnclosureGroup` | Group Cardinality: [0..1] | The group type defined by `@minInstanceQty=0, maxInstanceQty=1`. This enforces that selecting components from this group is optional (min 0) and at most one total component instance can be selected (max 1). |

      

```
/**
* The Root Bundle: GeneratorSetBundle
* This type holds instances of the defined Group Types and the definition of seismic certification */
type GeneratorSetBundle {
string seismicCertification = ["IBC Seismic Certification", "OSHPD Seismic Certification"];
CoreModelGroup coreModelGroup;
EnclosureGroup enclosureGroup;
// Constraint 1: If the selected GeneralModel has a powerKW greater than 1500,
// then a Control Cabinet Heater must be included in the Enclosure Group.
constraint(coreModelGroup.generalModel.powerKW > 1500 ->
enclosureGroup.cabinetHeater[ControlCabinetHeater] == 1);
// Constraint 2: Require an Enclosure component if the set requires seismic certification.
require(seismicCertification == "IBC Seismic Certification",
enclosureGroup.enclosure[Enclosure],
"Enclosure required for seismic certification");
// Action Rule Example: Disable a specific enclosure type if the core model is low power (e.g., 900kW).
rule(coreModelGroup.generalModel.powerKW == 900, "disable", "relation",
"enclosureGroup.enclosure", "type", "ReinforcedEnclosure");
}
/**
* Group Type 1: Core Model Group (Mandatory, Single Select)
* Min/Max Instance Quantity controls the selection rules for components within this group.
*/
@(minInstanceQty=1, maxInstanceQty=1)
type CoreModelGroup {
// Relation holds the actual Generator Model products
relation generalModel : GeneralModel[0..9999];
}
/**
* Group Type 2: Enclosure and Accessories Group (Optional)
* minInstanceQty=0 means selection is optional. maxInstanceQty=1 limits the selection to a single enclosure or accessory component instance.
*/
@(minInstanceQty=0, maxInstanceQty=1)
type EnclosureGroup {
relation enclosure : Enclosure;
relation cabinetHeater : ControlCabinetHeater;
}
/**
* Component Types (Children)
*/
type GeneralModel {
int powerKW;
}
type Enclosure {
@(defaultValue = "false")
boolean Weatherproof;
}
type ReinforcedEnclosure : Enclosure; // Subtype of Enclosure
type ControlCabinetHeater;
```

    

    

## Key Considerations

      
      

When reviewing Group Types in the context of the Generator Set model, keep these architectural points in mind.

      
        
- Group Cardinality Enforcement: The annotations `@(minInstanceQty)` (minimum instance quantity) and `@(maxInstanceQty)` (maximum instance quantity) are defined on the Group Type
          itself (`ElectricalSafetyGroup`). These annotations
          control the overall cardinality for all the components contained within that group,
          regardless of the individual relation cardinality defined (for example `[0..1]`, `[1..2]`).

        
- Root Reference: The `GeneratorSetBundle` includes the
          groups as variables (`coreModelGroup` and `enclosureGroup`).

        
- Constraint Syntax for Group Components: Constraints access attributes or components
          inside the groups using dot notation starting with the group variable name (for example,
            `coreModelGroup.generalModel.powerKW`).

        
- Limitation on Group Attributes: You cannot write a constraint directly on a group's
          attribute and expect it to apply to all components within that group (for example, `constraint(enclosureGroup.color == "Black")`) is
          not a valid constraint).

=== ARTICLE: cml_hide_disable_rule.htm ===
---
page_id: cml_hide_disable_rule.htm
title: Hide or Disable Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_hide_disable_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Hide or Disable Rule

The Hide or Disable Rule uses the rule() keyword to conditionally remove an element
    from the selection menu (hide) or preserve it in the menu while preventing user selection
    (disable).

    
      

This functionality can be applied.

      
        
- On a bundle, hide a component to remove it from the selection menu, or disable a component to preserve it in the menu but prevent users from selecting options for it.

        
- On an individual product, hide an attribute to remove it from the selection menu, or disable an attribute to preserve it in the menu but prevent users from selecting options for it.

        
- On an attribute, hide or disable an attribute value to preserve it in the menu but prevent users from selecting options for it. For attribute values, the hide and disable rules have the same behavior.

      

      

#### Note

In Visual Builder in Salesforce, for attribute values, only the hide rule is
        enabled. When you apply the hide rule to an attribute value in Visual Builder, the value
        appears in the menu but selections are disabled.

      

The hide and disable rules use this syntax, where `action` is replaced by either `hide` or
          `disable`.

      

```
rule(logic expression, action, actionScope, actionTarget)
rule(logic expression, action, actionScope, actionTarget, actionClassification, actionValueTarget)

```

    

    

## Example: Hiding and Disabling Features

      
      

In the example in this section, rules rely on specific variables to define the scope and target of the action.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Variable in Rule | Purpose | Example from Generator Set | Description |
| --- | --- | --- | --- |
| `logic expression` (Declaration) | Condition upon which the rule occurs. | `requiredKW <= 500` | The logical test that triggers the action. |
| `action` | Designates whether the rule is hide or disable. | `"hide", "disable"` | Determines if the element is removed from view or made unselectable. |
| `actionScope` | Designates whether the rule acts on an attribute or relation scope. | `"attribute", "relation`" | Specifies if the target is a variable property or a component relationship. |
| `actionTarget` | Designates the specific variable or relation that the rule acts on. | `"Voltage", "StarterMotors"` | The Constraint Modeling Language (CML) name of the attribute or relation. |
| `actionClassification` | Designates whether the rule acts on a type or a value. | `"type", "value"` | Used when targeting components within a relation (type) or specific options within an attribute domain (value). |
| `actionValueTarget` | Designates the specific type or value that the rule acts on. | `"7976/13800", "StarterMotor_Advanced"` | The specific string value or type name to hide or disable. |

      

```
// --- Component Definitions (For relations referenced below) ---
type LineItem;
type EngineModel : LineItem;
type StarterMotor : LineItem;
type OutputTerminal : LineItem;
type OutputTerminals2HoleLugNEMA : OutputTerminal; // Specific terminal type
type GeneratorSet : LineItem {
// Attributes subject to hide/disable rules
int requiredKW = [101..10000];
string Voltage = ["220/380", "240/416", "4160/7200", "7976/13800"]; // Voltage is the attribute being hidden/disabled
string specialApplication = ["None - Standard", "Motor Starting"]; // specialApplication attribute contains a value to hide
// Relations subject to hide/disable rules
relation StarterMotors : StarterMotor; // Relation target (component) to hide/disable
relation OutputTerminals : OutputTerminal[0..99]; // Relation being acted upon
// 1. Disable a Component (Type) in a Relation
// If requiredKW is too low (<= 500 kW), the advanced starter motor component is disabled (visible but unselectable).
rule(
requiredKW <= 500,
"disable",
"relation",
"StarterMotors",
"type",
"StarterMotor_Advanced"     );
// 2. Hide an Attribute
// If the Generator is configured for a special purpose (Motor Starting), hide the Voltage attribute entirely.
rule(
specialApplication == "Motor Starting",
"hide",
"attribute",
"Voltage"
);
// 3. Hide a Specific Attribute Value
// If the power requirement is low (< 2000 kW), hide the high voltage option (7976/13800) from the Voltage attribute domain.
rule(
requiredKW < 2000,
"hide",
"attribute",
"Voltage",
"value",
"7976/13800"
);
// 4. Disable a Component Type (Alternate Syntax using the component name)
// Disable the OutputTerminals2HoleLugNEMA component if the required KW is high.
rule(
requiredKW >= 5000,
"disable",
"relation",
"OutputTerminals",
"type",
"OutputTerminals2HoleLugNEMA"
);
}
type StarterMotor_Advanced : StarterMotor; // Subtype used in the rule
```

=== ARTICLE: cml_logical_constraints.htm ===
---
page_id: cml_logical_constraints.htm
title: Logical Constraints
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_logical_constraints.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Logical Constraints

A logical constraint defines a statement that must hold true logically. The constraint
    can be any logical expression by using a logical operator.

    

For example, the statement `c0 ? c1 : c2` means that if
        `c0` is true, then `c1` needs to be true, otherwise `c2` needs to be
      true.

    

## Constraint Syntax Patterns

Here are the details of the constraint
        syntax patterns.

        
- 
`constraint(logic expression);`: The simplest form,
          enforcing a logic statement.

        
- 
`constraint(logic expression, string literal | string
            variable);`: Includes an optional failure explanation that is displayed if the
          constraint is violated.

        
- 
`constraint(logic expression, string literal | string
            variable, arg, …, arg);`: Includes a failure explanation with additional
          arguments to be interpolated into the string of the failure explanation.

      

If a constraint is violated, it takes an optional string variable or string literal as
        the failure explanation. The failure explanation could be in a string format with additional
        arguments. CML supports two string formats. One is the standard string format and another is
        a string with {} placeholder, to be replaced with the actual argument value.

    

## Key Components of the Constraint Syntax

      
      

Here are the details of the key components of the constraint syntax.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

```

```

            

            
              

              

- 
- 

              

```

```

            

            
              

              

              

```

```

            

          

        
| Component | Description | Code Sample |
| --- | --- | --- |
| Logic Expression | This can be a basic mathematical expression (using operators like +, -, * , /) or a relational expression (using ==, !=, >, <, and so on). It can also include logical operators such as AND (&&), OR (||), NOT (!), the implication operator (->), or the bi-directional operator (< - >). | Basicconstraint(generator.sum(quantity) > 20); |
| Failure Explanation | This optional string literal or variable provides a human-readable reason for the violation. CML supports two formatting styles for these strings: Java string format (for example, using `%`d or `%s`). Placeholder format using `{}` | With Explanationconstraint(x + y <= 100, "Total must not exceed 100"); |
| Arguments (arg) | Arguments are used to replace the placeholders in the failure explanation string with actual values at runtime. | With Explanation and Argumentsconstraint(requiredKW <= 2500, "The required capacity of {} kW exceeds the maximum supported limit of 2500 kW.",requiredKW); |

      

See the complete example in [Constraints using Format Specifiers (%s, %d) and
        Dates](./cml_core_concept_examples.htm.md).

    

      

## Constraint Example

        
        

In this example, the first constraint specifies that, if the `DutyRating` value isn't `Prime Power (PRP)`,
        then the quantity of `Warranty_PRP (Warranties subtype)`
        must be 0. Similarly in the second constraint, if `DutyRating` value isn't `Data Center Continuous
          (DCC)` then the quantity of `Warranty_DCC` must
        be 0. Lastly, in the third constraint, if `DutyRating`
        value isn't `Emergency Standby Power (ESP)`, then the
        quantity of `Warranty_ESP` must be 0.

        

```
type Warranty;
type Warranty_PRP : Warranty;
type Warranty_DCC : Warranty;
type Warranty_ESP : Warranty;
type GeneratorSet  {
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)", "Emergency Standby Power (ESP)"];
relation Warranties : Warranty[3];
constraint(DutyRating != "Prime Power (PRP)" -> Warranties[Warranty_PRP] == 0);
constraint(DutyRating != "Data Center Continuous (DCC)" -> Warranties[Warranty_DCC] == 0);
constraint(DutyRating != "Emergency Standby Power (ESP)" -> Warranties[Warranty_ESP] == 0);
}
```

      

      

## Example: Constraints Using String and Logical Operators

        
        

This example demonstrates how a GeneratorSet uses string functions to extract a numeric
          voltage value, and then uses logical operators (`->`,
            `&&`,
            `||`) to enforce safety and certification
          requirements.

      

      

## Explanation of Operators Used in the Example

        
        

Here are the details of the operators used in the example.

        

            
            
            
            
              
                

                

                

              

            

            
              
                

                

                

              

              
                

                

                

              

              
                

                

                

              

              
                

                

                

              

              
                

                

                

              

              
                

                

                

              

              
                

                

                

              

            

          
| Operator/Function | Category | Usage in Example |
| --- | --- | --- |
| `strtoint()` | String Function | Converts the extracted voltage string to the integer `Voltage3`. |
| `regexpreplace()` | String Function | Replaces the full Voltage string with only the second matched group (the high voltage number) using the defined `VOLTAGE_REGEX`. |
| `strcontain()` | String Function | Checks if the `DutyRating` string contains the substring "Power". |
| `->` | Logical Implication | Defines a conditional rule: If the condition on the left is true, the condition on the right must be true. |
| `&&` | Logical AND | Requires both conditions (high requiredKW AND duty rating contains "Power") to be true. |
| `||` | Logical OR | Requires `standardsAndCompliance` to be "`Listing-UL 2200`" or "`Certification-CSA`". |
| `!=` | Comparison/Relational | Used to check if the string value is "Not Equal" to a specific string literal. |

      

```
// --- Constants (Required for String Manipulation) ---
define VOLTAGE_REGEX "^(+)/(+)$"

// --- Base Type and Configuration Attributes ---
type Warranty;
type Warranty_ESP : Warranty;

type GeneratorSet {
    // String input attribute for user selection
    string Voltage = ["277/480", "2400/4160", "7976/13800"];

    // String input attribute for operational mode
    string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];

    // String input attribute for compliance
    string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];
    // Required KW (Int attribute)
    int requiredKW = [101..10000];
// warranties for generator set
relation Warranties : Warranty[3];

    // 1. STRING OPERATORS/FUNCTIONS: Deriving Numeric Data
    // We use strtoint() combined with regexpreplace() to extract the second number (the high voltage)
    // from the Voltage string (e.g., extracting 480 from "277/480").
    int Voltage3 = strtoint(regexpreplace(Voltage, VOLTAGE_REGEX, "$2"), 0);
  // Prime Power or Continuous Power using strcontain
    boolean NonstandbyPower = !strcontain(DutyRating, "ESP");

    // 2. LOGICAL OPERATOR (Implication ->): Certification Validation
    // Constraint: If the standard is UL 2200 (precondition), THEN Voltage3 must be <= 600 (postcondition).
    constraint(
        standardsAndCompliance == "Listing-UL 2200" -> Voltage3 <= 600,
        "The UL 2200 standard covers stationary engine generator assemblies rated at 600 volts or less."
    );

    // 3. LOGICAL OPERATORS (AND &&, OR ||) and STRING FUNCTION (strcontain)
    // Constraint: If the required power is high AND the unit is used for Prime Power OR Continuous Power,
    // THEN a specific standard must be selected.
    constraint(
        (requiredKW >= 5000 && NonstandbyPower) 
        ->
        (standardsAndCompliance == "Listing-UL 2200" || standardsAndCompliance == "Certification-CSA"),  "High power and continuous use requires a major compliance standard.");

    // 4. LOGICAL OPERATOR (Implication ->) and String Comparison (!=)
    // Constraint: If the Duty Rating is NOT Emergency Standby Power, THEN a specific warranty (Warranties[Warranty_ESP]) must be excluded/zero.
    constraint(
        DutyRating != "Emergency Standby Power (ESP)" -> Warranties[Warranty_ESP] == 0,
        "The DutyRating when not equal to Emergency Standby Power, implies that the Warranty must be 0."
    );
}
```

      

    

## How User Input Order Affects Constraint Engine Behavior

      
      

The constraint engine is architecturally designed to never override or modify a
        user-selected value when evaluating constraints, except in the specific case of an `exclude` rule. If a constraint violation occurs due to user
        input, the engine generates an error message rather than attempting to fix the value
        itself.

    

      

## Example: Constraint Evaluation Based on Input Order (Generator Set)

        
        

The order in which a user configures attributes for a product (such as a `GeneratorSet`) determines whether the constraint engine
        performs an automatic update or enforces a validation error.

        

Consider a constraint within the `GeneratorSet` type
        that links the operational requirement (`DutyRating`) to
        the required certification (`standardsAndCompliance`).

        

```
type GeneratorSet {
// Attribute 1 (Precondition): User selects operational mode
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)"];
// Attribute 2 (Dependent): Certification standard
string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];
// Constraint: If the unit is configured for Prime Power, it must have UL 2200 Listing.
constraint(
DutyRating == "Prime Power (PRP)" -> standardsAndCompliance == "Listing-UL 2200",
"Prime Power Duty Rating requires UL 2200 Listing"
);
}
```

        

The outcomes depend on the user's input sequence.

        

            
            
            
            
              
                

                

                

              

            

            
              
                

                

                

              

              
                

                

                

              

            

          
| Scenario | User Input Sequence | Constraint Engine Result |
| --- | --- | --- |
| Scenario 1: Successful Update (Precondition first) | The user first sets `DutyRating` to "`Prime Power (PRP)`". | The constraint engine recognizes the precondition is met and updates the dependent attribute, setting `standardsAndCompliance` to "`Listing-UL 2200`". The constraint is validated. |
| Scenario 2: Constraint Violation (Conflicting Value first) | The user first sets `standardsAndCompliance` to "`Certification-CSA`", and then sets `DutyRating` to "`Prime Power (PRP)`". | The existing user-selected value ("`Certification-CSA`") violates the constraint. The constraint engine will not override the user's prior selection to change it to "`Listing-UL 2200`". Instead, the engine displays an error. |

        

To resolve the error in Scenario 2, the user must manually adjust one of their
        selections: either change the `DutyRating` (precondition)
        or manually update the `standardsAndCompliance`
        (dependent value) to "`Listing-UL 2200`".

      

      

## Left-Hand Side and Right-Hand Side Behavior in Constraint Resolution

        
        

Operator precedence and constraint engine resolution process determines whether the
          left-hand side (LHS) or right-hand side (RHS) of a constraint changes or is constrained
          to maintain logical validity. Variable origin, which means whether variables are
          user-selected, calculated, or restricted by system limitations, can also affect the
          outcome for the LHS or RHS in an expression.

        

These examples show how different user inputs lead to different outcomes for the LHS and
          RHS in the same expression.

      

        

## Example 1. Implication Operator (->): Directional Enforcement

          
          

```
type Order {
int quantity = [1..1000];
boolean requiresApproval;
constraint bulkOrderApproval (
quantity >= 100 -> requiresApproval == true
);
}
```

          

The implication constraint `A -> B` (if A, then
        B) is the primary method for defining a mandatory outcome. The engine evaluates the LHS (A)
        first. If the `quantity` is 150 (LHS TRUE), then the
        engine forces `requiresApproval` (RHS) to be `TRUE`.

          

              
              
              
                
                  

                  

                

              

              
                
                  

                  

                

                
                  

                  

                

              

            
| Scenario | Outcome |
| --- | --- |
| Scenario A: LHS is True, RHS Changes | The user sets a quantity greater than or equal to 100 on the LHS, which makes the condition true. The engine sets or changes the value of requiresApproval, the RHS, to true. |
| Scenario B: RHS is False, LHS is Constrained to be False | The user manually sets requiresApproval, the RHS variable, to false. Since the implication true -> false is forbidden, the LHS condition must be false to satisfy the constraint. The engine constrains quantity on the LHS to be less than 100 to make the LHS false. |

        

        

## Example 2. Bi-conditional (<->): Symmetrical Equivalence

          
          

```
type BulkOrderSystem {
int quantity = [1..1000];
boolean requiresApproval;
boolean isBulkOrder;

constraint bulkOrderStatus (
isBulkOrder <-> (quantity >= 100 && requiresApproval),
"Bulk order status requires 100+ quantity AND management approval."
);
}
```

          

The bi-conditional constraint A `<->` B (A if
        and only if B) requires that the LHS and RHS must share the same Boolean truth value. Either
        side can act as the driver, forcing the other side to change. In the example above:

          
            
- A is the boolean variable `isBulkOrder`.

            
- B is the complex condition `(quantity >= 100
            && requiresApproval)`.

          

          

              
              
              
                
                  

                  

                

              

              
                
                  

                  

                

                
                  

                  

                

              

            
| Scenario | Outcome |
| --- | --- |
| Scenario A: LHS Drives RHS | If the user manually sets the attribute isBulkOrder to true (making the LHS true), the engine immediately forces the RHS (quantity >= 100 && requiresApproval) to also be true, ensuring that both quantity is at least 100 and requiresApproval is set to true. |
| Scenario B: RHS Drives LHS | If the user selects a configuration where the quantity is high (for example, 500) and then sets requiresApproval to false (making the RHS condition false), the engine immediately forces the LHS attribute isBulkOrder to false to maintain equivalence. |

        

      

## Exception: The exclude Rule

        
        

The only scenario where the constraint engine intentionally overrides user input is when
        processing the `exclude` rule. If a user selects a
        component or sets an attribute value that violates an `exclude` rule, the engine will automatically override that user input to satisfy
        the exclusion constraint. In all other constraint types (like implication constraints shown
        previously), the engine relies on the user to fix the error. For more information, see [Exclude
        Rule](./cml_exclude_rule.htm.md).

=== ARTICLE: cml_mathematical_functions_numerical_derivation.htm ===
---
page_id: cml_mathematical_functions_numerical_derivation.htm
title: Mathematical Functions (Numerical Derivation)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_mathematical_functions_numerical_derivation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Mathematical Functions (Numerical Derivation)

Mathematical functions and operators are used to calculate derived values based on
    arithmetic relationships between variables.

    
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Function/Operator | Purpose | CML Keyword/Operator [Source] |
| --- | --- | --- |
| Arithmetic Operators | Perform standard arithmetic: addition (+), subtraction (-), multiplication (*), division (/), modulo (% or mod), and power (^). | `+, -, *, /, %, ^` |
| ceil() | Returns the smallest integer greater than or equal to the argument (rounds up). | `ceil` |

    

    

## Usage Example

      
      

```
surgeLoadKW == requiredKW * 1.25);
ceil(totalItems / itemsPerCrate)

```

      

See [Arithmetic Calculations and Functions](./cml_core_concept_examples.htm.md) and examples [here](./cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm.md).

=== ARTICLE: cml_message_rule.htm ===
---
page_id: cml_message_rule.htm
title: Message Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_message_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Message Rule

The message rule displays a message to users based on specified conditions.

    
      

Message rules have this syntax:

      

```
message(logical expression, string literal | string variable, argument, .., argument, severity);
message(logical expression, string literal | string variable, severity);
message(logical expression, string literal | string variable);

```

    

    
      

A message rule can take optional arguments to generate the message and indicate the
        severity of the message as the last argument. Message severity can be `Info`, `Warning`, or
          `Error`. Without an explicit message severity argument,
        the message will be treated as `Info`.

      

Understand the behaviour of each message severity type at runtime.

      
        
- The `Info` message type doesn't require the user
          to take any action in order to continue with the current task. Info messages display a
          gray banner.

        
- The `Warning` message type allows the user to
          continue working on the current task, but blocks them from taking the next step until they
          take action to address the issue described in the message. Warning messages display a
          yellow banner.

        
- The `Error` message type blocks the user from
          continuing with the current task until they fix the error described in the message. Error
          messages display a red banner. Note: An Error message doesn't block a user working in
          the Transaction Line Editor (Transaction Line Table, or TLT). In that component, the user
          can still make changes and save the quote, even when the quote contains conditions that
          trigger an Error message.

      

      

Message format can be a Java string, or a string with {} as a placeholder. The constraint solver replaces each {} with arguments specified after the string, in the order they are written.

    

    

## Example

      
      

In this example, if `requiredKW` is greater than `2500`, a message is displayed that the specified required kW
        is larger than the supported options and must be changed.

      

```
type GeneratorSet {
int requiredKW = [101..10000];
message(requiredKW > 2500, "The required kW is above what the current options can support. Please adjust to 2500 kW or select a new generator set that meets your requirements.");
}
```

=== ARTICLE: cml_preference_rule.htm ===
---
page_id: cml_preference_rule.htm
title: Preference Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_preference_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preference Rule

The preference rule encourages the constraint solver to satisfy the condition, but
    doesn't enforce it if the condition can't be met.

    

The system tries to satisfy the condition in a preference rule, but if for some
        reason it can't, the system delivers a failure message to the user with `Info` severity.

      

#### Note

If a preference rule auto-adds a product that has one or more Product
        Selling Model Options (PSMOs), set one PSMO on the product to Default. The system uses the
        default PSMO to determine which pricebook entry to use for the auto-added product. For more
        information, see [Manage Product Selling
          Model](https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_selling_model.htm&language=en_US) in Revenue Cloud in Salesforce Help.

The preference rule has this
        syntax.

```
preference(logic expression, string literal | string variable, argument, .., argument);
preference(logic expression, string literal | string variable);
preference(logic expression);

```

      

A preference rule can include an optional explanation message for failure. The message is of
          `Info` severity, meaning it does not block the user
        from continuing with the action.

In this example, the preference rule encourages the user
        to mention the `dBMax` value as `90` and the `requiredKW`
        value as `500`.

```
type GeneratorSet {
   int requiredKW = [101..10000];
   int dBMax = [0..140];
   preference(dBMax == 90, "90 preferred for dbMax");
   preference(requiredKW == 500,"50 preferred for requiredKW");
}
```

=== ARTICLE: cml_quote_group_ramp_segment_constraints.htm ===
---
page_id: cml_quote_group_ramp_segment_constraints.htm
title: Define Constraints for Quote Groups, Ramps, and Ramp Segments
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_quote_group_ramp_segment_constraints.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_types.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# Define Constraints for Quote Groups, Ramps, and Ramp Segments

 Apply rules to quote groups, ramps, and ramp segments by using the
  SalesTransactionItemGroup context tag. Assign a groupby value to messages defined in Constraint
  Rules Engine to include the messages in custom grouping strategies. 

 

- 
**[Define a Constraint for a Quote Group](./cml_quote_group_ramp_segment_constraints.htm.md#cml_quote_group_constraint)**  

To define a constraint for a quote group, use the require rule to assign the         SalesTransactionItemGroup attribute that’s contained on a type to the value of the         QuoteGroup container. 

- 
**[Define a Constraint for a Ramp Group](./cml_quote_group_ramp_segment_constraints.htm.md#cml_ramp_group_constraint)**  

To define a constraint that applies to a ramp group, use the IsLineGroupRamped__std   attribute in the require rule to specify that the group is a ramp group.

- 
**[Define a Constraint for a Ramp Segment](./cml_quote_group_ramp_segment_constraints.htm.md#cml_ramp_segment_constraint)**  

To define a rule that applies to a ramp segment for defined conditions, use the   ItemSegmentType attribute.

 

## Define a Constraint for a Quote Group

 
 
 
To define a constraint for a quote group, use the require rule to assign the
        SalesTransactionItemGroup attribute that’s contained on a type to the value of the
        QuoteGroup container. 

        

In this example for a GeneratorSet and its Enclosure, all the relations defined in the
            groupBy container include the `SalesTransactionItemGroup` attribute. Constraint Rules Engine creates a
            virtual container for each unique value of the `SalesTransactionItemGroup` attribute defined in the `groupBy` container. The engine creates one virtual
            container with its own self-contained rule execution for each group that contains one or
            more of the products defined in the `QuoteGroup`
            container.

        
        

#### Note

Groups don’t support rules such as Hide, Disable, or Recommend,
            that perform an action when specified conditions are true.

        
        

### Example

            

```
type LineItem {
    @(tagName = "SalesTransactionItemGroup")
    string SalesTransactionItemGroup;
}

type GeneratorSet : LineItem;
type Enclosure : LineItem;

// Transaction scoped container
@(virtual = true)
type Quote {
    relation quotegroup : QuoteGroup;
    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation generators : GeneratorSet;
    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation enclosures : Enclosure;
}

// Group scoped container
@(virtual = true, groupBy = SalesTransactionItemGroup)
type QuoteGroup {
    string SalesTransactionItemGroup; // Needed for the require rule to save

    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation generators : GeneratorSet;
    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation enclosures : Enclosure;

    require(generators[GeneratorSet], enclosures[Enclosure] {SalesTransactionItemGroup = SalesTransactionItemGroup});
}
```

        

    

 

## Define a Constraint for a Ramp Group

 
 
 
To define a constraint that applies to a ramp group, use the IsLineGroupRamped__std
  attribute in the require rule to specify that the group is a ramp group.

  

In this example, the Enclosure is added to the group only if the GeneratorSet is in a ramp
   group. In the last lines of the example, the `IsLineGroupRamped__std` attribute in the require rule specifies that the GeneratorSet
   is in a ramp group.

  
  

#### Note

Groups don’t support rules such as Hide, Disable, or Recommend, that
   perform an action when specified conditions are true.

  
  

#### Note

To add a type to an unramped group only and exclude the type from ramp
   groups, set the `IsLineGroupRamped__std` attribute to NOT (!)
   in the require rule. For example, `require(!(generators[GeneratorSet].IsLineGroupRamped__std),`. 

  

### Example

   

```
type LineItem {
    @(tagName = "SalesTransactionItemGroup")
    string SalesTransactionItemGroup;
    @(tagName = "IsLineGroupRamped__std")
    boolean IsLineGroupRamped__std;
}

type GeneratorSet : LineItem;
type Enclosure : LineItem;

// Transaction scoped container
@(virtual = true) type Quote;

// Group scoped container
@(virtual = true, groupBy = SalesTransactionItemGroup)
type QuoteGroup {
    string SalesTransactionItemGroup; // Needed for the require rule to save

    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation generators : GeneratorSet;
    @(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation enclosures : Enclosure;

    require(generators[GeneratorSet].IsLineGroupRamped__std, enclosures[Enclosure] {SalesTransactionItemGroup = SalesTransactionItemGroup});
}
```

  

 

 

## Define a Constraint for a Ramp Segment

 
 
 
To define a rule that applies to a ramp segment for defined conditions, use the
  ItemSegmentType attribute.

  

In this example, Enclosure is included in the group with GeneratorSet only if `ItemSegmentType` for GeneratorSet isn’t Trial. To set a value for
    `ItemSegmentType`, the type must be in a ramp group and be
   ramped.

  
  

#### Note

Groups don’t support rules such as Hide, Disable, or Recommend, that
   perform an action when specified conditions are true.

  
  

### Example

   

```
type LineItem {
@(tagName = "SalesTransactionItemGroup")
string SalesTransactionItemGroup;
@(tagName = "ItemSegmentType")
string ItemSegmentType;
}

type GeneratorSet : LineItem;
type Enclosure : LineItem;

// Transaction scoped container
@(virtual = true) type Quote;

// Group scoped container
@(virtual = true, groupBy = SalesTransactionItemGroup)
type QuoteGroup {
string SalesTransactionItemGroup; // Needed for the require rule to save

@(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation generators : GeneratorSet;
@(sourceContextNode = "SalesTransaction.SalesTransactionItem") relation enclosures : Enclosure;

require(generators[GeneratorSet].ItemSegmentType != "Trial", enclosures[Enclosure] {SalesTransactionItemGroup = SalesTransactionItemGroup});
}

```

=== ARTICLE: cml_recommendation_rule.htm ===
---
page_id: cml_recommendation_rule.htm
title: Recommendation Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_recommendation_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Recommendation Rule

The recommend keyword is used within a Constraint Modeling Language (CML) rule to
    display suggestions for related products in the Product Configurator. The rule defines the
    condition under which a specific product type or relation should be suggested to the
    user.

    
      

You can recommend a type, a relation, or both in the same rule. The recommendation rule can be added inside a standalone product, a product bundle, or a virtual container.

      

Unlike action rules that are interpreted directly by the Product Configurator API, when the
        condition is met, the engine forces a UI change (hiding or disabling a product option,
        attribute, or value). Recommendations are not automatically applied to the UI by the
        configuration engine alone. To suggest types or relations (products/bundles), typically for
        up-selling or cross-selling based on their current selections at runtime, use the Run Config
        Rules action within a Salesforce Flow. See [Run Config Rules Action](./actions_obj_run_config_rules.htm.md) in
        the Revenue Cloud Developer Guide.

      
        
- Use an action rule when a selection makes another option invalid or irrelevant. For example, if a user selects a basic warranty, you should "hide" or "disable" the premium support options to prevent a conflicting or impossible setup.

        
- Use a recommendation rule when you want to nudge the user toward a beneficial add-on. For example, if a user buys a high-end generator, you "recommend" a maintenance service contract. This does not block the user if they choose not to add it.

      

      

Here are 3 examples demonstrating how to implement product recommendation rules.

    

    

## Example 1: Recommending a Type (Based on Attribute Selection)

      
      

This rule is placed within the `GeneratorSet` type. If a
        user selects an extremely high voltage, the configuration engine recommends a specialized
        engineer component required for installation or commissioning.

      

```
type GeneratorSet {
// Attribute input
string Voltage = ["277/480", "7976/13800"];
// Relation to the component type being recommended
relation engineers : engineer[0..99];
// Recommend Engineer Specialist (type) for High Voltage
rule(
Voltage == "7976/13800", "recommend", "type", "EngineerSpecialist"
);
}
// Recommended type
type EngineerSpecialist ;
type engineer;
```

    

    

## Example 2: Recommending a Relation (Based on Component Quantity)

      
      

This rule recommends adding items to an existing relation (`Accessories`) if the user selects a high-end component (such as the most robust
        enclosure, `Enclosure_SA3`).

      

```
type GeneratorSet  {
// Relations defined in the GeneratorSet
relation Enclosures : Enclosure;
relation Accessories : Accessory[1..99]; // The relation being recommended
// Recommend Accessories when maximum sound dB is chosen
rule(
Enclosures[Enclosure_SA3] == 1,
"recommend",
"relation",
"Accessories");
}
type Enclosure ;
type Enclosure_SA3 : Enclosure;
type Accessory ;
```

    

    

## Example 3: Recommending a Type (From a Virtual/System Container)

      
      

This rule is applied at the Quote or System level (using a `virtual` type) and recommends a system integration product if multiple generators
        are being configured, reflecting the requirement that large projects often need central
        control components.

      

```
@(virtual = true)
type Quote {
// Relation referencing all GeneratorSet instances on the quote
@(sourceContextNode = "SalesTransaction.SalesTransactionItem")
relation lineItems : GeneratorSet[0..10];
// Recommend Switchgear for multi-unit orders
rule(
lineItems[GeneratorSet] > 1,
"recommend",
"type",
"Switchgear"
);
}
type GeneratorSet;
type Switchgear;
```

=== ARTICLE: cml_relationship_annotations.htm ===
---
page_id: cml_relationship_annotations.htm
title: Relationship Annotations
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_relationship_annotations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_relationships.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Relationship Annotations

You can annotate relationships by using annotations, such as configurable,
    allowNewInstance, closeRelation, sourceContextNode, and so on.

    
      

You can annotate relationships, as in this example, with `configurable=true`.

      

```
// 1. Define the target type
type Component;
// 2. Define the parent type to hold the relation
type System {
// 3. Add the relation with cardinality and proper nesting
@(configurable = true)
relation components : Component[0..10];
}
```

      

Here are the details of relationship annotations.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Annotation | Values | Description |
| --- | --- | --- |
| allowNewInstance | true, false | Enables require rule constraints to work on relationships that are otherwise closed. Must be set to true to enable require rule constraints on closed relationships. |
| closeRelation | true, false | If the value is true, prevents the addition of new line items to the relationship. false is the default value and allows the addition of new line items to the relationship. See examples [here](./cml_annotation_examples.htm.md). |
| compNumberVar | true, false | Avoids creating a component number variable if it is set to false. |
| disableCardinalityConstraint | true, false | Disable cardinality constraint in the relationship to optimize the performance. |
| domainComputation | true, false | `domainComputation` is a Constraint Modeling Language (CML) annotation that specifies how the domain of a model element is determined, either by using a fixed domain or by computing the domain dynamically during configuration. If `domainComputation` is not explicitly specified, the engine sets it implicitly as `true` for the relationship. If the domainComputation is specified as `true`, the relationship domain is dynamically determined based on the configuration and constraint logic. If the `domainComputation` is specified as `false`, the relationship domain is fixed. See examples [here](./cml_annotation_examples.htm.md). |
| generic | true, false | Indicates if generic instance is allowed in the relationship or not. Generic instance is used to prompt the user that they need to select a product in the relationship. |
| noneLeafCardVar | true, false | Avoids creating cardinality variables for none leaf type (a node with no children) in the relationship to optimize the performance. |
| propagateUp | true, false | Aggregates values from child elements to parent elements. If propagateUp is not specified, the engine sets it implicitly as false for the relationship. If the propagateUp annotation is specified as true, the engine aggregates values from children to parent elements (upward propagation). The engine cannot modify this value from the parent level (e.g. via constraint), so the children relation domain will not be affected. If the propagateUp is specified as false, both upward and downward propagations are applicable. The engine aggregates values from children to parent elements (upward propagation). Meanwhile the engine can modify this value (e.g. via constraint) from the parent level. The value is propagated downward and might affect the relation domain (downward propagation). See examples [here](./cml_annotation_examples.htm.md). |
| readOnly | true, false | Sets a relationship and all child relationships to read-only, to prevent the engine or user from modifying. |
| relatedAttributes | string value | `relatedAttributes` is a CML annotation that resets the domain to the original one for `domainComputation`. If `domainComputation` is not explicitly specified, the engine sets it implicitly as `true` for the relationship. If the `domainComputation` is specified as `true`, the relationship domain is dynamically determined based on the configuration and constraint logic. If the `domainComputation` is specified as `false`, the relationship domain is fixed. See examples [here](./cml_annotation_examples.htm.md). |
| relatedRelationships | string value | Related relationships whose cardinality variables must be unbound for domain computation. |
| sequence | integer | Indicates the sequence in which the relationship is configured and executed. |
| sharing | true, false | Indicates if the relationship is shared or not. If the relationship is shared, the engine connects the instance from another relationship to this relationship instead of instantiating the instance in the relationship itself. |
| singleton | true, false | Indicates if all types in the relationship must be singleton or none. |
| source | string | Data source defined in the model. |
| sourceAttribute | Variable name in string | Sets the domain of the current relationship to the domain of the source attribute. |
| sourceContextNode | string | For cases that use a virtual container, specifies the path in the context service for the instances in the relationship. |

=== ARTICLE: cml_relationship_variable_functions.htm ===
---
page_id: cml_relationship_variable_functions.htm
title: Relationship Variable Functions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_relationship_variable_functions.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_relationships.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Relationship Variable Functions

CML variable functions are fundamental tools used to perform both aggregation
    (summarizing data from related components) and complex mathematical calculations on attribute
    values (variables) within a configuration model. These functions are crucial for enforcing
    dimensional validity and calculating derived attributes.

    
      

You can use functions such as `count()`, `min()`, `max()`, `sum()` and `total()` to
        calculate values from all variables with the same name in the descendants of the current
        type. Aggregate functions are used primarily as relationship attributes within a relation to
        calculate values across multiple instances of a component type (descendants).

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Function | Purpose | CML Keyword [Source] |
| --- | --- | --- |
| `count()` | Counts the number of component instances within a relationship that match a specific logical condition. | `count` |
| `max() / min()` | Returns the maximum or minimum value of an attribute found across all instances in a relationship. | `max, min` |
| `sum()` | Calculates the sum of a specific numeric variable across all instances in a relationship. Note: executes multiplication of a variable value by a product quantity. | `sum` |
| `total()` | Calculates the sum of a specific numeric variable across all instances in a relationship. Note: Unlike the sum() function, does not execute multiplication of a variable value by line item quantity. | `total` |

    

    

## Example: Using Aggregate Functions

      
      

```
type LineItem;
type GeneratorSet : LineItem {
relation modelclassification : ModelClassification {
sumPowerKW = sum(powerKW);
maxPowerKW = max(powerKW);
highPowerModelsAmount = count(powerKW > 500);
}
relation warranties : Warranty  {
totalCoverageDays = total(coverageDays);
}
constraint(modelclassification.sumPowerKW > 2500 && modelclassification.sumPowerKW < 3500);
message(true, "The maximum `powerKW` from selected GeneralModels is: {}", modelclassification.maxPowerKW);
constraint(warranties[Warranty] == modelclassification.highPowerModelsAmount);
message(true, "Effective Warranty coverage days: {}", warranties.totalCoverageDays);
}
type ModelClassification : LineItem {
int powerKW = [900, 1750, 2500];
}
type GeneralModel1750 : ModelClassification {
int powerKW = 1750;
}
type GeneralModel2500 : ModelClassification {
int powerKW = 2500;
}
type GeneralModel900 : ModelClassification {
int powerKW = 900;
}
type Warranty {
int coverageDays;
}
type Warranty_PRP : Warranty {
int coverageDays = 50;
}
type Warranty_DCC : Warranty {
int coverageDays = 100;
}
type Warranty_ESP : Warranty {
int coverageDays = 200;
}
```

    

    

## sum()

      
      

In the example, the `sum()` function aggregates the
          `powerKW` variable values of the selected products in
        the `modelClassification` relationship. The model
        includes a constraint that enforces the selection rule based on the calculated total: the
          `sum` of `powerKW`
        for the selected products must be between 2500 and 3500.

      

```
constraint(modelclassification.sumPowerKW > 2500 && modelclassification.sumPowerKW < 3500);
```

      

As a result, the engine selects two products from the `modelClassification` relation (`GeneralModel1750` and `GeneralModel900`),
        since their calculated sum of `powerKW` values (2650)
        satisfies the constraint.

    

    

## max()

      
      

In the example, the `max()` function returns the maximum
          `powerKW` variable value among the selected products in
        the `modelClassification` relationship. The model defines
        a message that displays the maximum `powerKW` value in
        the Product Configurator.

      

```
message(true, "The maximum `powerKW` from selected GeneralModels is: {}", modelclassification.maxPowerKW);
```

      

As a result, because the previously described `sum()`
        function and constraint selected two products (`GeneralModel1750` and `GeneralModel900`), the
        maximum returned value is 1750.

    

    

## count()

      
      

In the example, the `count()` function calculates the
        amount of selected `modelClassification` relationship
        products that contain the `powerKW` variable value
        greater than 500. The model includes a constraint that enforces the selection of `warranties` product for each `GeneralModel` counted by the function.

      

```
constraint(warranties[Warranty] == modelclassification.highPowerModelsAmount);
```

      

As a result, based on the previous `sum()` description,
        the engine selects two products (`GeneralModel1750` and
          `GeneralModel900`). Since both products meet the
        count() condition (`powerKW` > 500), the engine adds
        one of the warranties product with quantity 2.

    

    

## total()

      
      

In the example, the `total()` function aggregates the
        values of the `coverageDays` variable for the selected
        products of the `warranties` relationship. The model
        defines a message that displays the calculated total in the Product Configuration.

      

```
message(true, "Effective Warranty coverage days: {}", warranties.totalCoverageDays);
```

      

As a result, based on previously described `count()`
        example, the system selects one of the `warranties`
        product (e.g., `Warranty_DCC`) with a quantity of 2 and
        calculates the total value of its `coverageDays` variable
        (100).

      

A key difference between `total()` and `sum()` functions is that for `total()` the engine ignores the `warranties`
        product quantity. The system does not multiply the quantity of the selected warranty by the
          `coverageDays` variable value when computing the
        overall total.

      

See also [Arithmetic Calculations and Functions](./cml_core_concept_examples.htm.md) and examples [here](./cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm.md).

=== ARTICLE: cml_relationships.htm ===
---
page_id: cml_relationships.htm
title: Relationships
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_relationships.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_cml_core_concepts.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Relationships

Relationships in Constraint Modeling Language (CML) define how different product types
    are associated with each other, forming the structural hierarchy of a product bundle.
    Relationships are also referred to as ports.

    
      

Here’s a comprehensive overview of relationships, their syntax, purpose, and key features,
        particularly using examples relevant to the Generator Set model.

      

#### Note

When you import product relationships from PCM into a constraint
        model, don’t include product component groups. Importing with product component groups
        increases complexity and can cause performance degradation.

    

    

## Definition and Syntax of Relationships

      
      

Relationships define the one-to-many connections between a parent type (such as a bundle) and its component types (children).

      
        
- Keyword: The keyword used is `relation`.

        
- Syntax: A basic relationship declaration includes the relation name, the target type,
          and cardinality
          bounds.

```
relation <relation name> : <Target Type>[min..max] { /* Optional content */ }
```

        
- Purpose: Relationships represent the product structure in a bundle. For example, the
          root product (GeneratorSet) has relationships with its components (`MainAlternators`, `TemperatureSensors`).

      

      

#### Note

To avoid testing unnecessary value combinations and improve performance,
        specify the smallest required cardinality (quantity range).

    

    

## Set Maximum Relationship Size

The `maxRelationSize` property is the maximum cardinality for a
        single relationship in the constraint model. It controls how many instances of a child
        component can exist under one parent through the relationship.  The maximum value for
          `maxRelationSize` is 1073741824. The default value is
        9999. 

Use `maxRelationSize` to set a limit based
        on the number of instances you need for your business purposes. For example, if the most a
        customer can order of a child component is 200,000, set `maxRelationSize` to 200,000. An overly high cardinality limit increases the risk
        of unbound variables that cause the constraint engine to backtrack through the entire range
        to resolve a conflict. Use `maxRelationSize` with the
          `property`.

      

```
property maxRelationSize = 100000;                                                                  
 type Quote {                                                                             

   relation items : LineItem[0..99999999]; // cardinality uses this max

 }
```

The `maxRelationSize` property doesn’t
        limit these values:

        
- The number of relationship declarations in a type 

        
- The number of types in the constraint model

        
- The total component count across all relationships

      

    

## Omit Unnecessary Relationships

When using the [visual builder](https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_visual_builder.htm&language=en_US) or the [CML editor](https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_cml_editor.htm&language=en_US) to create a CML
        code for a bundle, the system by default imports all the relationships for the selected
        bundle from the structure defined in Product Catalog Management (PCM). In large and complex
        CML code, some of these relationships may not be relevant to any constraint and can be
        potentially omitted.

To enable import of a subset of bundle components, add this
        property at the top of the constraint model CML
        file.

```
property allowMissingRelations = "true";
```

If your PCM bundle contains many relations but your CML code defines only one, the engine
        validates the model, but often returns a configuration failure. at run time. By setting
          `allowMissingRelations = "true"`, you don’t have to
        define every relation found in the PCM (such as GeneralModels in the Relationship Ordering
        example) if they don’t require specific configuration logic in your CML file.

Here’s an example with the allowMissingRelations property.

```
// 1. Enable skipping of unneeded relations from the Product Catalog (PCM)
property allowMissingRelations = "true";

type ConciseGeneratorBundle  {
    // Define only the specific accessory needed for this logic
    relation enclosures : Enclosure;

    // A simple variable to trigger the logic
    int requiredKW = [100..5000];

    // Logic: High power requirements force a specific enclosure type
    // This omits other accessories like filters, batteries, and heaters [2, 3].
    constraint(requiredKW > 2000 -> enclosures[ReinforcedEnclosure] == 1, 
               "Power levels above 2000kW require a Reinforced Enclosure.");
}

// 2. Define the accessory and its specific subtype
type Enclosure ;
type ReinforcedEnclosure : Enclosure;

```

For more information, see [Constraints](./cml_constraints.htm.md).

To ensure stability at run time without the allowMissingRelations property, you must manually
        define every relation and type present in the PCM bundle, even if you don't intend to write
        logic for them. This creates large CML files with a high number of variables and components,
        which lead to performance degradation, and even timeout issues.

#### Note

We don’t recommend using the pattern in this example.

```
// EXPENSIVE FIX: Mirroring everything
type GeneratorSet {
    relation engineModels : EngineModel; // Unused in CML logic
    relation alternators : Alternator;    // Unused in CML logic
    relation fuelFilters : FuelFilter;    // Unused in CML logic
    relation starterMotors : StarterMotor; // Unused in CML logic
    relation enclosures : Enclosure;      // The only one we need
    // ... potentially 15+ more relations ...

    constraint(requiredKW > 2000 -> enclosures[ReinforcedEnclosure] == 1);
}
type Enclosure ;
type ReinforcedEnclosure : Enclosure;

```

    

## Skip Type Generation for Types with Many Mapped
        Products

When you create a constraint model for a product whose type is mapped to
        a large number of products, either directly or through product classifications , the
        constraint engine loads all mapped product data into the model during model fetch,
        regardless of whether those products are used in your CML. In catalogs with hundreds or
        thousands of mapped products, the loading process can significantly increase model fetch and
        execution time, causing timeouts. To load only the types that you explicitly declare in your
        constraint model and skip generating types from unmapped product data, add the `skipTypeGeneration` property at the top of the constraint
        model CML file.

```
property skipTypeGeneration = "true";

```

When you set `skipTypeGeneration = "true"`, the constraint
        engine skips type generation for all products not declared in the CML file, to optimize
        model storage. This property applies to types only and doesn't affect relationship loading
        or other model elements.

Use skipTypeGeneration = "true" when all
        of the following are true.

        
- A type in your constraint model is mapped to hundreds or thousands of products, either
          directly or through a product classification. 

        
- Your CML defines constraints for only a subset of those mapped products. 

        
- You experience slow load times or execution timeouts.

      

#### Note

Before you enable `skipTypeGeneration`, confirm that you explictly declare every type that your CML
        references in the constraint model. When you skip type generation, the constraint engine can
        only resolve types that it finds in your declarations. A referenced type that isn't declared
        causes an error when you try to save the model. As a best practice, use `skipTypeGeneration` only when your constraint model includes
        classification types. 

    

## Example: skipTypeGeneration with a Large Classification
        Catalog

In this example, a `GeneratorSet` product is mapped to many
        products through a classification. The CML enforces duty-rating and engine constraints, but
        only needs two component types. Setting `skipTypeGeneration =
          "true"` at the top of the constraint model prevents the constraint engine from
        loading mapped products that the model doesn't use.

```
// Skip loading all classification types from PCM.
// Only the types explicitly declared in this file are loaded.
property skipTypeGeneration = "true";
type GeneratorSet : LineItem {
   string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];
   int requiredKW = [100..10000];
   relation engine : Engine[1..1];
   constraint(DutyRating == "Emergency Standby Power (ESP)" -> requiredKW >= 500,
              "Emergency Standby Power requires at least 500 kW.");
   constraint(DutyRating == "Prime Power (PRP)" -> engine[PrimePowerEngine] == 1,
              "Prime Power duty rating requires a Prime Power Engine.");
}
// Declare only the types this constraint model requires.
// Classification types not declared here are not loaded into the model.
type Engine;
type PrimePowerEngine : Engine;
type ContinuousPowerEngine : Engine;

```

    

## Order Keyword

      
      

The `order()` keyword is used within a `relation` declaration to define the specific sequence in which
        the constraint engine evaluates and attempts to instantiate the child subtypes available in
        that relationship. This controls the prioritization of component selection.

    

    

## Example: Relationship Ordering

      
      

```
// --- Component Subtypes (Specific Generator Models) ---
// Define a base type for generator models with a power attribute
type GeneralModel {
int powerKW = [0..3000]; // Explicit domain
}
// Specific subtypes that inherit from GeneralModel
type GeneralModel2500 : GeneralModel {
int powerKW = 2500;
}
type GeneralModel1750 : GeneralModel {
int powerKW = 1750;
}
type GeneralModel900 : GeneralModel {
int powerKW = 900;
}
// --- Parent Type (GeneratorSet) ---
type GeneratorSet {
// Required power defined by the parent (non-configurable)
@(configurable = false)
int requiredKW = [100..3000];
// Relation Declaration using order()
// Cardinality requires exactly one model to be selected.
// order() sets the selection priority (2500 KW model is checked before 1750 KW model).
relation GeneralModels : GeneralModel  order(GeneralModel2500, GeneralModel1750, GeneralModel900);
}
```

    

  

- 
**[Relationship Variable Functions](./cml_relationship_variable_functions.htm.md)**  

CML variable functions are fundamental tools used to perform both aggregation     (summarizing data from related components) and complex mathematical calculations on attribute     values (variables) within a configuration model. These functions are crucial for enforcing     dimensional validity and calculating derived attributes.

- 
**[Relationship Annotations](./cml_relationship_annotations.htm.md)**  

You can annotate relationships by using annotations, such as configurable,     allowNewInstance, closeRelation, sourceContextNode, and so on.

=== ARTICLE: cml_require_rule.htm ===
---
page_id: cml_require_rule.htm
title: Require Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_require_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Require Rule

The require rule requires certain components to be included in a relationship when
    specified conditions are met.

    

Required components can have attributes and quantity specified. The require rule can
        include an optional explanation message, for the rule failure explanation.

In certain
        scenarios, you can independently add a type at the header level. This means you can include
        a specific type even if it isn't explicitly defined as part of any of the relationships
        you've configured. This capability offers flexibility in managing and including
        necessary types that might not always fall under a specific relationship structure.

#### Note

If a require rule auto-adds a product that has one or more Product Selling
        Model Options (PSMOs), set one PSMO on the product to Default. The system uses the default
        PSMO to determine which pricebook entry to use for the auto-added product. For more
        information, see [Manage Product Selling
          Model](https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_selling_model.htm&language=en_US) in Revenue Cloud in Salesforce Help.

The
        require rule has this
        syntax:

```
require(logic expression, relationship[type]{var=value,…,var=value}==integer value, "Explanation message");
```

In
        this example, the require rule specifies that if the number of engineers is more than 0,
        installation is required. The installation will be automatically added upon adding an
        engineer.

```
type GeneratorSet {
    relation engineers : engineer[0..99];
relation installation : install[0..5];
   require(engineers[engineer] > 0, installation[install], "Installation is required if engineers are present");
}
type engineer{}
type install{}

```

=== ARTICLE: cml_require_rule_vs_constraint.htm ===
---
page_id: cml_require_rule_vs_constraint.htm
title: Require Rule vs Constraint
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_require_rule_vs_constraint.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Require Rule vs Constraint

In Constraint Modeling Language (CML), constraint() and require() can both enforce
    behavior, but they operate differently: constraint focuses on logical consistency, require
    focuses on physical presence of products.

    
      

Here's a comparison between `constraint()` and
          `require()`.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Feature | constraint() | require() |
| --- | --- | --- |
| Primary goal | Validates if a condition is met (LHS) and operates on the result (RHS). | Forces a product to be present. |
| Engine action | Resolves the constraint or displays an error if there are no options to resolve. | Adds the required product to the quote. |

=== ARTICLE: cml_set_product_selling_model_constraint.htm ===
---
page_id: cml_set_product_selling_model_constraint.htm
title: Set Product Selling Model in a Constraint
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_set_product_selling_model_constraint.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Set Product Selling Model in a Constraint

Use the productSellingModel tagname to write a constraint that sets the Product Selling
    Model (PSM) for a type. You can define a PSM as one time, time-deferred (subscription with end
    date), or evergreen (recurring subscription with no preset end date). The PSM is updated for new
    line items at runtime, based on the constraint.

    
      

You can’t use a Constraint Modeling Language (CML) constraint to update the PSM for an
        existing quote line. For more information on product selling models, see [Manage Product Selling Model](https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_selling_model.htm&language=en_US)
        in Revenue Cloud in Salesforce Help.

    

    

## Constraint Example

      
      

Using the `GeneratorSet` model, a constraint can be
        defined that sets the PSM based on a specific operational attribute chosen by the user, such
        as the `DutyRating`. This assumes that different duty
        ratings correspond to different billing models (for example, permanent installation versus
        temporary rental).

      

This example sets the PSM to a specific ID (for example, `PSM_EVERGREEN_ID`) if the user selects the "Continuous Power (COP)"
        duty rating.

      

```
//Global variable PSM ID
define PSM_EVERGREEN_ID "a00Tx000000Qz1g"
type GeneratorSet {
// Use the productSellingModel tag from the context definition
@(tagName = "ProductSellingModel")
string productSellingModel;
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];
// Set PSM based on Duty Rating
constraint(
DutyRating == 'Continuous Power (COP)' ->    productSellingModel == PSM_EVERGREEN_ID
);
}
```

=== ARTICLE: cml_setdefault_rule.htm ===
---
page_id: cml_setdefault_rule.htm
title: Setdefault Rule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_setdefault_rule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Setdefault Rule

The setdefault rule allows component selection with attribute values and quantity,
    similar to the require rule.

    
      

Unlike the require rule, the setdefault rule applies a default configuration status and
        uses a triggering mechanism to control when the solver attempts to satisfy the rule. The
        setdefault rule can include an optional explanation message.

      

The setdefault has this syntax, similar to the require rule.

      

```
setdefault(condition, expression, message);
```

      

The setdefault rule evaluates the condition. If the condition is false, the solver ignores
        the expression and doesn't display a message, regardless of whether any part of the
        condition is changed. If the condition is true, the solver performs one of these
        actions.

      
        
- If any part of the condition is changed or the parent component is new, the solver
          attempts to satisfy the expression. If the solver can't satisfy the expression, an
          explanation message is displayed (if included).

        
- If no part of the condition is changed, the solver evaluates the expression without
          attempting to satisfy it. If the expression evaluates to false, an explanation message is
          displayed (if included).

      

      

The key difference between the setdefault rule and the require rule is that the setdefault
        rule attempts to satisfy the expression only when a condition is changed. If no condition is
        changed, the setdefault rule performs a passive evaluation. The require rule always attempts
        to satisfy the expression when the condition is true.

      

In this scenario, we use the requiredKW attribute (the user's power requirement) as
        the condition and the Accessories relation as the target for the recommended
        cardinality.

      

```
type Accessory;
type GeneratorSet  {
int requiredKW = [101..10000];
relation Accessories : Accessory[1..99];
/**
* @Title High Power Accessory Recommendation
* The setdefault constraint specifies that 2 accessory units are
* recommended when the required power capacity is greater than 2000 kW.
*/
setdefault(
requiredKW > 2000,
Accessories[Accessory] == 2,
"2 specialized accessory kits are recommended for power levels above 2000 kW"
);
}
```

=== ARTICLE: cml_string_variable_functions_and_operators.htm ===
---
page_id: cml_string_variable_functions_and_operators.htm
title: String Variable Functions and Operators
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_string_variable_functions_and_operators.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# String Variable Functions and Operators

Constraint Modeling Language (CML) provides string manipulation and conversion
    functions, and string comparison and validation operators.

    
      

The functions can be used to modify strings, extract information, or convert strings to
        numeric types. The operators can be used to validate string values against sets or regular
        expressions.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Function | Purpose | Syntax, Examples, and Additional Details |
| --- | --- | --- |
| strlen() | Returns the length of the string as an integer. | `strlen(inputString)` `strlen("Hello"` returns 5. |
| substr() | Returns a substring from the input string. | `substr(inputString, startIndex)` or `substr(inputString, startIndex, endIndex)`The index starts with 0. The character at `startIndex` is included, and the character at `endIndex` is excluded. |
| strconcat() | Concatenates multiple strings using a specified separator. | `strconcat(separator, stringArgsToConcatenate) ``strconcat("-", "a", "b")` results in "a-b". |
| join() | An aggregate function that concatenates string values across related components, typically using a separator. The separator is a comma by default. | `names = join(name)` |
| trim() | Returns the string after removing any leading or trailing spaces. | `trim(strToTrim)` |
| strsplit() | Splits a string into an array of strings around a given separator. | `strsplit(stringToSplit, separator)` |
| strcontain() | Returns a boolean value (true or false) to specify whether the input string contains the specified search string. | `strcontain(inputString, searchString)` |
| strshare() | Splits two strings using a delimiter (comma by default) and returns true if the resulting lists have any elements in common. | `strshare(string1, string2, delimiter)` |
| strformat() | Returns a formatted string based on parameters and format specifiers. | `strformat("%d person", quantity)` Specifiers include `%d` for integer, `%s` for string, `%.2f `for decimal or float, and `%b` for boolean. |
| strtoint() | Converts a string to an integer. | `strtoint(inputString, defaultValue)`If the string can't be parsed as an integer (for example, it contains text or a decimal point), the provided defaultValue is returned. |
| strtofloat() | Converts a string to a decimal (floating point) value. | `strtofloat(inputString, defaultValue)` If the conversion fails, the provided `defaultValue` is returned. The resulting decimal attribute must be declared with the intended precision. For example, `decimal(3)`. |
| regexpreplace() | Take an input string and a defined Regular Expression (regex). Replace the entire input string with a specific captured group from the regex match. | `regexpreplace(InputString, RegexPattern, ReplacementGroup) `This function is commonly used to derive numeric data from complex, formatted strings before they are converted into integers or decimals. |
| get(index, array) | Used to retrieve an element at a specified index (starting at 0) from an array or list generated by a function like strsplit. | `string splitStr1 = get(0, strsplit("hello constraint engine", " ")); // returns hello` Using Get with Table Constraint—If your table constraint output for three columns is stored in a string[] variable named picklistValues, you would access the first row's attributes like this (assuming the columns are stored in a predictable sequence): `// Retrieve the first element (Row 0, Column 0) string value0_0 = get(0, picklistValues);` `// Retrieve the second element (Row 0, Column 1)` |

    

    

## String Comparison and Validation Operators

      
      

The in operator checks if the value of a string attribute is present within a defined set or array of strings.

      

Example

      

```
color in ["red", "blue"]
```

=== ARTICLE: cml_table_constraints.htm ===
---
page_id: cml_table_constraints.htm
title: Table Constraints
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_table_constraints.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Table Constraints

The table constraint in Constraint Modeling Language (CML) is used to define a set of
    valid combinations of values for two or more attributes. These combinations are specified in
    rows within the constraint definition.

    
      

The table constraint has this syntax:

      

```
table(variable, …, variable, {value, .. value}, …, {value, …, value});
```

      

Each row inside {} defines a valid combination of values.

    

    

## Example: Table Constraint

      
      

In this example:

      
        
- Variables: The attributes `Voltage` and `DutyRating` are listed as the columns for the table.

        
- Table Rows: Each row defined within the curly braces ({}) specifies a valid combination.
          For instance, `{"7976/13800", "Continuous Power
            (COP)"}` is a valid pairing.

        
- Enforcement: If a user attempts to select a high voltage (`"7976/13800"`) while choosing a Prime Power rating (`"Prime Power (PRP)"`), the table constraint is violated, and the engine
          displays the error message: "Selected Voltage is not compatible with the required Duty
          Rating."

      

      

```
// --- Component Types ---
type GeneratorSet {
// 1. Attributes whose values must align according to the table
string Voltage = ["220/380", "277/480", "7976/13800"];
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Emergency Standby Power (ESP)"];
// 2. Table Constraint
// Defines valid combinations where Voltage and DutyRating are mutually dependent.
constraint validOperationalModes(
table(
Voltage,
DutyRating,
{"220/380", "Prime Power (PRP)"},
{"220/380", "Continuous Power (COP)"},
{"220/380", "Emergency Standby Power (ESP)"},
{"277/480", "Prime Power (PRP)"},
{"277/480", "Emergency Standby Power (ESP)"},
{"7976/13800", "Continuous Power (COP)"}
),
"Selected Voltage is not compatible with the required Duty Rating."
);
}
```

    

    

## Import Data from a Salesforce Object to Populate a Table Constraint

      
      

Import data from a standard or custom Salesforce object to use in a table constraint in a constraint model. The imported data populates the columns and rows in the table constraint in CML, and saves you the step of manually entering the data.

      

To import data from a Salesforce object, first assign Read, Create, Edit, and Delete
        permissions for the object to the Constraint Rules Engine Licenseless permission set. See
          [Import Data from Salesforce Objects
          to Use in Constraint Models](https://help.salesforce.com/s/articleView?id=ind.product_configurator_import_object_data.htm&language=en_US) in Salesforce Help.

      

In CML, use the SalesforceTable keyword and the syntax shown here to import data from a
        Salesforce object. This example uses the `GeneratorSet`
        type to constrain the calculated running capacity (`gc_runningKw`) based on a user's selection of the nominal output (`Nominal_Power_Output`), referencing an external Salesforce
        custom object named PowerCst__c.

    

    

## Example: Imported Table Constraint

      
      

```
type GeneratorSet {
// 1. Attribute storing the user-selected power output (String)
string Nominal_Power_Output = ["100 kW", "300 kW", "500 kW", "700 kW"];
// 2. Attribute storing the resulting Running kW (Decimal, calculated)
@(configurable = false, defaultValue = "0")
decimal(2) gc_runningKw;
// Constraint ensures the pairing of Nominal_Power_Output and gc_runningKw is found in the imported Salesforce table.
constraint(
table(
Nominal_Power_Output, gc_runningKw,
SalesforceTable("PowerCst__c","Nominal__c,Running__c")
)
);
}
```

    

    

## Explanation of the Imported Table

      
      

The table constraint ensures that the selected values for `Nominal_Power_Output` and `gc_runningKw` must
        form one of the valid combinations defined in the external source.

      
        
- Table (`Nominal_Power_Output`, `gc_runningKw`, ...): These are the CML attributes whose
          values must correlate. They define the columns of the required combination table.

        
- Salesforce Table ("`PowerCst__c",
            "Nominal__c,Running__c`"): This function keyword directs the constraint engine
          to import data from the Salesforce custom object PowerCst__c.

        
- Field Mapping: The fields specified ("`Nominal__c,Running__c`") define the columns in the Salesforce object that
          correspond to the CML attributes listed in the table function. Nominal__c maps to `Nominal_Power_Output`, and Running__c maps to `gc_runningKw`.

=== ARTICLE: cml_type_annotations.htm ===
---
page_id: cml_type_annotations.htm
title: Type Annotations
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_type_annotations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_types.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Type Annotations

You can annotate types to add information. Type annotations are metadata applied to a
    type declaration to provide instructions to the constraint engine regarding how instances of
    that type should be handled, instantiated, or used in the configuration structure.

    
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

- 
- 
- 

            

            
              

              

              

            

          

        
| Annotation | Possible Values | Description |
| --- | --- | --- |
| virtual | true, false | If `true`, specifies whether the indicated type refers to the transaction header (such as Quote or Order) or to a logical container (sub group of the Quote or Order). If the value is `false`, then it’s the default behavior for types and doesn’t need to be explicitly specified. |
| groupBy | Variable name | Used with `virtual = true`, the `groupBy` annotation organizes child products—the individual instances populating a relationship—into virtual containers based on a shared attribute value. See [Relationships](./cml_relationships.htm.md) and the [Grouping Generators by Voltage example](./cml_core_concept_examples.htm.md) . |
| maxInstanceQty | Integer | Specifies the maximum cardinality for a component in a group. See [Group Type](./cml_group_type.htm.md). |
| minInstanceQty | Integer | Specifies the minimum cardinality for a component in a group. See [Group Type](./cml_group_type.htm.md). |
| source | String | Specifies the data source defined in the model. |
| split | true, false, none | Specifies whether the type should be split or not. If `split=true`, there can be multiple instances of the type, and the quantity of each instance is always 1. If `split=false`, there is only one instance in the relationship. If the user adds more instances, the engine adds more quantity to the existing instance. If `split=none` (the default), there are multiple instances of the same type in the relationship, with different quantities. The `split=true` annotation isn't supported for child products within a dynamic bundle. See examples [here](./cml_annotation_examples.htm.md). |
| sharingcount | Integer | Specifies the maximum number of times a single instance of a specific type can be shared or reused across different relationships within the configuration model. This annotation is used in conjunction with the @(`split=true`) annotation. When a type is marked for splitting, the constraint engine can process multiple instances in parallel to improve performance. The `sharingCount` tells the engine exactly how many times it can "split" or reuse that instance to satisfy the configuration requirements without generating entirely new, unique instances. It's a critical tool for managing large-scale configurations (for example, models with over 1,000 components). By setting a sharing limit, you reduce the number of variables the engine must instantiate, which helps prevent performance degradation and system timeouts.The `sharingCount` annotation works with the @(`sharing=true`) annotation applied to Relations. The relation annotation enables the general capability to share components across instances, while the `sharingCount` on the child type sets the numerical limit for that behavior. See [Relationship Annotations](./cml_relationship_annotations.htm.md) and the [Sharing Accessories in a Generator Set example](./cml_core_concept_examples.htm.md). |

    

    

## Creating a Virtual Container (@virtual = true)

      
      

In this example, the `@virtual = true` annotation is
        applied to a logical container type, `System`, which is
        primarily used to define relationships. These relationships aggregate data across line items
        in the quote that forms a sub-group called `system`. See
          [Relationships](./cml_relationships.htm.md).

      

```
@(virtual = true)
type System {
// This relation gathers all GeneratorSet line items on the sales transaction
@(sourceContextNode = "SalesTransaction.SalesTransactionItem")
relation generators : GeneratorSet[0..10];
// This variable aggregates the surge load (calculated inside GeneratorSet) from all collected generators
int totalQuotedLoad = generators.sum(surgeLoadKW);
}
type GeneratorSet {
// The attribute calculated here is aggregated in the virtual 'System' type above
@(configurable = false)
int requiredKW = [101..10000];
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)", "Emergency Standby Power (ESP)"];
decimal(2) surgeLoadKW = requiredKW * 1.25;
}
```

=== ARTICLE: cml_type_hierarchies.htm ===
---
page_id: cml_type_hierarchies.htm
title: Type Hierarchies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_type_hierarchies.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_types.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Type Hierarchies

Constraint Modeling Language (CML) supports inheritance and overriding, which allow you
    to create hierarchies between types. By establishing these hierarchies, constraint models become
    more modular and efficient.

    

## How Hierarchies Function

      
      
        
- Inheritance: This mechanism enables a specialized child type to automatically share common variables (attributes) and relationships defined in its parent type. By inheriting from a base type, child types don't need to redefine shared properties, which ensures consistency across the model.

        
- Overriding: While child types inherit the structure of the parent, they can override or specialize those properties. For example, a parent type might define a variable with a broad range of possible values, while a child type overrides that variable with a fixed value specific to that individual product.

      

    

    

## Practical Examples of Hierarchy

      
      
        
- Simple Product Extension: A `BaseProduct` might
          define an `id` and `name`. A `PhysicalProduct` can then inherit
          from `BaseProduct` to gain those fields while adding
          its own unique characteristics, such as `weight` or
            `color`.

        
- Multi-Level Nesting: Hierarchies can extend through multiple layers. For instance, a
            `Room` type can be the parent to a `Bedroom` type, and a `MasterBedroom` can further inherit from the `Bedroom` type, carrying all properties down the chain.

        
- Abstract Base Models: In complex configurations such as a `GeneratorSet`, a parent type such as `GeneralModel` defines the necessary attributes (such as `powerKW` and `dB`), while
          specific child types such as `GeneralModel900` or
            `GeneralModel1200` inherit those attributes and
          override them with their specific ratings.

      

    

    

## Core Benefits

      
      

By establishing these hierarchies, constraint models become more modular and efficient. You can create header-level declarations and base types to serve as a foundation for the entire model, allowing you to reference reusable components multiple times rather than writing redundant code for every product variation. This structural organization allows the constraint engine to effectively enforce business logic and validate configurations across all related types.

    

    

## Example 1: Simple Product Extension

      
      

In this pattern, a specialized type inherits from a broader base type. In the provided
        generator set model, the `GeneratorSet` type inherits
        from `LineItem`, gaining any properties defined at the
        line-item level while adding its own specific configuration fields like `requiredKW` and `Voltage`.

      

```
// The ultimate base type in the system
type LineItem;
// Child type extending LineItem with generator-specific attributes
type GeneratorSet : LineItem {
int requiredKW = [101..10000];
string Voltage = ["220/380", "240/416", "255/440"];
string DutyRating;
}
```

    

    

## Example 2: Multi-Level Nesting

      
      

CML supports hierarchies with multiple layers of depth. In this example, properties flow
        from the top-level `LineItem` down to the `GeneratorSet`, and finally to a highly specialized `EmergencyGenerator`. Each level inherits all attributes from
        the levels above it.

      

```
type LineItem;
// Level 2: Adds basic generator capacity attributes
type GeneratorSet : LineItem {
int requiredKW = [101..10000];
decimal(2) surgeLoadKW = requiredKW * 1.25; // Calculation shared down the chain
}
// Level 3: Specialized version inheriting everything from GeneratorSet and LineItem
type EmergencyGenerator : GeneratorSet {
// Automatically inherits requiredKW and surgeLoadKW
string DutyRating = "Emergency Standby Power (ESP)"; // Specific fixed rating
}
```

    

    

## Example 3: Abstract Base Models (Polymorphism & Overriding)

      
      

This pattern uses an abstract type as a structural blueprint. Specific components (the "General Models") inherit from this blueprint and override its generic attributes with fixed, real-world ratings.

      

```
// Base model acting as a blueprint for all engine options
type GeneralModel{
int powerKW = [100..2000]; // Broad domain
int dB = [60..100];
}
// Specific product type that overrides parent domains with fixed values
type GeneralModel900 : GeneralModel {
int powerKW = 900; // Overrides broad range with exact value
int dB = 78;
}
// Another specialized model with different fixed properties
type GeneralModel1500 : GeneralModel {
int powerKW = 1500;
int dB = 83;
}
```

=== ARTICLE: cml_types.htm ===
---
page_id: cml_types.htm
title: Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_types.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_cml_core_concepts.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Types

In Constraint Modeling Language (CML), you define types to represent entities or
    objects in the model. Types are the foundational building blocks of CML. A type encapsulates the
    property, relationships, constraint, and rules for the entity.

    
      

A type is similar to a class in object-oriented programming. You can define relationships
        that represent associations between different types. See [Relationships](./cml_relationships.htm.md).

      

#### Note

To define a constraint for a child product in a
        bundle, you must include the entire bundle in the constraint model. For example, if you
        define a constraint for a laptop, and the laptop is a child product in the Laptop Pro
        Bundle, you must include the Laptop Pro Bundle in the constraint model for the constraint on
        the laptop to run.

      

#### Note

Product variants aren't supported in constraint models.

    

    

## Generic Structure of a Type

      
      

This table explains the generic structure of types with examples.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

```

```

            

            
              

              

              

```

```

            

            
              

              

              

```

```

            

            
              

              

              

```

```

            

          

        
| Element | Purpose | Example |
| --- | --- | --- |
| Declaration | Defines the entity name, optionally preceded by annotations and optionally followed by inheritance, if applicable. | `type Product {}` Or optionally: @annotation_name("annotation parameters") type Product: BaseProduct {} |
| Variables (Attributes) | Defines the properties or characteristics of the entity, including data type and domain. | int requiredKW = [101..10000]; string color = ["Red", "Blue"]; |
| Relations | Defines one-to-many associations with other types, specifying cardinality (the quantity range) and optionally, the configuration order. | relation items : LineItem[1..10] {} |
| Constraints and Rules | Enforces business logic and restrictions that must be satisfied by the entity's variables and relationships. | constraint(condition); require(condition, items [type]); |

    

    

## Example: Basic Type Declaration with Variables

      
      

This example shows the declaration of the main `GeneratorSet` type. It defines several core attributes (variables) that
        characterize the product.

      

```
type GeneratorSet{
// Declaration only (inherits LineItem properties)
// Attributes with explicit domains
int requiredKW = [101..10000];
string Voltage = ["220/380", "240/416", "255/440", "277/480", "347/600", "2400/4160", "7200/12470", "7621/13200", "7976/13800];
string DutyRating = ["Prime Power (PRP)", "Continuous Power (COP)", "Data Center Continuous (DCC)", "Emergency Standby Power (ESP)"];
}
```

    

  

- 
**[Type Hierarchies](./cml_type_hierarchies.htm.md)**  

Constraint Modeling Language (CML) supports inheritance and overriding, which allow you     to create hierarchies between types. By establishing these hierarchies, constraint models become     more modular and efficient.

- 
**[Type Annotations](./cml_type_annotations.htm.md)**  

You can annotate types to add information. Type annotations are metadata applied to a     type declaration to provide instructions to the constraint engine regarding how instances of     that type should be handled, instantiated, or used in the configuration structure.

- 
**[Group Type](./cml_group_type.htm.md)**  

In Constraint Modeling Language (CML), a Group Type is used to logically containerize     related components within a bundle configuration, primarily when product component groups are     imported from Product Catalog Management (PCM).

- 
**[Define Constraints for Quote Groups, Ramps, and Ramp Segments](./cml_quote_group_ramp_segment_constraints.htm.md#cml_quote_group_ramp_segment_constraints)**  

Apply rules to quote groups, ramps, and ramp segments by using the   SalesTransactionItemGroup context tag. Assign a groupby value to messages defined in Constraint   Rules Engine to include the messages in custom grouping strategies.

=== ARTICLE: cml_use_the_apex_debugging_log_file.htm ===
---
page_id: cml_use_the_apex_debugging_log_file.htm
title: Use the Apex Debugging Log File
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_use_the_apex_debugging_log_file.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_debugging_cml.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Use the Apex Debugging Log File

To find possible reasons for the performance problems and identify solutions, look at
    the RLM_CONFIGURATOR_STATS section of the log file.

    
      

See the values for Total Execution Time, Constraints Violation Stats, and ChoicePoint
        Backtracking Stats.

      

For example, consider how the constraint engine performs with this sample constraint model.
        In the constraint model, the value of the `volts`
        variable is greater than 110/10000 (`volts = power/amps *
          9999;`). The constraint engine must backtrack the `power` variable to find a value that satisfies the constraint, starting with
        0.01, 0.02, and so on until it reaches a valid value.

      

```
relation laptops : Laptop[1..9999];
@(sequence = 1)
decimal(2) power = [0..500];
@(sequence = 1)
int amps = [1..5];
decimal(2)  volts = (power / amps) * laptops[Laptop];
constraint(volts > 110);
```

      

In the log file for this constraint model, see the execution statistics for Total Execution Time, Constraints Violation Stats, and ChoicePoint Backtracking Stats:

      

```
"rootId" : "ref_a67c6632_fa1f_40b4_8093_226a9ab8a4d0",
"Product" : "Laptop",
"Total Execution Time" : "676ms",
"Constraints Execution Stats" : "Distinct: 2 Total: 132006",
"Solving goal AndGoal([ConfigureComponentGoal(Laptop Laptop_0)]) took " : "677ms",
"Configurator Stats" : "Total Time 677ms",
"Number of Component" : "1",
"Number of Variables" : "4",
"Number of Constraints" : "1",
"Number of Backtracks" : "49500",
"Constraints Violation Stats" : "Distinct: 1 Total: 41250",
"IntComparison(GT,[DecimalVar(volts)])" : "41250",
"ChoicePoint Backtracking Stats" : "Distinct: 2 Total: 98999",
"VariableChoicePoint(DecimalVar(power))" : "49500",
"VariableChoicePoint(IntVar(amps))" : "49499"
```

      

Optimally, execution time for a constraint model is less than 100 milliseconds, with fewer
        than 1,000 backtracks and no violations. Values for the constraint model example are
        significantly higher, indicating that the constraint engine is performing inefficiently. To
        improve performance in this example, reduce the domain of the power variable without
        reducing the solution space. For example, define the domain as `[110..500]` instead of `[0..500]`. This change
        reduces the number of backtracks the constraint engine performs to find a solution.

=== ARTICLE: cml_using_proxy_variables_constraints.htm ===
---
page_id: cml_using_proxy_variables_constraints.htm
title: Proxy Variables with Constraints on Types and Relationships
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_using_proxy_variables_constraints.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_constraints.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Proxy Variables with Constraints on Types and Relationships

Use proxy variables to reference the variables of related types, including parent,
    root, and sibling types.

    
      

The supported proxy variables include:

      
        
- Cardinality

        
- Parent

        
- this.quantity

      

    

    

## Cardinality

      
      

Cardinality is a fundamental concept in Constraint Modeling Language (CML), controlling the
        quantity of product instances allowed in a defined relationship. It’s crucial for ensuring
        product structure validity and optimizing performance.

      

The `cardinality` proxy variable refers to the
        cardinality of a relationship, that is, the quantity of instances of the same type in a
        relationship. The first parameter is the type name. The second, optional parameter is the
        port name. This variable differs from the this.quantity proxy variable, which refers to the
        quantity of the current instance.

      

Use this format:

      

```
cardinality(<type name>, <relation name>) or cardinality(<type name>)
```

      

Each parameter value can be a string or a string variable. If you don’t specify the
        relation name, the engine searches all ports to find the type.

      

The cardinality bounds are defined within the relation declaration with square brackets,
        formatted as `[minimum..maximum]`.

    

    

## Cardinality Examples

      
      

These examples illustrate how cardinality is defined and managed in the Generator Set
        model, focusing on standard definition, conditional enforcement, and reading the
        quantity.

    

    

## Example 1: Using Cardinality Full Syntax

      
      

```
type Heater ;
type GeneratorSet  {
//Define the relation and specify the smallest cardinality required for performance
relation Heaters : Heater[0..10];
//Declare a variable to hold the count
int totalHeaterCount = [0..10];
// This counts instances of type "Heater" specifically within the "Heaters" relation.
int InstancesofHeater = cardinality(Heater, Heaters);
constraint(totalHeaterCount == InstancesofHeater);
// Optional message to display the count to the user
message(totalHeaterCount > 0, "Current configuration includes {} heaters.", totalHeaterCount, "Info");
}
```

      

See [Message
          Rule](./cml_message_rule.htm.md).

    

    

## Example 2: Using Cardinality Partial Syntax

      
      

```
type Heater ;
type OutputTerminal ;
// Main Generator Set type
type GeneratorSet {
// Define multiple relations that might contain specific types, each with a specified cardinality
relation Heaters : Heater[2];
relation OutputTerminals : OutputTerminal[0..99];
// Define derived attributes with an explicit domain
int totalHeatersFound = [0..100];
int totalTerminalsFound = [0..100];
// Partial cardinality SYNTAX
// The engine searches all relations to find the specified type
// Counts all instances of "Heater" across the entire GeneratorSet
int AllHeaterInstances = cardinality(Heater);
constraint(totalHeatersFound == AllHeaterInstances);
// Counts all instances of "OutputTerminal" across all relations
int AllOutputTerminals = cardinality(OutputTerminal);
constraint(totalTerminalsFound == AllOutputTerminals);
// Optional message for user visibility
message(totalHeatersFound > 0, "System found {} heaters in this configuration.", totalHeatersFound, "Info");
}
```

    

    

## Example 3: Defining Cardinality in Relations

      
      

This example shows how the Generator Set uses different cardinality ranges to define fixed
        requirements, optional components, and minimum quantities for necessary components.

      

```
type GeneratorSet {
// 1. Fixed Cardinality: Exactly one General Model (component) is required.
// means min=1 and max=1.
relation GeneralModels : GeneralModel [1..1];
// 2. Bounded Optional Cardinality: Between 0 and 5 Temperature Sensors are allowed.
// [0..5] means the component is optional but limited.
relation TemperatureSensors : TemperatureSensor[0..5];
// 3. Minimum Required Cardinality: At least 1 Test record is required, up to 99.
// [1..99] enforces inclusion.
relation Testing : Test[1..99];
}
type GeneralModel;
type TemperatureSensor;
type Test ;
```

      

Key Concepts:

      
        
- Syntax: Cardinality is specified immediately after the component type in the relation
          declaration.

        
- Best Practice: Specifying the smallest required range, such as [1..1] or [0..5], ensures
          the constraint engine tests fewer combinations, which prevents performance
          degradation.

      

    

    

## Example 4: Enforcing Conditional Cardinality via require()

      
      

Cardinality can be dynamically enforced based on attributes of the parent product using the
          `require()` constraint keyword. For more information,
        see [Require
          Rule](./cml_require_rule.htm.md).

      

```
type GeneratorSet {
int requiredKW = [101..10000];
string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];
// Relation for mandatory installation accessories
relation Accessories : Accessory[1..99];
relation Testing : Test[1..99];
// Conditional Requirement based on power level:
// If the required power is over 5000 kW, exactly 5 specific Accessory instances are required.
require(
requiredKW > 5000,
Accessories [Accessory] == 5,
"High capacity generators require exactly 5 specialized accessory kits."
);
// Conditional Requirement based on compliance standard:
// If UL 2200 is selected, exactly 2 Test records must be included.
require(
standardsAndCompliance == "Listing-UL 2200",
Testing [Test] == 2,
"UL 2200 listing mandates exactly two certification tests."
);
}
type Accessory;
type Test;
```

      

This pattern (`require(condition, relation[type] == N,
          ...)`) allows the CML model to enforce a precise fixed number of child components
        when a quantity threshold or attribute condition is met on the parent.

    

    

## Cardinality vs. Count

      
      

The `cardinality()` keyword is a proxy variable used to
        refer to the size of a relationship. The `count()`
        keyword is an aggregate function that counts matching components or attribute conditions
        within a relation. Both can be used to read quantities for validation or aggregation
        rules.

    

    

## Example for Similarity

      
      

Both `cardinality()` and `count()` can be used to determine the total quantity of items in a relationship.
        In this scenario, they return the same value because the `count()` condition covers all possible active instances.

      

```
type Accessory{
boolean isPresent = true;
}
type Bundle {
relation items : Accessory[0..10];
int totalByCount = [0..10];
// Similarity: Both can read the headcount of the relation
// Use the proxy variable to set an attribute
int totalByCardinality = cardinality(Accessory, items);
// Use count() aggregate function within a constraint
constraint(totalByCount == items.count(isPresent == true));
}
```

    

    

## Example for Difference

      
      

Cardinality is a proxy variable representing the headcount or size of the relation, whereas
        count is a function used to evaluate specific attribute conditions or filters within those
        instances.

      

```
type Accessory {
int weight = [1..100];
boolean isEssential;
}
type Bundle {
relation items : Accessory[1..20];
// 1. Declare variables with explicit domains
int totalHeadcount = cardinality(Accessory,items);
int heavyItemsCount = [0..20];
int essentialItemsCount = [0..20];
// DIFFERENCE 1: Cardinality (Proxy Variable)
// Cardinality refers to the relationship size (how many instances are present).
// It does not look at the values of the attributes within the instances.
// DIFFERENCE 2: Count (Aggregate Function)
// Count MUST use a logical expression to evaluate conditions within the relation.
// It filters the instances based on attribute logic before returning a total.
// Example: Counting only accessories that weigh more than 50kg
constraint(heavyItemsCount == items.count(weight > 50));
// Example: Counting only accessories marked as 'essential'
constraint(essentialItemsCount == items.count(isEssential == true));
// Business Logic using both:
message(
heavyItemsCount > (totalHeadcount / 2),
"Warning: More than half of your accessories ({}) are heavy items.",
heavyItemsCount
);
}
```

      

For more information, see [Message Rule](./cml_message_rule.htm.md).

    

    

## Instance Quantity

Instance Quantity is the
        quantity of a child product per instance of the parent product. It differs from the end
        quantity, which is the total quantity of the child product across all parent instances. For
        example, if a customer orders 3 generator sets and each set requires 2 alternators, the
        instance quantity is 2, the quantity per bundle. The end quantity of alternators is 6.
        

The constraint engine calculates instance quantity when the constraint model CML
        meets all of these conditions.

        
        
- Instance Quantity Access (`orgHasInstanceQtyAccess`)
          is turned on. To turn on Instance Quantity Access, go to Revenue Settings and turn on the
          Instance Quantity Access setting.

        
- The child product's `ProductRelatedComponent` record
          has `QuantityScalingMethod__c` set to Proportional. 

        
- The child product's end quantity divides evenly by the parent product's quantity.

      

The constraint engine divides the child's end quantity by the parent's quantity to
        derive the instance
      quantity.

```
Instance Quantity = Child End Quantity / Parent End Quantity

```

    

## Example: Using this.quantity to Calculate Instance
        Quantity 

In the Generator Set configuration, `instanceQty` is assigned the value of `this.quantity`. Quantities for `MainAlternator` and `TemperatureSensor` are
        returned as instance quantities of `GeneratorSet`.

The require rule validates against `instanceQty` values, confirming the per-set configuration is correct regardless
        of how many sets the customer orders.
      

```
type LineItem;
type GeneratorSet : LineItem {
   int instanceQty = this.quantity;
   int requiredKW = [101..10000];
   relation alternators: MainAlternator;
   relation sensors: TemperatureSensor;
   // Enforce per-unit component counts using instance quantities
   require(alternators.instanceQty == 2,
           alternators[MainAlternator] == 2,
           "Each generator set requires exactly 2 main alternators");
   require(sensors.instanceQty >= 1 && sensors.instanceQty <= 5,
           sensors[TemperatureSensor],
           "Each generator set requires 1 to 5 temperature sensors");
   message(true,
           "Generator set qty: {}, alternators per set: {}, sensors per set: {}",
           instanceQty, alternators.instanceQty, sensors.instanceQty);
}
type MainAlternator : LineItem {
   int instanceQty = this.quantity;  // Per-generator-set quantity when QSM is Proportional
}
type TemperatureSensor : LineItem {
   int instanceQty = this.quantity;  // Per-generator-set quantity when QSM is Proportional
}

```

    

## Parent

      
      

The `parent()` proxy variable is used to turn on
        components at any level of the product hierarchy (child, grandchild, and so on) to access
        the attributes (variables) defined by their ancestor types. This mechanism facilitates the
        flow of configuration data and calculated values from the top of the bundle down to its
        components.

      

The `parent()` keyword functions as a proxy variable
        used to reference attributes residing in the immediate parent or any ancestor type in the
        configuration model.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

          

        
| Variable Name | Syntax | Purpose |
| --- | --- | --- |
| `parent()` | `parent(<ancestor variable name>, <level>)` | Retrieves the value of an attribute from a parent or ancestor type. |

    

    

## Key Characteristics

      
      
        
- Targeting Ancestors: The first parameter is the name of the attribute in the ancestor
          type that you want to reference.

        
- Level Parameter: The second parameter (`<level>`) is optional and specifies how many levels up the hierarchy the
          engine searches. If omitted, it typically references the immediate parent. The level index
          for the `parent()` function effectively starts from 0
          (implicit) for the immediate parent.

        
- Level 0 (Default): When you use `parent(attributeName)`, the engine references the attribute in the immediate
          parent.

        
- Level n: When you specify `parent(attributeName, 1)`,
          the engine reaches one level beyond the immediate parent, to the grandparent.

        
- Data Flow: `parent()` makes sure that the data flows
          unidirectionally, where the child reads attributes calculated or defined by the parent,
          which helps to prevent complex circular dependencies.

        
- Single Inheritance: CML follows a single inheritance model, where a type can only extend
          one other type at a time.

        
- Same Variable Name: In CML, using the same variable name between a parent bundle and its
          child accessories is a standard architectural pattern for cascading values down a product
          hierarchy. This allows a child component to automatically inherit or synchronize its
          properties with the parent type, ensuring configuration consistency.

      

    

    

## Example: Standards and Compliance Synchronization

      
      

In this example, the `standardsAndCompliance` selection
        made at the bundle level is passed down to every accessory within that bundle.

      

```
type AccessoryBundle {
// 1. Define the attribute at the Bundle level
string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"];
// Relation to accessories
relation accessories : Accessory[1..10];
}
type Accessory {
// 2. Reuse the same variable name
// The parent() function targets the attribute in the immediate parent
string standardsAndCompliance = parent(standardsAndCompliance);
// Business Logic: If the inherited standard is UL 2200, price is affected
decimal(2) testingFee = [0.00..500.00];
constraint(standardsAndCompliance == "Listing-UL 2200" -> testingFee == 250.00);
}
```

      

The `parent()` proxy variable is essential for cascading
        configuration data and constraints down the product hierarchy, so that child components
        reference attributes defined by their ancestors.

    

    

## Example: Parent Attribute Reference

      
      

This example uses attributes found on the `GeneratorSet`
        type (the parent) and demonstrates how related components (like TemperatureSensor) access
        those values using the parent() proxy variable. Here’s the hierarchy context.

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Parent Type | Relation Name | Child Type | Cardinality | Key Attribute Usage |
| --- | --- | --- | --- | --- |
| Root `GeneratorSet` | `TemperatureSensors` | `TemperatureSensor` | `[0..5]` | Defines primary inputs (`requiredKW`) and a derived attribute (`ULComplianceEnforced`) based on the `standardsAndCompliance` selection. |
| Child `TemperatureSensor` (Instance within `GeneratorSet` relation) | Not Applicable | Not Applicable | Not Applicable | Uses the `parent() `proxy variable to reference the `requiredKW` attribute from its ancestor (`GeneratorSet`). A constraint ensures the component's capacity (`maxOperatingKW`) meets the requirement inherited from the parent. |
| Grandchild `StatorTemperatureSensor` (Subtype of `TemperatureSensor`) | Not Applicable | Not Applicable | Not Applicable | Inherits functionality from `TemperatureSensor`. Uses parent() to retrieve the calculated `ULComplianceEnforced` boolean from the `GeneratorSet`. Enforces a conditional installation rule using the Implication Operator (->). |

      

```
// --- Parent Type (GeneratorSet) ---
type GeneratorSet {
// Attributes defined by the parent
int requiredKW = [101..10000]; // Required power rating
string standardsAndCompliance = ["Certification-CSA", "Listing-UL 2200"]; // Compliance choice
// Derived status: True if UL 2200 is selected (precondition for compliance checks)
boolean ULComplianceEnforced = standardsAndCompliance == "Listing-UL 2200";
// Relation to child components
relation TemperatureSensors : TemperatureSensor[0..5];
}
// --- Child Component Type (TemperatureSensor) ---
type TemperatureSensor {
// Temperature sensors may have a model that defines max operating KW
int maxOperatingKW = [1000..10000];
// Retrieve the required KW value from the immediate parent (GeneratorSet)
int parentRequiredKW = parent(requiredKW);
// Constraint ensures the sensor can handle the power defined by the parent
constraint(maxOperatingKW >= parentRequiredKW, "Sensor capacity must meet the required KW set by the generator set.");
}
// --- Specific Sensor Type (Grandchild) ---
type StatorTemperatureSensor : TemperatureSensor {
// Retrieve the boolean compliance flag from the immediate parent (GeneratorSet)
boolean enforceULCompliance = parent(ULComplianceEnforced);
// Constraint ensures that if UL Compliance is enforced by the parent,
// this sensor must meet a specific installation requirement (e.g., must be shielded)
string installationMethod = ["Standard", "Shielded"];
constraint(enforceULCompliance -> installationMethod == "Shielded",
"UL Compliance requires a shielded temperature sensor installation."
);
}
// Note: To reference a value further up the hierarchy, the optional level parameter can be used:
// int grandParentValue = parent(requiredKW, 1); // Accesses attribute 1 level up
```

    

    

## Explanation of Parent Reference

      
      
        
- Direct Reference (Immediate Parent): In the `TemperatureSensor` type, `int parentRequiredKW =
            parent(requiredKW);` accesses the `requiredKW` attribute defined in the immediately superior type, which is
            `GeneratorSet`.

        
- Unidirectional Data Flow: The `parent()` proxy
          variable is critical for enabling unidirectional data flow, where calculated or defined
          values in the parent are read by children to enforce constraints. The engine makes sure
          that parent aggregation and calculation are complete before the `parent()` function executes in the child component.

      

    

    

## this.quantity

      
      

`this.quantity` is a proxy variable used specifically to
        access the quantity of the current instance (the specific product line item) within a
        configuration.

    

    

## Key Characteristics and Usage

      
      
        
- Scope: It refers only to the quantity of the specific instance in which it’s used. It’s
          used at the component level to determine the quantity of that item selected by the user or
          set by the constraint engine.

        
- Calculation Rule: The `this.quantity` proxy variable
          can be used only within a calculation rule.

        
- Distinction from `cardinality()`: `this.quantity` differs from the `cardinality()` proxy variable, which refers to the total number of instances of
          a specific type within a relationship and includes the quantity of other instances of the
          same type.

        
- Read-Only/Validation: When accessing quantity in CML, attributes like `this.quantity`, or external equivalents like `lineItemQuantity` or `ItemEndQuantity`, are treated as read only and should be used only in
          calculation or evaluation rules. It isn’t recommended to use it to drive component
          creation, which should be done via cardinality.

      

    

    

## Example: Using this.quantity for Calculation

      
      

In the Generator Set configuration, a component like the `NaturalGasReformer` uses `this.quantity` to
        define a local attribute representing how many units were selected, which is used for
        internal calculations (like total capacity or total weight contribution).

      

```
type LineItem;
type NaturalGasReformer : LineItem {
// 1. Definition: The LineItemQuantity attribute captures the quantity of this specific instance.
// The CML syntax dictates defining an attribute (LineItemQuantity) that equals this.quantity.
int LineItemQuantity = this.quantity;
// Placeholder: Attribute representing unit capacity per reformer unit
int unitCapacityKW = 100;
// 2. Calculation: Used in a calculation rule to determine total capacity based on the quantity selected for this line item instance.
int totalReformerCapacity = LineItemQuantity * unitCapacityKW;
}
```

=== ARTICLE: cml_variable_annotations.htm ===
---
page_id: cml_variable_annotations.htm
title: Variable Annotations
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_variable_annotations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variable Annotations

You can annotate variables with properties such as configurable, defaultValue,
    domainComputation, and relatedAttributes.

    
      

In this example, the `gc_runningKw` variable is
        annotated to indicate that it's not configurable and has a default value of `0.00`.

      

#### Note

This example requires an enclosing type.

      

```
@(configurable = false, defaultValue = 0.00)
decimal(2) gc_runningKw;
```

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

- 
- 

            

            
              

              

              

            

          

        
| Property | Values | Description |
| --- | --- | --- |
| allowOverride | true, false | Allows the engine to recalculate a value even if a value was already received from core. This annotation helps save on performance by allowing early calculation. |
| configurable | true, false | Indicates whether the variable is configurable (`true`) or not (`false`). If the configurable annotation isn’t explicitly specified, the engine sets it implicitly as `true` for the variable. If the configurable annotation is explicitly specified as `true`, the variable is indicated as configurable. The engine can set the value to the variable according to the defined logic, and users can modify it. If the configurable annotation is explicitly specified as `false`, the engine cannot set a value to the variable, and users can't update it. The variable value in this case is set through the PCM default. See examples [here](./cml_annotation_examples.htm.md). |
| defaultValue | literal | Indicates the default value for the variable. The configurator uses the default value defined in PCM (in Product Attribute Definition). If no PCM default is available, the configurator uses the first value in the variable domain as the initial value. If no default value is defined in PCM and a defaultValue is specified in CML, the configurator uses the value defined in CML as the initial value of the variable. See examples [here](./cml_annotation_examples.htm.md). |
| domainComputation | true, false | domainComputation is a CML annotation that specifies how the domain of a model element is determined, either by using a fixed domain or by computing the domain dynamically during configuration. If domainComputation is not explicitly specified, the engine sets it implicitly as false for the variable. If the domainComputation is specified as true, the variable domain is dynamically determined based on the configuration and constraint logic. If the domainComputation is specified as false, the variable domain is fixed. See examples [here](./cml_annotation_examples.htm.md). |
| nullAssignable | true, false | Sets an initial value for the calculated variable if the expression value can't be calculated. |
| Peelable | true, false | Indicates whether the constraint engine can override the variable’s value (whether set by default or user selection) to resolve a conflict (`true`) or not (`false`). If set to `true`, the engine treats the value as a "soft selection." When a configuration conflict occurs, the engine attempts to "peel" (unbind) this variable and retry the solution. If a valid configuration is found, the engine automatically changes the value to satisfy constraints, rather than displaying an error message to the user. If not explicitly set, or set to false, the engine treats the value as a "hard selection." If the value causes a conflict with a constraint, the engine will not attempt to change it automatically. Instead, it will stop and display a conflict error message to the user, requiring manual intervention to resolve the issue. See examples [here](./cml_annotation_examples.htm.md). |
| productGroup | integer | Used to represent the group cardinality for relationships under a type, either for specified relationships, or for all relationships (using`*`). We recommend using `maxInstanceQty` and `minInstanceQty` type annotations instead of productGroup. See [Type Annotations](./cml_type_annotations.htm.md). |
| relatedAttributes | string value | relatedAttributesannotation is required to reset the domain to the original domain for domain computation. If relatedAttributes annotation is not specified, the engine updates the variable domain according to domainComputation and constraint logic. If the relatedAttributes annotation is specified with one or multiple values (separated by comma), the variable domain is reset to the original domain. See examples [here](./cml_annotation_examples.htm.md). |
| sequence | integer | Indicates the sequence in which variables are configured. If a sequence value is not explicitly defined, the configurator implicitly determines the order based on the variable declaration order in the CML model. If a sequence value is explicitly defined, the configurator uses the sequence number to control the order in which variables are configured. Variables with lower sequence values are assigned first. See examples [here](./cml_annotation_examples.htm.md). |
| setDefault | true, false | Sets the variable status to default. |
| source | string value | Data source defined in the model. |
| sourceAttribute | Variable name in string | Sets the domain of the current variable to be the domain of the source variable. |
| strategy | descending, ascending, string | Defines the strategy to configure the variable. If the strategy is ascending, the engine tries values from low to high. If the strategy is descending, the engine tries values from high to low. See example [here](./cml_annotation_examples.htm.md). |
| tagName | string value | To create an external variable linked to a Sales Transaction header, use the tagName annotation with the contextPath annotation to reference context tags on SalesTransactionItem within a type. See contextPath in [External Variable Annotations](./cml_external_variables.htm.md). |

=== ARTICLE: cml_variable_data_types.htm ===
---
page_id: cml_variable_data_types.htm
title: Variable Data Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_variable_data_types.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variable Data Types

Variables support multiple data types including boolean, date, decimal, and so on.
    Variables without a domain definition may remain unbound, leading to errors.

    
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Data Type | Description | Defaulting Example |
| --- | --- | --- |
| boolean | Only true, false, or null can be assigned as a value. | `@(defaultValue="true") boolean isActive;` |
| date | A value that indicates a particular day, the same as local date in Java. | `date shipDate = ["2023-01-01".."2023-12-31"]; `If there's no `defaultValue` specified, the variable defaults to the first value in the domain. See the [Constraints using Format Specifiers (%s, %d) and Dates example](./cml_core_concept_examples.htm.md). |
| double(n) | A 64-bit number that includes a decimal point, the same as double in Java. | `double(2) percentage = [0.00..100.00];`If there's no defaultValue specified, the variable defaults to the first value in the domain. |
| decimal(n) | A fixed-point numeric value with n decimal places. Note: The decimal variable data type isn't supported for the quantity field in quote line items. Use the integer data type for the quantity field. | `decimal(2) TaxRate = 0.08;` |
| int | Integer. A 32-bit number that doesn't include a decimal point, the same as int in Java. | `@(defaultValue = "5") int defaultQty = [1..10];`If there's no `defaultValue` specified, the variable defaults to the first value in the domain. |
| string | Any set of characters surrounded by double quotes (") | `@(defaultValue = "Red") string color = ["Red", "Green", "Blue"];`If there's no `defaultValue` specified, the attribute defaults to the first value in the domain. |
| string[] | Used in multi-select picklists for the user to select more than one item from multiple options. For example, if a user selects "Red", "Green", and "Blue" values in a color picker, this variable holds those selected values. | `@(defaultValue = '["Red", "Green"]') string[] selectedColors;` If there's no `defaultValue` specified, the attribute picklist defaults to the first value in the domain. |

=== ARTICLE: cml_variable_domains_and_domain_restrictions.htm ===
---
page_id: cml_variable_domains_and_domain_restrictions.htm
title: Variable Domains and Domain Restrictions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_variable_domains_and_domain_restrictions.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_variables.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variable Domains and Domain Restrictions

A variable can have a fixed domain that defines a set of permitted values. You can
    specify the domain as a list of discrete values, a continuous range, or a combination.

    

## Variable Domains and Domain Restrictions

      
      

A variable can have a fixed domain that defines a set of permitted values. You can specify the domain as:

      
        
- A list of discrete values

        
- A continuous range

        
- A combination of ranges and discrete values

      

      

For more information, see domainComputation in [Variable Annotations](./cml_variable_annotations.htm.md).

    

    

## Example

      
      

This example defines a `SwitchgearBay` type with three
        variables, each having a fixed domain.

      
        
- 
`BayType` can be one of the specified string
          values.

        
- 
`Bay_Number` can be any integer from 1 through 9
          (inclusive).

        
- 
`Total_Power_Required_kW` can be any integer from 1
          through 100000 (inclusive).

      

      

#### Note

For string (picklist) variables, if you don't specify a `defaultValue` annotation and don't define a default in the
        Product Attribute Definition in Product Catalog Management (PCM), the configurator uses the
        first value in the domain as the initial value. In the example, `BayType` defaults to `"load"`. To set a
        different default, use the ` defaultValue` annotation on
        the variable. To avoid inconsistent behavior at run time, use the same default value in CML
        as the default value you define in PCM.

      

```
type SwitchgearBay {
  string BayType = ["load", "lv", "mv"];
  int Bay_Number = [1..9];
  int Total_Power_Required_kW = [1..100000];
}
```

=== ARTICLE: cml_variables.htm ===
---
page_id: cml_variables.htm
title: Variables
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_variables.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: cml_cml_core_concepts.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Variables

Variables are the properties or characteristics defined within a type. Variables can hold
    different types of data and can be calculated from other values.

- 
**[Variable Domains and Domain Restrictions](./cml_variable_domains_and_domain_restrictions.htm.md)**  

A variable can have a fixed domain that defines a set of permitted values. You can     specify the domain as a list of discrete values, a continuous range, or a combination.

- 
**[Variable Data Types](./cml_variable_data_types.htm.md)**  

Variables support multiple data types including boolean, date, decimal, and so on.     Variables without a domain definition may remain unbound, leading to errors.

- 
**[Mathematical Functions (Numerical Derivation)](./cml_mathematical_functions_numerical_derivation.htm.md)**  

Mathematical functions and operators are used to calculate derived values based on     arithmetic relationships between variables.

- 
**[String Variable Functions and Operators](./cml_string_variable_functions_and_operators.htm.md)**  

Constraint Modeling Language (CML) provides string manipulation and conversion     functions, and string comparison and validation operators.

- 
**[Variable Annotations](./cml_variable_annotations.htm.md)**  

You can annotate variables with properties such as configurable, defaultValue,     domainComputation, and relatedAttributes.

- 
**[External Variables](./cml_external_variables.htm.md)**  

External variables are global Constraint Modeling Language (CML) variables defined     within a virtual CML type.

=== ARTICLE: cml_what_is_constraint_modeling_language.htm ===
---
page_id: cml_what_is_constraint_modeling_language.htm
title: Constraint Modeling Language
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/cml_what_is_constraint_modeling_language.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Constraint Modeling Language

Constraint Modeling Language (CML) is a domain-specific language that defines models
    for complex systems. For product configuration, constraint models describe real-world entities
    and their relationships to each other.

    

Constraint models enforce business logic declaratively, without the need for extensive code
      in a general-purpose programming language. In Product Configurator, a product designers or
      admin create a constraint model in CML, then Constraint Rules Engine compiles the CML code.
      The constraint model enforces requirements in a product configuration to comply with the
      specified constraints.

    

To build a constraint model in CML, use this basic workflow.

    
      
- Create global properties and settings that are header-level declarations in CML that
        define the foundational, fixed values for the entire constraint model. They’re crucial for
        setting up the core configuration environment and ensuring reusability across the
        model.

      
- Create variables to define the properties or characteristics of a type. Variables can hold
        different kinds of data, such as strings, numbers, or lists, and can be calculated from
        other variables and values. In Revenue Management, variables represent product fields, product
        attributes, and sometimes context tags. See [Create a Context Definition](https://help.salesforce.com/s/articleView?id=ind.context_service_create_context_definitions.htm&language=en_US)
        in Salesforce Help.

      
- Define types, which represent entities or objects in the model. Types are the building
        blocks of CML. They're similar to classes in object-oriented programming. In Revenue Management,
        types represent standalone products, bundles, product components, and product classes.

      
- Define relationships that describe how different types are associated with each other. In
        Revenue Management, relationships represent the product structure in a bundle. For example, the
        root product has a relationship with its components.

      
- Apply constraints to define logical restrictions, and enforce rules and conditions on
        types, variables, and relationships.

    

    

In Product Configurator, use the Visual Builder and CML Editor in Constraint Builder to
      create constraint models with CML.

    
      
- [Use Constraint Builder With
          Constraint Rules Engine](https://help.salesforce.com/s/articleView?id=ind.product_configurator_constraint_builder.htm&language=en_US)

      
- [Define Constraints and Rules with
          the Visual Builder](https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_visual_builder.htm&language=en_US)

      
- [Use Code to Define Constraints and
          Rules in the CML Editor](https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_cml_editor.htm&language=en_US)

    

    

See the linked topics for information on working with CML, including detailed code
      examples.

  

- 
**[Modeling a Generator Set](./cml_constraint_model_example_modeling_a_generator_set.htm.md)**  

The Constraint Model for a Generator Set examples use CML to define a technical power     configuration, illustrating concepts such as calculated variables, enforcement of external     standards, and component selection based on requirements.

- 
**[Core Concepts](./cml_cml_core_concepts.htm.md)**  

Constraint Modeling Language (CML) includes components that cover high-level global         configurations to specific data types and constraints.

- 
**[Core Concept Examples](./cml_core_concept_examples.htm.md)**  

These examples illustrate core Constraint Modeling Language (CML) concepts including     type, relationships, constraints, and so on.

- 
**[Annotation Examples](./cml_annotation_examples.htm.md)**  

Constraint Modeling Language (CML) annotations are labels that you add to parts of a     model, such as types, variables, relationships, and constraints. Annotations control how these     elements are shown and how they behave in the configurator. Annotations help fine-tune the     configurator and the constraint engine without changing the actual structure of the     model.

- 
**[Constraint Modeling Language (CML) Best Practices](./cml_cml_best_practices.htm.md)**  

To prevent performance degradation or unexpected behaviors when the constraint engine     executes CML code, follow these practices when writing code.

- 
**[Business-Centric Constraint Modeling Language (CML) Guidelines](./cml_business-centric_cml_guidelines_quantity_and_aggregation_fun.htm.md)**  

Constraint Modeling Language (CML) must accurately calculate the total sum or aggregate     of specific attributes like quantity or userCount across child components, especially in complex     configurations requiring group-level aggregation

- 
**[Debugging Constraint Modeling Language (CML)](./cml_debugging_cml.htm.md)**  

To debug constraint models and troubleshoot performance issues, enable debug logging in     Apex and set the debug log level to FINE.

- 
**[Model Structure](./cml_appendix_model_structure.htm.md)**  

The tables on the following pages show the structure for the constraint model in Core     Concept Examples.

=== ARTICLE: connect_requests_add_nodes_configurator_input.htm ===
---
page_id: connect_requests_add_nodes_configurator_input.htm
title: Configurator Add Nodes Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_add_nodes_configurator_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Add Nodes Input

Input representation of the request to add nodes within a root node.

**JSON example**

: 

```
{
  "configuratorOptions": {
    "executePricing": true,
    "returnProductCatalogData": true,
    "qualifyAllProductsInTransaction": true,
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },
  "qualificationContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "addedNodes": [
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589"
      ],
      "addedObject": {
        "id": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemSource": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemParent": "0Q0xx0000004EvcCAE",
        "PricebookEntry": "01uxx00000090VuAAI",
        "ProductSellingModel": "0jPxx00000001KHEAY",
        "UnitPrice": 15.26,
        "Quantity": 1,
        "Product": "01txx0000006lfHAAQ",
        "businessObjectType": "QuoteLineItem"
      }
    },
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ref_d85b036d_d305_4bb6_aba8_a1dff645a664"
      ],
      "addedObject": {
        "id": "ref_d85b036d_d305_4bb6_aba8_a1dff645a664",
        "MainItem": "0QLxx0000004QdRGAU",
        "AssociatedItem": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ProductRelatedComponent": "0dSxx00000001p6EAA",
        "ProductRelationshipType": null,
        "AssociatedItemPricing": "NotIncludedInBundlePrice",
        "AssociatedQuantScaleMethod": "Proportional",
        "businessObjectType": "QuoteLineRelationship"
      }
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `added​Nodes` | [Configurator Added Node Input](./connect_requests_configurator_added_node_input.htm.md)[] | List of the nodes to be added. | Required | 60.0 |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |

=== ARTICLE: connect_requests_config_rule_input.htm ===
---
page_id: connect_requests_config_rule_input.htm
title: Configuration Rule Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_config_rule_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Rule Input

Input representation of the details of a configuration rule.

**JSON example**

: 

```
{
  "transactionContextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "transactionId": "0Q0DU0000005tJh0AI",
  "ruleOptions": {
    "isUpdateContextRequired": false
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `ruleOptions` | [Config Rule Options Input](./connect_requests_config_rule_options_input.htm.md)[] | Details of the options to run specific steps in rules. | Optional | 67.0 |
| `transactionContextId` | String | ID of the sales transaction context instance. | Required if the `transactionId` property isn’t specified. | 67.0 |
| `transactionId` | String | ID of the quote or order. | Required if the `transactionContextId` property isn’t specified. | 67.0 |

- 
**[Configuration Rule Options Input](./connect_requests_config_rule_options_input.htm.md)**  

Input representation of the details of the configuration rule options.

=== ARTICLE: connect_requests_config_rule_options_input.htm ===
---
page_id: connect_requests_config_rule_options_input.htm
title: Configuration Rule Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_config_rule_options_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: connect_requests_config_rule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Rule Options Input

Input representation of the details of the configuration rule options.

**JSON example**

: 

```
{
  "ruleOptions": {
    "isUpdateContextRequired": false
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `isUpdateContextRequired` | Boolean | Indicates whether context update is required with the capability to automatically add or delete a product and its components (`true`) or not (`false`). If Place Sales Transaction API is invoked with configuration enabled, set this property to `false` to avoid any redundant execution of context logic. | Optional | 67.0 |

=== ARTICLE: connect_requests_configurator_added_node_input.htm ===
---
page_id: connect_requests_configurator_added_node_input.htm
title: Configurator Added Node Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_added_node_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Added Node Input

Input representation of the nodes to be added to a product configuration.

**JSON example**

: 

```
{
  "addedNodes": [
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589"
      ],
      "addedObject": {
        "id": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemSource": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemParent": "0Q0xx0000004EvcCAE",
        "PricebookEntry": "01uxx00000090VuAAI",
        "ProductSellingModel": "0jPxx00000001KHEAY",
        "UnitPrice": 15.26,
        "Quantity": 1,
        "Product": "01txx0000006lfHAAQ",
        "businessObjectType": "QuoteLineItem"
      }
    },
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ref_d85b036d_d305_4bb6_aba8_a1dff645a664"
      ],
      "addedObject": {
        "id": "ref_d85b036d_d305_4bb6_aba8_a1dff645a664",
        "MainItem": "0QLxx0000004QdRGAU",
        "AssociatedItem": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ProductRelatedComponent": "0dSxx00000001p6EAA",
        "ProductRelationshipType": null,
        "AssociatedItemPricing": "NotIncludedInBundlePrice",
        "AssociatedQuantScaleMethod": "Proportional",
        "businessObjectType": "QuoteLineRelationship"
      }
    }
  ]
}
```

          
: This example shows a sample request for
            orders.

```
{
  "addedNodes": [
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589"
      ],
      "addedObject": {
        "id": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemSource": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemParent": "0Q0xx0000004EvcCAE",
        "PricebookEntry": "01uxx00000090VuAAI",
        "ProductSellingModel": "0jPxx00000001KHEAY",
        "UnitPrice": 15.26,
        "Quantity": 1,
        "Product": "01txx0000006lfHAAQ",
        "businessObjectType": "OrderItem"
      }
    },
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ref_d85b036d_d305_4bb6_aba8_a1dff645a664"
      ],
      "addedObject": {
        "id": "ref_d85b036d_d305_4bb6_aba8_a1dff645a664",
        "MainItem": "0QLxx0000004QdRGAU",
        "AssociatedItem": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ProductRelatedComponent": "0dSxx00000001p6EAA",
        "ProductRelationshipType": null,
        "AssociatedItemPricing": "NotIncludedInBundlePrice",
        "AssociatedQuantScaleMethod": "Proportional",
        "businessObjectType": "OrderItemRelationship"
      }
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
| `added​Object` | Map<String, Object> | Details of the object that’s being added. This property supports fields of objects from the Sales Transaction context definition, including custom objects and fields in your extended context definition. | Required | 60.0 |
| `path` | String[] | Path to the node that’s being added. The path includes the unique ID of the context node in the data structure. This ID must match the ID of the sales transaction item source such as a quote line or an order line item. Keep these considerations in mind when setting the `path` value. If the `businessObjectType` property value is `QuoteLineItem`, the path must contain 2 IDs. The first ID is the quote ID, and the second ID is the quote line item ID. If the `businessObjectType` property value is `QuoteLineItem`, the path must contain `SalesTransactionItemSource` and `SalesTransactionItemParent`. If the `businessObjectType` property value is `QuoteLineItemRelationship`, the path must contain 3 IDs. The first ID is the quote ID. The second ID is the quote line item ID. The third ID is the quote line item relationship ID. | Required | 60.0 |

=== ARTICLE: connect_requests_configurator_deleted_node_input.htm ===
---
page_id: connect_requests_configurator_deleted_node_input.htm
title: Configurator Deleted Node Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_deleted_node_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Deleted Node Input

Input representation of the nodes to be deleted from a product configuration.

**JSON example**

: 

```

    "deletedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"]
        }
    ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `path` | String[] | Path to the node that’s being deleted. | Required | 60.0 |

=== ARTICLE: connect_requests_configurator_input.htm ===
---
page_id: connect_requests_configurator_input.htm
title: Configurator Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Input

Input representation of the request to modify the product configuration.

**JSON example**

                    
: This example shows a sample to initiate a context based on a transaction
                        ID.

                    
: 
                        

```
{
    "transactionLineId": "0QLDE000000IBXw4AO",
    "transactionId": "0Q0xx0000000001GAA",
    "correlationId": "c95246d4-102c-4ecd-a263-f74ac525d1e5",
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    }
}
```

                    

          
: This example shows a sample to add, update, or delete a node in an existing
            context.

: 

```
{
    "transactionLineId": "0QLDE000000IBXw4AO",
    "transactionId": "0Q0DE000000ISHJs81",
    "correlationId": "c95246d4-102c-4ecd-a263-f74ac525d1e5",
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "contextResponseType": "Full",
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "transactionContextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "addedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "sti2_id"],
            "addedObject": {
                "id": "ref_sti2_id",
                "SalesTransactionSource": "sti2_id",
                "PricebookEntry": "01uxx0000000001AAA",
                "ProductSellingModel": "0jPxx0000000001AAA",
                "businessObjectType": "QuoteLineItem",
                "Quantity": 10,
                "UnitPrice": 2.0,
                "Product": "01txx0000000001AAA"
            }
        },
        {
            "path": ["0Q0DE000000ISHJs81", "ref_sti2_id","ref_stir1_id"],
            "addedObject": {
                "id": "ref_stir1_id",
                "businessObjectType": "QuoteLineItemRelationship",
                "MainItem": "0QLDE000000IBXw4AO",
                "AssociatedItem": "ref_sti2_id",
                "ProductRelatedComponent": "0dSxx0000000001AAA",
                "ProductRelationshipType": "0yoxx0000000001AAA",
                "AssociatedItemPricing": "IncludedInBundlePrice"
                
            }
        }
    ],
    "updatedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"],
            "updatedAttributes": {
                "Quantity": 5
            }
        }
    ],
    "deletedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"]
        }
    ]
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
| `added​Nodes` | [Configurator Added Node Input](./connect_requests_configurator_added_node_input.htm.md)[] | List of added context nodes that’s passed to the product configurator. | Optional | 60.0 |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md)[] | Options to pass to the configurator. | Optional | 60.0 |
| `context​ResponseType` | String | Specifies the type of transaction context response. Valid values are: `Delta`—Returns the sales transaction items that are added or updated. `Full`—Returns all sales transaction items in a transaction. `None`—Returns empty transaction context response. `Product`—Returns the sales transaction items related to the product that's being configured. | Required for large sales transactions with more than 1000 line items and less than 15K line items. | 65.0 |
| `correlation​Id` | String | ID that’s specified for traceability of logs. | Optional | 60.0 |
| `deleted​Nodes` | [Configurator Deleted Node Input](./connect_requests_configurator_deleted_node_input.htm.md)[] | List of deleted context nodes that’s passed to the product configurator. | Optional | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md)[] | Details such as account ID, contact ID, and context ID that are used for executing qualification rules. | Optional | 60.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 60.0 |
| `transaction​Id` | String | ID of the sales transaction that’s being configured such as a quote or an order. | Required | 60.0 |
| `transaction​LineId` | String | ID of the top-level line item that’s being configured. | Optional | 60.0 |
| `updated​Nodes` | [Configurator Updated Node Input](./connect_requests_configurator_updated_node_input.htm.md)[] | List of updated context nodes that’s passed to the product configurator. | Optional | 60.0 |

#### See Also

- [*Salesforce Help*: Context Service](https://help.salesforce.com/s/articleView?id=ind.context_service.htm&type=5&language=en_US)

- [*Developer Documentation*: Context Service](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/context_service_overview.htm)

=== ARTICLE: connect_requests_configurator_options_input.htm ===
---
page_id: connect_requests_configurator_options_input.htm
title: Configurator Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_options_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Options Input

Input representation of the request to get the product configuration options that’s
    passed to the configurator.

**JSON example**

: 

```

    "configuratorOptions": 
      {
        "addDefaultConfiguration": true,
        "executeConfigurationRules": true,
        "executePricing": true,
        "qualifyAllProductsInTransaction": true,
        "validateAmendRenewCancel": true,
        "validateProductCatalog": true
    }
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `add​Default​Configuration` | Boolean | Indicates whether to add the default configurations (`true`) or not (`false`). | Optional | 60.0 |
| `execute​Configuration​Rules` | Boolean | Indicates whether to execute the configuration rules (`true`) or not (`false`). | Optional | 60.0 |
| `execute​Pricing` | Boolean | Indicates whether to execute pricing (`true`) or not (`false`). | Optional | 60.0 |
| `explainability​Enabled` | Boolean | Indicates whether additional metadata about how the solver achieved the execution request solution must be collected and made available to the caller (`true`) or not (`false`). If you set this property to `true`, you can get explainability action logs by using the [Action Logs API](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/connect_resources_get_create_action_logs.htm). See [Troubleshoot Product Configurations](https://help.salesforce.com/s/articleView?id=ind.revenue_product_configuration_logs.htm&language=en_US) to set up configuration logs. | Optional | 66.0 |
| `pricing​Procedure` | String | Name of the pricing procedure to use during the API calls to Salesforce Pricing Management. | Optional | 60.0 |
| `qualifyAll​ProductsIn​Transaction` | Boolean | Indicates whether to run the qualification rules on all the products in the context (`true`) or not (`false`). | Optional | 60.0 |
| `returnProduct​Catalog​Data` | Boolean | Indicates whether to return the product catalog data (`true`) or not (`false`). Exclude this property or specify the property value as `false` if you’re using the API without the Product Configurator UI. | Optional | 60.0 |
| `validateAmend​Renew​Cancel` | Boolean | Indicates whether to run the amend, renew, cancel-related validations (`true`) or not (`false`). | Optional | 60.0 |
| `validate​Product​Catalog` | Boolean | Indicates whether to run the validations against the product catalog (`true`) or not (`false`). | Optional | 60.0 |

=== ARTICLE: connect_requests_configurator_updated_node_input.htm ===
---
page_id: connect_requests_configurator_updated_node_input.htm
title: Configurator Updated Node Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_updated_node_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Updated Node Input

Input representation of the nodes to be updated in a product configuration.

**JSON example**

: 

```

    "updatedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"],
            "updatedAttributes": {
                "Quantity": 5
            }
        }
    ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `path` | String[] | Path to the node that’s being updated. | Required | 60.0 |
| `updated​Attributes` | Map<String, Object> | Details of the object that’s being updated. This property supports fields of objects from the Sales Transaction context definition, including custom objects and fields in your extended context definition. | Required | 60.0 |

=== ARTICLE: connect_requests_configurator_user_context_input.htm ===
---
page_id: connect_requests_configurator_user_context_input.htm
title: User Context Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_user_context_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# User Context Input

Input representation of the request to get the context details of a user, which are
    used for qualification rules.

    
      
        
          

**JSON example**

          
: 
            

```

    "qualificationContext": {
        "accountId": "001DU000001nHUGYA2",
        "contactId": "003xx00000000D7AAI"
    }
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account in a user context. | Optional | 60.0 |
| `contactId` | String | ID of the contact in a user context. | Optional | 60.0 |
| `contextId` | String | ID of the context that represents the created session. | Optional | 60.0 |

=== ARTICLE: connect_requests_delete_nodes_configurator_input.htm ===
---
page_id: connect_requests_delete_nodes_configurator_input.htm
title: Configurator Delete Nodes Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_delete_nodes_configurator_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Delete Nodes Input

Input representation of the request to delete nodes from a product
        configuration.

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "deletedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"]
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `deleted​Nodes` | [Configurator Deleted Node Input](./connect_requests_configurator_deleted_node_input.htm.md)[] | List of the nodes to be deleted. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |

=== ARTICLE: connect_requests_favorite_input.htm ===
---
page_id: connect_requests_favorite_input.htm
title: Configuration Save Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_favorite_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Save Input

Input representation of the details to save a configuration.

**JSON example**

: 

```
{
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | JSON object that contains the details of the sales transaction, formatted as a string. | Optional | 63.0 |
| `description` | String | Description of the saved configuration. | Optional | 63.0 |
| `name` | String | Name of the saved configuration. | Optional | 63.0 |
| `referenceRecord​Id` | String | ID of the record for which the configuration must be saved. | Required | 63.0 |

=== ARTICLE: connect_requests_get_configuration_instance_input.htm ===
---
page_id: connect_requests_get_configuration_instance_input.htm
title: Configuration Get Instance Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_get_configuration_instance_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Get Instance Input

Input representation of the request to get a product configuration instance.

**JSON example**

: 

```

{
"contextId": "008d27d7-e004-4906-a949-ee7d7c323c77"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | Transaction context ID of the product configuration instance that’s to be fetched. | Required | 60.0 |

=== ARTICLE: connect_requests_load_configuration_instance_input.htm ===
---
page_id: connect_requests_load_configuration_instance_input.htm
title: Configuration Load Instance Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_load_configuration_instance_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Load Instance Input

Input representation of the request to load a product configuration
            instance.

**JSON example**

: 

```

{
    "configuratorOptions": 
      {
        "addDefaultConfiguration": true,
        "executeConfigurationRules": true,
        "executePricing": true,
        "qualifyAllProductsInTransaction": true,
        "validateAmendRenewCancel": true,
        "validateProductCatalog": true
    },
    "qualificationContext": {
        "accountId": "001DU000001nHUGYA2"
    },
    "transactionId": "0Q0DU0000000XoN0AU"
}
```

**Properties**

: 

                                        

                                        

                                        

                                        

                                        

                                    

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configurator options to execute. | Optional | 60.0 |
| `context​Mapping​Id` | String | ID of the context mapping record. | Optional | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `transaction​Id` | String | Transaction ID of the header entity that’s used to create a session. For example, a Quote or an Order. | Required | 60.0 |

=== ARTICLE: connect_requests_save_configuration_instance_input.htm ===
---
page_id: connect_requests_save_configuration_instance_input.htm
title: Configuration Save Instance Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_save_configuration_instance_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Save Instance Input

Input representation of the request to save a product configuration instance.

**JSON example**

: 

```

{
"contextId": "008d27d7-e004-4906-a949-ee7d7c323c77"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | Transaction context ID of the product configuration instance that’s to be saved. | Required | 60.0 |

=== ARTICLE: connect_requests_set_configuration_instance_input.htm ===
---
page_id: connect_requests_set_configuration_instance_input.htm
title: Configuration Set Instance Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_set_configuration_instance_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Set Instance Input

Input representation of the request to set a product configuration instance.

**JSON example**

          
: 
            

```
{
  "configuratorOptions": {
    "addDefaultConfiguration": true,
    "executeConfigurationRules": true,
    "executePricing": false,
    "qualifyAllProductsInTransaction": false,
    "validateAmendRenewCancel": false,
    "validateProductCatalog": false
  },
  "contextMappingId": "11jEk000017YdyUIAS",
  "qualificationContext": {
    "accountId": "001DU000001nHUGYA2"
  },
  "transaction": "{\"Quote\":[{\"QuoteLineItem\":[{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_1\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_2\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_3\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_4\"}],\"businessObjectType\":\"Quote\",\"id\":\"aJSdm0000003m3JGAQ\"}]}"
}
```

          

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configurator options to execute. | Optional | 60.0 |
| `context​MappingId` | String | ID of the context mapping record. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `transaction` | String | Transaction JSON payload representing an object in an external system that’s used to create a session. | Required | 60.0 |

=== ARTICLE: connect_requests_set_product_quantity_configurator_input.htm ===
---
page_id: connect_requests_set_product_quantity_configurator_input.htm
title: Product Quantity Set Configurator Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_set_product_quantity_configurator_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Quantity Set Configurator Input

Input representation of the request to set the quantity of a product.

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "quantity": 20,
    "transactionLinePath": "Quote.QuoteLineItem.Quantity"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `quantity` | Integer | Value of the product quantity. | Required | 60.0 |
| `transaction​Line​Path` | String[] | Path to the line item where the update to the quantity is applied. For example, Quote.QuoteLineItem.Quantity. | Required | 60.0 |

=== ARTICLE: connect_requests_update_favorite_input.htm ===
---
page_id: connect_requests_update_favorite_input.htm
title: Configuration Update Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_update_favorite_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Update Input

Input representation of the details to update a configuration.

**JSON example**

: 

```
{
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | JSON object that contains the details of the sales transaction, formatted as a string. | Required | 63.0 |
| `description` | String | Description of the configuration. | Required | 63.0 |
| `name` | String | Name of the configuration. | Required | 63.0 |

=== ARTICLE: connect_requests_update_nodes_configurator_input.htm ===
---
page_id: connect_requests_update_nodes_configurator_input.htm
title: Configurator Update Nodes Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_update_nodes_configurator_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Update Nodes Input

Input representation of the request to update the nodes in a product
        configuration.

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "updatedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"],
            "updatedAttributes": {
                "Quantity": 5
            }
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `updated​Nodes` | [Configurator Updated Node Input](./connect_requests_configurator_updated_node_input.htm.md)[] | List of the nodes to be updated. | Required | 60.0 |

=== ARTICLE: connect_resources_add_nodes.htm ===
---
page_id: connect_resources_add_nodes.htm
title: Configurator Add Nodes (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_add_nodes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Add Nodes (POST)

Add a node to the context through the runtime system without using
      the Salesforce user interface.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/add-nodes
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/add-nodes
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "configuratorOptions": {
    "executePricing": true,
    "returnProductCatalogData": true,
    "qualifyAllProductsInTransaction": true,
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },
  "qualificationContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "addedNodes": [
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589"
      ],
      "addedObject": {
        "id": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemSource": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemParent": "0Q0xx0000004EvcCAE",
        "PricebookEntry": "01uxx00000090VuAAI",
        "ProductSellingModel": "0jPxx00000001KHEAY",
        "UnitPrice": 15.26,
        "Quantity": 1,
        "Product": "01txx0000006lfHAAQ",
        "businessObjectType": "QuoteLineItem"
      }
    },
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ref_d85b036d_d305_4bb6_aba8_a1dff645a664"
      ],
      "addedObject": {
        "id": "ref_d85b036d_d305_4bb6_aba8_a1dff645a664",
        "MainItem": "0QLxx0000004QdRGAU",
        "AssociatedItem": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ProductRelatedComponent": "0dSxx00000001p6EAA",
        "ProductRelationshipType": null,
        "AssociatedItemPricing": "NotIncludedInBundlePrice",
        "AssociatedQuantScaleMethod": "Proportional",
        "businessObjectType": "QuoteLineRelationship"
      }
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `added​Nodes` | [Configurator Added Node Input](./connect_requests_configurator_added_node_input.htm.md)[] | List of the nodes to be added. | Required | 60.0 |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configurator Add
              Nodes](./connect_responses_add_nodes_configurator_output.htm.md)

=== ARTICLE: connect_resources_config_rules.htm ===
---
page_id: connect_resources_config_rules.htm
title: Config Rules (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_config_rules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Config Rules (POST)

Run rules for a specific quote or order based on a context ID or
      transaction ID.

    
      
        
          

**Resource**

          
: 
            

```
/revenue/product-configurator/rules/actions/execute
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/revenue/product-configurator/rules/actions/execute
```

          

        
        
          

**Available version**

          
: 67.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "transactionContextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "transactionId": "0Q0DU0000005tJh0AI",
  "ruleOptions": {
    "isUpdateContextRequired": false
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `ruleOptions` | [Config Rule Options Input](./connect_requests_config_rule_options_input.htm.md)[] | Details of the options to run specific steps in rules. | Optional | 67.0 |
| `transactionContextId` | String | ID of the sales transaction context instance. | Required if the `transactionId` property isn’t specified. | 67.0 |
| `transactionId` | String | ID of the quote or order. | Required if the `transactionContextId` property isn’t specified. | 67.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Rule Response](./connect_responses_config_rule_output.htm.md)

=== ARTICLE: connect_resources_delete_nodes.htm ===
---
page_id: connect_resources_delete_nodes.htm
title: Configurator Delete Nodes (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_delete_nodes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Delete Nodes (POST)

Delete nodes from a product configuration.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/delete-nodes
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/delete-nodes
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "deletedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"]
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `deleted​Nodes` | [Configurator Deleted Node Input](./connect_requests_configurator_deleted_node_input.htm.md)[] | List of the nodes to be deleted. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configurator Delete
              Nodes](./connect_responses_delete_nodes_configurator_output.htm.md)

=== ARTICLE: connect_resources_get_configurator_instance.htm ===
---
page_id: connect_resources_get_configurator_instance.htm
title: Configuration Get Instance (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_configurator_instance.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Get Instance (POST)

Fetch the JSON representation of a product configuration. Use the
      response to display the details of the product configuration instance on the Salesforce user
      interface, or save the product configuration instance to an external system.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/get-instance
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/get-instance
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```

{
"contextId": "008d27d7-e004-4906-a949-ee7d7c323c77"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | Transaction context ID of the product configuration instance that’s to be fetched. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Get
              Instance](./connect_responses_get_configuration_instance_output.htm.md)

=== ARTICLE: connect_resources_load_configurator_instance.htm ===
---
page_id: connect_resources_load_configurator_instance.htm
title: Configuration Load Instance (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_load_configurator_instance.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Load Instance (POST)

Create a session for the product configuration instance using the
      transaction ID. Get the session ID that includes the results of actions, such as configuration
      rules, qualification rules, and pricing management.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/load-instance
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/load-instance
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```

{
    "configuratorOptions": 
      {
        "addDefaultConfiguration": true,
        "executeConfigurationRules": true,
        "executePricing": true,
        "qualifyAllProductsInTransaction": true,
        "validateAmendRenewCancel": true,
        "validateProductCatalog": true
    },
    "qualificationContext": {
        "accountId": "001DU000001nHUGYA2"
    },
    "transactionId": "0Q0DU0000000XoN0AU"
}
```

**Properties**

: 

                                        

                                        

                                        

                                        

                                        

                                    

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configurator options to execute. | Optional | 60.0 |
| `context​Mapping​Id` | String | ID of the context mapping record. | Optional | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `transaction​Id` | String | Transaction ID of the header entity that’s used to create a session. For example, a Quote or an Order. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Load
              Instance](./connect_responses_load_configuration_instance_output.htm.md)

=== ARTICLE: connect_resources_product_configurator_configure.htm ===
---
page_id: connect_resources_product_configurator_configure.htm
title: Configuration (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_configurator_configure.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration (POST)

Retrieve and update a product’s configuration from a configurator.
      Execute configuration rules and notify users of any violations for changes to product bundle,
      attributes, or product quantity within a bundle. Additionally, get pricing details for the
      configured bundle.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/configure
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/configure
```

            If you’re calling this API from an external website, include the site name in the
            resource.

```
https://yourInstance.salesforce.com/<siteName>/services/data/v68.0/connect/cpq/configurator/actions/configure
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

                    
: This example shows a sample to initiate a context based on a transaction
                        ID.

                    
: 
                        

```
{
    "transactionLineId": "0QLDE000000IBXw4AO",
    "transactionId": "0Q0xx0000000001GAA",
    "correlationId": "c95246d4-102c-4ecd-a263-f74ac525d1e5",
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    }
}
```

                    

          
: This example shows a sample to add, update, or delete a node in an existing
            context.

: 

```
{
    "transactionLineId": "0QLDE000000IBXw4AO",
    "transactionId": "0Q0DE000000ISHJs81",
    "correlationId": "c95246d4-102c-4ecd-a263-f74ac525d1e5",
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "contextResponseType": "Full",
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "transactionContextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "addedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "sti2_id"],
            "addedObject": {
                "id": "ref_sti2_id",
                "SalesTransactionSource": "sti2_id",
                "PricebookEntry": "01uxx0000000001AAA",
                "ProductSellingModel": "0jPxx0000000001AAA",
                "businessObjectType": "QuoteLineItem",
                "Quantity": 10,
                "UnitPrice": 2.0,
                "Product": "01txx0000000001AAA"
            }
        },
        {
            "path": ["0Q0DE000000ISHJs81", "ref_sti2_id","ref_stir1_id"],
            "addedObject": {
                "id": "ref_stir1_id",
                "businessObjectType": "QuoteLineItemRelationship",
                "MainItem": "0QLDE000000IBXw4AO",
                "AssociatedItem": "ref_sti2_id",
                "ProductRelatedComponent": "0dSxx0000000001AAA",
                "ProductRelationshipType": "0yoxx0000000001AAA",
                "AssociatedItemPricing": "IncludedInBundlePrice"
                
            }
        }
    ],
    "updatedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"],
            "updatedAttributes": {
                "Quantity": 5
            }
        }
    ],
    "deletedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"]
        }
    ]
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
| `added​Nodes` | [Configurator Added Node Input](./connect_requests_configurator_added_node_input.htm.md)[] | List of added context nodes that’s passed to the product configurator. | Optional | 60.0 |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md)[] | Options to pass to the configurator. | Optional | 60.0 |
| `context​ResponseType` | String | Specifies the type of transaction context response. Valid values are: `Delta`—Returns the sales transaction items that are added or updated. `Full`—Returns all sales transaction items in a transaction. `None`—Returns empty transaction context response. `Product`—Returns the sales transaction items related to the product that's being configured. | Required for large sales transactions with more than 1000 line items and less than 15K line items. | 65.0 |
| `correlation​Id` | String | ID that’s specified for traceability of logs. | Optional | 60.0 |
| `deleted​Nodes` | [Configurator Deleted Node Input](./connect_requests_configurator_deleted_node_input.htm.md)[] | List of deleted context nodes that’s passed to the product configurator. | Optional | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md)[] | Details such as account ID, contact ID, and context ID that are used for executing qualification rules. | Optional | 60.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 60.0 |
| `transaction​Id` | String | ID of the sales transaction that’s being configured such as a quote or an order. | Required | 60.0 |
| `transaction​LineId` | String | ID of the top-level line item that’s being configured. | Optional | 60.0 |
| `updated​Nodes` | [Configurator Updated Node Input](./connect_requests_configurator_updated_node_input.htm.md)[] | List of updated context nodes that’s passed to the product configurator. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration
              Details](./connect_responses_configurator_output.htm.md)

=== ARTICLE: connect_resources_save_configuration_instance.htm ===
---
page_id: connect_resources_save_configuration_instance.htm
title: Configuration Save Instance (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_save_configuration_instance.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Save Instance (POST)

Save a configuration instance after a successful product
      configuration.

    

Use the Configuration Save Instance API to save the changes to the source after a
        successful configuration. For example, save changes to the quote line item of a product,
        which is the source used to load the configuration.

        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/save-instance
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/save-instance
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```

{
"contextId": "008d27d7-e004-4906-a949-ee7d7c323c77"
}
```

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | Transaction context ID of the product configuration instance that’s to be saved. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Save
              Instance](./connect_responses_save_configuration_instance_output.htm.md)

=== ARTICLE: connect_resources_save_product_configurations.htm ===
---
page_id: connect_resources_save_product_configurations.htm
title: Saved Configuration (GET, POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_save_product_configurations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Saved Configuration (GET, POST)

Save and reuse a record's configurations, and get a list of the saved configurations
    for a record.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/saved-configuration
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/saved-configuration
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET, POST

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceRecordId` | String | ID of the record whose saved configurations must be retrieved. | Required | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Configuration
              List](./connect_responses_favorite_list_output_represenation.htm.md)

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | JSON object that contains the details of the sales transaction, formatted as a string. | Optional | 63.0 |
| `description` | String | Description of the saved configuration. | Optional | 63.0 |
| `name` | String | Name of the saved configuration. | Optional | 63.0 |
| `referenceRecord​Id` | String | ID of the record for which the configuration must be saved. | Required | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Record
            Save](./connect_responses_create_favorite_output.htm.md)

        
      

    

  

#### See Also

- [*Salesforce Help*: Considerations to Save and Reuse Configurations](https://help.salesforce.com/s/articleView?id=ind.product_configurator_considerations_to_save_and_reuse_configurations.htm&language=en_US)

=== ARTICLE: connect_resources_saved_configuration.htm ===
---
page_id: connect_resources_saved_configuration.htm
title: Saved Configuration (DELETE, PUT)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_saved_configuration.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Saved Configuration (DELETE, PUT)

Update or delete a record's saved configuration by using the configuration
    ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/saved-configuration/id
```

          

          
: The id parameter is the ID of the configuration that you want to
            update or delete.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/saved-configuration/5KPxx0025063GSmSAX
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: DELETE, PUT

        
        
          

**Request body for PUT**

          
: 
            

**JSON example**

: 

```
{
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | JSON object that contains the details of the sales transaction, formatted as a string. | Required | 63.0 |
| `description` | String | Description of the configuration. | Required | 63.0 |
| `name` | String | Name of the configuration. | Required | 63.0 |

          

        
        
          

**Response body for PUT**

          
: [Configuration
              Update](./connect_responses_update_favorite_output.htm.md)

        
      

    

  

#### See Also

- [*Salesforce Help*: Considerations to Save and Reuse Configurations](https://help.salesforce.com/s/articleView?id=ind.product_configurator_considerations_to_save_and_reuse_configurations.htm&language=en_US)

=== ARTICLE: connect_resources_set_configurator_instance.htm ===
---
page_id: connect_resources_set_configurator_instance.htm
title: Configuration Set Instance (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_set_configurator_instance.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Set Instance (POST)

Set a product configuration instance. This API is used in scenarios
      where the configuration instance is available in a different database than Salesforce and the
      product catalog management data is in Salesforce.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/set-instance
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/set-instance
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: 
            

```
{
  "configuratorOptions": {
    "addDefaultConfiguration": true,
    "executeConfigurationRules": true,
    "executePricing": false,
    "qualifyAllProductsInTransaction": false,
    "validateAmendRenewCancel": false,
    "validateProductCatalog": false
  },
  "contextMappingId": "11jEk000017YdyUIAS",
  "qualificationContext": {
    "accountId": "001DU000001nHUGYA2"
  },
  "transaction": "{\"Quote\":[{\"QuoteLineItem\":[{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_1\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_2\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_3\"},{\"businessObjectType\":\"QuoteLineItem\",\"id\":\"qli_4\"}],\"businessObjectType\":\"Quote\",\"id\":\"aJSdm0000003m3JGAQ\"}]}"
}
```

          

**Properties**

: 

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configurator options to execute. | Optional | 60.0 |
| `context​MappingId` | String | ID of the context mapping record. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `transaction` | String | Transaction JSON payload representing an object in an external system that’s used to create a session. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configuration Set
              Instance](./connect_responses_set_configuration_instance_output.htm.md)

=== ARTICLE: connect_resources_set_product_quantity.htm ===
---
page_id: connect_resources_set_product_quantity.htm
title: Product Set Quantity (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_set_product_quantity.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Set Quantity (POST)

Set the quantity of a product through the runtime
    system.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/set-product-quantity
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/set-product-quantity
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "quantity": 20,
    "transactionLinePath": "Quote.QuoteLineItem.Quantity"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `quantity` | Integer | Value of the product quantity. | Required | 60.0 |
| `transaction​Line​Path` | String[] | Path to the line item where the update to the quantity is applied. For example, Quote.QuoteLineItem.Quantity. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Product Quantity Set
              Configurator](./connect_responses_set_product_quantity_configurator_output.htm.md)

=== ARTICLE: connect_resources_update_nodes.htm ===
---
page_id: connect_resources_update_nodes.htm
title: Configurator Update Nodes (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_update_nodes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Update Nodes (POST)

Update nodes in a product configuration.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/configurator/actions/update-nodes
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/configurator/actions/update-nodes
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
    "configuratorOptions": {
        "executePricing": true,
        "returnProductCatalogData": true,
        "qualifyAllProductsInTransaction": true,
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
    },
    "qualificationContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    },
    "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
    "updatedNodes": [
        {
            "path": ["0Q0DE000000ISHJs81", "0QLDE000000IBXw4AO"],
            "updatedAttributes": {
                "Quantity": 5
            }
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Options` | [Configurator Options Input](./connect_requests_configurator_options_input.htm.md) | List of the configuration options to execute. | Optional | 60.0 |
| `context​Id` | String | ID of the context object that’s being considered. | Required | 60.0 |
| `qualification​Context` | [User Context Input](./connect_requests_configurator_user_context_input.htm.md) | Context details that are used for the qualification rules. | Optional | 60.0 |
| `updated​Nodes` | [Configurator Updated Node Input](./connect_requests_configurator_updated_node_input.htm.md)[] | List of the nodes to be updated. | Required | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Configurator Update
              Nodes](./connect_responses_update_nodes_configurator_output.htm.md)

=== ARTICLE: connect_responses_add_nodes_configurator_output.htm ===
---
page_id: connect_responses_add_nodes_configurator_output.htm
title: Configurator Add Nodes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_add_nodes_configurator_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Add Nodes

Output representation of the configuration request details to add nodes.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, [Configurator Message](./connect_responses_configurator_message_output.htm.md)> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engines (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the qualification rule execution results. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_config_rule_errors_output.htm ===
---
page_id: connect_responses_config_rule_errors_output.htm
title: Configuration Rule Errors
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_config_rule_errors_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: connect_responses_config_rule_output.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Rule Errors

Output representation of the error details, if applicable, when you run config
    rules.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code indicating the type of error. | Small, 67.0 | 67.0 |
| `message` | String | Message stating the reason for error, if any. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_config_rule_output.htm ===
---
page_id: connect_responses_config_rule_output.htm
title: Configuration Rule Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_config_rule_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Rule Response

Output representation of the details of the configuration rule response.

        
          

**JSON example**

          
: 
            

```
{
  "errors": [],
  "messageRules": [
    {
      "message": "You have a 128GB LRDIMM QLI",
      "messageType": "error",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "You have a 16GB RDIMM QLI",
      "messageType": "warning",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "You have a 32GB RDIMM QLI",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "128GB LRDIMM disables 16GB RDIMM",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "Additional API disables Additional API Gov",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "Disable All other API Products",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "32GB RDIMM disables 128GB LRDIMM",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "API Access Requests AEH disables Additional API Prod",
      "messageType": "info",
      "primaryRecordId": "0Q0VW000000z8yN0AQ"
    }
  ],
  "productRecommendationRules": [
    {
      "message": "32GB RDIMM recommends 16GB RDIMM",
      "productIds": [
        "01tVW000003l7uaYAA"
      ],
      "recordType": "Type",
      "referenceId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "32GB RDIMM recommends 64GB RDIMM",
      "productIds": [
        "01tVW000003l7v6YAA"
      ],
      "recordType": "Type",
      "referenceId": "0Q0VW000000z8yN0AQ"
    }
  ],
  "success": true,
  "transactionContextId": "0000000r25tq18g00291775730228818e689c3c5756e409fb3f886f68937ab13",
  "visibilityRules": [
    {
      "message": "128GB LRDIMM disables 16GB RDIMM",
      "productIds": [
        "01tVW000003l7uaYAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "Additional API disables Additional API Gov",
      "productIds": [
        "01tVW000003l7tzYAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "Disable All other API Products",
      "productIds": [
        "01tVW000003l7u0YAA",
        "01tVW000003l7u1YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "32GB RDIMM disables 128GB LRDIMM",
      "productIds": [
        "01tVW000003l7v5YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "API Access Requests AEH disables Additional API Prod",
      "productIds": [
        "01tVW000003l7u1YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Config Rule Errors](./connect_responses_config_rule_errors_output.htm.md)[] | List of error messages from the configuration rule evaluation, if any. | Small, 67.0 | 67.0 |
| `message​Rules` | [Message Rules](./connect_responses_message_rules_output.htm.md)[] | List of message rules that were evaluated during configuration. | Small, 67.0 | 67.0 |
| `product​Recommendation​Rules` | [Product Recommendation Rules](./connect_responses_product_recommendation_rules_output.htm.md)[] | List of product recommendation rules that were evaluated during configuration. | Small, 67.0 | 67.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `transaction​ContextId` | String | ID of the transaction context for this configuration rule evaluation. | Small, 67.0 | 67.0 |
| `visibility​Rules` | [Visibility Rules](./connect_responses_visibility_rules_output.htm.md)[] | List of visibility rules that were evaluated during configuration. | Small, 67.0 | 67.0 |

- 
**[Configuration Rule Errors](./connect_responses_config_rule_errors_output.htm.md)**  

Output representation of the error details, if applicable, when you run config     rules.

- 
**[Message Rules](./connect_responses_message_rules_output.htm.md)**  

Output representation of the details of the message rules.

- 
**[Product Recommendation Rules](./connect_responses_product_recommendation_rules_output.htm.md)**  

Output representation of the details of the product recommendation rules.

- 
**[Visibility Rules](./connect_responses_visibility_rules_output.htm.md)**  

Output representation of the details of the visibility rules.

=== ARTICLE: connect_responses_configuration_list_error_response.htm ===
---
page_id: connect_responses_configuration_list_error_response.htm
title: Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configuration_list_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Response

Output representation of the details of the error.

    

        
          

**JSON example**

          
: 
            

```
{
  "errors": [
    {
      "code": "BAD_REQUEST",
      "message": "MISSING_REFERENCEOBJECTID"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code of the error. | Small, 63.0 | 63.0 |
| `message` | String | Description of the error. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_configurator_additional_fields_output.htm ===
---
page_id: connect_responses_configurator_additional_fields_output.htm
title: Configurator Additional Fields
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_additional_fields_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Additional Fields

Output representation of the additional fields of a product configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `field​ApiName` | String | API name of the field. | Small, 60.0 | 60.0 |
| `fieldName` | String | Name of the field. | Small, 60.0 | 60.0 |
| `value` | String | Value of the field. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_attribute_category_output.htm ===
---
page_id: connect_responses_configurator_attribute_category_output.htm
title: Configurator Attribute Category
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_attribute_category_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Attribute Category

Output representation of the attribute category in a product configuration.

        
          

**JSON example**

          
: 
            

```

    "attributeCategories": [
      {
        "attributes": [
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Load Capacity",
            "code": "CAP",
            "dataType": "NUMBER",
            "defaultValue": "1500",
            "description": "Server racks are designed to support a specific load capacity, commonly measured in kilograms (kg) or pounds (lbs). Typical load capacities range from 500 kg (1102 lbs) to 1500 kg (3307 lbs) depending on the model.",
            "id": "0tjxx00000001DpAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": false,
            "label": "Load Capacity",
            "name": "Load Capacity"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Expansion Slots",
            "code": "SLOTCAP",
            "dataType": "NUMBER",
            "defaultValue": "12",
            "id": "0tjxx00000001H3AAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Expansion Slots",
            "name": "Expansion Slots"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Memory",
            "attributePicklist": {
              "id": "0v5xx0000000001AAA",
              "values": [
                {
                  "code": "MEM",
                  "displayValue": "25",
                  "id": "0v6xx0000000001AAA",
                  "isBooleanValue": false,
                  "name": "25Mem",
                  "sequence": 0,
                  "textValue": "25"
                },
                {
                  "code": "50MEM",
                  "displayValue": "50",
                  "id": "0v6xx000000001eAAA",
                  "isBooleanValue": false,
                  "name": "50Mem",
                  "sequence": 1,
                  "textValue": "50"
                },
                {
                  "code": "100MEM",
                  "displayValue": "100",
                  "id": "0v6xx000000003FAAQ",
                  "isBooleanValue": false,
                  "name": "100Mem",
                  "sequence": 2,
                  "textValue": "100"
                }
              ]
            },
            "dataType": "MULTIPICKLIST",
            "defaultValue": "25",
            "id": "0tjxx00000001IfAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Memory",
            "name": "Memory"
          }
        ],
        "code": "SPEC",
        "name": "Server Rack Specifications"
      }
    ],
    "description": "Introducing the Cisco Server Rack, a sleek and robust solution designed to streamline your data center infrastructure. With its scalable design and advanced cable management features, it ensures optimal performance, efficiency, and easy maintenance for your critical network equipment.",
    "displayUrl": "https://www.cisco.com/content/dam/en/us/products/servers-unified-computing/ucs-c240-m4-rack-server/product-large.jpg",
    "id": "01txx0000006jkuAAA",
    "isActive": true,
    "isAssetizable": true,
    "isConfigurable": true,
    "isSoldOnlyWithOtherProds": false,
    "name": "Cisco Server Rack NX44",
    "nodeType": "bundleProduct",
    "prices": [],
    "productClassification": {
      "id": "11Bxx000002CC02EAG"
    },
    "productCode": "RACK",
    "productComponentGroups": [
      {
        "classifications": [],
        "code": "SERVICE",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Service, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jmWAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": false,
            "isQuantityEditable": false,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Service - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "SERVICE",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jmWAAQ",
              "childSellingModelId": "0jPxx000000004rEAA",
              "doesBundlePriceIncludeChild": true,
              "id": "0dSxx000000001dEAA",
              "isComponentRequired": false,
              "isDefaultComponent": false,
              "isQuantityEditable": false,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000004rEAA",
              "productComponentGroupId": "0y7xx000000001dAAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional"
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000009hEAA",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000PpEAI",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              }
            ]
          }
        ],
        "description": "The services available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx000000001dAAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Services",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 1
      },
      {
        "classifications": [],
        "code": "WARRANTY",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Warranty, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jjIAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": true,
            "isQuantityEditable": true,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Warranty - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "WARRANTY",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jjIAAQ",
              "childSellingModelId": "0jPxx000000001dEAA",
              "doesBundlePriceIncludeChild": false,
              "id": "0dSxx0000000001EAA",
              "isComponentRequired": false,
              "isDefaultComponent": true,
              "isQuantityEditable": true,
              "maxQuantity": 1,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000001dEAA",
              "productComponentGroupId": "0y7xx0000000001AAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional",
              "sequence": 0
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000001dEAA",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000001dEAA",
                  "name": "One Time",
                  "sellingModelType": "OneTime",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000001dEAA"
              },
              {
                "id": "0iOxx00000000HlEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000003FEAQ",
                  "name": "Termed Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000003FEAQ"
              },
              {
                "id": "0iOxx00000000JNEAY",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000KzEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              },
              {
                "id": "0iOxx00000000MbEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000006TEAQ",
                  "name": "Evergreen Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000006TEAQ"
              }
            ]
          }
        ],
        "description": "The warranties available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx0000000001AAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Warranties",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 0
      }
    ],
    "productSellingModelOptions": [
      {
        "id": "0iOxx000000003FEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000001dEAA",
          "name": "One Time",
          "sellingModelType": "OneTime",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000001dEAA"
      },
      {
        "id": "0iOxx000000004rEAA",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000003FEAQ",
          "name": "Termed Monthly",
          "pricingTerm": 1,
          "pricingTermUnit": "Months",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000003FEAQ"
      },
      {
        "id": "0iOxx000000006TEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000004rEAA",
          "name": "Termed Annually",
          "pricingTerm": 1,
          "pricingTermUnit": "Annual",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000004rEAA"
      }
    ],
    "productType": "Bundle"
  },
  "errors": [],
  "success": true,
  "transactionContext": {
    "SalesTransaction": [
      {
        "Status": "Draft",
        "Account": "001xx000003GeIxAAK",
        "BillingCity": "San Francisco",
        "Subtotal": 152500,
        "LastPricedDate": "2023-08-22T05:55:39Z",
        "businessObjectType": "Quote",
        "TotalAmount": 152500,
        "ShippingStreet": "415 Mission St",
        "SalesTransactionItem": [
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jkuAAA",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 150000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQmGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 150000,
            "TotalLineAmount": 150000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 150000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQmGAM",
            "PriceWaterFall": "{
                "currencyCode":"USD",
                "executionEndTimestamp":"2023-09-18T20:11:15.016Z",
                "executionId":"ruepwmHn2ZFvnQo5bjot",
                "executionStartTimestamp":"2023-09-18T20:11:14.906Z",
                "lineItemId":"0QLxx0000004CQmGAM",
                "output":{
                    "NetUnitPrice":150000.0,
                    "Subtotal":0.0
                 },
                "success":true,
                "waterfall":[
                {
                "fieldToTagNameMapping":{
                "NetUnitPrice":"ItemUnitPrice",
                "AdjustmentValue":"ItemAdjustmentValue",
                "Subtotal":"ItemTotalAdjustmentAmount",
                "Quantity":"ItemQuantity",
                "LineItemId":"SalesTransactionItemSource",
                "InputUnitPrice":"ItemUnitPrice"
                },
                "inputParameters":{
                    "Quantity":1.0,
                    "LineItemId":"0QLxx0000004CQmGAM",
                    "InputUnitPrice":150000.0,
                    "AdjustmentType":"Amount"
                },
                "outputParameters":{
                    "NetUnitPrice":150000.0,
                    "Subtotal":0.0
                },
            "pricingElement":{
                "adjustments":[
                  {
                    "AdjustmentType":"Amount"
                  }
              ],
            "elementType":"MANUALDISCOUNT",
            "name":"ManualDiscount"
            },
            "sequence":1
            }
            ]
            }",
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 150000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "SalesTransactionItemAttribute": [
              {
                "AttributeKey": "0tjxx00000001H3AAI",
                "AttributeValue": "30.0",
                "AttributePicklistValue": null,
                "IsPriceImpacting": true,
                "businessObjectType": "QuoteLineItemAttribute",
                "AttributeName": "Expansion Slots",
                "AttributeDefinitionCode": "SLOTCAP",
                "id": "0zuxx0000000001AAA",
                "SalesTransactionItemAttrParent": "0QLxx0000004CQmGAM"
              }
            ],
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx0000009154AAA",
            "PricingTermCount": 1,
            "NetUnitPrice": 150000,
            "UnitPrice": 150000,
            "StartingUnitPrice": 150000,
            "SalesTrxnItemRelationship": [
              {
                "ProductRelationshipType": "0yoxx00000001IfAAI",
                "MainItemRole": "Bundle",
                "AssociatedItem": "0QLxx0000004CQnGAM",
                "ProductRelatedComponent": "0dSxx0000000001EAA",
                "MainItem": "0QLxx0000004CQmGAM",
                "AssociatedQuantScaleMethod": "Proportional",
                "businessObjectType": "QuoteLineRelationship",
                "AssociatedItemRole": "BundleComponent",
                "SalesTrnItemRelationshipParent": "0Q0xx0000004CAeCAM",
                "id": "0yQxx000000001dEAA",
                "AssociatedItemPricing": "NotIncludedInBundlePrice"
              }
            ],
            "TotalPrice": 150000,
            "PeriodBoundaryDay": null
          },
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jjIAAQ",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 2000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQnGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 2000,
            "TotalLineAmount": 2000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 2000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQnGAM",
            "PriceWaterFall": "{
                "currencyCode":"USD",
                "executionEndTimestamp":"023-09-18T20:11:15.016Z",
                "executionId":"ruepwmHn2ZFvnQo5bjot",
                "executionStartTimestamp":"2023-09-18T20:11:14.906Z",
                "lineItemId":"0QLxx0000004CQnGAM",
                "output":{
                    "NetUnitPrice":2000.0,
                    "Subtotal":0.0
                 },
                "success":true,
                "waterfall":[
                {
                "fieldToTagNameMapping":{
                "NetUnitPrice":"ItemUnitPrice",
                "AdjustmentValue":"ItemAdjustmentValue",
                "Subtotal":"ItemTotalAdjustmentAmount",
                "Quantity":"ItemQuantity",
                "LineItemId":"SalesTransactionItemSource",
                "InputUnitPrice":"ItemUnitPrice"
                },
                "inputParameters":{
                    "Quantity":1.0,
                    "LineItemId":"0QLxx0000004CQnGAM",
                    "InputUnitPrice":2000.0,
                    "AdjustmentType":"Amount"
                },
                "outputParameters":{
                    "NetUnitPrice":2000.0,
                    "Subtotal":0.0
                },
            "pricingElement":{
                "adjustments":[
                  {}
              ],
            "elementType":"MANUALDISCOUNT",
            "name":"ManualDiscount"
            },
            "sequence":1
            }
            ]
            }",
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 2000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx000000913SAAQ",
            "PricingTermCount": 1,
            "NetUnitPrice": 2000,
            "UnitPrice": 2000,
            "StartingUnitPrice": 2000,
            "TotalPrice": 2000,
            "PeriodBoundaryDay": null
          }
        ],
        "BillingCountry": "US",
        "BillingStreet": "415 Mission St",
        "Pricebook": "01sxx0000005uDZAAY",
        "ShippingPostalCode": "94105",
        "SalesTransactionSource": "0Q0xx0000004CAeCAM",
        "ShippingCountry": "US",
        "ShippingCity": "San Francisco",
        "ShippingState": "CA",
        "BillingPostalCode": "94105",
        "id": "0Q0xx0000004CAeCAM",
        "BillToContact": null,
        "Contract": null,
        "BillingState": "CA"
      }
    ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Configurator Attribute](./connect_responses_configurator_attribute_output.htm.md)[] | Attributes of the attribute category. | Small, 60.0 | 60.0 |
| `code` | String | Code of the attribute category. | Small, 60.0 | 60.0 |
| `description` | String | Description of the attribute category. | Small, 60.0 | 60.0 |
| `id` | String | ID of the attribute category. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute category. | Small, 60.0 | 60.0 |
| `status` | String | Status of the attribute category. | Small, 60.0 | 60.0 |
| `totalSize` | Integer | Total size of the attribute category. | Small, 60.0 | 60.0 |
| `usageType` | String | Usage type of the attribute category. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_attribute_output.htm ===
---
page_id: connect_responses_configurator_attribute_output.htm
title: Configurator Attribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_attribute_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Attribute

Output representation of the attribute in a product configuration.

        
          

**JSON example**

          
: 
            

```

    "attributeCategories": [
      {
        "attributes": [
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Load Capacity",
            "code": "CAP",
            "dataType": "NUMBER",
            "defaultValue": "1500",
            "description": "Server racks are designed to support a specific load capacity, commonly measured in kilograms (kg) or pounds (lbs). Typical load capacities range from 500 kg (1102 lbs) to 1500 kg (3307 lbs) depending on the model.",
            "id": "0tjxx00000001DpAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": false,
            "label": "Load Capacity",
            "name": "Load Capacity"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Expansion Slots",
            "code": "SLOTCAP",
            "dataType": "NUMBER",
            "defaultValue": "12",
            "id": "0tjxx00000001H3AAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Expansion Slots",
            "name": "Expansion Slots"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Memory",
            "attributePicklist": {
              "id": "0v5xx0000000001AAA",
              "values": [
                {
                  "code": "MEM",
                  "displayValue": "25",
                  "id": "0v6xx0000000001AAA",
                  "isBooleanValue": false,
                  "name": "25Mem",
                  "sequence": 0,
                  "textValue": "25"
                },
                {
                  "code": "50MEM",
                  "displayValue": "50",
                  "id": "0v6xx000000001eAAA",
                  "isBooleanValue": false,
                  "name": "50Mem",
                  "sequence": 1,
                  "textValue": "50"
                },
                {
                  "code": "100MEM",
                  "displayValue": "100",
                  "id": "0v6xx000000003FAAQ",
                  "isBooleanValue": false,
                  "name": "100Mem",
                  "sequence": 2,
                  "textValue": "100"
                }
              ]
            },
            "dataType": "MULTIPICKLIST",
            "defaultValue": "25",
            "id": "0tjxx00000001IfAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Memory",
            "name": "Memory"
          }
        ],
        "code": "SPEC",
        "name": "Server Rack Specifications"
      }
    ],
    "description": "Introducing the Cisco Server Rack, a sleek and robust solution designed to streamline your data center infrastructure. With its scalable design and advanced cable management features, it ensures optimal performance, efficiency, and easy maintenance for your critical network equipment.",
    "displayUrl": "https://www.cisco.com/content/dam/en/us/products/servers-unified-computing/ucs-c240-m4-rack-server/product-large.jpg",
    "id": "01txx0000006jkuAAA",
    "isActive": true,
    "isAssetizable": true,
    "isConfigurable": true,
    "isSoldOnlyWithOtherProds": false,
    "name": "Cisco Server Rack NX44",
    "nodeType": "bundleProduct",
    "prices": [],
    "productClassification": {
      "id": "11Bxx000002CC02EAG"
    },
    "productCode": "RACK",
    "productComponentGroups": [
      {
        "classifications": [],
        "code": "SERVICE",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Service, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jmWAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": false,
            "isQuantityEditable": false,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Service - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "SERVICE",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jmWAAQ",
              "childSellingModelId": "0jPxx000000004rEAA",
              "doesBundlePriceIncludeChild": true,
              "id": "0dSxx000000001dEAA",
              "isComponentRequired": false,
              "isDefaultComponent": false,
              "isQuantityEditable": false,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000004rEAA",
              "productComponentGroupId": "0y7xx000000001dAAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional"
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000009hEAA",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000PpEAI",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              }
            ]
          }
        ],
        "description": "The services available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx000000001dAAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Services",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 1
      },
      {
        "classifications": [],
        "code": "WARRANTY",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Warranty, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jjIAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": true,
            "isQuantityEditable": true,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Warranty - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "WARRANTY",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jjIAAQ",
              "childSellingModelId": "0jPxx000000001dEAA",
              "doesBundlePriceIncludeChild": false,
              "id": "0dSxx0000000001EAA",
              "isComponentRequired": false,
              "isDefaultComponent": true,
              "isQuantityEditable": true,
              "maxQuantity": 1,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000001dEAA",
              "productComponentGroupId": "0y7xx0000000001AAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional",
              "sequence": 0
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000001dEAA",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000001dEAA",
                  "name": "One Time",
                  "sellingModelType": "OneTime",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000001dEAA"
              },
              {
                "id": "0iOxx00000000HlEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000003FEAQ",
                  "name": "Termed Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000003FEAQ"
              },
              {
                "id": "0iOxx00000000JNEAY",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000KzEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              },
              {
                "id": "0iOxx00000000MbEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000006TEAQ",
                  "name": "Evergreen Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000006TEAQ"
              }
            ]
          }
        ],
        "description": "The warranties available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx0000000001AAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Warranties",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 0
      }
    ],
    "productSellingModelOptions": [
      {
        "id": "0iOxx000000003FEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000001dEAA",
          "name": "One Time",
          "sellingModelType": "OneTime",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000001dEAA"
      },
      {
        "id": "0iOxx000000004rEAA",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000003FEAQ",
          "name": "Termed Monthly",
          "pricingTerm": 1,
          "pricingTermUnit": "Months",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000003FEAQ"
      },
      {
        "id": "0iOxx000000006TEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000004rEAA",
          "name": "Termed Annually",
          "pricingTerm": 1,
          "pricingTermUnit": "Annual",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000004rEAA"
      }
    ],
    "productType": "Bundle"
  },
  "errors": [],
  "success": true,
  "transactionContext": {
    "SalesTransaction": [
      {
        "Status": "Draft",
        "Account": "001xx000003GeIxAAK",
        "BillingCity": "San Francisco",
        "Subtotal": 152500,
        "LastPricedDate": "2023-08-22T05:55:39Z",
        "businessObjectType": "Quote",
        "TotalAmount": 152500,
        "ShippingStreet": "415 Mission St",
        "SalesTransactionItem": [
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jkuAAA",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 150000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQmGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 150000,
            "TotalLineAmount": 150000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 150000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQmGAM",
            "PriceWaterFall": "{
                "currencyCode":"USD",
                "executionEndTimestamp":"2023-09-18T20:11:15.016Z",
                "executionId":"ruepwmHn2ZFvnQo5bjot",
                "executionStartTimestamp":"2023-09-18T20:11:14.906Z",
                "lineItemId":"0QLxx0000004CQmGAM",
                "output":{
                    "NetUnitPrice":150000.0,
                    "Subtotal":0.0
                 },
                "success":true,
                "waterfall":[
                {
                "fieldToTagNameMapping":{
                "NetUnitPrice":"ItemUnitPrice",
                "AdjustmentValue":"ItemAdjustmentValue",
                "Subtotal":"ItemTotalAdjustmentAmount",
                "Quantity":"ItemQuantity",
                "LineItemId":"SalesTransactionItemSource",
                "InputUnitPrice":"ItemUnitPrice"
                },
                "inputParameters":{
                    "Quantity":1.0,
                    "LineItemId":"0QLxx0000004CQmGAM",
                    "InputUnitPrice":150000.0,
                    "AdjustmentType":"Amount"
                },
                "outputParameters":{
                    "NetUnitPrice":150000.0,
                    "Subtotal":0.0
                },
            "pricingElement":{
                "adjustments":[
                  {
                    "AdjustmentType":"Amount"
                  }
              ],
            "elementType":"MANUALDISCOUNT",
            "name":"ManualDiscount"
            },
            "sequence":1
            }
            ]
            }",
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 150000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "SalesTransactionItemAttribute": [
              {
                "AttributeKey": "0tjxx00000001H3AAI",
                "AttributeValue": "30.0",
                "AttributePicklistValue": null,
                "IsPriceImpacting": true,
                "businessObjectType": "QuoteLineItemAttribute",
                "AttributeName": "Expansion Slots",
                "AttributeDefinitionCode": "SLOTCAP",
                "id": "0zuxx0000000001AAA",
                "SalesTransactionItemAttrParent": "0QLxx0000004CQmGAM"
              }
            ],
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx0000009154AAA",
            "PricingTermCount": 1,
            "NetUnitPrice": 150000,
            "UnitPrice": 150000,
            "StartingUnitPrice": 150000,
            "SalesTrxnItemRelationship": [
              {
                "ProductRelationshipType": "0yoxx00000001IfAAI",
                "MainItemRole": "Bundle",
                "AssociatedItem": "0QLxx0000004CQnGAM",
                "ProductRelatedComponent": "0dSxx0000000001EAA",
                "MainItem": "0QLxx0000004CQmGAM",
                "AssociatedQuantScaleMethod": "Proportional",
                "businessObjectType": "QuoteLineRelationship",
                "AssociatedItemRole": "BundleComponent",
                "SalesTrnItemRelationshipParent": "0Q0xx0000004CAeCAM",
                "id": "0yQxx000000001dEAA",
                "AssociatedItemPricing": "NotIncludedInBundlePrice"
              }
            ],
            "TotalPrice": 150000,
            "PeriodBoundaryDay": null
          },
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jjIAAQ",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 2000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQnGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 2000,
            "TotalLineAmount": 2000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 2000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQnGAM",
            "PriceWaterFall": "{
                "currencyCode":"USD",
                "executionEndTimestamp":"023-09-18T20:11:15.016Z",
                "executionId":"ruepwmHn2ZFvnQo5bjot",
                "executionStartTimestamp":"2023-09-18T20:11:14.906Z",
                "lineItemId":"0QLxx0000004CQnGAM",
                "output":{
                    "NetUnitPrice":2000.0,
                    "Subtotal":0.0
                 },
                "success":true,
                "waterfall":[
                {
                "fieldToTagNameMapping":{
                "NetUnitPrice":"ItemUnitPrice",
                "AdjustmentValue":"ItemAdjustmentValue",
                "Subtotal":"ItemTotalAdjustmentAmount",
                "Quantity":"ItemQuantity",
                "LineItemId":"SalesTransactionItemSource",
                "InputUnitPrice":"ItemUnitPrice"
                },
                "inputParameters":{
                    "Quantity":1.0,
                    "LineItemId":"0QLxx0000004CQnGAM",
                    "InputUnitPrice":2000.0,
                    "AdjustmentType":"Amount"
                },
                "outputParameters":{
                    "NetUnitPrice":2000.0,
                    "Subtotal":0.0
                },
            "pricingElement":{
                "adjustments":[
                  {}
              ],
            "elementType":"MANUALDISCOUNT",
            "name":"ManualDiscount"
            },
            "sequence":1
            }
            ]
            }",
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 2000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx000000913SAAQ",
            "PricingTermCount": 1,
            "NetUnitPrice": 2000,
            "UnitPrice": 2000,
            "StartingUnitPrice": 2000,
            "TotalPrice": 2000,
            "PeriodBoundaryDay": null
          }
        ],
        "BillingCountry": "US",
        "BillingStreet": "415 Mission St",
        "Pricebook": "01sxx0000005uDZAAY",
        "ShippingPostalCode": "94105",
        "SalesTransactionSource": "0Q0xx0000004CAeCAM",
        "ShippingCountry": "US",
        "ShippingCity": "San Francisco",
        "ShippingState": "CA",
        "BillingPostalCode": "94105",
        "id": "0Q0xx0000004CAeCAM",
        "BillToContact": null,
        "Contract": null,
        "BillingState": "CA"
      }
    ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attribute​CategoryId` | String | ID of the attribute category. | Small, 60.0 | 60.0 |
| `attribute​NameOverride` | String | Name override value of the attribute. | Small, 60.0 | 60.0 |
| `attribute​Picklist` | [Configurator Attribute Picklist](./connect_responses_configurator_attribute_picklist_output.htm.md)[] | Picklist values of the attribute. | Small, 60.0 | 60.0 |
| `code` | String | Code of the attribute. | Small, 60.0 | 60.0 |
| `dataType` | String | Data type of the attribute. | Small, 60.0 | 60.0 |
| `default​HelpText` | String | Default help text value of the attribute. | Small, 60.0 | 60.0 |
| `default​Value` | String | Default value of the attribute. | Small, 60.0 | 60.0 |
| `description` | String | Description of the attribute. | Small, 60.0 | 60.0 |
| `display​Type` | String | Display type of the attribute. | Small, 60.0 | 60.0 |
| `id` | String | ID of the attribute. | Small, 60.0 | 60.0 |
| `is​Cloneable` | Boolean | Indicates if the attribute is cloneable (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Configurable` | Boolean | Indicates if the attribute is configurable (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isEncrypted` | Boolean | Indicates if the attribute is encrypted (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isHidden` | Boolean | Indicates if the attribute is hidden (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isPrice​Impacting` | Boolean | Indicates if this is a price impacting attribute (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isReadOnly` | Boolean | Indicates if the attribute is read-only (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isRequired` | Boolean | Indicates if the attribute is required (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `label` | String | Label of the attribute. | Small, 60.0 | 60.0 |
| `maximum​Value` | String | Maximum value for the product attribute. | Small, 60.0 | 60.0 |
| `minimum​Value` | String | Minimum value for the product attribute. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute. | Small, 60.0 | 60.0 |
| `sequence` | Integer | Sequence values of the attribute. | Small, 60.0 | 60.0 |
| `status` | String | Status of the attribute. | Small, 60.0 | 60.0 |
| `stepValue` | String | Step value for the attribute. | Small, 60.0 | 60.0 |
| `unitOfMeasure` | [Configurator Unit Of Measure](./connect_responses_configurator_unit_of_measure_output.htm.md)[] | Details about the unit of measure associated with an attribute. | Small, 63.0 | 63.0 |
| `userValue` | String | User value of the attribute. | Small, 60.0 | 60.0 |
| `value​Decoder` | String | Value decoder for the attribute. | Small, 60.0 | 60.0 |
| `value​Description` | String | Value description of the attribute. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_attribute_picklist_output.htm ===
---
page_id: connect_responses_configurator_attribute_picklist_output.htm
title: Configurator Attribute Picklist
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_attribute_picklist_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Attribute Picklist

Output representation of the attribute picklist in a product configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Description of the attribute picklist. | Small, 60.0 | 60.0 |
| `id` | String | ID of the attribute picklist. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute picklist. | Small, 60.0 | 60.0 |
| `status` | String | Status of the attribute picklist. | Small, 60.0 | 60.0 |
| `values` | [Configurator Attribute Picklist Value](./connect_responses_configurator_attribute_picklist_value_output.htm.md)[] | Values of the attribute picklist. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_attribute_picklist_value_output.htm ===
---
page_id: connect_responses_configurator_attribute_picklist_value_output.htm
title: Configurator Attribute Picklist Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_attribute_picklist_value_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Attribute Picklist Value

Output representation of the values of an attribute picklist in a product
    configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code of the attribute value. | Small, 60.0 | 60.0 |
| `description` | String | Description of the attribute value. | Small, 60.0 | 60.0 |
| `display​Value` | String | Display value of the attribute value. | Small, 60.0 | 60.0 |
| `id` | String | ID of the attribute value. | Small, 60.0 | 60.0 |
| `isBoolean​Value` | Boolean | Indicates if this attribute value is a boolean value (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `label` | String | Label of the attribute value. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute value. | Small, 60.0 | 60.0 |
| `sequence` | Integer | Sequence of the attribute value. | Small, 60.0 | 60.0 |
| `status` | String | Status of the attribute value. | Small, 60.0 | 60.0 |
| `textValue` | String | Text value of the attribute value. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_message_output.htm ===
---
page_id: connect_responses_configurator_message_output.htm
title: Configurator Message
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_message_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Message

Output representation of the messages of a product configurator.

        
          

**JSON example**

          
: 
            

```
{
  "messages": {
    "0Q0xx0000004CDsCAM": [
      {
        "message": "This is a quote with warranty",
        "messageType": "Info",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM"
      },
      {
        "message": "It is a group 1C9xx0000004CCGCA2",
        "messageType": "Warning",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM",
        "groupByValue": "1C9xx0000004CCGCA2"
      },
      {
        "message": "We're in group virtual bundle",
        "messageType": "Warning",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM",
        "groupByValue": "1C9xx0000004CCGCA2"
      },
      {
        "message": "It is a group 1C9xx0000004CCOCA2",
        "messageType": "Warning",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM",
        "groupByValue": "1C9xx0000004CCOCA2"
      },
      {
        "message": "We're in group virtual bundle",
        "messageType": "Warning",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM",
        "groupByValue": "1C9xx0000004CCOCA2"
      }
    ],
    "stiId-Laptop1": [
      {
        "message": "Only laptop",
        "messageType": "Info",
        "category": "ConfigurationRules",
        "primaryRecordId": "0Q0xx0000004CDsCAM",
        "relatedRecordId": "stiId-Laptop1"
      }
    ]
  }
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

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `category` | String | Category or type of the error message. Valid values are: `ArcResolutionService` `ArcValidationService` `BundleValidation` `ConfigurationRules` `Pricing` | Small, 60.0 | 60.0 |
| `group​ByValue` | String | Specifies the value from Constraint Modeling Language rule action details. | Small, 67.0 | 67.0 |
| `message` | String | Message that contains the error details. | Small, 60.0 | 60.0 |
| `message​Type` | String | Type of error message. Valid values are: `Error` `Info` `Warning` | Small, 60.0 | 60.0 |
| `primary​RecordId` | String | Primary record ID that contains the error. | Small, 60.0 | 60.0 |
| `related​RecordId` | String | Related record ID for the error, if any. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_output.htm ===
---
page_id: connect_responses_configurator_output.htm
title: Configuration Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Details

Output representation of the product configuration details.

        
          

**JSON example**

          
: 
            

```
{
  "catalogProducts": {
    "additionalFields": [],
    "attributeCategories": [
      {
        "attributes": [
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Load Capacity",
            "code": "CAP",
            "dataType": "NUMBER",
            "defaultValue": "1500",
            "description": "Server racks are designed to support a specific load capacity, commonly measured in kilograms (kg) or pounds (lbs). Typical load capacities range from 500 kg (1102 lbs) to 1500 kg (3307 lbs) depending on the model.",
            "id": "0tjxx00000001DpAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": false,
            "label": "Load Capacity",
            "name": "Load Capacity"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Expansion Slots",
            "code": "SLOTCAP",
            "dataType": "NUMBER",
            "defaultValue": "12",
            "id": "0tjxx00000001H3AAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Expansion Slots",
            "name": "Expansion Slots"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Memory",
            "attributePicklist": {
              "id": "0v5xx0000000001AAA",
              "values": [
                {
                  "code": "MEM",
                  "displayValue": "25",
                  "id": "0v6xx0000000001AAA",
                  "isBooleanValue": false,
                  "name": "25Mem",
                  "sequence": 0,
                  "textValue": "25"
                },
                {
                  "code": "50MEM",
                  "displayValue": "50",
                  "id": "0v6xx000000001eAAA",
                  "isBooleanValue": false,
                  "name": "50Mem",
                  "sequence": 1,
                  "textValue": "50"
                },
                {
                  "code": "100MEM",
                  "displayValue": "100",
                  "id": "0v6xx000000003FAAQ",
                  "isBooleanValue": false,
                  "name": "100Mem",
                  "sequence": 2,
                  "textValue": "100"
                }
              ]
            },
            "dataType": "MULTIPICKLIST",
            "defaultValue": "25",
            "id": "0tjxx00000001IfAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Memory",
            "name": "Memory"
          }
        ],
        "code": "SPEC",
        "name": "Server Rack Specifications"
      }
    ],
    "description": "Introducing the Cisco Server Rack, a sleek and robust solution designed to streamline your data center infrastructure. With its scalable design and advanced cable management features, it ensures optimal performance, efficiency, and easy maintenance for your critical network equipment.",
    "displayUrl": "https://www.cisco.com/content/dam/en/us/products/servers-unified-computing/ucs-c240-m4-rack-server/product-large.jpg",
    "id": "01txx0000006jkuAAA",
    "isActive": true,
    "isAssetizable": true,
    "isConfigurable": true,
    "isSoldOnlyWithOtherProds": false,
    "name": "Cisco Server Rack NX44",
    "nodeType": "bundleProduct",
    "prices": [],
    "productClassification": {
      "id": "11Bxx000002CC02EAG"
    },
    "productCode": "RACK",
    "productComponentGroups": [
      {
        "classifications": [],
        "code": "SERVICE",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Service, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jmWAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": false,
            "isQuantityEditable": false,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Service - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "SERVICE",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jmWAAQ",
              "childSellingModelId": "0jPxx000000004rEAA",
              "doesBundlePriceIncludeChild": true,
              "id": "0dSxx000000001dEAA",
              "isComponentRequired": false,
              "isDefaultComponent": false,
              "isQuantityEditable": false,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000004rEAA",
              "productComponentGroupId": "0y7xx000000001dAAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional"
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000009hEAA",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000PpEAI",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              }
            ]
          }
        ],
        "description": "The services available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx000000001dAAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Services",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 1
      },
      {
        "classifications": [],
        "code": "WARRANTY",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Warranty, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jjIAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": true,
            "isQuantityEditable": true,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Warranty - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "WARRANTY",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jjIAAQ",
              "childSellingModelId": "0jPxx000000001dEAA",
              "doesBundlePriceIncludeChild": false,
              "id": "0dSxx0000000001EAA",
              "isComponentRequired": false,
              "isDefaultComponent": true,
              "isQuantityEditable": true,
              "maxQuantity": 1,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000001dEAA",
              "productComponentGroupId": "0y7xx0000000001AAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional",
              "sequence": 0
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000001dEAA",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000001dEAA",
                  "name": "One Time",
                  "sellingModelType": "OneTime",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000001dEAA"
              },
              {
                "id": "0iOxx00000000HlEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000003FEAQ",
                  "name": "Termed Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000003FEAQ"
              },
              {
                "id": "0iOxx00000000JNEAY",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000KzEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              },
              {
                "id": "0iOxx00000000MbEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000006TEAQ",
                  "name": "Evergreen Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000006TEAQ"
              }
            ]
          }
        ],
        "description": "The warranties available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx0000000001AAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Warranties",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 0
      }
    ],
    "productSellingModelOptions": [
      {
        "id": "0iOxx000000003FEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000001dEAA",
          "name": "One Time",
          "sellingModelType": "OneTime",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000001dEAA"
      },
      {
        "id": "0iOxx000000004rEAA",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000003FEAQ",
          "name": "Termed Monthly",
          "pricingTerm": 1,
          "pricingTermUnit": "Months",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000003FEAQ"
      },
      {
        "id": "0iOxx000000006TEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000004rEAA",
          "name": "Termed Annually",
          "pricingTerm": 1,
          "pricingTermUnit": "Annual",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000004rEAA"
      }
    ],
    "productType": "Bundle"
  },
  "uiTreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "errors": [],
  "success": true,
  "productRecommendations": [
    {
      "referenceId": "CORE_BUNDLE_001",
      "productIds": [
        "01t000000001234",
        "01t000000005678"
      ]
    }
  ],
  "transactionContext": {
    "SalesTransaction": [
      {
        "Status": "Draft",
        "Account": "001xx000003GeIxAAK",
        "BillingCity": "San Francisco",
        "Subtotal": 152500,
        "LastPricedDate": "2023-08-22T05:55:39Z",
        "businessObjectType": "Quote",
        "TotalAmount": 152500,
        "ShippingStreet": "415 Mission St",
        "SalesTransactionItem": [
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jkuAAA",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 150000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQmGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 150000,
            "TotalLineAmount": 150000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 150000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQmGAM",
            "PriceWaterFall": {
              "currencyCode": "USD",
              "executionEndTimestamp": "2023-09-18T20:11:15.016Z",
              "executionId": "ruepwmHn2ZFvnQo5bjot",
              "executionStartTimestamp": "2023-09-18T20:11:14.906Z",
              "lineItemId": "0QLxx0000004CQmGAM",
              "output": {
                "NetUnitPrice": 150000,
                "Subtotal": 0
              },
              "success": true,
              "waterfall": [
                {
                  "fieldToTagNameMapping": {
                    "NetUnitPrice": "ItemUnitPrice",
                    "AdjustmentValue": "ItemAdjustmentValue",
                    "Subtotal": "ItemTotalAdjustmentAmount",
                    "Quantity": "ItemQuantity",
                    "LineItemId": "SalesTransactionItemSource",
                    "InputUnitPrice": "ItemUnitPrice"
                  },
                  "inputParameters": {
                    "Quantity": 1,
                    "LineItemId": "0QLxx0000004CQmGAM",
                    "InputUnitPrice": 150000,
                    "AdjustmentType": "Amount"
                  },
                  "outputParameters": {
                    "NetUnitPrice": 150000,
                    "Subtotal": 0
                  },
                  "pricingElement": {
                    "adjustments": [
                      {
                        "AdjustmentType": "Amount"
                      }
                    ],
                    "elementType": "MANUALDISCOUNT",
                    "name": "ManualDiscount"
                  },
                  "sequence": 1
                }
              ]
            },
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 150000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "SalesTransactionItemAttribute": [
              {
                "AttributeKey": "0tjxx00000001H3AAI",
                "AttributeValue": "30.0",
                "AttributePicklistValue": null,
                "IsPriceImpacting": true,
                "businessObjectType": "QuoteLineItemAttribute",
                "AttributeName": "Expansion Slots",
                "AttributeDefinitionCode": "SLOTCAP",
                "id": "0zuxx0000000001AAA",
                "SalesTransactionItemAttrParent": "0QLxx0000004CQmGAM"
              }
            ],
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx0000009154AAA",
            "PricingTermCount": 1,
            "NetUnitPrice": 150000,
            "UnitPrice": 150000,
            "StartingUnitPrice": 150000,
            "SalesTrxnItemRelationship": [
              {
                "ProductRelationshipType": "0yoxx00000001IfAAI",
                "MainItemRole": "Bundle",
                "AssociatedItem": "0QLxx0000004CQnGAM",
                "ProductRelatedComponent": "0dSxx0000000001EAA",
                "MainItem": "0QLxx0000004CQmGAM",
                "AssociatedQuantScaleMethod": "Proportional",
                "businessObjectType": "QuoteLineRelationship",
                "AssociatedItemRole": "BundleComponent",
                "SalesTrnItemRelationshipParent": "0Q0xx0000004CAeCAM",
                "id": "0yQxx000000001dEAA",
                "AssociatedItemPricing": "NotIncludedInBundlePrice"
              }
            ],
            "TotalPrice": 150000,
            "PeriodBoundaryDay": null
          },
          {
            "ProrationPolicy": null,
            "Discount": null,
            "ProductSellingModel": "0jPxx000000001dEAA",
            "Product": "01txx0000006jjIAAQ",
            "businessObjectType": "QuoteLineItem",
            "BasisTransactionItem": null,
            "PartnerUnitPrice": null,
            "StartingUnitPriceSource": "System",
            "ListPrice": 2000,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLxx0000004CQnGAM",
            "SubscriptionTerm": null,
            "StartDate": null,
            "NetTotalPrice": 2000,
            "TotalLineAmount": 2000,
            "PeriodBoundaryStartMonth": null,
            "ListPriceTotal": 2000,
            "PartnerDiscountPercent": null,
            "id": "0QLxx0000004CQnGAM",
            "PriceWaterFall": {
              "currencyCode": "USD",
              "executionEndTimestamp": "023-09-18T20:11:15.016Z",
              "executionId": "ruepwmHn2ZFvnQo5bjot",
              "executionStartTimestamp": "2023-09-18T20:11:14.906Z",
              "lineItemId": "0QLxx0000004CQnGAM",
              "output": {
                "NetUnitPrice": 2000,
                "Subtotal": 0
              },
              "success": true,
              "waterfall": [
                {
                  "fieldToTagNameMapping": {
                    "NetUnitPrice": "ItemUnitPrice",
                    "AdjustmentValue": "ItemAdjustmentValue",
                    "Subtotal": "ItemTotalAdjustmentAmount",
                    "Quantity": "ItemQuantity",
                    "LineItemId": "SalesTransactionItemSource",
                    "InputUnitPrice": "ItemUnitPrice"
                  },
                  "inputParameters": {
                    "Quantity": 1,
                    "LineItemId": "0QLxx0000004CQnGAM",
                    "InputUnitPrice": 2000,
                    "AdjustmentType": "Amount"
                  },
                  "outputParameters": {
                    "NetUnitPrice": 2000,
                    "Subtotal": 0
                  },
                  "pricingElement": {
                    "adjustments": [
                      {}
                    ],
                    "elementType": "MANUALDISCOUNT",
                    "name": "ManualDiscount"
                  },
                  "sequence": 1
                }
              ]
            },
            "BillingFrequency": null,
            "SalesTransactionItemParent": "0Q0xx0000004CAeCAM",
            "StartingPriceTotal": 2000,
            "Quantity": 1,
            "PeriodBoundary": null,
            "EndDate": null,
            "DiscountAmount": null,
            "PricebookEntry": "01uxx000000913SAAQ",
            "PricingTermCount": 1,
            "NetUnitPrice": 2000,
            "UnitPrice": 2000,
            "StartingUnitPrice": 2000,
            "TotalPrice": 2000,
            "PeriodBoundaryDay": null
          }
        ],
        "BillingCountry": "US",
        "BillingStreet": "415 Mission St",
        "Pricebook": "01sxx0000005uDZAAY",
        "ShippingPostalCode": "94105",
        "SalesTransactionSource": "0Q0xx0000004CAeCAM",
        "ShippingCountry": "US",
        "ShippingCity": "San Francisco",
        "ShippingState": "CA",
        "BillingPostalCode": "94105",
        "id": "0Q0xx0000004CAeCAM",
        "BillToContact": null,
        "Contract": null,
        "BillingState": "CA"
      }
    ]
  },
  "transactionContextId": "cda87acd-45ed-4913-903e-9dd33cec85a6",
  "transactionContextMappingId": "11jxx0000004LwOAAU"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​Products` | [Configurator Product Catalog](./connect_responses_configurator_product_catalog_output.htm.md)[] | Structure that contains the product catalog data. | Small, 61.0 | 61.0 |
| `errors` | [ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors that contains a message and an error code. | Small, 60.0 | 60.0 |
| `messages` | Map<String, [Configurator Message](./connect_responses_configurator_message_output.htm.md)>> | Messages from the validation, Business Rules Engine (BRE), or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `product​Recommendations` | [Configurator Product Recommendations](./connect_responses_configurator_product_recommendation_output.htm.md) | List of product recommendations. | Small, 65.0 | 65.0 |
| `success` | Boolean | Indicates whether the request is successful (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `transaction​Context` | Map<String, Object> | Serialized JSON representation of the transaction context. | Small, 60.0 | 60.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Small, 60.0 | 60.0 |
| `transactionContext​MappingId` | String | ID of the context mapping. | Small, 60.0 | 60.0 |
| `transaction​Qualification` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the qualification context. | Small, 60.0 | 60.0 |
| `ui​Treatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_configurator_price_output.htm ===
---
page_id: connect_responses_configurator_price_output.htm
title: Configurator Price
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_price_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Price

Output representation of the pricing details in a product configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `currency​IsoCode` | String | Currency ISO code of the price book entry. | Small, 60.0 | 60.0 |
| `effective​From` | String | Date from when the price book entry is effective. | Small, 60.0 | 60.0 |
| `effective​To` | String | Date until when the price book entry is effective. | Small, 60.0 | 60.0 |
| `isDefault` | Boolean | Indicates if this price book entry is the default pricing model (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Selected` | Boolean | Indicates if this price book entry is selected (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `pricebook​EntryId` | String | ID of the price book entry. | Small, 60.0 | 60.0 |
| `pricebookId` | String | Pricebook2 ID of the price book entry. | Small, 60.0 | 60.0 |
| `pricing​Model` | [Configurator Pricing Model](./connect_responses_configurator_pricing_model_output.htm.md)[] | Pricing model details of the price book entry. | Small, 60.0 | 60.0 |
| `unitPrice` | Double | Unit price of the price book entry. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_pricing_model_output.htm ===
---
page_id: connect_responses_configurator_pricing_model_output.htm
title: Configurator Pricing Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_pricing_model_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Pricing Model

Output representation of the details of a pricing model in a product
    configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `frequency` | String | Frequency of the pricing model. | Small, 60.0 | 60.0 |
| `id` | String | ID of the pricing model. | Small, 60.0 | 60.0 |
| `name` | String | Name of the pricing model. | Small, 60.0 | 60.0 |
| `occurrence` | Integer | Occurrence of the pricing model. | Small, 60.0 | 60.0 |
| `pricing​ModelType` | String | Type of the pricing model. | Small, 60.0 | 60.0 |
| `unitOf​Measure` | String | Unit of measure for the pricing model. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_product_catalog_output.htm ===
---
page_id: connect_responses_configurator_product_catalog_output.htm
title: Configurator Product Catalog
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_catalog_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Catalog

Output representation of the product catalog.

        
          

**JSON example**

          
: 
            

```

  "catalogProducts": {
    "additionalFields": [],
    "attributeCategories": [
      {
        "attributes": [
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Load Capacity",
            "code": "CAP",
            "dataType": "NUMBER",
            "defaultValue": "1500",
            "description": "Server racks are designed to support a specific load capacity, commonly measured in kilograms (kg) or pounds (lbs). Typical load capacities range from 500 kg (1102 lbs) to 1500 kg (3307 lbs) depending on the model.",
            "id": "0tjxx00000001DpAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": false,
            "label": "Load Capacity",
            "name": "Load Capacity"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Expansion Slots",
            "code": "SLOTCAP",
            "dataType": "NUMBER",
            "defaultValue": "12",
            "id": "0tjxx00000001H3AAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Expansion Slots",
            "name": "Expansion Slots"
          },
          {
            "attributeCategoryId": "0v3xx0000000001AAA",
            "attributeNameOverride": "Memory",
            "attributePicklist": {
              "id": "0v5xx0000000001AAA",
              "values": [
                {
                  "code": "MEM",
                  "displayValue": "25",
                  "id": "0v6xx0000000001AAA",
                  "isBooleanValue": false,
                  "name": "25Mem",
                  "sequence": 0,
                  "textValue": "25"
                },
                {
                  "code": "50MEM",
                  "displayValue": "50",
                  "id": "0v6xx000000001eAAA",
                  "isBooleanValue": false,
                  "name": "50Mem",
                  "sequence": 1,
                  "textValue": "50"
                },
                {
                  "code": "100MEM",
                  "displayValue": "100",
                  "id": "0v6xx000000003FAAQ",
                  "isBooleanValue": false,
                  "name": "100Mem",
                  "sequence": 2,
                  "textValue": "100"
                }
              ]
            },
            "dataType": "MULTIPICKLIST",
            "defaultValue": "25",
            "id": "0tjxx00000001IfAAI",
            "isCloneable": false,
            "isConfigurable": true,
            "isHidden": false,
            "isPriceImpacting": false,
            "isReadOnly": false,
            "isRequired": true,
            "label": "Memory",
            "name": "Memory"
          }
        ],
        "code": "SPEC",
        "name": "Server Rack Specifications"
      }
    ],
    "description": "Introducing the Cisco Server Rack, a sleek and robust solution designed to streamline your data center infrastructure. With its scalable design and advanced cable management features, it ensures optimal performance, efficiency, and easy maintenance for your critical network equipment.",
    "displayUrl": "https://www.cisco.com/content/dam/en/us/products/servers-unified-computing/ucs-c240-m4-rack-server/product-large.jpg",
    "id": "01txx0000006jkuAAA",
    "isActive": true,
    "isAssetizable": true,
    "isConfigurable": true,
    "isSoldOnlyWithOtherProds": false,
    "name": "Cisco Server Rack NX44",
    "nodeType": "bundleProduct",
    "prices": [],
    "productClassification": {
      "id": "11Bxx000002CC02EAG"
    },
    "productCode": "RACK",
    "productComponentGroups": [
      {
        "classifications": [],
        "code": "SERVICE",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Service, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jmWAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": false,
            "isQuantityEditable": false,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Service - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "SERVICE",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jmWAAQ",
              "childSellingModelId": "0jPxx000000004rEAA",
              "doesBundlePriceIncludeChild": true,
              "id": "0dSxx000000001dEAA",
              "isComponentRequired": false,
              "isDefaultComponent": false,
              "isQuantityEditable": false,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000004rEAA",
              "productComponentGroupId": "0y7xx000000001dAAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional"
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000009hEAA",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000PpEAI",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              }
            ]
          }
        ],
        "description": "The services available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx000000001dAAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Services",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 1
      },
      {
        "classifications": [],
        "code": "WARRANTY",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Warranty, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jjIAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": true,
            "isQuantityEditable": true,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Warranty - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "WARRANTY",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jjIAAQ",
              "childSellingModelId": "0jPxx000000001dEAA",
              "doesBundlePriceIncludeChild": false,
              "id": "0dSxx0000000001EAA",
              "isComponentRequired": false,
              "isDefaultComponent": true,
              "isQuantityEditable": true,
              "maxQuantity": 1,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000001dEAA",
              "productComponentGroupId": "0y7xx0000000001AAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional",
              "sequence": 0
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000001dEAA",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000001dEAA",
                  "name": "One Time",
                  "sellingModelType": "OneTime",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000001dEAA"
              },
              {
                "id": "0iOxx00000000HlEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000003FEAQ",
                  "name": "Termed Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000003FEAQ"
              },
              {
                "id": "0iOxx00000000JNEAY",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000KzEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              },
              {
                "id": "0iOxx00000000MbEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000006TEAQ",
                  "name": "Evergreen Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000006TEAQ"
              }
            ]
          }
        ],
        "description": "The warranties available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx0000000001AAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Warranties",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 0
      }
    ],
    "productSellingModelOptions": [
      {
        "id": "0iOxx000000003FEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000001dEAA",
          "name": "One Time",
          "sellingModelType": "OneTime",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000001dEAA"
      },
      {
        "id": "0iOxx000000004rEAA",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000003FEAQ",
          "name": "Termed Monthly",
          "pricingTerm": 1,
          "pricingTermUnit": "Months",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000003FEAQ"
      },
      {
        "id": "0iOxx000000006TEAQ",
        "productId": "01txx0000006jkuAAA",
        "productSellingModel": {
          "id": "0jPxx000000004rEAA",
          "name": "Termed Annually",
          "pricingTerm": 1,
          "pricingTermUnit": "Annual",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx000000004rEAA"
      }
    ],
    "productType": "Bundle"
  }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | [Configurator Additional Fields](./connect_responses_configurator_additional_fields_output.htm.md)[] | Additional fields for this product. | Small, 60.0 | 60.0 |
| `attribute​Categories` | [Configurator Attribute Category](./connect_responses_configurator_attribute_category_output.htm.md)[] | List of attribute categories. The categories that aren’t categorized are specified in the uncategorized entry in this list. | Small, 60.0 | 60.0 |
| `availability​Date` | String | Availability date of this product. | Small, 60.0 | 60.0 |
| `description` | String | Description of this product. | Small, 60.0 | 60.0 |
| `discontinued​Date` | String | Date when this product is discontinued. | Small, 60.0 | 60.0 |
| `display​Url` | String | Display URL of this product. | Small, 60.0 | 60.0 |
| `endOf​LifeDate` | String | End of life date for this product. | Small, 60.0 | 60.0 |
| `id` | String | ID of the product. | Small, 60.0 | 60.0 |
| `isActive` | Boolean | Indicates whether this product is active (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Assetizable` | Boolean | Indicates whether this product is assetizable (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isComponent​Required` | Boolean | Indicates whether the component is required (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Configurable` | Boolean | Indicates whether the component is configurable (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isDefault​Component` | Boolean | Indicates whether the component is a default component (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isQuantity​Editable` | Boolean | Indicates whether the quantity of the component is editable ( `true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isSoldOnly​WithOtherProds` | Boolean | Indicates whether this product is sold only with other products (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `name` | String | Name of the product. | Small, 60.0 | 60.0 |
| `nodeType` | String | Node type of the product. | Small, 60.0 | 60.0 |
| `prices` | [Configurator Price](./connect_responses_configurator_price_output.htm.md)[] | List of prices from the product catalog. | Small, 60.0 | 60.0 |
| `product​Classification` | [Configurator Product Classification](./connect_responses_configurator_product_classification_output.htm.md)[] | Classification details of the product. | Small, 60.0 | 60.0 |
| `productCode` | String | Code of the product. | Small, 60.0 | 60.0 |
| `product​ComponentGroups` | [Configurator Product Component Group](./connect_responses_configurator_product_component_group_output.htm.md)[] | List of product component groups for this product. | Small, 60.0 | 60.0 |
| `product​RelatedComponent` | [Configurator Product Related Component](./connect_responses_configurator_product_related_component_output.htm.md)[] | Details of the product related component of this product. | Small, 60.0 | 60.0 |
| `productSelling​ModelOptions` | [Configurator Product Selling Model Option](./connect_responses_configurator_product_selling_model_option_output.htm.md)[] | List of product selling model options for this product. | Small, 60.0 | 60.0 |
| `productType` | String | Type of product. | Small, 60.0 | 60.0 |
| `qualification​Context` | [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)[] | Details of the qualification context of the product. | Small, 60.0 | 60.0 |
| `status` | String | Status of the product. | Small, 60.0 | 60.0 |
| `unitOfMeasure` | [Configurator Unit Of Measure](./connect_responses_configurator_unit_of_measure_output.htm.md)[] | Details about the unit of measure associated with a product. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_configurator_product_classification_output.htm ===
---
page_id: connect_responses_configurator_product_classification_output.htm
title: Configurator Product Classification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_classification_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Classification

Output representation of the product classification in a product
    configuration.

        
          

**JSON example**

          
: 
            

```

    "productClassification": {
      "id": "11Bxx000002CC02EAG"
    }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the product classification. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_product_component_group_output.htm ===
---
page_id: connect_responses_configurator_product_component_group_output.htm
title: Configurator Product Component Group
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_component_group_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Component Group

Output representation of the product component group in a product
    classification.

        
          

**JSON example**

          
: 
            

```

    "productComponentGroups": [
      {
        "classifications": [],
        "code": "SERVICE",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Service, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jmWAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": false,
            "isQuantityEditable": false,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Service - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "SERVICE",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jmWAAQ",
              "childSellingModelId": "0jPxx000000004rEAA",
              "doesBundlePriceIncludeChild": true,
              "id": "0dSxx000000001dEAA",
              "isComponentRequired": false,
              "isDefaultComponent": false,
              "isQuantityEditable": false,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000004rEAA",
              "productComponentGroupId": "0y7xx000000001dAAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional"
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000009hEAA",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000PpEAI",
                "productId": "01txx0000006jmWAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              }
            ]
          }
        ],
        "description": "The services available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx000000001dAAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Services",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 1
      },
      {
        "classifications": [],
        "code": "WARRANTY",
        "components": [
          {
            "additionalFields": [],
            "attributeCategories": [],
            "description": "Introducing the Cisco Rack Server NX44 Warranty, a comprehensive protection plan designed to safeguard your valuable data infrastructure. With extended coverage and rapid response times, this warranty ensures peace of mind and uninterrupted performance for your critical business operations.",
            "id": "01txx0000006jjIAAQ",
            "isActive": true,
            "isAssetizable": true,
            "isComponentRequired": false,
            "isConfigurable": false,
            "isDefaultComponent": true,
            "isQuantityEditable": true,
            "isSoldOnlyWithOtherProds": false,
            "name": "Cisco Rack Server Warranty - 1 Year",
            "nodeType": "simpleProduct",
            "prices": [],
            "productClassification": {},
            "productCode": "WARRANTY",
            "productComponentGroups": [],
            "productRelatedComponent": {
              "childProductId": "01txx0000006jjIAAQ",
              "childSellingModelId": "0jPxx000000001dEAA",
              "doesBundlePriceIncludeChild": false,
              "id": "0dSxx0000000001EAA",
              "isComponentRequired": false,
              "isDefaultComponent": true,
              "isQuantityEditable": true,
              "maxQuantity": 1,
              "parentProductId": "01txx0000006jkuAAA",
              "parentSellingModelId": "0jPxx000000001dEAA",
              "productComponentGroupId": "0y7xx0000000001AAA",
              "productRelationshipTypeId": "0yoxx00000001IfAAI",
              "quantity": 1,
              "quantityScaleMethod": "Proportional",
              "sequence": 0
            },
            "productSellingModelOptions": [
              {
                "id": "0iOxx000000001dEAA",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000001dEAA",
                  "name": "One Time",
                  "sellingModelType": "OneTime",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000001dEAA"
              },
              {
                "id": "0iOxx00000000HlEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000003FEAQ",
                  "name": "Termed Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000003FEAQ"
              },
              {
                "id": "0iOxx00000000JNEAY",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000004rEAA",
                  "name": "Termed Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "TermDefined",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000004rEAA"
              },
              {
                "id": "0iOxx00000000KzEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx0000000085EAA",
                  "name": "Evergreen Annually",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Annual",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx0000000085EAA"
              },
              {
                "id": "0iOxx00000000MbEAI",
                "productId": "01txx0000006jjIAAQ",
                "productSellingModel": {
                  "id": "0jPxx000000006TEAQ",
                  "name": "Evergreen Monthly",
                  "pricingTerm": 1,
                  "pricingTermUnit": "Months",
                  "sellingModelType": "Evergreen",
                  "status": "Active"
                },
                "productSellingModelId": "0jPxx000000006TEAQ"
              }
            ]
          }
        ],
        "description": "The warranties available for the Cisco Server Rack NX44 product provide comprehensive coverage and support for optimal performance and reliability, ensuring peace of mind for your data center infrastructure.",
        "id": "0y7xx0000000001AAA",
        "maxBundleComponents": 1,
        "minBundleComponents": 0,
        "name": "Warranties",
        "parentProductId": "01txx0000006jkuAAA",
        "sequence": 0
      }
    ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `classifications` | [Configurator Product Classification](./connect_responses_configurator_product_classification_output.htm.md)[] | List of classifications for this product component group. | Small, 60.0 | 60.0 |
| `code` | String | Code of the product component group. | Small, 60.0 | 60.0 |
| `components` | [Configurator Product Catalog](./connect_responses_configurator_product_catalog_output.htm.md)[] | Components within the product component group. | Small, 60.0 | 60.0 |
| `description` | String | Description of the product component group. | Small, 60.0 | 60.0 |
| `id` | String | ID of the product component group. | Small, 60.0 | 60.0 |
| `maxBundle​Components` | Integer | Maximum number of bundle components within the product component group. | Small, 60.0 | 60.0 |
| `minBundle​Components` | Integer | Minimum number of bundle components within the product component group. | Small, 60.0 | 60.0 |
| `name` | String | Name of the product component group. | Small, 60.0 | 60.0 |
| `parent​ProductId` | String | Parent Product2 ID of the product component group. | Small, 60.0 | 60.0 |
| `sequence` | Integer | Sequence of the product component group. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_product_recommendation_output.htm ===
---
page_id: connect_responses_configurator_product_recommendation_output.htm
title: Configurator Product Recommendations
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_recommendation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Recommendations

Output representation of the details of the product recommendations.

      
        
          

**JSON Example**

          
: 
            

```
{
  "productRecommendations": [
    {
      "referenceId": "CORE_BUNDLE_001",
      "productIds": [
        "01t000000001234",
        "01t000000005678"
      ]
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `productIds` | String[] | List of recommended product IDs. | Small, 65.0 | 65.0 |
| `referenceId` | String | Reference ID for the recommendation. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_configurator_product_related_component_output.htm ===
---
page_id: connect_responses_configurator_product_related_component_output.htm
title: Configurator Product Related Component
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_related_component_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Related Component

Output representation of the product related component in a product
    configuration.

        
          

**JSON example**

          
: 
            

```

         "productRelatedComponent": {
           "childProductId": "01txx0000006jmWAAQ",
           "childSellingModelId": "0jPxx000000004rEAA",
           "doesBundlePriceIncludeChild": true,
           "id": "0dSxx000000001dEAA",
           "isComponentRequired": false,
           "isDefaultComponent": false,
           "isQuantityEditable": false,
           "parentProductId": "01txx0000006jkuAAA",
           "parentSellingModelId": "0jPxx000000004rEAA",
           "productComponentGroupId": "0y7xx000000001dAAA",
           "productRelationshipTypeId": "0yoxx00000001IfAAI",
           "quantity": 1,
           "quantityScaleMethod": "Proportional",
           "quoteVisibility": "Quote Document Only"
         }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

            
              

              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `child​ProductId` | String | ID of the child product in the bundle. | Small, 60.0 | 60.0 |
| `child​Selling​ModelId` | String | ID of the child product selling model record. | Small, 60.0 | 60.0 |
| `doesBundle​Price​IncludeChild` | Boolean | Indicates whether the price of the bundle includes the child product (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `id` | String | ID of the product related component. | Small, 60.0 | 60.0 |
| `isComponent​Required` | Boolean | Indicates whether the component is required in the bundle (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isDefault​Component` | Boolean | Indicates whether to select the component in the bundle group by default (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isQuantity​Editable` | Boolean | Indicates whether to allow changes to the quantity of the component in the bundle (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `max​Quantity` | Double | Maximum quantity of the product in the opportunity, quote, or order line item. | Small, 60.0 | 60.0 |
| `min​Quantity` | Double | Minimum quantity of the product in the opportunity, quote, or order line item. | Small, 60.0 | 60.0 |
| `parent​ProductId` | String | ID of the parent product. | Small, 60.0 | 60.0 |
| `parent​Selling​ModelId` | String | ID of the parent product selling model record. | Small, 60.0 | 60.0 |
| `product​Classification​Id` | String | ID of the product classification record. | Small, 60.0 | 60.0 |
| `product​Component​GroupId` | String | ID of the product component group. | Small, 60.0 | 60.0 |
| `product​Relationship​TypeId` | String | ID of the product relationship type record. | Small, 60.0 | 60.0 |
| `quantity` | Double | Quantity of the child products. | Small, 60.0 | 60.0 |
| `quantity​Scale​Method` | String | Method to scale the quantity of the child product in relation to the quantity of the parent. Valid values are: `Constant` `Proportional` | Small, 60.0 | 60.0 |
| `quote​Visibility` | String | Specifies whether a quote line item must be shown on the transaction line editor or quote document. Valid values are: `Always` `Transaction Line Editor Only`—Specifies whether to show a quote line item on quote editor only. `Quote Document Only`—Specifies whether to show a quote line item on quote proposal only. `Never` The API returns this property only if the CoreCPQ permission set is available. | Small, 64.0 | 64.0 |
| `sequence` | Integer | Order in which the child products are displayed. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_product_selling_model_option_output.htm ===
---
page_id: connect_responses_configurator_product_selling_model_option_output.htm
title: Configurator Product Selling Model Option
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_selling_model_option_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Selling Model Option

Output representation of the product selling model option in a product
    configuration.

        
          

**JSON example**

          
: 
            

```

         "productSellingModelOptions": [
           {
             "id": "0iOxx000000009hEAA",
             "productId": "01txx0000006jmWAAQ",
             "productSellingModel": {
               "id": "0jPxx000000004rEAA",
            "name": "Termed Annually",
               "pricingTerm": 1,
               "pricingTermUnit": "Annual",
               "sellingModelType": "TermDefined",
               "status": "Active"
             },
             "productSellingModelId": "0jPxx000000004rEAA"
           },
           {
             "id": "0iOxx00000000PpEAI",
             "productId": "01txx0000006jmWAAQ",
             "productSellingModel": {
               "id": "0jPxx0000000085EAA",
               "name": "Evergreen Annually",
               "pricingTerm": 1,
               "pricingTermUnit": "Annual",
               "sellingModelType": "Evergreen",
               "status": "Active"
             },
             "productSellingModelId": "0jPxx0000000085EAA"
           }
         ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the product selling model option. | Small, 60.0 | 60.0 |
| `product​Id` | String | ID of the product that’s associated with the product selling model option. | Small, 60.0 | 60.0 |
| `product​Selling​Model` | [Configurator Product Selling Model](./connect_responses_configurator_product_selling_model_output.htm.md)[] | Product selling model that’s associated with the product selling model option. | Small, 60.0 | 60.0 |
| `product​Selling​ModelId` | String | ID of the product selling model that’s associated with the product selling model option. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_product_selling_model_output.htm ===
---
page_id: connect_responses_configurator_product_selling_model_output.htm
title: Configurator Product Selling Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_product_selling_model_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Product Selling Model

Output representation of the product selling model in a product
    configuration.

        
          

**JSON example**

          
: 
            

```

     "productSellingModel": {
         "id": "0jPxx0000000085EAA",
         "name": "Evergreen Annually",
         "pricingTerm": 1,
         "pricingTermUnit": "Annual",
         "sellingModelType": "Evergreen",
         "status": "Active"
  }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the product selling model. | Small, 60.0 | 60.0 |
| `name` | String | Name of the product selling model. | Small, 60.0 | 60.0 |
| `pricing​Term` | Integer | Pricing term of the product selling model. | Small, 60.0 | 60.0 |
| `pricing​TermUnit` | String | Pricing term unit of the product selling model. | Small, 60.0 | 60.0 |
| `selling​ModelType` | String | Selling model type of the product selling model. | Small, 60.0 | 60.0 |
| `status` | String | Status of the product selling model. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_qualification_context_output.htm ===
---
page_id: connect_responses_configurator_qualification_context_output.htm
title: Configurator Qualification Context
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_qualification_context_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Qualification Context

Output representation of the qualification context in a product
    configuration.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `is​Qualified` | Boolean | Indicates whether the product is qualified (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `reason` | String | Reason for the qualification of this product. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_configurator_u_i_treatment_output.htm ===
---
page_id: connect_responses_configurator_u_i_treatment_output.htm
title: Configurator UI Treatment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_u_i_treatment_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator UI Treatment

Output representation of the details of the UI treatments of a product configurator. The
    details include the product configuration rule actions to override the disable or hide behavior
    in the UI for product options, product attributes, and attribute picklist values.

        
          

**JSON Example**

          
: 
            

```
[
  {
    "details": {
      "attributeId": "0tjxx0000000007AAA",
      "prcId": "0dSxx0000000007EAA",
      "stiId": "0QLxx0000004CU0GAM",
      "attributePicklistValueId": "0v6xx0000000005AAA"
    },
    "uiTreatmentScope": "Bundle",
    "uiTreatmentTarget": "Attribute_Picklist_Value",
    "uiTreatmentType": "Hide"
  },
  {
    "details": {
      "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
    },
    "uiTreatmentScope": "Product",
    "uiTreatmentTarget": "Component",
    "uiTreatmentType": "Disable"
  }
]
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

              

              

            

            
              

              

              

- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `details` | Map<String, Object> | Key-value pair that specifies the items to apply the rules on, which includes these details. ID of the sales transaction item ID of the product-related component ID of the attribute ID of the attribute picklist value | Small, 62.0 | 62.0 |
| `uiTreatment​Scope` | String | Type of the UI treatment to be performed. Valid values are: `Product`—UI treatment is applicable to a certain product only. `Bundle`—UI treatment is applicable to the whole bundle. | Small, 62.0 | 62.0 |
| `uiTreatment​Target` | String | Target of the UI treatment. Valid values are: `Component`—Represents a product option or bundle component. `Quantity`—Represents a quantity field. `Attribute`—Represents a certain attribute of the product. `Attribute_Picklist_Value`—Represents one of the picklist values of a product attribute. | Small, 62.0 | 62.0 |
| `uiTreatment​Type` | String | Type of UI treatment to be performed. Valid values are: `Hide`—Hide the associated target. `Disable`—Disable the associated target. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_configurator_unit_of_measure_output.htm ===
---
page_id: connect_responses_configurator_unit_of_measure_output.htm
title: Configurator Unit Of Measure
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_configurator_unit_of_measure_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Unit Of Measure

Output representation of the details of the unit of measure record.

      
        
          

**JSON Example**

          
: 
            

```
{
  "unitOfMeasure": {
    "id": "0hEXR00000000BJ2AY",
    "name": "Litres",
    "roundingMethod": "Down",
    "scale": 2,
    "unitCode": "Ltrs"
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the unit of measure record. | Small, 63.0 | 63.0 |
| `name` | String | Name of the unit of measure record. | Small, 63.0 | 63.0 |
| `rounding​Method` | String | Rounding method associated with the unit of measure record. | Small, 63.0 | 63.0 |
| `scale` | Integer | Scale associated with the unit of measure record. | Small, 63.0 | 63.0 |
| `unitCode` | String | Unit code associated with the unit of measure record. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_create_favorite_output.htm ===
---
page_id: connect_responses_create_favorite_output.htm
title: Configuration Record Save
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_create_favorite_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Record Save

Output representation of the details of a saved configuration.

        
          

**JSON example**

          
: This example shows a sample when the save operation is successful.

          
: 
            

```
{
  "errors": [],
  "id": "1Nyxx0000004CNYCA2"
}
```

          

          
: This example shows a sample when the save operation has errors.

          
: 
            

```
{
  "errors": [{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "INVALID_REFERENCEOBJECTID"
}]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](./connect_responses_configuration_list_error_response.htm.md) | List of errors that contains a message and an error code. | Small, 63.0 | 63.0 |
| `id` | String | ID of the configuration that's saved.This property isn't shown if the operation has errors. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_delete_nodes_configurator_output.htm ===
---
page_id: connect_responses_delete_nodes_configurator_output.htm
title: Configurator Delete Nodes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_delete_nodes_configurator_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Delete Nodes

Output representation of the details of the configuration request to delete
    nodes.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, [Configurator Message](./connect_responses_configurator_message_output.htm.md)> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engine (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the qualification rule execution results. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_favorite_list_output_represenation.htm ===
---
page_id: connect_responses_favorite_list_output_represenation.htm
title: Configuration List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_favorite_list_output_represenation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration List

Output representation of the details of the saved configuration.

    

        
          

**JSON example**

          
: 
            

```
{
  "errors": [],
  "savedConfigurations": [
    {
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
  ],
  "success": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](./connect_responses_configuration_list_error_response.htm.md) | List of errors that contains a message and an error code. | Small, 63.0 | 63.0 |
| `saved​Configurations` | [Configuration Save Details](./connect_responses_favorite_output_represenation.htm.md) | Configuration details associated with the `referenceRecordID` request parameter. | Small, 63.0 | 63.0 |
| `success` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_favorite_output_represenation.htm ===
---
page_id: connect_responses_favorite_output_represenation.htm
title: Configuration Save Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_favorite_output_represenation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Save Details

Output representation of the details of a saved configuration.

    

        
          

**JSON example**

          
: 
            

```
{
  "savedConfigurations": [
    {
  "data": "{\"LegalEntity\":null,\"ProductName\":\"Monitor\",\"businessObjectType\":\"QuoteLineItem\",\"Product\":\"01txx0000006i2aAAA\",\"ItemIsPrimarySegment\":false,\"ListPrice\":144.99,\"ValidationResult\":null,\"StartDate\":null,\"ContractVolumePasId\":null,\"BillingTreatment\":null,\"PeriodBoundaryStartMonth\":null,\"SalesTransactionSourceAsset\":null,\"id\":\"0QLxx0000004C9VGAU\",\"PartnerDiscountPercent\":10,\"PriceWaterFall\":null,\"BillingFrequency\":null,\"ProductCode\":\"MO001\",\"DerivedPricingAttribute\":false,\"TaxTreatment\":null,\"Subtotal\":1739.88,\"ItemRampIdentifier\":null,\"ItemSegmentName\":null,\"SalesTransactionItemAttribute\":[{\"AttributeKey\":\"0tjxx0000000001AAA\",\"AttributeValue\":\"1080p Built-in Display\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx0000000001AAA\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display\",\"id\":\"0zuxx000000000FAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"},{\"AttributeKey\":\"0tjxx0000000009AAA\",\"AttributeValue\":\"24 Inch\",\"ParentReference\":\"0QLxx0000004C9VGAU\",\"AttributePicklistValue\":\"0v6xx000000000GAAQ\",\"IsPriceImpacting\":false,\"businessObjectType\":\"QuoteLineItemAttribute\",\"AttributeName\":\"Display_Size\",\"id\":\"0zuxx000000000GAAQ\",\"AttributeDefinitionCode\":null,\"SalesTransactionItemAttrParent\":\"0QLxx0000004C9VGAU\"}],\"PricebookEntry\":\"01uxx0000008yX0AAI\",\"DiscountAmount\":null,\"PricingTermCount\":0,\"SubscriptionTermUnit\":null,\"NetUnitPrice\":144.99,\"ItemEffectiveGrantDate\":null,\"ProductCategory\":null,\"SalesTransactionAction\":null,\"SalesTransactionActionType\":null,\"SalesTransactionItemGroup\":null,\"PeriodBoundaryDay\":null,\"SalesTrxnItemDescription\":null,\"LineItemDistributionType\":null,\"ProrationPolicy\":null,\"ContractDiscountType\":null,\"TransactionType\":null,\"ParentReference\":\"0Q0xx0000004C92CAE\",\"Discount\":null,\"PricingTermUnit\":null,\"ProductSellingModel\":\"0jPxx0000000001EAA\",\"PricingSource\":null,\"StockKeepingUnit\":null,\"PartnerUnitPrice\":130.491,\"ItemTotalAdjustmentAmount\":0,\"SalesTransactionItemSource\":\"0QLxx0000004C9VGAU\",\"ContractAttributePasId\":null,\"SubscriptionTerm\":null,\"SellingModelType\":\"OneTime\",\"EndQuantity\":12,\"NetTotalPrice\":1739.88,\"TotalLineAmount\":1739.88,\"ItemSegmentType\":null,\"ProductBasedOn\":\"11Bxx000002C1nqEAC\",\"Deleted\":false,\"BillingReference\":null,\"ArePartialPeriodsAllowed\":false,\"ItemRecordedPrice\":null,\"CustomProductName\":null,\"ItemSegmentIdentifier\":null,\"SalesTransactionItemParent\":\"0Q0xx0000004C92CAE\",\"Quantity\":12,\"PeriodBoundary\":null,\"ContractDiscountValue\":null,\"LineItemDiscountValue\":null,\"ContractId\":null,\"EndDate\":null,\"ItemGroupSummarySubtotal\":null,\"IsContracted\":false,\"UnitPrice\":144.99,\"StartQuantity\":null,\"ContractPrice\":null,\"TotalPrice\":1739.88,\"LineItemDiscountType\":null,\"ItemPath\":\"01txx0000006i2aAAA\",\"productKey\":[\"0QLxx0000004C9VGAU\"]}\",
  \"description\": \"This configuration is saved for reuse.\",
  \"name\": \"Favorite Configuration\",
  \"referenceRecordId\": \"01txx0000006iCFAAY\"
}
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `data` | String | JSON object that contains the details of the sales transaction, formatted as a string. | Small, 63.0 | 63.0 |
| `description` | String | Description of the saved configuration. | Small, 63.0 | 63.0 |
| `id` | String | ID of the saved configuration. | Small, 63.0 | 63.0 |
| `name` | String | Name of the saved configuration. | Small, 63.0 | 63.0 |
| `referenceRecord​Id` | String | ID of the record that the saved configuration belongs to. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_get_configuration_instance_output.htm ===
---
page_id: connect_responses_get_configuration_instance_output.htm
title: Configuration Get Instance
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_get_configuration_instance_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Get Instance

Output representation of the request to retrieve the configuration instance.

      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |
| `transaction` | Map<String, Object> | Transaction JSON payload representing an object in an external system that’s used to create a session. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_load_configuration_instance_output.htm ===
---
page_id: connect_responses_load_configuration_instance_output.htm
title: Configuration Load Instance
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_load_configuration_instance_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Load Instance

Output representation of the details of the context or session that are returned with a
    load configuration request.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "contextId": "831f07b01cf0cbd2d046adf5350420f85f0611b4b1e22e183921a063857a1377",
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, <[Configurator Message](./connect_responses_configurator_message_output.htm.md)>> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engines (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `contextId` | String | ID of the transaction context. | Small, 60.0 | 60.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the execution results from qualification rules. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_message_rules_output.htm ===
---
page_id: connect_responses_message_rules_output.htm
title: Message Rules
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_message_rules_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: connect_responses_config_rule_output.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Message Rules

Output representation of the details of the message rules.

        
          

**JSON example**

          
: 
            

```
{
  "message": "Constraints is running for laptop",
  "messageType": "Info",
  "primaryRecordId": "0QLxx0000004CU0GAM",
  "relatedRecordId": "0QLxx0000004CU1GAM"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | List of message strings to display to the user. | Small, 67.0 | 67.0 |
| `messageType` | String | Severity level of the message. Valid values are: `INFO` `WARNING` `ERROR` | Small, 67.0 | 67.0 |
| `primaryRecordId` | String | ID of the primary sales transaction item record. | Small, 67.0 | 67.0 |
| `relatedRecordId` | String | ID of the related record. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_recommendation_rules_output.htm ===
---
page_id: connect_responses_product_recommendation_rules_output.htm
title: Product Recommendation Rules
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_recommendation_rules_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: connect_responses_config_rule_output.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Recommendation Rules

Output representation of the details of the product recommendation rules.

        
          

**JSON example**

          
: 
            

```
{
  "productRecommendationRules": [
    {
      "message": "32GB RDIMM recommends 16GB RDIMM",
      "productIds": [
        "01tVW000003l7uaYAA"
      ],
      "recordType": "Type",
      "referenceId": "0Q0VW000000z8yN0AQ"
    },
    {
      "message": "32GB RDIMM recommends 64GB RDIMM",
      "productIds": [
        "01tVW000003l7v6YAA"
      ],
      "recordType": "Type",
      "referenceId": "0Q0VW000000z8yN0AQ"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | Message to display with the product recommendation. | Small, 67.0 | 67.0 |
| `productIds` | String[] | List of recommended Product IDs. | Small, 67.0 | 67.0 |
| `recordType` | String | Record type associated with the recommendation. | Small, 67.0 | 67.0 |
| `referenceId` | String | Reference ID of the product recommendation rule. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_save_configuration_instance_output.htm ===
---
page_id: connect_responses_save_configuration_instance_output.htm
title: Configuration Save Instance
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_save_configuration_instance_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Save Instance

Output representation of the response that’s returned with a save configuration
    request.

      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_set_configuration_instance_output.htm ===
---
page_id: connect_responses_set_configuration_instance_output.htm
title: Configuration Set Instance
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_set_configuration_instance_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Set Instance

Output representation of the details of the context or session that are returned with a
    set configuration request.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "contextId": "831f07b01cf0cbd2d046adf5350420f85f0611b4b1e22e183921a063857a1377",
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, <[Configurator Message](./connect_responses_configurator_message_output.htm.md)>> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engines (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `context​Id` | String | ID of the transaction context. | Small, 60.0 | 60.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the execution results from qualification rules. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_set_product_quantity_configurator_output.htm ===
---
page_id: connect_responses_set_product_quantity_configurator_output.htm
title: Product Quantity Set Configurator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_set_product_quantity_configurator_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Quantity Set Configurator

Output representation of the request details to set product quantity.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, [Configurator Message](./connect_responses_configurator_message_output.htm.md)> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engines (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the qualification rule execution results. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_update_favorite_output.htm ===
---
page_id: connect_responses_update_favorite_output.htm
title: Configuration Update
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_update_favorite_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Update

Output representation of the details of the updated configuration.

        
          

**JSON example**

          
: This example shows a sample when the update operation is successful.

          
: 
            

```
{
  "errors": [],
  "success": true
}
```

          

          
: This example shows a sample when the update operation has errors.

          
: 
            

```
{
  "errors": [
    {
      "code": "INTERNAL_SERVER_ERROR",
      "message": "INVALID_REFERENCEOBJECTID"
    }
  ],
  "success": false
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](./connect_responses_configuration_list_error_response.htm.md) | List of errors that contains a message and an error code. | Small, 63.0 | 63.0 |
| `success` | Boolean | Indicates whether the update operation is successful (`true`) or not (`false`) | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_update_nodes_configurator_output.htm ===
---
page_id: connect_responses_update_nodes_configurator_output.htm
title: Configurator Update Nodes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_update_nodes_configurator_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Update Nodes

Output representation of the configuration request details to update nodes.

      
        
          

**JSON Example**

          
: 
            

```
{
  "configuratorMessages": {},
  "configuratorUITreatments": [
    {
      "details": {
        "attributeId": "0tjxx0000000007AAA",
        "prcId": "0dSxx0000000007EAA",
        "stiId": "0QLxx0000004CU0GAM",
        "attributePicklistValueId": "0v6xx0000000005AAA"
      },
      "uiTreatmentScope": "Bundle",
      "uiTreatmentTarget": "Attribute_Picklist_Value",
      "uiTreatmentType": "Hide"
    },
    {
      "details": {
        "stiId": "ref_f0f2da7b_c431_482d_bf4b_599052f3a2e1"
      },
      "uiTreatmentScope": "Product",
      "uiTreatmentTarget": "Component",
      "uiTreatmentType": "Disable"
    }
  ],
  "errors": [],
  "productQualifications": {
    "01tDU000000EOTCYA4": {
      "isQualified": true
    }
  },
  "success": true
}
```

          

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `configurator​Messages` | Map<String, [Configurator Message](./connect_responses_configurator_message_output.htm.md)> | Map of the product IDs to the list of configurator messages. Configurator messages are results from any validations, Business Rules Engines (BRE) calls, or Salesforce Pricing calls. | Small, 60.0 | 60.0 |
| `configurator​UITreatments` | [Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)[] | Details of the UI treatments that specify the product configuration rule actions to override the disable or hide behavior in the UI for product options, product attributes, and attribute picklist values. | Small, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors, which contains an error code and a message. | Small, 60.0 | 60.0 |
| `product​Qualifications` | Map<String, [Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)> | Map of the product IDs to the qualification rule execution results. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the call was successful (`true`) not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_visibility_rules_output.htm ===
---
page_id: connect_responses_visibility_rules_output.htm
title: Visibility Rules
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_visibility_rules_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: connect_responses_config_rule_output.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Visibility Rules

Output representation of the details of the visibility rules.

        
          

**JSON example**

          
: 
            

```
{
  "visibilityRules": [
    {
      "message": "128GB LRDIMM disables 16GB RDIMM",
      "productIds": [
        "01tVW000003l7uaYAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "Additional API disables Additional API Gov",
      "productIds": [
        "01tVW000003l7tzYAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "Disable All other API Products",
      "productIds": [
        "01tVW000003l7u0YAA",
        "01tVW000003l7u1YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "32GB RDIMM disables 128GB LRDIMM",
      "productIds": [
        "01tVW000003l7v5YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    },
    {
      "message": "API Access Requests AEH disables Additional API Prod",
      "productIds": [
        "01tVW000003l7u1YAA"
      ],
      "scope": "virtual",
      "target": "product",
      "type": "disable"
    }
  ]
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
| `attributeId` | String | ID of the attribute associated with this visibility rule. | Small, 67.0 | 67.0 |
| `attribute​Picklist​ValueId` | String | ID of the attribute picklist value associated with this visibility rule. | Small, 67.0 | 67.0 |
| `message` | String | Message to display when the visibility rule is applied. | Small, 67.0 | 67.0 |
| `prcId` | String | ID of the Product Relationship Configuration (PRC) associated with this visibility rule. | Small, 67.0 | 67.0 |
| `productIds` | String[] | List of product IDs affected by this visibility rule. | Small, 67.0 | 67.0 |
| `scope` | String | Scope of the visibility rule. Valid values are: `PRODUCT` `BUNDLE` `VIRTUAL` | Small, 67.0 | 67.0 |
| `stiId` | String | ID of the sales transaction item associated with this visibility rule. | Small, 67.0 | 67.0 |
| `target` | String | Target of the visibility rule. Valid values are: `COMPONENT` `QUANTITY` `ATTRIBUTE` `ATTRIBUTE_PICKLIST_VALUE` `PRODUCT` | Small, 67.0 | 67.0 |
| `type` | String | Type of visibility rule. Valid values are: `HIDE` `DISABLE` | Small, 67.0 | 67.0 |

=== ARTICLE: meta_productconfiguratorsettings.htm ===
---
page_id: meta_productconfiguratorsettings.htm
title: ProductConfiguratorSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productconfiguratorsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductConfiguratorSettings

Represents the settings for Product
			Configurator.

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

ProductConfiguratorSettings values are stored in the
					ProductConfiguratorSettings.settings file in the
					settings folder. The .settings files
				are different from other named components, because there is only one settings file
				for each settings component.

	

	

## Version

		
		

ProductConfiguratorSettings components are available in API version 60.0 and later.

	

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| enableProductConfigurator | **Field Type** boolean **Description** Indicates whether to enable Product Configurator at run time to customize product components and attributes during the sales process (`true`) or not (`false`). The default value is `false`. |

	

		

## Declarative Metadata Sample Definition

		
			

Here's an example of a ProductConfiguratorSettings component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<ProductConfiguratorSettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <enableProductConfigurator>true</enableProductConfigurator>
</ProductConfiguratorSettings>
```

			

Here's an example `package.xml` that references the
				previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>ProductConfigurator</members>
        <name>Settings</name>
    </types>
    <version>68.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

The wildcard character `*` (asterisk) in the
					package.xml manifest file doesn’t apply to metadata types
				for feature settings. The wildcard applies only when retrieving all settings, not
				for an individual setting. For details, see [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm). For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: prod_config_overview.htm ===
---
page_id: prod_config_overview.htm
title: Product Configurator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/prod_config_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configurator

Customize the components and attributes of a product to align with specific business
  requirements.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Management where Product Configurator is enabled |

  

 

- 
**[Product Configurator Standard Objects](./prod_config_std_objects_parent.htm.md)**  

The Product Configurator data model provides objects and fields to manage the product   configurator flow.

- 
**[Product Configurator Business APIs](./product_configurator_business_api_overview.htm.md)**  

Use the Product Configurator Business APIs to customize a product or a service     according to your business-specific requirements.

- 
**[Product Configurator Standard Invocable Actions](./product_configurator_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Product     Configurator.

- 
**[Product Configurator Metadata API Types](./product_configurator_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Constraint Modeling Language](./cml_what_is_constraint_modeling_language.htm.md)**  

Constraint Modeling Language (CML) is a domain-specific language that defines models     for complex systems. For product configuration, constraint models describe real-world entities     and their relationships to each other.

=== ARTICLE: prod_config_std_objects_parent.htm ===
---
page_id: prod_config_std_objects_parent.htm
title: Product Configurator Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/prod_config_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configurator Standard Objects

The Product Configurator data model provides objects and fields to manage the product
  configurator flow.

- 
**[ExpressionSetConstraintObj](./sforce_api_objects_expressionsetconstraintobj.htm.md)**  

       Represents the association between a Product object and the constraint model          tags defined in a given constraint model. This object is available in API version 63.0       and later. 

- 
**[ProductConfigurationFlow](./sforce_api_objects_productconfigurationflow.htm.md)**  

       Specifies the many-to-many relationship between Product Classification,          Product, and Flow Definition objects. The flow definition is used to configure standalone          and bundled products of a specific product classification along with the product          attributes, quantities, and product selling models. This object is available in API       version 60.0 and later. 

- 
**[ProductConfigFlowAssignment](./sforce_api_objects_productconfigflowassignment.htm.md)**  

       A junction object that represents the many-to-many relationship between          Product Configuration Flow, Product, and Product Classification. This object is       available in API version 60.0 and later. 

- 
**[ProductConfigurationRule](./sforce_api_objects_productconfigurationrule.htm.md)**  

       Represents the validation, inclusion, and exclusion rules for products in the          context of the selling process. The selling process can be quoting, configuration, or          ordering. This object is available in API version 61.0 and later. 

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: product_configurator_business_api_overview.htm ===
---
page_id: product_configurator_business_api_overview.htm
title: Product Configurator Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_business_api_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configurator Business APIs

Use the Product Configurator Business APIs to customize a product or a service
    according to your business-specific requirements.

    
      

Perform product configuration-related operations by using the Product Configurator Business
        APIs. Integrate these APIs with any front-end application to access the configurator
        capabilities.

      

These APIs are stateless and don't recall prior user actions between calls unless state is
        explicitly persisted and reloaded.

      

For example, if a user deselects a child product and later reselects it, the engine treats
        the request as adding a new item that doesn't currently exist in the model. It can’t infer
        that this request is a re-selection of a previously removed item. As a result, the original
        line item isn't restored and a new line item is created.

      

This table lists the available Product Configurator resources.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
            
            
            
          

        
| Resource | Description |
| --- | --- |
| [`/connect/cpq/configurator/actions/configure`](./connect_resources_product_configurator_configure.htm.md) (POST) | Retrieve and update a product’s configuration from a configurator. Execute configuration rules and notify users of any violations for changes to product bundle, attributes, or product quantity within a bundle. Additionally, get pricing details for the configured bundle. |
| [`/connect/cpq/configurator/actions/load-instance`](./connect_resources_load_configurator_instance.htm.md) (POST) | Create a session for the product configuration instance using the transaction ID. Get the session ID that includes the results of actions, such as configuration rules, qualification rules, and pricing management. |
| [`/connect/cpq/configurator/actions/set-instance`](./connect_resources_set_configurator_instance.htm.md) (POST) | Set a product configuration instance. This API is used in scenarios where the configuration instance is available in a different database than Salesforce and the product catalog management data is in Salesforce. |
| [`/connect/cpq/configurator/actions/get-instance`](./connect_resources_get_configurator_instance.htm.md) (POST) | Fetch the JSON representation of a product configuration. Use the response to display the details of the product configuration instance on the Salesforce user interface, or save the product configuration instance to an external system. |
| [`/connect/cpq/configurator/actions/save-instance`](./connect_resources_save_configuration_instance.htm.md) (POST) | Save a configuration instance after a successful product configuration. |
| [`/connect/cpq/configurator/actions/set-product-quantity`](./connect_resources_set_product_quantity.htm.md) (POST) | Set the quantity of a product through the runtime system. |
| [`/connect/cpq/configurator/actions/add-nodes`](./connect_resources_add_nodes.htm.md) (POST) | Add a node to the context through the runtime system without using the Salesforce user interface. |
| [`/connect/cpq/configurator/actions/update-nodes`](./connect_resources_update_nodes.htm.md) (POST) | Update nodes in a product configuration. |
| [`/connect/cpq/configurator/actions/delete-nodes`](./connect_resources_delete_nodes.htm.md) (POST) | Delete nodes from a product configuration. |
| [`/revenue/product-configurator/rules/actions/execute`](./connect_resources_config_rules.htm.md) (POST) | Run rules for a specific quote or order based on a context ID or transaction ID. |

    

  

- 
**[Resources](./product_configurator_business_apis_resources.htm.md)**  

Learn more about the available Product Configurator API resources.

- 
**[Request Bodies](./product_configurator_business_apis_requests.htm.md)**  

Learn more about the available Product Configurator API request bodies.

- 
**[Response Bodies](./product_configurator_business_apis_responses.htm.md)**  

Learn more about the available Product Configurator API response bodies.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

- [*Salesforce Help*: Product Configurator Permissions](https://help.salesforce.com/s/articleView?id=ind.product_configurator_product_configurator_permissions.htm&type=5&language=en_US)

=== ARTICLE: product_configurator_business_apis_requests.htm ===
---
page_id: product_configurator_business_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_business_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available Product Configurator API request bodies.

- 
**[Configuration Get Instance Input](./connect_requests_get_configuration_instance_input.htm.md)**  

Input representation of the request to get a product configuration instance.

- 
**[Configuration Load Instance Input](./connect_requests_load_configuration_instance_input.htm.md)**  

Input representation of the request to load a product configuration             instance.

- 
**[Configuration Save Input](./connect_requests_favorite_input.htm.md)**  

Input representation of the details to save a configuration.

- 
**[Configuration Update Input](./connect_requests_update_favorite_input.htm.md)**  

Input representation of the details to update a configuration.

- 
**[Configuration Save Instance Input](./connect_requests_save_configuration_instance_input.htm.md)**  

Input representation of the request to save a product configuration instance.

- 
**[Configuration Set Instance Input](./connect_requests_set_configuration_instance_input.htm.md)**  

Input representation of the request to set a product configuration instance.

- 
**[Configurator Add Nodes Input](./connect_requests_add_nodes_configurator_input.htm.md)**  

Input representation of the request to add nodes within a root node.

- 
**[Configurator Added Node Input](./connect_requests_configurator_added_node_input.htm.md)**  

Input representation of the nodes to be added to a product configuration.

- 
**[Configurator Delete Nodes Input](./connect_requests_delete_nodes_configurator_input.htm.md)**  

Input representation of the request to delete nodes from a product         configuration.

- 
**[Configurator Deleted Node Input](./connect_requests_configurator_deleted_node_input.htm.md)**  

Input representation of the nodes to be deleted from a product configuration.

- 
**[Configurator Input](./connect_requests_configurator_input.htm.md)**  

Input representation of the request to modify the product configuration.

- 
**[Configurator Options Input](./connect_requests_configurator_options_input.htm.md)**  

Input representation of the request to get the product configuration options that’s     passed to the configurator.

- 
**[Configuration Rule Input](./connect_requests_config_rule_input.htm.md)**  

Input representation of the details of a configuration rule.

- 
**[Configurator Update Nodes Input](./connect_requests_update_nodes_configurator_input.htm.md)**  

Input representation of the request to update the nodes in a product         configuration.

- 
**[Configurator Updated Node Input](./connect_requests_configurator_updated_node_input.htm.md)**  

Input representation of the nodes to be updated in a product configuration.

- 
**[Product Quantity Set Configurator Input](./connect_requests_set_product_quantity_configurator_input.htm.md)**  

Input representation of the request to set the quantity of a product.

- 
**[User Context Input](./connect_requests_configurator_user_context_input.htm.md)**  

Input representation of the request to get the context details of a user, which are     used for qualification rules.

=== ARTICLE: product_configurator_business_apis_resources.htm ===
---
page_id: product_configurator_business_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_business_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Product Configurator API resources.

- 
**[Configuration (POST)](./connect_resources_product_configurator_configure.htm.md)**  

Retrieve and update a product’s configuration from a configurator.       Execute configuration rules and notify users of any violations for changes to product bundle,       attributes, or product quantity within a bundle. Additionally, get pricing details for the       configured bundle.

- 
**[Saved Configuration (GET, POST)](./connect_resources_save_product_configurations.htm.md)**  

Save and reuse a record's configurations, and get a list of the saved configurations     for a record.

- 
**[Saved Configuration (DELETE, PUT)](./connect_resources_saved_configuration.htm.md)**  

Update or delete a record's saved configuration by using the configuration     ID.

- 
**[Configuration Get Instance (POST)](./connect_resources_get_configurator_instance.htm.md)**  

Fetch the JSON representation of a product configuration. Use the       response to display the details of the product configuration instance on the Salesforce user       interface, or save the product configuration instance to an external system.

- 
**[Configuration Load Instance (POST)](./connect_resources_load_configurator_instance.htm.md)**  

Create a session for the product configuration instance using the       transaction ID. Get the session ID that includes the results of actions, such as configuration       rules, qualification rules, and pricing management.

- 
**[Configuration Save Instance (POST)](./connect_resources_save_configuration_instance.htm.md)**  

Save a configuration instance after a successful product       configuration.

- 
**[Configuration Set Instance (POST)](./connect_resources_set_configurator_instance.htm.md)**  

Set a product configuration instance. This API is used in scenarios       where the configuration instance is available in a different database than Salesforce and the       product catalog management data is in Salesforce.

- 
**[Configurator Add Nodes (POST)](./connect_resources_add_nodes.htm.md)**  

Add a node to the context through the runtime system without using       the Salesforce user interface.

- 
**[Configurator Delete Nodes (POST)](./connect_resources_delete_nodes.htm.md)**  

Delete nodes from a product configuration.

- 
**[Configurator Update Nodes (POST)](./connect_resources_update_nodes.htm.md)**  

Update nodes in a product configuration.

- 
**[Product Set Quantity (POST)](./connect_resources_set_product_quantity.htm.md)**  

Set the quantity of a product through the runtime     system.

- 
**[Config Rules (POST)](./connect_resources_config_rules.htm.md)**  

Run rules for a specific quote or order based on a context ID or       transaction ID.

=== ARTICLE: product_configurator_business_apis_responses.htm ===
---
page_id: product_configurator_business_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_business_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available Product Configurator API response bodies.

- 
**[Configuration Details](./connect_responses_configurator_output.htm.md)**  

Output representation of the product configuration details.

- 
**[Configuration Get Instance](./connect_responses_get_configuration_instance_output.htm.md)**  

Output representation of the request to retrieve the configuration instance.

- 
**[Configuration Load Instance](./connect_responses_load_configuration_instance_output.htm.md)**  

Output representation of the details of the context or session that are returned with a     load configuration request.

- 
**[Configuration Save Details](./connect_responses_favorite_output_represenation.htm.md)**  

Output representation of the details of a saved configuration.

- 
**[Configuration Record Save](./connect_responses_create_favorite_output.htm.md)**  

Output representation of the details of a saved configuration.

- 
**[Configuration List](./connect_responses_favorite_list_output_represenation.htm.md)**  

Output representation of the details of the saved configuration.

- 
**[Configuration Save Instance](./connect_responses_save_configuration_instance_output.htm.md)**  

Output representation of the response that’s returned with a save configuration     request.

- 
**[Configuration Set Instance](./connect_responses_set_configuration_instance_output.htm.md)**  

Output representation of the details of the context or session that are returned with a     set configuration request.

- 
**[Configurator Add Nodes](./connect_responses_add_nodes_configurator_output.htm.md)**  

Output representation of the configuration request details to add nodes.

- 
**[Configurator Additional Fields](./connect_responses_configurator_additional_fields_output.htm.md)**  

Output representation of the additional fields of a product configuration.

- 
**[Configurator Attribute](./connect_responses_configurator_attribute_output.htm.md)**  

Output representation of the attribute in a product configuration.

- 
**[Configurator Attribute Category](./connect_responses_configurator_attribute_category_output.htm.md)**  

Output representation of the attribute category in a product configuration.

- 
**[Configurator Attribute Picklist](./connect_responses_configurator_attribute_picklist_output.htm.md)**  

Output representation of the attribute picklist in a product configuration.

- 
**[Configurator Attribute Picklist Value](./connect_responses_configurator_attribute_picklist_value_output.htm.md)**  

Output representation of the values of an attribute picklist in a product     configuration.

- 
**[Configurator Delete Nodes](./connect_responses_delete_nodes_configurator_output.htm.md)**  

Output representation of the details of the configuration request to delete     nodes.

- 
**[Configurator Message](./connect_responses_configurator_message_output.htm.md)**  

Output representation of the messages of a product configurator.

- 
**[Configurator Price](./connect_responses_configurator_price_output.htm.md)**  

Output representation of the pricing details in a product configuration.

- 
**[Configurator Pricing Model](./connect_responses_configurator_pricing_model_output.htm.md)**  

Output representation of the details of a pricing model in a product     configuration.

- 
**[Configurator Product Catalog](./connect_responses_configurator_product_catalog_output.htm.md)**  

Output representation of the product catalog.

- 
**[Configurator Product Classification](./connect_responses_configurator_product_classification_output.htm.md)**  

Output representation of the product classification in a product     configuration.

- 
**[Configurator Product Component Group](./connect_responses_configurator_product_component_group_output.htm.md)**  

Output representation of the product component group in a product     classification.

- 
**[Configurator Product Recommendations](./connect_responses_configurator_product_recommendation_output.htm.md)**  

Output representation of the details of the product recommendations.

- 
**[Configurator Product Related Component](./connect_responses_configurator_product_related_component_output.htm.md)**  

Output representation of the product related component in a product     configuration.

- 
**[Configurator Product Selling Model](./connect_responses_configurator_product_selling_model_output.htm.md)**  

Output representation of the product selling model in a product     configuration.

- 
**[Configurator Product Selling Model Option](./connect_responses_configurator_product_selling_model_option_output.htm.md)**  

Output representation of the product selling model option in a product     configuration.

- 
**[Configurator Qualification Context](./connect_responses_configurator_qualification_context_output.htm.md)**  

Output representation of the qualification context in a product     configuration.

- 
**[Configurator UI Treatment](./connect_responses_configurator_u_i_treatment_output.htm.md)**  

Output representation of the details of the UI treatments of a product configurator. The     details include the product configuration rule actions to override the disable or hide behavior     in the UI for product options, product attributes, and attribute picklist values.

- 
**[Configurator Unit Of Measure](./connect_responses_configurator_unit_of_measure_output.htm.md)**  

Output representation of the details of the unit of measure record.

- 
**[Configurator Update Nodes](./connect_responses_update_nodes_configurator_output.htm.md)**  

Output representation of the configuration request details to update nodes.

- 
**[Configuration Update](./connect_responses_update_favorite_output.htm.md)**  

Output representation of the details of the updated configuration.

- 
**[Error Response](./connect_responses_configuration_list_error_response.htm.md)**  

Output representation of the details of the error.

- 
**[Product Quantity Set Configurator](./connect_responses_set_product_quantity_configurator_output.htm.md)**  

Output representation of the request details to set product quantity.

- 
**[Configuration Rule Response](./connect_responses_config_rule_output.htm.md)**  

Output representation of the details of the configuration rule response.

=== ARTICLE: product_configurator_flow_metadata_api.htm ===
---
page_id: product_configurator_flow_metadata_api.htm
title: Flow for Product Configurator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: product_configurator_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Product Configurator

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Product Configurator exposes additional actionType values for the FlowActionCall Metadata
        type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Product Configurator include: `runConfigRules`—Run rules for a specific quote or order based on a context ID or transaction ID, and process other steps that are part of the configuration directly within a Flow. This action decouples rule execution from configurations to enable independent execution of rules and for easier retrieval of responses. |

=== ARTICLE: product_configurator_invocable_actions_parent.htm ===
---
page_id: product_configurator_invocable_actions_parent.htm
title: Product Configurator Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configurator Standard Invocable Actions

Learn more about the standard invocable actions available with Product
    Configurator.

- 
**[Run Config Rules Action](./actions_obj_run_config_rules.htm.md)**  

Run rules for a specific quote or order based on a context ID or             transaction ID, and process other steps that are part of the configuration directly             within a Flow. This action decouples rule execution from configurations to enable             independent execution of rules and for easier retrieval of responses.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

=== ARTICLE: product_configurator_metadata_api_parent.htm ===
---
page_id: product_configurator_metadata_api_parent.htm
title: Product Configurator Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configurator Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Product Configurator](./product_configurator_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

- 
**[ProductConfiguratorSettings](./meta_productconfiguratorsettings.htm.md)**  

Represents the settings for Product 			Configurator.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: sforce_api_objects_expressionsetconstraintobj.htm ===
---
page_id: sforce_api_objects_expressionsetconstraintobj.htm
title: ExpressionSetConstraintObj
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_expressionsetconstraintobj.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExpressionSetConstraintObj

      Represents the association between a Product object and the constraint model
         tags defined in a given constraint model. This object is available in API version 63.0
      and later. 

      

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

         
         

This object is available in orgs where Revenue Cloud is enabled.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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

                  

            

            
| Field | Details |
| --- | --- |
| ConstraintModelTag | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The product tag that is defined in the constraint model, for example, `Laptop`. |
| ConstraintModelTagType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of the product tag that is defined in the constraint model. Possible values are: `Port` `Type` The default value is `Type`. |
| ExpressionSetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The expression set associated with the expression set constraint object. This field is a relationship field. **Relationship Name** ExpressionSet **Refers To** ExpressionSet |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, the user accessed this record or list view (LastReferencedDate) but didn’t view it. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the expression set constraint. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** For internal use only. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ReferenceObjectId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The object associated with the expression set constraint object. This field is a polymorphic relationship field. **Relationship Name** ReferenceObject **Refers To** Product2, ProductClassification, ProductRelatedComponent |

=== ARTICLE: sforce_api_objects_productconfigflowassignment.htm ===
---
page_id: sforce_api_objects_productconfigflowassignment.htm
title: ProductConfigFlowAssignment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productconfigflowassignment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductConfigFlowAssignment

      A junction object that represents the many-to-many relationship between
         Product Configuration Flow, Product, and Product Classification. This object is
      available in API version 60.0 and later. 

      

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

: 

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
| AssignmentType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the Product Configuration Flow is assigned to the primary product or classification, or to dynamic components added within a bundle. Valid values are: `DynamicAdditionFlow` `PrimaryConfiguratorFlow` The default value is `PrimaryConfiguratorFlow`. Available in API version 65.0 and later. |
| ProductClassificationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product classification associated with the Product Configuration Flow. This field is a relationship field. **Relationship Name** ProductClassification **Relationship Type** Lookup **Refers To** ProductClassification |
| ProductConfigurationFlowId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The Product Configuration Flow associated with the Product Classification or Product. This field is a relationship field. **Relationship Name** ProductConfigurationFlow **Relationship Type** Lookup **Refers To** ProductConfigurationFlow |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product associated with the Product Configuration Flow. This field is a relationship field. **Relationship Name** Product **Relationship Type** Lookup **Refers To** Product2 |

=== ARTICLE: sforce_api_objects_productconfigurationflow.htm ===
---
page_id: sforce_api_objects_productconfigurationflow.htm
title: ProductConfigurationFlow
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productconfigurationflow.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductConfigurationFlow

      Specifies the many-to-many relationship between Product Classification,
         Product, and Flow Definition objects. The flow definition is used to configure standalone
         and bundled products of a specific product classification along with the product
         attributes, quantities, and product selling models. This object is available in API
      version 60.0 and later. 

      

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
- 
- 
- 

: 

                  

            

            
| Field | Details |
| --- | --- |
| FlowIdentifier | **Type** String **Properties** Create, Filter, Group, Sort, Update **Description** Stores the flow API name. |
| IsDefault | **Type** Boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates the default configurator flow. The default value is `false`. |
| IsRequestDetailEditable | **Type** Boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether request attributes and products can be edited (`true`) or not (`false`). When enabled, users can modify the attributes and products in associated cases, incidents, or service requests after the request is created. The default value is `false`. |
| Status | **Type** Picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Indicates the status of the product configuration flow. Possible values include Draft, Active, and Inactive Possible values are: `Active` `Draft` `Inactive` The default value is `Draft`. |

=== ARTICLE: sforce_api_objects_productconfigurationrule.htm ===
---
page_id: sforce_api_objects_productconfigurationrule.htm
title: ProductConfigurationRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productconfigurationrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Configurator
parent_page: prod_config_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductConfigurationRule

      Represents the validation, inclusion, and exclusion rules for products in the
         context of the selling process. The selling process can be quoting, configuration, or
         ordering. This object is available in API version 61.0 and later. 

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** |
| ConfigurationRuleDefinition | **Type** textarea **Properties** Create, Nillable, Update **Description** The configuration rule criteria and actions. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the configuration rule. |
| EffectiveFromDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time from which the configuration rules comes into effect. |
| EffectiveToDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time to which the configuration rules ceases to be in effect. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the configuration rule record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the configuration rule record was last viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the configuration rule. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the configuraion rule owner. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProcessScope | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The scope of the configuration rule. Possible values are: `Bundle` `Product` The default value is `Product`. |
| RuleSubType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The segregation of products into subsets such that the configuration rules only apply to the products that fall under the ambit of the selected rule subtype. Possible values are: `BundleProduct` `BundleProductClassification` `Product` `ProductClassification` The default value is `Product`. |
| RuleType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Indicates the industry vertical or the feature of the industry vertical that’s using the configuration rule. Possible values are: `Configurator` `Promotions` The default value is `Configurator`. |
| Sequence | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** Indicates the order for executing the configuration rule. Rules with lower numbers run first when multiple rules are triggered at once. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The lifecycle status of the configuration rule. Possible values are: `Active` `Draft` `Inactive` The default value is `Draft`. |

