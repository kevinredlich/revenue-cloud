# Revenue Management Developer Guide 264 — sección: Dynamic Revenue Orchestrator (58 artículos)

=== ARTICLE: actions_obj_decompose_sales_transaction.htm ===
---
page_id: actions_obj_decompose_sales_transaction.htm
title: Decompose Sales Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_decompose_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decompose Sales Transaction Action

Decompose a sales transaction, such as a quote, order, or
            order summary.

        
            

Specify the ID of the sales transaction to decompose. The decomposition process
                includes these steps.

            
                
- Intake process

                
- Sales transaction decomposition

            

            

The intake process occurs synchronously or asynchronously, as specified with the
                    intakeRequestType input parameter. You can also specify the
                decomposition priority using the fulfillmentPriority
                parameter.

            

This action executes only the decomposition process and stops before orchestration.
                You can execute custom logic in between the decomposition and orchestration
                processes.

            

This action is available in API version 68.0 and later.

        

        

## Special Access
                Rules

            
            

The Decompose Sales Transaction action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required permissions](https://help.salesforce.com/s/articleView?id=sf.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&language=en_US) to access and call
                this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v66.0/actions/standard/decomposeSalesTransaction`

                
                
                    

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

- 
- 

                        

                        
                            

                            

: 

: 

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

- 
- 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| allowOverride​OfPointOfNoReturn | **Type** boolean **Description** Indicates whether to override the point of no return setting for the fulfillment step (`true`) or not (`false`). The default value is `false`. |
| fulfillmentAdapter | **Type** string **Description** Required.Type of fulfillment adapter. Valid values are: `StandardOrder` `GenericAdapter` |
| fulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| hydratedContextId | **Type** string **Description** ID of the hydrated context. |
| intakeRequestType | **Type** string **Description** Type of request to process the intake. Valid values are: `Synchronous` `Asynchronous` |
| priorityLimit​Action | **Type** string **Description** Type of action to perform when the priority limit is reached. Valid values are: `Reject` `Downgrade` This parameter is applicable only when you specify the fulfillmentPriority parameter. |
| sales​TransactionId | **Type** id **Description** Required. ID of the sales transaction to submit. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code that corresponds to the type of error encountered. |
| requested​FulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| requestId | **Type** string **Description** Request ID of the invocation. |
| resolved​FulfillmentPriority | **Type** string **Description** Resolved priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| submitStatus | **Type** string **Description** Submission status of the sales transaction for decomposition. Valid values are: `Success` `Error` `Submitted` `Rejected` |
| usedContextId | **Type** string **Description** ID of the used context that updates the decomposition process. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Decompose Sales Transaction action.

                        

```
{
  "inputs": [
    {
      "fulfillmentAdapter": "StandardOrder",
      "intakeRequestType": "Synchronous",
      "salesTransactionId": "801xx000003GYexAAG"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Decompose Sales Transaction action.

                        

```
[
  {
    "actionName": "decomposeSalesTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "requestId": "ee3ded2e-fe43-401b-a54d-9124d48a0b72",
      "requestedFulfillmentPriority": "Default",
      "submitStatus": "SUCCESS",
      "usedContextId": "0000000s21to18g0009176412796953180a8259def914e1abbd863dde076b71f",
      "resolvedFulfillmentPriority": "Default"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_freeze_sales_transaction.htm ===
---
page_id: actions_obj_freeze_sales_transaction.htm
title: Freeze Sales Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_freeze_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Freeze Sales Transaction Action

Freeze a sales transaction to disable the modification of a line
            item.

        
            

A line item can reach a milestone in the fulfillment
                process, which is known as a point of no return, where the line item can’t accept
                modifications. Get details about the point of no return for each line item of a
                sales transaction.

            

This action is available in API version 64.0 and later.

        

        

## Special Access Rules

The Freeze Sales Transaction action is available in Enterprise, Unlimited, and Developer Editions
                of Revenue Cloud. See the [required permissions](https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&language=en_US) to access and call
                this invocable action.

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/freezeSalesTransaction`

                
                
                    

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
| salesTransactionId | **Type** id **Description** Required. ID of the sales transaction that's submitted to the Dynamic Revenue Orchestrator. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code indicating the type of error. |
| orchestration​PlanId | **Type** id **Description** ID of the created orchestration plan. |
| planState | **Type** string **Description** Status of the created orchestration plan. Valid values are: `FAILURE` `NOTSTARTED` `PENDING` `COMPLETED` `FROZEN` `INPROGRESS` |
| pointOf​NoReturn​DetailFor​LineItems​List | **Type** string **Description** Collection of sales transaction line items, where each item includes a boolean value indicating whether it has reached the point of no return. |
| requestId | **Type** string **Description** ID of the request to get the point of no return details. |
| salesTransaction​Id | **Type** string **Description** ID of the sales transaction that's submitted to the Dynamic Revenue Orchestrator. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Freeze Sales Transaction action.

                        

```
{
    "inputs": [
        {
            "salesTransactionId": "801SG00000jQO1ZYAW"
        }
    ]
}
```

                    

                    
: 
                        

This sample response is for the Freeze Sales Transaction action.

                        

```
[
  {
    "actionName": "freezeSalesTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "salesTransactionId": "801SG00000jQO1ZYAW",
      "orchestrationPlanId": "13VSG00000229Z72AI",
      "requestId": "452789a6-f2ab-4079-8aca-a11dbfef6a45",
      "pointOfNoReturnDetailForLineItemsList": "802SG000007D0B4YAK\": {\namendAllowed: false,\nanyChangesAllowed: true,\ncancelAllowed: false\n}, \n802SG000007D0B3YAK\": {\namendAllowed: false,\nanyChangesAllowed: true,\ncancelAllowed: false\n}",
      "planState": "Frozen"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_get_point_of_no_return.htm ===
---
page_id: actions_obj_get_point_of_no_return.htm
title: Get Point Of No Return Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_point_of_no_return.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Point Of No Return Action

Get details about the point of no return milestone for each line
            item in a sales transaction.

        

A line item can reach a milestone in the fulfillment
                process, which is known as a point of no return, where the line item can’t accept
                modifications. Get details about the point of no return for each line item of a
                sales transaction.

This action is available in API version 64.0 and later.

        

## Special Access Rules

            
            

The Get Point Of No Return action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required permissions](https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&language=en_US) to access and call
                this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/getPointOfNoReturnDetails`

                
                
                    

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
| salesTransactionId | **Type** id **Description** Required. ID of the sales transaction to get the point of no return details for. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code indicating the type of error. |
| lineItems​PointOf​NoReturn​Info | **Type** string **Description** Line items with the point of no return details. |
| planId | **Type** id **Description** ID of the composed fulfillment plan. |
| planState | **Type** string **Description** State of the fulfillment plan. |
| requestId | **Type** string **Description** Request ID of the invocation. |
| salesTransaction​Id | **Type** string **Description** ID of the submitted sales transaction. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Get Point Of No Return action.

                        

```
{
  "inputs": [
    {
      "salesTransactionId": "801SG00000jQO1ZYAW"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Get Point Of No Return action.

                        

```
[
  {
    "actionName": "getPointOfNoReturnDetails",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "planId": "13VSG00000229Z72AI",
      "requestId": "35c9388b-d30d-4d68-aae5-c109c8bff7ef",
      "lineItemsPointOfNoReturnInfo": "802SG000007D0B4YAK\": {\namendAllowed: false,\nanyChangesAllowed: true,\ncancelAllowed: false\n}, \n802SG000007D0B3YAK\": {\namendAllowed: false,\nanyChangesAllowed: true,\ncancelAllowed: false\n}",
      "salesTransactionId": "801SG00000jQO1ZYAW",
      "planState": "InProgress"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_orchestrate_sales_transaction.htm ===
---
page_id: actions_obj_orchestrate_sales_transaction.htm
title: Orchestrate Sales Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_orchestrate_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Orchestrate Sales Transaction Action

Initiate the orchestration process for a sales
            transaction. This action executes only the plan composition and orchestration
        phases, without performing decomposition.

        
            

Specify the ID of the sales transaction to orchestrate. The decomposition process
                includes these steps.

            
                
- Intake process

                
- Fulfillment orchestration

            

            

The intake process occurs synchronously or asynchronously, as specified with the
                    intakeRequestType input parameter. You can also specify the
                orchestration priority using the fulfillmentPriority
                parameter.

            

Use this action when the sales transaction is decomposed either by a previous
                decomposition action or by custom logic before orchestrating the fulfillment
                plan.

            

This action is available in API version 68.0 and later.

        

        

## Special Access
                Rules

            
            

The Orchestrate Sales Transaction action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required permissions](https://help.salesforce.com/s/articleView?id=sf.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&language=en_US) to access and call
                this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/orchestrateSalesTransaction`

                
                
                    

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

- 
- 

                        

                        
                            

                            

: 

: 

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

- 
- 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| allowOverride​OfPointOfNoReturn | **Type** boolean **Description** Indicates whether to override the point-of-no-return setting for the fulfillment step (`true`) or not (`false`). The default value is `false`. |
| fulfillmentAdapter | **Type** string **Description** Required. Type of fulfillment adapter. Valid values are: `StandardOrder` `GenericAdapter` |
| fulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| hydratedContextId | **Type** string **Description** ID of the hydrated context. |
| intakeRequestType | **Type** string **Description** Type of request to process the intake. Valid values are: `Synchronous` `Asynchronous` |
| priorityLimit​Action | **Type** string **Description** Type of action to perform when the priority limit is reached. Valid values are: `Reject` `Downgrade` This parameter is applicable only when you specify the fulfillmentPriority parameter. |
| salesTransactionId | **Type** id **Description** Required. ID of the sales transaction to submit. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code indicating the type of error. |
| fulfillmentPlanId | **Type** id **Description** ID of the composed fulfillment plan. |
| requested​FulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| requestId | **Type** string **Description** Request ID of the invocation. |
| resolved​FulfillmentPriority | **Type** string **Description** Resolved priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| submitStatus | **Type** string **Description** Submission status of the sales transaction for orchestration. Valid values are: `SUCCESS` `ERROR` `SUBMITTED` `REJECTED` |
| usedContextId | **Type** string **Description** ID of the context that updates the orchestration process. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Orchestrate Sales Transaction action.

                        

```
{
    "inputs": [
        {
            "fulfillmentAdapter": "StandardOrder",
            "intakeRequestType": "Synchronous",
            "salesTransactionId": "801xx000003GYgZAAW"
        }
    ]
}

```

                    

                    
: 
                        

This sample response is for the Orchestrate Sales Transaction action.

                        

```
[
  {
    "actionName": "orchestrateSalesTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "usedContextId": "0000000s21to18g00091764134566956e2100424de0d4af8869669df515e24cb",
      "requestId": "ac2a9d18-c702-43ee-bc08-1c03061b549c",
      "fulfillmentPlanId": "13Vxx0000004CFUEA2",
      "submitStatus": "SUCCESS",
      "resolvedFulfillmentPriority": "Default",
      "requestedFulfillmentPriority": "Default"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_orchestrate_transaction.htm ===
---
page_id: actions_obj_orchestrate_transaction.htm
title: Orchestrate Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_orchestrate_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Orchestrate Transaction Action

Orchestrate a transaction for any
            domain-specific object, such as a collection plan for Revenue billing, that requires the
            composition and execution of a fulfillment plan.

        
            

Specify the ID of the transaction to orchestrate and the orchestration type. The
                orchestration process includes:

            
                
- Composition of the orchestration plan

                
- Execution of the fulfillment plan

            

            

This action is available in API
                version
                66.0  and later.

        

        

## Special Access Rules

            
            

The Orchestrate Transaction action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required
                    permissions](https://help.salesforce.com/s/articleView?id=sf.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&language=en_US) to access and call this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/orchestrateTransaction`

                
                
                    

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
- 
- 
- 

                        

                    

                
| Input | Details |
| --- | --- |
| transactionId | **Type** string **Description** Required. ID of the business object or domain object to be orchestrated, such as a Collection Plan ID. |
| orchestration​Type | **Type** string **Description** Required. Type of orchestration that’s used to orchestrate the transaction. Valid values are: `Generic` `Fulfillment` `Billing` |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                    

                
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** Request ID of the invocation. |
| errorCode | **Type** string **Description** Code that corresponds to the type of encountered error. |
| fulfillment​PlanId | **Type** string **Description** ID of the composed fulfillment plan. |
| submitStatus | **Type** string **Description** Submission status of the transaction that’s orchestrated. Valid values are: `Success` `Error` |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Orchestrate Transaction action.

                        

```
{
  "inputs": [
    {
      "transactionId": "801xx000003GYexAAG",
      "orchestrationType": "Fulfillment"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Orchestrate Transaction action.

                        

```
[
  {
    "actionName": "orchestrateTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "requestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "fulfillmentPlanId": "0000000s21to18g0009176412796953180a8259def914e1abbd863dde076b71f",
      "submitStatus": "SUCCESS"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_submit_order.htm ===
---
page_id: actions_obj_submit_order.htm
title: Submit Order Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_submit_order.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Submit Order Action

Submit an order to Dynamic Revenue Orchestrator (DRO) for
			fulfillment.

		
			

By using the Submit Order action, you can perform:

			
				
- Order decomposition

				
- Fulfillment orchestration that’s driven through message queues

				
- Dynamic plan composition that’s based on the incoming order

			

			

This action is available in API version 61.0 and later.

		

		

## Special Access Rules

The Submit Order action is available in Enterprise, Unlimited, and Developer Editions of Revenue
        Cloud. See the [required permissions](https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&language=en_US) to
        access and call this invocable action.

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/submitOrder`

				
				
					

**Formats**

					
: JSON, XML

				
				
					

**HTTP Methods**

					
: POST

				
				
					

**Authentication**

					
: `Authorization: Bearer
							token`

				
			

		

		

## Inputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

- 
- 

						

						
							

							

: 

: 

						

					

				
| Input | Details |
| --- | --- |
| orderId | **Type** string **Description** Required. ID of the order to submit to DRO. |
| callType | **Type** string **Description** Optional. Mode that the order intake must be processed in. Valid values are: `Synchronous` `Asynchronous` The default value is `Asynchronous`. |
| contextId | **Type** string **Description** Optional. ID of the hydrated context. See [Context Service](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/context_service_overview.htm). |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Error code for the failed request, if any. |
| fulfillmentPlanId | **Type** string **Description** ID of the orchestrated fulfillment plan that’s generated. Returned only if the callType value is `Synchronous`. |
| requestId | **Type** string **Description** Unique ID of the invocation request that helps identify a single request. |
| submitStatus | **Type** string **Description** Submit status of the invocation request.Valid values are: `SUCCESS` `ERROR` `SUBMITTED` `REJECTED` |
| usedContextId | **Type** string **Description** Hydrated context ID that’s used in this request, which can be different from the contextId input. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request.

						

```
{
    "inputs": [
        {
            "orderId": "801RM0000007yGaYAI",
            "callType": "Synchronous"
        }
    ]
}
```

						

This example shows a sample response when the call type is
							synchronous.

						

```
[
    {
   "actionName":"submitOrder"
   "errors":NULL
   "invocationId":NULL
   "isSuccess":true
   "outputValues":{
   "requestId":"a161cfda-868c-41d2-b589-7c7d7ff2d4c1"
   "submitStatus":"SUCCESS"
   "usedContextId":"e275e930923106ee7e39cbfa232e38252bd4d63f4ea2dd956b7301e243554134"
   "fulfillmentPlanId":"13VZM00000000062AA"
}
]
```

						

This example shows a sample response when the call type is asynchronous
							or isn’t specified.

						

```
[
{
    "actionName": "submitOrder",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
    "submitStatus": "SUBMITTED"
    "requestId": "a161cfda-868c-41d2-b589-7c7d7ff2d4c1"
}
}
]
```

						

This example shows a sample response when a validation error occurs.

						

```
[
    {
    "actionName": "submitOrder",
    "errors": [
    {
        "statusCode": "UNKNOWN_EXCEPTION",
        "message": "Missing required input parameter: orderId",
        "fields": []
     }
  ],
        "invocationId": null,
        "isSuccess": false,
        "outputValues": {
          "requestId": "4c7d8ebb-6b0b-4852-a8a0-b67e0d36a73e",
          "errorCode": "DRO_INTERNAL_ERROR"
        },
    }
]
```

					

				
			

		

		

## Explainability Action Logs

				
					
: To troubleshoot or debug errors, retrieve a list of explainability action logs. See [Action Logs](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/connect_resources_get_create_action_logs.htm).

				
				
					

**Get logs for order intake**

					
: This resource example includes sample query parameters to retrieve the action logs for an
            order
            intake.

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/decision-explainer/action-logs?applicationSubType=DroSubmit&applicationType=7&processType=DroSubmit&primaryFilter=801xx000003GYzvAAG

```

					
: This example shows the sample response. The actionLog
						property contains the action logs.

```
{
  "actionLogs": [
    {
      "actionContextCode": "801NA000000XKPUYA4",
      "actionLog": {
        "OrderIntakeStatus": "",
        "OrderIntakeStatusMessage": "",
        "OrderId": "801NA000000XKPUYA4",
        "SubmitMode": "Synchronous",
        "UniqueRequestId": "d00c2aa7-56b0-411a-9b51-83d9fe2e4440",
        "ContexId": "a0ca3c2296c82ad071a5efa83e8974793910f44ebddb21d37f007ce4889b65d7",
        "DesActionSpecDevName": "DroSubmitAction",
        "ContextDefinition": "SalesTransactionContext__stdctx"
      },
      "additionalFilter": "undef",
      "applicationLogDate": "Thu Mar 28 12:36:26 GMT 2024",
      "applicationSubtype": "DroSubmit",
      "applicationType": "7",
      "explainabilitySpecName": "DroSubmitAction",
      "isChunked": false,
      "name": "DroSubmitAction",
      "primaryFilter": "801NA000000XKPUYA4",
      "processType": "DroSubmit",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "02c4bae9-d8b0-42f6-b031-e983d4247c76"
    }
  ],
  "queryMore": ""
}

```

				
				
					

**Get logs for decomposition scope**

					
: This resource example includes sample query parameters to retrieve the
            decomposition-related action
            logs.

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/decision-explainer/action-logs?applicationSubType=DroDcmp&applicationType=7&processType=DcmpScp&primaryFilter=801xx000003GYzvAAG

```

					
: This example shows the sample response. The actionLog
						property contains the action logs.

```
{
  "actionLogs": [
    {
      "actionContextCode": "801NA000000XKPeYAO",
      "actionLog": {
        "CandidateDecompositionRules": [
          {
            "decompRuleId": "13UNA0000004C932AE",
            "SourceProductId": "01tNA0000007NP5YAM",
            "AssociatedOlis": [
              "802NA000002lWjOYAU"
            ],
            "DestinationProductId": "01tNA0000007NOvYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "null"
          },
          {
            "decompRuleId": "13UNA0000004ITY2A2",
            "SourceProductId": "01tNA0000007NP5YAM",
            "AssociatedOlis": [
              "802NA000002lWjOYAU"
            ],
            "DestinationProductId": "01tNA0000007NOqYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "null"
          },
          {
            "decompRuleId": "13UNA0000004C942AE",
            "SourceProductId": "01tNA0000007NPAYA2",
            "AssociatedOlis": [
              "802NA000002lWjKYAU"
            ],
            "DestinationProductId": "01tNA0000007NOwYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "null"
          },
          {
            "decompRuleId": "13UNA0000004ITd2AM",
            "SourceProductId": "01tNA0000007NPAYA2",
            "AssociatedOlis": [
              "802NA000002lWjKYAU"
            ],
            "DestinationProductId": "01tNA0000007NP0YAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "null"
          },
          {
            "decompRuleId": "13UNA0000004C952AE",
            "SourceProductId": "01tNA0000007NPBYA2",
            "AssociatedOlis": [
              "802NA000002lWjLYAU"
            ],
            "DestinationProductId": "01tNA0000007NOxYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "9QwNA0000000CTu0AM"
          },
          {
            "decompRuleId": "13UNA0000004C982AE",
            "SourceProductId": "01tNA0000007NPCYA2",
            "AssociatedOlis": [
              "802NA000002lWjNYAU"
            ],
            "DestinationProductId": "01tNA0000007NOqYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "null"
          },
          {
            "decompRuleId": "13UNA0000004C992AE",
            "SourceProductId": "01tNA0000007NPCYA2",
            "AssociatedOlis": [
              "802NA000002lWjNYAU"
            ],
            "DestinationProductId": "01tNA0000007NOrYAM",
            "DestinationProductScope": "Order",
            "ConfiguredContextRuleId": "9QwNA0000000CTt0AM"
          }
        ],
        "SelectedDecompositionRules": [
          {
            "OliId": "802NA000002lWjKYAU",
            "DecompositionRuleIds": [
              "13UNA0000004C942AE",
              "13UNA0000004ITd2AM"
            ]
          },
          {
            "OliId": "802NA000002lWjOYAU",
            "DecompositionRuleIds": [
              "13UNA0000004C932AE",
              "13UNA0000004ITY2A2"
            ]
          },
          {
            "OliId": "802NA000002lWjNYAU",
            "DecompositionRuleIds": [
              "13UNA0000004C982AE"
            ]
          }
        ],
        "OliScopeDetails": [
          {
            "OliId": "802NA000002lWjLYAU",
            "ParentOliId": "802NA000002lWjOYAU",
            "BundleRootOli": "802NA000002lWjOYAU"
          },
          {
            "OliId": "802NA000002lWjMYAU",
            "ParentOliId": "802NA000002lWjOYAU",
            "BundleRootOli": "802NA000002lWjOYAU"
          },
          {
            "OliId": "802NA000002lWjKYAU",
            "ParentOliId": "802NA000002lWjOYAU",
            "BundleRootOli": "802NA000002lWjOYAU"
          },
          {
            "OliId": "802NA000002lWjNYAU",
            "ParentOliId": "802NA000002lWjOYAU",
            "BundleRootOli": "802NA000002lWjOYAU"
          }
        ],
        "FoliComputationDetails": [
          {
            "FoliId": "0a4NA000003HYbWYAW",
            "ComputedAction": "AMEND",
            "ComputedQuantity": "3.0"
          },
          {
            "FoliId": "0a4NA000003HYbXYAW",
            "ComputedAction": "AMEND",
            "ComputedQuantity": "6.0"
          },
          {
            "FoliId": "0a4NA000003HYbYYAW",
            "ComputedAction": "AMEND",
            "ComputedQuantity": "3.0"
          },
          {
            "FoliId": "0a4NA000003HYbZYAW",
            "ComputedAction": "AMEND",
            "ComputedQuantity": "3.0"
          }
        ],
        "FlsrDetails": [
          {
            "FlsrId": "16ANA000005idR82AI",
            "FlsrGuid": "WQoYClnAszG9axKxWxoe",
            "SourceId": "802NA000002lWjOYAU",
            "FoliId": "0a4NA000003HYbWYAW"
          },
          {
            "FlsrId": "16ANA000005idR92AI",
            "FlsrGuid": "80xWFpBK8sDmTFRV3Dn0",
            "SourceId": "802NA000002lWjOYAU",
            "FoliId": "0a4NA000003HYbXYAW"
          },
          {
            "FlsrId": "16ANA000005idRA2AY",
            "FlsrGuid": "nAql9VD3KiziZTFrfYXq",
            "SourceId": "802NA000002lWjNYAU",
            "FoliId": "0a4NA000003HYbXYAW"
          },
          {
            "FlsrId": "16ANA000005idRB2AY",
            "FlsrGuid": "wgCJT6NJ3ESolFXP5ajQ",
            "SourceId": "802NA000002lWjKYAU",
            "FoliId": "0a4NA000003HYbYYAW"
          },
          {
            "FlsrId": "16ANA000005idRC2AY",
            "FlsrGuid": "bvVhA34WvTBOYbG4q2Fj",
            "SourceId": "802NA000002lWjKYAU",
            "FoliId": "0a4NA000003HYbZYAW"
          }
        ],
        "OrderId": "801NA000000XKPeYAO",
        "SubmitMode": "Synchronous",
        "UniqueRequestId": "b9ac5971-0d71-45c6-a18e-f472976eaeae",
        "ContextId": "1422049ffa3cc42d8c060b9a7732be360bd62a346652cda9ab6e5fd54cd03eca",
        "DesActionSpecDevName": "DroDecompScopeAction",
        "ContextDefinition": "SalesTransactionContext__stdctx"
      },
      "additionalFilter": "undef",
      "applicationLogDate": "Fri Mar 29 10:02:26 GMT 2024",
      "applicationSubtype": "DroDcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroDecompScopeAction",
      "isChunked": false,
      "name": "DroDecompScopeAction",
      "primaryFilter": "801NA000000XKPeYAO",
      "processType": "DcmpScp",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "c1e11bc0-53e5-4f62-9ae8-1096e79a62b6"
    }
  ],
  "queryMore": ""
}
```

				
				
					

**Get logs for decomposition enrichment**

					
: This resource example includes sample query parameters to retrieve the logs for
            decomposition enrichment tasks. For example, conversion of order items to fulfillment
            order line
            items.

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/decision-explainer/action-logs?applicationSubType=DroDcmp&applicationType=7&processType=DcmpEnrich&primaryFilter=801xx000003GYzvAAG&secondaryFilter=BxyDQUJ2B49CoKXiuvGI

```

					
: The secondaryFilter property is optional. If this property is
            specified, the API returns the enrichment rule details for a decomposition rule. If this
            property is unspecified, the API returns all enrichment rule details for the order.

					
: This example shows the sample response. The actionLog
						property contains the action logs.

```
{
  "actionLogs": [
    {
      "actionContextCode": "801NA000000XKPUYA4",
      "actionLog": {
        "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
        "EnrichmentRulesExecutionDetails": [
          {
            "EnrichmentRuleId": "13TNA00000000eG2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CygYAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CyDYAU",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eH2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CylYAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CyIYAU",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eI2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CyqYAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CyhYAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eJ2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CzPYAU",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CymYAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eK2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CzUYAU",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CyrYAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eL2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004CzZYAU",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CywYAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "SUCCESS"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eM2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004D0dYAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004Cz1YAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "ERROR_DATA_TYPE_MISMATCH"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eN2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004D0iYAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CzQYAU",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "ERROR_DATA_TYPE_MISMATCH"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eO2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004D18YAE",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CzVYAU",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "ERROR_DATA_TYPE_MISMATCH"
          },
          {
            "EnrichmentRuleId": "13TNA00000000eP2AQ",
            "DecompRuleId": "13UNA0000004C942AE",
            "FlsrUid": "1FxfIhMq53OIpE9Hzs5w",
            "SourceType": "Attribute",
            "SourceAttributeId": "0tjNA0000004D1QYAU",
            "TargetType": "Attribute",
            "TargetAttributeId": "0tjNA0000004CzaYAE",
            "CalculationMethod": "Ad-verbatim",
            "ExecutionStatus": "ERROR_DATA_TYPE_MISMATCH"
          }
        ],
        "OrderId": "801NA000000XKPUYA4",
        "SubmitMode": "Synchronous",
        "UniqueRequestId": "d00c2aa7-56b0-411a-9b51-83d9fe2e4440",
        "ContexId": "a0ca3c2296c82ad071a5efa83e8974793910f44ebddb21d37f007ce4889b65d7",
        "DesActionSpecDevName": "DroDecompEnrichmentAction",
        "ContextDefinition": "SalesTransactionContext__stdctx"
      },
      "additionalFilter": "undef",
      "applicationLogDate": "Thu Mar 28 12:36:25 GMT 2024",
      "applicationSubtype": "DroDcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroDecompEnrichmentAction",
      "isChunked": false,
      "name": "DroDecompEnrichmentAction",
      "primaryFilter": "801NA000000XKPUYA4",
      "processType": "DcmpEnrich",
      "secondaryFilter": "1FxfIhMq53OIpE9Hzs5w",
      "uniqueIdentifier": "0bd42942-12b2-4c2e-9f10-b77ee85fd20b"
    }
  ],
  "queryMore": ""
}
```

				
				
					

**Get logs for plan composition**

					
: This resource example includes sample query parameters to retrieve the logs for plan
            composition.

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/decision-explainer/action-logs?applicationSubType=DroPcmp&applicationType=7&processType=PcmpSteps&primaryFilter=801xx000003GYzvAAG

```

					
: This example shows the sample response. The actionLog
						property contains the action logs.

```
{
  "actionLogs": [
    {
      "actionContextCode": "801NA000000XKPeYAO",
      "actionLog": {
        "PlanCompositionStatus": "",
        "PlanCompositionStatusMessage": "",
        "CandidateProductFulfillmentScenarios": [
          {
            "ProductFulfillmentScenarioId": "1axNA0000004C93YAE",
            "ProductId": "01tNA0000007NP5YAM",
            "FulfillmentStepDefinitionGroupId": "13oNA0000004CARYA2",
            "LineItemIds": [
              "802NA000002lWjOYAU"
            ],
            "ContextRulesetId": "9QwNA0000000CXq0AM"
          }
        ],
        "SelectedProductFulfillmentScenarios": [
          null
        ],
        "SelectedProductFulfillmentScenariosByOli": [
          {
            "OliId": "0a4NA000003HYbFYAW",
            "ProductFulfillmentScenarios": [
              null
            ]
          },
          {
            "OliId": "0a4NA000003HYbXYAW",
            "ProductFulfillmentScenarios": [
              null
            ]
          },
          {
            "OliId": "0a4NA000003HYbIYAW",
            "ProductFulfillmentScenarios": [
              null
            ]
          },
          {
            "OliId": "802NA000002lWjOYAU",
            "ProductFulfillmentScenarios": [
              null
            ]
          }
        ],
        "PlanId": "13VNA000000OQ9W2AW",
        "FulfillmentStepCreationStatus": "FulfillmentStepsCreated",
        "FulfillmentStepDependencyCreationStatus": "FulfilmentStepDepCreated",
        "OrderId": "801NA000000XKPeYAO",
        "SubmitMode": "Synchronous",
        "UniqueRequestId": "b9ac5971-0d71-45c6-a18e-f472976eaeae",
        "ContextId": "1422049ffa3cc42d8c060b9a7732be360bd62a346652cda9ab6e5fd54cd03eca",
        "DesActionSpecDevName": "DroPlanCompStepsAction",
        "ContextDefinition": "SalesTransactionContext__stdctx"
      },
      "additionalFilter": "undef",
      "applicationLogDate": "Fri Mar 29 10:02:27 GMT 2024",
      "applicationSubtype": "DroPcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroPlanCompStepsAction",
      "isChunked": false,
      "name": "DroPlanCompStepsAction",
      "primaryFilter": "801NA000000XKPeYAO",
      "processType": "PcmpSteps",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "bb532c9b-a88f-4add-8cd8-bd385359b1ad"
    }
  ],
  "queryMore": ""
}
```

				
        
          

**Capture logs for an order**

          
: This resource example includes sample query parameters to retrieve the logs for an
            order.

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/decision-explainer/action-logs?actionContextCode=801DU000000CqBJYA0&applicationType=7
```

          
: This example shows the sample response. The actionLog property
            contains the action logs.

```
{
  "actionLogs": [
    {
      "actionContextCode": "801xx000003GZSxAAO",
      "actionLog": "{&quot;FlsrUid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;DecompositionEnrichmentExecutionSequence&quot;:&quot;0&quot;,&quot;EnrichmentRulesExecutionDetails&quot;:[{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CLwEAM&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CCGEA2&quot;,&quot;FlsrUid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;SourceType&quot;:&quot;Attribute&quot;,&quot;SourceAttributeId&quot;:&quot;0tjxx0000000001AAA&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx0000000085AAA&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;ERROR_SOURCE_DATA_FETCH&quot;},{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CNYEA2&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CCGEA2&quot;,&quot;FlsrUid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;SourceType&quot;:&quot;Field&quot;,&quot;SourceFieldName&quot;:&quot;Product2Id&quot;,&quot;SourceContextTag&quot;:&quot;Product&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx000000006TAAQ&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;SUCCESS&quot;},{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CPAEA2&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CCGEA2&quot;,&quot;FlsrUid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;SourceType&quot;:&quot;Field&quot;,&quot;SourceFieldName&quot;:&quot;IsAssetizable&quot;,&quot;SourceContextTag&quot;:&quot;IsAssetizable&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx000000004rAAA&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;SUCCESS&quot;},{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CQmEAM&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CCGEA2&quot;,&quot;FlsrUid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;SourceType&quot;:&quot;Attribute&quot;,&quot;SourceAttributeId&quot;:&quot;0tjxx000000001dAAA&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx000000003FAAQ&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;ERROR_SOURCE_DATA_FETCH&quot;}],&quot;OrderId&quot;:&quot;801xx000003GZSxAAO&quot;,&quot;SubmitMode&quot;:&quot;Synchronous&quot;,&quot;UniqueRequestId&quot;:&quot;5dd3888e-e883-4770-b0ad-aa59e88450eb&quot;,&quot;ContextId&quot;:&quot;d9995de15eea0b3c1ed0a552813fe9cd02b73d0de80c0c15fd4e8ac6661508df&quot;,&quot;DesActionSpecDevName&quot;:&quot;DroDecompEnrichmentAction&quot;,&quot;ContextDefinition&quot;:&quot;SalesTransactionContext__stdctx&quot;}",
      "additionalFilter": "undef",
      "applicationLogDate": "Tue May 07 13:05:28 GMT 2024",
      "applicationSubtype": "DroDcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroDecompEnrichmentAction",
      "isChunked": false,
      "name": "DroDecompEnrichmentAction",
      "primaryFilter": "801xx000003GZSxAAO",
      "processType": "DcmpEnrich",
      "secondaryFilter": "qrh0Z3xv6buew1BW0wdn",
      "uniqueIdentifier": "768f7d03-6770-4939-980f-a6f42ad07cde"
    },
    {
      "actionContextCode": "801xx000003GZSxAAO",
      "actionLog": "{&quot;FlsrUid&quot;:&quot;hjow5L3YcntZsnNuEd5n&quot;,&quot;DecompositionEnrichmentExecutionSequence&quot;:&quot;0&quot;,&quot;EnrichmentRulesExecutionDetails&quot;:[{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CH6EAM&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CAeEAM&quot;,&quot;FlsrUid&quot;:&quot;hjow5L3YcntZsnNuEd5n&quot;,&quot;SourceType&quot;:&quot;Field&quot;,&quot;SourceFieldName&quot;:&quot;IsAssetizable&quot;,&quot;SourceContextTag&quot;:&quot;IsAssetizable&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx000000004rAAA&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;SUCCESS&quot;},{&quot;EnrichmentRuleId&quot;:&quot;13Txx0000004CKKEA2&quot;,&quot;DecompRuleId&quot;:&quot;13Uxx0000004CAeEAM&quot;,&quot;FlsrUid&quot;:&quot;hjow5L3YcntZsnNuEd5n&quot;,&quot;SourceType&quot;:&quot;Field&quot;,&quot;SourceFieldName&quot;:&quot;PricebookEntryId&quot;,&quot;SourceContextTag&quot;:&quot;ItemPricebookEntry&quot;,&quot;TargetType&quot;:&quot;Attribute&quot;,&quot;TargetAttributeId&quot;:&quot;0tjxx000000003FAAQ&quot;,&quot;CalculationMethod&quot;:&quot;Ad-verbatim&quot;,&quot;ExecutionStatus&quot;:&quot;SUCCESS&quot;}],&quot;OrderId&quot;:&quot;801xx000003GZSxAAO&quot;,&quot;SubmitMode&quot;:&quot;Synchronous&quot;,&quot;UniqueRequestId&quot;:&quot;5dd3888e-e883-4770-b0ad-aa59e88450eb&quot;,&quot;ContextId&quot;:&quot;d9995de15eea0b3c1ed0a552813fe9cd02b73d0de80c0c15fd4e8ac6661508df&quot;,&quot;DesActionSpecDevName&quot;:&quot;DroDecompEnrichmentAction&quot;,&quot;ContextDefinition&quot;:&quot;SalesTransactionContext__stdctx&quot;}",
      "additionalFilter": "undef",
      "applicationLogDate": "Tue May 07 13:05:28 GMT 2024",
      "applicationSubtype": "DroDcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroDecompEnrichmentAction",
      "isChunked": false,
      "name": "DroDecompEnrichmentAction",
      "primaryFilter": "801xx000003GZSxAAO",
      "processType": "DcmpEnrich",
      "secondaryFilter": "hjow5L3YcntZsnNuEd5n",
      "uniqueIdentifier": "7ce652e3-81a0-4b2d-a072-88b012c83864"
    },
    {
      "actionContextCode": "801xx000003GZSxAAO",
      "actionLog": "{&quot;CandidateDecompositionRules&quot;:[{&quot;decompRuleId&quot;:&quot;13Uxx0000004CCGEA2&quot;,&quot;SourceProductId&quot;:&quot;01txx0000006i5gAAA&quot;,&quot;AssociatedOlis&quot;:[&quot;802xx000001nbKhAAI&quot;],&quot;DestinationProductId&quot;:&quot;01txx0000006iAWAAY&quot;,&quot;DestinationProductScope&quot;:&quot;OrderLineItem&quot;,&quot;ConfiguredContextRuleId&quot;:&quot;null&quot;},{&quot;decompRuleId&quot;:&quot;13Uxx0000004CAeEAM&quot;,&quot;SourceProductId&quot;:&quot;01txx0000006i5gAAA&quot;,&quot;AssociatedOlis&quot;:[&quot;802xx000001nbKhAAI&quot;],&quot;DestinationProductId&quot;:&quot;01txx0000006i8uAAA&quot;,&quot;DestinationProductScope&quot;:&quot;OrderLineItem&quot;,&quot;ConfiguredContextRuleId&quot;:&quot;null&quot;}],&quot;SelectedDecompositionRules&quot;:[{&quot;OliId&quot;:&quot;802xx000001nbKhAAI&quot;,&quot;DecompositionRuleIds&quot;:[&quot;13Uxx0000004CCGEA2&quot;,&quot;13Uxx0000004CAeEAM&quot;]}],&quot;OliScopeDetails&quot;:[],&quot;FoliComputationDetails&quot;:[{&quot;FoliId&quot;:&quot;0a4xx00000000ODAAY&quot;,&quot;ComputedAction&quot;:&quot;ADD&quot;,&quot;ComputedQuantity&quot;:&quot;1.0&quot;},{&quot;FoliId&quot;:&quot;0a4xx00000000OEAAY&quot;,&quot;ComputedAction&quot;:&quot;ADD&quot;,&quot;ComputedQuantity&quot;:&quot;1.0&quot;}],&quot;FlsrDetails&quot;:[{&quot;FlsrId&quot;:&quot;16Axx0000004CXEEA2&quot;,&quot;FlsrGuid&quot;:&quot;qrh0Z3xv6buew1BW0wdn&quot;,&quot;SourceId&quot;:&quot;802xx000001nbKhAAI&quot;,&quot;FoliId&quot;:&quot;0a4xx00000000ODAAY&quot;},{&quot;FlsrId&quot;:&quot;16Axx0000004CXFEA2&quot;,&quot;FlsrGuid&quot;:&quot;hjow5L3YcntZsnNuEd5n&quot;,&quot;SourceId&quot;:&quot;802xx000001nbKhAAI&quot;,&quot;FoliId&quot;:&quot;0a4xx00000000OEAAY&quot;}],&quot;OrderId&quot;:&quot;801xx000003GZSxAAO&quot;,&quot;SubmitMode&quot;:&quot;Synchronous&quot;,&quot;UniqueRequestId&quot;:&quot;5dd3888e-e883-4770-b0ad-aa59e88450eb&quot;,&quot;ContextId&quot;:&quot;c132f6fca3628bf9608c0e61865b4cd0d9de1479f5171686abc040c69f0504d7&quot;,&quot;DesActionSpecDevName&quot;:&quot;DroDecompScopeAction&quot;,&quot;ContextDefinition&quot;:&quot;SalesTransactionContext__stdctx&quot;}",
      "additionalFilter": "undef",
      "applicationLogDate": "Tue May 07 13:05:32 GMT 2024",
      "applicationSubtype": "DroDcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroDecompScopeAction",
      "isChunked": false,
      "name": "DroDecompScopeAction",
      "primaryFilter": "801xx000003GZSxAAO",
      "processType": "DcmpScp",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "9f633a63-67d0-4f90-b4dc-c368defe8b44"
    },
    {
      "actionContextCode": "801xx000003GZSxAAO",
      "actionLog": "{&quot;CandidateProductFulfillmentScenarios&quot;:[{&quot;ProductFulfillmentScenarioId&quot;:&quot;1axxx0000000001AAA&quot;,&quot;ProductId&quot;:&quot;01txx0000006i8uAAA&quot;,&quot;FulfillmentStepDefinitionGroupId&quot;:&quot;13oxx0000004CFUAA2&quot;,&quot;LineItemIds&quot;:[&quot;0a4xx00000000OEAAY&quot;]},{&quot;ProductFulfillmentScenarioId&quot;:&quot;1axxx0000000002AAA&quot;,&quot;ProductId&quot;:&quot;01txx0000006i8uAAA&quot;,&quot;FulfillmentStepDefinitionGroupId&quot;:&quot;13oxx0000004CH6AAM&quot;,&quot;LineItemIds&quot;:[&quot;0a4xx00000000OEAAY&quot;]}],&quot;SelectedProductFulfillmentScenarios&quot;:[&quot;1axxx0000000001AAA&quot;,&quot;1axxx0000000002AAA&quot;],&quot;SelectedProductFulfillmentScenariosByOli&quot;:[{&quot;OliId&quot;:&quot;802xx000001nbKhAAI&quot;,&quot;ProductFulfillmentScenarios&quot;:[]},{&quot;OliId&quot;:&quot;0a4xx00000000ODAAY&quot;,&quot;ProductFulfillmentScenarios&quot;:[]},{&quot;OliId&quot;:&quot;0a4xx00000000OEAAY&quot;,&quot;ProductFulfillmentScenarios&quot;:[&quot;1axxx0000000001AAA&quot;,&quot;1axxx0000000002AAA&quot;]}],&quot;PlanId&quot;:&quot;13Vxx0000004Ck8EAE&quot;,&quot;FulfillmentStepCreationStatus&quot;:&quot;FulfillmentStepsCreated&quot;,&quot;FulfillmentStepDependencyCreationStatus&quot;:&quot;FulfilmentStepDepCreated&quot;,&quot;OrderId&quot;:&quot;801xx000003GZSxAAO&quot;,&quot;SubmitMode&quot;:&quot;Synchronous&quot;,&quot;UniqueRequestId&quot;:&quot;5dd3888e-e883-4770-b0ad-aa59e88450eb&quot;,&quot;ContextId&quot;:&quot;c132f6fca3628bf9608c0e61865b4cd0d9de1479f5171686abc040c69f0504d7&quot;,&quot;DesActionSpecDevName&quot;:&quot;DroPlanCompStepsAction&quot;,&quot;ContextDefinition&quot;:&quot;SalesTransactionContext__stdctx&quot;}",
      "additionalFilter": "undef",
      "applicationLogDate": "Tue May 07 13:05:33 GMT 2024",
      "applicationSubtype": "DroPcmp",
      "applicationType": "7",
      "explainabilitySpecName": "DroPlanCompStepsAction",
      "isChunked": false,
      "name": "DroPlanCompStepsAction",
      "primaryFilter": "801xx000003GZSxAAO",
      "processType": "PcmpSteps",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "47a956a6-ae52-4e4a-843b-08b404beb52a"
    },
    {
      "actionContextCode": "801xx000003GZSxAAO",
      "actionLog": "{&quot;OrderId&quot;:&quot;801xx000003GZSxAAO&quot;,&quot;SubmitMode&quot;:&quot;Synchronous&quot;,&quot;UniqueRequestId&quot;:&quot;5dd3888e-e883-4770-b0ad-aa59e88450eb&quot;,&quot;ContextId&quot;:&quot;c132f6fca3628bf9608c0e61865b4cd0d9de1479f5171686abc040c69f0504d7&quot;,&quot;DesActionSpecDevName&quot;:&quot;DroSubmitAction&quot;,&quot;ContextDefinition&quot;:&quot;SalesTransactionContext__stdctx&quot;}",
      "additionalFilter": "undef",
      "applicationLogDate": "Tue May 07 13:06:30 GMT 2024",
      "applicationSubtype": "DroSubmit",
      "applicationType": "7",
      "explainabilitySpecName": "DroSubmitAction",
      "isChunked": false,
      "name": "DroSubmitAction",
      "primaryFilter": "801xx000003GZSxAAO",
      "processType": "DroSubmit",
      "secondaryFilter": "undef",
      "uniqueIdentifier": "278caec4-680c-4df8-a1b2-608e05e44baa"
    }
  ],
  "queryMore": ""
}
```

=== ARTICLE: actions_obj_submit_sales_transaction.htm ===
---
page_id: actions_obj_submit_sales_transaction.htm
title: Submit Sales Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_submit_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Submit Sales Transaction Action

Initiate the fulfillment process of any sales transaction, such as a
            quote, an order, or an order summary.

        

Specify the ID of the sales transaction to be fulfilled. The fulfillment process includes these
                steps.

                
- Intake process

                
- Fulfillment orchestration

            

The intake process happens synchronously or asynchronously, which is specified
                by using the intakeRequestType input parameter. You can also
                specify the priority for the execution of the fulfillment process, which is
                specified by using the fulfillmentPriority
                parameter.

This action is available in API version 63.0 and
            later.

        

## Special Access Rules

            
            

The Submit Sales Transaction action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required permissions](https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&language=en_US) to access and call
                this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/submitSalesTransaction`

                
                
                    

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

- 
- 

                        

                        
                            

                            

: 

: 

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

- 
- 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| allowOverrideOfPointOfNoReturn | **Type** boolean **Description** Indicates whether to override the point of no return setting for the fulfillment step (`true`) or not (`false`). The default value is `false`. Available in API version 64.0 and later. |
| fulfillmentAdapter | **Type** string **Description** Type of fulfillment adapter. Valid values are: `StandardOrder` `GenericAdapter`—Available in API version 64.0 and later. |
| fulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| hydratedContextId | **Type** string **Description** ID of the hydrated context. |
| intakeRequestType | **Type** string **Description** Type of request to process the intake. Valid values are: `Synchronous` `Asynchronous` |
| priorityLimitAction | **Type** string **Description** Type of action to perform when the priority limit is reached. Valid values are: `Reject` `Downgrade` This parameter is applicable only when you specify the fulfillmentPriority parameter. |
| salesTransactionId | **Type** id **Description** Required. ID of the sales transaction to submit. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code indicating the type of error. |
| fulfillmentPlanId | **Type** id **Description** ID of the composed fulfillment plan. |
| requestedFulfillmentPriority | **Type** string **Description** Priority to fulfill the sales transaction. Valid values are: `High` `Bulk` `Default` |
| requestId | **Type** string **Description** Request ID of the invocation. |
| resolvedFulfillmentPriority | **Type** string **Description** Resolved priority to fulfill the sales transaction. |
| submitStatus | **Type** string **Description** Submit status of the invocation. |
| usedContextId | **Type** string **Description** ID of the used context that updates the decomposition process. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Submit Sales Transaction action.

                        

```
{
  "inputs": [
    {
      "allowOverrideOfPointOfNoReturn": false,
      "salesTransactionId": "801DV000000CbIPYA0",
      "intakeRequestType": "Synchronous",
      "fulfillmentAdapter": "StandardOrder",
      "fulfillmentPriority": "Default",
      "priorityLimitAction": "Reject"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Submit Sales Transaction action.

                        

```
[
  {
    "actionName": "submitSalesTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "submitStatus": "SUCCESS",
      "resolvedFulfillmentPriority": "Default",
      "requestedFulfillmentPriority": "Default",
      "usedContextId": "0abc8db32b30d09c5051e4561f0b39d938a3bd8db4ccb13e04d41019e427211d",
      "requestId": "927f72b7-85e0-4b5d-b92e-c265f41898f0",
      "fulfillmentPlanId": "13VDV00000008M92AI"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_unfreeze_sales_transaction.htm ===
---
page_id: actions_obj_unfreeze_sales_transaction.htm
title: Unfreeze Sales Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_unfreeze_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unfreeze Sales Transaction Action

Unfreeze a sales transaction to enable the modification of a line
            item.

        

A line item can reach a milestone in the fulfillment
                process, which is known as a point of no return, where the line item can’t accept
                modifications. Get details about the point of no return for each line item of a
                sales transaction.

This action is available in API version 64.0 and later.

        

## Special Access Rules

            
            

The Unfreeze Sales Transaction action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Management. See the [required permissions](https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&language=en_US) to access and call
                this invocable action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/unfreezeSalesTransaction`

                
                
                    

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
| salesTransactionId | **Type** id **Description** Required. ID of the sales transaction that's submitted to the Dynamic Revenue Orchestrator. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| errorCode | **Type** string **Description** Code indicating the type of error. |
| orchestrationPlanId | **Type** id **Description** ID of the created orchestration plan. |
| planState | **Type** string **Description** Status of the created orchestration plan. Valid values are: `FAILURE` `NOTSTARTED` `PENDING` `COMPLETED` `FROZEN` `INPROGRESS` |
| requestId | **Type** string **Description** ID of the request to get the point of no return details. |
| salesTransaction​Id | **Type** string **Description** ID of the sales transaction that's submitted to the Dynamic Revenue Orchestrator. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Unfreeze Sales Transaction action.

                        

```
{
  "inputs": [
    {
      "salesTransactionId": "801SG00000jQO1ZYAW"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Unfreeze Sales Transaction action.

                        

```
[
  {
    "actionName": "unfreezeSalesTransaction",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "orchestrationPlanId": "13VSG00000229Z72AI",
      "salesTransactionId": "801SG00000jQO1ZYAW",
      "planState": "InProgress",
      "requestId": "e9f2d961-b218-4911-8fee-8de31937850d"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: dro_integration_definition_for_standard_fulfillment_provider.htm ===
---
page_id: dro_integration_definition_for_standard_fulfillment_provider.htm
title: Integration Definition for Standard Fulfillment Provider
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dro_integration_definition_for_standard_fulfillment_provider.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_default_order_fulfillment_provider.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Integration Definition for Standard Fulfillment Provider

Use supported attribute values of an integration definition for a Standard Fulfillment
    Provider to implement features as per your requirement.

    

The Standard Fulfillment Provider supports these attribute values.

    
      
    

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

          
            

            

          

          
            

            
- 
- 
- 
- 

          

          
            

            

          

          
            

            

          

          
            

            

- 
- 

          

          
            

            

- 
- 

          

          
            

            

          

          
            

            

          

        

      
| Attribute Name | Description |
| --- | --- |
| Named Credentials | API name of the associated named credentials. |
| Path | Additional string that's added to the URL specified in the named credential endpoint. |
| Timeout (ms) | Number of milliseconds to set as a timeout parameter for the HTTP connection. |
| Callback URI | Attribute used by a third party as the callback to process steps in case of a async callout. Additionally, this attribute also indicates these scenarios. The configured callout is an async callout. If callback URI is defined, then it's included as the `ResponseUri` parameter value in the default payload for Standard Fulfillment Provider. For example, a `ResponseUri` parameter value as `/services/apexrest/async/callout`. The executor expects 202 response code from the remote destination. The 202 response code keeps the Fulfillment Step state as Running whereas 200 response code completes it. |
| Input Processor | `Type_Subtype` or `Id` of OmniProcess to process the input payload. |
| Output Processor | `Type_Subtype` or `Id` of OmniProcess to process the output payload. |
| Item Encoding Style | Required. Encoding style for fulfillment transaction items and sales transaction items. Valid values are: `Flat`—Includes a list of fulfillment transaction items and sales transaction items without any hierarchy details in the payload. `Structure`—Includes a list of all child line items if the step's source line item has a hierarchy of line items associated with it.If item encoding style is configured as `Structure` on a fulfillment order line item or a sales transaction item, then the payload contains the details of the line item that the fulfillment order line item or sales transaction item is decomposed from. If the fulfillment order line item or sales transaction item is decomposed from the root of a bundle order line item or sales transaction item, then the payload contains the entire order line item or sales transaction item bundle structure. The default value is `Flat`. |
| Attribute Encoding Style | Required. Generates the payload for attributes based on the specified encoding style. Valid values are: `Flat`—Includes specific details in key-value pair format that doesn't include granular details of attributes. `Structure`—This payload structure includes granular details of attributes. The default value is `Structure`. |
| Send Empty Attributes | If this checkbox is selected, the request payload includes empty attribute values wherever applicable. |
| Send Payload | If this checkbox is selected, a default request payload is generated to optimize processing performance. If this checkbox isn't selected, a value for the input processor is required. |

=== ARTICLE: dynamic_revenue_orchestrator_apex_type_provider.htm ===
---
page_id: dynamic_revenue_orchestrator_apex_type_provider.htm
title: Apex Type Provider
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_apex_type_provider.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apex Type Provider

Implement custom integration logic via Apex by using the Apex Type Provider. This
    provider requires an Apex Integration Developer to implement a custom Apex adapter
    interface.

    

Use a custom Apex adapter to:

    
      
- Include and use integration parameters in adapter implementations such as timeouts,
        credentials, and path.

      
- Generate and transform requests and responses via Omnistudio Integration Procedures or
        Extract, Transform, Load (ETL) libraries.

      
- Enable asynchronous interaction pattern.

      
- Enable request and response logging by implementing a specific Apex interface.

      
- Handle errors, and integrate with fallout rules.

    

    

To ‌configure the callout settings for Apex Type Provider, see [Configuration Steps](./dynamic_revenue_orchestrator_callout_configuration_steps.htm.md).

    

## Integration Adapter Implementation

      
      

Implement the `industriesintegrationfwk.ProcessIntegrationProvider` Apex interface. Use the
          `industriesintegrationfwk.ApexProviderAttr ` class to
        define and access the attribute values in the integration provider definition.

      

```
global with sharing class DROSampleOrderAdapter implements industriesintegrationfwk.ProcessIntegrationProvider {
    
    // Named credential attribute
    private static final String MOCK_CALLOUT_NAMED_CREDENTIAL = 'callout:DROOrderInterfaceNamedCred';
    private final static Integer TIMEOUT = 10000; // Request timeout in milliseconds, or can be defined on Integration Definition as an Attribute
    
    
    private static final industriesintegrationfwk.ApexProviderAttr NAMED_CRED_ATTR = new industriesintegrationfwk.ApexProviderAttr('Named Credential', 
    'Named_Credential', 'DROOrderInterfaceNamedCred', true, 'String');
    private static final industriesintegrationfwk.ApexProviderAttr ENDPOINT_ATTR = new industriesintegrationfwk.ApexProviderAttr('Endpoint URI', 
    'Endpoint_URI', '/v1/orderitems/', true, 'String');

    
    /**
     * @param requestGuid                 Request Globally Unique Identifier (GUID) provided by the client
     * @param inputRecordId               Input Record ID — value is taken from Fulfillment Step > Fulfillment Step Source > Source Line Item
     * @param payload                     Payload to be passed to the Provider Class (empty in DRO)
     * @param attributes                  Map of configuration attributes
     * @return IntegrationCalloutResponse Response sent to the client
    */
    global static industriesintegrationfwk.IntegrationCalloutResponse executeCallout(String requestGuid, String inputRecordId, String payload, Map<String, Object> attributes) {
        // create request
        String msgBody = '{\"message\":\"Hello\",' 
            + '\n\"requestGuid\":\"' + requestGuid + '\",\n'
            + '\n\"inputRecordId\":\"' + inputRecordId + '\",\n'
            + '\n\"payload\":\"' + payload + '\"}'            
            ;
        
        String endpointUri = (String) attributes.get('Endpoint_URI');

        // Make a call
        HttpResponse response = makeCallout(endpointUri, msgBody);
        // process response and pass details to the DRO Callout Step processor by using IntegrationCalloutResponse(isSuccess, ResponseCode, ErrorMessage)
 
         industriesintegrationfwk.IntegrationCalloutResponse integrationCalloutResponse = handleResponse(response); 

        return integrationCalloutResponse;
    }

    // define configurable attriobutes 
    global static List<industriesintegrationfwk.ApexProviderAttr> getProviderAttributes() {
        List<industriesintegrationfwk.ApexProviderAttr> defaults = new List<industriesintegrationfwk.ApexProviderAttr>();
        defaults.add(NAMED_CRED_ATTR);
        defaults.add(ENDPOINT_ATTR);
        // add any attributes such as endpoint, timeout, interface, and params
        // ...
        return defaults;
    }   

    // Call Mock Service API.
    private static HttpResponse makeCallout(String endpointUri, String msgBody) {
        
        // Construct the request object
        String endPoint = MOCK_CALLOUT_NAMED_CREDENTIAL + endpointUri;
        HttpRequest request = new HttpRequest();
        request.setMethod('POST');
        request.setHeader('Content-Type', 'application/json');
        request.setHeader('Accept', 'application/json');
        request.setEndpoint(endPoint);
        request.setTimeout(TIMEOUT);
        request.setBody(msgBody);
        
        // Send request
        HttpResponse response = new Http().send(request);
        return response;
    }
}
```

    

    

## Error Handling

      
      

This sample shows how to pass errors from response to orchestration via the `IntegrationResponse` interface in the Apex provider
        implementation. See [ProcessIntegrationProvider Interface](https://help.salesforce.com/s/articleView?id=ind.consumption_framework_process_integration_provider_interface.htm&type=5&language=en_US).

      

```
public static industriesintegrationfwk.IntegrationCalloutResponse handleResponse(HttpResponse response) { 
    
        industriesintegrationfwk.IntegrationCalloutResponse integrationCalloutResponse;
        
        Map<String, Object> responseGroup = getResponseGroupAfterCallout(response);
        
        if(response.getStatusCode() == 200)
        {
            // SUCCESS
            integrationCalloutResponse = new industriesintegrationfwk.IntegrationCalloutResponse(true);
                    integrationCalloutResponse.setResponseCode(response.getStatusCode());
              integrationCalloutResponse.setReturnValue(responseGroup);
        
        } else {
            //FAILURE - pass error to DRO Fallout Handling to apply Retry Policies
            integrationCalloutResponse = new industriesintegrationfwk.IntegrationCalloutResponse(false);
            integrationCalloutResponse.setResponseCode(response.getStatusCode());
            integrationCalloutResponse.setReturnValue(responseGroup);
            integrationCalloutResponse.setErrorMessage('Unable to process request.');
        }
        return integrationCalloutResponse;
        }
    
    // Process Response payLoad 
    private static Map<String, Object> getResponseGroupAfterCallout(HttpResponse response) {
        Map<String, Object> responseGroup = new Map<String, Object>();
        if (response.getStatusCode() == 200) {
            responseGroup.put('isSuccess', true);
        } else {
            responseGroup.put('isSuccess', false);
        }
        responseGroup.put('response', getResponseMap(response.getBody()));
        return responseGroup;
    }
    
    // Convert response string into Map 
    private static Map<String,Object> getResponseMap(String responseBody) {
        try {
            Map<String,Object> responseBodyMap = (Map<String,Object>) JSON.deserializeUntyped(responseBody);
            return responseBodyMap;
        } catch (Exception e) {
            Map<String, Object> responseMap = new Map<String,Object>();
            responseMap.put('response', responseBody);
            return responseMap;
        }
    }
```

      

The fulfillment step state changes to `Fatally Failed`,
        and the error message is saved in the Execution Message field.

      
        
      

      
        
      

    

    

## Apex Advanced Interface Implementation

      
      

To use advanced features such as logging, the Apex provider must implement the Apex
        Provider Advanced interface. You must use the HttpBaseProvider client for HTTP requests.

      

This example shows a sample of the `ProcessIntegrationProviderAdvanced` Apex interface implementation.

      

```
global with sharing class DFOApexVlocMockWithDelay
implements industriesintegrationfwk.ProcessIntegrationProviderAdvanced {
...
global static industriesintegrationfwk.IntegrationCalloutResponse executeCallout(String requestGuid, String inputRecordId, String payload, Map<String, Object> attributes,
industriesintegrationfwk.HttpBaseProvider httpProvider) {
...
String endPoint = MOCK_CALLOUT_NAMED_CREDENTIAL + '/delay/5';
HttpRequest request = new HttpRequest();
request.setMethod('POST');
request.setHeader('Content-Type', 'application/json');
request.setHeader('Accept', 'application/json');
request.setEndpoint(endPoint);
request.setTimeout(TIMEOUT);
request.setBody(msgBody);

// Send request
//HttpResponse response = httpProvider.httpCallout(request);
HttpResponse response = new Http().send(request);

```

    

    

## Integration Definition Configuration

      
      

Select the
              **Save
              the request and response as attachments to the record** checkbox for the
            integration definition to save request and response payloads as attachments to the
            Integration Provider Execution record. Content publish limits apply when saving request
            and response payloads as attachments. Use [Shield
              Platform Encryption](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_overview.htm&type=5&language=en_US) for secure storage of sensitive information.

      

See [Create an
          Integration Definition](https://help.salesforce.com/s/articleView?id=ind.consumption_framework_integration_definitions.htm&type=5&language=en_US).

    

    

## Log Records

      
      

Integration Provider execution records are created on every request and associated with the
        fulfillment step. The referenced object identifier is set to order item or fulfillment order
        line item ID. See[IntegrationProviderExecution](https://developer.salesforce.com/docs/atlas.en-us.264.0.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_IntegrationProviderExecution.htm).

      

To view the Integration Provider execution records, configure the Fulfillment Step record
        page to include the Integration Provider Executions related list by using Lightning App
        Builder. See [Lightning App
          Builder](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_overview.htm&type=5&language=en_US).

=== ARTICLE: dynamic_revenue_orchestrator_async_interaction_pattern.htm ===
---
page_id: dynamic_revenue_orchestrator_async_interaction_pattern.htm
title: Asynchronous Interaction Pattern
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_async_interaction_pattern.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asynchronous Interaction Pattern

To specify an asynchronous request, you must add the callback URI to the integration
    definition for Standard Fulfillment Provider or Apex Type Provider as an optional
    attribute.

    

## Standard Fulfillment Provider

      
      
        
- Provide the callback URI in the integration definition to accept the callback.

        
- Use these steps to set up the async callout.
            
  - 
              
                
    - Use the `ResponseUri` key to retrieve the
                  Callback URI value from the payload.

                
    - Use the `StepId` key to retrieve the
                  Fulfillment Step value from the payload. If order item ID is returned instead of
                  Fulfillment Step ID, use `CorrelationId` key to
                  extract the value of the step ID. For example, `callout:13Wxx0000004CAf:`.

                
    - Pass the StepId value to the callback URI endpoint. Return 202 response code to
                  ensure the Fulfillment Step is in `Running`
                  state. Otherwise, the 200 response code completes the step.

Here's a sample
                    payload.

```
{
    "ResponseUri": "/services/apexrest/async/callout",
    "StepId": "802xx000001nb1MAAQ",
    "CorrelationId": "callout:13Wxx0000004CAf:",
    ...//Other values
}
```

              

            

          

        
- Extract the step ID from the request. Find the Fulfillment Step ID in the org by using
          the extracted step ID and update the Fulfillment Step state to `Completed`.

      

    

    

## Apex Type Provider

      
      
        
- Provide the callback URI in the integration definition to accept the callback.

        
- Set up the async callout by using Apex Type Provider.
            
  - 
              
                
    - Create an Apex class that implements the `ProcessIntegrationProvider` interface.

Here's a sample that shows the
                    addition of a callback URI to the provider attribute for Apex Type
                  Provider.

global with sharing class DFOAsyncApexSample implements industriesintegrationfwk.ProcessIntegrationProvider {

    private static final industriesintegrationfwk.ApexProviderAttr NAMED_CRED_ATTR = 
        new industriesintegrationfwk.ApexProviderAttr('Named Credential', 
        'Named_Credential', 'DFOCalloutMockCreds', true, 'String');
 
    private static final industriesintegrationfwk.ApexProviderAttr CALLBACK_URL_ATTR = 
        new industriesintegrationfwk.ApexProviderAttr('Callback URL', 
        'Callback_URL', 'DFOCallbackUrl', true, 'String');

    global static List<industriesintegrationfwk.ApexProviderAttr> getProviderAttributes() {
        List<industriesintegrationfwk.ApexProviderAttr> defaults = new List<industriesintegrationfwk.ApexProviderAttr>();
        defaults.add(NAMED_CRED_ATTR);
        defaults.add(CALLBACK_URL_ATTR);
     
        return defaults;
    }
```

                
    - Specify the Fulfillment Step ID as the value of the `requestGuid` parameter of the `executeCallout` method. You can also extract the Step ID from the
                    `CorrelationId` key value. For example,
                    `"callout:13Wxx0000004CAf:"`.

Here's a
                    sample payload that assigns the provider attribute
                  values.

public interface ProcessIntegrationProvider {
    IntegrationCalloutResponse executeCallout(String requestGuid, 
    String inputRecordId, String payload, Map<String, Object> attributes);

    List<ProviderAttr> getProviderAttributes();
}
```

              

            

            
  - Set response code to 202 to indicate that the callout is asynchronously executed and
              in `Processing` state.

Here's a sample payload
                that sets the response
              code.

global with sharing class DFOAsyncApexSample implements industriesintegrationfwk.ProcessIntegrationProvider {
...
IntegrationCalloutResponse executeCallout(String requestGuid, 
    String inputRecordId, String payload, Map<String, Object> attributes){
    // execute http request
    ...
    // set accepted if no failures
    IntegrationCalloutResponse acceptedResponse = 
        new IntegrationCalloutResponse(true);
    acceptedResponse.setResponseCode(202);
    
    return new IntegrationCalloutResponse();
    }
}

```

            
  - The callback URI is visible in the integration definition.
                
              

          

        
- Extract the step ID from the request. Find the Fulfillment Step ID in the org by using
          the extracted step ID and update the Fulfillment Step state to `Completed`.

```
FulfillmentStep step = new FulfillmentStep(id = 'stepId', State = 'Completed'); 
upsert step;
```

=== ARTICLE: dynamic_revenue_orchestrator_callout_configuration_steps.htm ===
---
page_id: dynamic_revenue_orchestrator_callout_configuration_steps.htm
title: Configure Callout Settings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_callout_configuration_steps.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configure Callout Settings

Before you set up a callout provider, configure the callout settings. The settings
  include the creation of a named credential and an external credential, the creation of an
  integration definition, and the configuration of a fulfillment step definition.

  
   

Meet these prerequisites before you configure the callout settings.

   

     
      
       

      

     

    
| Available in: **Developer**, **Enterprise**, and **Unlimited** Editions |
| --- |

  

   

     
     
     
      
       

      

     

     
      
       

       

      

     

    
| User Permissions Needed |  |
| --- | --- |
| To create authenticated callouts: | External Credentials Principal Access Permission |

  

  

- 
    Configure named and external credentials to define access to an external system. Specify a
     named credential as the callout endpoint and an external credential to configure the
     authentication protocol.
    See [Create Named
      Credentials and External Credentials](https://help.salesforce.com/s/articleView?id=xcloud.nc_named_creds_and_ext_creds.htm&type=5&language=en_US).
   

- 
    Create integration definitions to connect Salesforce with an external system. Integration
     definitions use APIs to perform operations in both Salesforce and the external system. You can
     create Apex Defined, External Services Defined, or Standard integration definitions.
    See [Create an
      Integration Definition](https://help.salesforce.com/s/articleView?id=ind.consumption_framework_integration_definitions.htm&type=5&language=en_US).
   

- 
    Define a fulfillment step with `Callout` as the step
     type. Additionally, set the integration definition name and integration user.
    See [Callout Fulfillment
      Step](https://help.salesforce.com/s/articleView?id=ind.dro_callout.htm&type=5&language=en_US).

=== ARTICLE: dynamic_revenue_orchestrator_callouts_overview.htm ===
---
page_id: dynamic_revenue_orchestrator_callouts_overview.htm
title: Callouts in Dynamic Revenue Orchestrator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_callouts_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Callouts in Dynamic Revenue Orchestrator

Use callout step types to make ‌HTTP calls to an external system. Callout step types
    use the Data Consumption Framework and Process Type Integration for interface management and
    communication with external systems.

    

Use callout step types to implement these features.

    
      
- Endpoint configuration

      
- Authentication parameters

      
- Default sync and async implementation

      
- Extensions or Apex Interfaces

      
- Error handling and fallout management

      
- Request and response logging

      
- Timeouts

    

    

Dynamic Revenue Orchestrator supports these types of callouts.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

          
            

            

          

        

      
| Type | Description |
| --- | --- |
| Standard Fulfillment Provider | Use this callout provider to use a fixed payload structure to request an order. You can also define Omnistudio Integration Procedures for request transformation and response handling. |
| Apex Type Provider | Use this callout provider to implement custom integration scenarios via the `industriesintegrationfwk.ProcessIntegrationProvider ` Apex interface. |
| External Services Defined Provider | Use this callout provider to implement custom integration scenarios via external services through the OpenAPI specification. You can also define Omnistudio Integration Procedures for request transformation and response handling. To use this callout, the Omnistudio Admin and Omnistudio Runtime permissions are required. |

    

Callouts support these integration patterns.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

        

      
| Type | Description |
| --- | --- |
| Sync | The callout step is completed when the external system returns a response. |
| Async | The callout step is set to `In Progress` when the external system returns the acknowledgment response with 202 HTTP code. The system waits until the external system sends a callback response to complete the callout step. See [Asynchronous Interaction Pattern](./dynamic_revenue_orchestrator_async_interaction_pattern.htm.md). |

  

- 
**[Configure Callout Settings](./dynamic_revenue_orchestrator_callout_configuration_steps.htm.md)**  

Before you set up a callout provider, configure the callout settings. The settings   include the creation of a named credential and an external credential, the creation of an   integration definition, and the configuration of a fulfillment step definition.

- 
**[Standard Fulfillment Provider](./dynamic_revenue_orchestrator_default_order_fulfillment_provider.htm.md)**  

The Standard Fulfillment Provider or `CalloutIntegrationProvider` is a provider for the order fulfillment usage type. A     Fulfillment Designer can configure this provider.

- 
**[Apex Type Provider](./dynamic_revenue_orchestrator_apex_type_provider.htm.md)**  

Implement custom integration logic via Apex by using the Apex Type Provider. This     provider requires an Apex Integration Developer to implement a custom Apex adapter     interface.

- 
**[External Services Defined Provider](./dynamic_revenue_orchestrator_external_services_defined_provider.htm.md)**  

Generate interface contract and Apex types by using external services and Open API     compatible schema.

- 
**[Asynchronous Interaction Pattern](./dynamic_revenue_orchestrator_async_interaction_pattern.htm.md)**  

To specify an asynchronous request, you must add the callback URI to the integration     definition for Standard Fulfillment Provider or Apex Type Provider as an optional     attribute.

- 
**[Input and Output Transformation Processors](./dynamic_revenue_orchestrator_input_output_processors.htm.md)**  

Use input and output processors to process a standard fulfillment request before     sending it to an external system.

#### See Also

- [*Salesforce Help*: Data Consumption Framework](https://help.salesforce.com/s/articleView?id=ind.consumption_framework.htm&type=5&language=en_US)

=== ARTICLE: dynamic_revenue_orchestrator_default_order_fulfillment_provider.htm ===
---
page_id: dynamic_revenue_orchestrator_default_order_fulfillment_provider.htm
title: Standard Fulfillment Provider
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_default_order_fulfillment_provider.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standard Fulfillment Provider

The Standard Fulfillment Provider or `CalloutIntegrationProvider` is a provider for the order fulfillment usage type. A
    Fulfillment Designer can configure this provider.

    

The Standard Fulfillment Provider includes these features.

    
      
- Predefined payload with sales transaction items and fulfillment items data, including
        attribute values

      
- Fixed integration parameters such as timeouts, credentials, encoding styles, and path. See
          [Integration Definition for Standard
          Fulfillment Provider](./dro_integration_definition_for_standard_fulfillment_provider.htm.md) for details about the integration parameters.

      
- Modified requests and responses via Omnistudio Integration Procedures

      
- Asynchronous interaction pattern. See [Asynchronous Interaction Pattern](./dynamic_revenue_orchestrator_async_interaction_pattern.htm.md).

      
- Request and response logging

      
- Error handling and retry policies. See [Fallout Design and
        Management](https://help.salesforce.com/s/articleView?id=ind.dro_fallout_design_and_management.htm&language=en_US).

      
- Request transformation and response handling via integration procedures

    

    

To ‌configure the callout settings for Standard Fulfillment Provider, see [Configuration Steps](./dynamic_revenue_orchestrator_callout_configuration_steps.htm.md).

    

## Request Payload

This example shows a sample request payload structure
        with data for sales transaction items and fulfillment transaction items. This data is
        derived using context definition mappings that are defined through settings. See [Context Definitions in Order
          Orchestration](https://help.salesforce.com/s/articleView?id=ind.dro_use_context_definitions.htm&language=en_US).

```
{
  "AccountId": "001xx000003GbsxAAC",
  "OrderId": "801xx000003GbsyAAC",
  "StepId": "802xx000001ndnyAAA",
  "PlanSourceId": "802xx000001ndnyAAA",
  "StepSourceId": "13Wxx0000004Cdh",
  "CorrelationId": "callout:13Wxx0000004Cdh:",
  "SalesTransactionItems": [
    {
      "ArePartialPeriodsAllowed": "false",
      "ParentReference": "801xx000003GbsyAAC",
      "IsAssetizable": "true",
      "ProductName": "iPhone18",
      "ProductCode": "iPhone18",
      "SalesTransactionItemParent": "801xx000003GbsyAAC",
      "Attributes": [
        {
          "AttributeKey": "0tjxx00000000ePAAQ",
          "ParentReference": "802xx000001ndnxAAA",
          "AttributeValue": "true",
          "AttributeName": "IsDeliveryNotificationNeeded",
          "AttributeDefinitionCode": "FDT5",
          "SalesTransactionItemAttrParent": "802xx000001ndnxAAA"
        },
        {
          "AttributeKey": "0tjxx00000000eNAAQ",
          "ParentReference": "802xx000001ndnxAAA",
          "AttributeValue": "10",
          "AttributeName": "FDTCharge",
          "AttributeDefinitionCode": "FDT3",
          "SalesTransactionItemAttrParent": "802xx000001ndnxAAA"
        }
      ],
      "Product": "01txx0000006igoAAA",
      "Quantity": "1.0",
      "ListPrice": "1.0",
      "ItemTotalAdjustmentAmount": "0.0",
      "SalesTransactionItemSource": "802xx000001ndnxAAA",
      "PricebookEntry": "01uxx0000008zT8AAI",
      "StartDate": "2024-10-15T00:00:00.000Z",
      "UnitPrice": "1.0",
      "RoundedLineAmount": "1.0",
      "EndQuantity": "1.0",
      "TotalTaxAmount": "0.0",
      "IsItemLocked": "false",
      "TotalPrice": "1.0",
      "ProductBasedOn": "11Bxx000002C9M2EAK",
      "SalesTransactionActionType": "Add",
      "SalesTransactionAction": "8OAxx0000004DGOGA2"
    },
    {
      "ArePartialPeriodsAllowed": "false",
      "ParentReference": "801xx000003GbsyAAC",
      "IsAssetizable": "true",
      "ProductName": "iPhone19",
      "ProductCode": "iPhone19",
      "SalesTransactionItemParent": "801xx000003GbsyAAC",
      "Attributes": [
        {
          "AttributeKey": "0tjxx00000000eQAAQ",
          "ParentReference": "802xx000001ndnyAAA",
          "AttributeValue": "false",
          "AttributeName": "IsDelivered",
          "AttributeDefinitionCode": "FDT6",
          "SalesTransactionItemAttrParent": "802xx000001ndnyAAA"
        }
      ],
      "Product": "01txx0000006igpAAA",
      "Quantity": "1.0",
      "ListPrice": "1.0",
      "ItemTotalAdjustmentAmount": "0.0",
      "SalesTransactionItemSource": "802xx000001ndnyAAA",
      "PricebookEntry": "01uxx0000008zTAAAY",
      "StartDate": "2024-10-20T00:00:00.000Z",
      "UnitPrice": "1.0",
      "RoundedLineAmount": "1.0",
      "EndQuantity": "1.0",
      "TotalTaxAmount": "0.0",
      "IsItemLocked": "false",
      "TotalPrice": "1.0",
      "ProductBasedOn": "11Bxx000002C9M2EAK",
      "SalesTransactionActionType": "Add",
      "SalesTransactionAction": "8OAxx0000004DGOGA2",
      "SalesTrxnItemDescription": "TrackingRef:TRK-HUBSWQT18-4238"
    }
  ],
  "FulfillmentTransactionItems": [
    {
      "ParentReference": "0a3xx00000000JOAAY",
      "OriginalQuantity": "2.0",
      "FulfillmentItemSource": "0a4xx00000000JOAAY",
      "Attributes": [
        {
          "FulfillmentOrderLineId": "0a4xx00000000JOAAY",
          "LineAttributeDefinitionCode": "FDT6",
          "ParentReference": "0a4xx00000000JOAAY",
          "LineAttributeName": "IsDelivered",
          "LineAttributeValue": "false",
          "LineAttributeKey": "0tjxx00000000eQAAQ"
        },
        {
          "FulfillmentOrderLineId": "0a4xx00000000JOAAY",
          "LineAttributeDefinitionCode": "FDT2",
          "ParentReference": "0a4xx00000000JOAAY",
          "LineAttributeName": "FDTColor",
          "LineAttributeKey": "0tjxx00000000eMAAQ"
        },
        {
          "FulfillmentOrderLineId": "0a4xx00000000JOAAY",
          "LineAttributeDefinitionCode": "FDT1",
          "ParentReference": "0a4xx00000000JOAAY",
          "LineAttributeName": "FDTSize",
          "LineAttributeKey": "0tjxx00000000eLAAQ"
        }
      ],
      "FulfillmentItemAction": "ADD",
      "FulfillmentItemProductCode": "iPhone-Pack",
      "FulfillmentOrderItemQuantity": "2.0",
      "FulfillmentItemProductName": "iPhone-Pack",
      "FulfillmentOrderId": "0a3xx00000000JOAAY",
      "FulfillmentItemTypeCode": "Product",
      "FulfillmentItemType": "Order Product",
      "FulfillmentOrderNumber": "FO-0002",
      "FulfillmentItemStartDate": "2024-10-20T00:00:00.000Z",
      "FulfillmentItemProductId": "01txx0000006igqAAA"
    },
    {
      "ParentReference": "0a3xx00000000JNAAY",
      "OriginalQuantity": "2.0",
      "FulfillmentItemSource": "0a4xx00000000JNAAY",
      "Attributes": [
        {
          "FulfillmentOrderLineId": "0a4xx00000000JNAAY",
          "LineAttributeDefinitionCode": "FDT2",
          "ParentReference": "0a4xx00000000JNAAY",
          "LineAttributeName": "FDTColor",
          "LineAttributeKey": "0tjxx00000000eMAAQ"
        },
        {
          "FulfillmentOrderLineId": "0a4xx00000000JNAAY",
          "LineAttributeDefinitionCode": "FDT5",
          "ParentReference": "0a4xx00000000JNAAY",
          "LineAttributeName": "IsDeliveryNotificationNeeded",
          "LineAttributeValue": "false",
          "LineAttributeKey": "0tjxx00000000ePAAQ"
        },
        {
          "FulfillmentOrderLineId": "0a4xx00000000JNAAY",
          "LineAttributeDefinitionCode": "FDT3",
          "ParentReference": "0a4xx00000000JNAAY",
          "LineAttributeName": "FDTCharge",
          "LineAttributeKey": "0tjxx00000000eNAAQ"
        }
      ],
      "FulfillmentItemAction": "ADD",
      "FulfillmentItemProductCode": "iPhone-Tech",
      "FulfillmentOrderItemQuantity": "2.0",
      "FulfillmentItemProductName": "iPhone-Tech",
      "FulfillmentOrderId": "0a3xx00000000JNAAY",
      "FulfillmentItemTypeCode": "Product",
      "FulfillmentItemType": "Order Product",
      "FulfillmentOrderNumber": "FO-0001",
      "FulfillmentItemStartDate": "2024-10-10T00:00:00.000Z",
      "FulfillmentItemProductId": "01txx0000006igrAAA"
    }
  ]
}
```

The step source ID of the fulfillment step, which is either a related
        order or fulfillment item, determines the payload composition with these considerations.

        
- If the step source ID is an order item, then all order items of the order are included
          in the payload under the SalesTransactionItems node.

        
- If the step source ID is a fulfillment item, then all fulfillment items of the
          fulfillment order are included in the payload under the FulfillmentTransactionItems
          node.

        
- If a product attribute doesn't have a defined code, then the attribute is excluded from
          the payload.

      

    

## Considerations

      
      

Keep these considerations in mind for the request payload.

      
        
- The maximum request payload size limit is 12 MB. 

        
- The default timeout period is five seconds, and the maximum timeout period is 120
          seconds.

        
- The encoding style for fulfillment order line items, sales transaction items, and
          attributes can be configured through the [Integration Definition for Standard
            Fulfillment Provider](./dro_integration_definition_for_standard_fulfillment_provider.htm.md).

      

    

    

## Error Handling

      
      

To verify if the callout request was successful, check the `status` value in the payload. If the status is undefined, then these HTTP codes
        indicate ‌a successful response.

      
        
- `200`

        
- `201`

        
- `202`

        
- `203`

        
- `204`

        
- `205`

        
- `206`

        
- `302`

        
- `304`

      

      

If the request isn't successful, then the fulfillment step state is marked as `Fatally Failed`.

    

    

## Integration Definition Configurations

      
      

You can configure these additional features for the integration definition.

      
        
- 
          

Select the
              **Save
              the request and response as attachments to the record** checkbox for the
            integration definition to save request and response payloads as attachments to the
            Integration Provider Execution record. Content publish limits apply when saving request
            and response payloads as attachments. Use [Shield
              Platform Encryption](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_overview.htm&type=5&language=en_US) for secure storage of sensitive information.

        

        
- 
[Define Input and Output Processors
            for the Integration Definition](./dynamic_revenue_orchestrator_input_output_processors.htm.md) for the pre-processing of the standard fulfillment
          request before you send the request to an external system. See [Omnistudio
            Integration Procedures](https://help.salesforce.com/s/articleView?id=xcloud.os_omnistudio_integration_procedures_48334.htm&type=5&language=en_US).

      

      

See [Create an
          Integration Definition](https://help.salesforce.com/s/articleView?id=ind.consumption_framework_integration_definitions.htm&type=5&language=en_US).

    

  

- 
**[Integration Definition for Standard Fulfillment Provider](./dro_integration_definition_for_standard_fulfillment_provider.htm.md)**  

Use supported attribute values of an integration definition for a Standard Fulfillment     Provider to implement features as per your requirement.

=== ARTICLE: dynamic_revenue_orchestrator_events_parent.htm ===
---
page_id: dynamic_revenue_orchestrator_events_parent.htm
title: Dynamic Revenue Orchestrator Platform Events
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_events_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator Platform Events

Salesforce publishes standard platform events in response to an action that occurred in
    the org or to report errors.

- 
**[FulfillmentSourceChangeEvent](./sforce_api_objects_fulfillmentsourcechangeevent.htm.md)**  

       Notifies updates to the sources orchestrated by Dynamic Revenue Orchestrator          like order product or fulfillment order product. This object is available in API       version 66.0 and later. 

- 
**[SalesTrxnDecompositionEvent](./sforce_api_objects_salestrxndecompositionevent.htm.md)**  

       Notifies when the decomposition process status changes. This object is       available in API version 66.0 and later.

=== ARTICLE: dynamic_revenue_orchestrator_external_services_defined_provider.htm ===
---
page_id: dynamic_revenue_orchestrator_external_services_defined_provider.htm
title: External Services Defined Provider
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_external_services_defined_provider.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# External Services Defined Provider

Generate interface contract and Apex types by using external services and Open API
    compatible schema.

    

To ‌configure the callout settings for External Services Defined Provider, see [Configuration Steps](./dynamic_revenue_orchestrator_callout_configuration_steps.htm.md).

    

​​As an integration specialist user or admin user, perform these steps.

    
      
- Set up an external service and actions.

      
- In the external service definition, include integration parameters such as error codes,
        credentials, and path.

    

    

## External Service

      
      

Use external services for outbound integrations from Salesforce by using low-code,
        process-based integrations to enhance your Apex integrations. See [External Services](https://help.salesforce.com/s/articleView?id=platform.external_services.htm&type=5&language=en_US).

    

    

## Integration Definition Configurations

      
      

You can configure these additional features for the integration definition.

      
        
- 
          

Select the
              **Save
              the request and response as attachments to the record** checkbox for the
            integration definition to save request and response payloads as attachments to the
            Integration Provider Execution record. Content publish limits apply when saving request
            and response payloads as attachments. Use [Shield
              Platform Encryption](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_overview.htm&type=5&language=en_US) for secure storage of sensitive information.

        

        
- 
[Define Input and Output Processors
            for the Integration Definition](./dynamic_revenue_orchestrator_input_output_processors.htm.md) for the pre-processing of the standard fulfillment
          request before you send the request to an external system. See [Omnistudio
            Integration Procedures](https://help.salesforce.com/s/articleView?id=xcloud.os_omnistudio_integration_procedures_48334.htm&type=5&language=en_US).

      

      

See [Create an
          Integration Definition](https://help.salesforce.com/s/articleView?id=ind.consumption_framework_integration_definitions.htm&type=5&language=en_US).

    

    

## Step Definition

      
      

Set the created integration definition on the Step Definition record with `Callout` as the step type.

=== ARTICLE: dynamic_revenue_orchestrator_flow_metadata_api.htm ===
---
page_id: dynamic_revenue_orchestrator_flow_metadata_api.htm
title: Flow for Dynamic Revenue Orchestrator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Dynamic Revenue Orchestrator

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Dynamic Revenue Orchestrator exposes additional actionType values for the FlowActionCall
        Metadata type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 
- 
- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Dynamic Revenue Orchestrator include: `decomposeSalesTransaction`—Decompose a sales transaction, such as a quote, order, or order summary. `freezeSalesTransaction`—Freeze a sales transaction to disable the modification of a line item. `getPointOfNoReturn`—Get details about the point of no return milestone for each line item in a sales transaction. `orchestrateSalesTransaction`—Initiate the orchestration process for a sales transaction. `orchestrateTransaction`—Orchestrate a transaction for any domain-specific object, such as a collection plan for Revenue billing, that requires the composition and execution of a fulfillment plan. `submitOrder`—Submit an order to Dynamic Revenue Orchestrator (DRO) for fulfillment. `submitSalesTransaction`—Initiate the fulfillment process of any sales transaction, such as a quote, an order, or an order summary. `unfreezeSalesTransaction`—Unfreeze a sales transaction to enable the modification of a line item. |

=== ARTICLE: dynamic_revenue_orchestrator_input_output_processors.htm ===
---
page_id: dynamic_revenue_orchestrator_input_output_processors.htm
title: Input and Output Transformation Processors
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_input_output_processors.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_callouts_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Input and Output Transformation Processors

Use input and output processors to process a standard fulfillment request before
    sending it to an external system.

    

## Prerequisites

      
      
        
- Omnistudio license is required.

        
- Omnistudio Admin permission set license is assigned to Integration Configuration User
          (Fulfillment Designer).

        
- The input and output procedure attributes of an integration definition, which are
          available from Setup, are assigned with the Omnistudio Integration Procedure request and
          response. You can use `Type_Subtype` or `Id` of OmniProcess as the values for attributes.

      

      

When a callout step is executed, these steps are followed.

      
        
- The defined integration procedures are identified for request and response handling from
          an integration definition.

        
- The input processor generates the request by using `Fulfillment Step Source > SourceIdentifier` as the `InputRecordId` input parameter value. For example, the ID of an order
          item.

        
- The output processor handles the response by passing a map to the Integration Procedure
          service. The results from the Integration Procedure are used to identify any errors and
          details are passed to Dynamic Revenue Orchestrator.

=== ARTICLE: dynamic_revenue_orchestrator_invocable_actions_parent.htm ===
---
page_id: dynamic_revenue_orchestrator_invocable_actions_parent.htm
title: Dynamic Revenue Orchestrator Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator Standard Invocable Actions

Use standard invocable actions to submit an order or a sales transaction to Dynamic
    Revenue Orchestrator (DRO) for fulfillment.

- 
**[Decompose Sales Transaction Action](./actions_obj_decompose_sales_transaction.htm.md)**  

Decompose a sales transaction, such as a quote, order, or             order summary.

- 
**[Freeze Sales Transaction Action](./actions_obj_freeze_sales_transaction.htm.md)**  

Freeze a sales transaction to disable the modification of a line             item.

- 
**[Get Point Of No Return Action](./actions_obj_get_point_of_no_return.htm.md)**  

Get details about the point of no return milestone for each line             item in a sales transaction.

- 
**[Orchestrate Sales Transaction Action](./actions_obj_orchestrate_sales_transaction.htm.md)**  

Initiate the orchestration process for a sales             transaction. This action executes only the plan composition and orchestration         phases, without performing decomposition.

- 
**[Orchestrate Transaction Action](./actions_obj_orchestrate_transaction.htm.md)**  

Orchestrate a transaction for any             domain-specific object, such as a collection plan for Revenue billing, that requires the             composition and execution of a fulfillment plan.

- 
**[Submit Order Action](./actions_obj_submit_order.htm.md)**  

Submit an order to Dynamic Revenue Orchestrator (DRO) for 			fulfillment.

- 
**[Submit Sales Transaction Action](./actions_obj_submit_sales_transaction.htm.md)**  

Initiate the fulfillment process of any sales transaction, such as a             quote, an order, or an order summary.

- 
**[Unfreeze Sales Transaction Action](./actions_obj_unfreeze_sales_transaction.htm.md)**  

Unfreeze a sales transaction to enable the modification of a line             item.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

=== ARTICLE: dynamic_revenue_orchestrator_metadata_api_parent.htm ===
---
page_id: dynamic_revenue_orchestrator_metadata_api_parent.htm
title: Dynamic Revenue Orchestrator Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Dynamic Revenue Orchestrator](./dynamic_revenue_orchestrator_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

- 
**[DynamicFulfillmentOrchestratorSettings](./meta_dynamicfulfillmentorchestratorsettings.htm.md)**  

Represents the settings for Dynamic 			Revenue Orchestrator. 	

- 
**[OrchestrationPlanCtxMapping](./meta_orchestrationplanctxmapping.htm.md)**  

Represents the context mapping that Dynamic 			Revenue Orchestrator (DRO) uses to generate and orchestrate a plan for an object, such 			as a non-sales transaction for billing or another generic business process. 	

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: dynamic_revenue_orchestrator_overview.htm ===
---
page_id: dynamic_revenue_orchestrator_overview.htm
title: Dynamic Revenue Orchestrator
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator

Get visibility into a product’s fulfillment journey. Also, get a complete view of the
  entire fulfillment design that includes processes such as order decomposition, fulfillment plans,
  and jeopardy management.

  

    
     
      

     

    

   
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions |
| --- |

  

 

- 
**[Dynamic Revenue Orchestrator Standard Objects](./dynamic_revenue_orchestrator_std_objects_parent.htm.md)**  

The Dynamic Revenue Orchestrator data model provides objects and fields to manage   details of a product’s fulfillment.

- 
**[Dynamic Revenue Orchestrator Standard Invocable Actions](./dynamic_revenue_orchestrator_invocable_actions_parent.htm.md)**  

Use standard invocable actions to submit an order or a sales transaction to Dynamic     Revenue Orchestrator (DRO) for fulfillment.

- 
**[Dynamic Revenue Orchestrator Metadata API Types](./dynamic_revenue_orchestrator_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Dynamic Revenue Orchestrator Tooling API Objects](./dynamic_revenue_orchestrator_tooling_api_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

- 
**[Callouts in Dynamic Revenue Orchestrator](./dynamic_revenue_orchestrator_callouts_overview.htm.md)**  

Use callout step types to make ‌HTTP calls to an external system. Callout step types     use the Data Consumption Framework and Process Type Integration for interface management and     communication with external systems.

- 
**[Dynamic Revenue Orchestrator Platform Events](./dynamic_revenue_orchestrator_events_parent.htm.md)**  

Salesforce publishes standard platform events in response to an action that occurred in     the org or to report errors.

=== ARTICLE: dynamic_revenue_orchestrator_std_objects_parent.htm ===
---
page_id: dynamic_revenue_orchestrator_std_objects_parent.htm
title: Dynamic Revenue Orchestrator Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator Standard Objects

The Dynamic Revenue Orchestrator data model provides objects and fields to manage
  details of a product’s fulfillment.

- 
**[AssetFulfillmentDecomp](./sforce_api_objects_assetfulfillmentdecomp.htm.md)**  

Represents the relationship between an ordered asset and its          corresponding fulfillment asset. This object is available in API version 62.0 and       later.

- 
**[FulfillmentAsset](./sforce_api_objects_fulfillmentasset.htm.md)**  

Represents an instance of a technical product used to provide a          customer asset. This object is available in API version 61.0 and later.

- 
**[FulfillmentAssetAttribute](./sforce_api_objects_fulfillmentassetattribute.htm.md)**  

Represents an attribute of a fulfillment asset. This object is       available in API version 61.0 and later.

- 
**[FulfillmentAssetRelationship](./sforce_api_objects_fulfillmentassetrelationship.htm.md)**  

Represents a relationship between two fulfillment assets. This       object is available in API version 61.0 and later.

- 
**[FulfillmentAssetStatePeriod](./sforce_api_objects_fulfillmentassetstateperiod.htm.md)**  

       Represents the period during which the fulfillment asset configuration is          applicable. This object is available in API version 67.0 and later. 

- 
**[FulfmtAssetStatePeriodAttr](./sforce_api_objects_fulfillmentassetstateperiodattribute.htm.md)**  

       Represents the key-value pair of a fulfillment asset attribute applicable          during a specific asset state period. This object is available in API version 67.0 and       later. 

- 
**[FulfillmentFalloutRule](./sforce_api_objects_fulfillmentfalloutrule.htm.md)**  

Represents the fulfillment fallout handling rule. This object is       available in API version 61.0 and later.

- 
**[FulfillmentLineAttribute](./sforce_api_objects_fulfillmentlineattribute.htm.md)**  

Represents an attribute of a fulfillment order line. This object       is available in API version 61.0 and later.

- 
**[FulfillmentLineRel](./sforce_api_objects_fulfillmentlinerel.htm.md)**  

Represents a relationship between two fulfillment order lines.       This object is available in API version 61.0 and later.

- 
**[FulfillmentLineSourceRel](./sforce_api_objects_fulfillmentlinesourcerel.htm.md)**  

Represents the relationship between a fulfillment order line and its          decomposition source. This object is available in API version 61.0 and       later.

- 
**[FulfillmentPlan](./sforce_api_objects_fulfillmentplan.htm.md)**  

Represents a set of steps to be created to fulfill the order.       This object is available in API version 61.0 and later.

- 
**[FulfillmentStep](./sforce_api_objects_fulfillmentstep.htm.md)**  

Represents a task that's required to perform a certain action as part          of order fulfillment. This task can be manual or automated. This object is available       in API version 61.0 and later.

- 
**[FulfillmentStepDefinition](./sforce_api_objects_fulfillmentstepdefinition.htm.md)**  

Represents a definition of a step that must be executed during          fulfillment orchestration. This object is available in API version 61.0 and       later.

- 
**[FulfillmentStepDefinitionGroup](./sforce_api_objects_fulfillmentstepdefinitiongroup.htm.md)**  

Represents a set of fulfillment step definitions. This object is       available in API version 61.0 and later.

- 
**[FulfillmentStepDependency](./sforce_api_objects_fulfillmentstepdependency.htm.md)**  

Represents a dependency between tasks by defining the order between a          task and one that depends on it. This object is available in API version 61.0 and       later.

- 
**[FulfillmentStepDependencyDef](./sforce_api_objects_fulfillmentstepdependencydef.htm.md)**  

Represents a dependency that must be created between two fulfillment          step records. This object is available in API version 62.0 and later.

- 
**[FulfillmentStepJeopardyRule](./sforce_api_objects_fulfillmentstepjeopardyrule.htm.md)**  

Represents the duration and tolerance for the step in the fulfillment          process to allow the overall tracking of rules and risks. This object is available in       API version 61.0 and later.

- 
**[FulfillmentStepSource](./sforce_api_objects_fulfillmentstepsource.htm.md)**  

Represents a link between a fulfillment step and the corresponding          order lines. This object is available in API version 61.0 and later.

- 
**[FulfillmentTaskAssignmentRule](./sforce_api_objects_fulfillmenttaskassignmentrule.htm.md)**  

Represents a set of actions that assign a task to a user or          queue. This object is available in API version 63.0 and later.

- 
**[FulfillmentWorkspace](./sforce_api_objects_fulfillmentworkspace.htm.md)**  

Represents a visual designer for fulfillment plans that can have          multiple step groups and their dependencies. This object is available in API version       61.0 and later.

- 
**[FulfillmentWorkspaceItem](./sforce_api_objects_fulfillmentworkspaceitem.htm.md)**  

Represents information about the attributes that are used in the          definition for a fulfillment step group. This object is available in API version 61.0       and later.

- 
**[ProductDecompEnrichmentRule](./sforce_api_objects_productdecompenrichmentrule.htm.md)**  

       Represents mappings between fields and attributes. Enrichment rules are part          of a decomposition rule, and are used to propagate data to fulfillment order lines.       This object is available in API version 61.0 and later. 

- 
**[ProdtDecompEnrchVarMap](./sforce_api_objects_prodtdecompenrchvarmap.htm.md)**  

       Represents the mapping of a field context tag or an attribute to a variable          within an expression set. This object is available in API version 64.0 and later. 

- 
**[ProductFulfillmentDecompRule](./sforce_api_objects_productfulfillmentdecomprule.htm.md)**  

Represents a rule that determines how an order is broken into          sub-orders with specific technical details that help in order fulfillment. It can be          applied to a commercial or a technical product. This object is available in API       version 61.0 and later.

- 
**[ProductFulfillmentScenario](./sforce_api_objects_productfulfillmentscenario.htm.md)**  

Represents a link between a product and the corresponding group of          fulfillment steps that's necessary to fulfill that product. This object is available       in API version 61.0 and later.

- 
**[SalesTrxnDeleteEvent](./sforce_api_objects_salestrxndeleteevent.htm.md)**  

       Represents the platform event that triggers the deletion of sales transaction          fulfillment request records when the corresponding reference records are deleted. This       object is available in API version 64.0 and later. 

- 
**[SalesTransactionFulfillReq](./sforce_api_objects_salestransactionfulfillreq.htm.md)**  

       Represents the statuses of all the sub-orders that belong to the selected          commercial or technical product. This object is available in API version 62.0 and       later. 

- 
**[ValTfrm](./sforce_api_objects_valtfrm.htm.md)**  

Represents mappings between fields and attributes. Enrichment rules          are part of a decomposition rule, and are used to propagate data to fulfillment order          lines. This object is available in API version 61.0 and later.

- 
**[ValTfrmGrp](./sforce_api_objects_valtfrmgrp.htm.md)**  

Represents a rule that determines how an order is broken into          sub-orders with specific technical details that help in order fulfillment. The rule can be          applied to a commercial or a technical product. This object is available in API       version 61.0 and later.

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: dynamic_revenue_orchestrator_tooling_api_parent.htm ===
---
page_id: dynamic_revenue_orchestrator_tooling_api_parent.htm
title: Dynamic Revenue Orchestrator Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_tooling_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Dynamic Revenue Orchestrator Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

- 
**[CustomFulfillmentScopeCnfg](./tooling_api_objects_customfulfillmentscopecnfg.htm.md)**  

       Represents a user-defined scope to define and customize scope-specific          validation and orchestration for flexible fulfillment. This object is available in API       version 64.0 and later.

- 
**[OrchestrationPlanCtxMapping](./tooling_api_objects_orchestrationplanctxmapping.htm.md)**  

Represents an orchestration plan context mapping entry in the org.          This entry is used to connect the business data in an object to the orchestration logic          within Dynamic Revenue Orchestrator (DRO) by using the orchestration type. This object       is available in API version 66.0.0 and later.

#### See Also

- [*Tooling API Developer Guide*: Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

=== ARTICLE: meta_dynamicfulfillmentorchestratorsettings.htm ===
---
page_id: meta_dynamicfulfillmentorchestratorsettings.htm
title: DynamicFulfillmentOrchestratorSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_dynamicfulfillmentorchestratorsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DynamicFulfillmentOrchestratorSettings

Represents the settings for Dynamic
			Revenue Orchestrator.
	

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

DynamicFulfillmentOrchestratorSettings values are stored in the
					DynamicFulfillmentOrchestratorSettings.settings file in the
					settings folder. The .settings files
				are different from other named components, because there is only one settings file
				for each settings component.

	

	

## Version

		
		

DynamicFulfillmentOrchestratorSettings components are available in API version 61.0 and
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

				

				

			
| Field Name | Description |
| --- | --- |
| enableDFOFallout | **Field Type** boolean **Description** Indicates whether to enable fallout management to handle fallouts and retry policies (`true`) or not (`false`). The default value is `false`. See [Turn On Feature to Manage Fallout](https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_features_to_manage_fallout_and_service_level_agreements.htm&language=en_US). |
| enableDFOJeopardy | **Field Type** boolean **Description** Indicates whether to enable management of Service Level Agreements (`true`) or not (`false`). The default value is `false`. See [Turn On Feature to Manage Service Level Agreements](https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_features_to_manage_fallout_and_service_level_agreements.htm&language=en_US). |
| enableDFOPref | **Field Type** boolean **Description** Indicates whether to enable features of Dynamic Revenue Orchestrator (`true`) or not (`false`). The default value is `false`. See [Turn On Dynamic Revenue Orchestrator](https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_dynamic_revenue_orchestrator.htm&language=en_US). |
| enableDROFutureDatedTasks | **Field Type** boolean **Description** Indicates whether to enable the Future Dated Steps feature (`true`) or not (`false`). The default value is `false`. See [Enable Future Dated Steps](https://help.salesforce.com/s/articleView?id=ind.enable_future_dated_steps.htm&language=en_US). Available in API version 63.0 and later. |
| enableDROInflightRequest | **Field Type** boolean **Description** Indicates whether to allow changes to fulfillment requests that are in progress (`true`) or not (`false`). The default value is `false`. Available in API version 64.0 and later. |
| enableDROTaskSource | **Field Type** boolean **Description** Indicates whether to link a Salesforce manual task to a fulfillment step source (`true`) or not (`false`). The default value is `false`. See [Enable the Linking of Task to Step Source](https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_feature_to_link_task_to_step_source.htm&language=en_US). Available in API version 63.0 and later. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a DynamicFulfillmentOrchestratorSettings component.

			

```
<DynamicFulfillmentOrchestratorSettings xmlns="http://soap.sforce.com/2006/04/metadata">
     <enableDFOPref>true</enableDFOPref>
     <enableDFOFallout>true</enableDFOFallout>
     <enableDFOJeopardy>true</enableDFOJeopardy>
     <enableDROFutureDatedTasks>true</enableDROFutureDatedTasks>
     <enableDROInflightRequest>true</enableDROInflightRequest>
     <enableDROTaskSource>true</enableDROTaskSource>
</DynamicFulfillmentOrchestratorSettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>DynamicFulfillmentOrchestrator</members>
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

=== ARTICLE: meta_orchestrationplanctxmapping.htm ===
---
page_id: meta_orchestrationplanctxmapping.htm
title: OrchestrationPlanCtxMapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_orchestrationplanctxmapping.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrchestrationPlanCtxMapping

Represents the context mapping that Dynamic
			Revenue Orchestrator (DRO) uses to generate and orchestrate a plan for an object, such
			as a non-sales transaction for billing or another generic business process.
	

		

## Parent Type

 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
			field.

		

## File Suffix and Directory Location

			
			

OrchestrationPlanCtxMapping components have the suffix
					.orchestrationPlanCtxMapping and are stored in the
					orchestrationPlanCtxMappings folder.

		

		

## Version

			
			

OrchestrationPlanCtxMapping components are available in API version 67.0 and
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

						

					

				
| Field Name | Description |
| --- | --- |
| context​Definition | **Field Type** string **Description** Required. [ContextDefinition](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_contextdefinition.htm) that the orchestration use case is based on. |
| contextItem​Node | **Field Type** string **Description** Name of the item-level node in the context definition. The item node represents the line items or child records of the root node, such as the items in an order. |
| contextMapping | **Field Type** string **Description** Required. Name of the context mapping that maps the source object fields to the nodes in the context definition. |
| context​RootNode | **Field Type** string **Description** Required. Name of the root node in the context definition. The root node represents the parent record that the orchestration plan is generated for, such as an order. |
| label | **Field Type** string **Description** Required. UI label for the orchestration plan context mapping. |
| objectName | **Field Type** string **Description** Required. API name of the object that the orchestration plan is generated for. The combination of objectName and orchestrationType must be unique. |
| orchestration​Type | **Field Type** PlanUsageType (enumeration of type string) **Description** Required. Type of orchestration plan that this context mapping applies to. Valid values are: `Billing` `Fulfillment` `Generic` `IntegrationOrchestrator` `InsuranceRuleAction` `OrderFulfillment` `StageManagement` |

		

		

## Declarative Metadata Sample Definition

			
			

This sample shows the definition of an OrchestrationPlanCtxMapping component for a
				fulfillment plan that orchestrates an order.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<OrchestrationPlanCtxMapping xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Order Fulfillment Context Mapping</label>
    <orchestrationType>Fulfillment</orchestrationType>
    <contextDefinition>SalesTransactionContext__stdctx</contextDefinition>
    <objectName>Order</objectName>
    <contextMapping>OrderEntitiesMapping</contextMapping>
    <contextRootNode>SalesTransaction</contextRootNode>
    <contextItemNode>SalesTransactionItem</contextItemNode>
</OrchestrationPlanCtxMapping>
```

			

This sample `package.xml` references the previous
				definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>OrchestrationPlanCtxMapping</name>
    </types>
    <version>68.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based.htm).

=== ARTICLE: sforce_api_objects_assetfulfillmentdecomp.htm ===
---
page_id: sforce_api_objects_assetfulfillmentdecomp.htm
title: AssetFulfillmentDecomp
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetfulfillmentdecomp.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetFulfillmentDecomp

Represents the relationship between an ordered asset and its
         corresponding fulfillment asset. This object is available in API version 62.0 and
      later.

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
- 

                  

               

            
| Field | Details |
| --- | --- |
| FulfillmentSourceAssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The identifier of the relationship between an asset and a fulfillment asset. This field is a polymorphic relationship field. **Relationship Name** FulfillmentSourceAsset **Refers To** Asset, FulfillmentAsset |
| FulfillmentTargetAssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The identifier of the target asset that's being fulfilled. This field is a relationship field. **Relationship Name** FulfillmentTargetAsset **Refers To** FulfillmentAsset |
| IsUsedForFulfmtAssetActivation | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if internal jobs are allowed to activate the related fulfillment asset. The default value is true. This field is available in API version 6.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the asset that's being fulfilled. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the request record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RelationshipType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of relationship between an asset and a fulfillment asset. Valid values are: `SourceBundleRoot` `SourceLineItem` |
| SegmentIdentifier | **Type** string **Properties** Create, Group, Nillable, Sort, **Description** The ID of the ramp segment associated with the asset state period. This field is available in API version 63.0 and later in orgs that have Revenue Management when the Ramp Deals setting is enabled. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The status of the fulfillment asset. Valid values are: `Active` `Inactive` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[AssetFulfillmentDecompHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object starting API version
                  65.0.

            
            
            
               

**[AssetFulfillmentDecompShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentasset.htm ===
---
page_id: sforce_api_objects_fulfillmentasset.htm
title: FulfillmentAsset
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentasset.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentAsset

Represents an instance of a technical product used to provide a
         customer asset. This object is available in API version 61.0 and later.

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The identifier of the account. This field is a relationship field. **Relationship Name** Account **Relationship Type** Lookup **Refers To** Account |
| IsTimeAware | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if the fulfillment asset's configuration data is tracked in a time-aware or time-agnostic manner. Available in API version 67.0 and later. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **For internal use only.** |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **For internal use only.** |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment asset. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** For internal use only. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The identifier of the corresponding product. This field is a relationship field. **Relationship Name** Product **Relationship Type** Lookup **Refers To** Product2 |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** For internal use only. |
| ScopeIdentifierText | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort **Description** The scope in which this fulfillment asset record is created. This field is available in API version 65.0 and later. |
| StateEndTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the end time of the current fulfillment asset state period. Available in API version 67.0 and later. |
| StateStartTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the start time of the current fulfillment asset state period. Available in API version 67.0 and later. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The status of the fulfillment asset. Valid values are: `Active` `InActive` |
| UnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The unit of measure for the asset quantity such as, unit, gallon, ton, or case. This field is available in API version 63.0 and later. This field is a relationship field. **Relationship Name** UnitOfMeasure **Refers To** UnitOfMeasure |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[FulfillmentAssetHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object starting API version
                  65.0.

            
            
            
               

**[FulfillmentAssetShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentassetattribute.htm ===
---
page_id: sforce_api_objects_fulfillmentassetattribute.htm
title: FulfillmentAssetAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentassetattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentAssetAttribute

Represents an attribute of a fulfillment asset. This object is
      available in API version 61.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `update()`, `upsert()`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The attribute definition in the catalog. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The name of the attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** AttributePicklistValue **Relationship Type** Lookup **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the attribute. |
| ExternalId | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. |
| FulfillmentAssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The identifier of the fulfillment asset. This field is a relationship field. **Relationship Name** FulfillmentAsset **Relationship Type** Master-detail **Refers To** FulfillmentAsset (the master object) |

=== ARTICLE: sforce_api_objects_fulfillmentassetrelationship.htm ===
---
page_id: sforce_api_objects_fulfillmentassetrelationship.htm
title: FulfillmentAssetRelationship
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentassetrelationship.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentAssetRelationship

Represents a relationship between two fulfillment assets. This
      object is available in API version 61.0 and later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

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

: 

                  

                  
                     

                     

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
| AssociatedFulfillAssetRole | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The role of the associated fulfillment asset. Valid values are: `BundleComponent` `ClassificationComponent`—Product Classification Component |
| AssociatedFulfillmentAssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The name of the associated fulfillment asset. This field is a relationship field. **Relationship Name** AssociatedFulfillmentAsset **Refers To** FulfillmentAsset |
| EndTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The time until when this asset relationship is valid. |
| MainFulfillmentAssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The name of the primary fulfillment asset. This field is a relationship field. **Relationship Name** MainFulfillmentAsset **Relationship Type** Master-detail **Refers To** FulfillmentAsset (the master object) |
| MainFulfillmentAssetRole | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The role of the primary fulfillment asset. Valid value is `Bundle Parent`. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment asset relationship. |
| ProductRelationshipTypeId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The type of relationship between two assets. This field is a relationship field. **Relationship Name** ProductRelationshipType **Refers To** ProductRelationshipType |
| StartTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The time from when this asset relationship is valid. |

=== ARTICLE: sforce_api_objects_fulfillmentassetstateperiod.htm ===
---
page_id: sforce_api_objects_fulfillmentassetstateperiod.htm
title: FulfillmentAssetStatePeriod
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentassetstateperiod.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentAssetStatePeriod

      Represents the period during which the fulfillment asset configuration is
         applicable. This object is available in API version 67.0 and later. 

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         
      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Possible values are: `EUR`—Euro `INR`—Indian Rupee `USD`—U.S. Dollar The default value is `USD`. |
| EndTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the end time of the state period. If null, the configuration is effective from Start Time. If Start Time is also null, the configuration is effective at all times. |
| FulfillmentAssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Represents the fulfillment asset to which this fulfillment asset state period applies. This field is a relationship field. **Relationship Name** FulfillmentAsset **Relationship Type** Master-detail **Refers To** FulfillmentAsset (the master object) |
| IsSuperseded | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if the state period is superseded and the record is replaced by a newer version due to updates by the fulfillment process. The default value is `false`. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the fulfillment asset state period. |
| Quantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** Represents the fulfillment product quantity applicable for the state period. |
| StartTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the start time of the state period. If null, the configuration is effective until End Time. If End Time is also null, the configuration is effective at all times. |

=== ARTICLE: sforce_api_objects_fulfillmentassetstateperiodattribute.htm ===
---
page_id: sforce_api_objects_fulfillmentassetstateperiodattribute.htm
title: FulfmtAssetStatePeriodAttr
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentassetstateperiodattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfmtAssetStatePeriodAttr

      Represents the key-value pair of a fulfillment asset attribute applicable
         during a specific asset state period. This object is available in API version 67.0 and
      later. 

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

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

                  

                  
                     

                     

: 

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
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Represents the definition of the fulfillment asset state period attribute. This field is a relationship field. **Relationship Name** AttributeDefinition **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** Represents the name of the fulfillment asset state period attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents the reference identifier of the selected picklist value. This field is a relationship field. **Relationship Name** AttributePicklistValue **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents the value of the fulfillment asset state period attribute. |
| ExternalId | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents the external ID of the fulfillment asset state period attribute. |
| FulfillmentAssetStatePeriodId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Represents the fulfillment asset period applicable to the object. This field is a relationship field. **Relationship Name** FulfillmentAssetStatePeriod **Relationship Type** Master-detail **Refers To** FulfillmentAssetStatePeriod (the master object) |

=== ARTICLE: sforce_api_objects_fulfillmentfalloutrule.htm ===
---
page_id: sforce_api_objects_fulfillmentfalloutrule.htm
title: FulfillmentFalloutRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentfalloutrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentFalloutRule

Represents the fulfillment fallout handling rule. This object is
      available in API version 61.0 and later.

      

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

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                  
                     

                     
                     

: 

: 

: 

                     
                  

                  
                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

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
- 
- 
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| ErrorCode | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The failure error code of the fulfillment step that's associated with the rule. |
| FalloutQueueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fallout queue that's associated with the fallout task. This field is available in API version 62.0 and later. This field is a relationship field. **Relationship Name** FalloutQueue **Refers To** Group |
| FlowDefinitionName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the flow definition that's associated with the `AutoTask` type of fulfillment step. |
| IntegrationDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The integration definition that's associated with the `Callout` type of fulfillment step. This field is a relationship field. **Relationship Name** IntegrationDefinition **Relationship Type** Lookup **Refers To** IntegrationProviderDef |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the flow definition that's associated with the `AutoTask` type of fulfillment step. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the fulfillment record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| RetriesAllowed | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of times a retry policy is run before the fulfillment step is considered failed. |
| RetryIntervals | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The interval after which the selected retry policy is run when the fulfillment step fails. This field is available in API version 62.0 and later. |
| RetryPolicy | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the retry policy used when the fulfillment step fails. Valid value is: `Immediate` `Monotonous` `Staggered` |
| StepType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of fulfillment step associated with the fallout rule. Valid values are: `AutoTask` `Callout` `ManualTask` `Milestone` `Pause` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[FulfillmentFalloutRuleHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[FulfillmentFalloutRuleShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentlineattribute.htm ===
---
page_id: sforce_api_objects_fulfillmentlineattribute.htm
title: FulfillmentLineAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentlineattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentLineAttribute

Represents an attribute of a fulfillment order line. This object
      is available in API version 61.0 and later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `update()`, `upsert()`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** A unique identifier for the attribute definition in the catalog. This field is a relationship field. **Relationship Name** AttributeDefinition **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The name of the attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** AttributePicklistValue **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the attribute. |
| ExternalId | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID that uniquely identifies the relationship in an external data source. |
| FulfillmentOrderLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** A unique identifier for the fulfillment order line item. This field is a relationship field. **Relationship Name** FulfillmentOrderLineItem **Relationship Type** Master-detail **Refers To** FulfillmentOrderLineItem (the master object) |

=== ARTICLE: sforce_api_objects_fulfillmentlinerel.htm ===
---
page_id: sforce_api_objects_fulfillmentlinerel.htm
title: FulfillmentLineRel
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentlinerel.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentLineRel

Represents a relationship between two fulfillment order lines.
      This object is available in API version 61.0 and later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

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
| AssociatedFoItemInventory | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Inventory level for the associated fulfillment order item. Valid values are: `Included in Main Inventory` `Not Included in Main Inventory` This field is available in API version 63.0 and later. |
| AssociatedFulfillOrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The identifier of the associated fulfillment order line item. This field is a relationship field. **Relationship Name** AssociatedFulfillOrderItem **Refers To** FulfillmentOrderLineItem |
| AssociatedLineRole | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The role of the associated fulfillment order line item. Valid values are: `BundleComponent` `ClassificationComponent`—Product Classification Component |
| AssociatedQuanScaleMethod | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Method used to scale the quantity of the associated order item summary relative to the main fulfillment order item. Valid values are: `Constant` `Proportional` The default value is `Proportional`. This field is available in API version 63.0 and later. |
| FulfillmentOrderId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the parent fulfillment order. This field is a relationship field. **Relationship Name** FulfillmentOrder **Refers To** FulfillmentOrder |
| MainFulfillOrderItemRole | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The role of the primary fulfillment order line item. Valid value is `Bundle`. |
| MainFulfillmentOrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the associated fulfillment order line item. This field is a relationship field. **Relationship Name** MainFulfillmentOrderItem **Relationship Type** Master-detail **Refers To** FulfillmentOrderLineItem (the master object) |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the fulfillment order line relationship. |
| ProductRelationshipTypeId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The type of relationship between two assets. This field is a relationship field. **Relationship Name** ProductRelationshipType **Refers To** ProductRelationshipType |

=== ARTICLE: sforce_api_objects_fulfillmentlinesourcerel.htm ===
---
page_id: sforce_api_objects_fulfillmentlinesourcerel.htm
title: FulfillmentLineSourceRel
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentlinesourcerel.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentLineSourceRel

Represents the relationship between a fulfillment order line and its
         decomposition source. This object is available in API version 61.0 and
      later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| Action | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the action to be performed on the asset fulfillment decomposition record. This field is available in API version 66.0 and later. Possible values are: `Add` `Cancel` `NoChange`—No Change |
| FulfilmentOrderLineId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the fulfillment order line. This field is a relationship field. **Relationship Name** FulfilmentOrderLine **Refers To** FulfillmentOrderLineItem |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The relation between the two order line sources. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| SourceItemIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The ID of the decomposition source that's related to the fulfilment order line. This field is available in API version 64.0 and later. |
| SourceLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the source line item. This field is a polymorphic relationship field. **Relationship Name** SourceLineItem **Refers To** FulfillmentOrderLineItem, OrderItem |
| SourceType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of source for the line item. Valid values are: `SourceBundleRoot` `SourceLineItem` |
| SupplementalAction | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The supplemental action that's applied to the line item based on the run-time changes made to the original fulfillment request. This field is available in API version 62.0 and later. Valid values are: `Add` `Amend` `Cancel` `NoChange` |
| UniqueIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort **Description** For internal use only. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
            
            
               

**[FulfillmentLineSourceRelShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentplan.htm ===
---
page_id: sforce_api_objects_fulfillmentplan.htm
title: FulfillmentPlan
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentplan.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentPlan

Represents a set of steps to be created to fulfill the order.
      This object is available in API version 61.0 and later.

      

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

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| ExecutionUserId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. **Relationship Name** ExecutionUser **Refers To** User |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the fulfillment plan. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Priority | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The priority of the fulfillment plan execution. This field is available in API version 63.0 and later. Valid values are: `Default` `High` `Bulk` |
| SourceIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update, idLookup (Available in API version 64.0 and later) **Description** For internal use only. |
| SourceType | **Type** string **Properties** Create, Filter, Group, Nillable, Sort **Description** The type of source for the fulfillment plan. This field is available in API version 62.0 and later. |
| State | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the fulfillment plan. Valid values are: `Completed` `InProgress` `NotStarted` |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The business that uses Fulfillment Orchestration. Valid values are: `IntegrationOrchestrator` `Generic` `StageManagement` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[FulfillmentPlanChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
            
               

**[FulfillmentPlanHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object starting API version
                  65.0.

            
            
            
               

**[FulfillmentPlanShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentsourcechangeevent.htm ===
---
page_id: sforce_api_objects_fulfillmentsourcechangeevent.htm
title: FulfillmentSourceChangeEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentsourcechangeevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_events_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentSourceChangeEvent

      Notifies updates to the sources orchestrated by Dynamic Revenue Orchestrator
         like order product or fulfillment order product. This object is available in API
      version 66.0 and later. 

      
         

         
         

      

      

## Supported Calls

         
         

            `describeSObjects()`
         

      

      

## Supported Subscribers

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

               

            
| Subscriber | Supported? |
| --- | --- |
| Apex Triggers |  |
| Flows |  |
| Processes |  |
| Pub/Sub API |  |
| Streaming API (CometD) |  |

      

      

## Streaming API Subscription Channel

         
         

`/event/SalesTrxnDecompositionEvent`

      

      

## Special Access Rules

         
         

This object is available in orgs with Revenue Management.

      

      

## Event Delivery Allocation Enforced

         
         

Yes

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| RecordIdentifier | **Type** string **Properties** Create, Nillable **Description** The identifier of the source record that has been updated. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |

=== ARTICLE: sforce_api_objects_fulfillmentstep.htm ===
---
page_id: sforce_api_objects_fulfillmentstep.htm
title: FulfillmentStep
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstep.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStep

Represents a task that's required to perform a certain action as part
         of order fulfillment. This task can be manual or automated. This object is available
      in API version 61.0 and later.

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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
- 
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| ActualCompletionDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the fulfillment step state changed to `Completed` or `Skipped`. |
| ActualStartDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the fulfillment step state changed to `Ready`. |
| AssignedToId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The user or queue associated with the fulfillment step. This field is a polymorphic relationship field. **Relationship Name** AssignedTo **Relationship Type** Lookup **Refers To** Queue, User |
| CustomConfigParameter | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents the custom configuration context set by the designer in the Fulfillment Step Definition record. This context is passed to fulfillment steps during execution to enable flow reusability. |
| CompensatedStepId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The alternative step that's executed when a particular step in the fulfillment plan is amended or canceled. This field is a relationship field. This field is available in API version 62.0 and later. **Relationship Name** CompensatedStep **Refers To** FulfillmentStep |
| DelayOf | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the delay. This field is available in API version 63.0 and later. |
| DelayUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit for the delay of the fulfillment step. This field is available in API version 63.0 and later. Valid values are: `Days` `Hours` `Minutes` |
| ExecuteOn | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies when to execute the fulfillment step. This field is available in API version 63.0 and later. Valid values are: `PreviousStepExecutionDate` `SourceLineStartDate` |
| ExecuteOnRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the expression set. The fulfillment step is executed only when its corresponding expression set returns the value `true`. This field is a polymorphic relationship field. **Relationship Name** ExecuteOnRule **Relationship Type** Lookup **Refers To** ExpressionSet |
| ExecutionMessage | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. |
| FalloutQueueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fallout queue that's associated with the fallout task. This field is available in API version 62.0 and later. This field is a relationship field. **Relationship Name** FalloutQueue **Refers To** Group |
| FlowDefinitionName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the flow definition that's associated with the `AutoTask` type of fulfillment step. This field is available in API version 62.0 and later. |
| FlowInterviewId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The flow interview associated with the fulfillment step. This field is a relationship field. **Relationship Name** FlowInterview **Relationship Type** Lookup **Refers To** FlowInterview |
| ForcePlanFreezeDuringExecution | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to freeze the plan while the step is in progress. If enabled, specifies how to complete the step before resuming the plan. This field is available in API version 63.0 and later. Valid values are: `Never` `YesButWaitForStepCompletion` The default value is `Never`. |
| FulfillmentPlanId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The fulfillment plan associated with the fulfillment step. This field is a relationship field. **Relationship Name** FulfillmentPlan **Relationship Type** Lookup **Refers To** FulfillmentPlan |
| FulfillmentStepDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fulfillment step definition associated with the fulfillment step. This field is a relationship field. **Relationship Name** FulfillmentStepDefinition **Relationship Type** Lookup **Refers To** FulfillmentStepDefinition |
| IntegrationDefinitionNameId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** IntegrationDefinitionName **Relationship Type** Lookup **Refers To** IntegrationProviderDef |
| IsSkipBranch | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the remaining steps in the fulfillment step group are skipped from execution when the Execute On Rule condition is set (`true`) or not (`false`). This field is available in API version 62.0 and later. The default value is `false`. |
| JeopardyStatus | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The jeopardy status of the fulfillment step. This field is a calculated field. |
| JeopardyThreshold | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of days, hours, minutes, or seconds, counting back from the expected duration, before a fulfillment step is in jeopardy. |
| JeopardyThresholdUnit | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The time unit of the jeopardy threshold. Valid values are: `Days` `Hours` `Minutes` `Seconds` The default value is `Minutes`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment step. |
| NextEarliestRunTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The next available time for the process execution. This field is available in API version 62.0 and later. |
| OmniscriptName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For inyternal use only. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| PlannedCompletionDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time Dynamic Revenue Orchestrator estimates that the fulfillment step will complete. |
| PlannedStartDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the Dynamic Revenue Orchestrator calculates the fulfillment step state change to `Ready`. |
| PointOfNoReturn | **Type** multipicklist **Properties** Create, Filter, Nillable **Description** The type of source change applied to the line item. This field is available in API version 62.0 and later. Valid value is: `Changes Denied` |
| RequestedCompletionDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The planned completion date and time of the fulfillment step. |
| RequestedStartDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The planned start date and time of the fulfillment step. |
| ResumeOnRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rule set or expression set for the fulfillment step. The step is completed only when the corresponding expression set returns the `isExecuteStep` output as `true`. This field is a polymorphic relationship field. **Relationship Name** ResumeOnRule **Relationship Type** Lookup **Refers To** ExpressionSet |
| RetryAttempts | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of attempts allowed for retry as set up in the Fallout Qualification Rule table. |
| RunAsUserId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Overrides user context for an automated step. The default user context is AutomatedProc user. This field is a relationship field. **Relationship Name** RunAsUser **Relationship Type** Lookup **Refers To** User |
| ScopeIdentifierText | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The scope under which the Fulfillment Step was created.This field is available in API version 68.0 and later. |
| State | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The state of the fulfillment step. For example, `In Progress` or `Completed`. Valid values are: `Completed` `Failed` `FatallyFailed` `InProgress` `Pending` `Ready` `Scheduled` `Skipped` |
| StepType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The fulfillment step type associated with the fulfillment step. Valid values are: `AutoTask` `Callout` `ManualTask` `Milestone` `Pause` `StagedAssetize`—Available in API version 63.0 and later. |
| TaskAllocationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The method of assigning the manual step. This field is available in API version 63.0 and later. Valid values are: `ContextBased` `LeastLoaded` `RoundRobin` |
| TaskId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the task assigned to a user or queue. This field is available in API version 63.0 and later. This field is a relationship field. **Relationship Name** Task **Refers To** Task |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The details about the business that uses Fulfillment Orchestration. Some examples of UsageBy include Financial Services Cloud and CPQ. Valid values are: `Fulfillment` `InsuranceRuleAction` `IntegrationOrchestrator` `OrderFulfillment` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[FulfillmentStepChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
            
               

**[FulfillmentStepHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[FulfillmentStepShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentstepdefinition.htm ===
---
page_id: sforce_api_objects_fulfillmentstepdefinition.htm
title: FulfillmentStepDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepdefinition.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepDefinition

Represents a definition of a step that must be executed during
         fulfillment orchestration. This object is available in API version 61.0 and
      later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

                  
                     

                     

: 

: 

: 
: 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AmendGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fulfillment step group that's added to the fulfillment plan when the step is amended. This field is available in API version 62.0 and later. This field is a relationship field. **Relationship Name** AmendGroup **Refers To** FulfillmentStepDefinitionGroup |
| AssignedToId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The user or queue associated with the fulfillment step definition. This field is a polymorphic relationship field. **Relationship Name** AssignedTo **Relationship Type** Lookup **Refers To** Queue, User |
| CancelledGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fulfillment step group that's added to the fulfillment plan when the step is canceled. This field is available in API version 62.0 and later. This field is a relationship field. **Relationship Name** CancelledGroup **Refers To** FulfillmentStepDefinitionGroup |
| CustomBaseExecutionDate | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context tag containing a custom date that's used to calculate the execution time for a future-dated step. This field is available in API version 65.0 and later. |
| CustomConfigParameter | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents the custom configuration context given by the designer. This context is passed to fulfillment steps during execution to support flow reusability. |
| CustomFulfillmentScope | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The custom scope to use during order fulfillment. This field is available in API version 65.0 and later. |
| DelayOf | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the delay. This field is available in API version 63.0 and later. |
| DelayUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit for the delay of the fulfillment step. This field is available in API version 63.0 and later. Valid values are: `Days` `Hours` `Minutes` |
| Description | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Description of the fulfillment step definition, shown to admins in the orchestration plan. This field is available in API version 68.0 and later. |
| ExecuteOn | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies when to execute the fulfillment step. This field is available in API version 63.0 and later. Valid values are: `PreviousStepsStartDate` `SourceLineStartDate` |
| ExecuteOnConditionData | **Type** textarea **Properties** Create, Nillable, Update **Description** The condition for executing the fulfillment step. The condition is defined as a rule or a set of rules in JSON format. This field is available in API version 66.0 and later. |
| ExecuteOnRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The expression set for the fulfillment step. The step is executed only when the corresponding expression set is `true`. This field is a polymorphic relationship field. **Relationship Name** ExecuteOnRule **Relationship Type** Lookup **Refers To** ExpressionSet |
| FlowDefinitionName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the associated flow. |
| ForcePlanFreezeDuringExecution | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to freeze the plan while the step is in progress. If enabled, specifies how to complete the step before resuming the plan. This field is available in API version 63.0 and later. Valid values are: `Never` `YesButForcefullyCompleteStep` The default value is `Never`. |
| IntegrationDefinitionNameId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the integration definition that’s used to set up communication with an external endpoint. This field is a relationship field. **Relationship Name** IntegrationDefinitionName **Relationship Type** Lookup **Refers To** IntegrationProviderDef |
| IsSkipBranch | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the remaining steps in the fulfillment step group are skipped from execution when the Execute On Rule condition is set. This field is available in API version 62.0 and later. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment step definition. |
| OmniscriptName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. |
| PointOfNoReturn | **Type** multipicklist **Properties** Create, Filter, Nillable, Update **Description** The type of source change applied to the line item. This field is available in API version 62.0 and later. Valid value is: `Changes Denied` |
| ResumeOnConditionData | **Type** textarea **Properties** Create, Nillable, Update **Description** The condition for resuming the paused fulfillment step. The condition is defined as a rule or a set of rules in JSON format. This field is available in API version 66.0 and later. |
| ResumeOnRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The expression set for the fulfillment step definition. The step is completed when the expression set is `true`. This field is a polymorphic relationship field. **Relationship Name** ResumeOnRule **Relationship Type** Lookup **Refers To** ExpressionSet |
| RunAsUserId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The user context to run a fulfillment step when the fulfillment operator wants to override the default autoproc user. This field is a relationship field. **Relationship Name** RunAsUser **Relationship Type** Lookup **Refers To** User |
| Scope | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The scope of the fulfillment step definition. For example, `Bundle` or `Order`. Valid values are: `Bundle` `CrossPlan` `LineItem` `Plan` The default value is `Plan`. |
| StepDefinitionGroupId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** StepDefinitionGroup **Relationship Type** Master-detail **Refers To** FulfillmentStepDefinitionGroup (the master object) |
| StepType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** For internal use only. Valid values are: `AutoTask` `Callout` `ManualTask` `Milestone` `Pause` `StagedAssetize` |
| TaskAllocationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The method of assigning the manual step. This field is available in API version 62.0 and later. Valid value is: `RoundRobin` `LeastLoaded` `ContextBased` |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The business vertical that uses fulfillment orchestration. For example, Financial Services Cloud. Valid values are: `IntegrationOrchestrator` `OrderFulfillment` |

=== ARTICLE: sforce_api_objects_fulfillmentstepdefinitiongroup.htm ===
---
page_id: sforce_api_objects_fulfillmentstepdefinitiongroup.htm
title: FulfillmentStepDefinitionGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepdefinitiongroup.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepDefinitionGroup

Represents a set of fulfillment step definitions. This object is
      available in API version 61.0 and later.

      

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
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment step definition group. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The business that uses Fulfillment Orchestration. Possible values are: `IntegrationOrchestrator` `Generic` `InsuranceRuleAction` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[FulfillmentStepDefinitionGroupHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[FulfillmentStepDefinitionGroupShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentstepdependency.htm ===
---
page_id: sforce_api_objects_fulfillmentstepdependency.htm
title: FulfillmentStepDependency
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepdependency.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepDependency

Represents a dependency between tasks by defining the order between a
         task and one that depends on it. This object is available in API version 61.0 and
      later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| DependencyDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the fulfillment step dependency definition. This field is a relationship field. **Relationship Name** DependencyDefinition **Refers To** FulfillmentStepDependencyDef |
| DependentStepId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The name of a fulfillment step that depends on this step. This field is a relationship field. **Relationship Name** DependentStep **Relationship Type** Master-detail **Refers To** FulfillmentStep |
| DependsOnStepId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the fulfillment step that this step depends on. That is, the name of the step that must be executed before this one can run. This field is a relationship field. **Relationship Name** DependsOnStep **Refers To** FulfillmentStep |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** An automatically generated name for the fulfillment step dependency. |

=== ARTICLE: sforce_api_objects_fulfillmentstepdependencydef.htm ===
---
page_id: sforce_api_objects_fulfillmentstepdependencydef.htm
title: FulfillmentStepDependencyDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepdependencydef.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepDependencyDef

Represents a dependency that must be created between two fulfillment
         step records. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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
- 
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| CustomScope | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the custom scope when the dependency scope is set to custom. This field is available in API version 68.0 and later. |
| DependencyScope | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The scope of the fulfillment step dependency definition. For example, Order or Order Item. Valid values are: `Bundle` `LineItem` `Plan` `CrossPlan` `Custom` The default value is `Plan`. |
| DependsOnStepDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The fulfillment step definition that must be executed before this step. This field is a relationship field. **Relationship Name** DependsOnStepDefinition **Refers To** FulfillmentStepDefinition |
| FulfillmentStepDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The identifier of the fulfillment step definition. This field is a relationship field. **Relationship Name** FulfillmentStepDefinition **Relationship Type** Master-detail **Refers To** FulfillmentStepDefinition (the master object) |
| IsCompensateInReverse | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the order to insert the compensated group steps is reversed when a fulfillment step is canceled (`true`) or not (`false`). The default value is `false`. This field is available in API version 63.0 and later. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment step dependency definition. |
| PropagateStateToDependentStep | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The state that’s propagated to the dependent fulfillment step when the source fulfillment step is amended or canceled in the fulfillment plan. Valid values are: `Amended` `Both` `Canceled` `None` This field is available in API version 63.0 and later. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[FulfillmentStepDependencyDefChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
               

**[FulfillmentStepDependencyDefFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[FulfillmentStepDependencyDefHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[FulfillmentStepDependencyDefOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[FulfillmentStepDependencyDefShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentstepjeopardyrule.htm ===
---
page_id: sforce_api_objects_fulfillmentstepjeopardyrule.htm
title: FulfillmentStepJeopardyRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepjeopardyrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepJeopardyRule

Represents the duration and tolerance for the step in the fulfillment
         process to allow the overall tracking of rules and risks. This object is available in
      API version 61.0 and later.

      

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

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| EstimatedDuration | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The estimated time to complete the fulfillment step. |
| EstimatedDurationUnit | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The unit of measurement that applies to the estimated time to complete the fulfillment step. Valid values are: `Days` `Hours` `Minutes` `Seconds` The default value is `Minutes`. |
| FlowDefinition | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The flow definition that's associated with the `AutoTask` type of the fulfillment step. |
| IntegrationDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The integration definition that's associated with the `Callout` type of the fulfillment step. This field is a relationship field. **Relationship Name** IntegrationDefinition **Relationship Type** Lookup **Refers To** IntegrationProviderDef |
| JeopardyThreshold | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The value indicating the threshold after which the fulfillment step is in jeopardy. |
| JeopardyThresholdUnit | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The unit of measurement that applies to the jeopardy threshold value. Valid values are: `Days` `Hours` `Minutes` `Seconds` The default value is `Minutes`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** For internal use only. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** For internal use only. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** For internal use only. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** For internal use only. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| StepType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of fulfillment step that's affected by the jeopardy rule. Valid values are: `AutoTask` `Callout` `ManualTask` `Milestone` `Pause` |

=== ARTICLE: sforce_api_objects_fulfillmentstepsource.htm ===
---
page_id: sforce_api_objects_fulfillmentstepsource.htm
title: FulfillmentStepSource
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentstepsource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentStepSource

Represents a link between a fulfillment step and the corresponding
         order lines. This object is available in API version 61.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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

                     
                  

                  
               

            
| Field | Details |
| --- | --- |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An automatically generated name for the fulfillment step source. |
| SourceIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The identifier of the source order line item (order item or fulfillment order line). |
| SourceLineItemId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a polymorphic relationship field. **Relationship Name** SourceLineItem **Refers To** FulfillmentOrderLineItem, OrderItem |
| StepId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The identifier of the fulfillment step. This field is a relationship field. **Relationship Name** Step **Relationship Type** Master-detail **Refers To** FulfillmentStep (the master object) |
| VersionGroupIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the version group that's assigned to the fulfillment step source item. This field is available in API version 64.0 and later. |

      

      
      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[FulfillmentStepSourceChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

=== ARTICLE: sforce_api_objects_fulfillmenttaskassignmentrule.htm ===
---
page_id: sforce_api_objects_fulfillmenttaskassignmentrule.htm
title: FulfillmentTaskAssignmentRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmenttaskassignmentrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentTaskAssignmentRule

Represents a set of actions that assign a task to a user or
         queue. This object is available in API version 63.0 and later.

      

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
- 
- 
- 
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ConditionData | **Type** textarea **Properties** Create, Nillable, Update **Description** The condition for executing the fulfillment task assignment rule. The condition is defined as a rule or a set of rules in JSON format. This field is available in API version 66.0 and later. |
| ConditionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Condition ID that's used to determine the task assignment. This field is a polymorphic relationship field. **Relationship Name** Condition **Refers To** ExpressionSet |
| DestinationId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Destination ID of the task assignment such as, Queue or User. This field is a polymorphic relationship field. **Relationship Name** Destination **Refers To** Group, User |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the object that specifies the condition used to determine the task assignment. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the task assignment rule record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Priority | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The priority of the rule for execution. |
| SourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Source ID of the task assignment such as Queue. This field is a relationship field. **Relationship Name** Source **Refers To** Group |
| TaskAllocationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The method of assigning the manual step. Valid values are: `ContextBased` `LeastLoaded` `RoundRobin` |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Name of the usage type. Possible values are: `Fulfillment` `Generic` `InsuranceRuleAction`—Insurance Rule Action `IntegrationOrchestrator`—Integration Orchestrator The default value is `Fulfillment`. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[FulfillmentTaskAssignmentRuleFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[FulfillmentTaskAssignmentRuleHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[FulfillmentTaskAssignmentRuleShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentworkspace.htm ===
---
page_id: sforce_api_objects_fulfillmentworkspace.htm
title: FulfillmentWorkspace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentworkspace.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentWorkspace

Represents a visual designer for fulfillment plans that can have
         multiple step groups and their dependencies. This object is available in API version
      61.0 and later.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the fulfillment workspace. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the fulfillment workspace. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who owns this record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[FulfillmentWorkspaceHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object starting API version
                  65.0.

            
            
               

**[FulfillmentWorkspaceShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_fulfillmentworkspaceitem.htm ===
---
page_id: sforce_api_objects_fulfillmentworkspaceitem.htm
title: FulfillmentWorkspaceItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_fulfillmentworkspaceitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FulfillmentWorkspaceItem

Represents information about the attributes that are used in the
         definition for a fulfillment step group. This object is available in API version 61.0
      and later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| FulfillmentStepDefinitionGroupId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** For internal use only. This field is a relationship field. **Relationship Name** FulfillmentStepDefinitionGroup **Relationship Type** Master-detail **Refers To** FulfillmentStepDefinitionGroup (the detail object) |
| FulfillmentWorkspaceId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the parent fulfillment workspace that's related to this record. This field is a relationship field. **Relationship Name** FulfillmentWorkspace **Relationship Type** Master-detail **Refers To** FulfillmentWorkspace (the master object) |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the fulfillment workspace item. |
| ShowOrder | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The display sequence value of the fulfillment workspace item. |

=== ARTICLE: sforce_api_objects_prodtdecompenrchvarmap.htm ===
---
page_id: sforce_api_objects_prodtdecompenrchvarmap.htm
title: ProdtDecompEnrchVarMap
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_prodtdecompenrchvarmap.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProdtDecompEnrchVarMap

      Represents the mapping of a field context tag or an attribute to a variable
         within an expression set. This object is available in API version 64.0 and later. 

      

## Supported Calls

      
      

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, 

      

      

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
- 
- 

: 

                  

            

            
| Field | Details |
| --- | --- |
| AttributeDefinitionId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The attribute definition the expression set variable is mapped to when creating the enrichment rule. This field is a relationship field. **Relationship Name** AttributeDefinition **Refers To** AttributeDefinition |
| ExpressionSetVarName | **Type** string **Properties** Filter, Group, Sort **Description** The name of the variable that's mapped to the expression set defined in the enrichment rule. |
| FieldContextTagName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the field context tag to which the expression set variable is mapped when creating the enrichment rule. |
| ProductAttributeIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The product attribute from an internal or external catalog, used by DRO to copy data during the enrichment process. This field is available in API version 65.0 and later. |
| ProductDecompEnrichmentRuleId | **Type** reference **Properties** Filter, Group, Sort **Description** The rule that contains the mappings between the fields and attributes for the decomposing product. This field is a relationship field. **Relationship Name** ProductDecompEnrichmentRule **Relationship Type** Master-detail **Refers To** ProductDecompEnrichmentRule (the master object) |
| VariableType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Specifies whether the expression set variable is an input or output variable. Valid values are: `Input` `Output` The default value is `Input`. |

=== ARTICLE: sforce_api_objects_productdecompenrichmentrule.htm ===
---
page_id: sforce_api_objects_productdecompenrichmentrule.htm
title: ProductDecompEnrichmentRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productdecompenrichmentrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductDecompEnrichmentRule

      Represents mappings between fields and attributes. Enrichment rules are part
         of a decomposition rule, and are used to propagate data to fulfillment order lines.
      This object is available in API version 61.0 and later. 

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

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
| CalculationDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** An expression set or a decision matrix that calculates the destination value. This field is a polymorphic relationship field. **Relationship Name** CalculationDefinition **Refers To** DecisionMatrixDefinition, ExpressionSet |
| CalculationMethod | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of enrichment rule. Valid values are: `Ad-verbatim`—As Is `Static-Lookup`—List Lookup `Expression-Set`—Available in API version 64.0 and later |
| DecompositionRuleId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The identifier of the decomposition rule. This field is a relationship field. **Relationship Name** DecompositionRule **Relationship Type** Parent-child **Refers To** ProductFulfillmentDecompRule (the master object) |
| DestinationApiName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the destination field or attribute code of an attribute. |
| DestinationAttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** DestinationAttributeDefinition **Refers To** AttributeDefinition |
| DestinationAttributeIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The destination entity attribute that is mapped from the source entity attribute. This field can store a Salesforce AttributeDefinition ID or an external identifier. This field is available in API version 65.0 and later. |
| DestinationContextTag | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the destination context definition. |
| DestinationType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The destination type for mapping. Valid values are: `Attribute` `Field` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record |
| ListMappingGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** ListMappingGroup **Refers To** ValTfrmGrp |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the decomposition rule. |
| RuleEnforcement | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the rule applies to all fulfillment requests or only to specific ones. Valid values are: `AllFulfillmentRequests` `InitialFulfillmentRequest` This field is available in API version 63.0 and later. |
| SourceApiName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The API name of the source field or attribute code of an attribute. |
| SourceAttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** For internal use only. This field is a relationship field. **Relationship Name** SourceAttributeDefinition **Refers To** AttributeDefinition |
| SourceAttributeIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The source entity attribute that is mapped to the destination entity attribute. This field can store a Salesforce AttributeDefinition ID or an external identifier. This field is available in API version 65.0 and later. |
| SourceContextTag | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The source type for the context definition. |
| SourceType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The source type for mapping. Valid values are: `Attribute` `Field` |

=== ARTICLE: sforce_api_objects_productfulfillmentdecomprule.htm ===
---
page_id: sforce_api_objects_productfulfillmentdecomprule.htm
title: ProductFulfillmentDecompRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productfulfillmentdecomprule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductFulfillmentDecompRule

Represents a rule that determines how an order is broken into
         sub-orders with specific technical details that help in order fulfillment. It can be
         applied to a commercial or a technical product. This object is available in API
      version 61.0 and later.

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
| ConditionData | **Type** textarea **Properties** Create, Nillable, Update **Description** The condition for executing the product fulfillment decomposition. The condition is defined as a rule or a set of rules in JSON format. This field is available in API version 66.0 and later. |
| DestinationProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The destination product for the decomposition rule. This field is a relationship field. **Relationship Name** DestinationProduct **Relationship Type** Lookup **Refers To** Product2 |
| DestinationIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The destination entity in the product fulfillment decomposition rule. This field can store a Salesforce product ID or an external identifier. This field is available in API version 65.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the decomposition rule. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| Priority | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The priority of the decomposition rule. Decomposition rules are executed in order of priority. |
| SourceProductClassificationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The classification of the source product that's used for decomposition. This field is available in API version 62.0 and later. This field is a relationship field. **Relationship Name** SourceProductClassification **Refers To** ProductClassification |
| SourceClassIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The source classification entity in the product fulfillment decomposition rule. This field can store a Salesforce product ID or an external identifier. This field is available in API version 65.0 and later. |
| SourceIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The source entity in the product fulfillment decomposition rule. This field can store a Salesforce product ID or an external identifier. This field is available in API version 65.0 and later. |
| SourceProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Source product for the decomposition rule. This field is a relationship field. **Relationship Name** SourceProduct **Relationship Type** Lookup **Refers To** Product2 |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
            
            
               

**[ProductFulfillmentDecompRuleShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productfulfillmentscenario.htm ===
---
page_id: sforce_api_objects_productfulfillmentscenario.htm
title: ProductFulfillmentScenario
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productfulfillmentscenario.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductFulfillmentScenario

Represents a link between a product and the corresponding group of
         fulfillment steps that's necessary to fulfill that product. This object is available
      in API version 61.0 and later.

      

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
- 
- 
- 
- 
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| Action | **Type** multipicklist **Properties** Create, Filter, Nillable, Update **Description** For internal use only. Valid values are: `Add` `Amend` `Cancel` `NoChange` `Renew` |
| ConditionData | **Type** textarea **Properties** Create, Nillable, Update **Description** The condition for executing the product fulfillment scenario. The condition is defined as a rule or a set of rules in JSON format. This field is available in API version 66.0 and later. |
| FulfillmentStepDefnGroupId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The fulfillment step definition group associated with the product fulfillment scenario. This field is a relationship field. **Relationship Name** FulfillmentStepDefnGroup **Relationship Type** Lookup **Refers To** FulfillmentStepDefinitionGroup |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** For internal use only. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** For internal use only. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the product fulfillment scenario. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** For internal use only. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProductClassificationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product classification associated with the product fulfillment scenario. This field is a relationship field. **Relationship Name** ProductClassification **Relationship Type** Lookup **Refers To** ProductClassification |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update, Nillable (Available in API version 64.0 and later) **Description** The product associated with the product fulfillment scenario. This field is a relationship field. **Relationship Name** Product **Relationship Type** Lookup **Refers To** Product2 |
| SourceClassIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The source classification entity in the product fulfillment scenario. This field can store a Salesforce Product Class ID or an external identifier. This field is available in API version 65.0 and later. |
| SourceIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The source entity in the product fulfillment scenario. This field can store a Salesforce product ID or an external identifier. This field is available in API version 65.0 and later. |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Name of the usage type. This field is available in API version 66.0 and later. Possible values are: `Fulfillment` `Generic` `InsuranceRuleAction`—Insurance Rule Action `IntegrationOrchestrator`—Integration Orchestrator `StageManagement`—Stage Management The default value is `Fulfillment`. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
            
            
               

**[ProductFulfillmentScenarioShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_salestransactionfulfillreq.htm ===
---
page_id: sforce_api_objects_salestransactionfulfillreq.htm
title: SalesTransactionFulfillReq
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_salestransactionfulfillreq.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SalesTransactionFulfillReq

      Represents the statuses of all the sub-orders that belong to the selected
         commercial or technical product. This object is available in API version 62.0 and
      later. 

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`
      

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

            

            
| Field | Details |
| --- | --- |
| AssetizationStatus | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Specifies the status of the assetization. Valid values are: `Completed` `Failed` `InProgress` `NotStarted` `Rejected` `NotApplicable`- Available in API version 64.0 and later. |
| DecompositionStatus | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Specifies the status of the decomposition. Valid values are: `Completed` `Failed` `InProgress` `NotStarted` `Rejected` `NotApplicable`- Available in API version 64.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the sales transaction fulfillment request. |
| OrchestrationGroupKey | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The identifier of the group of sales transactions that require synchronization before processing. This field is available in API version 63.0 and later. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the user who created the request record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PlanCompositionStatus | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** For internal use only. Valid values are: `Completed` `Failed` `InProgress` `NotStarted` `Rejected` `NotApplicable` - Available in API version 64.0 and later. |
| PlanExecutionStatus | **Type** picklist **Properties** Filter, Group, Nillable, Sort **Description** Specifies the status of the plan execution. Valid values are: `InProgress` `Frozen` `Freezing` |
| PlanId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The identifier of the plan. This field is a relationship field. **Relationship Name** Plan **Refers To** FulfillmentPlan |
| PreviousRequestId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The identifier of the previous fulfillment request. This field is a relationship field. **Relationship Name** PreviousRequest **Refers To** SalesTransactionFulfillReq |
| ReferenceObjectIdentifier | **Type** reference **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The ID of the sales transaction record. This field is available in API version 64.0 and later. |
| SalesTransactionType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Specifies the type of sales transaction that's processed by the fulfillment request. Valid values are: `StandardOrder` `GenericAdapter`—Available in API version 64.0 and later. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Specifies the overall status of the fulfillment. Valid values are: `Created` `Freezing` `Frozen` `Fulfilled` `Fulfilling` `Rejected` `Superseded` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
            
            
               

**[SalesTransactionFulfillReqShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_salestrxndecompositionevent.htm ===
---
page_id: sforce_api_objects_salestrxndecompositionevent.htm
title: SalesTrxnDecompositionEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_salestrxndecompositionevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_events_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SalesTrxnDecompositionEvent

      Notifies when the decomposition process status changes. This object is
      available in API version 66.0 and later. 

      
         

         
         

      

      

## Supported Calls

      
      

            `describeSObjects()`
         

      

      

## Supported Subscribers

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

                  
                     

                     

                  

               

            
| Subscriber | Supported? |
| --- | --- |
| Apex Triggers |  |
| Flows |  |
| Processes |  |
| Pub/Sub API |  |
| Streaming API (CometD) |  |

      

      

## Streaming API Subscription Channel

         
         

`/event/SalesTrxnDecompositionEvent`

      

      

## Special Access Rules

         
         

This object is available in orgs with Revenue Management.

      

      

## Event Delivery Allocation Enforced

         
         

Yes

      

      

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
| ErrorCode | **Type** string **Properties** Create, Nillable **Description** The error code returned for a decomposition process failure. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| SalesTransactionIdentifier | **Type** string **Properties** Create, Nillable **Description** The sales transaction being decomposed. |
| Status | **Type** string **Properties** Create, Nillable **Description** The status of the decomposition process. |

=== ARTICLE: sforce_api_objects_salestrxndeleteevent.htm ===
---
page_id: sforce_api_objects_salestrxndeleteevent.htm
title: SalesTrxnDeleteEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_salestrxndeleteevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SalesTrxnDeleteEvent

      Represents the platform event that triggers the deletion of sales transaction
         fulfillment request records when the corresponding reference records are deleted. This
      object is available in API version 64.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `describeSObjects()`
      

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| ReferenceObjectIdentifier | **Type** string **Properties** Create, Nillable **Description** Object identifier for the sales transaction fulfillment request to be deleted. |

=== ARTICLE: sforce_api_objects_valtfrm.htm ===
---
page_id: sforce_api_objects_valtfrm.htm
title: ValTfrm
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_valtfrm.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ValTfrm

Represents mappings between fields and attributes. Enrichment rules
         are part of a decomposition rule, and are used to propagate data to fulfillment order
         lines. This object is available in API version 61.0 and later.

      
         

#### Important

Where
            possible, we changed noninclusive terms to align with our company value of Equality. We
            maintained certain terms to avoid any effect on customer implementations.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| InputDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date of value entry. |
| InputDatetime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The time of value entry. |
| InputNumber | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The value of input number. |
| InputPicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The identifier of the input list of values. This field is a relationship field. **Relationship Name** InputPicklistValue **Refers To** AttributePicklistValue |
| InputString | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of input text. |
| IsInputBoolean | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if a value was entered (`true`) or not (`false`). The default value is `false`. |
| IsOutputBoolean | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if there was an output value (`true`) or not (`false`). The default value is `false`. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the related transformation group. |
| OutputDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date of matched output. |
| OutputDatetime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The time of matched output. |
| OutputNumber | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The value of output number. |
| OutputPicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The identifier of the output list of values. This field is a relationship field. **Relationship Name** OutputPicklistValue **Refers To** AttributePicklistValue |
| OutputString | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of output text. |
| ValueTransformGroupId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The identifier of the related transformation group. This field is a relationship field. **Relationship Name** ValueTransformGroup **Relationship Type** Master-detail **Refers To** ValTfrmGrp (the master object) |

=== ARTICLE: sforce_api_objects_valtfrmgrp.htm ===
---
page_id: sforce_api_objects_valtfrmgrp.htm
title: ValTfrmGrp
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_valtfrmgrp.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ValTfrmGrp

Represents a rule that determines how an order is broken into
         sub-orders with specific technical details that help in order fulfillment. The rule can be
         applied to a commercial or a technical product. This object is available in API
      version 61.0 and later.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| DestinationPrimitiveType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The data type of the output value. Valid values are: `Boolean` `Currency` `Date` `Datetime` `Number` `Percent`—Picklist Value `Text` |
| IsDestinationEnumerated | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the output is a list of values (`true`) or not (`false`). The default value is `false`. |
| IsSourceEnumerated | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the input is from a list of values (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date when a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the list mapping. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who owns this record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| SourcePrimitiveType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The data type of the input value. Valid values are: `Boolean` `Currency` `Date` `Datetime` `Number` `Percent`—Picklist Value `Text` |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The data mapping feature that uses this value transformation group. Valid value is `DFOListMapping` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
            
            
               

**[ValTfrmGrpShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: tooling_api_objects_customfulfillmentscopecnfg.htm ===
---
page_id: tooling_api_objects_customfulfillmentscopecnfg.htm
title: CustomFulfillmentScopeCnfg
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/tooling_api_objects_customfulfillmentscopecnfg.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CustomFulfillmentScopeCnfg

      Represents a user-defined scope to define and customize scope-specific
         validation and orchestration for flexible fulfillment. This object is available in API
      version 64.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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

- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AssetContextTag | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Context tag that's used to derive custom scope value from assets. This field is available in API version 65.0 and later. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. Name of the custom fulfillment scope. |
| DoesParticipatingAssetImpact | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. Indicates whether the technical assets related to sales transactions impact the fulfillment line item actions (`true`) or not (`false`). If set to `true`, Dynamic Revenue Orchestrator reuses the existing technical assets with the same custom value. The default value is `false`. |
| FallbackScope | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Scope that's used when custom scope can't be determined. Valid value is: `LineItem` If an empty value is returned, then ID of the line item is used. The default value is `LineItem`. |
| IsAssetized | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the fulfillment line items grouped by the custom scope are assetized `true` or not (`false`). If set to `false`, then the scope can't be associated with assetizable products. The default value is `false`. |
| ItemContextTag | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. Context tag that's used to derive custom scope from item context nodes. The supported value is of string type only. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the CustomFulfillmentScopeCnfg tooling API object. |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label of the custom fulfillment scope. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |

=== ARTICLE: tooling_api_objects_orchestrationplanctxmapping.htm ===
---
page_id: tooling_api_objects_orchestrationplanctxmapping.htm
title: OrchestrationPlanCtxMapping
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/tooling_api_objects_orchestrationplanctxmapping.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Dynamic Revenue Orchestrator
parent_page: dynamic_revenue_orchestrator_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrchestrationPlanCtxMapping

Represents an orchestration plan context mapping entry in the org.
         This entry is used to connect the business data in an object to the orchestration logic
         within Dynamic Revenue Orchestrator (DRO) by using the orchestration type. This object
      is available in API version 66.0.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

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

- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

               

            
| Field | Details |
| --- | --- |
| ContextDefinition | **Type** reference **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Name of the context definition to be used for the object. |
| ContextItemNode | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Required. Name of the node that represents an item in the context definition. |
| ContextMapping | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. Name of the context definition mapping to apply. This mapping must be related to the specified context definition. |
| ContextRootNode | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. Name of the node that represents the root in the context definition. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The language of the OrchestrationPlanCtxMapping tooling API object. Valid values are: |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label for the orchestration plan context mapping. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |
| ObjectName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** API name of the object for orchestration. |
| OrchestrationType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Name of the type of the orchestration plan. Valid value is `Generic`. |

