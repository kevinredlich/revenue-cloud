# Revenue Management Developer Guide 264 — sección: Rate Management (28 artículos)

=== ARTICLE: actions_obj_invoke_rating_service.htm ===
---
page_id: actions_obj_invoke_rating_service.htm
title: Invoke Rating Service Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_invoke_rating_service.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoke Rating Service Action

Invoke the rating service to rate the usage records.

		
			

The Invoke Rating Service action acts as a connector between batch management and the rating
				service. This action is available in API version 62.0 and later.

		

		

## Special Access Rules

			
			

The Invoke Rating Service action is available in  Enterprise, Unlimited, and
				Developer Editions where Rate Management is enabled.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/invokeRatingService`

				
				
					

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
| attributeRateCardID | **Type** string **Description** ID of the rate card that’s used to define adjustments based on the attributes that impact the rate. |
| baseRateCardID | **Type** string **Description** ID of the rate card that includes the base rate for the resource to be rated, based on its consumption. |
| contextDefinitionId | **Type** string **Description** Required. ID of the context definition that’s used to create the context instance. |
| contextMappingID | **Type** string **Description** ID of the context mapping that maps a standard object, context definition object, or any other input data source to the node that’s defined in the context definition. |
| isSkipWaterfall | **Type** boolean **Description** Indicates whether to skip the generation of price waterfall data (`true`) or not (`false`). |
| procedureName | **Type** string **Description** Name of the rating procedure that’s used to calculate the rates. |
| recordID | **Type** reference **Description** Required. ID of the usage ratable summary record to be rated. |
| tierRateCardID | **Type** string **Description** ID of the rate card that’s used to define adjustments for different tiers of a resource. |

		

		

## Outputs

None

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Invoke Rating Service action.

						

```
{
  "inputs": [
    {
      "recordIDs": "56jSB000002Bn12CXC",
      "contextMappingId": "11jSB000002Bn13YAC",
      "contextDefinitionId": "11OSB0000000WSv2AM",
      "procedureName": "Invoke Rate",
      "isSkipWaterfall": false,
      "baseRateCardID": "11jSB000002Bn13YAC",
      "tierRateCardID": "fgjjSB0sdf987dsf",
      "attributeRateCardID": "asdfgh563034lk"
    }
  ]
}
```

					

					
: 
						

This example shows a sample response for the Invoke Rating Service action.

						

```
[
    {
        "actionName": "invokeRatingService",
        "errors": null,
        "isSuccess": true,
        "outputValues": {}
    }
]
```

=== ARTICLE: connect_resources_get_rate_plan.htm ===
---
page_id: connect_resources_get_rate_plan.htm
title: Rate Plan (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_rate_plan.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Plan (GET)

Get a rate plan for a specified set of context input. Use this API to retrieve rate
    cards, rate card entries, and related adjustments based on the filter criteria for the context
    input.

    

Keep these considerations in mind when you use this API.

        
- This API request supports one pricebook and one sellable product.

        
- The ID of the product is required to invoke this API.

        
- Invoke this API even if a hydrated context is available to fetch the rate card, rate
          card entry, and adjustment details.

      

    

        
          

**Special Access Rules**

          
: The org must have the Rate Management: Run Time User permission set to use this API.
            Additionally, the org must also have a default usage rating discovery procedure defined
            in the Revenue Settings from Setup.

        
      

    
      
        
          

**Resource**

          
: 
            

```
/connect/core-rating/rate-plan
```

          

        
        
          

**Resource example**

          
: 
            

```
https://your​Instance.salesforce.com​/services​/data/v68.0/connect/​core-rating/rate-plan​?contextId=858a3ad3e5a0e​5c319652a6ab92f6​fdb2b4fa8be72b390506​d014596c6da62c9&procedure​ApiName=Sample​Procedure
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `contextId` | String | ID of the context to specify as an input to the procedure. | Required | 62.0 |
| `procedure​ApiName` | String | API name of the procedure to be executed. | Required | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Rate Plan Response](./connect_responses_rate_plan_response.htm.md)

=== ARTICLE: connect_resources_rating_waterfall_fetch.htm ===
---
page_id: connect_resources_rating_waterfall_fetch.htm
title: Rating Waterfall (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_rating_waterfall_fetch.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rating Waterfall (GET)

Get the persisted rating waterfall that stores the process logs.
      Rating waterfall provides insights into the internal rating process.

    
      
        
          

**Resource**

          
: 
            

```
/connect/core-pricing/waterfall/lineItemId/executionId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/core-pricing/waterfall/Gold/2yHdNNEFOZr9jAe4gHS7?tagsToFilter=UnitPrice&usageType=Rating
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Query parameters**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `tagsTo​Filter` | String | Comma-separated tags to filter. | Optional | 62.0 |
| `usage​Type` | String | Usage type of the waterfall log record. Valid values are: `Rating` `Pricing`—Specifies that the record type is `Pricing`. If this value is specified, the API creates a log of pricing waterfall. See [Pricing Waterfall](./connect_resources_pricing_waterfall_post.htm.md). The default value is `Pricing`. | Optional | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Line Item Waterfall
            Response](./connect_responses_rating_line_item_waterfall_response.htm.md)

=== ARTICLE: connect_responses_rate_adjustment_detail.htm ===
---
page_id: connect_responses_rate_adjustment_detail.htm
title: Adjustment Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rate_adjustment_detail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Adjustment Details

Output representation of a rate adjustment request.

    
      
        
          

**JSON example**

          
: 
            

```

 "pricingElement": {
      "adjustments": [{
      "adjustmentType": null,
      "adjustmentValue": null
    }],
      "name": "List Price",
      "elementType": "ListPrice"
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `adjustments` | Map<String, Object>[] | Details of the rate element. | Small, 60.0 | 60.0 |
| `description` | String | Description of the rate element. | Small, 60.0 | 60.0 |
| `element​Type` | String | Type of the rate element. | Small, 60.0 | 60.0 |
| `name` | String | Name of the rate element. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_rate_plan_response.htm ===
---
page_id: connect_responses_rate_plan_response.htm
title: Rate Plan Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rate_plan_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Plan Response

Output representation of the details of a rate plan.

      
        
          

**JSON example**

          
: 
            

```
{
  "success": true,
  "executionId" : "a521d592-71c3-4db3-8048-r64504df1605",
  "error": {}
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Rating Error Response](./connect_responses_rating_error_response.htm.md)[] | Error response for the API request, if any. | Small, 62.0 | 62.0 |
| `executionId` | String | ID of the procedure execution record. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the request is successful (`true`) or not (`false`) | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_rating_error_response.htm ===
---
page_id: connect_responses_rating_error_response.htm
title: Rating Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rating_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rating Error Response

Output representation of the error details related to the API request.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code indicating the type of error. | Small, 62.0 | 62.0 |
| `message` | String | Message stating the reason for error, if any. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_rating_line_item_waterfall_response.htm ===
---
page_id: connect_responses_rating_line_item_waterfall_response.htm
title: Line Item Waterfall Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rating_line_item_waterfall_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Line Item Waterfall Response

Output representation of the line item waterfall response.

    
      
        
          

**JSON example**

          
: 
            

```
{
       "currencyCode": "USD",
       "error": null,
       "executionEndTimestamp": "2023-07-31T20:11:29.625Z",
       "executionId": "gdLVwn2x1uats2xWMAjV",
       "executionStartTimestamp": null,
       "lineItemId": "item1",
       "success": true,
       "usageType":"Rating",
       "output": {
          "quantity": "10",
          "netUnitPrice": "10",
          "subtotal": "100"
        },
        "waterfall": []
}

```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `context​Definition​VersionId` | String | Context definition version ID of the rating procedure. | Small, 62.0 | 62.0 |
| `context​MappingId` | String | Context mapping ID of the record. | Small, 62.0 | 62.0 |
| `currency​Code` | String | Currency code. For example, USD or INR. | Small, 62.0 | 62.0 |
| `error` | [Rating Error Response](./connect_responses_rating_error_response.htm.md) | Details of any errors. | Small, 62.0 | 62.0 |
| `execution​End​Timestamp` | String | End timestamp of procedure execution. | Small, 62.0 | 62.0 |
| `execution​Id` | String | Execution ID of a particular execution of a rating procedure. | Small, 62.0 | 62.0 |
| `execution​Start​Timestamp` | String | Start timestamp of procedure execution. | Small, 62.0 | 62.0 |
| `line​ItemId` | String | Line item ID for which the price is being calculated. | Small, 62.0 | 62.0 |
| `output` | Map<String, Object> | Output of the rating procedure. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `usage​Type` | String | Usage type of the waterfall log record. | Small, 62.0 | 62.0 |
| `waterfall` | [Rating Waterfall Response](./connect_responses_rating_waterfall_response.htm.md)[] | Details of the rating waterfall. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_rating_waterfall_response.htm ===
---
page_id: connect_responses_rating_waterfall_response.htm
title: Rating Waterfall Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rating_waterfall_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rating Waterfall Response

Output representation of a rating waterfall request.

    
      
        
          

**JSON example**

          
: 
            

```

{
  "inputParameters": {
    "productId": "01txx0000006i2SAAQ",
    "pricebookId": "01sxx0000005ptpAAA",
    "pricingModelType": "OneTime"
  },
  "fieldToTagNameMapping": {
    "Product2Id": "ItemProduct",
    "Subtotal": "Subtotal",
    "Pricebook2Id": "Pricebook",
    "Quantity": "ItemQuantity",
    "LineItemId": "SalesTransactionSource",
    "ListPrice": "ItemListPrice"
  },
  "sequence": 0,
  "outputParameters": {
    "listPrice": "10"
  },
  "pricingElement": {
    "adjustments": [
      {
        "adjustmentType": null,
        "adjustmentValue": null
      }
    ],
    "name": "List Price"
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `fieldTo​TagName​Mapping` | Map<String, String> | Mappings of field to tag names. | Small, 62.0 | 62.0 |
| `input​Parameters` | Map<String, Object> | Parameters of rating element input. | Small, 62.0 | 62.0 |
| `output​Parameters` | Map<String, Object> | Parameters of rating element output. | Small, 62.0 | 62.0 |
| `pricing​Element` | [Adjustment Details](./connect_responses_rate_adjustment_detail.htm.md) | Details of the rate adjustment of a rating element. | Small, 62.0 | 62.0 |
| `sequence` | Integer | Sequence of rating element execution. | Small, 62.0 | 62.0 |

=== ARTICLE: meta_industriesratingsettings.htm ===
---
page_id: meta_industriesratingsettings.htm
title: IndustriesRatingSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_industriesratingsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# IndustriesRatingSettings

Represents the settings for Rate
		Management.

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

The IndustriesRatingSettings values are stored in the
					IndustriesRating.settings file in the
					settings folder. The .settings files
				are different from other named components, because there’s only one settings file
				for each settings component.

	

	

## Version

		
		

IndustriesRatingSettings components are available in API version 62.0 and later.

	

	

## Special Access Rules

		
			

This metadata type is available with Rate Management.

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| enableRating | **Field Type** boolean **Description** Indicates whether to enable Rate Management (`true`) or not (`false`). The default value is `false`. |
| enableRatingWaterfall | **Field Type** boolean **Description** Indicates whether to enable Rating Waterfall (`true`) or not (`false`). The default value is `false`. Rating Waterfall provides insights into the rating data, which you can synchronize with your rating lookup tables. |
| enableRatingWaterfallPersistence | **Field Type** boolean **Description** Indicates whether to enable Rating Waterfall Persistence (`true`) or not (`false`). The default value is `false`. Rating Waterfall Persistence stores rating data, which you can use to enhance the internal processes and increase efficiency. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of an IndustriesRatingSettings component.

			

```
<IndustriesRatingSettings xmlns="http://soap.sforce.com/2006/04/metadata">
     <enableRating>true</enableRating>
     <enableRatingWaterfall>true</enableRatingWaterfall> 
     <enableRatingWaterfallPersistence>true</enableRatingWaterfallPersistence>
</IndustriesRatingSettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>IndustriesRating</members>
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

=== ARTICLE: rate_management_business_api_overview.htm ===
---
page_id: rate_management_business_api_overview.htm
title: Rate Management Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_business_api_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Management Business APIs

Use the Rate Management Business APIs to get rate plan and persisted rating waterfall
    details.

- 
**[Resources](./rate_management_business_apis_resources.htm.md)**  

Learn more about the available Rate Management API resources.

- 
**[Response Bodies](./rate_management_business_apis_responses.htm.md)**  

Learn more about the available response bodies of Rate Management APIs.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: rate_management_business_apis_resources.htm ===
---
page_id: rate_management_business_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_business_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Rate Management API resources.

- 
**[Rate Plan (GET)](./connect_resources_get_rate_plan.htm.md)**  

Get a rate plan for a specified set of context input. Use this API to retrieve rate     cards, rate card entries, and related adjustments based on the filter criteria for the context     input.

- 
**[Rating Waterfall (GET)](./connect_resources_rating_waterfall_fetch.htm.md)**  

Get the persisted rating waterfall that stores the process logs.       Rating waterfall provides insights into the internal rating process.

=== ARTICLE: rate_management_business_apis_responses.htm ===
---
page_id: rate_management_business_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_business_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available response bodies of Rate Management APIs.

- 
**[Adjustment Details](./connect_responses_rate_adjustment_detail.htm.md)**  

Output representation of a rate adjustment request.

- 
**[Line Item Waterfall Response](./connect_responses_rating_line_item_waterfall_response.htm.md)**  

Output representation of the line item waterfall response.

- 
**[Rate Plan Response](./connect_responses_rate_plan_response.htm.md)**  

Output representation of the details of a rate plan.

- 
**[Rating Error Response](./connect_responses_rating_error_response.htm.md)**  

Output representation of the error details related to the API request.

- 
**[Rating Waterfall Response](./connect_responses_rating_waterfall_response.htm.md)**  

Output representation of a rating waterfall request.

=== ARTICLE: rate_management_flow_metadata_api.htm ===
---
page_id: rate_management_flow_metadata_api.htm
title: Flow for Rate Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Rate Management

Represents the metadata associated with a flow. With Flow, you can create an
    application that takes users through a series of pages to query and update the records in the
    database. You can also run logic and provide branching capability based on user input to build
    dynamic applications.

    

## FlowActionCall

      
      

Rate Management exposes additional actionType values for the FlowActionCall metadata
        type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values for Rate Management include: `invokeRatingService`—Invoke the rating service to rate the usage records. |

=== ARTICLE: rate_management_invocable_actions_parent.htm ===
---
page_id: rate_management_invocable_actions_parent.htm
title: Rate Management Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Management Standard Invocable Actions

Learn more about the standard invocable actions available with Rate
  Management.

- 
**[Invoke Rating Service Action](./actions_obj_invoke_rating_service.htm.md)**  

Invoke the rating service to rate the usage records.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: rate_management_metadata_api_parent.htm ===
---
page_id: rate_management_metadata_api_parent.htm
title: Rate Management Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Management Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[IndustriesRatingSettings](./meta_industriesratingsettings.htm.md)**  

Represents the settings for Rate 		Management.

- 
**[Flow for Rate Management](./rate_management_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that takes users through a series of pages to query and update the records in the     database. You can also run logic and provide branching capability based on user input to build     dynamic applications.

=== ARTICLE: rate_management_overview.htm ===
---
page_id: rate_management_overview.htm
title: Rate Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Management

Quote and price products based on predefined rates for future use of the product or
  service.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Management where Rate Management is enabled |

  

 

- 
**[Rate Management Standard Objects](./rate_management_std_objects_parent.htm.md)**  

The Rate Management data model provides objects and fields to manage rates and discounts   for a product's resource consumption.

- 
**[Rate Management Metadata API Types](./rate_management_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Rate Management Business APIs](./rate_management_business_api_overview.htm.md)**  

Use the Rate Management Business APIs to get rate plan and persisted rating waterfall     details.

- 
**[Rate Management Standard Invocable Actions](./rate_management_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Rate   Management.

#### See Also

- [*Salesforce Help*: Rate Management Permission Set Licenses](https://help.salesforce.com/s/articleView?id=ind.rm_rate_management_psls.htm&type=5&language=en_US)

=== ARTICLE: rate_management_std_objects_parent.htm ===
---
page_id: rate_management_std_objects_parent.htm
title: Rate Management Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rate Management Standard Objects

The Rate Management data model provides objects and fields to manage rates and discounts
  for a product's resource consumption.

- 
**[BindingObjectCustomExt](./sforce_api_objects_bindingobjectcustomext.htm.md)**  

Represents the external or custom target object that's bound to the          entitlements granted with the sellable product. This object is available in API       version 64.0 and later.

- 
**[BindingObjectRateAdjustment](./sforce_api_objects_bindingobjectrateadjustment.htm.md)**  

Represents the rate adjustments of the usage resource associated with          the binding object that's used to charge over consumption. This object is available in       API version 64.0 and later.

- 
**[BindingObjectRateCardEntry](./sforce_api_objects_bindingobjectratecardentry.htm.md)**  

Represents the rate card entry details of the usage resource          associated with the binding object that's used to charge over consumption. This object       is available in API version 64.0 and later. 

- 
**[PriceBookRateCard](./sforce_api_objects_pricebookratecard.htm.md)**  

Represents a junction between price book and rate card objects.       This object is available in API version 62.0 and later.

- 
**[RateAdjustmentByAttribute](./sforce_api_objects_rateadjustmentbyattribute.htm.md)**  

       Represents the adjustments that determine the rate of a resource based on its          rate-impacting attributes. These attributes are linked to the usage product record. Rates          are then influenced by conditions specified in the Attribute Based Adjustment Condition          object. Finally, the charge rate is determined by using the Attribute Based Adjustment Rule          object. This object is available in API version 62.0 and later.

- 
**[RateAdjustmentByTier](./sforce_api_objects_rateadjustmentbytier.htm.md)**  

Represents the adjustments for the rate of a resource that’s          determined based on the specified tiers. This object stores information about the type of          adjustment used, the value of the adjustment type, and any applicable boundaries. This       object is available in API version 62.0 and later.

- 
**[RateCard](./sforce_api_objects_ratecard.htm.md)**  

Represents the rules used to rate the consumption of a group of          resources within a product. Usage of a resource is billed at a specified rate if the user          consumes more than their allowance for a time period. This object is available in API       version 62.0 and later.

- 
**[RateCardEntry](./sforce_api_objects_ratecardentry.htm.md)**  

Represents a rule that determines the charge rate for using a          product's resource. Each entry is linked to one rate card exclusively, and its activation          or deactivation can be controlled by assigning effective dates. This object is       available in API version 62.0 and later.

- 
**[RatingFrequencyPolicy](./sforce_api_objects_ratingfrequencypolicy.htm.md)**  

Represents the policy that defines the frequency at which rating is          triggered for the ratable summary records. This object is available in API version       62.0 and later.

- 
**[RatingRequest](./sforce_api_objects_ratingrequest.htm.md)**  

Represents the common run-time parameters, such as context definition          and rating procedure for a set of records in the rateable summary table. This object       is available in API version 62.0 and later.

- 
**[RatingRequestBatchJob](./sforce_api_objects_ratingrequestbatchjob.htm.md)**  

Represents a junction between the rating request and batch job          objects. This object is available in API version 62.0 and later.

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: sforce_api_objects_bindingobjectcustomext.htm ===
---
page_id: sforce_api_objects_bindingobjectcustomext.htm
title: BindingObjectCustomExt
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_bindingobjectcustomext.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BindingObjectCustomExt

Represents the external or custom target object that's bound to the
         entitlements granted with the sellable product. This object is available in API
      version 64.0 and later.

      

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

         
         
            
- 
               

This object is available in Revenue Management when Rate Management is enabled.

            

            
- 
               

Users with any Rate Management permission set (Admin, Manager, Designtime,
                  Runtime) can view records. Only Admins can create, edit, and delete records.

            

         

      

      

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
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the binding custom object record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product usage grant. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |

=== ARTICLE: sforce_api_objects_bindingobjectrateadjustment.htm ===
---
page_id: sforce_api_objects_bindingobjectrateadjustment.htm
title: BindingObjectRateAdjustment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_bindingobjectrateadjustment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BindingObjectRateAdjustment

Represents the rate adjustments of the usage resource associated with
         the binding object that's used to charge over consumption. This object is available in
      API version 64.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

         
         
            
- This object is available in Revenue Management when Rate Management is enabled.

            
- Users with any Rate Management permission set (Admin, Manager, Designtime, Runtime)
               can view records.

         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AdjustmentType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The type of rate adjustment related to the associated rate card entry. Valid values are: `Amount` `Override` `Percentage` |
| AdjustmentValue | **Type** double **Properties** Filter, Sort **Description** The value of the rate adjustment based on the adjustment type. |
| BindingObjectRateCardEntryId | **Type** reference **Properties** Filter, Group, Sort **Description** The binding object rate card entry associated with the binding object rate adjustment. This field is a relationship field. **Relationship Name** BindingObjectRateCardEntry **Relationship Type** Master-detail **Refers To** BindingObjectRateCardEntry (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| LowerBound | **Type** double **Properties** Filter, Sort **Description** The minimum quantity of the rate adjustment value that can be applied to the binding object rate adjustment record. This must be a positive number that's less than or equal to the upper bound of the tier. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The autogenerated identifier for the binding object rate adjustment record. |
| UpperBound | **Type** double **Properties** Filter, Nillable, Sort **Description** The maximum quantity of the rate adjustment value that can be applied to the binding object rate adjustment record. This must be a positive number. Set this value one digit higher than the quantity you want the tier to include. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BindingObjectRateAdjustmentFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[BindingObjectRateAdjustmentHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[BindingObjectRateAdjustmentShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_bindingobjectratecardentry.htm ===
---
page_id: sforce_api_objects_bindingobjectratecardentry.htm
title: BindingObjectRateCardEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_bindingobjectratecardentry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BindingObjectRateCardEntry

Represents the rate card entry details of the usage resource
         associated with the binding object that's used to charge over consumption. This object
      is available in API version 64.0 and later. 

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

         
         
            
- This object is available in Revenue Management when Rate Management is enabled.

            
- Users with any Rate Management permission set (Admin, Manager, Designtime, Runtime)
               can view records.

         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| BindingObjectId | **Type** reference **Properties** Filter, Group, Sort **Description** The object associated with the entitlements that are granted with the sellable product. This field is a polymorphic relationship field. **Relationship Name** BindingObject **Refers To** Account, BindingObjectCustomExt, Contract |
| BindingObjectRateOrder | **Type** double **Properties** Filter, Nillable, Sort **Description** The order that determines the applicable binding object rate when multiple rates are defined for an Anchor target within an effective period. Available in API version 65.0 and later. |
| BindingObjectUsageResourceKey | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** Specifies the autogenerated composite key combining the BindingObjectId and UsageResourceId fields. The format used is `BindingObjectId_UsageResourceId` and must be within 18 characters. The key is generated on saving the BindingObjectRateCardEntry record. For example,`001xx000003Gc4FAAS_1BRxx0000004C95GAE`. Available in API version 66.0 and later. |
| EffectiveFrom | **Type** dateTime **Properties** Filter, Sort **Description** The date and time when the associated rate card entry comes into effect. |
| EffectiveTo | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time until which the associated rate card entry remains effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The autogenerated identifier for the binding object rate card entry record. For example, `BORCE-00004` or `BORCE-4567`. |
| NegotiatedRate | **Type** double **Properties** Filter, Nillable, Sort **Description** The rate negotiated for the associated binding object. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RateCardEntryId | **Type** reference **Properties** Filter, Group, Sort **Description** The rate card entry associated with the binding object. This field is a relationship field. **Relationship Name** RateCardEntry **Refers To** RateCardEntry |
| RateCardId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The rate card associated to the binding object. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateCardType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of the rate card associated with the binding object rate card entry. Valid values are: `Attribute` `Base` `Tier` |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The standard unit of measure associated with the rate defined for the binding object. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| SourceAssetId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The asset that's used to create the binding object rate card entry. This field is a relationship field. **Relationship Name** SourceAsset **Refers To** Asset |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the binding object rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BindingObjectRateAdjustmentFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[BindingObjectRateAdjustmentHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[BindingObjectRateAdjustmentShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_pricebookratecard.htm ===
---
page_id: sforce_api_objects_pricebookratecard.htm
title: PriceBookRateCard
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_pricebookratecard.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PriceBookRateCard

Represents a junction between price book and rate card objects.
      This object is available in API version 62.0 and later.

      
         

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
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated identifier for the price book rate card record. |
| PriceBookId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Price book ID that's associated with the rate cards IDs. For Quote, Order, and Contracts, the price book IDs identify the associated rate cards. This field is a relationship field. **Relationship Name** PriceBook **Relationship Type** Master-detail **Refers To** Pricebook2 (the master object) |
| RateCardId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Rate card ID that's associated with the price book. This field is a relationship field. **Relationship Name** RateCard **Relationship Type** Master-detail **Refers To** RateCard (the detail object) |
| RateCardType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Type of rate card associated with the price book. Valid values are: `Attribute` `Base` `Tier` |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[PriceBookRateCardFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[PriceBookRateCardHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_rateadjustmentbyattribute.htm ===
---
page_id: sforce_api_objects_rateadjustmentbyattribute.htm
title: RateAdjustmentByAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_rateadjustmentbyattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RateAdjustmentByAttribute

      Represents the adjustments that determine the rate of a resource based on its
         rate-impacting attributes. These attributes are linked to the usage product record. Rates
         are then influenced by conditions specified in the Attribute Based Adjustment Condition
         object. Finally, the charge rate is determined by using the Attribute Based Adjustment Rule
         object. This object is available in API version 62.0 and later.

      
         

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
| AdjustmentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Type of rate adjustment. Valid values are: `Amount` `Override` `Percentage` |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** Value of the rate adjustment based on the selected adjustment type. |
| AttributeBasedAdjRuleId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the attribute based adjustment rule associated with this rate adjustment by attribute record. This field is a relationship field. **Relationship Name** AttributeBasedAdjRule **Refers To** AttributeBasedAdjRule |
| EffectiveFrom | **Type** dateTime **Properties** Filter, Sort **Description** Date and time when the associated rate card entry comes into effect. |
| EffectiveTo | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time until when the associated rate card entry remains effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated identifier for the rate adjustment by attribute record. |
| ProductId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the product whose resource is being used as the associated rate card entry. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |
| ProductSellingModelId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the product selling model for the associated rate card entry. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| RateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the rate card entry associated with this rate adjustment by attribute record. This field is a relationship field. **Relationship Name** RateCardEntry **Relationship Type** Master-detail **Refers To** RateCardEntry (the master object) |
| RateCardEntryStatus | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Status of the rate card entry associated with this rate adjustment by attribute. Valid values are: `Active` `Draft` `Inactive` The default value is `Draft`. Available in API version 63.0 and later. |
| RateCardId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the rate card of the associated rate card entry. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the standard unit of measure record of the associated rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| RateUnitOfMeasureName | **Type** string **Properties** Filter, Group, Sort **Description** Name of the standard unit of measure record of the associated rate card entry. |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the resource selected for the associated rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RateAdjustmentByAttributeFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RateAdjustmentByAttributeHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_rateadjustmentbytier.htm ===
---
page_id: sforce_api_objects_rateadjustmentbytier.htm
title: RateAdjustmentByTier
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_rateadjustmentbytier.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RateAdjustmentByTier

Represents the adjustments for the rate of a resource that’s
         determined based on the specified tiers. This object stores information about the type of
         adjustment used, the value of the adjustment type, and any applicable boundaries. This
      object is available in API version 62.0 and later.

      
         

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
| AdjustmentType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Type of rate adjustment. Valid values are: `Amount` `Override` `Percentage` |
| AdjustmentValue | **Type** double **Properties** Create, Filter, Sort, Update **Description** Value of the rate adjustment based on the selected adjustment type. |
| EffectiveFrom | **Type** dateTime **Properties** Filter, Sort **Description** Date and time when the associated rate card entry comes into effect. |
| EffectiveTo | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Date and time until when the associated rate card entry remains effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| LowerBound | **Type** double **Properties** Create, Filter, Sort, Update **Description** Minimum quantity of the rate adjustment value that can be applied to the record. This value must be a positive integer and must be less than the upper bound of the tier. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated identifier for the rate adjustment by tier record. |
| ProductId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the product whose resource is being used as the associated rate card entry. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |
| ProductSellingModelId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the product selling model for the associated rate card entry record. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| RateCardEntryId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the rate card entry associated with this rate adjustment by tier record. This field is a relationship field. **Relationship Name** RateCardEntry **Relationship Type** Master-detail **Refers To** RateCardEntry (the master object) |
| RateCardEntryStatus | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Status of the rate card entry associated with this rate adjustment by tier. Valid values are: `Active` `Draft` `Inactive` The default value is `Draft`. Available in API version 63.0 and later. |
| RateCardId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the rate card of the associated rate card entry. This field is a relationship field. **Relationship Name** RateCard **Refers To** RateCard |
| RateUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the standard unit of measure record of the associated rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| RateUnitOfMeasureName | **Type** string **Properties** Filter, Group, Sort **Description** Name of the standard unit of measure record of the associated rate card entry. |
| UpperBound | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Maximum quantity of the rate adjustment value that can be applied to the record. This value must be a positive double and must be greater than the lower bound of the tier. |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the resource selected for the associated rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RateAdjustmentByTierFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RateAdjustmentByTierHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_ratecard.htm ===
---
page_id: sforce_api_objects_ratecard.htm
title: RateCard
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_ratecard.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RateCard

Represents the rules used to rate the consumption of a group of
         resources within a product. Usage of a resource is billed at a specified rate if the user
         consumes more than their allowance for a time period. This object is available in API
      version 62.0 and later.

      

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
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Description about the rate card. |
| EffectiveFrom | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** Date and time when the rate card becomes effective. |
| EffectiveTo | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Date and time until when the rate card remains effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Name of the rate card. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Type of rate card. Valid values are: `Attribute` `Base` `Tier` |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RateCardFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RateCardHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[RateCardShare](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_ratecardentry.htm ===
---
page_id: sforce_api_objects_ratecardentry.htm
title: RateCardEntry
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_ratecardentry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RateCardEntry

Represents a rule that determines the charge rate for using a
         product's resource. Each entry is linked to one rate card exclusively, and its activation
         or deactivation can be controlled by assigning effective dates. This object is
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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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
| DefaultUnitOfMeasureClassId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the default unit of measure classification record associated with this rate card entry. This field is a relationship field. **Relationship Name** DefaultUnitOfMeasureClass **Refers To** UnitOfMeasureClass |
| DefaultUnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the default unit of measure record associated with this rate card entry. This field is a relationship field. **Relationship Name** DefaultUnitOfMeasure **Refers To** UnitOfMeasure |
| EffectiveFrom | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** Date and time when the rate card entry comes into effect. |
| EffectiveTo | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** Date and time until when the rate card entry remains effective. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated identifier for the rate card entry record. |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the product whose resource is being used as a rate card entry. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |
| ProductSellingModelId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the product selling model associated with this rate card entry. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| Rate | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Value of the rate card entry. |
| RateCardId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the rate card associated with this rate card entry. This field is a relationship field. **Relationship Name** RateCard **Relationship Type** Master-detail **Refers To** RateCard (the master object) |
| RateCardType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Type of rate card associated with this rate card entry. Valid values are: `Attribute` `Base` `Tier` Available in API version 63.0 and later. |
| RateNegotiation | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Type of rate negotiation applicable to the rate card entry. Valid values are: `Negotiable` `NonNegotiable` The default value is `Negotiable`. Available in API version 63.0 and later. |
| RateUnitOfMeasureClassId | **Type** reference **Properties** Filter, Group, Sort **Description** ID of the unit of measure classification record associated with this rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasureClass **Refers To** UnitOfMeasureClass |
| RateUnitOfMeasureId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the standard unit of measure record associated with this rate card entry. This field is a relationship field. **Relationship Name** RateUnitOfMeasure **Refers To** UnitOfMeasure |
| RateUnitOfMeasureName | **Type** string **Properties** Filter, Group, Sort **Description** Name of the standard unit of measure record of the associated rate card entry. |
| Status | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Status of the rate card entry. `Active` `Draft` `Inactive` The default value is `Draft`. Available in API version 63.0 and later. |
| UsageProductId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the product associated with the resource for which the rate is specified. This field is a relationship field. **Relationship Name** UsageProduct **Refers To** Product2 |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the resource associated with this rate card entry. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RateCardEntryFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RateCardEntryHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_ratingfrequencypolicy.htm ===
---
page_id: sforce_api_objects_ratingfrequencypolicy.htm
title: RatingFrequencyPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_ratingfrequencypolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RatingFrequencyPolicy

Represents the policy that defines the frequency at which rating is
         triggered for the ratable summary records. This object is available in API version
      62.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Name of the rating frequency policy. This is a mandatory field. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** ID of the product for which the rating policy is defined. This field is a relationship field. This field is deprecated and will be retired in a future version. **Relationship Name** Product **Refers To** Product2 |
| RatingDelayDuration | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Duration of delay—in hours—post the billing period after which the rating is to be triggered. |
| RatingDelayDurationUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the unit for the specified rating delay duration. Available in API version 65.0 and later. Valid values are: `Days` `Hours` |
| RatingPeriod | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Period for which the usage of a product and usage resource combination is to be rated. Valid values are: `Daily` `Monthly` |
| UsageResourceId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the usage resource for which the rating policy is defined. This field is a relationship field. This field is deprecated and will be retired in a future version. **Relationship Name** UsageResource **Refers To** UsageResource |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RatingFrequencyPolicyFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RatingFrequencyPolicyHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[RatingFrequencyPolicyOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[RatingFrequencyPolicyShare](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_ratingrequest.htm ===
---
page_id: sforce_api_objects_ratingrequest.htm
title: RatingRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_ratingrequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RatingRequest

Represents the common run-time parameters, such as context definition
         and rating procedure for a set of records in the rateable summary table. This object
      is available in API version 62.0 and later.

      

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
- 
- 
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| ContextDefinition | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Context definition that's used for context instance creation, which encapsulates all aggregated records that are stamped for the rating request. |
| ContextMapping | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Context mapping that's used for context instance creation, which encapsulates all aggregated records that are stamped for the rating request. If no ID is provided, default context mapping is used. |
| DoesExcludeWaterfall | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the waterfall isn't generated for the rating request (`true`) or is generated (`false`). The default value is `false`. Available in API version 64.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-generated identifier for the rating request record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RatingProcedureName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Procedure name that's used to rate the aggregated records that are stamped for rating request. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Status of the rating request. Valid values are: `Failed` `Pending` `RatingComplete` `RatingInProgress` `ReadyForRating` |

      

      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RatingRequestFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RatingRequestHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[RatingRequestShare](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_ratingrequestbatchjob.htm ===
---
page_id: sforce_api_objects_ratingrequestbatchjob.htm
title: RatingRequestBatchJob
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_ratingrequestbatchjob.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Rate Management
parent_page: rate_management_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RatingRequestBatchJob

Represents a junction between the rating request and batch job
         objects. This object is available in API version 62.0 and later.

      
         

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
| BatchJobId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** ID of the batch job that triggered the rating request on the aggregated records. This field is a relationship field. **Relationship Name** BatchJob **Refers To** BatchJob |
| ErrorCode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Error code that defines the batch job failure. Valid values are: `BadRequest` `InternalError` |
| ErrorMessage | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Error message that describes the cause of the batch job failure. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last referred to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** Timestamp for when the current user last viewed a record related to this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Name of the rating request batch job record. |
| RatingRequestId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** ID of the rating request record associated with the batch job. This field is a relationship field. **Relationship Name** RatingRequest **Relationship Type** Master-detail **Refers To** RatingRequest (the master object) |

      

      
      

## Associated Objects

         
         

This object has these associated objects. If the API version isn’t specified, they’re
            available in the same API versions as this object. Otherwise, they’re available in the
            specified API version and later.

         
            
               

**[RatingRequestBatchJobFeed](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[RatingRequestBatchJobHistory](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

