# Revenue Management Developer Guide 264 — sección: Transaction Management (parte 1/2) (136 artículos)

=== ARTICLE: actions_obj_amend_assets.htm ===
---
page_id: actions_obj_amend_assets.htm
title: Initiate Amendment Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_amend_assets.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Amendment Action

Initiate and execute the amendment of an asset.

		

			

Specify the IDs of assets to amend, the amendment start date, and any quantity
				changes. You can choose whether the action creates an amendment quote or order.

		

		

## Considerations

			
			

For usage products, creating an order directly by setting `amendOutputType` to `Order` is
				currently not supported. The direct-to-order flow can create Order Products without
				required related Rate Card Entry records, which can cause order activation to
				fail.

			

When you amend usage assets, use a two-step flow.

			
				
1. Create an amendment quote by calling `initiateAmendment` with `amendOutputType` set to `Quote`.

				
2. Create an order from that amendment quote.

			

		

		
		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/initiateAmendment`

				
				
					

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

						

						
							

							

: 

: 

						

						
							

							

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
| amendAssetIds | **Type** string **Description** Required. The IDs of the assets that you want to amend. |
| amendContractId | **Type** string **Description** The ID of the contract record to be synced with the amendment. |
| amendStartDate | **Type** datetime **Description** Required. Effective start date of the amendment. |
| amendOpportunityId | **Type** string **Description** The ID of the Opportunity record to be synced with the amendment quote. |
| amendOutputType | **Type** string **Description** Required. Type of amendment record to create such as a quote or an order. For usage products, set this value to `Quote`. The usage-related records (`QuoteLineItemUseResourceGrant`, `QuoteLineItemUsageResourcePolicy`, and `QuoteLineRateCardEntry`) are copied in the quote action flow, not in the amend order flow. |
| quantityChange | **Type** double **Description** Required. Quantity to add to or reduce from the asset's existing quantity. |
| skipPricing | **Type** boolean **Description** Indicates whether the pricing procedure must be skipped (`true`) or performed (`false`). Available in API version 64.0 and later. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| amendRecordId | **Type** string **Description** The ID of the amendment record that’s created. |
| requestIdentifier | **Type** string **Description** Request ID that’s used to track the async request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Initiate Amendment action.

						

```
{
    "inputs": [
        {
            "amendAssetIds": ["02iI8000000HPzXIAW"],
            "amendStartDate": "2023-10-21T00:00:00.000Z",
            "quantityChange": 5,
            "amendOutputType": "Quote",
            "amendContractId": "800DU0000000lZlYAI",
            "amendOpportunityId": "006DU0000025AanYAE",
            "skipPricing": false
        }
    ]
}
```

						

This sample response is for the Initiate Amendment action.

						

```
[
    {
        "actionName": "initiateAmendment",
        "errors": null,
        "isSuccess": true,
        "outputValues": {
            "record_id": "0Q0xx0000004NsSCAU",
            "requestIdentifier": "16Pxx0000004NIy"
        },
        "version": 1
    }
]
```

=== ARTICLE: actions_obj_cancel_assets.htm ===
---
page_id: actions_obj_cancel_assets.htm
title: Initiate Cancellation Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_cancel_assets.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Cancellation Action

Initiate and execute the cancellation of an asset.

		

Specify the IDs of the assets that you want to add to cancel by specifying a start date. You can
				also specify the type of cancellation record that you want to create, such as a
				quote or an order.

This action is available in API version 60.0 and
				later.

		
		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/initiateCancellation`

				
				
					

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
| cancelAssetIds | **Type** string **Description** Required. The IDs of the assets that you want to cancel. All assets in a request must belong to the same price book. |
| cancelContractId | **Type** string **Description** The ID of the contract record to sync with the cancellation. |
| cancelOpportunityId | **Type** string **Description** The ID of the Opportunity record to sync with the cancellation quote. |
| cancelOutputType | **Type** string **Description** Required. Type of cancellation record to create such as a quote or an order. |
| cancelStartDate | **Type** datetime **Description** Required. Effective date of the cancellation. |
| skipPricing | **Type** boolean **Description** Indicates whether the pricing procedure must be skipped (`true`) or performed (`false`). Available in API version 64.0 and later. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| cancelRecordId | **Type** string **Description** The ID of the cancellation record that’s created. |
| requestIdentifier | **Type** string **Description** Request ID that’s used to track the async request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Initiate Cancellation action.

						

```
{
    "inputs": [
        {
            "cancelAssetIds": [
                "02iI8000000Lc5fIAC"
            ],
            "cancelStartDate": "2023-11-09T00:00:00",
            "cancelOutputType": "Quote",
            "cancelContractId": "800DU0000000lZlYAI",
            "cancelOpportunityId": "006DU0000025AanYAE",
            "skipPricing": false
        }
    ]
}
```

						

This sample response is for the Initiate Cancellation action.

						

```
[
    {
        "actionName": "initiateCancellation",
        "errors": null,
        "isSuccess": true,
        "outputValues": {
            "record_id": "0Q0xx0000004P32CAE",
            "requestIdentifier": "16Pxx0000004OTY"
        },
        "version": 1
    }
]
```

=== ARTICLE: actions_obj_create_contract_from_quote.htm ===
---
page_id: actions_obj_create_contract_from_quote.htm
title: Create Contract Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_contract_from_quote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Contract Action

Create a contract from a specific quote record.

		
			

This action is available in API version 60.0 and later.

		

		

## Special Access Rules

			
			

The Create Contract action is available in Developer, Enterprise, and Unlimited Editions of
				Revenue Management.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/createContract`

				
				
					

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

- 
- 
- 

						

						
							

							

: 

: 

						

					

				
| Input | Details |
| --- | --- |
| contractPriceOption | **Type** string **Description** Optional. Determines how the contract price is set for quote line items based on the selected value. Valid values are: `CONTRACT_HEADER_ONLY`—Creates a contract with only the header information, without using net prices or discounts. `NET_UNIT_PRICE_ONLY`—Creates a contract specifically for quote line items with a net unit price, saving all net unit prices of the quote as contract prices. `DISCOUNT_ONLY`—Creates contract prices specifically for quote line items with discounts, saving all discounts of the quote as contract prices. The default value is `CONTRACT_HEADER_ONLY`. |
| sourceId | **Type** string **Description** Required. ID of the quote or order that you want to create a contract from. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| contractId | **Type** string **Description** ID of the contract created for the specified order or quote. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Create Contract action.

						

```
{
  "inputs": [
    {
      "sourceId": "0Q0RO0000003LyU",
      "contractPriceOption": "NET_UNIT_PRICE_ONLY"
    }
  ]
}
```

						

This sample response is for the Create Contract action.

						

```
[
  {
    "actionName": "createContract",
    "errors": null,
    "isSuccess": true,
    "outputValues": {
      "contractId": "800XXX123456789"
    }
  }
]
```

					

				
			

		

	

#### See Also

- [*Salesforce Help*: Use a Custom Flow to Create Contracts](https://help.salesforce.com/s/articleView?id=ind.qocal_create_contracts_using_a_flow.htm&type=5&language=en_US)

=== ARTICLE: actions_obj_create_order_from_quote.htm ===
---
page_id: actions_obj_create_order_from_quote.htm
title: Create Order From Quote Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_order_from_quote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Order From Quote Action

Create a draft order from a quote record.

		
			

This action is available in API version 60.0 and later.

			

#### Note

 This API has been deprecated as of API version 65.0. In API version 65.0 and
				later, use the [Create
					Orders From Quote Action](./actions_obj_create_orders_from_quote.htm.md).

		

		

## Special Access Rules

			
			

The Create Order From Quote action is available in Enterprise, Unlimited, and Developer
				Editions of Revenue Management.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/createOrderFromQuote`

				
				
					

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
| quoteRecordId | **Type** id **Description** Required. ID of the quote record. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| orderId | **Type** string **Description** ID of the created draft order. |
| orderNumber | **Type** string **Description** Unique order number of the created draft order. |
| requestId | **Type** string **Description** ID of the request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Create Order From Quote action.

						

```
{
    "inputs": [
        {
        "quoteRecordId": "0Q0D200000000DhKAI"
        }
    ]
}
```

						

This sample response is for the Create Order From Quote action.

						

```
[
  {
    "actionName": "createOrderFromQuote",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "orderNumber": "00000122",
      "orderId": "801oB000000DCrNQAW"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_create_orders_from_quote.htm ===
---
page_id: actions_obj_create_orders_from_quote.htm
title: Create Orders From Quote Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_orders_from_quote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Orders From Quote Action

Create multiple orders from a single quote instead of a single
            order, ensuring easier order management and fulfillment operations.

        You can split a quote to create orders in these ways.
                
- You can create an order by selecting a subset of quote line items.

                
- You can split a quote into multiple orders based on quote line group.

                
- You can split a quote into multiple orders based on a quote line item field,
                    such as Product2.

            

See [Considerations for
                    Creating Multiple Orders from a Quote](https://help.salesforce.com/s/articleView?id=ind.qocal_split_quote_to_orders_important_considerations.htm&language=en_US). This action is available in API
                version 65.0 and later.

        

## Special Access Rules

            
            

Ensure the **Advanced Order Creation From Quote** toggle from
                Revenue Settings from Setup is enabled to access this action.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/createOrdersFromQuote`

                
                
                    

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

- 
- 
- 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| orderCreationMethod | **Type** string **Description** If specified, represents the method used to create orders. Valid values are: `CreateSingleOrder`—Creates a single order from a quote. This method creates the order header and order line items synchronously. `CreateOrderByGroup`—Create multiple orders based on a quote line group. `CreateOrderByField`—Create multiple orders based on a specified quote line item field. If you're creating multiple orders from a quote, the order header records are created synchronously and order line items are created asynchronously. If unspecified, the default value is `CreateSingleOrder`. |
| orderCreationParameters | **Type** Apex-defined **Description** An Apex `ConnectApi.OrderCreationParametersInputRepresentation` record that contains the additional parameters required by the specified order creation method. |
| quoteId | **Type** id **Description** Required. The ID of the source quote tied to the orders created. |
| quoteLineItemIds | **Type** id **Description** List of quote line item IDs to create the orders from. If specified, the orders are created for the list of provided quote line items. If unspecified, orders are created for all quote line items. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| orderIds | **Type** id **Description** List of the created order IDs. |
| requestId | **Type** string **Description** The request ID used to query the async status. |
| statusUrl | **Type** string **Description** The status URL that's used to track the async status. |

        

        
        

## Examples

            
            
                
                    

**Create a partial order from a quote**

                    
: 
                        

This example shows a sample request to create a partial order from a
                            quote.

                        

```
{
  "inputs": [
    {
      "quoteId": "0Q0DU0000005tJc0AI",
      "quoteLineItemIds": [
        "0QLDU000000ay2G4AQ",
        "0QLDU000000ay2n4AA"
      ],
      "orderCreationMethod": "CreateSingleOrder"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
{
    "actionName": "createOrdersFromQuote",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "requestId": null,
      "statusUrl": null,
      "orderIds": [
        "801DU000000EYySYAW"
      ]
    },
    "sortOrder": -1,
    "version": 1
  }
```

                    

                
                
                    

**Create orders from a quote based on a quote line group**

                    
: 
                        

This example shows a sample request to create orders from a quote based
                            on a quote line group.

                        

```
{
  "inputs": [
    {
      "quoteId": "0Q0DU0000005tJk0AI",
      "orderCreationMethod": "CreateOrderByGroup"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
{
  "actionName": "createOrdersFromQuote",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": {
    "requestId": "16PRM0000004DBq",
    "orderIds": [
      "801S70000001VKgIAM"
    ],
    "success": true,
    "errors": [],
    "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16PRM0000004DBq"
  },
  "sortOrder": -1,
  "version": 1
}
```

                    

                
                
                    

**Create orders from a quote based on a quote line item field**

                    
: 
                        

This example shows a sample request to create orders from a quote based
                            on a quote line item field

                        

```
{
  "inputs": [
    {
      "quoteId": "0Q0DU0000005tJW0AY",
      "orderCreationMethod": "CreateOrderByField",
      "orderCreationParameters": {
        "splitFieldName": "Product2Id"
      }
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
{
  "actionName": "createOrdersFromQuote",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": {
    "requestId": "16PRM0000004DBq",
    "orderIds": [
      "801S70000001VKgIAM",
      "801S70000001WKgIBN"
    ],
    "success": true,
    "errors": [],
    "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16PRM0000004DBq"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_create_update_asset_from_order.htm ===
---
page_id: actions_obj_create_update_asset_from_order.htm
title: Create or Update Asset From Order Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_update_asset_from_order.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create or Update Asset From Order Action

Create an asset for each order item in the specified order. New
			assets are created for a new order. Modify existing assets for change order requests,
			such as a renewal or a cancellation.

		

When the custom product name for an order line item has a value, the asset name is set
				to custom product name.

This action is available in API version 60.0 and
				later.

		

## Special Access Rules

You need the Assetize Order permission set to use
				this invocable action.

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/createOrUpdateAssetFromOrder`

				
				
					

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
| orderId | **Type** string **Description** Required. ID of the order. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** ID of the request to create an asset. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Create or Update Asset From Order action.

						

```
{
  "inputs": [
    {
      "orderId": "801DE000000oJfAYAU"
    }
  ]
}
```

						

This sample response is for the Create or Update Asset From Order action.

						

```
[
    {
        "actionName": "createOrUpdateAssetFromOrder",
        "errors": null,
        "isSuccess": true,
        "outputValues": {
            "requestId": "3b89392d-6987-40d9-9190-d18fdb5cb849"
        }
    }
]
```

=== ARTICLE: actions_obj_create_update_asset_from_order_item.htm ===
---
page_id: actions_obj_create_update_asset_from_order_item.htm
title: Create or Update Asset From Order Item Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_update_asset_from_order_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create or Update Asset From Order Item Action

Create assets from individual order items within an order. Track
			assets after the individual line items of an order reach a certain stage in their
			lifecycle, such as submitted, fulfilled, or provisioned. If the order item is part of a
			renewal, an amendment, or a cancellation, existing assets are changed. 

		
			

This action is available in API version 60.0 and later.

		

		

## Special Access Rules

You need the Assetize Order permission set to
				use this invocable action.

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/createOrUpdateAssetFromOrderItem`

				
				
					

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
| orderId | **Type** string **Description** Required. ID of the order. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** ID of the request to create an asset. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Create or Update Asset From Order Item
							action.

						

```
{
    "inputs": [
        {
            "orderItemIds": ["802SG000002HixxYAC"]
        }
    ]
}
```

						

This sample response is for the Create or Update Asset From Order Item
							action.

						

```
{
  "actionName": "createOrUpdateAssetFromOrderItem",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "requestId": "b2a2b4b9-845b-4078-980a-759308389604"
  },
  "version": 1
}
```

=== ARTICLE: actions_obj_deep_clone_sales_transaction.htm ===
---
page_id: actions_obj_deep_clone_sales_transaction.htm
title: Deep Clone Sales Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_deep_clone_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone Sales Transaction

Clone a quote or an order, including full object graph with related
			objects, selected lines, or selected groups.

		
			

This action is available in API version 67.0 and later.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/deepCloneSalesTransaction`

				
				
					

**Formats**

					
: JSON, XML

				
				
					

**HTTP Methods**

					
: POST

				
				
					

**Authentication**

					
: `Authorization: Bearer token`

				
			

		

		

## Inputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Input | Details |
| --- | --- |
| options | **Type** Apex-defined **Description** Specifies options to clone a ramp segment within a sales transaction. You can clone only the last ramp segment. Valid values are: `recordTypeId`—ID of the record type related to the record to clone. Optional. `lineScope`—Specifies the scope for cloning a ramp segment. This property determines which line items must be cloned and added to the cloned segment. You can specify these options. `AllLines`—Specifies whether all line items in a ramped group must be cloned. `RampedLinesOnly`—Specifies whether only the ramped line items must be cloned. A segment identifier is created for the newly cloned line items, ensuring date continuity between the existing and cloned segment. |
| recordIds | **Type** List<String> **Description** Required. ID of the record to be cloned. You can specify a single record ID only. |
| salesTransactionId | **Type** String **Description** Required. ID of the sales transaction related to the record IDs to clone. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| newRecordId | **Type** String **Description** ID of the cloned sales transaction. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

Here’s a sample request for the Deep Clone Sales Transaction action.

						

```
{
  "inputs": [
    {
      "recordIds": ["0QLxx0000004CBYGA2"],
      "salesTransactionId": "0Q0xx0000004CE0CAM",
      "options": {
        "lineScope": "AllLines"
      }
    }
  ]
}
```

					

					
: 
						

Here’s a sample response for the Deep Clone Sales Transaction action.

						

```
{
  "actionName": "deepCloneSalesTransaction",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "newRecordId": "0Q0SG000000ACxf0AG"
  }
}
```

=== ARTICLE: actions_obj_get_renewable_assets_summary.htm ===
---
page_id: actions_obj_get_renewable_assets_summary.htm
title: Get Renewable Assets Summary Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_renewable_assets_summary.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Renewable Assets Summary Action

Retrieve details about renewable assets in a given order. You can
            use this information to create renewal opportunities.

        

This action gets pricing data from the OrderEntitiesMapping context mapping
                within the SalesTransactionContext context definition. Before you use this action,
                edit the context mapping to map the objects and fields used in your pricing
                procedure to the nodes and attributes in the context definition.

This action
                doesn’t support providing a summary with procedure plans. As a result, renewal line
                items may return a price of zero.

#### Note

We recommend adding the same fields and
                mappings for the Quote and Order objects, and for the Quote Line Item and Order
                Product objects.

This action is available in API version 64.0 and
                later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/getRenewableAssetsSummary`

                
                
                    

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
| orderId | **Type** id **Description** Required. ID of the order related to the assets to check for renewal opportunities. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| renewableAssetsSummary | **Type** Apex-defined **Description** Summary of the assets associated with the order, including details about renewal opportunities such as renewal pricing information. See [renew_assets_summary Apex Namespace](./apex_namespace_renew_assets_summary.htm.md). |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Get Renewable Assets Summary action.

                        

```
{
  "inputs": [
    {
      "orderId": "801xx000003GZ39AAG"
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Get Renewable Assets Summary action.

                        

```
[
  {
    "actionName": "getRenewableAssetsSummary",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "renewableAssetsSummary": [
        {
          "startDate": "2025-07-22",
          "rootAssetOpportunity": null,
          "renewalPriceDetails": [
            {
              "quantity": 1,
              "netUnitPrice": 0
            }
          ],
          "productId": "01txx0000006i3DAAQ",
          "priceBookId": "01sxx0000005ptpAAA",
          "priceBookEntryId": "01uxx0000008yXCAAY",
          "orderItem": "802xx000001nb1LAAQ",
          "opportunityProductId": null,
          "lastAssetActionSubtype": null,
          "lastAssetAction": "Initial Sale",
          "endDate": "2025-08-21",
          "assetId": "02ixx0000004HKwAAM",
          "account": "001xx000003GZ1XAAW"
        }
      ]
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_initiate_rollback_last_action.htm ===
---
page_id: actions_obj_initiate_rollback_last_action.htm
title: Initiate Rollback on Last Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_initiate_rollback_last_action.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Rollback on Last Action

Initiate the reversal of the last action on an asset to rectify any
            transactional errors or to meet changing business requirements.

        

Use this action to revert the last amendment or renewal on a particular asset,
                restoring the asset to its previous state. This action creates a quote or an order
                based on the specified output type. Use the created reversal quote to verify the
                reversal and convert the quote into an order.

Keep these considerations in
                mind when you use this action.

                
- You can roll back only future dated transactions.

                
- Rollback action isn't supported for legacy assets.

                
- The rollback operation is supported for amendment and renewal only.

            

This action is available in API version 65.0 and later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/initiateRollBackLastAction`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| assetIds | **Type** string **Description** Required. List of asset IDs to include in the last action rollback. |
| outputType | **Type** string **Description** Required. The type of record to create for reversal. Valid values are: `Quote`—Creates a reversal quote. `Order`—Creates a reversal order. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| recordId | **Type** id **Description** The ID of the created quote or order. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This example shows a sample request that initiates the rollback action on
                            an asset and converts it into a quote.

                        

```
{
  "inputs": [
    {
      "assetIds": [
        "02iDU0000006UisYAE"
      ],
      "outputType": "Quote"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
{
  "actionName": "initiateRollBackLastAction",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "recordId": "0Q0xx0000004NsSCAU"
  },
  "version": 1
}
```

=== ARTICLE: actions_obj_initiate_transfer.htm ===
---
page_id: actions_obj_initiate_transfer.htm
title: Initiate Transfer Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_initiate_transfer.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Transfer Action

Transfer an asset or multiple assets from one account to
            another.

        
            

Keep these considerations in mind when you use this invocable action.

            
                
- This action generates 2 quotes or 2 orders.

                
- One transaction is considered the source, which is used to calculate the
                    reduction amount of the transfer. The other transaction is the target, which is
                    used to calculate the new amount on the target account. 

                
- The quantity on the source is negative, which reduces the existing asset's
                    quantity. The quantity on the target is positive, which creates a new asset on
                    the target account.

                
- You can change the quantity on the source or the target, but the quantities must
                    be equal and opposite. For example, the source quote line can have a quantity
                    value as `-5`, and the target quote line can
                    have a quantity value `5`. If you change the
                    source value to `-10`, you must update the
                    target value to `10`. You must update quotes
                    or orders manually.

                
- The transfer is complete after the orders are assetized.

            

            

This action is available in API version 65.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/initiateTransfer`

                
                
                    

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| outputRecordType | **Type** string **Description** Required. Specifies either a quote or order record type that’s being transferred. |
| shouldSkipPricing | **Type** boolean **Description** Indicates whether to skip pricing at the time of asset transfer (`true`) or not (`false`). |
| targetAccountId | **Type** string **Description** Required. The ID of the target account where the asset is transferred. |
| targetContractId | **Type** string **Description** The ID of the target contract that’s associated with the asset that’s being transferred. |
| transferDate | **Type** datetime **Description** Required. The date of the asset transfer. |
| transferRecords | **Type** Apex-defined **Description** Required. A collection of Apex `connectapi__TransferRecordInputRepresentation` records that contain details about the assets to be transferred. See [ConnectApi.TransferRecordInputRepresentation](./apex_connectapi_input_transfer_record.htm.md). |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| assetTransferSourceId | **Type** id **Description** The ID of the quote or order that’s related to the source account used to start the transfer. |
| assetTransferTargetId | **Type** id **Description** The ID of the quote or order that’s related to the target account used to start the transfer. |
| requestIdentifier | **Type** id **Description** The request ID can be used to track the async request. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample input to call this invocable action.

                        

```
{
  "inputs": [
    {
      "transferRecords": [
        {
          "assetId": "02ixx0000004HZbAAM",
          "transferQuantity": 1
        }
      ],
      "transferDate": "2025-10-21T00:00:00.000Z",
      "targetAccountId": "001xx000003GbeXAAS",
      "targetContractId": "800DU0000000lZlYAI",
      "outputRecordType": "Quote"
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
ConnectApi.TransferRecordInputRepresentation transferRecord = new ConnectApi.TransferRecordInputRepresentation();
transferRecord.assetId = '02ixx0000004HHjAAM';
transferRecord.transferQuantity = 1;
List<ConnectApi.TransferRecordInputRepresentation> transferRecords = new List<ConnectApi.TransferRecordInputRepresentation>();
transferRecords.add(transferRecord);

Invocable.Action action = Invocable.Action.createStandardAction('initiateTransfer');
action.setInvocationParameter('transferRecords', transferRecords);
action.setInvocationParameter('targetAccountId', '001xx000003GYiHAAW');
action.setInvocationParameter('transferDate', '2025-03-01T00:00:00.000Z');
action.setInvocationParameter('outputRecordType', 'Quote');
List<Invocable.Action.Result> results = action.invoke();
System.assertEquals(true, results[0].isSuccess());
Assert.isNotNull(results[0].getOutputParameters().get('assetTransferSourceId'));
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "initiateTransfer",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "assetTransferSourceId": "0Q0DU0000006SYF0A2",
      "assetTransferTargetId": "0Q0DU0000006SYE0A2"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_renew_assets.htm ===
---
page_id: actions_obj_renew_assets.htm
title: Initiate Renewal Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_renew_assets.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Renewal Action

Initiate and execute the renewal of an asset.

		

Specify the IDs of the assets that you want to add to renew by specifying a start date. You can
				also specify the type of renewal record that you want to create, such as a quote or
				an order.

This action is available in API version 60.0 and
			later.

		
		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/initiateRenewal`

				
				
					

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

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

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
| rampOptionsDetails | **Type** Apex-defined **Description** An Apex RampOptionInputRepresentation record that contains the details of ramp options. The details include segment type, duration, and segment count. Specify this property if you want to include assets in a group ramp with a ramp schedule. See [RampOptionInputRepresentation](./apex_connectapi_input_ramp_option.htm.md) to refer to the associated properties for ramp options. Available in API version 67.0 and later. |
| renewAssetIds | **Type** string **Description** Required. The IDs of the assets that you want to renew. |
| renewContractId | **Type** string **Description** ID of the contract record to sync with the renewal quote. |
| renewEndDate | **Type** datetime **Description** Effective end date of the renewal. Available in API version 62.0 and later. |
| renewOpportunityId | **Type** string **Description** ID of the Opportunity record to sync with the renewal quote. |
| renewOutputType | **Type** string **Description** Required. Type of renewal record to create such as a quote or an order. |
| renewStartDate | **Type** datetime **Description** Optional Effective start date of the renewal. Required for early asset renewals and renewing expired assets, by using today’s date or a future date. Available in API version 62.0 and later. |
| skipPricing | **Type** boolean **Description** Indicates whether the pricing procedure must be skipped (`true`) or performed (`false`). Available in API version 64.0 and later. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| renewRecordId | **Type** string **Description** The ID of the amendment record that’s created. |
| requestIdentifier | **Type** string **Description** Request ID that’s used to track the async request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This sample request is for the Initiate Renewal action.

						

```
{
  "inputs": [
    {
      "rampOptionsDetails": {
        "segmentType": "Custom",
        "duration": 40,
        "numberOfSegments": 10
      },
      "renewAssetIds": [
        "02ixx0000004LMwAAM"
      ],
      "renewOutputType": "Quote",
      "renewContractId": "800DU0000000lZlYAI",
      "renewOpportunityId": "006DU0000025AanYAE",
      "renewStartDate": "2023-10-21T00:00:00.000Z",
      "renewEndDate": "2024-10-21T00:00:00.000Z",
      "skipPricing": false
    }
  ]
}
```

						

This sample response is for the Initiate Renewal action.

						

```
[
    {
        "actionName": "initiateRenewal",
        "errors": null,
        "isSuccess": true,
        "outputValues": {
            "renewRecordId": "0Q0xx0000004P32CAE",
            "requestIdentifier": "16Pxx0000004OTY"
        },
        "version": 1
    }
]
```

=== ARTICLE: apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm ===
---
page_id: apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm
title: ConfigurationOptionsInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationOptionsInput Class

Contains methods and properties to set the configuration options for the input to the
    product configurator.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

## Usage

      

This class holds the required details of the product configuration input. Set the class
        properties to enable default configuration, execution of configuration rules, and validation
        of the product catalog. Use these class properties as an input to the [PlaceSalesTransactionExecutor](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor) class method.

## Example

      

```
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test', listOfRecords);
    RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
    RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
    RevSalesTrxn.ConfigurationOptionsInput cInput = new RevSalesTrxn.ConfigurationOptionsInput();
    cInput.addDefaultConfiguration = true;
    cInput.executeConfigurationRules = true;
    cInput.validateAmendRenewCancel = true;
    cInput.validateProductCatalog = true;
        //Place Sales Transaction API Call
     RevSalesTrxn.PlaceSalesTransactionResponse resp = PlaceQuote.PlaceSalesTransactionExecutor.execute(graph,pricingPrefEnum,configurationExecutionEnum,cInput,null);
```

- 
**[ConfigurationOptionsInput Properties](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_properties)**  

Set the ConfigurationOptionsInput class properties to add default configuration,     execute configuration rules, and validate the product catalog.

- 
**[ConfigurationOptionsInput Methods](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_methods)**  

Learn more about the methods available with the ConfigurationOptionsInput     class.

  

## ConfigurationOptionsInput Properties

  
  
  
Set the ConfigurationOptionsInput class properties to add default configuration,
    execute configuration rules, and validate the product catalog.

    
      

The `ConfigurationOptionsInput` class includes these
        properties.

    

    
  

- 
**[addDefaultConfiguration](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_addDefaultConfiguration)**  

Sets the default product configuration, such as bundle and product attributes, for a     quote request.

- 
**[executeConfigurationRules](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_executeConfigurationRules)**  

Sets the requirement for a quote to adhere to the configuration rules.

- 
**[validateAmendRenewCancel](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_validateAmendRenewCancel)**  

Sets the requirement to run validations related to amend, renew, or cancel     processes.

- 
**[validateProductCatalog](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_validateProductCatalog)**  

Sets the requirement to validate a quote against the product catalog.

### addDefaultConfiguration

Sets the default product configuration, such as bundle and product attributes, for a
    quote request.

#### Signature

`public Boolean addDefaultConfiguration {get; set;}`

#### Property Value

Type: Boolean

Indicates whether
        to automatically add default configuration to the order (`true`) or not (`false`).

### executeConfigurationRules

Sets the requirement for a quote to adhere to the configuration rules.

#### Signature

`public Boolean executeConfigurationRules {get; set;}`

#### Property Value

Type: Boolean

      

Indicates whether the order must adhere to configuration rules during processing (`true`) or bypass them (`false`).

### validateAmendRenewCancel

Sets the requirement to run validations related to amend, renew, or cancel
    processes.

#### Signature

`public Boolean validateAmendRenewCancel {get; set;}`

#### Property Value

Type: Boolean

Indicates whether
        to run validations related to amend, renew, or cancel processes (`true`) or not (`false`).

### validateProductCatalog

Sets the requirement to validate a quote against the product catalog.

#### Signature

`public Boolean validateProductCatalog {get; set;}`

#### Property Value

Type: Boolean

      

Indicates whether the quote must be validated against the product catalog (`true`) or not (`false`).

  

## ConfigurationOptionsInput Methods

  
  
  
Learn more about the methods available with the ConfigurationOptionsInput
    class.

    
      

The `ConfigurationOptionsInput` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_equals)**  

Determines the equality of external objects in a list. This method is dynamic and is     based on the equals() method in Java.

- 
**[hashCode()](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_hashCode)**  

Determines the uniqueness of the external object records in a list.

- 
**[toString()](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_RevSalesTrxn_ConfigurationOptionsInput_toString)**  

Converts a value to a string.

### equals(obj)

Determines the equality of external objects in a list. This method is dynamic and is
    based on the equals() method in Java.

#### Signature

`public Boolean equals(Object obj)`

#### Parameters

**obj**

: Type: Object

          
: Reference object that’s used to compare with the class object.

#### Return Value

Type: Boolean

      

Indicates if the class object is same as the reference object (`true`) or not (`false`).

### hashCode()

Determines the uniqueness of the external object records in a list.

#### Signature

`public Integer hashCode()`

#### Return Value

Type: Integer

      

Integer hash code that represents the value of the object. Equal objects as per the `equals()` method must return the same hash code.

### toString()

Converts a value to a string.

#### Signature

`public String toString()`

#### Return Value

Type: String

=== ARTICLE: apex_class_RevSalesTrxn_GraphRequest.htm ===
---
page_id: apex_class_RevSalesTrxn_GraphRequest.htm
title: GraphRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_GraphRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GraphRequest Class

Contains constructors and properties to set the graph ID and a list of records to be
    ingested. The list of records is specified in a key-value map format that contains field
    values.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

- 
**[GraphRequest Constructors](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_RevSalesTrxn_GraphRequest_constructors)**  

Learn more about the available constructors with the GraphRequest class.

- 
**[GraphRequest Properties](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_RevSalesTrxn_GraphRequest_properties)**  

Learn more about the available properties with the GraphRequest class.

  

## GraphRequest Constructors

  
  
  
Learn more about the available constructors with the GraphRequest class.

    
      

The `GraphRequest` class includes these constructors.

    

    
  

- 
**[GraphRequest(graphId, records)](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_RevSalesTrxn_GraphRequest_ctor)**  

Creates an instance of the GraphRequest class to assign the graph ID and a list of     records to be ingested.

### GraphRequest(graphId, records)

Creates an instance of the GraphRequest class to assign the graph ID and a list of
    records to be ingested.

#### Signature

`public GraphRequest(String graphId,
          List<RevSalesTrxn.RecordWithReferenceRequest> records)`

#### Parameters

**graphId**

: Type: String

: ID of the graph.

**records**

: Type: List<[revsalestrxn.RecordWithReferenceRequest](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_class_RevSalesTrxn_RecordWithReferenceRequest)>

          
: List of records to be ingested.

## GraphRequest Properties

  
Learn more about the available properties with the GraphRequest class.

The `GraphRequest` class includes these properties.

- 
**[graphId](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_RevSalesTrxn_GraphRequest_graphId)**  

Set the `graphId` property to assign the ID value of     the graph.

### graphId

  
Set the `graphId` property to assign the ID value of
    the graph.

#### Signature

`public String graphId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm ===
---
page_id: apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm
title: PlaceSalesTransactionException Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceSalesTransactionException Class

Contains methods to hold the exception details for the place sales transaction
    request.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

- 
**[PlaceSalesTransactionException Methods](./apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionException_methods)**  

Learn more about the methods available with the PlaceSalesTransactionException     class.

  

## PlaceSalesTransactionException Methods

  
  
  
Learn more about the methods available with the PlaceSalesTransactionException
    class.

    
      

The `PlaceSalesTransactionException` class includes these
        methods.

    

    
  

- 
**[getErrorCode()](./apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionException_getErrorCode)**  

Gets the error code that’s associated to the place sales transaction request.

### getErrorCode()

Gets the error code that’s associated to the place sales transaction request.

#### Signature

`public String getErrorCode()`

#### Return Value

Type: String

=== ARTICLE: apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm ===
---
page_id: apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm
title: PlaceSalesTransactionExecutor Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# PlaceSalesTransactionExecutor Class

  
  
  
Contains methods to place a sales transaction with details of the graph request,
    pricing preferences, and configuration options.

    

## Namespace

      
      

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

    

    
    
  

- 
**[PlaceSalesTransactionExecutor Methods](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_methods)**  

Learn more about the methods available with the `PlaceSalesTransactionExecutor` class.

- 
**[PlaceSalesTransactionExecutor Example Implementation](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_example_implementation)**  

To place a sales transaction from Apex, refer to the example implementation of the             `PlaceSalesTransactionExecutor` class.

  

## PlaceSalesTransactionExecutor Methods

  
  
  
Learn more about the methods available with the `PlaceSalesTransactionExecutor` class.

    
      

The `PlaceSalesTransactionExecutor` class includes these
        methods.

    

    
  

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationExecutionEnum, configuratorOptions, contextId)](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_execute)**  

Use the method in the `PlaceSalesTransactionExecutor`     class to execute the Place Sales Transaction Apex API request by assigning the properties for     graph request, pricing references, and configurator options.

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationExecutionEnum, configuratorOptions, contextId, catalogRatesPreferenceEnum)](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_execute_1)**  

Use the method in the `PlaceSalesTransactionExecutor`     class to execute the Place Sales Transaction Apex API request by assigning the properties for     graph request, pricing references, configurator options, and catalog rates.

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationExecutionEnum, configuratorOptions, contextId, catalogRatesPreferenceEnum, taxPreferenceEnum, persistPreferenceEnum)](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_execute_2)**  

Use the method in the `PlaceSalesTransactionExecutor`     class to execute the Place Sales Transaction Apex API request by assigning the properties for     graph request, pricing and tax preferences, configurator options, and catalog rates.

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationExecutionEnum, configuratorOptions, contextId, taxPreferenceEnum, persistPreferenceEnum, groupRampActionEnum)](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_execute_3)**  

Use the method in the `PlaceSalesTransactionExecutor`     class to execute the Place Sales Transaction Apex API request by assigning the properties for     graph request, pricing and tax preferences, configurator options, persist preference, and group ramp action.

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationExecutionEnum, configuratorOptions, contextId, catalogRatesPreferenceEnum, taxPreferenceEnum, persistPreferenceEnum, groupRampActionEnum)](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionExecutor_execute_4)**  

Use the method in the `PlaceSalesTransactionExecutor`     class to execute the Place Sales Transaction Apex API request by assigning the properties for     graph request, pricing and tax preferences, configurator options, catalog rates, persist preference, and group ramp action.

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationExecutionEnum, configuratorOptions, contextId)

  
  
  
Use the method in the `PlaceSalesTransactionExecutor`
    class to execute the Place Sales Transaction Apex API request by assigning the properties for
    graph request, pricing references, and configurator options.

    

#### Signature

      
      

`public static revsalestrxn.PlaceSalesTransactionResponse
          execute(revsalestrxn.GraphRequest graphRequest, revsalestrxn.PricingPreferenceEnum
          pricingPreferenceEnum, revsalestrxn.ConfigurationExecutionEnum configurationExecutionEnum,
          revsalestrxn.ConfiguratorOptions configuratorOptions, revsalestrxn.ContextId
          contextId)`

      
    

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [revsalestrxn.GraphRequest](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [revsalestrxn.PricingPreferenceEnum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the sales transaction process.

        
        
          

**configurationExecutionEnum**

          
: Type: [revsalestrxn.ConfigurationExecutionEnum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)

          
: Configuration method for the sales transaction request.

        
        
          

**configuratorOptions**

          
: Type: [revsalestrxn.ConfigurationOptionsInput](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)

          
: Configuration options during the creation of the sales transaction.

        
        
          

**contextId**

          
: Type: String

          
: Context ID to assign to the sales transaction.

        
      

    

    

#### Return Value

      
      

Type: [revsalestrxn.PlaceSalesTransactionResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)

    

  

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationExecutionEnum, configuratorOptions, contextId,
      catalogRatesPreferenceEnum)

  
  
  
Use the method in the `PlaceSalesTransactionExecutor`
    class to execute the Place Sales Transaction Apex API request by assigning the properties for
    graph request, pricing references, configurator options, and catalog rates.

    

#### Signature

[Usage Selling](https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_sellling.htm&language=en_US) must be enabled
        to use this signature.

`public static
          revsalestrxn.PlaceSalesTransactionResponse execute(revsalestrxn.GraphRequest graphRequest,
          revsalestrxn.PricingPreferenceEnum pricingPreferenceEnum,
          revsalestrxn.ConfigurationExecutionEnum configurationExecutionEnum,
          revsalestrxn.ConfiguratorOptions configuratorOptions, revsalestrxn.ContextId contextId,
          revsalestrxn.CatalogRatesPreferenceEnum
      catalogRatesPreferenceEnum)`

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [revsalestrxn.GraphRequest](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [revsalestrxn.PricingPreferenceEnum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the sales transaction process.

        
        
          

**configurationExecutionEnum**

          
: Type: [revsalestrxn.ConfigurationExecutionEnum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)

          
: Configuration method for the sales transaction request.

        
        
          

**configuratorOptions**

          
: Type: [revsalestrxn.ConfigurationOptionsInput](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)

          
: Configuration options during the creation of the sales transaction.

        
        
          

**contextId**

          
: Type: String

          
: Context ID to assign to the sales transaction.

        
        
          

**catalogRatesPreferenceEnum**

          
: Type: [revsalestrxn.CatalogRatesPreferenceEnum](./apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm.md)

          
: Rate card entries defined in the catalog that must be fetched for quote line items,
            with usage-based selling during the place sales transaction process.

        
      

    

    

#### Return Value

      
      

Type: [revsalestrxn.PlaceSalesTransactionResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)

    

  

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationExecutionEnum, configuratorOptions, contextId, catalogRatesPreferenceEnum,
      taxPreferenceEnum, persistPreferenceEnum)

  
  
  
Use the method in the `PlaceSalesTransactionExecutor`
    class to execute the Place Sales Transaction Apex API request by assigning the properties for
    graph request, pricing and tax preferences, configurator options, and catalog rates.

    

#### Signature

      
      

[Usage Selling](https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_sellling.htm&language=en_US) must be enabled
        to use this signature.

      

`public static revsalestrxn.PlaceSalesTransactionResponse
          execute(revsalestrxn.GraphRequest graphRequest, revsalestrxn.PricingPreferenceEnum
          pricingPreferenceEnum, revsalestrxn.ConfigurationExecutionEnum configurationExecutionEnum,
          revsalestrxn.ConfiguratorOptions configuratorOptions, revsalestrxn.ContextId contextId,
          revsalestrxn.CatalogRatesPreferenceEnum catalogRatesPreferenceEnum,
          revsalestrxn.TaxPreferenceEnum taxPreferenceEnum, revsalestrxn.PersistPreferenceEnum
          persistPreferenceEnum)`

      
    

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [revsalestrxn.GraphRequest](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [revsalestrxn.PricingPreferenceEnum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the sales transaction process.

        
        
          

**configurationExecutionEnum**

          
: Type: [revsalestrxn.ConfigurationExecutionEnum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)

          
: Configuration method for the sales transaction request.

        
        
          

**configuratorOptions**

          
: Type: [revsalestrxn.ConfigurationOptionsInput](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)

          
: Configuration options during the creation of the sales transaction.

        
        
          

**contextId**

          
: Type: String

          
: Context ID to assign to the sales transaction.

        
        
          

**catalogRatesPreferenceEnum**

          
: Type: [revsalestrxn.CatalogRatesPreferenceEnum](./apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm.md)

          
: Rate card entries defined in the catalog that must be fetched for quote line items,
            with usage-based selling during the place sales transaction process.

        
        
          

**taxPreferenceEnum**

          
: Type: [revsalestrxn.taxPreferenceEnum](./apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm.md)

          
: Tax preference during the sales transaction process. Available in API version 65.0 and
            later.

        
        
          

**persistPreferenceEnum**

          
: Type: [revsalestrxn.persistPreferenceEnum](./apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm.md)

          
: Persist preference during the sales transaction process. Available in API version 65.0
            and later.

        
      

    

    

#### Return Value

      
      

Type: [revsalestrxn.PlaceSalesTransactionResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)

    

  

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationExecutionEnum, configuratorOptions, contextId, taxPreferenceEnum,
      persistPreferenceEnum, groupRampActionEnum)

  
  
  
Use the method in the `PlaceSalesTransactionExecutor`
    class to execute the Place Sales Transaction Apex API request by assigning the properties for
    graph request, pricing and tax preferences, configurator options, persist preference, and group ramp action.

    

#### Signature

      
      

`public static revsalestrxn.PlaceSalesTransactionResponse
          execute(revsalestrxn.GraphRequest graphRequest, revsalestrxn.PricingPreferenceEnum
          pricingPreferenceEnum, revsalestrxn.ConfigurationExecutionEnum configurationExecutionEnum,
          revsalestrxn.ConfiguratorOptions configuratorOptions, revsalestrxn.ContextId contextId,
          revsalestrxn.TaxPreferenceEnum taxPreferenceEnum, revsalestrxn.PersistPreferenceEnum
          persistPreferenceEnum, revsalestrxn.GroupRampActionEnum groupRampActionEnum)`

      
    

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [revsalestrxn.GraphRequest](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [revsalestrxn.PricingPreferenceEnum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the sales transaction process.

        
        
          

**configurationExecutionEnum**

          
: Type: [revsalestrxn.ConfigurationExecutionEnum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)

          
: Configuration method for the sales transaction request.

        
        
          

**configuratorOptions**

          
: Type: [revsalestrxn.ConfigurationOptionsInput](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)

          
: Configuration options during the creation of the sales transaction.

        
        
          

**contextId**

          
: Type: String

          
: Context ID to assign to the sales transaction.

        
        
          

**taxPreferenceEnum**

          
: Type: [revsalestrxn.taxPreferenceEnum](./apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm.md)

          
: Tax preference during the sales transaction process. Available in API version 65.0 and
            later.

        
        
          

**persistPreferenceEnum**

          
: Type: [revsalestrxn.persistPreferenceEnum](./apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm.md)

          
: Persist preference during the sales transaction process. Available in API version 65.0
            and later.

        
        
          

**groupRampActionEnum**

          
: Type: [revsalestrxn.GroupRampActionEnum](./apex_enum_RevSalesTrxn_GroupRampActionEnum.htm.md)

          
: Specifies the action that you want to perform on group ramp segments.

        
      

    

    

#### Return Value

      
      

Type: [revsalestrxn.PlaceSalesTransactionResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)

    

  

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationExecutionEnum, configuratorOptions, contextId, catalogRatesPreferenceEnum,
      taxPreferenceEnum, persistPreferenceEnum, groupRampActionEnum)

  
  
  
Use the method in the `PlaceSalesTransactionExecutor`
    class to execute the Place Sales Transaction Apex API request by assigning the properties for
    graph request, pricing and tax preferences, configurator options, catalog rates, persist preference, and group ramp action.

    

#### Signature

      
      

[Usage Selling](https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_sellling.htm&language=en_US) must be enabled to use this signature.

      

`public static revsalestrxn.PlaceSalesTransactionResponse
          execute(revsalestrxn.GraphRequest graphRequest, revsalestrxn.PricingPreferenceEnum
          pricingPreferenceEnum, revsalestrxn.ConfigurationExecutionEnum configurationExecutionEnum,
          revsalestrxn.ConfiguratorOptions configuratorOptions, revsalestrxn.ContextId contextId,
          revsalestrxn.CatalogRatesPreferenceEnum catalogRatesPreferenceEnum,
          revsalestrxn.TaxPreferenceEnum taxPreferenceEnum, revsalestrxn.PersistPreferenceEnum
          persistPreferenceEnum, revsalestrxn.GroupRampActionEnum groupRampActionEnum)`

      
    

    

#### Parameters

      
      
        

**graphRequest**

: Type: [revsalestrxn.GraphRequest](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)

: The sObject graph values of the order payload to be ingested.

        

**pricingPreferenceEnum**

: Type: [revsalestrxn.PricingPreferenceEnum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)

: Pricing preference during the sales transaction process.

        

**configurationExecutionEnum**

: Type: [revsalestrxn.ConfigurationExecutionEnum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)

: Configuration method for the sales transaction request.

        

**configuratorOptions**

: Type: [revsalestrxn.ConfigurationOptionsInput](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)

: Configuration options during the creation of the sales transaction.

        

**contextId**

: Type: String

: Context ID to assign to the sales transaction.

        

**catalogRatesPreferenceEnum**

: Type: [revsalestrxn.CatalogRatesPreferenceEnum](./apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm.md)

: Rate card entries defined in the catalog that must be fetched for quote line items, with usage-based selling during the place sales transaction process.

        

**taxPreferenceEnum**

: Type: [revsalestrxn.taxPreferenceEnum](./apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm.md)

: Tax preference during the sales transaction process. Available in API version 65.0 and later.

        

**persistPreferenceEnum**

: Type: [revsalestrxn.persistPreferenceEnum](./apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm.md)

: Persist preference during the sales transaction process. Available in API version 65.0 and later.

        

**groupRampActionEnum**

: Type: [revsalestrxn.GroupRampActionEnum](./apex_enum_RevSalesTrxn_GroupRampActionEnum.htm.md)

: Specifies the action that you want to perform on group ramp segments.

      

    

    

#### Return Value

      
      

Type: [revsalestrxn.PlaceSalesTransactionResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)

    

  

    

## PlaceSalesTransactionExecutor Example Implementation

    
    
    
To place a sales transaction from Apex, refer to the example implementation of the
            `PlaceSalesTransactionExecutor` class.

        

### Namespace

            
            

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

        

        

### Usage

            
            

Customize this example to suit your requirements. Create the list of records to be
                ingested by using these steps. Replace the respective IDs with the values that are
                present in your org. For example, replace the value of `${Pricebook2Id}` field with the price book ID that’s present in the
                org.

        

        

### Example

This example shows a sample request to create a sales transaction, update a quote with a quote
                line item, delete a quote line item, or skip or persist pricing changes. It includes
                these steps.

            
                
- Set up a quote and quote line item.

                
- To create a quote line relationship, create an instance of the `RecordResource` class. To create an object with
                    its fields, specify the object that you want to create by using POST method.
                    Create a map of the fields and its values by using put(key, value) operation.
                    Assign this field map to the record object.

                
- To update an object's specific fields, specify the object you want to update by
                    using the PATCH method along with the ID of the object. Create a map of the
                    fields and its values by using put(key, value) operation. Only certain fields on
                    an object can be updated. Add the fields that you want to update to the map.
                    Assign this field map to the record object.

                
- To associate the Record object with a reference identifier, create an instance
                    of the `RecordWithReferenceRequest` class.

                
- To contain all record objects, create an instance of the `GraphRequest` class.

            

```
public class PlaceSalesTransactionTest {
    public static void callPSTAPI_Post() {
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
        
        //Quote setup
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'POST');
        Map<String,Object> quoteFieldValues = new Map<String,Object>();
        quoteFieldValues.put('Name','q-ap12');
        quoteFieldValues.put('OpportunityId','006xx000001a3e8AAA');
        quoteFieldValues.put('Pricebook2Id','01sDU000000JRX8YAO');
        quoteRecord.fieldValues = quoteFieldValues;
        
        //Quote line item setup
        
        //1st quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord1 = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
        quoteLineItemFieldValues.put('Product2Id','01txx0000006i7JAAQ');
        quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008yc6AAA');
        quoteLineItemFieldValues.put('Quantity','2.0');
        quoteLineItemFieldValues.put('UnitPrice','1000');
        quoteLineItemFieldValues.put('StartDate','2025-03-15');
        quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord1.fieldValues = quoteLineItemFieldValues;
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords1 = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem1',quoteLineItemRecord1);
        
        //2nd quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord2 = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues2 = new Map<String,Object>();
        quoteLineItemFieldValues2.put('Product2Id','01txx0000006i7RAAQ');
        quoteLineItemFieldValues2.put('PricebookEntryId','01uxx0000008ybvAAA');
        quoteLineItemFieldValues2.put('Quantity','2.0');
        quoteLineItemFieldValues2.put('UnitPrice','7.0');
        quoteLineItemFieldValues2.put('StartDate','2025-03-15');
        quoteLineItemFieldValues2.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord2.fieldValues = quoteLineItemFieldValues2;
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords2 = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem2',quoteLineItemRecord2);
        
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords1);
        listOfRecords.add(quoteLineItemRecords2);
        
        
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test',listOfRecords);
        System.debug(graph);
        
        //Place sales transaction API call - There are different executor signatures detailed in the documentation
        RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null, null, null, null);
        //If you do not have Usage Based Selling Feature, you can use the signatures without catalog rates enum
        //RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null);
        System.debug(resp);
    }
    
    public static void callPSTAPI_Post_Skip_Tax_Skip_Persist() {
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
        RevSalesTrxn.TaxPreferenceEnum taxPrefEnum = RevSalesTrxn.TaxPreferenceEnum.SKIP;
        RevSalesTrxn.PersistPreferenceEnum persistPrefEnum = RevSalesTrxn.PersistPreferenceEnum.SKIP;
        
        //Quote setup
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'POST');
        Map<String,Object> quoteFieldValues = new Map<String,Object>();
        quoteFieldValues.put('Name','q-ap12');
        quoteFieldValues.put('OpportunityId','006xx000001a3e8AAA');
        quoteFieldValues.put('Pricebook2Id','01sDU000000JRX8YAO');
        quoteRecord.fieldValues = quoteFieldValues;
        
        //Quote line item setup
        
        //1st quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord1 = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
        quoteLineItemFieldValues.put('Product2Id','01txx0000006i7JAAQ');
        quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008yc6AAA');
        quoteLineItemFieldValues.put('Quantity','2.0');
        quoteLineItemFieldValues.put('UnitPrice','1000');
        quoteLineItemFieldValues.put('StartDate','2025-03-15');
        quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord1.fieldValues = quoteLineItemFieldValues;
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords1 = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem1',quoteLineItemRecord1);
        
        //2nd quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord2 = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues2 = new Map<String,Object>();
        quoteLineItemFieldValues2.put('Product2Id','01txx0000006i7RAAQ');
        quoteLineItemFieldValues2.put('PricebookEntryId','01uxx0000008ybvAAA');
        quoteLineItemFieldValues2.put('Quantity','2.0');
        quoteLineItemFieldValues2.put('UnitPrice','7.0');
        quoteLineItemFieldValues2.put('StartDate','2025-03-15');
        quoteLineItemFieldValues2.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord2.fieldValues = quoteLineItemFieldValues2;
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords2 = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem2',quoteLineItemRecord2);
        
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords1);
        listOfRecords.add(quoteLineItemRecords2);
        
        
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test',listOfRecords);
        System.debug(graph);
        
        //Place sales transaction API call
        RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null, null, taxPrefEnum, persistPrefEnum);
        System.debug(resp);
    }
    
    public static void callPSTAPI_Patch() {
        
        // Apex test to update a quote with a quote line item
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
        
        //Quote setup
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'PATCH','0Q0xx0000004CYsCAM');
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        
        //Quote line item setup
        //New quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
        quoteLineItemFieldValues.put('Product2Id','01txx0000006i7KAAQ');
        quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008ycFAAQ');
        quoteLineItemFieldValues.put('Quantity','2.0');
        quoteLineItemFieldValues.put('UnitPrice','7.0');
        quoteLineItemFieldValues.put('StartDate','2025-03-15');
        quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord.fieldValues = quoteLineItemFieldValues;
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem',quoteLineItemRecord);
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords);
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test', listOfRecords);
        
        //Place sales transaction API call
        RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null, null, null, null);
        System.debug(resp);
    }

    public static void callPSTAPI_Patch_Skip_Config_Skip_Pricing() {
        
        // Apex test to update a quote with a quote line item
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SKIP;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SKIP;
        
        //Quote setup
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'PATCH','0Q0xx0000004CYsCAM');
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        
        //Quote line item setup
        //New quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
        quoteLineItemFieldValues.put('Product2Id','01txx0000006i7KAAQ');
        quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008ycFAAQ');
        quoteLineItemFieldValues.put('Quantity','2.0');
        quoteLineItemFieldValues.put('UnitPrice','7.0');
        quoteLineItemFieldValues.put('StartDate','2025-03-15');
        quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord.fieldValues = quoteLineItemFieldValues;
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem',quoteLineItemRecord);
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords);
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test', listOfRecords);
        
        //Place sales transaction API call
        RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null, null, null, null);
        System.debug(resp);
    }

    public static void callPSTAPI_Patch_With_ContextId() {
        
          // Apex test to update a quote with a quote line item
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
        
        //Quote setup
       String contextId = 'MY_CONTEXT_ID';
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'PATCH','0Q0xx0000004CYsCAM');
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        
        //Quote line item setup
        //New quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'POST');
        Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
        quoteLineItemFieldValues.put('Product2Id','01txx0000006i7KAAQ');
        quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008ycFAAQ');
        quoteLineItemFieldValues.put('Quantity','2.0');
        quoteLineItemFieldValues.put('UnitPrice','7.0');
        quoteLineItemFieldValues.put('StartDate','2025-03-15');
        quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
        quoteLineItemRecord.fieldValues = quoteLineItemFieldValues;
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem',quoteLineItemRecord);
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords);
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test', listOfRecords);
        
        //Place sales transaction API call
        RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), contextId, null, null, null);
        System.debug(resp);
    }

    public static void callPSTAPI_Delete() {
        
        // Apex test to update a quote with a quote line item
        RevSalesTrxn.PricingPreferenceEnum pricingPrefEnum = RevSalesTrxn.PricingPreferenceEnum.SYSTEM;
        RevSalesTrxn.ConfigurationExecutionEnum configurationExecutionEnum = RevSalesTrxn.ConfigurationExecutionEnum.SYSTEM;
        
        //Quote setup
        RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'PATCH','0Q0xx0000004CYsCAM');
        RevSalesTrxn.RecordWithReferenceRequest quoteItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuote',quoteRecord);
        
        //Quote line item setup
        //Delete a quote line item
        RevSalesTrxn.RecordResource quoteLineItemRecord = new RevSalesTrxn.RecordResource(QuoteLineItem.getSobjectType(),'DELETE','0QLxx0000004CYsCAM');
        RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem',quoteLineItemRecord);
        List<RevSalesTrxn.RecordWithReferenceRequest> listOfRecords = new List<RevSalesTrxn.RecordWithReferenceRequest>();
        listOfRecords.add(quoteItemRecords);
        listOfRecords.add(quoteLineItemRecords);
        RevSalesTrxn.GraphRequest graph = new RevSalesTrxn.GraphRequest('test',listOfRecords);
        
        //Place sales transaction API call
        RevSalesTrxn.PlaceSalesTransactionResponse resp =
            RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null,null, null, null);
        System.debug(resp);
    }
}
```

=== ARTICLE: apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm ===
---
page_id: apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm
title: PlaceSalesTransactionResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceSalesTransactionResponse Class

Contains properties to hold the response to the place sales transaction
    request.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

    

## Example

      
      

```
RevSalesTrxn.PlaceSalesTransactionResponse resp = RevSalesTrxn.PlaceSalesTransactionExecutor.execute(graph, pricingPrefEnum, configurationExecutionEnum, new RevSalesTrxn.ConfigurationOptionsInput(), null);
```

    

- 
**[PlaceSalesTransactionResponse Properties](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_properties)**  

Learn more about the available properties with the PlaceSalesTransactionResponse     class.

  

## PlaceSalesTransactionResponse Properties

  
  
  
Learn more about the available properties with the PlaceSalesTransactionResponse
    class.

    
      

The `PlaceSalesTransactionResponse` class includes these
        properties.

    

    
  

- 
**[contextDetails](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_contextDetails)**  

Get the details of the context that’s created for the sales transaction.

- 
**[errorResponse](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_errorResponse)**  

Get the list of errors encountered during the synchronous processing of the API     request.

- 
**[isSuccess](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_isSuccess)**  

Get the request status of the synchronous part of the processing.

- 
**[salesTransactionId](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_salesTransactionId)**  

Get the ID of the sales transaction, such as a quote or an order.

- 
**[statusUrl](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_statusUrl)**  

Get the asynchronous status URL of the request, if available.

- 
**[trackerId](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_RevSalesTrxn_PlaceSalesTransactionResponse_trackerId)**  

Get the unique identifier assigned to a specific operation or request that's used for     tracking and referencing the operation.

### contextDetails

Get the details of the context that’s created for the sales transaction.

#### Signature

`public ConnectApi.ContextDetails contextDetails {get; set;}`

#### Property Value

Type: ConnectApi.ContextDetails

### errorResponse

Get the list of errors encountered during the synchronous processing of the API
    request.

#### Signature

`public List<ConnectApi.PlaceSalesTransactionErrorResponse> errorResponse {get; set;}`

#### Property Value

Type: List<ConnectApi.PlaceSalesTransactionErrorResponse>

### isSuccess

Get the request status of the synchronous part of the processing.

#### Signature

`public Boolean isSuccess {get; set;}`

#### Property Value

      
      

Type: Boolean

      

Indicates whether the synchronous part of the processing is successful
          (`true`) or not (`false`).

    

### salesTransactionId

Get the ID of the sales transaction, such as a quote or an order.

#### Signature

`public String salesTransactionId {get; set;}`

#### Property Value

Type: String

### statusUrl

Get the asynchronous status URL of the request, if available.

#### Signature

`public String statusUrl {get; set;}`

#### Property Value

Type: String

### trackerId

Get the unique identifier assigned to a specific operation or request that's used for
    tracking and referencing the operation.

#### Signature

`public String trackerId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_RevSalesTrxn_RecordResource.htm ===
---
page_id: apex_class_RevSalesTrxn_RecordResource.htm
title: RecordResource Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordResource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordResource Class

Contains constructors and properties to create a record object from the field values of a
    sales transaction.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

    

## Example

      
      

```
RevSalesTrxn.RecordResource quoteRecord = new RevSalesTrxn.RecordResource(Quote.getSobjectType(),'POST');
```

    

- 
**[RecordResource Constructors](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_constructors)**  

Learn more about the available constructors with the RecordResource class.

- 
**[RecordResource Properties](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_properties)**  

Learn more about the available properties with the RecordResource class.

  

## RecordResource Constructors

  
  
  
Learn more about the available constructors with the RecordResource class.

    
      

The `RecordResource` class has these constructors.

    

    
  

- 
**[RecordResource(type, method, groupAction, criteria)](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_ctor)**  

Creates an instance of the RecordResource class to assign values to the fields of a     sales transaction by using the sObject type, API method, and sales transaction ID properties.     Additionally, you can group order or quote line items based on a criteria by using the     groupAction and criteria properties.

- 
**[RecordResource(type, method, id)](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_ctor_2)**  

Creates an instance of the RecordResource class to assign values to the fields of a sales     transaction by using the sObject type, API method, and sales transaction ID     properties.

- 
**[RecordResource(type, method)](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_ctor_3)**  

Creates an instance of the RecordResource class to assign the values to the fields of a     sales transaction by using the sObject type and API method properties.

### RecordResource(type, method, groupAction, criteria)

  
Creates an instance of the RecordResource class to assign values to the fields of a
    sales transaction by using the sObject type, API method, and sales transaction ID properties.
    Additionally, you can group order or quote line items based on a criteria by using the
    groupAction and criteria properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method, String groupAction, Map<String,ANY> criteria)`

#### Parameters

        
          

**type**

          
: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

          
: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result
            using the `getSObjectType() `method.

        
        
          

**method**

          
: Type: String

          
: Method for the API request, such as POST, PATCH, or DELETE.

        

**groupAction**

: Type: String

: Action to group order or quote line items. Valid values are:
              
- `GroupBy`

              
- `Group`

              
- `Ungroup`

              
- `GroupAll`

              
- `DeleteGroup`

            

**criteria**

: Type: Map<String,ANY>

: Criteria to group order or quote line items. For example, group order or quote line items based
            on a monthly billing frequency.

### RecordResource(type, method, id)

Creates an instance of the RecordResource class to assign values to the fields of a sales
    transaction by using the sObject type, API method, and sales transaction ID
    properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method, Id id)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

          
: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result
            using the `getSObjectType() `method.

**method**

: Type: String

          
: Method for the API request, such as POST, PATCH, or DELETE.

**id**

: Type: Id

          
: ID of the sales transaction, such as a quote or an order.

### RecordResource(type, method)

Creates an instance of the RecordResource class to assign the values to the fields of a
    sales transaction by using the sObject type and API method properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

          
: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result
            using the `getSObjectType()`method.

**method**

: Type: String

          
: Method for the API request, such as POST, PATCH, or DELETE.

  

## RecordResource Properties

  
  
  
Learn more about the available properties with the RecordResource class.

    
      

The `RecordResource` class includes these properties.

    

    
  

- 
**[criteria](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_criteria)**  

Set the criteria property to group order or quote line items. For example, group order     or quote line items based on a monthly billing frequency.

- 
**[fieldValues](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_fieldValues)**  

Set the fieldValues property to assign values to the fields to update the sales     transaction.

- 
**[groupAction](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_groupAction)**  

Set the groupAction property to group order or quote line items.

- 
**[id](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_id)**  

Set the id property to assign the ID of the sales transaction record.

- 
**[method](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_method)**  

Set the method property to specify the API request method, such as POST, PATCH, or     DELETE.

- 
**[type](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_RevSalesTrxn_RecordResource_type)**  

Set the type property to assign the object type that’s returned from the field describe     result by using the getReferenceTo() method or from the sObject describe result by using the     getSObjectType() method.

### criteria

  
Set the criteria property to group order or quote line items. For example, group order
    or quote line items based on a monthly billing frequency.

#### Signature

`public Map<String,ANY> criteria {get; set;}`

#### Property Value

Type: Map<String,ANY>

### fieldValues

Set the fieldValues property to assign values to the fields to update the sales
    transaction.

#### Signature

`public Map<String,ANY> fieldValues {get; set;}`

#### Property Value

Type: [List](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_methods_system_list.htm#apex_methods_system_list)Map<String,ANY>

### groupAction

Set the groupAction property to group order or quote line items.

    
      

You can group order or quote line items based on location, work types, or departments, if
        groups are enabled for your org. Groups provide a visualization of the products to view
        large quotes.

    

#### Signature

`public String groupAction {get; set;}`

#### Property Value

Type: String

Valid values are:

        
- `GroupBy`

        
- `Group`

        
- `Ungroup`

        
- `GroupAll`

        
- `DeleteGroup`

      

### id

Set the id property to assign the ID of the sales transaction record.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### method

Set the method property to specify the API request method, such as POST, PATCH, or
    DELETE.

#### Signature

`public String method {get; set;}`

#### Property Value

Type: String

### type

Set the type property to assign the object type that’s returned from the field describe
    result by using the getReferenceTo() method or from the sObject describe result by using the
    getSObjectType() method.

#### Signature

`public Schema.SObjectType type {get; set;}`

#### Property Value

Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

=== ARTICLE: apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm ===
---
page_id: apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm
title: RecordWithReferenceRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordWithReferenceRequest Class

Contains constructors and properties to associate a record object with a reference
    identifier.

## Namespace

[RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)

    

## Example

      
      

```
RevSalesTrxn.RecordWithReferenceRequest quoteLineItemRecords = new RevSalesTrxn.RecordWithReferenceRequest('refQuoteItem',quoteLineItemRecord);
```

    

- 
**[RecordWithReferenceRequest Constructors](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_RevSalesTrxn_RecordWithReferenceRequest_constructors)**  

Learn more about the available constructors with the RecordWithReferenceRequest     class.

- 
**[RecordWithReferenceRequest Properties](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_RevSalesTrxn_RecordWithReferenceRequest_properties)**  

Learn more about the available properties with the RecordWithReferenceRequest     class.

  

## RecordWithReferenceRequest Constructors

  
  
  
Learn more about the available constructors with the RecordWithReferenceRequest
    class.

    
      

The `RecordWithReferenceRequest` class includes these
        constructors.

    

    
  

- 
**[RecordWithReferenceRequest(referenceId, record)](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_RevSalesTrxn_RecordWithReferenceRequest_ctor)**  

Creates an instance of the RecordWithReferenceRequest class to associate a record object     with a reference identifier by using the referenceId and record object properties.

### RecordWithReferenceRequest(referenceId, record)

Creates an instance of the RecordWithReferenceRequest class to associate a record object
    with a reference identifier by using the referenceId and record object properties.

#### Signature

`public RecordWithReferenceRequest(String referenceId, RevSalesTrxn.RecordResource record)`

#### Parameters

**referenceId**

: Type: String

: Reference ID that maps to the subrequest response and can be used to reference the response in
            subsequent subrequests. You can reference the referenceId in either the body or URL of a
            subrequest. Use this syntax to include a reference: @{referenceId.FieldName}. See [referenceId property of a
              composite subrequest](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_composite_graph_composite_subrequest.htm).

**record**

: Type: [RevSalesTrxn.RecordResource](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_class_RevSalesTrxn_RecordResource)

: Record object that’s defined using the `RecordResource`
            class.

  

## RecordWithReferenceRequest Properties

  
  
  
Learn more about the available properties with the RecordWithReferenceRequest
    class.

    
      

The `RecordWithReferenceRequest` class has these
        properties.

    

    
  

- 
**[record](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_RevSalesTrxn_RecordWithReferenceRequest_record)**  

Set the record property to specify the record object that’s defined by using the     RecordResource class.

- 
**[referenceId](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_RevSalesTrxn_RecordWithReferenceRequest_referenceId)**  

Set the referenceId property to specify the reference ID that maps to the subrequest     response. This reference ID can be used to reference the response in subsequent     subrequests.

### record

Set the record property to specify the record object that’s defined by using the
    RecordResource class.

#### Signature

`public RevSalesTrxn.RecordResource record {get; set;}`

#### Property Value

Type: [RevSalesTrxn.RecordResource](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_class_RevSalesTrxn_RecordResource)

### referenceId

Set the referenceId property to specify the reference ID that maps to the subrequest
    response. This reference ID can be used to reference the response in subsequent
    subrequests.

#### Signature

`public String referenceId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_commerceorders_ConfigurationOptionsInput.htm ===
---
page_id: apex_class_commerceorders_ConfigurationOptionsInput.htm
title: ConfigurationOptionsInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_ConfigurationOptionsInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationOptionsInput Class

Contains methods and properties to set the configuration options for the input to the
        product configurator.

## Namespace

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

        

## Usage

            
            

This class holds the required details of the product configuration input. Set the
                class properties to enable default configuration, execution of configuration rules,
                and validation of the product catalog. Use these class properties as an input to the
                    [PlaceOrderExecutor Class](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_class_commerceorders_PlaceOrderExecutor) method.

        

## Example

      
      

```
CommerceOrders.ConfigurationOptionsInput configurationInput = new CommerceOrders.ConfigurationOptionsInput();
configurationInput.validateProductCatalog = true;
configurationInput.validateAmendRenewCancel = true;
configurationInput.executeConfigurationRules = true;
configurationInput.addDefaultConfiguration = true;

CommerceOrders.GraphRequest graph = new CommerceOrders.GraphRequest('testGraph', recordNodes);
CommerceOrders.PlaceOrderResult result = CommerceOrders.PlaceOrderExecutor.execute(graph, pricingPreference, configurationPreference, configurationInput);
```

    

- 
**[ConfigurationOptionsInput Properties](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_properties)**  

Set the `ConfigurationOptionsInput` class properties     to add default configuration, execute configuration rules, and validate the product     catalog.

- 
**[ConfigurationOptionsInput Methods](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_methods)**  

Learn more about the methods available with the `ConfigurationOptionsInput` class.

  

## ConfigurationOptionsInput Properties

  
  
  
Set the `ConfigurationOptionsInput` class properties
    to add default configuration, execute configuration rules, and validate the product
    catalog.

    
      

The `ConfigurationOptionsInput` class includes these
        properties.

    

    
  

- 
**[addDefaultConfiguration](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_addDefaultConfiguration)**  

Sets the default product configuration, such as bundle and product attributes, for an     order request.

- 
**[executeConfigurationRules](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_executeConfigurationRules)**  

Sets the requirement for an order to adhere to the configuration rules.

- 
**[validateAmendRenewCancel](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_validateAmendRenewCancel)**  

Sets the requirement to run validations related to amend, renew, or cancel     processes.

- 
**[validateProductCatalog](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_validateProductCatalog)**  

Sets the requirement to validate an order against the product catalog.

### addDefaultConfiguration

Sets the default product configuration, such as bundle and product attributes, for an
    order request.

#### Signature

`public Boolean addDefaultConfiguration {get; set;}`

#### Property Value

Type: Boolean

Indicates whether to automatically add default configuration to the order (`true`) or not (`false`).

### executeConfigurationRules

Sets the requirement for an order to adhere to the configuration rules.

#### Signature

`public Boolean executeConfigurationRules {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the order must
        adhere to configuration rules during processing (`true`)
        or bypass them (`false`).

### validateAmendRenewCancel

Sets the requirement to run validations related to amend, renew, or cancel
    processes.

#### Signature

`public Boolean validateAmendRenewCancel {get; set;}`

#### Property Value

Type: Boolean

Indicates whether to run validations
        related to amend, renew, or cancel processes (`true`) or
        not (`false`).

### validateProductCatalog

Sets the requirement to validate an order against the product catalog.

#### Signature

`public Boolean validateProductCatalog {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the order must be validated against the product catalog (`true`) or not (`false`).

  

## ConfigurationOptionsInput Methods

  
  
  
Learn more about the methods available with the `ConfigurationOptionsInput` class.

    
      

The `ConfigurationOptionsInput` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_equals)**  

Determines the equality of external objects in a list. This method is dynamic and is     based on the `equals()` method in Java.

- 
**[hashCode()](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_hashCode)**  

Determines the uniqueness of the external object records in a list.

- 
**[toString()](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_commerceorders_ConfigurationOptionsInput_toString)**  

Converts a value to a string.

### equals(obj)

Determines the equality of external objects in a list. This method is dynamic and is
    based on the `equals()` method in Java.

#### Signature

`public Boolean equals(Object obj)`

#### Parameters

**obj**

: Type: Object

: Reference object that’s used to compare with the class object.

#### Return Value

Type: Boolean

Indicates if the class object is same as the reference object (`true`) or not (`false`).

### hashCode()

Determines the uniqueness of the external object records in a list.

#### Signature

`public Integer hashCode()`

#### Return Value

Type: Integer

Integer hash code that represents the
        value of the object. Equal objects as per the `equals()` method must return the same hash code.

### toString()

Converts a value to a string.

#### Signature

`public String toString()`

#### Return Value

Type: String

=== ARTICLE: apex_class_commerceorders_GraphRequest.htm ===
---
page_id: apex_class_commerceorders_GraphRequest.htm
title: GraphRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_GraphRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GraphRequest Class

Contains constructors and properties to set the graph ID and a list of records to be
    ingested. The list of records is specified in a key-value map format that contains the field
    values of an order.

    

## Namespace

      
      

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

    

    

## Example

      
      

Create the list of records to be ingested by using these steps.

      
        
- Create the list of records by constructing the `Map<String, Object>` map of field values of an
          order.

```
List<CommerceOrders.RecordWithReferenceRequest> recordNodes = new List<CommerceOrders.RecordWithReferenceRequest>();
    
// Prepare for the Order 
Map<String,Object> orderFieldValues = new Map<String,Object>();
orderFieldValues.put('Pricebook2Id', '01sDU0000000lEIYAY');
orderFieldValues.put('AccountId', '001DU000001nIPKYA2');
orderFieldValues.put('EffectiveDate', '2024-01-01');
```

        
- To create a record object from the field values, create an instance of the `RecordResource`
                    class.

```

CommerceOrders.RecordResource orderRecord = new CommerceOrders.RecordResource(Order.getSobjectType(), 'POST');
orderRecord.fieldValues = orderFieldValues;
```

        
- To associate the Record object with a reference identifier, create an instance of the
                        `RecordWithReferenceRequest`
                    class.

```

CommerceOrders.RecordWithReferenceRequest orderRecordNode = new CommerceOrders.RecordWithReferenceRequest('refOrder', orderRecord);
recordNodes.add(orderRecordNode);

// Prepare for the App Usage Assignment
Map<String,Object> auaFieldValues = new Map<String,Object>();
auaFieldValues.put('AppUsageType', 'RevenueLifecycleManagement');
auaFieldValues.put('RecordId', '@{refOrder.id}');

CommerceOrders.RecordResource auaRecord = new CommerceOrders.RecordResource(AppUsageAssignment.getSobjectType(), 'POST');
auaRecord.fieldValues = auaFieldValues;

CommerceOrders.RecordWithReferenceRequest auaRecordNode = new CommerceOrders.RecordWithReferenceRequest('refAppTag', auaRecord);
recordNodes.add(auaRecordNode);

// Prepare for the Order Item
Map<String,Object> oiFieldValues = new Map<String,Object>();
oiFieldValues.put('OrderId', '@{refOrder.id}');
oiFieldValues.put('PricebookEntryId', '01uDU000000YPkIYAW');
oiFieldValues.put('Product2Id', '01tDU000000ESCSYA4');
oiFieldValues.put('Quantity', 2);
oiFieldValues.put('UnitPrice', 800);

CommerceOrders.RecordResource oiRecord = new CommerceOrders.RecordResource(OrderItem.getSobjectType(), 'POST');
oiRecord.fieldValues = oiFieldValues;

CommerceOrders.RecordWithReferenceRequest oiRecordNode = new CommerceOrders.RecordWithReferenceRequest('refOrderItem', oiRecord);
recordNodes.add(oiRecordNode);

```

                
- Invoke the Place Order Apex API. 

#### Note

The `CatalogRatesPreferenceEnum` enum is available when the Usage-Based Selling
            feature is enabled.

```

// Invoke the Place Order Apex API
CommerceOrders.PricingPreferenceEnum pricingPreference = CommerceOrders.PricingPreferenceEnum.System;
CommerceOrders.CatalogRatesPreferenceEnum catalogRatesPreference = CommerceOrders.CatalogRatesPreferenceEnum.Fetch;
CommerceOrders.ConfigurationInputEnum configurationPreference = CommerceOrders.ConfigurationInputEnum.RunAndAllowErrors;
CommerceOrders.ConfigurationOptionsInput configurationInput = new CommerceOrders.ConfigurationOptionsInput();
configurationInput.validateProductCatalog = true;
configurationInput.validateAmendRenewCancel = true;
configurationInput.executeConfigurationRules = true;
configurationInput.addDefaultConfiguration = true;
```

        
- To contain all record objects, create an instance of the `GraphRequest` class.

```

CommerceOrders.GraphRequest graph = new CommerceOrders.GraphRequest('testGraph', recordNodes);
CommerceOrders.PlaceOrderResult result = CommerceOrders.PlaceOrderExecutor.execute(graph, pricingPreference, catalogRatesPreference, configurationPreference, configurationInput);

// Process any error, if exists
if (!result.success) {
  List<ConnectApi.PlaceOrderErrorResponse> errors = result.responseError;
  for (ConnectApi.PlaceOrderErrorResponse error : errors) {
    System.debug(error.errorCode + ': ' + error.message);
  }
}
```

      

    

  

- 
**[GraphRequest Constructors](./apex_class_commerceorders_GraphRequest.htm.md#apex_commerceorders_GraphRequest_constructors)**  

Learn more about the available constructors with the `GraphRequest` class.

- 
**[GraphRequest Properties](./apex_class_commerceorders_GraphRequest.htm.md#apex_commerceorders_GraphRequest_properties)**  

Learn more about the available properties with the `GraphRequest` class.

  

## GraphRequest Constructors

  
  
  
Learn more about the available constructors with the `GraphRequest` class.

    
      

The `GraphRequest` class includes these constructors.

    

    
  

- 
**[GraphRequest(graphId, records)](./apex_class_commerceorders_GraphRequest.htm.md#apex_commerceorders_GraphRequest_ctor)**  

Creates an instance of the `GraphRequest` class to     assign the graph ID and a list of records to be ingested.

### GraphRequest(graphId, records)

Creates an instance of the `GraphRequest` class to
    assign the graph ID and a list of records to be ingested.

#### Signature

`public GraphRequest(String graphId, List<commerceorders.RecordWithReferenceRequest> records)`

#### Parameters

**graphId**

: Type: String

: ID of the graph.

**records**

: Type: List<[commerceorders.RecordWithReferenceRequest](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_class_commerceorders_RecordWithReferenceRequest)>

: List of records to be ingested.

  

## GraphRequest Properties

  
  
  
Learn more about the available properties with the `GraphRequest` class.

    
      

The `GraphRequest` class includes these properties.

    

    
  

- 
**[graphId](./apex_class_commerceorders_GraphRequest.htm.md#apex_commerceorders_GraphRequest_graphId)**  

Set the `graphId` property to assign the ID value of     the graph.

### graphId

Set the `graphId` property to assign the ID value of
    the graph.

#### Signature

`public String graphId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_commerceorders_PlaceOrderExecutor.htm ===
---
page_id: apex_class_commerceorders_PlaceOrderExecutor.htm
title: PlaceOrderExecutor Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_PlaceOrderExecutor.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceOrderExecutor Class

Contains methods to place an order with details of the graph request, pricing
    preferences, and configuration options.

## Namespace

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

## Example

      

```
CommerceOrders.PlaceOrderResult resp = CommerceOrders.PlaceOrderExecutor.execute(graph,internalEnum,cEnum,cInput,catalogRatesPreference);
```

- 
**[PlaceOrderExecutor Methods](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_commerceorders_PlaceOrderExecutor_methods)**  

Learn more about the methods available with the `PlaceOrderExecutor` class.

- 
**[PlaceOrderExecutor Example Implementation](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_commerceorders_PlaceOrderExecutor_example_implementation)**  

Place orders with integrated pricing, configuration, and validation, and manage them         throughout their entire lifecycle. To place an order from Apex, refer to the example         implementation of the `PlaceOrderExecutor`         class.

  

## PlaceOrderExecutor Methods

  
  
  
Learn more about the methods available with the `PlaceOrderExecutor` class.

    
      

The `PlaceOrderExecutor` class includes these methods.

    

    
  

- 
**[execute(graphRequest, pricingPreferenceEnum, configurationInputEnum, configurationOptionsInput)](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_commerceorders_PlaceOrderExecutor_execute_1)**  

Use the method in the `PlaceOrderExecutor` class     to execute the Place Order Apex API request by assigning the properties for graph request,     pricing reference, and configuration options.

- 
**[execute(graphRequest, pricingPreferenceEnum, catalogRatesPreference, configurationInputEnum, configurationOptionsInput)](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_commerceorders_PlaceOrderExecutor_execute_3)**  

Use the method in the `PlaceOrderExecutor` class     to execute the Place Order Apex API request by assigning the properties for graph request,     pricing reference, and configuration options. This method also includes the property to define     fetching of rate card entries.

- 
**[execute(graphRequest)](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_commerceorders_PlaceOrderExecutor_execute_2)**  

Use the method in the `PlaceOrderExecutor` class to     execute the Place Order Apex API request by assigning the properties for graph     request.

  

### execute(graphRequest, pricingPreferenceEnum,
      configurationInputEnum, configurationOptionsInput)

  
  
  
Use the method in the `PlaceOrderExecutor` class
    to execute the Place Order Apex API request by assigning the properties for graph request,
    pricing reference, and configuration options.

    

#### Signature

      
      

`public static commerceorders.PlaceOrderResult
          execute(commerceorders.GraphRequest graphRequest, commerceorders.PricingPreferenceEnum
          pricingPreferenceEnum, commerceorders.ConfigurationInputEnum configurationInputEnum,
          commerceorders.ConfigurationOptionsInput configurationOptionsInput)`

      
    

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [commerceorders.GraphRequest](./apex_class_commerceorders_GraphRequest.htm.md#apex_class_commerceorders_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [commerceorders.PricingPreferenceEnum](./apex_enum_commerceorders_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the order process.

        
        
          

**configurationInputEnum**

          
: Type: [commerceorders.ConfigurationInputEnum](./apex_enum_commerceorders_ConfigurationInputEnum.htm.md)

          
: Configuration input for the place order process.

        
        
          

**configurationOptionsInput**

          
: Type: [commerceorders.ConfigurationOptionsInput](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_class_commerceorders_ConfigurationOptionsInput)

          
: Configuration options during the ingestion process.

        
      

    

    

#### Return Value

      
      

Type: [commerceorders.PlaceOrderResult](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_class_commerceorders_PlaceOrderResult)

    

  

  

### execute(graphRequest, pricingPreferenceEnum,
      catalogRatesPreference, configurationInputEnum, configurationOptionsInput)

  
  
  
Use the method in the `PlaceOrderExecutor` class
    to execute the Place Order Apex API request by assigning the properties for graph request,
    pricing reference, and configuration options. This method also includes the property to define
    fetching of rate card entries.

    

#### Signature

      
      

`public static commerceorders.PlaceOrderResult
          execute(commerceorders.GraphRequest graphRequest, commerceorders.PricingPreferenceEnum
          pricingPreferenceEnum, commerceorders.CatalogRatesPreferenceEnum
          catalogRatesPreferenceEnum, commerceorders.ConfigurationInputEnum configurationInputEnum,
          commerceorders.ConfigurationOptionsInput configurationOptionsInput)`

      
    

    

#### Parameters

      
      
        
          

**graphRequest**

          
: Type: [commerceorders.GraphRequest](./apex_class_commerceorders_GraphRequest.htm.md#apex_class_commerceorders_GraphRequest)

          
: The sObject graph values of the order payload to be ingested.

        
        
          

**pricingPreferenceEnum**

          
: Type: [commerceorders.PricingPreferenceEnum](./apex_enum_commerceorders_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the order process.

        
        
          

**catalogRatesPreference**

          
: Type: [commerceorders.CatalogRatesPreferenceEnum](./apex_enum_commerceorders_CatalogRatesPreferenceEnum.htm.md)

          
: The rate card entries defined in the catalog that must be fetched for order items,
            with usage-based pricing during the order creation process. The `CatalogRatesPreferenceEnum` enum is available when the
            Usage-Based Selling feature is enabled.

        
        
          

**configurationInputEnum**

          
: Type: [commerceorders.ConfigurationInputEnum](./apex_enum_commerceorders_ConfigurationInputEnum.htm.md)

          
: Configuration input for the place order process.

        
        
          

**configurationOptionsInput**

          
: Type: [commerceorders.ConfigurationOptionsInput](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_class_commerceorders_ConfigurationOptionsInput)

          
: Configuration options during the ingestion process.

        
      

    

    

#### Return Value

      
      

Type: [commerceorders.PlaceOrderResult](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_class_commerceorders_PlaceOrderResult)

    

  

### execute(graphRequest)

Use the method in the `PlaceOrderExecutor` class to
    execute the Place Order Apex API request by assigning the properties for graph
    request.

#### Signature

`public static commerceorders.PlaceOrderResult execute(commerceorders.GraphRequest graphRequest)`

#### Parameters

**graphRequest**

: Type: [commerceorders.GraphRequest](./apex_class_commerceorders_GraphRequest.htm.md#apex_class_commerceorders_GraphRequest)

: The sObject graph values of the order payload to be ingested.

#### Return Value

Type: [commerceorders.PlaceOrderResult](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_class_commerceorders_PlaceOrderResult)

    

## PlaceOrderExecutor Example Implementation

    
    
    
Place orders with integrated pricing, configuration, and validation, and manage them
        throughout their entire lifecycle. To place an order from Apex, refer to the example
        implementation of the `PlaceOrderExecutor`
        class.

        

### Namespace

            
            

[commerceorders](./apex_namespace_commerceorders.htm.md)

        

        

### Usage

            
            

Customize this example to suit your requirements. Create the list of records to be
                ingested by using these steps. Replace the respective IDs with the values that are
                present in your org. For example, replace the value of `${Pricebook2Id}` field with the price book ID that’s present in the
                org.

        

        

### Example

            
                
- Create the list of records by constructing the `Map<String, Object>` map of field
                    values of an
                    order.

```
List<CommerceOrders.RecordWithReferenceRequest> recordNodes = new List<CommerceOrders.RecordWithReferenceRequest>();
    
// Prepare for the Order 
Map<String,Object> orderFieldValues = new Map<String,Object>();
orderFieldValues.put('Pricebook2Id', '01sDU0000000lEIYAY');
orderFieldValues.put('AccountId', '001DU000001nIPKYA2');
orderFieldValues.put('EffectiveDate', '2024-01-01');
```

                
- To create a record object from the field values, create an instance of the
                        `RecordResource`
                    class.

```

CommerceOrders.RecordResource orderRecord = new CommerceOrders.RecordResource(Order.getSobjectType(), 'POST');
orderRecord.fieldValues = orderFieldValues;
```

                
- To associate the Record object with a reference identifier, create an instance
                    of the `RecordWithReferenceRequest`
                    class.

```

CommerceOrders.RecordWithReferenceRequest orderRecordNode = new CommerceOrders.RecordWithReferenceRequest('refOrder', orderRecord);
recordNodes.add(orderRecordNode);

// Prepare for the App Usage Assignment
Map<String,Object> auaFieldValues = new Map<String,Object>();
auaFieldValues.put('AppUsageType', 'RevenueLifecycleManagement');
auaFieldValues.put('RecordId', '@{refOrder.id}');

CommerceOrders.RecordResource auaRecord = new CommerceOrders.RecordResource(AppUsageAssignment.getSobjectType(), 'POST');
auaRecord.fieldValues = auaFieldValues;

CommerceOrders.RecordWithReferenceRequest auaRecordNode = new CommerceOrders.RecordWithReferenceRequest('refAppTag', auaRecord);
recordNodes.add(auaRecordNode);

// Prepare for the Order Item
Map<String,Object> oiFieldValues = new Map<String,Object>();
oiFieldValues.put('OrderId', '@{refOrder.id}');
oiFieldValues.put('PricebookEntryId', '01uDU000000YPkIYAW');
oiFieldValues.put('Product2Id', '01tDU000000ESCSYA4');
oiFieldValues.put('Quantity', 2);
oiFieldValues.put('UnitPrice', 800);

CommerceOrders.RecordResource oiRecord = new CommerceOrders.RecordResource(OrderItem.getSobjectType(), 'POST');
oiRecord.fieldValues = oiFieldValues;

CommerceOrders.RecordWithReferenceRequest oiRecordNode = new CommerceOrders.RecordWithReferenceRequest('refOrderItem', oiRecord);
recordNodes.add(oiRecordNode);

```

                
- Invoke the Place Order Apex API. 

#### Note

The `CatalogRatesPreferenceEnum` enum is available when the
                        Usage-Based Selling feature is
                    enabled.

```

// Invoke the Place Order Apex API
CommerceOrders.PricingPreferenceEnum pricingPreference = CommerceOrders.PricingPreferenceEnum.System;
CommerceOrders.CatalogRatesPreferenceEnum catalogRatesPreference = CommerceOrders.CatalogRatesPreferenceEnum.Fetch;
CommerceOrders.ConfigurationInputEnum configurationPreference = CommerceOrders.ConfigurationInputEnum.RunAndAllowErrors;
CommerceOrders.ConfigurationOptionsInput configurationInput = new CommerceOrders.ConfigurationOptionsInput();
configurationInput.validateProductCatalog = true;
configurationInput.validateAmendRenewCancel = true;
configurationInput.executeConfigurationRules = true;
configurationInput.addDefaultConfiguration = true;
```

                
- To contain all record objects, create an instance of the `GraphRequest`
                    class.

```

CommerceOrders.GraphRequest graph = new CommerceOrders.GraphRequest('testGraph', recordNodes);
CommerceOrders.PlaceOrderResult result = CommerceOrders.PlaceOrderExecutor.execute(graph, pricingPreference, catalogRatesPreference, configurationPreference, configurationInput);

// Process any error, if exists
if (!result.success) {
  List<ConnectApi.PlaceOrderErrorResponse> errors = result.responseError;
  for (ConnectApi.PlaceOrderErrorResponse error : errors) {
    System.debug(error.errorCode + ': ' + error.message);
  }
}
```

=== ARTICLE: apex_class_commerceorders_PlaceOrderResult.htm ===
---
page_id: apex_class_commerceorders_PlaceOrderResult.htm
title: PlaceOrderResult Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_PlaceOrderResult.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceOrderResult Class

Contains properties to hold the response to the place order request.

## Namespace

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

## Example

      

```
CommerceOrders.PlaceOrderResult resp = CommerceOrders.PlaceOrderExecutor.execute(graph,internalEnum,cEnum,cInput,catalogRatesPreference);
```

- 
**[PlaceOrderResult Properties](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_properties)**  

Learn more about the available properties with the `PlaceOrderResult` class.

  

## PlaceOrderResult Properties

  
  
  
Learn more about the available properties with the `PlaceOrderResult` class.

    
      

The `PlaceOrderResult` class includes these
        properties.

    

    
  

- 
**[orderId](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_orderId)**  

Get the ID of the order that’s created after a successful request.

- 
**[requestIdentifier](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_requestIdentifier)**  

Get the request ID of the process to query the asynchronous status of the Place Order     Apex API.

- 
**[responseError](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_responseError)**  

Get the list of errors encountered during the synchronous processing of the API     request.

- 
**[statusURL](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_statusURL)**  

Get the asynchronous status URL of the request, if available.

- 
**[success](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_commerceorders_PlaceOrderResult_success)**  

Get the request status of the synchronous part of the processing.

### orderId

Get the ID of the order that’s created after a successful request.

#### Signature

`public String orderId {get; set;}`

#### Property Value

Type: String

### requestIdentifier

Get the request ID of the process to query the asynchronous status of the Place Order
    Apex API.

#### Signature

`public String requestIdentifier {get; set;}`

#### Property Value

Type: String

### responseError

Get the list of errors encountered during the synchronous processing of the API
    request.

#### Signature

`public List<commerceorders.PlaceOrderErrorResponse> responseError {get; set;}`

#### Property Value

Type: List<ConnectApi.PlaceOrderErrorResponse>

### statusURL

Get the asynchronous status URL of the request, if available.

#### Signature

`public String statusURL {get; set;}`

#### Property Value

Type: String

### success

Get the request status of the synchronous part of the processing.

#### Signature

`public Boolean success {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the synchronous part
        of the processing is successful (`true`) or not (`false`).

=== ARTICLE: apex_class_commerceorders_RecordResource.htm ===
---
page_id: apex_class_commerceorders_RecordResource.htm
title: RecordResource Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_RecordResource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordResource Class

Contains constructors and properties to create a record object from field values of an
    order.

## Namespace

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

## Example

      

```
CommerceOrders.RecordResource orderRecord = new CommerceOrders.RecordResource(Order.getSobjectType(), 'POST');
orderRecord.fieldValues = orderFieldValues;
```

- 
**[RecordResource Constructors](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_constructors)**  

Learn more about the available constructors with the `RecordResource` class.

- 
**[RecordResource Properties](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_properties)**  

Learn more about the available properties with the `RecordResource` class.

  

## RecordResource Constructors

  
  
  
Learn more about the available constructors with the `RecordResource` class.

    
      

The `RecordResource` class includes these
        constructors.

    

    
  

- 
**[RecordResource(type, method, id)](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_ctor)**  

Creates an instance of the `RecordResource` class to     assign values to the fields of an order item by using the sObject type, API method, and order ID     properties.

- 
**[RecordResource(type, method)](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_ctor_2)**  

Creates an instance of the `RecordResource` class to     assign the values to the fields of an order item by using the sObject type and API method     properties.

### RecordResource(type, method, id)

Creates an instance of the `RecordResource` class to
    assign values to the fields of an order item by using the sObject type, API method, and order ID
    properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method, Id id)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result using
              the `getSObjectType()` method.

**method**

: Type: String

: Method for the API request, such as POST or PATCH.

**id**

: Type: Id

: ID of the order.

### RecordResource(type, method)

Creates an instance of the `RecordResource` class to
    assign the values to the fields of an order item by using the sObject type and API method
    properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

          
: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result
            using the `getSObjectType()` method.

**method**

: Type: String

          
: Method for the API request, such as POST or PATCH.

  

## RecordResource Properties

  
  
  
Learn more about the available properties with the `RecordResource` class.

    
      

The `RecordResource` class includes these properties.

    

    
  

- 
**[fieldValues](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_fieldValues)**  

Set the `fieldValues` property to assign values to the     fields to update the order record.

- 
**[id](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_id)**  

Set the `id` property to assign the ID of the order     record.

- 
**[method](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_method)**  

Set the `method` property to specify the API request     method, such as POST or PATCH.

- 
**[type](./apex_class_commerceorders_RecordResource.htm.md#apex_commerceorders_RecordResource_type)**  

Set the `type` property to assign the object type that’s     returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result using the `getSObjectType()` method.

### fieldValues

Set the `fieldValues` property to assign values to the
    fields to update the order record.

#### Signature

`public Map<String,ANY> fieldValues {get; set;}`

#### Property Value

Type: [List](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_methods_system_list.htm#apex_methods_system_list)<Map<String,ANY>>

### id

Set the `id` property to assign the ID of the order
    record.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### method

Set the `method` property to specify the API request
    method, such as POST or PATCH.

#### Signature

`public String method {get; set;}`

#### Property Value

Type: String

### type

Set the `type` property to assign the object type that’s
    returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result using the `getSObjectType()` method.

#### Signature

`public Schema.SObjectType type {get; set;}`

#### Property Value

Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

=== ARTICLE: apex_class_commerceorders_RecordWithReferenceRequest.htm ===
---
page_id: apex_class_commerceorders_RecordWithReferenceRequest.htm
title: RecordWithReferenceRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commerceorders_RecordWithReferenceRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordWithReferenceRequest Class

Contains constructors and properties to associate a record object with a reference
    identifier.

## Namespace

[CommerceOrders](./apex_namespace_commerceorders.htm.md)

## Example

      

```
CommerceOrders.RecordWithReferenceRequest orderRecordNode = new CommerceOrders.RecordWithReferenceRequest('refOrder', orderRecord);
```

- 
**[RecordWithReferenceRequest Constructors](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_commerceorders_RecordWithReferenceRequest_constructors)**  

Learn more about the available constructors with the `RecordWithReferenceRequest` class.

- 
**[RecordWithReferenceRequest Properties](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_commerceorders_RecordWithReferenceRequest_properties)**  

Learn more about the available properties with the `RecordWithReferenceRequest` class.

  

## RecordWithReferenceRequest Constructors

  
  
  
Learn more about the available constructors with the `RecordWithReferenceRequest` class.

    
      

The `RecordWithReferenceRequest` class includes these
        constructors.

    

    
  

- 
**[RecordWithReferenceRequest(referenceId, record)](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_commerceorders_RecordWithReferenceRequest_ctor)**  

Creates an instance of the `RecordWithReferenceRequest` class to associate a record object with a reference     identifier by using the `referenceId` and `record` object properties.

### RecordWithReferenceRequest(referenceId, record)

Creates an instance of the `RecordWithReferenceRequest` class to associate a record object with a reference
    identifier by using the `referenceId` and `record` object properties.

#### Signature

`public RecordWithReferenceRequest(String referenceId, commerceorders.RecordResource record)`

#### Parameters

**referenceId**

: Type: String

: 
            

Reference ID that maps to the subrequest response and can be used to reference the
              response in subsequent subrequests. You can reference the `referenceId` in either the body or URL of a subrequest. Use this syntax to
              include a reference: `@{referenceId.FieldName}`.
              See [referenceId property of a composite subrequest](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_composite_graph_composite_subrequest.htm).

          

**record**

: Type: [commerceorders.RecordResource](./apex_class_commerceorders_RecordResource.htm.md#apex_class_commerceorders_RecordResource)

: Record object that’s defined using the `RecordResource`
            class.

  

## RecordWithReferenceRequest Properties

  
  
  
Learn more about the available properties with the `RecordWithReferenceRequest` class.

    
      

The `RecordWithReferenceRequest` class includes these
        properties.

    

    
  

- 
**[record](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_commerceorders_RecordWithReferenceRequest_record)**  

Set the `record` property to specify the record object     that’s defined by using the `RecordResource` class.

- 
**[referenceId](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_commerceorders_RecordWithReferenceRequest_referenceId)**  

Set the `referenceId` property to specify the reference     ID that maps to the subrequest response. This reference ID can be used to reference the response     in subsequent subrequests.

### record

Set the `record` property to specify the record object
    that’s defined by using the `RecordResource` class.

#### Signature

`public commerceorders.RecordResource record {get; set;}`

#### Property Value

Type: [commerceorders.RecordResource](./apex_class_commerceorders_RecordResource.htm.md#apex_class_commerceorders_RecordResource)

### referenceId

Set the `referenceId` property to specify the reference
    ID that maps to the subrequest response. This reference ID can be used to reference the response
    in subsequent subrequests.

#### Signature

`public String referenceId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_commercetax_AbstractTransactionResponse.htm ===
---
page_id: apex_class_commercetax_AbstractTransactionResponse.htm
title: AbstractTransactionResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_AbstractTransactionResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# AbstractTransactionResponse Class

  
  
  
Abstract class that contains methods for setting tax fields based on
      the external tax provider's response. Response classes that extend `AbstractTransactionResponse` inherit these methods.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

  

- 
**[AbstractTransactionResponse Methods](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_methods)**  

Learn more about the methods for AbstractTransactionResponse class.

  

## AbstractTransactionResponse Methods

  
  
  
Learn more about the methods for AbstractTransactionResponse class.

    
      

The `AbstractTransactionResponse` class includes these
        methods.

    

    
  

- 
**[setAddresses(addresses)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setAddresses)**  

Uses an instance of `AddressesResponse` to set the values of tax address fields.

- 
**[setAmountDetails(amountDetails)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setAmountDetails)**  

Uses an instance of `AmountDetailsResponse` to set tax amount fields such as exemption amount and tax       amount.

- 
**[setCurrencyIsoCode(currencyIsoCode)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setCurrencyIsoCode)**  

Sets the currencyIsoCode field.

- 
**[setCustomTaxAttributes(customTaxAttributes)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setCustomTaxAttributes)**  

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax       response at the header level.

- 
**[setDescription(dscptn)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setDescription)**  

Sets the Description field.

- 
**[setDocumentCode(documentCode)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setDocumentCode)**  

Sets the DocumentCode field. Document codes are often used to       reference tax documents that the external tax engine uses in the tax calculation process.       Document code acts as a unique link to chain-related transactions, such as amendment or       refunds.

- 
**[setEffectiveDate(effectiveDate)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setEffectiveDate)**  

Sets the EffectiveDate field. Effective Date fields are optional       fields that store the date that a transaction takes effect. We provide these fields only for       recordkeeping purposes – for example, if you must report an effective date to an       external general ledger system. Salesforce doesn't use them to calculate any tax or payment       values.

- 
**[setLineItems(lineItems)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setLineItems)**  

Uses an instance of the `LineItemResponse` class to set a list of line items. Each line item represents an       item sent to an external tax engine for tax calculation.

- 
**[setReferenceDocumentCode(referenceDocumentCode)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setReferenceDocumentCode)**  

Sets the ReferenceDocumentCode field. Use this field to store the       code of an additional document used in the tax calculation process. For example, use this       field in case of a refund for a previously taxed purchase.

- 
**[setReferenceEntityId(referenceEntityId)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setReferenceEntityId)**  

Sets the ID of a reference entity. In Commerce Tax, a reference       entity represents a record related to the items sent to the external tax engine for tax       calculation. For example, if you sent order items for tax calculation, you could define the       parent order as the reference entity.

- 
**[setTaxTransactionId(taxTrxnId)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setTaxTransactionId)**  

Sets the TaxTransactionId field using the ID of a tax transaction       record. In Commerce Tax, a tax transaction record stores information about a specific tax       calculation process.

- 
**[setTransactionDate(transactionDate)](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_commercetax_AbstractTransactionResponse_setTransactionDate)**  

Sets the TransactionDate field.

  

### setAddresses(addresses)

  
  
  
Uses an instance of `AddressesResponse` to set the values of tax address fields.

    

#### Signature

`global void setAddresses(commercetax.AddressesResponse
          addresses)`

    

#### Parameters

        
- 
**addresses**:

Type: [AddressesResponse](./apex_class_commercetax_AddressesResponse.htm.md#apex_class_commercetax_AddressesResponse)

Class that contains methods to set the Ship To, Ship From, and Sold To address
            information.

      

    

#### Return Value

Type: void

  

  

### setAmountDetails(amountDetails)

  
  
  
Uses an instance of `AmountDetailsResponse` to set tax amount fields such as exemption amount and tax
      amount.

    

#### Signature

`global void setAmountDetails(commercetax.AmountDetailsResponse
          amountDetails)`

    

#### Parameters

        
- 
**amountDetails**:

Type: [AmountDetailsResponse](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_class_commercetax_AmountDetailsResponse)

Class that contains methods to set the tax exemption amount, tax amount, total amount,
            and total amount with tax.

      

    

#### Return Value

Type: void

  

  

### setCurrencyIsoCode(currencyIsoCode)

  
  
  
Sets the currencyIsoCode field.

    

#### Signature

`global void
          setCurrencyIsoCode(String
      currencyIsoCode)`

    

#### Parameters

        
- 
**currencyIsoCode**:

Type: String

Three-letter ISO 4217 currency code associated with a tax object.

      

    

#### Return Value

Type: void

  

  

### setCustomTaxAttributes(customTaxAttributes)

  
  
  
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax
      response at the header level.

    

#### Signature

      
      

`global void
          setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse
          customTaxAttributes)`

      
    

    

#### Parameters

      
      
        
- 
**customTaxAttributes**:

Type: [CustomTaxAttributesResponse](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_class_commercetax_CustomTaxAttributesResponse)

Additional

data or custom attributes to include in the tax response.

      

    

    

#### Return Value

      
      

Type: void

    

  

  

### setDescription(dscptn)

  
  
  
Sets the Description field.

    

#### Signature

`global void
          setDescription(String
      dscptn)`

    

#### Parameters

        
- 
**dscptn**:

Type: String

Optional field for providing additional information about a record.

      

    

#### Return Value

Type: void

  

  

### setDocumentCode(documentCode)

  
  
  
Sets the DocumentCode field. Document codes are often used to
      reference tax documents that the external tax engine uses in the tax calculation process.
      Document code acts as a unique link to chain-related transactions, such as amendment or
      refunds.

    

#### Signature

`global void
          setDocumentCode(String
      documentCode)`

    

#### Parameters

        
- 
**documentCode**:

Type: String

Code

for a tax document used in the tax calculation process.

      

    

#### Return Value

Type: void

  

  

### setEffectiveDate(effectiveDate)

  
  
  
Sets the EffectiveDate field. Effective Date fields are optional
      fields that store the date that a transaction takes effect. We provide these fields only for
      recordkeeping purposes – for example, if you must report an effective date to an
      external general ledger system. Salesforce doesn't use them to calculate any tax or payment
      values.

    

#### Signature

`global void
          setEffectiveDate(Datetime
      effectiveDate)`

    

#### Parameters

        
- 
**effectiveDate**:

Type: Datetime

Optional field that stores the date that a transaction takes effect.

      

    

#### Return Value

Type: void

  

  

### setLineItems(lineItems)

  
  
  
Uses an instance of the `LineItemResponse` class to set a list of line items. Each line item represents an
      item sent to an external tax engine for tax calculation.

    

#### Signature

`global void setLineItems(List<commercetax.LineItemResponse>
          lineItems)`

    

#### Parameters

        
- 
**lineItems**:

Type: List<[LineItemResponse](./apex_class_commercetax_LineItemResponse.htm.md#apex_class_commercetax_LineItemResponse)>

A list of line items sent to an external tax engine for tax calculation.

      

    

#### Return Value

Type: void

  

  

### setReferenceDocumentCode(referenceDocumentCode)

  
  
  
Sets the ReferenceDocumentCode field. Use this field to store the
      code of an additional document used in the tax calculation process. For example, use this
      field in case of a refund for a previously taxed purchase.

    

#### Signature

`global void
          setReferenceDocumentCode(String
      referenceDocumentCode)`

    

#### Parameters

        
- 
**referenceDocumentCode**:

Type: String

The code for a document used in the tax calculation process.

      

    

#### Return Value

Type: void

  

  

### setReferenceEntityId(referenceEntityId)

  
  
  
Sets the ID of a reference entity. In Commerce Tax, a reference
      entity represents a record related to the items sent to the external tax engine for tax
      calculation. For example, if you sent order items for tax calculation, you could define the
      parent order as the reference entity.

    

#### Signature

`global void
          setReferenceEntityId(String
      referenceEntityId)`

    

#### Parameters

        
- 
**referenceEntityId**:

Type: String

ID of a record related to the items sent for tax calculation.

      

    

#### Return Value

Type: void

  

  

### setTaxTransactionId(taxTrxnId)

  
  
  
Sets the TaxTransactionId field using the ID of a tax transaction
      record. In Commerce Tax, a tax transaction record stores information about a specific tax
      calculation process.

    

#### Signature

`global void
          setTaxTransactionId(String
      taxTrxnId)`

    

#### Parameters

        
- 
**taxTrxnId**:

Type: String

The ID of a tax transaction record in Commerce Tax.

      

    

#### Return Value

Type: void

  

  

### setTransactionDate(transactionDate)

  
  
  
Sets the TransactionDate field.

    

#### Signature

`global void
          setTransactionDate(Datetime
      transactionDate)`

    

#### Parameters

        
- 
**transactionDate**:

Type: Datetime

Date that a tax transaction occurred.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_AddressResponse.htm ===
---
page_id: apex_class_commercetax_AddressResponse.htm
title: AddressResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_AddressResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# AddressResponse Class

  
  
  
Contains a location code sent from the external tax
    engine.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Usage

      
      

Use the `AddressResponse` class to set unique values for
        each address.

      

```
commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();

//AddressResponse containing ShipTo information
commercetax.AddressResponse shipToAddress = new commercetax.AddressResponse();
shipToAddress.setLocationCode('1234567');

//AddressResponse containing ShipFrom information
commercetax.AddressResponse shipFromAddress = new commercetax.AddressResponse();
shipFromAddress.setLocationCode('84720385');

//AddressResponse containing Sold To information
commercetax.AddressResponse soldToAddress = new commercetax.AddressResponse();
soldToAddress.setLocationCode('92381749');

//set values of addressesRes
addressesRes.setShipFrom(shipFromAddress);
addressesRes.setShipTo(shipToAddress);
addressesRes.setSoldTo(soldToAddress);

```

    

  

- 
**[AddressResponse Methods](./apex_class_commercetax_AddressResponse.htm.md#apex_commercetax_AddressResponse_methods)**  

Learn more about the available methods with the `AddressResponse` class.

  

## AddressResponse Methods

  
  
  
Learn more about the available methods with the `AddressResponse` class.

    
      

The `AddressResponse` class includes these
        methods.

    

    
  

- 
**[setLocationCode(locationCode)](./apex_class_commercetax_AddressResponse.htm.md#apex_commercetax_AddressResponse_setLocationCode)**  

Sets the value of a LocationCode field.

  

### setLocationCode(locationCode)

  
  
  
Sets the value of a LocationCode field.

    

#### Signature

`global void
          setLocationCode(String
      locationCode)`

    

#### Parameters

        
- 
**locationCode**:

Type: String

A code that contains address information. This value can be passed to a
            method
            that sets the value of an address field.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_AddressesResponse.htm ===
---
page_id: apex_class_commercetax_AddressesResponse.htm
title: AddressesResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_AddressesResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# AddressesResponse Class

  
  
  
Sets the tax address fields based on a response from the external
      tax engine. Contains setter methods for the Ship From, Ship To, and Sold To
    addresses.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Usage

Because `AddressesResponse`
      contains multiple addresses, we recommend using multiple instances of `AddressResponse` to set unique values for each address.

    

## Example

      
      

This code sample represents a portion of the code used in a mock tax adapter. In this
        example, you create three `AddressResponse` classes, set
        their location codes, and pass them to the `Ship
        To`, `Ship From`, and
          `Sold To` setter methods in `AddressesResponse`. In an actual implementation, your `AddressResponse` classes already have a location code based on
        the response from the external tax engine.

      

```
commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();

//AddressResponse containing ShipTo information
commercetax.AddressResponse shipToAddress = new commercetax.AddressResponse();
shipToAddress.setLocationCode('1234567');

//AddressResponse containing ShipFrom information
commercetax.AddressResponse shipFromAddress = new commercetax.AddressResponse();
shipFromAddress.setLocationCode('84720385');

//AddressResponse containing Sold To information
commercetax.AddressResponse soldToAddress = new commercetax.AddressResponse();
soldToAddress.setLocationCode('92381749');

//set values of addressesRes
addressesRes.setShipFrom(shipFromAddress);
addressesRes.setShipTo(shipToAddress);
addressesRes.setSoldTo(soldToAddress);

```

    

  

- 
**[AddressesResponse Methods](./apex_class_commercetax_AddressesResponse.htm.md#apex_commercetax_AddressesResponse_methods)**  

Learn more about the methods for AddressesResponse class.

  

## AddressesResponse Methods

  
  
  
Learn more about the methods for AddressesResponse class.

    
      

The `AddressesResponse` class includes these
        methods.

    

    
  

- 
**[setShipFrom(shipFrom)](./apex_class_commercetax_AddressesResponse.htm.md#apex_commercetax_AddressesResponse_setShipFrom)**  

Sets the value of a       ShipFrom       address field.

- 
**[setShipTo(shipTo)](./apex_class_commercetax_AddressesResponse.htm.md#apex_commercetax_AddressesResponse_setShipTo)**  

Sets the value of a ShipTo address field.

- 
**[setSoldTo(soldTo)](./apex_class_commercetax_AddressesResponse.htm.md#apex_commercetax_AddressesResponse_setSoldTo)**  

Sets the value of a SoldTo address field.

  

### setShipFrom(shipFrom)

  
  
  
Sets the value of a
      ShipFrom
      address field.

    

#### Signature

`global void setShipFrom(commercetax.AddressResponse
          shipFrom)`

    

#### Parameters

        
- 
**shipFrom**:

Type: [AddressResponse](./apex_class_commercetax_AddressResponse.htm.md#apex_class_commercetax_AddressResponse)

A single address. Use this generic address parameter  to store any type of address,
            such as Ship From, Ship To, and Sold To details. Users set the specific address in an
              `AddressResponse` instance and then pass that
            instance to the `AddressesResponse`’s `setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as
            needed.

      

    

#### Return Value

Type: void

  

  

### setShipTo(shipTo)

  
  
  
Sets the value of a ShipTo address field.

    

#### Signature

`global void setShipTo(commercetax.AddressResponse
        shipTo)`

    

#### Parameters

        
- 
**shipTo**:

Type: [AddressResponse](./apex_class_commercetax_AddressResponse.htm.md#apex_class_commercetax_AddressResponse)

Stores

a single address. This is a generic address parameter and can be used to store
            any type of address, such as Ship From, Ship To, and Sold To details. Users set the
            specific address in an `AddressResponse` instance and
            then pass that instance to the `AddressesResponse`’s
              `setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as
            needed.

      

    

#### Return Value

Type: void

  

  

### setSoldTo(soldTo)

  
  
  
Sets the value of a SoldTo address field.

    

#### Signature

`global void setSoldTo(commercetax.AddressResponse
        soldTo)`

    

#### Parameters

        
- 
**soldTo**:

Type: [AddressResponse](./apex_class_commercetax_AddressResponse.htm.md#apex_class_commercetax_AddressResponse)

Stores

a single address. This is a generic address parameter and can be used to store
            any type of address, such as Ship From, Ship To, Sold To details. Users set the specific
            address in an AddressResponse instance and then pass that instance to the `AddressesResponse`’s `setShipTo()`, `setShipFrom()`, and `setSoldTo()` methods as needed.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_AmountDetailsResponse.htm ===
---
page_id: apex_class_commercetax_AmountDetailsResponse.htm
title: AmountDetailsResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_AmountDetailsResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# AmountDetailsResponse Class

  
  
  
Sets tax amount fields based on a response from the external tax
      engine.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Example

      

In this example, an instance of `AmountDetailsResponse`
        class in a mock adapter calculates several tax amount fields. The `totalTax` and `totalAmount` parameters were
        defined in an instance of [`LineItemResponse`](./apex_class_commercetax_LineItemResponse.htm.md#apex_class_commercetax_LineItemResponse) class. The adapter then assigns the instance to
          `lineItemResponse`.

      commercetax.AmountDetailsResponse amountResponse = new commercetax.AmountDetailsResponse();
amountResponse.setTotalAmountWithTax(totalTax+totalAmount);
amountResponse.setExemptAmount(0);
amountResponse.setTotalAmount(totalAmount);
amountResponse.setTaxAmount(totalTax);
lineItemResponse.setAmountDetails(amountResponse);
```

  

- 
**[AmountDetailsResponse Methods](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_commercetax_AmountDetailsResponse_methods)**  

Learn more about the methods available from the `AmountDetailsResponse` class.

  

## AmountDetailsResponse Methods

  
  
  
Learn more about the methods available from the `AmountDetailsResponse` class.

    
      

The following are methods for `AmountDetailsResponse`.

    

    
  

- 
**[setExemptAmount(exemptAmount)](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_commercetax_AmountDetailsResponse_setExemptAmount)**  

Sets the value of the ExemptAmount field.

- 
**[setTaxAmount(taxAmount)](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_commercetax_AmountDetailsResponse_setTaxAmount)**  

Sets the value of the TaxAmount field.

- 
**[setTotalAmount(totalAmount)](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_commercetax_AmountDetailsResponse_setTotalAmount)**  

Sets the value of the TotalAmount field.

- 
**[setTotalAmountWithTax(totalAmtWithTax)](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_commercetax_AmountDetailsResponse_setTotalAmountWithTax)**  

Sets the value of the TotalAmountWithTax field.

  

### setExemptAmount(exemptAmount)

  
  
  
Sets the value of the ExemptAmount field.

    

#### Signature

`global void
          setExemptAmount(Double
      exemptAmount)`

    

#### Parameters

        
- 
**exemptAmount**:

Type: Double

The amount of a line item's total amount that's exempt from tax calculation.

      

    

#### Return Value

Type: void

  

  

### setTaxAmount(taxAmount)

  
  
  
Sets the value of the TaxAmount field.

    

#### Signature

`global void
          setTaxAmount(Double
      taxAmount)`

    

#### Parameters

        
- 
**taxAmount**:

Type: Double

The calculated amount of tax for a line item.

      

    

#### Return Value

Type: void

  

  

### setTotalAmount(totalAmount)

  
  
  
Sets the value of the TotalAmount field.

    

#### Signature

`global void
          setTotalAmount(Double
      totalAmount)`

    

#### Parameters

        
- 
**totalAmount**:

Type: Double

The total amount of a line item, excluding tax.

      

    

#### Return Value

Type: void

  

  

### setTotalAmountWithTax(totalAmtWithTax)

  
  
  
Sets the value of the TotalAmountWithTax field.

    

#### Signature

`global void setTotalAmountWithTax(Double totalAmtWithTax)`

    

#### Parameters

        
- 
**totalAmtWithTax**:

Type: Double

The total amount of a line item combined with the calculated tax for that line
            item.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_CalculateTaxRequest.htm ===
---
page_id: apex_class_commercetax_CalculateTaxRequest.htm
title: CalculateTaxRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_CalculateTaxRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# CalculateTaxRequest Class

  
  
  
Represents a request to an external tax engine to calculate tax.
      Extends the [TaxTransactionRequest](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_class_commercetax_TaxTransactionRequest) class and is the top-level request
      class.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    

## Usage

      
      

Keep these considerations in mind when you use this class.

      
        
- If the `shouldVoidTax` property value is set to
            `true`, then the operation returns a response with
            `documentCode` property value updated to `referenceDocumentCode` property value that was originally
          sent in the request payload. The response also includes the `taxTransactionType` property value as `Void`. This indicates that the document specified in the `referenceDocumentCode` property value is voided.

        
- If document is locked or you can't void the tax transaction for any reason, then you can
          use the Tax Calculation request to perform another transaction such as a Credit Tax
          request. In this scenario, the response includes the `documentCode` property value that was sent in the request payload.

        
- If the document that's mentioned in the `referenceDocumentCode` property value isn't available in the tax engine, then
          an error response occurs with ResultCode value as `ReferenceDocumentCodeMissing`.

      

    

    

## Example

See [TaxEngineAdapter Example Implementation](./apex_interface_commercetax_TaxEngineAdapter.htm.md#apex_interface_commercetax_TaxEngineAdapter_Example) for more details on how
        to access information from the `CalculateTaxRequest`
        class.

  

- 
**[CalculateTaxRequest Constructors](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_constructors)**  

Learn more about the constructors that are available with the `CalculateTaxRequest` class. This constructor is intended for test usage and throws an     exception if used outside of the Apex test context.

- 
**[CalculateTaxRequest Properties](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_properties)**  

Learn more about the available properties with the `CalculateTaxRequest` class.

- 
**[CalculateTaxRequest Methods](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_methods)**  

Learn more about the available methods with the `CalculateTaxRequest` class.

  

## CalculateTaxRequest Constructors

  
  
  
Learn more about the constructors that are available with the `CalculateTaxRequest` class. This constructor is intended for test usage and throws an
    exception if used outside of the Apex test context.

    
      

The `CalculateTaxRequest` class includes these
        constructors.

    

    
  

- 
**[CalculateTaxRequest(taxType)](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_ctor)**  

This constructor is intended for test usage only and throws an       exception if used outside of the Apex test context.

  

### CalculateTaxRequest(taxType)

  
  
  
This constructor is intended for test usage only and throws an
      exception if used outside of the Apex test context.

    

#### Signature

`global CalculateTaxRequest(commercetax.CalculateTaxType
          taxType)`

    

#### Parameters

        
- 
**taxType**:

Type: [CalculateTaxType](./apex_enum_commercetax_CalculateTaxType.htm.md)

Indicates whether the tax calculation is for estimated tax or actual tax.

      

  

  

## CalculateTaxRequest Properties

  
  
  
Learn more about the available properties with the `CalculateTaxRequest` class.

    
      

The `CalculateTaxRequest` class includes these
        properties.

    

    
  

- 
**[isCommit](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_isCommit)**  

Indicates whether the tax calculation has to be committed or       reported to government authorities.

- 
**[isHeaderTaxRequested](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_isHeaderTaxRequested)**  

Indicates whether header tax is enabled in the tax engine (`true`) or not (`false`).

- 
**[shouldVoidTax](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_shouldVoidTax)**  

Indicates whether to void the tax transaction associated with a       document that's mentioned in the `referenceDocumentCode`       property value with `taxType` property value set to `Actual` and `isCommit` property       value set to `true`.

- 
**[taxTransactionType](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_taxTransactionType)**  

Shows whether the tax transaction is for a credit or debit       transaction.

- 
**[taxType](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_taxType)**  

Shows whether the tax calculation is for estimated or actual tax       wherein only actual tax can be submitted.

  

### isCommit

  
  
  
Indicates whether the tax calculation has to be committed or
      reported to government authorities.

    

#### Signature

`global Boolean
          isCommit {get;
      set;}`

    

#### Property Value

Type: Boolean

  

  

### isHeaderTaxRequested

  
  
  
Indicates whether header tax is enabled in the tax engine (`true`) or not (`false`).

    

#### Signature

      
      

`global Boolean isHeaderTaxRequested {get; set;}`

      
    

    

#### Property Value

      
      

Type: Boolean

    

  

  

### shouldVoidTax

  
  
  
Indicates whether to void the tax transaction associated with a
      document that's mentioned in the `referenceDocumentCode`
      property value with `taxType` property value set to `Actual` and `isCommit` property
      value set to `true`.

    

#### Signature

      
      

`global commercetax.CalculateTaxType shouldVoidTax {get;
          set;}`

      
    

    

#### Property Value

      
      

Type: Boolean

    

  

  

### taxTransactionType

  
  
  
Shows whether the tax transaction is for a credit or debit
      transaction.

    

#### Signature

`global commercetax.TaxTransactionType taxTransactionType {get;
          set;}`

    

#### Property Value

Type: [TaxTransactionType](./apex_enum_commercetax_TaxTransactionType.htm.md)

  

  

### taxType

  
  
  
Shows whether the tax calculation is for estimated or actual tax
      wherein only actual tax can be submitted.

    

#### Signature

`global commercetax.CalculateTaxType taxType {get;
        set;}`

    

#### Property Value

Type: [CalculateTaxType](./apex_enum_commercetax_CalculateTaxType.htm.md)

  

  

## CalculateTaxRequest Methods

  
  
  
Learn more about the available methods with the `CalculateTaxRequest` class.

    
      

The `CalculateTaxRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_equals)**  

Maintains the integrity of lists of type `CalculateTaxRequest` by determining the equality of external objects in a list.       This method is dynamic and is based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_hashCode)**  

Maintains the integrity of lists of type `CalculateTaxRequest` by determining the uniqueness of the external object records       in a       list.

- 
**[toString()](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_commercetax_CalculateTaxRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `CalculateTaxRequest` by determining the equality of external objects in a list.
      This method is dynamic and is based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object
            whose
            key is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `CalculateTaxRequest` by determining the uniqueness of the external object records
      in a
      list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_CalculateTaxResponse.htm ===
---
page_id: apex_class_commercetax_CalculateTaxResponse.htm
title: CalculateTaxResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_CalculateTaxResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# CalculateTaxResponse Class

  
  
  
Sets
            the values of the tax transaction following a response from the external tax engine.
            Extends the [AbstractTransactionResponse](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_class_commercetax_AbstractTransactionResponse) class and is the top-level response
        class.

        

## Namespace

            
            

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

        

## Example

            
            

```
if(requestType == commercetax.RequestType.CalculateTax){
             commercetax.calculatetaxtype type = request.taxtype;
             String docCode='';
             if(request.DocumentCode == 'simulateEmptyDocumentCode')
                 docCode = '';
             else if(request.DocumentCode != null)
                 docCode =request.DocumentCode;
             else if(request.ReferenceEntityId != null) docCode = request.ReferenceEntityId;
             else docCode =  String.valueOf(getRandomInteger(0,2147483647));
             commercetax.CalculateTaxResponse response = new commercetax.CalculateTaxResponse();
             if(request.isCommit == true) {
                 response.setStatus(commercetax.TaxTransactionStatus.Committed);
             } else {
                 response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);
             }
             response.setDocumentCode(docCode);
             response.setReferenceDocumentCode(request.referenceDocumentCode);
             response.setTaxType(type);
             response.setStatusDescription('statusDescription');
             if(request.sellerDetails.code == 'testSellerCode') {
                 response.setDescription('SellerCode fetched from TaxEngine entity');
             }
             else {
                 response.setDescription('description');
             }
            response.setEffectiveDate(system.now());
            if(request.transactionDate == null) {
               response.setTransactionDate(system.now());
            } else {
               response.setTransactionDate(request.transactionDate);
            }
            if(request.taxTransactionType == null) {
                response.setTaxTransactionType(commercetax.TaxTransactionType.Debit);
            } else {
                response.setTaxTransactionType(request.taxTransactionType);
            }
             if(request.currencyIsoCode == null || request.currencyIsoCode == '') {
                response.setCurrencyIsoCode('USD');
             } else {
                response.setCurrencyIsoCode(request.currencyIsoCode);
             }
             response.setReferenceEntityId(request.ReferenceEntityId);
}
```

        

    

- 
**[CalculateTaxResponse Methods](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_methods)**  

Learn more about the available methods with the `CalculateTaxResponse` class.

  

## CalculateTaxResponse Methods

  
  
  
Learn more about the available methods with the `CalculateTaxResponse` class.

    
      

The `CalculateTaxResponse` class includes these
        methods.

    

    
  

- 
**[setAddresses(addresses)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setAddresses)**  

Sets the value of the Addresses field using the addresses contained       in an instance of the AddressesResponse     class.

- 
**[setAmountDetails(amountDetails)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setAmountDetails)**  

Sets the value of the AmountDetails field using an instance of `AmountDetailsResponse`.

- 
**[setCurrencyIsoCode(currencyIsoCode)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setCurrencyIsoCode)**  

Sets the value of the CurrencyIsoCode field of the `CalculateTaxResponse` object.

- 
**[setDescription(dscptn)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setDescription)**  

Sets the value of the Description field of the `CalculateTaxResponse` object.

- 
**[setDocumentCode(documentCode)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setDocumentCode)**  

Sets the value of the DocumentCode field of the `CalculateTaxResponse` object.

- 
**[setEffectiveDate(effectiveDate)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setEffectiveDate)**  

Sets the value of the EffectiveDate field of the `CalculateTaxResponse` object.

- 
**[setLineItems(lineItems)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setLineItems)**  

Sets the value of the LineItems field of the `CalculateTaxResponse` object.

- 
**[setReferenceDocumentCode(referenceDocumentCode)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setReferenceDocumentCode)**  

Sets the value of the ReferenceDocumentCode field of the `CalculateTaxResponse` object.

- 
**[setReferenceEntityId(referenceEntityId)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setReferenceEntityId)**  

Sets the value of the ReferenceEntityId field of the `CalculateTaxResponse` object.

- 
**[setStatus(status)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setStatus)**  

Sets the value of the Status field of the `CalculateTaxResponse` object.

- 
**[setStatusDescription(statusDescription)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setStatusDescription)**  

Sets the value of the StatusDescription field of the `CalculateTaxResponse` object.

- 
**[setTaxTransactionId(taxTrxnId)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setTaxTransactionId)**  

Sets the value of the TaxTransactionId field of the `CalculateTaxResponse` object.

- 
**[setTaxTransactionType(taxTransactionType)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setTaxTransactionType)**  

Sets the value of the TaxTransactionType field of the `CalculateTaxResponse` object.

- 
**[setTaxType(taxType)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setTaxType)**  

Sets the value of the TaxType field of the `CalculateTaxResponse` object.

- 
**[setTransactionDate(transactionDate)](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_commercetax_CalculateTaxResponse_setTransactionDate)**  

Sets the value of the TransactionDate field of the `CalculateTaxResponse` object.

  

### setAddresses(addresses)

  
  
  
Sets the value of the Addresses field using the addresses contained
      in an instance of the [AddressesResponse](./apex_class_commercetax_AddressesResponse.htm.md#apex_class_commercetax_AddressesResponse)
    class.

    

#### Signature

`global void setAddresses(commercetax.AddressesResponse
          addresses)`

    

#### Parameters

        
- 
**addresses**:

Type: [AddressesResponse](./apex_class_commercetax_AddressesResponse.htm.md#apex_class_commercetax_AddressesResponse)

Contains Ship To, Ship From, and Sold To addresses.

      

    

#### Return Value

Type: void

  

  

### setAmountDetails(amountDetails)

  
  
  
Sets the value of the AmountDetails field using an instance of [`AmountDetailsResponse`](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_class_commercetax_AmountDetailsResponse).

    

#### Signature

`global void setAmountDetails(commercetax.AmountDetailsResponse
          amountDetails)`

    

#### Parameters

        
- 
**amountDetails**:

Type: [AmountDetailsResponse](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_class_commercetax_AmountDetailsResponse)

The tax amount details for a line item on which tax was calculated.

      

    

#### Return Value

Type: void

  

  

### setCurrencyIsoCode(currencyIsoCode)

  
  
  
Sets the value of the CurrencyIsoCode field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setCurrencyIsoCode(String
      currencyIsoCode)`

    

#### Parameters

        
- 
**currencyIsoCode**:

Type: String

Three-letter ISO 4217 currency code associated with a tax object.

      

    

#### Return Value

Type: void

  

  

### setDescription(dscptn)

  
  
  
Sets the value of the Description field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setDescription(String
      dscptn)`

    

#### Parameters

        
- 
**dscptn**:

Type: String

Optional description for providing more information about the calculate tax
            response.

      

    

#### Return Value

Type: void

  

  

### setDocumentCode(documentCode)

  
  
  
Sets the value of the DocumentCode field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setDocumentCode(String
      documentCode)`

    

#### Parameters

        
- 
**documentCode**:

Type: String

Code

for a tax document that’s created by the tax engine for the calculation
            process.

      

    

#### Return Value

Type: void

  

  

### setEffectiveDate(effectiveDate)

  
  
  
Sets the value of the EffectiveDate field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setEffectiveDate(Datetime
      effectiveDate)`

    

#### Parameters

        
- 
**effectiveDate**:

Type: Datetime

The date a tax calculation action takes effect. This parameter is optional and is
            provided only for recordkeeping purpose. Additionally, this parameter is used to
            determine the tax rates or rules and overrides the transaction date. For example, if the
            tax calculation request is placed on January 3 and the transaction date is January 1,
            you can set the effective date as January 1.

      

    

#### Return Value

Type: void

  

  

### setLineItems(lineItems)

  
  
  
Sets the value of the LineItems field of the `CalculateTaxResponse` object.

    

#### Signature

`global void setLineItems(List<commercetax.LineItemResponse>
          lineItems)`

    

#### Parameters

        
- 
**lineItems**:

Type: List<[LineItemResponse](./apex_class_commercetax_LineItemResponse.htm.md#apex_class_commercetax_LineItemResponse)>

Response object that the tax adapter populates from the response of the external tax
            engine.

      

    

#### Return Value

Type: void

  

  

### setReferenceDocumentCode(referenceDocumentCode)

  
  
  
Sets the value of the ReferenceDocumentCode field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setReferenceDocumentCode(String
      referenceDocumentCode)`

    

#### Parameters

        
- 
**referenceDocumentCode**:

Type: String

Code

for a reference document used in the tax calculation process.

      

    

#### Return Value

Type: void

  

  

### setReferenceEntityId(referenceEntityId)

  
  
  
Sets the value of the ReferenceEntityId field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setReferenceEntityId(String
      referenceEntityId)`

    

#### Parameters

        
- 
**referenceEntityId**:

Type: String

ID of an entity related to the line items submitted for tax calculation. For example,
            if order items were sent for tax calculation, you could use the ID of their parent
            order.

      

    

#### Return Value

Type: void

  

  

### setStatus(status)

  
  
  
Sets the value of the Status field of the `CalculateTaxResponse` object.

    

#### Signature

`global void setStatus(commercetax.TaxTransactionStatus
          status)`

    

#### Parameters

        
- 
**status**:

Type: [TaxTransactionStatus](./apex_enum_commercetax_TaxTransactionStatus.htm.md)

Indicates whether a tax transaction has been committed.

      

    

#### Return Value

Type: void

  

  

### setStatusDescription(statusDescription)

  
  
  
Sets the value of the StatusDescription field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setStatusDescription(String
      statusDescription)`

    

#### Parameters

        
- 
**statusDescription**:

Type: String

Optional value for providing more information about a tax transaction's status.

      

    

#### Return Value

Type: void

  

  

### setTaxTransactionId(taxTrxnId)

  
  
  
Sets the value of the TaxTransactionId field of the `CalculateTaxResponse` object.

    

#### Signature

`public void
          setTaxTransactionId(String
      taxTrxnId)`

    

#### Parameters

        
- 
**taxTrxnId**:

Type: String

The ID of the
            Salesforce
            tax transaction entity that stores information about the tax
            calculation transaction.

      

    

#### Return Value

Type: void

  

  

### setTaxTransactionType(taxTransactionType)

  
  
  
Sets the value of the TaxTransactionType field of the `CalculateTaxResponse` object.

    

#### Signature

`global void setTaxTransactionType(commercetax.TaxTransactionType
          taxTransactionType)`

    

#### Parameters

        
- 
**taxTransactionType**:

Type: [TaxTransactionType](./apex_enum_commercetax_TaxTransactionType.htm.md)

Whether the tax transaction was for a credit, debit, or voided transaction.

      

    

#### Return Value

Type: void

  

  

### setTaxType(taxType)

  
  
  
Sets the value of the TaxType field of the `CalculateTaxResponse` object.

    

#### Signature

`global void setTaxType(commercetax.CalculateTaxType
          taxType)`

    

#### Parameters

        
- 
**taxType**:

Type: [CalculateTaxType](./apex_enum_commercetax_CalculateTaxType.htm.md)

Indicates whether a tax calculation request is for estimated or actual tax.

      

    

#### Return Value

Type: void

  

  

### setTransactionDate(transactionDate)

  
  
  
Sets the value of the TransactionDate field of the `CalculateTaxResponse` object.

    

#### Signature

`global void
          setTransactionDate(Datetime
      transactionDate)`

    

#### Parameters

        
- 
**transactionDate**:

Type: Datetime

The date that the tax transaction occurred.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_CustomTaxAttributesResponse.htm ===
---
page_id: apex_class_commercetax_CustomTaxAttributesResponse.htm
title: CustomTaxAttributesResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_CustomTaxAttributesResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

    

# CustomTaxAttributesResponse Class

    
    
    
Sets additional data or custom attributes in the tax
            response.

        

## Namespace

            
            

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

    

- 
**[CustomTaxAttributesResponse Constructors](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_commercetax_CustomTaxAttributesResponse_constructors)**  

Learn more about the available constructors with the `CustomTaxAttributesResponse` class.

- 
**[CustomTaxAttributesResponse Methods](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_commercetax_CustomTaxAttributesResponse_methods)**  

Learn more about the available methods with the `CustomTaxAttributesResponse` class.

  

## CustomTaxAttributesResponse Constructors

  
  
  
Learn more about the available constructors with the `CustomTaxAttributesResponse` class.

    
      

The `CustomTaxAttributesResponse` class includes
        these constructors.

    

    
  

- 
**[CustomTaxAttributesResponse()](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_commercetax_CustomTaxAttributesResponse_ctor)**  

Constructor to set additional data or custom attributes in the tax       response.

  

### CustomTaxAttributesResponse()

  
  
  
Constructor to set additional data or custom attributes in the tax
      response.

    

#### Signature

      
      

`global CustomTaxAttributesResponse()`

    

  

  

## CustomTaxAttributesResponse Methods

  
  
  
Learn more about the available methods with the `CustomTaxAttributesResponse` class.

    
      

The `CustomTaxAttributesResponse` class includes
        these methods.

    

    
  

- 
**[setData(data)](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_commercetax_CustomTaxAttributesResponse_setData)**  

Sets additional data or custom attributes in the tax     response.

  

### setData(data)

  
  
  
Sets additional data or custom attributes in the tax
    response.

    

#### Signature

      
      

`global void setData(Map<String, Object>
        data)`

      
    

    

#### Parameters

      
      
        
- 
**data**:

Type: Map<String, Object> Additional data or custom attributes to be included in the tax response.

      

    

    

#### Return Value

      
      

Type: void

=== ARTICLE: apex_class_commercetax_ErrorResponse.htm ===
---
page_id: apex_class_commercetax_ErrorResponse.htm
title: ErrorResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_ErrorResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

    

# ErrorResponse Class

    
    
    
Use to respond with an error after receiving errors from the
            PaymentGatewayAdapter
            methods of the [CommercePayments](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)
            namespace, such as request-forbidden responses, custom validation errors, or expired API
            tokens.

        

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

## Example

            
            

This example snippet of
                a
                mock tax adapter shows a hypothetical scenario to demo an error
                response. The adapter receives request information from `TaxEngineContext` and stores it in an instance of `CalculateTaxRequest`. If the request's `documentCode` property is null or indicates an error,
                the adapter returns an error response with information about the error.

            

```

global virtual class MockAdapter implements commercetax.TaxEngineAdapter {
 
     global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext taxEngineContext) {
         commercetax.RequestType requestType = taxEngineContext.getRequestType();
         commercetax.CalculateTaxRequest request = (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();

if(request.documentCode == null) {
             return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '404', 'documentCode  is mandatory');
         }
         if(request.documentCode == 'TaxEngineError') {
             return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '504', 'documentCode  - not supported');
         }
         if(request.documentCode == 'simulateValidationFailureInAdapter') {
             return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '400', 'validations for documentCode failed in adapter');
         }
         if(request.documentCode == 'simulateMalformedErrorInAdapter') {
                     return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, null, 'malformed adapter error response');
         }
         if(request.documentCode == 'simulateTaxEngineProcessFailure') {
             return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '500', 'Tax Engine couldnt process your request');
         }
 
```

        

    

- 
**[ErrorResponse Constructors](./apex_class_commercetax_ErrorResponse.htm.md#apex_commercetax_ErrorResponse_constructors)**  

Learn more about the available constructors with the `ErrorResponse` class.

  

## ErrorResponse Constructors

  
  
  
Learn more about the available constructors with the `ErrorResponse` class.

    
      

The `ErrorResponse` class includes these
        constructors.

    

    
  

- 
**[ErrorResponse(resultCode, errorCode, errorMessage)](./apex_class_commercetax_ErrorResponse.htm.md#apex_commercetax_ErrorResponse_ctor)**  

Constructor to initialize an `ErrorResponse` object from the result code, error code, and error message sent from       the tax engine.

  

### ErrorResponse(resultCode, errorCode,
    errorMessage)

  
  
  
Constructor to initialize an `ErrorResponse` object from the result code, error code, and error message sent from
      the tax engine.

    

#### Signature

`global ErrorResponse(commercetax.ResultCode resultCode, String
          errorCode, String errorMessage)`

    

#### Parameters

        
- 
**resultCode**:

Type: [ResultCode](./apex_enum_commercetax_ResultCode.htm.md)

Code for the type of result sent by the tax engine.

        
- 
**errorCode**:

Type: String

Code for the type of error sent by the tax engine. Codes must match the HTTP status codes to be returned to the user. Here are a few examples:

              
  - If the status code is for a bad request, set `errorCode` to `400`.

              
  - If the status code is for a forbidden request, set `errorCode` to `403`.

              
  - If `errorCode` isn't a valid HTTP status code,
                a
                500 internal server error is returned.

            

        
- 
**errorMessage**:

Type: String

The error message sent by the tax engine.

=== ARTICLE: apex_class_commercetax_HeaderTaxAddressesRequest.htm ===
---
page_id: apex_class_commercetax_HeaderTaxAddressesRequest.htm
title: HeaderTaxAddressesRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_HeaderTaxAddressesRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# HeaderTaxAddressesRequest Class

  
  
  
Captures the address values that are applicable for the quote or
      order transaction.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
    
  

- 
**[HeaderTaxAddressesRequest Constructors](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_constructors)**  

Learn more about the constructors available with the `HeaderTaxAddressesRequest` class.

- 
**[HeaderTaxAddressesRequest Properties](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_properties)**  

Learn more about the available properties with the `HeaderTaxAddressesRequest` class.

- 
**[HeaderTaxAddressesRequest Methods](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_methods)**  

Learn more about the available methods with the `HeaderTaxAddressesRequest` class.

  

## HeaderTaxAddressesRequest Constructors

  
  
  
Learn more about the constructors available with the `HeaderTaxAddressesRequest` class.

    
      

The `HeaderTaxAddressesRequest` class includes these
        constructors.

    

    
  

- 
**[HeaderTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_ctor)**  

Constructor for initializing the required addresses of the tax             addresses request such as the ship from, ship to, sold to, and bill to addresses. This             constructor is intended for test usage and throws an exception if used outside of the             Apex test context.

    

### HeaderTaxAddressesRequest(shipFrom, shipTo, soldTo,
            billTo, taxEngineAddress)

    
    
    
Constructor for initializing the required addresses of the tax
            addresses request such as the ship from, ship to, sold to, and bill to addresses. This
            constructor is intended for test usage and throws an exception if used outside of the
            Apex test context.

        

#### Signature

`global HeaderTaxAddressesRequest(commercetax.TaxAddressRequest
                    shipFrom, commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest
                    soldTo, commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest
                    taxEngineAddress)`

        

#### Parameters

                
- 
**shipFrom**:

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

Address where a line item was shipped from.

                
- 
**shipTo**:

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

Address where a line item was shipped to.

                
- 
**soldTo**:

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

Address of the line item's buyer.

                
- 
**billTo**:

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

Person or group who was billed

for the line item.

                
- 
**taxEngineAddress**:

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

Address that the tax engine uses to calculate tax.

            

    

  

## HeaderTaxAddressesRequest Properties

  
  
  
Learn more about the available properties with the `HeaderTaxAddressesRequest` class.

    
      

The `HeaderTaxAddressesRequest` class includes these
        properties.

    

    
  

- 
**[billTo](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_billTo)**  

Specifies the billTo address for a       line       item on which tax was calculated.

- 
**[shipFrom](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_shipFrom)**  

Specifies the shipFrom address for a line       item       on which tax was calculated.

- 
**[shipTo](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_shipTo)**  

Specifies the shipTo address for a line       item       on which tax was calculated.

- 
**[soldTo](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_soldTo)**  

Specifies the soldTo address for a line       item       on which tax was calculated.

- 
**[taxEngineAddress](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_taxEngineAddress)**  

Address used by the tax engine when calculating tax for       a       line item.

  

### billTo

  
  
  
Specifies the billTo address for a
      line
      item on which tax was calculated.

    

#### Signature

`global commercetax.TaxAddressRequest billTo {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### shipFrom

  
  
  
Specifies the shipFrom address for a line
      item
      on which tax was calculated.

    

#### Signature

`global commercetax.TaxAddressRequest shipFrom {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### shipTo

  
  
  
Specifies the shipTo address for a line
      item
      on which tax was calculated.

    

#### Signature

`global commercetax.TaxAddressRequest shipTo {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### soldTo

  
  
  
Specifies the soldTo address for a line
      item
      on which tax was calculated.

    

#### Signature

`global commercetax.TaxAddressRequest soldTo {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### taxEngineAddress

  
  
  
Address used by the tax engine when calculating tax for
      a
      line item.

    

#### Signature

`global commercetax.TaxAddressRequest taxEngineAddress {get;
          set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

## HeaderTaxAddressesRequest Methods

  
  
  
Learn more about the available methods with the `HeaderTaxAddressesRequest` class.

    
      

The `HeaderTaxAddressesRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_equals)**  

Maintains the integrity of lists of type `HeaderTaxAddressesRequest` by determining the equality of external objects in a       list. This method is dynamic and is based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_hashCode)**  

Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external objects in a       list.

- 
**[toString()](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_commercetax_HeaderTaxAddressesRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `HeaderTaxAddressesRequest` by determining the equality of external objects in a
      list. This method is dynamic and is based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object
            whose
            key is to be validated.

      

    

#### Return Value

      
      

Type: Boolean

    

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external objects in a
      list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_ImpositionResponse.htm ===
---
page_id: apex_class_commercetax_ImpositionResponse.htm
title: ImpositionResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_ImpositionResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# ImpositionResponse Class

  
  
  
Stores details of tax impositions from the external tax
    engine.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Example

      

In this
        mock
        adapter example, the adapter sets the `TaxDetailsResponse.setImposition()` method parameter to null if the request's
        document code indicates that the tax calculation didn't require any exceptions. Otherwise,
        it creates an instance of `ImpositionResponse` and sets its
        SubType and Type values, and then assigns it to `TaxDetailsResponse`.

      if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
  taxDetailsResponse.setImposition(null);
                     }else{
                        commercetax.ImpositionResponse imposition = new commercetax.ImpositionResponse();
                        imposition.setSubType('subtype');
                        imposition.setType('type');
                        taxDetailsResponse.setImposition(imposition);
                   }
```

  

- 
**[ImpositionResponse Methods](./apex_class_commercetax_ImpositionResponse.htm.md#apex_commercetax_ImpositionResponse_methods)**  

Learn more about the available methods with the `ImpositionResponse` class.

  

## ImpositionResponse Methods

  
  
  
Learn more about the available methods with the `ImpositionResponse` class.

    
      

The `ImpositionResponse` class includes these
        methods.

    

    
  

- 
**[setId(id)](./apex_class_commercetax_ImpositionResponse.htm.md#apex_commercetax_ImpositionResponse_setId)**  

Sets the ID field of the `ImpositionResponse` class.

- 
**[setName(name)](./apex_class_commercetax_ImpositionResponse.htm.md#apex_commercetax_ImpositionResponse_setName)**  

Sets the Name field of the `ImpositionResponse` class.

- 
**[setSubType(subType)](./apex_class_commercetax_ImpositionResponse.htm.md#apex_commercetax_ImpositionResponse_setSubType)**  

Sets the SubType field of the `ImpositionResponse` class.

- 
**[setType(type)](./apex_class_commercetax_ImpositionResponse.htm.md#apex_commercetax_ImpositionResponse_setType)**  

Sets the Type field of the `ImpositionResponse` class.

  

### setId(id)

  
  
  
Sets the ID field of the `ImpositionResponse` class.

    

#### Signature

`global void
          setId(String
      id)`

    

#### Parameters

        
- 
**id**:

Type: String

User-defined ID value used

for referencing the tax imposition.

      

    

#### Return Value

Type: void

  

  

### setName(name)

  
  
  
Sets the Name field of the `ImpositionResponse` class.

    

#### Signature

`global void
          setName(String
      name)`

    

#### Parameters

        
- 
**name**:

Type: String

Optional user-defined name for the tax imposition response.

      

    

#### Return Value

Type: void

  

  

### setSubType(subType)

  
  
  
Sets the SubType field of the `ImpositionResponse` class.

    

#### Signature

`global void
          setSubType(String
      subType)`

    

#### Parameters

        
- 
**subType**:

Type: String

Many tax calculation organizations use types and subtypes to categorize their tax
            imposition procedures.

If the tax engine you use follows this process, set the subtype
            with this parameter.

      

    

#### Return Value

Type: void

  

  

### setType(type)

  
  
  
Sets the Type field of the `ImpositionResponse` class.

    

#### Signature

`public void
          setType(String
      type)`

    

#### Parameters

        
- 
**type**:

Type: String

Many tax calculation organizations use types and subtypes to categorize their tax
            imposition procedures.

If the tax engine you use follows this process, set the type with
            this parameter.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_JurisdictionResponse.htm ===
---
page_id: apex_class_commercetax_JurisdictionResponse.htm
title: JurisdictionResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_JurisdictionResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# JurisdictionResponse Class

  
  
  
Stores details from the external tax engine about the tax
      jurisdiction used in the tax calculation process. A tax jurisdiction represents a government
      entity that collects tax.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Example

      

In
        this
        mock adapter example, the adapter sets the `TaxDetailsResponse.setJurisdiction()` method parameter to null if the request's
        document code indicates that the tax calculation didn't require any exceptions. Otherwise,
        it creates an instance of `JurisdictionResponse` and sets
        its address values. Because this code represents a mock adapter, the example defines the
        address parameters directly. In a standard implementation, the jurisdiction's setters
        receive values passed from the eternal tax engine.

      if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                         taxDetailsResponse.setJurisdiction(null);
                     }else{
                        commercetax.JurisdictionResponse jurisdiction = new commercetax.JurisdictionResponse();
                        jurisdiction.setCountry('country');
                        jurisdiction.setRegion('region');                         
                        jurisdiction.setName('name');
                        jurisdiction.setStateAssignedNumber('stateAssignedNo');
                        jurisdiction.setId('id');
                        jurisdiction.setLevel('level');
                        taxDetailsResponse.setJurisdiction(jurisdiction);                     
}
```

  

- 
**[JurisdictionResponse Methods](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_methods)**  

Learn more about the available methods with the `JurisdictionResponse` class.

  

## JurisdictionResponse Methods

  
  
  
Learn more about the available methods with the `JurisdictionResponse` class.

    
      

The `JurisdictionResponse` class includes these
        methods.

    

    
  

- 
**[setCountry(country)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setCountry)**  

Sets the Country field of the `JurisdictionResponse` class.

- 
**[setId(id)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setId)**  

Sets the ID field of the `JurisdictionResponse` class.

- 
**[setLevel(level)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setLevel)**  

Sets the Level field of the `JurisdictionResponse` class.

- 
**[setName(name)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setName)**  

Sets the Name field of the `JurisdictionResponse` class.

- 
**[setRegion(region)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setRegion)**  

Sets the Region value of the `JurisdictionResponse` class.

- 
**[setStateAssignedNumber(stateAssignedNo)](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_commercetax_JurisdictionResponse_setStateAssignedNumber)**  

Sets the StateAssignedNumber field of the `JurisdictionResponse` class.

  

### setCountry(country)

  
  
  
Sets the Country field of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setCountry(String
      country)`

    

#### Parameters

        
- 
**country**:

Type: String

The country of the tax jurisdiction entity's address.

      

    

#### Return Value

Type: void

  

  

### setId(id)

  
  
  
Sets the ID field of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setId(String
      id)`

    

#### Parameters

        
- 
**id**:

Type: String

User-defined Id value used to reference

the jurisdiction response.

      

    

#### Return Value

Type: void

  

  

### setLevel(level)

  
  
  
Sets the Level field of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setLevel(String
      level)`

    

#### Parameters

        
- 
**level**:

Type: String

Level
            value used in the jurisdiction entity's address.

      

    

#### Return Value

Type: void

  

  

### setName(name)

  
  
  
Sets the Name field of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setName(String
      name)`

    

#### Parameters

        
- 
**name**:

Type: String

Optional user-defined name field for referencing the jurisdiction response.

      

    

#### Return Value

Type: void

  

  

### setRegion(region)

  
  
  
Sets the Region value of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setRegion(String
      region)`

    

#### Parameters

        
- 
**region**:

Type: String

Region value used in the tax jurisdiction entity's address.

      

    

#### Return Value

Type: void

  

  

### setStateAssignedNumber(stateAssignedNo)

  
  
  
Sets the StateAssignedNumber field of the `JurisdictionResponse` class.

    

#### Signature

`global void
          setStateAssignedNumber(String
      stateAssignedNo)`

    

#### Parameters

        
- 
**stateAssignedNo**:

Type: String

State assigned number

value of the tax jurisdiction entity's address.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_LineItemResponse.htm ===
---
page_id: apex_class_commercetax_LineItemResponse.htm
title: LineItemResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_LineItemResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

    

# LineItemResponse Class

    
    
    
Response class that stores details of a list of one or more line
            items on which the tax engine has calculated tax.

        

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

## Example

            

This example uses a `LineItemResponse` list to store
                information about each line item that was processed as part of the request. For
                simplicity, the sample code uses a static value of 1 for the tax rate. However, most
                integrations typically have a more complex process for determining a tax rate. Most
                integrations also build a `TaxDetailsResponse` list
                to store the actual tax value information that they assign to each line item in the
                    `LineItemResponse` list.

            Double totalTax = 0.0;
             Double totalAmount = 0.0;
             List<commercetax.LineItemResponse> lineItemResponses = new List<commercetax.LineItemResponse>();
             for(Commercetax.TaxLineItemRequest lineItem : request.lineItems){
                 commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();
                 if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                     addressesRes.setShipFrom(null);
                     addressesRes.setShipTO(null);
                     addressesRes.setSoldTo(null);
                 }else{
                     commercetax.AddressResponse addRes = new commercetax.AddressResponse();
                     addRes.setLocationCode('locationCode');
                     addressesRes.setShipFrom(addRes);
                     addressesRes.setShipTO(addRes);
                     addressesRes.setSoldTo(addRes);
                 }
                 commercetax.LineItemResponse lineItemResponse = new commercetax.LineItemResponse();
                 Double totalLineTax = 0;
                 List<commercetax.TaxDetailsResponse> taxDetailsResponses = new List<commercetax.TaxDetailsResponse>();
                 for(integer i =0;i<1;i++){
                     Integer rate  = 1;
                     Double taxableAmount = lineItem.amount;
                     commercetax.TaxDetailsResponse taxDetailsResponse = new commercetax.TaxDetailsResponse();
                     taxDetailsResponse.setRate(Double.valueOf(rate));
                     taxDetailsResponse.setTaxableAmount(taxableAmount);
                     Double tax = taxableAmount*rate;
                     totalLineTax+=tax;
                     taxDetailsResponse.setTax(taxableAmount*rate);
                     taxDetailsResponse.setExemptAmount(0);
                     taxDetailsResponse.setExemptReason('exemptReason');
                     taxDetailsResponse.setTaxRegionId('taxRegionId');
                     taxDetailsResponse.setTaxId(String.valueOf(getRandomInteger(0,2323233)));
                     taxDetailsResponse.setSerCode('serCode');
                     taxDetailsResponse.setTaxAuthorityTypeId('taxAuthorityTypeId');
                     if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                         taxDetailsResponse.setImposition(null);
                     }else{
                         commercetax.ImpositionResponse imposition = new commercetax.ImpositionResponse();
                         imposition.setSubType('subtype');
                         imposition.setType('type');
                         taxDetailsResponse.setImposition(imposition);
                     }
 
                     if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                         taxDetailsResponse.setJurisdiction(null);
                     }else{
                         commercetax.JurisdictionResponse jurisdiction = new commercetax.JurisdictionResponse();
                         jurisdiction.setCountry('country');
                         jurisdiction.setRegion('region');
                         jurisdiction.setName('name');
                         jurisdiction.setStateAssignedNumber('stateAssignedNo');
                         jurisdiction.setId('id');
                         jurisdiction.setLevel('level');
                         taxDetailsResponse.setJurisdiction(jurisdiction);
                     }
 
                     taxDetailsResponses.add(taxDetailsResponse);
                 }
                 lineItemResponse.setTaxes(taxDetailsResponses);
                 totalTax +=totalLineTax;
                 totalAmount+=lineItem.amount;
```

    

- 
**[LineItemResponse Methods](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_methods)**  

Learn more about the available methods with the `LineItemResponse` class.

  

## LineItemResponse Methods

  
  
  
Learn more about the available methods with the `LineItemResponse` class.

    
      

The `LineItemResponse` class includes these
        methods.

    

    
  

- 
**[setAddresses(addresses)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setAddresses)**  

Sets the Addresses field on the `LineItemResponse` using an instance of `AddressesResponse` class.

- 
**[setAmountDetails(amountDetails)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setAmountDetails)**  

Sets the Amount Details field on the `LineItemResponse` using an instance of `AmountDetails`.

- 
**[setCustomTaxAttributes(customTaxAttributes)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setCustomTaxAttributes)**  

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax       response at line item level.

- 
**[setEffectiveDate(effectiveDate)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setEffectiveDate)**  

Sets the EffectiveDate field on the `LineItemResponse` class. Effective Date fields are optional fields that store the       date that a transaction takes effect. We provide these fields only for recordkeeping purposes       – for example, if you must report an effective date to an external general ledger       system. Salesforce doesn't use them to calculate any tax or payment values.

- 
**[setIsTaxable(isTaxable)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setIsTaxable)**  

Sets the IsTaxable field on the `LineItemResponse` class.

- 
**[setLineNumber(lineNumber)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setLineNumber)**  

Sets the LineNumber field on the `LineItemResponse` class.

- 
**[setProductCode(productCode)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setProductCode)**  

Sets the ProductCode field on the `LineItemResponse` class.

- 
**[setQuantity(quantity)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setQuantity)**  

Sets the Quantity field on the `LineItemResponse` class.

- 
**[setTaxCode(taxCode)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setTaxCode)**  

Sets the TaxCode field on the `LineItemResponse`.

- 
**[setTaxes(taxes)](./apex_class_commercetax_LineItemResponse.htm.md#apex_commercetax_LineItemResponse_setTaxes)**  

Sets the Taxes field on a `LineItemResponse`.

  

### setAddresses(addresses)

  
  
  
Sets the Addresses field on the `LineItemResponse` using an instance of `AddressesResponse` class.

    

#### Signature

`global void setAddresses(commercetax.AddressesResponse
          addresses)`

    

#### Parameters

        
- 
**addresses**:

Type: [AddressesResponse](./apex_class_commercetax_AddressesResponse.htm.md#apex_class_commercetax_AddressesResponse)

Class that contains methods to set the Ship To, Ship From, and Sold To address
            information.

      

    

#### Return Value

Type: void

  

  

### setAmountDetails(amountDetails)

  
  
  
Sets the Amount Details field on the `LineItemResponse` using an instance of `AmountDetails`.

    

#### Signature

`global void setAmountDetails(commercetax.AmountDetailsResponse
          amountDetails)`

    

#### Parameters

        
- 
**amountDetails**:

Type: [AmountDetailsResponse](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_class_commercetax_AmountDetailsResponse)

Class that contains methods to set the tax amount, total amount with tax, total
            amount, and exempt amount.

      

    

#### Return Value

Type: void

  

  

### setCustomTaxAttributes(customTaxAttributes)

  
  
  
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax
      response at line item level.

    

#### Signature

      
      

`global void
          setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse
          customTaxAttributes)`

      
    

    

#### Parameters

      
      
        
- 
**customTaxAttributes**:

Type: [CustomTaxAttributesResponse](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_class_commercetax_CustomTaxAttributesResponse)

Additional

data or custom attributes to include in the tax response.

      

    

    

#### Return Value

      
      

Type: void

    

  

  

### setEffectiveDate(effectiveDate)

  
  
  
Sets the EffectiveDate field on the `LineItemResponse` class. Effective Date fields are optional fields that store the
      date that a transaction takes effect. We provide these fields only for recordkeeping purposes
      – for example, if you must report an effective date to an external general ledger
      system. Salesforce doesn't use them to calculate any tax or payment values.

    

#### Signature

`global void
          setEffectiveDate(Datetime
      effectiveDate)`

    

#### Parameters

        
- 
**effectiveDate**:

Type: Datetime

Optional field that stores the date that a transaction takes effect.

      

    

#### Return Value

Type: void

  

  

### setIsTaxable(isTaxable)

  
  
  
Sets the IsTaxable field on the `LineItemResponse` class.

    

#### Signature

`global void
          setIsTaxable(Boolean
      isTaxable)`

    

#### Parameters

        
- 
**isTaxable**:

Type: Boolean

Whether line items were taxed as part of the tax calculation request.

      

    

#### Return Value

Type: void

  

  

### setLineNumber(lineNumber)

  
  
  
Sets the LineNumber field on the `LineItemResponse` class.

    

#### Signature

`global void
          setLineNumber(String
      lineNumber)`

    

#### Parameters

        
- 
**lineNumber**:

Type: String

User-defined number used to identify

a line item.

      

    

#### Return Value

Type: void

  

  

### setProductCode(productCode)

  
  
  
Sets the ProductCode field on the `LineItemResponse` class.

    

#### Signature

`global void
          setProductCode(String
      productCode)`

    

#### Parameters

        
- 
**productCode**:

Type: String

Code

for the product that a line item represents.

      

    

#### Return Value

Type: void

  

  

### setQuantity(quantity)

  
  
  
Sets the Quantity field on the `LineItemResponse` class.

    

#### Signature

`global void
          setQuantity(Double
      quantity)`

    

#### Parameters

        
- 
**quantity**:

Type: Double

Quantity of a line item.

      

    

#### Return Value

Type: void

  

  

### setTaxCode(taxCode)

  
  
  
Sets the TaxCode field on the `LineItemResponse`.

    

#### Signature

`global void
          setTaxCode(String
      taxCode)`

    

#### Parameters

        
- 
**taxCode**:

Type: String

Federal code that an individual or business uses to pay their taxes to a federal or
            state government. The tax engine uses this code during the tax calculation process.

      

    

#### Return Value

Type: void

  

  

### setTaxes(taxes)

  
  
  
Sets the Taxes field on a `LineItemResponse`.

    

#### Signature

`global void setTaxes(List<commercetax.TaxDetailsResponse>
          taxes)`

    

#### Parameters

        
- 
**taxes**:

Type: List<[TaxDetailsResponse](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_class_commercetax_TaxDetailsResponse)>

Tax values applied to a line item in the `LineItemResponse` list. This information is stored in a list of `TaxDetailsResponses`, which contains values such as tax,
            taxable amount, and tax rate.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_LineTaxAddressesRequest.htm ===
---
page_id: apex_class_commercetax_LineTaxAddressesRequest.htm
title: LineTaxAddressesRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_LineTaxAddressesRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# LineTaxAddressesRequest Class

  
  
  
Stores details of the addresses applied per line item in a tax
      calculation request.

    

## Namespace

      
      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

  

- 
**[LineTaxAddressesRequest Constructors](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_constructors)**  

Learn more about the constructors available with the `LineTaxAddressesRequest` class.

- 
**[LineTaxAddressesRequest Properties](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_properties)**  

Learn more about the available properties with the `LineTaxAddressesRequest` class.

- 
**[LineTaxAddressesRequest Methods](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_methods)**  

Learn more about the available methods with the `LineTaxAddressesRequest` class.

  

## LineTaxAddressesRequest Constructors

  
  
  
Learn more about the constructors available with the `LineTaxAddressesRequest` class.

    
      

The `LineTaxAddressesRequest` class includes these
        constructors.

    

    
  

- 
**[LineTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_ctor)**  

Constructor for initializing the required addresses for a line             item of the tax addresses request such as the ship to, ship from, and bill to             addresses.             This constructor is intended for test usage and throws an exception if used outside of             the Apex test context.

    

### LineTaxAddressesRequest(shipFrom, shipTo, soldTo, billTo,
            taxEngineAddress)

    
    
    
Constructor for initializing the required addresses for a line
            item of the tax addresses request such as the ship to, ship from, and bill to
            addresses.
            This constructor is intended for test usage and throws an exception if used outside of
            the Apex test context.

        

#### Signature

`global LineTaxAddressesRequest(commercetax.TaxAddressRequest
                    shipFrom, commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest
                    soldTo, commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest
                    taxEngineAddress)`

        

#### Parameters

                
- 
**shipFrom**: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest) Address where a line item was shipped from.

                
- 
**shipTo**: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest) Address where a line item is shipped to.

                
- 
**soldTo**: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest) Address of the line item's buyer.

                
- 
**billTo**: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest) Person or group who was billed for the line item.

                
- 
**taxEngineAddress**: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest) Address that the tax engine uses to calculate tax.

            

    

  

## LineTaxAddressesRequest Properties

  
  
  
Learn more about the available properties with the `LineTaxAddressesRequest` class.

    
      

The `LineTaxAddressesRequest` class includes these
        properties.

    

    
  

- 
**[billTo](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_billTo)**  

The Bill To address for a line item.

- 
**[shipFrom](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_shipFrom)**  

The Ship From address for a line item.

- 
**[shipTo](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_shipTo)**  

The Ship To address for a line item.

- 
**[soldTo](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_soldTo)**  

The Sold To address for a line item.

  

### billTo

  
  
  
The Bill To address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest billTo {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest)

  

  

### shipFrom

  
  
  
The Ship From address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest shipFrom {get;
        set;}`

    

#### Property Value

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### shipTo

  
  
  
The Ship To address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest shipTo {get;
        set;}`

    

#### Property Value

      

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### soldTo

  
  
  
The Sold To address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest soldTo {get;
        set;}`

    

#### Property Value

      

Type: [TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

## LineTaxAddressesRequest Methods

  
  
  
Learn more about the available methods with the `LineTaxAddressesRequest` class.

    
      

The `LineTaxAddressesRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_equals)**  

Maintains the integrity of lists of type `LineTaxAddressesRequest` by determining the equality of external objects in a list.       This method is dynamic and is based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_hashCode)**  

Maintains the integrity of lists of type `LineTaxAddressesRequest` by determining the uniquness of the external object       records in a list.

- 
**[toString()](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_commercetax_LineTaxAddressesRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `LineTaxAddressesRequest` by determining the equality of external objects in a list.
      This method is dynamic and is based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose
            key
            is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `LineTaxAddressesRequest` by determining the uniquness of the external object
      records in a list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_RuleDetailsResponse.htm ===
---
page_id: apex_class_commercetax_RuleDetailsResponse.htm
title: RuleDetailsResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_RuleDetailsResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# RuleDetailsResponse Class

  
  
  
Contains details about the tax rules used for tax
    calculation.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
    
  

- 
**[RuleDetailsResponse Methods](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_methods)**  

Learn more about the available methods with the `RuleDetailsResponse` class.

  

## RuleDetailsResponse Methods

  
  
  
Learn more about the available methods with the `RuleDetailsResponse` class.

    
      

The `RuleDetailsResponse` includes these methods.

    

    
  

- 
**[RuleDetailsResponse()](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_RuleDetailsResponse)**  

Contains information about the tax rules used when calculating tax       for line items.

- 
**[setNonTaxableRuleId(nonTaxableRuleId)](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_setNonTaxableRuleId)**  

Sets the NonTaxableRuleId field of the `RuleDetailsResponse`.

- 
**[setNonTaxableType(nonTaxableType)](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_setNonTaxableType)**  

Sets the NonTaxableType field of the `RuleDetailsResponse`.

- 
**[setRateRuleId(rateRuleId)](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_setRateRuleId)**  

Sets the RateRuleId field of the `RuleDetailsResponse`.

- 
**[setRateSourceId(rateSourceId)](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_commercetax_RuleDetailsResponse_setRateSourceId)**  

Sets the RateSourceId field on the `RuleDetailsResponse`.

  

### RuleDetailsResponse()

  
  
  
Contains information about the tax rules used when calculating tax
      for line items.

    

#### Signature

`global void
          RuleDetailsResponse()`

    

#### Return Value

Type: void

  

  

### setNonTaxableRuleId(nonTaxableRuleId)

  
  
  
Sets the NonTaxableRuleId field of the `RuleDetailsResponse`.

    

#### Signature

`global void
          setNonTaxableRuleId(String
      nonTaxableRuleId)`

    

#### Parameters

        
- 
**nonTaxableRuleId**:

Type: String

ID of the tax rule applied to non-taxable line items.

      

    

#### Return Value

Type: void

  

  

### setNonTaxableType(nonTaxableType)

  
  
  
Sets the NonTaxableType field of the `RuleDetailsResponse`.

    

#### Signature

`global void
          setNonTaxableType(String
      nonTaxableType)`

    

#### Parameters

        
- 
**nonTaxableType**:

Type: String

Reason
            (from
            several possible types) that a line item is non-taxable.

      

    

#### Return Value

Type: void

  

  

### setRateRuleId(rateRuleId)

  
  
  
Sets the RateRuleId field of the `RuleDetailsResponse`.

    

#### Signature

`global void
          setRateRuleId(String
      rateRuleId)`

    

#### Parameters

        
- 
**rateRuleId**:

Type: String

ID of the tax rule used to determine a tax rate.

      

    

#### Return Value

Type: void

  

  

### setRateSourceId(rateSourceId)

  
  
  
Sets the RateSourceId field on the `RuleDetailsResponse`.

    

#### Signature

`global void
          setRateSourceId(String
      rateSourceId)`

    

#### Parameters

        
- 
**rateSourceId**:

Type: String

ID of the source object used for calculating tax rate.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_TaxAddressRequest.htm ===
---
page_id: apex_class_commercetax_TaxAddressRequest.htm
title: TaxAddressRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxAddressRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxAddressRequest Class

  
  
  
Contains address details used for tax calculation.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
  

- 
**[TaxAddressRequest Constructors](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_constructors)**  

Learn more about the available constructors with the `TaxAddressRequest` class.

- 
**[TaxAddressRequest Properties](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_properties)**  

Learn more about the available properties with the `TaxAddressRequest` class.

- 
**[TaxAddressRequest Methods](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_methods)**  

Learn more about the available methods with the `TaxAddressRequest` class.

  

## TaxAddressRequest Constructors

  
  
  
Learn more about the available constructors with the `TaxAddressRequest` class.

    
      

The `TaxAddressRequest` class includes these
        constructors.

    

    
  

- 
**[TaxAddressRequest(city, country, latitude, longitude, postalCode, state, street, locationCode)](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_ctor)**  

Initializes the `TaxAddressRequest`       object using address details. This constructor is intended for test usage and throws an       exception if used outside of the Apex test context.

  

### TaxAddressRequest(city, country, latitude, longitude,
      postalCode, state, street, locationCode)

  
  
  
Initializes the `TaxAddressRequest`
      object using address details. This constructor is intended for test usage and throws an
      exception if used outside of the Apex test context.

    

#### Signature

`global TaxAddressRequest(String city, String country, Double
          latitude, Double longitude, String postalCode, String state, String street, String
          locationCode)`

    

#### Parameters

        
- 
**city**:

Type: String

City used in an address, which is required for tax calculation.

        
- 
**country**:

Type: String

Country used in an address, which is required for tax calculation.

        
- 
**latitude**:

Type: Double

Latitude used in an address, which is required for tax calculation.

        
- 
**longitude**:

Type: Double

Longitude used in an address, which is required for tax calculation.

        
- 
**postalCode**:

Type: String

Postal code used in an address, which is required for tax calculation.

        
- 
**state**:

Type: String

State used in an address, which is required for tax calculation.

        
- 
**street**:

Type: String

Street used in an address, which is required for tax calculation.

        
- 
**locationCode**:

Type: String

Location code used in an address, which is required for tax calculation.

      

  

  

## TaxAddressRequest Properties

  
  
  
Learn more about the available properties with the `TaxAddressRequest` class.

    
      

The `TaxAddressRequest` class includes these
        properties.

    

    
  

- 
**[city](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_city)**  

City used in an address, which is required for tax     calculation.

- 
**[country](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_country)**  

Country used in an address, which is required for tax       calculation.

- 
**[countryCode](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_countryCode)**  

Country code used in an address, which is required for tax       calculation.

- 
**[latitude](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_latitude)**  

Latitude used in an address, which is required for tax       calculation.

- 
**[locationCode](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_locationCode)**  

Location code used in an address, which is required for tax       calculation.

- 
**[longitude](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_longitude)**  

Longitude used in an address, which is required for tax       calculation.

- 
**[postalCode](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_postalCode)**  

Postal code used in an address, which is required for tax       calculation.

- 
**[state](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_state)**  

State used in an address, which is required for tax       calculation.

- 
**[stateCode](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_stateCode)**  

State code used in an address, which is required for tax       calculation.

- 
**[street](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_street)**  

Street used in an address, which is required for tax       calculation.

  

### city

  
  
  
City used in an address, which is required for tax
    calculation.

    

#### Signature

`global String city
          {get;
      set;}`

    

#### Property Value

Type: String

  

  

### country

  
  
  
Country used in an address, which is required for tax
      calculation.

    

#### Signature

`global String
          country {get;
      set;}`

    

#### Property Value

Type: String

  

  

### countryCode

  
  
  
Country code used in an address, which is required for tax
      calculation.

    

#### Signature

      
      

`global String countryCode {get; set;}`

      
    

    

#### Property Value

      
      

Type: String

    

  

  

### latitude

  
  
  
Latitude used in an address, which is required for tax
      calculation.

    

#### Signature

`global Double
          latitude {get;
      set;}`

    

#### Property Value

Type: Double

  

  

### locationCode

  
  
  
Location code used in an address, which is required for tax
      calculation.

    

#### Signature

`global String
          locationCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### longitude

  
  
  
Longitude used in an address, which is required for tax
      calculation.

    

#### Signature

`global Double
          longitude {get;
      set;}`

    

#### Property Value

Type: Double

  

  

### postalCode

  
  
  
Postal code used in an address, which is required for tax
      calculation.

    

#### Signature

`global String
          postalCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### state

  
  
  
State used in an address, which is required for tax
      calculation.

    

#### Signature

`global String state
          {get;
      set;}`

    

#### Property Value

Type: String

  

  

### stateCode

  
  
  
State code used in an address, which is required for tax
      calculation.

    

#### Signature

      
      

`global String stateCode {get; set;}`

      
    

    

#### Property Value

      
      

Type: String

    

  

  

### street

  
  
  
Street used in an address, which is required for tax
      calculation.

    

#### Signature

`global String street
          {get;
      set;}`

    

#### Property Value

Type: String

  

  

## TaxAddressRequest Methods

  
  
  
Learn more about the available methods with the `TaxAddressRequest` class.

    
      

The `TaxAddressRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_equals)**  

Maintains the integrity of lists of type TaxAddressRequest by       determining the equality of external objects in a list. This method is dynamic and based on       the `equals()` method in Java.

- 
**[hashCode()](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_hashCode)**  

Maintains the integrity of lists of type `TaxAddressRequest` by determining the uniqueness of the external object in a       list.

- 
**[toString()](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_commercetax_TaxAddressRequest_toString)**  

Converts a date to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type TaxAddressRequest by
      determining the equality of external objects in a list. This method is dynamic and based on
      the `equals()` method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose
            key
            is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxAddressRequest` by determining the uniqueness of the external object in a
      list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a date to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_TaxAddressesRequest.htm ===
---
page_id: apex_class_commercetax_TaxAddressesRequest.htm
title: TaxAddressesRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxAddressesRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxAddressesRequest Class

  
  
  
Contains methods to get and set tax address values.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
  

- 
**[TaxAddressesRequest Constructors](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_constructors)**  

Learn more about the available constructors with the `TaxAddressesRequest` class.

- 
**[TaxAddressesRequest Properties](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_properties)**  

Learn more about the available properties with the `TaxAddressesRequest` class.

- 
**[TaxAddressesRequest Methods](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_methods)**  

Learn more about the available methods with the `TaxAddressesRequest` class.

  

## TaxAddressesRequest Constructors

  
  
  
Learn more about the available constructors with the `TaxAddressesRequest` class.

    
      

The `TaxAddressesRequest` class includes these
        constructors.

    

    
  

- 
**[TaxAddressesRequest(shipFrom, shipTo, soldTo, billTo, taxEngineAddress)](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_ctor)**  

Constructor for defining addresses for the tax addresses request.       This constructor is intended for test usage and throws an exception if used outside of the       Apex test context.

  

### TaxAddressesRequest(shipFrom, shipTo, soldTo, billTo,
      taxEngineAddress)

  
  
  
Constructor for defining addresses for the tax addresses request.
      This constructor is intended for test usage and throws an exception if used outside of the
      Apex test context.

    

#### Signature

`global TaxAddressesRequest(commercetax.TaxAddressRequest shipFrom,
          commercetax.TaxAddressRequest shipTo, commercetax.TaxAddressRequest soldTo,
          commercetax.TaxAddressRequest billTo, commercetax.TaxAddressRequest
          taxEngineAddress)`

    

#### Parameters

      
      
        
- 
**shipFrom**: [TaxAddressRequest](#apex_class_commercetax_TaxAddressesRequest) The address where a line item was shipped from.

        
- 
**shipTo**: [TaxAddressRequest](#apex_class_commercetax_TaxAddressesRequest) The address where a line item is shipped to.

        
- 
**soldTo**: [TaxAddressRequest](#apex_class_commercetax_TaxAddressesRequest) The address of the line item's buyer.

        
- 
**billTo**: [TaxAddressRequest](#apex_class_commercetax_TaxAddressesRequest) The person or group who was billed for the line item.

        
- 
**taxEngineAddress**: [TaxAddressRequest](#apex_class_commercetax_TaxAddressesRequest) The address that the tax engine uses to calculate tax.

      

    

  

  

## TaxAddressesRequest Properties

  
  
  
Learn more about the available properties with the `TaxAddressesRequest` class.

    
      

The `TaxAddressesRequest` class includes these
        properties.

    

    
  

- 
**[billTo](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_billTo)**  

The Bill To address for a line item.

- 
**[shipFrom](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_shipFrom)**  

The Ship From address for a line item.

- 
**[shipTo](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_shipTo)**  

The Ship To address for a line item.

- 
**[soldTo](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_soldTo)**  

The Sold To address for a line item.

- 
**[taxEngineAddress](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_taxEngineAddress)**  

The Tax Engine Address for a line item.

  

### billTo

  
  
  
The Bill To address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest billTo {get;
        set;}`

    

#### Property Value

      

[TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### shipFrom

  
  
  
The Ship From address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest shipFrom {get;
        set;}`

    

#### Property Value

      

[TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### shipTo

  
  
  
The Ship To address for a line item.

    

#### Signature

`public commercetax.TaxAddressRequest shipTo {get;
        set;}`

    

#### Property Value

      

[TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### soldTo

  
  
  
The Sold To address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest soldTo {get;
        set;}`

    

#### Property Value

[TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

### taxEngineAddress

  
  
  
The Tax Engine Address for a line item.

    

#### Signature

`global commercetax.TaxAddressRequest taxEngineAddress {get;
          set;}`

    

#### Property Value

      

[TaxAddressRequest](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)

  

  

## TaxAddressesRequest Methods

  
  
  
Learn more about the available methods with the `TaxAddressesRequest` class.

    
      

The `TaxAddressesRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_equals)**  

Maintains the integrity of lists of type `TaxAddressesRequest` by determining the equality of external objects in a list.       This method is dynamic and is based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_hashCode)**  

Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external object records       in a list.

- 
**[toString()](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_commercetax_TaxAddressesRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `TaxAddressesRequest` by determining the equality of external objects in a list.
      This method is dynamic and is based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose
            key
            is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxAddressesRequest` by determining the uniqueness of the external object records
      in a list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_TaxApiException.htm ===
---
page_id: apex_class_commercetax_TaxApiException.htm
title: TaxApiException Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxApiException.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxApiException Class

  
  
  
Contains details about any exceptions during the tax calculation
      process. Extends the `ApexBaseException`
    class.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
  

- 
**[TaxApiException Constructors](./apex_class_commercetax_TaxApiException.htm.md#apex_commercetax_TaxApiException_constructors)**  

Learn more about the available constructors with the `TaxApiException` class.

  

## TaxApiException Constructors

  
  
  
Learn more about the available constructors with the `TaxApiException` class.

    
      

The `TaxApiException` class includes these
        constructors.

    

    
  

- 
**[TaxApiException(var1, var2)](./apex_class_commercetax_TaxApiException.htm.md#apex_commercetax_TaxApiException_ctor)**  

Initializes the `TaxApiException`       class using an `Exception` and a string to provide more       details about the exception. This constructor is intended for test usage and throws an       exception if used outside of the Apex test context.

- 
**[TaxApiException(var1)](./apex_class_commercetax_TaxApiException.htm.md#apex_commercetax_TaxApiException_ctor_2)**  

Initializes the `TaxApiException`       class using an `Exception`. This constructor is intended for       test usage and throws an exception if used outside of the Apex test context.

- 
**[TaxApiException()](./apex_class_commercetax_TaxApiException.htm.md#apex_commercetax_TaxApiException_ctor_3)**  

Initializes the `TaxApiException`       class without any initialized parameters. This constructor is intended for test usage and       throws an exception if used outside of the Apex test context.

  

### TaxApiException(var1,
      var2)

  
  
  
Initializes the `TaxApiException`
      class using an `Exception` and a string to provide more
      details about the exception. This constructor is intended for test usage and throws an
      exception if used outside of the Apex test context.

    

#### Signature

`global
          TaxApiException(String var1, Exception
      var2)`

    

#### Parameters

        
- 
**var1**:

Type: String

Text that provides more information about

the returned exception.

        
- 
**var2**:

Type: [Exception](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

An exception denotes an error that disrupts the normal flow of code execution. You can
            use Apex built-in exceptions or create custom exceptions. All exceptions have common
            methods.

      

  

  

### TaxApiException(var1)

  
  
  
Initializes the `TaxApiException`
      class using an `Exception`. This constructor is intended for
      test usage and throws an exception if used outside of the Apex test context.

    

#### Signature

`global
          TaxApiException(Exception
      var1)`

    

#### Parameters

        
- 
**var1**:

Type: [Exception](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

An exception denotes an error that disrupts the normal flow of code execution. You can
            use Apex built-in exceptions or create custom exceptions. All exceptions have common
            methods.

      

  

  

### TaxApiException()

  
  
  
Initializes the `TaxApiException`
      class without any initialized parameters. This constructor is intended for test usage and
      throws an exception if used outside of the Apex test context.

    

#### Signature

`global
          TaxApiException()`

=== ARTICLE: apex_class_commercetax_TaxCustomerDetailsRequest.htm ===
---
page_id: apex_class_commercetax_TaxCustomerDetailsRequest.htm
title: TaxCustomerDetailsRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxCustomerDetailsRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxCustomerDetailsRequest Class

  
  
  
Contains customer details used in tax calculation.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
  

- 
**[TaxCustomerDetailsRequest Constructors](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_constructors)**  

Learn more about the available constructors with the `TaxCustomerDetailsRequest` class.

- 
**[TaxCustomerDetailsRequest Properties](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_properties)**  

Learn more about the available properties with the `TaxCustomerDetailsRequest` class.

- 
**[TaxCustomerDetailsRequest Methods](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_methods)**  

Learn more about the available methods with the `TaxCustomerDetailsRequest` class.

  

## TaxCustomerDetailsRequest Constructors

  
  
  
Learn more about the available constructors with the `TaxCustomerDetailsRequest` class.

    
      

The `TaxCustomerDetailsRequest` class includes these
        constructors.

    

    
  

- 
**[TaxCustomerDetailsRequest(accountId, code, exemptionNo, exemptionReason)](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_ctor)**  

Initializes the `TaxCustomerDetailsRequest` object. This constructor is intended for test usage and       throws an exception if used outside of the Apex test context.

  

### TaxCustomerDetailsRequest(accountId, code, exemptionNo,
      exemptionReason)

  
  
  
Initializes the `TaxCustomerDetailsRequest` object. This constructor is intended for test usage and
      throws an exception if used outside of the Apex test context.

    

#### Signature

`global
          TaxCustomerDetailsRequest(String accountId, String code, String exemptionNo, String
          exemptionReason)`

    

#### Parameters

        
- 
**accountId**:

Type: String

The customer account
            ID
            for the line items sent for tax calculation.

        
- 
**code**:

Type: String

The
            tax
            code used during tax calculation.

        
- 
**exemptionNo**:

Type: String

The
            exemption
            number applied to any tax exempt line items.

        
- 
**exemptionReason**:

Type: String

The reason that certain line items are tax exempt.

        
- 
**taxCertificateId**:

Type: String

ID of the tax certificate used in tax calculation.

      

  

  

## TaxCustomerDetailsRequest Properties

  
  
  
Learn more about the available properties with the `TaxCustomerDetailsRequest` class.

    
      

The `TaxCustomerDetailsRequest` class includes these
        properties.

    

    
  

- 
**[accountId](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_accountId)**  

Customer account that contains the line items sent for tax       calculation.

- 
**[code](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_code)**  

Tax       code used during tax calculation.

- 
**[exemptionNo](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_exemptionNo)**  

Number used to qualify a line item for tax     exemption.

- 
**[exemptionReason](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_exemptionReason)**  

Reason why a line item qualifies for tax exemption.

- 
**[taxCertificateId](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_taxCertificateId)**  

 ID of a tax certificate used for tax calculation.

  

### accountId

  
  
  
Customer account that contains the line items sent for tax
      calculation.

    

#### Signature

`global String
          accountId {get;
      set;}`

    

#### Property Value

Type: String

  

  

### code

  
  
  
Tax
      code used during tax calculation.

    

#### Signature

`global String code
          {get;
      set;}`

    

#### Property Value

Type: String

  

  

### exemptionNo

  
  
  
Number used to qualify a line item for tax
    exemption.

    

#### Signature

`global String
          exemptionNo {get;
      set;}`

    

#### Property Value

Type: String

  

  

### exemptionReason

  
  
  
Reason why a line item qualifies for tax exemption.

    

#### Signature

`global String
          exemptionReason {get;
      set;}`

    

#### Property Value

Type: String

  

  

### taxCertificateId

  
  
  
 ID of a tax certificate used for tax calculation.

    

#### Signature

`global String
          taxCertificateId {get;
      set;}`

    

#### Property Value

Type: String

  

  

## TaxCustomerDetailsRequest Methods

  
  
  
Learn more about the available methods with the `TaxCustomerDetailsRequest` class.

    
      

The `TaxCustomerDetailsRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_equals)**  

Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the equality of external objects in a       list. This method is dynamic and based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_hashCode)**  

Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the uniqueness of the external objects in       a list.

- 
**[toString()](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_commercetax_TaxCustomerDetailsRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the equality of external objects in a
      list. This method is dynamic and based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose
            key
            is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxCustomerDetailsRequest` by determining the uniqueness of the external objects in
      a list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_TaxDetailsResponse.htm ===
---
page_id: apex_class_commercetax_TaxDetailsResponse.htm
title: TaxDetailsResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxDetailsResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

    

# TaxDetailsResponse Class

    
    
    
Stores details of the tax values that an external tax engine
            calculates in response to a tax calculation request.

        

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

## Usage

If your tax calculation request contains multiple line items,
            we recommend building your adapter using a list of `TaxDetailsResponse` instances. Each instance represents the tax details
            calculated for a given line item.

        

## Example

            List<commercetax.TaxDetailsResponse> taxDetailsResponses = new List<commercetax.TaxDetailsResponse>();
                 for(integer i =0;i<1;i++){
                     Integer rate  = 1;
                     Double taxableAmount = lineItem.amount;
                     commercetax.TaxDetailsResponse taxDetailsResponse = new commercetax.TaxDetailsResponse();
                     taxDetailsResponse.setRate(Double.valueOf(rate));
                     taxDetailsResponse.setTaxableAmount(taxableAmount);
                     Double tax = taxableAmount*rate;
                     totalLineTax+=tax;
                     taxDetailsResponse.setTax(taxableAmount*rate);
                     taxDetailsResponse.setExemptAmount(0);
                     taxDetailsResponse.setExemptReason('exemptReason');
                     taxDetailsResponse.setTaxRegionId('taxRegionId');
                     taxDetailsResponse.setTaxId(String.valueOf(getRandomInteger(0,2323233)));
                     taxDetailsResponse.setSerCode('serCode');
                     taxDetailsResponse.setTaxAuthorityTypeId('taxAuthorityTypeId');
                     if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                         taxDetailsResponse.setImposition(null);
                     }else{
                         commercetax.ImpositionResponse imposition = new commercetax.ImpositionResponse();
                         imposition.setSubType('subtype');
                         imposition.setType('type');
                         taxDetailsResponse.setImposition(imposition);
                     }
 
                     if(request.DocumentCode == 'SetsNullForResponseWithoutException'){
                         taxDetailsResponse.setJurisdiction(null);
                     }else{
                         commercetax.JurisdictionResponse jurisdiction = new commercetax.JurisdictionResponse();
                         jurisdiction.setCountry('country');
                         jurisdiction.setRegion('region');
                         jurisdiction.setName('name');
                         jurisdiction.setStateAssignedNumber('stateAssignedNo');
                         jurisdiction.setId('id');
                         jurisdiction.setLevel('level');
                         taxDetailsResponse.setJurisdiction(jurisdiction);
                     }
 
                     taxDetailsResponses.add(taxDetailsResponse);
                 }
                 lineItemResponse.setTaxes(taxDetailsResponses);
                 totalTax +=totalLineTax;
                 totalAmount+=lineItem.amount;
```

    

- 
**[TaxDetailsResponse Methods](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_methods)**  

Learn more about the available methods with the `TaxDetailsResponse` class.

  

## TaxDetailsResponse Methods

  
  
  
Learn more about the available methods with the `TaxDetailsResponse` class.

    
      

The `TaxDetailsResponse` class includes these
        methods.

    

    
  

- 
**[setCustomTaxAttributes(customTaxAttributes)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setCustomTaxAttributes)**  

Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax       response at the tax line item level.

- 
**[setExemptAmount(exemptAmount)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setExemptAmount)**  

Sets the ExemptAmount field of the `TaxDetailsResponse` class.

- 
**[setExemptReason(reason)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setExemptReason)**  

Sets the ExemptReason field of the `TaxDetailsResponse` class.

- 
**[setImposition(imposition)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setImposition)**  

Sets the Imposition field of the `TaxDetailsResponse` class using an instance of the `ImpositionResponse` class.

- 
**[setJurisdiction(jurisdiction)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setJurisdiction)**  

Sets the Jurisdiction field of the `TaxDetailsResponse` using an instance of the `JurisdictionResponse` class.

- 
**[setRate(rate)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setRate)**  

Sets the Rate field of the `TaxDetailsResponse` class.

- 
**[setSerCode(serCode)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setSerCode)**  

Sets the Service Code field of the `TaxDetailsResponse` class.

- 
**[setTax(tax)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTax)**  

Sets the Tax field of the `TaxDetailsResponse` class.

- 
**[setTaxAuthorityTypeId(taxAuthorityTypeId)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTaxAuthorityTypeId)**  

Sets the TaxAuthorityTypeId field of the `TaxDetailsResponse` class.

- 
**[setTaxId(taxId)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTaxId)**  

Sets the TaxId field of the `TaxDetailsResponse` class.

- 
**[setTaxRegionId(taxRegionId)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTaxRegionId)**  

Sets the TaxRegionId field on the `TaxDetailsResponse` class.

- 
**[setTaxRuleDetails(taxRuleDetails)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTaxRuleDetails)**  

Sets the       TaxRuleDetails       field of the `TaxDetailsResponse` class.

- 
**[setTaxableAmount(taxableAmount)](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_commercetax_TaxDetailsResponse_setTaxableAmount)**  

Sets the TaxableAmount field of the `TaxDetailsResponse class`.

  

### setCustomTaxAttributes(customTaxAttributes)

  
  
  
Uses an instance of `CustomTaxAttributesResponse` class to include additional attributes in the tax
      response at the tax line item level.

    

#### Signature

      
      

`global void
          setCustomTaxAttributes(commercetax.CustomTaxAttributesResponse
          customTaxAttributes)`

      
    

    

#### Parameters

      
      
        
- 
**customTaxAttributes**:

Type: [CustomTaxAttributesResponse](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_class_commercetax_CustomTaxAttributesResponse)

Additional

data or custom attributes to include in the tax response.

      

    

    

#### Return Value

      
      

Type: void

    

  

  

### setExemptAmount(exemptAmount)

  
  
  
Sets the ExemptAmount field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setExemptAmount(Double
      exemptAmount)`

    

#### Parameters

        
- 
**exemptAmount**:

Type: Double

Amount of tax on a line item that is exempt from tax calculation.

      

    

#### Return Value

Type: void

  

  

### setExemptReason(reason)

  
  
  
Sets the ExemptReason field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setExemptReason(String
      reason)`

    

#### Parameters

        
- 
**reason**:

Type: String

Optional user-defined information on why a tax exemption applies to a line item.

      

    

#### Return Value

Type: void

  

  

### setImposition(imposition)

  
  
  
Sets the Imposition field of the `TaxDetailsResponse` class using an instance of the `ImpositionResponse` class.

    

#### Signature

`global void setImposition(commercetax.ImpositionResponse
          imposition)`

    

#### Parameters

        
- 
**imposition**:

Type: [ImpositionResponse](./apex_class_commercetax_ImpositionResponse.htm.md#apex_class_commercetax_ImpositionResponse)

Contains information about why tax was imposed on a line item.

      

    

#### Return Value

Type: void

  

  

### setJurisdiction(jurisdiction)

  
  
  
Sets the Jurisdiction field of the `TaxDetailsResponse` using an instance of the `JurisdictionResponse` class.

    

#### Signature

`global void setJurisdiction(commercetax.JurisdictionResponse
          jurisdiction)`

    

#### Parameters

        
- 
**jurisdiction**:

Type: [JurisdictionResponse](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_class_commercetax_JurisdictionResponse)

Contains address information about the tax jurisdiction used in the tax calculation
            process.

      

    

#### Return Value

Type: void

  

  

### setRate(rate)

  
  
  
Sets the Rate field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setRate(Double
      rate)`

    

#### Parameters

        
- 
**rate**:

Type: Double

Tax used during tax calculation.

This value is often a decimal amount, such as 0.1 or
            0.06, based on the applied tax percentage.

      

    

#### Return Value

Type: void

  

  

### setSerCode(serCode)

  
  
  
Sets the Service Code field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setSerCode(String
      serCode)`

    

#### Parameters

        
- 
**serCode**:

Type: String

Service code used in tax calculation.

      

    

#### Return Value

Type: void

  

  

### setTax(tax)

  
  
  
Sets the Tax field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setTax(Double
      tax)`

    

#### Parameters

        
- 
**tax**:

Type: Double

Amount of tax

for a line item.

      

    

#### Return Value

Type: void

  

  

### setTaxAuthorityTypeId(taxAuthorityTypeId)

  
  
  
Sets the TaxAuthorityTypeId field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setTaxAuthorityTypeId(String
      taxAuthorityTypeId)`

    

#### Parameters

        
- 
**taxAuthorityTypeId**:

Type: String

ID of the organization that oversees tax collection.

      

    

#### Return Value

Type: void

  

  

### setTaxId(taxId)

  
  
  
Sets the TaxId field of the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setTaxId(String
      taxId)`

    

#### Parameters

        
- 
**taxId**:

Type: String

ID value used to determine

the tax for an individual or business.

      

    

#### Return Value

Type: void

  

  

### setTaxRegionId(taxRegionId)

  
  
  
Sets the TaxRegionId field on the `TaxDetailsResponse` class.

    

#### Signature

`global void
          setTaxRegionId(String
      taxRegionId)`

    

#### Parameters

        
- 
**taxRegionId**:

Type: String

ID of the tax region used in tax calculation. A tax region represents a geographical
            area where tax is applied.

      

    

#### Return Value

Type: void

  

  

### setTaxRuleDetails(taxRuleDetails)

  
  
  
Sets the
      TaxRuleDetails
      field of the `TaxDetailsResponse` class.

    

#### Signature

`global void setTaxRuleDetails(commercetax.RuleDetailsResponse
          taxRuleDetails)`

    

#### Parameters

        
- 
**taxRuleDetails**:

Type: [RuleDetailsResponse](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_class_commercetax_RuleDetailsResponse)

Information about

the Salesforce tax rules used during tax calculation.

      

    

#### Return Value

Type: void

  

  

### setTaxableAmount(taxableAmount)

  
  
  
Sets the TaxableAmount field of the `TaxDetailsResponse class`.

    

#### Signature

`global void
          setTaxableAmount(Double
      taxableAmount)`

    

#### Parameters

        
- 
**taxableAmount**:

Type: Double

Amount that c

an be taxed on a line item.

      

    

#### Return Value

Type: void

=== ARTICLE: apex_class_commercetax_TaxEngineContext.htm ===
---
page_id: apex_class_commercetax_TaxEngineContext.htm
title: TaxEngineContext Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxEngineContext.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

    

# TaxEngineContext Class

    
    
    
Wrapper class that stores details about the type of a tax
            calculation request.

        

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

        

## Example

            

At the beginning of a tax adapter, use `TaxEngineContext` class to pass the value of a request type to an
                instance of `RequestType`.

            

```
global virtual class MockAdapter implements commercetax.TaxEngineAdapter {
 
     global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext taxEngineContext) {
         commercetax.RequestType requestType = taxEngineContext.getRequestType();
         commercetax.CalculateTaxRequest request = (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();
```

            

Build the rest of your adapter based on the type of request that you got from `TaxEngineContext` class.

            

```
if(requestType == commercetax.RequestType.CalculateTax){
             commercetax.calculatetaxtype type = request.taxtype;
             String docCode='';
             if(request.DocumentCode == 'simulateEmptyDocumentCode')
                 docCode = '';
             else if(request.DocumentCode != null)
                 docCode =request.DocumentCode;
             else if(request.ReferenceEntityId != null) docCode = request.ReferenceEntityId;
             else docCode =  String.valueOf(getRandomInteger(0,2147483647));
             commercetax.CalculateTaxResponse response = new commercetax.CalculateTaxResponse();
             if(request.isCommit == true) {
                 response.setStatus(commercetax.TaxTransactionStatus.Committed);
             } else {
                 response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);
             }
}
```

    

- 
**[TaxEngineContext Constructors](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_constructors)**  

Learn more about the available constructors with the `TaxEngineContext` class.

- 
**[TaxEngineContext Methods](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_methods)**  

Learn more about the available methods with the `TaxEngineContext` class.

  

## TaxEngineContext Constructors

  
  
  
Learn more about the available constructors with the `TaxEngineContext` class.

    
      

The `TaxEngineContext` class includes these
        constructors.

    

    
  

- 
**[TaxEngineContext(request, requestType, namedUri)](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_ctor)**  

Initializes the `TaxEngineContext`       object. This constructor is intended for test usage and throws an exception if used outside of       the Apex test context.

  

### TaxEngineContext(request, requestType,
    namedUri)

  
  
  
Initializes the `TaxEngineContext`
      object. This constructor is intended for test usage and throws an exception if used outside of
      the Apex test context.

    

#### Signature

` TaxEngineContext(commercetax.TaxEngineRequest request,
          commercetax.RequestType requestType, String namedUri)`

    

#### Parameters

        
- 
**request**:

Type: TaxEngineRequest Information about

the request.

        
- 
**requestType**:

Type: [RequestType](./apex_enum_commercetax_RequestType.htm.md)

Whether the tax request is to calculate or estimate tax.

        
- 
**namedUri**:

Type: String

URI that was called as part of the tax calculation request.

      

  

  

## TaxEngineContext Methods

  
  
  
Learn more about the available methods with the `TaxEngineContext` class.

    
      

The `TaxEngineContext` class includes these
        methods.

    

    
  

- 
**[getNamedUri()](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_getNamedUri)**  

Retrieves the value of the NamedUri field of the `TaxEngineContext` class.

- 
**[getRequest()](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_getRequest)**  

Gets the value of the `TaxEngineContext`'s Request field.

- 
**[getRequestType()](./apex_class_commercetax_TaxEngineContext.htm.md#apex_commercetax_TaxEngineContext_getRequestType)**  

Gets the value of the RequestType field of the `TaxEngineContext` class.

  

### getNamedUri()

  
  
  
Retrieves the value of the NamedUri field of the `TaxEngineContext` class.

    

#### Signature

`global String
          getNamedUri()`

    

#### Return Value

Type: String

  

  

### getRequest()

  
  
  
Gets the value of the `TaxEngineContext`'s Request field.

    

#### Signature

`global commercetax.TaxEngineRequest getRequest()`

    

#### Return Value

      
      

Type:
        TaxEngineRequest

      

An implemented instance of an external tax engine's interface for processing requests.
        We've provided the `TaxEngineRequest` interface for you to
        test within mock adapters with classes that implement it, such as [CalculateTaxRequest](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_class_commercetax_CalculateTaxRequest). However,
        don’t use it outside of a testing context.

    

  

  

### getRequestType()

  
  
  
Gets the value of the RequestType field of the `TaxEngineContext` class.

    

#### Signature

`global commercetax.RequestType getRequestType()`

    

#### Return Value

Type: [RequestType](./apex_enum_commercetax_RequestType.htm.md)

Indicates whether the calculation request was for actual or calculated tax.

=== ARTICLE: apex_class_commercetax_TaxLineItemRequest.htm ===
---
page_id: apex_class_commercetax_TaxLineItemRequest.htm
title: TaxLineItemRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxLineItemRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxLineItemRequest Class

  
  
  
Contains line item details of a tax request.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

  

- 
**[TaxLineItemRequest Constructors](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_constructors)**  

Learn more about the constructors available with the `TaxLineItemRequest` class.

- 
**[TaxLineItemRequest Properties](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_properties)**  

Learn more about the available properties with the `TaxLineItemRequest` class.

- 
**[TaxLineItemRequest Methods](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_methods)**  

Learn more about the available methods with the `TaxLineItemRequest` class.

  

## TaxLineItemRequest Constructors

  
  
  
Learn more about the constructors available with the `TaxLineItemRequest` class.

    
      

The `TaxLineItemRequest` class includes these
        constructors.

    

    
  

- 
**[TaxLineItemRequest(addresses, amount, description, productCode, quantity, lineNumber, taxCode, effectiveDate)](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_ctor)**  

Initializes the request for the tax line item. This constructor is       intended for test usage and throws an exception if used outside of the Apex test     context.

  

### TaxLineItemRequest(addresses, amount, description,
      productCode, quantity, lineNumber, taxCode, effectiveDate)

  
  
  
Initializes the request for the tax line item. This constructor is
      intended for test usage and throws an exception if used outside of the Apex test
    context.

    

#### Signature

`global TaxLineItemRequest(commercetax.LineTaxAddressesRequest
          addresses, Double amount, String description, String productCode, Double quantity, String
          lineNumber, String taxCode, Datetime effectiveDate)`

```
commercetax.TaxLineItemRequest, newinstance, [commercetax.LineTaxAddressesRequest, Double, String, String, Double, String, String, Datetime], commercetax.TaxLineItemRequest
```

    

#### Parameters

        
- 
**addresses**:

Type: [LineTaxAddressesRequest](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_class_commercetax_LineTaxAddressesRequest)

Information about

the addresses applied to each line item in a tax calculation
            request.

        
- 
**amount**:

Type: Double

Total amount (in

a given currency) represented by a line item sent for tax
            calculation.

        
- 
**description**:

Type: String

User-defined description

for a tax line item.

        
- 
**productCode**:

Type: String

Catalog code

for the product represented by the tax line item.

        
- 
**quantity**:

Type: Double

Number of units of a given product that the tax line item represents.

        
- 
**lineNumber**:

Type: String

Unique number used to identify a tax line item.

        
- 
**taxCode**:

Type: String

Code used to identify how tax is calculated

for a tax line item.

        
- 
**effectiveDate**:

Type: Datetime

This is a user-defined date used for reporting only. For negative invoice lines, this
            parameter represents the invoice date from the original invoice. In other cases, it
            represents the date when the tax transaction takes effect on the line item. The previous
            tax transaction type is always `Debit` for negative
            invoice lines.

      

  

  

## TaxLineItemRequest Properties

  
  
  
Learn more about the available properties with the `TaxLineItemRequest` class.

    
      

The `TaxLineItemRequest` class includes these
        properties.

    

    
  

- 
**[addresses](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_addresses)**  

Contains the list of addresses of a line item.

- 
**[amount](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_amount)**  

Total amount (in a given currency) represented by a line item sent       for tax calculation.

- 
**[customTaxAttributes](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_customTaxAttributes)**  

Customised tax contract to include additional attributes at the line       item level.

- 
**[description](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_description)**  

User-defined description for a tax line item.

- 
**[effectiveDate](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_effectiveDate)**  

The date that a tax transaction takes effect on a line item. This is       a user-defined date used for reporting only.

- 
**[lineNumber](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_lineNumber)**  

Unique number used to identify a tax line item.

- 
**[productCode](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_productCode)**  

Catalog code for the product represented by the tax line     item.

- 
**[productSKU](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_productSKU)**  

Unique identifier of a product that can be used to identify products       that are exempted from tax.

- 
**[quantity](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_quantity)**  

Number of units of a given product that the tax line item       represents.

- 
**[referenceDocumentCode](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_referenceDocumentCode)**  

Identifier that combines the original invoice ID, previous tax       transaction type, and tax engine ID, used in tax calculations for negative invoice     lines.

- 
**[taxCode](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_taxCode)**  

Code used to identify how tax is calculated for a tax line       item.

  

### addresses

  
  
  
Contains the list of addresses of a line item.

    

#### Signature

`public
          commercetax.LineTaxAddressesRequest addresses {get;
      set;}`

    

#### Property Value

Type: [commercetax.LineTaxAddressesRequest](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_class_commercetax_LineTaxAddressesRequest)

  

  

### amount

  
  
  
Total amount (in a given currency) represented by a line item sent
      for tax calculation.

    

#### Signature

`global Double amount
          {get;
      set;}`

    

#### Property Value

Type: Double

  

  

### customTaxAttributes

  
  
  
Customised tax contract to include additional attributes at the line
      item level.

    

#### Signature

      
      

`global commercetax.TaxLineItemRequest customTaxAttributes
          {get; set;}`

      
    

    

#### Property Value

      
      

Type: Map<String, Object>

    

  

  

### description

  
  
  
User-defined description for a tax line item.

    

#### Signature

`global String
          description {get;
      set;}`

    

#### Property Value

Type: String

  

  

### effectiveDate

  
  
  
The date that a tax transaction takes effect on a line item. This is
      a user-defined date used for reporting only.

    

#### Signature

`global Datetime
          effectiveDate {get;
      set;}`

    

#### Property Value

Type: Datetime

  

  

### lineNumber

  
  
  
Unique number used to identify a tax line item.

    

#### Signature

`global String
          lineNumber {get;
      set;}`

    

#### Property Value

Type: String

  

  

### productCode

  
  
  
Catalog code for the product represented by the tax line
    item.

    

#### Signature

`global String
          productCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### productSKU

  
  
  
Unique identifier of a product that can be used to identify products
      that are exempted from tax.

    

#### Signature

      
      

`global String productSKU {get; set;}`

      
    

    

#### Property Value

      
      

Type: String

    

  

  

### quantity

  
  
  
Number of units of a given product that the tax line item
      represents.

    

#### Signature

`global Double
          quantity {get;
      set;}`

    

#### Property Value

Type: Double

  

  

### referenceDocumentCode

  
  
  
Identifier that combines the original invoice ID, previous tax
      transaction type, and tax engine ID, used in tax calculations for negative invoice
    lines.

    
      

For example, a referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA` indicates `3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID. The previous tax transaction type is
        always `Debit` for negative invoice lines.

    

    

#### Signature

      
      

`global String referenceDocumentCode {get; set;}`

      
    

    

#### Property Value

      
      

Type: String

    

  

  

### taxCode

  
  
  
Code used to identify how tax is calculated for a tax line
      item.

    

#### Signature

`global String
          taxCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

## TaxLineItemRequest Methods

  
  
  
Learn more about the available methods with the `TaxLineItemRequest` class.

    
      

The `TaxLineItemRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_equals)**  

Maintains the integrity of lists of type `TaxLineItemRequest` by determining the equality of external objects in a list. This       method is dynamic and is based on the `equals()` method in       Java.

- 
**[hashCode()](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_hashCode)**  

Maintains the integrity of lists of type `TaxLineItemRequest` by determining the uniqueness of the external object records in       a list.

- 
**[toString()](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_commercetax_TaxLineItemRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `TaxLineItemRequest` by determining the equality of external objects in a list. This
      method is dynamic and is based on the `equals()` method in
      Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose
            key
            is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxLineItemRequest` by determining the uniqueness of the external object records in
      a list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_TaxSellerDetailsRequest.htm ===
---
page_id: apex_class_commercetax_TaxSellerDetailsRequest.htm
title: TaxSellerDetailsRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxSellerDetailsRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxSellerDetailsRequest Class

  
  
  
Contains tax code details used in the tax calculation
      request.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

    
    
    
  

- 
**[TaxSellerDetailsRequest Constructors](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_constructors)**  

Learn more about the available constructors with the `TaxSellerDetailsRequest` class.

- 
**[TaxSellerDetailsRequest Properties](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_properties)**  

Learn more about the available properties with the `TaxSellerDetailsRequest` class.

- 
**[TaxSellerDetailsRequest Methods](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_methods)**  

Learn more about the available methods with the `TaxSellerDetailsRequest` class.

  

## TaxSellerDetailsRequest Constructors

  
  
  
Learn more about the available constructors with the `TaxSellerDetailsRequest` class.

    
      

The `TaxSellerDetailsRequest` class includes these
        constructors.

    

    
  

- 
**[TaxSellerDetailsRequest(code)](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_ctor)**  

Initializes the request for the tax seller details. This constructor       is intended for test usage and throws an exception if used outside of the Apex test       context

  

### TaxSellerDetailsRequest(code)

  
  
  
Initializes the request for the tax seller details. This constructor
      is intended for test usage and throws an exception if used outside of the Apex test
      context

    

#### Signature

`global
          TaxSellerDetailsRequest(String
      code)`

    

#### Parameters

        
- 
**code**:

Type: String

Tax code used

for tax calculation.

      

  

  

## TaxSellerDetailsRequest Properties

  
  
  
Learn more about the available properties with the `TaxSellerDetailsRequest` class.

    
      

The `TaxSellerDetailsRequest` class includes these
        properties.

    

    
  

- 
**[code](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_code)**  

Tax code used for tax calculation.

  

### code

  
  
  
Tax code used for tax calculation.

    

#### Signature

`global String code
          {get;
      set;}`

    

#### Property Value

Type: String

  

  

## TaxSellerDetailsRequest Methods

  
  
  
Learn more about the available methods with the `TaxSellerDetailsRequest` class.

    
      

The `TaxSellerDetailsRequest` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_equals)**  

Maintains the integrity of lists of type `TaxSellerDetailsRequest` by determining the equality of the external objects in a       list. This method is dynamic and based on the `equals()`       method in Java.

- 
**[hashCode()](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_hashCode)**  

Maintains the integrity of lists of type `TaxSellerDetailsRequest` by determining the uniqueness of the external objects in a       list.

- 
**[toString()](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_commercetax_TaxSellerDetailsRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `TaxSellerDetailsRequest` by determining the equality of the external objects in a
      list. This method is dynamic and based on the `equals()`
      method in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: 

Object External object whose key is to be validated.

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxSellerDetailsRequest` by determining the uniqueness of the external objects in a
      list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_commercetax_TaxTransactionRequest.htm ===
---
page_id: apex_class_commercetax_TaxTransactionRequest.htm
title: TaxTransactionRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_commercetax_TaxTransactionRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxTransactionRequest Class

  
  
  
Abstract class for storing customer details used in tax calculation
      and estimation requests.

    

## Namespace

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

## Usage

      
      

Specify
        the `CommerceTax` namespace when creating an instance of
        this class. The constructor of this class takes no arguments. For example, let's say you
        create an instance of `CalculateTaxRequest` class, which
        extends the `TaxTransactionRequest` class.

    

    
  

- 
**[TaxTransactionRequest Constructors](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_constructors)**  

Learn more about the available constructors with the `TaxTransactionRequest` class.

- 
**[TaxTransactionRequest Properties](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_properties)**  

Learn more about the available properties with the `TaxTransactionRequest` class.

- 
**[TaxTransactionRequest Methods](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_methods)**  

  

## TaxTransactionRequest Constructors

  
  
  
Learn more about the available constructors with the `TaxTransactionRequest` class.

    
      

The `TaxTransactionRequest` class includes these
        constructors.

    

    
  

- 
**[TaxTransactionRequest(addresses, currencyIsoCode, customerDetails, description, documentCode, referenceDocumentCode, transactionDate, effectiveDate, lineItems, referenceEntityId, sellerDetails, customTaxAttributes)](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_ctor)**  

Initializes the request for the tax transaction. This constructor is       intended for test usage and throws an exception if used outside of the Apex test     context.

  

### TaxTransactionRequest(addresses, currencyIsoCode,
      customerDetails, description, documentCode, referenceDocumentCode, transactionDate,
      effectiveDate, lineItems, referenceEntityId, sellerDetails,
    customTaxAttributes)

  
  
  
Initializes the request for the tax transaction. This constructor is
      intended for test usage and throws an exception if used outside of the Apex test
    context.

    

#### Signature

`global TaxTransactionRequest(commercetax.HeaderTaxAddressesRequest
          addresses, String currencyIsoCode, commercetax.TaxCustomerDetailsRequest customerDetails,
          String description, String documentCode, String referenceDocumentCode, Datetime
          transactionDate, Datetime effectiveDate, List<commercetax.TaxLineItemRequest>
          lineItems, String referenceEntityId, commercetax.TaxSellerDetailsRequest
          sellerDetails,Map<String,Object> customTaxAttributes)`

    

#### Parameters

        
- 
**addresses**:

Type: [HeaderTaxAddressesRequest](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_class_commercetax_HeaderTaxAddressesRequest)

Tax addresses, such as Ship To and Bill From.

        
- 
**currencyIsoCode**:

Type: String

Three-letter ISO 4217 currency code associated with the `TaxTransactionRequest`.

        
- 
**customerDetails**:

Type: [TaxCustomerDetailsRequest](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_class_commercetax_TaxCustomerDetailsRequest)

Customer information used in tax calculation.

        
- 
**description**:

Type: String

Optional user-defined description for providing more information about the tax
            transaction request.

        
- 
**documentCode**:

Type: String

Code

for documents that are used to provide more information in the tax calculation
            process.

        
- 
**referenceDocumentCode**:

Type: String

Identifier that combines

the original invoice ID, previous tax transaction type, and
            tax engine ID, used in tax calculations for negative invoice lines. For example, a
            referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA` indicates `3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID.

        
- 
**transactionDate**:

Type: Datetime

The date that the tax transaction occurred.

        
- 
**effectiveDate**:

Type: Datetime

The date that the tax transaction takes effect. User-defined and used only for
            reporting purposes.

        
- 
**lineItems**:

Type: List<[TaxLineItemRequest](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_class_commercetax_TaxLineItemRequest)>

A list of line items on which tax is calculated.

        
- 
**referenceEntityId**:

Type: String

ID of an object related to the line items sent for tax calculation.

        
- 
**sellerDetails**:

Type: [TaxSellerDetailsRequest](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_class_commercetax_TaxSellerDetailsRequest)

Contains tax code information used in a tax calculation request.

        
- 
**customTaxAttributes**:

Type: Map<String, Object> Customised tax contract to include additional attributes at the header level.

      

  

  

## TaxTransactionRequest Properties

  
  
  
Learn more about the available properties with the `TaxTransactionRequest` class.

    
      

The `TaxTransactionRequest` class includes these
        properties.

    

    
  

- 
**[addresses](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_addresses)**  

A list of addresses (such as Ship To and Sold To) used as part of       the tax transaction.

- 
**[currencyIsoCode](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_currencyIsoCode)**  

Three-letter ISO 4217 currency code associated with the `TaxTransactionRequest`.

- 
**[customerDetails](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_customerDetails)**  

Customer information used in tax calculation.

- 
**[customTaxAttributes](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_customTaxAttributes)**  

Customised tax contract to include additional attributes at the       header level.

- 
**[description](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_description)**  

Optional user-defined description for providing more information       about the tax transaction request.

- 
**[documentCode](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_documentCode)**  

Code for documents used to provide more information in the tax       calculation process.

- 
**[effectiveDate](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_effectiveDate)**  

The date that the tax transaction takes effect. User-defined and       used only for reporting purposes.

- 
**[lineItems](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_lineItems)**  

A list of line items on which tax will be     calculated.

- 
**[referenceDocumentCode](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_referenceDocumentCode)**  

Identifier that combines the original invoice ID, previous tax       transaction type, and tax engine ID, used in tax calculations for negative invoice     lines.

- 
**[referenceEntityId](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_referenceEntityId)**  

ID of an object related to the line items sent for tax       calculation.

- 
**[sellerDetails](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_sellerDetails)**  

Contains       tax code information used in a tax calculation request.

- 
**[transactionDate](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_transactionDate)**  

The date that the tax transaction occurred.

  

### addresses

  
  
  
A list of addresses (such as Ship To and Sold To) used as part of
      the tax transaction.

    

#### Signature

`global commercetax.HeaderTaxAddressesRequest addresses {get;
          set;}`

    

#### Property Value

Type: [HeaderTaxAddressesRequest](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_class_commercetax_HeaderTaxAddressesRequest)

  

  

### currencyIsoCode

  
  
  
Three-letter ISO 4217 currency code associated with the `TaxTransactionRequest`.

    

#### Signature

`global String
          currencyIsoCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### customerDetails

  
  
  
Customer information used in tax calculation.

    

#### Signature

`global
          CommerceTax.TaxCustomerDetailsRequest
          customerDetails {get; set;}`

    

#### Property Value

Type: [TaxCustomerDetailsRequest](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_class_commercetax_TaxCustomerDetailsRequest)

  

  

### customTaxAttributes

  
  
  
Customised tax contract to include additional attributes at the
      header level.

    

#### Signature

      
      

`global commercetax.TaxTransactionRequest customTaxAttributes
          {get; set;}`

      
    

    

#### Property Value

      
      

Type: Map<String, Object>

    

  

  

### description

  
  
  
Optional user-defined description for providing more information
      about the tax transaction request.

    

#### Signature

`global String
          description {get;
      set;}`

    

#### Property Value

Type: String

  

  

### documentCode

  
  
  
Code for documents used to provide more information in the tax
      calculation process.

    

#### Signature

`global String
          documentCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### effectiveDate

  
  
  
The date that the tax transaction takes effect. User-defined and
      used only for reporting purposes.

    

#### Signature

`global Datetime
          effectiveDate {get;
      set;}`

    

#### Property Value

Type: Datetime

  

  

### lineItems

  
  
  
A list of line items on which tax will be
    calculated.

    

#### Signature

`global
          List<CommerceTax.TaxLineItemRequest>
          lineItems {get; set;}`

    

#### Property Value

Type: List<[TaxLineItemRequest](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_class_commercetax_TaxLineItemRequest)>

  

  

### referenceDocumentCode

  
  
  
Identifier that combines the original invoice ID, previous tax
      transaction type, and tax engine ID, used in tax calculations for negative invoice
    lines.

    
      

For example, a referenceDocumentCode parameter value `3ttxx00000004Bh_Debit-4wAxx0000000001EAA` indicates `3ttxx00000004Bh` is the original invoice ID and `4wAxx0000000001EAA` is the tax engine ID.

    

    

#### Signature

`global String
          referenceDocumentCode {get;
      set;}`

    

#### Property Value

Type: String

  

  

### referenceEntityId

  
  
  
ID of an object related to the line items sent for tax
      calculation.

    

#### Signature

`global String
          referenceEntityId {get;
      set;}`

    

#### Property Value

Type: String

  

  

### sellerDetails

  
  
  
Contains
      tax code information used in a tax calculation request.

    

#### Signature

`global
          commercetax.TaxSellerDetailsRequest sellerDetails {get;
      set;}`

    

#### Property Value

Type: [TaxSellerDetailsRequest](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_class_commercetax_TaxSellerDetailsRequest)

  

  

### transactionDate

  
  
  
The date that the tax transaction occurred.

    

#### Signature

`global Datetime
          transactionDate {get;
      set;}`

    

#### Property Value

Type: Datetime

  

  

## TaxTransactionRequest Methods

  
  
    

The following are methods for `TaxTransactionRequest`.

    
  

- 
**[equals(obj)](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_equals)**  

Maintains the integrity of lists of type `TaxTransactionRequest` by determining the equality of external objects in a list.       This method is dynamic and based on the `equals()` method       in Java.

- 
**[hashCode()](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_hashCode)**  

Maintains the integrity of lists of type `TaxTransactionRequest` by determining the uniqueness of the external object records       in a list.

- 
**[toString()](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_commercetax_TaxTransactionRequest_toString)**  

Converts a value to a string.

  

### equals(obj)

  
  
  
Maintains the integrity of lists of type `TaxTransactionRequest` by determining the equality of external objects in a list.
      This method is dynamic and based on the `equals()` method
      in Java.

    

#### Signature

`global Boolean
          equals(Object
      obj)`

    

#### Parameters

        
- 
**obj**:

Type: Object

      

    

#### Return Value

Type: Boolean

  

  

### hashCode()

  
  
  
Maintains the integrity of lists of type `TaxTransactionRequest` by determining the uniqueness of the external object records
      in a list.

    

#### Signature

`global Integer
          hashCode()`

    

#### Return Value

Type: Integer

  

  

### toString()

  
  
  
Converts a value to a string.

    

#### Signature

`global String
          toString()`

    

#### Return Value

Type: String

=== ARTICLE: apex_class_placequote_ConfigurationOptionsInput.htm ===
---
page_id: apex_class_placequote_ConfigurationOptionsInput.htm
title: ConfigurationOptionsInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_ConfigurationOptionsInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationOptionsInput Class

Contains methods and properties to set the configuration options for the input to the
    product configurator.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

## Usage

This class holds the required details of the product configuration input. Set the class
        properties to enable default configuration, execution of configuration rules, and validation
        of the product catalog. Use these class properties as an input to the [PlaceQuoteRLMApexProcessor](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_class_placequote_PlaceQuoteRLMApexProcessor) class method.

    

## Example

      
      

```
PlaceQuote.GraphRequest graph = new PlaceQuote.GraphRequest('test',listOfRecords);
    PlaceQuote.PricingPreferenceEnum pricingPreference = PlaceQuote.PricingPreferenceEnum.System;
    PlaceQuote.ConfigurationInputEnum configurationPreference = PlaceQuote.ConfigurationInputEnum.RunAndAllowErrors;
    PlaceQuote.ConfigurationOptionsInput cInput = new PlaceQuote.ConfigurationOptionsInput();
    cInput.addDefaultConfiguration = true;
    cInput.executeConfigurationRules = true;
    cInput.validateAmendRenewCancel = true;
    cInput.validateProductCatalog = true;
        //Place Quote Call
     PlaceQuote.PlaceQuoteResponse resp = PlaceQuote.PlaceQuoteRLMApexProcessor.execute(pricingPreference,graph,configurationPreference,cInput);
```

    

- 
**[ConfigurationOptionsInput Properties](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_properties)**  

Set the `ConfigurationOptionsInput` class properties     to add default configuration, execute configuration rules, and validate the product     catalog.

- 
**[ConfigurationOptionsInput Methods](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_methods)**  

Learn more about the methods available with the `ConfigurationOptionsInput` class.

  

## ConfigurationOptionsInput Properties

  
  
  
Set the `ConfigurationOptionsInput` class properties
    to add default configuration, execute configuration rules, and validate the product
    catalog.

    
      

The `ConfigurationOptionsInput` class includes these
        properties.

    

    
  

- 
**[addDefaultConfiguration](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_addDefaultConfiguration)**  

Sets the default product configuration, such as bundle and product attributes, for a     quote request.

- 
**[executeConfigurationRules](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_executeConfigurationRules)**  

Sets the requirement for a quote to adhere to the configuration rules.

- 
**[validateAmendRenewCancel](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_validateAmendRenewCancel)**  

Sets the requirement to run validations related to amend, renew, or cancel     processes.

- 
**[validateProductCatalog](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_validateProductCatalog)**  

Sets the requirement to validate a quote against the product catalog.

### addDefaultConfiguration

Sets the default product configuration, such as bundle and product attributes, for a
    quote request.

#### Signature

`public Boolean addDefaultConfiguration {get; set;}`

#### Property Value

Type: Boolean

Indicates whether to automatically add
        default configuration to the order (`true`) or not
          (`false`).

### executeConfigurationRules

Sets the requirement for a quote to adhere to the configuration rules.

#### Signature

`public Boolean executeConfigurationRules {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the order must
        adhere to configuration rules during processing (`true`)
        or bypass them (`false`).

### validateAmendRenewCancel

Sets the requirement to run validations related to amend, renew, or cancel
    processes.

#### Signature

`public Boolean validateAmendRenewCancel {get; set;}`

#### Property Value

Type: Boolean

Indicates whether to run validations
        related to amend, renew, or cancel processes (`true`) or
        not (`false`).

### validateProductCatalog

Sets the requirement to validate a quote against the product catalog.

#### Signature

`public Boolean validateProductCatalog {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the quote must be
        validated against the product catalog (`true`) or not
          (`false`).

  

## ConfigurationOptionsInput Methods

  
  
  
Learn more about the methods available with the `ConfigurationOptionsInput` class.

    
      

The `ConfigurationOptionsInput` class includes these
        methods.

    

    
  

- 
**[equals(obj)](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_equals)**  

Determines the equality of external objects in a list. This method is dynamic and is     based on the `equals()` method in Java.

- 
**[hashCode()](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_hashCode)**  

Determines the uniqueness of the external object records in a list.

- 
**[toString()](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_placequote_ConfigurationOptionsInput_toString)**  

Converts a value to a string.

### equals(obj)

Determines the equality of external objects in a list. This method is dynamic and is
    based on the `equals()` method in Java.

#### Signature

`public Boolean equals(Object obj)`

#### Parameters

**obj**

: Type: Object

: Reference object that’s used to compare with the class object.

#### Return Value

Type: Boolean

Indicates if the class object is same as the reference object (`true`) or not (`false`).

### hashCode()

Determines the uniqueness of the external object records in a list.

#### Signature

`public Integer hashCode()`

#### Return Value

Type: Integer

Integer hash code that represents the value of the object. Equal objects as per the `equals()` method must return the same hash code.

### toString()

Converts a value to a string.

#### Signature

`public String toString()`

#### Return Value

Type: String

=== ARTICLE: apex_class_placequote_GraphRequest.htm ===
---
page_id: apex_class_placequote_GraphRequest.htm
title: GraphRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_GraphRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GraphRequest Class

Contains constructors and properties to set the graph ID and a list of records to be
    ingested. The list of records is specified in a key-value map format that contains the field
    values of an order.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

    

## Example

      
      

Invoke the Place Quote Apex API by using these steps.

      
        
- Set up a quote and quote line item. To associate the Record object with a reference
          identifier, create an instance of the `RecordWithReferenceRequest` class.

```

         //Quote Setup 
    PlaceQuote.RecordResource quoteRecord = new PlaceQuote.RecordResource(Quote.getSobjectType(),'POST');
    Map<String,Object> quoteFieldValues = new Map<String,Object>();
    quoteFieldValues.put('Name','q-ap12');
    quoteFieldValues.put('OpportunityId','006xx000001aBFcAAM');
    quoteFieldValues.put('Pricebook2Id','01sxx0000005pvRAAQ');
    quoteRecord.fieldValues = quoteFieldValues;
    
           //Quote Line Item Setup
    PlaceQuote.RecordResource quoteLineItemRecord1 = new PlaceQuote.RecordResource(QuoteLineItem.getSobjectType(),'POST');
    Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
    quoteLineItemFieldValues.put('Product2Id','01txx0000006ibwAAA');
    quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008zPqAAI');
    quoteLineItemFieldValues.put('Quantity','2.0');
    quoteLineItemFieldValues.put('UnitPrice','5.0');
    quoteLineItemFieldValues.put('StartDate','2023-03-15');
    quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
    quoteLineItemRecord1.fieldValues = quoteLineItemFieldValues;
    PlaceQuote.RecordWithReferenceRequest quoteItemRecords = new PlaceQuote.RecordWithReferenceRequest('refQuote',quoteRecord);
    PlaceQuote.RecordWithReferenceRequest quoteLineItemRecords1 = new PlaceQuote.RecordWithReferenceRequest('refQuoteItem1',quoteLineItemRecord1);
   
```

        
- To create a quote line relationship, create an instance of the `RecordResource`
          class.

```
PlaceQuote.RecordResource quoteLineRelationship1 = new PlaceQuote.RecordResource(QuoteLineRelationship.getSobjectType(),'POST');
    Map<String,Object> quoteLineRelationshipValues = new Map<String,Object>();
    quoteLineRelationshipValues.put('ProductRelationshipTypeId','0yoxx00000000JNAAY');
    quoteLineRelationshipValues.put('MainQuoteLineId','@{refQuoteItem2.id}');
    quoteLineRelationshipValues.put('AssociatedQuoteLineId','@{refQuoteItem1.id}');
    quoteLineRelationshipValues.put('AssociatedQuoteLinePricing','IncludedInBundlePrice');
    quoteLineRelationship1.fieldValues = quoteLineRelationshipValues;
```

        
- Create the list of records to be ingested.

```

    PlaceQuote.RecordWithReferenceRequest quoteLineRelationship = new PlaceQuote.RecordWithReferenceRequest('QuoteLineRelationship',quoteLineRelationship1);
    List<PlaceQuote.RecordWithReferenceRequest> listOfRecords = new List<PlaceQuote.RecordWithReferenceRequest>();
    listOfRecords.add(quoteItemRecords);
    listOfRecords.add(quoteLineItemRecords1);
    listOfRecords.add(quoteLineItemRecords2);
    listOfRecords.add(quoteLineRelationship);
```

        
- To contain all record objects, create an instance of the `GraphRequest` class. 

#### Note

The `CatalogRatesPreferenceEnum` enum is available when the Usage-Based Selling
            feature is enabled.

```

    PlaceQuote.GraphRequest graph = new PlaceQuote.GraphRequest('test',listOfRecords);
    PlaceQuote.ConfigurationOptionsInput cInput = new PlaceQuote.ConfigurationOptionsInput();
    PlaceQuote.CatalogRatesPreferenceEnum catalogRatesPreference = PlaceQuote.CatalogRatesPreferenceEnum.Fetch;
....PlaceQuote.ConfigurationInputEnum configurationPreference = PlaceQuote.ConfigurationInputEnum.RunAndAllowErrors;
    PlaceQuote.PricingPreferenceEnum pricingPreference = PlaceQuote.PricingPreferenceEnum.System;
    //System.debug(graph);
      
    //Place Quote Call
    PlaceQuote.PlaceQuoteResponse resp = PlaceQuote.PlaceQuoteRLMApexProcessor.execute(pricingPreference, catalogRatesPreference, graph, configurationPreference, cInput);
    System.debug(resp);
```

      

    

- 
**[GraphRequest Constructors](./apex_class_placequote_GraphRequest.htm.md#apex_placequote_GraphRequest_constructors)**  

Learn more about the available constructors with the `GraphRequest` class.

- 
**[GraphRequest Properties](./apex_class_placequote_GraphRequest.htm.md#apex_placequote_GraphRequest_properties)**  

  

## GraphRequest Constructors

  
  
  
Learn more about the available constructors with the `GraphRequest` class.

    
      

The `GraphRequest` class includes these constructors.

    

    
  

- 
**[GraphRequest(graphId, records)](./apex_class_placequote_GraphRequest.htm.md#apex_placequote_GraphRequest_ctor)**  

Creates an instance of the `GraphRequest` class         to assign the graph ID and a list of records to be ingested.

### GraphRequest(graphId, records)

    
Creates an instance of the `GraphRequest` class
        to assign the graph ID and a list of records to be ingested.

#### Signature

`public GraphRequest(String graphId, List<placequote.RecordWithReferenceRequest> records)`

#### Parameters

**graphId**

: Type: String

          
: ID of the graph.

**records**

: Type: List<[placequote.RecordWithReferenceRequest](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_class_placequote_RecordWithReferenceRequest)>

          
: List of records to be ingested.

## GraphRequest Properties

The following are properties for `GraphRequest`.

- 
**[graphId](./apex_class_placequote_GraphRequest.htm.md#apex_placequote_GraphRequest_graphId)**  

Set the `graphId` property to assign the ID value of     the graph.

### graphId

  
Set the `graphId` property to assign the ID value of
    the graph.

#### Signature

`public String graphId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_placequote_PlaceQuoteException.htm ===
---
page_id: apex_class_placequote_PlaceQuoteException.htm
title: PlaceQuoteException Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_PlaceQuoteException.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceQuoteException Class

Contains methods to hold the exception details for the place quote request.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

- 
**[PlaceQuoteException Methods](./apex_class_placequote_PlaceQuoteException.htm.md#apex_placequote_PlaceQuoteException_methods)**  

Learn more about the methods available with the `PlaceQuoteException` class.

  

## PlaceQuoteException Methods

  
  
  
Learn more about the methods available with the `PlaceQuoteException` class.

    
      

The `PlaceQuoteException` class includes these
        methods.

    

    
  

- 
**[getErrorCode()](./apex_class_placequote_PlaceQuoteException.htm.md#apex_placequote_PlaceQuoteException_getErrorCode)**  

Gets the error code that’s associated to the place quote request.

### getErrorCode()

Gets the error code that’s associated to the place quote request.

#### Signature

`public String getErrorCode()`

#### Return Value

Type: String

=== ARTICLE: apex_class_placequote_PlaceQuoteRLMApexProcessor.htm ===
---
page_id: apex_class_placequote_PlaceQuoteRLMApexProcessor.htm
title: PlaceQuoteRLMApexProcessor Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_PlaceQuoteRLMApexProcessor.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceQuoteRLMApexProcessor Class

Contains methods to place a quote with details of the graph request, pricing preferences,
    and configuration options.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

- 
**[PlaceQuoteRLMApexProcessor Methods](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_methods)**  

Learn more about the methods available with the `PlaceQuoteRLMApexProcessor` class.

- 
**[PlaceQuoteRLMApexProcessor Example Implementation](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_example_implementation)**  

To place a quote from Apex, refer to the example implementation of the `PlaceQuoteRLMApexProcessor` class.

  

## PlaceQuoteRLMApexProcessor Methods

  
  
  
Learn more about the methods available with the `PlaceQuoteRLMApexProcessor` class.

    
      

The `PlaceQuoteRLMApexProcessor` class includes these
        methods.

    

    
  

- 
**[execute(pricingPreferenceEnum, graphRequest, configurationInputEnum, configurationOptionsInput)](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_execute)**  

Use the method in the `PlaceQuoteExecutor` class to     execute the Place Quote Apex API request by assigning the properties for graph request, pricing     references, and configuration options.

- 
**[execute(pricingPreferenceEnum, catalogRatesPreference, graphRequest, configurationInputEnum, configurationOptionsInput)](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_execute_2)**  

Use the method in the `PlaceQuoteExecutor` class to     execute the Place Quote Apex API request by assigning the properties for graph request, pricing     references, and configuration options. This method also includes the property to define fetching     of rate card entries.

### execute(pricingPreferenceEnum, graphRequest, configurationInputEnum, configurationOptionsInput)

Use the method in the `PlaceQuoteExecutor` class to
    execute the Place Quote Apex API request by assigning the properties for graph request, pricing
    references, and configuration options.

#### Signature

`public static placequote.PlaceQuoteResponse execute(placequote.PricingPreferenceEnum pricingPreferenceEnum, placequote.GraphRequest graphRequest, placequote.ConfigurationInputEnum configurationInputEnum, placequote.ConfigurationOptionsInput configurationOptionsInput)`

#### Parameters

**pricingPreferenceEnum**

: Type: [placequote.PricingPreferenceEnum](./apex_enum_placequote_PricingPreferenceEnum.htm.md)

: Pricing preference during the quote process.

**graphRequest**

: Type: [placequote.GraphRequest](./apex_class_placequote_GraphRequest.htm.md#apex_class_placequote_GraphRequest)

: The sObject graph values of the quote payload to be ingested.

**configurationInputEnum**

: Type: [placequote.ConfigurationInputEnum](./apex_enum_placequote_ConfigurationInputEnum.htm.md)

: Configuration input for the quote process.

**configurationOptionsInput**

: Type: [placequote.ConfigurationOptionsInput](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_class_placequote_ConfigurationOptionsInput)

: Configuration options during the ingestion process.

#### Return Value

Type: [placequote.PlaceQuoteResponse](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_class_placequote_PlaceQuoteResponse)

  

### execute(pricingPreferenceEnum, catalogRatesPreference,
      graphRequest, configurationInputEnum, configurationOptionsInput)

  
  
  
Use the method in the `PlaceQuoteExecutor` class to
    execute the Place Quote Apex API request by assigning the properties for graph request, pricing
    references, and configuration options. This method also includes the property to define fetching
    of rate card entries.

    

#### Signature

      
      

`public static placequote.PlaceQuoteResponse
          execute(placequote.PricingPreferenceEnum pricingPreferenceEnum,
          placequote.CatalogRatesPreferenceEnum catalogRatesPreference, placequote.GraphRequest
          graphRequest, placequote.ConfigurationInputEnum configurationInputEnum,
          placequote.ConfigurationOptionsInput configurationOptionsInput)`

      
    

    

#### Parameters

      
      
        
          

**pricingPreferenceEnum**

          
: Type: [placequote.PricingPreferenceEnum](./apex_enum_placequote_PricingPreferenceEnum.htm.md)

          
: Pricing preference during the quote process.

        
        
          

**catalogRatesPreference**

          
: Type: [placequote.CatalogRatesPreferenceEnum](./apex_enum_placequote_CatalogRatesPreferenceEnum.htm.md)

          
: The rate card entries defined in the catalog that must be fetched for quote line
            items, with usage-based pricing during the quote creation process. The `CatalogRatesPreferenceEnum` enum is available when the
            Usage-Based Selling feature is enabled.

        
        
          

**graphRequest**

          
: Type: [placequote.GraphRequest](./apex_class_placequote_GraphRequest.htm.md#apex_class_placequote_GraphRequest)

          
: The sObject graph values of the quote payload to be ingested.

        
        
          

**configurationInputEnum**

          
: Type: [placequote.ConfigurationInputEnum](./apex_enum_placequote_ConfigurationInputEnum.htm.md)

          
: Configuration input for the quote process.

        
        
          

**configurationOptionsInput**

          
: Type: [placequote.ConfigurationOptionsInput](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_class_placequote_ConfigurationOptionsInput)

          
: Configuration options during the ingestion process.

        
      

    

    

#### Return Value

      
      

Type: [placequote.PlaceQuoteResponse](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_class_placequote_PlaceQuoteResponse)

    

  

    

## PlaceQuoteRLMApexProcessor Example Implementation

    
    
    
To place a quote from Apex, refer to the example implementation of the `PlaceQuoteRLMApexProcessor` class.

        

### Namespace

            
            

[PlaceQuote](./apex_namespace_placequote.htm.md)

        

        

### Usage

            
            

Customize this example to suit your requirements. Create the list of records to be
                ingested by using these steps. Replace the respective IDs with the values that are
                present in your org. For example, replace the value of `${Pricebook2Id}` field with the price book ID that’s present in the
                org.

        

        

### Example

            
                
- Set up a quote and quote line item. To associate the Record object with a
                    reference identifier, create an instance of the `RecordWithReferenceRequest`
                    class.

```

         //Quote Setup 
    PlaceQuote.RecordResource quoteRecord = new PlaceQuote.RecordResource(Quote.getSobjectType(),'POST');
    Map<String,Object> quoteFieldValues = new Map<String,Object>();
    quoteFieldValues.put('Name','q-ap12');
    quoteFieldValues.put('OpportunityId','006xx000001aBFcAAM');
    quoteFieldValues.put('Pricebook2Id','01sxx0000005pvRAAQ');
    quoteRecord.fieldValues = quoteFieldValues;
    
           //Quote Line Item Setup
    PlaceQuote.RecordResource quoteLineItemRecord1 = new PlaceQuote.RecordResource(QuoteLineItem.getSobjectType(),'POST');
    Map<String,Object> quoteLineItemFieldValues = new Map<String,Object>();
    quoteLineItemFieldValues.put('Product2Id','01txx0000006ibwAAA');
    quoteLineItemFieldValues.put('PricebookEntryId','01uxx0000008zPqAAI');
    quoteLineItemFieldValues.put('Quantity','2.0');
    quoteLineItemFieldValues.put('UnitPrice','5.0');
    quoteLineItemFieldValues.put('StartDate','2023-03-15');
    quoteLineItemFieldValues.put('QuoteId','@{refQuote.id}');
    quoteLineItemRecord1.fieldValues = quoteLineItemFieldValues;
    PlaceQuote.RecordWithReferenceRequest quoteItemRecords = new PlaceQuote.RecordWithReferenceRequest('refQuote',quoteRecord);
    PlaceQuote.RecordWithReferenceRequest quoteLineItemRecords1 = new PlaceQuote.RecordWithReferenceRequest('refQuoteItem1',quoteLineItemRecord1);
   
```

                
- To create a quote line relationship, create an instance of the `RecordResource`
                    class.

```
PlaceQuote.RecordResource quoteLineRelationship1 = new PlaceQuote.RecordResource(QuoteLineRelationship.getSobjectType(),'POST');
    Map<String,Object> quoteLineRelationshipValues = new Map<String,Object>();
    quoteLineRelationshipValues.put('ProductRelationshipTypeId','0yoxx00000000JNAAY');
    quoteLineRelationshipValues.put('MainQuoteLineId','@{refQuoteItem2.id}');
    quoteLineRelationshipValues.put('AssociatedQuoteLineId','@{refQuoteItem1.id}');
    quoteLineRelationshipValues.put('AssociatedQuoteLinePricing','IncludedInBundlePrice');
    quoteLineRelationship1.fieldValues = quoteLineRelationshipValues;
```

                
- Create the list of records to be
                    ingested.

```

    PlaceQuote.RecordWithReferenceRequest quoteLineRelationship = new PlaceQuote.RecordWithReferenceRequest('QuoteLineRelationship',quoteLineRelationship1);
    List<PlaceQuote.RecordWithReferenceRequest> listOfRecords = new List<PlaceQuote.RecordWithReferenceRequest>();
    listOfRecords.add(quoteItemRecords);
    listOfRecords.add(quoteLineItemRecords1);
    listOfRecords.add(quoteLineItemRecords2);
    listOfRecords.add(quoteLineRelationship);
```

                
- To contain all record objects, create an instance of the `GraphRequest` class. 

#### Note

The `CatalogRatesPreferenceEnum` enum is available
                        when the Usage-Based Selling feature is
                    enabled.

```

    PlaceQuote.GraphRequest graph = new PlaceQuote.GraphRequest('test',listOfRecords);
    PlaceQuote.ConfigurationOptionsInput cInput = new PlaceQuote.ConfigurationOptionsInput();
    PlaceQuote.CatalogRatesPreferenceEnum catalogRatesPreference = PlaceQuote.CatalogRatesPreferenceEnum.Fetch;
....PlaceQuote.ConfigurationInputEnum configurationPreference = PlaceQuote.ConfigurationInputEnum.RunAndAllowErrors;
    PlaceQuote.PricingPreferenceEnum pricingPreference = PlaceQuote.PricingPreferenceEnum.System;
    //System.debug(graph);
      
    //Place Quote Call
    PlaceQuote.PlaceQuoteResponse resp = PlaceQuote.PlaceQuoteRLMApexProcessor.execute(pricingPreference, catalogRatesPreference, graph, configurationPreference, cInput);
    System.debug(resp);
```

=== ARTICLE: apex_class_placequote_PlaceQuoteResponse.htm ===
---
page_id: apex_class_placequote_PlaceQuoteResponse.htm
title: PlaceQuoteResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_PlaceQuoteResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceQuoteResponse Class

Contains properties to hold the response to the place quote request.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

    

## Example

      
      

```
PlaceQuote.PlaceQuoteResponse resp = PlaceQuote.PlaceQuoteExecutor.execute(internalEnum,graph);
```

    

- 
**[PlaceQuoteResponse Properties](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_properties)**  

Learn more about the available properties with the `PlaceQuoteResponse` class.

  

## PlaceQuoteResponse Properties

  
  
  
Learn more about the available properties with the `PlaceQuoteResponse` class.

    
      

The `PlaceQuoteResponse` class includes these
        properties.

    

    
  

- 
**[quoteId](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_quoteId)**  

Get the ID of the quote that’s created after a successful request.

- 
**[requestIdentifier](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_requestIdentifier)**  

Get the request ID of the process to query the asynchronous status of the Place Quote     Apex API.

- 
**[responseError](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_responseError)**  

Get the list of errors encountered during the synchronous processing of the API     request.

- 
**[statusURL](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_statusURL)**  

Get the asynchronous status URL of the request, if available.

- 
**[success](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_placequote_PlaceQuoteResponse_success)**  

Get the request status of the synchronous part of the processing.

### quoteId

Get the ID of the quote that’s created after a successful request.

#### Signature

`public String quoteId {get; set;}`

#### Property Value

Type: String

### requestIdentifier

Get the request ID of the process to query the asynchronous status of the Place Quote
    Apex API.

#### Signature

`public String requestIdentifier {get; set;}`

#### Property Value

Type: String

### responseError

Get the list of errors encountered during the synchronous processing of the API
    request.

#### Signature

`public List<ConnectApi.PlaceQuoteErrorResponse> responseError {get; set;}`

#### Property Value

Type: List<ConnectApi.PlaceQuoteErrorResponse>

### statusURL

Get the asynchronous status URL of the request, if available.

#### Signature

`public String statusURL {get; set;}`

#### Property Value

Type: String

### success

Get the request status of the synchronous part of the processing.

#### Signature

`public Boolean success {get; set;}`

#### Property Value

Type: Boolean

Indicates whether the synchronous part
        of the processing is successful (`true`) or not (`false`).

=== ARTICLE: apex_class_placequote_RecordResource.htm ===
---
page_id: apex_class_placequote_RecordResource.htm
title: RecordResource Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_RecordResource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordResource Class

Contains constructors and properties to create a record object from the field values of a
    quote.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

    

## Example

```
PlaceQuote.RecordResource quoteLineRelationship1 = new PlaceQuote.RecordResource(QuoteLineRelationship.getSobjectType(),'POST');
```

See
          [PlaceQuoteRLMApexProcessor](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_example_implementation) to
        refer to an example implementation.

- 
**[RecordResource Constructors](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_constructors)**  

Learn more about the available constructors with the `RecordResource` class.

- 
**[RecordResource Properties](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_properties)**  

Learn more about the available properties with the `RecordResource` class.

  

## RecordResource Constructors

  
  
  
Learn more about the available constructors with the `RecordResource` class.

    
      

The `RecordResource` class includes these
        constructors.

    

    
  

- 
**[RecordResource(type, method, id)](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_ctor)**  

Creates an instance of the `RecordResource` class to     assign values to the fields of a quote item by using the sObject type, API method, and quote ID     properties.

- 
**[RecordResource(type, method)](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_ctor_2)**  

Creates an instance of the `RecordResource` class to     assign the values to the fields of a quote item by using the sObject type and API method     properties.

### RecordResource(type, method, id)

Creates an instance of the `RecordResource` class to
    assign values to the fields of a quote item by using the sObject type, API method, and quote ID
    properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method, Id id)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result using
              the `getSObjectType() `method.

**method**

: Type: String

: Method for the API request, such as POST or PATCH.

**id**

: Type: Id

: ID of the quote.

### RecordResource(type, method)

Creates an instance of the `RecordResource` class to
    assign the values to the fields of a quote item by using the sObject type and API method
    properties.

#### Signature

`public RecordResource(Schema.SObjectType type, String method)`

#### Parameters

**type**

: Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

          
: Object that’s returned from the field describe result using the `getReferenceTo()` method or from the sObject describe result
            using the `getSObjectType() `method.

**method**

: Type: String

: Method for the API request, such as POST or PATCH.

  

## RecordResource Properties

  
  
  
Learn more about the available properties with the `RecordResource` class.

    
      

The `RecordResource` class includes these properties.

    

    
  

- 
**[fieldValues](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_fieldValues)**  

Set the `fieldValues` property to assign values to the     fields to update the quote record.

- 
**[id](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_id)**  

Set the `id` property to assign the ID of the quote     record.

- 
**[method](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_method)**  

Set the `method` property to specify the API request     method, such as POST or PATCH.

- 
**[type](./apex_class_placequote_RecordResource.htm.md#apex_placequote_RecordResource_type)**  

Set the type property to assign the object type that’s returned from the field describe     result by using the `getReferenceTo()` method or from the     sObject describe result by using the `getSObjectType()` method.

### fieldValues

Set the `fieldValues` property to assign values to the
    fields to update the quote record.

#### Signature

`public Map<String,ANY> fieldValues {get; set;}`

#### Property Value

Type: [List](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_methods_system_list.htm#apex_methods_system_list)
        <Map<String,ANY>>

### id

Set the `id` property to assign the ID of the quote
    record.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### method

Set the `method` property to specify the API request
    method, such as POST or PATCH.

#### Signature

`public String method {get; set;}`

#### Property Value

Type: String

### type

Set the type property to assign the object type that’s returned from the field describe
    result by using the `getReferenceTo()` method or from the
    sObject describe result by using the `getSObjectType()` method.

#### Signature

`public Schema.SObjectType type {get; set;}`

#### Property Value

Type: [Schema.SObjectType](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

=== ARTICLE: apex_class_placequote_RecordWithReferenceRequest.htm ===
---
page_id: apex_class_placequote_RecordWithReferenceRequest.htm
title: RecordWithReferenceRequest Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_placequote_RecordWithReferenceRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RecordWithReferenceRequest Class

Contains constructors and properties to associate a record object with a reference
    identifier.

## Namespace

[PlaceQuote](./apex_namespace_placequote.htm.md)

    

## Example

```
PlaceQuote.RecordWithReferenceRequest quoteLineRelationship = new PlaceQuote.RecordWithReferenceRequest('QuoteLineRelationship',quoteLineRelationship1);
```

See
          [PlaceQuoteRLMApexProcessor](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_placequote_PlaceQuoteRLMApexProcessor_example_implementation) to
        refer to an example implementation.

- 
**[RecordWithReferenceRequest Constructors](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_placequote_RecordWithReferenceRequest_constructors)**  

Learn more about the available constructors with the `RecordWithReferenceRequest` class.

- 
**[RecordWithReferenceRequest Properties](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_placequote_RecordWithReferenceRequest_properties)**  

Learn more about the available properties with the `RecordWithReferenceRequest` class.

  

## RecordWithReferenceRequest Constructors

  
  
  
Learn more about the available constructors with the `RecordWithReferenceRequest` class.

    
      

The `RecordWithReferenceRequest` class includes these
        constructors.

    

    
  

- 
**[RecordWithReferenceRequest(referenceId, record)](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_placequote_RecordWithReferenceRequest_ctor)**  

Creates an instance of the `RecordWithReferenceRequest` class to associate a record object with a reference     identifier by using the `referenceId` and `record` object properties.

### RecordWithReferenceRequest(referenceId, record)

Creates an instance of the `RecordWithReferenceRequest` class to associate a record object with a reference
    identifier by using the `referenceId` and `record` object properties.

#### Signature

`public RecordWithReferenceRequest(String referenceId, placequote.RecordResource record)`

#### Parameters

**referenceId**

: Type: String

: Reference ID that maps to the subrequest response and can be used to reference the response in
            subsequent subrequests. You can reference the referenceId in either the body or URL of a
            subrequest. Use this syntax to include a reference: @{referenceId.FieldName}. See [referenceId property of a
              composite subrequest](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_composite_graph_composite_subrequest.htm).

**record**

: Type: [placequote.RecordResource](./apex_class_placequote_RecordResource.htm.md#apex_class_placequote_RecordResource)

: Record object that’s defined using the `RecordResource` class.

  

## RecordWithReferenceRequest Properties

  
  
  
Learn more about the available properties with the `RecordWithReferenceRequest` class.

    
      

The `RecordWithReferenceRequest` class includes these
        properties.

    

    
  

- 
**[record](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_placequote_RecordWithReferenceRequest_record)**  

Set the `record` property to specify the record object     that’s defined by using the `RecordResource` class.

- 
**[referenceId](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_placequote_RecordWithReferenceRequest_referenceId)**  

Set the `referenceId` property to specify the reference     ID that maps to the subrequest response. This reference ID can be used to reference the response     in subsequent subrequests.

### record

Set the `record` property to specify the record object
    that’s defined by using the `RecordResource` class.

#### Signature

`public placequote.RecordResource record {get; set;}`

#### Property Value

Type: [placequote.RecordResource](./apex_class_placequote_RecordResource.htm.md#apex_class_placequote_RecordResource)

### referenceId

Set the `referenceId` property to specify the reference
    ID that maps to the subrequest response. This reference ID can be used to reference the response
    in subsequent subrequests.

#### Signature

`public String referenceId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_renew_assets_summary_RenewalOpptyDetail.htm ===
---
page_id: apex_class_renew_assets_summary_RenewalOpptyDetail.htm
title: RenewalOpptyDetail Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_renew_assets_summary_RenewalOpptyDetail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_renew_assets_summary.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RenewalOpptyDetail Class

Contains asset details and renewal pricing information for creating renewal opportunities.

## Namespace

[renew_assets_summary](./apex_namespace_renew_assets_summary.htm.md)

- 
**[RenewalOpptyDetail Constructors](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_constructors)**  

Learn more about the constructors available with the RenewalOpptyDetail     class.

- 
**[RenewalOpptyDetail Properties](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_properties)**  

Learn more about the properties available with the RenewalOpptyDetail     class.

  

## RenewalOpptyDetail Constructors

  
  
  
Learn more about the constructors available with the RenewalOpptyDetail
    class.

    
      

The `RenewalOpptyDetail` class includes these
        constructors.

    

    
  

- 
**[RenewalOpptyDetail(assetId, startDate, endDate, productId, account, priceBookId, priceBookEntryId, lastAssetActionSubtype, renewalPriceDetails, opportunityProductId, orderItem, rootAssetOpportunity, lastAssetAction, totalLineAmount)](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_ctor)**  

Initializes the RenewalOpptyDetail class that contains asset details and renewal pricing information.

### RenewalOpptyDetail(assetId, startDate, endDate, productId, account, priceBookId, priceBookEntryId, lastAssetActionSubtype, renewalPriceDetails, opportunityProductId, orderItem, rootAssetOpportunity, lastAssetAction, totalLineAmount)

Initializes the RenewalOpptyDetail class that contains asset details and renewal pricing information.

#### Signature

`public RenewalOpptyDetail(String assetId, Date startDate, Date endDate, String productId, String account, String priceBookId, String priceBookEntryId, String lastAssetActionSubtype, List<renew_assets_summary.RenewalPriceDetail> renewalPriceDetails, String opportunityProductId, String orderItem, String rootAssetOpportunity, String lastAssetAction, Decimal totalLineAmount)`

```
renew_assets_summary.RenewalOpptyDetail, newinstance, [String, Date, Date, String, String, String, String, String, List<renew_assets_summary.RenewalPriceDetail>, String, String, String, String, Decimal], renew_assets_summary.RenewalOpptyDetail
```

#### Parameters

**assetId**

: Type: String

: 

The ID of the asset.

**startDate**

: Type: Date

: 

The start date of the asset.

**endDate**

: Type: Date

: 

The end date of the asset.

**productId**

: Type: String

: 

The ID of the product associated with the asset.

**account**

: Type: String

: 

The ID of the account.

**priceBookId**

: Type: String

: 

The ID of the price book.

**priceBookEntryId**

: Type: String

: 

The ID of the price book entry.

**lastAssetActionSubtype**

: Type: String

: 

The subtype of the last action performed on the asset. Valid value is `Start Date Adjustment`.

**renewalPriceDetails**

: Type: List<[renew_assets_summary.RenewalPriceDetail](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_class_renew_assets_summary_RenewalPriceDetail)>

: 

List of renewal price details for the asset.

**opportunityProductId**

: Type: String

: 

The ID of the associated opportunity product.

**orderItem**

: Type: String

: 

The ID of the associated order item.

**rootAssetOpportunity**

: Type: String

: 

The ID of the root asset opportunity.

**lastAssetAction**

: Type: String

: 

The last action performed on the asset.

            
              
- `Initial Sale`

              
- `Upsell`

              
- `Downsell`

              
- `Renewal`

              
- `Cancellation`

            

**totalLineAmount**

: Type: Decimal

: 

The total line amount for the asset.

  

## RenewalOpptyDetail Properties

  
  
  
Learn more about the properties available with the RenewalOpptyDetail
    class.

    
      

The `RenewalOpptyDetail` class includes these
        properties.

    

    
  

- 
**[account](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_account)**  

Get or set the ID of the account.

- 
**[assetId](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_assetId)**  

Get or set the ID of the asset.

- 
**[endDate](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_endDate)**  

Get or set the end date of the asset.

- 
**[lastAssetAction](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_lastAssetAction)**  

Get or set the last action performed on the asset.

- 
**[lastAssetActionSubtype](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_lastAssetActionSubtype)**  

Get or set the subtype of the last action performed on the asset.

- 
**[opportunityProductId](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_opportunityProductId)**  

Get or set the ID of the associated opportunity product.

- 
**[orderItem](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_orderItem)**  

Get or set the ID of the associated order item.

- 
**[priceBookEntryId](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_priceBookEntryId)**  

Get or set the ID of the price book entry.

- 
**[priceBookId](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_priceBookId)**  

Get or set the ID of the price book.

- 
**[productId](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_productId)**  

Get or set the ID of the product associated with the asset.

- 
**[renewalPriceDetails](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_renewalPriceDetails)**  

Get or set the list of renewal price details for the asset.

- 
**[rootAssetOpportunity](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_rootAssetOpportunity)**  

Get or set the ID of the root asset opportunity.

- 
**[startDate](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_startDate)**  

Get or set the start date of the asset.

- 
**[totalLineAmount](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_renew_assets_summary_RenewalOpptyDetail_totalLineAmount)**  

Get or set the total line amount for the asset.

### account

Get or set the ID of the account.

#### Signature

`public String account {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, account
```

#### Property Value

Type: String

### assetId

Get or set the ID of the asset.

#### Signature

`public String assetId {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, assetId
```

#### Property Value

Type: String

### endDate

Get or set the end date of the asset.

#### Signature

`public Date endDate {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, endDate
```

#### Property Value

Type: Date

### lastAssetAction

Get or set the last action performed on the asset.

#### Signature

`public String lastAssetAction {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, lastAssetAction
```

#### Property Value

Type: String

Valid values are:

      
        
- `Initial Sale`

        
- `Upsell`

        
- `Downsell`

        
- `Renewal`

        
- `Cancellation`

      

### lastAssetActionSubtype

Get or set the subtype of the last action performed on the asset.

#### Signature

`public String lastAssetActionSubtype {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, lastAssetActionSubtype
```

#### Property Value

Type: String

Valid value is `Start Date Adjustment`.

### opportunityProductId

Get or set the ID of the associated opportunity product.

#### Signature

`public String opportunityProductId {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, opportunityProductId
```

#### Property Value

Type: String

### orderItem

Get or set the ID of the associated order item.

#### Signature

`public String orderItem {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, orderItem
```

#### Property Value

Type: String

### priceBookEntryId

Get or set the ID of the price book entry.

#### Signature

`public String priceBookEntryId {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, priceBookEntryId
```

#### Property Value

Type: String

### priceBookId

Get or set the ID of the price book.

#### Signature

`public String priceBookId {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, priceBookId
```

#### Property Value

Type: String

### productId

Get or set the ID of the product associated with the asset.

#### Signature

`public String productId {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, productId
```

#### Property Value

Type: String

### renewalPriceDetails

Get or set the list of renewal price details for the asset.

#### Signature

`public List<renew_assets_summary.RenewalPriceDetail> renewalPriceDetails {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, renewalPriceDetails
```

#### Property Value

Type: List<[renew_assets_summary.RenewalPriceDetail](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_class_renew_assets_summary_RenewalPriceDetail)>

### rootAssetOpportunity

Get or set the ID of the root asset opportunity.

#### Signature

`public String rootAssetOpportunity {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, rootAssetOpportunity
```

#### Property Value

Type: String

### startDate

Get or set the start date of the asset.

#### Signature

`public Date startDate {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, startDate
```

#### Property Value

Type: Date

### totalLineAmount

Get or set the total line amount for the asset.

#### Signature

`public Decimal totalLineAmount {get; set;}`

```
renew_assets_summary.RenewalOpptyDetail, totalLineAmount
```

#### Property Value

Type: Decimal

=== ARTICLE: apex_class_renew_assets_summary_RenewalPriceDetail.htm ===
---
page_id: apex_class_renew_assets_summary_RenewalPriceDetail.htm
title: RenewalPriceDetail Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_renew_assets_summary_RenewalPriceDetail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_renew_assets_summary.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RenewalPriceDetail Class

Contains net unit price and quantity details for an asset to set as sales price for renewal opportunities.

## Namespace

[renew_assets_summary](./apex_namespace_renew_assets_summary.htm.md)

- 
**[RenewalPriceDetail Constructors](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_renew_assets_summary_RenewalPriceDetail_constructors)**  

Learn more about the constructors available with the RenewalPriceDetail     class.

- 
**[RenewalPriceDetail Properties](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_renew_assets_summary_RenewalPriceDetail_properties)**  

Learn more about the properties available with the RenewalPriceDetail     class.

  

## RenewalPriceDetail Constructors

  
  
  
Learn more about the constructors available with the RenewalPriceDetail
    class.

    
      

The `RenewalPriceDetail` class includes these
        constructors.

    

    
  

- 
**[RenewalPriceDetail(netUnitPrice, quantity)](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_renew_assets_summary_RenewalPriceDetail_ctor)**  

Initializes the RenewalPriceDetail class that contains net unit price and quantity information.

### RenewalPriceDetail(netUnitPrice, quantity)

Initializes the RenewalPriceDetail class that contains net unit price and quantity information.

#### Signature

`public RenewalPriceDetail(Decimal netUnitPrice, Decimal quantity)`

```
renew_assets_summary.RenewalPriceDetail, newinstance, [Decimal, Decimal], renew_assets_summary.RenewalPriceDetail
```

#### Parameters

**netUnitPrice**

: Type: Decimal

: 

The net unit price of the asset.

**quantity**

: Type: Decimal

: 

The quantity of the asset.

  

## RenewalPriceDetail Properties

  
  
  
Learn more about the properties available with the RenewalPriceDetail
    class.

    
      

The `RenewalPriceDetail` class includes these
        properties.

    

    
  

- 
**[netUnitPrice](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_renew_assets_summary_RenewalPriceDetail_netUnitPrice)**  

Get or set the net unit price of the asset.

- 
**[quantity](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_renew_assets_summary_RenewalPriceDetail_quantity)**  

Get or set the quantity of the asset.

### netUnitPrice

Get or set the net unit price of the asset.

#### Signature

`public Decimal netUnitPrice {get; set;}`

```
renew_assets_summary.RenewalPriceDetail, netUnitPrice
```

#### Property Value

Type: Decimal

### quantity

Get or set the quantity of the asset.

#### Signature

`public Decimal quantity {get; set;}`

```
renew_assets_summary.RenewalPriceDetail, quantity
```

#### Property Value

Type: Decimal

=== ARTICLE: apex_connectapi_input_ramp_option.htm ===
---
page_id: apex_connectapi_input_ramp_option.htm
title: ConnectApi.RampOptionInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_ramp_option.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: transaction_management_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.RampOptionInputRepresentation

Input representation of the ramp option details during an asset renewal.

This Apex class is used by the `rampOptionDetails`
        Apex-defined input variable. See [Initiate Renewal Action](./actions_obj_renew_assets.htm.md).

          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              
- 
- 

              

              

            

          

        
| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `durationInMonths` | Double | Maximum duration of all ramp segments. | Required | 67.0 |
| `segmentCount` | Double | Number of created ramp segments based on the specified duration. | Required if you specify `Custom` value for the `segmentType` property. | 67.0 |
| `segmentType` | `ConnectApi.RampSegmentType` | Type of ramp schedule. Valid values are: `Custom`—Specifies the number of segments. The total duration is divided equally across segments. `Yearly`—Creates 12-month segments. If the total duration isn't a multiple of 12, the last segment covers the remaining months. If the duration divided by the number of months has a remainder, that segment is listed first as a prorated segment. | Required | 67.0 |

=== ARTICLE: apex_connectapi_input_transfer_record.htm ===
---
page_id: apex_connectapi_input_transfer_record.htm
title: ConnectApi.TransferRecordInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_transfer_record.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: transaction_management_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.TransferRecordInputRepresentation

Input representation of the details of the assets to be transferred.

This Apex class is used by the `transferRecords`
        apex-defined input variable. See [Initiate Transfer Action](./actions_obj_initiate_transfer.htm.md).

          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetId` | String | ID of the asset to transfer. | Required | 65.0 |
| `transferQuantity` | Double | Transfer quantity for the request. | Required | 65.0 |

=== ARTICLE: apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm
title: CatalogRatesPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CatalogRatesPreferenceEnum Enum

Specifies the rate card entries defined in the catalog that must be fetched for quote
    line items, with usage-based selling during the place sales transaction process.

## Usage

This enum is available when [Usage Selling](https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_sellling.htm&language=en_US) is enabled.

## Enum Values

The `RevSalesTrxn.CatalogRatesPreferenceEnum` enum includes
        these values.

| Value | Description |
| --- | --- |
| `Fetch` | Retrieves the rate card entries defined in the catalog for quote line items during the quote creation process. |
| `Skip` | Skips the retrieval of rate card entries for quote line items during the quote creation process. The default value is `Skip`. |

=== ARTICLE: apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm
title: ConfigurationExecutionEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationExecutionEnum Enum

Specifies the configuration method for the place sales transaction request.

## Usage

      

Use these enum values for the `configurationExecutionEnum` property in the [PlaceSalesTransactionExecutor](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor) class.

## Enum Values

The `RevSalesTrxn.ConfigurationExecutionEnum` enum has these
        values.

| Value | Description |
| --- | --- |
| `Force` | Specifies to enforce the predefined configuration process during the sales transaction process. |
| `Skip` | Specifies to skip the configuration process during the quote creation process. The default value is `Skip`. |
| `System` | Specifies the system to determine whether the configuration process is required. |

=== ARTICLE: apex_enum_RevSalesTrxn_GroupRampActionEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_GroupRampActionEnum.htm
title: GroupRampActionEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_GroupRampActionEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GroupRampActionEnum Enum

Specifies the action ‌that you want to perform on group ramp segments. Additionally,
    you can also convert a non-ramped group into a ramped group. 

    

## Enum Values

The `RevSalesTrxn.GroupRampActionEnum` enum includes these values.

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `AddProducts` | Specifies to add rampable products to group ramp segments. |
| `DeleteProducts` | Specifies to delete ramped products. |
| `EditGroup` | Specifies to convert a non-ramped group into a group ramp segment, or edit group ramp segment attributes such as name and description, except the start and end dates. |
| `EditRampSchedule` | Specifies to edit details of the group ramp segments, including start and end dates. |
| `DeleteSegment` | Specifies to delete the first or last segment in a group ramp schedule. |
| `ConvertToNonRampedGroup` | Specifies to convert the first or last group ramp segment into a non-ramped group. |

To add or delete ramped line items from multiple group ramp segments, pass all the applicable
        values in the `graph` request. To refer to Connect API
        examples that specify actions to create ramp deals for groups, see [Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md).

=== ARTICLE: apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm
title: PersistPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PersistPreferenceEnum Enum

Specifies whether to persist pricing changes for each sales transaction record.
    Available in API version 65.0 and later.

    

## Enum Values

      
      

The `RevSalesTrxn.PersistPreferenceEnum` enum includes
        this value.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `Skip` | Skips the persistence of pricing changes for each sales transaction record. To persist pricing changes, specify `null` as the value in the method signature. If this value isn't specified, then request to persist pricing changes is performed by default. |

=== ARTICLE: apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm
title: PricingPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PricingPreferenceEnum Enum

Specifies the pricing preference during the creation of a sales transaction.

## Usage

      

Used by the [PlaceSalesTransactionExecutor](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor) class.

## Enum Values

The `RevSalesTrxn.PricingPreferenceEnum` enum includes these
        values.

| Value | Description |
| --- | --- |
| `Force` | Specifies to enforce pricing during the creation of sales transactions. |
| `Skip` | Specifies to skip pricing during the creation of sales transactions. |
| `System` | Specifies the system to determine whether a pricing calculation is required. The default value is `System`. |

=== ARTICLE: apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm ===
---
page_id: apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm
title: TaxPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_RevSalesTrxn.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxPreferenceEnum Enum

Specifies whether to execute or skip the tax calculation step for each sales
    transaction record. Available in API version 65.0 and later.

    

## Enum Values

      
      

The `RevSalesTrxn.TaxPreferenceEnum` enum includes this
        value.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `Skip` | Specifies to skip tax calculation request for each sales transaction record. If this value isn't specified, then tax calculation request is performed by default. |

=== ARTICLE: apex_enum_commerceorders_CatalogRatesPreferenceEnum.htm ===
---
page_id: apex_enum_commerceorders_CatalogRatesPreferenceEnum.htm
title: CatalogRatesPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commerceorders_CatalogRatesPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CatalogRatesPreferenceEnum Enum

Specifies the rate card entries defined in the catalog that must be fetched for order
    items, with usage-based selling during the order creation process.

## Usage

This enum is available when the Usage-Based Selling feature is enabled.

## Enum Values

The `commerceorders.CatalogRatesPreferenceEnum` enum includes
        these values.

| Value | Description |
| --- | --- |
| `Fetch` | Retrieves the rate card entries defined in the catalog for order items during the order creation process. |
| `Skip` | Skips the retrieval of rate card entries for order items during the order creation process. The default value is `Skip`. |

=== ARTICLE: apex_enum_commerceorders_ConfigurationInputEnum.htm ===
---
page_id: apex_enum_commerceorders_ConfigurationInputEnum.htm
title: ConfigurationInputEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commerceorders_ConfigurationInputEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationInputEnum Enum

Specifies the configuration input for the request to place an order.

## Usage

Use these enum values for the `configurationInputEnum` property
        in the [PlaceOrderExecutor Class](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_class_commerceorders_PlaceOrderExecutor)

## Enum Values

The `commerceorders.ConfigurationInputEnum` enum has these
        values.

| Value | Description |
| --- | --- |
| `RunAndAllowErrors` | Run the configuration and proceed with order ingestion upon encountering any configuration errors. |
| `RunAndBlockErrors` | Run the configuration and block order ingestion upon encountering any configuration errors. |
| `Skip` | Skip the configuration execution. |

=== ARTICLE: apex_enum_commerceorders_PricingPreferenceEnum.htm ===
---
page_id: apex_enum_commerceorders_PricingPreferenceEnum.htm
title: PricingPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commerceorders_PricingPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commerceorders.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PricingPreferenceEnum Enum

Specifies the pricing preference during the create order process.

## Usage

Used by the [PlaceOrderExecutor](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_class_commerceorders_PlaceOrderExecutor)
        class.

## Enum Values

The `commerceorders.PricingPreferenceEnum` enum includes these
        values.

| Value | Description |
| --- | --- |
| `Force` | Enforce pricing during the order ingestion process. |
| `Skip` | Skip pricing during the order ingestion process. |
| `System` | Determine whether a pricing calculation is required. |

=== ARTICLE: apex_enum_commercetax_CalculateTaxType.htm ===
---
page_id: apex_enum_commercetax_CalculateTaxType.htm
title: CalculateTaxType Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commercetax_CalculateTaxType.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CalculateTaxType Enum

Shows whether a tax calculation request is for estimated or actual
      tax.

    

## Usage

      
      

Used by the [CalculateTaxRequest](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_class_commercetax_CalculateTaxRequest) and [CalculateTaxResponse](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_class_commercetax_CalculateTaxResponse) class methods.

    

    

## Enum Values

      
      

The `commercetax.CalculateTaxType` enum includes these
        values.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `Actual` | Specifies that the tax calculation service should calculate the finalized (actual) tax for the requested line items. |
| `Estimated` | Specifies that the tax calculation service should estimate the tax for the requested line items. |

=== ARTICLE: apex_enum_commercetax_RequestType.htm ===
---
page_id: apex_enum_commercetax_RequestType.htm
title: RequestType Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commercetax_RequestType.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RequestType Enum

Shows the type of tax request made to the tax
    engine.

    

## Usage

      
      

Used by the [TaxEngineContext](./apex_class_commercetax_TaxEngineContext.htm.md#apex_class_commercetax_TaxEngineContext)
        class method. 

    

    

## Enum Values

      
      

The `commercetax.RequestType` enum includes these
        values.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `CalculateTax` | Represents a request to calculate tax on a list of taxable line items. |

=== ARTICLE: apex_enum_commercetax_ResultCode.htm ===
---
page_id: apex_enum_commercetax_ResultCode.htm
title: ResultCode Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commercetax_ResultCode.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ResultCode Enum

Code that represents the results of a tax request made to the tax
      engine.

    

## Usage

      
      

Used by the [ErrorResponse](./apex_class_commercetax_ErrorResponse.htm.md#apex_class_commercetax_ErrorResponse)
        class method.

    

    

## Enum Values

      
      

The `commercetax.ResultCode` enum includes these
        values.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `TaxEngineError` | Represents an error that occurred during the tax request process. |
| `ReferenceDocumentCodeMissing` | Specifies if the document mentioned as a `referenceDocumentCode` value isn't available in the tax engine. |

=== ARTICLE: apex_enum_commercetax_TaxTransactionStatus.htm ===
---
page_id: apex_enum_commercetax_TaxTransactionStatus.htm
title: TaxTransactionStatus Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commercetax_TaxTransactionStatus.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxTransactionStatus Enum

Shows whether the tax transaction has been committed or
      uncommitted.

    

## Usage

      
      

Used by the [CalculateTaxResponse](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_class_commercetax_CalculateTaxResponse) class method.

    

    

## Enum Values

      
      

The `commercetax.TaxTransactionStatus` enum includes
        these values.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `Committed` | Tax has been calculated and committed. |
| `Uncommitted` | Tax has been calculated but hasn't been committed. |

=== ARTICLE: apex_enum_commercetax_TaxTransactionType.htm ===
---
page_id: apex_enum_commercetax_TaxTransactionType.htm
title: TaxTransactionType Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_commercetax_TaxTransactionType.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxTransactionType Enum

Shows whether the tax transaction is for a credit or debit
      transaction.

    

## Usage

      
      

Used by the [CalculateTaxResponse](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_class_commercetax_CalculateTaxResponse) and [CalculateTaxRequest](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_class_commercetax_CalculateTaxRequest) class
        methods.

    

    

## Enum Values

      
      

The `commercetax.TaxTransactionType` enum includes
        these values.

      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Value | Description |
| --- | --- |
| `Credit` | Represents a credit transaction. |
| `Debit` | Represents a debit transaction. |
| `Void` | Specifies that the tax engine has voided the document that's mentioned in the `referenceDocumentCode` property value. |

=== ARTICLE: apex_enum_placequote_CatalogRatesPreferenceEnum.htm ===
---
page_id: apex_enum_placequote_CatalogRatesPreferenceEnum.htm
title: CatalogRatesPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_placequote_CatalogRatesPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CatalogRatesPreferenceEnum Enum

Specifies the rate card entries defined in the catalog that must be fetched for quote
    line items, with usage-based selling during the quote creation process.

## Usage

This enum is available when the Usage-Based Selling feature is enabled.

## Enum Values

The `placequote.CatalogRatesPreferenceEnum` enum includes these
        values.

| Value | Description |
| --- | --- |
| `Fetch` | Retrieves the rate card entries defined in the catalog for quote line items during the quote creation process. |
| `Skip` | Skips the retrieval of rate card entries for quote line items during the quote creation process. The default value is `Skip`. |

=== ARTICLE: apex_enum_placequote_ConfigurationInputEnum.htm ===
---
page_id: apex_enum_placequote_ConfigurationInputEnum.htm
title: ConfigurationInputEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_placequote_ConfigurationInputEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigurationInputEnum Enum

Specifies the configuration input for the request to place a quote.

## Usage

Use these enum values for the `configurationInputEnum` property
        in the [PlaceQuoteRLMApexProcessor](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_class_placequote_PlaceQuoteRLMApexProcessor) class.

## Enum Values

The `placequote.ConfigurationInputEnum` enum has these
        values.

| Value | Description |
| --- | --- |
| `RunAndAllowErrors` | Run the configuration and proceed with order ingestion upon encountering any configuration errors. |
| `RunAndBlockErrors` | Run the configuration and block order ingestion upon encountering any configuration errors. |
| `Skip` | Skip the configuration execution. |

=== ARTICLE: apex_enum_placequote_PricingPreferenceEnum.htm ===
---
page_id: apex_enum_placequote_PricingPreferenceEnum.htm
title: PricingPreferenceEnum Enum
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_enum_placequote_PricingPreferenceEnum.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_placequote.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PricingPreferenceEnum Enum

Specifies the pricing preference during the create quote process.

## Usage

Used by the [PlaceQuoteRLMApexProcessor](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_class_placequote_PlaceQuoteRLMApexProcessor) class.

## Enum Values

The `placequote.PricingPreferenceEnum` enum class includes these
        values.

| Value | Description |
| --- | --- |
| `Force` | Enforce pricing during the quote ingestion process. |
| `Skip` | Skip pricing during the quote ingestion process. |
| `System` | Determine whether a pricing calculation is required. |

=== ARTICLE: apex_interface_commercetax_TaxEngineAdapter.htm ===
---
page_id: apex_interface_commercetax_TaxEngineAdapter.htm
title: TaxEngineAdapter Interface
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_interface_commercetax_TaxEngineAdapter.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: apex_namespace_commercetax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

  

# TaxEngineAdapter Interface

  
  
  
Retrieves information from the tax engine and evaluates the information to define tax
    details.

    

## Namespace

      
      

[CommerceTax](./apex_namespace_commercetax.htm.md)

    

  

- 
**[TaxEngineAdapter Methods](./apex_interface_commercetax_TaxEngineAdapter.htm.md#apex_commercetax_TaxEngineAdapter_methods)**  

Learn more about the available methods with the `TaxEngineAdapter` class.

- 
**[TaxEngineAdapter Example Implementation](./apex_interface_commercetax_TaxEngineAdapter.htm.md#apex_interface_commercetax_TaxEngineAdapter_Example)**  

Refer to the example implementation of the `TaxEngineAdapter` interface to accept information from a tax engine and         evaluate the information to define tax details.

- 
**[Tax Mappings for Quotes and Orders](./apex_interface_commercetax_TaxEngineAdapter.htm.md#tax_contract_mappings_for_quotes_and_orders)**  

You can extend and customize the tax interface for quotes and orders by using custom     metadata types and tax mappings. These customizations help you with unique business requirements     such as the inclusion of specific data for accurate calculations and audits.

  

## TaxEngineAdapter Methods

  
  
  
Learn more about the available methods with the `TaxEngineAdapter` class.

    
      

The `TaxEngineAdapter` class includes these
        methods.

    

    
  

- 
**[processRequest(requestType)](./apex_interface_commercetax_TaxEngineAdapter.htm.md#apex_commercetax_TaxEngineAdapter_processRequest)**  

The `processRequest` method takes       an instance of `TaxEngineContext` class and returns a       response with the calculated tax details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

  

### processRequest(requestType)

  
  
  
The `processRequest` method takes
      an instance of `TaxEngineContext` class and returns a
      response with the calculated tax details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

    

#### Signature

`global commercetax.TaxEngineResponse
          processRequest(commercetax.TaxEngineContext var1)`

    

#### Parameters

        
- 
**var1**:

Type: [TaxEngineContext](./apex_class_commercetax_TaxEngineContext.htm.md#apex_class_commercetax_TaxEngineContext)

Wrapper class that stores information about

the type of a tax calculation
            request.

      

    

#### Return Value

Type:
        TaxEngineResponse

Generic interface representing a response from a tax engine.

  

    

## TaxEngineAdapter Example Implementation

    
    
    
Refer to the example implementation of the `TaxEngineAdapter` interface to accept information from a tax engine and
        evaluate the information to define tax details.

        

### Namespace

            
            

[commercetax](./apex_namespace_commercetax.htm.md)

        

        

### Usage

The `TaxEngineAdapter` interface accepts information from the
                tax engine through the `TaxEngineContext` class.
                The interface evaluates the information to define tax in the response with details,
                such as tax amount and addresses. The response is used to update and create entities
                in the Salesforce org.

Use these steps to build a sample tax adapter implementation. Each tax
                adapter implementation varies based on your implementation requirements. Customize
                this example to suit your business requirements.

        

### Example

            
                
- 
                    

The custom adapter class implements the `TaxEngineAdapter` interface. The `processRequest` method takes an instance of `TaxEngineContext` class and returns a response
                        with the calculated tax details through the `TaxDetailsResponse` class or an error response through the
                            `ErrorResponse` class.

                    

```

global virtual class AvalaraAdapter implements commercetax.TaxEngineAdapter {
    global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext taxEngineContext) {
        commercetax.RequestType requestType = taxEngineContext.getRequestType();
        if(requestType == commercetax.RequestType.CalculateTax){
            return CalculateTaxService.getTax(taxEngineContext);
        }
        else 
            return null;
    }
}
```

                

                
- 
                    

This example shows the `CalculateTaxService`
                        class.

                    

```
global class CalculateTaxService {
    // ============================================================================
    // CONSTANT 
    // ============================================================================
    private static final String AVALARA_ENDPOINT_URL_SANDBOX = 'https://sandbox-rest.avatax.com/api/v2';
    // Avalara Endpoint URL Production
    private static final String AVALARA_ENDPOINT_URL_PRODUCTION = 'https://rest.avatax.com/api/v2';
    private static final String TEST_REQUEST_BODY = '{  "id": -1,  "code": "00000131",  "companyId": -1,  "date": "2017-02-03T00:00:00",  "taxDate": "2017-02-03T00:00:00",  "status": "Temporary",  "type": "SalesOrder",  "reconciled": false,  "totalAmount": 4000,  "totalExempt": 0,  "totalTax": 290,  "totalTaxable": 4000,  "totalTaxCalculated": 290,  "adjustmentReason": "NotAdjusted",  "locked": false,  "version": 1,  "modifiedDate": "2017-02-03T12:18:18.7347388Z",  "modifiedUserId": 53894,  "lines": [    {      "id": -1,      "transactionId": -1,      "lineNumber": "80241000000jNDCAA2",      "discountAmount": 0,      "exemptAmount": 0,      "exemptCertId": 0,      "isItemTaxable": true,      "lineAmount": 1000,      "reportingDate": "2017-02-03T00:00:00",      "tax": 72.5,      "taxableAmount": 1000,      "taxCalculated": 72.5,      "taxCode": "P0000000",      "taxDate": "2017-02-03T00:00:00",      "taxIncluded": false,      "details": [        {          "id": -1,          "transactionLineId": -1,          "transactionId": -1,          "country": "US",          "region": "CA",          "exemptAmount": 0,          "jurisCode": "06",          "jurisName": "CALIFORNIA",          "stateAssignedNo": "",          "jurisType": "STA",          "nonTaxableAmount": 0,          "rate": 0.06,          "tax": 60,          "taxableAmount": 1000,          "taxType": "Sales",          "taxName": "CA STATE TAX",          "taxAuthorityTypeId": 45,          "taxCalculated": 60,          "rateType": "General"        },        {          "id": -1,          "transactionLineId": -1,          "transactionId": -1,          "country": "US",          "region": "CA",          "exemptAmount": 0,          "jurisCode": "075",          "jurisName": "SAN FRANCISCO",          "stateAssignedNo": "",          "jurisType": "CTY",          "nonTaxableAmount": 0,          "rate": 0.0025,          "tax": 2.5,          "taxableAmount": 1000,          "taxType": "Sales",          "taxName": "CA COUNTY TAX",          "taxAuthorityTypeId": 45,          "taxCalculated": 2.5,          "rateType": "General"        },        {          "id": -1,          "transactionLineId": -1,          "transactionId": -1,          "country": "US",          "region": "CA",          "exemptAmount": 0,          "jurisCode": "EMTV0",          "jurisName": "SAN FRANCISCO CO LOCAL TAX SL",          "stateAssignedNo": "38",          "jurisType": "STJ",          "nonTaxableAmount": 0,          "rate": 0.01,          "tax": 10,          "taxableAmount": 1000,          "taxType": "Sales",          "taxName": "CA SPECIAL TAX",          "taxAuthorityTypeId": 45,          "taxCalculated": 10,          "rateType": "General"        }      ]    }  ]}';
    
    private static String getTestResponseString(){
    
     List<String> jsonResponse = new List<String> {
                                    '"id": 0',
                                    '"code": "testDocCode1231245984"',
                                    '"companyId": 468039',
                                    '"date": "2020-07-15"',
                                    '"paymentDate": "2020-07-15"',
                                    '"status": "Temporary"',
                                    '"type": "SalesOrder"',
                                    '"customerVendorCode": "testDocCode1234"',
                                    '"customerCode": "testDocCode1234"',
                                    '"reconciled": false',
                                    '"totalAmount": 232',
                                    '"totalExempt": 0',
                                    '"totalDiscount": 0',
                                    '"totalTax": 23.43',
                                    '"totalTaxable": 232',
                                    '"totalTaxCalculated": 23.43',
                                    '"adjustmentReason": "NotAdjusted"',
                                    '"locked": false',
                                    '"version": 1',
                                    '"exchangeRateEffectiveDate": "2020-07-15"',
                                    '"exchangeRate": 1',
                                    '"modifiedDate": "2020-08-13T11:19:20.4836636Z"',
                                    '"modifiedUserId": 53894',
                                    '"taxDate": "2020-07-15T00:00:00"',
                                    '"lines": [{"id": 0,"transactionId": 0,"lineNumber": "1","discountAmount": 0,"exemptAmount": 0,"exemptCertId": 0,"isItemTaxable": true,"itemCode": "","lineAmount": 232,"quantity": 1,"reportingDate": "2020-07-15","tax": 23.43,"taxableAmount": 232,"taxCalculated": 23.43,"taxCode": "P0000000","taxCodeId": 8087,"taxDate": "2020-07-15","taxOverrideType": "None","taxOverrideAmount": 0,"taxIncluded": false,"details": [{"id": 0,"transactionLineId": 0,"transactionId": 0,"country": "US","region": "WA","exemptAmount": 0,"jurisCode": "53","jurisName": "WASHINGTON","stateAssignedNo": "","jurisType": "STA","jurisdictionType": "State","nonTaxableAmount": 0,"rate": 0.065,"tax": 15.08,"taxableAmount": 232,"taxType": "Sales","taxSubTypeId": "S","taxName": "WA STATE TAX","taxAuthorityTypeId": 45,"taxCalculated": 15.08,"rateType": "General","rateTypeCode": "G","unitOfBasis": "PerCurrencyUnit","isNonPassThru": false,"isFee": false},{"id": 0,"transactionLineId": 0,"transactionId": 0,"country": "US","region": "WA","exemptAmount": 0,"jurisCode": "033","jurisName": "KING","stateAssignedNo": "1700","jurisType": "CTY","jurisdictionType": "County","nonTaxableAmount": 0,"rate": 0,"tax": 0,"taxableAmount": 232,"taxType": "Sales","taxSubTypeId": "S","taxName": "WA COUNTY TAX","taxAuthorityTypeId": 45,"taxCalculated": 0,"rateType": "General","rateTypeCode": "G","unitOfBasis": "PerCurrencyUnit","isNonPassThru": false,"isFee": false}],"nonPassthroughDetails": [],"hsCode": "","costInsuranceFreight": 0,"vatCode": "","vatNumberTypeId": 0}]',
                                    '"addresses": [{"id": 0,"transactionId": 0,"boundaryLevel": "Address","line1": "255 S. King Street","line2": "","line3": "","city": "Seattle","region": "WA","postalCode": "98104","country": "US","taxRegionId": 2109700,"latitude": "47.59821","longitude": "-122.33108"}]',
                                    '"summary": [{"country": "US","region": "WA","jurisType": "State","jurisCode": "53","jurisName": "WASHINGTON","taxAuthorityType": 45,"stateAssignedNo": "","taxType": "Sales","taxSubType": "S","taxName": "WA STATE TAX","rateType": "General","taxable": 232,"rate": 0.065,"tax": 15.08,"taxCalculated": 15.08,"nonTaxable": 0,"exemption": 0},{"country": "US","region": "WA","jurisType": "County","jurisCode": "033","jurisName": "KING","taxAuthorityType": 45,"stateAssignedNo": "1700","taxType": "Sales","taxSubType": "S","taxName": "WA COUNTY TAX","rateType": "General","taxable": 232,"rate": 0,"tax": 0,"taxCalculated": 0,"nonTaxable": 0,"exemption": 0}]'
                                };
            return '{' + String.join(jsonResponse, ',') + '}';
        }
    
    public static commercetax.TaxEngineResponse getTax(commercetax.TaxEngineContext taxEngineContext) 
    { 
        commercetax.CalculateTaxRequest request = (commercetax.CalculateTaxRequest)taxEngineContext.getRequest();
        commercetax.calculatetaxtype requestType = request.taxtype;
        string referenceEntity = request.ReferenceEntityId;
        try{
            List<commercetax.TaxLineItemRequest> listOfLines = request.lineItems;
            if(!listOfLines.isEmpty()){
                HttpService sendHttpRequest = new HttpService();
                sendHttpRequest.addHeader('Content-type', 'application/json');
                String requestBody = AvalaraJSONBuilder.getInstance().frameJsonForGetTaxOrderItem(request);
                sendHttpRequest.post('/transactions/create',requestBody);
                //system.debug('Request '+requestBody);
                String responseString = '';
                if(Test.isRunningTest()){
                    responseString = getTestResponseString();
                } else{
                    responseString = sendHttpRequest.getResponse().getBody();
                }
                //system.debug(sendHttpRequest.getResponse());
                //system.debug('response'+responseString);
                //responseString = TEST_REQUEST_BODY;
                system.debug('Heap size used ' +Limits.getHeapSize());
                
                if(!responseString.contains('error'))
                {
                    commercetax.CalculateTaxResponse response = new commercetax.CalculateTaxResponse();
                    JsonSuccessParser jsonSuccessParserClass = JsonSuccessParser.parse(responseString);
                    response.setTaxTransactionType(request.taxTransactionType);
                    response.setDocumentCode(jsonSuccessParserClass.code);
                    response.setReferenceDocumentCode(jsonSuccessParserClass.referenceCode);
                    if(jsonSuccessParserClass.status == 'Temporary')  {
                        response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);
                    }
                    if(jsonSuccessParserClass.status == 'Committed') {
                        response.setStatus(commercetax.TaxTransactionStatus.Committed);
                    }
                    response.setTaxType(requestType);
                    commercetax.AmountDetailsResponse headerAmountResponse = new commercetax.AmountDetailsResponse();
                    headerAmountResponse.setTotalAmountWithTax(jsonSuccessParserClass.totalAmount + jsonSuccessParserClass.totaltax);
                    headerAmountResponse.setExemptAmount(jsonSuccessParserClass.totalExempt);
                    headerAmountResponse.setTotalAmount(jsonSuccessParserClass.totalAmount);
                    headerAmountResponse.setTaxAmount(jsonSuccessParserClass.totalTax);
                    response.setAmountDetails(headerAmountResponse);
                    response.setStatusDescription(jsonSuccessParserClass.adjustmentReason);
                    response.setEffectiveDate(date.valueof(jsonSuccessParserClass.taxDate));
                    response.setTransactionDate(date.valueof(jsonSuccessParserClass.transactionDate));
                    response.setReferenceEntityId(referenceEntity);
                    response.setTaxTransactionId(jsonSuccessParserClass.id);
                    response.setCurrencyIsoCode(request.currencyIsoCode);
                    List<commercetax.LineItemResponse> lineItemResponses = new List<commercetax.LineItemResponse>();
                    for(JsonSuccessParser.Lines linesToProcess: jsonSuccessParserClass.lines)
                    {
                        commercetax.LineItemResponse lineItemResponse = new commercetax.LineItemResponse();
                        Double rateCalculated = 0.0;
                        List<commercetax.TaxDetailsResponse> taxDetailsResponses = new List<commercetax.TaxDetailsResponse>();
                        for(JsonSuccessParser.details linesDetails : linesToProcess.details)
                        {
                            commercetax.TaxDetailsResponse taxDetailsResponse = new commercetax.TaxDetailsResponse();
                            if(linesDetails.exemptAmount != 0){
                                taxDetailsResponse.setExemptAmount(linesDetails.exemptAmount);
                                taxDetailsResponse.setExemptReason('Some reason we dont know');
                            }
                                commercetax.ImpositionResponse imposition = new commercetax.ImpositionResponse();
                                    imposition.setSubType(linesDetails.taxName);
                                    imposition.setType(linesDetails.ratetype);
                                    imposition.setSubType(linesDetails.taxName);
                                    taxDetailsResponse.setImposition(imposition);
                                commercetax.JurisdictionResponse jurisdiction = new commercetax.JurisdictionResponse();
                                    jurisdiction.setCountry(linesDetails.country);
                                    jurisdiction.setRegion(linesDetails.region);
                                    jurisdiction.setName(linesDetails.jurisName);
                                    jurisdiction.setStateAssignedNumber(linesDetails.stateAssignedNo);
                                    jurisdiction.setId(linesDetails.jurisCode);
                                    jurisdiction.setLevel(linesDetails.jurisType);
                                    taxDetailsResponse.setJurisdiction(jurisdiction);
                                    rateCalculated += linesDetails.rate; 
                                taxDetailsResponse.setRate(rateCalculated);
                                taxDetailsResponse.setTax(linesDetails.taxCalculated);
                                taxDetailsResponse.setTaxableAmount(linesDetails.taxableAmount);
                                taxDetailsResponse.setTaxAuthorityTypeId(String.valueOf(linesDetails.taxAuthorityTypeId));
                                taxDetailsResponse.setTaxId(linesDetails.id);
                                taxDetailsResponse.setTaxRegionId(linesDetails.region);
                                taxDetailsResponses.add(taxDetailsResponse);    
                            
                        }
                            lineItemResponse.setTaxes(taxDetailsResponses);
                            lineItemResponse.setEffectiveDate(date.valueof(linesToProcess.taxDate));
                            lineItemResponse.setIsTaxable(true);
                                commercetax.AmountDetailsResponse amountResponse = new commercetax.AmountDetailsResponse();
                                amountResponse.setTaxAmount(linesToProcess.taxCalculated);
                                amountResponse.setTotalAmount(linesToProcess.lineAmount);
                                amountResponse.setTotalAmountWithTax(linesToProcess.lineAmount+linesToProcess.taxCalculated);
                                amountResponse.setExemptAmount(linesToProcess.exemptAmount);
                                lineItemResponse.setAmountDetails(amountResponse);
                            lineItemResponse.setIsTaxable(linesToProcess.isItemTaxable);
                            lineItemResponse.setProductCode(linesToProcess.itemCode);
                            lineItemResponse.setTaxCode(linesToProcess.taxCode);
                            lineItemResponse.setLineNumber(linesToProcess.lineNumber);
                            lineItemResponse.setQuantity(linesToProcess.quantity);
                            lineItemResponses.add(lineItemResponse);
                    }
                    response.setLineItems(lineItemResponses);
                    return response;
                }
                else
                {
                    JsonErrorParser jsonErrorParserClass = JsonErrorParser.parse(responseString);
                    String message = null;
                    if(String.isNotBlank(jsonErrorParserClass.error.message))
                    {
                       message=jsonErrorParserClass.error.message;
                    }else{
                           String errorMessage = '';
                            for(JsonErrorParser.cls_details messageString : jsonErrorParserClass.error.details)
                            {
                                if(String.isNotBlank(messageString.message) )
                                {
                                    errorMessage = messageString.message;
                                }
                            }
                            message = errorMessage; 
                        }
                     return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '501', message);

                }
            }else return null;
        }
        catch (Exception e) 
        {
            throw e; 
        }
    }
}
```

                

                
- 
                    

In the `HttpService` class, replace the
                            `test` value in the endpoint variable
                        with the name of the `TaxTypedNamedCredential` record. This class contains the
                        credentials that are required to access your Avalara account through
                        Salesforce.

                    

```

public with sharing class HttpService 
{   
    // Attribute to implement singleton pattern for Order Product Service class
    private static HttpService httpServiceInstance;
    
    // VARIABLES
    
    private HttpResponse httpResponse;
    private Map<String,String> mapOfHeaderParameter = new Map<String,String>();
    private enum Method {GET, POST}
    
    /**
    * @name getInstance
    * @description get an Instance of Service class
    * @params NA
    * @return Http Service Class Instance
    */ 
    public static HttpService getInstance() 
    {
        if (NULL == httpServiceInstance) 
        {
            httpServiceInstance =  new HttpService();  
        }
        return httpServiceInstance;
    }
    
    /**
    * @name get
    * @description Get Method to get a HTTP request
    */    
    public void get(String endPoint) 
    {
        send(newRequest(Method.GET, endPoint));
    }
    
    /**
    * @name post
    * @description Post Method to Post a HTTP request
    */ 
    public void post(String path, String requestBody)
    {
       String endPoint = 'callout:commerce.tax.TaxTypedNamedCredential:test'+path;
        send(newRequest(Method.POST, endPoint, requestBody));
    }
    
    /**
    * @name addHeader
    * @description addHeader Methods to add all the defualt Header's required fo rthe request
    */
    public void addHeader(String name, String value)
    {
        mapOfHeaderParameter.put(name, value);
    }
    
    /**
    * @name setHeader
    * @description setHeader Methods to set setHeader for the request
    */
    private void setHeader(HttpRequest request) 
    {
        for(String headerValue : mapOfHeaderParameter.keySet())
        {
            request.setHeader(headerValue, mapOfHeaderParameter.get(headerValue));
        }
    }
    /**
    * @name newRequest
    * @description newRequest Methods to make a new request
    */
    private HttpRequest newRequest(Method method, String endPoint)
    {
        return newRequest(method, endPoint, NULL);
    }
    
    /**
    * @name newRequest
    * @description newRequest Methods to make a new request
    */
    private HttpRequest newRequest(Method method, String endPoint, String requestBody) 
    {
        HttpRequest request = new HttpRequest();
        request.setMethod(Method.name());
        setHeader(request);
        request.setEndpoint(endPoint);
        if (String.isNotBlank(requestBody)) 
        {
            request.setBody(requestBody);
        }   
        request.setTimeout(120000);
        return request;
    }
    
    /**
    * @name send
    * @description send Methods to send a request
    */
    private void send(HttpRequest request) 
    {
        try 
        {
            Http http = new Http();
            httpResponse = http.send(request);
        }
        catch(System.CalloutException e) 
        {
            system.debug('callout exception happened' + e.getMessage());
        }
        catch(Exception e) 
        {
            system.debug('callout did not happen' + e.getMessage());
        }
    }
    
    /**
    * @name getResponse
    * @description getResponse Method to get the Response
    */
    public HttpResponse getResponse()
    {
        return httpResponse;
    }
    
    /**
    * @name getResponseToString
    * @description getResponse Method to get the Responses
    */
    public String getResponseToString()
    {
        return getResponse().toString();
    }
}
```

                

                
- 
                    

Parse the `JsonSuccessParser` response
                        object by using the `AvalaraJSONBuilder`
                        class to build the response for your adapter.

                    

This example shows the `JsonSuccessParser`
                        class.

                    

```
global with sharing class JsonSuccessParser
{
  public static void consumeObject(JSONParser parser)
  {
    Integer depth = 0;
    do {
      JSONToken curr = parser.getCurrentToken();
      if (curr == JSONToken.START_OBJECT ||
        curr == JSONToken.START_ARRAY) {
        depth++;
      } else if (curr == JSONToken.END_OBJECT ||
        curr == JSONToken.END_ARRAY) {
        depth--;
      }
    } while (depth > 0 && parser.nextToken() != null);
  }

    public class Addresses {
        public String id {get;set;}
        public String transactionId {get;set;}
        public String boundaryLevel {get;set;}
        public String line1 {get;set;}
        public String city {get;set;}
        public String region {get;set;}
        public String postalCode {get;set;}
        public String country {get;set;}
        public Integer taxRegionId {get;set;}

        public Addresses(JSONParser parser) {
            while (parser.nextToken() != JSONToken.END_OBJECT) {
                if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                    String text = parser.getText();
                    if (parser.nextToken() != JSONToken.VALUE_NULL) {
                        if (text == 'id') {
                            id = parser.getText();
                        } else if (text == 'transactionId') {
                            transactionId = parser.getText();
                        } else if (text == 'boundaryLevel') {
                            boundaryLevel = parser.getText();
                        } else if (text == 'line1') {
                            line1 = parser.getText();
                        } else if (text == 'city') {
                            city = parser.getText();
                        } else if (text == 'region') {
                            region = parser.getText();
                        } else if (text == 'postalCode') {
                            postalCode = parser.getText();
                        } else if (text == 'country') {
                            country = parser.getText();
                        } else if (text == 'taxRegionId') {
                            taxRegionId = parser.getIntegerValue();
                        } else {
                            consumeObject(parser);
                        }
                    }
                }
            }
        }
    }

    public class Details {
        public String id {get;set;}
        public String transactionLineId {get;set;}
        public String transactionId {get;set;}
        public String country {get;set;}
        public String region {get;set;}
        public Integer exemptAmount {get;set;}
        public String jurisCode {get;set;}
        public String jurisName {get;set;}
        public String stateAssignedNo {get;set;}
        public String jurisType {get;set;}
        public Integer nonTaxableAmount {get;set;}
        public Double rate {get;set;}
        public Double tax {get;set;}
        public Integer taxableAmount {get;set;}
        public String taxType {get;set;}
        public String taxName {get;set;}
        public Integer taxAuthorityTypeId {get;set;}
        public Double taxCalculated {get;set;}
        public String rateType {get;set;}

        public Details(JSONParser parser) {
            while (parser.nextToken() != JSONToken.END_OBJECT) {
                if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                    String text = parser.getText();
                    if (parser.nextToken() != JSONToken.VALUE_NULL) {
                        if (text == 'id') {
                            id = parser.getText();
                        } else if (text == 'transactionLineId') {
                            transactionLineId = parser.getText();
                        } else if (text == 'transactionId') {
                            transactionId = parser.getText();
                        } else if (text == 'country') {
                            country = parser.getText();
                        } else if (text == 'region') {
                            region = parser.getText();
                        } else if (text == 'exemptAmount') {
                            exemptAmount = parser.getIntegerValue();
                        } else if (text == 'jurisCode') {
                            jurisCode = parser.getText();
                        } else if (text == 'jurisName') {
                            jurisName = parser.getText();
                        } else if (text == 'stateAssignedNo') {
                            stateAssignedNo = parser.getText();
                        } else if (text == 'jurisType') {
                            jurisType = parser.getText();
                        } else if (text == 'nonTaxableAmount') {
                            nonTaxableAmount = parser.getIntegerValue();
                        } else if (text == 'rate') {
                            rate = parser.getDoubleValue();
                        } else if (text == 'tax') {
                            tax = parser.getDoubleValue();
                        } else if (text == 'taxableAmount') {
                            taxableAmount = parser.getIntegerValue();
                        } else if (text == 'taxType') {
                            taxType = parser.getText();
                        } else if (text == 'taxName') {
                            taxName = parser.getText();
                        } else if (text == 'taxAuthorityTypeId') {
                            taxAuthorityTypeId = parser.getIntegerValue();
                        } else if (text == 'taxCalculated') {
                            taxCalculated = parser.getDoubleValue();
                        } else if (text == 'rateType') {
                            rateType = parser.getText();
                        } else {
                            consumeObject(parser);
                        }
                    }
                }
            }
        }
    }

    public class Messages {
        public String summary {get;set;}
        public String details {get;set;}
        public String refersTo {get;set;}
        public String severity {get;set;}
        public String source {get;set;}

        public Messages(JSONParser parser) {
            while (parser.nextToken() != JSONToken.END_OBJECT) {
                if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                    String text = parser.getText();
                    if (parser.nextToken() != JSONToken.VALUE_NULL) {
                        if (text == 'summary') {
                            summary = parser.getText();
                        } else if (text == 'details') {
                            details = parser.getText();
                        } else if (text == 'refersTo') {
                            refersTo = parser.getText();
                        } else if (text == 'severity') {
                            severity = parser.getText();
                        } else if (text == 'source') {
                            source = parser.getText();
                        } else {
                            consumeObject(parser);
                        }
                    }
                }
            }
        }
    }

    public String id {get;set;}
    public String code {get;set;}
    public String referenceCode {get;set;}
    public Integer companyId {get;set;}
    public String taxDate {get;set;}
    public String transactionDate {get;set;}
    public String status {get;set;}
    public String type_Z {get;set;} // in json: type
    public Boolean reconciled {get;set;}
    public Integer totalAmount {get;set;}
    public Integer totalExempt {get;set;}
    public Double totalTax {get;set;}
    public Integer totalTaxable {get;set;}
    public Double totalTaxCalculated {get;set;}
    public String adjustmentReason {get;set;}
    public Boolean locked {get;set;}
    public Integer version {get;set;}
    public String modifiedDate {get;set;}
    public Integer modifiedUserId {get;set;}
    public List<Lines> lines {get;set;}
    public List<Addresses> addresses {get;set;}
    public List<Summary> summary {get;set;}
    public List<Messages> messages {get;set;}

    public JsonSuccessParser(JSONParser parser) {
        while (parser.nextToken() != JSONToken.END_OBJECT) {
            if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                String text = parser.getText();
                if (parser.nextToken() != JSONToken.VALUE_NULL) {
                    if (text == 'id') {
                        id = parser.getText();
                    } else if (text == 'code') {
                        code = parser.getText();
                    } else if (text == 'referenceCode'){
                        referenceCode = parser.getText();
                    } else if (text == 'companyId') {
                        companyId = parser.getIntegerValue();
                    } else if (text == 'taxDate') {
                        taxDate = parser.getText();
                    } else if (text == 'date') {
                        transactionDate = parser.getText();
                    } else if (text == 'status') {
                        status = parser.getText();
                    } else if (text == 'type') {
                        type_Z = parser.getText();
                    } else if (text == 'reconciled') {
                        reconciled = parser.getBooleanValue();
                    } else if (text == 'totalAmount') {
                        totalAmount = parser.getIntegerValue();
                    } else if (text == 'totalExempt') {
                        totalExempt = parser.getIntegerValue();
                    } else if (text == 'totalTax') {
                        totalTax = parser.getDoubleValue();
                    } else if (text == 'totalTaxable') {
                        totalTaxable = parser.getIntegerValue();
                    } else if (text == 'totalTaxCalculated') {
                        totalTaxCalculated = parser.getDoubleValue();
                    } else if (text == 'adjustmentReason') {
                        adjustmentReason = parser.getText();
                    } else if (text == 'locked') {
                        locked = parser.getBooleanValue();
                    } else if (text == 'version') {
                        version = parser.getIntegerValue();
                    } else if (text == 'modifiedDate') {
                        modifiedDate = parser.getText();
                    } else if (text == 'modifiedUserId') {
                        modifiedUserId = parser.getIntegerValue();
                    } else if (text == 'lines') {
                        lines = new List<Lines>();
                        while (parser.nextToken() != JSONToken.END_ARRAY) {
                            lines.add(new Lines(parser));
                        }
                    } else if (text == 'addresses') {
                        addresses = new List<Addresses>();
                        while (parser.nextToken() != JSONToken.END_ARRAY) {
                            addresses.add(new Addresses(parser));
                        }
                    } else if (text == 'summary') {
                        summary = new List<Summary>();
                        while (parser.nextToken() != JSONToken.END_ARRAY) {
                            summary.add(new Summary(parser));
                        }
                    } else if (text == 'messages') {
                        messages = new List<Messages>();
                        while (parser.nextToken() != JSONToken.END_ARRAY) {
                            messages.add(new Messages(parser));
                        }
                    } else {
                        consumeObject(parser);
                    }
                }
            }
        }
    }

    public class Summary {
        public String country {get;set;}
        public String region {get;set;}
        public String jurisType {get;set;}
        public String jurisCode {get;set;}
        public String jurisName {get;set;}
        public Integer taxAuthorityType {get;set;}
        public String stateAssignedNo {get;set;}
        public String taxType {get;set;}
        public String taxName {get;set;}
        public String taxGroup {get;set;}
        public String rateType {get;set;}
        public Integer taxable {get;set;}
        public Double rate {get;set;}
        public Double tax {get;set;}
        public Double taxCalculated {get;set;}
        public Integer nonTaxable {get;set;}
        public Integer exemption {get;set;}

        public Summary(JSONParser parser) {
            while (parser.nextToken() != JSONToken.END_OBJECT) {
                if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                    String text = parser.getText();
                    if (parser.nextToken() != JSONToken.VALUE_NULL) {
                        if (text == 'country') {
                            country = parser.getText();
                        } else if (text == 'region') {
                            region = parser.getText();
                        } else if (text == 'jurisType') {
                            jurisType = parser.getText();
                        } else if (text == 'jurisCode') {
                            jurisCode = parser.getText();
                        } else if (text == 'jurisName') {
                            jurisName = parser.getText();
                        } else if (text == 'taxAuthorityType') {
                            taxAuthorityType = parser.getIntegerValue();
                        } else if (text == 'stateAssignedNo') {
                            stateAssignedNo = parser.getText();
                        } else if (text == 'taxType') {
                            taxType = parser.getText();
                        } else if (text == 'taxName') {
                            taxName = parser.getText();
                        } else if (text == 'taxGroup') {
                            taxGroup = parser.getText();
                        } else if (text == 'rateType') {
                            rateType = parser.getText();
                        } else if (text == 'taxable') {
                            taxable = parser.getIntegerValue();
                        } else if (text == 'rate') {
                            rate = parser.getDoubleValue();
                        } else if (text == 'tax') {
                            tax = parser.getDoubleValue();
                        } else if (text == 'taxCalculated') {
                            taxCalculated = parser.getDoubleValue();
                        } else if (text == 'nonTaxable') {
                            nonTaxable = parser.getIntegerValue();
                        } else if (text == 'exemption') {
                            exemption = parser.getIntegerValue();
                        } else {
                            consumeObject(parser);
                        }
                    }
                }
            }
        }
    }

    public class Lines {
        public String id {get;set;}
        public String transactionId {get;set;}
        public String lineNumber {get;set;}
        public Integer discountAmount {get;set;}
        public Integer exemptAmount {get;set;}
        public Integer exemptCertId {get;set;}
        public Boolean isItemTaxable {get;set;}
        public Integer lineAmount {get;set;}
        public Double quantity {get;set;}
        public String reportingDate {get;set;}
        public Double tax {get;set;}
        public Integer taxableAmount {get;set;}
        public Double taxCalculated {get;set;}
        public String taxCode {get;set;}
        public String taxDate {get;set;}
        public Boolean taxIncluded {get;set;}
        public List<Details> details {get;set;}
        public String itemCode {get;set;}
        public Lines(JSONParser parser) {
            while (parser.nextToken() != JSONToken.END_OBJECT) {
                if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {
                    String text = parser.getText();
                    if (parser.nextToken() != JSONToken.VALUE_NULL) {
                        if (text == 'id') {
                            id = parser.getText();
                        } else if (text == 'transactionId') {
                            transactionId = parser.getText();
                        }else if (text == 'itemCode') {
                            itemCode = parser.getText();
                        }else if (text == 'lineNumber') {
                            lineNumber = parser.getText();
                        } else if (text == 'discountAmount') {
                            discountAmount = parser.getIntegerValue();
                        } else if (text == 'exemptAmount') {
                            exemptAmount = parser.getIntegerValue();
                        } else if (text == 'exemptCertId') {
                            exemptCertId = parser.getIntegerValue();
                        } else if (text == 'isItemTaxable') {
                            isItemTaxable = parser.getBooleanValue();
                        } else if (text == 'lineAmount') {
                            lineAmount = parser.getIntegerValue();
                        } else if (text == 'quantity') {
                            quantity = parser.getDoubleValue();
                        } else if (text == 'reportingDate') {
                            reportingDate = parser.getText();
                        } else if (text == 'tax') {
                            tax = parser.getDoubleValue();
                        } else if (text == 'taxableAmount') {
                            taxableAmount = parser.getIntegerValue();
                        } else if (text == 'taxCalculated') {
                            taxCalculated = parser.getDoubleValue();
                        } else if (text == 'taxCode') {
                            taxCode = parser.getText();
                        } else if (text == 'taxDate') {
                            taxDate = parser.getText();
                        } else if (text == 'taxIncluded') {
                            taxIncluded = parser.getBooleanValue();
                        } else if (text == 'details') {
                            details = new List<Details>();
                            while (parser.nextToken() != JSONToken.END_ARRAY) {
                                details.add(new Details(parser));
                            }
                        } else {
                            consumeObject(parser);
                        }
                    }
                }
            }
        }
    }

    public static JsonSuccessParser parse(String json)
    {
        return new JsonSuccessParser(System.JSON.createParser(json));
    }
}

```

                    

Prepare your JSON request to call the Avalara endpoint by using the `AvalaraJSONBuilder` class.

                    

```
public with sharing class AvalaraJSONBuilder 
{
    private static AvalaraJSONBuilder avalaraJSONBuilderInstance;
    
    public static AvalaraJSONBuilder getInstance() 
    {
        if (NULL == avalaraJSONBuilderInstance) 
        {
            avalaraJSONBuilderInstance = new AvalaraJSONBuilder();
        }
        return avalaraJSONBuilderInstance;
    }
    
    public String frameJsonForGetTaxOrderItem(commercetax.CalculateTaxRequest calculateTaxRequest) 
    {
        try
        {
            Id accountid  = null;
            if(calculateTaxRequest.CustomerDetails.AccountId != null &&  calculateTaxRequest.CustomerDetails.AccountId != '')
               accountid = Id.valueof(calculateTaxRequest.CustomerDetails.AccountId);
            JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);
            jsonGeneratorInstance.writeStartObject();
            String type = null;
            if(calculateTaxRequest.taxtype == commercetax.CalculateTaxType.Actual)
                type ='SalesInvoice';
                else type = 'SalesOrder';
            jsonGeneratorInstance.writeStringField('type', type);
            if(calculateTaxRequest.SellerDetails != null)
                jsonGeneratorInstance.writeStringField('companyCode', calculateTaxRequest.SellerDetails.code);
            else 
                jsonGeneratorInstance.writeStringField('companyCode', 'billing2');
            if(calculateTaxRequest.isCommit != null) {
                jsonGeneratorInstance.writeBooleanField('commit', calculateTaxRequest.isCommit);
            }
            if(calculateTaxRequest.documentcode != null){
                jsonGeneratorInstance.writeStringField('code', calculateTaxRequest.documentcode);
            }else if(calculateTaxRequest.referenceEntityId != null) {
                jsonGeneratorInstance.writeStringField('code', calculateTaxRequest.referenceEntityId);
            }
            if(calculateTaxRequest.CustomerDetails.code == null && accountid !=null) {
                Account acc = [select id, name from account where id=:accountid];
                jsonGeneratorInstance.writeStringField('customerCode', acc.name);
            } else {
                jsonGeneratorInstance.writeStringField('customerCode', calculateTaxRequest.CustomerDetails.code);
            }
            if(calculateTaxRequest.EffectiveDate == null)
                jsonGeneratorInstance.writeDateField('date', system.today());
            else         
                jsonGeneratorInstance.writeDateTimeField('date', calculateTaxRequest.EffectiveDate);
            
            jsonGeneratorInstance.writeFieldName('lines');
            jsonGeneratorInstance.writeStartArray();
            for(integer i=0;i<1;i++){
                for(Commercetax.TaxLineItemRequest lineItem : calculateTaxRequest.LineItems)
                {
                    jsonGeneratorInstance.writeStartObject();
                    if(lineItem.linenumber != null){
                        jsonGeneratorInstance.writeStringField('number', lineItem.linenumber);
                    }
                    jsonGeneratorInstance.writeNumberField('quantity', lineItem.Quantity);
                    jsonGeneratorInstance.writeNumberField('amount', (lineItem.Amount));
                    jsonGeneratorInstance.writeStringField('taxCode',lineItem.taxCode);
                    
                    jsonGeneratorInstance.writeFieldName('addresses');
                    jsonGeneratorInstance.writeStartObject();  
                    jsonGeneratorInstance.writeFieldName('ShipFrom');
                    jsonGeneratorInstance.writeStartObject();
                    jsonGeneratorInstance.writeStringField('line1', lineItem.addresses.shipfrom.street);
                    jsonGeneratorInstance.writeStringField('line2', lineItem.addresses.shipfrom.street);
                    jsonGeneratorInstance.writeStringField('city', lineItem.addresses.shipfrom.city);
                    jsonGeneratorInstance.writeStringField('region', lineItem.addresses.shipfrom.state);
                    jsonGeneratorInstance.writeStringField('country', lineItem.addresses.shipfrom.country);
                    jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.shipfrom.postalcode);              
                    jsonGeneratorInstance.writeEndObject();               

                    jsonGeneratorInstance.writeFieldName('ShipTo');
                    jsonGeneratorInstance.writeStartObject();
                    jsonGeneratorInstance.writeStringField('line1', lineItem.addresses.shipto.street);
                    jsonGeneratorInstance.writeStringField('line2', lineItem.addresses.shipto.street);
                    jsonGeneratorInstance.writeStringField('city', lineItem.addresses.shipto.city);
                    jsonGeneratorInstance.writeStringField('region', lineItem.addresses.shipto.state);
                    jsonGeneratorInstance.writeStringField('country', lineItem.addresses.shipto.country);
                    jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.shipto.postalcode); 
                    jsonGeneratorInstance.writeEndObject();               

                    jsonGeneratorInstance.writeFieldName('pointOfOrderOrigin');
                    jsonGeneratorInstance.writeStartObject();
                    jsonGeneratorInstance.writeStringField('line1', lineItem.addresses.soldto.street);
                    jsonGeneratorInstance.writeStringField('line2', lineItem.addresses.soldto.street);
                    jsonGeneratorInstance.writeStringField('city', lineItem.addresses.soldto.city);
                    jsonGeneratorInstance.writeStringField('region', lineItem.addresses.soldto.state);
                    jsonGeneratorInstance.writeStringField('country', lineItem.addresses.soldto.country);
                    jsonGeneratorInstance.writeStringField('postalCode',lineItem.addresses.soldto.postalcode); 
                    jsonGeneratorInstance.writeEndObject(); 

                    if(lineItem.effectiveDate != null)    
                    {
                        jsonGeneratorInstance.writeFieldName('taxOverride');
                        jsonGeneratorInstance.writeStartObject();
                        jsonGeneratorInstance.writeDateTimeField('taxDate', lineItem.effectiveDate);             
                        jsonGeneratorInstance.writeEndObject();               
                    }
                    jsonGeneratorInstance.writeEndObject(); 
                    jsonGeneratorInstance.writeEndObject(); 
                }
            }
                jsonGeneratorInstance.writeEndArray();             
            jsonGeneratorInstance.writeEndObject();
            return jsonGeneratorInstance.getAsString();
        }
        catch (Exception e) 
        { 
             throw e;
        } 
    }
}
```

                

                
- 
                    

Use the `JsonErrorParser` class to extract
                        the error details, if any.

                    

```
global with sharing class JsonErrorParser
{
    public cls_error error;
    
    public class cls_error
    {
        public String code; 
        public String message;
        public String target;
        public cls_details[] details;
    }
    
    public class cls_details
    {
        public String code;
        public String message;
        public String description;
        public String faultCode;
        public String helpLink;
        public String severity;
    }
    public static JsonErrorParser parse(String json)
    {
        return (JsonErrorParser) System.JSON.deserialize(json, JsonErrorParser.class);
    }
}
```

                

            

        

    

  

## Tax Mappings for Quotes and Orders

  
  
  
You can extend and customize the tax interface for quotes and orders by using custom
    metadata types and tax mappings. These customizations help you with unique business requirements
    such as the inclusion of specific data for accurate calculations and audits.

    

Tax callout extensions are supported for the Quote, QuoteLineItem, Order, and OrderItem objects
        to include additional fields to tax requests. See [custom metadata types](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_overview.htm&language=en_US) to specify all your tax
        mapping definitions.

    

### Request Mappings for Header Attributes

      
      

This table defines the request mappings between the header attributes of a tax callout and
        fields of applicable quote and order objects.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Header Attributes | Quote Mapping | Order Mapping |
| --- | --- | --- |
| currencyIsoCode | If multi-currency is enabled, then this value is `Quote.CurrencyISOCode`. Otherwise, this value is NULL. | If multi-currency is enabled, then this value is `Order.CurrencyISOCode`. Otherwise, this value is NULL. |
| isCommit | `False` | `False` |
| referenceEntityId | Quote.ID | Order.ID |
| taxEngineId | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID |
| transactionDate | Current System Date | System Date |
| **sellerDetails** | NULL |  |
| code |  | TaxEngine.SellerCode |
| **customerDetails** |  |  |
| accountId | Quote.AccountId | Order.AccountId |
| code | NULL | NULL |
| exemptionNo | NULL | NULL |
| exemptionReason | NULL | NULL |
| taxType | `Estimated` | `Estimated` |
| taxTransactionType | NULL | NULL |
| effectiveDate | NULL | NULL |
| **addresses** |  |  |
| billTo | NULL | NULL |
| shipTo | NULL | NULL |
| shipFrom | NULL | NULL |
| soldTo | NULL | NULL |
| taxEngineAddress | TaxEngine.Address | TaxEngine.Address |
| referenceDocumentCode | NULL | NULL |
| description | NULL | NULL |
| documentCode | `Quote.ID-TaxEngineId` | `Order.ID-TaxEngineId` |
| shouldVoid | `FALSE` | `FALSE` |
| lineItems | Refer to the next line attributes section. | Refer to the next line attributes section. |

    

    

### Request Mappings for Line Attributes

      
      

This table defines the request mappings between the line attributes of a tax callout and
        fields of applicable quote line items and order products.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Line Attributes | Quote Line Item Mapping | Order Product Mapping |
| --- | --- | --- |
| taxCode | TaxTreatment.TaxCode | TaxTreatment.TaxCode |
| productCode | TaxTreatment.ProductCode | TaxTreatment.ProductCode |
| productId | QuoteLineItem.Product2.Id | OrderItem.Product2.Id |
| amount | QuoteLineItem.TotalPrice | OrderItem.TotalPrice |
| effectiveDate | Current System Date | Current System Date |
| lineNumber | QuoteLineItem.Id | OrderItem.Id |
| description | NULL | NULL |
| quantity | QuoteLineItem.Quantity | OrderItem.Quantity |
| **addresses** |  |  |
| billTo | Quote.BillingAddress. If Quote.BillingAddress is null, then this value is Quote.Account.BillingAddress. | Order.BillingAddress |
| shipTo | Quote.ShippingAddress. If Quote.ShippingAddress is null, then this value is Quote.Account.ShippingAddress. | Order.ShippingAddress |
| shipFrom | NULL | NULL |
| soldTo | NULL | NULL |
| productsku | QuoteLineItem.Product2.ProductCode | OrderItem.Product2.ProductCode |
| referenceDocumentCode | NULL | NULL |

    

    

### Response Mappings for Header Attributes

      
      

This table defines the response mappings between the header attributes of a tax callout and
        fields of applicable objects. Most response data is used for tax calculation and isn’t
        persisted on quote or order records.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Header Attributes | Quote Mapping | Order Mapping |
| --- | --- | --- |
| currencyIsoCode | Quote.CurrencyISOCode | Order.CurrencyISOCode |
| isCommit | Not returned. | Not returned. |
| referenceEntityId | Quote.ID | Order.ID |
| taxEngineId | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID |
| transactionDate | System Date | System Date |
| **sellerDetails** | Not returned. | Not returned. |
| code | Not returned. | Not returned. |
| **customerDetails** | Not returned. | Not returned. |
| accountId | Not returned. | Not returned. |
| code | Not returned. | Not returned. |
| exemptionNo | Not returned. | Not returned. |
| exemptionReason | Not returned. | Not returned. |
| taxType | `Estimated` | `Estimated` |
| taxTransactionType | Not returned. | Not returned. |
| effectiveDate | System Date | System Date |
| **addresses** |  |  |
| billTo | Not returned. | Not returned. |
| shipTo | locationCode -> locationCode | locationCode -> locationCode |
| shipFrom | Not returned. | Not returned. |
| soldTo | Not returned. | Not returned. |
| taxEngineAddress | Not returned. | Not returned. |
| referenceDocumentCode | Not returned. | Not returned. |
| description | Not returned. | Not returned. |
| documentCode | `Quote.ID-TaxEngineId` | `Order.ID-TaxEngineId` |
| status | `Uncommitted` | `Uncommitted` |
| taxEngineLogs | Not returned. | Not returned. |
| resultCode | Not returned. | Not returned. |
| transactionDate | System Date | System Date |
| **amountDetails** |  |  |
| exemptAmount | Actual exemptAmount from response. | Actual exemptAmount from response. |
| taxAmount | Actual taxAmount from response. | Actual taxAmount from response. |
| totalAmount | Quote.Subtotal | Order.Subtotal |
| totalAmountWithTax | TaxAmount + TotalAmount | TaxAmount + TotalAmount |
| lineItems | Refer to the next line attributes section. | Refer to the next line attributes section. |

    

    

### Response Mappings for Line Attributes

      
      

This table defines the response mappings between the line attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Line Attributes | Quote Line Item Mapping | Order Product Mapping |
| --- | --- | --- |
| taxCode | TaxTreatment.TaxCode | TaxTreatment.TaxCode |
| productCode | TaxTreatment.ProductCode | TaxTreatment.ProductCode |
| productId | Not returned. | Not returned. |
| **amountDetails** |  |  |
| exemptAmount | Actual exemptAmount from response | Actual exemptAmount from response |
| taxAmount | Actual taxAmount from response | Actual taxAmount from response |
| totalAmount | QuoteLineItem.Subtotal | OrderItem.Subtotal |
| totalAmountWithTax | TaxAmount + TotalAmount | TaxAmount + TotalAmount |
| effectiveDate | System Date | System Date |
| lineNumber | QuoteLineItem.Id | OrderItem.Id |
| description | Not returned. | Not returned. |
| quantity | Not returned. | Not returned. |
| **addresses** |  |  |
| billTo | Not persisted. | Not persisted. |
| shipTo | locationCode -> locationCode | locationCode -> locationCode |
| shipFrom | Not returned. | Not returned. |
| soldTo | Not returned. | Not returned. |
| productsku | Not returned. | Not returned. |
| referenceDocumentCode | Not returned. | Not returned. |
| taxes | Refer to the next tax attributes section. | Refer to the next tax attributes section. |

    

    

### Response Mappings for Tax Attributes

      
      

This table defines the response mappings between the tax attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Tax Attributes | Quote Mapping | Order Mapping |
| --- | --- | --- |
| exemptAmount | Not returned. | Not returned. |
| exemptReason | Not returned. | Not returned. |
| **imposition** |  |  |
| type | Not returned. | Not returned. |
| Name | Not returned. | Not returned. |
| **jurisdiction** |  |  |
| country | Not returned. | Not returned. |
| id | Not returned. | Not returned. |
| level | Not returned. | Not returned. |
| name | Not returned. | Not returned. |
| region | Not returned. | Not returned. |
| stateAssignedNo | Not returned. | Not returned. |
| rate | QuoteItemTaxItem.Rate | OrderItemTaxItem.Rate |
| tax | QuoteItemTaxItem.amount | OrderItemTaxItem.amount |
| taxId | Not returned. | Not returned. |
| taxableAmount | Not returned. | Not returned. |

=== ARTICLE: apex_namespace_RevSalesTrxn.htm ===
---
page_id: apex_namespace_RevSalesTrxn.htm
title: RevSalesTrxn Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_RevSalesTrxn.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RevSalesTrxn Namespace

Create a sales transaction, such as a quote or an order, with integrated
      pricing and configuration. Additionally, update an order or a quote, and insert and delete
      order or quote line items to calculate the estimated tax.

The `RevSalesTrxn` namespace includes these classes.

- 
**[CatalogRatesPreferenceEnum Enum](./apex_enum_RevSalesTrxn_CatalogRatesPreferenceEnum.htm.md)**  

Specifies the rate card entries defined in the catalog that must be fetched for quote     line items, with usage-based selling during the place sales transaction process.

- 
**[ConfigurationExecutionEnum Enum](./apex_enum_RevSalesTrxn_ConfigurationExecutionEnum.htm.md)**  

Specifies the configuration method for the place sales transaction request.

- 
**[ConfigurationOptionsInput Class](./apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm.md#apex_class_RevSalesTrxn_ConfigurationOptionsInput)**  

Contains methods and properties to set the configuration options for the input to the     product configurator.

- 
**[GraphRequest Class](./apex_class_RevSalesTrxn_GraphRequest.htm.md#apex_class_RevSalesTrxn_GraphRequest)**  

Contains constructors and properties to set the graph ID and a list of records to be     ingested. The list of records is specified in a key-value map format that contains field     values.

- 
**[GroupRampActionEnum Enum](./apex_enum_RevSalesTrxn_GroupRampActionEnum.htm.md)**  

Specifies the action ‌that you want to perform on group ramp segments. Additionally,     you can also convert a non-ramped group into a ramped group. 

- 
**[PersistPreferenceEnum Enum](./apex_enum_RevSalesTrxn_PersistPreferenceEnum.htm.md)**  

Specifies whether to persist pricing changes for each sales transaction record.     Available in API version 65.0 and later.

- 
**[PlaceSalesTransactionException Class](./apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionException)**  

Contains methods to hold the exception details for the place sales transaction     request.

- 
**[PlaceSalesTransactionExecutor Class](./apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor)**  

Contains methods to place a sales transaction with details of the graph request,     pricing preferences, and configuration options.

- 
**[PlaceSalesTransactionResponse Class](./apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm.md#apex_class_RevSalesTrxn_PlaceSalesTransactionResponse)**  

Contains properties to hold the response to the place sales transaction     request.

- 
**[PricingPreferenceEnum Enum](./apex_enum_RevSalesTrxn_PricingPreferenceEnum.htm.md)**  

Specifies the pricing preference during the creation of a sales transaction.

- 
**[RecordResource Class](./apex_class_RevSalesTrxn_RecordResource.htm.md#apex_class_RevSalesTrxn_RecordResource)**  

Contains constructors and properties to create a record object from the field values of a     sales transaction.

- 
**[RecordWithReferenceRequest Class](./apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm.md#apex_class_RevSalesTrxn_RecordWithReferenceRequest)**  

Contains constructors and properties to associate a record object with a reference     identifier.

- 
**[TaxPreferenceEnum Enum](./apex_enum_RevSalesTrxn_TaxPreferenceEnum.htm.md)**  

Specifies whether to execute or skip the tax calculation step for each sales     transaction record. Available in API version 65.0 and later.

=== ARTICLE: apex_namespace_commerceorders.htm ===
---
page_id: apex_namespace_commerceorders.htm
title: CommerceOrders Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_commerceorders.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CommerceOrders Namespace

The `CommerceOrders` namespace provides classes and
    methods to place orders with integrated pricing, configuration, and validation.

      

#### Note

This namespace has been deprecated as of API version 63.0. In API version 63.0 and
        later, use the new [RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)
        namespace.

The `CommerceOrders` namespace includes these classes.

- 
**[CatalogRatesPreferenceEnum Enum](./apex_enum_commerceorders_CatalogRatesPreferenceEnum.htm.md)**  

Specifies the rate card entries defined in the catalog that must be fetched for order     items, with usage-based selling during the order creation process.

- 
**[ConfigurationInputEnum Enum](./apex_enum_commerceorders_ConfigurationInputEnum.htm.md)**  

Specifies the configuration input for the request to place an order.

- 
**[ConfigurationOptionsInput Class](./apex_class_commerceorders_ConfigurationOptionsInput.htm.md#apex_class_commerceorders_ConfigurationOptionsInput)**  

Contains methods and properties to set the configuration options for the input to the         product configurator.

- 
**[GraphRequest Class](./apex_class_commerceorders_GraphRequest.htm.md#apex_class_commerceorders_GraphRequest)**  

Contains constructors and properties to set the graph ID and a list of records to be     ingested. The list of records is specified in a key-value map format that contains the field     values of an order.

- 
**[PlaceOrderExecutor Class](./apex_class_commerceorders_PlaceOrderExecutor.htm.md#apex_class_commerceorders_PlaceOrderExecutor)**  

Contains methods to place an order with details of the graph request, pricing     preferences, and configuration options.

- 
**[PlaceOrderResult Class](./apex_class_commerceorders_PlaceOrderResult.htm.md#apex_class_commerceorders_PlaceOrderResult)**  

Contains properties to hold the response to the place order request.

- 
**[PricingPreferenceEnum Enum](./apex_enum_commerceorders_PricingPreferenceEnum.htm.md)**  

Specifies the pricing preference during the create order process.

- 
**[RecordResource Class](./apex_class_commerceorders_RecordResource.htm.md#apex_class_commerceorders_RecordResource)**  

Contains constructors and properties to create a record object from field values of an     order.

- 
**[RecordWithReferenceRequest Class](./apex_class_commerceorders_RecordWithReferenceRequest.htm.md#apex_class_commerceorders_RecordWithReferenceRequest)**  

Contains constructors and properties to associate a record object with a reference     identifier.

=== ARTICLE: apex_namespace_commercetax.htm ===
---
page_id: apex_namespace_commercetax.htm
title: CommerceTax Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_commercetax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CommerceTax Namespace

Manage the communication between Salesforce and an external tax engine.

    

The `CommerceTax` namespace includes these classes.

  

- 
**[AbstractTransactionResponse Class](./apex_class_commercetax_AbstractTransactionResponse.htm.md#apex_class_commercetax_AbstractTransactionResponse)**  

Abstract class that contains methods for setting tax fields based on       the external tax provider's response. Response classes that extend `AbstractTransactionResponse` inherit these methods.

- 
**[AddressesResponse Class](./apex_class_commercetax_AddressesResponse.htm.md#apex_class_commercetax_AddressesResponse)**  

Sets the tax address fields based on a response from the external       tax engine. Contains setter methods for the Ship From, Ship To, and Sold To     addresses.

- 
**[AddressResponse Class](./apex_class_commercetax_AddressResponse.htm.md#apex_class_commercetax_AddressResponse)**  

Contains a location code sent from the external tax     engine.

- 
**[AmountDetailsResponse Class](./apex_class_commercetax_AmountDetailsResponse.htm.md#apex_class_commercetax_AmountDetailsResponse)**  

Sets tax amount fields based on a response from the external tax       engine.

- 
**[CalculateTaxRequest Class](./apex_class_commercetax_CalculateTaxRequest.htm.md#apex_class_commercetax_CalculateTaxRequest)**  

Represents a request to an external tax engine to calculate tax.       Extends the TaxTransactionRequest class and is the top-level request       class.

- 
**[CalculateTaxResponse Class](./apex_class_commercetax_CalculateTaxResponse.htm.md#apex_class_commercetax_CalculateTaxResponse)**  

Sets             the values of the tax transaction following a response from the external tax engine.             Extends the AbstractTransactionResponse class and is the top-level response         class.

- 
**[CalculateTaxType Enum](./apex_enum_commercetax_CalculateTaxType.htm.md)**  

Shows whether a tax calculation request is for estimated or actual       tax.

- 
**[CustomTaxAttributesResponse Class](./apex_class_commercetax_CustomTaxAttributesResponse.htm.md#apex_class_commercetax_CustomTaxAttributesResponse)**  

Sets additional data or custom attributes in the tax             response.

- 
**[ErrorResponse Class](./apex_class_commercetax_ErrorResponse.htm.md#apex_class_commercetax_ErrorResponse)**  

Use to respond with an error after receiving errors from the             PaymentGatewayAdapter             methods of the [CommercePayments](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)             namespace, such as request-forbidden responses, custom validation errors, or expired API             tokens.

- 
**[HeaderTaxAddressesRequest Class](./apex_class_commercetax_HeaderTaxAddressesRequest.htm.md#apex_class_commercetax_HeaderTaxAddressesRequest)**  

Captures the address values that are applicable for the quote or       order transaction.

- 
**[ImpositionResponse Class](./apex_class_commercetax_ImpositionResponse.htm.md#apex_class_commercetax_ImpositionResponse)**  

Stores details of tax impositions from the external tax     engine.

- 
**[JurisdictionResponse Class](./apex_class_commercetax_JurisdictionResponse.htm.md#apex_class_commercetax_JurisdictionResponse)**  

Stores details from the external tax engine about the tax       jurisdiction used in the tax calculation process. A tax jurisdiction represents a government       entity that collects tax.

- 
**[LineItemResponse Class](./apex_class_commercetax_LineItemResponse.htm.md#apex_class_commercetax_LineItemResponse)**  

Response class that stores details of a list of one or more line             items on which the tax engine has calculated tax.

- 
**[LineTaxAddressesRequest Class](./apex_class_commercetax_LineTaxAddressesRequest.htm.md#apex_class_commercetax_LineTaxAddressesRequest)**  

Stores details of the addresses applied per line item in a tax       calculation request.

- 
**[RequestType Enum](./apex_enum_commercetax_RequestType.htm.md)**  

Shows the type of tax request made to the tax     engine.

- 
**[ResultCode Enum](./apex_enum_commercetax_ResultCode.htm.md)**  

Code that represents the results of a tax request made to the tax       engine.

- 
**[RuleDetailsResponse Class](./apex_class_commercetax_RuleDetailsResponse.htm.md#apex_class_commercetax_RuleDetailsResponse)**  

Contains details about the tax rules used for tax     calculation.

- 
**[TaxAddressesRequest Class](./apex_class_commercetax_TaxAddressesRequest.htm.md#apex_class_commercetax_TaxAddressesRequest)**  

Contains methods to get and set tax address values.

- 
**[TaxAddressRequest Class](./apex_class_commercetax_TaxAddressRequest.htm.md#apex_class_commercetax_TaxAddressRequest)**  

Contains address details used for tax calculation.

- 
**[TaxApiException Class](./apex_class_commercetax_TaxApiException.htm.md#apex_class_commercetax_TaxApiException)**  

Contains details about any exceptions during the tax calculation       process. Extends the `ApexBaseException`     class.

- 
**[TaxCustomerDetailsRequest Class](./apex_class_commercetax_TaxCustomerDetailsRequest.htm.md#apex_class_commercetax_TaxCustomerDetailsRequest)**  

Contains customer details used in tax calculation.

- 
**[TaxDetailsResponse Class](./apex_class_commercetax_TaxDetailsResponse.htm.md#apex_class_commercetax_TaxDetailsResponse)**  

Stores details of the tax values that an external tax engine             calculates in response to a tax calculation request.

- 
**[TaxEngineAdapter Interface](./apex_interface_commercetax_TaxEngineAdapter.htm.md#apex_interface_commercetax_TaxEngineAdapter)**  

Retrieves information from the tax engine and evaluates the information to define tax     details.

- 
**[TaxEngineContext Class](./apex_class_commercetax_TaxEngineContext.htm.md#apex_class_commercetax_TaxEngineContext)**  

Wrapper class that stores details about the type of a tax             calculation request.

- 
**[TaxLineItemRequest Class](./apex_class_commercetax_TaxLineItemRequest.htm.md#apex_class_commercetax_TaxLineItemRequest)**  

Contains line item details of a tax request.

- 
**[TaxSellerDetailsRequest Class](./apex_class_commercetax_TaxSellerDetailsRequest.htm.md#apex_class_commercetax_TaxSellerDetailsRequest)**  

Contains tax code details used in the tax calculation       request.

- 
**[TaxTransactionRequest Class](./apex_class_commercetax_TaxTransactionRequest.htm.md#apex_class_commercetax_TaxTransactionRequest)**  

Abstract class for storing customer details used in tax calculation       and estimation requests.

- 
**[TaxTransactionStatus Enum](./apex_enum_commercetax_TaxTransactionStatus.htm.md)**  

Shows whether the tax transaction has been committed or       uncommitted.

- 
**[TaxTransactionType Enum](./apex_enum_commercetax_TaxTransactionType.htm.md)**  

Shows whether the tax transaction is for a credit or debit       transaction.

=== ARTICLE: apex_namespace_placequote.htm ===
---
page_id: apex_namespace_placequote.htm
title: PlaceQuote Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_placequote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceQuote Namespace

The `PlaceQuote` namespace provides classes and methods
    to create or update quotes with pricing preferences and configuration options.

      

#### Note

This namespace has been deprecated as of API version 63.0. In API version 63.0 and
        later, use the new [RevSalesTrxn](./apex_namespace_RevSalesTrxn.htm.md)
        namespace.

The `PlaceQuote` namespace includes these classes.

- 
**[CatalogRatesPreferenceEnum Enum](./apex_enum_placequote_CatalogRatesPreferenceEnum.htm.md)**  

Specifies the rate card entries defined in the catalog that must be fetched for quote     line items, with usage-based selling during the quote creation process.

- 
**[ConfigurationInputEnum Enum](./apex_enum_placequote_ConfigurationInputEnum.htm.md)**  

Specifies the configuration input for the request to place a quote.

- 
**[ConfigurationOptionsInput Class](./apex_class_placequote_ConfigurationOptionsInput.htm.md#apex_class_placequote_ConfigurationOptionsInput)**  

Contains methods and properties to set the configuration options for the input to the     product configurator.

- 
**[GraphRequest Class](./apex_class_placequote_GraphRequest.htm.md#apex_class_placequote_GraphRequest)**  

Contains constructors and properties to set the graph ID and a list of records to be     ingested. The list of records is specified in a key-value map format that contains the field     values of an order.

- 
**[PlaceQuoteException Class](./apex_class_placequote_PlaceQuoteException.htm.md#apex_class_placequote_PlaceQuoteException)**  

Contains methods to hold the exception details for the place quote request.

- 
**[PlaceQuoteResponse Class](./apex_class_placequote_PlaceQuoteResponse.htm.md#apex_class_placequote_PlaceQuoteResponse)**  

Contains properties to hold the response to the place quote request.

- 
**[PlaceQuoteRLMApexProcessor Class](./apex_class_placequote_PlaceQuoteRLMApexProcessor.htm.md#apex_class_placequote_PlaceQuoteRLMApexProcessor)**  

Contains methods to place a quote with details of the graph request, pricing preferences,     and configuration options.

- 
**[PricingPreferenceEnum Enum](./apex_enum_placequote_PricingPreferenceEnum.htm.md)**  

Specifies the pricing preference during the create quote process.

- 
**[RecordResource Class](./apex_class_placequote_RecordResource.htm.md#apex_class_placequote_RecordResource)**  

Contains constructors and properties to create a record object from the field values of a     quote.

- 
**[RecordWithReferenceRequest Class](./apex_class_placequote_RecordWithReferenceRequest.htm.md#apex_class_placequote_RecordWithReferenceRequest)**  

Contains constructors and properties to associate a record object with a reference     identifier.

=== ARTICLE: apex_namespace_renew_assets_summary.htm ===
---
page_id: apex_namespace_renew_assets_summary.htm
title: renew_assets_summary Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_renew_assets_summary.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# renew_assets_summary Namespace

Retrieve details about renewable assets to create renewal opportunities.

The `renew_assets_summary` namespace includes these classes.

    

- 
**[RenewalOpptyDetail Class](./apex_class_renew_assets_summary_RenewalOpptyDetail.htm.md#apex_class_renew_assets_summary_RenewalOpptyDetail)**  

Contains asset details and renewal pricing information for creating renewal opportunities.

- 
**[RenewalPriceDetail Class](./apex_class_renew_assets_summary_RenewalPriceDetail.htm.md#apex_class_renew_assets_summary_RenewalPriceDetail)**  

Contains net unit price and quantity details for an asset to set as sales price for renewal opportunities.

=== ARTICLE: connect_requests_amend_input.htm ===
---
page_id: connect_requests_amend_input.htm
title: Amendment Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_amend_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Amendment Input

Input representation of the details of the request to create an amendment
    record.

          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "amendmentStartDate": "2023-10-04T00:00:00",
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote",
  "quantityChange": 5
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to add to the amendment record. | Required | 62.0 |
| `amendmentStart​Date` | String | Start date of the amendment. | Required | 62.0 |
| `contract​Id` | String | ID of the Contract record that you want to sync with the amendment quote. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the amendment quote. | Optional | 62.0 |
| `outputRecord​Id` | String | ID of the quote or order record that you want to add the assets to. | Optional | 62.0 |
| `output​RecordType` | String | Type of amendment record that you want to create. For usage products, set this value to `Quote`. The usage-related records (`QuoteLineItemUseResourceGrant`, `QuoteLineItemUsageResourcePolicy`, and `QuoteLineRateCardEntry`) are copied in the quote action flow, not in the amend order flow. | Required | 62.0 |
| `quantity​Change` | Double | Quantity to add to or reduce from the asset's existing quantity. | Required | 62.0 |

=== ARTICLE: connect_requests_cancel_input.htm ===
---
page_id: connect_requests_cancel_input.htm
title: Cancellation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_cancel_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Cancellation Input

Input representation of the details of the request to cancel a quote or an
    order.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "cancellationDate": "2023-10-04T00:00:00",
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to cancel. All assets in a request must belong to the same price book. | Required | 62.0 |
| `cancellation​Date` | String | Effective date of the cancellation. | Required | 62.0 |
| `contract​Id` | String | ID of the Contract record that you want to sync with the cancellation quote. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the cancellation quote. | Optional | 62.0 |
| `output​RecordId` | String | ID of the quote or order that you want to cancel. | Optional | 62.0 |
| `output​RecordType` | String | Type of cancellation record that you want to create. | Required | 62.0 |

=== ARTICLE: connect_requests_clone_options_input.htm ===
---
page_id: connect_requests_clone_options_input.htm
title: Clone Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_clone_options_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Clone Options Input

Input representation of the options to clone a sales transaction.

    
      
        
          

**JSON example**

          
: This is a sample request to clone all line items in a ramped group within a sales
            transaction.

```
{
  "recordIds": ["0QLxx0000004CBYGA2"],
  "salesTransactionId": "0Q0xx0000004CE0CAM",
  "options": {
    "lineScope": "AllLines"
  }
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `recordTypeId` | String | ID of the record type related to the record to clone. | Optional | 65.0 |
| `lineScope` | String | Specifies the scope for cloning a ramp segment. You can clone only the last ramp segment. This property determines which line items must be cloned and added to the cloned segment. Valid values are: `AllLines`—Specifies whether all line items in a ramped group must be cloned. `RampedLinesOnly`—Specifies whether only the ramped line items must be cloned. A segment identifier is created for the newly cloned line items, ensuring date continuity between the existing and cloned segment. | Optional | 65.0 |

=== ARTICLE: connect_requests_clone_sales_transaction_input.htm ===
---
page_id: connect_requests_clone_sales_transaction_input.htm
title: Clone Sales Transaction Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_clone_sales_transaction_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Clone Sales Transaction Input

Input representation of the request to clone records within a sales
    transaction.

    
      
        
          

**JSON example**

          
: This is a sample request to clone a record within a sales transaction.

          
: 

```
{
  "recordIds": ["0QLxx0000004CBYGA2"],
  "salesTransactionId": "0Q0xx0000004CE0CAM"
}
```

This is a sample request to clone all line items in a ramped group within a
            sales transaction.

```
{
  "recordIds": ["0QLxx0000004CBYGA2"],
  "salesTransactionId": "0Q0xx0000004CE0CAM",
  "options": {
    "lineScope": "AllLines"
  }
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `recordIds` | String[] | ID of the record to be cloned. You can specify a single record ID only. | Required | 64.0 |
| `salesTransactionId` | String | ID of the sales transaction related to the record IDs to clone. | Required | 64.0 |
| `options` | [Clone Options Input](./connect_requests_clone_options_input.htm.md) | Specifies options to clone a ramp segment within a sales transaction. You can clone only the last ramp segment. | Optional | 65.0 |

=== ARTICLE: connect_requests_configuration_options_input.htm ===
---
page_id: connect_requests_configuration_options_input.htm
title: Configuration Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configuration_options_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configuration Options Input

Input representation for the configuration options.

**JSON example**

: 

```
{
  "configurationOptions": {
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addDefault​Configuration` | Boolean | Indicates whether to automatically add default configurations to the order (`true`) or not (`false`). | Optional | 60.0 |
| `execute​Configuration​Rules` | Boolean | Indicates whether the order must adhere to configuration rules during processing (`true`) or bypass them (`false`). | Optional | 60.0 |
| `validate​Amend​Renew​Cancel` | Boolean | Indicates whether to run validations related to amend, renew, or cancel processes (`true`) or not (`false`). | Optional | 60.0 |
| `validate​Product​Catalog` | Boolean | Indicates whether the order must be validated against the product catalog (`true`) or not (`false`). | Optional | 60.0 |

=== ARTICLE: connect_requests_configurator_preference_input.htm ===
---
page_id: connect_requests_configurator_preference_input.htm
title: Configurator Preference Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_configurator_preference_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Configurator Preference Input

Input representation of the configuration preference for the place sales transaction
    request.

**JSON example**

: 

```
{
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
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
| `configuration​Method` | String | Configuration method for the place sales transaction request. Valid values are: `Force`—Specifies to enforce the predefined configuration process during the sales transaction process. `Skip`—Specifies to skip the configuration process during the quote creation process. `System`—Specifies the system to determine whether the configuration process is required. The default value is `Skip`. | Optional | 63.0 |
| `configuration​Options` | [Configuration Options Input](./connect_requests_configuration_options_input.htm.md) | Configuration options during the ingestion process. | Optional | 63.0 |

=== ARTICLE: connect_requests_context_info_input.htm ===
---
page_id: connect_requests_context_info_input.htm
title: Context Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_info_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Input

Input representation of the context that's associated with a sales transaction for a
    quote or an order.

**JSON example**

: 

```
{
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of the context that represents the created session for the sales transaction. This property is supported only for a PATCH request.If the `contextId` property isn’t specified, the Place Sales Transaction API generates the context ID for the sales transaction. | Optional | 63.0 |

=== ARTICLE: connect_requests_context_node_input.htm ===
---
page_id: connect_requests_context_node_input.htm
title: Context Node Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_node_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Node Input

Input representation of the details of the context nodes for ramp segments.

**JSON example**

: 

```
  "updatedNodes": [
     {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9", // ContextId
        "0Q0xx0000004CPACA2", //Quote or OrderId
        "0QLxx0000004CfIGAU" // Quote Line ID or Order Line ID to update
      ],
      "contextNode": {
          "Discount": 10,
          "Quantity": 5
      }
    }, 
    {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9",
        "0Q0xx0000004CPACA2",
        "2b6401d144904e10aa"
      ],
      "contextNode": {
          "Discount": 20,
          "Quantity": 15
      }
    }
  ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `context​Node` | Map<String, Object> | Details of the context node to be added, updated, or deleted. | Required | 62.0 |
| `contextNode​Path` | String[] | Path to the context node to be added, updated, or deleted. | Required | 62.0 |

=== ARTICLE: connect_requests_create_ramp_deal_input.htm ===
---
page_id: connect_requests_create_ramp_deal_input.htm
title: Create Ramp Deal Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_create_ramp_deal_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Ramp Deal Input

Input representation of the request to create a ramp deal.

**JSON example**

: 

```
{
  "transactionId": "0Q0xx0000004C92CAE",
  "transactionLineId": "0QLxx0000004C9VGAU",
  "subscriptionTerm": 14,
  "subscriptionTermUnit": "MONTHS",
  "trialTerm": 45,
  "trialTermUnit": "DAYS",
  "segmentType": "YEARLY",
  "executionSettings": {
       "executePricing": true,
       "executeConfigRules": false
   }
}
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
| `execution​Settings` | [Execution Settings Input](./connect_requests_execution_settings_input.htm.md)[] | Settings to run the pricing or configuration rules. | Optional | 62.0 |
| `segment​Type` | String | Type of segment that the user wants to create. Valid values are: `FREE_TRIAL` `CUSTOM` `YEARLY` | Required | 62.0 |
| `subscription​Term` | Integer | Subscription length of the term-defined product. | Required | 62.0 |
| `subscription​TermUnit` | String | Unit of time for the subscription length. Valid value is: `MONTHS` | Required | 62.0 |
| `transaction​Id` | String | ID of the sales transaction that’s configured, such as quote or order. | Required | 62.0 |
| `transaction​LineId` | String | Quote line item ID or order item ID that the price ramp is created for. | Required | 62.0 |
| `trialTerm` | Integer | Length of the trial period, if any. | Optional | 62.0 |
| `trialTerm​Unit` | String | Unit of time for the trial period. Valid value is: `DAYS` | Optional. Required if `trialTerm` property is specified. | 62.0 |

=== ARTICLE: connect_requests_delete_ramp_deal_input.htm ===
---
page_id: connect_requests_delete_ramp_deal_input.htm
title: Delete Ramp Deal Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_delete_ramp_deal_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Delete Ramp Deal Input

Input representation of the request to delete a ramp deal.

**JSON example**

: 

```
{
  "rampDealIds": [
    "0Q0xx0000004CDxCAM",
    "0QLxx0000004CSOGA2"
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `rampDeal​Ids` | String[] | Ramp identifier on the quote line item or order item. | Required | 62.0 |

=== ARTICLE: connect_requests_execution_settings_input.htm ===
---
page_id: connect_requests_execution_settings_input.htm
title: Execution Settings Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_execution_settings_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Execution Settings Input

Input representation of the execution settings for a ramp deal.

**JSON example**

: 

```
  "executionSettings": {
       "executePricing": true,
       "executeConfigRules": false
   }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `execute​ConfigRules` | Boolean | Indicates whether to run configuration rules (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |
| `execute​Pricing` | Boolean | Indicates whether to run pricing request (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |

=== ARTICLE: connect_requests_get_eligible_promotions_input.htm ===
---
page_id: connect_requests_get_eligible_promotions_input.htm
title: Eligible Promotions Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_get_eligible_promotions_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Eligible Promotions Input

Input representation of the request to get eligible promotions for line items. This
    representation includes the details to accept line item IDs and a sales transaction
    ID.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "salesTransactionId": "0Q0xx0000004EOECA2",
  "lineItemIds": [
    "0QLxx0000004E7eGAE",
    "0QLxx0000004GCeGAM",
    "0QLxx0000004E7gGAE"
  ]
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `lineItemIds` | String[] | List of line item IDs to evaluate for promotions. The object type is auto-determined from the sales transaction ID. | Required | 66.0 |
| `salesTransactionId` | String | The sales transaction ID, such as an order ID or a quote ID, for the promotion evaluation. | Required | 66.0 |

=== ARTICLE: connect_requests_get_instant_pricing_input.htm ===
---
page_id: connect_requests_get_instant_pricing_input.htm
title: Instant Pricing Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_get_instant_pricing_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Instant Pricing Input

Input representation to fetch the instant pricing details.

        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "7847127122596",
  "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
  "records": [
    {
      "referenceId": "0Q0xx0000004DOSCA2",
      "record": {
        "attributes": {
          "type": "Quote",
          "method": "POST"
        },
        "Name": "Test Quote Proration Pricing",
        "OpportunityId": "006xx000001a4ISAAY",
        "Pricebook2Id": "01sxx0000005ptpAAA"
      }
    },
    {
      "referenceId": "refQuoteLine",
      "record": {
        "attributes": {
          "type": "QuoteLineItem",
          "method": "POST"
        },
        "QuoteId": "0Q0xx0000004DOSCA2",
        "PricebookEntryId": "01uxx0000008zHmAAI",
        "Product2Id": "01txx0000006jmWAAQ",
        "Quantity": 2,
        "UnitPrice": 25,
        "StartDate": "2022-09-28",
        "EndDate": "2028-09-27",
        "PeriodBoundary": "ANNIVERSARY",
        "BillingFrequency": "ANNUAL"
      }
    }
  ]
}
```

          

          
: This example shows a sample request to specify grouping of lines based on
                        criteria.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004DOSCA2",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "0QLxx0000004F3gGAE",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 5
            }
        }, {
            "referenceId": "0QLxx0000004F3hGAE",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupBy",
                    "criteria": {
                        "Quantity": 5
                    }
                },
                "Name": "record"
            }
        }, {
            "referenceId": "GroupId2",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupBy",
                    "criteria": {
                        "Quantity": 2
                    }
                },
                "Name": "record1",
            }
        }
    ]
}
```

          
: This example shows a sample request for the initial grouping of the quote with the
                        quote lines assigned to the first
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupAll" 
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to ungroup a quote but retain the quote
                        lines.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
         {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2,
                "QuoteLineGroupId": null
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "DELETE",
                    "action": "Ungroup"
                }
            }
        }
    ]
}
```

          
: This example shows a sample request to create a new
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST"
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to delete a
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "DELETE",
                    "action": "DeleteGroup"
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to move a
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2
                "QuoteLineGroupId": "{@GroupId2}"
            }
        },
    ]
}
```

        

**Properties**

: 

                                        

                                        

                                        

                                        

                                        

                                    

                                        

                                        

                                        

                                        

                                        

                                    

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID generated by the context service. If you don’t specify a context ID, a new context is created. | Optional | 59.0 |
| `correlationId` | String | Client-generated ID for tracking multiple related API requests. | Optional | 59.0 |
| `records` | [Object with Reference Input](./connect_requests_object_with_reference_input.htm.md)[] | List of pricing data to be fetched. | Required | 59.0 |

=== ARTICLE: connect_requests_group_ramp_action_input.htm ===
---
page_id: connect_requests_group_ramp_action_input.htm
title: Group Ramp Action Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_group_ramp_action_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: connect_requests_place_sales_transaction_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Group Ramp Action Input

Understand the sample request to specify group ramp actions during initial
    sale.

    
      

Keep these considerations in mind when you specify ramp actions.

      
        
- Use the [Clone Sales Transaction API](./connect_resources_clone_sales_transaction.htm.md) to clone a
          ramp segment, and specify the clone option.

        
- Use the [Place Sales Transaction API](./connect_resources_place_sales_transaction.htm.md) to specify a
          group ramp action by using the `groupRampAction`
          property. You can refer to the sections in this topic for examples.

      

    

    
      
        
          

**JSON example to edit a group**

          
: 

This is a sample request that creates the first ramp segment. This request accepts
              IDs of a quote and quote line group. Additionally, the request accepts attributes of
              quote line group such as `IsRamped`, `SegmentType`, `StartDate`, and `EndDate`. A ramp
              segment is created with a ramp identifier and segment identifier added to all the
              quote line items available in the ramp segment.

This process converts a group
              into a segment, which becomes the first segment in the ramp schedule. A quote can
              contain a single ramp schedule only. To create another segment in the ramp schedule,
              use the [Clone Sales Transaction API](./connect_resources_clone_sales_transaction.htm.md).

          
: 
            

```
{
  "groupRampAction": "EditGroup",
  "pricingPref": "System",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0xx0000004CYqCAM",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CYqCAM"
          }
        }
      },
      {
        "referenceId": "1C9xx0000004CVcCAM",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CVcCAM"
          },
          "StartDate": "2025-05-01",
          "EndDate": "2025-06-30",
          "SortOrder": 1,
          "IsRamped": true,
          "SegmentType": "Custom"
        }
      }
    ]
  }
}
```

          

        
        
          

**JSON example to edit a ramp segment**

          
: This is a sample request to edit multiple ramp segments simultaneously, maintaining
            date continuity among ramp
            segments.

```
{
  "groupRampAction": "EditRampSchedule",
  "pricingPref": "System",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0xx0000004CYqCAM",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CYqCAM"
          }
        }
      },
      {
        "referenceId": "1C9xx0000004CVcCAM",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CVcCAM"
          },
          "StartDate": "2025-05-01",
          "EndDate": "2025-06-30"
        }
      },
      {
        "referenceId": "1C9xx0000004CVcAAM",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CVcAAM"
          },
          "StartDate": "2025-07-01",
          "EndDate": "2025-08-30"
        }
      },
      {
        "referenceId": "1C9xx0000004CVcBAM",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CVcBAM"
          },
          "StartDate": "2025-09-01",
          "EndDate": "2025-10-30"
        }
      }
    ]
  }
}
```

        
        
          

**JSON example to add a product**

        
        
          
: This is a sample request to add a product to the current and subsequent segments. A
            ramp identifier and segment identifier are added to the quote line
            items.

```
{
  "groupRampAction": "AddProducts",
  "pricingPref": "System",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0xx0000004CKKCA2",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CKKCA2"
          }
        }
      },
      {
        "referenceId": "1C9xx0000004CCGCA2",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CCGCA2"
          }
        }
      },
      {
        "referenceId": "ref_01txx0000006iCXAAY_0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST",
            "id": "ref_01txx0000006iCXAAY_0"
          },
          "QuoteId": "@{0Q0xx0000004CKKCA2.id}",
          "Id": "ref_01txx0000006iCXAAY_0",
          "UnitPrice": 2000,
          "Product2Id": "01txx0000006iCXAAY",
          "PricebookEntryId": "01uxx0000008yciAAA",
          "Quantity": 1,
          "StartDate": "2025-05-28T00:00:00.000Z",
          "BillingFrequency": null,
          "PeriodBoundary": null,
          "QuoteLineGroupId": "1C9xx0000004CCGCA2"
        }
      },
      {
        "referenceId": "1C9xx0000004CCGCAB",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004CCGCAB"
          }
        }
      },
      {
        "referenceId": "ref_01txx0000006iCXABY_0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST",
            "id": "ref_01txx0000006iCXABY_0"
          },
          "QuoteId": "@{0Q0xx0000004CKKCA2.id}",
          "Id": "ref_01txx0000006iCXAAY_0",
          "UnitPrice": 2000,
          "Product2Id": "01txx0000006iCXAAY",
          "PricebookEntryId": "01uxx0000008yciAAA",
          "Quantity": 1,
          "StartDate": "2025-05-28T00:00:00.000Z",
          "BillingFrequency": null,
          "PeriodBoundary": null,
          "QuoteLineGroupId": "1C9xx0000004CCGCAB"
        }
      }
    ]
  }
}
```

        
        
          

**JSON example to delete a product**

        
        
          
: This is a sample request to delete a product from the current and subsequent ramp
            segments.

```
{
  "pricingPref": "System",
  "groupRampAction": "DeleteProducts",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0SG000000L5r70AC",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0SG000000L5r70AC"
          }
        }
      },
      {
        "referenceId": "0QLSG000000WuTh4AK",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "DELETE",
            "id": "0QLSG000000WuTh4AK"
          }
        }
      },
      {
        "referenceId": "0QLSG000000WuTh4BK",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "DELETE",
            "id": "0QLSG000000WuTh4AK"
          }
        }
      }
    ]
  }
}
```

        
        
          

**JSON example to delete a segment**

          
: This is a sample request to delete the first and last segment in a ramp schedule. The
            API throws an error if the specified segment isn't the first and last segment, ensuring
            there are no gaps between quote line items in different ramp
            segments.

```
{
  "pricingPref": "System",
  "groupRampAction": "DeleteSegment",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0xx0000004CfICAU",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CfICAU"
          }
        }
      },
      {
        "referenceId": "1C9xx0000004FjcCAE",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "DELETE",
            "id": "1C9xx0000004FjcCAE",
            "action": "DeleteGroup"
          }
        }
      }
    ]
  }
}
```

        
        
          

**JSON example to remove a segment from a ramp schedule**

          
: This is a sample request to remove the first or last ramp segment in a ramp schedule.
            This request removes the ramp-specific fields from a quote line group such as `IsRamped` and `SegmentType`. Additionally, this request removes the `RampIdentifier` and `SegmentIdentifier` fields from a quote line
            item.

```
{
  "pricingPref": "System",
  "groupRampAction": "ConvertToNonRampedGroup",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "0Q0xx0000004CfICAU",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CfICAU"
          }
        }
      },
      {
        "referenceId": "1C9xx0000004FjcCAE",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "PATCH",
            "id": "1C9xx0000004FjcCAE"
          }
        }
      }
    ]
  }
}
```

=== ARTICLE: connect_requests_initiate_downgrade_input.htm ===
---
page_id: connect_requests_initiate_downgrade_input.htm
title: Initiate Downgrade Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_initiate_downgrade_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Downgrade Input

Input representation of the details of the request to initiate a downgrade
    action.

**JSON example**

: 

```
{
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "DOWNGRADE-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "downgradeRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2022-09-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to downgrade. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to downgrade. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the downgrade. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the downgrade. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the downgrade action. | Required | 66.0 |

=== ARTICLE: connect_requests_initiate_swap_input.htm ===
---
page_id: connect_requests_initiate_swap_input.htm
title: Initiate Swap Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_initiate_swap_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Swap Input

Input representation of the details of the request to initiate a swap action.

**JSON example**

: 

```
{
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "SWAP-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "swapRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2022-09-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to swap. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to swap. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the swap. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the swap. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the swap action. | Required | 66.0 |

=== ARTICLE: connect_requests_initiate_upgrade_input.htm ===
---
page_id: connect_requests_initiate_upgrade_input.htm
title: Initiate Upgrade Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_initiate_upgrade_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Upgrade Input

Input representation of the details of the request to initiate an upgrade action. The
    response includes the ID of the sales transaction that the upgrade action creates.

**JSON example**

: 

```
{
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "UPGRADE-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "upgradeRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2026-03-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to upgrade. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to upgrade. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the upgrade. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the upgrade. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the upgrade action. | Required | 66.0 |

=== ARTICLE: connect_requests_object_graph_input.htm ===
---
page_id: connect_requests_object_graph_input.htm
title: Object Graph Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_object_graph_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Object Graph Input

Input representation of an sObject  with a graph ID.

      
        
          

**JSON example**

          
: 
            

```
{
  "graph": {
    "graphId": "1",
    "records": [
      {
        "referenceId": "refOrder",
        "record": {
          "attributes": {
            "type": "Order",
            "method": "POST"
          }
        }
      }
    ]
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `graphId` | String | The ID of the graph. | Required | 60.0 |
| `records` | [Object with Reference Input](./connect_requests_object_with_reference_input.htm.md)[] | List of the records to be ingested. | Required | 60.0 |

=== ARTICLE: connect_requests_object_input_representation_map.htm ===
---
page_id: connect_requests_object_input_representation_map.htm
title: Object Input Map
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_object_input_representation_map.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Object Input Map

Input representation of an sObject record in a key-value map format.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "records": [
    {
      "referenceId": "refOrder",
      "record": {
        "attributes": {
          "type": "Order",
          "method": "PATCH",
          "id": "402xx000003KY5vJGH"
        },
        "Quantity": 5
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
- 
- 
  - 
  - 
  - 
  - 
  - 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | Map <String, String> | Configuration input for the record process. Valid values are: `type`—Type of sales transaction such as Quote or Order. `method`—HTTP methods such as POST, PATCH, and DELETE. `id`—Unique identifier for the record. Required for PATCH and DELETE operations. `criteria`—Criteria to group order or quote line items. For example, group order or quote line items based on a monthly billing frequency. `action`—Action to group order or quote line items. Valid values are: `GroupBy` `Group` `Ungroup` `GroupAll` `DeleteGroup` | Required | 60.0 |

=== ARTICLE: connect_requests_object_with_reference_input.htm ===
---
page_id: connect_requests_object_with_reference_input.htm
title: Object with Reference Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_object_with_reference_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Object with Reference Input

Input representation of a list of records to be inserted or updated. To update a
    record, specify the record ID.

    

This is a sample request to create a sales transaction for an order line item.

        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refOrderItem0",
  "record": {
    "attributes": {
      "type": "OrderItem",
      "method": "POST"
    },
    "OrderId": "@{refOrder.id}",
    "OrderActionId": "@{refOrderAction.id}",
    "PricebookEntryId": "01uRM000000igZG",
    "Quantity": 2
  }
}
```

          

        
      

This is a sample request to update an order line item.

        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refOrderItem0",
  "record": {
    "attributes": {
      "type": "OrderItem",
      "method": "PATCH",
      "id": "402xx000003KY5vJGH"
    },
    "OrderId": "@{refOrder.id}",
    "OrderActionId": "@{refOrderAction.id}",
    "PricebookEntryId": "01uRM000000igZG",
    "Quantity": 2,
    "UnitPrice": 800
  }
}
```

          

        
      

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceId` | String | Reference ID that maps to the response and can be used as a reference in later subrecords. This property value starts with a letter or number only and can contain letters, numbers, and underscores. It's also case-sensitive when used for referencing. | Required | 60.0 |
| `records` | [Object Input Map](./connect_requests_object_input_representation_map.htm.md) | Details of a record to be ingested. | Required | 60.0 |

=== ARTICLE: connect_requests_place_order_input.htm ===
---
page_id: connect_requests_place_order_input.htm
title: Place Order Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_place_order_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Order Input

Input representation of the request to create or update an order.

        
          

**JSON example**

          
: 
            

```
{
  "pricingPref": "System",
  "configurationInput": "RunAndAllowErrors",
  "configurationOptions": {
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "refOrder",
        "record": {
          "attributes": {
            "type": "Order",
            "method": "POST",
            "Id": "POST"
          }
        }
      },
      {
         "referenceId":"refOrderItem",
         "record":{
         "attributes":{
             "type":"OrderItem",
             "method":"POST"
            },
            "OrderId":"@{refOrder.id}",
            "OrderActionId":"@{refOrderAction.id}",
            "ListPrice":"144.99",
            "Quantity":3,
            "PricebookEntryId":"01uxx0000008yXPAAY",
            "Product2Id":"01txx0000006i2UAAQ",
            "UnitPrice":"199.49"
       }
      }
    ]
  }
}
```

          

          
: This example shows a sample request to define grouping of order
            items.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "801xx000003GZ9bAAG"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST"
                    },
                    "Name": "New Group",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to ungroup order
            items.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "DELETE",
                        "id": "refOlg1",
                        "action": "Ungroup"
                    }
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to create a new
            group.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "refOlg",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST"
                    },
                    "Name": "New Group",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
    "contextId": "",
    "correlationId": "",
    "records": [
        {
            "referenceId": "refOrder",
            "record": {
                "attributes": {
                    "type": "Order",
                    "method": "PATCH",
                    "id": "refOrder"
                }
            }
        },
        {
            "referenceId": "refOlg",
            "record": {
                "attributes": {
                    "type": "OrderItemGroup",
                    "method": "DELETE",
                    "id": "refOlg",
                    "action": "DeleteGroup"
                }
            }
        }
    ]
}
```

          
: This example shows a sample request to group order items based on
            criteria.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "g0",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": null
                        }
                    },
                    "Name": "Billing Frequency: ",
                    "OrderId": "@{refOrder.id}"
                }
            },
            {
                "referenceId": "g1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": "Monthly"
                        }
                    },
                    "Name": "Billing Frequency: Monthly",
                    "OrderId": "@{refOrder.id}"
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
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
                    

                    

                    

                  

                  
                    

                    

                    
- 
- 
- 

                    

                    

                  

                

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​RatesPref` | String | Rate card entries defined in the catalog that must be fetched for order items with usage-based pricing during the order creation process. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for order items during the order creation process. `Skip`—Skips the retrieval of rate card entries for order items during the order creation process. The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 62.0 |
| `configuration​Input` | String | Configuration input for the place order process. Valid values are: `RunAndAllowErrors`—Specifies to run the configuration and to proceed order ingestion upon encountering any configuration errors. `RunAndBlockErrors`—Specifies to run configuration and to block order ingestion upon encountering any configuration errors. `Skip`—Specifies to skip configuration. The default value is `RunAndBlockErrors`. | Optional | 60.0 |
| `configuration​Options` | [Configuration Options Input​](./connect_requests_configuration_options_input.htm.md)[] | Configuration options during the ingestion process. | Optional | 60.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph of the order payload to be ingested. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. | Required | 60.0 |
| `pricing​Pref` | String | Pricing preference during the create order process. Valid values are: `Force`—Specifies to force pricing during the order ingestion process. `Skip`—Specifies to skip pricing during the order ingestion process. `System`—Specifies the system to determine whether a pricing calculation is required. The default value is `System`. | Optional | 60.0 |

=== ARTICLE: connect_requests_place_quote_input.htm ===
---
page_id: connect_requests_place_quote_input.htm
title: Place Quote Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_place_quote_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Quote Input

Input representation of the request to create or update a quote.

        
          

**JSON example**

          
: This example shows a sample request to create a
            quote.

```
{
  "pricingPref": "System",
  "configurationInput": "RunAndAllowErrors",
  "configurationOptions": {
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },  "graph": {
    "graphId": "createQuote",
    "records": [{ 
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "POST"
          },
          "opportunityId": "---",
          "quoteProp1": "value1",
          "quoteProp2": "value2"
        }
      },
      {
        "referenceId": "refQuoteLineItem1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteLineItemProp1": "value1",
          "QuoteLineItemProp2": "value2"
        }
      },
      {
      "referenceId": "refQuoteLineItemAttribute",
      "record": {
        "attributes": {
              "type": "QuoteLineItemAttribute",
              "method": "POST"
       },
       "QuoteLineItemId": "@{refQuoteLineItem1.id}",
       "AttributeDefinitionId": "0tjxx0000000001AAA"
      }
}
    ]
  }
}
```

          
: This example shows a sample request to insert, update, or delete a quote line
            item.

```
{
  "pricingPref": "System",
  "configurationInput": "skip",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004E2mCAE"
          },
          "Name": "Quote_Acme"
        }
      },
      {
        "referenceId": "refQuoteLineItemToCreate1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "0Q0xx0000004E2mCAE",
          "PricebookEntryId": "01uxx0000008yXPAAY",
          "Product2Id": "01txx0000006i2UAAQ",
          "Quantity": 2.0,
          "UnitPrice": 800.0,
          "PeriodBoundary": "Anniversary",
          "BillingFrequency": "Monthly",
          "StartDate": "2024-03-11"
        }
      },
      {
        "referenceId": "refQuoteLineItemToPatch2",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "0Q0xx0000004E2mCAE"
          },
          "Quantity": 2.0,
          "UnitPrice": 600.0
        }
      },
      {
        "referenceId": "refQuoteLineItemToDelete3",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "DELETE",
            "id": "0Q0xx0000004E2mYLK"
          }
        }
      }
    ]
  }
}
```

          
: This example shows a sample request to define grouping of quote line
            items.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "groupLines",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST",
                  "action": "GroupBy",
                  "criteria": {
                    "Quantity": 1
                  }
               },
               "Name": "From Place Quote API Group",
               "QuoteId": "@{refQuote.id}"
            }
         },
         {
            "referenceId": "refQuoteItem1",
            "record": {
               "attributes": {
                  "type": "QuoteLineItem",
                  "method": "PATCH",
                  "id":"0QLxx0000004DJcGAM"
               },
               "QuoteLineGroupId": "@{refQlg1.id}",
               "Quantity": 1
            }
         }
      ]
   }
}
```

          
: This example shows a sample request for the initial grouping of the quote with the
            quote lines assigned to the first
            group.

```
{
  "pricingPref": "Force",
  "graph": {
    "graphId": "test",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CAmCAM"
          }
        }
      },
      {
        "referenceId": "refQlg1",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "POST",
            "action": "GroupAll"
          },
          "Name": "From PQ API Group",
          "QuoteId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This example shows a sample request to ungroup a quote but retain the quote
            lines.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote", 
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "{GroupId}",
                  "action": "Ungroup"
               }
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to create a new
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST"
               },
               "Name": "From PQ API Group",
               "QuoteId": "@{refQuote.id}"
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "{GroupId}",
                  "action": "DeleteGroup"
               }
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to move a
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From PlaceQuote Api"
            }
         },
        {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PATCH"
                    "id": "0QLxx0000004CBYGA2"
                },
                "Quantity": 2,
                "QuoteLineGroupId": "@{GroupId2}"
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
- 
- 

                    

                    

                  

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​RatesPref` | String | Rate card entries defined in the catalog that must be fetched for quote line items with usage-based pricing during the quote creation process. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for quote line items during the quote creation process. `Skip`—Skips the retrieval of rate card entries for quote line items during the quote creation process. The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 62.0 |
| `configuration​Input` | String | Configuration input for the place quote process. Valid values are: `RunAndAllowErrors` `RunAndBlockErrors` `Skip` The default value is `RunAndBlockErrors`. | Optional | 60.0 |
| `configuration​Options` | [Configuration Options Input](./connect_requests_configuration_options_input.htm.md) | Configuration options during the ingestion process. | Optional | 60.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph representing the quote structure. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. | Required | 60.0 |
| `pricing​Pref` | String | Pricing preference during the quote process. Valid values are: `Force` `Skip` `System` The default value is `System`. | Optional | 60.0 |

=== ARTICLE: connect_requests_place_sales_transaction_input.htm ===
---
page_id: connect_requests_place_sales_transaction_input.htm
title: Sales Transaction Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_place_sales_transaction_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Input

Input representation of the details of the request to place a sales transaction, such as
    a quote or an order.

      
        
          

**JSON example**

          
: This is a sample request to create a sales transaction for a quote. This example also
            skips tax calculation by specifying a value for the optional `taxPref` property.

          
: 
            

```
{
  "pricingPref": "System",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "taxPref": "Skip",
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "createQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "POST",
            "type": "Quote"
          },
          "Name": "Quote_Acme",
          "Pricebook2Id": "01sDU000000JvhbYAC"
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "Product2Id": "01tDU000000F7b8YAC",
          "PricebookEntryId": "01uDU000000fxt2YAA",
          "UnitPrice": 100,
          "Quantity": "1",
          "StartDate": "2024-10-29",
          "EndDate": "2025-03-01",
          "PeriodBoundary": "Anniversary"
        }
      },
      {
        "referenceId": "refQuoteLine1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "Product2Id": "01tLT00000AA2M9YAL",
          "PricebookEntryId": "01uLT000007PTafYAG",
          "Quantity": "1"
        }
      },
      {
        "referenceId": "refQuoteLineItemAttribute1",
        "record": {
          "attributes": {
            "type": "QuoteLineItemAttribute",
            "method": "POST"
          },
          "QuoteLineItemId": "@{refQuoteLine0.id}",
          "AttributeDefinitionId": "0tjRT0000000XbtYAE",
          "AttributeValue": "True"
        }
      },
      {
        "referenceId": "refQuoteLineRelationship1",
        "record": {
          "attributes": {
            "type": "QuoteLineRelationship",
            "method": "POST"
          },
          "ProductRelationshipTypeId": "0yoLT000000wHq6YAE",
          "ProductRelatedComponentId": "0dSLT00000076IP2AY",
          "MainQuoteLineId": "@{refQuoteLine0.id}",
          "AssociatedQuoteLineId": "@{refQuoteLine1.id}",
          "AssociatedQuoteLinePricing": "NotIncludedInBundlePrice"
        }
      }
    ]
  }
}
```

          

          
: This sample request assigns a TransactionProcessingType record to a quote without any
            additional preferences. In this example, the TransactionType value for a record is set
            to a TransactionProcessingType record. See [TransactionProcessingType](./tooling_api_objects_transactionprocessingtype.htm.md) tooling
            object for more details.

```
{
  "pricingPref": "Force",
  "contextDetails": {
    "contextId": "f1c9e3e1c335f7959a88de09d3a867cc2b95e08709b99de8e2edeb8f5039e8ed",
    "scope": "Session"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "POST"
          },
          "OpportunityId": "006xx000001a2oWAAQ",
          "PriceBook2Id": "01sxx0000005ptpAAA",
          "TransactionType": "SkipPricingAndRunTax",
          "Name": "Quote_No_Tax_System"
        }
      },
      {
        "referenceId": "refQLI1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "UnitPrice": 49.99,
          "Product2Id": "01txx0000006i2aAAA",
          "PricebookEntryId": "01uxx0000008yX0AAI",
          "Quantity": 10
        }
      }
    ]
  }
}
```

          
: This is a sample request to insert, update, or delete a quote line
            item.

```
{
  {
  "pricingPref": "System",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "PATCH",
            "type": "Quote",
            "id": "801xx000003GZ9bAAG"
          }
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "402xx000003KY5vJGH"
          },
          "Quantity": "5"
        }
      }
    ]
  }
}
```

          
: This is a sample request to define grouping of quote line
            items.

```
{
  "pricingPref": "Force",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "groupQuoteLines",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "PATCH",
            "type": "Quote",
            "id": "801xx000003GZ9bAAG"
          }
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "402xx000003KY5vJGH"
          },
          "QuoteLineGroupId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This is s a sample request for the initial grouping of the quote with all the quote
            lines assigned to the first
            group.

```
{
  "pricingPref": "Force",
  "catalogRatesPref": "Skip",
  "graph": {
    "graphId": "groupQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CAmCAM"
          }
        }
      },
      {
        "referenceId": "refQlg1",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "POST",
            "action": "GroupAll"
          },
          "Name": "From PST API Group",
          "QuoteId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This is a sample request to ungroup a quote but retain the quote
            lines.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "ungroupQuote",
      "records": [
         {
            "referenceId": "refQuote", 
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "402xx000003KY5vJGH",
                  "action": "Ungroup"
               }
            }
         }
      ]
   }
}
```

          
: This is a sample request to create a new
            group.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "createGroup",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST"
               },
               "Name": "From PQ API Group",
               "QuoteId": "@{refQuote.id}"
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "deleteGroup",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "402xx000003KY5vJGH",
                  "action": "DeleteGroup"
               }
            }
         }
      ]
   }
}
```

          
: This is a sample request to group order items based on
            criteria.

```
{
    "catalogRatesPref": "Skip",
    "pricingPref": "Force",
    "graph": {
        "graphId": "groupOrderItems",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "0Q0xx0000004C99CAE"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": null
                        }
                    },
                    "Name": "Billing Frequency: ",
                    "OrderId": "@{refOrder.id}"
                }
            },
            {
                "referenceId": "g1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": "Monthly"
                        }
                    },
                    "Name": "Billing Frequency: Monthly",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This is a sample request to save changes to a ramp deal by using context ID. The
            context ID is returned by the Ramp Deal APIs. See [Create Ramp Deal
            (POST)](./connect_resources_create_ramp_deal.htm.md).

```
{
  "pricingPref": "Force",
  "contextDetails": {
    "contextId": "f1c9e3e1c335f7959a88de09d3a867cc2b95e08709b99de8e2edeb8f5039e8ed",
    "scope": "Session"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004DQ4CAM"
          }
        }
      }
    ]
  }
}
```

          
: To see examples that specify actions to create ramp deals for groups, see [Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md).

          
          
: To see examples that apply to usage-based products, see [Usage-Based Product Input](./connect_requests_usage_based_product_input.htm.md).

        
        
          

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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalogRates​Pref` | String | Rate card entries defined in the catalog that must be fetched for sales items with usage-based pricing during the creation of the sales transaction. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for sales items during the creation of the sales transaction. `Skip`—Skips the retrieval of rate card entries for sales items during the creation of the sales transaction.The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 63.0 |
| `configuration​Pref` | [Configurator Preference Input](./connect_requests_configurator_preference_input.htm.md) | Configuration preference during the quote process. These preferences ensure that quotes are defined as per the requirement. | Optional | 63.0 |
| `contextDetails` | [Context Input](./connect_requests_context_info_input.htm.md) | Context details that are created for a sales transaction. | Required if the `graph` property isn’t specified. | 63.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph of the sales transaction to be ingested. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. To create custom objects that are at the grandchildren level from a line item, you must create the hierarchy of objects until the grandchild object in the same request. | Required if the `contextDetails` property isn’t specified. | 63.0 |
| `groupRampAction` | String | Specifies the action ‌that you want to perform on group ramp segments. You can also convert a non-ramped group into a ramped group. Valid values are: `AddProducts`—Adds rampable products to group ramp segments. `DeleteProducts`—Deletes ramped products. `EditGroup`—Converts a non-ramped group into a group ramp segment, or edit group ramp segment attributes such as name and description, except the start and end dates. `EditRampSchedule`—Edits details of the group ramp segments, including start and end dates. `DeleteSegment`—Deletes the first or last segment in a group ramp schedule. `ConvertToNonRampedGroup`—Converts the first or last group ramp segment into a non-ramped group. To add or delete ramped line items from multiple group ramp segments, specify the applicable values in the `graph` property. See [Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md) to refer to examples. | Optional | 65.0 |
| `pricingPref` | String | Pricing preference during the creation of a sales transaction. Valid values are: `Force`—Enforces pricing during the creation of sales transactions. `Skip`—Skips pricing during the creation of sales transactions. `System`—Determines whether a pricing calculation is required. The default value is `System`. | Optional | 63.0 |
| `taxPref` | String | Specifies whether to execute or skip the tax calculation step for each sales transaction record. Valid value is `Skip`. If you don't specify this value, then tax calculation request is performed by default. | Optional | 65.0 |

          

        
      

    

- 
**[Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md)**  

Understand the sample request to specify group ramp actions during initial     sale.

=== ARTICLE: connect_requests_place_supplemental_transaction_input.htm ===
---
page_id: connect_requests_place_supplemental_transaction_input.htm
title: Supplemental Transaction Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_place_supplemental_transaction_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Supplemental Transaction Input

Input representation of the details of the request to create a supplemental
    order.

**JSON example**

                    
: This sample creates a supplemental order, which is a clone of the original
                        order. The supplemental order is related to the original
                        order.

```
{
  "relatedSalesTransactionId": "801S70000001VKgIAM"
}
```

: This sample overrides a field value of an order line item to supplement the order item with ID
                        value as `802SG000003vZ15YAE`.

```
{
    "relatedSalesTransactionId": "801S70000001VKgIAM",
    "pricingPref": "System",
    "supplementalGraph": {
        "graphId": "1",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "801S70000001VKgIAM"
                    },
                    "EffectiveDate": "2025-03-01",
                    "QuoteId": "0Q0xx0000004DQ4CAM"
                }
            },
            {
                "referenceId": "refOrderItem",
                "record": {
                    "attributes": {
                        "type": "OrderItem",
                        "method": "PATCH",
                        "id": "802SG000003vZ15YAE"
                    },
                    "QuoteLineItemId": "0Q0xx0000004E2mYLK"
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
| `pricingPref` | String | Pricing preference for this supplemental transaction or order ingestion process. Valid values are: `Force`—Enforces pricing during the creation of sales transactions. `Skip`—Skips pricing during the creation of sales transactions. `System`—Determines whether a pricing calculation is required. If `pricingPref` value is defined as either `Force` or `System`, the supplemental order can have a different pricing from the original order. | Optional | 64.0 |
| `relatedSales​TransactionId` | String | Related or the original sales transaction upon which a supplemental transaction is created. | Required | 64.0 |
| `supplemental​Graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph that represents a payload with the additional changes to be ingested. The attribute's HTTP method must be PATCH. The attribute ID must be the ID of the original order or order item that you want to supplement. | Optional | 64.0 |

=== ARTICLE: connect_requests_read_sales_transaction_input.htm ===
---
page_id: connect_requests_read_sales_transaction_input.htm
title: Read Sales Transaction Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_read_sales_transaction_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Read Sales Transaction Input

Input representation of the filter criteria details to read a sales
    transaction.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "queryTags": [
    "Quote",
    "QuoteLineItem",
    "Product"
  ],
  "sobjectFieldMap": {
    "Quote": [],
    "QuoteLineItem": [
      "Quantity",
      "Product2Id"
    ]
  },
  "filters": [
    {
      "sObjectName": "Quote",
      "fieldName": "Status",
      "operator": "Equals",
      "operands": [
        {
          "value": "Draft",
          "type": "STRING"
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
| `contextId` | String | ID of the context to retrieve the data records. | Required | 65.0 |
| `queryTags` | List<String> | List of objects that must be retrieved from the context. | Optional | 65.0 |
| `sobjectFieldMap` | Map<String, List<String>> | Mapping of an sObject name to a list. The list includes the sObject field names on the object or can be an empty list. An empty list specifies that all fields on the object must be queried. | Optional | 67.0 |
| `filters` | List<[Sales Transaction Filter Condition](./connect_requests_sales_transaction_filter_condition_input.htm.md#SalesTransactionFilterConditionInputRepresentation)> | Filter conditions to query the context data. | Optional | 67.0 |

=== ARTICLE: connect_requests_renew_input.htm ===
---
page_id: connect_requests_renew_input.htm
title: Renewal Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_renew_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Renewal Input

Input representation of the details of the request to initiate the renewal of an
    asset.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote",
  "renewalEndDate": "2024-10-03T23:59:59",
  "renewalStartDate": "2023-10-04T00:00:00"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to renew. | Required | 62.0 |
| `contractId` | String | ID of the Contract record that you want to sync with the renewal of the Quote or Order record. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the renewal quote. | Optional | 62.0 |
| `output​RecordId` | String | ID of the Quote or Order record that you want to renew. | Optional | 62.0 |
| `output​RecordType` | String | Type of renewal record that you want to create. | Required | 62.0 |
| `renewal​EndDate` | String | End date of the renewal process for the assets. | Optional | 62.0 |
| `renewal​StartDate` | String | Start date of the renewal process for the assets. Required for early asset renewals and renewing expired assets, using today’s date or a future date. | Optional | 62.0 |

=== ARTICLE: connect_requests_sales_transaction_filter_condition_input.htm ===
---
page_id: connect_requests_sales_transaction_filter_condition_input.htm
title: Sales Transaction Filter Condition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sales_transaction_filter_condition_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Filter Condition Input

Input representation of filter conditions used to query sales transaction context
    data.

    

        
          

**JSON example**

          
: 
            

```
{
  "filters": [
    {
      "sObjectName": "Quote",
      "fieldName": "Status",
      "operator": "Equals",
      "operands": [
        {
          "value": "Draft",
          "type": "STRING"
        }
      ]
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
- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sObjectName` | String | Name of the sObject that contains the field to filter on. | Required if the `fieldName` property value isn’t specified. Or, specify the `nodeName` and `attributeName` property values. | 67.0 |
| `fieldName` | String | Name of the field on the specified sObject to filter on. | Required if the `sObjectName` property value isn’t specified. Or, specify the `nodeName` and `attributeName` property values. | 67.0 |
| `operator` | String | Operator to use to filter the results. Valid values are: `Equals` `NotEquals` `Gt`—Greater Than `GtEq`—Greater Than or Equals `Lt`—Less Than `LtEq`—Less Than or Equals `In` | Required | 67.0 |
| `nodeName` | String | Name of the context node to apply filtering on. | Optional | 67.0 |
| `attributeName` | String | Name of the node attribute to apply filtering on. | Optional | 67.0 |
| `operands` | [Sales Transaction Operand](./connect_requests_sales_transaction_operand_input.htm.md#SalesTransactionOperandInputRepresentation)[] | Operand values with explicit value and type metadata. | Required | 67.0 |
| `underlyingFilters` | [Sales Transaction Filter Condition](#SalesTransactionFilterConditionInputRepresentation)[] | Nested filter conditions used to compose a composite filter. | Optional | 67.0 |
| `operatorLogic` | String | Logical expression that defines how underlying filters are combined. Valid values are: `AND` `OR` | Optional | 67.0 |

=== ARTICLE: connect_requests_sales_transaction_operand_input.htm ===
---
page_id: connect_requests_sales_transaction_operand_input.htm
title: Sales Transaction Operand Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sales_transaction_operand_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Operand Input

Input representation of a filter operand for reading sales transaction context
    data.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "operands": [
    {
      "value": "Draft",
      "type": "STRING"
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
- 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `value` | String | Operand value used by the filter condition. | Required | 67.0 |
| `type` | String | Data type of the operand value. Valid values are: `STRING` `NUMBER` `BOOLEAN` `DATETIME` `DATE` | Required | 67.0 |

=== ARTICLE: connect_requests_swap_group.htm ===
---
page_id: connect_requests_swap_group.htm
title: Swap Group Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_swap_group.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Swap Group Input

Input representation of the details of the swap groupings for swap
    operations.

**JSON example**

: 

```
{
  "swapGroups": {
    "groups": [
      {
        "referenceId": "SWAP-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "swapRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2022-09-22"
              }
            }
          ]
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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inGroup` | Object | Products to include in the swap. These objects are supported. QuoteLineItem OrderItem | Required | 66.0 |
| `outGroup` | [Swap Group](#)[] | Assets to exclude from the swap. You can’t use string values for properties, such as quantity and price. | Required | 66.0 |
| `referenceId` | String | Reference ID of the operation. | Required | 66.0 |

=== ARTICLE: connect_requests_update_ramp_deal_input.htm ===
---
page_id: connect_requests_update_ramp_deal_input.htm
title: Update Ramp Deal Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_update_ramp_deal_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Update Ramp Deal Input

Input representation of the request to update a ramp deal.

**JSON example**

: 

```
{
  "executionSettings": {
       "executePricing": true,
       "executeConfigRules": false
  },
  "addedNodes": [
    {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9", // Context ID
        "0Q0xx0000004CPACA2", //Quote or Order ID
        "RandomUUID" // random UUID for Quote Line Item or Order Item ID
      ],
      "contextNode": {
         "Discount": 10,
         "Quantity": 5,
         "ItemSegmentName": "Year 5",
         "StartDate":"2024-09-07T00:00:00.000Z",
         "EndDate":"2024-09-07T00:00:00.000Z"
      }
    }
  ],
  "updatedNodes": [
     {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9", // Context ID
        "0Q0xx0000004CPACA2", //Quote or Order ID
        "0QLxx0000004CfIGAU" // Quote Line ID or Order Line ID to update
      ],
      "contextNode": {
          "Discount": 10,
          "Quantity": 5
      }
    } 
  ],
  "deletedNodes": [
    {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9",
        "0Q0xx0000004CPACA2",
        "0QLxx0000004CfIGAU" // Quote Line Item ID to delete
      ]
    }
  ]
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `added​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be added. | Required | 62.0 |
| `deleted​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be deleted. | Required | 62.0 |
| `execution​Settings` | [Execution Settings Input](./connect_requests_execution_settings_input.htm.md)[] | Settings to run the pricing or configuration rules. | Optional | 62.0 |
| `updated​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be updated. | Required | 62.0 |

=== ARTICLE: connect_requests_usage_based_product_input.htm ===
---
page_id: connect_requests_usage_based_product_input.htm
title: Usage-Based Product Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_usage_based_product_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Usage-Based Product Input

Understand the sample request structure to specify and manage usage-based products
    within a sales transaction.

    
      
        
          

**JSON example to create a quote record with default rates and default grants**

          
: 
            

The example shows a sample request to creates these records with these updates.

            
              
- 
`Quote`—Creates the main quote record
                with default rates and default grants.

              
- 
`Quote Line Item`—Adds a product to the
                quote.

              
- 
`Rate Card Entry`—Links default pricing
                from rate card. When `NegotiatedRate` property
                value is null, the rate card price is used.

              
- 
`Usage Grant`—Allocates all default
                grants.

            

            

```
{
  "pricingPref": "system",
  "configurationPref": {
    "configurationMethod": "skip",
    "configurationOptions": {
      "validateProductCatalog": false,
      "validateAmendRenewCancel": false,
      "executeConfigurationRules": false,
      "addDefaultConfiguration": false
    }
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "POST"
          },
          "Name": "Q-2024-001",
          "QuoteAccountId": "001xx000003DHP0AAO",
          "OpportunityId": "006xx000004TmiGAAS",
          "Status": "Draft",
          "Pricebook2Id": "01sxx0000001SGEAA2"
        }
      },
      {
        "referenceId": "refQuoteLineItem",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "Product2Id": "01txx0000001SGEAA2",
          "StartDate": "2024-10-29",
          "PeriodBoundary": "Anniversary",
          "EndDate": "2027-03-01",
          "PricebookEntryId": "01uxx0000001SGEAA2",
          "UnitPrice": 100,
          "Quantity": 1
        }
      },
      {
        "referenceId": "refRateCardEntry",
        "record": {
          "attributes": {
            "type": "QuoteLineRateCardEntry",
            "method": "POST"
          },
          "RateCardEntryId": "1CJxx0000004CXEGA2",
          "NegotiatedRate": null,
          "QuoteLineItemId": "@{refQuoteLineItem.id}"
        }
      }
    ]
  }
}
```

          

        
        
        
          

**JSON example to specify negotiated grants**

          
: 
            

This example shows a sample response to create a QuotLineItmUseRsrcGrant record that
              links a quote line item to a product usage grant for usage-based products. This
              request performs these updates.

            
              
- Associates a usage grant with a quote line item.

              
- Allocates a quantity of usage resources.

              
- Applies a usage policy that defines how the resources can be consumed.

              
- Links to a base product usage grant that defines the grant structure.

            

            

```
{
  "pricingPref": "system",
  "configurationPref": {
    "configurationMethod": "skip",
    "configurationOptions": {
      "validateProductCatalog": false,
      "validateAmendRenewCancel": false,
      "executeConfigurationRules": false,
      "addDefaultConfiguration": false
    }
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "ref1CJxx0000004CXGGA2",
        "record": {
          "attributes": {
            "type": "QuotLineItmUseRsrcGrant",
            "method": "POST"
          },
          "GrantQuantity": 4,
          "ProductUsageResourcePolicyId": "7Suxx0000004C92CAE",
          "QuoteLineItemId": "0QLxx0000004CnMGAU",
          "ProductUsageGrantId": "1BXxx0000004C92GAE"
        }
      }
    ]
  }
}
```

          

          
: 
            

This example shows a sample response to update the previously created
              QuotLineItmUseRsrcGrant record with additional units, which is specified by using the
                `GrantQuantity` property. The quote line item now
              has 97 units of usage resource allocation.

            

```
{
  "pricingPref": "system",
  "configurationPref": {
    "configurationMethod": "skip",
    "configurationOptions": {
      "validateProductCatalog": false,
      "validateAmendRenewCancel": false,
      "executeConfigurationRules": false,
      "addDefaultConfiguration": false
    }
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "ref1X6xx000000003GCAQ",
        "record": {
          "attributes": {
            "method": "PATCH",
            "type": "QuotLineItmUseRsrcGrant",
            "id": "1X6xx000000003GCAQ"
          },
          "GrantQuantity": 97
        }
      }
    ]
  }
}
```

          

        
        
          

**JSON example to specify tiered pricing and usage grants**

          
: 

This example shows a sample request to update an existing quote with tiered pricing
              and usage grants. This request sets up a multi-tier rate structure and updates a usage
              grant quantity along with these additional updates.

              
- Creates a base rate card entry with a negotiated rate of 10. Sets the base price
                for the quote line item.

              
- Creates a second rate card entry for tiered pricing without any negotiated rate.
                The default rate card is used. This rate card entry is the base for tier
                adjustments.

              
- Creates a tier adjustment for quantities 0 through 50 and adds $5 adjustment to
                the base rate.

              
- Creates a tier adjustment for quantities 50 through 100 and adds an adjustment of
                $10.

              
- Updates an existing usage resource grant record to set grant quantity to 150
                units.

            

For example, if an order is placed for 75 units, the base rate is $10. As tier 2
              is applicable for this order, an adjustment of $10 is applicable. The final price per
              unit is $20 with a total of $1500 for 75
            units.

```
{
  "pricingPref": "system",
  "configurationPref": {
    "configurationMethod": "skip",
    "configurationOptions": {
      "validateProductCatalog": false,
      "validateAmendRenewCancel": false,
      "executeConfigurationRules": false,
      "addDefaultConfiguration": false
    }
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "refLineItemParent",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CXEGA2"
          }
        }
      },
      {
        "referenceId": "ref1",
        "record": {
          "attributes": {
            "type": "QuoteLineRateCardEntry",
            "method": "POST"
          },
          "RateCardEntryId": "1CJxx0000004CXEGA2",
          "NegotiatedRate": 10,
          "QuoteLineItemId": "0QLxx0000004Eh6GAE"
        }
      },
      {
        "referenceId": "refTierRateCardEntry0",
        "record": {
          "attributes": {
            "type": "QuoteLineRateCardEntry",
            "method": "POST"
          },
          "RateCardEntryId": "1CJxx0000004CXFGA2",
          "QuoteLineItemId": "0QLxx0000004Eh6GAE"
        }
      },
      {
        "referenceId": "refTier0",
        "record": {
          "attributes": {
            "type": "QuoteLineRateAdjustment",
            "method": "POST"
          },
          "Name": "Tier 1",
          "AdjustmentType": "Amount",
          "AdjustmentValue": 5,
          "LowerBound": 0,
          "UpperBound": 50,
          "QuoteLineRateCardEntryId": "@{refTierRateCardEntry0.id}"
        }
      },
      {
        "referenceId": "refTier1",
        "record": {
          "attributes": {
            "type": "QuoteLineRateAdjustment",
            "method": "POST"
          },
          "Name": "Tier 2",
          "AdjustmentType": "Amount",
          "AdjustmentValue": 10,
          "LowerBound": 50,
          "UpperBound": 100,
          "QuoteLineRateCardEntryId": "@{refTierRateCardEntry0.id}"
        }
      },
      {
        "referenceId": "refTier2",
        "record": {
          "attributes": {
            "type": "QuoteLineRateAdjustment",
            "method": "POST"
          },
          "Name": "Tier 3",
          "AdjustmentType": "Amount",
          "AdjustmentValue": 15,
          "LowerBound": 100,
          "UpperBound": 150,
          "QuoteLineRateCardEntryId": "@{refTierRateCardEntry0.id}"
        }
      },
      {
        "referenceId": "refGt2xzdUP",
        "record": {
          "attributes": {
            "type": "QuotLineItmUseRsrcGrant",
            "method": "PATCH",
            "id": "1X6xx000000003GCAQ"
          },
          "GrantQuantity": 150
        }
      }
    ]
  }
}
```

=== ARTICLE: connect_resources_assets_amend.htm ===
---
page_id: connect_resources_assets_amend.htm
title: Asset Amendment (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_assets_amend.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset Amendment (POST)

Initiate and execute the amendment of a quote or an
    order.

    

## Considerations

      
      

For usage products, creating an order directly by setting `outputRecordType` to `Order` is currently not
        supported. The direct-to-order flow can create Order Products without required related Rate
        Card Entry records, which can cause order activation to fail.

      

When you amend usage assets, use a two-step flow.

      
        
- Create an amendment quote by calling `initiateAmendment` with `outputRecordType`
          set to `Quote`.

        
- Create an order from that amendment quote.

      

    

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the InitiateAmend API permission set.

        
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/assets/actions/amend
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/assets/actions/amend
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "amendmentStartDate": "2023-10-04T00:00:00",
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote",
  "quantityChange": 5
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to add to the amendment record. | Required | 62.0 |
| `amendmentStart​Date` | String | Start date of the amendment. | Required | 62.0 |
| `contract​Id` | String | ID of the Contract record that you want to sync with the amendment quote. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the amendment quote. | Optional | 62.0 |
| `outputRecord​Id` | String | ID of the quote or order record that you want to add the assets to. | Optional | 62.0 |
| `output​RecordType` | String | Type of amendment record that you want to create. For usage products, set this value to `Quote`. The usage-related records (`QuoteLineItemUseResourceGrant`, `QuoteLineItemUsageResourcePolicy`, and `QuoteLineRateCardEntry`) are copied in the quote action flow, not in the amend order flow. | Required | 62.0 |
| `quantity​Change` | Double | Quantity to add to or reduce from the asset's existing quantity. | Required | 62.0 |

          

        

          

        
        
          

**Response body for POST**

          
: [Amendment](./connect_responses_amend_output.htm.md)

=== ARTICLE: connect_resources_assets_cancel.htm ===
---
page_id: connect_resources_assets_cancel.htm
title: Asset Cancellation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_assets_cancel.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset Cancellation (POST)

Initiate and execute the cancellation of an asset.

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the InitiateCancellation API permission set.

        
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/assets/actions/cancel
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/assets/actions/cancel
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "cancellationDate": "2023-10-04T00:00:00",
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to cancel. All assets in a request must belong to the same price book. | Required | 62.0 |
| `cancellation​Date` | String | Effective date of the cancellation. | Required | 62.0 |
| `contract​Id` | String | ID of the Contract record that you want to sync with the cancellation quote. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the cancellation quote. | Optional | 62.0 |
| `output​RecordId` | String | ID of the quote or order that you want to cancel. | Optional | 62.0 |
| `output​RecordType` | String | Type of cancellation record that you want to create. | Required | 62.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Cancellation](./connect_responses_cancel_output.htm.md)

=== ARTICLE: connect_resources_assets_renew.htm ===
---
page_id: connect_resources_assets_renew.htm
title: Asset Renewal (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_assets_renew.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset Renewal (POST)

Initiate and execute the renewal of an asset.

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the InitiateRenewal API permission set.

        
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/assets/actions/renew
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/assets/actions/renew
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "assetIds": [
    "02iSG0000003NMhYAM",
    "02iSG0000006DvSYAU"
  ],
  "contractId": "800SG00000CFpepYAD",
  "opportunityId": "006SG000004W5tVYAS",
  "outputRecordId": "801SG00000DX1jWYAT",
  "outputRecordType": "Quote",
  "renewalEndDate": "2024-10-03T23:59:59",
  "renewalStartDate": "2023-10-04T00:00:00"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assetIds` | String[] | IDs of the assets that you want to renew. | Required | 62.0 |
| `contractId` | String | ID of the Contract record that you want to sync with the renewal of the Quote or Order record. | Optional | 62.0 |
| `opportunity​Id` | String | ID of the Opportunity record that you want to sync with the renewal quote. | Optional | 62.0 |
| `output​RecordId` | String | ID of the Quote or Order record that you want to renew. | Optional | 62.0 |
| `output​RecordType` | String | Type of renewal record that you want to create. | Required | 62.0 |
| `renewal​EndDate` | String | End date of the renewal process for the assets. | Optional | 62.0 |
| `renewal​StartDate` | String | Start date of the renewal process for the assets. Required for early asset renewals and renewing expired assets, using today’s date or a future date. | Optional | 62.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Renewal](./connect_responses_renew_output.htm.md)

=== ARTICLE: connect_resources_clone_sales_transaction.htm ===
---
page_id: connect_resources_clone_sales_transaction.htm
title: Clone Sales Transaction (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_clone_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Clone Sales Transaction (POST)

Create a clone of a sales transaction, such as a quote or an order.
      You can also clone a quote line item or an order item record with its related records and
      configurations.

    

This API supports the cloning of records for these objects.

        
- Quote

        
- QuoteLineItem

        
- OrderItem

        
- QuoteLineGroup

        
- Order

        
- OrderItemGroup

      

You can clone all items in a quote line group or order item group when the record to
        clone is a quote line group or an order item group record.

      
        
          

**Resource**

          
: 
            

```
/connect/rev/sales-transaction/actions/clone
```

          

        
        
          

**Resource example**

          
: 
            

```
https://<varname>yourInstance</varname>.salesforce.com/services/data/v64.0/connect/rev/sales-transaction/actions/clone
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: This is a sample request to clone a record within a sales transaction.

          
: 

```
{
  "recordIds": ["0QLxx0000004CBYGA2"],
  "salesTransactionId": "0Q0xx0000004CE0CAM"
}
```

This is a sample request to clone all line items in a ramped group within a
            sales transaction.

```
{
  "recordIds": ["0QLxx0000004CBYGA2"],
  "salesTransactionId": "0Q0xx0000004CE0CAM",
  "options": {
    "lineScope": "AllLines"
  }
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `recordIds` | String[] | ID of the record to be cloned. You can specify a single record ID only. | Required | 64.0 |
| `salesTransactionId` | String | ID of the sales transaction related to the record IDs to clone. | Required | 64.0 |
| `options` | [Clone Options Input](./connect_requests_clone_options_input.htm.md) | Specifies options to clone a ramp segment within a sales transaction. You can clone only the last ramp segment. | Optional | 65.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: 
            [Clone Sales
              Transaction](./connect_responses_clone_sales_transaction_output.htm.md)

=== ARTICLE: connect_resources_cpq_instant_pricing.htm ===
---
page_id: connect_resources_cpq_instant_pricing.htm
title: Instant Pricing (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_cpq_instant_pricing.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Instant Pricing (POST)

Fetch instant pricing data on the quote or order line data grid and
      associated summary component. This API offers capabilities to either create a context or
      update the existing one based on the provided context ID.

    
      

You can also group quote line items or order items based on location, work types, or
        departments, if groups are enabled for your org. Groups provide a visualization of the
        products to view large quotes.

    

    
      
        
          

**Resource**

          
: 
            

```
/industries/cpq/quotes/actions/get-instant-price
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/industries/cpq/quotes/actions/get-instant-price
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

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
  "correlationId": "7847127122596",
  "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
  "records": [
    {
      "referenceId": "0Q0xx0000004DOSCA2",
      "record": {
        "attributes": {
          "type": "Quote",
          "method": "POST"
        },
        "Name": "Test Quote Proration Pricing",
        "OpportunityId": "006xx000001a4ISAAY",
        "Pricebook2Id": "01sxx0000005ptpAAA"
      }
    },
    {
      "referenceId": "refQuoteLine",
      "record": {
        "attributes": {
          "type": "QuoteLineItem",
          "method": "POST"
        },
        "QuoteId": "0Q0xx0000004DOSCA2",
        "PricebookEntryId": "01uxx0000008zHmAAI",
        "Product2Id": "01txx0000006jmWAAQ",
        "Quantity": 2,
        "UnitPrice": 25,
        "StartDate": "2022-09-28",
        "EndDate": "2028-09-27",
        "PeriodBoundary": "ANNIVERSARY",
        "BillingFrequency": "ANNUAL"
      }
    }
  ]
}
```

          

          
: This example shows a sample request to specify grouping of lines based on
                        criteria.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004DOSCA2",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "0QLxx0000004F3gGAE",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 5
            }
        }, {
            "referenceId": "0QLxx0000004F3hGAE",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupBy",
                    "criteria": {
                        "Quantity": 5
                    }
                },
                "Name": "record"
            }
        }, {
            "referenceId": "GroupId2",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupBy",
                    "criteria": {
                        "Quantity": 2
                    }
                },
                "Name": "record1",
            }
        }
    ]
}
```

          
: This example shows a sample request for the initial grouping of the quote with the
                        quote lines assigned to the first
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST",
                    "action": "GroupAll" 
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to ungroup a quote but retain the quote
                        lines.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
         {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2,
                "QuoteLineGroupId": null
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "DELETE",
                    "action": "Ungroup"
                }
            }
        }
    ]
}
```

          
: This example shows a sample request to create a new
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "POST"
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to delete a
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "GroupId1",
            "record": {
                "attributes": {
                    "type": "QuoteLineGroup",
                    "method": "DELETE",
                    "action": "DeleteGroup"
                },
                "Name": "sample"
            }
        }
    ]
}
```

          
: This example shows a sample request to move a
                        group.

```
{
    "contextId": "0000000b28op21g00281751271041790cc1e5686282849a387dd3c59b310418b",
    "correlationId": "7847127122596",
    "records": [
        {
            "referenceId": "0Q0xx0000004CAgCAM",
            "record": {
                "attributes": {
                    "type": "Quote",
                    "method": "PUT"
                }
            }
        },
        {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PUT"
                },
                "Quantity": 2
                "QuoteLineGroupId": "{@GroupId2}"
            }
        },
    ]
}
```

        

**Properties**

: 

                                        

                                        

                                        

                                        

                                        

                                    

                                        

                                        

                                        

                                        

                                        

                                    

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID generated by the context service. If you don’t specify a context ID, a new context is created. | Optional | 59.0 |
| `correlationId` | String | Client-generated ID for tracking multiple related API requests. | Optional | 59.0 |
| `records` | [Object with Reference Input](./connect_requests_object_with_reference_input.htm.md)[] | List of pricing data to be fetched. | Required | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Instant Pricing](./connect_responses_get_instant_pricing_output.htm.md)

=== ARTICLE: connect_resources_create_promotions.htm ===
---
page_id: connect_resources_create_promotions.htm
title: Create Promotions (GET, POST, PUT)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_promotions.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Promotions (GET, POST, PUT)

Get rewards based on a product selling model
    template.

    
      
        
          

**Resource**

          
: 
            

```
/global-promotions-management/promotions
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/global-promotions-management/promotions
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: GET, POST, PUT

        
        
          

**Request and response body**

          
: This example shows a sample request to create a
            promotion.

```
{
  "promotionDetails": {
    "additionalFieldValues": {
      "attributes": {}
    },
    "displayName": "10% off on Cisco Router",
    "isAutomatic": true,
    "isEmailActivated": false,
    "name": "10% off on Cisco Router",
    "promotionEligibility": {
      "eligibleCustomerEvents": {},
      "eligibleEnrollmentPeriod": {
        "isEnrollmentRequired": false
      },
      "eligibleProducts": [
        {
          "id": "01txx0000006igmAAA",
          "name": "Cisco Router",
          "productType": "SimpleProduct"
        }
      ]
    },
    "promotionLimits": {},
    "ruleLibrary": {
      "id": "9Qsxx0000004H76CAE",
      "name": "RLMSales"
    },
    "startDateTime": "2025-11-01T08:43:00.000Z"
  },
  "rules": [
    {
      "eventConfiguration": [],
      "journalSubType": null,
      "journalSubTypeName": null,
      "journalType": "Customer Purchase",
      "priority": 10,
      "rewardConfiguration": [
        {
          "scope": "SimpleProduct",
          "scopeDetails": [
            {
              "name": "Cisco Router",
              "id": "01txx0000006igmAAA"
            }
          ],
          "doNotDefineRewards": false,
          "rewardDetailsList": [
            {
              "productSellingModel": {
                "name": "Monthly",
                "id": "0jPxx0000000001EAA"
              },
              "discountType": "PercentageOff",
              "discountValue": 10,
              "termBasedRewards": {
                "psmTenure": {
                  "tenure": "SpecificTerm",
                  "operator": "Equals",
                  "value": 12
                },
                "rewardDuration": {
                  "tenure": "SpecificTerm",
                  "value": 3
                }
              }
            }
          ],
          "childProducts": [],
          "type": "PSMDiscount",
          "isPrimaryReward": false
        }
      ],
      "ruleName": "rule",
      "templateName": "GetRewardsBasedOnSellingModel"
    }
  ]
}
```

          
: See [Promotions Creation API](https://developer.salesforce.com/docs/atlas.en-us.264.0.loyalty.meta/loyalty/connect_resources_unified_promotions.htm)
            reference to get additional details of the request and response properties.

=== ARTICLE: connect_resources_create_ramp_deal.htm ===
---
page_id: connect_resources_create_ramp_deal.htm
title: Create Ramp Deal (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_ramp_deal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Ramp Deal (POST)

Create a ramp deal for a customer on a product. Sales reps can use
      ramp deals to provide yearly deals to a customer, resulting in long-term revenue and customer
      relationship. A customer can create, update, or view multiple segments of periods for their
      subscription term with different attributes for each segment.

    
This API request creates segments based on the specified input properties such as term, segment
        type, and trial details. The API response includes the context ID and the updated context
        object for the sales transaction. You must call the Place Sales Transaction API by
        specifying this context ID to apply the ramp deal updates. See [Place Sales Transaction
          API](./connect_resources_place_sales_transaction.htm.md).

#### Note

This API is applicable when you're working with line
          ramps. To work with ramp deals for groups, you must use the Place Sales Transaction API
          and specify the `groupRampActions` property.

    
      
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-create
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/sales-transaction-contexts/0QLxx0000004CfIGAU/actions/ramp-deal-create
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `resourceId` | String | ID of the quote line item, order item, or context. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "transactionId": "0Q0xx0000004C92CAE",
  "transactionLineId": "0QLxx0000004C9VGAU",
  "subscriptionTerm": 14,
  "subscriptionTermUnit": "MONTHS",
  "trialTerm": 45,
  "trialTermUnit": "DAYS",
  "segmentType": "YEARLY",
  "executionSettings": {
       "executePricing": true,
       "executeConfigRules": false
   }
}
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
| `execution​Settings` | [Execution Settings Input](./connect_requests_execution_settings_input.htm.md)[] | Settings to run the pricing or configuration rules. | Optional | 62.0 |
| `segment​Type` | String | Type of segment that the user wants to create. Valid values are: `FREE_TRIAL` `CUSTOM` `YEARLY` | Required | 62.0 |
| `subscription​Term` | Integer | Subscription length of the term-defined product. | Required | 62.0 |
| `subscription​TermUnit` | String | Unit of time for the subscription length. Valid value is: `MONTHS` | Required | 62.0 |
| `transaction​Id` | String | ID of the sales transaction that’s configured, such as quote or order. | Required | 62.0 |
| `transaction​LineId` | String | Quote line item ID or order item ID that the price ramp is created for. | Required | 62.0 |
| `trialTerm` | Integer | Length of the trial period, if any. | Optional | 62.0 |
| `trialTerm​Unit` | String | Unit of time for the trial period. Valid value is: `DAYS` | Optional. Required if `trialTerm` property is specified. | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Ramp Deal
              Service](./connect_responses_ramp_deal_service_output.htm.md)

=== ARTICLE: connect_resources_delete_ramp_deal.htm ===
---
page_id: connect_resources_delete_ramp_deal.htm
title: Delete Ramp Deal (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_delete_ramp_deal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Delete Ramp Deal (POST)

Delete a ramp deal to convert a ramped product to include a single
      quote line item or order item.

    
This API request deletes the segments related to the product. The API response includes the
        updated context with the context ID. You must call the Place Sales Transaction (POST) API by
        specifying this context ID to apply the ramp deal updates. See [Place Sales Transaction (POST)
          API](./connect_resources_place_sales_transaction.htm.md).

#### Note

This API is applicable when you're working with line
          ramps. To work with ramp deals for groups, you must use the Place Sales Transaction API
          and specify the `groupRampActions` property.

    
      
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-delete
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/sales-transaction-contexts/0QLxx0000004CfIGAU/actions/ramp-deal-delete
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `resourceId` | String | ID of the context. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "rampDealIds": [
    "0Q0xx0000004CDxCAM",
    "0QLxx0000004CSOGA2"
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `rampDeal​Ids` | String[] | Ramp identifier on the quote line item or order item. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Ramp Deal
              Service](./connect_responses_ramp_deal_service_output.htm.md)

=== ARTICLE: connect_resources_get_eligible_promotions.htm ===
---
page_id: connect_resources_get_eligible_promotions.htm
title: Get Eligible Promotions (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_eligible_promotions.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Eligible Promotions (POST)

Get eligible promotions for line items within a quote or an
      order.

    

This API accepts line item IDs and sales transaction ID as the input and then
        initializes the context by filtering on the specific line items.

    
      
        
          

**Resource**

          
: 
            

```
/revenue/transaction-management/sales-transactions/actions/get-eligible-promotions
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/transaction-management/sales-transactions/actions/get-eligible-promotions
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
  "salesTransactionId": "0Q0xx0000004EOECA2",
  "lineItemIds": [
    "0QLxx0000004E7eGAE",
    "0QLxx0000004GCeGAM",
    "0QLxx0000004E7gGAE"
  ]
}

```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `lineItemIds` | String[] | List of line item IDs to evaluate for promotions. The object type is auto-determined from the sales transaction ID. | Required | 66.0 |
| `salesTransactionId` | String | The sales transaction ID, such as an order ID or a quote ID, for the promotion evaluation. | Required | 66.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Get Eligible
              Promotions](./connect_responses_get_eligible_promotions_output.htm.md)

=== ARTICLE: connect_resources_initiate_downgrade.htm ===
---
page_id: connect_resources_initiate_downgrade.htm
title: Initiate Downgrade (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_initiate_downgrade.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Downgrade (POST)

Move to a lower-tier or lower-value product. The change is tracked as a
      downgrade request with linked asset actions and quote or order line linkage for reporting and
      auditing. This API creates an amendment quote and order with downgrade-specific order actions
      and quote action subtypes.

      

After assetization, the original asset receives an asset action with business category as
        Downgrade (or equivalent). This step indicates that the downgrade-from product and the new
        asset is created with an asset action (downgraded to), with relationships between the two.
        This step also enables sales reps to process downgrades and makes sure that downgrades are
        auditable and reportable separately from cancellations and new sales.

**Resource**

: 

```
/revenue/transaction-management/assets/actions/downgrade
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/transaction-management/assets/actions/downgrade
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
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "DOWNGRADE-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "downgradeRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2022-09-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to downgrade. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to downgrade. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the downgrade. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the downgrade. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the downgrade action. | Required | 66.0 |

          

        

**Response body for POST**

: [Initiate Downgrade Response](./connect_responses_initiate_downgrade_output.htm.md)

#### See Also

- [*Salesforce Help*: Swap, Upgrade, or Downgrade Assets](https://help.salesforce.com/s/articleView?id=ind.qocal_swap_upgrade_downgrade_amendments.htm&language=en_US)

=== ARTICLE: connect_resources_initiate_swap.htm ===
---
page_id: connect_resources_initiate_swap.htm
title: Initiate Swap (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_initiate_swap.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Swap (POST)

Exchange one product for another of equivalent or different value. The
      change is tracked as a swap request with linked asset actions and a net-zero order total where
      applicable. The API creates an amendment quote and order with order actions and quote action
      subtypes.

      

When the order is assetized, the source asset gets an asset action with business category
        as `Swap` (reduced quantity). The new asset is created
        with an asset action that identifies it as swapped in, with relationships that link the
        swapped-from and swapped-to assets. The swaps are auditable and reportable separately from
        cancellations and new sales. This API also supports use cases such as trading unused
        licenses for credits or moving spend between products while preserving contract intent.

**Resource**

: 

```
/revenue/transaction-management/assets/actions/swap
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/transaction-management/assets/actions/swap
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
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "SWAP-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "swapRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2022-09-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to swap. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to swap. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the swap. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the swap. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the swap action. | Required | 66.0 |

          

        

**Response body for POST**

: [Initiate Swap Response](./connect_responses_initiate_swap_output.htm.md)

#### See Also

- [*Salesforce Help*: Swap, Upgrade, or Downgrade Assets](https://help.salesforce.com/s/articleView?id=ind.qocal_swap_upgrade_downgrade_amendments.htm&language=en_US)

=== ARTICLE: connect_resources_initiate_upgrade.htm ===
---
page_id: connect_resources_initiate_upgrade.htm
title: Initiate Upgrade (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_initiate_upgrade.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Upgrade (POST)

Move a lower-tier product to a higher-tier product. The change is
      tracked as an upgrade request with linked asset actions and quote or order line linkage for
      reporting and auditing. This API creates an amendment quote and order with order actions and
      quote action subtypes.

      

The original asset receives an asset action with an `Upgrade` (or equivalent) business category. This step indicates that the
        upgrade-from product and the new asset is created with an asset action (upgraded to), with
        relationships between the two. This step also enables sales reps to process upgrades and
        makes sure that upgrades are distinguishable in reporting and analytics from cancellations
        plus new sales.

**Resource**

: 

```
/revenue/transaction-management/assets/actions/upgrade
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/transaction-management/assets/actions/upgrade
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
  "swapStartDate": "2025-12-01T00:00:00Z",
  "outputRecordType": "Quote",
  "swapGroups": {
    "groups": [
      {
        "referenceId": "UPGRADE-001",
        "outGroup": {
          "swapAssets": [
            {
              "assetId": "02ixx0000004HOAAA2",
              "quantity": 1
            }
          ]
        },
        "inGroup": {
          "graphId": "upgradeRequest",
          "records": [
            {
              "referenceId": "refQuoteLine0",
              "record": {
                "attributes": {
                  "type": "QuoteLineItem",
                  "method": "POST"
                },
                "Product2Id": "01txx0000006iVlAAI",
                "PricebookEntryId": "01uxx0000008ym4AAA",
                "UnitPrice": 1049,
                "Quantity": "1",
                "StartDate": "2026-03-22"
              }
            }
          ]
        }
      }
    ]
  }
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contractId` | String | ID of the contract record to upgrade. | Optional | 66.0 |
| `opportunityId` | String | ID of the opportunity record to upgrade. | Optional | 66.0 |
| `outputRecordType` | String | Record type of the output for the upgrade. | Required | 66.0 |
| `swapGroups` | [Swap Group](./connect_requests_swap_group.htm.md)[] | Groups that contain the asset details for the upgrade. | Required | 66.0 |
| `swapStartDate` | String | Amendment start date for the upgrade action. | Required | 66.0 |

          

**Response body for POST**

: [Initiate Upgrade Response](./connect_responses_initiate_upgrade_output.htm.md)

#### See Also

- [*Salesforce Help*: Swap, Upgrade, or Downgrade Assets](https://help.salesforce.com/s/articleView?id=ind.qocal_swap_upgrade_downgrade_amendments.htm&language=en_US)

=== ARTICLE: connect_resources_place_order.htm ===
---
page_id: connect_resources_place_order.htm
title: Place Order (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_place_order.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Order (POST)

Place orders with integrated pricing, configuration, and validation,
      and manage them throughout their entire lifecycle. Additionally, update an order or insert
      order items.

    

You can also group order items based on location, work types, or departments, if
        groups are enabled for your org. Groups provide a visualization of the products to view
        large quotes.

This API supports a maximum of 300 transaction line items.

      

#### Note

This API has been deprecated as of API version 63.0. In API version 63.0 and later, use
        the new [Place Sales Transaction](./connect_resources_place_sales_transaction.htm.md)
        API.

    
      
        
          

**Special Access Rules**

          
: You need the PlaceOrder API permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/sales-orders/actions/place
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/sales-orders/actions/place
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
  "pricingPref": "System",
  "configurationInput": "RunAndAllowErrors",
  "configurationOptions": {
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },
  "graph": {
    "graphId": "graphId",
    "records": [
      {
        "referenceId": "refOrder",
        "record": {
          "attributes": {
            "type": "Order",
            "method": "POST",
            "Id": "POST"
          }
        }
      },
      {
         "referenceId":"refOrderItem",
         "record":{
         "attributes":{
             "type":"OrderItem",
             "method":"POST"
            },
            "OrderId":"@{refOrder.id}",
            "OrderActionId":"@{refOrderAction.id}",
            "ListPrice":"144.99",
            "Quantity":3,
            "PricebookEntryId":"01uxx0000008yXPAAY",
            "Product2Id":"01txx0000006i2UAAQ",
            "UnitPrice":"199.49"
       }
      }
    ]
  }
}
```

          

          
: This example shows a sample request to define grouping of order
            items.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "801xx000003GZ9bAAG"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST"
                    },
                    "Name": "New Group",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to ungroup order
            items.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "DELETE",
                        "id": "refOlg1",
                        "action": "Ungroup"
                    }
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to create a new
            group.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "refOlg",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST"
                    },
                    "Name": "New Group",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
    "contextId": "",
    "correlationId": "",
    "records": [
        {
            "referenceId": "refOrder",
            "record": {
                "attributes": {
                    "type": "Order",
                    "method": "PATCH",
                    "id": "refOrder"
                }
            }
        },
        {
            "referenceId": "refOlg",
            "record": {
                "attributes": {
                    "type": "OrderItemGroup",
                    "method": "DELETE",
                    "id": "refOlg",
                    "action": "DeleteGroup"
                }
            }
        }
    ]
}
```

          
: This example shows a sample request to group order items based on
            criteria.

```
{
    "pricingPref": "system",
    "graph": {
        "graphId": "placeOrder",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "refOrder"
                    }
                }
            },
            {
                "referenceId": "g0",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": null
                        }
                    },
                    "Name": "Billing Frequency: ",
                    "OrderId": "@{refOrder.id}"
                }
            },
            {
                "referenceId": "g1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": "Monthly"
                        }
                    },
                    "Name": "Billing Frequency: Monthly",
                    "OrderId": "@{refOrder.id}"
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
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    
                    

                    

                    

                  

                  
                    

                    

                    
- 
- 
- 

                    

                    

                  

                

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​RatesPref` | String | Rate card entries defined in the catalog that must be fetched for order items with usage-based pricing during the order creation process. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for order items during the order creation process. `Skip`—Skips the retrieval of rate card entries for order items during the order creation process. The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 62.0 |
| `configuration​Input` | String | Configuration input for the place order process. Valid values are: `RunAndAllowErrors`—Specifies to run the configuration and to proceed order ingestion upon encountering any configuration errors. `RunAndBlockErrors`—Specifies to run configuration and to block order ingestion upon encountering any configuration errors. `Skip`—Specifies to skip configuration. The default value is `RunAndBlockErrors`. | Optional | 60.0 |
| `configuration​Options` | [Configuration Options Input​](./connect_requests_configuration_options_input.htm.md)[] | Configuration options during the ingestion process. | Optional | 60.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph of the order payload to be ingested. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. | Required | 60.0 |
| `pricing​Pref` | String | Pricing preference during the create order process. Valid values are: `Force`—Specifies to force pricing during the order ingestion process. `Skip`—Specifies to skip pricing during the order ingestion process. `System`—Specifies the system to determine whether a pricing calculation is required. The default value is `System`. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Place Order](./connect_responses_place_order_output.htm.md)

=== ARTICLE: connect_resources_place_quote.htm ===
---
page_id: connect_resources_place_quote.htm
title: Place Quote (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_place_quote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Quote (POST)

Create a quote to discover and price products and services.
      Additionally, insert, update, or delete a quote line item.

    

You can also group quote line items based on location, work types, or departments,
        if groups are enabled for your org. Groups provide a visualization of the products to view
        large quotes.

This API supports a maximum of 300 transaction line items.

      

#### Note

This API has been deprecated as of API version 63.0. In API version 63.0 and later, use
        the new [Place Sales Transaction](./connect_resources_place_sales_transaction.htm.md)
        API.

    
      
        
          

**Special Access Rules**

          
: You need the Create on Quotes user permission to create quotes.

        
        
          

**Resource**

          
: 
            

```
/commerce/quotes/actions/place
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/quotes/actions/place
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: This example shows a sample request to create a
            quote.

```
{
  "pricingPref": "System",
  "configurationInput": "RunAndAllowErrors",
  "configurationOptions": {
    "validateProductCatalog": true,
    "validateAmendRenewCancel": true,
    "executeConfigurationRules": true,
    "addDefaultConfiguration": true
  },  "graph": {
    "graphId": "createQuote",
    "records": [{ 
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "POST"
          },
          "opportunityId": "---",
          "quoteProp1": "value1",
          "quoteProp2": "value2"
        }
      },
      {
        "referenceId": "refQuoteLineItem1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteLineItemProp1": "value1",
          "QuoteLineItemProp2": "value2"
        }
      },
      {
      "referenceId": "refQuoteLineItemAttribute",
      "record": {
        "attributes": {
              "type": "QuoteLineItemAttribute",
              "method": "POST"
       },
       "QuoteLineItemId": "@{refQuoteLineItem1.id}",
       "AttributeDefinitionId": "0tjxx0000000001AAA"
      }
}
    ]
  }
}
```

          
: This example shows a sample request to insert, update, or delete a quote line
            item.

```
{
  "pricingPref": "System",
  "configurationInput": "skip",
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004E2mCAE"
          },
          "Name": "Quote_Acme"
        }
      },
      {
        "referenceId": "refQuoteLineItemToCreate1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "0Q0xx0000004E2mCAE",
          "PricebookEntryId": "01uxx0000008yXPAAY",
          "Product2Id": "01txx0000006i2UAAQ",
          "Quantity": 2.0,
          "UnitPrice": 800.0,
          "PeriodBoundary": "Anniversary",
          "BillingFrequency": "Monthly",
          "StartDate": "2024-03-11"
        }
      },
      {
        "referenceId": "refQuoteLineItemToPatch2",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "0Q0xx0000004E2mCAE"
          },
          "Quantity": 2.0,
          "UnitPrice": 600.0
        }
      },
      {
        "referenceId": "refQuoteLineItemToDelete3",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "DELETE",
            "id": "0Q0xx0000004E2mYLK"
          }
        }
      }
    ]
  }
}
```

          
: This example shows a sample request to define grouping of quote line
            items.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "groupLines",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST",
                  "action": "GroupBy",
                  "criteria": {
                    "Quantity": 1
                  }
               },
               "Name": "From Place Quote API Group",
               "QuoteId": "@{refQuote.id}"
            }
         },
         {
            "referenceId": "refQuoteItem1",
            "record": {
               "attributes": {
                  "type": "QuoteLineItem",
                  "method": "PATCH",
                  "id":"0QLxx0000004DJcGAM"
               },
               "QuoteLineGroupId": "@{refQlg1.id}",
               "Quantity": 1
            }
         }
      ]
   }
}
```

          
: This example shows a sample request for the initial grouping of the quote with the
            quote lines assigned to the first
            group.

```
{
  "pricingPref": "Force",
  "graph": {
    "graphId": "test",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CAmCAM"
          }
        }
      },
      {
        "referenceId": "refQlg1",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "POST",
            "action": "GroupAll"
          },
          "Name": "From PQ API Group",
          "QuoteId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This example shows a sample request to ungroup a quote but retain the quote
            lines.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote", 
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "{GroupId}",
                  "action": "Ungroup"
               }
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to create a new
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST"
               },
               "Name": "From PQ API Group",
               "QuoteId": "@{refQuote.id}"
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From Place Quote API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "{GroupId}",
                  "action": "DeleteGroup"
               }
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to move a
            group.

```
{
   "pricingPref": "Force",
   "configurationInput": "skip",
   "graph": {
      "graphId": "test",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "From PlaceQuote Api"
            }
         },
        {
            "referenceId": "0QLxx0000004CBYGA2",
            "record": {
                "attributes": {
                    "type": "QuoteLineItem",
                    "method": "PATCH"
                    "id": "0QLxx0000004CBYGA2"
                },
                "Quantity": 2,
                "QuoteLineGroupId": "@{GroupId2}"
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
- 
- 

                    

                    

                  

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​RatesPref` | String | Rate card entries defined in the catalog that must be fetched for quote line items with usage-based pricing during the quote creation process. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for quote line items during the quote creation process. `Skip`—Skips the retrieval of rate card entries for quote line items during the quote creation process. The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 62.0 |
| `configuration​Input` | String | Configuration input for the place quote process. Valid values are: `RunAndAllowErrors` `RunAndBlockErrors` `Skip` The default value is `RunAndBlockErrors`. | Optional | 60.0 |
| `configuration​Options` | [Configuration Options Input](./connect_requests_configuration_options_input.htm.md) | Configuration options during the ingestion process. | Optional | 60.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph representing the quote structure. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. | Required | 60.0 |
| `pricing​Pref` | String | Pricing preference during the quote process. Valid values are: `Force` `Skip` `System` The default value is `System`. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Place Quote](./connect_responses_place_quote_output.htm.md)

=== ARTICLE: connect_resources_place_sales_transaction.htm ===
---
page_id: connect_resources_place_sales_transaction.htm
title: Place Sales Transaction (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_place_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Sales Transaction (POST)

Create a sales transaction, such as an order or a quote, with
      integrated pricing and configuration. Also, update an order or a quote, and insert and delete
      order or quote line items to calculate the estimated tax.

    
      

You can also group order or quote line items based on location, work types, or departments,
        if groups are enabled for your org. Groups provide a visualization of the products to view
        large quotes.

      

Keep these considerations in mind when you use this API.

      
        
- You can add up to 1000 quote line items for a quote, and 1000 order products for an
          order. For complex flows that involve a large volume of records, make sure that the number
          of line items that are sent to this API are within this limit.

        
- A quote can have up to 3000 quote line item attributes, and an order can have up to 3000
          order line item attributes.

        
- This API doesn’t support creation of amendment, renewal, or cancellation quote or order.
          Use the amendment, renewal, or cancellation APIs or invocable actions.

        
- Create or update quote lines with an associated group ID if you plan to use the sales
          transaction line editor after the API request.

        
- Bundle quantity handling depends on the AssociatedQuantScaleMethod field in the payload.
          If AssociatedQuantScaleMethod field value is `Proportional`, child quantity is `parent ×
            child`. For example, 10 × 2 = 20. Without this value, the API can enforce
          quantity or cardinality restrictions and return validation errors. Include it explicitly
          for predictable results. See [OrderItemRelationship](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_orderitemrelationship.htm) for details of
          AssociatedQuantScaleMethod field.

        
- For custom objects at level 2 or deeper in the sales transaction hierarchy, configure
          context mapping so that `parentReference` maps to the
          custom object’s immediate parent field. For custom object `child_one` under QuoteLineItem object, map `parentReference` to quote_line_item_c in QuoteEntitiesMapping object. Without
          this mapping, this API fails as delta processing can’t reconcile all input records.

        
- This API saves and commits the quote header first, then processes configuration, pricing,
          and persistence for components, such as line items and groups. If a later step fails, the
          header isn’t rolled back.

      

      
        
          

**Resource**

          
: 
            

```
/connect/rev/sales-transaction/actions/place
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/rev/sales-transaction/actions/place
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: This is a sample request to create a sales transaction for a quote. This example also
            skips tax calculation by specifying a value for the optional `taxPref` property.

          
: 
            

```
{
  "pricingPref": "System",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "taxPref": "Skip",
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "createQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "POST",
            "type": "Quote"
          },
          "Name": "Quote_Acme",
          "Pricebook2Id": "01sDU000000JvhbYAC"
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "Product2Id": "01tDU000000F7b8YAC",
          "PricebookEntryId": "01uDU000000fxt2YAA",
          "UnitPrice": 100,
          "Quantity": "1",
          "StartDate": "2024-10-29",
          "EndDate": "2025-03-01",
          "PeriodBoundary": "Anniversary"
        }
      },
      {
        "referenceId": "refQuoteLine1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "Product2Id": "01tLT00000AA2M9YAL",
          "PricebookEntryId": "01uLT000007PTafYAG",
          "Quantity": "1"
        }
      },
      {
        "referenceId": "refQuoteLineItemAttribute1",
        "record": {
          "attributes": {
            "type": "QuoteLineItemAttribute",
            "method": "POST"
          },
          "QuoteLineItemId": "@{refQuoteLine0.id}",
          "AttributeDefinitionId": "0tjRT0000000XbtYAE",
          "AttributeValue": "True"
        }
      },
      {
        "referenceId": "refQuoteLineRelationship1",
        "record": {
          "attributes": {
            "type": "QuoteLineRelationship",
            "method": "POST"
          },
          "ProductRelationshipTypeId": "0yoLT000000wHq6YAE",
          "ProductRelatedComponentId": "0dSLT00000076IP2AY",
          "MainQuoteLineId": "@{refQuoteLine0.id}",
          "AssociatedQuoteLineId": "@{refQuoteLine1.id}",
          "AssociatedQuoteLinePricing": "NotIncludedInBundlePrice"
        }
      }
    ]
  }
}
```

          

          
: This sample request assigns a TransactionProcessingType record to a quote without any
            additional preferences. In this example, the TransactionType value for a record is set
            to a TransactionProcessingType record. See [TransactionProcessingType](./tooling_api_objects_transactionprocessingtype.htm.md) tooling
            object for more details.

```
{
  "pricingPref": "Force",
  "contextDetails": {
    "contextId": "f1c9e3e1c335f7959a88de09d3a867cc2b95e08709b99de8e2edeb8f5039e8ed",
    "scope": "Session"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "POST"
          },
          "OpportunityId": "006xx000001a2oWAAQ",
          "PriceBook2Id": "01sxx0000005ptpAAA",
          "TransactionType": "SkipPricingAndRunTax",
          "Name": "Quote_No_Tax_System"
        }
      },
      {
        "referenceId": "refQLI1",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "POST"
          },
          "QuoteId": "@{refQuote.id}",
          "UnitPrice": 49.99,
          "Product2Id": "01txx0000006i2aAAA",
          "PricebookEntryId": "01uxx0000008yX0AAI",
          "Quantity": 10
        }
      }
    ]
  }
}
```

          
: This is a sample request to insert, update, or delete a quote line
            item.

```
{
  {
  "pricingPref": "System",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "PATCH",
            "type": "Quote",
            "id": "801xx000003GZ9bAAG"
          }
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "402xx000003KY5vJGH"
          },
          "Quantity": "5"
        }
      }
    ]
  }
}
```

          
: This is a sample request to define grouping of quote line
            items.

```
{
  "pricingPref": "Force",
  "catalogRatesPref": "Skip",
  "configurationPref": {
    "configurationMethod": "Skip",
    "configurationOptions": {
      "validateProductCatalog": true,
      "validateAmendRenewCancel": true,
      "executeConfigurationRules": true,
      "addDefaultConfiguration": true
    }
  },
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
  },
  "graph": {
    "graphId": "groupQuoteLines",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "method": "PATCH",
            "type": "Quote",
            "id": "801xx000003GZ9bAAG"
          }
        }
      },
      {
        "referenceId": "refQuoteLine0",
        "record": {
          "attributes": {
            "type": "QuoteLineItem",
            "method": "PATCH",
            "id": "402xx000003KY5vJGH"
          },
          "QuoteLineGroupId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This is s a sample request for the initial grouping of the quote with all the quote
            lines assigned to the first
            group.

```
{
  "pricingPref": "Force",
  "catalogRatesPref": "Skip",
  "graph": {
    "graphId": "groupQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004CAmCAM"
          }
        }
      },
      {
        "referenceId": "refQlg1",
        "record": {
          "attributes": {
            "type": "QuoteLineGroup",
            "method": "POST",
            "action": "GroupAll"
          },
          "Name": "From PST API Group",
          "QuoteId": "@{refQuote.id}"
        }
      }
    ]
  }
}
```

          
: This is a sample request to ungroup a quote but retain the quote
            lines.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "ungroupQuote",
      "records": [
         {
            "referenceId": "refQuote", 
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "402xx000003KY5vJGH",
                  "action": "Ungroup"
               }
            }
         }
      ]
   }
}
```

          
: This is a sample request to create a new
            group.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "createGroup",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "POST"
               },
               "Name": "From PQ API Group",
               "QuoteId": "@{refQuote.id}"
            }
         }
      ]
   }
}
```

          
: This example shows a sample request to delete a
            group.

```
{
   "catalogRatesPref": "Skip",
   "pricingPref": "Force",
   "graph": {
      "graphId": "deleteGroup",
      "records": [
         {
            "referenceId": "refQuote",
            "record": {
               "attributes": {
                  "type": "Quote",
                  "method": "PATCH",
                  "id":"0Q0xx0000004C99CAE"
               },
               "Name": "Grouped Quote with PST API"
            }
         },
         {
            "referenceId": "refQlg1",
            "record": {
               "attributes": {
                  "type": "QuoteLineGroup",
                  "method": "DELETE",
                  "id": "402xx000003KY5vJGH",
                  "action": "DeleteGroup"
               }
            }
         }
      ]
   }
}
```

          
: This is a sample request to group order items based on
            criteria.

```
{
    "catalogRatesPref": "Skip",
    "pricingPref": "Force",
    "graph": {
        "graphId": "groupOrderItems",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "0Q0xx0000004C99CAE"
                    }
                }
            },
            {
                "referenceId": "refOlg1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": null
                        }
                    },
                    "Name": "Billing Frequency: ",
                    "OrderId": "@{refOrder.id}"
                }
            },
            {
                "referenceId": "g1",
                "record": {
                    "attributes": {
                        "type": "OrderItemGroup",
                        "method": "POST",
                        "action": "GroupBy",
                        "criteria": {
                            "BillingFrequency2": "Monthly"
                        }
                    },
                    "Name": "Billing Frequency: Monthly",
                    "OrderId": "@{refOrder.id}"
                }
            }
        ]
    }
}
```

          
: This is a sample request to save changes to a ramp deal by using context ID. The
            context ID is returned by the Ramp Deal APIs. See [Create Ramp Deal
            (POST)](./connect_resources_create_ramp_deal.htm.md).

```
{
  "pricingPref": "Force",
  "contextDetails": {
    "contextId": "f1c9e3e1c335f7959a88de09d3a867cc2b95e08709b99de8e2edeb8f5039e8ed",
    "scope": "Session"
  },
  "graph": {
    "graphId": "updateQuote",
    "records": [
      {
        "referenceId": "refQuote",
        "record": {
          "attributes": {
            "type": "Quote",
            "method": "PATCH",
            "id": "0Q0xx0000004DQ4CAM"
          }
        }
      }
    ]
  }
}
```

          
: To see examples that specify actions to create ramp deals for groups, see [Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md).

          
          
: To see examples that apply to usage-based products, see [Usage-Based Product Input](./connect_requests_usage_based_product_input.htm.md).

        
        
          

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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalogRates​Pref` | String | Rate card entries defined in the catalog that must be fetched for sales items with usage-based pricing during the creation of the sales transaction. Valid values are: `Fetch`—Retrieves the rate card entries defined in the catalog for sales items during the creation of the sales transaction. `Skip`—Skips the retrieval of rate card entries for sales items during the creation of the sales transaction.The default value is `Skip`. This property is available when the Usage-Based Selling feature is enabled. | Optional | 63.0 |
| `configuration​Pref` | [Configurator Preference Input](./connect_requests_configurator_preference_input.htm.md) | Configuration preference during the quote process. These preferences ensure that quotes are defined as per the requirement. | Optional | 63.0 |
| `contextDetails` | [Context Input](./connect_requests_context_info_input.htm.md) | Context details that are created for a sales transaction. | Required if the `graph` property isn’t specified. | 63.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph of the sales transaction to be ingested. You can perform create, update, or delete operations on objects from the Sales Transaction context definition by using this property. Additionally, perform create, update, or delete operations on custom objects and fields in your extended context definition. To create custom objects that are at the grandchildren level from a line item, you must create the hierarchy of objects until the grandchild object in the same request. | Required if the `contextDetails` property isn’t specified. | 63.0 |
| `groupRampAction` | String | Specifies the action ‌that you want to perform on group ramp segments. You can also convert a non-ramped group into a ramped group. Valid values are: `AddProducts`—Adds rampable products to group ramp segments. `DeleteProducts`—Deletes ramped products. `EditGroup`—Converts a non-ramped group into a group ramp segment, or edit group ramp segment attributes such as name and description, except the start and end dates. `EditRampSchedule`—Edits details of the group ramp segments, including start and end dates. `DeleteSegment`—Deletes the first or last segment in a group ramp schedule. `ConvertToNonRampedGroup`—Converts the first or last group ramp segment into a non-ramped group. To add or delete ramped line items from multiple group ramp segments, specify the applicable values in the `graph` property. See [Group Ramp Action Input](./connect_requests_group_ramp_action_input.htm.md) to refer to examples. | Optional | 65.0 |
| `pricingPref` | String | Pricing preference during the creation of a sales transaction. Valid values are: `Force`—Enforces pricing during the creation of sales transactions. `Skip`—Skips pricing during the creation of sales transactions. `System`—Determines whether a pricing calculation is required. The default value is `System`. | Optional | 63.0 |
| `taxPref` | String | Specifies whether to execute or skip the tax calculation step for each sales transaction record. Valid value is `Skip`. If you don't specify this value, then tax calculation request is performed by default. | Optional | 65.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Place Sales
              Transaction](./connect_responses_place_sales_transaction_output.htm.md)

=== ARTICLE: connect_resources_place_supplemental_transaction.htm ===
---
page_id: connect_resources_place_supplemental_transaction.htm
title: Place Supplemental Transaction (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_place_supplemental_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Supplemental Transaction (POST)

Create a supplemental order or change orders after they are submitted
      for processing, such as during the fulfillment process.

    
      

Keep these considerations in mind when you use this API.

      
        
- The original order must not be assetized.

        
- If Billing is enabled and configured for the order, verify that the original order
          hasn't been billed.

        
- If Dynamic Revenue Orchestration (DRO) is enabled and configured for the order, ensure
          the original order hasn't reached the point of no return milestone. If point of no return
          milestone hasn't been reached, the fulfillment plan is frozen.

      

    

**Resource**

: 

```
/connect/rev/sales-transaction/actions/place-supplemental-transaction
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/rev/sales-transaction/actions/place-supplemental-transaction
```

**Available version**

: 64.0

**HTTP methods**

: POST

**Request body for POST**

: 

**JSON example**

                    
: This sample creates a supplemental order, which is a clone of the original
                        order. The supplemental order is related to the original
                        order.

```
{
  "relatedSalesTransactionId": "801S70000001VKgIAM"
}
```

: This sample overrides a field value of an order line item to supplement the order item with ID
                        value as `802SG000003vZ15YAE`.

```
{
    "relatedSalesTransactionId": "801S70000001VKgIAM",
    "pricingPref": "System",
    "supplementalGraph": {
        "graphId": "1",
        "records": [
            {
                "referenceId": "refOrder",
                "record": {
                    "attributes": {
                        "type": "Order",
                        "method": "PATCH",
                        "id": "801S70000001VKgIAM"
                    },
                    "EffectiveDate": "2025-03-01",
                    "QuoteId": "0Q0xx0000004DQ4CAM"
                }
            },
            {
                "referenceId": "refOrderItem",
                "record": {
                    "attributes": {
                        "type": "OrderItem",
                        "method": "PATCH",
                        "id": "802SG000003vZ15YAE"
                    },
                    "QuoteLineItemId": "0Q0xx0000004E2mYLK"
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
| `pricingPref` | String | Pricing preference for this supplemental transaction or order ingestion process. Valid values are: `Force`—Enforces pricing during the creation of sales transactions. `Skip`—Skips pricing during the creation of sales transactions. `System`—Determines whether a pricing calculation is required. If `pricingPref` value is defined as either `Force` or `System`, the supplemental order can have a different pricing from the original order. | Optional | 64.0 |
| `relatedSales​TransactionId` | String | Related or the original sales transaction upon which a supplemental transaction is created. | Required | 64.0 |
| `supplemental​Graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | The sObject graph that represents a payload with the additional changes to be ingested. The attribute's HTTP method must be PATCH. The attribute ID must be the ID of the original order or order item that you want to supplement. | Optional | 64.0 |

**Response body for POST**

: [Supplemental
              Transaction](./connect_responses_place_supplemental_transaction_output.htm.md)

=== ARTICLE: connect_resources_read_sales_transaction.htm ===
---
page_id: connect_resources_read_sales_transaction.htm
title: Read Sales Transaction (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_read_sales_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Read Sales Transaction (POST)

Retrieve sales transaction data efficiently from an initialized or a
      hydrated context.

**Resource**

: 

```
/connect/revenue/transaction-management/sales-transactions/actions/read
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue/transaction-management/sales-transactions/actions/read
```

**Available version**

: 65.0

**HTTP methods**

: POST

        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "contextId": "008d27d7-e004-4906-a949-ee7d7c323c77",
  "queryTags": [
    "Quote",
    "QuoteLineItem",
    "Product"
  ],
  "sobjectFieldMap": {
    "Quote": [],
    "QuoteLineItem": [
      "Quantity",
      "Product2Id"
    ]
  },
  "filters": [
    {
      "sObjectName": "Quote",
      "fieldName": "Status",
      "operator": "Equals",
      "operands": [
        {
          "value": "Draft",
          "type": "STRING"
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
| `contextId` | String | ID of the context to retrieve the data records. | Required | 65.0 |
| `queryTags` | List<String> | List of objects that must be retrieved from the context. | Optional | 65.0 |
| `sobjectFieldMap` | Map<String, List<String>> | Mapping of an sObject name to a list. The list includes the sObject field names on the object or can be an empty list. An empty list specifies that all fields on the object must be queried. | Optional | 67.0 |
| `filters` | List<[Sales Transaction Filter Condition](./connect_requests_sales_transaction_filter_condition_input.htm.md#SalesTransactionFilterConditionInputRepresentation)> | Filter conditions to query the context data. | Optional | 67.0 |

          

        
      

          

        

**Response body for POST**

: [Read Sales Transaction](./connect_responses_read_sales_transaction_output.htm.md)

=== ARTICLE: connect_resources_retrieve_place_sales_transaction_error.htm ===
---
page_id: connect_resources_retrieve_place_sales_transaction_error.htm
title: Retrieve Sales Transaction API Errors (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_retrieve_place_sales_transaction_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Retrieve Sales Transaction API Errors (GET)

Retrieve any asynchronous error details associated with
      a sales transaction request.

    
      

This API returns detailed error status and a retryable payload from [Place Sales Transaction API](./connect_resources_place_sales_transaction.htm.md)
        that runs asynchronously. Also, view any blocking errors that prevent a subrequest from
        persisting. This request doesn’t return any non-blocking warnings, such as configuration or
        tax warnings.

      

You can view the list of `rollbackedReferenceIds`, which
        shows synthetic or reference IDs that roll back when the batch fails.

      
        
          

**Resource**

          
: 
            

```
connect/revenue/transaction-management/sales-transactions/actions/place/trackerId/errors
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue/transaction-management/sales-transactions/actions/place/16PRM0000004DBq/errors
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `includeRetryable​Payload` | Boolean | Indicates whether to return a subset of the original Place Sales Transaction API payload errors (`true`) or not (`false`). The default value is `false`. | Optional | 66.0 |

          

        
        
          

**Response body for GET**

          
: [Sales Transaction
              Async Error](./connect_responses_place_sales_transaction_async_error_output.htm.md)

=== ARTICLE: connect_resources_update_ramp_deal.htm ===
---
page_id: connect_resources_update_ramp_deal.htm
title: Update Ramp Deal (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_update_ramp_deal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Update Ramp Deal (POST)

Modify a ramp deal in scenarios where a segment has updates such as
      quantity, discount, or date change.

    

Update a ramp deal in these scenarios.

        
- A segment has quantity or discount changes.

        
- A trial segment or custom segment has a date change. A custom segment is an added or
          deleted segment. In this scenario, you can update a ramp deal during the initial sale
          before assetization.

      

This API request returns the updated context with the context ID. You must call the Place Sales
        Transaction (POST) API by specifying this context ID to apply the ramp deal updates. See
          [Place Sales Transaction (POST)
          API](./connect_resources_place_sales_transaction.htm.md).

#### Note

This API is applicable when you're working with line
          ramps. To work with ramp deals for groups, you must use the Place Sales Transaction API
          and specify the `groupRampActions` property.

    
      
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-update
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/sales-transaction-contexts/4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9/actions/ramp-deal-update
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `resourceId` | String | ID of the context data that’s used to build the pricing procedure. Get the context instance ID by invoking the Context Service API. See [Context Service (POST)](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/connect_resources_create_context.htm). | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "executionSettings": {
       "executePricing": true,
       "executeConfigRules": false
  },
  "addedNodes": [
    {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9", // Context ID
        "0Q0xx0000004CPACA2", //Quote or Order ID
        "RandomUUID" // random UUID for Quote Line Item or Order Item ID
      ],
      "contextNode": {
         "Discount": 10,
         "Quantity": 5,
         "ItemSegmentName": "Year 5",
         "StartDate":"2024-09-07T00:00:00.000Z",
         "EndDate":"2024-09-07T00:00:00.000Z"
      }
    }
  ],
  "updatedNodes": [
     {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9", // Context ID
        "0Q0xx0000004CPACA2", //Quote or Order ID
        "0QLxx0000004CfIGAU" // Quote Line ID or Order Line ID to update
      ],
      "contextNode": {
          "Discount": 10,
          "Quantity": 5
      }
    } 
  ],
  "deletedNodes": [
    {
      "contextNodePath": [
        "4f23961a5c98806f89305e064c67b397e93f1bb8a2a7a3a80db506f1d4110ee9",
        "0Q0xx0000004CPACA2",
        "0QLxx0000004CfIGAU" // Quote Line Item ID to delete
      ]
    }
  ]
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `added​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be added. | Required | 62.0 |
| `deleted​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be deleted. | Required | 62.0 |
| `execution​Settings` | [Execution Settings Input](./connect_requests_execution_settings_input.htm.md)[] | Settings to run the pricing or configuration rules. | Optional | 62.0 |
| `updated​Nodes` | [Context Node Input](./connect_requests_context_node_input.htm.md)[] | Details of the nodes to be updated. | Required | 62.0 |

          

          

        
        
          

**Response body for POST**

          
: [Ramp Deal
              Service](./connect_responses_ramp_deal_service_output.htm.md)

=== ARTICLE: connect_resources_view_ramp_deal.htm ===
---
page_id: connect_resources_view_ramp_deal.htm
title: View Ramp Deal (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_view_ramp_deal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# View Ramp Deal (GET)

View a ramp deal related to a quote line item or an order
    item.

    
This API request retrieves the segments if the ramp deal already exists.

#### Note

This API is applicable when you're working with line
          ramps. To work with ramp deals for groups, you must use the Place Sales Transaction API
          and specify the `groupRampActions` property.

    
      
        
          

**Resource**

          
: 
            

```
/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-view
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/revenue-management/sales-transaction-contexts/0QLxx0000004CSOGA2/actions/ramp-deal-view?transactionId=0Q0xx0000004CDxCAM&transactionLineId=0QLxx0000004CSOGA2
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Path parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `resourceId` | String | ID of the quote line item, order item, or context. | Required | 62.0 |

          

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `transaction​Id` | String | ID of the quote or order required to hydrate the context and retrieve the quote lines. | Required | 62.0 |
| `transaction​LineId` | String | ID of the quote or order line required to retrieve the segmented details. | Required | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Ramp Deal
              Service](./connect_responses_ramp_deal_service_output.htm.md)

=== ARTICLE: connect_responses_amend_output.htm ===
---
page_id: connect_responses_amend_output.htm
title: Amendment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_amend_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Amendment

Output representation of the details of an amendment record.

        
          

**JSON example**

          
: 
            

```
{
  "amendmenRecordId": "0Q0xx0000004NsSCAU",
  "errors": [
    {
      "errorCode": "REQUIRED_FIELD_MISSING",
      "errorMessage": "Specify a value for quantityChange, and try again."
    }
  ],
  "requestId": "16Pxx0000004NIy",
  "success": true
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `amendment​RecordId` | String | ID of the amendment record that’s created for a quote or an order. | Small, 62.0 | 62.0 |
| `errors` | [ARC Base Error](./connect_responses_assets_arc_error.htm.md)[] | Error responses if the creation of an amendment record fails. | Small, 62.0 | 62.0 |
| `request​Id` | String | Request ID that’s used to track an async request. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_assets_arc_error.htm ===
---
page_id: connect_responses_assets_arc_error.htm
title: ARC Base Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_assets_arc_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ARC Base Error

Output representation of the error response related to the amendment, renewal,
    or
    cancellation of assets.

    
      

```
    "errors": [ 
        { 
            "errorCode": "REQUIRED_FIELD_MISSING",
            "errorMessage": "Specify a value for quantityChange, and try again."
        } 
    ]
```

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​Code` | String | Code for the resultant error. | Big, 62.0 | 62.0 |
| `error​Message` | String | Error message for the resultant error. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_cancel_output.htm ===
---
page_id: connect_responses_cancel_output.htm
title: Cancellation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_cancel_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Cancellation

Output representation of the details of a cancellation record.

      
        
          

**JSON example**

          
: 
            

```
{
  "cancellationRecordId": "0Q0xx0000004NsSCAU",
  "errors": [
    {
      "errorCode": "REQUIRED_FIELD_MISSING",
      "errorMessage": "Specify a value for quantityChange, and try again."
    }
  ],
  "requestId": "16Pxx0000004NIy",
  "success": true
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `cancellation​RecordId` | String | ID of the cancellation record that’s created for a quote or an order. | Small, 62.0 | 62.0 |
| `errors` | [ARC Base Error](./connect_responses_assets_arc_error.htm.md)[] | Error responses if the creation of a cancellation record fails. | Small, 62.0 | 62.0 |
| `requestId` | String | Request ID that’s used to track the async request. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

