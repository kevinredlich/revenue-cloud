# Revenue Management Developer Guide 264 — sección: Usage Management (91 artículos)

=== ARTICLE: actions_obj_invoke_summary_creation.htm ===
---
page_id: actions_obj_invoke_summary_creation.htm
title: Invoke Summary Creation Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_invoke_summary_creation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoke Summary Creation Action

Invoke the service that creates various summaries, such as usage,
			ratable, and liable summaries where the usage amount is zero. The service also checks
			and updates the billing period of the usage entitlement account if the billing period is
			expired.

		
			

This action is available in API version 63.0 and later.

		

		

## Special Access Rules

			
			

The Invoke Summary Creation action is available in Enterprise, Developer,
				and Unlimited Editions where Usage Management is enabled. To use this action, you
				need the Usage Management Run Time User permission.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/invokeSummaryCreationService`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| usageEntitlementAccountId | **Type** string **Description** Required. ID of the usage entitlement account record that’s used to create summaries. |

		

		

## Outputs

			
			

None.

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Invoke Summary Creation
							action.

						

```
{
  "inputs": [
    {
      "usageEntitlementAccountId": "3ttDU00000000iZYAQ"
    }
  ]
}
```

						

This example shows a sample response for the Invoke Summary Creation
							action.

						

```
{
  "actionName": "invokeSummaryCreationService",
  "errors": null,
  "isSuccess": true
}
```

					

				
			

		

	

#### See Also

- [*Salesforce Help*: Permission Set Licenses, Personas, and User Permissions for
       Usage Management](https://help.salesforce.com/s/articleView?id=ind.um_usage_management_psls_and_personas.htm&language=en_US)

=== ARTICLE: actions_obj_process_consumption_overages.htm ===
---
page_id: actions_obj_process_consumption_overages.htm
title: Process Consumption Overages Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_process_consumption_overages.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Process Consumption Overages Action

Process consumption overages for the usage summary records with
				`SummaryComplete` status. This action uses the
			entitlement service to process the overages.

		
			

This action is available in API version 63.0 and later.

		

		

## Special Access Rules

			
			

The Process Consumption Overages action is available in Enterprise, Developer,
				and Unlimited Editions where Usage Management is enabled. To use this action, you
				need the Usage Management Run Time User permission.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/processConsumptionOverages`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| usageRatableSummaryId | **Type** string **Description** Required. ID of the usage ratable summary record that contains the consumption details, and is used to calculate consumption overages and create usage entitlement entry records. |

		

		

## Outputs

			
			

None.

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Process Consumption Overages
							action.

						

```
{
  "inputs": [
    {
      "usageRatableSummaryId": "3ttDU00000000iZYAQ"
    }
  ]
}
```

						

This example shows a sample response for the Process Consumption Overages
							action.

						

```
{
  "actionName": "processConsumptionOverages",
  "errors": null,
  "isSuccess": true
}
```

					

				
			

		

	

#### See Also

- [*Salesforce Help*: Permission Set Licenses, Personas, and User Permissions for
       Usage Management](https://help.salesforce.com/s/articleView?id=ind.um_usage_management_psls_and_personas.htm&language=en_US)

=== ARTICLE: actions_obj_refresh_usage_entitlement_bucket.htm ===
---
page_id: actions_obj_refresh_usage_entitlement_bucket.htm
title: Refresh Usage Entitlement Bucket Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_refresh_usage_entitlement_bucket.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Refresh Usage Entitlement Bucket Action

Refresh entitlements by evaluating the usage entitlement bucket
			records and creating a new usage entitlement entry.

		
			

This action is available in API version 63.0 and later.

		

		

## Special Access Rules

			
			

The Refresh Usage Entitlement Bucket action is available in Enterprise, Developer,
				and Unlimited Editions where Usage Management is enabled. To use this action, you
				need the Usage Management Run Time User permission.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/refreshUsageEntitlementBucket`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| transactionUsageEntitlementId | **Type** string **Description** Required. ID of the transaction usage entitlement record that's associated with the usage entitlement buckets that you need to refresh. |

		

		

## Outputs

			
			

None.

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Refresh Usage Entitlement
							Bucket action.

						

```
{
  "inputs": [
    {
      "transactionUsageEntitlementId": "3ttDU00000000iZYAQ"
    }
  ]
}
```

						

This example shows a sample response for the Refresh Usage Entitlement
							Bucket action.

						

```
{
  "actionName": "refreshUsageEntitlementBucket",
  "errors": null,
  "isSuccess": true
}
```

					

				
			

		

	

#### See Also

- [*Salesforce Help*: Permission Set Licenses, Personas, and User Permissions for
       Usage Management](https://help.salesforce.com/s/articleView?id=ind.um_usage_management_psls_and_personas.htm&language=en_US)

=== ARTICLE: actions_obj_retrigger_entitlement_creation_process.htm ===
---
page_id: actions_obj_retrigger_entitlement_creation_process.htm
title: Retrigger Entitlement Creation Process Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_retrigger_entitlement_creation_process.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Retrigger Entitlement Creation Process Action

Retrigger entitlement creation process for failed or unprocessed
            assets.

        

Trigger the entitlement creation process again in these scenarios.

                
- Process failed assets in the asset to entitlement journey.

                
- Assetize or create wallets for assets without corresponding records in Usage
                    Management.

            

This action is available in API version 65.0 and later.

        

## Special Access Rules

            
            

The Retrigger Entitlement Creation Process action is available in Enterprise,
                Developer, and       Unlimited Editions where Usage Management is enabled. To use
                this action, you need the Usage       Management Run Time User permission.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/retriggerEntlCreaProc`

                
                
                    

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
| assetId | **Type** string **Description** Required. ID of the asset for which you want to trigger the asset to entitlement process again. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Retrigger Entitlement Creation Process
                            action.

                        

```
{
  "inputs": [
    {
      "assetId": "02iSB000000JzZFYA0"
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Retrigger Entitlement Creation Process
                            action.

                        

```
[
  {
    "actionName": "retriggerEntlCreaProc",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": null,
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: connect_requests_consumption_traceabilities_input.htm ===
---
page_id: connect_requests_consumption_traceabilities_input.htm
title: Consumption Traceabilities Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_consumption_traceabilities_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Consumption Traceabilities Input

Input representation of the details of the liable summary IDs that are used to trace the
    consumption.

**JSON example**

: 

```
{
  "liableSummaryIds": [
    "1HG000000000001"
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `liableSummaryIds` | String[] | List of liable summary IDs to trace the consumption. | Required | 66.0 |

=== ARTICLE: connect_requests_usage_activation_input.htm ===
---
page_id: connect_requests_usage_activation_input.htm
title: Usage Product Activation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_usage_activation_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Activation Input

Input representation of a usage product activation request.

**JSON example**

: 
            

```
{
  "shouldValidateProductSetup": false,
  "activationRequests": [
    {
      "productId": "01txx0000006i2gAAA",
      "usageResourceIds": [
        "0hUxx000000001",
        "0hUxx000000002"
      ]
    }
  ]
}

```

          

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `activation​Requests` | [Usage Activation Request Input](./connect_requests_usage_activation_request_input.htm.md)[] | List of activation requests. Each entry identifies a product and the usage resources to activate for that product. This list accepts only one entry. If you include more, the API returns the `MAX_LIMIT_EXCEEDED` error. | Required | 67.0 |
| `shouldValidate​ProductSetup` | Boolean | Indicates whether to run product setup validation before activation (`true`) or not (`false`). The default value is `true`. | Optional | 67.0 |

=== ARTICLE: connect_requests_usage_activation_request_input.htm ===
---
page_id: connect_requests_usage_activation_request_input.htm
title: Usage Activation Request Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_usage_activation_request_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Activation Request Input

Input representation for a single product entry in a usage product activation request.
    Each entry identifies one product and the usage resources to activate for that
    product.

**JSON example**

: 
            

```
{
  "productId": "01txx0000006i2gAAA",
  "usageResourceIds": [
    "0hUxx000000001",
    "0hUxx000000002"
  ]
}
```

          

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `product​Id` | String | ID of the Product2 record whose associated usage records are activated. | Required | 67.0 |
| `usage​Resource​Ids` | String[] | List of usage resource IDs to activate for the given product. The activation extends to all design-time records linked to these resources, such as product usage grants, usage policies, units of measure, units of measure classes, and rate card entries. If this property is empty or omitted, all usage records associated with the given product are activated. | Optional | 67.0 |

=== ARTICLE: connect_requests_usage_product_validation_input.htm ===
---
page_id: connect_requests_usage_product_validation_input.htm
title: Usage Product Validation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_usage_product_validation_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Validation Input

Input representation of the usage product validation request.

**JSON example**

: 

```
{
  "productIds": [
    "01txx0000006i2gAAA",
    "01txx0000006j2gAAA"
  ],
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-12-31T23:59:59Z"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `productIds` | String[] | List of product IDs to be validated. The maximum limit is `10` valid product IDs. | Required | 66.0 |
| `startDate` | String | Start date of the date range in which all active records are validated. | Optional | 66.0 |
| `endDate` | String | End date of the date range in which all active records are validated. | Optional | 66.0 |

=== ARTICLE: connect_resources_asset_usage_details.htm ===
---
page_id: connect_resources_asset_usage_details.htm
title: Asset Usage Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_asset_usage_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset Usage Details (GET)

Get details of a usage-based product associated with an asset. This
      covers details of grants, resources, and configured rates for the product, including
      negotiated rates in case of a rate override.

    

Here are the details that this API returns.

        
- Grants and resources for the product, if rates aren’t configured.

        
- Grants, resources, and any configured rates for the product. The rates are returned by
          the [Rate Plan (GET) API](./connect_resources_get_rate_plan.htm.md).

        
- Resources that include grants, if applicable, and any negotiated rates for the product
          in case of a rate override request.

      

This API doesn't return binding target rates. Use the [Binding Object Usage Details
          API](./connect_resources_retrieve_binding_object_details.htm.md) to retrieve binding target rates.

    
      
        
          

**Resource**

          
: 
            

```
/asset-management/assets/assetId/usage-details
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/asset-management/assets/02iRM0000000tCdYAI/usage-details
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Path parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetId` | String | ID of the asset. | Required | 63.0 |

          

        
        
          

**Query parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
- 
- 

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `effectiveDate` | String | Date that's used to search for the applicable rate card entries. | Required | 63.0 |
| `optionalFields` | String[] | Custom fields that you can use to query these objects. [AssetRateCardEntry](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_assetratecardentry.htm) [AssetRateAdjustment](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_assetrateadjustment.htm) | Optional | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Usage
            Details](./connect_responses_usage_detail_output.htm.md)

=== ARTICLE: connect_resources_consumption_traceabilities.htm ===
---
page_id: connect_resources_consumption_traceabilities.htm
title: Consumption Traceabilities (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_consumption_traceabilities.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Consumption Traceabilities (POST)

Get a comprehensive breakdown of overage charges and resource drawdown,
      enabling you to view information that's applicable to specific invoice lines.

This API provides an automated, clear, and traceable breakdown of all charges with
        details of specific rates, tiers, and discounts.

        
          

**Resource**

          
: 
            

```
/revenue/usage-management/consumption/actions/trace
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/usage-management/consumption/actions/trace
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "liableSummaryIds": [
    "1HG000000000001"
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `liableSummaryIds` | String[] | List of liable summary IDs to trace the consumption. | Required | 66.0 |

          

        
        
          

**Response body for POST**

          
: [Consumption
              Traceabilities](./connect_responses_consumption_traceabilities_output.htm.md)

=== ARTICLE: connect_resources_order_usage_details.htm ===
---
page_id: connect_resources_order_usage_details.htm
title: Order Item Usage Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_order_usage_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Order Item Usage Details (GET)

Get details of a usage-based product associated with an order
      item.

    

Here are the details that this API returns.

        
- Grants and resources for the product, if rates aren’t configured.

        
- Grants, resources, and any configured rates for the product. The rates are returned by
          the [Rate Plan (GET) API](./connect_resources_get_rate_plan.htm.md).

        
- Resources that include grants, if applicable, and any negotiated rates for the product
          in case of a rate override request.

      

This API doesn't return binding target rates. Use the [Binding Object Usage Details
          API](./connect_resources_retrieve_binding_object_details.htm.md) to retrieve binding target rates.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/sales-orders/line-items/orderItemId/usage-details
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/sales-orders/line-items/802SG000003vZ15YAE/usage-details
```

            

```
https://yourInstance.salesforce.com/services/data​/v68.0/commerce/sales-orders/line-items/802SG000003vZ15YAE/usage-details?optionalFields=OrderItemRateCardEntry.MyCustomDate__c,OrderItemRateCardEntry.MyCustomNumber__c,OrderItemRateAdjustment.myCustomString__c
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Path parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `orderItemId` | String | ID of the order item. | Required | 63.0 |

          

        
        
          

**Query parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
- 
- 

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `effectiveDate` | String | Date that's used to search for the applicable rate card entries. | Optional | 63.0 |
| `optionalFields` | String[] | Custom fields that you can use to query these objects. [OrderItemRateCardEntry](./sforce_api_objects_orderitemratecardentry.htm.md) [OrderItemRateAdjustment](./sforce_api_objects_orderitemrateadjustment.htm.md) | Optional | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Usage
            Details](./connect_responses_usage_detail_output.htm.md)

=== ARTICLE: connect_resources_quote_usage_details.htm ===
---
page_id: connect_resources_quote_usage_details.htm
title: Quote Line Item Usage Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_quote_usage_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Quote Line Item Usage Details (GET)

Get details of a usage-based product associated with a quote line
      item.

    

Here are the details that this API returns.

        
- Grants and resources for the product, if rates aren’t configured.

        
- Grants, resources, and any configured rates for the product. The rates are returned by
          the [Rate Plan (GET) API](./connect_resources_get_rate_plan.htm.md).

        
- Resources that include grants, if applicable, and any negotiated rates for the product
          in case of a rate override request.

      

This API doesn't return binding target rates. Use the [Binding Object Usage Details
          API](./connect_resources_retrieve_binding_object_details.htm.md) to retrieve binding target rates.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/quotes/line-items/quoteLineItemId/usage-details
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/quotes/line-items/0QLXXXXXXXXXXXABC/usage-details
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
- 
- 

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `effectiveDate` | String | Date that's used to search for the applicable rate card entries. | Optional | 62.0 |
| `optionalFields` | String[] | Custom fields that you can use to query these objects. [QuoteLineRateCardEntry](./sforce_api_objects_quotelineratecardentry.htm.md) [QuoteLineRateAdjustment](./sforce_api_objects_quotelinerateadjustment.htm.md) | Optional | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Usage
            Details](./connect_responses_usage_detail_output.htm.md)

=== ARTICLE: connect_resources_retrieve_binding_object_details.htm ===
---
page_id: connect_resources_retrieve_binding_object_details.htm
title: Binding Object Usage Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_retrieve_binding_object_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Usage Details (GET)

Get details of grants, resources, rates, and any configured policies
      for a specified binding object.

    

Use this API to display the details for a binding object during the selling journey.
        Additionally, display the details after assetization on the selected binding objects.

The supported binding objects are Account, Contract, BindingObjectCustomExt, or Anchor Asset
        that's not bound to a target.

        
          

**Resource**

          
: 
            

```
/revenue/usage-management/binding-objects/bindingObjectId/actions/usage-details
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/usage-management/binding-objects/1BRxx0000004C9EGAU/actions/usage-details?effectiveDate=2025-08-07
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Path parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `bindingObjectId` | String | ID of the binding object. | Required | 65.0 |

          

        
        
          

**Query parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `effectiveDate` | String | Date filter that's used to retrieve the grants, rates, and applicable policies as of the specified date in `yyyy-MM-dd` format. | Required | 65.0 |

          

        
        
          

**Response body for GET**

          
: [Binding Object Usage
              Detail](./connect_responses_usage_detail_binding_object_output.htm.md)

=== ARTICLE: connect_resources_usage_product_activation.htm ===
---
page_id: connect_resources_usage_product_activation.htm
title: Usage Product Activation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_usage_product_activation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Activation (POST)

Activate a usage product and its related records, such as usage resources, grants,
    policies, and rate card entries, in a single request.

    
      

Keep these considerations in mind when you use this API.

      
        
- In version 67.0, each request activates one
          product.
          If a request includes more than one product, the API returns the `MAX_LIMIT_EXCEEDED` error.

        
- Each record in the request stays in Draft status until activation runs. If any record
          for the product fails to activate, the API rolls back all activations for that
          product.

        
- The records activate in the order required by their dependencies, so a child record
          never activates before its parent.

        
- Each request activates a maximum of 200 records, including the product and all of its
          associated child records. If the request exceeds 200 records, the API returns the `MAX_LIMIT_EXCEEDED` error.

      

      
        
          

**Resource**

          
: 
            

```
/revenue/usage-management/usage-products/actions/activate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/usage-management/usage-products/actions/activate
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
  "shouldValidateProductSetup": false,
  "activationRequests": [
    {
      "productId": "01txx0000006i2gAAA",
      "usageResourceIds": [
        "0hUxx000000001",
        "0hUxx000000002"
      ]
    }
  ]
}

```

          

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `activation​Requests` | [Usage Activation Request Input](./connect_requests_usage_activation_request_input.htm.md)[] | List of activation requests. Each entry identifies a product and the usage resources to activate for that product. This list accepts only one entry. If you include more, the API returns the `MAX_LIMIT_EXCEEDED` error. | Required | 67.0 |
| `shouldValidate​ProductSetup` | Boolean | Indicates whether to run product setup validation before activation (`true`) or not (`false`). The default value is `true`. | Optional | 67.0 |

          

        

          

        
        
          

**Response body for POST**

          
: [Usage Product Activation](./connect_responses_usage_activation_output.htm.md)

=== ARTICLE: connect_resources_usage_product_validation.htm ===
---
page_id: connect_resources_usage_product_validation.htm
title: Usage Product Validation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_usage_product_validation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Validation (POST)

Validate cross-object relationships and business rules for usage-based products.

This API returns validation results with errors and warnings.

        
          

**Resource**

          
: 
            

```
/revenue/usage-management/usage-products/actions/validate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/usage-management/usage-products/actions/validate
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "productIds": [
    "01txx0000006i2gAAA",
    "01txx0000006j2gAAA"
  ],
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-12-31T23:59:59Z"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `productIds` | String[] | List of product IDs to be validated. The maximum limit is `10` valid product IDs. | Required | 66.0 |
| `startDate` | String | Start date of the date range in which all active records are validated. | Optional | 66.0 |
| `endDate` | String | End date of the date range in which all active records are validated. | Optional | 66.0 |

          

        
        
          

**Response body for POST**

          
: [Usage Product Validation](./connect_responses_usage_product_validation_output.htm.md)

=== ARTICLE: connect_responses_asset_detail_output.htm ===
---
page_id: connect_responses_asset_detail_output.htm
title: Asset Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_asset_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset Detail

Output representation of the details of a specific asset.

      
        
          

**JSON example**

          
: 
            

```
{
  "assets": [
    {
      "assetId": "ASSET1",
      "usageEntitlementAccountId": "1EA000000000001",
      "grantBindingTargetId": "1GB000000000001",
      "billingPeriods": [
        {
          "startDate": "2025-01-01",
          "endDate": "2025-01-31",
          "resources": [
            {
              "liableSummaryId": "1HG000000000001",
              "usageResourceId": "1BX000000000004",
              "usageResourceName": "SF Credits",
              "usageResourceUomId": "1UM000000000001",
              "usageResourceUomUnitCode": "CREDIT",
              "resourceTotalOverageQuantity": 333.33,
              "resourceTotalOverageAmount": 333.33,
              "resourceTotalConsumption": 1500,
              "rateAndConsumptionSources": [
                {
                  "startDate": "2025-01-01",
                  "endDate": "2025-01-31",
                  "rateUomId": "USD",
                  "ratableSummaryId": "URS3",
                  "ratingExecutionId": "1RE000000000001",
                  "overageQuantity": 333.33,
                  "overageAmount ": 333.33,
                  "totalConsumption": 1500,
                  "netUnitRate": 1,
                  "consumptionSources": [
                    {
                      "consumptionSourceId": "1AE000000000001",
                      "consumptionUnit": 500
                    },
                    {
                      "consumptionSourceId": "1CO000000000001",
                      "consumptionUnit": 375,
                      "commitRate": 1.5,
                      "targetRate": 2,
                      "cmtAssetRatableSummaryId": "URSCARID1"
                    },
                    {
                      "consumptionSourceId": "1CO000000000002",
                      "consumptionUnit": 125,
                      "commitRate": 0.75,
                      "targetRate": 1,
                      "cmtAssetRatableSummaryId": "URSCARID2"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `assetId` | String | Unique identifier of the related asset. | Big, 66.0 | 66.0 |
| `billingPeriods` | [Billing Period](./connect_responses_billing_period_output.htm.md)[] | List of billing periods for the asset. | Big, 66.0 | 66.0 |
| `grantBinding​TargetId` | String | ID of the object the consumption is bound to. | Big, 66.0 | 66.0 |
| `usageEntitlement​AccountId` | String | ID of the account that holds the usage entitlement. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_billing_period_output.htm ===
---
page_id: connect_responses_billing_period_output.htm
title: Billing Period
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_period_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Period

Output representation of the details of a specific billing period.

      
        
          

**JSON example**

          
: 
            

```
{
  "billingPeriods": [
    {
      "startDate": "2025-01-01",
      "endDate": "2025-01-31",
      "resources": [
        {
          "liableSummaryId": "1HG000000000001",
          "usageResourceId": "1BX000000000004",
          "usageResourceName": "SF Credits",
          "usageResourceUomId": "1UM000000000001",
          "usageResourceUomUnitCode": "CREDIT",
          "resourceTotalOverageQuantity": 333.33,
          "resourceTotalOverageAmount": 333.33,
          "resourceTotalConsumption": 1500,
          "rateAndConsumptionSources": [
            {
              "startDate": "2025-01-01",
              "endDate": "2025-01-31",
              "rateUomId": "USD",
              "ratableSummaryId": "URS3",
              "ratingExecutionId": "1RE000000000001",
              "overageQuantity": 333.33,
              "overageAmount ": 333.33,
              "totalConsumption": 1500,
              "netUnitRate": 1,
              "consumptionSources": [
                {
                  "consumptionSourceId": "1AE000000000001",
                  "consumptionUnit": 500
                },
                {
                  "consumptionSourceId": "1CO000000000001",
                  "consumptionUnit": 375,
                  "commitRate": 1.5,
                  "targetRate": 2,
                  "cmtAssetRatableSummaryId": "URSCARID1"
                },
                {
                  "consumptionSourceId": "1CO000000000002",
                  "consumptionUnit": 125,
                  "commitRate": 0.75,
                  "targetRate": 1,
                  "cmtAssetRatableSummaryId": "URSCARID2"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `endDate` | String | End date of the billing period. | Big, 66.0 | 66.0 |
| `resources` | [Resource Detail](./connect_responses_resource_detail_output.htm.md)[] | List of usage resources within the billing period. | Big, 66.0 | 66.0 |
| `startDate` | String | Start date of the billing period. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_binding_object_detail_output.htm ===
---
page_id: connect_responses_binding_object_detail_output.htm
title: Binding Object Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Detail

Output representation of the list of records with the binding target details.

        
          

**JSON example**

          
: This example includes the details of a binding
            object.

```
{
  "records": [
    {
      "bindingObjectRate": {
        "id": "1QNSB0000001JyH4AU,1QNSB0000001JyI4AU",
        "negotiatedRate": null,
        "negotiatedRateAdjustments": [
          {
            "lowerBound": 101,
            "name": null,
            "rateAdjustmentId": "1DMSB000001N3C74AK",
            "rateAdjustmentType": "Amount",
            "rateAdjustmentValue": 10,
            "tierUnitOfMeasure": "USD",
            "upperBound": null
          },
          {
            "lowerBound": 1,
            "name": null,
            "rateAdjustmentId": "1DMSB000001N3C64AK",
            "rateAdjustmentType": "Percentage",
            "rateAdjustmentValue": 30,
            "tierUnitOfMeasure": "USD",
            "upperBound": 100
          }
        ],
        "rate": 100,
        "rateCardEntryId": "1CJSB000000207R4AQ,1CJSB000000207S4AQ",
        "rateUnitOfMeasureName": "USD"
      },
      "bindingObjectResourceGrantAndPolicyDetail": {
        "bindingObjectGrantDetail": [
          {
            "effectiveEndDate": "Sat Oct 04 23:59:59 GMT 2025",
            "effectiveStartDate": "Fri Sep 05 00:00:00 GMT 2025",
            "grantType": "Grant",
            "id": "1B0SB0000000Eiv0AE",
            "product": {
              "id": "01tSB000006XMtqYAG"
            },
            "quantity": 100,
            "record": {
              "id": "02iSB000000IoETYA0"
            },
            "unitOfMeasure": {
              "id": "0hESB0000003yfp2AA"
            },
            "usageRefreshPolicy": {
              "id": "1BYSB0000001lOH4AY",
              "negotiable": null
            },
            "usageRolloverPolicy": {
              "id": "1BVSB000000A1xJ4AS",
              "negotiable": null
            },
            "validityPeriodTerm": 1,
            "validityPeriodUnit": "Month"
          }
        ],
        "bindingObjectResourcePolicyDetail": {
          "drawdownOrder": "ExpiringFirst",
          "id": "1X2SB00000002WT0AY",
          "ratingFrequencyPolicy": {
            "id": "1HJSB0000000G3B4AU",
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": "1cfSB0000001xHPYAY",
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageOveragePolicy": {
            "id": "7UkSB00000002OP0AY",
            "negotiable": null
          }
        }
      },
      "usageResource": {
        "id": "1BRSB0000001x4h4AA"
      }
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `binding​ObjectRate` | [Binding Object Rate](./connect_responses_binding_object_rate_output.htm.md) | Details about the `Binding Object Rates` object or `Asset Rates` object. | Big, 65.0 | 65.0 |
| `binding​Object​ResourceGrantAnd​PolicyDetail` | [Binding Object Resource Grant and Policy Detail](./connect_responses_binding_object_resource_grant_and_policy_detail_output.htm.md) | Details about the resource grants and binding policies. | Big, 65.0 | 65.0 |
| `usage​Resource` | [Lookup Detail](./connect_responses_lookup_detail_output.htm.md) | Details of the usage resource such as the ID of the record. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_binding_object_grant_detail_output.htm ===
---
page_id: connect_responses_binding_object_grant_detail_output.htm
title: Binding Object Grant Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_grant_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Grant Detail

Output representation of the details of usage resource grants for a specified binding
    object.

        
          

**JSON example**

          
: This example includes the details of usage resource grants for a specified binding
            object.

```
{
  "bindingObjectGrantDetail": [
    {
      "effectiveEndDate": "Sat Oct 04 23:59:59 GMT 2025",
      "effectiveStartDate": "Fri Sep 05 00:00:00 GMT 2025",
      "grantType": "Grant",
      "id": "1B0SB0000000Eiv0AE",
      "product": {
        "id": "01tSB000006XMtqYAG"
      },
      "quantity": 100,
      "record": {
        "id": "02iSB000000IoETYA0"
      },
      "unitOfMeasure": {
        "id": "0hESB0000003yfp2AA"
      },
      "usageRefreshPolicy": {
        "id": "1BYSB0000001lOH4AY",
        "negotiable": null
      },
      "usageRolloverPolicy": {
        "id": "1BVSB000000A1xJ4AS",
        "negotiable": null
      },
      "validityPeriodTerm": 1,
      "validityPeriodUnit": "Month"
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `effective​EndDate` | String | Effective end date for the asset lifecycle. | Big, 65.0 | 65.0 |
| `effective​StartDate` | String | Effective start date for the asset lifecycle. | Big, 65.0 | 65.0 |
| `grantType` | String | Type of usage resource grant. | Big, 65.0 | 65.0 |
| `id` | String | ID of the `Transaction Usage Entitlement` record responsible for the grant. | Big, 65.0 | 65.0 |
| `product` | [Lookup Detail](./connect_responses_lookup_detail_output.htm.md) | Details of the product. | Big, 65.0 | 65.0 |
| `quantity` | Double | Quantity of the binding object usage resource grant. | Big, 65.0 | 65.0 |
| `record` | [Lookup Detail](./connect_responses_lookup_detail_output.htm.md) | ID of the asset. | Big, 65.0 | 65.0 |
| `unitOf​Measure` | [Lookup Detail](./connect_responses_lookup_detail_output.htm.md) | unit of measure of the usage resource. | Big, 65.0 | 65.0 |
| `usageRefresh​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | ID of the usage grant refresh policy. | Big, 65.0 | 65.0 |
| `usageRollover​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | ID of the usage grant rollover policy. | Big, 65.0 | 65.0 |
| `validityPeriod​Term` | Double | Validity period term of the usage resource grant. | Big, 65.0 | 65.0 |
| `validityPeriod​Unit` | String | Validity period unit of the usage resource grant. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_binding_object_rate_adjustments_output.htm ===
---
page_id: connect_responses_binding_object_rate_adjustments_output.htm
title: Binding Object Rate Adjustments
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_rate_adjustments_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Rate Adjustments

Output representation of the details of binding target rate adjustments.

      
        
          

**JSON example**

          
: This example includes the details of binding target rate
            adjustments.

```
{
  "negotiatedRateAdjustments": [
    {
      "lowerBound": 101,
      "name": null,
      "rateAdjustmentId": "1DMSB000001N3C74AK",
      "rateAdjustmentType": "Amount",
      "rateAdjustmentValue": 10,
      "tierUnitOfMeasure": "USD",
      "upperBound": null
    },
    {
      "lowerBound": 1,
      "name": null,
      "rateAdjustmentId": "1DMSB000001N3C64AK",
      "rateAdjustmentType": "Percentage",
      "rateAdjustmentValue": 30,
      "tierUnitOfMeasure": "USD",
      "upperBound": 100
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `lowerBound` | Double | Minimum quantity for the adjustment to be applicable. | Small, 65.0 | 65.0 |
| `name` | String | Name of the tier or binding object rate adjustment. | Small, 65.0 | 65.0 |
| `rateAdjustmentId` | String | ID of the binding object rate adjustment. | Small, 65.0 | 65.0 |
| `rateAdjustmentType` | String | Type of the binding object rate adjustment. | Small, 65.0 | 65.0 |
| `rateAdjustmentValue` | Double | Value of the binding object rate adjustment. | Small, 65.0 | 65.0 |
| `tierUnitOfMeasure` | String | Unit of measure that represents the tier or binding object rate adjustment. | Small, 65.0 | 65.0 |
| `upperBound` | Double | Maximum quantity for the adjustment to be applicable. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_binding_object_rate_output.htm ===
---
page_id: connect_responses_binding_object_rate_output.htm
title: Binding Object Rate
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_rate_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Rate

Output representation of the details of Binding Object Rates object or Asset Rates
    object.

        
          

**JSON example**

          
: This example includes the details of a binding object
            rate.

```
{
  "bindingObjectRate": {
    "id": "1QNSB0000001JyH4AU,1QNSB0000001JyI4AU",
    "negotiatedRate": null,
    "negotiatedRateAdjustments": [
      {
        "lowerBound": 101,
        "name": null,
        "rateAdjustmentId": "1DMSB000001N3C74AK",
        "rateAdjustmentType": "Amount",
        "rateAdjustmentValue": 10,
        "tierUnitOfMeasure": "USD",
        "upperBound": null
      },
      {
        "lowerBound": 1,
        "name": null,
        "rateAdjustmentId": "1DMSB000001N3C64AK",
        "rateAdjustmentType": "Percentage",
        "rateAdjustmentValue": 30,
        "tierUnitOfMeasure": "USD",
        "upperBound": 100
      }
    ],
    "rate": 100,
    "rateCardEntryId": "1CJSB000000207R4AQ,1CJSB000000207S4AQ",
    "rateUnitOfMeasureName": "USD"
  }
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the `Binding Object Rate Card Entry` or `Asset Rate Card Entry` object. | Big, 65.0 | 65.0 |
| `negotiated​Rate` | Double | Negotiated rate available in the `Binding Object Rate Card Entry` or `Asset Rate Card Entry` object. | Big, 65.0 | 65.0 |
| `negotiatedRate​Adjustments` | [Binding Object Rate Adjustments](./connect_responses_binding_object_rate_adjustments_output.htm.md)[] | List of rate adjustments available in the `Binding Object Rate Adjustment` or `Asset Rate Adjustment`. | Big, 65.0 | 65.0 |
| `rate` | Double | Rate of the rate card entry associated to the `Binding Object Rate Card Entry` or `Asset Rate Card Entry` object. | Big, 65.0 | 65.0 |
| `rateCard​EntryId` | String | ID of the rate card entry associated to the `Binding Object Rate Card Entry` or `Asset Rate Card Entry` object. | Big, 65.0 | 65.0 |
| `rateUnitOf​MeasureName` | String | Rate unit of measure of the rates. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_binding_object_resource_grant_and_policy_detail_output.htm ===
---
page_id: connect_responses_binding_object_resource_grant_and_policy_detail_output.htm
title: Binding Object Resource Grant And Policy Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_resource_grant_and_policy_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Resource Grant And Policy Detail

Output representation of the details of resource grants and binding policies.

        
          

**JSON example**

          
: This example includes the details of resource grants and binding policies for a
            specified binding object.

```
{
  "bindingObjectResourceGrantAndPolicyDetail": {
    "bindingObjectGrantDetail": [
      {
        "effectiveEndDate": "Sat Oct 04 23:59:59 GMT 2025",
        "effectiveStartDate": "Fri Sep 05 00:00:00 GMT 2025",
        "grantType": "Grant",
        "id": "1B0SB0000000Eiv0AE",
        "product": {
          "id": "01tSB000006XMtqYAG"
        },
        "quantity": 100,
        "record": {
          "id": "02iSB000000IoETYA0"
        },
        "unitOfMeasure": {
          "id": "0hESB0000003yfp2AA"
        },
        "usageRefreshPolicy": {
          "id": "1BYSB0000001lOH4AY",
          "negotiable": null
        },
        "usageRolloverPolicy": {
          "id": "1BVSB000000A1xJ4AS",
          "negotiable": null
        },
        "validityPeriodTerm": 1,
        "validityPeriodUnit": "Month"
      }
    ],
    "bindingObjectResourcePolicyDetail": {
      "drawdownOrder": "ExpiringFirst",
      "id": "1X2SB00000002WT0AY",
      "ratingFrequencyPolicy": {
        "id": "1HJSB0000000G3B4AU",
        "negotiable": null
      },
      "usageAggregationPolicy": {
        "id": "1cfSB0000001xHPYAY",
        "negotiable": null
      },
      "usageCommitmentPolicy": {
        "id": null,
        "negotiable": null
      },
      "usageOveragePolicy": {
        "id": "7UkSB00000002OP0AY",
        "negotiable": null
      }
    }
  }
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `bindingObject​Grant​Detail` | [Binding Object Grant Detail](./connect_responses_binding_object_grant_detail_output.htm.md)[] | Details of the negotiated resource grants for the specified binding object. | Big, 65.0 | 65.0 |
| `bindingObject​ResourcePolicy​Detail` | [Binding Object Resource Policy Detail](./connect_responses_binding_object_resource_policy_detail_output.htm.md) | Detail of the binding policies. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_binding_object_resource_policy_detail_output.htm ===
---
page_id: connect_responses_binding_object_resource_policy_detail_output.htm
title: Binding Object Resource Policy Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_binding_object_resource_policy_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Resource Policy Detail

Output representation of the details of a usage resource policy.

        
          

**JSON example**

          
: This example includes the details of a usage resource
            policy.

```
{
  "bindingObjectResourcePolicyDetail": {
    "drawdownOrder": "ExpiringFirst",
    "id": "1X2SB00000002WT0AY",
    "ratingFrequencyPolicy": {
      "id": "1HJSB0000000G3B4AU",
      "negotiable": null
    },
    "usageAggregationPolicy": {
      "id": "1cfSB0000001xHPYAY",
      "negotiable": null
    },
    "usageCommitmentPolicy": {
      "id": null,
      "negotiable": null
    },
    "usageOveragePolicy": {
      "id": "7UkSB00000002OP0AY",
      "negotiable": null
    }
  }
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `drawdown​Order` | String | Specifies the order or way to process the drawdown. See [Usage Management Essentials](https://help.salesforce.com/s/articleView?id=ind.usage_management_essentials.htm&language=en_US) to know more about a drawdown process. | Big, 65.0 | 65.0 |
| `id` | String | ID of the `Binding Object Usage Resource Policy` record. | Big, 65.0 | 65.0 |
| `ratingFrequency​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the rating frequency policy. | Big, 65.0 | 65.0 |
| `usageAggregation​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the usage aggregation policy. | Big, 65.0 | 65.0 |
| `usageCommitment​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the commitment policy of the usage resource. | Big, 65.0 | 65.0 |
| `usageOverage​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the overage policy of the usage resource. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_consumption_source_detail_output.htm ===
---
page_id: connect_responses_consumption_source_detail_output.htm
title: Consumption Source Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_consumption_source_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Consumption Source Detail

Output representation of the details of a specific consumption source.

      
        
          

**JSON example**

          
: 
            

```
{
  "consumptionSources": [
    {
      "consumptionSourceId": "1AE000000000001",
      "consumptionUnit": 500
    },
    {
      "consumptionSourceId": "1CO000000000001",
      "consumptionUnit": 375,
      "commitRate": 1.5,
      "targetRate": 2,
      "cmtAssetRatableSummaryId": "URSCARID1"
    },
    {
      "consumptionSourceId": "1CO000000000002",
      "consumptionUnit": 125,
      "commitRate": 0.75,
      "targetRate": 1,
      "cmtAssetRatableSummaryId": "URSCARID2"
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `cmtAssetRatable​SummaryId` | String | ID for querying rating waterfall. | Big, 66.0 | 66.0 |
| `commitRate` | Double | Net unit rate at which drawdown is done for commitment products. | Big, 66.0 | 66.0 |
| `consumption​SourceId` | String | Object on which the consumption was recorded. | Big, 66.0 | 66.0 |
| `consumption​Unit` | Double | Recorded quantity of consumption. | Big, 66.0 | 66.0 |
| `targetRate` | Double | Input unit rate which is used for commitment products. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_consumption_traceabilities_data_output.htm ===
---
page_id: connect_responses_consumption_traceabilities_data_output.htm
title: Consumption Traceabilities Data
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_consumption_traceabilities_data_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Consumption Traceabilities Data

Output representation of the list of asset details.

      
        
          

**JSON example**

          
: 
            

```
{
  "data": {
    "assets": [
      {
        "assetId": "ASSET1",
        "usageEntitlementAccountId": "1EA000000000001",
        "grantBindingTargetId": "1GB000000000001",
        "billingPeriods": [
          {
            "startDate": "2025-01-01",
            "endDate": "2025-01-31",
            "resources": [
              {
                "liableSummaryId": "1HG000000000001",
                "usageResourceId": "1BX000000000004",
                "usageResourceName": "SF Credits",
                "usageResourceUomId": "1UM000000000001",
                "usageResourceUomUnitCode": "CREDIT",
                "resourceTotalOverageQuantity": 333.33,
                "resourceTotalOverageAmount": 333.33,
                "resourceTotalConsumption": 1500,
                "rateAndConsumptionSources": [
                  {
                    "startDate": "2025-01-01",
                    "endDate": "2025-01-31",
                    "rateUomId": "USD",
                    "ratableSummaryId": "URS3",
                    "ratingExecutionId": "1RE000000000001",
                    "overageQuantity": 333.33,
                    "overageAmount ": 333.33,
                    "totalConsumption": 1500,
                    "netUnitRate": 1,
                    "consumptionSources": [
                      {
                        "consumptionSourceId": "1AE000000000001",
                        "consumptionUnit": 500
                      },
                      {
                        "consumptionSourceId": "1CO000000000001",
                        "consumptionUnit": 375,
                        "commitRate": 1.5,
                        "targetRate": 2,
                        "cmtAssetRatableSummaryId": "URSCARID1"
                      },
                      {
                        "consumptionSourceId": "1CO000000000002",
                        "consumptionUnit": 125,
                        "commitRate": 0.75,
                        "targetRate": 1,
                        "cmtAssetRatableSummaryId": "URSCARID2"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `assets` | [Asset Detail](./connect_responses_asset_detail_output.htm.md)[] | List of assets for the specified liable summaries. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_consumption_traceabilities_output.htm ===
---
page_id: connect_responses_consumption_traceabilities_output.htm
title: Consumption Traceabilities
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_consumption_traceabilities_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Consumption Traceabilities

Output representation of the overage and resource drawdown details.

      
        
          

**JSON example**

          
: 
            

```
{
  "success": true,
  "data": {
    "assets": [
      {
        "assetId": "ASSET1",
        "usageEntitlementAccountId": "1EA000000000001",
        "grantBindingTargetId": "1GB000000000001",
        "billingPeriods": [
          {
            "startDate": "2025-01-01",
            "endDate": "2025-01-31",
            "resources": [
              {
                "liableSummaryId": "1HG000000000001",
                "usageResourceId": "1BX000000000004",
                "usageResourceName": "SF Credits",
                "usageResourceUomId": "1UM000000000001",
                "usageResourceUomUnitCode": "CREDIT",
                "resourceTotalOverageQuantity": 333.33,
                "resourceTotalOverageAmount": 333.33,
                "resourceTotalConsumption": 1500,
                "rateAndConsumptionSources": [
                  {
                    "startDate": "2025-01-01",
                    "endDate": "2025-01-31",
                    "rateUomId": "USD",
                    "ratableSummaryId": "URS3",
                    "ratingExecutionId": "1RE000000000001",
                    "overageQuantity": 333.33,
                    "overageAmount ": 333.33,
                    "totalConsumption": 1500,
                    "netUnitRate": 1,
                    "consumptionSources": [
                      {
                        "consumptionSourceId": "1AE000000000001",
                        "consumptionUnit": 500
                      },
                      {
                        "consumptionSourceId": "1CO000000000001",
                        "consumptionUnit": 375,
                        "commitRate": 1.5,
                        "targetRate": 2,
                        "cmtAssetRatableSummaryId": "URSCARID1"
                      },
                      {
                        "consumptionSourceId": "1CO000000000002",
                        "consumptionUnit": 125,
                        "commitRate": 0.75,
                        "targetRate": 1,
                        "cmtAssetRatableSummaryId": "URSCARID2"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    ],
    "error": null
  }
}
```

          

        
      

| zProperty Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `data` | [Consumption Traceabilities Data](./connect_responses_consumption_traceabilities_data_output.htm.md)[] | Payload that contains the traceability details. | Big, 66.0 | 66.0 |
| `error` | [Generic Error Details](./connect_responses_generic_error_output.htm.md)[] | Error details if the request isn't successful. | Big, 66.0 | 66.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_error_message_output.htm ===
---
page_id: connect_responses_error_message_output.htm
title: Error Message
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_error_message_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Message

Output representation of the details of records that failed with this specific
    error.

      
        
          

**JSON example**

          
: This example shows an error message with
            details.

```
{
  "errorMessages": [
    {
      "errorMessage": "PUR and RCE effective date ranges must have overlap for proper rating functionality",
      "errorDetails": [
        {
          "relatedObjectAPIName": "ProductUsageRule",
          "records": [
            {
              "id": "a0bxx0000004CqZAAU",
              "name": "PUR-001"
            }
          ]
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorMessage` | String | Human-readable error message that describes the validation failure. | Big, 66.0 | 66.0 |
| `errorDetails` | [Error Warning Details](./connect_responses_error_warning_details_output.htm.md)[] | Details of records that failed with this specific error. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_error_output.htm ===
---
page_id: connect_responses_error_output.htm
title: Error Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Details

Output representation of the top-level error detail when validation fails.

      
        
          

**JSON example**

          
: This example shows a sample error
            response.

```
{
  "errors": [
    {
      "errorCode": "VALIDATION_FAILED",
      "message": "Product validation completed with cross-entity errors",
      "products": [
        {
          "productId": "01txx0000006i2gAAA",
          "validationResult": {
            "validationErrors": [],
            "validationWarnings": []
          }
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Standardized error code. For example, `VALIDATION_FAILED`. | Big, 66.0 | 66.0 |
| `message` | String | Human-readable error message that describes the overall validation failure. | Big, 66.0 | 66.0 |
| `products` | [Product Validation Result](./connect_responses_product_validation_result_output.htm.md)[] | List of product validation results. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_error_warning_details_output.htm ===
---
page_id: connect_responses_error_warning_details_output.htm
title: Error Warning Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_error_warning_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Warning Details

Output representation of the individual warning or error message with associated record details.

      
        
          

**JSON example**

          
: This example shows error details with record
            information.

```
{
  "errorDetails": [
    {
      "relatedObjectAPIName": "ProductUsageRule",
      "records": [
        {
          "id": "a0bxx0000004CqZAAU",
          "name": "PUR-001"
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `relatedObjectAPIName` | String | API name of the related object. | Big, 66.0 | 66.0 |
| `records` | [Record Details](./connect_responses_record_details_output.htm.md)[] | Details of records that triggered the specific warning or error. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_errors_output.htm ===
---
page_id: connect_responses_errors_output.htm
title: Errors
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_errors_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Errors

Output representation of the group of error messages with the same error code.

      
        
          

**JSON example**

          
: This example shows a group of error messages with the same error
            code.

```
{
  "errors": [
    {
      "errorCode": "EFFECTIVITY_MISMATCH",
      "errorMessages": [
        {
          "errorMessage": "PUR and RCE effective date ranges must have overlap for proper rating functionality",
          "errorDetails": []
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Standardized error code. For example, `EFFECTIVITY_MISMATCH`. | Big, 66.0 | 66.0 |
| `errorMessages` | [Error Message](./connect_responses_error_message_output.htm.md)[] | List of error messages for records that failed with this error code. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_fields_output.htm ===
---
page_id: connect_responses_fields_output.htm
title: Fields Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_fields_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Fields Response

Output representation of the details of the optional fields on the usage-based
    selling-related objects.

      
        
          

**JSON Example**

          
: 
            

```
  "fields": {
    "MyCustomDate__c": {
      "displayValue": "2024-09-24",
      "value": "2024-09-24T17:46:30.662Z"
    },
    "MyCustomNumber__c": {
      "displayValue": "20.0",
      "value": 20
    }
  }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `display​Value` | String | Display value of a field. | Big, 63.0 | 63.0 |
| `value` | Object | Value of a field in its original data form. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_generic_error_output.htm ===
---
page_id: connect_responses_generic_error_output.htm
title: Generic Error Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_generic_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Generic Error Details

Output representation of the error details encountered during the API
    request.

      
        
          

**JSON example**

          
: 
            

```
{
  "data": [],
  "error": {
    "errorCode": "INVALID_API_INPUT",
    "message": "Liable summary IDs cannot be null or empty."
  },
  "success": false
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code that represents the type of error. | Big, 67.0 | 67.0 |
| `message` | String | Detailed error message that specifies the cause of failure. | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_lookup_detail_output.htm ===
---
page_id: connect_responses_lookup_detail_output.htm
title: Lookup Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_lookup_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Lookup Detail

Output representation of the details of a usage resource record.

        
          

**JSON example**

          
: This example includes the details of a usage
            resource.

```
{
  "usageResource": {
    "id": "1BRxx0000004C9EGAU"
  }
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the usage resource record. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_negotiated_grant_detail_output.htm ===
---
page_id: connect_responses_negotiated_grant_detail_output.htm
title: Grant Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_negotiated_grant_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Grant Detail

Output representation of the details of a grant from the ProductUsageGrant,
    LineItemUsageResourceGrant, or TransactionUsageEntitlement objects.

      
        
          

**JSON Example**

          
: 
            

```
{
  "negotiatedGrantDetail": {
    "grantType": "Grant",
    "id": "1X6xx00000000OECAY",
    "quantity": 100,
    "usageGrantNegotiable": "Negotiable",
    "usageRefreshPolicy": {
      "displayName": null,
      "id": "1BYxx0000004C92GAE",
      "negotiable": "Non-Negotiable"
    },
    "usageRolloverPolicy": {
      "displayName": null,
      "id": "1BVxx0000004C92GAE",
      "negotiable": "Non-Negotiable"
    },
    "validityPeriodTerm": 12,
    "validityPeriodUnit": "Month"
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `grantType` | String | Details about the grant type. | Big, 65.0 | 65.0 |
| `id` | String | ID of the usage resource grant. | Big, 65.0 | 65.0 |
| `quantity` | Double | Quantity of the negotiated usage resource grant. | Big, 65.0 | 65.0 |
| `usageGrant​Negotiable` | String | Specifies whether the grant is negotiable or not. | Big, 65.0 | 65.0 |
| `usageRefresh​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | ID of the usage grant refresh policy. | Big, 65.0 | 65.0 |
| `usageRollover​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | ID of the usage grant rollover policy. | Big, 65.0 | 65.0 |
| `validity​PeriodTerm` | Double | Validity period term of the grant. | Big, 65.0 | 65.0 |
| `validity​PeriodUnit` | String | Validity period unit of the grant. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_policy_detail_output.htm ===
---
page_id: connect_responses_policy_detail_output.htm
title: Policy Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_policy_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Policy Details

Output representation of the details of a policy.

        
          

**JSON example**

          
: This example includes the details for different policy
            types.

```
{
  "bindingObjectGrantDetail": [
    {
      "effectiveEndDate": "Sat Oct 04 23:59:59 GMT 2025",
      "effectiveStartDate": "Fri Sep 05 00:00:00 GMT 2025",
      "grantType": "Grant",
      "id": "1B0SB0000000Eiv0AE",
      "product": {
        "id": "01tSB000006XMtqYAG"
      },
      "quantity": 100,
      "record": {
        "id": "02iSB000000IoETYA0"
      },
      "unitOfMeasure": {
        "id": "0hESB0000003yfp2AA"
      },
      "usageRefreshPolicy": {
        "id": "1BYSB0000001lOH4AY",
        "negotiable": null
      },
      "usageRolloverPolicy": {
        "id": "1BVSB000000A1xJ4AS",
        "negotiable": null
      },
      "validityPeriodTerm": 1,
      "validityPeriodUnit": "Month"
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the policy. | Big, 65.0 | 65.0 |
| `negotiable` | String | Indicates whether the policy is negotiable. Valid values are: `Negotiable` `Non-Negotiable` | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_product_activation_result_output.htm ===
---
page_id: connect_responses_product_activation_result_output.htm
title: Product Activation Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_activation_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Activation Result

Output representation of the activation outcome for a single product, including any
    errors that occurred while activating the product or its associated usage records.

        
          

**JSON example**

          
: 
            

```
{
  "productId": "01txx0000006i2hAAA",
  "errors": [
    {
      "productUsageResourceId": "0iUxx000000009",
      "usageResourceId": "0hUxx000000003",
      "message": "Usage Resource not found for product",
      "objectApiName": "ProductUsageResource",
      "fieldName": "UsageResourceId",
      "recordId": null,
      "recordName": null
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Usage Activation Error](./connect_responses_usage_activation_error_output.htm.md)[] | List of errors that occurred while activating the product or its associated usage records. | Big, 67.0 | 67.0 |
| `productId` | String | ID of the Product2 record that this activation outcome describes. | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_validation_result_output.htm ===
---
page_id: connect_responses_product_validation_result_output.htm
title: Product Validation Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_validation_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Validation Result

Output representation of the validation result for a specific product.

      
        
          

**JSON example**

          
: This example shows the product validation result.

```
{
  "products": [
    {
      "productId": "01txx0000006i2gAAA",
      "validationResult": {
        "validationErrors": [],
        "validationWarnings": []
      }
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `productId` | String | Unique product ID that's being validated. | Big, 67.0 | 67.0 |
| `validationResult` | [Validation Result](./connect_responses_validation_result_output.htm.md) | Validation results grouped by rule name. | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_rate_adjustments_output.htm ===
---
page_id: connect_responses_rate_adjustments_output.htm
title: Rate Adjustments
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rate_adjustments_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Adjustments

Output representation of the details of a rate adjustment.

        
          

**JSON Example**

          
: 
            

```
      "rateAdjustments": [
        {
           "fields": {},
           "lowerBound": 0.0,
           "name": null,
           "negotiatedRateAdjustmentId": null,
           "rateAdjustmentId": "1ENxx0000004C9BGAU",
           "rateAdjustmentType": "Percentage",
           "rateAdjustmentValue": 10.0,
           "tierUnitOfMeasure": "USD",
           "upperBound": 50.0
        }
    ]
```

          

        
      

If the `negotiable` property value that’s associated with a
        rate card entry is blank, then the data is derived from Product Catalog Management. If it
        isn’t blank, then the data is derived from Rate Management.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `fields` | Map<String, [Fields Response](./connect_responses_fields_output.htm.md)> | List of optional fields and their values that belong to the rate adjustment object. | Big, 63.0 | 63.0 |
| `lowerBound` | Double | Minimum quantity for the adjustment to be applicable. | Small, 63.0 | 63.0 |
| `name` | String | Name of the tier. | Small, 63.0 | 63.0 |
| `negotiatedRate​Adjustment​Id` | String | ID of the negotiated rate adjustment. | Small, 63.0 | 63.0 |
| `rateAdjustment​Id` | String | ID of the rate adjustment. | Small, 63.0 | 63.0 |
| `rateAdjustment​Type` | String | Type of the rate adjustment. | Small, 63.0 | 63.0 |
| `rateAdjustment​Value` | Double | Value of the rate adjustment. | Small, 63.0 | 63.0 |
| `tierUnitOf​Measure` | String | Unit of measure representing the tier. | Small, 63.0 | 63.0 |
| `upperBound` | Double | Maximum quantity for the adjustment to be applicable. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_rate_and_consumption_source_detail_output.htm ===
---
page_id: connect_responses_rate_and_consumption_source_detail_output.htm
title: Rate and Consumption Source Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rate_and_consumption_source_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate and Consumption Source Detail

Output representation of the details of a specific rate and its consumption
    source.

      
        
          

**JSON example**

          
: 
            

```
{
  "rateAndConsumptionSources": [
    {
      "startDate": "2025-01-01",
      "endDate": "2025-01-31",
      "rateUomId": "USD",
      "ratableSummaryId": "URS3",
      "ratingExecutionId": "1RE000000000001",
      "overageQuantity": 333.33,
      "overageAmount ": 333.33,
      "totalConsumption": 1500,
      "netUnitRate": 1,
      "consumptionSources": [
        {
          "consumptionSourceId": "1AE000000000001",
          "consumptionUnit": 500
        },
        {
          "consumptionSourceId": "1CO000000000001",
          "consumptionUnit": 375,
          "commitRate": 1.5,
          "targetRate": 2,
          "cmtAssetRatableSummaryId": "URSCARID1"
        },
        {
          "consumptionSourceId": "1CO000000000002",
          "consumptionUnit": 125,
          "commitRate": 0.75,
          "targetRate": 1,
          "cmtAssetRatableSummaryId": "URSCARID2"
        }
      ]
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `consumptionSource​Details` | [Consumption Source Detail](./connect_responses_consumption_source_detail_output.htm.md)[] | Details on the consumption source. | Big, 66.0 | 66.0 |
| `endDate` | String | End date for the specific rate period. | Big, 66.0 | 66.0 |
| `netUnit​Rate` | Double | Net unit rate. | Big, 66.0 | 66.0 |
| `overageAmt` | Double | Amount for the overage quantity. | Big, 66.0 | 66.0 |
| `overageQty` | Double | Quantity of consumption that was rated as overage. | Big, 66.0 | 66.0 |
| `ratable​SummaryId` | String | Unique ID for the summary used in rating. | Big, 66.0 | 66.0 |
| `ratable​SummaryStatus` | String | Status of ratable summary. | Big, 66.0 | 66.0 |
| `rateUomId` | String | Unit of measure for the rate. | Big, 66.0 | 66.0 |
| `rateUomName` | String | Name of the rate unit of measure | Big, 66.0 | 66.0 |
| `ratingExecution​Id` | String | Execution ID of the rating. | Big, 66.0 | 66.0 |
| `sourceUsage​ResourceId` | String | ID of the source usage resource. | Big, 66.0 | 66.0 |
| `sourceUsage​ResourceName` | String | Name of the source usage resource. | Big, 66.0 | 66.0 |
| `startDate` | String | Start date for the specific rate period. | Big, 66.0 | 66.0 |
| `total​Consumption` | Double | Total quantity consumed for this rate. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_rate_card_entry_output.htm ===
---
page_id: connect_responses_rate_card_entry_output.htm
title: Rate Card Entry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rate_card_entry_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Card Entry

Output representation of the details of a rate card entry.

    
      
        
          

**JSON Example**

          
: 
            

```
{
  "records": [
    {
      "bindingInstanceTargetType": "Product",
      "bindingInstanceType": "Target",
      "chargeForOverages": "Yes",
      "fields": {},
      "isOptional": false,
      "name": "Paddle Board",
      "negotiable": "Negotiable,Non-Negotiable",
      "negotiatedRate": 20,
      "negotiatedRateCardEntryId": "1ELxx0000004C9JGAU,1ELxx0000004C9KGAU",
      "quantity": 15,
      "rate": 5,
      "rateAdjustments": [
        {
          "fields": {},
          "lowerBound": 0,
          "name": "Tier 1",
          "negotiatedRateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentType": "Percentage",
          "rateAdjustmentValue": 10,
          "tierUnitOfMeasure": "USD",
          "upperBound": 50
        }
      ],
      "rateCardEntryId": "1CJxx0000004C9IGAU,1CJxx0000004C9JGAU",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": "GB",
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

          

        
      

    

If the `negotiable` property value is blank, then the
        data is derived from Product Catalog Management. If it isn’t blank, then the data is derived
        from Rate Management.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `binding​Instance​TargetType` | String | Type of the target object that's associated with this transaction. | Big, 63.0 | 63.0 |
| `bindingInstance​Type` | String | Type of the binding instance. Valid values are: `Self` `Target` | Big, 63.0 | 63.0 |
| `chargeFor​Overages` | String | Specifies whether overage is permitted. Valid values are: `Yes` `No` `NA` | Big, 63.0 | 63.0 |
| `fields` | Map<String, [Fields Response](./connect_responses_fields_output.htm.md)> | List of optional fields and their values that's associated with the rate card entry object. | Big, 63.0 | 63.0 |
| `isOptional` | Boolean | Indicates whether the product usage resource is optional when the associated product is one of the commitment usage model types (`true`) or not (`false`). | Big, 65.0 | 65.0 |
| `name` | String | Name of the resource. | Big, 63.0 | 63.0 |
| `negotiable` | String | Type of the base rate and the tier rate, if applicable. Valid values are: `Negotiable` `Non-Negotiable` | Big, 63.0 | 63.0 |
| `negotiated​Rate` | Double | User-overridden overage rate. | Big, 63.0 | 63.0 |
| `negotiated​RateCard​EntryId` | String | ID of the negotiated rate card entry and the tier rate card entry, if applicable. | Big, 63.0 | 63.0 |
| `quantity` | Double | Amount granted for the resource. | Big, 63.0 | 63.0 |
| `rate` | Double | Base overage rate. | Big, 63.0 | 63.0 |
| `rate​Adjustments` | [Rate Adjustments](./connect_responses_rate_adjustments_output.htm.md)[] | List of tiers associated with the rate card entry, if applicable. | Big, 63.0 | 63.0 |
| `rateCard​EntryId` | String | ID of the base rate card entry and the tier rate card entry, if applicable. | Big, 63.0 | 63.0 |
| `rateUnit​OfMeasure​Name` | String | Unit of measure for rates in the rate card entry. | Big, 64.0 | 64.0 |
| `unitOf​Measure` | String | Unit of measure of the grant. For example, `Unit`. | Big, 63.0 | 63.0 |
| `usageResource​Id` | String | ID of the usage resource. | Big, 65.0 | 65.0 |
| `usageResource​GrantAndPolicy​Detail` | [Usage Resource Grant And Policy Detail](./connect_responses_usage_resource_grant_and_policy_detail_output.htm.md) | Details of a usage resource grant and policy. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_record_details_output.htm ===
---
page_id: connect_responses_record_details_output.htm
title: Record Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_record_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Record Details

Output representation of the record details including ID and name.

      
        
          

**JSON example**

          
: This example shows the record details with ID and name.

```
{
  "records": [
    {
      "id": "a0bxx0000004CqZAAU",
      "name": "PUR-001"
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | Unique identifier of the object. | Big, 66.0 | 66.0 |
| `name` | String | Display name of the object. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_resource_detail_output.htm ===
---
page_id: connect_responses_resource_detail_output.htm
title: Resource Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_resource_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resource Detail

Output representation of the details of a specific usage resource.

      
        
          

**JSON example**

          
: 
            

```
{
  "resources": [
    {
      "liableSummaryId": "1HG000000000001",
      "usageResourceId": "1BX000000000004",
      "usageResourceName": "SF Credits",
      "usageResourceUomId": "1UM000000000001",
      "usageResourceUomUnitCode": "CREDIT",
      "resourceTotalOverageQuantity": 333.33,
      "resourceTotalOverageAmount": 333.33,
      "resourceTotalConsumption": 1500,
      "rateAndConsumptionSources": [
        {
          "startDate": "2025-01-01",
          "endDate": "2025-01-31",
          "rateUomId": "USD",
          "ratableSummaryId": "URS3",
          "ratingExecutionId": "1RE000000000001",
          "overageQuantity": 333.33,
          "overageAmount ": 333.33,
          "totalConsumption": 1500,
          "netUnitRate": 1,
          "consumptionSources": [
            {
              "consumptionSourceId": "1AE000000000001",
              "consumptionUnit": 500
            },
            {
              "consumptionSourceId": "1CO000000000001",
              "consumptionUnit": 375,
              "commitRate": 1.5,
              "targetRate": 2,
              "cmtAssetRatableSummaryId": "URSCARID1"
            },
            {
              "consumptionSourceId": "1CO000000000002",
              "consumptionUnit": 125,
              "commitRate": 0.75,
              "targetRate": 1,
              "cmtAssetRatableSummaryId": "URSCARID2"
            }
          ]
        }
      ]
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `liableSummaryId` | String | Unique identifier for the consumption summary. | Big, 66.0 | 66.0 |
| `liableSummary​Status` | String | Status of liable summary. | Big, 66.0 | 66.0 |
| `rateAnd​Consumption​Sources` | [Rate And Consumption Source Detail](./connect_responses_rate_and_consumption_source_detail_output.htm.md)[] | Details on rates and consumption sources. | Big, 66.0 | 66.0 |
| `resourceTotal​Consumption` | Double | Total quantity of consumption for the resource. | Big, 66.0 | 66.0 |
| `resourceTotal​OverageAmount` | Double | Total amount for the overage. | Big, 66.0 | 66.0 |
| `resourceTotal​OverageQuantity` | Double | Total overage quantity. | Big, 66.0 | 66.0 |
| `usageResource​Id` | String | ID of the specific usage resource. | Big, 66.0 | 66.0 |
| `usageResource​Name` | String | Name of the usage resource. | Big, 66.0 | 66.0 |
| `usageResource​UomId` | String | Unit of measure ID for the usage resource. | Big, 66.0 | 66.0 |
| `usageResource​UomUnitCode` | String | Unit of measure code for the usage resource. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_resource_policy_detail_output.htm ===
---
page_id: connect_responses_resource_policy_detail_output.htm
title: Resource Policy Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_resource_policy_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resource Policy Detail

Output representation of the details of a usage resource policy.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the usage resource policy. | Big, 65.0 | 65.0 |
| `ratingFrequency​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the rating frequency policy. | Big, 65.0 | 65.0 |
| `usageAggregation​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the usage aggregation policy. | Big, 65.0 | 65.0 |
| `usageCommitment​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the usage commitment policy. | Big, 65.0 | 65.0 |
| `usageOverage​Policy` | [Policy Detail](./connect_responses_policy_detail_output.htm.md) | Details of the usage overage policy. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_usage_activation_error_output.htm ===
---
page_id: connect_responses_usage_activation_error_output.htm
title: Usage Activation Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_activation_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Activation Error

Output representation of a single error encountered while activating a usage product or one of its related records.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "productUsageResourceId": "0iUxx0000000678",
  "usageResourceId": "0hUxx000000004",
  "message": "Related Unit of measure records is inactive, activate it first.",
  "objectApiName": "ProductUsageGrant",
  "fieldName": "DefaultUnitofMeasure",
  "recordId": "1BXSM000000404f4AA",
  "recordName": "PUG-000000001"
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `fieldName` | String | API name of the field that caused the error. | Big, 67.0 | 67.0 |
| `message` | String | Human-readable description of the error. | Big, 67.0 | 67.0 |
| `object​ApiName` | String | API name of the object on which the error occurred. | Big, 67.0 | 67.0 |
| `productUsage​ResourceId` | String | ID of the ProductUsageResource record that links the product and the usage resource for which the error occurred. | Big, 67.0 | 67.0 |
| `recordId` | String | ID of the record that failed activation. | Big, 67.0 | 67.0 |
| `recordName` | String | Name of the record that failed activation. | Big, 67.0 | 67.0 |
| `usage​ResourceId` | String | ID of the usage resource record from the input request for which the error occurred. | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_usage_activation_output.htm ===
---
page_id: connect_responses_usage_activation_output.htm
title: Usage Product Activation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_activation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Activation

Output representation of a usage product activation response.

        
          

**JSON example**

          
: 
            

```
{
  "success": true,
  "errors": null,
  "activatedProducts": [
    "01txx0000006i2hAAB"
  ],
  "activationResults": {
    "productActivationResults": [
      {
        "productId": "01txx0000006i2hAAA",
        "errors": [
          {
            "productUsageResourceId": "0iUxx000000009",
            "usageResourceId": "0hUxx000000003",
            "message": "Usage Resource not found for product",
            "objectApiName": "ProductUsageResource",
            "fieldName": "UsageResourceId",
            "recordId": null,
            "recordName": null
          },
          {
            "productUsageResourceId": "0iUxx0000000678",
            "usageResourceId": "0hUxx000000004",
            "message": "Related Unit of measure records is inactive, activate it first.",
            "objectApiName": "ProductUsageGrant",
            "fieldName": "DefaultUnitofMeasure",
            "recordId": "1BXSM000000404f4AA",
            "recordName": "PUG-000000001"
          }
        ]
      }
    ],
    "productValidationResults": [
      {
        "productId": "01txx0000006i2gAAA",
        "validationResult": {
          "validationErrors": [
            {
              "ruleName": "Usage vs Rating Effectivity",
              "errors": [
                {
                  "errorCode": "EFFECTIVITY_MISMATCH",
                  "errorMessages": [
                    {
                      "errorMessage": "PUR and RCE effective date ranges must overlap for proper rating functionality.",
                      "errorDetails": [
                        {
                          "relatedObjectAPIName": "ProductUsageResource",
                          "records": [
                            {
                              "id": "0Wnxx0000004CDEAA2",
                              "name": "API Calls PUR"
                            }
                          ]
                        },
                        {
                          "relatedObjectAPIName": "RateCardEntry",
                          "records": [
                            {
                              "id": "0Rcxx0000004FGHAA2",
                              "name": "API Calls Rate Entry"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "validationWarnings": []
        }
      }
    ]
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `activated​Products` | String[] | ID of the product whose associated usage records were activated. The array contains at most one entry. | Big, 67.0 | 67.0 |
| `activation​Results` | [Usage Activation Result](./connect_responses_usage_activation_result_output.htm.md) | Activation and validation outcome for the product in the request. | Big, 67.0 | 67.0 |
| `errors` | [Generic Error](./connect_responses_generic_error_output.htm.md)[] | List of top-level API errors. For example, a guardrail violation or an invalid request. | Big, 67.0 | 67.0 |
| `success` | Boolean | Indicates whether the API request was processed (`true`) or rejected at the top level (`false`). | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_usage_activation_result_output.htm ===
---
page_id: connect_responses_usage_activation_result_output.htm
title: Usage Activation Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_activation_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Activation Result

Output representation that groups the activation outcome and the validation outcome
    for the product in a usage product activation request.

        
          

**JSON example**

          
: 
            

```
{
  "productActivationResults": [
    {
      "productId": "01txx0000006i2hAAA",
      "errors": []
    }
  ],
  "productValidationResults": [
    {
      "productId": "01txx0000006i2gAAA",
      "validationResult": {
        "validationErrors": [],
        "validationWarnings": []
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `product​ActivationResults` | [Product Activation Result](./connect_responses_product_activation_result_output.htm.md)[] | List of product activation results. | Big, 67.0 | 67.0 |
| `product​ValidationResults` | [Product Validation Result](./connect_responses_product_validation_result_output.htm.md)[] | List of product validation results. | Big, 67.0 | 67.0 |

=== ARTICLE: connect_responses_usage_detail_binding_object_output.htm ===
---
page_id: connect_responses_usage_detail_binding_object_output.htm
title: Binding Object Usage Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_detail_binding_object_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Binding Object Usage Detail 

Output representation of the usage details of a binding object.

        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "records": [
    {
      "bindingObjectRate": {
        "id": "1QNSB0000001JyH4AU,1QNSB0000001JyI4AU",
        "negotiatedRate": null,
        "negotiatedRateAdjustments": [
          {
            "lowerBound": 101,
            "name": null,
            "rateAdjustmentId": "1DMSB000001N3C74AK",
            "rateAdjustmentType": "Amount",
            "rateAdjustmentValue": 10,
            "tierUnitOfMeasure": "USD",
            "upperBound": null
          },
          {
            "lowerBound": 1,
            "name": null,
            "rateAdjustmentId": "1DMSB000001N3C64AK",
            "rateAdjustmentType": "Percentage",
            "rateAdjustmentValue": 30,
            "tierUnitOfMeasure": "USD",
            "upperBound": 100
          }
        ],
        "rate": 100,
        "rateCardEntryId": "1CJSB000000207R4AQ,1CJSB000000207S4AQ",
        "rateUnitOfMeasureName": "USD"
      },
      "bindingObjectResourceGrantAndPolicyDetail": {
        "bindingObjectGrantDetail": [
          {
            "effectiveEndDate": "Sat Oct 04 23:59:59 GMT 2025",
            "effectiveStartDate": "Fri Sep 05 00:00:00 GMT 2025",
            "grantType": "Grant",
            "id": "1B0SB0000000Eiv0AE",
            "product": {
              "id": "01tSB000006XMtqYAG"
            },
            "quantity": 100,
            "record": {
              "id": "02iSB000000IoETYA0"
            },
            "unitOfMeasure": {
              "id": "0hESB0000003yfp2AA"
            },
            "usageRefreshPolicy": {
              "id": "1BYSB0000001lOH4AY",
              "negotiable": null
            },
            "usageRolloverPolicy": {
              "id": "1BVSB000000A1xJ4AS",
              "negotiable": null
            },
            "validityPeriodTerm": 1,
            "validityPeriodUnit": "Month"
          }
        ],
        "bindingObjectResourcePolicyDetail": {
          "drawdownOrder": "ExpiringFirst",
          "id": "1X2SB00000002WT0AY",
          "ratingFrequencyPolicy": {
            "id": "1HJSB0000000G3B4AU",
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": "1cfSB0000001xHPYAY",
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageOveragePolicy": {
            "id": "7UkSB00000002OP0AY",
            "negotiable": null
          }
        }
      },
      "usageResource": {
        "id": "1BRSB0000001x4h4AA"
      }
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Usage Detail Error Response](./connect_responses_usage_detail_error_response.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 65.0 | 65.0 |
| `records` | [Binding Object Detail](./connect_responses_binding_object_detail_output.htm.md)[] | List of records that contains the binding target details. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_usage_detail_error_response.htm ===
---
page_id: connect_responses_usage_detail_error_response.htm
title: Usage Details Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_detail_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Details Error Response

Output representation of the details of an error related to usage details.

      
        
          

**JSON Example**

          
: 
            

```
{
   "errors": [
        {
            "referenceId": "MyOrderItem",
            "errorCode": "INVALID_API_INPUT",
            "message": "Something has failed"
        }
   ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code associated with the error. | Small, 63.0 | 63.0 |
| `message` | String | Message associated with the error. | Small, 63.0 | 63.0 |
| `referenceId` | String | Unique ID that’s associated with the specific error for tracking and reference purposes. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_usage_detail_output.htm ===
---
page_id: connect_responses_usage_detail_output.htm
title: Usage Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Details

Output representation of the usage details of a quote, an order, or an asset.

      
        
          

**JSON example**

          
: This sample response shows resources that include grants, if applicable, and resources
            without rates when you retrieve the usage details of an order
            item.

```
{
  "records": [
    {
      "bindingInstanceTargetType": null,
      "bindingInstanceType": null,
      "chargeForOverages": "Yes",
      "isOptional": false,
      "fields": {},
      "name": "API Calls",
      "negotiable": ",",
      "negotiatedRate": null,
      "negotiatedRateCardEntryId": ",",
      "quantity": 1000,
      "rate": null,
      "rateAdjustments": [],
      "rateCardEntryId": ",",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": null,
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

          
: This example shows a sample response without negotiated rates when you retrieve the
            usage details of an order item.

```
{
  "records": [
    {
      "bindingInstanceTargetType": "Product",
      "bindingInstanceType": "Target",
      "chargeForOverages": "Yes",
      "isOptional": false,
      "fields": {},
      "name": "Paddle Board",
      "negotiable": "Negotiable,Non-Negotiable",
      "negotiatedRate": null,
      "negotiatedRateCardEntryId": ",",
      "quantity": 15,
      "rate": 5,
      "rateAdjustments": [
        {
          "fields": {},
          "lowerBound": 0,
          "name": null,
          "negotiatedRateAdjustmentId": null,
          "rateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentType": "Percentage",
          "rateAdjustmentValue": 10,
          "tierUnitOfMeasure": "USD",
          "upperBound": 50
        }
      ],
      "rateCardEntryId": "1CJxx0000004C9IGAU,1CJxx0000004C9JGAU",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": "GB",
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

          
: This sample response shows negotiated rates when you retrieve the usage details of an
            order item. The negotiated rates are derived from these objects for assets, order items,
            or quote line items. 
              
- AssetRateCardEntry

              
- AssetRateAdjustment

              
- OrderItemRateCardEntry

              
- OrderItemRateAdjustment

              
- QuoteLineRateCardEntry

              
- QuoteLineRateAdjustment

            

```
{
  "records": [
    {
      "bindingInstanceTargetType": "Product",
      "bindingInstanceType": "Target",
      "chargeForOverages": "Yes",
      "isOptional": false,
      "fields": {},
      "name": "Paddle Board",
      "negotiable": "Negotiable,Non-Negotiable",
      "negotiatedRate": 20,
      "negotiatedRateCardEntryId": "1ELxx0000004C9JGAU,1ELxx0000004C9KGAU",
      "quantity": 15,
      "rate": 5,
      "rateAdjustments": [
        {
          "fields": {},
          "lowerBound": 0,
          "name": "Tier 1",
          "negotiatedRateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentType": "Percentage",
          "rateAdjustmentValue": 10,
          "tierUnitOfMeasure": "USD",
          "upperBound": 50
        }
      ],
      "rateCardEntryId": "1CJxx0000004C9IGAU,1CJxx0000004C9JGAU",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": "GB",
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

          
: This sample response shows details of the custom fields when you retrieve the usage
            details of an order item.

```
{
  "records": [
    {
      "fields": {
        "MyCustomDate__c": {
          "displayValue": "2024-09-24",
          "value": "2024-09-24T17:46:30.662Z"
        },
        "MyCustomNumber__c": {
          "displayValue": "20.0",
          "value": 20
        }
      },
      "isOptional": false,
      "bindingInstanceTargetType": "Product",
      "bindingInstanceType": "Target",
      "chargeForOverages": "Yes",
      "name": "Therapy",
      "negotiable": "Negotiable,Non-Negotiable",
      "negotiatedRate": 20,
      "negotiatedRateCardEntryId": "1ELxx0000004C9JGAU,1ELxx0000004C9KGAU",
      "quantity": 15,
      "rate": 5,
      "rateAdjustments": [
        {
          "fields": {
            "MyCustomString__c": {
              "displayValue": "My Custom String",
              "value": "MyCustomString"
            }
          },
          "lowerBound": 0,
          "name": "Tier 1",
          "negotiatedRateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentId": "1ENxx0000004C9BGAU",
          "rateAdjustmentType": "Percentage",
          "rateAdjustmentValue": 10,
          "tierUnitOfMeasure": "USD",
          "upperBound": 50
        }
      ],
      "rateCardEntryId": "1CJxx0000004C9IGAU,1CJxx0000004C9JGAU",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": "GB",
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

                    
: This sample response shows values for the type and target type of a binding
            instance if the `BindingInstanceTargetId` value is
            available in the QuoteLineItem, OrderItem, and AssetStatePeriod objects. Additionally,
            the rate, negotiated rates, and rate card entry values show the associated details of
            the binding object.

```
{
  "records": [
    {
      "bindingInstanceTargetType": "Account",
      "bindingInstanceType": "Target",
      "chargeForOverages": "Yes",
      "fields": {},
      "isOptional": false,
      "name": "Data Transfers",
      "negotiable": "Non-Negotiable,Non-Negotiable",
      "negotiatedRate": null,
      "negotiatedRateCardEntryId": "1QNxx0000004CQmGAM,1QNxx0000004CLwGAM",
      "quantity": 250,
      "rate": 0.098765,
      "rateAdjustments": [
        {
          "fields": {},
          "lowerBound": 0,
          "name": null,
          "negotiatedRateAdjustmentId": null,
          "rateAdjustmentId": "1Soxx0000004CAeCAM",
          "rateAdjustmentType": "Percentage",
          "rateAdjustmentValue": 0,
          "tierUnitOfMeasure": "USD",
          "upperBound": 121
        }
      ],
      "rateCardEntryId": "1CJxx0000004C9CGAU,1CJxx0000004C9GGAU",
      "rateUnitOfMeasureName": "USD",
      "unitOfMeasure": "GB",
      "usageResourceGrantAndPolicyDetail": {
        "grantDetail": {
          "grantType": "Grant",
          "id": "1BXxx0000004C9lGAE",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedGrantDetail": {
          "grantType": "Grant",
          "id": "1X6xx00000000OECAY",
          "quantity": 100,
          "usageGrantNegotiable": "Negotiable",
          "usageRefreshPolicy": {
            "id": "1BYxx0000004C92GAE",
            "negotiable": "Non-Negotiable"
          },
          "usageRolloverPolicy": {
            "id": "1BVxx0000004C93GAE",
            "negotiable": "Non-Negotiable"
          },
          "validityPeriodTerm": 1,
          "validityPeriodUnit": "Month"
        },
        "negotiatedResourcePolicyDetail": {
          "id": "1X5xx00000000OECAY",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        },
        "resourcePolicyDetail": {
          "id": "7Suxx0000004C9kCAE",
          "ratingFrequencyPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageAggregationPolicy": {
            "id": null,
            "negotiable": null
          },
          "usageCommitmentPolicy": {
            "id": "7Pexx0000004C92CAE",
            "negotiable": "Non-Negotiable"
          },
          "usageOveragePolicy": {
            "id": null,
            "negotiable": null
          }
        }
      },
      "usageResourceId": "1BRxx0000004C9CGAU"
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Usage Detail Error Response](./connect_responses_usage_detail_error_response.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 63.0 | 63.0 |
| `records` | [Rate Card Entry](./connect_responses_rate_card_entry_output.htm.md)[] | List of rate card entry records. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_usage_product_validation_output.htm ===
---
page_id: connect_responses_usage_product_validation_output.htm
title: Usage Product Validation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_product_validation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Product Validation

Output representation of all the performed validations.

      
        
          

**JSON example**

          
: This example shows the validation output with errors and
            warnings.

```
{
  "errors": [
    {
      "errorCode": "VALIDATION_FAILED",
      "message": "Product validation completed with cross-entity errors",
      "products": [
        {
          "productId": "01txx0000006i2gAAA",
          "validationResult": {
            "validationErrors": [
              {
                "errors": [
                  {
                    "errorCode": "EFFECTIVITY_MISMATCH",
                    "errorMessages": [
                      {
                        "errorMessage": "PUR and RCE effective date ranges must have overlap for proper rating functionality",
                        "errorDetails": [
                          {
                            "relatedObjectAPIName": "ProductUsageRule",
                            "records": [
                              {
                                "id": "a0bxx0000004CqZAAU",
                                "name": "PUR-001"
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ],
                "ruleName": "Usage vs Rating Effectivity"
              }
            ],
            "validationWarnings": []
          }
        }
      ]
    }
  ],
  "success": false
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `success` | Boolean | Indicates whether the product validation passed (`true`) or failed (`false`). | Big, 66.0 | 66.0 |
| `errors` | [Error Details](./connect_responses_error_output.htm.md)[] | List of top-level error details when validation fails. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_usage_resource_grant_and_policy_detail_output.htm ===
---
page_id: connect_responses_usage_resource_grant_and_policy_detail_output.htm
title: Usage Resource Grant And Policy Detail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_usage_resource_grant_and_policy_detail_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Resource Grant And Policy Detail

Output representation of the details of a usage resource grant and policy.

      
        
          

**JSON Example**

          
: 
            

```
{
  "usageResourceGrantAndPolicyDetail": {
    "grantDetail": {
      "grantType": "Grant",
      "id": "1BXxx0000004C9lGAE",
      "quantity": 100,
      "usageGrantNegotiable": "Negotiable",
      "usageRefreshPolicy": {
        "id": "1BYxx0000004C92GAE",
        "negotiable": "Non-Negotiable"
      },
      "usageRolloverPolicy": {
        "id": "1BVxx0000004C93GAE",
        "negotiable": "Non-Negotiable"
      },
      "validityPeriodTerm": 1,
      "validityPeriodUnit": "Month"
    },
    "negotiatedGrantDetail": {
      "grantType": "Grant",
      "id": "1X6xx00000000OECAY",
      "quantity": 100,
      "usageGrantNegotiable": "Negotiable",
      "usageRefreshPolicy": {
        "id": "1BYxx0000004C92GAE",
        "negotiable": "Non-Negotiable"
      },
      "usageRolloverPolicy": {
        "id": "1BVxx0000004C93GAE",
        "negotiable": "Non-Negotiable"
      },
      "validityPeriodTerm": 1,
      "validityPeriodUnit": "Month"
    },
    "negotiatedResourcePolicyDetail": {
      "id": "1X5xx00000000OECAY",
      "ratingFrequencyPolicy": {
        "id": null,
        "negotiable": null
      },
      "usageAggregationPolicy": {
        "id": null,
        "negotiable": null
      },
      "usageCommitmentPolicy": {
        "id": "7Pexx0000004C92CAE",
        "negotiable": "Non-Negotiable"
      },
      "usageOveragePolicy": {
        "id": null,
        "negotiable": null
      }
    },
    "resourcePolicyDetail": {
      "id": "7Suxx0000004C9kCAE",
      "ratingFrequencyPolicy": {
        "id": null,
        "negotiable": null
      },
      "usageAggregationPolicy": {
        "id": null,
        "negotiable": null
      },
      "usageCommitmentPolicy": {
        "id": "7Pexx0000004C92CAE",
        "negotiable": "Non-Negotiable"
      },
      "usageOveragePolicy": {
        "id": null,
        "negotiable": null
      }
    }
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `grant​Detail` | [Grant Detail](./connect_responses_negotiated_grant_detail_output.htm.md) | Details about the grants from the ProductUsageGrant object. | Big, 65.0 | 65.0 |
| `negotiated​Grant​Detail` | [Grant Detail](./connect_responses_negotiated_grant_detail_output.htm.md) | Details about the negotiated grants from the LineItemUsageResourceGrant or TransactionUsageEntitlement object. | Big, 65.0 | 65.0 |
| `negotiated​Resource​PolicyDetail` | [Resource Policy Detail](./connect_responses_resource_policy_detail_output.htm.md) | Details about the policy from the LineItemUsageResourcePolicy or BindingObjectUsageResourcePolicy object. | Big, 65.0 | 65.0 |
| `resourcePolicy​Detail` | [Resource Policy Detail](./connect_responses_resource_policy_detail_output.htm.md) | Details about the policy from the ProductUsageResourcePolicy object. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_validation_error_output.htm ===
---
page_id: connect_responses_validation_error_output.htm
title: Validation Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_validation_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Validation Error

Output representation of the validation errors grouped by rule name.

      
        
          

**JSON example**

          
: This example shows a validation error grouped by rule
            name.

```
{
  "validationErrors": [
    {
      "ruleName": "Usage vs Rating Effectivity",
      "errors": [
        {
          "errorCode": "EFFECTIVITY_MISMATCH",
          "errorMessages": []
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `ruleName` | String | Name of the validation rule. For example, `Usage vs Rating Effectivity`. | Big, 66.0 | 66.0 |
| `errors` | [Errors](./connect_responses_errors_output.htm.md)[] | List of error code groups for this validation. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_validation_result_output.htm ===
---
page_id: connect_responses_validation_result_output.htm
title: Validation Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_validation_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Validation Result

Output representation of the validation results grouped by rule name.

      
        
          

**JSON example**

          
: This example shows a validation result with errors and
            warnings.

```
{
  "validationResult": {
    "validationErrors": [
      {
        "ruleName": "Usage vs Rating Effectivity",
        "errors": []
      }
    ],
    "validationWarnings": [
      {
        "ruleName": "Performance Optimization",
        "warnings": []
      }
    ]
  }
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `validationErrors` | [Validation Error](./connect_responses_validation_error_output.htm.md)[] | List of validation errors grouped by rule name. | Big, 66.0 | 66.0 |
| `validationWarnings` | [Validation Warning](./connect_responses_validation_warning_output.htm.md)[] | List of validation warnings grouped by rule name. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_validation_warning_output.htm ===
---
page_id: connect_responses_validation_warning_output.htm
title: Validation Warning
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_validation_warning_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Validation Warning

Output representation of the validation warnings grouped by rule name.

      
        
          

**JSON example**

          
: This example shows a validation warning grouped by rule
            name.

```
{
  "validationWarnings": [
    {
      "ruleName": "Performance Optimization",
      "warnings": [
        {
          "warningCode": "PERFORMANCE_SUBOPTIMAL",
          "warningMessages": []
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `ruleName` | String | Name of the validation rule. For example, `Performance Optimization`. | Big, 66.0 | 66.0 |
| `warnings` | [Warnings](./connect_responses_warnings_output.htm.md)[] | List of warning code groups for this validation. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_warning_message_output.htm ===
---
page_id: connect_responses_warning_message_output.htm
title: Warning Message
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_warning_message_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Warning Message

Output representation of the details of records that triggered this specific
    warning.

      
        
          

**JSON example**

          
: This example shows a warning message with
            details.

```
{
  "warningMessages": [
    {
      "warningMessage": "PUR and RCE date ranges could be optimized for better performance",
      "warningDetails": [
        {
          "relatedObjectAPIName": "ProductUsageRule",
          "records": [
            {
              "id": "a0bxx0000004CqZAAU",
              "name": "PUR-001"
            }
          ]
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `warningMessage` | String | Human-readable warning message that describes the validation concern. | Big, 66.0 | 66.0 |
| `warningDetails` | [Error Warning Details](./connect_responses_error_warning_details_output.htm.md)[] | Details of records that triggered this specific warning. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_warnings_output.htm ===
---
page_id: connect_responses_warnings_output.htm
title: Warnings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_warnings_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Warnings

Output representation of a group of warning messages with the same warning
    code.

      
        
          

**JSON example**

          
: This example shows a group of warning messages with the same warning
            code.

```
{
  "warnings": [
    {
      "warningCode": "PERFORMANCE_SUBOPTIMAL",
      "warningMessages": [
        {
          "warningMessage": "PUR and RCE date ranges could be optimized for better performance",
          "warningDetails": []
        }
      ]
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `warningCode` | String | Standardized warning code. For example, `PERFORMANCE_SUBOPTIMA`L. | Big, 66.0 | 66.0 |
| `warningMessages` | [Warning Message](./connect_responses_warning_message_output.htm.md)[] | List of warning messages for records that triggered with this warning. | Big, 66.0 | 66.0 |

=== ARTICLE: meta_industriesusagesettings.htm ===
---
page_id: meta_industriesusagesettings.htm
title: IndustriesUsageSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_industriesusagesettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# IndustriesUsageSettings

Represents the settings for Usage Management.
	

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

IndustriesUsageSettings values are stored in the
					IndustriesUsage.settings file in the
					settings folder. The .settings files
				are different from other named components, because there is only one settings file
				for each settings component.

	

	

## Version

		
		

IndustriesUsageSettings components are available in API version 63.0 and later.

	

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| enableUsage | **Field Type** boolean **Description** Indicates whether to create and access Usage Management objects to manage product usage and determine rates based on usage (`true`) or not (`false`). The default value is `false`. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of an IndustriesUsageSettings component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<IndustriesUsageSettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <enableUsage>true</enableUsage>
</IndustriesUsageSettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>IndustriesUsage</members>
        <name>Settings</name>
    </types>
    <version>[ftest]</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

The wildcard character `*` (asterisk) in the
					package.xml manifest file doesn’t apply to metadata types
				for feature settings. The wildcard applies only when retrieving all settings, not
				for an individual setting. For details, see [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm). For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: sforce_api_objects_productusagegrant.htm ===
---
page_id: sforce_api_objects_productusagegrant.htm
title: ProductUsageGrant
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productusagegrant.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductUsageGrant

      Represents the details of a grant associated with a resource, product, or
         service, such as the purchased quantity, renewal and rollover policy, and validity of the
         grant. This object is available in API version 62.0 and later.

      

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

To create, update, and delete product usage
            grant records, you must have the Usage Management Design Time permission set
            license.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| DrawdownOrder | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The order that's used to debit entitlement consumption from the usage entitlement bucket. Valid values are: `ExpiringFirst` `GrantedFirst` `GrantedLast` This field is deprecated and will be retired in a future version. |
| EffectiveEndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time until when the grant remains effective. |
| EffectiveStartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the grant becomes effective. |
| Label | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The identifying label for the product usage grant. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| OverageChargeable | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to charge for overages. Valid values are: `No` `Yes` This field is deprecated and will be retired in a future version. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product usage grant. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ProductOfferId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The sellable product that grants the usage resource. This field is a relationship field. This field is deprecated and will be retired in a future version. **Relationship Name** ProductOffer **Refers To** Product2 |
| ProductSellingModelId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product selling model associated with the product usage grant. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| ProductUsageGrantNum | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The number of each resource grant map that starts with one and is consecutive. |
| ProductUsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The product usage resource associated with the product usage grant. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** ProductUsageResource **Refers To** ProductUsageResource |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The quantity of the granted resource. |
| RenewalPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The grant renewal policy associated with the product usage grant. This field is a relationship field. **Relationship Name** RenewalPolicy **Refers To** UsageGrantRenewalPolicy |
| RolloverPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The grant rollover policy associated with the product usage grant. This field is a relationship field. **Relationship Name** RolloverPolicy **Refers To** UsageGrantRolloverPolicy |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the product usage grant. Valid values are: `Active` `Draft` `Inactive` |
| Type | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of model that defines how the usage resource is consumed. Valid values are: `Commit` `Grant` The default value is `Grant`. Available in API version 64.0 and later. |
| UnitOfMeasureClassId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure class associated with the product usage grant. This field is a relationship field. **Relationship Name** UnitOfMeasureClass **Refers To** UnitOfMeasureClass |
| UnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unit for measure associated with the product usage grant. This value when specified, overrides the default unit of measure defined in the associated unit of measure class. This field is a relationship field. **Relationship Name** UnitOfMeasure **Refers To** UnitOfMeasure |
| UsageDefinitionProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The sellable product associated with the usage resource that's used to retrieve tax policy, calculate rating during overages, and other invoicing actions. This field is a relationship field. **Relationship Name** UsageDefinitionProduct **Refers To** Product2 |
| UsageModelType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The ID of the unit of measure associated with the product. The type of usage model for a product or service. `Anchor` is the main subscription product or service. `Pack` is the add-on product or service that grants additional usage resources for consumption. `Commit` is the product or service with a specific committed quantity of consumption. Valid values are: `Anchor` `Pack` `Token Commitment` `Quantity Commitment` `Monetary Commitment` This field is available in API version 65.0 and later. |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the product usage grant. This field is a relationship field. This field is deprecated and will be retired in a future version. **Relationship Name** UsageResource **Refers To** UsageResource |
| ValidityPeriodTerm | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The period until when the resource grant is valid. |
| ValidityPeriodUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The length of a validity period for the resource grant, when used with the ValidityPeriodTerm field. Valid values are: `Month` `None` `Year` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[ProductUsageGrantHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[ProductUsageGrantOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[ProductUsageGrantShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productusageresource.htm ===
---
page_id: sforce_api_objects_productusageresource.htm
title: ProductUsageResource
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productusageresource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductUsageResource

Represents the mapping of a product and its usage resources.
      This object is available in API version 64.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| EffectiveEndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the relationship between the product and the usage resource stops being active, and any usage tracking or billing related to this relationship ends. |
| EffectiveStartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the relationship between the product and the usage resource becomes active or effective, and any usage tracking or billing related to this relationship begins. |
| IsOptional | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the product usage resource is optional when the associated product is one of the commitment usage model types (`true`) or not (`false`). The default value is `false`. This field is available in API version 65.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product usage grant. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The sellable product that grants the usage resource. This field is a relationship field. **Relationship Name** ProductOffer **Refers To** Product2 |
| ProductUsageResourceNum | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The number of each resource grant map that starts with one and is consecutive. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the product usage resource record. Valid values are: `Active` `Draft` `Inactive` |
| TokenResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource of category `Token` that’s associated with the selected usage resource. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** TokenResource **Refers To** UsageResource |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the product usage grant. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[ProductUsageResourceChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
               

**[ProductUsageResourceFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductUsageResourceHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[ProductUsageResourceOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[ProductUsageResourceShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productusageresourcepolicy.htm ===
---
page_id: sforce_api_objects_productusageresourcepolicy.htm
title: ProductUsageResourcePolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productusageresourcepolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductUsageResourcePolicy

Represents the policies applicable to the usage resource when it’s
         associated with a sellable product. These policies are derived from the parent usage
         resource and can be overridden when setting up usage modeling.This object is available
      in API version 65 and later.

      
         

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
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record. |
| ProductSellingModelId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product selling model associated with this policy. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| ProductUsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The product usage resource associated with this policy. This field is a relationship field. **Relationship Name** ProductUsageResource **Relationship Type** Master-detail **Refers To** ProductUsageResource (the master object) |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rating frequency policy associated with the usage resource. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| UsageAggregationPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage aggregation policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageCommitmentPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage commitment policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageCommitmentPolicy **Refers To** UsageCommitmentPolicy |
| UsageOveragePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage overage policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageOveragePolicy **Refers To** UsageOveragePolicy |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[ProductUsageResourcePolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductUsageResourcePolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_transactionjournal.htm ===
---
page_id: sforce_api_objects_transactionjournal.htm
title: TransactionJournal
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_transactionjournal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TransactionJournal

      Represents consumption details of a usage resource that are recorded for
         creating usage summaries. This object is available for usage management in API version
      63.0 and later.

      

## Supported Calls

         
         

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You must have the Usage Management Run Time permission set license.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The account associated with the consumption. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| ActivityDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** Required. The date of the transaction. |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The three-letter ISO 4217 currency code of the monetary currency in which the transaction took place. Possible values are: `AED`—UAE Dirham `EUR`—Euro `GBP`—British Pound `INR`—Indian Rupee `JPY`—Japanese Yen `USD`—U.S. Dollar The default value is `USD`. |
| EndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The end date associated with the transaction. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The autogenerated number of the transaction journal. |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The number of units consumed. |
| QuantityUnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unit of measure for the associated usage resource. This field is a relationship field. **Relationship Name** QuantityUnitOfMeasure **Refers To** UnitOfMeasure |
| ReferenceRecordId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset associated with the transaction journal. This field is a polymorphic relationship field. **Relationship Name** ReferenceRecord **Refers To** Asset |
| StartDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The start date associated with the transaction. |
| Status | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the transaction. Possible values are: `Cancelled` `Error` `Pending` `Processed` |
| UniqueIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier of the transaction journal. |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource that's associated with the transaction journal. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |
| UsageSummaryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage summary that's associated with the transaction journal. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** UsageSummary **Refers To** UsageSummary |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of usage. Valid value is `UsageManagement`. |

=== ARTICLE: sforce_api_objects_transactionusageentitlement.htm ===
---
page_id: sforce_api_objects_transactionusageentitlement.htm
title: TransactionUsageEntitlement
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_transactionusageentitlement.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TransactionUsageEntitlement

Represents the details of each usage entitlement that's granted with
         the purchased sellable product, such as quantity and date when the entitlements were
         granted. This object is available in API version 63.0 and later. 

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

To create, update, and delete transaction usage entitlement records, you must have the
            Usage Management Run Time permission set license.

      

      

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

                  

                  
                     

                     

: 

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

: 

: 

                  

                  
                     

                     

: 

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
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that's associated with the usage entitlement. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| ActionType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of action that resulted in the transaction usage entitlement. Valid values are: `Amend` `Cancellation` `New` `Ramp` `Renewal` |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset associated with the sellable product. This field is a relationship field. **Relationship Name** Asset **Refers To** Asset |
| ChargeForOverage | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The action to be taken when the entitlements are used beyond their grant values. Valid values are: `No`—Don't charge for overconsumption `Yes`—Charge for overconsumption |
| DrawdownOrder | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The order that's used to debit entitlement consumption from the usage entitlement bucket. Valid values are: `ExpiringFirst` `GrantedFirst` `GrantedLast` |
| EffectiveEndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the active transaction usage entitlement ends. |
| EffectiveStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the transaction usage entitlement becomes active. |
| EntitlementQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The entitlement quantity for the usage resource. |
| EntitlementProcessingStatus | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Indicates whether the transaction usage entitlement has been processed by entitlement service to be used in Billing. Available in API version 65.0 and later. Possible values are: `PENDING`—Pending `PROCESSED`—Processed The default value is `PENDING`. |
| EntitlementUomClassId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unit of measure class for the usage entitlement. This field is a relationship field. **Relationship Name** EntitlementUomClass **Refers To** UnitOfMeasureClass |
| EntitlementUomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure to calculate the usage entitlement. This field is a relationship field. **Relationship Name** EntitlementUom **Refers To** UnitOfMeasure |
| ExternalOrderItem | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The custom or external order item that's associated with the entitlement. |
| GrantBindingTargetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The target associated with the entitlements that are granted with the sellable product. This field is a relationship field. **Relationship Name** GrantBindingTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| GrantType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of model that defines how the usage resource is consumed. Available in API version 65.0 and later. Possible values are: `Commit` `Grant` The default value is `Grant`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Auto number, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the transaction usage entitlement record. |
| NetQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The total quantity that combines the amended quantity with the initial transaction quantity in the order item. |
| OriginalEndDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The end date of the transaction usage entitlement when the related order was assetized, amended, renewed, or canceled. |
| OrderItemId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The order item that's associated with the entitlement. This field is a polymorphic relationship field. **Relationship Name** OrderItem **Refers To** OrderItem, WorkOrderLineItem |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the transaction usage entitlement. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PricebookEntryId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The price book entry that's associated with the sellable product. This field is a relationship field. **Relationship Name** PricebookEntry **Refers To** PricebookEntry |
| ProductId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The sellable product for which the entitlement is granted. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The sellable product for which the entitlement is granted. Available in API version 64.0 and later. This field is deprecated and will be retired in a future version. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| TokenResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource of category Token associated with the usage resource related to the usage product added in the quote line item. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** TokenResource **Refers To** UsageResource |
| TransactionQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The transaction quantity in the order for the usage entitlement. |
| UsageAggregationPolicyId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage aggregation policy for this entitlement. This field is deprecated and will be retired in a future version. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageGrantRefreshPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant refresh policy that's associated with the transaction usage entitlement. This field is a relationship field. **Relationship Name** UsageGrantRefreshPolicy **Refers To** UsageGrantRenewalPolicy |
| UsageGrantRolloverPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant rollover policy that's associated with the transaction usage entitlement. This field is a relationship field. **Relationship Name** UsageGrantRolloverPolicy **Refers To** UsageGrantRolloverPolicy |
| UsageModelType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of usage model for a product or service. `Anchor` is the main subscription product or service. `Pack` is the add-on product or service that grants additional usage resources for consumption. `Commit` is the product or service with a specific committed quantity of consumption. Valid values are: `Anchor` `Monetary Commitment` `Pack` `Quantity Commitment` `Token Commitment` Available in API version 64.0 and later. |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource record that's associated with the transaction usage entitlement. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |
| ValidityPeriodTerm | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The duration for which the usage resource grant is valid, when used with the validity period units. |
| ValidityPeriodUnit | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The length of a validity period for the usage resource grant, when used with the validity period term. Valid values are: `Month` `None` `Year` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[TransactionUsageEntitlementFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[TransactionUsageEntitlementHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[TransactionUsageEntitlementOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[TransactionUsageEntitlementShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_unitofmeasure.htm ===
---
page_id: sforce_api_objects_unitofmeasure.htm
title: UnitOfMeasure
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_unitofmeasure.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UnitOfMeasure

Defines the units and systems of units used to account for quantities of a usage
      resource. This object is available for usage management in API version 62.0 and
      later.

      
         

Examples of units of measure include Liter (for volume), Kilogram (for weight), and
            single units (such as Can, sachet, and packet).

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ConversionFactor | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The factor or rate that's used to convert this unit of measurement to the base unit. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Autogenerated identifier for the unit of measure record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the unit of measure record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Sequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The sequence number assigned to the unit of measure. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The status of the unit of measure. Valid values are: `Active` `Draft` `Inactive` |
| Type | **Type** picklist **Properties** Create, Filter, Group, Sort, Update **Description** The type of the unit of measure. For example, weight, distance, period. |
| UnitCode | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The code for the unit of measure. |
| UnitOfMeasureClassId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unit of measure class associated with the unit of measure. This field is a relationship field. **Relationship Name** UnitOfMeasureClass **Refers To** UnitOfMeasureClass |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UnitOfMeasureChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
               

**[UnitOfMeasureShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_unitofmeasureclass.htm ===
---
page_id: sforce_api_objects_unitofmeasureclass.htm
title: UnitOfMeasureClass
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_unitofmeasureclass.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UnitOfMeasureClass

Represents a standard unit of measure dimension. This object is
      available in API version 63.0 and later.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| BaseUnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The base unit of measure that's used to calculate and display quantities. This field is a relationship field. **Relationship Name** BaseUnitOfMeasure **Refers To** UnitOfMeasure |
| Code | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique user-defined string for the unit of measure class. |
| DefaultUnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The default unit of measure that's used to calculate and display quantities. This measure can be different from the base unit of measure and overridden by individual resources. This field is a relationship field. **Relationship Name** DefaultUnitOfMeasure **Refers To** UnitOfMeasure |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the unit of measure class. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Autogenerated identifier for the unit of measure class record. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the unit of measure class. Valid values are: `Active` `Draft` `Inactive` |
| Type | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of the unit of measure class. Valid values are: `Currency` `Token` `Usage` The default value is `Usage`. Available in API version 64.0 and later. This is a required field. |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UnitOfMeasureClassHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usagebillingperioditem.htm ===
---
page_id: sforce_api_objects_usagebillingperioditem.htm
title: UsageBillingPeriodItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagebillingperioditem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageBillingPeriodItem

Represents the calculated overages for the usage entitlement and the
         amount that's charged for these overages. This object is available in API version 63.0
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
         `search()`, 
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

To create, update, and delete transaction usage
            entitlement records, you must have the Usage Management Run Time permission set
            license.

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that's associated with the billing period item. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset that's associated with the usage billing period item. This field is a relationship field. **Relationship Name** Asset **Refers To** Asset |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The end date and time of the billing period. |
| ErrorCode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The error code when the billing request fails. Valid value is: `INTERNAL_ERROR` |
| ErrorDescription | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The error description that corresponds to the error code. |
| GrantBindingTargetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record that's associated with the usage entitlement account. This field is a relationship field. **Relationship Name** GrantBindingTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| OverageAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The amount calculated for the overage. |
| OverageAmountDerived | **Type** double **Properties** Filter, Nillable, Sort **Description** The numeric value specified in the OverageAmount field to process Data processing Engine (DPE) jobs. This field is a calculated field. |
| OverageQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity of the usage entitlement that was overused for the specified billing period. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage billing period item. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The start date and time of the billing period. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the usage billing period item. Valid values are: `Invoiced` `InvoicingFailed` `LiableSummaryComplete` `New` `ReadyForInvoicing` `Inactive`—Available in API version 65.0 and later. `InProgress`—Available in API version 66.0 and later. |
| TotalUsedQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The total quantity of usage entitlement that was used for the billing period. This includes granted and overused entitlements. |
| UoMId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure for the overage quantity of usage entitlement. This field is a relationship field. **Relationship Name** UoM **Refers To** UnitOfMeasure |
| UsageBillingPeriodItemNum | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage billing period item record. |
| UsageEntitlementAccountId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage entitlement account associated with the source usage entitlement bucket. This field is a relationship field. **Relationship Name** UsageEntitlementAccount **Refers To** UsageEntitlementAccount |
| UsageEntitlementBucketId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage entitlement bucket that's associated with the billing period item. This field is a relationship field. **Relationship Name** UsageEntitlementBucket **Refers To** UsageEntitlementBucket |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the usage entitlement bucket. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageBillingPeriodItemFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageBillingPeriodItemHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageBillingPeriodItemOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageBillingPeriodItemShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_usagecmtassetrelatedobj.htm ===
---
page_id: sforce_api_objects_usagecmtassetrelatedobj.htm
title: UsageCmtAssetRelatedObj
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagecmtassetrelatedobj.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageCmtAssetRelatedObj

Represents the relation between an asset for the commitment-based
         usage product and an asset, account, contract, or custom object. This object is
      available in API version 64.0 and later.

      
         

#### Important

            

Where possible, we changed noninclusive terms to align with our company value of
               Equality. We maintained certain terms to avoid any effect on customer
               implementations.

         

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The asset associated with the commitment-based usage product. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Master-detail **Refers To** Asset (the master object) |
| EffectiveEndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time until when the commitment for the related asset remains effective. |
| EffectiveStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the commitment for the related asset becomes effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage commitment asset related object record. |
| RelatedObjectId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The asset, account, or contract associated with the asset. This field is a polymorphic relationship field. **Relationship Name** RelatedObject **Refers To** Account, Asset, Contract Only Asset is supported in API version 64.0. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[UsageCmtAssetRelatedObjFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageCmtAssetRelatedObjHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usagecommitmentpolicy.htm ===
---
page_id: sforce_api_objects_usagecommitmentpolicy.htm
title: UsageCommitmentPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagecommitmentpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageCommitmentPolicy

Represents the set of rules that determines how commitments are
         applied to a usage resource. This object is available in API version 65 and
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
         `search()`, 
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CommitmentRate | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The rate that’s applicable to the usage resource’s units consumed post the commitment is utilized, but the commitment period is still active. Valid values are: `Bounded Object Rate` `Lowest Commitment Rate` The default value is `Lowest Commitment Rate`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the usage commitment policy. |

=== ARTICLE: sforce_api_objects_usageentitlementaccount.htm ===
---
page_id: sforce_api_objects_usageentitlementaccount.htm
title: UsageEntitlementAccount
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageentitlementaccount.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageEntitlementAccount

Represents the entitlement account details related to the asset that
         holds the wallet with the granted units. This object is available in API version 63.0
      and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that's associated with the usage entitlement. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| BillDayOfMonth | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The day of the month that the bill is generated on and that ends the billing period. |
| BillingPeriodEndDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the billing period of the usage entitlements ends. |
| BillingPeriodStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the billing period of the usage entitlements starts. |
| BillingPeriodTerm | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** The frequency at which the bill is generated. |
| BillingPeriodUnit | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The unit to measure the billing frequency. Valid value is: `MONTH` |
| EffectiveEndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the usage entitlement account ends. |
| EffectiveStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the usage entitlement account starts. |
| GrantBindingTargetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The target that's associated with the usage entitlement account. This field is a relationship field. **Relationship Name** GrantBindingTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Auto number, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage entitlement account record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage entitlement account. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PricebookEntryId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The price book entry that's associated with the sellable product. This field is a relationship field. **Relationship Name** PricebookEntry **Refers To** PricebookEntry |
| ProductId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The sellable product for which the entitlements are granted. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageEntitlementAccountFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageEntitlementAccountHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageEntitlementAccountOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageEntitlementAccountShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_usageentitlementbucket.htm ===
---
page_id: sforce_api_objects_usageentitlementbucket.htm
title: UsageEntitlementBucket
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageentitlementbucket.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageEntitlementBucket

Represents a usage entitlement that's granted with the sellable
         product. This object is available in API version 63.0 and later.

      

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

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
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
| BucketBalance | **Type** double **Properties** Create, Filter, Sort, Update **Description** The balance of the usage entitlement bucket after each transaction. |
| BucketBalanceUomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit that's used to measure the usage entitlement bucket balance. This field is a relationship field. **Relationship Name** BucketBalanceUom **Refers To** UnitOfMeasure |
| CompletedRollovers | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of rollovers that were completed for the entitlements. |
| ConsumedEntitlement | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The entitlements that have been consumed from this bucket. |
| EffectiveEndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the usage entitlement bucket period ends. |
| EffectiveStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the usage entitlement bucket becomes effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage entitlement bucket record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage entitlement bucket. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The parent record that's associated with the usage entitlement bucket. This field is a polymorphic relationship field. **Relationship Name** Parent **Refers To** UsageEntitlementAccount, UsageEntitlementBucket |
| ProvisionalBucketBalance | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The provisional entitlement balance available in the usage bucket. Available in API version 66.0 and later. |
| TotalAsOfBalance | **Type** double **Properties** Filter, Nillable, Sort **Description** The balance of the entitlements granted with the usage resource for a Usage entitlement account. |
| TotalConsumedEntitlement | **Type** double **Properties** Filter, Nillable, Sort **Description** The entitlements that have been consumed from this bucket. |
| TotalProvisionalBalance | **Type** double **Properties** Filter, Nillable, Sort **Description** The total provisional entitlement balance in the usage entitlement account as of the specified date. Available in API version 66.0 and later. |
| TransactionUsageEntitlementId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The transaction usage entitlement associated with this usage entitlement bucket. This field is a relationship field. **Relationship Name** TransactionUsageEntitlement **Refers To** TransactionUsageEntitlement |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource that's associated with the usage entitlement bucket. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageEntitlementBucketFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageEntitlementBucketHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageEntitlementBucketOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageEntitlementBucketShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_usageentitlemententry.htm ===
---
page_id: sforce_api_objects_usageentitlemententry.htm
title: UsageEntitlementEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageentitlemententry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageEntitlementEntry

Represents the usage entitlement details, such as the usage
         consumption, rollovers, and details of expired units for each tenure. This object is
      available in API version 63.0 and later.

      
         

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
| ClosingBalance | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity of the entitlement after adjusting the transaction quantity for the current entitlement validity period. |
| EffectiveEndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the usage entitlement entry ends. |
| EffectiveStartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the usage entitlement entry starts. |
| EntitlementBucketId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage entitlement bucket that's associated with the entitlement entry. This field is a relationship field. **Relationship Name** EntitlementBucket **Relationship Type** Master-detail **Refers To** UsageEntitlementBucket (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage entitlement entry record. |
| OpeningBalance | **Type** double **Properties** Create, Filter, Sort, Update **Description** The starting quantity of the entitlement for the current entitlement validity period. |
| ParentEntitlementBucketId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The parent usage entitlement bucket record that's associated with the entitlement entry. This field is a relationship field. **Relationship Name** ParentEntitlementBucket **Refers To** UsageEntitlementBucket |
| TransactionDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date when the transaction usage entitlement entry was updated. |
| TransactionQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity of the entitlement used during the current entitlement validity period. |
| TransactionReason | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The reason for the usage entitlement entry. Valid values are: `Amend` `Cancel` `Consumption` `Original` `Refresh` `Renew` `Rollover` |
| TransactionType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of transaction. Valid values are: `Credit` `Debit` `Expired` |
| TransactionUsageEntitlementId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The transaction usage entitlement that's associated with this usage entitlement entry. This field is a relationship field. **Relationship Name** TransactionUsageEntitlement **Refers To** TransactionUsageEntitlement |
| TransactionalBucketId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage entitlement bucket that's used to debit the consumption of entitlements. This field is a relationship field. **Relationship Name** TransactionalBucket **Refers To** UsageEntitlementBucket |
| UomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure that's associated with the usage entitlement. This field is a relationship field. **Relationship Name** Uom **Refers To** UnitOfMeasure |
| UsageSummaryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage summary that's associated with the usage entitlement. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** UsageSummary **Refers To** UsageSummary |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageEntitlementEntryFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageEntitlementEntryHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usagegrantrenewalpolicy.htm ===
---
page_id: sforce_api_objects_usagegrantrenewalpolicy.htm
title: UsageGrantRenewalPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagegrantrenewalpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageGrantRenewalPolicy

Represents a policy about the rollover of a usage grant. This
      object is available in API version 62.0 and later.

      
         

A usage grant renewal policy is used if you want to never renew a usage grant or renew
            on a specific frequency. 

      

      

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
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** A unique user-defined string for the usage grant renewal policy. |
| IsRenewalAllowed | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the policy renewal is allowed (`true`) or not (`false`). If `true`, then the policy can be renewed. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the renewal policy record. |
| RenewalFrequency | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The frequency of the policy renewals, when used with the RenewalFrequencyUnit field. |
| RenewalFrequencyUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The renewal duration for a policy. Valid values are: `Month` `Quarter` `Year` |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the renewal policy. Valid values are: `Active` `Draft` `Inactive` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageGrantRenewalPolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageGrantRenewalPolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usagegrantrolloverpolicy.htm ===
---
page_id: sforce_api_objects_usagegrantrolloverpolicy.htm
title: UsageGrantRolloverPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagegrantrolloverpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageGrantRolloverPolicy

      Represents a policy about the rollover of a usage grant.This object is
      available in API version 62.0 and later. 

      

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
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** A unique user-defined string for the usage grant rollover policy. |
| IsRolloverAllowed | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the policy allows the rollover of the usage grant. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| MaximumRolloverCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of times that the usage grant can roll over. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the rollover policy record. |
| ShouldAllowRolloverExpiry | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the rollover for the associated usage grant is allowed to expire. The default value is `false`. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the status of the rollover policy. Possible values are: `Active` `Draft` `Inactive` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageGrantRolloverPolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageGrantRolloverPolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usageoveragepolicy.htm ===
---
page_id: sforce_api_objects_usageoveragepolicy.htm
title: UsageOveragePolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageoveragepolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageOveragePolicy

      Represents the set of rules that determine the management of usage resource’s
         units consumed beyond the granted limit. This object is available in API version 65
      and later.

      

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
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the usage overage policy. |
| OverageChargeable | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies whether the overconsumption beyond the granted quantity is to be charged. Valid values are: `No` `Yes` |

=== ARTICLE: sforce_api_objects_usageprdgrantbindingpolicy.htm ===
---
page_id: sforce_api_objects_usageprdgrantbindingpolicy.htm
title: UsagePrdGrantBindingPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageprdgrantbindingpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsagePrdGrantBindingPolicy

Represents the association of a usage resource's grants with a
         sellable product. This object is available in API version 63.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      
      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

                  

               

            
| Field | Details |
| --- | --- |
| GrantBindingTargetType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of binding instance to which the grant is added. Valid values are: `Custom` `Product` `Contract` `Account` |
| GrantBindingType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of binding that indicates where the grant is added. Valid values are: `Self` `Target` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Autogenerated identifier for the usage product grant binding policy. |
| Product2Id | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The sellable product associated with the usage product grant binding policy. This field is a relationship field. **Relationship Name** Product2 **Refers To** Product2 |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsagePrdGrantBindingPolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsagePrdGrantBindingPolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usageratablesumcmtassetrt.htm ===
---
page_id: sforce_api_objects_usageratablesumcmtassetrt.htm
title: UsageRatableSumCmtAssetRt
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageratablesumcmtassetrt.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageRatableSumCmtAssetRt

      Represents the rate that’s calculated and applicable for the usage resource
         associated with the commitment assets related to an anchor. This object is available
      in API version 65.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CommitmentAssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The asset ID associated with the Usage Ratable Summary. This field is a relationship field. **Relationship Name** CommitmentAsset **Refers To** Asset |
| ErrorCode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the unique code generated when an error occurs. Valid value is `INTERNAL_ERROR`. |
| ErrorDescription | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the description of the error that occurred. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Name of the Usage Commitment Summary record. |
| NetUnitRate | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The calculated per-unit rate for usage after applying commitment-specific discounts during the rating process. |
| UsageRatableSummaryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The usage ratable summary associated with the usage commitment summary record. This field is a relationship field. **Relationship Name** UsageRatableSummary **Relationship Type** Master-detail **Refers To** UsageRatableSummary (the master object) |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[UsageRatableSumCmtAssetRtHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usageratablesummary.htm ===
---
page_id: sforce_api_objects_usageratablesummary.htm
title: UsageRatableSummary
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageratablesummary.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageRatableSummary

Represents the aggregation of the usage summaries that are used to
         calculate the rate at which the overages are charged. This object is available in API
      version 63.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that's associated with the ratable summary. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset that's associated with the ratable summary. This field is a relationship field. **Relationship Name** Asset **Refers To** Asset |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The end date and time of the ratable period. |
| ErrorCode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The code that represents the error encountered when the ratable summary is rated. Valid value is: `INTERNAL_ERROR` |
| ErrorDescription | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The error description that corresponds to the error code. |
| GrantBindingTargetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record that's associated with the usage ratable summary. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** GrantBindingTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage ratable summary record. |
| NetUnitRate | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The rate that's used to calculate the amount for each unit of usage entitlement overage. |
| NetUnitRateUomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure for the net unit rate applied to the overage. This field is a relationship field. **Relationship Name** NetUnitRateUom **Refers To** UnitOfMeasure |
| OverageQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity of the usage entitlements that were overused. |
| OverageQuantityUomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure that's used for overage quantity. This field is a relationship field. **Relationship Name** OverageQuantityUom **Refers To** UnitOfMeasure |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage ratable summary. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RatingDecisionDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the decision about rating consumption is done. |
| RatingExecutionIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the rating service execution that's used to retrieve waterfall logs. |
| RatingRequestId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID that invokes the rating service that's used to rate the usage ratable summary. This field is a relationship field. **Relationship Name** RatingRequest **Refers To** RatingRequest |
| SourceUsageResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource that’s rated in tokens when usage ratable summary is created. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** SourceUsageResource **Refers To** UsageResource |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The start date and time of the ratable period. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the ratable summary. Valid values are: `New` `RatingComplete` `RatingFailed` `SummaryCreated` `Inactive`—Available in API version 65.0 and later. `InProgress`—Available in API version 66.0 and later. |
| TierQuantity | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity that impacts the net unit rate of a usage entitlement. |
| TierQuantityUomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure for the tier quantity. This field is a relationship field. **Relationship Name** TierQuantityUom **Refers To** UnitOfMeasure |
| TotalAmount | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The total amount after calculating the overage based on the net unit rate. |
| UsageEntitlementAccountId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage entitlement account that's associated with the source of the ratable summary. This field is a relationship field. **Relationship Name** UsageEntitlementAccount **Refers To** UsageEntitlementAccount |
| UsageEntitlementBucketId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage entitlement bucket that's associated with the source of the ratable summary. This field is a relationship field. **Relationship Name** UsageEntitlementBucket **Refers To** UsageEntitlementBucket |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the usage entitlement bucket. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageRatableSummaryHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageRatableSummaryOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageRatableSummaryShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_usageresource.htm ===
---
page_id: sforce_api_objects_usageresource.htm
title: UsageResource
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageresource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageResource

Represents an entitlement granted to a user or party by a provider,
         such as data storage, computing power, bandwidth, or any other product or service.
         Additionally, this object is used to represent resources consumed over time. This
      object is available in API version 62.0 and later.

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| Category | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The category of the usage resource that's used to organize and understand the product grant maps. Valid values are: `Currency`—Available in API version 65.0 and later. `Usage` `Token`—Available in API version 64.0 and later. |
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The unique user-defined string for the usage resource. |
| DefaultUnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The default unit of measure for the given resource. The default value can be overridden with an alternate default unit of measure for a given resource. This field is a relationship field. **Relationship Name** DefaultUnitOfMeasure **Refers To** UnitOfMeasure |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the usage resource. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the usage resource record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage resource record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the usage resource. Valid values are: `Active` `Draft` `Inactive` |
| TokenResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource of Category `Token` that’s used to charge this usage resource. For example, you can select a usage resource Credits (Token category) to rate the usage resource Data (Usage category). This field is available in API version 65.0 and later. **Relationship Name** TokenResource **Refers To** UsageResource |
| UnitOfMeasureClassId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unit of measure class that's used with the resource to define the units in which this resource is measured. This field is a relationship field. **Relationship Name** UnitOfMeasureClass **Refers To** UnitOfMeasureClass |
| UsageDefinitionProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product associated with the usage resource to retrieve tax policy, calculate rating during overages, and other invoicing actions. This field is a relationship field. **Relationship Name** UsageDefinitionProduct **Refers To** Product2 |
| UsageResourceBillingPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource billing policy that defines how the usage resource can be aggregated before it's sent for rating. This field is a relationship field. This field is deprecated and will be retired in a future version. **Relationship Name** UsageResourceBillingPolicy **Refers To** UsageResourceBillingPolicy |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageResourceFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageResourceHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageResourceOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageResourceShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_usageresourcebillingpolicy.htm ===
---
page_id: sforce_api_objects_usageresourcebillingpolicy.htm
title: UsageResourceBillingPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageresourcebillingpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageResourceBillingPolicy

Represents information about how the usage is accumulated before
         rating a usage resource.This object is available in API version 62.0 and
      later.

      
         

A usage resource billing policy object is used to configure the properties of usage
            resources related to how aggregation is performed on the usage records before rating.
            Usage resource billing policies are defined at the usage resource level and can be
            reused across multiple usage resources.

      

      

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
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** A unique user-defined string for the usage resource billing policy. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the usage resource billing policy record. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the policy. Valid values are: `Active` `Draft` `Inactive` |
| UsageAccumulationMethod | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update, Defaulted On Create **Description** The method used to accumulate the usage. Valid values are: `Peak` `Sum` |
| UsageAccumulationPeriod | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The duration for which the usage is accumulated. Valid values are: `Daily` `Monthly` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageResourceBillingPolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageResourceBillingPolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usageresourcepolicy.htm ===
---
page_id: sforce_api_objects_usageresourcepolicy.htm
title: UsageResourcePolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usageresourcepolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageResourcePolicy

Represents the policies applicable to the usage resource whether it’s
         associated with a sellable product or not. This object is available in API version 65
      and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

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
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time when the current user last viewed or modified this record. |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rating frequency policy associated with the usage resource. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| UsageAggregationPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage aggregation policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageCommitmentPolicyId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage commitment policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageCommitmentPolicy **Refers To** UsageCommitmentPolicy |
| UsageOveragePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage overage policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageOveragePolicy **Refers To** UsageOveragePolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The usage resource associated with the usage resource policy. This field is a relationship field. **Relationship Name** UsageResource **Relationship Type** Master-detail **Refers To** UsageResource (the master object) |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[UsageResourcePolicyFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[UsageResourcePolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_usagesummary.htm ===
---
page_id: sforce_api_objects_usagesummary.htm
title: UsageSummary
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_usagesummary.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UsageSummary

Represents the aggregation of the entries in the transaction journal
         for a usage entitlement for a specified period. This object is available in API
      version 63.0 and later.

      

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that's associated with the sellable product that was purchased. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset that's associated with the entitlement that was summarized. This field is a relationship field. **Relationship Name** Asset **Refers To** Asset |
| ConsumptionUnits | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity that was used by the usage entitlement bucket. |
| DebitedUnits | **Type** double **Properties** Create, Filter, Sort, Update **Description** The units that are debited from the associated usage entitlement bucket. |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The end date and time of the usage summary. |
| GrantBindingTargetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record that's associated with the usage summary. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** GrantBindingTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LiableSummaryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage billing period item that's associated with this usage summary. This field is a relationship field. **Relationship Name** LiableSummary **Refers To** UsageBillingPeriodItem |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Autogenerated identifier for the usage summary record. |
| OverageUnits | **Type** double **Properties** Create, Filter, Sort, Update **Description** The quantity that was overused by the usage entitlement bucket. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the usage summary. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ParentUsageSummaryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The parent usage summary that’s associated with this usage summary. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** ParentUsageSummary **Refers To** UsageSummary |
| RatableSummaryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ratable summary that's associated with this usage summary. This field is a relationship field. **Relationship Name** RatableSummary **Refers To** UsageRatableSummary |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The start date and time of the usage summary. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the usage summary. Valid values are: `DrawdownComplete` `LiableSummaryComplete` `New` `RatableSummaryComplete` `Rated` `UsageSummaryComplete` `UsageSummaryInProgress` `Inactive`—Available in API version 65.0 and later. |
| UomId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unit of measure for the usage resource. This value overrides the default unit of measure defined in the associated unit of measure class. This field is a relationship field. **Relationship Name** Uom **Refers To** UnitOfMeasure |
| UsageEntitlementAccountId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage entitlement account that's associated with the usage summary. This field is a relationship field. **Relationship Name** UsageEntitlementAccount **Refers To** UsageEntitlementAccount |
| UsageEntitlementBucketId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage entitlement bucket that's associated with the usage summary. This field is a relationship field. **Relationship Name** UsageEntitlementBucket **Refers To** UsageEntitlementBucket |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource that's associated with the source of the usage entitlement bucket. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[UsageSummaryHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[UsageSummaryOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[UsageSummaryShare](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: usage_management_business_apis.htm ===
---
page_id: usage_management_business_apis.htm
title: Usage Management Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_business_apis.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Business APIs

Use the Usage Management Business APIs to get details of a usage-based product that’s
    associated with an asset, an order item, or a quote line item.

    

This table lists the available Usage Management resources.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

        

      
| Resource | Description |
| --- | --- |
| [`/asset-management/assets/assetId/usage-details`](./connect_resources_asset_usage_details.htm.md) (GET) | Get details of a usage-based product associated with an asset. This covers details of grants, resources, and configured rates for the product, including negotiated rates in case of a rate override. |
| [`/commerce/sales-orders/line-items/orderItemId/usage-details`](./connect_resources_order_usage_details.htm.md) (GET) | Get details of a usage-based product associated with an order item. |
| [`/commerce/quotes/line-items/quoteLineItemId/usage-details`](./connect_resources_quote_usage_details.htm.md) (GET) | Get details of a usage-based product associated with a quote line item. |
| [`/revenue/usage-management/binding-objects/bindingObjectId/actions/usage-details`](./connect_resources_retrieve_binding_object_details.htm.md) (GET) | Get details of grants, resources, rates, and any configured policies for a specified binding object. |
| [`/revenue/usage-management/consumption/actions/trace`](./connect_resources_consumption_traceabilities.htm.md) (POST) | Get a comprehensive breakdown of overage charges and resource drawdown, enabling you to view information that's applicable to specific invoice lines. |
| [`/revenue/usage-management/usage-products/actions/validate`](./connect_resources_usage_product_validation.htm.md) (POST) | Validate cross-object relationships and business rules for usage-based products. |

  

- 
**[Resources](./usage_management_business_apis_resources.htm.md)**  

Learn more about the available Usage Management API resources.

- 
**[Request Bodies](./usage_management_business_apis_requests.htm.md)**  

Learn more about the available request bodies of Usage Management APIs.

- 
**[Response Bodies](./usage_management_business_apis_responses.htm.md)**  

Learn more about the available response bodies of Usage Management APIs.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: usage_management_business_apis_requests.htm ===
---
page_id: usage_management_business_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_business_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available request bodies of Usage Management APIs.

- 
**[Consumption Traceabilities Input](./connect_requests_consumption_traceabilities_input.htm.md)**  

Input representation of the details of the liable summary IDs that are used to trace the     consumption.

- 
**[Usage Activation Request Input](./connect_requests_usage_activation_request_input.htm.md)**  

Input representation for a single product entry in a usage product activation request.     Each entry identifies one product and the usage resources to activate for that     product.

- 
**[Usage Product Activation Input](./connect_requests_usage_activation_input.htm.md)**  

Input representation of a usage product activation request.

- 
**[Usage Product Validation Input](./connect_requests_usage_product_validation_input.htm.md)**  

Input representation of the usage product validation request.

=== ARTICLE: usage_management_business_apis_resources.htm ===
---
page_id: usage_management_business_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_business_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Usage Management API resources.

- 
**[Asset Usage Details (GET)](./connect_resources_asset_usage_details.htm.md)**  

Get details of a usage-based product associated with an asset. This       covers details of grants, resources, and configured rates for the product, including       negotiated rates in case of a rate override.

- 
**[Binding Object Usage Details (GET)](./connect_resources_retrieve_binding_object_details.htm.md)**  

Get details of grants, resources, rates, and any configured policies       for a specified binding object.

- 
**[Consumption Traceabilities (POST)](./connect_resources_consumption_traceabilities.htm.md)**  

Get a comprehensive breakdown of overage charges and resource drawdown,       enabling you to view information that's applicable to specific invoice lines.

- 
**[Order Item Usage Details (GET)](./connect_resources_order_usage_details.htm.md)**  

Get details of a usage-based product associated with an order       item.

- 
**[Quote Line Item Usage Details (GET)](./connect_resources_quote_usage_details.htm.md)**  

Get details of a usage-based product associated with a quote line       item.

- 
**[Usage Product Activation (POST)](./connect_resources_usage_product_activation.htm.md)**  

Activate a usage product and its related records, such as usage resources, grants,     policies, and rate card entries, in a single request.

- 
**[Usage Product Validation (POST)](./connect_resources_usage_product_validation.htm.md)**  

Validate cross-object relationships and business rules for usage-based products.

=== ARTICLE: usage_management_business_apis_responses.htm ===
---
page_id: usage_management_business_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_business_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available response bodies of Usage Management APIs.

- 
**[Asset Detail](./connect_responses_asset_detail_output.htm.md)**  

Output representation of the details of a specific asset.

- 
**[Billing Period](./connect_responses_billing_period_output.htm.md)**  

Output representation of the details of a specific billing period.

- 
**[Binding Object Detail](./connect_responses_binding_object_detail_output.htm.md)**  

Output representation of the list of records with the binding target details.

- 
**[Binding Object Grant Detail](./connect_responses_binding_object_grant_detail_output.htm.md)**  

Output representation of the details of usage resource grants for a specified binding     object.

- 
**[Binding Object Rate Adjustments](./connect_responses_binding_object_rate_adjustments_output.htm.md)**  

Output representation of the details of binding target rate adjustments.

- 
**[Binding Object Rate](./connect_responses_binding_object_rate_output.htm.md)**  

Output representation of the details of Binding Object Rates object or Asset Rates     object.

- 
**[Binding Object Resource Grant And Policy Detail](./connect_responses_binding_object_resource_grant_and_policy_detail_output.htm.md)**  

Output representation of the details of resource grants and binding policies.

- 
**[Binding Object Resource Policy Detail](./connect_responses_binding_object_resource_policy_detail_output.htm.md)**  

Output representation of the details of a usage resource policy.

- 
**[Binding Object Usage Detail](./connect_responses_usage_detail_binding_object_output.htm.md)**  

Output representation of the usage details of a binding object.

- 
**[Consumption Source Detail](./connect_responses_consumption_source_detail_output.htm.md)**  

Output representation of the details of a specific consumption source.

- 
**[Consumption Traceabilities](./connect_responses_consumption_traceabilities_output.htm.md)**  

Output representation of the overage and resource drawdown details.

- 
**[Errors](./connect_responses_errors_output.htm.md)**  

Output representation of the group of error messages with the same error code.

- 
**[Error Details](./connect_responses_error_output.htm.md)**  

Output representation of the top-level error detail when validation fails.

- 
**[Error Message](./connect_responses_error_message_output.htm.md)**  

Output representation of the details of records that failed with this specific     error.

- 
**[Error Warning Details](./connect_responses_error_warning_details_output.htm.md)**  

Output representation of the individual warning or error message with associated record details.

- 
**[Consumption Traceabilities Data](./connect_responses_consumption_traceabilities_data_output.htm.md)**  

Output representation of the list of asset details.

- 
**[Fields Response](./connect_responses_fields_output.htm.md)**  

Output representation of the details of the optional fields on the usage-based     selling-related objects.

- 
**[Grant Detail](./connect_responses_negotiated_grant_detail_output.htm.md)**  

Output representation of the details of a grant from the ProductUsageGrant,     LineItemUsageResourceGrant, or TransactionUsageEntitlement objects.

- 
**[Generic Error Details](./connect_responses_generic_error_output.htm.md)**  

Output representation of the error details encountered during the API     request.

- 
**[Lookup Detail](./connect_responses_lookup_detail_output.htm.md)**  

Output representation of the details of a usage resource record.

- 
**[Policy Details](./connect_responses_policy_detail_output.htm.md)**  

Output representation of the details of a policy.

- 
**[Product Activation Result](./connect_responses_product_activation_result_output.htm.md)**  

Output representation of the activation outcome for a single product, including any     errors that occurred while activating the product or its associated usage records.

- 
**[Product Validation Result](./connect_responses_product_validation_result_output.htm.md)**  

Output representation of the validation result for a specific product.

- 
**[Rate Adjustments](./connect_responses_rate_adjustments_output.htm.md)**  

Output representation of the details of a rate adjustment.

- 
**[Rate and Consumption Source Detail](./connect_responses_rate_and_consumption_source_detail_output.htm.md)**  

Output representation of the details of a specific rate and its consumption     source.

- 
**[Rate Card Entry](./connect_responses_rate_card_entry_output.htm.md)**  

Output representation of the details of a rate card entry.

- 
**[Record Details](./connect_responses_record_details_output.htm.md)**  

Output representation of the record details including ID and name.

- 
**[Resource Detail](./connect_responses_resource_detail_output.htm.md)**  

Output representation of the details of a specific usage resource.

- 
**[Resource Policy Detail](./connect_responses_resource_policy_detail_output.htm.md)**  

Output representation of the details of a usage resource policy.

- 
**[Usage Activation Error](./connect_responses_usage_activation_error_output.htm.md)**  

Output representation of a single error encountered while activating a usage product or one of its related records.

- 
**[Usage Activation Result](./connect_responses_usage_activation_result_output.htm.md)**  

Output representation that groups the activation outcome and the validation outcome     for the product in a usage product activation request.

- 
**[Usage Details](./connect_responses_usage_detail_output.htm.md)**  

Output representation of the usage details of a quote, an order, or an asset.

- 
**[Usage Details Error Response](./connect_responses_usage_detail_error_response.htm.md)**  

Output representation of the details of an error related to usage details.

- 
**[Usage Product Activation](./connect_responses_usage_activation_output.htm.md)**  

Output representation of a usage product activation response.

- 
**[Usage Product Validation](./connect_responses_usage_product_validation_output.htm.md)**  

Output representation of all the performed validations.

- 
**[Usage Resource Grant And Policy Detail](./connect_responses_usage_resource_grant_and_policy_detail_output.htm.md)**  

Output representation of the details of a usage resource grant and policy.

- 
**[Validation Error](./connect_responses_validation_error_output.htm.md)**  

Output representation of the validation errors grouped by rule name.

- 
**[Validation Result](./connect_responses_validation_result_output.htm.md)**  

Output representation of the validation results grouped by rule name.

- 
**[Validation Warning](./connect_responses_validation_warning_output.htm.md)**  

Output representation of the validation warnings grouped by rule name.

- 
**[Warnings](./connect_responses_warnings_output.htm.md)**  

Output representation of a group of warning messages with the same warning     code.

- 
**[Warning Message](./connect_responses_warning_message_output.htm.md)**  

Output representation of the details of records that triggered this specific     warning.

=== ARTICLE: usage_management_fields_on_product2.htm ===
---
page_id: usage_management_fields_on_product2.htm
title: Usage Management Fields on Product2
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_fields_on_product2.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Fields on Product2

Standard and custom fields extend the standard Product2 object for
         use in Usage Management to represent information about products.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| UsageModelType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of usage model for a product or service. Valid values are: `Anchor`—The main subscription product or service. Available in API version 62.0 and later. `Pack`—The add-on product or service that grants additional usage resources for consumption. Available in API version 62.0 and later. `Monetary Commitment`—An agreement by a customer to spend a minimum amount for a product or service in a defined period. Available in API version 65.0 and later. `Quantity Commitment`—An agreement by a customer to use a minimum quantity of a product or service in a defined period. Available in API version 65.0 and later. `Token Commitement`—An agreement by a customer to use a minimum quantity of tokens for a product or service in a defined period. Available in API version 65.0 and later. |

      

   

#### See Also

- [Product2](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_product2.htm)

=== ARTICLE: usage_management_fields_on_standard_objects.htm ===
---
page_id: usage_management_fields_on_standard_objects.htm
title: Usage Management Fields on Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_fields_on_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Fields on Standard Objects

Usage Management adds standard and custom fields to some standard
         Salesforce objects. These fields are available only in orgs where Usage Management is
         enabled. This object is available in API version 63.0 and later.

- 
**[Usage Management Fields on Product2](./usage_management_fields_on_product2.htm.md)**  

Standard and custom fields extend the standard Product2 object for          use in Usage Management to represent information about products.

=== ARTICLE: usage_management_flow_metadata_api.htm ===
---
page_id: usage_management_flow_metadata_api.htm
title: Flow for Usage Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Usage Management

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Usage Management exposes additional actionType values for the FlowActionCall Metadata
        type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Usage Management include: `invokeSummaryCreationService`—Invoke the service that creates various summaries, such as usage, ratable, and liable summaries where the usage amount is zero. The service also checks and updates the billing period of the usage entitlement account if the billing period is expired. `processConsumptionOverages`—Process consumption overages for the usage summary records with `SummaryComplete` status. This action uses the entitlement service to process the overages. `refreshUsageEntitlementBucket`—Refresh entitlements by evaluating the usage entitlement bucket records and creating a new usage entitlement entry. `retriggerEntlCreaProc`—Retrigger entitlement creation process for failed or unprocessed assets. |

=== ARTICLE: usage_management_invocable_actions_parent.htm ===
---
page_id: usage_management_invocable_actions_parent.htm
title: Usage Management Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Standard Invocable Actions

Learn more about the standard invocable actions available with Usage
    Management.

- 
**[Invoke Summary Creation Action](./actions_obj_invoke_summary_creation.htm.md)**  

Invoke the service that creates various summaries, such as usage, 			ratable, and liable summaries where the usage amount is zero. The service also checks 			and updates the billing period of the usage entitlement account if the billing period is 			expired.

- 
**[Process Consumption Overages Action](./actions_obj_process_consumption_overages.htm.md)**  

Process consumption overages for the usage summary records with 				`SummaryComplete` status. This action uses the 			entitlement service to process the overages.

- 
**[Refresh Usage Entitlement Bucket Action](./actions_obj_refresh_usage_entitlement_bucket.htm.md)**  

Refresh entitlements by evaluating the usage entitlement bucket 			records and creating a new usage entitlement entry.

- 
**[Retrigger Entitlement Creation Process Action](./actions_obj_retrigger_entitlement_creation_process.htm.md)**  

Retrigger entitlement creation process for failed or unprocessed             assets.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

- [*Salesforce Help*: Usage Management](https://help.salesforce.com/s/articleView?id=ind.um_usage_management.htm&language=en_US)

=== ARTICLE: usage_management_metadata_api_parent.htm ===
---
page_id: usage_management_metadata_api_parent.htm
title: Usage Management Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Usage Management](./usage_management_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

- 
**[IndustriesUsageSettings](./meta_industriesusagesettings.htm.md)**  

Represents the settings for Usage Management. 	

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: usage_management_overview.htm ===
---
page_id: usage_management_overview.htm
title: Usage Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management

Provide transparent, accurate, and efficient management of
  usage data and estimated usage amount to enhance revenue management capabilities.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[Usage Management Standard Objects](./usage_management_std_objects_parent.htm.md)**  

The Usage Management data model provides objects and fields to set up and manage   consumption of usage-based products.

- 
**[Usage Management Fields on Standard Objects](./usage_management_fields_on_standard_objects.htm.md)**  

Usage Management adds standard and custom fields to some standard          Salesforce objects. These fields are available only in orgs where Usage Management is          enabled. This object is available in API version 63.0 and later.

- 
**[Usage Management Standard Invocable Actions](./usage_management_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Usage     Management.

- 
**[Usage Management Business APIs](./usage_management_business_apis.htm.md)**  

Use the Usage Management Business APIs to get details of a usage-based product that’s     associated with an asset, an order item, or a quote line item.

- 
**[Usage Management Metadata API Types](./usage_management_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

=== ARTICLE: usage_management_std_objects_parent.htm ===
---
page_id: usage_management_std_objects_parent.htm
title: Usage Management Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Usage Management
parent_page: usage_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage Management Standard Objects

The Usage Management data model provides objects and fields to set up and manage
  consumption of usage-based products.

- 
**[ProductUsageGrant](./sforce_api_objects_productusagegrant.htm.md)**  

       Represents the details of a grant associated with a resource, product, or          service, such as the purchased quantity, renewal and rollover policy, and validity of the          grant. This object is available in API version 62.0 and later.

- 
**[ProductUsageResource](./sforce_api_objects_productusageresource.htm.md)**  

Represents the mapping of a product and its usage resources.       This object is available in API version 64.0 and later.

- 
**[ProductUsageResourcePolicy](./sforce_api_objects_productusageresourcepolicy.htm.md)**  

Represents the policies applicable to the usage resource when it’s          associated with a sellable product. These policies are derived from the parent usage          resource and can be overridden when setting up usage modeling.This object is available       in API version 65 and later.

- 
**[TransactionUsageEntitlement](./sforce_api_objects_transactionusageentitlement.htm.md)**  

Represents the details of each usage entitlement that's granted with          the purchased sellable product, such as quantity and date when the entitlements were          granted. This object is available in API version 63.0 and later. 

- 
**[TransactionJournal](./sforce_api_objects_transactionjournal.htm.md)**  

       Represents consumption details of a usage resource that are recorded for          creating usage summaries. This object is available for usage management in API version       63.0 and later.

- 
**[UnitOfMeasure](./sforce_api_objects_unitofmeasure.htm.md)**  

Defines the units and systems of units used to account for quantities of a usage       resource. This object is available for usage management in API version 62.0 and       later.

- 
**[UnitOfMeasureClass](./sforce_api_objects_unitofmeasureclass.htm.md)**  

Represents a standard unit of measure dimension. This object is       available in API version 63.0 and later.

- 
**[UsageBillingPeriodItem](./sforce_api_objects_usagebillingperioditem.htm.md)**  

Represents the calculated overages for the usage entitlement and the          amount that's charged for these overages. This object is available in API version 63.0       and later.

- 
**[UsageCmtAssetRelatedObj](./sforce_api_objects_usagecmtassetrelatedobj.htm.md)**  

Represents the relation between an asset for the commitment-based          usage product and an asset, account, contract, or custom object. This object is       available in API version 64.0 and later.

- 
**[UsageCommitmentPolicy](./sforce_api_objects_usagecommitmentpolicy.htm.md)**  

Represents the set of rules that determines how commitments are          applied to a usage resource. This object is available in API version 65 and       later.

- 
**[UsageEntitlementAccount](./sforce_api_objects_usageentitlementaccount.htm.md)**  

Represents the entitlement account details related to the asset that          holds the wallet with the granted units. This object is available in API version 63.0       and later.

- 
**[UsageEntitlementBucket](./sforce_api_objects_usageentitlementbucket.htm.md)**  

Represents a usage entitlement that's granted with the sellable          product. This object is available in API version 63.0 and later.

- 
**[UsageEntitlementEntry](./sforce_api_objects_usageentitlemententry.htm.md)**  

Represents the usage entitlement details, such as the usage          consumption, rollovers, and details of expired units for each tenure. This object is       available in API version 63.0 and later.

- 
**[UsageGrantRenewalPolicy](./sforce_api_objects_usagegrantrenewalpolicy.htm.md)**  

Represents a policy about the rollover of a usage grant. This       object is available in API version 62.0 and later.

- 
**[UsageGrantRolloverPolicy](./sforce_api_objects_usagegrantrolloverpolicy.htm.md)**  

       Represents a policy about the rollover of a usage grant.This object is       available in API version 62.0 and later. 

- 
**[UsageOveragePolicy](./sforce_api_objects_usageoveragepolicy.htm.md)**  

       Represents the set of rules that determine the management of usage resource’s          units consumed beyond the granted limit. This object is available in API version 65       and later.

- 
**[UsagePrdGrantBindingPolicy](./sforce_api_objects_usageprdgrantbindingpolicy.htm.md)**  

Represents the association of a usage resource's grants with a          sellable product. This object is available in API version 63.0 and later.

- 
**[UsageRatableSummary](./sforce_api_objects_usageratablesummary.htm.md)**  

Represents the aggregation of the usage summaries that are used to          calculate the rate at which the overages are charged. This object is available in API       version 63.0 and later.

- 
**[UsageRatableSumCmtAssetRt](./sforce_api_objects_usageratablesumcmtassetrt.htm.md)**  

       Represents the rate that’s calculated and applicable for the usage resource          associated with the commitment assets related to an anchor. This object is available       in API version 65.0 and later.

- 
**[UsageResource](./sforce_api_objects_usageresource.htm.md)**  

Represents an entitlement granted to a user or party by a provider,          such as data storage, computing power, bandwidth, or any other product or service.          Additionally, this object is used to represent resources consumed over time. This       object is available in API version 62.0 and later.

- 
**[UsageResourcePolicy](./sforce_api_objects_usageresourcepolicy.htm.md)**  

Represents the policies applicable to the usage resource whether it’s          associated with a sellable product or not. This object is available in API version 65       and later.

- 
**[UsageResourceBillingPolicy](./sforce_api_objects_usageresourcebillingpolicy.htm.md)**  

Represents information about how the usage is accumulated before          rating a usage resource.This object is available in API version 62.0 and       later.

- 
**[UsageSummary](./sforce_api_objects_usagesummary.htm.md)**  

Represents the aggregation of the entries in the transaction journal          for a usage entitlement for a specified period. This object is available in API       version 63.0 and later.

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

