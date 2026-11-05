# Revenue Management Developer Guide 264 — sección: Transaction Management (parte 2/2) (101 artículos)

=== ARTICLE: connect_responses_clone_sales_transaction_error_response.htm ===
---
page_id: connect_responses_clone_sales_transaction_error_response.htm
title: Clone Sales Transaction Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_clone_sales_transaction_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Clone Sales Transaction Error Response

Output representation of the errors that occur during the clone sales transaction
    operation.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "errors": [
    {
      "errorCode": "INVALID_API_INPUT",
      "message": "Specify only one record",
      "referenceId": "0QLxx0000004CBYGA2"
    }
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errorCode` | String | Code associated with the error. | 64.0 |
| `message` | String | Message associated with the error. | 64.0 |
| `referenceId` | String | Reference ID associated with the error. | 64.0 |

=== ARTICLE: connect_responses_clone_sales_transaction_output.htm ===
---
page_id: connect_responses_clone_sales_transaction_output.htm
title: Clone Sales Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_clone_sales_transaction_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Clone Sales Transaction

Output representation for the result of cloning records within a sales transaction.

    
      
        
          

**JSON example**

          
: This example shows a sample of a successful
            response.

```
{
    "requestId": "9356bcbf04f06e22360a09807c13e1d4e395",
    "salesTransactionId": "0Q0SG000000ACxf0AG",
    "errors": [],
    "success": true
}
```

This example shows a sample error
            response.

```
{
    "requestId": "9356bcbf04f06e22360a09807c13e1d4e395",
    "salesTransactionId": "0Q0SG000000ACxf0AG",
    "errors": [
        {
            "errorCode": "INVALID_API_INPUT",
            "message": "Specify only one record",
            "referenceId": "0QLxx0000004CBYGA2"
        }
    ],
    "success": false
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `requestId` | String | Request ID of the process that can be used to query the async status. | 64.0 |
| `salesTransactionId` | String | ID of the quote line item, order item, quote line group, or order item group record. | 64.0 |
| `success` | Boolean | Indicates whether the synchronous part of the processing is successful (`true`) or not (`false`). | 64.0 |
| `errors` | [Clone Sales Transaction Error Response](./connect_responses_clone_sales_transaction_error_response.htm.md)[] | List of errors encountered during synchronous processing. | 64.0 |

=== ARTICLE: connect_responses_coupon_details.htm ===
---
page_id: connect_responses_coupon_details.htm
title: Promotion Coupon
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_coupon_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Coupon

Output representation of the details of a coupon that's eligible for the recommended
    promotion.

        
          

**JSON example**

          
: 
            

```
{
  "coupon": {
    "couponCode": "COUPON_002",
    "endDateTime": null,
    "startDateTime": "2025-10-08T19:00:00.000Z",
    "status": "Active"
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `couponCode` | String | Unique code of the coupon. | Big, 66.0 | 66.0 |
| `endDateTime` | String | End date and time of the coupon. | Big, 66.0 | 66.0 |
| `startDateTime` | String | Start date and time of the coupon. | Big, 66.0 | 66.0 |
| `status` | String | Status of the coupon. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_get_eligible_promotions_output.htm ===
---
page_id: connect_responses_get_eligible_promotions_output.htm
title: Eligible Promotions Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_get_eligible_promotions_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Eligible Promotions Response

Output representation of the details of the eligible promotions.

    

        
          

**JSON example**

          
: 
            

```
{
  "eligiblePromotions": [
    {
      "additionalPromotionFields": {},
      "couponDetails": {
        "coupon": {
          "couponCode": "COUPON_002",
          "endDateTime": null,
          "startDateTime": "2025-10-08T19:00:00.000Z",
          "status": "Active"
        },
        "couponAvailabilityMessage": null
      },
      "currencyIsoCode": "USD",
      "description": "15% on Accessories",
      "displayName": "Comms Manual Promotion 15% on Accessories",
      "endDateTime": null,
      "isAutomatic": false,
      "priorityNumber": null,
      "promotionCode": null,
      "promotionEligibleRules": [
        {
          "ruleName": "CommsAutoPromotionRule",
          "rulePriority": 1,
          "ruleRewards": [
            {
              "rewardDetails": {
                "discountLevel": "Line",
                "discountType": "PercentageOff",
                "discountValue": "10.0",
                "discountAppliedAt": "LineItem",
                "discountCategory": "Accessories"
              },
              "rewardType": "ProvideDiscount"
            }
          ]
        }
      ],
      "promotionId": "0c8DX00000001UeYAI",
      "promotionLimits": [],
      "startDateTime": "2025-07-01T17:02:00.000Z",
      "termsAndCondition": "&lt;p&gt;test&lt;/p&gt;"
    },
    {
      "additionalPromotionFields": {},
      "couponDetails": {
        "coupon": {
          "couponCode": "COUPON_001",
          "endDateTime": null,
          "startDateTime": null,
          "status": "Active"
        },
        "couponAvailabilityMessage": null
      },
      "currencyIsoCode": "USD",
      "description": "Promo_Printer_Child",
      "displayName": "Promo_Printer_Child",
      "endDateTime": null,
      "isAutomatic": false,
      "priorityNumber": null,
      "promotionCode": null,
      "promotionEligibleRules": [
        {
          "ruleName": "Rule001",
          "rulePriority": 1,
          "ruleRewards": [
            {
              "rewardDetails": {
                "discountLevel": "Line",
                "discountProduct": "Printer Paper",
                "discountType": "AmountOff",
                "discountValue": "2.0",
                "discountAppliedAt": "LineItem"
              },
              "rewardType": "ProvideDiscount"
            }
          ]
        }
      ],
      "promotionId": "0c8DX00000001h5YAA",
      "promotionLimits": [],
      "startDateTime": "2025-11-03T12:44:00.000Z",
      "termsAndCondition": "&lt;p&gt;Promo_Printer_Child&lt;/p&gt;"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `eligiblePromotions` | [Promotion Details Response](./connect_responses_promotion_details.htm.md) | List of eligible promotions for the specified line items. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_get_instant_pricing_output.htm ===
---
page_id: connect_responses_get_instant_pricing_output.htm
title: Instant Pricing
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_get_instant_pricing_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Instant Pricing

Output representation containing the results of the instant pricing request.

      
        
          

**Sample Response**

          
: 
            

```
{
  "contextId": "0000000p18dq18g0025177552281982954d1f35410374495bc923a2319a1247c",
  "correlationId": "7847127122596",
  "records": [
    {
      "error": {},
      "record": {
        "NetUnitPrice": 900.8972677417262,
        "Discount": null,
        "EndQuantity": 5,
        "NetTotalPrice": 3603.5890709669047,
        "AggregatedQuantity": 4,
        "TotalLineAmount": 3603.5890709669047,
        "Quantity": 4,
        "attributes": {
          "type": "QuoteLineItem"
        },
        "ListPrice": 900.8972677417262
      },
      "referenceId": "0QLLT0000018DY14AM"
    },
    {
      "error": {},
      "record": {
        "NetUnitPrice": 720.3738964743471,
        "Discount": null,
        "EndQuantity": 5,
        "NetTotalPrice": 2881.4955858973885,
        "AggregatedQuantity": 4,
        "TotalLineAmount": 2881.4955858973885,
        "Quantity": 4,
        "attributes": {
          "type": "QuoteLineItem"
        },
        "ListPrice": 720.3738964743471
      },
      "referenceId": "0QLLT0000018DYr4AM"
    },
    {
      "error": {},
      "record": {
        "NetUnitPrice": 218.36199390885784,
        "Discount": null,
        "EndQuantity": 5,
        "NetTotalPrice": 873.4479756354314,
        "AggregatedQuantity": 4,
        "TotalLineAmount": 873.4479756354314,
        "Quantity": 4,
        "attributes": {
          "type": "QuoteLineItem"
        },
        "ListPrice": 218.36199390885784
      },
      "referenceId": "0QLLT0000018DYG4A2"
    },
    {
      "error": {},
      "record": {
        "AccountId": "001LT000011SA6bYAG",
        "TotalPrice": 406014.84549259685,
        "attributes": {
          "type": "Quote"
        },
        "Discount": 0,
        "psmSummaryFields": {
          "evergreen##months##1": {
            "aggregatedTotal": 140349.76846114534,
            "pricingTerm": 1,
            "pricingTermUnit": "Months",
            "sellingModelType": "Evergreen"
          },
          "onetime": {
            "aggregatedTotal": 128927.94222255558,
            "sellingModelType": "OneTime"
          },
          "termdefined##annual##1": {
            "aggregatedTotal": 136737.13480889596,
            "pricingTerm": 1,
            "pricingTermUnit": "Annual",
            "sellingModelType": "TermDefined"
          }
        },
        "Subtotal": 406014.84549259685
      },
      "referenceId": "0Q0LT000000Q1LR0A0"
    }
  ],
  "success": true
}
```

          

        
      

              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | Context ID returned by the context service. | Small, 59.0 | 59.0 |
| `correlationId` | String | Client-generated ID for tracking multiple related API calls. | Small, 59.0 | 59.0 |
| `records` | [Object Reference](./connect_responses_object_with_reference_response.htm.md)[] | List of records related to pricing results. | Small, 59.0 | 59.0 |
| `success` | Boolean | Indicates whether the fetching of instant pricing is successful (`true`) or not (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_initiate_downgrade_output.htm ===
---
page_id: connect_responses_initiate_downgrade_output.htm
title: Initiate Downgrade Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_initiate_downgrade_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Downgrade Response

Output representation of the request to initiate a downgrade action.

        
          

**JSON example**

          
: 
            

```
{
  "salesTransactionId": "0Q09Q000005IkEPSA0"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `salesTransactionId` | String | ID of the sales transaction that’s created by the downgrade action. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_initiate_swap_output.htm ===
---
page_id: connect_responses_initiate_swap_output.htm
title: Initiate Swap Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_initiate_swap_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Swap Response

Output representation of the request to initiate a swap action.

        
          

**JSON example**

          
: 
            

```
{
  "salesTransactionId": "0Q09Q000005IkEPSA0"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `salesTransactionId` | String | ID of the sales transaction that’s created by the swap action. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_initiate_upgrade_output.htm ===
---
page_id: connect_responses_initiate_upgrade_output.htm
title: Initiate Upgrade Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_initiate_upgrade_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Initiate Upgrade Response

Output representation of the request to initiate an upgrade action.

        
          

**JSON example**

          
: 
            

```
{
  "salesTransactionId": "0Q09Q000005IkEPSA0"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `salesTransactionId` | String | ID of the sales transaction that’s created by the upgrade action. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_object_with_reference_response.htm ===
---
page_id: connect_responses_object_with_reference_response.htm
title: Object Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_object_with_reference_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Object Reference

Output representation of an sObject with a reference ID along with any potential
    error.

    
      
        
          

**Sample Response**

          
: 
            

```
{
  "referenceid": "refQuote",
  "record": {
    "attributes": {
      "type": "Quote",
      "method": "POST"
    },
    "quantity": "2"
  },
  "error": {
    "errorCode": "INVALID_API_INPUT",
    "message": "Reference Id format is irrelevant."
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `referenceId` | String | ID that identifies the specific Salesforce object that’s returned in the API response. | Small, 59.0 | 59.0 |
| `record` | Map<String, Object> | The sObject record data represented as a map of attribute names to their values. | Small, 59.0 | 59.0 |
| `error` | [https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_responses_error_response.htm](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm)[] | Detailed information about any error associated with the sObject in the response. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_place_order_error_response.htm ===
---
page_id: connect_responses_place_order_error_response.htm
title: Place Order Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_order_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Order Error Response

Output representation of the error response for the place order request.

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code representing the type of error encountered during the place order create request. | Small, 60.0 | 60.0 |
| `message` | String | Message stating the reason for the error, if any. | Small, 60.0 | 60.0 |
| `reference​Id` | String | Reference ID associated with the specific error instance for tracking and reference purposes. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_place_order_output.htm ===
---
page_id: connect_responses_place_order_output.htm
title: Place Order Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_order_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Order Response

Output representation of the request to create or update an order.

        
          

**JSON example**

          
: 
            

```
{
  "requestId": "16PRM0000004DBq",
  "orderId": "801S70000001VKgIAM",
  "success": true,
  "errors": [],
  "statusURL": "/services/data/vXX.X/sobjects/AsyncOperationTracker/16PRM0000004DBq"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              
              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Place Order​Error​Response](./connect_responses_place_order_error_response.htm.md)[] | List of errors encountered during the synchronous processing. | Small, 60.0 | 60.0 |
| `orderId` | String | ID of the order created after a successful request. | Small, 60.0 | 60.0 |
| `requestId` | String | Request ID of the process to query asynchronous status of the place order API. | Small, 60.0 | 60.0 |
| `status​URL` | String | Asynchronous status URL of the request, if available. | Small, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the synchronous part of the processing is successful (`true`) or not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_place_quote_error_response.htm ===
---
page_id: connect_responses_place_quote_error_response.htm
title: Place Quote Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_quote_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Quote Error Response

Output representation of the error responses of a place quote request.

      
        
          

**JSON Example**

          
: 
            

```
{
 "errorCode": "INVALID_API_INPUT",
 "message": "Include record type and method in the request and try again.",
 "referenceId": "refQuoteItem2"
 }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​Code` | String | Error code representing the type of error encountered in the create place quote request. | Small, 60.0 | 60.0 |
| `message` | String | Message stating the reason for the error, if any. | Small, 60.0 | 60.0 |
| `reference​Id` | String | Reference ID associated with the specific error instance for tracking and reference purposes. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_place_quote_output.htm ===
---
page_id: connect_responses_place_quote_output.htm
title: Place Quote
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_quote_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Place Quote

Output representation of the request to create or update a quote.

      
        
          

**JSON Example**

          
: This example shows a sample response of the place quote request.

          
: 
            

```
{
    "quoteId": "0Q0xx0000004E2mCAE",
    "requestIdentifier": "95Txx0000004Cx2",
    "responseError": [],
    "statusURL": "/services/data/v60.0/sobjects/RevenueAsyncOperation/95Txx0000004Cx2EAE",
    "success": true
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `quoteId` | String | ID of the quote created after a successful request. | Small, 60.0 | 60.0 |
| `request​Identifier` | String | Unique request identifier that can be used to poll the async request. | Big, 60.0 | 60.0 |
| `response​Error` | [Place Quote Error Response](./connect_responses_place_quote_error_response.htm.md) [] | List of errors encountered during the synchronous processing. | Small, 60.0 | 60.0 |
| `status​URL` | String | Asynchronous status URL to track the operation, if available. | Big, 60.0 | 60.0 |
| `success` | Boolean | Indicates whether the synchronous part of the processing is successful (`true`) or not (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_place_sales_transaction_async_error_output.htm ===
---
page_id: connect_responses_place_sales_transaction_async_error_output.htm
title: Sales Transaction Async Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_sales_transaction_async_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Async Error

Output representation of the details of errors encountered during the async processing of
    the Place Sales Transaction API request.

        
          

**JSON example**

          
: 
            

```
{
  "errors": [
    {
      "errorCode": "FIELD_CUSTOM_VALIDATION_EXCEPTION",
      "message": "Quantity cannot exceed 10",
      "referenceId": "refQuoteLineItem2"
    }
  ],
  "jobStatus": "Completed",
  "retryablePayload": {
    "pricingPref": "System",
    "configurationPref": {
      "configurationMethod": "System",
      "configurationOptions": {
        "validateProductCatalog": true,
        "validateAmendRenewCancel": true,
        "executeConfigurationRules": true,
        "addDefaultConfiguration": true
      }
    },
    "graph": {
      "graphId": "1",
      "records": [
        {
          "referenceId": "refQuoteLineItem2",
          "record": {
            "attributes": {
              "type": "QuoteLineItem",
              "method": "POST"
            },
            "QuoteId": "000xx0000004CNYCA2",
            "PricebookEntryId": "01uxx0000009CL2",
            "Product2Id": "01txx0000006uu2",
            "Quantity": 15,
            "UnitPrice": 100
          }
        },
        {
          "referenceId": "refQuoteLineItem3",
          "record": {
            "attributes": {
              "type": "QuoteLineItem",
              "method": "POST"
            },
            "QuoteId": "000xx0000004CNYCA2",
            "PricebookEntryId": "01uxx0000009CL3",
            "Product2Id": "01txx0000006uu3",
            "Quantity": 20,
            "UnitPrice": 100
          }
        },
        {
          "referenceId": "refQuoteLinePriceAdjustment1",
          "record": {
            "attributes": {
              "type": "QuoteLinePriceAdjustment",
              "method": "POST"
            },
            "QuoteLineItemId": "@{refQuoteLineItem3.id}",
            "Name": "Some Promo",
            "Amount": -25
          }
        }
      ]
    }
  },
  "rolledBackReferenceIds": [
    "refQuoteLineItem3",
    "refQuoteLinePriceAdjustment1"
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Place Sales Transaction Error](./connect_responses_place_sales_transaction_error_response.htm.md)[] | List of async errors from Place Sales Transaction API. The details include a reference ID for the failed subrequest, an error code, and a detailed message. | Small, 66.0 | 66.0 |
| `jobStatus` | String | Status of the async tracker ID. Error results are returned after the job is in a `Completed` status. | Small, 66.0 | 66.0 |
| `retryablePayload` | [Sales Transaction Input](./connect_requests_place_sales_transaction_input.htm.md) | Subset of the original Place Sales Transaction API payload errors that can be used for retry attempts. Reference IDs that are saved are replaced by their corresponding record IDs.This property is included in the response only when the `includeRetryablePayload` query parameter is set to `true`. | Small, 66.0 | 66.0 |
| `rolledBack​ReferenceIds` | String[] | List of rolled-back reference IDs for subrequests due to failure of a subrequest in the same transaction. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_place_sales_transaction_error_response.htm ===
---
page_id: connect_responses_place_sales_transaction_error_response.htm
title: Sales Transaction Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_sales_transaction_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Error Response

Output representation of the error details associated with the API request.

    

        
          

**JSON example**

          
: 
            

```
{
  "errorResponse": {
    "errorCode": "INVALID_API_INPUT",
    "message": "Include record type and method in the request and try again.",
    "referenceId": "refQuoteItem2"
  }
}
```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | Small, 63.0 | 63.0 |
| `message` | String | Error message for the resultant error. | Small, 63.0 | 63.0 |
| `referenceId` | String | Unique ID that’s associated with the specific error for tracking and reference purposes. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_place_sales_transaction_output.htm ===
---
page_id: connect_responses_place_sales_transaction_output.htm
title: Sales Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_sales_transaction_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction

Output representation of the request to create a sales transaction.

    

        
          

**JSON example**

          
: 
            

```
{
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708",
    "isBuiltInTransaction": true
  },
  "errorResponse": {
    "errorCode": "INVALID_API_INPUT",
    "message": "Include record type and method in the request and try again.",
    "referenceId": "refQuoteItem2"
  },
  "isSuccess": true,
  "salesTransactionId": "0Q0xx0000004CNYCA2",
  "statusUrl": null,
  "trackerId": null
}
```

          

        
      

    

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextDetails` | [Sales Transaction Context](./connect_responses_sales_transaction_context_output.htm.md) | Details of the context that’s created for the sales transaction. | Small, 63.0 | 63.0 |
| `errorResponse` | [Sales Transaction Error Response](./connect_responses_place_sales_transaction_error_response.htm.md)[] | Details of the error if the operation fails. | Small, 63.0 | 63.0 |
| `isSuccess` | Boolean | Indicates if the operation is successful (`true`) or not (`false`). | Small, 63.0 | 63.0 |
| `salesTransactionId` | String | ID of the sales transaction, such as a quote or an order. | Small, 63.0 | 63.0 |
| `statusUrl` | String | URL to check the status of the operation. | Small, 63.0 | 63.0 |
| `trackerId` | String | Unique identifier assigned to a specific operation or request that's used for tracking and referencing the operation. | Small, 63.0 | 63.0 |

The **Calculation Status** field for a quote or an order shows
        an intermediate status as `Saving` during the creation of
        a sales transaction. If the pricing calculation fails, then the **Calculation
          Status** field shows the `Pricing Calculation
          Failed` status. See  [Quote standard object](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_quote.htm) for a
        list of applicable calculation status values.

=== ARTICLE: connect_responses_place_supplemental_transaction_error_response.htm ===
---
page_id: connect_responses_place_supplemental_transaction_error_response.htm
title: Supplemental Transaction Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_supplemental_transaction_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Supplemental Transaction Error Response

Output representation of the error details associated with the Place Supplemental
    Transaction API.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | Small, 64.0 | 64.0 |
| `message` | String | Message stating the reason for error, if any. | Small, 64.0 | 64.0 |
| `referenceId` | String | Unique ID that’s associated with the specific error for tracking and reference purposes. | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_place_supplemental_transaction_output.htm ===
---
page_id: connect_responses_place_supplemental_transaction_output.htm
title: Supplemental Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_place_supplemental_transaction_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Supplemental Transaction

Output representation of the details of the created supplemental order.

        
          

**JSON example**

          
: 
            

```
{
  "requestId": "16PRM0000004DBq",
  "statusURL": "/services/data/vXX.X/sobjects/AsyncOperationTracker/16PRM0000004DBq",
  "orderId": "801S70000001VKgIAM",
  "success": true,
  "errors": []
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Supplemental Transaction Error Response](./connect_responses_place_supplemental_transaction_error_response.htm.md)[] | List of errors encountered during synchronous processing. | Small, 64.0 | 64.0 |
| `requestId` | String | Request ID of the process that can be used to query the async status. | Small, 64.0 | 64.0 |
| `statusURL` | String | URL to check the status of the async operation, if available. | Small, 64.0 | 64.0 |
| `success` | Boolean | Indicates whether the synchronous part of the processing is successful (`true`) or not (`false`). | Small, 64.0 | 64.0 |
| `supplemental​TransactionId` | String | ID of the created supplemental transaction. | Small, 64.0 | 64.0 |

=== ARTICLE: connect_responses_promotion_coupon_availability.htm ===
---
page_id: connect_responses_promotion_coupon_availability.htm
title: Promotion Coupon Availability
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_coupon_availability.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Coupon Availability

Output representation of the details of the coupon that's eligible for the promotion.
    Additionally, this representation specifies the reason for any coupon ineligibility.

        
          

**JSON example**

          
: 
            

```
{
  "couponDetails": {
    "coupon": {
      "couponCode": "COUPON_002",
      "endDateTime": null,
      "startDateTime": "2025-10-08T19:00:00.000Z",
      "status": "Active"
    },
    "couponAvailabilityMessage": null
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `coupon` | [Promotion Coupon](./connect_responses_coupon_details.htm.md)[] | Coupon that's eligible for the customers' cart. | Big, 66.0 | 66.0 |
| `couponAvailability​Message` | String | Specifies the reason for coupon ineligibility for the promotion. Valid values are: `MultipleActiveCoupons` `NoActiveCoupons` `SingleActiveCouponLimitReached` | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_promotion_details.htm ===
---
page_id: connect_responses_promotion_details.htm
title: Promotion Details Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Details Response

Output representation of the eligible promotion and its details. This representation
    includes details of any coupons, eligibility rules, and terms and conditions.

        
          

**JSON example**

          
: 
            

```
{
  "eligiblePromotions": [
    {
      "additionalPromotionFields": {},
      "couponDetails": {
        "coupon": {
          "couponCode": "COUPON_002",
          "endDateTime": null,
          "startDateTime": "2025-10-08T19:00:00.000Z",
          "status": "Active"
        },
        "couponAvailabilityMessage": null
      },
      "currencyIsoCode": "USD",
      "description": "15% on Accessories",
      "displayName": "Comms Manual Promotion 15% on Accessories",
      "endDateTime": null,
      "isAutomatic": false,
      "priorityNumber": null,
      "promotionCode": null,
      "promotionEligibleRules": [
        {
          "ruleName": "CommsAutoPromotionRule",
          "rulePriority": 1,
          "ruleRewards": [
            {
              "rewardDetails": {
                "discountLevel": "Line",
                "discountType": "PercentageOff",
                "discountValue": "10.0",
                "discountAppliedAt": "LineItem",
                "discountCategory": "Accessories"
              },
              "rewardType": "ProvideDiscount"
            }
          ]
        }
      ],
      "promotionId": "0c8DX00000001UeYAI",
      "promotionLimits": [],
      "startDateTime": "2025-07-01T17:02:00.000Z",
      "termsAndCondition": "&lt;p&gt;test&lt;/p&gt;"
    },
    {
      "additionalPromotionFields": {},
      "couponDetails": {
        "coupon": {
          "couponCode": "COUPON_001",
          "endDateTime": null,
          "startDateTime": null,
          "status": "Active"
        },
        "couponAvailabilityMessage": null
      },
      "currencyIsoCode": "USD",
      "description": "Promo_Printer_Child",
      "displayName": "Promo_Printer_Child",
      "endDateTime": null,
      "isAutomatic": false,
      "priorityNumber": null,
      "promotionCode": null,
      "promotionEligibleRules": [
        {
          "ruleName": "Rule001",
          "rulePriority": 1,
          "ruleRewards": [
            {
              "rewardDetails": {
                "discountLevel": "Line",
                "discountProduct": "Printer Paper",
                "discountType": "AmountOff",
                "discountValue": "2.0",
                "discountAppliedAt": "LineItem"
              },
              "rewardType": "ProvideDiscount"
            }
          ]
        }
      ],
      "promotionId": "0c8DX00000001h5YAA",
      "promotionLimits": [],
      "startDateTime": "2025-11-03T12:44:00.000Z",
      "termsAndCondition": "&lt;p&gt;Promo_Printer_Child&lt;/p&gt;"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additional​PromotionFields` | Map<String, Object> | Values of the additional promotion fields that are mapped in the context definition. | Big, 66.0 | 66.0 |
| `couponDetails` | [Promotion Coupon Availability](./connect_responses_promotion_coupon_availability.htm.md)[] | Specifies the details of the coupon eligible for the promotion or specifies the reason why there isn’t an eligible coupon for the promotion. | Big, 66.0 | 66.0 |
| `currencyIso​Code` | String | Three-letter ISO 4217 code of the monetary currency associated with the promotion. | Big, 66.0 | 66.0 |
| `description` | String | Description of the promotion. | Big, 66.0 | 66.0 |
| `displayName` | String | Display name of the eligible promotion. | Big, 66.0 | 66.0 |
| `endDateTime` | String | End date and time of the promotion in the ISO 8601 date format. | Big, 60.0 | 66.0 |
| `isAutomatic` | Boolean | Indicates whether the promotion is automatically applied for eligible carts (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `priorityNumber` | Integer | Priority number of the eligible promotion for promotion ordering. | Big, 66.0 | 66.0 |
| `promotionCode` | String | Code of the eligible promotion. | Big, 66.0 | 66.0 |
| `promotionEligible​Rules` | [Promotion Rules List](./connect_responses_promotion_rules_list.htm.md)[] | List of promotion rules that are eligible for the customer's cart. | Big, 66.0 | 66.0 |
| `promotionId` | String | ID of the eligible promotion. | Big, 66.0 | 66.0 |
| `promotion​Limits` | [Promotion Limit](./connect_responses_promotion_limit.htm.md)[] | List of the promotion's cart level and cart item level limits. | Big, 66.0 | 66.0 |
| `startDate​Time` | String | Start date and time of the promotion in the ISO 8601 date format. | Big, 66.0 | 66.0 |
| `termsAnd​Condition` | String | Terms and conditions of the promotion. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_promotion_limit.htm ===
---
page_id: connect_responses_promotion_limit.htm
title: Promotion Limit
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_limit.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Limit

Output representation of the details of the promotion limit of an eligible
    promotion.

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `limitCurrent​Attainment` | Double | Current attainment of the promotion's limit value. | Big, 66.0 | 66.0 |
| `limitTarget` | Double | Value beyond which the promotion can't be applied to customer carts. | Big, 66.0 | 66.0 |
| `limitType` | String | Limit type for the promotion. Valid values are: `CartItemCount`—Specifes the limit type that represents the maximum number of cart items the promotion can applied for. `OrderCount`—Specifies the limit type that represents the maximum number of carts the promotion can applied for. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_promotion_reward_details.htm ===
---
page_id: connect_responses_promotion_reward_details.htm
title: Promotion Reward Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_reward_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Reward Details

Output representation of the details of the rewards of an eligible promotion
    rule.

        
          

**JSON example**

          
: 
            

```
{
  "ruleRewards": [
    {
      "rewardDetails": {
        "discountLevel": "Line",
        "discountProduct": "Printer Paper",
        "discountType": "AmountOff",
        "discountValue": "2.0",
        "discountAppliedAt": "LineItem"
      },
      "rewardType": "ProvideDiscount"
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

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `rewardDetails` | Map<String, Object> | Details of the reward offered by the promotion rule. | Big, 66.0 | 66.0 |
| `rewardType` | String | Reward type of the promotion. Valid values are: `AssignBadge` `AssignGame` `CreditFixedPoints` `CreditMultiplierPoints` `GiveFreeProduct` `IssueVoucher` `ProvideDiscount` | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_promotion_rules_list.htm ===
---
page_id: connect_responses_promotion_rules_list.htm
title: Promotion Rules List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_rules_list.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Rules List

Output representation of the details of the rules of an eligible promotion.

        
          

**JSON example**

          
: 
            

```
{
  "promotionEligibleRules": [
    {
      "ruleName": "Rule001",
      "rulePriority": 1,
      "ruleRewards": [
        {
          "rewardDetails": {
            "discountLevel": "Line",
            "discountProduct": "Printer Paper",
            "discountType": "AmountOff",
            "discountValue": "2.0",
            "discountAppliedAt": "LineItem"
          },
          "rewardType": "ProvideDiscount"
        }
      ]
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `ruleName` | String | Rule name in the promotion which is eligible for rewards. | Big, 66.0 | 66.0 |
| `rulePriority` | Integer | Rule priority in the promotion which is eligible for rewards. | Big, 66.0 | 66.0 |
| `ruleRewards` | [Promotion Reward Details](./connect_responses_promotion_reward_details.htm.md)[] | Rewards associated with the eligible rule. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_ramp_deal_service_error_response.htm ===
---
page_id: connect_responses_ramp_deal_service_error_response.htm
title: Ramp Deal Service Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_ramp_deal_service_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Ramp Deal Service Error Response

Output representation of the details of errors encountered during the processing of the
    API request.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code from the API request. For example,` INVALID_INPUT_ERROR`. | Small, 62.0 | 62.0 |
| `message` | String | Error message from the API request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_ramp_deal_service_output.htm ===
---
page_id: connect_responses_ramp_deal_service_output.htm
title: Ramp Deal Service
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_ramp_deal_service_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Ramp Deal Service

Output representation of the details of a created, updated, or deleted ramp
    deal.

      
        
          

**JSON Example**

          
: This example shows the sample response for the create, update, or view ramp deal
            requests.

```
{
  "correlationId": "0QLDU0000002t0Z4AQ",
  "errors": [],
  "salesTransactionContext": {
    "SalesTransaction": [
      {
        "LegalEntity": null,
        "Account": null,
        "HeaderDistributionType": null,
        "BillingCity": null,
        "AccountBusinessType": null,
        "HeaderDiscountType": null,
        "businessObjectType": "Quote",
        "QuoteAccount": null,
        "EmployeeCount": null,
        "SalesTransactionName": "WarrantyPriceRampAR",
        "StartDate": null,
        "HeaderDiscountValue": null,
        "SalesTransactionType": null,
        "Pricebook": "01sDU000000JGf4YAG",
        "Opportunity": null,
        "ShippingCountry": null,
        "ShippingCity": null,
        "BillingPostalCode": null,
        "id": "0Q0DU0000002f3d0AA",
        "BillToContact": null,
        "CalculationStatus": "CompletedWithTax",
        "Status": "Draft",
        "LastPricedDate": null,
        "Subtotal": 108.47145205479453,
        "OriginalActionType": null,
        "TotalAmount": 99.98,
        "CurrencyIsoCode": null,
        "ShippingStreet": null,
        "SalesTransactionItem": [
          {
            "LegalEntity": null,
            "ProductName": "Warranty",
            "businessObjectType": "QuoteLineItem",
            "Product": "01tDU000000EsWSYA0",
            "ItemIsPrimarySegment": true,
            "ListPrice": 49.99,
            "ValidationResult": null,
            "StartDate": "2024-08-23T00:00:00.000Z",
            "ContractVolumePasId": null,
            "BillingTreatment": null,
            "PeriodBoundaryStartMonth": null,
            "SalesTransactionSourceAsset": null,
            "id": "0QLDU0000002t0Z4AQ",
            "PartnerDiscountPercent": null,
            "PriceWaterFall": "0QLDU0000002t0Z4AQ:548201414593252",
            "ItemProductRecipient": null,
            "BillingFrequency": "Annual",
            "ProductCode": "W001",
            "DerivedPricingAttribute": null,
            "TaxTreatment": "1ttDU0000001oGKYAY",
            "Subtotal": 8.491452054794523,
            "ItemRampIdentifier": "RDI5b5ce52b2db4484",
            "ItemSegmentName": "Trial",
            "PricebookEntry": "01uDU000000f4LSYAY",
            "DiscountAmount": null,
            "PricingTermCount": 0.0849315068493151,
            "NetUnitPrice": 0,
            "ItemEffectiveGrantDate": null,
            "ProductCategory": null,
            "SalesTransactionAction": null,
            "SalesTransactionActionType": null,
            "SalesTransactionItemGroup": null,
            "PeriodBoundaryDay": null,
            "LineItemDistributionType": null,
            "ProrationPolicy": "0muDU00000029ryYAA",
            "ContractDiscountType": null,
            "TransactionType": null,
            "ParentReference": null,
            "Discount": 100,
            "ProductSellingModel": "0jPDU00000029zb2AA",
            "PricingTermUnit": "Annual",
            "PricingSource": null,
            "StockKeepingUnit": null,
            "PartnerUnitPrice": null,
            "ItemTotalAdjustmentAmount": -8.491452054794523,
            "SalesTransactionItemSource": "0QLDU0000002t0Z4AQ",
            "ContractAttributePasId": null,
            "SubscriptionTerm": 1,
            "SellingModelType": "TermDefined",
            "EndQuantity": 2,
            "NetTotalPrice": 0,
            "TotalLineAmount": 8.491452054794523,
            "ItemSegmentType": "FreeTrial",
            "ProductBasedOn": null,
            "Deleted": null,
            "BillingReference": null,
            "ArePartialPeriodsAllowed": true,
            "ItemRecordedPrice": null,
            "CustomProductName": "Warranty",
            "ItemSegmentIdentifier": "SEG4380006a1c2b416",
            "SalesTransactionItemParent": "0Q0DU0000002f3d0AA",
            "Quantity": 2,
            "PeriodBoundary": "Anniversary",
            "ContractDiscountValue": null,
            "LineItemDiscountValue": null,
            "ContractId": null,
            "EndDate": "2024-09-22T00:00:00.000Z",
            "ItemGroupSummarySubtotal": null,
            "IsContracted": null,
            "UnitPrice": 49.99,
            "StartQuantity": 0,
            "ContractPrice": null,
            "TotalPrice": 0,
            "ItemPath": null,
            "LineItemDiscountType": null
          },
          {
            "LegalEntity": null,
            "ProductName": "Warranty",
            "businessObjectType": "QuoteLineItem",
            "Product": "01tDU000000EsWSYA0",
            "ItemIsPrimarySegment": false,
            "ListPrice": 49.99,
            "ValidationResult": null,
            "StartDate": "2024-09-23T00:00:00.000Z",
            "ContractVolumePasId": null,
            "BillingTreatment": null,
            "PeriodBoundaryStartMonth": null,
            "SalesTransactionSourceAsset": null,
            "id": "0QLDU0000003CZ94AM",
            "PartnerDiscountPercent": null,
            "PriceWaterFall": "0QLDU0000003CZ94AM:548201414593252",
            "ItemProductRecipient": null,
            "BillingFrequency": "Annual",
            "ProductCode": "W001",
            "DerivedPricingAttribute": null,
            "TaxTreatment": "1ttDU0000001oGKYAY",
            "Subtotal": 99.98,
            "ItemRampIdentifier": "RDI5b5ce52b2db4484",
            "ItemSegmentName": "Year-1",
            "PricebookEntry": "01uDU000000f4LSYAY",
            "DiscountAmount": null,
            "PricingTermCount": 1,
            "NetUnitPrice": 49.99,
            "ItemEffectiveGrantDate": null,
            "ProductCategory": null,
            "SalesTransactionAction": null,
            "SalesTransactionActionType": null,
            "SalesTransactionItemGroup": null,
            "PeriodBoundaryDay": null,
            "LineItemDistributionType": null,
            "ProrationPolicy": "0muDU00000029ryYAA",
            "ContractDiscountType": null,
            "TransactionType": null,
            "ParentReference": null,
            "Discount": null,
            "ProductSellingModel": "0jPDU00000029zb2AA",
            "PricingTermUnit": "Annual",
            "PricingSource": null,
            "StockKeepingUnit": null,
            "PartnerUnitPrice": null,
            "ItemTotalAdjustmentAmount": 0,
            "SalesTransactionItemSource": "0QLDU0000003CZ94AM",
            "ContractAttributePasId": null,
            "SubscriptionTerm": 1,
            "SellingModelType": "TermDefined",
            "EndQuantity": 2,
            "NetTotalPrice": 99.98,
            "TotalLineAmount": 99.98,
            "ItemSegmentType": "Yearly",
            "ProductBasedOn": null,
            "Deleted": null,
            "BillingReference": null,
            "ArePartialPeriodsAllowed": true,
            "ItemRecordedPrice": null,
            "CustomProductName": "Warranty",
            "ItemSegmentIdentifier": "SEG73ad7378e1ed4c5",
            "SalesTransactionItemParent": "0Q0DU0000002f3d0AA",
            "Quantity": 2,
            "PeriodBoundary": "Anniversary",
            "ContractDiscountValue": null,
            "LineItemDiscountValue": null,
            "ContractId": null,
            "EndDate": "2025-08-22T00:00:00.000Z",
            "ItemGroupSummarySubtotal": null,
            "IsContracted": null,
            "UnitPrice": 49.99,
            "StartQuantity": 0,
            "ContractPrice": null,
            "TotalPrice": 99.98,
            "ItemPath": null,
            "LineItemDiscountType": null
          }
        ],
        "AppUsageAssignment": [
          {
            "businessObjectType": "AppUsageAssignment",
            "ParentReference": null,
            "Record": "0Q0DU0000002f3d0AA",
            "id": "0j8DU0000002VKiYAM",
            "AppUsageType": "RevenueLifecycleManagement"
          }
        ],
        "BillingCountry": null,
        "BillingStreet": null,
        "ShippingPostalCode": null,
        "SalesTransactionSource": "0Q0DU0000002f3d0AA",
        "PrimaryIndustry": null,
        "ShippingState": null,
        "HeaderDistributionLogic": null,
        "Contract": null,
        "BillingState": null,
        "AnnualRevenue": null,
        "EffectiveDate": null
      }
    ]
  },
  "success": true,
  "transactionContextId": "d3fd83b007418ce4980340313b40fd45665b194973486ebac3674c2b8002336f"
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Resource ID to correlate the API request with the response. | Small, 62.0 | 62.0 |
| `errors` | [Ramp Deal Service Error Response](./connect_responses_ramp_deal_service_error_response.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 62.0 | 62.0 |
| `sales​Transaction​Context` | Map<String, Object> | Context object for the sales transaction with updated segment details. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `transaction​ContextId` | String | ID of the sales transaction context record instance. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_read_sales_transaction_output.htm ===
---
page_id: connect_responses_read_sales_transaction_output.htm
title: Read Sales Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_read_sales_transaction_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Read Sales Transaction

Output representation of the request to read a sales transaction.

        
          

**JSON example**

          
: 
            

```
{
  "response": {
    "records": {
      "Quote": [
        {
          "data": {
            "Id": "0Q05g000000AJK954",
            "Name": "Sample Quote",
            "Status": "Draft",
            "TotalPrice": 1500
          }
        }
      ],
      "QuoteLineItem": [
        {
          "data": {
            "Id": "0QL5g000000DEF456",
            "Product2Id": "01t5g000000GUE752",
            "Quantity": 2,
            "UnitPrice": 750,
            "TotalPrice": 1500
          }
        }
      ]
    }
  },
  "isSuccess": true,
  "errorResponse": []
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Place Sales Transaction Error Response](./connect_responses_place_sales_transaction_error_response.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 65.0 | 65.0 |
| `isSuccess` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 65.0 | 65.0 |
| `response` | [Read Sales Transaction Records](./connect_responses_read_sales_transaction_records_output.htm.md)[] | Contains a map of keys and associated values. The keys are record type names, such as a Quote or QuoteLineItem, and values are lists of records of that type. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_read_sales_transaction_records_output.htm ===
---
page_id: connect_responses_read_sales_transaction_records_output.htm
title: Read Sales Transaction Records
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_read_sales_transaction_records_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Read Sales Transaction Records

Output representation of the details of a map of keys and associated values. The keys are
    record type names, such as a Quote or QuoteLineItem, and values are lists of records of that
    type.

        
          

**JSON example**

          
: 
            

```
{
  "response": {
    "records": {
      "Quote": [
        {
          "data": {
            "Id": "0Q05g000000AJK954",
            "Name": "Sample Quote",
            "Status": "Draft",
            "TotalPrice": 1500
          }
        }
      ],
      "QuoteLineItem": [
        {
          "data": {
            "Id": "0QL5g000000DEF456",
            "Product2Id": "01t5g000000GUE752",
            "Quantity": 2,
            "UnitPrice": 750,
            "TotalPrice": 1500
          }
        }
      ]
    }
  },
  "isSuccess": true,
  "errorResponse": []
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `records` | Map<String, [Sales Transaction Record](./connect_responses_sales_transaction_record_output.htm.md)>> | Map of record type names to the list of records. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_renew_output.htm ===
---
page_id: connect_responses_renew_output.htm
title: Renewal
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_renew_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Renewal

Output representation of the details of a renewal record.

        
          

**JSON example**

          
: 
            

```
{
  "renewalRecordId": "0Q0xx0000004NsSCAU",
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
| `errors` | [ARC Base Error](./connect_responses_assets_arc_error.htm.md)[] | Error responses if the creation of a renewal record fails. | Small, 62.0 | 62.0 |
| `renewal​RecordId` | String | ID of the renewal record that’s created for the Quote or Order record. | Small, 62.0 | 62.0 |
| `requestId` | String | Request ID that’s used to track the async request. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_sales_transaction_context_output.htm ===
---
page_id: connect_responses_sales_transaction_context_output.htm
title: Sales Transaction Context
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sales_transaction_context_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Context

Output representation of the context details that are associated with a sales
    transaction.

    

        
          

**JSON example**

          
: 
            

```
{
  "contextDetails": {
    "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708",
    "isBuiltInTransaction": true
  }
}
```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of the context that’s created for a session of the sales transaction. | Small, 63.0 | 63.0 |
| `isBuiltIn​Transaction` | Boolean | Indicates whether a new context ID is created for the sales transaction (`true`) or not (`false`).If the `contextId` property isn’t specified, the Place Sales Transaction API generates it. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_sales_transaction_record_output.htm ===
---
page_id: connect_responses_sales_transaction_record_output.htm
title: Sales Transaction Record
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sales_transaction_record_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sales Transaction Record

Generic output representation for any sales transaction record type.

        
          

**JSON example**

          
: 
            

```
{
  "response": {
    "records": {
      "Quote": [
        {
          "data": {
            "Id": "0Q05g000000AJK954",
            "Name": "Sample Quote",
            "Status": "Draft",
            "TotalPrice": 1500
          }
        }
      ],
      "QuoteLineItem": [
        {
          "data": {
            "Id": "0QL5g000000DEF456",
            "Product2Id": "01t5g000000GUE752",
            "Quantity": 2,
            "UnitPrice": 750,
            "TotalPrice": 1500
          }
        }
      ]
    }
  },
  "isSuccess": true,
  "errorResponse": []
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `data` | Map<String, Object> | Represents the data map for any sales transaction record. | Small, 65.0 | 65.0 |

=== ARTICLE: qoc_apex_reference.htm ===
---
page_id: qoc_apex_reference.htm
title: Transaction Management Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Apex Reference

Use built-in Apex classes and interfaces grouped by
    namespace.

- 
**[CommerceOrders Namespace](./apex_namespace_commerceorders.htm.md)**  

The `CommerceOrders` namespace provides classes and     methods to place orders with integrated pricing, configuration, and validation.

- 
**[ConnectApi Namespace](./transaction_management_connect_api_namespace.htm.md)**  

The `ConnectApi` namespace (also called Connect in         Apex) provides an Apex class to specify details for asset transfer request from one account         to another.

- 
**[CommerceTax Namespace](./apex_namespace_commercetax.htm.md)**  

Manage the communication between Salesforce and an external tax engine.

- 
**[PlaceQuote Namespace](./apex_namespace_placequote.htm.md)**  

The `PlaceQuote` namespace provides classes and methods     to create or update quotes with pricing preferences and configuration options.

- 
**[renew_assets_summary Namespace](./apex_namespace_renew_assets_summary.htm.md)**  

Retrieve details about renewable assets to create renewal opportunities.

- 
**[RevSalesTrxn Namespace](./apex_namespace_RevSalesTrxn.htm.md)**  

Create a sales transaction, such as a quote or an order, with integrated       pricing and configuration. Additionally, update an order or a quote, and insert and delete       order or quote line items to calculate the estimated tax.

=== ARTICLE: qoc_api_requests.htm ===
---
page_id: qoc_api_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_api_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available API request bodies.

- 
**[Amendment Input](./connect_requests_amend_input.htm.md)**  

Input representation of the details of the request to create an amendment     record.

- 
**[Cancellation Input](./connect_requests_cancel_input.htm.md)**  

Input representation of the details of the request to cancel a quote or an     order.

- 
**[Create Ramp Deal Input](./connect_requests_create_ramp_deal_input.htm.md)**  

Input representation of the request to create a ramp deal.

- 
**[Clone Options Input](./connect_requests_clone_options_input.htm.md)**  

Input representation of the options to clone a sales transaction.

- 
**[Clone Sales Transaction Input](./connect_requests_clone_sales_transaction_input.htm.md)**  

Input representation of the request to clone records within a sales     transaction.

- 
**[Configuration Options Input](./connect_requests_configuration_options_input.htm.md)**  

Input representation for the configuration options.

- 
**[Configurator Preference Input](./connect_requests_configurator_preference_input.htm.md)**  

Input representation of the configuration preference for the place sales transaction     request.

- 
**[Context Input](./connect_requests_context_info_input.htm.md)**  

Input representation of the context that's associated with a sales transaction for a     quote or an order.

- 
**[Context Node Input](./connect_requests_context_node_input.htm.md)**  

Input representation of the details of the context nodes for ramp segments.

- 
**[Delete Ramp Deal Input](./connect_requests_delete_ramp_deal_input.htm.md)**  

Input representation of the request to delete a ramp deal.

- 
**[Eligible Promotions Input](./connect_requests_get_eligible_promotions_input.htm.md)**  

Input representation of the request to get eligible promotions for line items. This     representation includes the details to accept line item IDs and a sales transaction     ID.

- 
**[Execution Settings Input](./connect_requests_execution_settings_input.htm.md)**  

Input representation of the execution settings for a ramp deal.

- 
**[Initiate Downgrade Input](./connect_requests_initiate_downgrade_input.htm.md)**  

Input representation of the details of the request to initiate a downgrade     action.

- 
**[Initiate Swap Input](./connect_requests_initiate_swap_input.htm.md)**  

Input representation of the details of the request to initiate a swap action.

- 
**[Initiate Upgrade Input](./connect_requests_initiate_upgrade_input.htm.md)**  

Input representation of the details of the request to initiate an upgrade action. The     response includes the ID of the sales transaction that the upgrade action creates.

- 
**[Instant Pricing Input](./connect_requests_get_instant_pricing_input.htm.md)**  

Input representation to fetch the instant pricing details.

- 
**[Object Graph Input](./connect_requests_object_graph_input.htm.md)**  

Input representation of an sObject  with a graph ID.

- 
**[Object Input Map](./connect_requests_object_input_representation_map.htm.md)**  

Input representation of an sObject record in a key-value map format.

- 
**[Object with Reference Input](./connect_requests_object_with_reference_input.htm.md)**  

Input representation of a list of records to be inserted or updated. To update a     record, specify the record ID.

- 
**[Place Order Input](./connect_requests_place_order_input.htm.md)**  

Input representation of the request to create or update an order.

- 
**[Place Quote Input](./connect_requests_place_quote_input.htm.md)**  

Input representation of the request to create or update a quote.

- 
**[Read Sales Transaction Input](./connect_requests_read_sales_transaction_input.htm.md)**  

Input representation of the filter criteria details to read a sales     transaction.

- 
**[Renewal Input](./connect_requests_renew_input.htm.md)**  

Input representation of the details of the request to initiate the renewal of an     asset.

- 
**[Sales Transaction Filter Condition Input](./connect_requests_sales_transaction_filter_condition_input.htm.md)**  

Input representation of filter conditions used to query sales transaction context     data.

- 
**[Sales Transaction Input](./connect_requests_place_sales_transaction_input.htm.md)**  

Input representation of the details of the request to place a sales transaction, such as     a quote or an order.

- 
**[Sales Transaction Operand Input](./connect_requests_sales_transaction_operand_input.htm.md)**  

Input representation of a filter operand for reading sales transaction context     data.

- 
**[Supplemental Transaction Input](./connect_requests_place_supplemental_transaction_input.htm.md)**  

Input representation of the details of the request to create a supplemental     order.

- 
**[Swap Group Input](./connect_requests_swap_group.htm.md)**  

Input representation of the details of the swap groupings for swap     operations.

- 
**[Update Ramp Deal Input](./connect_requests_update_ramp_deal_input.htm.md)**  

Input representation of the request to update a ramp deal.

- 
**[Usage-Based Product Input](./connect_requests_usage_based_product_input.htm.md)**  

Understand the sample request structure to specify and manage usage-based products     within a sales transaction.

=== ARTICLE: qoc_api_responses.htm ===
---
page_id: qoc_api_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_api_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available response bodies.

- 
**[Amendment](./connect_responses_amend_output.htm.md)**  

Output representation of the details of an amendment record.

- 
**[ARC Base Error](./connect_responses_assets_arc_error.htm.md)**  

Output representation of the error response related to the amendment, renewal,     or     cancellation of assets.

- 
**[Cancellation](./connect_responses_cancel_output.htm.md)**  

Output representation of the details of a cancellation record.

- 
**[Clone Sales Transaction](./connect_responses_clone_sales_transaction_output.htm.md)**  

Output representation for the result of cloning records within a sales transaction.

- 
**[Clone Sales Transaction Error Response](./connect_responses_clone_sales_transaction_error_response.htm.md)**  

Output representation of the errors that occur during the clone sales transaction     operation.

- 
**[Eligible Promotions Response](./connect_responses_get_eligible_promotions_output.htm.md)**  

Output representation of the details of the eligible promotions.

- 
**[Initiate Downgrade Response](./connect_responses_initiate_downgrade_output.htm.md)**  

Output representation of the request to initiate a downgrade action.

- 
**[Initiate Swap Response](./connect_responses_initiate_swap_output.htm.md)**  

Output representation of the request to initiate a swap action.

- 
**[Initiate Upgrade Response](./connect_responses_initiate_upgrade_output.htm.md)**  

Output representation of the request to initiate an upgrade action.

- 
**[Instant Pricing](./connect_responses_get_instant_pricing_output.htm.md)**  

Output representation containing the results of the instant pricing request.

- 
**[Object Reference](./connect_responses_object_with_reference_response.htm.md)**  

Output representation of an sObject with a reference ID along with any potential     error.

- 
**[Place Order Error Response](./connect_responses_place_order_error_response.htm.md)**  

Output representation of the error response for the place order request.

- 
**[Place Order Response](./connect_responses_place_order_output.htm.md)**  

Output representation of the request to create or update an order.

- 
**[Place Quote Error Response](./connect_responses_place_quote_error_response.htm.md)**  

Output representation of the error responses of a place quote request.

- 
**[Place Quote](./connect_responses_place_quote_output.htm.md)**  

Output representation of the request to create or update a quote.

- 
**[Sales Transaction Async Error](./connect_responses_place_sales_transaction_async_error_output.htm.md)**  

Output representation of the details of errors encountered during the async processing of     the Place Sales Transaction API request.

- 
**[Promotion Coupon](./connect_responses_coupon_details.htm.md)**  

Output representation of the details of a coupon that's eligible for the recommended     promotion.

- 
**[Promotion Coupon Availability](./connect_responses_promotion_coupon_availability.htm.md)**  

Output representation of the details of the coupon that's eligible for the promotion.     Additionally, this representation specifies the reason for any coupon ineligibility.

- 
**[Promotion Details Response](./connect_responses_promotion_details.htm.md)**  

Output representation of the eligible promotion and its details. This representation     includes details of any coupons, eligibility rules, and terms and conditions.

- 
**[Promotion Limit](./connect_responses_promotion_limit.htm.md)**  

Output representation of the details of the promotion limit of an eligible     promotion.

- 
**[Promotion Reward Details](./connect_responses_promotion_reward_details.htm.md)**  

Output representation of the details of the rewards of an eligible promotion     rule.

- 
**[Promotion Rules List](./connect_responses_promotion_rules_list.htm.md)**  

Output representation of the details of the rules of an eligible promotion.

- 
**[Ramp Deal Service Error Response](./connect_responses_ramp_deal_service_error_response.htm.md)**  

Output representation of the details of errors encountered during the processing of the     API request.

- 
**[Ramp Deal Service](./connect_responses_ramp_deal_service_output.htm.md)**  

Output representation of the details of a created, updated, or deleted ramp     deal.

- 
**[Read Sales Transaction](./connect_responses_read_sales_transaction_output.htm.md)**  

Output representation of the request to read a sales transaction.

- 
**[Read Sales Transaction Records](./connect_responses_read_sales_transaction_records_output.htm.md)**  

Output representation of the details of a map of keys and associated values. The keys are     record type names, such as a Quote or QuoteLineItem, and values are lists of records of that     type.

- 
**[Renewal](./connect_responses_renew_output.htm.md)**  

Output representation of the details of a renewal record.

- 
**[Sales Transaction](./connect_responses_place_sales_transaction_output.htm.md)**  

Output representation of the request to create a sales transaction.

- 
**[Sales Transaction Context](./connect_responses_sales_transaction_context_output.htm.md)**  

Output representation of the context details that are associated with a sales     transaction.

- 
**[Sales Transaction Error Response](./connect_responses_place_sales_transaction_error_response.htm.md)**  

Output representation of the error details associated with the API request.

- 
**[Sales Transaction Record](./connect_responses_sales_transaction_record_output.htm.md)**  

Generic output representation for any sales transaction record type.

- 
**[Supplemental Transaction Error Response](./connect_responses_place_supplemental_transaction_error_response.htm.md)**  

Output representation of the error details associated with the Place Supplemental     Transaction API.

- 
**[Supplemental Transaction](./connect_responses_place_supplemental_transaction_output.htm.md)**  

Output representation of the details of the created supplemental order.

=== ARTICLE: qoc_business_apis.htm ===
---
page_id: qoc_business_apis.htm
title: Transaction Management Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_business_apis.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Business APIs

Use the Transaction Management Business APIs to fetch instant pricing data on a quote
    or an order, to create a quote, or to create an order.

    

This table lists the available Transaction Management resources.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

        

      
| Resource | Description |
| --- | --- |
| [`/connect/revenue-management/assets/actions/amend`](./connect_resources_assets_amend.htm.md) (POST) | Initiate and execute the amendment of a quote or an order. |
| [`/connect/revenue-management/assets/actions/cancel`](./connect_resources_assets_cancel.htm.md) (POST) | Initiate and execute the cancellation of an asset. |
| [`/connect/revenue-management/assets/actions/renew`](./connect_resources_assets_renew.htm.md) (POST) | Initiate and execute the renewal of an asset. |
| [`/industries/cpq/quotes/actions/get-instant-price`](./connect_resources_cpq_instant_pricing.htm.md) (POST) | Fetch instant pricing data on the quote or order line data grid and associated summary component. This API offers capabilities to either create a context or update the existing one based on the provided context ID. |
| [`/commerce/sales-orders/actions/place`](./connect_resources_place_order.htm.md) (POST) | Place orders with integrated pricing, configuration, and validation, and manage them throughout their entire lifecycle. Additionally, update an order or insert order items. |
| [`/commerce/quotes/actions/place`](./connect_resources_place_quote.htm.md) (POST) | Create a quote to discover and price products and services. Additionally, insert, update, or delete a quote line item. |
| [`/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-create`](./connect_resources_create_ramp_deal.htm.md) (POST) | Create a ramp deal for a customer on a product. Sales reps can use ramp deals to provide yearly deals to a customer, resulting in long-term revenue and customer relationship. A customer can create, update, or view multiple segments of periods for their subscription term with different attributes for each segment. |
| [`/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-update`](./connect_resources_update_ramp_deal.htm.md) (POST) | Modify a ramp deal in scenarios where a segment has updates such as quantity, discount, or date change. |
| [`/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-view`](./connect_resources_view_ramp_deal.htm.md) (GET) | View a ramp deal related to a quote line item or an order item. |
| [`/connect/revenue-management/sales-transaction-contexts/resourceId/actions/ramp-deal-delete`](./connect_resources_delete_ramp_deal.htm.md) (POST) | Delete a ramp deal to convert a ramped product to include a single quote line item or order item. |
| [`/connect/rev/sales-transaction/actions/place`](./connect_resources_place_sales_transaction.htm.md) (POST) | Create a sales transaction, such as an order or a quote, with integrated pricing and configuration. Also, update an order or a quote, and insert and delete order or quote line items to calculate the estimated tax. |
| [`/connect/rev/sales-transaction/actions/clone`](./connect_resources_clone_sales_transaction.htm.md) (POST) | Create a clone of a sales transaction, such as a quote or an order. You can also clone a quote line item or an order item record with its related records and configurations. |
| [`/connect/rev/sales-transaction/actions/place-supplemental-transaction`](./connect_resources_place_supplemental_transaction.htm.md) (POST) | Create a supplemental order or change orders after they are submitted for processing, such as during the fulfillment process. |
| [`/connect/revenue/transaction-management/sales-transactions/actions/read`](./connect_resources_read_sales_transaction.htm.md) (POST) | Retrieve sales transaction data efficiently from an initialized or a hydrated context. |
| [`/global-promotions-management/promotions`](./connect_resources_create_promotions.htm.md) (GET, POST, PUT) | Get rewards based on a product selling model template. |
| [`/revenue/transaction-management/sales-transactions/actions/get-eligible-promotions`](./connect_resources_get_eligible_promotions.htm.md) (POST) | Get eligible promotions for line items within a quote or an order. |
| [`/revenue/transaction-management/assets/actions/swap`](./connect_resources_initiate_swap.htm.md) (POST) | Exchange one product for another of equivalent or different value. The change is tracked as a swap request with linked asset actions and a net-zero order total where applicable. The API creates an amendment quote and order with order actions and quote action subtypes. |
| [`/revenue/transaction-management/assets/actions/upgrade`](./connect_resources_initiate_upgrade.htm.md) (POST) | Move a lower-tier product to a higher-tier product. The change is tracked as an upgrade request with linked asset actions and quote or order line linkage for reporting and auditing. This API creates an amendment quote and order with order actions and quote action subtypes. |
| [`/revenue/transaction-management/assets/actions/downgrade`](./connect_resources_initiate_downgrade.htm.md) (POST) | Move to a lower-tier or lower-value product. The change is tracked as a downgrade request with linked asset actions and quote or order line linkage for reporting and auditing. This API creates an amendment quote and order with downgrade-specific order actions and quote action subtypes. |

  

- 
**[Resources](./qoc_business_apis_rest_references.htm.md)**  

Learn more about the available Quote and Order Capture resources.

- 
**[Request Bodies](./qoc_api_requests.htm.md)**  

Learn more about the available API request bodies.

- 
**[Response Bodies](./qoc_api_responses.htm.md)**  

Learn more about the available response bodies.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: qoc_business_apis_rest_references.htm ===
---
page_id: qoc_business_apis_rest_references.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_business_apis_rest_references.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Quote and Order Capture resources.

- 
**[Asset Amendment (POST)](./connect_resources_assets_amend.htm.md)**  

Initiate and execute the amendment of a quote or an     order.

- 
**[Asset Cancellation (POST)](./connect_resources_assets_cancel.htm.md)**  

Initiate and execute the cancellation of an asset.

- 
**[Asset Renewal (POST)](./connect_resources_assets_renew.htm.md)**  

Initiate and execute the renewal of an asset.

- 
**[Clone Sales Transaction (POST)](./connect_resources_clone_sales_transaction.htm.md)**  

Create a clone of a sales transaction, such as a quote or an order.       You can also clone a quote line item or an order item record with its related records and       configurations.

- 
**[Create Promotions (GET, POST, PUT)](./connect_resources_create_promotions.htm.md)**  

Get rewards based on a product selling model     template.

- 
**[Get Eligible Promotions (POST)](./connect_resources_get_eligible_promotions.htm.md)**  

Get eligible promotions for line items within a quote or an       order.

- 
**[Initiate Downgrade (POST)](./connect_resources_initiate_downgrade.htm.md)**  

Move to a lower-tier or lower-value product. The change is tracked as a       downgrade request with linked asset actions and quote or order line linkage for reporting and       auditing. This API creates an amendment quote and order with downgrade-specific order actions       and quote action subtypes.

- 
**[Initiate Swap (POST)](./connect_resources_initiate_swap.htm.md)**  

Exchange one product for another of equivalent or different value. The       change is tracked as a swap request with linked asset actions and a net-zero order total where       applicable. The API creates an amendment quote and order with order actions and quote action       subtypes.

- 
**[Initiate Upgrade (POST)](./connect_resources_initiate_upgrade.htm.md)**  

Move a lower-tier product to a higher-tier product. The change is       tracked as an upgrade request with linked asset actions and quote or order line linkage for       reporting and auditing. This API creates an amendment quote and order with order actions and       quote action subtypes.

- 
**[Instant Pricing (POST)](./connect_resources_cpq_instant_pricing.htm.md)**  

Fetch instant pricing data on the quote or order line data grid and       associated summary component. This API offers capabilities to either create a context or       update the existing one based on the provided context ID.

- 
**[Place Order (POST)](./connect_resources_place_order.htm.md)**  

Place orders with integrated pricing, configuration, and validation,       and manage them throughout their entire lifecycle. Additionally, update an order or insert       order items.

- 
**[Place Quote (POST)](./connect_resources_place_quote.htm.md)**  

Create a quote to discover and price products and services.       Additionally, insert, update, or delete a quote line item.

- 
**[Place Sales Transaction (POST)](./connect_resources_place_sales_transaction.htm.md)**  

Create a sales transaction, such as an order or a quote, with       integrated pricing and configuration. Also, update an order or a quote, and insert and delete       order or quote line items to calculate the estimated tax.

- 
**[Place Supplemental Transaction (POST)](./connect_resources_place_supplemental_transaction.htm.md)**  

Create a supplemental order or change orders after they are submitted       for processing, such as during the fulfillment process.

- 
**[Read Sales Transaction (POST)](./connect_resources_read_sales_transaction.htm.md)**  

Retrieve sales transaction data efficiently from an initialized or a       hydrated context.

- 
**[Retrieve Sales Transaction API Errors (GET)](./connect_resources_retrieve_place_sales_transaction_error.htm.md)**  

Retrieve any asynchronous error details associated with       a sales transaction request.

- 
**[Create Ramp Deal (POST)](./connect_resources_create_ramp_deal.htm.md)**  

Create a ramp deal for a customer on a product. Sales reps can use       ramp deals to provide yearly deals to a customer, resulting in long-term revenue and customer       relationship. A customer can create, update, or view multiple segments of periods for their       subscription term with different attributes for each segment.

- 
**[Delete Ramp Deal (POST)](./connect_resources_delete_ramp_deal.htm.md)**  

Delete a ramp deal to convert a ramped product to include a single       quote line item or order item.

- 
**[Update Ramp Deal (POST)](./connect_resources_update_ramp_deal.htm.md)**  

Modify a ramp deal in scenarios where a segment has updates such as       quantity, discount, or date change.

- 
**[View Ramp Deal (GET)](./connect_resources_view_ramp_deal.htm.md)**  

View a ramp deal related to a quote line item or an order     item.

=== ARTICLE: qoc_flow_metadata_api.htm ===
---
page_id: qoc_flow_metadata_api.htm
title: Flow for Transaction Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Transaction Management

The flow for Transaction Management represents the metadata associated with a flow.
    With Flow, you can create an application that takes users through a series of pages to query and
    update the records in the database. You can also run logic and provide branching capability
    based on user input to build dynamic applications.

    

## FlowActionCall

Transaction Management exposes additional actionType
        values for the FlowActionCall metadata type.

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 
- 
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
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values for Transaction Management are: `createContract`—Create a contract from a specific quote record. `createOrderFromQuote`—Create a draft order from a quote record. `createServiceDocument`—Create service documents from work orders, work order line items, or service appointments. `deepCloneSalesTransaction`—Clone a quote or an order, including full object graph with related objects, selected lines, or selected groups. Added in API version 67.0 and later. `getRenewableAssetsSummary`—Retrieve details about renewable assets in a given order. You can use this information to create renewal opportunities. Added in API version 64.0 and later. `createOrUpdateAssetFromOrder`—Create an asset for each order item in the specified order. New assets are created for a new order. Modify existing assets for change order requests, such as a renewal or a cancellation. `createOrUpdateAssetFromOrderItem`—Create assets from individual order items within an order. Track assets after the individual line items of an order reach a certain stage in their lifecycle, such as submitted, fulfilled, or provisioned. If the order item is part of a renewal, an amendment, or a cancellation, existing assets are changed. `initiateAmendment`—Initiate and execute the amendment of an asset. `initiateRenewal`—Initiate and execute the renewal of an asset. `initiateCancellation`—Initiate and execute the cancellation of an asset. `initiateRollBackLastAction`—Initiate the reversal of the last action on an asset to rectify any transactional errors or to meet changing business requirements. `createOrdersFromQuote`—Create multiple orders from a single quote instead of a single order, ensuring easier order management and fulfillment operations. `initiateTransfer`—Transfer an asset or multiple assets from one account to another. |

/

=== ARTICLE: qoc_invocable_actions_parent.htm ===
---
page_id: qoc_invocable_actions_parent.htm
title: Transaction Management Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Standard Invocable Actions

Learn more about the standard invocable actions available with Transaction
    Management.

- 
**[Create Contract Action](./actions_obj_create_contract_from_quote.htm.md)**  

Create a contract from a specific quote record.

- 
**[Create or Update Asset From Order Action](./actions_obj_create_update_asset_from_order.htm.md)**  

Create an asset for each order item in the specified order. New 			assets are created for a new order. Modify existing assets for change order requests, 			such as a renewal or a cancellation.

- 
**[Create or Update Asset From Order Item Action](./actions_obj_create_update_asset_from_order_item.htm.md)**  

Create assets from individual order items within an order. Track 			assets after the individual line items of an order reach a certain stage in their 			lifecycle, such as submitted, fulfilled, or provisioned. If the order item is part of a 			renewal, an amendment, or a cancellation, existing assets are changed. 

- 
**[Create Order From Quote Action](./actions_obj_create_order_from_quote.htm.md)**  

Create a draft order from a quote record.

- 
**[Create Orders From Quote Action](./actions_obj_create_orders_from_quote.htm.md)**  

Create multiple orders from a single quote instead of a single             order, ensuring easier order management and fulfillment operations.

- 
**[Deep Clone Sales Transaction](./actions_obj_deep_clone_sales_transaction.htm.md)**  

Clone a quote or an order, including full object graph with related 			objects, selected lines, or selected groups.

- 
**[Get Renewable Assets Summary Action](./actions_obj_get_renewable_assets_summary.htm.md)**  

Retrieve details about renewable assets in a given order. You can             use this information to create renewal opportunities.

- 
**[Initiate Amendment Action](./actions_obj_amend_assets.htm.md)**  

Initiate and execute the amendment of an asset.

- 
**[Initiate Cancellation Action](./actions_obj_cancel_assets.htm.md)**  

Initiate and execute the cancellation of an asset.

- 
**[Initiate Renewal Action](./actions_obj_renew_assets.htm.md)**  

Initiate and execute the renewal of an asset.

- 
**[Initiate Rollback on Last Action](./actions_obj_initiate_rollback_last_action.htm.md)**  

Initiate the reversal of the last action on an asset to rectify any             transactional errors or to meet changing business requirements.

- 
**[Initiate Transfer Action](./actions_obj_initiate_transfer.htm.md)**  

Transfer an asset or multiple assets from one account to             another.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

=== ARTICLE: qoc_metadata_api_parent.htm ===
---
page_id: qoc_metadata_api_parent.htm
title: Transaction Management Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Transaction Management](./qoc_flow_metadata_api.htm.md)**  

The flow for Transaction Management represents the metadata associated with a flow.     With Flow, you can create an application that takes users through a series of pages to query and     update the records in the database. You can also run logic and provide branching capability     based on user input to build dynamic applications.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: qoc_overview.htm ===
---
page_id: qoc_overview.htm
title: Transaction Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management

Configure, price, and sell products with Transaction Management in Revenue Management.
  Transaction Management supports subscription lifecycles and ensures end-to-end integrity of your
  quotes and orders.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Cloud where Transaction Management is enabled |

  

 

- 
**[Transaction Management Standard Objects](./quote_and_order_capture_standard_objects.htm.md)**  

The Transaction Management data model provides objects and fields to manage     transactions.

- 
**[Transaction Management Fields on Standard Objects](./quote_and_order_capture_fields_on_standard_objects.htm.md)**  

Transaction Management adds standard and custom fields to some standard       Salesforce objects. These fields are available only in orgs where Transaction Management is       enabled.

- 
**[Transaction Management Tooling API Objects](./quote_and_order_capture_tooling_api_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

- 
**[Transaction Management Platform Event](./quote_and_order_capture_platform_event.htm.md)**  

Use the QuoteSaveEvent event to notify subscribers after saving of a quote is   processed.

- 
**[Transaction Management Business APIs](./qoc_business_apis.htm.md)**  

Use the Transaction Management Business APIs to fetch instant pricing data on a quote     or an order, to create a quote, or to create an order.

- 
**[Transaction Management Apex Reference](./qoc_apex_reference.htm.md)**  

Use built-in Apex classes and interfaces grouped by     namespace.

- 
**[Transaction Management Standard Invocable Actions](./qoc_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Transaction     Management.

- 
**[Transaction Management Metadata API Types](./qoc_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

#### See Also

- [*Salesforce Help*: Permissions for Quote and Order Capture](https://help.salesforce.com/s/articleView?id=ind.qocal_permissions_for_quote_and_order_capture.htm&type=5&language=en_US)

=== ARTICLE: quote_and_order_capture_fields_on_object_state_definition.htm ===
---
page_id: quote_and_order_capture_fields_on_object_state_definition.htm
title: Transaction Management Fields on Object State Definition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_object_state_definition.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Object State Definition

      Standard and custom fields extend the standard Object State Definition object
         for use in Transaction Management to represent the object state model for a particular
         status field for an entity.  This object is available in API version 60.0 and later. 

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| AppUsageType | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** This field indicates under which AppUsageType the transition applies to. For example, ObjectStateDefinition associated with “Revenue Lifecycle Management” AppUsageType will apply to quotes, assets, or orders associated with “Revenue Lifecycle Management”. |

=== ARTICLE: quote_and_order_capture_fields_on_object_state_transition.htm ===
---
page_id: quote_and_order_capture_fields_on_object_state_transition.htm
title: Transaction Management Fields on Object State Transition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_object_state_transition.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Object State Transition

      Standard and custom fields extend the standard Object State Transition object
         for use in Transaction Management to define the valid transition between two statuses.
      This object is available in API version 60.0 and later. 

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| CustomPermissionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the associated custom permission. This field is a relationship field. **Relationship Name** CustomPermission **Relationship Type** Lookup **Refers To** CustomPermission |

=== ARTICLE: quote_and_order_capture_fields_on_object_state_value.htm ===
---
page_id: quote_and_order_capture_fields_on_object_state_value.htm
title: Transaction Management Fields on Object State Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_object_state_value.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Object State Value

      Standard and custom fields extend the standard Object State Transition object
         for use in Transaction Management This object is available in API version 60.0 and
      later. 

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| CustomPermissionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the associated custom permission. This field is a relationship field. **Relationship Name** CustomPermission **Relationship Type** Lookup **Refers To** CustomPermission |

=== ARTICLE: quote_and_order_capture_fields_on_order.htm ===
---
page_id: quote_and_order_capture_fields_on_order.htm
title: Transaction Management Fields on Order
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_order.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Order

Standard and custom fields extend the standard Order object for use
         in Transaction Management.

      

## Special Access Rules

         
         

To view these fields, you must have the Revenue Cloud Advanced license. See [Order](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_order.htm) for fields on the platform
            object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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
- 
- 
- 
- 
- 
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
| AdjustmentDistributionLogic | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies how the overall discount amount distributes among all the order line items that have prices associated with them. The amount distributed is either the value specified in the AppliedDiscountAmount field or the difference between the values in the calculated TotalAmount and the user-specified TotalAmountOverride fields. Valid values are: `Equal`—Distributes the discount amount equally among all the order items. `Proportionate`—Distributes the discount amount in proportion to the ListPriceTotal values of the order items. Available in API version 65.0 and later. |
| AppliedDiscount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The discount amount that’s distributed among all the order items that have prices associated with them. This amount is distributed based on the logic specified in the AdjustmentDistributionLogic field. Available in API version 65.0 and later. |
| AppliedDiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The percent discount applied to each order item. Available in API version 65.0 and later. |
| CalculationStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of the price and tax calculations for the order. Valid values are: `CompletedWithPricing`—Indicates that pricing is complete and tax will now be calculated. `CompletedWithTax`—Indicates that pricing and tax calculation are complete. `CompletedWithoutPricing`—Indicates that pricing and tax calculation were skipped. For a sales rep, this value appears as Unknown on the order page. `ConfigurationFailed`—Indicates that configuration failed. Available in API version 62.0 `ConfigurationInProgress`—Indicates that the configuration is in progress. Available in API version 62.0 `GroupRampConfigurationFailed`—Indicates that the checks for group ramps have failed. Available in API version 65.0 and later. `OrderRequestFailed`—Indicates that the requested order changes weren’t saved. Available in API version 62.0 `OrderRequestPartiallySaved`—Indicates that the requested order changes were partially saved. Available in API version 62.0 `PriceCalculationFailed`—Indicates that pricing failed. `ReconciliationFailed`—Indicates that the arrangement of order data failed. Available in API version 62.0 `ReconciliationInProgress`—Indicates that the arrangement of data is in progress. For a sales rep, this value appears as Saving on the order page. Available in API version 62.0 `SaveFailedOrIncomplete`—Indicates that the recent changes to the order weren’t saved. For a sales rep, this value appears as Some Records Weren’t Saved on the order page. `TaxCalculationFailed`—Indicates that pricing is complete but tax calculation failed. `TaxCalculationWaiting`—Indicates that pricing is complete and a request sent to the tax engine, but tax calculation isn’t complete. This read-only field is available in API version 61.0 and later. |
| DiscountPercent | **Type** percent **Properties** Filter, Nillable, Sort **Description** The percentage of discount applied to the order. The discount percent calculation is ((TotalRoundedLineAmount - TotalAmount) / TotalRoundedLineAmount) * 100. Available in API version 60.0 and later. |
| FulfillmentPlanId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique ID of the fulfillment plan associated with the order. This field is a relationship field. This field is available only in orgs where Dynamic Revenue Orchestrator is enabled. Available in API version 60.0 and later. **Relationship Name** FulfillmentPlan **Relationship Type** Lookup **Refers To** FulfillmentPlan |
| LastPricedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the order price was last calculated. Available in API version 60.0 and later. |
| OrchestrationSbmsStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of order submission for orchestration. This field is available only in orgs where Dynamic Revenue Orchestrator is enabled. Valid values are: `Completed` `Rejected` `Submitted` This read-only field is available in API version 61.0 and later. |
| OriginalActionType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the action that created the order. Valid values are: `Amend`—Indicates that the order was created to amend assets. `Cancel`—Indicates that the order was created to cancel assets. `Renew`—Indicates that the order was created to renew assets. `Transfer`—Indicates that the order was created to transfer assets. Available in API version 61.0 and later. |
| SalesTransactionTypeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The foreign key to the Sales Transaction Type object. Available in API version 61.0 and later. This field is a relationship field. **Relationship Name** SalesTransactionType **Relationship Type** Lookup **Refers To** SalesTransactionType |
| TotalAmountOverride | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The value that the TotalAmount field must be set to by applying overall discounts. Transaction Management calculates the overall discount amount by finding the difference between the value in the calculated TotalAmount field and the value in this field. It then uses the logic specified in the AdjustmentDistributionLogic field to distribute the discount amount among all the order items that have prices associated with them. Available in API version 65.0 and later. |
| TotalRoundedLineAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of all line items in an order without pricing adjustments, such as discounts or tax calculations. Available in API version 60.0 and later. |
| TransactionType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of order being processed. The valid value is: `AdvancedConfigurator`—Indicates that the order must be processed by using the configuration rules and constraints set up in Constraint Rules Engine. Available in API version 61.0 and later. |
| ValidationResult | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the order was configured and priced. Orders can be activated only after they’re configured and priced. Valid values are: `MissingContributor`—Indicates that the order contains a derived product but not its pricing source. `TransactionIncomplete`—Indicates that the order wasn’t configured and priced. Available in API version 61.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_order_action.htm ===
---
page_id: quote_and_order_capture_fields_on_order_action.htm
title: Transaction Management Fields on Order Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_order_action.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Order Action

Standard and custom fields extend the standard Order Action object for use in
         Transaction Management. This object is available in API version 55.0 and
      later.

      

## Special Access Rules

         
         

To view these fields, you must have the Revenue Cloud Advanced license. See [Order Action](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_orderaction.htm) for fields on the Salesforce
            platform object.

      

      

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
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The business action that created the order product. Valid values are: `Add` `Amend` `Cancel` `No Change`—A child product was added to the bundle, but the top-level product in the bundle was otherwise unchanged. `Renew` |

=== ARTICLE: quote_and_order_capture_fields_on_order_item.htm ===
---
page_id: quote_and_order_capture_fields_on_order_item.htm
title: Transaction Management Fields on Order Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_order_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Order Item

      Standard and custom fields extend the standard Order Item object for use in
         Transaction Management.

      

## Special Access Rules

         
         

These fields require the Revenue Cloud Advanced license. See [Order Item](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_orderitem.htm) for fields on the Salesforce
            platform object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ApplUnitPriceUpliftPct | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price uplift percent that’s applied to the order item, used for ramp pricing. This field is available in API version 68.0 and later. |
| CustomProductName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The custom name of a product that's used to override the product name. The maximum supported length is 80 characters. Available in API version 61.0 and later. |
| Discount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The manual discount percentage for the order item. Available in API version 60.0 and later. |
| DiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The manual discount amount for the order item. Available in API version 60.0 and later. |
| EffectiveGrantDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date when the resources associated with the order item are granted. |
| EndDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The end date and time of the order item, which is calculated by using the values in the EndDate, EndTime, and ServiceEndTimeZone fields. If the EndTime field doesn’t have a value, 23:59:59 is used for the calculation. If the ServiceEndTimeZone field doesn’t have a value, GMT is used for the calculation. Available in API version 65.0 and later. |
| EndQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The revised quantity of the item after adjusting changes. The field is read-only. It’s calculated by adding the Start Quantity and the Quantity fields. Available in API version 60.0 and later. |
| EndTime | **Type** time **Properties** Create, Filter, Nillable, Sort, Update **Description** The end time of the order item. Available in API version 65.0 and later. |
| Margin | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin percentage, specified by the sales representative at the line item level. Available in API version 65.0 and later. |
| MarginAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin amount specified by the sales representative at the line item level. Available in API version 65.0 and later. |
| NetTotalPrice | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The total price after applying all price adjustments. Available in API version 60.0 and later. |
| OrderItemGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The order item group associated with the order item. This field is a relationship field. **Relationship Name** OrderItemGroup **Refers To** OrderItemGroup |
| PartnerDiscountPercent | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The discount percentage given to the partner for the order item. Available in API version 60.0 and later. |
| PartnerUnitPrice | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price after applying the discount given to the partner for the order item. Available in API version 60.0 and later. |
| PriceWaterfallIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing of this order item record. Available in API version 60.0 and later. |
| RampUpliftType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The pricing uplift calculation type for ramp segments. Valid values are: `Compound` `Standard` This field is available in API version 68.0 and later. |
| SegmentType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The duration type of the segment. You can use this field from Revenue Management only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned on. Valid values are: `Custom`—Available in API version 65.0 and later. `Prorated`—Available in API version 67.0 and later. `Trial`—Available in API version 67.0 and later. `Yearly`—Available in API version 65.0 and later. The default value is `Yearly`. |
| ServiceDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The start date and time of the order item, which is calculated by using the values in the ServiceDate, ServiceTime, and ServiceEndTimeZone fields. If the ServiceTime field doesn’t have a value, 00:00:00 is used for the calculation. If the ServiceEndTimeZone field doesn’t have a value, GMT is used for the calculation. Available in API version 65.0 and later. |
| ServiceEndTimeZone | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The time zone for the order item's start and end dates, times, and datetimes. Available in API version 65.0 and later. |
| ServiceTime | **Type** time **Properties** Create, Filter, Nillable, Sort, Update **Description** The start time of the order item. Available in API version 65.0 and later. |
| StartQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The quantity available on the order item start date. Available in API version 60.0 and later. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The status of the order item. Available in API version 60.0 and later. |
| SubscriptionTerm | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of terms in the subscription for the item. The unit of the subscription term is stored in the PricingTermUnit field of this order item’s related product selling model record (OrderItem.ProductSellingModel.PricingTermUnit). Available in API version 61.0 and later. |
| SupplementalChangeType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the order item change type in the supplemental order. Possible values are: `Add` `Amend` `Cancel` `No Change` This field is available in API version 64.0 and later. |
| TotalAdjustment | **Type** percent **Properties** Filter, Nillable, Sort **Description** The total discount percentage applied at the line item level. This percentage is calculated by using the formula: (Total Line Amount - Net Total Price) / Total Line Amount. Available in API version 65.0 and later. |
| TotalCost | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total cost of all products sold in the order is calculated by multiplying the quantity by the unit cost. Available in API version 65.0 and later. |
| TotalMargin | **Type** percent **Properties** Filter, Nillable, Sort **Description** The effective margin percentage at the line item level. This percentage is calculated by using the formula: (Net Total Price - Total Cost) / Net Total Price. Available in API version 65.0 and later. |
| TotalMarginAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The effective margin amount at the line item level. This amount is calculated by subtracting total cost from net total price. Available in API version 65.0 and later. |
| UnitCost | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit cost of a product sold as part of the order. Available in API version 65.0 and later. |
| ValidationResult | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the order item was configured and priced. An order can be activated only after all its order items are configured and priced. Valid value is: `Warning`—Indicates that the order item isn’t configured and priced. Available in API version 60.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_order_item_group.htm ===
---
page_id: quote_and_order_capture_fields_on_order_item_group.htm
title: Transaction Management Fields on Order Item Group
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_order_item_group.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Order Item Group

Standard and custom fields extend the standard Order Item Group object
   for use in Transaction Management.

  

## Special Access Rules

   
   

These fields require the Revenue Cloud Advanced license. See [Order Item Group](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_orderitemgroup.htm) for fields on the platform
    object.

  

  

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

      

     

    
| Field | Details |
| --- | --- |
| Discount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount percentage, specified by the sales representative at the group level. Available in API version 65.0 and later. |
| DiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount amount specified by the sales representative at the group level. Available in API version 65.0 and later. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The end date of the group. If the IsRamped field is set to `true`, Transaction Management sets this date as the end date of all the line items in the group that have the Term-Defined product selling model. Available in API version 65.0 and later. |
| IsRamped | **Type** boolean **Properties** Create, Defaulted on Create, Filter, Group, Sort, Update **Description** Indicates whether the group is a group ramp segment, which is a period in a group ramp schedule with specific products, quantities, and discounts. You can use this field from Revenue Management only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned on. The default value is `false`. Available in API version 65.0 and later. |
| Margin | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin percentage, specified by the sales representative at the group level. Available in API version 65.0 and later. |
| MarginAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin amount specified by the sales representative at the group level. This amount can also be considered as the summary margin amount calculated by subtracting the total cost from the summary subtotal. Available in API version 65.0 and later. |
| ParentOrderItemGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the parent group for a nested quote line group. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** ParentOrderItemGroup **Refers To** OrderItemGroup |
| RampUpliftType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The pricing uplift calculation type for ramp segments. Valid values are: `Compound` `Standard` This field is available in API version 68.0 and later. |
| SegmentType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The duration type of the segment. You can use this field from Revenue Management only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned on. Valid values are: `Custom`—Available in API version 65.0 and later. `Prorated`—Available in API version 67.0 and later. `Trial`—Available in API version 67.0 and later. `Yearly`—Available in API version 65.0 and later. |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The start date of the group. If the IsRamped field is set to `true`, Transaction Management sets this date as the start date of all the line items in the group. Available in API version 65.0 and later. |
| SummaryTotalAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The aggregated total amount of nested group lines before any discounts are applied. Available in API version 65.0 and later. |
| TotalAdjustment | **Type** percent **Properties** Filter, Nillable, Sort **Description** The total discount percentage applied at the group level. This percentage is calculated by using the formula: (Summary Total Amount - Summary Subtotal) / Summary Total Amount. Available in API version 65.0 and later. |
| TotalAdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total discount amount at the group level. This amount is calculated by subtracting the summary subtotal from the summary total amount. Available in API version 65.0 and later. |
| TotalCost | **Type** currency **Properties** Filter, Nillable, Sort **Description** The aggregated total cost of nested group lines. Available in API version 65.0 and later. |
| TotalMargin | **Type** percent **Properties** Filter, Nillable, Sort **Description** The summary margin percentage at the line item level. This percentage is calculated by using the formula: (Summary Subtotal Total Cost) / Summary Subtotal. Available in API version 65.0 and later. |
| TotalMarginAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The summary margin amount calculated at the group level. Available in API version 65.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_order_item_relationship.htm ===
---
page_id: quote_and_order_capture_fields_on_order_item_relationship.htm
title: Transaction Management Fields on Order Item Relationship
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_order_item_relationship.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Order Item Relationship

      Standard and custom fields extend the standard Order Item Relationship object
         for use in Transaction Management. This object is available in API version 58.0 and
      later.

      

## Special Access Rules

         
         

To view these fields, you must have the Revenue Cloud Advanced license. See [Order Item Relationship](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_orderitemrelationship.htm) for fields on the
            platform object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ProductRelatedComponentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The ID of the product that is included in a product bundle, a set, or a product and an add-on. This field is a relationship field. **Relationship Name** ProductRelatedComponent **Relationship Type** Lookup **Refers To** ProductRelatedComponent |

=== ARTICLE: quote_and_order_capture_fields_on_quote.htm ===
---
page_id: quote_and_order_capture_fields_on_quote.htm
title: Transaction Management Fields on Quote
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_quote.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Quote

      Standard and custom fields extend the standard Quote object for use in
         Transaction Management to represent information about quotes. This object is available
      in API version 60.0 and later.

      

## Special Access Rules

         
         

To view these fields, you must have the Revenue Cloud Advanced license. See [Quote](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_quote.htm) for fields on the platform
            object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

                  

               

            
| Field | Details |
| --- | --- |
| AdjustmentDistributionLogic | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies how the overall discount amount is distributed among all the quote line items that have prices associated with them. The amount distributed is either the value specified in the AppliedDiscountAmount field or the difference between the values in the calculated TotalPrice and the user-specified TotalPriceOverride fields. Valid values are: `Equal`—Distributes the discount amount equally among all the quote line items. `Proportionate`—Distributes the discount amount in proportion to the ListPriceTotal values of the quote line items. Available in API version 65.0 and later. |
| AppliedDiscount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percent discount applied to each quote line item. Available in API version 65.0 and later. |
| AppliedDiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The discount amount that’s distributed among all the quote line items that have prices associated with them. This amount is distributed based on the logic specified in the AdjustmentDistributionLogic field. Available in API version 65.0 and later. |
| LastPricedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the quote is last priced. |
| OriginalActionType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the action that created the quote. Valid values are: `Amend`—Indicates that the quote was created to amend assets. `Cancel`—Indicates that the quote was created to cancel assets. `Renew`—Indicates that the quote was created to renew assets. `Transfer`—Indicates that the quote was created to transfer assets. Available in API version 61.0 and later. |
| PartnerAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the related partner account. This field is a relationship field. **Relationship Name** PartnerAccount **Relationship Type** Lookup **Refers To** Account |
| TotalPriceOverride | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The value that the TotalPrice field must be set to by applying overall discounts. Transaction Management calculates the overall discount amount by finding the difference between the value in the calculated TotalPrice field and the value in this field. It then uses the logic specified in the AdjustmentDistributionLogic field to distribute the discount amount among all the quote line items that have prices associated with them. Available in API version 65.0 and later. |
| TotalPriceWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of TotalPrice and TotalTaxAmount. This field is available only when you turn on Add Estimated Tax to Quotes and Orders settings and enable Revenue Cloud in your org. Available in API version 64.0 and later. |
| TotalTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of all taxes. This field is available only when you turn on Add Estimated Tax to Quotes and Orders settings and enable Revenue Cloud in your org. Available in API version 64.0 and later. This field is a calculated field. |
| TransactionType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of quote being processed. Valid value is: `AdvancedConfigurator`—Indicates that the transaction must be processed by using the configuration rules and constraints set up in Constraint Rules Engine. Available in API version 62.0 and later. |
| ValidationResult | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the quote was configured and priced. This field serves as a staleness indicator. When this value is blank, pricing is up-to-date. When this value is set, it signals that the quote needs attention before its pricing can be trusted. Valid values are: `Blank/null`—Specifies that the quote pricing is current and valid. `MissingContributor`—Specifies that the quote contains a derived product but not its pricing source. This occurs when the quote contains derived products without its necessary pricing sources. `TransactionIncomplete`—Specifies that the quote wasn’t configured and priced. This typically occurs when a line item or action is modified outside the standard pricing flow, such as saving changes through a method other than the Place Quote or Place Sales Transaction API. Available in API version 61.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_quote_document.htm ===
---
page_id: quote_and_order_capture_fields_on_quote_document.htm
title: Transaction Management Fields on Quote Document
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_quote_document.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Quote Document

      Standard and custom fields extend the standard Quote Document object for use
         in Transaction Management to represent information about quote documents. This object
      is available in API version 61.0 and later.

      

## Special Access Rules

         
         

To view these fields, you must have the Revenue Cloud Advanced license. See [Quote Document](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_quotedocument.htm) for fields on the Salesforce
            platform object.

      

      

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
- 

: 

                  

               

            
| Field | Details |
| --- | --- |
| Document Template | **Type** String **Properties** Create, Filter, Group, Nillable, Sort **Description** The template ID used for generating the quote document. |
| Status | **Type** Picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The status of the quote document. Possible values are: `Completed` `Failed` `Generating` `In Progress` `None` `Queued` The default value is `None`. |

=== ARTICLE: quote_and_order_capture_fields_on_quote_line_group.htm ===
---
page_id: quote_and_order_capture_fields_on_quote_line_group.htm
title: Transaction Management Fields on Quote Line Group
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_quote_line_group.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Quote Line Group

Standard and custom fields extend the standard Quote Line Group object
   for use in Transaction Management.

  

## Special Access Rules

   
   

These fields require the Revenue Cloud Advanced license. See [Quote Line Group](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_quotelinegroup.htm) for fields on the platform
    object.

  

  

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

      

     

    
| Field | Details |
| --- | --- |
| Discount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount percentage, specified by the sales representative at the group level. Available in API version 65.0 and later. |
| DiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount amount specified by the sales representative at the group level. Available in API version 65.0 and later. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The end date of the group. If the IsRamped field is set to `true`, Transaction Management sets this date as the end date of all the line items in the group that have the Term-Defined product selling model. Available in API version 65.0 and later. |
| IsRamped | **Type** boolean **Properties** Create, Defaulted on Create, Filter, Group, Sort, Update **Description** Indicates whether the group is a group ramp segment, which is a period in a group ramp schedule with specific products, quantities, and discounts. You can use this field from Revenue Management only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned on. The default value is `false`. Available in API version 65.0 and later. |
| Margin | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin percentage, specified by the sales representative at the group level. Available in API version 65.0 and later. |
| MarginAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin amount specified by the sales representative at the group level. This amount can also be considered as the summary margin amount calculated by subtracting the total cost from the summary subtotal. Available in API version 65.0 and later. |
| ParentQuoteLineGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the parent group for a nested quote line group. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** ParentQuoteLineGroup **Refers To** QuoteLineGroup |
| RampUpliftType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The pricing uplift calculation type for ramp segments. Valid values are: `Compound` `Standard` This field is available in API version 68.0 and later. |
| SegmentType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The duration type of the segment. You can use this field from Revenue Management only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned on. Valid values are: `Custom`—Available in API version 65.0 and later. `Prorated`—Available in API version 67.0 and later. `Trial`—Available in API version 67.0 and later. `Yearly`—Available in API version 65.0 and later. |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The start date of the group. If the IsRamped field is set to `true`, Transaction Management sets this date as the start date of all the line items in the group. Available in API version 65.0 and later. |
| SummaryTotalAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The aggregated total amount of nested group lines before any discounts are applied. Available in API version 65.0 and later. |
| TotalAdjustment | **Type** percent **Properties** Filter, Nillable, Sort **Description** The total discount percentage applied at the group level. This percentage is calculated by using the formula: (Summary Total Amount - Summary Subtotal) / Summary Total Amount. Available in API version 65.0 and later. |
| TotalAdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total discount amount at the group level. This amount is calculated by subtracting the summary subtotal from the summary total amount. Available in API version 65.0 and later. |
| TotalCost | **Type** currency **Properties** Filter, Nillable, Sort **Description** The aggregated total cost of nested group lines. Available in API version 65.0 and later. |
| TotalMargin | **Type** percent **Properties** Filter, Nillable, Sort **Description** The summary margin percentage at the line item level. This percentage is calculated by using the formula: (Summary Subtotal Total Cost) / Summary Subtotal. Available in API version 65.0 and later. |
| TotalMarginAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The summary margin amount calculated at the group level. Available in API version 65.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_quote_line_item.htm ===
---
page_id: quote_and_order_capture_fields_on_quote_line_item.htm
title: Transaction Management Fields on Quote Line Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_quote_line_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Quote Line Item

      Standard and custom fields extend the standard Quote Line Item object for use
         in Transaction Management to represent information about line items in a quote. This object
         is available in API version 60.0 and later. 

      

## Special Access Rules

         
         

These fields require the Revenue Cloud Advanced license. See [Quote Line Item](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_quotelineitem.htm) for fields on the Salesforce
            platform object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ApplUnitPriceUpliftPct | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price uplift percent that’s applied to the quote line item, used for ramp pricing. This field is available in API version 68.0 and later. |
| DiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** Specifies the fixed amount discount to apply to the quote line item. |
| EffectiveGrantDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date on which the resources associated with the quote line item are granted. |
| EndDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The end date and time of the quote line item, which is calculated by using the values in the EndDate, EndTime, and StartEndTimeZone fields. If the EndTime field doesn’t have a value, 23:59:59 is used for the calculation. If the StartEndTimeZone field doesn’t have a value, GMT is used for the calculation. Available in API version 65.0 and later. |
| EndQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The quantity available on the quote line item end date. The field is read-only. It’s calculated by adding the Start Quantity and the existing Quantity fields. |
| EndTime | **Type** time **Properties** Create, Filter, Nillable, Sort, Update **Description** The end time of the quote line item. Available in API version 65.0 and later. |
| Margin | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin percentage, specified by the sales representative at the line item level. Available in API version 65.0 and later. |
| MarginAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin amount specified by the sales representative at the line item level. Available in API version 65.0 and later. |
| PartnerDiscountPercent | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The discount percentage given to the partner for the quote line. |
| PartnerUnitPrice | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price after discount given to the partner for the quote line. |
| PriceWaterfallIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing of the detail record. |
| RampUpliftType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The pricing uplift calculation type for ramp segments. Valid values are: `Compound` `Standard` This field is available in API version 68.0 and later. |
| StartDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The start date and time of the quote line item, which is calculated by using the values in the StartDate, StartTime, and StartEndTimeZone fields. If the StartTime field doesn’t have a value, 00:00:00 is used for the calculation. If the StartEndTimeZone field doesn’t have a value, GMT is used for the calculation. Available in API version 65.0 and later. |
| StartEndTimeZone | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The time zone for the quote line item's start and end dates, times, and datetimes. Available in API version 65.0 and later. |
| StartTime | **Type** time **Properties** Create, Filter, Nillable, Sort, Update **Description** The start time of the quote line item. Available in API version 65.0 and later. |
| StartQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort **Description** The quantity available on the quote line item start date. |
| TotalAdjustment | **Type** percent **Properties** Filter, Nillable, Sort **Description** The total discount percentage applied at the line item level. This percentage is calculated by using the formula: (Total Line Amount - Net Total Price) / Total Line Amount. Available in API version 65.0 and later. |
| TotalCost | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total cost of all products sold in the order is calculated by multiplying the quantity by the unit cost. Available in API version 65.0 and later. |
| TotalMargin | **Type** percent **Properties** Filter, Nillable, Sort **Description** The effective margin percentage at the line item level. This percentage is calculated by using the formula: (Net Total Price - Total Cost) / Net Total Price. Available in API version 65.0 and later. |
| TotalMarginAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The effective margin amount at the line item level. This amount is calculated by subtracting total cost from net total price. Available in API version 65.0 and later. |
| UnitCost | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit cost of a product sold as part of the order. Available in API version 65.0 and later. |
| ValidationResult | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the quote line item is configured and priced. A quote can be activated only after all its quote line items are configured and priced. Valid value is: `Warning`—Indicates that the quote line item isn’t configured and priced. Available in API version 60.0 and later. |

=== ARTICLE: quote_and_order_capture_fields_on_standard_objects.htm ===
---
page_id: quote_and_order_capture_fields_on_standard_objects.htm
title: Transaction Management Fields on Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_fields_on_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Fields on Standard Objects

Transaction Management adds standard and custom fields to some standard
      Salesforce objects. These fields are available only in orgs where Transaction Management is
      enabled.

- 
**[Transaction Management Fields on Object State Definition](./quote_and_order_capture_fields_on_object_state_definition.htm.md)**  

       Standard and custom fields extend the standard Object State Definition object          for use in Transaction Management to represent the object state model for a particular          status field for an entity.  This object is available in API version 60.0 and later. 

- 
**[Transaction Management Fields on Object State Transition](./quote_and_order_capture_fields_on_object_state_transition.htm.md)**  

       Standard and custom fields extend the standard Object State Transition object          for use in Transaction Management to define the valid transition between two statuses.       This object is available in API version 60.0 and later. 

- 
**[Transaction Management Fields on Object State Value](./quote_and_order_capture_fields_on_object_state_value.htm.md)**  

       Standard and custom fields extend the standard Object State Transition object          for use in Transaction Management This object is available in API version 60.0 and       later. 

- 
**[Transaction Management Fields on Order](./quote_and_order_capture_fields_on_order.htm.md)**  

Standard and custom fields extend the standard Order object for use          in Transaction Management.

- 
**[Transaction Management Fields on Order Item](./quote_and_order_capture_fields_on_order_item.htm.md)**  

       Standard and custom fields extend the standard Order Item object for use in          Transaction Management.

- 
**[Transaction Management Fields on Order Item Group](./quote_and_order_capture_fields_on_order_item_group.htm.md)**  

Standard and custom fields extend the standard Order Item Group object    for use in Transaction Management.

- 
**[Transaction Management Fields on Order Action](./quote_and_order_capture_fields_on_order_action.htm.md)**  

Standard and custom fields extend the standard Order Action object for use in          Transaction Management. This object is available in API version 55.0 and       later.

- 
**[Transaction Management Fields on Order Item Relationship](./quote_and_order_capture_fields_on_order_item_relationship.htm.md)**  

       Standard and custom fields extend the standard Order Item Relationship object          for use in Transaction Management. This object is available in API version 58.0 and       later.

- 
**[Transaction Management Fields on Quote](./quote_and_order_capture_fields_on_quote.htm.md)**  

       Standard and custom fields extend the standard Quote object for use in          Transaction Management to represent information about quotes. This object is available       in API version 60.0 and later.

- 
**[Transaction Management Fields on Quote Line Group](./quote_and_order_capture_fields_on_quote_line_group.htm.md)**  

Standard and custom fields extend the standard Quote Line Group object    for use in Transaction Management.

- 
**[Transaction Management Fields on Quote Line Item](./quote_and_order_capture_fields_on_quote_line_item.htm.md)**  

       Standard and custom fields extend the standard Quote Line Item object for use          in Transaction Management to represent information about line items in a quote. This object          is available in API version 60.0 and later. 

- 
**[Transaction Management Fields on Quote Document](./quote_and_order_capture_fields_on_quote_document.htm.md)**  

       Standard and custom fields extend the standard Quote Document object for use          in Transaction Management to represent information about quote documents. This object       is available in API version 61.0 and later.

=== ARTICLE: quote_and_order_capture_platform_event.htm ===
---
page_id: quote_and_order_capture_platform_event.htm
title: Transaction Management Platform Event
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_platform_event.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Platform Event

Use the QuoteSaveEvent event to notify subscribers after saving of a quote is
  processed.

          
            

          

          
            

          

        

| Available in: Lightning Experience |
| --- |
| Available in all Salesforce orgs where the admin settings for products related to the use case are enabled. The Salesforce org must have a Revenue Management or Subscription Management license. |

  

- 
**[CreateAssetOrderEvent](./sforce_api_objects_createassetorderevent.htm.md)**  

Notifies subscribers that the process started by the `/actions/standard/createOrUpdateAssetFromOrder` or  `/actions/standard/createOrUpdateAssetFromOrderItem` 			request is complete. If the process is successful, use this event to learn about the new 			assets. If the request isn't successful, use this event to learn about the errors and 			how to fix them. This object is available in API version 55.0 and 		later.

- 
**[PlaceOrderCompletedEvent](./sforce_api_objects_placeordercompletedevent.htm.md)**  

Notifies subscribers of an order being created or updated by invoking 			the Place Order API or the Place Sales Transaction API. This object is available in 		API version 63.0 and later.

- 
**[QuoteSaveEvent](./sforce_api_objects_quotesaveevent.htm.md)**  

Notifies subscribers that the process started by the Place Quote or 			Place Sales Transaction API request is complete. If the process is successful, use this 			event to learn about the updated quote. If the request isn't successful, use this event 			to learn about the errors and how to fix them. This object is available in API 		version 60.0 and later.

- 
**[QuoteToOrderCompletedEvent](./sforce_api_objects_quotetoordercompletedevent.htm.md)**  

Notifies subscribers when the `/actions/standard/createOrderFromQuote` REST request is complete. If the 			request is successful, use this event to learn about the Order record. If the request 			isn’t successful, use this event to learn about the errors associated with the 			request. This object is available in API version 56.0 and later.

=== ARTICLE: quote_and_order_capture_standard_objects.htm ===
---
page_id: quote_and_order_capture_standard_objects.htm
title: Transaction Management Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Standard Objects

The Transaction Management data model provides objects and fields to manage
    transactions.

- 
**[Asset](./sforce_api_objects_asset.htm.md)**  

Represents an item of commercial value, such as a product sold by your company or a competitor, that a customer has purchased.

- 
**[AssetAction](./sforce_api_objects_assetaction.htm.md)**  

       Represents a change made to a lifecycle-managed asset. The fields can’t be          edited. This object is available in API version 50.0 and later. 

- 
**[AssetActionSource](./sforce_api_objects_assetactionsource.htm.md)**  

       Represents an optional way to record what transactions caused changes to          lifecycle-managed assets. Use it to trace financial and other information about asset          actions. This object supports Salesforce order products and work order line items, and          transaction IDs from other systems. The fields can’t be edited. This object is       available in API version 50.0 and later. 

- 
**[AssetActionSrcPriceAdjustment](./sforce_api_objects_assetactionsrcpriceadjustment.htm.md)**  

       Each row represents a junction between an asset and the calculated price          adjustment that's applied to an asset. This object is available in API version 66.0       and later. 

- 
**[AssetContractRelationship](./sforce_api_objects_assetcontractrelationship.htm.md)**  

Represents a relationship between an asset and a contract. This       object is available in API version 60.0 and later.

- 
**[AssetDowntimePeriod](./sforce_api_objects_assetdowntimeperiod.htm.md)**  

     Represents a period during which an asset is not able to perform as expected.       Downtime periods include planned activities, such as maintenance, and unplanned events, such       as mechanical breakdown. This object is available in API version 49.0 and later. 

- 
**[AssetOwnerSharingRule](./sforce_api_objects_assetownersharingrule.htm.md)**  

Represents the rules for sharing an Asset with users other than the          owner. This object is available in API version 33.0 and later.

- 
**[AssetRateAdjustment](./sforce_api_objects_assetrateadjustment.htm.md)**  

Stores the tier rate adjustments for the asset rate card          entries.This object is available in API version 62.0 and later.

- 
**[AssetRateCardEntry](./sforce_api_objects_assetratecardentry.htm.md)**  

Stores the negotiated rate card entries that are associated with an          asset in Revenue Cloud. This object is available in API version 62.0 and       later.

- 
**[AssetRelationship](./sforce_api_objects_assetrelationship.htm.md)**  

Represents a non-hierarchical relationship between assets due to an 			asset modification; for example, a replacement, upgrade, or other circumstance. In 			Revenue Lifecycle Management, this object represents an asset or assets grouped in a 			bundle or set. This object is available in API version 41.0 and later.

- 
**[AssetShare](./sforce_api_objects_assetshare.htm.md)**  

Represents a sharing entry on an Asset. This object is available       in API version 33.0 and later.

- 
**[AssetStatePeriod](./sforce_api_objects_assetstateperiod.htm.md)**  

       Represents a time span when an asset has the same quantity, amount, and          monthly recurring revenue (MRR). An asset has as many asset state periods as there are          changes to it (asset actions) during its lifecycle. The dashboard and related pages show          the current asset state period. The fields can’t be edited. This object is available       in API version 50.0 and later. 

- 
**[AssetStatePeriodAttribute](./sforce_api_objects_assetstateperiodattribute.htm.md)**  

Represents a virtual object that holds the key-value pair of the          asset attribute in a specified asset state period. This object is a child object of          AssetStatePeriod. This object is available in API version 60.0 and later.

- 
**[AssetTag](./sforce_api_objects_assettag.htm.md)**  

Associates a word or short phrase with an Asset.

- 
**[AssetTokenEvent](./sforce_api_objects_assettokenevent.htm.md)**  

The documentation has moved to [AssetTokenEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.platform_events.meta/platform_events/sforce_api_objects_assettokenevent.htm) in the Platform Events Developer Guide.

- 
**[AssetWarranty](./sforce_api_objects_assetwarranty.htm.md)**  

     Defines the warranty terms applicable to an asset along with any exclusions and       extensions. This object is available in API version 50.0 and later. 

- 
**[BindingObjUsageRsrcPlcy](./sforce_api_objects_bindingobjusagersrcplcy.htm.md)**  

Represents the policies that are used for the usage resource that's          associated with an asset or a binding object. This object is available in API version       65.0 and later.

- 
**[ContractItemPrice](./sforce_api_objects_contractitemprice.htm.md)**  

Represents an object that’s used to capture a price for a product on          a contract. This object is available in API version 61.0 and later.

- 
**[ContractItemPriceAdjTier](./sforce_api_objects_contractitempriceadjtier.htm.md)**  

       Represents the tiers of a price adjustment to a product on a contract.       This object is available in API version 63.0 and later. 

- 
**[ContractItemPriceHistory](./sforce_api_objects_contractitempricehistory.htm.md)**  

Represents the history of changes to the values in the fields of a          ContractItemPrice object. This object is available in API version 61.0 and       later.

- 
**[OrderDeliveryMethod](./sforce_api_objects_orderdeliverymethod.htm.md)**  

     Shows the customizations and options that a buyer selected for their delivery       method. This object is available in API version 48.0 and later.  

- 
**[OrderItemAttribute](./sforce_api_objects_orderitemattribute.htm.md)**  

       Represents          a virtual object that stores an attribute specified for an order          item.This object is available in API version 60.0 and later. 

- 
**[OrderItemDetail](./sforce_api_objects_orderitemdetail.htm.md)**  

       Represents the breakdown details of an order product. Revenue Management generates          these records to capture pricing and quantity changes, such as negative quantity          reductions, early renewals, derived pricing or repricing during an amendment, and bundle or          product attribute reconfigurations. This object is available in API version 60.0 and       later. 

- 
**[OrderItemRateAdjustment](./sforce_api_objects_orderitemrateadjustment.htm.md)**  

       Represents the negotiated rate adjustment for an order product. This       object is available in API version 62.0 and later. 

- 
**[OrderItemRateCardEntry](./sforce_api_objects_orderitemratecardentry.htm.md)**  

       Represents the catalog and negotiated rates of a usage metric associated with          an order item that's used to charge overage consumption. This object is available in       API version 62.0 and later. 

- 
**[OrderItemUsageRsrcGrant](./sforce_api_objects_orderitemusagersrcgrant.htm.md)**  

Represents the negotiated grants for the usage resource that's          associated with the usage product added in the order item. This object is available in       API version 65.0 and later.

- 
**[OrderItemUsageRsrcPlcy](./sforce_api_objects_orderitemusagersrcplcy.htm.md)**  

Represents the policies that are used for the usage resource that's          associated with the usage product added in the order item. This object is available in       API version 65.0 and later.

- 
**[SalesTransactionType](./sforce_api_objects_salestransactiontype.htm.md)**  

Represents the type of the sales transaction. This object is       available in API version 61.0 and later. 

- 
**[QuoteAction](./sforce_api_objects_quoteaction.htm.md)**  

Indicates the type of sales transaction that’s being quoted; for          example, a renewal sale. This object is available in API version 59.0 and       later.

- 
**[QuoteItemTaxItem](./sforce_api_objects_quoteitemtaxitem.htm.md)**  

       The tax that is applied to a quote line item. This object is available       in API version 55.0 and later. 

- 
**[QuoteLineDetail](./sforce_api_objects_quotelinedetail.htm.md)**  

       Represents the breakdown details of a quote line item. Revenue Management          generates these records to capture pricing and quantity changes, such as negative quantity          reductions, early renewals, derived pricing or repricing during an amendment, and bundle or          product attribute reconfigurations. This object is available in API version 60.0 and       later. 

- 
**[QuoteLineGroup](./sforce_api_objects_quotelinegroup.htm.md)**  

       Stores the group information for line items in a quote. It also stores the          aggregated line field information (subtotal). It contains a parent-child relationship to          quote. This object is available in API version 61.0 and later. 

- 
**[QuoteLineItemAttribute](./sforce_api_objects_quotelineitemattribute.htm.md)**  

       Represents a virtual object that stores an attribute specified for a quote          line item. This object is available in API version 59.0 and later. 

- 
**[QuotLineItmUseRsrcGrant](./sforce_api_objects_quotlineitmusersrcgrant.htm.md)**  

Represents the negotiated grants for the usage resource that's          associated with the usage product added in the quote line item. This object is       available in API version 65.0 and later.

- 
**[QuotLineItmUsageRsrcPlcy](./sforce_api_objects_quotlineitmusagersrcplcy.htm.md)**  

Represents the policies that are used for the usage resource that's          associated with the usage product added in the quote line item. This object is       available in API version 65.0 and later.

- 
**[QuoteLineRateAdjustment](./sforce_api_objects_quotelinerateadjustment.htm.md)**  

       Represents the negotiated rate adjustment for a quote line item. This       object is available in API version 62.0 and later. 

- 
**[QuoteLineRateCardEntry](./sforce_api_objects_quotelineratecardentry.htm.md)**  

       Represents the catalog and negotiated rates of a usage resource associated          with a quote line item that's used to charge overage consumption. This object is       available in API version 62.0 and later. 

- 
**[QuoteToOpportunitySyncEvent](./sforce_api_objects_quotetoopportunitysyncevent.htm.md)**  

       Represents an asynchronous quote to opportunity synchronization event. It          tracks whether the sync succeeded or failed and notifies associated subscribers upon          completion. This object is available in API version XX.0 and later. 

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: quote_and_order_capture_tooling_api_parent.htm ===
---
page_id: quote_and_order_capture_tooling_api_parent.htm
title: Transaction Management Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/quote_and_order_capture_tooling_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Transaction Management Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

- 
**[TransactionProcessingType](./tooling_api_objects_transactionprocessingtype.htm.md)**  

Represents the settings to configure the processing constraints for a          request.. This object is available in API version 63.0 and later.

=== ARTICLE: sforce_api_objects_asset.htm ===
---
page_id: sforce_api_objects_asset.htm
title: Asset
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_asset.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Asset

Represents an item of commercial value, such as a product sold by your company or a competitor, that a customer has purchased.

		

## Supported Calls

			
			

`create()`, `delete()`, `describeLayout()`,
					`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

		

		

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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** (Required) ID of the Account associated with this asset. Must be a valid account ID. Required if ContactId isn’t specified. This field is a relationship field. **Relationship Name** Account **Relationship Type** Lookup **Refers To** Account |
| Address | **Type** address **Properties** Filter, Nillable **Description** Represents the physical address or geolocation of the asset. |
| AssetLevel | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The asset’s position in an asset hierarchy. If the asset has no parent or child assets, its level is 1. Assets that belong to a hierarchy have a level of 1 for the root asset, 2 for the child assets of the root asset, 3 for their children, and so forth. On assets created before the introduction of this field, the asset level defaults to –1. After the asset record is updated, the asset level is calculated and automatically updated. |
| AssetProvidedById | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The account that provided the asset, typically a manufacturer. This field is a relationship field. **Relationship Name** AssetProvidedBy **Relationship Type** Lookup **Refers To** Account |
| AssetServicedById | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The account in charge of servicing the asset. This field is a relationship field. **Relationship Name** AssetServicedBy **Relationship Type** Lookup **Refers To** Account |
| AssetTypeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset type associated with the asset. This field is a relationship field. This field is available in API version 62.0 and later for users with the Health Cloud Appointment Management permission set. **Relationship Name** AssetType **Relationship Type** Lookup **Refers To** AssetType |
| Availability | **Type** percent **Properties** Filter, Nillable, Sort **Description** The percentage of expected uptime where the asset was available for use. |
| AveragetimetoRepair | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the number of hours it typically takes to repair an asset after a failure. |
| AveragetimeBetweenFailure | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Represents the number of hours that typically elapses before the asset is likely to fail again. |
| AverageUptimePerDay | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The average number of hours per day the asset is expected to be available for use. |
| City | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The city detail for the address. |
| ConsequenceOfFailure | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The business impact associated with the asset’s failure. Using this field, you can address the asset’s health and take action using [Flows](https://help.salesforce.com/s/articleView?id=platform.flow.htm&type=5&language=en_US). To enable this field, use Object Manager to update the field availability. Make sure that the field is visible for field-level security and for page layout. To learn more, see [What Determines Field Access](https://help.salesforce.com/s/articleView?id=platform.customize_fieldaccess.htm&type=5&language=en_US). The picklist values aren’t predefined in orgs created before Winter ’22 that aren’t Field Service enabled. This field is available in API version 53.0 and later. Possible values are: `Insignificant` `Minor` `Moderate` `Major` `Critical` |
| ContactId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Required if AccountId isn’t specified. ID of the Contact associated with this asset. Must be a valid contact ID that has an account parent (but doesn’t need to match the asset’s AccountId). This field is a relationship field. **Relationship Name** Contact **Relationship Type** Lookup **Refers To** Contact |
| Country | **Type** String **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The country detail for the address. |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Three-letter ISO 4217 currency code associated with the invoice. The default value is USD. This field is available in API version 55.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| CurrentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** Reserved for future use. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| CurrentLifecycleEndDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Represents the end of the period shown as current. System-populated field inherited from the end date of the current asset state period. If that field is empty, as with an evergreen subscription, the Current Lifecycle End Date field is also empty. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| CurrentMrr | **Type** currency **Properties** Filter, Nillable, Sort **Description** The asset’s monthly recurring revenue during the current asset state period. System-populated field inherited from the monthly recurring revenue on the current asset state period. If no asset state period is current, the value is `0`. Label is Current Monthly Recurring Revenue. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| CurrentQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The asset’s quantity during the current asset state period. System-populated field inherited from the quantity on the current asset state period. If no asset state period is current, the value is `0`. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** Description of the asset. |
| DigitalAssetStatus | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Status of digital tracking of the asset. The default picklist includes the following values: `On` `Off` `Warning` `Error` |
| ExternalIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the matching record in an external system. This field is available in API version 49.0 and later. |
| GeocodeAccuracy | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Accuracy level of the geocode for the address. |
| HasLifecycleManagement | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** True if this asset is a lifecycle-managed asset, otherwise false. You can’t switch an asset to a lifecycle-managed asset or the reverse. This field is system populated. The default value is `false`.This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| InstallDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Date when the asset was installed. |
| IsCompetitorProduct | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this Asset represents a product sold by a competitor (`true`) or not (`false`). The default value is `false`. Its UI label is Competitor Asset. |
| IsInternal | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates that the asset is produced or used internally (`true`) or not (`false`). The default value is `false`. Its UI label is Internal Asset. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time that the asset was last modified. Its UI label is Last Modified Date. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time that the asset was last viewed. |
| Latitude | **Type** double **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Used with Longitude to specify the precise geolocation of the address. |
| LifecycleEndDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Represents the end of the asset’s lifecycle. System-populated field inherited from the end date of the final asset state period. If that field is empty, as with an evergreen subscription, the lifecycle has no end date. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| LifecycleStartDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Represents the beginning of the asset’s lifecycle. System-populated field inherited from the start date of the earliest asset state period. This field can’t be edited. When a new asset action affects the start date of an asset state period, the period is deleted and a new one is generated. This field is available in API version 50.0 and later. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| LocationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset’s location. Typically, this location is the place where the asset is stored, such as a warehouse or van. If you have access to the location entity, it doesn’t necessarily mean you can access the location id field. To access the location, you must have userHasLocation user access. |
| Longitude | **Type** double **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Used with Latitude to specify the precise geolocation of the address. |
| ManufactureDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date when the asset was manufactured. This field is available from API version 49.0 and later. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** (Required) Name of the asset. Label is Asset Name. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The asset’s owner. By default, the asset owner is the user who created the asset record. Its UI label is Asset Owner. This field is a relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** User |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset’s parent asset. Its UI label is Parent Asset. This field is a relationship field. **Relationship Name** Parent **Relationship Type** Lookup **Refers To** Asset |
| PostalCode | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The postal code for the address. |
| Price | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** Price paid for this asset. |
| PricingSource | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Pricing source to use when amending or renewing an asset. Valid values are: `LastTransaction`—Last Transaction `PriceBookListPrice`—Price Book or List Price Available in API version 60.0 and later. |
| Product2Id | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** (Optional) ID of the Product2 associated with this asset. Must be a valid Product2 ID. Its UI label is Product. This field is a relationship field. **Relationship Name** Product2 **Relationship Type** Lookup **Refers To** Product2 |
| ProductCode | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The product code of the related product. |
| ProductDescription | **Type** string **Properties** Filter, Sort, Nillable **Description** The product description of the related product. |
| ProductFamily | **Type** picklist **Properties** Filter, Group, Sort, Nillable **Description** The product family of the related product. |
| PurchaseDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Date on which this asset was purchased. |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Quantity purchased or installed. The Quantity field value isn’t set by Customer Asset Lifecycle Management. Instead, you can populate the field as you need. |
| QuantityIncreasePricingType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specify which pricing type to use when the quantity of this asset is increased. Its UI label is Pricing Type for Quantity Increase. This field is available in API version 56.0 and later. This field is available when Revenue Cloud is enabled. Possible values are: `LastNegotiatedPrice`—Available in API version 58.0 and later. `ListPrice` |
| RecordTypeId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The unique identifier for the asset. This field is a relationship field. **Relationship Name** RecordType **Relationship Type** Lookup **Refers To** RecordType |
| Reliability | **Type** percent **Properties** Filter, Nillable, Sort **Description** The percentage of expected uptime where the asset wasn’t subject to unplanned downtime. |
| RenewalPricingType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The price used when renewing a subscription. Its UI label is Pricing Type for Renewal. This field is available in API version 55.0 and later. This field is available when Revenue Cloud is enabled. Possible values are: `LastNegotiatedPrice` `ListPrice` |
| RenewalTerm | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** With Renewal Term Unit, defines the default subscription term for renewal quotes. This field is available in API version 55.0 and later. This field is available when Revenue Cloud is enabled. |
| RenewalTermUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit of time for a subscription term. This field is available in API version 55.0 and later. This field is available when Revenue Cloud is enabled. Possible values are: `Annual`—Available in API version 58.0 and later. —UI label is `Years`. `Months` |
| SalesStoreId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the RetailStore or WebStore associated with this Asset. This field is a polymorphic relationship field. To access this field, your org must have a Salesforce Order Management license or a B2B Commerce License. This field is available in API v60.0 and later. **Relationship Name** SalesStore **Relationship Type** Lookup **Refers To** RetailStore, WebStore |
| SerialNumber | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Serial number for this asset. |
| State | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The state detail for the address. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Customizable picklist of values. The default picklist includes the following values: `Purchased` `Shipped` `Installed` `Registered` `Obsolete` |
| StatusReason | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The explanation of the device status. This field is available from API version 49.0 and later. Possible values are: `Not Ready` `Off` `Offline` `Online` `Paused` `Standby` |
| StockKeepingUnit | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The SKU assigned to the related product. |
| Street | **Type** textarea **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The street detail for the address. |
| SumDowntime | **Type** double **Properties** Filter, Nillable, Sort **Description** Accumulated downtime (planned and unplanned), determined as follows: When only UptimeRecordStart is set, the sum of all downtime from UptimeRecordStart When UptimeRecordStart and UptimeRecordEnd are set, the sum of all downtime from UptimeRecordStart to UptimeRecordEnd Otherwise, downtime isn’t accumulated. |
| SumUnplannedDowntime | **Type** double **Properties** Filter, Nillable, Sort **Description** Accumulated unplanned downtime, determined as follows: When only UptimeRecordStart is set, the sum of all unplanned downtime from UptimeRecordStart When UptimeRecordStart and UptimeRecordEnd are set, the sum of all unplanned downtime from UptimeRecordStart to UptimeRecordEnd Otherwise, unplanned downtime isn’t accumulated. |
| TotalLifecycleAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of revenue for the asset, including revenue from each stage in the asset lifecycle. This field is available when CPQ Plus, Salesforce Billing, or Revenue Cloud is enabled. |
| UptimeRecordEnd | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date until which SumDowntime and SumUnplannedDowntime are accumulated. |
| UptimeRecordStart | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date from which SumDowntime and SumUnplannedDowntime are accumulated. |
| UsageEndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Date when usage for this asset ends or expires. |
| Uuid | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique ID for the asset. This field is available in API version 49.0 and later. |

		

		

## Usage

			
			

Use this object to track products sold to customers. With asset tracking, a client
				application can quickly determine which products were previously sold or are
				currently installed at a specific account. You can also create hierarchies of up to
				10,000 assets.

			

For example, suppose that your company wants to renew and upsell opportunities on
				products sold in the past. Similarly, your company can track competitive products in
				a customer environment where products can be replaced or swapped out.

			

Asset tracking is also useful for product support, providing detailed information to
				assist with product-specific support issues. For example, the
					PurchaseDate or SerialNumber can
				indicate whether a given product has certain maintenance requirements, including
				product recalls. Similarly, the UsageEndDate can indicate when
				the asset was removed from service or when a license or warranty expires.

			

If an application creates an Asset record, it must specify a
					Name and either an AccountId,
					ContactId, or both.

		

		

With REST API, use the `getRelatedListInfo` function to get
			information about related lists on the asset. Note that when requesting information
			about `PrimaryAssets`, the response is labeled `Related Assets`, and the response for
				`RelatedAssets` is labeled `Primary
				Assets`.

		

## Associated Objects

			
			

This object has the following associated objects. If the API version isn’t specified,
				those objects are available in the same API versions as this object. Otherwise,
				they’re available in the specified API version and later.

			
				
					

**
[AssetChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm) (API version 44.0)**

					
: Change events are available for the object.

				
				
					

**[AssetFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

					
: Feed tracking is available for the object.

				
				
					

**[AssetHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

					
: History is available for tracked fields of the object.

				
				
					

**[AssetOwnerSharingRule](./sforce_api_objects_assetownersharingrule.htm.md)**

					
: Sharing rules are available for the object.

				
				
					

**[AssetShare](./sforce_api_objects_assetshare.htm.md)**

					
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assetaction.htm ===
---
page_id: sforce_api_objects_assetaction.htm
title: AssetAction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetAction

      Represents a change made to a lifecycle-managed asset. The fields can’t be
         edited. This object is available in API version 50.0 and later. 

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

To use Customer Asset Lifecycle Management APIs,
         you must have the Access Customer Asset Lifecycle Management APIs permission and Read
         access to the Asset, Asset Action, Asset Action Source, and Asset State Period
         objects.

      

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
- 
- 
- 
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
- 
- 
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
- 
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| ActionDate | **Type** dateTime **Properties** Filter, Sort **Description** The date when an asset action change is recorded. This date can differ from the start date of the related asset state period. For example, suppose that a customer cancels a subscription in June, and the subscription expires in October. The date the customer cancels the subscription (June) is the action date of the asset action. The cancellation's effective date (October) is the start date of the asset state period. |
| ActualTaxChange | **Type** currency **Properties** Filter, Nillable, Sort **Description** The rollup of actual tax from all asset action sources. This field is populated by the system. Label is **Change in Actual Tax**. This field is a calculated field. |
| AdjustmentAmountChange | **Type** currency **Properties** Filter, Nillable, Sort **Description** The rollup of adjustment amount from all asset action sources. This field is populated by the system. Label is **Change in Adjustment Amount**. This field is a calculated field. |
| Amount | **Type** currency **Properties** Filter, Sort **Description** The delta in the total asset amount resulting from an asset action. |
| AssetActionNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The ID of the asset action. Label is **Name**. |
| AssetId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the related lifecycle-managed asset. Label is **Asset**. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| CanRollBack | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the last asset action can be rolled back (`true`). If this property is set to `false`, the asset and the last asset action can’t be rolled back. The default value is `false`. This field is available in API version 65.0 and later. |
| CategoryEnum | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The business category of the asset action, for use in reporting. Asset action totals are broken out by the picklist values on this required field, and those totals are in turn reflected on assets. These categories are available and aren’t customizable. Label is **Business Category**. Possible values are: `Cancellations` `Cross-Sells` `Downgrades` Indicates a transition to a lower-level version or tier of an asset. `Downsells` Indicates a negative quantity amendment or a decreased Line Item total price with no change in quantity. `Initial Sale` Indicates that the asset is initially purchased by an account. `Other` `Renewals` `Swaps` Indicates the exchange of one asset for another. Applies to both swapped-out and swapped-in actions. `Terms And Conditions Changes` `Transfers` Indicates that an asset is transferred from one account to another. `Upgrades` Indicates a transition to a higher-level version or tier of an asset. `Upsells` Indicates a positive quantity amendment or an increased Line Item total price with no change in quantity. |
| EstimatedTaxChange | **Type** currency **Properties** Filter, Nillable, Sort **Description** The rollup of estimated tax from all asset action sources. This field is populated by the system. Label is **Change in Estimated Tax**. This field is a calculated field. |
| MrrChange | **Type** currency **Properties** Filter, Sort **Description** The delta in the asset’s monthly recurring revenue resulting from an asset action. For example, suppose that the MRR during an asset state period is $200 and the next asset action adds $100. Then this field’s value is $100. Label is **Change in Monthly Recurring Revenue**. |
| ProductAmountChange | **Type** currency **Properties** Filter, Nillable, Sort **Description** The rollup of product amount from all asset action sources. This field is populated by the system. Label is **Change in Product Amount**. This field is a calculated field. |
| QuantityChange | **Type** double **Properties** Filter, Sort **Description** The delta in the asset quantity resulting from an asset action. For example, suppose that the asset quantity during an asset state period is 20 and the next asset action adds 10. Then this field’s value is 10. Label is **Change in Quantity**. |
| RolledbackAssetAction | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The last asset action rolled back in the current rollback transaction. This field is available in API version 65.0 and later. |
| SubtotalChange | **Type** currency **Properties** Filter, Nillable, Sort **Description** The rollup of subtotal from all asset action sources. This field is populated by the system. Label is **Change in Subtotal**. This field is a calculated field. |
| Subtype | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The subtype of the action on the asset. Valid values are: `DowngradeFrom`—Available in API version 66.0 and later. `DowngradeTo`—Available in API version 66.0 and later. `FieldAmendment` `Rollback` `StartDateAdjustment` `SwapIn`—Available in API version 66.0 and later. `SwapOut`—Available in API version 66.0 and later. `TransferFrom` `TransferTo` `UpgradeFrom`—Available in API version 66.0 and later. `UpgradeTo`—Available in API version 66.0 and later. This field is available in API version 65.0 and later. |
| TotalAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the current and previous asset action amount. This field is populated by the system. This field is a calculated field. |
| TotalCancellationsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Cancellations`. This field is populated by the system. |
| TotalCrossSellsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Cross-Sells`. This field is populated by the system. |
| TotalDowngradesAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Downgrades`. This field is populated by the system and is available in API version 66.0 and later. |
| TotalDownsellsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Downsells`. This field is populated by the system. |
| TotalInitialSaleAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Initial Sale`. This field is populated by the system. |
| TotalMrr | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the monthly recurring revenue for the current and previous asset action. This field is populated by the system. Label is **Total Monthly Recurring Revenue**. |
| TotalOtherAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Other`. This field is populated by the system. |
| TotalQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The sum of the changes in quantity for the current and previous asset action. This field is populated by the system. |
| TotalRenewalsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Renewals`. This field is populated by the system. |
| TotalSwapsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Swaps`. This field is populated by the system and is available in API version 66.0 and later. |
| TotalTermsAndConditionsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Terms and Conditions Changes`. This field is populated by the system. Label is **Total Terms and Conditions Changes Amount**. |
| TotalTransfersAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Transfers`. This field is populated by the system. |
| TotalUpgradesAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Upgrades`. This field is populated by the system and is available in API version 66.0 and later. |
| TotalUpsellsAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of current and previous asset action amounts categorized as `Upsells`. This field is populated by the system. |
| Type | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The REST API used to generate the asset action. This field is populated by the system. Valid values are: `Cancel` `Change` `Convert` `Generate` |

=== ARTICLE: sforce_api_objects_assetactionsource.htm ===
---
page_id: sforce_api_objects_assetactionsource.htm
title: AssetActionSource
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetactionsource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetActionSource

      Represents an optional way to record what transactions caused changes to
         lifecycle-managed assets. Use it to trace financial and other information about asset
         actions. This object supports Salesforce order products and work order line items, and
         transaction IDs from other systems. The fields can’t be edited. This object is
      available in API version 50.0 and later. 

      

## Supported Calls

         
         

`describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`.

      

      

## Special Access Rules

To use Customer Asset Lifecycle Management APIs,
         you must have the Access Customer Asset Lifecycle Management APIs permission and Read
         access to the Asset, Asset Action, Asset Action Source, and Asset State Period
         objects.

      

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

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ActualTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The region-specific tax amount determined at time of the order. This field is not used for price and tax calculations. |
| AdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** An adjustment to the product amount, such as a discount. |
| AssetActionId | **Type** reference **Properties** Filter, Group, Sort **Description** The related asset action, that is, the change caused by an asset action source transaction. This field is a relationship field. **Relationship Name** AssetAction **Relationship Type** Lookup **Refers To** AssetAction |
| AssetActionSourceNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The ID of the asset action source. Label is **Name**. |
| BillingReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ID of the OrderItem or OrderItemDetail record that this AssetActionSource record is created for. |
| BillingTerm | **Type** int **Properties** Defaulted on create, Filter, Group, Nillable, Sort **Description** The number of billing frequency units to combine into a billing period item. This field is available in API version 68.0 and later. |
| Discount | **Type** percent **Properties** Filter, Nillable, Sort **Description** The discount, expressed as a percentage, that's applied to the asset. This field is available in API version 62.0 and later. |
| DiscountAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The discount, expressed as currency, that's applied to the asset. This field is available in API version 62.0 and later. |
| EffectiveGrantDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the resources associated with the asset were granted. This field is available in orgs that have Revenue Cloud when Rate Management is enabled. This field is available in API version 62.0 and later. |
| EndDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The end date of the service or change. |
| EstimatedTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The estimate of the region-specific tax amount made at time of the transaction. |
| ExternalReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ID of an asset action source transaction originating in a system outside of Salesforce. |
| ExternalReferenceDataSource | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** A system outside of Salesforce that contains asset action source transactions. |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the legal entity record associated with the asset action source transaction. This field is a relationship field. This field is available in API version 62.0 and later. **Relationship Name** LegalEntity **Relationship Type** Lookup **Refers To** LegalEntity |
| ListPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** List price for the order product. Value is inherited from the associated PriceBookEntry upon order product creation. |
| NetUnitPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** The final adjusted unit price, inclusive of all adjustments, but exclusive of tax. The unit price after all price adjustments are applied. |
| ObligatedAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** When a line amount is prorated, this amount shows the service amount that’s been consumed. |
| OriginalLineNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of the original order item detail line. Salesforce uses this information to create a record to amend, renew, or cancel an order. This field is available in API version 64.0 and later. **Relationship Name** OrderItemDetail **Relationship Type** Lookup **Refers To** LineNumber |
| PeriodBoundary | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Boundary delimiters for periods. It determines when a period starts and/or ends. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` |
| PeriodBoundaryDay | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number specifying the day number when Period Boundary is a specific day in a week/month/year. It only applies when PeriodBoundary is set to "day of period.” |
| PeriodBoundaryStartMonth | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay when BillingFrequency2 is Annual or by manual user entry. Possible values are: 1-January 2-February 3-March 4-April 5-May 6-June 7-July 8-August 9-September 10-October 11-November 12-December |
| PricebookEntryId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** PricebookEntry is used as a lookup for price information in order to pre-populate OrderItem's ListPrice and UnitPrice. |
| PricingTermCount | **Type** double **Properties** Filter, Nillable, Sort **Description** Number of pricing terms is this subscription product. |
| ProductAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The product amount after the asset action source transaction. |
| ProductSellingModelId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** Specifies the product selling model type. Foreignkey to ProductSellingModel entity. |
| ProrationPolicyId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the ProrationPolicy used for pricing. |
| Quantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The product quantity or the change in product quantity after the asset action source transaction. |
| ReferenceEntityItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of an asset action source transaction originating in Salesforce. The transaction can be an order product or a work order line item. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntityItem **Relationship Type** Lookup **Refers To** OrderItem, WorkOrderLineItem |
| SegmentIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ID of the ramp segment associated with the asset action source transaction. The maximum supported length is 255 characters from API version 67.0 and later. This field is available in API version 62.0 and later. |
| StartDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The start date of the service or change. |
| Subtotal | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the product amount and the adjustment amount. This field is a calculated field. |
| TaxTreatmentId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** Lookup to Tax Treatment entity. It's used to calculate tax. |
| TotalLineAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The price of the line before any price adjustments were applied. SalesTransactionItem: ProratedStartingTotal / StartingPriceTotal. Note: TotalPrice is computed using the UnitPrice, which includes discounts (price adjustments), while TotalLineAmount doesn’t include price adjustments. |
| TotalPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** Calculated by the pricing engine for ARC. Summation of TotalAdjustmentAmount plus TotalLineAmount for this item. |
| TransactionDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date of a source transaction, such as an order date. |
| UnitPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** The unit price of the item before any discounts or tax calculation. |

=== ARTICLE: sforce_api_objects_assetactionsrcpriceadjustment.htm ===
---
page_id: sforce_api_objects_assetactionsrcpriceadjustment.htm
title: AssetActionSrcPriceAdjustment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetactionsrcpriceadjustment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetActionSrcPriceAdjustment

      Each row represents a junction between an asset and the calculated price
         adjustment that's applied to an asset. This object is available in API version 66.0
      and later. 

      
         

         
         

      

      

## Supported Calls

      
      

         `create()`, 
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

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

            

            
| Field | Details |
| --- | --- |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Nillable, Sort **Description** The value of the price adjustment that was applied to the asset. |
| AppliedPriceAdjustmentDate | **Type** dateTime **Properties** Create, Filter, Sort **Description** The date and time on which the price adjustment was applied to the asset. |
| AssetActionSourceId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the asset action source related to the asset for which the price adjustment was applied. This field is a relationship field. **Relationship Name** AssetActionSource **Relationship Type** Master-detail **Refers To** AssetActionSource (the master object) |
| AssetId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the asset that this price adjustment applies to. This field is a relationship field. **Relationship Name** Asset **Refers To** Asset |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the asset price adjustment record. |
| PriceAdjustmentCauseId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the record that caused the price adjustment. This field is a polymorphic relationship field. **Relationship Name** PriceAdjustmentCause **Refers To** Promotion |
| PriceAdjustmentSource | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the source of price adjustment. Possible values are: `Discretionary`—Reserved for future use. `Promotion` `Rule`—Reserved for future use. `System`—Reserved for future use. |
| PrioritySequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort **Description** The priority sequence of the applied price adjustment. |

=== ARTICLE: sforce_api_objects_assetcontractrelationship.htm ===
---
page_id: sforce_api_objects_assetcontractrelationship.htm
title: AssetContractRelationship
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetcontractrelationship.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetContractRelationship

Represents a relationship between an asset and a contract. This
      object is available in API version 60.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the asset related to the contract. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| ContractId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the contract related to the asset. This field is a relationship field. **Relationship Name** Contract **Relationship Type** Lookup **Refers To** Contract |
| EndDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The end date and time of the relationship between contract and asset. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. The associated UI label is **Last Modified Date**. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, the user accessed this record or list view (LastReferencedDate) but didn’t view it. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated number assigned to AssetContractRelationship. (Read Only) |
| StartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The start date and time of the relationship between contract and asset. |

      

      
      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssetContractRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssetContractRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_assetdowntimeperiod.htm ===
---
page_id: sforce_api_objects_assetdowntimeperiod.htm
title: AssetDowntimePeriod
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetdowntimeperiod.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetDowntimePeriod

    Represents a period during which an asset is not able to perform as expected.
      Downtime periods include planned activities, such as maintenance, and unplanned events, such
      as mechanical breakdown. This object is available in API version 49.0 and later. 

    

## Supported Calls

      
      

`create()`, 
`delete()`, 
`describeLayout()`, 
`describeSObjects()`, 
`getDeleted()`, `getUpdated()`, 
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
| AssetDowntimePeriodNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The unique number of this asset downtime period record. |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the asset this asset downtime period record is for. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of this asset downtime period. |
| DowntimeType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of this asset downtime period. Possible values are: `Planned` `Unplanned` |
| EndTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The time this asset downtime period ended. |
| IsExcluded | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Whether this asset downtime period is excluded from the calculation of accumulated downtime and accumulated unplanned downtime, and therefore not included in availability and reliability calculations. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, this record might only have been referenced (LastReferencedDate) and not viewed. |
| StartTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The time this asset downtime period started. |

=== ARTICLE: sforce_api_objects_assetownersharingrule.htm ===
---
page_id: sforce_api_objects_assetownersharingrule.htm
title: AssetOwnerSharingRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetownersharingrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetOwnerSharingRule

Represents the rules for sharing an Asset with users other than the
         owner. This object is available in API version 33.0 and later.

      
         

#### Note

To enable access to this object for your org, contact Salesforce customer support.
            However, we recommend that you instead use Metadata API to programmatically update owner
            sharing rules because it triggers automatic sharing rule recalculation. The [SharingRules](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_sharingrules.htm) Metadata API type is enabled for
            all orgs.

      

      

## Supported Calls

         
         

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

      

      

## Special Access Rules

         
         

Customer Portal users can’t access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AssetAccessLevel | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** A value that represents the type of sharing being allowed. The possible values are: Read Edit |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** A description of the sharing rule. Maximum size is 1000 characters. |
| DeveloperName | **Type** string **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. |
| GroupId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID representing the source group. Cases owned by users in the source group trigger the rule to give access. |
| Name | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label of the sharing rule as it appears in the user interface. Limited to 80 characters. Corresponds to **Label** on the user interface. |
| UserOrGroupId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID representing the target user or group. Target users or groups are given access. |

      

      

## Usage

         
         

Use this object to manage the sharing rules for assets. General sharing uses this
            object.

=== ARTICLE: sforce_api_objects_assetrateadjustment.htm ===
---
page_id: sforce_api_objects_assetrateadjustment.htm
title: AssetRateAdjustment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetrateadjustment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetRateAdjustment

Stores the tier rate adjustments for the asset rate card
         entries.This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`

      

      

## Special Access Rules

         
         

This object is available in orgs where Revenue Cloud is enabled.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AdjustmentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of rate adjustment. Valid values are: `Amount`—Adjusts rate by using a specific amount. `Override`—Adjusts rate by using the override rate. `Percentage`—Adjusts rate by using a percentage. |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** The value of the adjustment. |
| AssetRateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the parent asset rate card entry record associated with the asset rate adjustment. This field is a relationship field. **Relationship Name** AssetRateCardEntry **Relationship Type** Master-detail **Refers To** AssetRateCardEntry (the master object) |
| LowerBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The minimum quantity for the adjustment to be applicable. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the asset rate adjustment. |
| UpperBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The maximum quantity for the adjustment to be applicable. |

=== ARTICLE: sforce_api_objects_assetratecardentry.htm ===
---
page_id: sforce_api_objects_assetratecardentry.htm
title: AssetRateCardEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetratecardentry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetRateCardEntry

Stores the negotiated rate card entries that are associated with an
         asset in Revenue Cloud. This object is available in API version 62.0 and
      later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

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
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the asset rate card entry record. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Master-detail **Refers To** Asset (the master object) |
| BindingObjectFormula | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The formula that returns the ID of the associated binding object, if specified. If binding object isn't added, the formula returns the asset ID of the asset related to this asset rate card entry. This field is read-only. Available in API version 65.0 and later. |
| BindingObjectId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the binding object associated with the asset rate card entry. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** BindingObject **Refers To** Asset |
| BindingObjectRateOrder | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The order that determines the applicable binding object rate when multiple rates are defined for an Anchor binding object within a effective period. Available in API version 65.0 and later. |
| CurrencyIsoCode | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The ID of the binding object associated with the asset rate card entry. Possible values are: AED - UAE Dirham AUD - Australian Dollar BRL - Brazilian Real CAD - Canadian Dollar EUR - Euro GBP - British Pound INR - Indian Rupee JPY - Japanese Yen SEK - Swedish Krona USD - U.S. Dollar The default value is USD. Available in API version 65.0 and later. |
| EndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the rate card's time period becomes inactive. The rate card becomes inactive at 11:59:00 PM on the end date. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An auto-generated number assigned to the asset rate card entry. Read-only. |
| NegotiatedRate | **Type** double **Properties** Create, Filter, Sort, Update **Description** The base negotiated rate used to charge overage consumption. |
| RateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the rate card entry record containing the catalog rates that's associated with the asset rate card entry. This field is a relationship field. **Relationship Name** RateCardEntry **Refers To** RateCardEntry |
| RateCardId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the rate card record that's associated with the asset rate card entry. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the unit of measure record that's associated with the asset rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| StartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date when the rate card's time period becomes active. The rate card becomes active at 12:00:00 AM on the start date. |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the usage resource record that's associated with the asset rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_assetrelationship.htm ===
---
page_id: sforce_api_objects_assetrelationship.htm
title: AssetRelationship
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetrelationship.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetRelationship

Represents a non-hierarchical relationship between assets due to an
			asset modification; for example, a replacement, upgrade, or other circumstance. In
			Revenue Lifecycle Management, this object represents an asset or assets grouped in a
			bundle or set. This object is available in API version 41.0 and later.

		
			

Asset relationships appear in the Primary Assets and Related Assets related lists on
				asset records in the UI.

		

		

## Supported Calls

			
			

`create()`, `delete()`, `describeLayout()`,
					`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

		

		

## Special Access Rules

			
			

Some fields are available only in Revenue Cloud. Field availability is noted in the field
				detail column. 

		

		

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

: 

: 

						

						
							

							

: 

: 

: 

						

						
							

							

: 

: 

: 
: 

						

						
							

							

: 

: 

: 
: 
: 

: 

: 

: 

						

						
							

							

: 

: 

: 
: 
: 

: 

: 

: 

						

						
							

							

: 

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

						

					

				
| Field Name | Details |
| --- | --- |
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The unique identifier of the new asset, which is the asset that is taking the place of the existing asset. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| AssetRelationshipNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An auto-generated number identifying the asset relationship. |
| AssetRole | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Describes the position of the main asset relative to the other assets in the relationship. This field is available in API version 58.0 and later. This field is available in orgs with Revenue Cloud. Possible values are: `Add-on`—The main asset is an add-on. `Bundle`—The main asset is the bundle parent. `Set`—The asset is the main asset in the set. |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Three-letter ISO 4217 currency code associated with the asset. The default value is USD. |
| FromDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the new asset was installed. |
| GroupingKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** Read-only field used to indicate the bundle that an asset belongs to. For example, if two assets have the same GroupingKey value, then it means that the assets are bundled together. This field is available in API v.60.0 and later. This field is available in orgs with Revenue Cloud. |
| ProductRelationshipTypeId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the record that describes the relationship between the main and associated assets. This field is available in API version 58.0 and later. This field is available in orgs with Revenue Cloud. This field is a relationship field. **Relationship Name** ProductRelationshipType **Relationship Type** Lookup **Refers To** ProductRelationshipType |
| ProductRelatedComponent | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The product related component that’s associated with the asset relationship. This field is a relationship field. This field is available in API 60.0 and later in Revenue Cloud. **Relationship Name** ProductRelatedComponent **Relationship Type** Lookup **Refers To** ProductRelatedComponent |
| RelatedAssetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The existing asset that is being modified. This field is a relationship field. **Relationship Name** RelatedAsset **Relationship Type** Lookup **Refers To** Asset |
| RelatedAssetPricing | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the price of the related asset is included in the bundle price. Valid values are: `IncludedInBundlePrice` `NotIncludedInBundlePrice` This field is available in API version 59.0 and later in Revenue Cloud. |
| RelatedAssetQtyScaleMethod | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies how the quantity of the related asset changes relative to the quantity of the parent asset. Valid values are: `Constant` `Proportional` This field is available in API version 59.0 and later in Revenue Cloud. |
| RelatedAssetRole | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Describes the position of the associated asset relative to other assets in the relationship. This field is available in API version 58.0 and later. This field is available in orgs with Revenue Cloud. Valid values are: `Add-on`—The main asset is an add-on. `Bundle`—The main asset is the bundle parent. `Set`—The asset is the main asset in the set. `Simple`—The asset is purchased individually and isn’t associated with variations. `Variation Parent`——The main asset is the variation parent. |
| RelationshipType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Sort, Update **Description** The type of relationship between the existing asset and the new asset. This field comes with three values—Replacement, Upgrade, and Crossgrade—, but you can create more values in Setup. Possible values are: `Crossgrade`—The new asset is a crossgrade of an existing asset. For example, changing a subscription to a plan with the same service, but that runs for a longer amount of time. `Replacement`—The new asset is replacing an existing asset. For example, a customer’s faulty widget that was under warranty is being replaced with a new one. `Upgrade`—The new asset is an upgrade of an existing asset. For example, upgrading a customer’s existing subscription plan to a new plan with more services. The default value is `Replacement`. |
| ToDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the modified asset is uninstalled. |

		

		

## Associated Objects

			
			

This object has the following associated objects. If the API version isn’t specified,
				they’re available in the same API versions as this object. Otherwise, they’re
				available in the specified API version and later.

			
				
					

**
[AssetRelationshipChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm) (API version
						62.0)**

					
: Change events are available for the object.

				
				
					

**[AssetRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

					
: Feed tracking is available for the object.

				
				
					

**[AssetRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

					
: History is available for tracked fields of the object.

				
				
					

**
[AssetRelationshipOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)(API
						version 58.0)**

					
: Sharing rules are available for the object.

				
				
					

**
[AssetRelationshipShare](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm) (API version
						58.0)**

					
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assetshare.htm ===
---
page_id: sforce_api_objects_assetshare.htm
title: AssetShare
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetshare.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetShare

Represents a sharing entry on an Asset. This object is available
      in API version 33.0 and later.

      

You can only create, edit, and delete sharing entries for
            standard objects whose RowCause field is set to `Manual`. Sharing entries for standard objects with
            different RowCause values are created as a result of your
            Salesforce org’s sharing configuration and are read-only. For some sharing mechanisms,
            such as sharing sets, sharing entries aren’t stored at all.

#### Note

While Salesforce currently maintains read-only sharing
            entries for multiple sharing mechanisms, it’s possible that we’ll stop storing certain
            share records to improve performance. As a best practice, don’t create customizations
            that rely on the availability of these sharing entries. Any changes to sharing behavior
            will be communicated before they occur.

      

## Supported Calls

         
         

`describeSObjects()`, `query()`, `retrieve()`

      

      

## Special Access Rules

         
         

Customer Portal users can’t access this object.

      

      

## Fields

         
         

The properties available for some fields depend on the default organization-wide sharing
            settings. The properties listed are true for the default settings of such fields.

         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

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

                  

               

            
| Field | Details |
| --- | --- |
| AssetAccessLevel | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Level of access that the User or Group has to the Asset. The possible values are: Read Edit All This value is not valid for creating or deleting records. This field must be set to an access level that is higher than the organization’s default access level for cases. |
| AssetId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the Asset associated with this sharing entry. This field can't be updated. This is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| IsDeleted | **Type** boolean **Properties** Defaulted on create, Filter **Description** Indicates whether the object has been moved to the Recycle Bin (`true`) or not (`false`). Label is **Deleted**. |
| RowCause | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted value is `Manual`. If no value is specified, the field defaults to `Manual`. All other RowCause values are read-only. After the sharing entry is created, this field can’t be edited. Valid values include: `Manual`—The User or Group has access because a user with “All” access manually shared the Asset with them. `Owner`—The User is the owner of the Asset. `Rule`—The User or Group has access via an Asset sharing rule. `GuestRule`—The User or Group has access via an Asset guest user sharing rule. `LpuImplicit`—The User has access to records owned by high-volume Experience Cloud site users via a share group. |
| UserOrGroupId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the User or Group that has been given access to the Asset. This field can't be updated. This is a polymorphic relationship field. **Relationship Name** UserOrGroup **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Usage

         
         

This object allows you to determine which users and groups can view and edit Asset
            records owned by other users.

         

If you attempt to create a new record that matches an existing record, request updates
            any modified fields and returns the existing record.

=== ARTICLE: sforce_api_objects_assetstateperiod.htm ===
---
page_id: sforce_api_objects_assetstateperiod.htm
title: AssetStatePeriod
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetstateperiod.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetStatePeriod

      Represents a time span when an asset has the same quantity, amount, and
         monthly recurring revenue (MRR). An asset has as many asset state periods as there are
         changes to it (asset actions) during its lifecycle. The dashboard and related pages show
         the current asset state period. The fields can’t be edited. This object is available
      in API version 50.0 and later. 

      

## Supported Calls

         
         

`createable()`, `deletable()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `updateable()`.

      

      

## Special Access Rules

Customer Asset Lifecycle Management APIs require
         the Access Customer Asset Lifecycle Management APIs permission and read access to the
         Asset, Asset Action, Asset Action Source, and Asset State Period objects.

      

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

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
| Amount | **Type** currency **Properties** Createable, Filter, Sort, Updateable **Description** An asset’s total amount during an asset state period. Revenue Management doesn't set or use this field's value currently. |
| ApplUnitPriceUpliftPct | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price uplift percent that’s applied to the asset state period, used for ramp pricing. This field is available in API version 68.0 and later. |
| AssetId | **Type** reference **Properties** Createable, Filter, Group, Sort **Description** The asset related to an asset state period. Label is **Asset**. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| AssetStatePeriodNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The ID of the asset state period. Label is **Name**. |
| BillingFrequency | **Type** picklist **Properties** Createable, Filter, Group, Nillable, Restricted picklist, Sort, Updateable **Description** The time period that indicates how often the line item is billed. Possible values are: `Annual` `Monthly` `Quarterly` `Semi-Annual` Available in API version 65.0 and later. |
| BindingInstanceTargetId | **Type** reference **Properties** Createable, Filter, Group, Nillable, Sort, Updateable **Description** The ID of a custom product target for a usage-based quote line item, order item, or asset allocation. This field is a polymorphic relationship field. **Relationship Name** BindingInstanceTarget **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| Discount | **Type** percent **Properties** Createable, Filter, Nillable, Sort, Updateable **Description** Editable number from 0 to 100. Available in API version 65.0 and later. |
| DiscountAmount | **Type** currency **Properties** Createable, Filter, Nillable, Sort, Updateable **Description** The fixed amount discount to apply to the line item. Available in API version 65.0 and later. |
| EndDate | **Type** dateTime **Properties** Createable, Filter, Nillable, Sort, Updateable **Description** The end date and time of an asset state period. On an asset that is an evergreen subscription, the last asset state period has no end date. |
| LegalEntityId | **Type** reference **Properties** Createable, Filter, Group, Nillable, Sort, Updateable **Description** The ID of the related legal entity. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Mrr | **Type** currency **Properties** Createable, Filter, Sort, Updateable **Description** An asset’s monthly recurring revenue during an asset state period. |
| PriceRevisionPolicy | **Type** reference **Properties** Createable, Filter, Group, Sort, Updateable **Description** Specifies the price uplift policy associated with this asset state period. This field is a relationship field. This field is available in API version 65.0 and later. **Relationship Name** Price Revision Policy **Relationship Type** Lookup **Refers To** PriceRevisionPolicy |
| Quantity | **Type** double **Properties** Createable, Filter, Sort, Updateable **Description** The total quantity of an asset during an asset state period. |
| RampIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ramp record used to group order item segments for this asset state period. This field is available in orgs that have Revenue Management with the Ramp Deals setting enabled. The maximum supported length is 255 characters from API version 67.0 and later. This field is available in API version 62.0 and later. |
| RampUpliftType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The pricing uplift calculation type for ramp segments. Valid values are: `Compound` `Standard` This field is available in API version 68.0 and later. |
| SegmentIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The order item segment for this asset state period. This field is available in orgs that have Revenue Management with the Ramp Deals setting enabled. The maximum supported length is 255 characters from API version 67.0 and later. This field is available in API version 62.0 and later. |
| SegmentName | **Type** string **Properties** Createable, Filter, Group, Nillable, Sort, Updateable **Description** The name of the order item segment for this asset state period. This field is available in orgs that have Revenue Management with the Ramp Deals setting enabled. The maximum supported length is 255 characters from API version 67.0 and later. This field is available in API version 62.0 and later. |
| SegmentType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Updateable **Description** The period for the order item segment for this asset state period. Valid values are: `Custom` `Free Trial` `Yearly` The default value is `Yearly`. This field is available in orgs that have Revenue Management with the Ramp Deals setting enabled. This field is available in API version 62.0 and later. |
| StartDate | **Type** dateTime **Properties** Createable, Filter, Sort, Updateable **Description** The start date and time of an asset state period. |
| UnitPrice | **Type** currency **Properties** Createable, Filter, Nillable, Sort, Updateable **Description** The price per unit for the line item. Available in API version 65.0 and later. Revenue Management won't populate this field in API version 66.0 and later. |
| UnitPriceUplift | **Type** percent **Properties** Createable, Filter, Nillable, Sort, Updateable **Description** Indicates the percentage increase of a line item's unit price. Available in API version 65.0 and later. |

=== ARTICLE: sforce_api_objects_assetstateperiodattribute.htm ===
---
page_id: sforce_api_objects_assetstateperiodattribute.htm
title: AssetStatePeriodAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetstateperiodattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetStatePeriodAttribute

Represents a virtual object that holds the key-value pair of the
         asset attribute in a specified asset state period. This object is a child object of
         AssetStatePeriod. This object is available in API version 60.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

This object is available in Enterprise,
            Unlimited, and Developer Editions of Revenue Cloud with the [Access Lifecycle-Managed Assets user
            permission](https://help.salesforce.com/s/articleView?id=ind.rev_cloud_asset_migration_permission.htm&language=en_US). This object is editable only through API and not the
         UI.

      

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
| AssetStatePeriodId | **Type** reference **Properties** Filter, Group, Sort **Description** The asset state period that's associated with the asset attribute. This field is a relationship field. **Relationship Name** AssetStatePeriod **Relationship Type** Master-detail **Refers To** AssetStatePeriod (the master object) |
| AttributeDefinitionId | **Type** reference **Properties** Filter, Group, Sort **Description** The attribute definition that's associated with the asset state period attribute. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The name of the asset attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The value specified in the picklist type field that corresponds to the attribute in the AttributePicklistValue object. This field is a relationship field. **Relationship Name** AttributePicklistValue **Relationship Type** Lookup **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The value of the asset state period attribute. For example, a shirt can have the value of `blue`, which indicates the shirt's color, or it can have the value of `small`, which indicates the shirt's size. You can use this field to filter records only if the DataType value in the related AttributeDefinitionId record is `Text`. If the DataType value is `Picklist`, use the value in the AttributePicklistValueId field for filtering. You can’t use this field to filter records if the DataType value is `Checkbox`, `Currency`, `Date`, `Datetime`, `Multipicklist`, `Number`, or `Percent`. |

      

      

## Usage

         
         

This object doesn’t support custom fields, validation rules, or triggers. In SOQL
            queries, you can filter records by using Id and
               AttributeDefinition. You can’t use
               AttributeValue in the `WHERE`
            clause.

=== ARTICLE: sforce_api_objects_assettag.htm ===
---
page_id: sforce_api_objects_assettag.htm
title: AssetTag
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assettag.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetTag

Associates a word or short phrase with an Asset.

        

## Supported Calls

            
            

`create()`, `delete()`, `describeSObjects()`,
                    `query()`, `retrieve()`

        

        

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

                        

                    

                
| Field Name | Details |
| --- | --- |
| ItemId | **Type** reference **Properties** Create, Filter **Description** ID of the tagged item. |
| Name | **Type** string **Properties** Create, Filter **Description** Name of the tag. If this value does not already exist, a new TagDefinition is created and becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name becomes the parent of this Tag object. Parent relationships are created automatically. |
| TagDefinitionId | **Type** reference **Properties** Filter **Description** ID of the parent TagDefinition object that owns the tag. |
| Type | **Type** picklist **Properties** Create, Filter, Restricted picklist **Description** Defines the visibility of a tag. Valid values: `Public`—The tag can be viewed and manipulated by all users in an organization. `Personal`—The tag can be viewed or manipulated only by a user with a matching OwnerId. |

        

        

## Usage

            
            

AssetTag stores the relationship between its parent TagDefinition and the Asset being
                tagged. Tag objects act as metadata, allowing users to describe and organize their
                data.

            

When a tag is deleted, its parent TagDefinition will also be deleted if the name is
                not being used; otherwise, the parent remains. Deleting a TagDefinition sends it to
                the Recycle Bin, along with any associated tag entries.

=== ARTICLE: sforce_api_objects_assettokenevent.htm ===
---
page_id: sforce_api_objects_assettokenevent.htm
title: AssetTokenEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assettokenevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetTokenEvent

The documentation has moved to [AssetTokenEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.platform_events.meta/platform_events/sforce_api_objects_assettokenevent.htm) in the Platform Events Developer Guide.

=== ARTICLE: sforce_api_objects_assetwarranty.htm ===
---
page_id: sforce_api_objects_assetwarranty.htm
title: AssetWarranty
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_assetwarranty.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssetWarranty

    Defines the warranty terms applicable to an asset along with any exclusions and
      extensions. This object is available in API version 50.0 and later. 

    

## Supported Calls

      
      

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
          `search()`, `undelete()`, `update()`, `upsert()`

    

    

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
| AssetId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the asset this warranty term applies to. |
| AssetWarrantyNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The identifier of the asset warranty record. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date on which this warranty term expires. |
| ExchangeType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The type of exchange offered by this warranty term. |
| Exclusions | **Type** textarea **Properties** Create, Nillable, Update **Description** Description of any exclusions. |
| ExpensesCovered | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percentage of expenses covered. |
| ExpensesCoveredEndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date on which cover for expenses ends. |
| IsTransferable | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Defines whether the warranty term can be transferred to a new owner. |
| LaborCovered | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percentage of labor covered. |
| LaborCoveredEndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date on which cover for labor ends. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the asset warranty term was last modified. Its label in the user interface is Last Modified Date. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the asset warranty term was last viewed. |
| PartsCovered | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percentage of parts covered. |
| PartsCoveredEndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date on which cover for parts ends. |
| Pricebook2Id | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the price book item associated with this asset warranty term. |
| StartDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date on which cover under this warranty term starts. |
| WarrantyTermId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the warranty term this asset warranty term extends. |
| WarrantyType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The type of the warranty. |

    

    

## Associated Objects

      
      

This object has the following associated objects. If the API version isn’t specified,
        they’re available in the same API versions as this object. Otherwise, they’re available in
        the specified API version and later.

      
        
          

**[AssetWarrantyChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

          
: Change events are available for the object.

=== ARTICLE: sforce_api_objects_bindingobjusagersrcplcy.htm ===
---
page_id: sforce_api_objects_bindingobjusagersrcplcy.htm
title: BindingObjUsageRsrcPlcy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_bindingobjusagersrcplcy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BindingObjUsageRsrcPlcy

Represents the policies that are used for the usage resource that's
         associated with an asset or a binding object. This object is available in API version
      65.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| BindingObjectId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The object that's bounded with the quote line policy or order policy. This field is a polymorphic relationship field. **Relationship Name** BindingObject **Refers To** Account, Asset, BindingObjectCustomExt, Contract |
| DrawdownOrder | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the order that's used to debit consumption of entitlements related to the usage resource from the usage entitlement bucket. Valid values are: `ExpiringFirst` `GrantedFirst` `GrantedLast` |
| EffectiveEndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time until when the policy remains effective. |
| EffectiveStartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when the policy becomes effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated identifier for the quote line item usage resource policy record. For example, BOURP-000004. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the binding object usage resource policy. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rating frequency policy associated with the usage resource. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| UsageAggregationPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage aggregation policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageCommitmentPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage commitment policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageCommitmentPolicy **Refers To** UsageCommitmentPolicy |
| UsageOveragePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage overage policy associated with the usage resource. This field is a relationship field. **Relationship Name** UsageOveragePolicy **Refers To** UsageOveragePolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the usage product. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Binding Object Usage Resource Policy Behavior During Asset
            Operations

When you create or update an order and an asset is created or modified, Usage Management creates
            a Binding Object Usage Resource Policy (BOURP) record per Usage Resource based on the
            Product Usage Resource Policy (PURP) from the asset that's processed first. After the
            BOURP record is created, the policy references remain unchanged regardless of subsequent
            operations.

The Effective Start Date and
            Effective End Date fields extend to accommodate new or renewed assets associated with
            the same Binding Object and Usage Resource. However, the policy fields can't be updated
            after initial BOURP creation.

Here's how each operation affects BOURP creation,
            date ranges, and policy updates.

               
               
               
               
               
               
               
                  
                     

                     

                     

                     

                     

                     

                  

               

               
                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

                  
                     

                     

                     

                     

                     

                     

                  

               

            
| Operation | BOURP Create | Start Date Update | End Date Update | Policy Update | Delete/Expire |
| --- | --- | --- | --- | --- | --- |
| New Sale (first asset for Binding Object) | Yes | — | — | — | — |
| New Sale (subsequent asset, same Binding Object, and Usage Resource) | No | Extends to an earlier date, if applicable | Extends to a later date, if applicable | No | — |
| Renew (existing BOURP) | No | No | Extends to a later date, if applicable | No | — |
| Renew (new Usage Resource on asset) | Yes | — | — | — | — |
| Amend (new Usage Resource on asset) | Yes | — | — | — | — |
| Amend (existing Usage Resource) | No | No | No | No | — |
| Cancel | No | No | No | No | No |

#### Important

 Policy fields on a BOURP record are never updated after the initial record
            is created. If an asset operation introduces a different Product Usage Resource Policy
            for the same Binding Object and Usage Resource combination, the BOURP retains the policy
            from the first asset that was processed. The system doesn’t split BOURP records or
            create multiple BOURPs per Usage Resource and Binding Object combination. 

#### Note

 If you must change the policy for a Usage Resource, you must manually update the existing
            BOURP record or implement custom automation to handle policy changes during specific
            operations.

=== ARTICLE: sforce_api_objects_contractitemprice.htm ===
---
page_id: sforce_api_objects_contractitemprice.htm
title: ContractItemPrice
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_contractitemprice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContractItemPrice

Represents an object that’s used to capture a price for a product on
         a contract. This object is available in API version 61.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to
    align with our company value of Equality. We maintained certain terms to avoid any effect on
    customer implementations. 

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| AdjustmentMethod | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Method used to apply discount. Valid values are: `Range`—Apply the discount to all items after you reach the discount tier. For example, suppose that you give a 10% discount for 50 or more items. If a customer orders 50 products, and the type is `range`, apply the 10% discount to all 50 items. `Slab`—Apply discounts in tiers. For example, suppose that you order 30 products, and the type is `slab`, you can apply a 10% discount to units 1–9, a 20% discount to units 10–19, and a 30% discount to units 20–30. |
| ContractId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the contract. This field is a relationship field. **Relationship Name** Contract **Relationship Type** Master-detail **Refers To** Contract (the master object) |
| DiscountType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of discount applied, a percentage of the price or an amount. Valid values are: `AdjustmentAmount` `AdjustmentPercentage` |
| DiscountValue | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The value of the discount applied, based on the discount type. |
| EndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** End date and time of the relationship between the contract and contract item price. |
| ItemId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the product or product category related to a price in a contract. This field is a polymorphic relationship field. **Relationship Name** Item **Relationship Type** Lookup **Refers To** Product2, ProductCategory |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp when the current user last viewed this record or list view. If this value is null, the user accessed this record or list view (LastReferencedDate) but didn’t view it. |
| ListPrice | **Type** currency **Properties** Filter, Nillable **Description** The list price of the product. This value is read-only and inherited from the price book related to the contract when the contract item price is created. Use the list price to compare the advertised price to prices that customers receive during contract negotiations. This field is available in API version 66.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated number assigned to the contract item price. (Read only) |
| Price | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** Unit price for the product sold as part of the contract. |
| ProductSellingModelId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Product selling model for the product associated with the price. This field is a relationship field. **Relationship Name** ProductSellingModel **Relationship Type** Lookup **Refers To** ProductSellingModel |
| SellingModelType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Selling mode type to specify whether the product sold is a one-time sale, an evergreen subscription, or a subscription with a defined term. Valid values are: `Evergreen` `OneTime` `TermDefined` The value derived from the product selling model. |
| StartDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** Start date and time of the relationship between the contract and contract item price. |

      

      

## Associated Objects

         
         
         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[ContractItemPriceHistory](./sforce_api_objects_contractitempricehistory.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_contractitempriceadjtier.htm ===
---
page_id: sforce_api_objects_contractitempriceadjtier.htm
title: ContractItemPriceAdjTier
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_contractitempriceadjtier.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContractItemPriceAdjTier

      Represents the tiers of a price adjustment to a product on a contract.
      This object is available in API version 63.0 and later. 

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

This object is available with Revenue Management.

      

      

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

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ContractItemPriceId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The contract item price ID associated with the contract item price adjustment tier. This field is a relationship field. **Relationship Name** ContractItemPrice **Relationship Type** Master-detail **Refers To** ContractItemPrice (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp when the current user last viewed this record or list view. If this value is null, the user accessed this record or list view (LastReferencedDate) but didn’t view it. |
| LowerBound | **Type** double **Properties** Create, Filter, Sort, Update **Description** The minimum quantity for the adjustment to be applicable. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| TierType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The type of adjustment tier. Valid values are: `AdjustmentAmount` `AdjustmentPercentage` `OverrideAmount` |
| TierValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** The price adjustment value. |
| UpperBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The maximum quantity for the adjustment to be applicable. |

      

      

## Associated Objects

         
         

This object has associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[ContractItemPriceAdjTierFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ContractItemPriceAdjTierHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_contractitempricehistory.htm ===
---
page_id: sforce_api_objects_contractitempricehistory.htm
title: ContractItemPriceHistory
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_contractitempricehistory.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContractItemPriceHistory

Represents the history of changes to the values in the fields of a
         ContractItemPrice object. This object is available in API version 61.0 and
      later.

      

## Supported Calls

         
         

            `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
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
- 
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

                  

               

            
| Field | Details |
| --- | --- |
| ContractItemPriceId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the ContractItemPrice record. This field is a relationship field. **Relationship Name** ContractItemPrice **Relationship Type** Lookup **Refers To** ContractItemPrice |
| DataType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Data type of the field that was changed. Valid values are: `Address` `AnyType` `AutoNumber` `Base64` `BitVector` `Boolean` `Content` `Currency` `DataCategoryGroupReference` `DateOnly` `DateTime` `Division` `Double` `DynamicEnum` `Email` `EncryptedBase64` `EncryptedText` `EntityId` `EnumOrId` `ExternalId` `Fax` `File` `HtmlMultiLineText` `HtmlStringPlusClob` `InetAddress` `Json` `Location` `MultiEnum` `MultiLineText` `Namespace` `Percent` `PersonName` `Phone` `Raw` `RecordType` `SfdcEncryptedText` `SimpleNamespace` `StringPlusClob` `Switchable_PersonName` `Text` `TimeOnly` `Url` `YearQuarter` |
| Field | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Name of the field that was changed. Possible values are: `AdjustmentMethod` `Contract` `DiscountType` `DiscountValue` `EndDate` `Item` `Name` `Price` `ProductSellingModel` `StartDate` `created` `customPersonMerged` `feedEvent` `individualMerged` `locked`—Record locked. `ownerAccepted`—Owner (Accepted) `ownerAssignment`—Owner (Assignment) `unlocked`—Record unlocked. |
| NewValue | **Type** anyType **Properties** Nillable, Sort **Description** New value of the field that was changed. |
| OldValue | **Type** anyType **Properties** Nillable, Sort **Description** Latest value of the field before it was changed. |

=== ARTICLE: sforce_api_objects_createassetorderdtlevent.htm ===
---
page_id: sforce_api_objects_createassetorderdtlevent.htm
title: CreateAssetOrderDtlEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_createassetorderdtlevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: sforce_api_objects_createassetorderevent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreateAssetOrderDtlEvent

Contains information about an attempt to create or update an asset as a
			result of `/actions/standard/createOrUpdateAssetFromOrder`. If the request was
			successful, the event shows information about the asset. If the request failed, the
			event shows error information. This object is included in an `CreateAssetOrderEvent` message. You can't subscribe to
			`CreateAssetOrderDtlEvent` directly. This object is
		available in API version 55.0 and later.

		

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

		

		

## Subscription Channel

			
			

`/event/CreateAssetOrderDtlEvent`

		

		

## Special Access Rules

			
			

This object is available if Revenue Cloud is installed in your org. Users must have Read
				access on this event to receive or view event notifications.

		

		

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
| AssetId | **Type** reference **Properties** Nillable **Description** The ID of the asset that was created or updated. This field is a relationship field. **Relationship Name** Asset **Relationship Type** Lookup **Refers To** Asset |
| ErrorCode | **Type** string **Properties** Nillable **Description** Reference code for the type of error that occurred. |
| ErrorMessage | **Type** string **Properties** Nillable **Description** Information about the error that occurred after the request was made. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| IsSuccess | **Type** boolean **Properties** Defaulted on create **Description** Indicates whether the request to create the asset for the order item was successful (true) or not (false). The default value is `false`. Available in API version 61.0 and later. |
| OrderItemId | **Type** reference **Properties** **Description** The ID of the order item used in the request. Available in API version 61.0 and later. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Lookup **Refers To** OrderItem |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |

=== ARTICLE: sforce_api_objects_createassetorderevent.htm ===
---
page_id: sforce_api_objects_createassetorderevent.htm
title: CreateAssetOrderEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_createassetorderevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreateAssetOrderEvent

Notifies subscribers that the process started by the `/actions/standard/createOrUpdateAssetFromOrder` or  `/actions/standard/createOrUpdateAssetFromOrderItem`
			request is complete. If the process is successful, use this event to learn about the new
			assets. If the request isn't successful, use this event to learn about the errors and
			how to fix them. This object is available in API version 55.0 and
		later.

		

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

		

		

## Subscription Channel

			
			

`/event/CreateAssetOrderEvent`

		

		

## Event Delivery Allocation Enforced

			
			

No

		

		

## Special Access Rules

			
			

This object is available if Subscription Management or Revenue Cloud is enabled in your org.
				Users must have Read access on this event to receive or view event
				notifications.

		

		

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

						

					

				
| Field | Details |
| --- | --- |
| AssetDetails | **Type** [CreateAssetOrderDtlEvent](./sforce_api_objects_createassetorderdtlevent.htm.md) **Properties** Nillable **Description** A list of AssetDetail records created as a result of a successful request. Each AssetDetail contains an order item ID, asset ID, and IsSuccess flag. If the request failed, the AssetDetail also contains an error code and error message. |
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| IsLastEvent | **Type** boolean **Properties** Defaulted on create **Description** Indicates whether this event is the final event in the request (`true`) or not (`false`). If `true`, then there are no more events associated with the request. This field is populated only in the final event in the request. The default value is `false`. This field is available in API version 62.0 and later. |
| OrderIdentifier | **Type** string **Properties** Nillable **Description** The ID of the order associated with this event. Available with Revenue Cloud in API version 64.0 and later. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** Id of the request that triggered the event. |

		

		

## Example

A user successfully runs a `createOrUpdateAssetFromOrder` request on an order with two order items. The
			published createAssetOrderEvent contains this information.
				
- RequestId: 0001

				
- AssetDetail
						
  - OrderItemId: 802XX0000000001

						
  - AssetId: 02iXX000000001

						
  - IsSuccess: True

					

				
- AssetDetail
						
  - OrderItemId: 802XX0000000001

						
  - AssetId: 02iXX000000002

						
  - IsSuccess: True

					

			

		

## Example

A user runs a `createOrUpdateAssetFromOrder` request on an order with two order items, but
			doesn't have Create access on assets. The request fails, and the published
			createAssetOrderEvent contains this information.
				
- RequestId: 0002

				
- AssetDetail
						
  - OrderItemId: 802XX0000000001

						
  - IsSuccess: False

						
  - ErrorCode: `INSUFFICIENT_ACCESS`

						
  - ErrorMessage: User doesn’t have Create Access to asset.

					

				
- AssetDetail
						
  - OrderItemId: 802XX0000000001

						
  - IsSuccess: False

						
  - ErrorCode: `INSUFFICIENT_ACCESS`

						
  - ErrorMessage: User doesn’t have Create Access to asset.

					

			

	

- 
**[CreateAssetOrderDtlEvent](./sforce_api_objects_createassetorderdtlevent.htm.md)**  

Contains information about an attempt to create or update an asset as a 			result of `/actions/standard/createOrUpdateAssetFromOrder`. If the request was 			successful, the event shows information about the asset. If the request failed, the 			event shows error information. This object is included in an `CreateAssetOrderEvent` message. You can't subscribe to 			`CreateAssetOrderDtlEvent` directly. This object is 		available in API version 55.0 and later.

=== ARTICLE: sforce_api_objects_orderdeliverymethod.htm ===
---
page_id: sforce_api_objects_orderdeliverymethod.htm
title: OrderDeliveryMethod
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderdeliverymethod.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderDeliveryMethod

    Shows the customizations and options that a buyer selected for their delivery
      method. This object is available in API version 48.0 and later.  

    

## Supported Calls

      
      

        `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
          `search()`, `undelete()`, `update()`, `upsert()`
      

    

    

## Special Access Rules

      
      

To access Commerce Orders entities, your org must have a Salesforce Order Management
        license. Commerce Orders entities are available only in Lightning Experience.

    

    

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

            

          

        
| Field | Details |
| --- | --- |
| Carrier | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The carrier that the buyer chose for their delivery method. Developers must add values to this field. |
| ClassOfService | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The carrier class of service that the buyer chose for their delivery method. Developers must add values to this field. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** Description of the delivery method. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Assign new delivery groups to active delivery methods. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, this record might only have been referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. Default name of this record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The user who owns an order delivery method record. |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Optional. This product represents a delivery charge order product for a delivery using this delivery method. For example, you could create a product that represents an overnight express charge and assign it to an overnight express delivery method. |
| ReferenceNumber | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Reference number for an external delivery method. |
| ShippingCarrierMethod | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Optional. A specific shipping service provided by a shipping carrier, such as Ground, 2Day, and NextDay. Depends on the range of transit times available for each carrier. |

    

    

## Associated Objects

      
      

This object has the following associated objects. If the API version isn’t specified,
        they’re available in the same API versions as this object. Otherwise, they’re available in
        the specified API version and later.

      
        
          

**
[OrderDeliveryMethodChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm) (API version 62.0)**

          
: Change events are available for the object.

=== ARTICLE: sforce_api_objects_orderitemattribute.htm ===
---
page_id: sforce_api_objects_orderitemattribute.htm
title: OrderItemAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemAttribute

      Represents
         a virtual object that stores an attribute specified for an order
         item.This object is available in API version 60.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeLayout()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the attribute definition for this order item attribute. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The name given to order item attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the attribute picklist value if the attribute is a picklist type. This field is a relationship field. **Relationship Name** AttributePicklistValue **Relationship Type** Lookup **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Stores the value of the order item attribute. For example 5-TB storage. You can use this field to filter records only if the DataType value in the related AttributeDefinitionId record is `Text`. If the DataType value is `Picklist`, use the value in the AttributePicklistValueId field for filtering. You can’t use this field to filter records if the DataType value is `Checkbox`, `Currency`, `Date`, `Datetime`, `Multipicklist`, `Number`, or `Percent`. |
| ExternalId | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** An auto-generated ID of the attribute record saved in an external system (for example an HBase database). |
| IsPriceImpacting | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** The pricing impacting the status of the attribute. The default value is `false`. |
| OrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent order item associated with the order item attribute. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Lookup **Refers To** OrderItem |

=== ARTICLE: sforce_api_objects_orderitemdetail.htm ===
---
page_id: sforce_api_objects_orderitemdetail.htm
title: OrderItemDetail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemdetail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemDetail

      Represents the breakdown details of an order product. Revenue Management generates
         these records to capture pricing and quantity changes, such as negative quantity
         reductions, early renewals, derived pricing or repricing during an amendment, and bundle or
         product attribute reconfigurations. This object is available in API version 60.0 and
      later. 

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| BillingReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Reference to the original order item for which this amend or cancel record is created. |
| EffectiveFrom | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the transaction becomes effective. |
| EffectiveTo | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the transaction ends. |
| LineNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The line number of the detail record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| NetUnitPrice | **Type** currency **Properties** Filter, Sort **Description** The unit price of the item that's calculated after applying any discounts and before tax calculation. |
| OrderItemId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the related order item. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Lookup **Refers To** OrderItem |
| PriceWaterfallIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing of the detail record. |
| Quantity | **Type** double **Properties** Filter, Sort **Description** The quantity specified for the item in the detail record. |
| ReferenceDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The reference date of the item. For example, the start date of the subscription that's associated with the detail record. |
| ReferenceNumber | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The reference number of the item. For example, the order number that's associated with the detail record. |
| TotalLineAmount | **Type** currency **Properties** Filter, Sort **Description** The net total price of the order product, before price adjustments, inclusive of quantity and subscription term. |
| TotalPrice | **Type** currency **Properties** Filter, Sort **Description** The total price of the item in the detail record that's calculated using the quantity, net unit price, and after applying the pricing terms. |
| UnitPrice | **Type** currency **Properties** Filter, Sort **Description** The unit price of the item before any discounts or tax calculation. |

=== ARTICLE: sforce_api_objects_orderitemrateadjustment.htm ===
---
page_id: sforce_api_objects_orderitemrateadjustment.htm
title: OrderItemRateAdjustment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemrateadjustment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemRateAdjustment

      Represents the negotiated rate adjustment for an order product. This
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
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

This object is available with Revenue
         Cloud.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| AdjustmentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of rate adjustment. Possible values are: `Amount` `Override` `Percentage` |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** The value of the adjustment. |
| LowerBound | **Type** double **Properties** Create, Filter, Sort, Update **Description** The minimum quantity for the adjustment to be applicable. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the order item rate adjustment. |
| OrderItemRateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent order item rate card entry associated with the order item rate adjustment. This field is a relationship field. **Relationship Name** OrderItemRateCardEntry **Relationship Type** Master-detail **Refers To** OrderItemRateCardEntry (the master object) |
| UpperBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The quantity below which the adjustment must be applicable. For example, if you want the adjustment to be applicable when the quantity is 99 or less, set this value to 100. |

=== ARTICLE: sforce_api_objects_orderitemratecardentry.htm ===
---
page_id: sforce_api_objects_orderitemratecardentry.htm
title: OrderItemRateCardEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemratecardentry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemRateCardEntry

      Represents the catalog and negotiated rates of a usage metric associated with
         an order item that's used to charge overage consumption. This object is available in
      API version 62.0 and later. 

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

This object is available with Revenue
         Cloud.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| IsChosenRate | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this rate is the chosen rate for the associated binding target and usage resource (`true`) or not (`false`). The default value is `false`. Available in API version 64.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An auto-generated number assigned to the order item rate card entry record. |
| NegotiatedRate | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The base negotiated rate used to charge overage consumption. |
| OrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent order item associated with the order item rate card entry. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Master-detail **Refers To** OrderItem (the master object) |
| RateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The rate card entry containing catalog rates that's associated with the order item rate card entry. This field is a relationship field. **Relationship Name** RateCardEntry **Refers To** RateCardEntry |
| RateCardId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The rate card associated with the order item rate card entry. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The standard unit of measure containing the unit for the negotiated rate that's associated with the order item rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the order item rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_orderitemusagersrcgrant.htm ===
---
page_id: sforce_api_objects_orderitemusagersrcgrant.htm
title: OrderItemUsageRsrcGrant
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemusagersrcgrant.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemUsageRsrcGrant

Represents the negotiated grants for the usage resource that's
         associated with the usage product added in the order item. This object is available in
      API version 65.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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
| GrantQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The granted or negotiated quantity of a usage resource associated with the usage product. |
| GrantType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of model that defines how the usage resource is consumed. Valid values are: `Commit` `Grant` The default value is `Grant`. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated identifier for the order item usage resource grant record. For example, OIURG-00004 or OIURG-4567. |
| OrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The order item associated with the usage product. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Master-detail **Refers To** OrderItem (the master object) |
| ProductUsageGrantId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product usage grant associated with the order item. This field is a relationship field. **Relationship Name** ProductUsageGrant **Refers To** ProductUsageGrant |
| TokenResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource of category Token associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** TokenResource **Refers To** UsageResource |
| UsageGrantRefreshPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant refresh policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** UsageGrantRefreshPolicy **Refers To** UsageGrantRenewalPolicy |
| UsageGrantRolloverPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant rollover policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** UsageGrantRolloverPolicy **Refers To** UsageGrantRolloverPolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the usage product that's added in the order item. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |
| ValidityPeriodTerm | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The duration for which the usage resource grant is valid, when used with the validity period units. |
| ValidityPeriodUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The length of a validity period for the usage resource grant, when used with the validity period term. Valid values are: `Month` `None` `Year` |

=== ARTICLE: sforce_api_objects_orderitemusagersrcplcy.htm ===
---
page_id: sforce_api_objects_orderitemusagersrcplcy.htm
title: OrderItemUsageRsrcPlcy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_orderitemusagersrcplcy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OrderItemUsageRsrcPlcy

Represents the policies that are used for the usage resource that's
         associated with the usage product added in the order item. This object is available in
      API version 65.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

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
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
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
| DrawdownOrder | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the order that's used to debit consumption of entitlements related to the usage resource from the usage entitlement bucket. Valid values are: `ExpiringFirst` `GrantedFirst` `GrantedLast` |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An auto-generated number assigned to the order item for usage product grant record. For example, OIURG-4567 |
| OrderItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The order item associated with the usage product. This field is a relationship field. **Relationship Name** OrderItem **Relationship Type** Master-detail **Refers To** OrderItem (the master object) |
| ProductUsageResourcePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product usage resource policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** ProductUsageResourcePolicy **Refers To** ProductUsageResourcePolicy |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rating frequency policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| UsageAggregationPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage aggregation policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageCommitmentPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage commitment policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** UsageCommitmentPolicy **Refers To** UsageCommitmentPolicy |
| UsageOveragePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage overage policy associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** UsageOveragePolicy **Refers To** UsageOveragePolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the usage product that's added in the order item. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_placeordercompletedevent.htm ===
---
page_id: sforce_api_objects_placeordercompletedevent.htm
title: PlaceOrderCompletedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_placeordercompletedevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PlaceOrderCompletedEvent

Notifies subscribers of an order being created or updated by invoking
			the Place Order API or the Place Sales Transaction API. This object is available in
		API version 63.0 and later.

		

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

		

		

## Subscription Channel

			
			

`/event/PlaceOrderCompletedEvent`

		

		

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

: 
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
| AppUsageTypes | **Type** string **Properties** Nillable **Description** Tag that represents the application that's using the order and determines how an order is processed. For example, the AppUsageTypes field value for Revenue Cloud orders is `RevenueLifecycleManagement`. |
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| HasErrors | **Type** boolean **Properties** Defaulted on create **Description** Indicates whether errors occurred when creating or updating the order (`true`) or not (`false`). The default value is `false`. |
| OrderId | **Type** reference **Properties** Nillable **Description** ID of the order record. This field is a relationship field. **Relationship Name** Order **Refers To** Order |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** ID of the request that triggered the event. |

=== ARTICLE: sforce_api_objects_quoteaction.htm ===
---
page_id: sforce_api_objects_quoteaction.htm
title: QuoteAction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quoteaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteAction

Indicates the type of sales transaction that’s being quoted; for
         example, a renewal sale. This object is available in API version 59.0 and
      later.

      

         

If a quote doesn't have a quote action, Salesforce treats it as a quote of the `Add` type. When such a quote is used to create an order,
            Salesforce automatically creates an order action of the `Add` type.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

This object is available in orgs with Revenue Cloud. It’s also available in Industries
            Automotive and Industries Field Service.

      

      

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
- 
- 
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

                  

               

            
| Field | Details |
| --- | --- |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** ISO code of the currency. Use only one of the valid alphabetic, three-letter currency ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY`. Must be unique within your organization. Label is **Currency ISO Code**. The default value is `USD`. See [Supported Currencies (ICU)](https://help.salesforce.com/s/articleView?id=xcloud.admin_supported_currencies.htm&type=5&language=en_US) for a list of currency codes Salesforce supports. This field is available in Revenue Cloud in API version 66.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, the user accessed this record or list view indirectly, but didn’t view it. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name given to the quote action. |
| QuoteId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The quote related to this quote action. This field is a relationship field. **Relationship Name** Quote **Relationship Type** Lookup **Refers To** Quote |
| SourceAssetId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The asset changed by this sales transaction. For example, if the quote action is a quantity amendment, this field contains the ID of the asset that’s amended. This field is a relationship field. **Relationship Name** SourceAsset **Relationship Type** Lookup **Refers To** Asset |
| Subtype | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The subtype of the action on the quote line item. Valid values are: `DowngradeFrom`—Available in API version 66.0 and later. `DowngradeTo`—Available in API version 66.0 and later. `FieldAmendment` `Rollback` `StartDateAdjustment` `SwapIn`—Available in API version 66.0 and later. `SwapOut`—Available in API version 66.0 and later. `TransferFrom` `TransferTo` `UpgradeFrom`—Available in API version 66.0 and later. `UpgradeTo`—Available in API version 66.0 and later. This field is available with Revenue Cloud in API version 64.0 and later. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort **Description** The type of sales transaction that the related quote is for. Valid values are: `Add` `Amend` `Association`—Available in API version 66.0 and later. `Cancel` `No Change` `Renew` `Transfer`—Available with Revenue Cloud in API version 65.0 and later. |

=== ARTICLE: sforce_api_objects_quoteitemtaxitem.htm ===
---
page_id: sforce_api_objects_quoteitemtaxitem.htm
title: QuoteItemTaxItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quoteitemtaxitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteItemTaxItem

      The tax that is applied to a quote line item. This object is available
      in API version 55.0 and later. 

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

This object is available if Subscription
         Management is enabled in your org. This object is also available in Enterprise, Unlimited,
         and Developer Editions of Revenue Cloud.

      

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

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
| Amount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The tax amount for the quote line item. |
| CurrencyIsoCode | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Available only for orgs with the multicurrency feature enabled. Contains the ISO code for any currency allowed by the org. Possible values are: `BHD`—Bahraini Dinar `EUR`—Euro `JPY`—Japanese Yen `USD`—U.S. Dollar The default value is 'USD'. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** User-defined description of the tax. For example, state sales tax or value-added tax (VAT). |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Name of the tax. |
| ProductSurchargeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product surcharge associated with the quote item tax item. This field is a relationship field. This field is available with Digital Insurance. **Relationship Name** ProductSurcharge **Refers To** ProductSurcharge |
| ProratedSurchargeAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The prorated portion of the tax amount based on the quote line item's effective dates. This field is available with Digital Insurance. |
| QuoteLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the related quote line item. This is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Lookup **Refers To** QuoteLineItem |
| Rate | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** If the tax is a percentage tax, then this field contains the percent value. If the tax is a fixed amount, then this field is null. |
| TaxEffectiveDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date used to calculate the tax rate. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Whether the tax is estimated or calculated by the tax provider. Possible values are: `Actual` `Estimated` |

=== ARTICLE: sforce_api_objects_quotelinedetail.htm ===
---
page_id: sforce_api_objects_quotelinedetail.htm
title: QuoteLineDetail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotelinedetail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteLineDetail

      Represents the breakdown details of a quote line item. Revenue Management
         generates these records to capture pricing and quantity changes, such as negative quantity
         reductions, early renewals, derived pricing or repricing during an amendment, and bundle or
         product attribute reconfigurations. This object is available in API version 60.0 and
      later. 

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`
      

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| BillingReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Reference to the original order item for which this amend or cancel record is created. |
| EffectiveFrom | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the transaction becomes effective. |
| EffectiveTo | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the transaction ends. |
| LineNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The line number of the detail record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| NetUnitPrice | **Type** currency **Properties** Filter, Sort **Description** The unit price of the item that's calculated after applying any discounts and before tax calculation. |
| PriceWaterfallIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing of the detail record. |
| Quantity | **Type** double **Properties** Filter, Sort **Description** The quantity specified for the item in the detail record. |
| QuoteLineItemId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the related quote line. This field is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Lookup **Refers To** QuoteLineItem |
| ReferenceDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The reference date of the item. For example, the start date of the subscription that's associated with the detail record. |
| ReferenceNumber | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The reference number of the item. For example, the order number that's associated with the detail record. |
| TotalLineAmount | **Type** currency **Properties** Filter, Sort **Description** The net total price of the order product, before price adjustments, inclusive of quantity and the subscription term. |
| TotalPrice | **Type** currency **Properties** Filter, Sort **Description** The total price of the item in the detail record that's calculated using the quantity, net unit price, and after applying the pricing terms. |
| UnitPrice | **Type** currency **Properties** Filter, Sort **Description** The unit price of the item before any discounts or tax calculation. |

=== ARTICLE: sforce_api_objects_quotelinegroup.htm ===
---
page_id: sforce_api_objects_quotelinegroup.htm
title: QuoteLineGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotelinegroup.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteLineGroup

      Stores the group information for line items in a quote. It also stores the
         aggregated line field information (subtotal). It contains a parent-child relationship to
         quote. This object is available in API version 61.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
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
- 
- 

: 

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the group. |
| Discount | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount percentage, specified by the sales representative at the group level. |
| DiscountAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional discount amount, specified by the sales representative at the group level. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The end date of the group ramp segment. |
| IsRamped | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the group is a group ramp segment, which is a period in a group ramp deal with specific prices and volume. The default value is `false`. |
| Margin | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin percentage, specified by the sales representative at the group level. |
| MarginAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The optional margin amount, specified by the sales representative at the group level. This amount can also be considered as the summary margin amount calculated by subtracting the total cost from the summary subtotal. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the group. |
| ParentQuoteLineGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the parent group for a nested quote line group. This field is a relationship field. **Relationship Name** ParentQuoteLineGroup **Refers To** QuoteLineGroup |
| QuoteId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the related quote. This field is a relationship field. **Relationship Name** Quote **Relationship Type** Master-detail **Refers To** Quote (the master object) |
| SegmentType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The duration type of the segment. Possible values are: `Custom` `Yearly` |
| SortOrder | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The start date of the group ramp segment. |
| SummarySubtotal | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The aggregated subtotal amount of nested group lines. |
| SummaryTotalAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The aggregated total amount of nested group lines before any discounts are applied. |
| TotalAdjustment | **Type** percent **Properties** Filter, Nillable, Sort **Description** The total discount percentage applied at the group level. This percentage is calculated by using the formula: (Summary Total Amount - Summary Subtotal) / Summary Total Amount. |
| TotalAdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total discount amount at the group level. This amount is calculated by subtracting the summary subtotal from the summary total amount. |
| TotalCost | **Type** currency **Properties** Filter, Nillable, Sort **Description** The aggregated total cost of nested group lines. |
| TotalMargin | **Type** percent **Properties** Filter, Nillable, Sort **Description** The summary margin percentage at the line item level. This percentage is calculated by using the formula: (Summary Subtotal - Total Cost) / Summary Subtotal. |
| TotalMarginAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The summary margin amount calculated at the group level. |
| Type | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of quote line group. Possible values are: `AssetDowngrade` `AssetSwap` `AssetUpgrade` `CPQQuoteGroup`—CPQ Line Grouping `RampScheduleGroup` The default value is `CPQQuoteGroup`. |

=== ARTICLE: sforce_api_objects_quotelineitemattribute.htm ===
---
page_id: sforce_api_objects_quotelineitemattribute.htm
title: QuoteLineItemAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotelineitemattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteLineItemAttribute

      Represents a virtual object that stores an attribute specified for a quote
         line item. This object is available in API version 59.0 and later. 

      
         

#### Note

Where possible, we changed noninclusive terms to align with our company
            value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

This object is available in Enterprise, Unlimited,
         and Developer Editions of Revenue Management.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the attribute definition for this quote line item attribute. This field is a relationship field. **Relationship Name** AttributeDefinition **Refers To** AttributeDefinition |
| AttributeName | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The name of the quote line item attribute. |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the attribute picklist value if the attribute is a picklist type. This field is a relationship field. **Relationship Name** AttributePicklistValue **Refers To** AttributePicklistValue |
| AttributeValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The value of the quote line item attribute. For example 5-TB storage. You can use this field to filter records only if the DataType value in the related AttributeDefinitionId record is `Text`. If the DataType value is `Picklist`, use the value in the AttributePicklistValueId field for filtering. You can’t use this field to filter records if the DataType value is `Checkbox`, `Currency`, `Date`, `Datetime`, `Multipicklist`, `Number`, or `Percent`. |
| ExternalId | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** An auto-generated ID of the attribute record saved in an external system, such as an HBase database. |
| IsPriceImpacting | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** The pricing impacting the status of the attribute. The default value is `false`. |
| QuoteLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The associated parent quote line item. This field is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Master-detail **Refers To** QuoteLineItem (the master object) |

      

      

## Usage

         
         

This object doesn’t support custom fields, validation rules, or triggers. In SOQL
            queries, you can filter records by using Id and
               AttributeDefinition. You can’t use
               AttributeValue in the `WHERE`
            clause.

=== ARTICLE: sforce_api_objects_quotelinerateadjustment.htm ===
---
page_id: sforce_api_objects_quotelinerateadjustment.htm
title: QuoteLineRateAdjustment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotelinerateadjustment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteLineRateAdjustment

      Represents the negotiated rate adjustment for a quote line item. This
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
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

This object is available with Revenue
         Cloud.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| AdjustmentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of rate adjustment. Possible values are: `Amount` `Override` `Percentage` |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** The value of the adjustment. |
| LowerBound | **Type** double **Properties** Create, Filter, Sort, Update **Description** The minimum quantity for the adjustment to be applicable. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the quote line rate adjustment record. |
| QuoteLineRateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent quote line rate card entry associated with the quote line rate adjustment. This field is a relationship field. **Relationship Name** QuoteLineRateCardEntry **Relationship Type** Master-detail **Refers To** QuoteLineRateCardEntry (the master object) |
| UpperBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The quantity below which the adjustment must be applicable. For example, if you want the adjustment to be applicable when the quantity is 99 or less, set this value to 100. |

=== ARTICLE: sforce_api_objects_quotelineratecardentry.htm ===
---
page_id: sforce_api_objects_quotelineratecardentry.htm
title: QuoteLineRateCardEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotelineratecardentry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteLineRateCardEntry

      Represents the catalog and negotiated rates of a usage resource associated
         with a quote line item that's used to charge overage consumption. This object is
      available in API version 62.0 and later. 

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| IsChosenRate | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this rate is the chosen rate for the associated binding target and usage resource (`true`) or not (`false`). The default value is `false`. Available in API version 64.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An auto-generated number assigned to the quote line rate card entry record. |
| NegotiatedRate | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The base negotiated rate used to charge overage consumption. |
| QuoteLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent quote line item associated with the quote line rate card entry. This field is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Master-detail **Refers To** QuoteLineItem (the master object) |
| RateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The rate card entry containing catalog rates that's associated with the quote line rate card entry. This field is a relationship field. **Relationship Name** RateCardEntry **Refers To** RateCardEntry |
| RateCardId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The rate card associated with the quote line rate card entry. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The standard unit of measure containing the unit for the negotiated rate that's associated with the quote line rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the quote line rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_quotesaveevent.htm ===
---
page_id: sforce_api_objects_quotesaveevent.htm
title: QuoteSaveEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotesaveevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteSaveEvent

Notifies subscribers that the process started by the Place Quote or
			Place Sales Transaction API request is complete. If the process is successful, use this
			event to learn about the updated quote. If the request isn't successful, use this event
			to learn about the errors and how to fix them. This object is available in API
		version 60.0 and later.

		

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

			
			

`/event/QuoteSaveEvent`

		

		

## Special Access Rules

			
			

This object is available in orgs with Subscription Management or Revenue Management.

		

		

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

						

					

				
| Field | Details |
| --- | --- |
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| HasErrors | **Type** boolean **Properties** Defaulted on create **Description** The default value is false. Possible values are: false true |
| QuoteId | **Type** reference **Properties** Nillable **Description** The ID of the quote associated with this event. This field is a relationship field. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** ID of the request that triggered the event. |

=== ARTICLE: sforce_api_objects_quotetoopportunitysyncevent.htm ===
---
page_id: sforce_api_objects_quotetoopportunitysyncevent.htm
title: QuoteToOpportunitySyncEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotetoopportunitysyncevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteToOpportunitySyncEvent

      Represents an asynchronous quote to opportunity synchronization event. It
         tracks whether the sync succeeded or failed and notifies associated subscribers upon
         completion. This object is available in API version XX.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `describeSObjects()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CorrelationIdentifier | **Type** string **Properties** Create, Nillable **Description** The caller-specified ID that matches this event to the originating request. |
| ErrorCode | **Type** string **Properties** Create, Nillable **Description** The error code returned when the sync fails. Null when Has Errors is False. |
| ErrorMessage | **Type** textarea **Properties** Create, Nillable **Description** The error message that explains why the sync failed. Null when Has Errors is False. |
| HasErrors | **Type** boolean **Properties** Create, Defaulted on create **Description** Indicates whether the sync failed. True if the sync completed with errors or False if the sync succeeded. The default value is `false`. |
| OpportunityRecordId | **Type** reference **Properties** Create, Nillable **Description** The ID of the Opportunity record being synced. Null if the sync fails before an Opportunity is associated. This field is a relationship field. **Relationship Name** OpportunityRecord **Refers To** Opportunity |
| QuoteRecordId | **Type** reference **Properties** Create **Description** The ID of the Quote record synced to its related Opportunity. This field is a relationship field. **Relationship Name** QuoteRecord **Refers To** Quote |
| RequestIdentifier | **Type** string **Properties** Create, Nillable **Description** The unique identifier for the request that triggered this sync event. |
| RevenueTransactionErrLogId | **Type** reference **Properties** Create, Nillable **Description** The ID of the Revenue Transaction Error Log record created when the sync fails. Null when Has Errors is False. This field is a relationship field. **Relationship Name** RevenueTransactionErrLog **Refers To** RevenueTransactionErrorLog |

=== ARTICLE: sforce_api_objects_quotetoordercompletedevent.htm ===
---
page_id: sforce_api_objects_quotetoordercompletedevent.htm
title: QuoteToOrderCompletedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotetoordercompletedevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuoteToOrderCompletedEvent

Notifies subscribers when the `/actions/standard/createOrderFromQuote` REST request is complete. If the
			request is successful, use this event to learn about the Order record. If the request
			isn’t successful, use this event to learn about the errors associated with the
			request. This object is available in API version 56.0 and later. 

		

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

		

		

## Subscription Channel

			
			

`/event/QuoteToOrderCompletedEvent`

		

		

## Event Delivery Allocation Enforced

			
			

No

		

		

## Special Access Rules

			
			

This object is available with Revenue Cloud.

		

		

				
				
				
					
						

						

					

				

				
					
						

						

: 

: 

: 

					

					
						

						

: 

: 

: 

					

					
						

						

: 

: 

: 

					

					
						

						

: 

: 

: 

					

					
						

						

: 

: 

: 

					

					
						

						

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
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| HasErrors | **Type** boolean **Properties** Defaulted on create **Description** Contains `true` if errors occurred during the process; otherwise `false`. The default value is `false`. |
| OrderId | **Type** string **Properties** Nillable **Description** The ID of the order created from the quote. If the process failed, this field is null. |
| OrderNumber | **Type** string **Properties** Nillable **Description** The user-friendly, unique number assigned to the order created from the quote. |
| QuoteToOrderErrorDetailEvents | **Type** [QuoteToOrderErrDtlEvent](https://developer.salesforce.com/docs/atlas.en-us.264.0.platform_events.meta/platform_events/sforce_api_objects_quotetoordererrdtlevent.htm)[] **Properties** Nillable **Description** Contains a list of error messages and error codes if the request failed. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** The unique ID returned in the `actions/standard/createOrderFromQuote` response. Use this ID to identify the event for a specific request. |

=== ARTICLE: sforce_api_objects_quotlineitmusagersrcplcy.htm ===
---
page_id: sforce_api_objects_quotlineitmusagersrcplcy.htm
title: QuotLineItmUsageRsrcPlcy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotlineitmusagersrcplcy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuotLineItmUsageRsrcPlcy

Represents the policies that are used for the usage resource that's
         associated with the usage product added in the quote line item. This object is
      available in API version 65.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`
         

      

      

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
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
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
| DrawdownOrder | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the order that's used to debit consumption of entitlements related to the usage resource from the usage entitlement bucket. Valid values are: `ExpiringFirst` `GrantedFirst` `GrantedLast` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated identifier for the quote line item usage resource policy record. For example, QLIURP-00004 or QLIURP-4567. |
| ProductUsageResourcePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product usage resource policy associated with the quote line item. This field is a relationship field. **Relationship Name** ProductUsageResourcePolicy **Refers To** ProductUsageResourcePolicy |
| QuoteLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The quote line item associated with the usage product. This field is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Master-detail **Refers To** QuoteLineItem (the master object) |
| RatingFrequencyPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The rating frequency policy associated with the usage resource related to the usage product added in the quote line item. This field is a relationship field. **Relationship Name** RatingFrequencyPolicy **Refers To** RatingFrequencyPolicy |
| UsageAggregationPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage aggregation policy associated with the usage resource related to the usage product added in the quote line item. This field is a relationship field. **Relationship Name** UsageAggregationPolicy **Refers To** UsageResourceBillingPolicy |
| UsageCommitmentPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage commitment policy associated with the usage resource related to the usage product added in the quote line item. This field is a relationship field. **Relationship Name** UsageCommitmentPolicy **Refers To** UsageCommitmentPolicy |
| UsageOveragePolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage overage policy associated with the quote line item. This field is a relationship field. **Relationship Name** UsageOveragePolicy **Refers To** UsageOveragePolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the usage product that's added in the quote line item. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_quotlineitmusersrcgrant.htm ===
---
page_id: sforce_api_objects_quotlineitmusersrcgrant.htm
title: QuotLineItmUseRsrcGrant
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_quotlineitmusersrcgrant.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QuotLineItmUseRsrcGrant

Represents the negotiated grants for the usage resource that's
         associated with the usage product added in the quote line item. This object is
      available in API version 65.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

      

      

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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
| GrantQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The granted or negotiated quantity of a usage resource associated with the usage product. |
| GrantType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the type of model that defines how the usage resource is consumed. Valid values are: `Commit` `Grant` The default value is `Grant`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated identifier for the quote line item usage resource grant record. For example, QLIURG-00004 or QLIURG-4567. |
| ProductUsageGrantId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The product usage grant associated with the quote line item. This field is a relationship field. **Relationship Name** ProductUsageGrant **Refers To** ProductUsageGrant |
| QuoteLineItemId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The quote line item associated with the usage product. This field is a relationship field. **Relationship Name** QuoteLineItem **Relationship Type** Master-detail **Refers To** QuoteLineItem (the master object) |
| TokenResourceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage resource of category Token associated with the usage resource related to the usage product added in the order item. This field is a relationship field. **Relationship Name** TokenResource **Refers To** UsageResource |
| UsageGrantRefreshPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant refresh policy associated with the usage resource related to the usage product added in the quote line item. This field is a relationship field. **Relationship Name** UsageGrantRefreshPolicy **Refers To** UsageGrantRenewalPolicy |
| UsageGrantRolloverPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The usage grant rollover policy associated with the usage resource related to the usage product added in the quote line item. This field is a relationship field. **Relationship Name** UsageGrantRolloverPolicy **Refers To** UsageGrantRolloverPolicy |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The usage resource associated with the usage product that's added as the quote line item. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |
| ValidityPeriodTerm | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The duration for which the usage resource grant is valid, when used with the validity period units. |
| ValidityPeriodUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The length of a validity period for the usage resource grant, when used with the validity period term. Valid values are: `Month` `None` `Year` |

=== ARTICLE: sforce_api_objects_salestransactiontype.htm ===
---
page_id: sforce_api_objects_salestransactiontype.htm
title: SalesTransactionType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_salestransactiontype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SalesTransactionType

Represents the type of the sales transaction. This object is
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
      

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Unlimited, and Developer Editions of Revenue
            Cloud.

      

      

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
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, the user might have only accessed this record or list view but not viewed it directly. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the sales transaction type. |

=== ARTICLE: tooling_api_objects_transactionprocessingtype.htm ===
---
page_id: tooling_api_objects_transactionprocessingtype.htm
title: TransactionProcessingType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/tooling_api_objects_transactionprocessingtype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: quote_and_order_capture_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TransactionProcessingType

Represents the settings to configure the processing constraints for a
         request.. This object is available in API version 63.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

Refer to the Usage section to learn more about creating Transaction Processing
            Type records based on your requirements. See the [setup details](https://help.salesforce.com/s/articleView?id=ind.product_configurator_specify_which_rule_engine_to_use.htm&language=en_US) to specify
            the default rule engine on the Revenue Settings page.

      

## Supported SOAP API Calls

         
         

            `create()`, `describeSObjects()`, `query()`, `retrieve()`
         

      

      

## Supported REST API Methods

         
         

`GET, HEAD, POST, Query`
         

      

      
      

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

- 
- 

                  

                  
                     

                     

: 

: 

: 
: 

                  

               

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the transaction processing configuration to help Salesforce admins with configuration in their orgs. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Nillable, Update **Description** The language of the TransactionProcessingType object. Valid values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The label for the TransactionProcessingType object. |
| PricingPreference | **Type** string **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to execute the price calculation step for each sales transaction record. Valid values are: `Force`—Reprices all lines. `System`—Performs a delta pricing request on the unprocessed lines when [Delta Pricing](https://help.salesforce.com/s/articleView?id=ind.qocal_use_delta_pricing_for_quotes_and_orders.htm&language=en_US) is enabled in the org. `Skip`—Skips the pricing request on all lines. Available in API version 65.0 and later. |
| RatingPreference | **Type** string **Properties** **Description** Specifies whether catalog rates are fetched and saved during quote creation. Valid value is `Fetch`. Use this value to retrieve and save catalog rates for usage resources associated with each sales transaction record. If this value isn't specified, catalog rates aren't saved by default when a quote line item is added to a quote. Available in API version 66.0 and later if Rate Management is enabled. |
| RuleEngine | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The rule engine to be used for processing rules. Valid values are: `AdvancedConfigurator` `StandardConfigurator` |
| SaveType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies how the transaction results are processed when saved for Salesforce administrators to adjust the user experience as desired. Valid values are: `Standard` `Large`—Reserved for future use. |
| TaxPreference | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to execute or skip the tax calculation step for each sales transaction record. Valid value is `Skip`. If this value isn't specified, then tax calculation request is performed by default. Available in API version 65.0 and later. |

      

      

## Usage

Create transaction type records by calling this resource
            through a POST
         method.

```
/services/data/v68.0/tooling/sobjects/TransactionProcessingType
```

Here's
         a sample payload that specifies the rule engine to use and steps to skip for each sales
         transaction record.

```
{
  "SaveType": "Standard",
  "Description": "Setup for Transaction Processing Type",
  "DeveloperName": "SkipPricingAndTaxStep",
  "MasterLabel": "SkipPricingAndTaxStep",
  "RuleEngine": "StandardConfigurator",
  "PricingPreference": "Skip",
  "TaxPreference": "Skip"
}
```

Here's a sample payload that specifies a value for rating preference and the
         steps to skip for each sales transaction
         record.

```
{
  "SaveType": "Standard",
  "Description": "Setup for Transaction Processing Type",
  "DeveloperName": "SkipPricingAndTaxStep",
  "MasterLabel": "SkipPricingAndTaxStep",
  "RuleEngine": "StandardConfigurator",
  "PricingPreference": "Skip",
  "TaxPreference": "Skip",
  "RatingPreference": "Fetch"
}
```

=== ARTICLE: transaction_management_apex_input_classes.htm ===
---
page_id: transaction_management_apex_input_classes.htm
title: ConnectApi Input Classes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/transaction_management_apex_input_classes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: transaction_management_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi Input Classes

Transaction Management includes this Apex input class.

- 
**[ConnectApi.RampOptionInputRepresentation](./apex_connectapi_input_ramp_option.htm.md)**  

Input representation of the ramp option details during an asset renewal.

- 
**[ConnectApi.TransferRecordInputRepresentation](./apex_connectapi_input_transfer_record.htm.md)**  

Input representation of the details of the assets to be transferred.

=== ARTICLE: transaction_management_connect_api_namespace.htm ===
---
page_id: transaction_management_connect_api_namespace.htm
title: ConnectApi Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/transaction_management_connect_api_namespace.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Transaction Management
parent_page: qoc_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# 
ConnectApi Namespace

The `ConnectApi` namespace (also called Connect in
        Apex) provides an Apex class to specify details for asset transfer request from one account
        to another.

        
            

These classes are available in the `ConnectApi`
                namespace.

        

    

- 
**[ConnectApi Input Classes](./transaction_management_apex_input_classes.htm.md)**  

Transaction Management includes this Apex input class.

