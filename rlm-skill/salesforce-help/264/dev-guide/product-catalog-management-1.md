# Revenue Management Developer Guide 264 — sección: Product Catalog Management (parte 1/2) (135 artículos)

=== ARTICLE: actions_obj_execute_qualification_procedure.htm ===
---
page_id: actions_obj_execute_qualification_procedure.htm
title: Execute Qualification Procedure Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_execute_qualification_procedure.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Execute Qualification Procedure Action

Execute a qualification procedure, which returns the qualification
            status for the specified products.

        

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

## Special Access Rules

The Execute Qualification Procedure action is
                available in Enterprise, Unlimited, and Developer Editions where Product Discovery
                is enabled.

        
        

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
| additionalContextData | **Type** Apex-defined **Description** Collection of Apex AdditionalContextData records that contain additional context data for nodes of the custom context definition, if applicable. You can add details for up to 10 nodes. See [AdditionalContextData](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md). |
| contextDefinitionName | **Type** string **Description** Name of the custom context definition that’s used to create context data for categories. If null, the default context definition is used. |
| contextMappingName | **Type** string **Description** Name of the context mapping. By default, the default context mapping associated with the context definition is used. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| productIds | **Type** string **Description** Required. Collection of IDs of products that are to be checked for qualification. |
| qualificationProcedureName | **Type** string **Description** Name of the custom qualification procedure that’s executed to determine the category list. If null, the default qualification procedure is executed. |
| userContextInputRepresentation | **Type** Apex-defined **Description** An Apex UserContextInputRepresentation record that contains user details, such as account ID, geographical location, language preferences, and more. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex ApiStatusOutputRepresentation record that contains the status of the request, including the status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created by using the specified context definition. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| qualificationResultRepresentations | **Type** Apex-defined **Description** Collection of Apex QualificationResultRepresentation records that contain details about the qualified product. |

        

        
        

## Example

            
            
                
                    
                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
Invocable.Action action = Invocable.Action.createStandardAction('executeQualificationProcedure');

ConnectApi.UserContextInputRepresentation userContext = new ConnectApi.UserContextInputRepresentation();
userContext.accountId = '001xx000003GYiEAAW';

runtime_industries_cpq.ContextDataInput data = new runtime_industries_cpq.ContextDataInput();
String nodeNameVal = 'Quote__c';
Map<String,Object> nodeDataVal = new Map<String,Object>();
nodeDataVal.put('id',(Object)'0Q0xx0000004CDsCAM');
nodeDataVal.put('businessObjectType',(Object)'Quote');
data.nodeName = nodeNameVal;
data.nodeData = nodeDataVal;
List<runtime_industries_cpq.ContextDataInput> contextData= new List<runtime_industries_cpq.ContextDataInput>();
contextData.add(data);
runtime_industries_cpq.AdditionalContextData additionalContextDataOut = new runtime_industries_cpq.AdditionalContextData();
additionalContextDataOut.additionalContextData = new List<runtime_industries_cpq.ContextDataInput>();
additionalContextDataOut.additionalContextData.add(data);

List<String> productIds = new List<String>();
prodIds.add('01txx0000006i2ZAAQ');
prodIds.add('01txx0000006i35AAA');
action2.setInvocationParameter('productIds', productIds);
action.setInvocationParameter('correlationId', '9cbb9650-48c5-11ed-96d1-0afcf185843b');
action.setInvocationParameter('userContextInputRepresentation', userContext);
action.setInvocationParameter('qualificationProcedureName', 'CatQual02');
action.setInvocationParameter('contextDefinitionName', 'CategoryCD');
action.setInvocationParameter('contextMappingName', 'ProductDiscoveryMapping');
action.setInvocationParameter('additionalContextData', additionalContextDataOut);

List<Invocable.Action.Result> results = action.invoke();
System.debug('Execute Qualification Procedure Action + '+results);
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "executeQualificationProcedure",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "apiStatusOutputRepresentation": {
        "statusMessage": null,
        "statusCode": "FetchedDetailsSuccessfully",
        "messages": []
      },
      "qualificationResultRepresentations": [
        {
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "productId": "01tSG000007uDL8YAM"
        },
        {
          "qualificationContext": {
            "reason": "Product is not qualified because one or more field(s) do not match the qualification criteria. Fields:- ProductId - 01tSG000007uDLBYA2 Max_Number_of_Employees - 50 Min_Number_of_Employees - 50 RootProductId - ",
            "isQualified": false
          },
          "productId": "01tSG000007uDLBYA2"
        }
      ],
      "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
      "contextId": "0000000b28op21g00251747224654739cade16577eac4c8fb5d94a20d952fdab"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_find_products.htm ===
---
page_id: actions_obj_find_products.htm
title: Find Products Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_find_products.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Find Products Action

Search for the products from a catalog, category, or subcategory by
			using the specified search term.

		
			

This action is available in API version 62.0 and later.

		

		

## Special Access Rules

The Find Products action is available in
				Enterprise, Unlimited, and Developer Editions where Product Discovery is
				enabled.

You can invoke this action via Apex and Flows only.

		
		

## Inputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** An array of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain the additional nodes that are used along with the context definition nodes for data hydration. The maximum number of supported nodes is 10. |
| additionalFields | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.AdditionalFields`](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains an array of additional standard or custom fields to include in the response. The supported objects are: `Product2` `ProductAttributeDefinition`—If the fields defined for the `ProductAttributeDefinition` object aren’t available for the `ProductClassificationAttr` object, then the API request fails. |
| catalogId | **Type** string **Description** Catalog ID that’s used to find and retrieve the products. |
| categoryId | **Type** string **Description** ID of the category or subcategory to get the products for. |
| contextDefinition | **Type** string **Description** API name of the context definition used for context creation. If you don’t specify a value, the context selected on the Product Discovery Settings page from Setup is used. |
| contextMapping | **Type** string **Description** API name of the context mapping that’s used for data hydration. The value of this parameter is used only if it belongs to the specified context definition. |
| correlationId | **Type** string **Description** Currency code that’s used to calculate and show prices. Only the products with the currency code matching the specified currency code are fetched. |
| currencyCode | **Type** string **Description** Currency code that’s used to calculate and show prices. |
| cursor | **Type** string **Description** A unique identifier that represents the position of the product from which the next set of results are retrieved. |
| executeConfigurationRules | **Type** boolean **Description** Indicates whether configuration rules must run (`true`) or not (`false`). Available in API version 67.0 and later. |
| enablePricing | **Type** boolean **Description** Indicates whether the pricing procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Pricing Procedure setting from Setup. |
| enableQualification | **Type** boolean **Description** Indicates whether the qualification procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Qualification Procedure setting from Setup. |
| filter | **Type** Apex-defined **Description** A collection of Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) records where each record contains a related object and the filter criteria that’s applied on the object. The filter parameter supports only the `name` property. The supported operators are: `eq` `in` `contains` If this parameter contains multiple criteria, all the criteria are applied. |
| includeCatalogDetails | **Type** boolean **Description** Indicates whether catalog details must be included in the response (`true`) or not (`false`). |
| limit | **Type** integer **Description** Maximum number of results to be returned in the response. Enter a value from 1 through 100. The default value is 10. |
| orderBy | **Type** string **Description** Comma-separated string of key-value pairs that specify how results are sorted. Each string must contain a field name and its sort order. For example, `["name:asc",”custom_field:asc”]`. |
| priceBookId | **Type** string **Description** ID of the pricebook from which you wan to retrieve the pricing details. |
| productClassificationId | **Type** string **Description** ID of the product classification that’s used to filter products. |
| pricingProcedure | **Type** string **Description** API name of the pricing procedure to calculate product prices. If you don’t specify a value, the pricing procedure selected on the Product Discovery Settings page from Setup is used. |
| qualificationProcedure | **Type** string **Description** API name of the qualification procedure to evaluate product eligibility. If you don’t specify a value, the qualification procedure selected on the Product Discovery Settings page from Setup is used. |
| transactionContextId | **Type** string **Description** Context ID of the quote or order. Available in API version 67.0 and later. |
| transactionId | **Type** string **Description** ID of the quote or order. Available in API version 67.0 and later. |
| relatedObjectFilters | **Type** Apex-defined **Description** A collection of Apex [`runtime_industries_cpq.RelatedObjectFilterInputRepresentation`](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md) records, where each record contains a related object and the filter criteria that’s applied on the object. |
| searchTerm | **Type** string **Description** Required. Search term to find and retrieve products. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextInputRepresentation` record that contains the user details to evaluate product eligibility and calculate prices. |

		

		

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

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| apiStatus | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains a status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created by using the specified context definition. |
| correlationId | **Type** string **Description** ID to reference a series of related actions. |
| cursor | **Type** string **Description** Unique identifier that represents the position of the next product in the dataset. It’s used as an input to retrieve the next set of products. |
| facets | **Type** Apex-defined **Description** Collection of Apex ProductFacetsRepresentation records that contain details of the facet that's retrieved. |
| results | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.SearchProductsRepresentation`](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md) record that contains the products that match the query. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextRepresentation` record that includes the user details. |

		

		

## Example

			
			
				
					
					
					
: 
						

Here's a sample input to call this invocable action from Apex code.

						

```
Invocable.Action action = Invocable.Action.createStandardAction('findProducts');
action.setInvocationParameter('searchTerm', 'Additional API');
action.setInvocationParameter('executeConfigurationRules', true);
action.setInvocationParameter('catalogId', '0ZSVW000000AhdB4AS');
action.setInvocationParameter('transactionId', '0Q0VW0000018J6X0AU');
List<String> orderBy = new List<String>();
orderBy.add('name:asc');
action.setInvocationParameter('orderBy', orderBy);
List<Invocable.Action.Result> results = action.invoke();

for (Invocable.Action.Result res : results) {
    if (res.isSuccess()) {
        Map<String, Object> outMap = res.getOutputParameters();
        String jsonOutput = JSON.serialize(outMap);	
        System.debug(jsonOutput);
    }
}

```

					

					
: 
						

Here’s a sample response for this action.

						

```
{
  "facets": [],
  "apiStatus": {
    "statusMessage": null,
    "statusCode": "FetchedDetailsSuccessfully",
    "messages": []
  },
  "results": [
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w22AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w12AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w32AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API",
      "productClassification": {
        "id": "11BVW000004ljiZ2AQ"
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfGYAQ",
          "price": 15000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg8YAA",
          "price": 2000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg9YAA",
          "price": 1500,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7txYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_api",
      "discontinuedDate": null,
      "description": null,
      "configureDuringSale": "Allowed",
      "configurationRules": [
        {
          "type": "disable",
          "details": [
            {
              "message": "This is disabled"
            }
          ]
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tyYAA",
          "id": "0iOVW00000049w42AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-FLEX",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfFYAQ",
          "price": 450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Flex (100M)",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tyYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_flex",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tzYAA",
          "id": "0iOVW00000049w52AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-GOVT",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfHYAQ",
          "price": 1450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Gov",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tzYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_govt",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u0YAA",
          "id": "0iOVW00000049w92AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PREP",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfSYAQ",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Pre-Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u0YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_preprod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u1YAA",
          "id": "0iOVW00000049wA2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PROD",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfdYAA",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u1YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_prod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    }
  ],
  "contextId": "0000000r25tp21g002517775323419202e0743b1f275423d8a489c12ca99da72",
  "correlationId": "4ac34e38-13d6-4720-97c4-4db7b3d41678"
}
```

					

				
			

		

		

## Usage of an Apex-Defined Data Type in a Flow

To use an Apex-defined input parameter in a flow, follow these guidelines.

			
				
					

**Create an Apex Class**

					
: Create an Apex class defining the input and output parameters. In the flow, include the
						Apex-defined input parameters for which you want to add the details. In this
						example, we’ve created a class named ProductServiceAction that takes an
						object’s API name and record ID as input, and returns the additional context
						data.

```
public class ProductServiceAction {
    // Define input parameters
    public class FlowInput{
        @InvocableVariable(required=false)
        public String objectApiName;
        
        @InvocableVariable(required=false)
        public String recordId;
    }
    
    // Define output parameters
    public class FlowOutput{
        @invocableVariable
        public runtime_industries_cpq.AdditionalContextData additionalContextDataFinalOutput = new runtime_industries_cpq.AdditionalContextData();
    }
    
    // This method is invoked from a Flow
    @InvocableMethod(label='Process Input' description='Creates the Array of ContextDataInput for additional Context Data')
    public static List<FlowOutput> processContextData(List<FlowInput> inputs){
        String apiName;
        String recId;
        FlowOutput output = new FlowOutput();
        
    // Capture input from the flow
        for(FlowInput input: inputs){
            apiName = input.objectApiName;
            recId = input.recordId;
            }
    // Populate the ContextDataInput list to store additional context data    
        List<runtime_industries_cpq.ContextDataInput> listContextData = new List<runtime_industries_cpq.ContextDataInput>();
        runtime_industries_cpq.ContextDataInput cd1 = new runtime_industries_cpq.ContextDataInput();
        cd1.nodeName = apiName;
        cd1.nodeData = new Map<String, Object>();
        cd1.nodeData.put('id',recId);
        listContextData.add(cd1);
       
        output.additionalContextDataFinalOutput.additionalContextData = listContextData;
        List<FlowOutput> flowOutputs = new List<FlowOutput>();
        flowOutputs.add(output);
        
        List<runtime_industries_cpq.RelatedObjectFilter> relatedObjectFilterList = new List<runtime_industries_cpq.RelatedObjectFilter>();
       
        runtime_industries_cpq.RelatedObjectFilter relatedObjectFilter = new runtime_industries_cpq.RelatedObjectFilter();

        relatedObjectFilter.objectName = 'ProductSpecificationRecType';
        List<runtime_industries_cpq.FilterCriteriaInputRepresentation> criteriaList = new  List<runtime_industries_cpq.FilterCriteriaInputRepresentation>();
        runtime_industries_cpq.FilterCriteriaInputRepresentation criteria = new runtime_industries_cpq.FilterCriteriaInputRepresentation();
        criteria.property = 'IsCommercial';
        criteria.operator = 'eq';
        criteria.value = 'true';
        criteriaList.add(criteria);
        relatedObjectFilter.criteria = criteriaList;

        relatedObjectFilterList.add(relatedObjectFilter);
        output.relatedObjectFilter.relatedObjectFilter  = relatedObjectFilterList;
         
		output.userContext.accountId = '001DU000001nx9BYAQ';
        
        return flowOutputs;
       
    }

}
```

				
				
					

**Create a Flow with the Necessary Variables and Components**

					
: Create a flow that enables users to add a search term to find products. Add the
						ProductService action that you’ve created above by using Apex. When a flow
						is invoked from a record, the flow sends the record's objectApiName and
						recordId to the Apex class, which then generates the flow output. The flow
						passes the objectApiName and recordId of the record that the flow is invoked
						from to the Apex class to generate the flow output. See [Example of How to
							Create a Flow for Product Discovery](https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm&type=5&language=en_US).

				
				
					

**Configure the Action**

					
: Configure the action (for example, Find Products action) to add values for the Apex-defined
						input parameters. Use the output of the created Apex class as the input of
						the Apex-defined parameter in the Find Products action, which users can use
						to find products.

=== ARTICLE: actions_obj_get_catalog_details.htm ===
---
page_id: actions_obj_get_catalog_details.htm
title: Get Catalog Details Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_catalog_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Catalog Details Action

Get details of a catalog record.

        
            

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

        

## Special Access Rules

            
            

The Get Catalog Details action is available in Enterprise, Unlimited, and Developer
                Editions where Product Discovery is enabled.

        

        
        

## Inputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| catalogId | **Type** string **Description** Required. ID of the catalog record. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, enabling reference to a specific transaction or event chain. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| catalogDetailsResult | **Type** Apex-defined **Description** Details of the catalog record. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |

        

        
        

## Example

            
            
                
                    
                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
Invocable.Action action = Invocable.Action.createStandardAction('getCatalogDetails');

action.setInvocationParameter('correlationId', '9cbb9650-48c5-11ed-96d1-0afcf185843b');
action.setInvocationParameter('catalogId', '0ZSZ6000000CtXYOA0');

List<Invocable.Action.Result> results = action.invoke();
System.debug('Catalog Details Action + '+results);
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "getCatalogDetails",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "apiStatusOutputRepresentation": {
        "statusMessage": null,
        "statusCode": "FetchedDetailsSuccessfully",
        "messages": []
      },
      "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
      "catalogDetailsResult": {
        "status": null,
        "numberOfCategories": 2,
        "name": "Hardware Catalog",
        "id": "0ZSZ6000000CtXYOA0",
        "effectiveStartDate": null,
        "effectiveEndDate": null,
        "description": "Hardware Catalog Desc",
        "customFields": null,
        "catalogType": "Sales",
        "catalogCode": "HC"
      }
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_get_catalogs.htm ===
---
page_id: actions_obj_get_catalogs.htm
title: Get Catalogs Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_catalogs.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Catalogs Action

Get a list of catalog records.

        
            

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

        

## Special Access Rules

            
        

        
        

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
| recordLimit | **Type** integer **Description** Number of catalog records to get. The minimum is 1, the maximum is 100, and the default is 100. |
| recordOffset | **Type** integer **Description** Number of catalog records to skip in the request. The default is 0. |
| correlationId | **Type** string **Description** Unique identifier for tracking requests and messages, allowing reference to a specific transaction or event chain. |
| orderBy | **Type** string **Description** Sort records in ascending or descending order. |

        

        

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
| resultCatalogList | **Type** Apex-defined **Description** List of filtered catalog records. See [CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md). |
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| recordLimit | **Type** integer **Description** Number of catalog records to show per page. |
| resultListCount | **Type** integer **Description** Number of catalog records in the result. |
| correlationId | **Type** string **Description** Unique identifier for tracking requests and messages, allowing reference to a specific transaction or event chain. |
| recordOffset | **Type** integer **Description** Number of catalog records to skip in the request. The default is 0. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
Invocable.Action action = Invocable.Action.createStandardAction('getCatalogs');

action.setInvocationParameter('correlationId', '9cbb9650-48c5-11ed-96d1-0afcf185843b');
action.setInvocationParameter('recordLimit', 1);
action.setInvocationParameter('recordOffset', 1);
String[] sortOrder = new String[]{'Name:ASC'};
action.setInvocationParameter('orderBy', sortOrder);

List<Invocable.Action.Result> results = action.invoke();
System.debug('Catalog List Action + '+results);
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "getCatalogs",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "resultListCount": 2,
      "apiStatusOutputRepresentation": {
        "statusMessage": null,
        "statusCode": "FetchedDetailsSuccessfully",
        "messages": []
      },
      "resultCatalogList": [
        {
          "status": null,
          "numberOfCategories": 2,
          "name": "Hardware Catalog",
          "id": "0ZSZ6000000CtXYOA0",
          "effectiveStartDate": null,
          "effectiveEndDate": null,
          "description": "Hardware Catalog Desc",
          "customFields": [],
          "catalogType": "Sales",
          "catalogCode": "HC"
        }
      ],
      "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
      "recordOffset": 0,
      "recordLimit": 1
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_get_categories.htm ===
---
page_id: actions_obj_get_categories.htm
title: Get Categories Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_categories.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Categories Action

Get the list of categories associated with a catalog
        record.

        
            

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

        

## Special Access Rules

            
            

The Get Categories action is available in Enterprise, Unlimited, and Developer
                Editions where Product Discovery is enabled.

        

        
        

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain additional context data for nodes of the custom context definition, if applicable. You can add details for up to 10 nodes. |
| catalogId | **Type** string **Description** Required. ID of the catalog record. |
| categoryNestLevel | **Type** integer **Description** Level of nesting within the category hierarchy to include in the request. |
| contextDefinitionName | **Type** string **Description** Name of the custom context definition that’s used to create context data for categories. If null, the default context definition is used. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| contextMappingName | **Type** string **Description** Name of the context mapping. By default, the default context mapping associated with the context definition is used. |
| enableQualificationProcedure | **Type** boolean **Description** Indicates whether qualification rules are applied to categories (`true`) or not (`false`). |
| filterInputRepresentation | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) records that contain the filter criteria applied to the category records. |
| parentCategoryId | **Type** string **Description** ID of the parent category record. |
| qualificationProcedureName | **Type** string **Description** Name of the custom qualification procedure that’s executed to determine the category list. If null, the default qualification procedure is executed. |
| userContextInputRepresentation | **Type** Apex-defined **Description** An Apex UserContextInputRepresentation record that contains user details, such as account ID, geographical location, language preferences, and more. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

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
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| resultCategoryList | **Type** Apex-defined **Description** List of filtered category records. See [CategoryOutputRepresentation](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md). |
| resultListCount | **Type** integer **Description** Number of category records in the result. |

        

        
        

## Example

            
            
                
                    
                    
: 

Here's a sample input to call this invocable action from Apex
                        code.

```
Invocable.Action action = Invocable.Action.createStandardAction('getCategories');

ConnectApi.UserContextInputRepresentation userContext = new ConnectApi.UserContextInputRepresentation();
userContext.accountId = '001xx000003GYiEAAW';

runtime_industries_cpq.ContextDataInput data = new runtime_industries_cpq.ContextDataInput();
String nodeNameVal = 'Quote__c';
Map<String,Object> nodeDataVal = new Map<String,Object>();
nodeDataVal.put('id',(Object)'0Q0xx0000004CDsCAM');
nodeDataVal.put('businessObjectType',(Object)'Quote');
data.nodeName = nodeNameVal;
data.nodeData = nodeDataVal;
List<runtime_industries_cpq.ContextDataInput> contextData= new List<runtime_industries_cpq.ContextDataInput>();
contextData.add(data);
runtime_industries_cpq.AdditionalContextData additionalContextDataOut = new runtime_industries_cpq.AdditionalContextData();
additionalContextDataOut.additionalContextData = new List<runtime_industries_cpq.ContextDataInput>();
additionalContextDataOut.additionalContextData.add(data);

action.setInvocationParameter('catalogId', '0ZSxx0000000002GAA');
action.setInvocationParameter('correlationId', '9cbb9650-48c5-11ed-96d1-0afcf185843b');
action.setInvocationParameter('userContextInputRepresentation', userContext);
action.setInvocationParameter('enableQualificationProcedure', True);
action.setInvocationParameter('qualificationProcedureName', 'CatQual02');
action.setInvocationParameter('contextDefinitionName', 'CategoryCD');
action.setInvocationParameter('contextMappingName', 'ProductDiscoveryMapping');
action.setInvocationParameter('additionalContextData', additionalContextDataOut);
//action.setInvocationParameter('categoryDepth', 4);
//action.setInvocationParameter('parentCategoryId', '0ZGxx0000000001GAA');

List<Invocable.Action.Result> results = action.invoke();
System.debug('Search Action + '+results);
```

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "getCategories",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "resultCategoryList": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": "Category is not qualified because one or more field(s) do not match the qualification criteria. Fields:- CategoryId - 0ZGxx0000000001GAA quotename - null Max_Number_of_Employees - 1500 Min_Number_of_Employees - 1500",
            "isQualified": false
          },
          "parentCategoryId": null,
          "name": "Laptops",
          "isNavigational": true,
          "id": "0ZGxx0000000001GAA",
          "hasSubCategories": true,
          "description": null,
          "childCategories": [],
          "catalogId": "0ZSxx0000000002GAA"
        },
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "Desktops",
          "isNavigational": true,
          "id": "0ZGxx0000000002GAA",
          "hasSubCategories": false,
          "description": null,
          "childCategories": [],
          "catalogId": "0ZSxx0000000002GAA"
        },
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "Accessories",
          "isNavigational": true,
          "id": "0ZGxx0000000003GAA",
          "hasSubCategories": false,
          "description": null,
          "childCategories": [],
          "catalogId": "0ZSxx0000000002GAA"
        }
      ],
      "resultListCount": 3,
      "apiStatusOutputRepresentation": {
        "statusMessage": null,
        "statusCode": "FetchedDetailsSuccessfully",
        "messages": []
      },
      "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_get_category_details.htm ===
---
page_id: actions_obj_get_category_details.htm
title: Get Category Details Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_category_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Category Details Action

Get details of a category record.

        
            

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

        

## Special Access Rules

            
            

The Get Category Details action is available in Enterprise, Unlimited, and Developer
                Editions where Product Discovery is enabled.

        

        
        

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain additional context data for nodes of the custom context definition, if applicable. You can add details for up to 10 nodes. |
| catalogId | **Type** string **Description** ID of the catalog record that’s used to search for products within a category. |
| categoryId | **Type** string **Description** Required. ID of the category or subcategory that’s used to search for products. |
| contextDefinitionName | **Type** string **Description** Name of the custom context definition that’s used to create context data for categories. If null, the default context definition is used. |
| contextMappingName | **Type** string **Description** Name of the context mapping. By default, the default context mapping associated with the context definition is used. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| enableQualificationProcedure | **Type** boolean **Description** Indicates whether qualification rules are applied to categories (`tru`e) or not (`false`). |
| filterInputRepresentation | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) records that contain the filter criteria applied to the category records. |
| qualificationProcedureName | **Type** string **Description** Name of the custom qualification procedure that’s executed to determine the category list. If null, the default qualification procedure is executed. |
| userContextInputRepresentation | **Type** Apex-defined **Description** An Apex UserContextInputRepresentation record that contains user details, such as account ID, geographical location, language preferences, and more. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| categoryDetailsRepresentations | **Type** Apex-defined **Description** Collection of Apex [CategoryDetailsRepresentation](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md) records that contain details about the retrieved category. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |

        

        
        

## Example

            
            
                
                    
                    
: 

Here's a sample input to call this invocable action from Apex
                        code.

```
Invocable.Action action = Invocable.Action.createStandardAction('getCategoryDetails');

ConnectApi.UserContextInputRepresentation userContext = new ConnectApi.UserContextInputRepresentation();
userContext.accountId = '001xx000003GYiEAAW';

runtime_industries_cpq.ContextDataInput data = new runtime_industries_cpq.ContextDataInput();
String nodeNameVal = 'Quote__c';
Map<String,Object> nodeDataVal = new Map<String,Object>();
nodeDataVal.put('id',(Object)'0Q0xx0000004CDsCAM');
nodeDataVal.put('businessObjectType',(Object)'Quote');
data.nodeName = nodeNameVal;
data.nodeData = nodeDataVal;
List<runtime_industries_cpq.ContextDataInput> contextData= new List<runtime_industries_cpq.ContextDataInput>();
contextData.add(data);
runtime_industries_cpq.AdditionalContextData additionalContextDataOut = new runtime_industries_cpq.AdditionalContextData();
additionalContextDataOut.additionalContextData = new List<runtime_industries_cpq.ContextDataInput>();
additionalContextDataOut.additionalContextData.add(data);

action.setInvocationParameter('categoryId', '0ZGxx0000000001GAA');
action.setInvocationParameter('correlationId', '9cbb9650-48c5-11ed-96d1-0afcf185843b');
action.setInvocationParameter('userContext', userContext);
action.setInvocationParameter('enableQualification', True);
action.setInvocationParameter('qualificationProcedure', 'CatQual02');
action.setInvocationParameter('contextDefinition', 'CategoryCD');
action.setInvocationParameter('contextMapping', 'ProductDiscoveryMapping');
action.setInvocationParameter('additionalContextData', additionalContextDataOut);

List<Invocable.Action.Result> results = action.invoke();
System.debug('Search Action + '+results);
```

                    
: 
                        

Here's a sample response when you call this action.

                        

```
{
  "root": [
    {
      "actionName": "getCategoryDetails",
      "errors": null,
      "invocationId": null,
      "isSuccess": true,
      "outcome": null,
      "outputValues": {
        "apiStatusOutputRepresentation": {
          "statusMessage": null,
          "statusCode": "FetchedDetailsSuccessfully",
          "messages": []
        },
        "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
        "categoryDetailsRepresentations": {
          "sortOrder": null,
          "qualificationContext": {
            "reason": "Category is not qualified because one or more field(s) do not match the qualification criteria. Fields:- CategoryId - 0ZGxx0000000001GAA quotename - null Max_Number_of_Employees - 1500 Min_Number_of_Employees - 1500",
            "isQualified": false
          },
          "parentCategoryId": null,
          "name": "Laptops",
          "isNavigational": true,
          "id": "0ZGxx0000000001GAA",
          "hasSubCategories": true,
          "description": null,
          "childCategories": [
            {
              "sortOrder": null,
              "qualificationContext": {
                "reason": null,
                "isQualified": true
              },
              "parentCategoryId": "0ZGxx0000000001GAA",
              "name": "level1",
              "isNavigational": true,
              "id": "0ZGxx000000004rGAA",
              "hasSubCategories": true,
              "description": null,
              "childCategories": [],
              "catalogId": null
            }
          ],
          "catalogId": "0ZSxx0000000002GAA"
        }
      },
      "sortOrder": -1,
      "version": 1
    }
  ]
}
```

=== ARTICLE: actions_obj_get_multiple_product_details.htm ===
---
page_id: actions_obj_get_multiple_product_details.htm
title: Get Multiple Product Details Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_multiple_product_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Multiple Product Details Action

Get product details for a list of products.

        
            

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

        

## Special Access Rules

            
            

The Get Multiple Product Details action is available in Enterprise, Unlimited, and
                Developer Editions where Product Discovery is enabled.

        

        
        

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

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
| additionalContextData | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain additional context data for nodes of the custom context definition, if applicable. You can add details for up to 10 nodes. |
| additionalFields | **Type** Apex-defined **Description** An Apex [AdditionalFields](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains the additional fields that are passed for the Product2 object. |
| catalogId | **Type** string **Description** ID of the catalog record. |
| contextDefinitionName | **Type** string **Description** Name of the custom context definition that’s used to create context data for categories. If null, the default context definition is used. |
| contextMappingName | **Type** string **Description** Name of the context mapping. By default, the default context mapping associated with the context definition is used. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| currencyCode | **Type** string **Description** Currency code that’s used to calculate and show prices. |
| enablePricing | **Type** boolean **Description** Indicates whether pricing procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, the **Pricing Procedure** setting must be enabled. |
| enableQualificationProcedure | **Type** boolean **Description** Indicates whether the qualification procedure is applied to categories (`true`) or not (`false`). |
| priceBookId | **Type** string **Description** ID of the pricebook that the pricing information is retrieved from. |
| pricingProcedureName | **Type** string **Description** Name of the pricing procedure to calculate product prices. If you don’t enter a value, the pricing procedure selected on the **Product Discovery Settings** page is used. |
| productDataInputs | **Type** Apex-defined **Description** Required. Collection of Apex [BulkProductDetailsInputBody](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md) records that contain details about the products that are to be retrieved. |
| qualificationProcedureName | **Type** string **Description** Name of the custom qualification procedure that’s executed to determine the category list. If null, the default qualification procedure is executed. |
| userContextInputRepresentation | **Type** Apex-defined **Description** An Apex UserContextInputRepresentation record that contains user details, such as account ID, geographical location, language preferences, and more. |

        

        

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

                        

                    

                
| Output | Details |
| --- | --- |
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created using the specified context definition. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| productDetailsOutputRepresentation | **Type** Apex-defined **Description** Collection of Apex [BulkProductDetailsRepresentation](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md) records that contain details of available products. |
| userContext | **Type** Apex-defined **Description** An Apex ConnectApi.UserContextRepresentation record containing user information. |

        

        
        

## Example

            
            
                
                    
                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
Invocable.Action action = Invocable.Action.createStandardAction('getMultipleProductDetails');

List<runtime_industries_cpq.BulkProductDetailsInputBody> productDataList = new List<runtime_industries_cpq.BulkProductDetailsInputBody>();
runtime_industries_cpq.BulkProductDetailsInputBody productData = new runtime_industries_cpq.BulkProductDetailsInputBody();
productData.productId = '01tIY000000nCxhYAE';

productDataList.add(productData);

runtime_industries_cpq.BulkProductDetailsInputBodyList productList = new runtime_industries_cpq.BulkProductDetailsInputBodyList();
productList.productData = productDataList; 

action.setInvocationParameter('productDataInputs', productList); 

List<Invocable.Action.Result> results = action.invoke();
System.debug('Result === ' + results);
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
[
  {
    "actionName": "getMultipleProductDetails",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "apiStatusOutputRepresentation": {
        "statusMessage": null,
        "statusCode": "FetchedDetailsSuccessfully",
        "messages": []
      },
      "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
      "contextId": null,
      "productDetailsOutputRepresentation": [
        {
          "unitOfMeasure": {
            "unitCode": null,
            "scale": null,
            "roundingMethod": null,
            "name": null,
            "id": null
          },
          "status": null,
          "qualificationContext": null,
          "productType": null,
          "productSpecificationType": null,
          "productSellingModelOptions": [
            {
              "productSellingModelId": "0jPxx0000000002EAA",
              "productSellingModel": {
                "status": "Active",
                "sellingModelType": "TermDefined",
                "pricingTermUnit": "Annual",
                "pricingTerm": 1,
                "name": "Term Based - Yearly",
                "id": "0jPxx0000000002EAA"
              },
              "productId": "01txx0000006i2oAAA",
              "id": "0iOxx000000000JEAQ"
            }
          ],
          "productRelatedComponent": {
            "unitOfMeasure": null,
            "sequence": null,
            "quoteVisibility": null,
            "quantityScaleMethod": null,
            "quantity": null,
            "productRelationshipTypeId": null,
            "productComponentGroupId": null,
            "productClassificationId": null,
            "parentSellingModelId": null,
            "parentProductId": null,
            "minQuantity": null,
            "maxQuantity": null,
            "isQuantityEditable": null,
            "isExcluded": null,
            "isDefaultComponent": null,
            "isComponentRequired": null,
            "id": null,
            "doesBundlePriceIncludeChild": null,
            "childSellingModelId": null,
            "childProductId": null
          },
          "productQuantity": {
            "quantity": null,
            "minQuantity": null,
            "maxQuantity": null
          },
          "productPricingInformation": null,
          "productInformation": null,
          "productComponentGroups": [],
          "productCode": "ASTCERT001",
          "productClassification": {
            "id": null
          },
          "prices": [
            {
              "pricingModel": {
                "unitOfMeasure": null,
                "pricingModelType": "TermDefined",
                "occurrence": 1,
                "name": "Term Based - Yearly",
                "id": "0jPxx0000000002EAA",
                "frequency": "Annual"
              },
              "priceBookId": "01sxx0000005ptpAAA",
              "priceBookEntryId": "01uxx0000008yXaAAI",
              "price": 2000,
              "isSelected": true,
              "isDerived": false,
              "isDefault": true,
              "effectiveTo": null,
              "effectiveFrom": null,
              "currencyIsoCode": "USD"
            }
          ],
          "nodeType": "simpleProduct",
          "name": "AI Specialist Certification",
          "isSoldOnlyWithOtherProds": false,
          "isQuantityEditable": null,
          "isDefaultComponent": null,
          "isComponentRequired": null,
          "isAssetizable": true,
          "isActive": true,
          "id": "01txx0000006i2oAAA",
          "endOfLifeDate": null,
          "displayUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsp4GoUP_nGiCXJ-wzYkPx-RlA_UCUX0zIDv3slxnJACqXaRd1vHJUZe6yQklUiXvEDgo&usqp=CAU",
          "discontinuedDate": null,
          "description": "The Certified Artificial Intelligence Expert certification is typically designed for individuals who have an in-depth understanding of artificial intelligence (AI) concepts, algorithms, and applications and want to validate their expertise in the field.",
          "configureDuringSale": "NotAllowed",
          "childProducts": [],
          "catalogs": [],
          "availabilityDate": null,
          "attributes": [],
          "attributeCategories": [],
          "additionalFields": []
        },
        {
          "unitOfMeasure": {
            "unitCode": null,
            "scale": null,
            "roundingMethod": null,
            "name": null,
            "id": null
          },
          "status": null,
          "qualificationContext": null,
          "productType": null,
          "productSpecificationType": null,
          "productSellingModelOptions": [
            {
              "productSellingModelId": "0jPxx0000000002EAA",
              "productSellingModel": {
                "status": "Active",
                "sellingModelType": "TermDefined",
                "pricingTermUnit": "Annual",
                "pricingTerm": 1,
                "name": "Term Based - Yearly",
                "id": "0jPxx0000000002EAA"
              },
              "productId": "01txx0000006i2rAAA",
              "id": "0iOxx000000000QEAQ"
            }
          ],
          "productRelatedComponent": {
            "unitOfMeasure": null,
            "sequence": null,
            "quoteVisibility": null,
            "quantityScaleMethod": null,
            "quantity": null,
            "productRelationshipTypeId": null,
            "productComponentGroupId": null,
            "productClassificationId": null,
            "parentSellingModelId": null,
            "parentProductId": null,
            "minQuantity": null,
            "maxQuantity": null,
            "isQuantityEditable": null,
            "isExcluded": null,
            "isDefaultComponent": null,
            "isComponentRequired": null,
            "id": null,
            "doesBundlePriceIncludeChild": null,
            "childSellingModelId": null,
            "childProductId": null
          },
          "productQuantity": {
            "quantity": null,
            "minQuantity": null,
            "maxQuantity": null
          },
          "productPricingInformation": null,
          "productInformation": null,
          "productComponentGroups": [],
          "productCode": "ACERT001",
          "productClassification": {
            "id": null
          },
          "prices": [
            {
              "pricingModel": {
                "unitOfMeasure": null,
                "pricingModelType": "TermDefined",
                "occurrence": 1,
                "name": "Term Based - Yearly",
                "id": "0jPxx0000000002EAA",
                "frequency": "Annual"
              },
              "priceBookId": "01sxx0000005ptpAAA",
              "priceBookEntryId": "01uxx0000008yXdAAI",
              "price": 2000,
              "isSelected": true,
              "isDerived": false,
              "isDefault": true,
              "effectiveTo": null,
              "effectiveFrom": null,
              "currencyIsoCode": "USD"
            }
          ],
          "nodeType": "simpleProduct",
          "name": "Admin Certification",
          "isSoldOnlyWithOtherProds": false,
          "isQuantityEditable": null,
          "isDefaultComponent": null,
          "isComponentRequired": null,
          "isAssetizable": true,
          "isActive": true,
          "id": "01txx0000006i2rAAA",
          "endOfLifeDate": null,
          "displayUrl": null,
          "discontinuedDate": null,
          "description": null,
          "configureDuringSale": "Allowed",
          "childProducts": [],
          "catalogs": [],
          "availabilityDate": null,
          "attributes": [],
          "attributeCategories": [],
          "additionalFields": []
        }
      ]
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_get_product_details.htm ===
---
page_id: actions_obj_get_product_details.htm
title: Get Product Details Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_product_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Product Details Action

Get details such as attributes, hierarchy, and cardinality for the
			specified product.

		
			

This action is available in API version 62.0 and later.

			

You can invoke this action via Apex and Flows only.

		

		

## Special Access Rules

			
			

The Get Product Details action is available in Enterprise, Unlimited, and Developer Editions
				where Product Discovery is enabled.

		

		
		

## Inputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** An array of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain the additional nodes that are used along with the context definition nodes for data hydration. The maximum number of supported nodes is 10. |
| additionalFields | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.AdditionalFields`](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains an array of additional standard or custom fields to include in the response. The supported objects are: `Product2` `ProductAttributeDefinition`—If the fields defined for the `ProductAttributeDefinition` object aren’t available for the `ProductClassificationAttr` object, then the API request fails. |
| catalogId | **Type** string **Description** Catalog ID that’s used to find and retrieve the products. |
| contextDefinition | **Type** string **Description** API name of the context definition for context creation. If you don’t provide a value, the context selected on the Product Discovery Settings page from Setup is used. |
| contextMapping | **Type** string **Description** API name of the context mapping for data hydration. The value of this parameter is used only if it belongs to the specified context definition. |
| correlationId | **Type** string **Description** Currency code that’s used to calculate and show prices. Only the products with the currency code matching the specified currency code are fetched. |
| currencyCode | **Type** string **Description** Currency code that’s used to calculate and show prices. |
| enablePricing | **Type** boolean **Description** Indicates whether the pricing procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Pricing Procedure setting from Setup. |
| enableQualification | **Type** boolean **Description** Indicates whether the qualification procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Qualification Procedure setting from Setup. |
| priceBookId | **Type** string **Description** ID of the pricebook from which you want to retrieve the pricing details. |
| pricingProcedure | **Type** string **Description** API name of the pricing procedure to calculate product prices. If you don’t specify a value, the pricing procedure selected on the Product Discovery Settings page from Setup is used. |
| productId | **Type** string **Description** Required. ID of the product to get the details for. |
| productSellingModelId | **Type** string **Description** ID of the product selling model. |
| qualificationProcedure | **Type** string **Description** API name of the qualification procedure to evaluate product eligibility. If you don’t specify a value, the qualification procedure selected on the Product Discovery Settings page from Setup is used. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextInputRepresentation` record that contains the user details to evaluate product eligibility and calculate prices. |

		

		

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

						

					

				
| Output | Details |
| --- | --- |
| apiStatus | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains a status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created by using the specified context definition. |
| correlationId | **Type** string **Description** ID to reference a series of related actions. |
| results | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ProductDetailsRepresentation`](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md) record that contains the product details. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextRepresentation` record that contains the user details. |

		

		

## Example

			
			
				
					
					
				
			

		

		

## Usage of an Apex-Defined Data Type in a Flow

			
			

To use an Apex-defined input parameter in a flow, follow these guidelines.

			
				
					

**Create an Apex Class**

					
: Create an Apex class defining the input and output parameters. In the flow,
						include the Apex-defined input parameters for which you want to add the
						details. In this example, we have created a class named ProductServiceAction
						that takes an object’s API name and record ID as input, and returns the
						additional context
						data.

```
public class ProductServiceAction {
    // Define input parameters
    public class FlowInput{
        @InvocableVariable(required=false)
        public String objectApiName;
        
        @InvocableVariable(required=false)
        public String recordId;
    }
    
    // Define output parameters
    public class FlowOutput{
        @invocableVariable
        public runtime_industries_cpq.AdditionalContextData additionalContextDataFinalOutput = new runtime_industries_cpq.AdditionalContextData();
        
    }
    
    // This method is invoked from a Flow
    @InvocableMethod(label='Process Input' description='Creates the Array of ContextDataInput for additional Context Data')
    public static List<FlowOutput> processContextData(List<FlowInput> inputs){
        String apiName;
        String recId;
        FlowOutput output = new FlowOutput();
        
    // Capture input from the flow
        for(FlowInput input: inputs){
            apiName = input.objectApiName;
            recId = input.recordId;
            }
    // Populate the ContextDataInput list to store additional context data    
        List<runtime_industries_cpq.ContextDataInput> listContextData = new List<runtime_industries_cpq.ContextDataInput>();
        runtime_industries_cpq.ContextDataInput cd1 = new runtime_industries_cpq.ContextDataInput();
        cd1.nodeName = apiName;
        cd1.nodeData = new Map<String, Object>();
        cd1.nodeData.put('id',recId);
        listContextData.add(cd1);
       
        output.additionalContextDataFinalOutput.additionalContextData = listContextData;
        List<FlowOutput> flowOutputs = new List<FlowOutput>();
        flowOutputs.add(output);
        
        List<runtime_industries_cpq.RelatedObjectFilter> relatedObjectFilterList = new List<runtime_industries_cpq.RelatedObjectFilter>();
       
        runtime_industries_cpq.RelatedObjectFilter relatedObjectFilter = new runtime_industries_cpq.RelatedObjectFilter();

        relatedObjectFilter.objectName = 'ProductSpecificationRecType';
        List<runtime_industries_cpq.FilterCriteriaInputRepresentation> criteriaList = new  List<runtime_industries_cpq.FilterCriteriaInputRepresentation>();
        runtime_industries_cpq.FilterCriteriaInputRepresentation criteria = new runtime_industries_cpq.FilterCriteriaInputRepresentation();
        criteria.property = 'IsCommercial';
        criteria.operator = 'eq';
        criteria.value = 'true';
        criteriaList.add(criteria);
        relatedObjectFilter.criteria = criteriaList;

        relatedObjectFilterList.add(relatedObjectFilter);
        output.relatedObjectFilter.relatedObjectFilter  = relatedObjectFilterList;
         
		output.userContext.accountId = '001DU000001nx9BYAQ';
        
        return flowOutputs;
       
    }

}
```

				
				
					

**Create a Flow with the Necessary Variables and Components**

					
: Create a flow that enables users to add a search term to find products. Add
						the ProductService action that you’ve created above by using Apex. When a
						flow is invoked from a record, the flow sends the record's objectApiName and
						recordId to the Apex class, which then generates the flow output. The flow
						passes the objectApiName and recordId of the record that the flow is invoked
						from to the Apex class to generate the flow output. See [Example of How to
							Create a Flow for Product Discovery](https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm&type=5&language=en_US).

				
				
					

**Configure the action**

					
: Configure the action (for example, Get Product Details action) to add values
						for the Apex-defined input parameters. Use the output of the created Apex
						class as the input of the Apex-defined parameter in the Get Product Details
						action, which users can use to get the product details.

=== ARTICLE: actions_obj_get_products.htm ===
---
page_id: actions_obj_get_products.htm
title: Get Products Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_products.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Products Action

Get products from the specified catalog, category, or subcategory,
			including product qualification and pricing details.

		

If a catalog, category, or subcategory isn’t specified, then this action retrieves all
				the products from all catalogs. This action is available in API version 62.0 and
				later.

      

You can invoke this action via Apex and Flows only.

		

## Special Access Rules

			
			

The Get Products action is available in Enterprise, Unlimited, and Developer Editions where
				Product Discovery is enabled.

		

		
		

## Inputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

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

						

					

				
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** An array of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain the additional nodes that are used along with the context definition nodes for data hydration. The maximum number of supported nodes is 10. |
| additionalFields | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.AdditionalFields`](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains an array of additional standard or custom fields to include in the response. The supported objects are: `Product2` `ProductAttributeDefinition`—If the fields defined for the `ProductAttributeDefinition` object aren’t available for the `ProductClassificationAttr` object, then the API request fails. |
| catalogId | **Type** string **Description** Catalog ID that’s used to find and retrieve the products. |
| categoryId | **Type** string **Description** ID of the category or subcategory to get the products for. |
| contextDefinition | **Type** string **Description** API name of the context definition that’s used for context creation. If you don’t specify a value, the context selected on the Product Discovery Settings page from Setup is used. |
| contextMapping | **Type** string **Description** API name of the context mapping that’s used for data hydration. The value of this parameter is used only if it belongs to the specified context definition. |
| correlationId | **Type** string **Description** Unique ID that’s used to reference a series of related actions. |
| currencyCode | **Type** string **Description** Currency code that’s used to calculate and show prices. Only the products with the currency code matching the specified currency code are fetched. |
| cursor | **Type** string **Description** Unique identifier that represents the position of the product from which the next set of results are retrieved. |
| enablePricing | **Type** boolean **Description** Indicates whether the pricing procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Pricing Procedure setting from Setup. |
| enableQualification | **Type** boolean **Description** Indicates whether the qualification procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, you must enable the Qualification Procedure setting from Setup. |
| executeConfigurationRules | **Type** boolean **Description** Indicates whether configuration rules must run (`true`) or not (`false`). Available in API version 67.0 and later. |
| filter | **Type** Apex-defined **Description** A collection of Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) records where each record contains a related object and the filter criteria that’s applied on the object. The filter parameter supports only the `name` property. The supported operators are: `eq` `in` `contains` If this parameter contains multiple criteria, all the criteria are applied. |
| includeCatalogDetails | **Type** boolean **Description** Indicates whether catalog details must be included in the response (`true`) or not (`false`). |
| limit | **Type** integer **Description** Maximum number of results to be returned in the response. Specify a value from 1 through 100. The default value is 10. |
| orderBy | **Type** string **Description** Comma-separated string of key-value pairs that specify how the results are sorted. Each string must contain a field name and its sort order. For example, `["name:asc",”custom_field:asc”]`. |
| priceBookId | **Type** string **Description** ID of the pricebook that the pricing details are retrieved from. |
| pricingProcedure | **Type** string **Description** API name of the pricing procedure to calculate product prices. If you don’t specify a value, the pricing procedure selected on the Product Discovery Settings page from Setup is used. |
| productClassificationId | **Type** string **Description** ID of the product classification that’s used to filter the products. |
| qualificationProcedure | **Type** string **Description** API name of the qualification procedure to evaluate product eligibility. If you don’t specify a value, the qualification procedure selected on the Product Discovery Settings page from Setup is used. |
| transactionContextId | **Type** string **Description** Context ID of the quote or order. Available in API version 67.0 and later. |
| transactionId | **Type** string **Description** ID of the quote or order. Available in API version 67.0 and later. |
| relatedObjectFilters | **Type** Apex-defined **Description** A collection of Apex [`runtime_industries_cpq.RelatedObjectFilterInputRepresentation`](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md) records, where each record contains a related object and the filter criteria that’s applied on the object. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextInputRepresentation` record that contains the user details to evaluate product eligibility and calculate prices. |

		

		

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
| apiStatus | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains a status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created by using the specified context definition. |
| correlationId | **Type** string **Description** ID to reference a series of related actions. |
| cursor | **Type** string **Description** Unique identifier that represents the position of the product from which the next set of results are retrieved. |
| results | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ProductListRepresentation`](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md) record that contains the retrieved products. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextRepresentation` record that includes the user details. |

		

		

## Example

			
			
				
					
					
					
: 
						

Here's a sample input to call this invocable action from Apex code.

						

```
Invocable.Action action = Invocable.Action.createStandardAction('getProducts');
action.setInvocationParameter('executeConfigurationRules', true);
action.setInvocationParameter('catalogId', '0ZSVW000000AhdB4AS');
action.setInvocationParameter('transactionId', '0Q0VW0000018J6X0AU');
List<String> orderBy = new List<String>();
orderBy.add('name:asc');
action.setInvocationParameter('orderBy', orderBy);
List<Invocable.Action.Result> results = action.invoke();

for (Invocable.Action.Result res : results) {
    if (res.isSuccess()) {
        Map<String, Object> outMap = res.getOutputParameters();
        String jsonOutput = JSON.serialize(outMap);	
        System.debug(jsonOutput);
    }
}
```

					

					
: 
						

Here’s a sample response for this action.

						

```
{
  "facets": [],
  "apiStatus": {
    "statusMessage": null,
    "statusCode": "FetchedDetailsSuccessfully",
    "messages": []
  },
  "results": [
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w22AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w12AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w32AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API",
      "productClassification": {
        "id": "11BVW000004ljiZ2AQ"
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfGYAQ",
          "price": 15000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg8YAA",
          "price": 2000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg9YAA",
          "price": 1500,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7txYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_api",
      "discontinuedDate": null,
      "description": null,
      "configureDuringSale": "Allowed",
      "configurationRules": [
        {
          "type": "disable",
          "details": [
            {
              "message": "This is disabled"
            }
          ]
        }
      ],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tyYAA",
          "id": "0iOVW00000049w42AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-FLEX",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfFYAQ",
          "price": 450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Flex (100M)",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tyYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_flex",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tzYAA",
          "id": "0iOVW00000049w52AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-GOVT",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfHYAQ",
          "price": 1450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Gov",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tzYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_govt",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u0YAA",
          "id": "0iOVW00000049w92AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PREP",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfSYAQ",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Pre-Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u0YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_preprod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u1YAA",
          "id": "0iOVW00000049wA2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PROD",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfdYAA",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u1YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_prod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u3YAA",
          "id": "0iOVW00000049wF2AQ"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7u3YAA",
          "id": "0iOVW00000049wE2AQ"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7u3YAA",
          "id": "0iOVW00000049wG2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-AUT-CRED",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfUYAQ",
          "price": 25,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzgAYAQ",
          "price": 2.5,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzgBYAQ",
          "price": 2,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional Automation QB Credits",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u3YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_auto_credit",
      "discontinuedDate": null,
      "description": "Your QuantumBit Automation subscription plan includes a quota of Automation QB Credits that you can use with QB RPA, QB Orchestrator, or a combination of both products. As you use processes to create automations, your total credit quota is depleted. 1 QB Automation Credit = 2 RPA Bot Minutes, 1 QB Automation Credit = 100 RPA API Calls, 1 QB Automation Credit = 50 Orchestrator Tasks",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7uPYAQ",
          "id": "0iOVW00000049wR2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-DAT-GRPH",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzffYAA",
          "price": 25000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional QB DataGraph (500M)",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7uPYAQ",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_data_graph",
      "discontinuedDate": null,
      "description": "With QuantumBit DataGraph, you can reuse multiple APIs in a single request. Enterprise architects can easily unify APIs into one data service — all without writing more code. Developers can consume multiple APIs from the data service in a single GraphQL request.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u2YAA",
          "id": "0iOVW00000049wC2AQ"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7u2YAA",
          "id": "0iOVW00000049wB2AQ"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7u2YAA",
          "id": "0iOVW00000049wD2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-REQT",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfOYAQ",
          "price": 45,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzgJYAQ",
          "price": 5,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzgKYAQ",
          "price": 5,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "API Access Requests (AEH)",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u2YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_access",
      "discontinuedDate": null,
      "description": "QuantumBit API Experience Hub enables you to create vibrant ecosystems and grow engagement for your API products",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7uhYAA",
          "id": "0iOVW00000049x22AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-SUPP-1005",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfRYAQ",
          "price": 30000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Gold Hardware Maintenance",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7uhYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/gold_maint",
      "discontinuedDate": null,
      "description": "System maintenance, administration, and configuration performed by a certified technician. Also includes 24x7 phone service and monthly on-site check-ups. 20% of hardware.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "Maintenance",
          "isNavigational": null,
          "id": "0ZGVW000000IUEJ4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": "Base",
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003olLNYAY",
          "id": "0iOVW0000005X1l2AE"
        },
        {
          "productSellingModelId": "0jPVW0000001fh42AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "OneTime",
            "pricingTermUnit": null,
            "pricingTerm": null,
            "name": "One-Time",
            "id": "0jPVW0000001fh42AA"
          },
          "productId": "01tVW000003olLNYAY",
          "id": "0iOVW0000005X092AE"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "LaptopDell",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000lsJfYAI",
          "price": 600,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "OneTime",
            "occurrence": null,
            "name": "One-Time",
            "id": "0jPVW0000001fh42AA",
            "frequency": null
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000lsPxYAI",
          "price": 100,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "variationParentProduct",
      "name": "Laptop Dell",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003olLNYAY",
      "endOfLifeDate": null,
      "displayUrl": null,
      "discontinuedDate": null,
      "description": null,
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "Variants",
          "isNavigational": null,
          "id": "0ZGVW000000ItXV4A0",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    }
  ],
  "contextId": "0000000r25tp21g0025177753245202837fde5e54eed45178ef77c9e453083fd",
  "correlationId": "ee883b85-2c99-48fb-88e6-95cb35e8751e",
  "cursor": "MTAwMDAwMDAxMw=="
}
```

					

				
			

		

		

## Usage of an Apex-Defined Data Type in a Flow

			
			

To use an Apex-defined input parameter in a Flow, follow these guidelines.

			
				
					

**Create an Apex class**

					
: Create an Apex class defining the input and output parameters. In the flow,
						include the Apex-defined input parameters for which you want to add the
						details. In this example, we have created a class named ProductServiceAction
						that takes an object’s API name and record ID as input, and returns the
						additional context
						data.

```
public class ProductServiceAction {
    // Define input parameters
    public class FlowInput{
        @InvocableVariable(required=false)
        public String objectApiName;
        
        @InvocableVariable(required=false)
        public String recordId;
    }
    
    // Define output parameters
    public class FlowOutput{
        @invocableVariable
        public runtime_industries_cpq.AdditionalContextData additionalContextDataFinalOutput = new runtime_industries_cpq.AdditionalContextData();
        
        @invocableVariable
        public runtime_industries_cpq.RelatedObjectFilterInputRepresentation relatedObjectFilter = new runtime_industries_cpq.RelatedObjectFilterInputRepresentation();
        
        @invocableVariable
        public ConnectApi.UserContextInputRepresentation userContext = new ConnectApi.UserContextInputRepresentation();
        
        }
    
    // This method is invoked from a Flow
    @InvocableMethod(label='Process Input' description='Creates the Array of ContextDataInput for additional Context Data')
    public static List<FlowOutput> processContextData(List<FlowInput> inputs){
        String apiName;
        String recId;
        FlowOutput output = new FlowOutput();
        
    // Capture input from the flow
        for(FlowInput input: inputs){
            apiName = input.objectApiName;
            recId = input.recordId;
            }
    // Populate the ContextDataInput list to store additional context data    
        List<runtime_industries_cpq.ContextDataInput> listContextData = new List<runtime_industries_cpq.ContextDataInput>();
        runtime_industries_cpq.ContextDataInput cd1 = new runtime_industries_cpq.ContextDataInput();
        cd1.nodeName = apiName;
        cd1.nodeData = new Map<String, Object>();
        cd1.nodeData.put('id',recId);
        listContextData.add(cd1);
       
        output.additionalContextDataFinalOutput.additionalContextData = listContextData;
        List<FlowOutput> flowOutputs = new List<FlowOutput>();
        flowOutputs.add(output);
        
        List<runtime_industries_cpq.RelatedObjectFilter> relatedObjectFilterList = new List<runtime_industries_cpq.RelatedObjectFilter>();
       
        runtime_industries_cpq.RelatedObjectFilter relatedObjectFilter = new runtime_industries_cpq.RelatedObjectFilter();

        relatedObjectFilter.objectName = 'ProductSpecificationRecType';
        List<runtime_industries_cpq.FilterCriteriaInputRepresentation> criteriaList = new  List<runtime_industries_cpq.FilterCriteriaInputRepresentation>();
        runtime_industries_cpq.FilterCriteriaInputRepresentation criteria = new runtime_industries_cpq.FilterCriteriaInputRepresentation();
        criteria.property = 'IsCommercial';
        criteria.operator = 'eq';
        criteria.value = 'true';
        criteriaList.add(criteria);
        relatedObjectFilter.criteria = criteriaList;

       relatedObjectFilterList.add(relatedObjectFilter);

        output.relatedObjectFilter.relatedObjectFilter  = relatedObjectFilterList;
         
		output.userContext.accountId = '001Hs00003r17HNIAY';
        
        return flowOutputs;
        
    }

}
```

				
				
					

**Create a Flow with the necessary variables and components**

					
: Create a flow that enables users to add a search term to find products. Add
						the ProductService action that you’ve created above by using Apex. When a
						flow is invoked from a record, the flow sends the record's objectApiName and
						recordId to the Apex class, which then generates the flow output. The flow
						passes the objectApiName and recordId of the record that the flow is invoked
						from to the Apex class to generate the flow output. See [Example of How to
							Create a Flow for Product Discovery](https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm&type=5&language=en_US).

				
				
					

**Configure the action**

					
: Configure the action (for example, Get Products action) to add values for
						the Apex-defined input parameters. Use the output of the created Apex class
						as the input of the Apex-defined parameter in the Get Products action, which
						users can use to get products.

=== ARTICLE: actions_obj_get_recommendation_products.htm ===
---
page_id: actions_obj_get_recommendation_products.htm
title: Get Product Recommendations Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_recommendation_products.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Product Recommendations Action

Retrieve a list of recommended products for a quote or order by using
			the Constraint Rule Engine.

		
			

This action is available in API version 67.0 and later.

		

		

## Special Access Rules

			

The Get Product Details action is available in Enterprise, Unlimited, and
				Developer Editions where Product Discovery is enabled.

			

You can invoke this action via Apex and Flows only.

		
		

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

						

					

				
| Input | Details |
| --- | --- |
| additionalContextData | **Type** Apex-defined **Description** An array of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain the additional nodes used along with the context definition nodes for data hydration. The maximum number of supported nodes is 10. |
| additionalFields | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.AdditionalFields`](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains an array of additional standard or custom fields from the `Product2` object to include in the response. |
| catalogId | **Type** string **Description** ID of the catalog from which to retrieve recommended products. |
| contextDefinition | **Type** string **Description** API name of the context definition used for context creation. If you don't specify a value, the context definition selected on the Product Discovery Settings page from Setup is used. |
| contextMapping | **Type** string **Description** API name of the context mapping used for data hydration. The value of this parameter is used only if it belongs to the specified context definition. If you don't specify a value, the default context mapping of the context definition is used. |
| currencyCode | **Type** string **Description** Currency code used for pricing calculations and product filtering. |
| enablePricing | **Type** boolean **Description** Indicates whether the pricing procedure must run (`true`) or not (`false`). For orgs where pricing is enabled, you can override to `false` to skip Salesforce Pricing execution. For orgs where pricing is disabled, you can't override to `true`. |
| enableQualification | **Type** boolean **Description** Indicates whether the qualification procedure must run (`true`) or not (`false`). For orgs where qualification is enabled, you can override to `false` to skip BRE qualification rules. For orgs where qualification is disabled, you can't override to `true`. |
| filterCriteria | **Type** Apex-defined **Description** A collection of Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) records used to filter products. The filterCriteria parameter supports only the `name` property. The supported operators are: `eq` `in` `contains` If this parameter contains multiple criteria, all criteria are applied using the `and` operator. |
| nextCursor | **Type** string **Description** A unique identifier that represents the position of the product from which the next set of results are retrieved. |
| pageSize | **Type** integer **Description** Maximum number of recommended products to return in the response. |
| priceBookId | **Type** string **Description** ID of the pricebook from which to retrieve pricing details. |
| pricingProcedure | **Type** string **Description** API name of the pricing procedure used to calculate product prices. If you don't specify a value, the pricing procedure selected on the Product Discovery Settings page from Setup is used. |
| qualificationProcedure | **Type** string **Description** API name of the qualification procedure used to evaluate product eligibility. If you don't specify a value, the qualification procedure selected on the Product Discovery Settings page from Setup is used. |
| transactionContextId | **Type** string **Description** Context ID of the transaction. |
| transactionId | **Type** string **Description** ID of the transaction. |
| usePromotions | **Type** boolean **Description** Indicates whether to fetch promotions for recommended products (`true`) or not (`false`). Applies only when promotions are enabled for the org. |
| userContext | **Type** Apex-defined **Description** An Apex `ConnectApi.UserContextInputRepresentation` record that contains the user details used to evaluate product eligibility and calculate prices. |

		

		

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

						

					

				
| Output | Details |
| --- | --- |
| errorMessages | **Type** Apex-defined **Description** A list of Apex `runtime_industries_cpq.ProductRecommendationErrorsOutputRepresentation` records that contain error codes and messages returned by the action. |
| isSuccessful | **Type** boolean **Description** Indicates whether the action call succeeded (`true`) or not (`false`). |
| nextCursor | **Type** string **Description** Unique identifier that represents the position of the next product in the dataset. Use this value as an input to retrieve the next page of results. |
| recommendedProducts | **Type** Apex-defined **Description** A list of Apex `runtime_industries_cpq.RecommendedProductsOutputRepresentation` records that contain the recommended products returned by the Constraint Rule Engine. |
| transactionContextId | **Type** string **Description** Context ID of the transaction. |

		

		

## Example

			
			
				
					
: Here's a sample input to call this invocable action from Apex
						code.

```
Invocable.Action action = Invocable.Action.createStandardAction('getRecommendedProducts');
action.setInvocationParameter('catalogId', '0ZSVW000000AhdB4AS');
action.setInvocationParameter('transactionId', '0Q0VW0000018J6X0AU');
List<Invocable.Action.Result> results = action.invoke();

for (Invocable.Action.Result res : results) {
    if (res.isSuccess()) {
        Map<String, Object> outMap = res.getOutputParameters();
        String jsonOutput = JSON.serialize(outMap);	
        System.debug(jsonOutput);
    }
}

```

					
: 
						

Here’s a sample response for the Get Product Recommendations action.

						

```
{
  "prodRecomErrorOutRepresentation": [],
  "isSuccessful": true,
  "productCursor": "MTAwMDAwMDAwNg==",
  "transactionContextId": "0000000r25tq18g00291777531846434b162e02f878f425680e0d95dc5f650fe",
  "recomProdOutputRepresentations": [
    {
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w22AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w12AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w32AA"
        }
      ],
      "productQuantity": null,
      "productCode": "QB-API",
      "productClassification": {
        "id": "11BVW000004ljiZ2AQ"
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfGYAQ",
          "price": 15000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg8YAA",
          "price": 2000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg9YAA",
          "price": 1500,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7txYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_api",
      "discontinuedDate": null,
      "description": null,
      "configureDuringSale": "Allowed",
      "configurationRules": [
        {
          "type": "recommend",
          "details": [
            {
              "message": "APIAccessRequests recommends AdditionalAPI"
            }
          ]
        },
        {
          "type": "disable",
          "details": [
            {
              "message": "This is disabled"
            }
          ]
        }
      ],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [
        {
          "status": null,
          "numberOfCategories": 8,
          "name": "QuantumBit Software",
          "id": "0ZSVW000000AhdB4AS",
          "effectiveStartDate": null,
          "effectiveEndDate": null,
          "description": null,
          "customFields": [],
          "catalogType": null,
          "catalogCode": null
        }
      ],
      "availabilityDate": null,
      "additionalFields": []
    }
  ]
}
```

=== ARTICLE: actions_obj_search_products_with_guided_selection.htm ===
---
page_id: actions_obj_search_products_with_guided_selection.htm
title: Search Product with Guided Selection Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_search_products_with_guided_selection.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Search Product with Guided Selection Action

Use guided product selection to search for
        products.

        

This action is available in API version 64.0 and later.

            

You can invoke this action via Apex and Flows only.

        

## Special Access Rules

            
            

The Search Product with Guided Selection action is available in Enterprise,
                Unlimited, and Developer Editions where Product Discovery is enabled.

        

        
        

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

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
| additionalContextData | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.AdditionalContextData`](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md) records that contain the nodes used in addition to context definition nodes for data hydration. This parameter can contain up to 10 nodes. |
| additionalFields | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.AdditionalFields`](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md) record that contains the collection of additional fields to be included in the response. This parameter supports only the fields from the Product2 and ProductAttributeDefinition objects. The fields defined for the ProductAttributeDefinition object must also be available on the ProductClassificationAttr object. |
| catalogId | **Type** string **Description** ID of the catalog to find and retrieve products. |
| categoryId | **Type** string **Description** ID of the category or subcategory to find and retrieve products. |
| contextDefinition | **Type** string **Description** API name of the context definition that's used for context creation. If you don’t specify a value, the context selected on the **Product Discovery Settings** page is used. |
| contextMapping | **Type** string **Description** API name of the context mapping that's used for data hydration. The value of this parameter is used only if it belongs to the specified context definition. |
| correlationId | **Type** string **Description** Unique ID that’s used to reference a series of related actions. |
| currencyCode | **Type** string **Description** Currency code that’s used to calculate and show prices. Only the products with the currency code matching the entered currency code are fetched. |
| executeConfigurationRules | **Type** boolean **Description** Indicates whether configuration rules must run (`true`) or not (`false`). Available in API version 67.0 and later. |
| enablePricing | **Type** boolean **Description** Indicates whether pricing procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, the **Pricing Procedure** setting must be enabled. |
| enableQualification | **Type** boolean **Description** Indicates whether qualification procedure must run (`true`) or not (`false`). The default value is `true`. To use this parameter, the** Qualification Procedure** setting must be enabled. |
| filterInputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.FilterInputRepresentation`](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md) record that contains the filter criteria. This parameter supports only the `name` property and the `eq`, `in`, or `contains` operators. If it contains multiple criteria, all the criteria are applied. |
| guidedSelectionResponseId | **Type** string **Description** Response identifier that stores user responses specified in the guided product selection window. |
| includeCatalogDetails | **Type** boolean **Description** Indicates whether catalog details must be included in the response (`true`) or not (`false`). |
| orderBy | **Type** string **Description** Comma-delimited string of key-value pairs that specify how results are sorted. Each string must contain a field name and its sort order. For example, ["name:asc",”custom_field:asc”]. |
| priceBookId | **Type** string **Description** ID of the pricebook that the pricing information is retrieved from. |
| pricingProcedure | **Type** string **Description** API name of the pricing procedure to calculate product prices. If you don’t specify a value, the pricing procedure selected on the **Product Discovery Settings** page is used. |
| productClassificationId | **Type** string **Description** ID of the product classification that's used to filter products. |
| productCursor | **Type** string **Description** Unique identifier that represents the position of the product from which the next set of results are retrieved. |
| qualificationProcedure | **Type** string **Description** API name of the qualification procedure to evaluate product eligibility. If you don’t specify a value, the qualification procedure selected on the **Product Discovery Settings** page is used. |
| recordLimit | **Type** integer **Description** Maximum number of results to be returned in the response. Specify a value from 1 through 100. Default value is 10. |
| relatedObjectFilters | **Type** Apex-defined **Description** Collection of Apex [`runtime_industries_cpq.RelatedObjectFilterInputRepresentation`](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md) records, each containing a related object and the filter criteria that’s applied on the object. |
| searchTerms | **Type** Apex-defined **Description** Collection of terms that are used to search products. See [GuidedSelectionSearchTerm](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md). |
| transactionContextId | **Type** string **Description** Context ID of the quote or order. Available in API version 67.0 and later. |
| transactionId | **Type** string **Description** ID of the quote or order. Available in API version 67.0 and later. |
| userContext | **Type** Apex-defined **Description** An Apex ConnectApi.UserContextInputRepresentation record containing user information to evaluate product eligibility and calculate pricing. |

        

        

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| apiStatusOutputRepresentation | **Type** Apex-defined **Description** An Apex [`runtime_industries_cpq.ApiStatusRepresentation`](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md) record that contains the status of the request, including the status code and message. |
| contextId | **Type** string **Description** ID of the context that’s created by using the specified context definition. |
| correlationId | **Type** string **Description** Unique identifier attached to requests and messages, allowing reference to a specific transaction or event chain. |
| productCursor | **Type** string **Description** Unique identifier that represents the position of the product from which the next set of results are retrieved. |
| productListOutputRepresentations | **Type** Apex-defined **Description** Collection of Apex [ProductListOutputRepresentation](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md) records that contain details about the product shown by the Guided Product Selection. |
| recordOffset | **Type** integer **Description** Number of catalog records to skip in the request. The default is 0. |
| searchTerms | **Type** Apex-defined **Description** Collection of terms that are used to search products. See [GuidedSelectionSearchTerm](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md). |
| userContext | **Type** Apex-defined **Description** An Apex ConnectApi.UserContextRepresentation record containing user information. |

        

        
        

## Example

            
            
                
                    
                    
: 
                        

Here's a sample input to call this invocable action from Apex code.

                        

```
Invocable.Action action = Invocable.Action.createStandardAction('searchPrdctWithGuidedSelection');

action.setInvocationParameter('correlationId', '77f9dc6a-8ecc-44a3-8d89-4050179cc846');
//action.setInvocationParameter('catalogId', '0ZSxx000000004sGAA');
action.setInvocationParameter('guidedSelectionResponseId', '0U3xx0000004CPACA2');
//action.setInvocationParameter('priceBookId', '01sxx0000005pyfAAA');
//action.setInvocationParameter('categoryId', '0ZGxx000000004rGAA');
action.setInvocationParameter('enableQualification', true);
action.setInvocationParameter('enablePricing', true);
//action.setInvocationParameter('contextDefinition', 'PDACDCtx');
//action.setInvocationParameter('contextMapping', 'ProductDiscoveryMapping');
//action.setInvocationParameter('qualificationProcedure', 'PDQualProceWithQuote');
//action.setInvocationParameter('pricingProcedure', 'IconpricingProcedure');
action.setInvocationParameter('includeCatalogDetails', true);
action.setInvocationParameter('currencyCode', 'USD');
action.setInvocationParameter('executeConfigurationRules', true);
List<String> orderByInputs = new List<String>();
orderByInputs.add('name:asc');
orderByInputs.add('id:desc');
action.setInvocationParameter('orderBy', orderByInputs);
List<runtime_industries_cpq.GuidedSelectionSearchTerm> searchTerms = new List<runtime_industries_cpq.GuidedSelectionSearchTerm>();
runtime_industries_cpq.GuidedSelectionSearchTerm searchTerm = new runtime_industries_cpq.GuidedSelectionSearchTerm();
searchTerm.term = 'Laptop Basic Bundle';
List<String> tags = new List<String>();
tags.add('Laptop');
tags.add('Desktop');
searchTerm.tags = tags;
searchTerms.add(searchTerm);

runtime_industries_cpq.GuidedSelectionSearchTermList searchTermList = new runtime_industries_cpq.GuidedSelectionSearchTermList();
searchTermList.searchTerms = searchTerms;
action.setInvocationParameter('searchTerms', searchTermList);
List<Invocable.Action.Result> results = action.invoke();
System.debug('Guided Selection result = ' + results);
```

                    

                    
: 
                        

Here's a sample response when you call this action.

                        

```
{
  "recordOffset": 5,
  "contextId": null,
  "correlationId": "854c487d-183e-40b6-ba42-f079a6e695a3",
  "apiStatusOutputRepresentation": {
    "statusMessage": null,
    "statusCode": "FetchedDetailsSuccessfully",
    "messages": []
  },
  "searchTerms": [
    {
      "term": "Additional API",
      "tags": []
    }
  ],
  "productListOutputRepresentations": [
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w22AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh52AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "Evergreen",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w12AA"
        },
        {
          "productSellingModelId": "0jPVW0000001fh62AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Months",
            "pricingTerm": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA"
          },
          "productId": "01tVW000003l7txYAA",
          "id": "0iOVW00000049w32AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API",
      "productClassification": {
        "id": "11BVW000004ljiZ2AQ"
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfGYAQ",
          "price": 15000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "Evergreen",
            "occurrence": 1,
            "name": "Evergreen Monthly",
            "id": "0jPVW0000001fh52AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg8YAA",
          "price": 2000,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        },
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Monthly",
            "id": "0jPVW0000001fh62AA",
            "frequency": "Months"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzg9YAA",
          "price": 1500,
          "isSelected": false,
          "isDerived": false,
          "isDefault": false,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7txYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/add_api",
      "discontinuedDate": null,
      "description": null,
      "configureDuringSale": "Allowed",
      "configurationRules": [
        {
          "type": "disable",
          "details": [
            {
              "message": "This is disabled"
            }
          ]
        }
      ],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tyYAA",
          "id": "0iOVW00000049w42AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-FLEX",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfFYAQ",
          "price": 450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Flex (100M)",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tyYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_flex",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7tzYAA",
          "id": "0iOVW00000049w52AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-GOVT",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfHYAQ",
          "price": 1450,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Gov",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7tzYAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_govt",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u0YAA",
          "id": "0iOVW00000049w92AA"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PREP",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfSYAQ",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Pre-Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u0YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_preprod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    },
    {
      "unitOfMeasure": null,
      "status": null,
      "qualificationContext": {
        "reason": null,
        "isQualified": true
      },
      "productType": null,
      "productSpecificationType": null,
      "productSellingModelOptions": [
        {
          "productSellingModelId": "0jPVW0000001fh32AA",
          "productSellingModel": {
            "status": "Active",
            "sellingModelType": "TermDefined",
            "pricingTermUnit": "Annual",
            "pricingTerm": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA"
          },
          "productId": "01tVW000003l7u1YAA",
          "id": "0iOVW00000049wA2AQ"
        }
      ],
      "productRelatedComponent": null,
      "productQuantity": null,
      "productPricingInformation": null,
      "productInformation": null,
      "productComponentGroups": [],
      "productCode": "QB-API-PROD",
      "productClassification": {
        "id": null
      },
      "prices": [
        {
          "pricingModel": {
            "unitOfMeasure": null,
            "pricingModelType": "TermDefined",
            "occurrence": 1,
            "name": "Term Annual",
            "id": "0jPVW0000001fh32AA",
            "frequency": "Annual"
          },
          "priceBookId": "01sVW0000024PZlYAM",
          "priceBookEntryId": "01uVW000000jzfdYAA",
          "price": 3240,
          "isSelected": false,
          "isDerived": false,
          "isDefault": true,
          "effectiveTo": null,
          "effectiveFrom": null,
          "currencyIsoCode": "USD"
        }
      ],
      "nodeType": "simpleProduct",
      "name": "Additional API Prod",
      "isSoldOnlyWithOtherProds": false,
      "isQuantityEditable": null,
      "isDefaultComponent": null,
      "isComponentRequired": null,
      "isAssetizable": true,
      "isActive": true,
      "id": "01tVW000003l7u1YAA",
      "endOfLifeDate": null,
      "displayUrl": "/resource/api_prod",
      "discontinuedDate": null,
      "description": "API instances remain under management until they are deleted. Instances of API Manager are aggregated using a Max Concurrent model. The usage for a month is the highest number of APIs Managed in a single given hour during a month.",
      "configureDuringSale": null,
      "configurationRules": [],
      "childProducts": [],
      "categories": [
        {
          "sortOrder": null,
          "qualificationContext": {
            "reason": null,
            "isQualified": true
          },
          "parentCategoryId": null,
          "name": "API",
          "isNavigational": null,
          "id": "0ZGVW000000IUEG4A4",
          "hasSubCategories": null,
          "description": null,
          "childCategories": null,
          "catalogId": "0ZSVW000000AhdB4AS"
        }
      ],
      "catalogs": [],
      "availabilityDate": null,
      "attributeCategories": [],
      "additionalFields": []
    }
  ]
}
```

=== ARTICLE: apex_class_ricpq_ProductRelatedComponentOR.htm ===
---
page_id: apex_class_ricpq_ProductRelatedComponentOR.htm
title: ProductRelatedComponentOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_ricpq_ProductRelatedComponentOR.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductRelatedComponentOutputRepresentation Class

Represents a related component product in a bundle or product relationship, including component configuration details such as quantity constraints, required status, and relationship metadata.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductRelatedComponentOutputRepresentation Properties](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_properties)**  

## ProductRelatedComponentOutputRepresentation Properties

The following are properties for `ProductRelatedComponentOutputRepresentation`.

- 
**[childProductId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_childProductId)**  

Get or set the identifier of the child product in the relationship.

- 
**[childSellingModelId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_childSellingModelId)**  

Get or set the identifier of the child product's selling model in the relationship.

- 
**[doesBundlePriceIncludeChild](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_doesBundlePriceIncludeChild)**  

Get or set whether the bundle price includes the price of this child component.

- 
**[id](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_runtime_industries_cpq_ProductRelatedComponentOutputRepresentation_id)**  

Get or set the unique identifier of the product related component relationship.

- 
**[isComponentRequired](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_isComponentRequired)**  

Get or set whether this component is required in the bundle or product relationship.

- 
**[isDefaultComponent](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_isDefaultComponent)**  

Get or set whether this component is selected by default in the bundle or product relationship.

- 
**[isQuantityEditable](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_isQuantityEditable)**  

Get or set whether the quantity of this component can be edited.

- 
**[maxQuantity](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_maxQuantity)**  

Get or set the maximum quantity allowed for this component.

- 
**[minQuantity](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_minQuantity)**  

Get or set the minimum quantity required for this component.

- 
**[parentProductId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_parentProductId)**  

Get or set the identifier of the parent product in the relationship.

- 
**[parentSellingModelId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_parentSellingModelId)**  

Get or set the identifier of the parent product's selling model in the relationship.

- 
**[productClassificationId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_productClassificationId)**  

Get or set the identifier of the product classification for this component.

- 
**[productComponentGroupId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_productComponentGroupId)**  

Get or set the identifier of the product component group that this component belongs to.

- 
**[productRelationshipTypeId](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_productRelationshipTypeId)**  

Get or set the identifier of the product relationship type that defines this relationship.

- 
**[quantity](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_quantity)**  

Get or set the current quantity of this component.

- 
**[quantityScaleMethod](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_quantityScaleMethod)**  

Get or set the method used to scale the quantity of this component, such as "PerUnit" or "PerBundle".

- 
**[sequence](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_sequence)**  

Get or set the display sequence order of this component within the bundle or product relationship.

- 
**[unitOfMeasure](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_unitOfMeasure)**  

Get or set the unit of measure for the quantity of this component.

- 
**[isExcluded](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_isExcluded)**  

Indicates whether excluded is true or false.

- 
**[quoteVisibility](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_ricpq_ProductRelatedComponentOR_quoteVisibility)**  

Get the quotevisibility value.

### childProductId

Get or set the identifier of the child product in the relationship.

#### Signature

`public String childProductId {get; set;}`

#### Property Value

Type: String

### childSellingModelId

Get or set the identifier of the child product's selling model in the relationship.

#### Signature

`public String childSellingModelId {get; set;}`

#### Property Value

Type: String

### doesBundlePriceIncludeChild

Get or set whether the bundle price includes the price of this child component.

#### Signature

`public Boolean doesBundlePriceIncludeChild {get; set;}`

#### Property Value

Type: Boolean

### id

Get or set the unique identifier of the product related component relationship.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isComponentRequired

Get or set whether this component is required in the bundle or product relationship.

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Get or set whether this component is selected by default in the bundle or product relationship.

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Get or set whether the quantity of this component can be edited.

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### maxQuantity

Get or set the maximum quantity allowed for this component.

#### Signature

`public Double maxQuantity {get; set;}`

#### Property Value

Type: Double

### minQuantity

Get or set the minimum quantity required for this component.

#### Signature

`public Double minQuantity {get; set;}`

#### Property Value

Type: Double

### parentProductId

Get or set the identifier of the parent product in the relationship.

#### Signature

`public String parentProductId {get; set;}`

#### Property Value

Type: String

### parentSellingModelId

Get or set the identifier of the parent product's selling model in the relationship.

#### Signature

`public String parentSellingModelId {get; set;}`

#### Property Value

Type: String

### productClassificationId

Get or set the identifier of the product classification for this component.

#### Signature

`public String productClassificationId {get; set;}`

#### Property Value

Type: String

### productComponentGroupId

Get or set the identifier of the product component group that this component belongs to.

#### Signature

`public String productComponentGroupId {get; set;}`

#### Property Value

Type: String

### productRelationshipTypeId

Get or set the identifier of the product relationship type that defines this relationship.

#### Signature

`public String productRelationshipTypeId {get; set;}`

#### Property Value

Type: String

### quantity

Get or set the current quantity of this component.

#### Signature

`public Double quantity {get; set;}`

#### Property Value

Type: Double

### quantityScaleMethod

Get or set the method used to scale the quantity of this component, such as "PerUnit" or "PerBundle".

#### Signature

`public String quantityScaleMethod {get; set;}`

#### Property Value

Type: String

### sequence

Get or set the display sequence order of this component within the bundle or product relationship.

#### Signature

`public Integer sequence {get; set;}`

#### Property Value

Type: Integer

### unitOfMeasure

Get or set the unit of measure for the quantity of this component.

#### Signature

`public ConnectApi.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: ConnectApi.UnitOfMeasureOutputRepresentation

### isExcluded

Indicates whether excluded is true or false.

#### Signature

`public Boolean isExcluded {get; set;}`

#### Property Value

Type: Boolean

### quoteVisibility

Get the quotevisibility value.

#### Signature

`public String quoteVisibility {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_ricpq_ProductSellingModelOptionOR.htm ===
---
page_id: apex_class_ricpq_ProductSellingModelOptionOR.htm
title: ProductSellingModelOptionOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_ricpq_ProductSellingModelOptionOR.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSellingModelOptionOutputRepresentation Class

Represents a selling model option available for a product, which defines how the product can be sold (such as subscription, one-time, or usage-based).

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductSellingModelOptionOutputRepresentation Properties](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_ricpq_ProductSellingModelOptionOR_properties)**  

Learn more about the properties available with the     ProductSellingModelOptionOutputRepresentation class.

  

## ProductSellingModelOptionOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductSellingModelOptionOutputRepresentation class.

    
      

The  `ProductSellingModelOptionOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[id](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_runtime_industries_cpq_ProductSellingModelOptionOutputRepresentation_id)**  

Get or set the unique identifier of the product selling model option.

- 
**[productId](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_ricpq_ProductSellingModelOptionOR_productId)**  

Get or set the identifier of the product that this selling model option applies to.

- 
**[productSellingModel](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_ricpq_ProductSellingModelOptionOR_productSellingModel)**  

Get or set the product selling model details for this option.

- 
**[productSellingModelId](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_ricpq_ProductSellingModelOptionOR_productSellingModelId)**  

Get or set the identifier of the product selling model for this option.

### id

Get or set the unique identifier of the product selling model option.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### productId

Get or set the identifier of the product that this selling model option applies to.

#### Signature

`public String productId {get; set;}`

#### Property Value

Type: String

### productSellingModel

Get or set the product selling model details for this option.

#### Signature

`public runtime_industries_cpq.ProductSellingModelOutputRepresentation productSellingModel {get; set;}`

#### Property Value

Type: runtime_industries_cpq.ProductSellingModelOutputRepresentation

### productSellingModelId

Get or set the identifier of the product selling model for this option.

#### Signature

`public String productSellingModelId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_ricpq_ProductSpecificationRecordTypeOR.htm ===
---
page_id: apex_class_ricpq_ProductSpecificationRecordTypeOR.htm
title: ProductSpecificationRecordTypeOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_ricpq_ProductSpecificationRecordTypeOR.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationRecordTypeOutputRepresentation Class

Represents the record type information for a product specification, which defines the type of record used to store product specification data.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductSpecificationRecordTypeOutputRepresentation Properties](./apex_class_ricpq_ProductSpecificationRecordTypeOR.htm.md#apex_ricpq_ProductSpecificationRecordTypeOR_properties)**  

Learn more about the properties available with the     ProductSpecificationRecordTypeOutputRepresentation class.

  

## ProductSpecificationRecordTypeOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductSpecificationRecordTypeOutputRepresentation class.

    
      

The  `ProductSpecificationRecordTypeOutputRepresentation`
        class includes these properties.

    

    
  

- 
**[isCommercial](./apex_class_ricpq_ProductSpecificationRecordTypeOR.htm.md#apex_ricpq_ProductSpecificationRecordTypeOR_isCommercial)**  

Get or set whether this product specification record type is commercial.

### isCommercial

Get or set whether this product specification record type is commercial.

#### Signature

`public Boolean isCommercial {get; set;}`

#### Property Value

Type: Boolean

=== ARTICLE: apex_class_ricpq_ProductSpecificationTypeOR.htm ===
---
page_id: apex_class_ricpq_ProductSpecificationTypeOR.htm
title: ProductSpecificationTypeOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_ricpq_ProductSpecificationTypeOR.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationTypeOutputRepresentation Class

Represents a product specification type that defines the structure and attributes available for configuring a product.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductSpecificationTypeOutputRepresentation Properties](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_ricpq_ProductSpecificationTypeOR_properties)**  

Learn more about the properties available with the     ProductSpecificationTypeOutputRepresentation class.

  

## ProductSpecificationTypeOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductSpecificationTypeOutputRepresentation class.

    
      

The `ProductSpecificationTypeOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[name](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_ricpq_ProductSpecificationTypeOR_name)**  

Get or set the name of the product specification type.

- 
**[productSpecificationRecordType](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_ricpq_ProductSpecificationTypeOR_productSpecificationRecordType)**  

Get or set the product specification record type associated with this specification type.

### name

Get or set the name of the product specification type.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### productSpecificationRecordType

Get or set the product specification record type associated with this specification type.

#### Signature

`public runtime_industries_cpq.ProductSpecificationRecordTypeOutputRepresentation productSpecificationRecordType {get; set;}`

#### Property Value

Type: runtime_industries_cpq.ProductSpecificationRecordTypeOutputRepresentation

=== ARTICLE: apex_class_runtime_industries_cpq_AdditionalContextData.htm ===
---
page_id: apex_class_runtime_industries_cpq_AdditionalContextData.htm
title: AdditionalContextData Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AdditionalContextData.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AdditionalContextData Class

Contains properties to include a list of additional context data nodes. These nodes are
    used along with the context definition nodes for data hydration.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AdditionalContextData Properties](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md#apex_runtime_industries_cpq_AdditionalContextData_properties)**  

Set the AdditionalContextData class property to specify a list of additional nodes for     data hydration.

  

## AdditionalContextData Properties

  
  
  
Set the AdditionalContextData class property to specify a list of additional nodes for
    data hydration.

    
      

The `AdditionalContextData` class includes this
        property.

    

    
  

- 
**[additionalContextData](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md#apex_runtime_industries_cpq_AdditionalContextData_additionalContextData)**  

Include a list of additional nodes that are used along with the context definition nodes     for data hydration. The maximum number of supported nodes is 10.

### additionalContextData

Include a list of additional nodes that are used along with the context definition nodes
    for data hydration. The maximum number of supported nodes is 10.

#### Signature

`public List<runtime_industries_cpq.ContextDataInput> additionalContextData {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ContextDataInput](./apex_class_runtime_industries_cpq_ContextDataInput.htm.md#apex_class_runtime_industries_cpq_ContextDataInput)>

=== ARTICLE: apex_class_runtime_industries_cpq_AdditionalFields.htm ===
---
page_id: apex_class_runtime_industries_cpq_AdditionalFields.htm
title: AdditionalFields Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AdditionalFields.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AdditionalFields Class

Contains properties to include a map where the key is a string and the value is an
    instance of the AdditionalFieldsInput class.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AdditionalFields Properties](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md#apex_runtime_industries_cpq_AdditionalFields_properties)**  

Set the AdditionalFields class property to include a map where the key is a string and     the value is an instance of the AdditionalFieldsInput class.

  

## AdditionalFields Properties

  
  
  
Set the AdditionalFields class property to include a map where the key is a string and
    the value is an instance of the AdditionalFieldsInput class.

    
      

The `AdditionalFields` class includes this property.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md#apex_runtime_industries_cpq_AdditionalFields_additionalFields)**  

Includes a map where the key is a string and the value is an instance of the     AdditionalFieldsInput class.

### additionalFields

Includes a map where the key is a string and the value is an instance of the
    AdditionalFieldsInput class.

#### Signature

`public Map<String,runtime_industries_cpq.AdditionalFieldsInput> additionalFields {get; set;}`

#### Property Value

Type: Map<String,[runtime_industries_cpq.AdditionalFieldsInput](./apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm.md#apex_class_runtime_industries_cpq_AdditionalFieldsInput)>

=== ARTICLE: apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm ===
---
page_id: apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm
title: AdditionalFieldsInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AdditionalFieldsInput Class

Contains properties to include the additional standard or custom fields in the
    request.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AdditionalFieldsInput Properties](./apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm.md#apex_runtime_industries_cpq_AdditionalFieldsInput_properties)**  

Set the AdditionalFieldsInput class property to include the additional standard or     custom fields in the response.

  

## AdditionalFieldsInput Properties

  
  
  
Set the AdditionalFieldsInput class property to include the additional standard or
    custom fields in the response.

    
      

The `AdditionalFieldsInput` class includes this
        property.

    

    
  

- 
**[fields](./apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm.md#apex_runtime_industries_cpq_AdditionalFieldsInput_fields)**  

Include the additional standard or custom fields in the response.

### fields

Include the additional standard or custom fields in the response.

#### Signature

`public List<String> fields {get; set;}`

#### Property Value

Type: List<String>

=== ARTICLE: apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm
title: ApiStatusRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ApiStatusRepresentation Class

Stores details of the API request such as execution messages, status code, and status
    message.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ApiStatusRepresentation Properties](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md#apex_runtime_industries_cpq_ApiStatusRepresentation_properties)**  

Contains properties to include the API response details.

  

## ApiStatusRepresentation Properties

  
  
  
Contains properties to include the API response details.

    
      

The `ApiStatusRepresentation` class includes these
        properties.

    

    
  

- 
**[messages](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md#apex_runtime_industries_cpq_ApiStatusRepresentation_messages)**  

Get the status messages of the API execution.

- 
**[statusCode](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md#apex_runtime_industries_cpq_ApiStatusRepresentation_statusCode)**  

Get the status code of the API execution.

- 
**[statusMessage](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md#apex_runtime_industries_cpq_ApiStatusRepresentation_statusMessage)**  

Get the display label for the API status.

### messages

Get the status messages of the API execution.

#### Signature

`public List<ConnectApi.CpqMessageOutputRepresentation> messages {get; set;}`

#### Property Value

Type: List<ConnectApi.CpqMessageOutputRepresentation>

### statusCode

Get the status code of the API execution.

#### Signature

`public String statusCode {get; set;}`

#### Property Value

Type: String

### statusMessage

Get the display label for the API status.

#### Signature

`public String statusMessage {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm
title: AttributeCategoryOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttributeCategoryOutputRepresentation Class

Stores details of an attribute such as code, description, usage type, and so
    on.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AttributeCategoryOutputRepresentation Properties](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_properties)**  

Contains properties to include details of an attribute.

  

## AttributeCategoryOutputRepresentation Properties

  
  
  
Contains properties to include details of an attribute.

    
      

The `AttributeCategoryOutputRepresentation` class includes
        these properties.

    

    
  

- 
**[code](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_code)**  

Get the code of the attribute category.

- 
**[description](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_ricpq_AttributeCategoryOR_description)**  

Get the description of the attribute category.

- 
**[id](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_id)**  

Get the ID of the attribute category.

- 
**[name](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_name)**  

Get the name of the attribute category.

- 
**[records](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_records)**  

Get the attributes of the attribute category.

- 
**[status](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_status)**  

Get the status of the attribute category.

- 
**[totalSize](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_totalSize)**  

Get the total size of the attribute category.

- 
**[usageType](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributeCategoryOutputRepresentation_usageType)**  

Get the usage type of the attribute category.

### code

Get the code of the attribute category.

#### Signature

`public String code {get; set;}`

#### Property Value

Type: String

### description

Get the description of the attribute category.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the attribute category.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the attribute category.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### records

Get the attributes of the attribute category.

#### Signature

`public List<runtime_industries_cpq.ProductAttributeOutputRepresentation> records {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductAttributeOutputRepresentation](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation)>

### status

Get the status of the attribute category.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### totalSize

Get the total size of the attribute category.

#### Signature

`public Integer totalSize {get; set;}`

#### Property Value

Type: Integer

### usageType

Get the usage type of the attribute category.

#### Signature

`public String usageType {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm
title: AttributePickListOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttributePickListOutputRepresentation Class

Stores details of an attribute picklist.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AttributePickListOutputRepresentation Properties](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_properties)**  

Contains properties to include details of an attribute picklist.

  

## AttributePickListOutputRepresentation Properties

  
  
  
Contains properties to include details of an attribute picklist.

    
      

The `AttributePickListOutputRepresentation` class includes
        these properties.

    

    
  

- 
**[description](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_ricpq_AttributePickListOR_description)**  

Get the description of the attribute picklist.

- 
**[id](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_id)**  

Get the ID of the attribute picklist.

- 
**[name](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_name)**  

Get the name of the attribute picklist.

- 
**[status](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_status)**  

Get the status of the attribute picklist.

- 
**[values](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_values)**  

Get the values of the attribute picklist.

- 
**[dataType](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListOutputRepresentation_dataType)**  

Get the datatype value.

### description

Get the description of the attribute picklist.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the attribute picklist.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the attribute picklist.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### status

Get the status of the attribute picklist.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### values

Get the values of the attribute picklist.

#### Signature

`public List<runtime_industries_cpq.AttributePickListValueOutputRepresentation> values {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributePickListValueOutputRepresentation](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation)>

### dataType

Get the datatype value.

#### Signature

`public String dataType {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm
title: AttributePickListValueOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttributePickListValueOutputRepresentation Class

Stores details of an attribute picklist value.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[AttributePickListValueOutputRepresentation Properties](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_properties)**  

Contains properties to include details of an attribute picklist value.

  

## AttributePickListValueOutputRepresentation Properties

  
  
  
Contains properties to include details of an attribute picklist value.

    
      

The `AttributePickListValueOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[code](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListValueOutputRepresentation_code)**  

Get the code of the attribute picklist value.

- 
**[description](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_description)**  

Get the description of attribute picklist value.

- 
**[displayValue](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_displayValue)**  

Get the display value of the attribute value.

- 
**[id](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListValueOutputRepresentation_id)**  

Get the ID of the attribute picklist value.

- 
**[isBooleanValue](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_isBooleanValue)**  

Indicates whether this attribute value is a boolean value (true) or not     (false).

- 
**[label](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListValueOutputRepresentation_label)**  

Get the label of the attribute picklist value.

- 
**[name](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_runtime_industries_cpq_AttributePickListValueOutputRepresentation_name)**  

Get the name of the attribute picklist value.

- 
**[sequence](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_sequence)**  

Get the sequence of the attribute picklist value.

- 
**[status](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_status)**  

Get the status of the attribute picklist value.

- 
**[textValue](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_ricpq_AttributePickListValueOR_textValue)**  

Get the text value of the attribute picklist value.

### code

Get the code of the attribute picklist value.

#### Signature

`public String code {get; set;}`

#### Property Value

Type: String

### description

Get the description of attribute picklist value.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### displayValue

Get the display value of the attribute value.

#### Signature

`public String displayValue {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the attribute picklist value.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isBooleanValue

Indicates whether this attribute value is a boolean value (true) or not
    (false).

#### Signature

`public Boolean isBooleanValue {get; set;}`

#### Property Value

Type: Boolean

### label

Get the label of the attribute picklist value.

#### Signature

`public String label {get; set;}`

#### Property Value

Type: String

### name

Get the name of the attribute picklist value.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### sequence

Get the sequence of the attribute picklist value.

#### Signature

`public Integer sequence {get; set;}`

#### Property Value

Type: Integer

### status

Get the status of the attribute picklist value.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### textValue

Get the text value of the attribute picklist value.

#### Signature

`public String textValue {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm ===
---
page_id: apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm
title: BulkProductDetailsInputBody Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BulkProductDetailsInputBody Class

Contains the details of the request to retrieve product details by using product ID and
    product selling model ID.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[BulkProductDetailsInputBody Properties](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md#apex_runtime_industries_cpq_BulkProductDetailsInputBody_properties)**  

Contains properties to retrieve details of products.

  

## BulkProductDetailsInputBody Properties

  
  
  
Contains properties to retrieve details of products.

    
      

The `BulkProductDetailsInputBody` class includes these
        properties.

    

    
  

- 
**[productId](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md#apex_runtime_industries_cpq_BulkProductDetailsInputBody_productId)**  

Set the ID of the product to return the details for.

- 
**[productSellingModelId](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md#apex_ricpq_BulkProductDetailsInputBody_productSellingModelId)**  

Set the ID of the product selling model to return the details for.

### productId

Set the ID of the product to return the details for.

#### Signature

`public String productId {get; set;}`

#### Property Value

Type: String

### productSellingModelId

Set the ID of the product selling model to return the details for.

#### Signature

`public String productSellingModelId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm ===
---
page_id: apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm
title: BulkProductDetailsInputBodyList Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BulkProductDetailsInputBodyList Class

Contains details of the request to retrieve a list of products.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[BulkProductDetailsInputBodyList Properties](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm.md#apex_runtime_industries_cpq_BulkProductDetailsInputBodyList_properties)**  

Contains properties to retrieve details of a list of products.

  

## BulkProductDetailsInputBodyList Properties

  
  
  
Contains properties to retrieve details of a list of products.

    
      

The `BulkProductDetailsInputBodyList` class includes these
        properties.

    

    
  

- 
**[productData](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm.md#apex_runtime_industries_cpq_BulkProductDetailsInputBodyList_productData)**  

Set the list of maps that contain product IDs and product selling model IDs.

### productData

Set the list of maps that contain product IDs and product selling model IDs.

#### Signature

`public List<runtime_industries_cpq.BulkProductDetailsInputBody> productData {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.BulkProductDetailsInputBody](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md#apex_class_runtime_industries_cpq_BulkProductDetailsInputBody)>

=== ARTICLE: apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm
title: BulkProductDetailsRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BulkProductDetailsRepresentation Class

Get the details of multiple product definitions in a single request. This class is used for bulk product retrieval operations in Product Discovery.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[BulkProductDetailsRepresentation Constructor](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_constructors)**  

Learn more about the constructors that are available with the BulkProductDetailsRepresentation     class.

- 
**[BulkProductDetailsRepresentation Properties](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_properties)**  

Contains properties to include details of product definitions retrieved in bulk operations.

  

## BulkProductDetailsRepresentation Constructor

  
  
  
Learn more about the constructors that are available with the BulkProductDetailsRepresentation
    class.

    
      

The `BulkProductDetailsRepresentation` class includes these
        constructors.

    

    
  

- 
**[BulkProductDetailsRepresentation(apexObj)](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_ctor)**  

Constructor to create a BulkProductDetailsRepresentation instance from a ConnectApi CPQProductDetailsOutputRepresentation object.

- 
**[BulkProductDetailsRepresentation()](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_ctor_2)**  

Default constructor to create an empty BulkProductDetailsRepresentation instance.

### BulkProductDetailsRepresentation(apexObj)

Constructor to create a BulkProductDetailsRepresentation instance from a ConnectApi CPQProductDetailsOutputRepresentation object.

#### Signature

`public BulkProductDetailsRepresentation(ConnectApi.CPQProductDetailsOutputRepresentation apexObj)`

#### Parameters

**apexObj**

: Type: ConnectApi.CPQProductDetailsOutputRepresentation

: The ConnectApi product details representation object to convert to BulkProductDetailsRepresentation.

### BulkProductDetailsRepresentation()

Default constructor to create an empty BulkProductDetailsRepresentation instance.

#### Signature

`public BulkProductDetailsRepresentation()`

  

## BulkProductDetailsRepresentation Properties

  
  
  
Contains properties to include details of product definitions retrieved in bulk operations.

    
      

The `BulkProductDetailsRepresentation` class includes these
        properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_additionalFields)**  

Get the list of additionalfield.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_attributeCategories)**  

Get the list of attributecategorie.

- 
**[attributes](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_attributes)**  

Get the list of attribute.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_availabilityDate)**  

Get the availability date.

- 
**[catalogs](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_catalogs)**  

Get the list of catalog.

- 
**[childProducts](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_childProducts)**  

Get the list of childproduct.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_configureDuringSale)**  

Get the configureduringsale value.

- 
**[description](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_description)**  

Get the description of the bulkproductdetails.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_discontinuedDate)**  

Get the discontinued date.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_displayUrl)**  

Get the displayurl value.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_endOfLifeDate)**  

Get the endoflife date.

- 
**[isActive](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_isActive)**  

Indicates whether the item is active.

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_isAssetizable)**  

Indicates whether assetizable is true or false.

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_isComponentRequired)**  

Indicates whether componentrequired is true or false.

- 
**[id](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_id)**  

Get the ID of the product.

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_isDefaultComponent)**  

Indicates whether defaultcomponent is true or false.

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_isQuantityEditable)**  

Indicates whether quantityeditable is true or false.

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_isSoldOnlyWithOtherProds)**  

Indicates whether soldonlywithotherprods is true or false.

- 
**[name](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_name)**  

Get the name of the bulkproductdetails.

- 
**[nodeType](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_nodeType)**  

Get the nodetype value.

- 
**[prices](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_prices)**  

Get the list of price.

- 
**[productClassification](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productClassification)**  

Get the productclassification value.

- 
**[productCode](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_productCode)**  

Get the productcode value.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productComponentGroups)**  

Get the list of productcomponentgroup.

- 
**[productInformation](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productInformation)**  

Get the productinformation value.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productPricingInformation)**  

Get the productpricinginformation value.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_productQuantity)**  

Get the productquantity value.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productRelatedComponent)**  

Get the productrelatedcomponent value.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productSellingModelOptions)**  

Get the list of productsellingmodeloption.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_productSpecificationType)**  

Get the productspecificationtype value.

- 
**[productType](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_productType)**  

Get the producttype value.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_ricpq_BulkProductDetailsR_qualificationContext)**  

Get the qualificationcontext value.

- 
**[status](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_status)**  

Get the status of the bulkproductdetails.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_BulkProductDetailsRepresentation_unitOfMeasure)**  

Get the unitofmeasure value.

### additionalFields

Get the list of additionalfield.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get the list of attributecategorie.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributeCategoryOutputRepresentation](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)>

### attributes

Get the list of attribute.

#### Signature

`public List<runtime_industries_cpq.ProductAttributeOutputRepresentation> attributes {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductAttributeOutputRepresentation](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation)>

### availabilityDate

Get the availability date.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get the list of catalog.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)>

### childProducts

Get the list of childproduct.

#### Signature

`public List<runtime_industries_cpq.BulkProductDetailsRepresentation> childProducts {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.BulkProductDetailsRepresentation](#apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation)>

### configureDuringSale

Get the configureduringsale value.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get the description of the bulkproductdetails.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get the discontinued date.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get the displayurl value.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get the endoflife date.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### isActive

Indicates whether the item is active.

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Indicates whether assetizable is true or false.

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Indicates whether componentrequired is true or false.

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### id

Get the ID of the product.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isDefaultComponent

Indicates whether defaultcomponent is true or false.

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Indicates whether quantityeditable is true or false.

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Indicates whether soldonlywithotherprods is true or false.

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the bulkproductdetails.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get the nodetype value.

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### prices

Get the list of price.

#### Signature

`public List<runtime_industries_cpq.ProductPricesOutputRepresentation> prices {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductPricesOutputRepresentation](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation)>

### productClassification

Get the productclassification value.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)

### productCode

Get the productcode value.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get the list of productcomponentgroup.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupRepresentation](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation)>

### productInformation

Get the productinformation value.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get the productpricinginformation value.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get the productquantity value.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductQuantityOutputRepresentation](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)

### productRelatedComponent

Get the productrelatedcomponent value.

#### Signature

`public runtime_industries_cpq.ProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductRelatedComponentOutputRepresentation](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_class_ricpq_ProductRelatedComponentOR)

### productSellingModelOptions

Get the list of productsellingmodeloption.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)>

### productSpecificationType

Get the productspecificationtype value.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)

### productType

Get the producttype value.

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the qualificationcontext value.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### status

Get the status of the bulkproductdetails.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get the unitofmeasure value.

#### Signature

`public runtime_industries_cpq.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.UnitOfMeasureOutputRepresentation](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation)

=== ARTICLE: apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm
title: CatalogOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CatalogOutputRepresentation Class

Contains properties to store details of a catalog definition.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[CatalogOutputRepresentation Properties](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_properties)**  

Contains properties to include details of a catalog definition.

  

## CatalogOutputRepresentation Properties

  
  
  
Contains properties to include details of a catalog definition.

    
      

The `CatalogOutputRepresentation` class includes these
        properties.

    

    
  

- 
**[catalogCode](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_catalogCode)**  

Get the unique ID associated with the catalog.

- 
**[catalogType](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_catalogType)**  

Get the category of an entry in the catalog, which is customizable. For example, catalog     types, such as sellable products, services, parts, technical services, or technical     resources.

- 
**[customFields](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_customFields)**  

Get details of the custom fields associated with a catalog.

- 
**[description](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_description)**  

Get the description of the catalog.

- 
**[effectiveEndDate](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_effectiveEndDate)**  

Get the date and time from when the catalog isn't available to the end users.

- 
**[effectiveStartDate](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_effectiveStartDate)**  

Get the date and time from when the catalog is available to the end users.

- 
**[id](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_id)**  

Get the ID of the catalog.

- 
**[name](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_name)**  

Get the name of the catalog.

- 
**[numberOfCategories](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_numberOfCategories)**  

Get the number of categories in the catalog.

- 
**[status](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_runtime_industries_cpq_CatalogOutputRepresentation_status)**  

Get the status of the catalog.

### catalogCode

Get the unique ID associated with the catalog.

#### Signature

`public String catalogCode {get; set;}`

#### Property Value

Type: String

### catalogType

Get the category of an entry in the catalog, which is customizable. For example, catalog
    types, such as sellable products, services, parts, technical services, or technical
    resources.

#### Signature

`public String catalogType {get; set;}`

#### Property Value

Type: String

### customFields

Get details of the custom fields associated with a catalog.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> customFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### description

Get the description of the catalog.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### effectiveEndDate

Get the date and time from when the catalog isn't available to the end users.

#### Signature

`public String effectiveEndDate {get; set;}`

#### Property Value

Type: String

### effectiveStartDate

Get the date and time from when the catalog is available to the end users.

#### Signature

`public String effectiveStartDate {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the catalog.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the catalog.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### numberOfCategories

Get the number of categories in the catalog.

#### Signature

`public Integer numberOfCategories {get; set;}`

#### Property Value

Type: Integer

### status

Get the status of the catalog.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm
title: CategoryOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CategoryOutputRepresentation Class

Contains properties to store details of a category.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[CategoryOutputRepresentation Properties](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_properties)**  

Learn more about the properties available with the CategoryOutputRepresentation     class.

  

## CategoryOutputRepresentation Properties

  
  
  
Learn more about the properties available with the CategoryOutputRepresentation
    class.

    
      

The `CategoryOutputRepresentation` class includes these
        properties.

    

    
  

- 
**[catalogId](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_catalogId)**  

Get the ID of the catalog that the category is associated with.

- 
**[description](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_description)**  

Get the description of a catalog.

- 
**[hasSubCategories](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_hasSubCategories)**  

Indicates whether the subcategories are available (true) or not (false).

- 
**[id](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_id)**  

Get the ID of the category.

- 
**[isNavigational](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_isNavigational)**  

Indicates whether the category node is navigational (true) or not (false).

- 
**[name](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_name)**  

Get the name of the category. If data translation is set up and specified in the org, the     translated name is available.

- 
**[parentCategoryId](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_parentCategoryId)**  

Get the ID of the parent category.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_ricpq_CategoryOR_qualificationContext)**  

Get the context details of a user, which are used for qualification rules.

- 
**[sortOrder](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_sortOrder)**  

Get the display order of the product category relative to the siblings with the same     parent category.

- 
**[childCategories](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_runtime_industries_cpq_CategoryOutputRepresentation_childCategories)**  

Get the list of childcategorie.

### catalogId

Get the ID of the catalog that the category is associated with.

#### Signature

`public String catalogId {get; set;}`

#### Property Value

Type: String

### description

Get the description of a catalog.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### hasSubCategories

Indicates whether the subcategories are available (true) or not (false).

#### Signature

`public Boolean hasSubCategories {get; set;}`

#### Property Value

Type: Boolean

### id

Get the ID of the category.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isNavigational

Indicates whether the category node is navigational (true) or not (false).

#### Signature

`public Boolean isNavigational {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the category. If data translation is set up and specified in the org, the
    translated name is available.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### parentCategoryId

Get the ID of the parent category.

#### Signature

`public String parentCategoryId {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the context details of a user, which are used for qualification rules.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### sortOrder

Get the display order of the product category relative to the siblings with the same
    parent category.

#### Signature

`public Integer sortOrder {get; set;}`

#### Property Value

Type: Integer

### childCategories

Get the list of childcategorie.

#### Signature

`public List<runtime_industries_cpq.CategoryOutputRepresentation> childCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CategoryOutputRepresentation](#apex_class_runtime_industries_cpq_CategoryOutputRepresentation)>

=== ARTICLE: apex_class_runtime_industries_cpq_ConfigRuleResult.htm ===
---
page_id: apex_class_runtime_industries_cpq_ConfigRuleResult.htm
title: ConfigRuleResult Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ConfigRuleResult.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConfigRuleResult Class

Contains the results of configuration rule evaluation, including message rules, product recommendation rules, and visibility rules that are applied during product configuration.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ConfigRuleResult Constructor](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_constructors)**  

Learn more about the constructor that's available with the ConfigRuleResult     class.

- 
**[ConfigRuleResult Properties](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_properties)**  

Contains properties to store configuration rule evaluation results.

  

## ConfigRuleResult Constructor

  
  
  
Learn more about the constructor that's available with the ConfigRuleResult
    class.

    
      

The `ConfigRuleResult` class includes this
        constructor.

    

    
  

- 
**[ConfigRuleResult(transactionContextId, messageRules, productRecommendationRules, visibilityRules, errors)](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_ctor)**  

Constructor to create a ConfigRuleResult instance with configuration rule evaluation results.

### ConfigRuleResult(transactionContextId, messageRules, productRecommendationRules, visibilityRules, errors)

Constructor to create a ConfigRuleResult instance with configuration rule evaluation results.

#### Signature

`public ConfigRuleResult(String transactionContextId, List<runtime_industries_cpq.MessageRule> messageRules, List<runtime_industries_cpq.ProductRecommendationRule> productRecommendationRules, List<runtime_industries_cpq.VisibilityRule> visibilityRules, List<String> errors)`

#### Parameters

**transactionContextId**

: Type: String

: The ID of the transaction context for this configuration rule evaluation.

**messageRules**

: Type: List<runtime_industries_cpq.MessageRule>

: List of message rules that were evaluated during configuration.

**productRecommendationRules**

: Type: List<runtime_industries_cpq.ProductRecommendationRule>

: List of product recommendation rules that were evaluated during configuration.

**visibilityRules**

: Type: List<runtime_industries_cpq.VisibilityRule>

: List of visibility rules that were evaluated during configuration.

**errors**

: Type: List<String>

: List of error messages from the configuration rule evaluation, if any.

  

## ConfigRuleResult Properties

  
  
  
Contains properties to store configuration rule evaluation results.

    
      

The `ConfigRuleResult` class includes these
        properties.

    

    
  

- 
**[errors](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_errors)**  

Get the list of error messages.

- 
**[messageRules](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_messageRules)**  

Get the list of messagerule.

- 
**[productRecommendationRules](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_productRecommendationRules)**  

Get the list of productrecommendationrule.

- 
**[transactionContextId](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_transactionContextId)**  

Get the ID of the transactioncontext.

- 
**[visibilityRules](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_runtime_industries_cpq_ConfigRuleResult_visibilityRules)**  

Get the list of visibilityrule.

### errors

Get the list of error messages.

#### Signature

`public List<String> errors {get; set;}`

#### Property Value

Type: List<String>

### messageRules

Get the list of messagerule.

#### Signature

`public List<runtime_industries_cpq.MessageRule> messageRules {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.MessageRule](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_class_runtime_industries_cpq_MessageRule)>

### productRecommendationRules

Get the list of productrecommendationrule.

#### Signature

`public List<runtime_industries_cpq.ProductRecommendationRule> productRecommendationRules {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductRecommendationRule](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_class_runtime_industries_cpq_ProductRecommendationRule)>

### transactionContextId

Get the ID of the transactioncontext.

#### Signature

`public String transactionContextId {get; set;}`

#### Property Value

Type: String

### visibilityRules

Get the list of visibilityrule.

#### Signature

`public List<runtime_industries_cpq.VisibilityRule> visibilityRules {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.VisibilityRule](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_class_runtime_industries_cpq_VisibilityRule)>

=== ARTICLE: apex_class_runtime_industries_cpq_ContextDataInput.htm ===
---
page_id: apex_class_runtime_industries_cpq_ContextDataInput.htm
title: ContextDataInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ContextDataInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ContextDataInput Class

Get details of a context.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ContextDataInput Properties](./apex_class_runtime_industries_cpq_ContextDataInput.htm.md#apex_runtime_industries_cpq_ContextDataInput_properties)**  

Learn more about the properties available with the ContextDataInput class.

  

## ContextDataInput Properties

  
  
  
Learn more about the properties available with the ContextDataInput class.

    
      

The `ContextDataInput` class includes these
        properties.

    

    
  

- 
**[nodeData](./apex_class_runtime_industries_cpq_ContextDataInput.htm.md#apex_runtime_industries_cpq_ContextDataInput_nodeData)**  

Get details of the node.

- 
**[nodeName](./apex_class_runtime_industries_cpq_ContextDataInput.htm.md#apex_runtime_industries_cpq_ContextDataInput_nodeName)**  

Get the name of the node.

### nodeData

Get details of the node.

#### Signature

`public Map<String,ANY> nodeData {get; set;}`

#### Property Value

Type: Map<String,ANY>

### nodeName

Get the name of the node.

#### Signature

`public String nodeName {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_FacetValueRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_FacetValueRepresentation.htm
title: FacetValueRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_FacetValueRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FacetValueRepresentation Class

Get details of the facet values that are found in the search result.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[FacetValueRepresentation Properties](./apex_class_runtime_industries_cpq_FacetValueRepresentation.htm.md#apex_runtime_industries_cpq_FacetValueRepresentation_properties)**  

Learn more about the properties available with the FacetValueRepresentation     class.

  

## FacetValueRepresentation Properties

  
  
  
Learn more about the properties available with the FacetValueRepresentation
    class.

    
      

The `FacetValueRepresentation` class includes these
        properties.

    

    
  

- 
**[displayName](./apex_class_runtime_industries_cpq_FacetValueRepresentation.htm.md#apex_runtime_industries_cpq_FacetValueRepresentation_displayName)**  

Get the display name of the facet value.

- 
**[nameOrId](./apex_class_runtime_industries_cpq_FacetValueRepresentation.htm.md#apex_runtime_industries_cpq_FacetValueRepresentation_nameOrId)**  

Get the name or ID of the facet. Reserved for internal use.

### displayName

Get the display name of the facet value.

#### Signature

`public String displayName {get; set;}`

#### Property Value

Type: String

### nameOrId

Get the name or ID of the facet. Reserved for internal use.

#### Signature

`public String nameOrId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_Filter.htm ===
---
page_id: apex_class_runtime_industries_cpq_Filter.htm
title: Filter Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_Filter.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Filter Class

Contains the criteria property to store the details of a filter criteria, which is used
    to filter records.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[Filter Properties](./apex_class_runtime_industries_cpq_Filter.htm.md#apex_runtime_industries_cpq_Filter_properties)**  

Learn more about the properties available with the Filter class.

  

## Filter Properties

  
  
  
Learn more about the properties available with the Filter class.

    
      

The `Filter` class includes these properties.

    

    
  

- 
**[criteria](./apex_class_runtime_industries_cpq_Filter.htm.md#apex_runtime_industries_cpq_Filter_criteria)**  

Get the filter criteria to filter the records.

### criteria

Get the filter criteria to filter the records.

#### Signature

`public List<runtime_industries_cpq.FilterCriteriaInputRepresentation> criteria {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.FilterCriteriaInputRepresentation](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation)>

=== ARTICLE: apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm
title: FilterCriteriaInputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FilterCriteriaInputRepresentation Class

Contains properties to store criteria details to filter records based on supported
    properties.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[FilterCriteriaInputRepresentation Properties](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterCriteriaInputRepresentation_properties)**  

Learn more about the properties available with the FilterCriteriaInputRepresentation     class.

  

## FilterCriteriaInputRepresentation Properties

  
  
  
Learn more about the properties available with the FilterCriteriaInputRepresentation
    class.

    
      

The `FilterCriteriaInputRepresentation` class includes
        these properties.

    

    
  

- 
**[attributeType](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterCriteriaInputRepresentation_attributeType)**  

Get details of the search attribute type of the facet for a faceted search.

- 
**[operator](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterCriteriaInputRepresentation_operator)**  

Get the operator that's used for the filter criteria.

- 
**[property](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterCriteriaInputRepresentation_property)**  

Get the property name to use in the filter, which must be the same as the object field.     The supported property is name.

- 
**[value](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterCriteriaInputRepresentation_value)**  

Get the value for the filter criteria.

### attributeType

Get details of the search attribute type of the facet for a faceted search.

#### Signature

`public String attributeType {get; set;}`

#### Property Value

Type: String

    

#### Usage

      
      

Valid values are:

      
                        
- `ProductStandard`

                        
- `ProductCustom`

                        
- `ProductDynamicAttribute`

                        
- `ProductAttributeStandard`

                        
- `ProductAttributeCustom`

                      

    

### operator

Get the operator that's used for the filter criteria.

#### Signature

`public String operator {get; set;}`

#### Property Value

Type: String

    

#### Usage

      
      

The supported operators are:

      
                        
- `eq`

                        
- `in`

                        
- `contains`

                        
- 
`gt`—Specifies a greater than
                          criteria. Available from API version 63.0 and later for Number, Date, and
                          Datetime data types only.

                        
- 
`lt`—Specifies a less than
                          criteria. Available from API version 63.0 and later for Number, Date, and
                          Datetime data types only.

                        
- 
`gte`—Specifies a greater than
                          or equal to criteria. Available from API version 63.0 and later for
                          Number, Date, and Datetime data types only.

                        
- 
`lte`—Specifies a less than or
                          equal to criteria. Available from API version 63.0 and later for Number,
                          Date, and Datetime data types only.

                      

    

### property

Get the property name to use in the filter, which must be the same as the object field.
    The supported property is name.

#### Signature

`public String property {get; set;}`

#### Property Value

Type: String

### value

Get the value for the filter criteria.

#### Signature

`public String value {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_FilterInputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_FilterInputRepresentation.htm
title: FilterInputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_FilterInputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# FilterInputRepresentation Class

Contains the filter property to filters records based on supported criteria.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[FilterInputRepresentation Properties](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterInputRepresentation_properties)**  

Learn more about the available properties with the FilterInputRepresentation     class.

  

## FilterInputRepresentation Properties

  
  
  
Learn more about the available properties with the FilterInputRepresentation
    class.

    
      

The `FilterInputRepresentation` class includes these
        properties.

    

    
  

- 
**[filter](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md#apex_runtime_industries_cpq_FilterInputRepresentation_filter)**  

Filters records based on supported criteria. The supported property is name.

### filter

Filters records based on supported criteria. The supported property is name.

#### Signature

`public runtime_industries_cpq.Filter filter {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.Filter](./apex_class_runtime_industries_cpq_Filter.htm.md#apex_class_runtime_industries_cpq_Filter)

    

#### Usage

      
      

The supported operators are:

      
                        
- `eq`

                        
- `in`

                        
- 
`contains`—This value isn't
                          applicable if the **Use Indexed Data For Product Listing and
                            Search** toggle from the Product Discovery Settings page from
                          Setup is enabled.

                      

      

If multiple criteria are specified, then the resultant criteria are combined by using the
          `and` operator.

=== ARTICLE: apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm
title: GuidedSelectionRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GuidedSelectionRepresentation Class

Contains properties to represent a product in a guided selection flow. This class is used in Product Discovery to provide structured product information during guided product selection processes.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[GuidedSelectionRepresentation Properties](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_properties)**  

Contains properties to include details of a product in a guided selection flow.

  

## GuidedSelectionRepresentation Properties

  
  
  
Contains properties to include details of a product in a guided selection flow.

    
      

The `GuidedSelectionRepresentation` class includes these
        properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_additionalFields)**  

Get the list of additionalfield.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_attributeCategories)**  

Get the list of attributecategorie.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_availabilityDate)**  

Get the availability date.

- 
**[catalogs](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_catalogs)**  

Get the list of catalog.

- 
**[categories](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_categories)**  

Get the list of categorie.

- 
**[childProducts](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_childProducts)**  

Get the list of childproduct.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_configureDuringSale)**  

Get the configureduringsale value.

- 
**[description](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_description)**  

Get the description of the guidedselection.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_discontinuedDate)**  

Get the discontinued date.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_displayUrl)**  

Get the displayurl value.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_endOfLifeDate)**  

Get the endoflife date.

- 
**[id](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_id)**  

Get the ID of the guidedselection.

- 
**[isActive](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_isActive)**  

Indicates whether the item is active.

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_isAssetizable)**  

Indicates whether assetizable is true or false.

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_isComponentRequired)**  

Indicates whether componentrequired is true or false.

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_isDefaultComponent)**  

Indicates whether defaultcomponent is true or false.

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_isQuantityEditable)**  

Indicates whether quantityeditable is true or false.

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_isSoldOnlyWithOtherProds)**  

Indicates whether soldonlywithotherprods is true or false.

- 
**[name](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_name)**  

Get the name of the guidedselection.

- 
**[nodeType](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_nodeType)**  

Get the nodetype value.

- 
**[prices](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_prices)**  

Get the list of price.

- 
**[productClassification](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productClassification)**  

Get the productclassification value.

- 
**[productCode](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_productCode)**  

Get the productcode value.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productComponentGroups)**  

Get the list of productcomponentgroup.

- 
**[productInformation](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_productInformation)**  

Get the productinformation value.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productPricingInformation)**  

Get the productpricinginformation value.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_productQuantity)**  

Get the productquantity value.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productRelatedComponent)**  

Get the productrelatedcomponent value.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productSellingModelOptions)**  

Get the list of productsellingmodeloption.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_productSpecificationType)**  

Get the productspecificationtype value.

- 
**[productType](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_productType)**  

Get the producttype value.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_ricpq_GuidedSelectionR_qualificationContext)**  

Get the qualificationcontext value.

- 
**[status](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_status)**  

Get the status of the guidedselection.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_runtime_industries_cpq_GuidedSelectionRepresentation_unitOfMeasure)**  

Get the unitofmeasure value.

### additionalFields

Get the list of additionalfield.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get the list of attributecategorie.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributeCategoryOutputRepresentation](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)>

### availabilityDate

Get the availability date.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get the list of catalog.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)>

### categories

Get the list of categorie.

#### Signature

`public List<runtime_industries_cpq.CategoryOutputRepresentation> categories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CategoryOutputRepresentation](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CategoryOutputRepresentation)>

### childProducts

Get the list of childproduct.

#### Signature

`public List<runtime_industries_cpq.ProductListRepresentation> childProducts {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductListRepresentation](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductListRepresentation)>

### configureDuringSale

Get the configureduringsale value.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get the description of the guidedselection.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get the discontinued date.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get the displayurl value.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get the endoflife date.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### id

Get the ID of the guidedselection.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isActive

Indicates whether the item is active.

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Indicates whether assetizable is true or false.

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Indicates whether componentrequired is true or false.

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Indicates whether defaultcomponent is true or false.

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Indicates whether quantityeditable is true or false.

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Indicates whether soldonlywithotherprods is true or false.

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the guidedselection.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get the nodetype value.

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### prices

Get the list of price.

#### Signature

`public List<runtime_industries_cpq.ProductPricesOutputRepresentation> prices {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductPricesOutputRepresentation](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation)>

### productClassification

Get the productclassification value.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)

### productCode

Get the productcode value.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get the list of productcomponentgroup.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupOutputRepresentation](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)>

### productInformation

Get the productinformation value.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get the productpricinginformation value.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get the productquantity value.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductQuantityOutputRepresentation](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)

### productRelatedComponent

Get the productrelatedcomponent value.

#### Signature

`public ConnectApi.CPQProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: ConnectApi.CPQProductRelatedComponentOutputRepresentation

### productSellingModelOptions

Get the list of productsellingmodeloption.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)>

### productSpecificationType

Get the productspecificationtype value.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)

### productType

Get the producttype value.

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the qualificationcontext value.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### status

Get the status of the guidedselection.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get the unitofmeasure value.

#### Signature

`public runtime_industries_cpq.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.UnitOfMeasureOutputRepresentation](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation)

=== ARTICLE: apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm ===
---
page_id: apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm
title: GuidedSelectionSearchTerm Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GuidedSelectionSearchTerm Class

Represents a search term used in guided product selection. Contains the search term text and associated tags for filtering and searching products in Product Discovery.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[GuidedSelectionSearchTerm Constructor](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_constructors)**  

Learn more about the constructors that are available with the GuidedSelectionSearchTerm     class.

- 
**[GuidedSelectionSearchTerm Properties](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_properties)**  

Contains properties to include search term details for guided product selection.

  

## GuidedSelectionSearchTerm Constructor

  
  
  
Learn more about the constructors that are available with the GuidedSelectionSearchTerm
    class.

    
      

The `GuidedSelectionSearchTerm` class includes these
        constructors.

    

    
  

- 
**[GuidedSelectionSearchTerm(apexObj)](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_ctor)**  

Constructor to create a GuidedSelectionSearchTerm instance from a ConnectApi CPQGuidedSelectionSearchTermOutputRepresentation object.

- 
**[GuidedSelectionSearchTerm()](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_ctor_2)**  

Default constructor to create an empty GuidedSelectionSearchTerm instance.

### GuidedSelectionSearchTerm(apexObj)

Constructor to create a GuidedSelectionSearchTerm instance from a ConnectApi CPQGuidedSelectionSearchTermOutputRepresentation object.

#### Signature

`public GuidedSelectionSearchTerm(ConnectApi.CPQGuidedSelectionSearchTermOutputRepresentation apexObj)`

#### Parameters

**apexObj**

: Type: ConnectApi.CPQGuidedSelectionSearchTermOutputRepresentation

: The ConnectApi guided selection search term representation object to convert to GuidedSelectionSearchTerm.

### GuidedSelectionSearchTerm()

Default constructor to create an empty GuidedSelectionSearchTerm instance.

#### Signature

`public GuidedSelectionSearchTerm()`

  

## GuidedSelectionSearchTerm Properties

  
  
  
Contains properties to include search term details for guided product selection.

    
      

The `GuidedSelectionSearchTerm` class includes these
        properties.

    

    
  

- 
**[tags](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_tags)**  

Get the list of tags.

- 
**[term](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTerm_term)**  

Get the term value.

### tags

Get the list of tags.

#### Signature

`public List<String> tags {get; set;}`

#### Property Value

Type: List<String>

### term

Get the term value.

#### Signature

`public String term {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm ===
---
page_id: apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm
title: GuidedSelectionSearchTermList Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GuidedSelectionSearchTermList Class

Contains a list of search terms used in guided product selection. This class is used to pass multiple search terms for filtering and searching products in Product Discovery.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[GuidedSelectionSearchTermList Constructor](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTermList_constructors)**  

Learn more about the constructor that's available with the GuidedSelectionSearchTermList     class.

- 
**[GuidedSelectionSearchTermList Properties](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTermList_properties)**  

Contains properties to include a list of search terms for guided product selection.

  

## GuidedSelectionSearchTermList Constructor

  
  
  
Learn more about the constructor that's available with the GuidedSelectionSearchTermList
    class.

    
      

The `GuidedSelectionSearchTermList` class includes this
        constructor.

    

    
  

- 
**[GuidedSelectionSearchTermList()](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTermList_ctor)**  

Default constructor to create an empty GuidedSelectionSearchTermList instance.

### GuidedSelectionSearchTermList()

Default constructor to create an empty GuidedSelectionSearchTermList instance.

#### Signature

`public GuidedSelectionSearchTermList()`

  

## GuidedSelectionSearchTermList Properties

  
  
  
Contains properties to include a list of search terms for guided product selection.

    
      

The `GuidedSelectionSearchTermList` class includes these
        properties.

    

    
  

- 
**[searchTerms](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm.md#apex_runtime_industries_cpq_GuidedSelectionSearchTermList_searchTerms)**  

Get the list of searchterm.

### searchTerms

Get the list of searchterm.

#### Signature

`public List<runtime_industries_cpq.GuidedSelectionSearchTerm> searchTerms {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.GuidedSelectionSearchTerm](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm)>

=== ARTICLE: apex_class_runtime_industries_cpq_MessageRule.htm ===
---
page_id: apex_class_runtime_industries_cpq_MessageRule.htm
title: MessageRule Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_MessageRule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# MessageRule Class

Represents a message rule that is evaluated during product configuration. Message rules display informational, warning, or error messages to users based on configuration conditions.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[MessageRule Constructor](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_constructors)**  

Learn more about the constructor that's available with the MessageRule     class.

- 
**[MessageRule Properties](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_properties)**  

Contains properties to store message rule details from configuration rule evaluation.

  

## MessageRule Constructor

  
  
  
Learn more about the constructor that's available with the MessageRule
    class.

    
      

The `MessageRule` class includes this
        constructor.

    

    
  

- 
**[MessageRule(stiId, severity, messages)](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_ctor)**  

Constructor to create a MessageRule instance with the specified STI ID, severity, and messages.

### MessageRule(stiId, severity, messages)

Constructor to create a MessageRule instance with the specified STI ID, severity, and messages.

#### Signature

`public MessageRule(String stiId, String severity, List<String> messages)`

#### Parameters

**stiId**

: Type: String

: The ID of the Sales Transaction Item (STI) associated with this message rule.

**severity**

: Type: String

: The severity level of the message (for example, Error, Warning, or Info).

**messages**

: Type: List<String>

: List of message strings to display to the user.

  

## MessageRule Properties

  
  
  
Contains properties to store message rule details from configuration rule evaluation.

    
      

The `MessageRule` class includes these
        properties.

    

    
  

- 
**[messages](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_messages)**  

Get the list of messages.

- 
**[severity](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_severity)**  

Get the severity value.

- 
**[stiId](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_runtime_industries_cpq_MessageRule_stiId)**  

Get the ID of the sti.

### messages

Get the list of messages.

#### Signature

`public List<String> messages {get; set;}`

#### Property Value

Type: List<String>

### severity

Get the severity value.

#### Signature

`public String severity {get; set;}`

#### Property Value

Type: String

### stiId

Get the ID of the sti.

#### Signature

`public String stiId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm
title: PricingModelOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PricingModelOutputRepresentation Class

Contains details of a pricing model in a product configuration.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[PricingModelOutputRepresentation Properties](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_properties)**  

Learn more about the properties available with the PricingModelOutputRepresentation     class.

  

## PricingModelOutputRepresentation Properties

  
  
  
Learn more about the properties available with the PricingModelOutputRepresentation
    class.

    
      

The `PricingModelOutputRepresentation` class includes
        these properties.

    

    
  

- 
**[frequency](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_frequency)**  

Contains frequency details of the pricing model.

- 
**[id](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_id)**  

Contains the ID of the pricing model.

- 
**[name](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_name)**  

Contains the name of the pricing model.

- 
**[occurrence](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_occurrence)**  

Contains details about the occurrence of the pricing model.

- 
**[pricingModelType](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_ricpq_PricingModelOR_pricingModelType)**  

Contains the type of the pricing model.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_PricingModelOutputRepresentation_unitOfMeasure)**  

Contains details about the unit of measure for the pricing model.

### frequency

Contains frequency details of the pricing model.

#### Signature

`public String frequency {get; set;}`

#### Property Value

Type: String

### id

Contains the ID of the pricing model.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Contains the name of the pricing model.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### occurrence

Contains details about the occurrence of the pricing model.

#### Signature

`public Integer occurrence {get; set;}`

#### Property Value

Type: Integer

### pricingModelType

Contains the type of the pricing model.

#### Signature

`public String pricingModelType {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Contains details about the unit of measure for the pricing model.

#### Signature

`public String unitOfMeasure {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm
title: ProductAttributeOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductAttributeOutputRepresentation Class

Contains details about the attribute in a product configuration.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductAttributeOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_properties)**  

Learn more about the properties available with the ProductAttributeOutputRepresentation     class.

  

## ProductAttributeOutputRepresentation Properties

  
  
  
Learn more about the properties available with the ProductAttributeOutputRepresentation
    class.

    
      

The `ProductAttributeOutputRepresentation` class includes
        these properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_additionalFields)**  

Get the key-value pairs of additional standard or custom fields and their values for the product attribute.

- 
**[attributeCategoryId](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_attributeCategoryId)**  

Get the ID of the attribute category.

- 
**[attributeNameOverride](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_attributeNameOverride)**  

Get the name override value of the attribute.

- 
**[attributePickList](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_attributePickList)**  

Get the picklist values of the attribute.

- 
**[code](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_code)**  

Get the code of the attribute.

- 
**[dataType](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_dataType)**  

Get the data type of the attribute.

- 
**[defaultHelpText](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_defaultHelpText)**  

Get the default help text value of the attribute.

- 
**[defaultValue](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_defaultValue)**  

Get the default value of the attribute.

- 
**[description](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_description)**  

Get the description of the attribute.

- 
**[developerName](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_developerName)**  

Get the developer name of the product attribute.

- 
**[displayTypeOverride](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_displayTypeOverride)**  

Get the override value of the display type of the attribute.

- 
**[hidden](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_hidden)**  

Indicates whether the attribute is hidden (true) or not (false).

- 
**[id](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_id)**  

Get the ID of the attribute.

- 
**[isCloneable](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_isCloneable)**  

Indicates whether the attribute is cloneable (true) or not (false).

- 
**[isConfigurable](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_isConfigurable)**  

Indicates whether the attribute is configurable (true) or not (false).

- 
**[isEncrypted](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_isEncrypted)**  

Indicates whether the attribute is encrypted (true) or not (false).

- 
**[isPriceImpacting](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_isPriceImpacting)**  

Indicates whether this is a price impacting attribute (true) or not (false).

- 
**[isReadOnly](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_isReadOnly)**  

Indicates whether the attribute is read-only (true) or not (false).

- 
**[isRequired](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_isRequired)**  

Indicates whether the attribute is required (true) or not (false).

- 
**[label](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_label)**  

Get the label of the attribute.

- 
**[maximumValue](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_maximumValue)**  

Get the maximum value for the product attribute.

- 
**[minimumValue](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_minimumValue)**  

Get the minimum value for the product attribute.

- 
**[name](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_name)**  

Get the name of the attribute.

- 
**[sequence](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_sequence)**  

Get the sequence values of the attribute.

- 
**[status](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_status)**  

Get the status of the attribute.

- 
**[stepValue](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_stepValue)**  

Get the step value for the attribute.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_unitOfMeasure)**  

Get details about the unit of measure associated with an attribute.

- 
**[userValue](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductAttributeOutputRepresentation_userValue)**  

Get the user value of the attribute.

- 
**[valueDescription](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_ricpq_ProductAttributeOR_valueDescription)**  

Get the value description of the attribute.

### additionalFields

Get the key-value pairs of additional standard or custom fields and their values for the product attribute.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategoryId

Get the ID of the attribute category.

#### Signature

`public String attributeCategoryId {get; set;}`

#### Property Value

Type: String

### attributeNameOverride

Get the name override value of the attribute.

#### Signature

`public String attributeNameOverride {get; set;}`

#### Property Value

Type: String

### attributePickList

Get the picklist values of the attribute.

#### Signature

`public runtime_industries_cpq.AttributePickListOutputRepresentation attributePickList {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.AttributePickListOutputRepresentation](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation)

### code

Get the code of the attribute.

#### Signature

`public String code {get; set;}`

#### Property Value

Type: String

### dataType

Get the data type of the attribute.

#### Signature

`public String dataType {get; set;}`

#### Property Value

Type: String

### defaultHelpText

Get the default help text value of the attribute.

#### Signature

`public String defaultHelpText {get; set;}`

#### Property Value

Type: String

### defaultValue

Get the default value of the attribute.

#### Signature

`public String defaultValue {get; set;}`

#### Property Value

Type: String

### description

Get the description of the attribute.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### developerName

Get the developer name of the product attribute.

#### Signature

`public String developerName {get; set;}`

#### Property Value

Type: String

### displayTypeOverride

Get the override value of the display type of the attribute.

#### Signature

`public String displayTypeOverride {get; set;}`

#### Property Value

Type: String

### hidden

Indicates whether the attribute is hidden (true) or not (false).

#### Signature

`public Boolean hidden {get; set;}`

#### Property Value

Type: Boolean

### id

Get the ID of the attribute.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isCloneable

Indicates whether the attribute is cloneable (true) or not (false).

#### Signature

`public Boolean isCloneable {get; set;}`

#### Property Value

Type: Boolean

### isConfigurable

Indicates whether the attribute is configurable (true) or not (false).

#### Signature

`public Boolean isConfigurable {get; set;}`

#### Property Value

Type: Boolean

### isEncrypted

Indicates whether the attribute is encrypted (true) or not (false).

#### Signature

`public Boolean isEncrypted {get; set;}`

#### Property Value

Type: Boolean

### isPriceImpacting

Indicates whether this is a price impacting attribute (true) or not (false).

#### Signature

`public Boolean isPriceImpacting {get; set;}`

#### Property Value

Type: Boolean

### isReadOnly

Indicates whether the attribute is read-only (true) or not (false).

#### Signature

`public Boolean isReadOnly {get; set;}`

#### Property Value

Type: Boolean

### isRequired

Indicates whether the attribute is required (true) or not (false).

#### Signature

`public Boolean isRequired {get; set;}`

#### Property Value

Type: Boolean

### label

Get the label of the attribute.

#### Signature

`public String label {get; set;}`

#### Property Value

Type: String

### maximumValue

Get the maximum value for the product attribute.

#### Signature

`public String maximumValue {get; set;}`

#### Property Value

Type: String

### minimumValue

Get the minimum value for the product attribute.

#### Signature

`public String minimumValue {get; set;}`

#### Property Value

Type: String

### name

Get the name of the attribute.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### sequence

Get the sequence values of the attribute.

#### Signature

`public Integer sequence {get; set;}`

#### Property Value

Type: Integer

### status

Get the status of the attribute.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### stepValue

Get the step value for the attribute.

#### Signature

`public String stepValue {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get details about the unit of measure associated with an attribute.

#### Signature

`public ConnectApi.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: ConnectApi.UnitOfMeasureOutputRepresentation

### userValue

Get the user value of the attribute.

#### Signature

`public String userValue {get; set;}`

#### Property Value

Type: String

### valueDescription

Get the value description of the attribute.

#### Signature

`public String valueDescription {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm
title: ProductClassificationOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductClassificationOutputRepresentation Class

Get details of the product classification in a product configuration.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductClassificationOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_ricpq_ProductClassificationOR_properties)**  

Learn more about the properties available with the     ProductClassificationOutputRepresentation class.

  

## ProductClassificationOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductClassificationOutputRepresentation class.

    
      

The `ProductClassificationOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[id](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductClassificationOutputRepresentation_id)**  

Get the ID of the product classification.

### id

Get the ID of the product classification.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm
title: ProductComponentGroupOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductComponentGroupOutputRepresentation Class

Get details of the product component group in a product classification.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductComponentGroupOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_properties)**  

Learn more about the properties available with the     ProductComponentGroupOutputRepresentation class.

  

## ProductComponentGroupOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductComponentGroupOutputRepresentation class.

    
      

The `ProductComponentGroupOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[childGroups](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_childGroups)**  

Get the child groups associated with a product component group.

- 
**[classifications](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_classifications)**  

Get the list of classifications for the product component group.

- 
**[code](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupOutputRepresentation_code)**  

Get the code of the product component group.

- 
**[components](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_components)**  

Get the details of components within the product component group.

- 
**[description](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_description)**  

Get the description of the product component group.

- 
**[id](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupOutputRepresentation_id)**  

Get the ID of the product component group.

- 
**[name](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupOutputRepresentation_name)**  

Get the name of the product component group.

- 
**[parentGroupId](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_parentGroupId)**  

Get the ID of the parent group.

- 
**[parentProductId](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_parentProductId)**  

Get the parent Product2 ID of the product component group.

- 
**[sequence](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_ricpq_ProductComponentGroupOR_sequence)**  

Get the sequence of the product component group.

### childGroups

Get the child groups associated with a product component group.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> childGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupOutputRepresentation](#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)>

### classifications

Get the list of classifications for the product component group.

#### Signature

`public List<runtime_industries_cpq.ProductClassificationOutputRepresentation> classifications {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)>

### code

Get the code of the product component group.

#### Signature

`public String code {get; set;}`

#### Property Value

Type: String

### components

Get the details of components within the product component group.

#### Signature

`public List<runtime_industries_cpq.ProductDetailsRepresentation> components {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductDetailsRepresentation](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductDetailsRepresentation)>

### description

Get the description of the product component group.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the product component group.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the product component group.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### parentGroupId

Get the ID of the parent group.

#### Signature

`public String parentGroupId {get; set;}`

#### Property Value

Type: String

### parentProductId

Get the parent Product2 ID of the product component group.

#### Signature

`public String parentProductId {get; set;}`

#### Property Value

Type: String

### sequence

Get the sequence of the product component group.

#### Signature

`public Integer sequence {get; set;}`

#### Property Value

Type: Integer

=== ARTICLE: apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm
title: ProductComponentGroupRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductComponentGroupRepresentation Class

Represents a product component group used in bulk product operations. This class is similar to ProductComponentGroupOutputRepresentation but is used specifically for bulk product detail representations where components are represented as BulkProductDetailsRepresentation objects.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductComponentGroupRepresentation Constructor](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_constructors)**  

Learn more about the constructor that's available with the ProductComponentGroupRepresentation     class.

- 
**[ProductComponentGroupRepresentation Properties](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_properties)**  

Contains properties to include details of a product component group used in bulk operations.

  

## ProductComponentGroupRepresentation Constructor

  
  
  
Learn more about the constructor that's available with the ProductComponentGroupRepresentation
    class.

    
      

The `ProductComponentGroupRepresentation` class includes this
        constructor.

    

    
  

- 
**[ProductComponentGroupRepresentation(apexObj)](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_ctor)**  

Constructor to create a ProductComponentGroupRepresentation instance from a ConnectApi CPQProductComponentGroupOutputRepresentation object.

### ProductComponentGroupRepresentation(apexObj)

Constructor to create a ProductComponentGroupRepresentation instance from a ConnectApi CPQProductComponentGroupOutputRepresentation object.

#### Signature

`public ProductComponentGroupRepresentation(ConnectApi.CPQProductComponentGroupOutputRepresentation apexObj)`

#### Parameters

**apexObj**

: Type: ConnectApi.CPQProductComponentGroupOutputRepresentation

: The ConnectApi product component group representation object to convert to ProductComponentGroupRepresentation.

  

## ProductComponentGroupRepresentation Properties

  
  
  
Contains properties to include details of a product component group used in bulk operations.

    
      

The `ProductComponentGroupRepresentation` class includes these
        properties.

    

    
  

- 
**[childGroups](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_childGroups)**  

Get the list of childgroup.

- 
**[classifications](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_ricpq_ProductComponentGroupR_classifications)**  

Get the list of product classifications.

- 
**[code](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_code)**  

Get the code of the productcomponentgroup.

- 
**[components](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_components)**  

Get the list of component.

- 
**[description](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_description)**  

Get the description of the productcomponentgroup.

- 
**[id](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_id)**  

Get the ID of the productcomponentgroup.

- 
**[name](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_name)**  

Get the name of the productcomponentgroup.

- 
**[parentGroupId](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_ricpq_ProductComponentGroupR_parentGroupId)**  

Get the ID of the parentgroup.

- 
**[parentProductId](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_ricpq_ProductComponentGroupR_parentProductId)**  

Get the ID of the parentproduct.

- 
**[sequence](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_runtime_industries_cpq_ProductComponentGroupRepresentation_sequence)**  

Get the sequence value.

### childGroups

Get the list of childgroup.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupRepresentation> childGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupRepresentation](#apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation)>

### classifications

Get the list of product classifications.

#### Signature

`public List<runtime_industries_cpq.ProductClassificationOutputRepresentation> classifications {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)>

### code

Get the code of the productcomponentgroup.

#### Signature

`public String code {get; set;}`

#### Property Value

Type: String

### components

Get the list of component.

#### Signature

`public List<runtime_industries_cpq.BulkProductDetailsRepresentation> components {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.BulkProductDetailsRepresentation](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation)>

### description

Get the description of the productcomponentgroup.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### id

Get the ID of the productcomponentgroup.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the productcomponentgroup.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### parentGroupId

Get the ID of the parentgroup.

#### Signature

`public String parentGroupId {get; set;}`

#### Property Value

Type: String

### parentProductId

Get the ID of the parentproduct.

#### Signature

`public String parentProductId {get; set;}`

#### Property Value

Type: String

### sequence

Get the sequence value.

#### Signature

`public Integer sequence {get; set;}`

#### Property Value

Type: Integer

=== ARTICLE: apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm
title: ProductDetailsRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductDetailsRepresentation Class

Get the details of a product definition.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductDetailsRepresentation Constructor](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_constructors)**  

Learn more about the constructor that's available with the ProductDetailsRepresentation     class.

- 
**[ProductDetailsRepresentation Properties](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_properties)**  

Learn more about the properties available with the ProductDetailsRepresentation     class.

  

## ProductDetailsRepresentation Constructor

  
  
  
Learn more about the constructor that's available with the ProductDetailsRepresentation
    class.

    
      

The `ProductDetailsRepresentation` class includes this
        constructor.

    

    
  

- 
**[ProductDetailsRepresentation()](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_ctor_2)**  

Constructor to get the product details for a product definition.

### ProductDetailsRepresentation()

Constructor to get the product details for a product definition.

#### Signature

`public ProductDetailsRepresentation()`

  

## ProductDetailsRepresentation Properties

  
  
  
Learn more about the properties available with the ProductDetailsRepresentation
    class.

    
      

The `ProductDetailsRepresentation` includes these
        properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_additionalFields)**  

Get the key-value pair of additional standard or custom fields with their     values.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_attributeCategories)**  

Get the list of categorized attributes related to the product.

- 
**[attributes](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_attributes)**  

Get the list of uncategorized attributes related to the product.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_availabilityDate)**  

Get the date when the part is used in the product or is made available for     sale.

- 
**[catalogs](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_catalogs)**  

Get the list of the associated catalogs returned with the Product List API (POST)     response. The Product By ID API (GET) returns an empty catalog list in the response. Returns the     name and id values only.

- 
**[childProducts](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_childProducts)**  

Get the hierarchy of the child products.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_configureDuringSale)**  

Determines whether to allow or prevent configuration when a bundle is sold.

- 
**[description](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_description)**  

Get the description of the product.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_discontinuedDate)**  

Get the date from when the part can’t be used in the product or sold.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_displayUrl)**  

Get the display image URL of the product.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_endOfLifeDate)**  

Get the date after which a product isn’t supported, ordered, or maintained.

- 
**[id](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_id)**  

Get the ID of the product.

- 
**[isActive](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_isActive)**  

Indicates whether the product is active (true) or not (false).

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_isAssetizable)**  

Indicates whether the product instance remains a customer asset after it's purchased     (true) or not (false).

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_isComponentRequired)**  

Indicates whether the product component is required (true) or not (false).

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_isDefaultComponent)**  

Indicates whether the product component is the default component (true) or not     (false).

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_isQuantityEditable)**  

Indicates whether the product quantity is editable (true) or not (false).

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_isSoldOnlyWithOtherProds)**  

Indicates whether the product can't be sold separately (true) or not (false).

- 
**[name](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_name)**  

Get the name of the product.

- 
**[nodeType](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_nodeType)**  

Get the type of the node, such as a product or bundled product.

- 
**[prices](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_prices)**  

Get the price details associated with the products.

- 
**[productClassification](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productClassification)**  

Get the details of the product classification that the product is based on.

- 
**[productCode](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_productCode)**  

Get the universal product code that's used to track the part that’s used in the     product.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productComponentGroups)**  

Get the logical grouping of the component products in a bundle and the group cardinality     for ordering the product components.

- 
**[productInformation](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_productInformation)**  

Get the details of a product.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productPricingInformation)**  

Get the pricing details of a product.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_productQuantity)**  

Get the quantity of a product.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productRelatedComponent)**  

Get the details of the related components of a product.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productSellingModelOptions)**  

Get the details of the product selling model options.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_productSpecificationType)**  

Get the details of the product specification type.

- 
**[productType](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_productType)**  

Get the product type.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_ricpq_ProductDetailsR_qualificationContext)**  

Get the context details of a user, which are used for qualification rules.

- 
**[status](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_status)**  

Get or set the status of the product, such as Active or Inactive.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_runtime_industries_cpq_ProductDetailsRepresentation_unitOfMeasure)**  

Get details about the unit of measure for a specific set of records.

### additionalFields

Get the key-value pair of additional standard or custom fields with their
    values.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get the list of categorized attributes related to the product.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributeCategoryOutputRepresentation](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)>

### attributes

Get the list of uncategorized attributes related to the product.

#### Signature

`public List<runtime_industries_cpq.ProductAttributeOutputRepresentation> attributes {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductAttributeOutputRepresentation](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation)>

### availabilityDate

Get the date when the part is used in the product or is made available for
    sale.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get the list of the associated catalogs returned with the Product List API (POST)
    response. The Product By ID API (GET) returns an empty catalog list in the response. Returns the
    name and id values only.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)>

### childProducts

Get the hierarchy of the child products.

#### Signature

`public List<runtime_industries_cpq.ProductDetailsRepresentation> childProducts {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductDetailsRepresentation](#apex_class_runtime_industries_cpq_ProductDetailsRepresentation)>

### configureDuringSale

Determines whether to allow or prevent configuration when a bundle is sold.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get the description of the product.

    
      

If data translation is set up and specified in the org, the translated description is
        available.

    

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get the date from when the part can’t be used in the product or sold.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get the display image URL of the product.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get the date after which a product isn’t supported, ordered, or maintained.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### id

Get the ID of the product.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isActive

Indicates whether the product is active (true) or not (false).

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Indicates whether the product instance remains a customer asset after it's purchased
    (true) or not (false).

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Indicates whether the product component is required (true) or not (false).

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Indicates whether the product component is the default component (true) or not
    (false).

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Indicates whether the product quantity is editable (true) or not (false).

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Indicates whether the product can't be sold separately (true) or not (false).

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the product.

    
      

If data translation is set up and specified in the org, the translated name is
        available.

    

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get the type of the node, such as a product or bundled product.

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### prices

Get the price details associated with the products.

#### Signature

`public List<runtime_industries_cpq.ProductPricesOutputRepresentation> prices {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductPricesOutputRepresentation](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation)>

### productClassification

Get the details of the product classification that the product is based on.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)

### productCode

Get the universal product code that's used to track the part that’s used in the
    product.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get the logical grouping of the component products in a bundle and the group cardinality
    for ordering the product components.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupOutputRepresentation](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)>

### productInformation

Get the details of a product.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get the pricing details of a product.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get the quantity of a product.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductQuantityOutputRepresentation](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)

### productRelatedComponent

Get the details of the related components of a product.

#### Signature

`public ConnectApi.CPQProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: ConnectApi.CPQProductRelatedComponentOutputRepresentation

### productSellingModelOptions

Get the details of the product selling model options.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)>

### productSpecificationType

Get the details of the product specification type.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)

### productType

Get the product type.

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the context details of a user, which are used for qualification rules.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### status

Get or set the status of the product, such as Active or Inactive.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get details about the unit of measure for a specific set of records.

#### Signature

`public ConnectApi.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: ConnectApi.UnitOfMeasureOutputRepresentation

=== ARTICLE: apex_class_runtime_industries_cpq_ProductListRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductListRepresentation.htm
title: ProductListRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductListRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductListRepresentation Class

Get the list of retrieved products.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductListRepresentation Properties](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_properties)**  

Learn more about the properties available with the ProductListRepresentation     class.

  

## ProductListRepresentation Properties

  
  
  
Learn more about the properties available with the ProductListRepresentation
    class.

    
      

The following are properties for `ProductListRepresentation`.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_additionalFields)**  

Get the key-value pair of additional standard or custom fields with their     values.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_attributeCategories)**  

Get the list of categorized attributes related to the product.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_availabilityDate)**  

Get the date when the part is used in the product or is made available for     sale.

- 
**[catalogs](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_catalogs)**  

Get the list of associated catalogs. Returns the name and id values only.

- 
**[categories](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_categories)**  

Get the list of associated categories. Returns the name and id values only.

- 
**[childProducts](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_childProducts)**  

Get the hierarchy of the child products.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_configureDuringSale)**  

Determines whether to allow or prevent configuration when a bundle is sold.

- 
**[description](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_description)**  

Get the description of the product. If data translation is set up and specified in the     org, the translated description is available.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_discontinuedDate)**  

Get the date from when the part can’t be used in the product or sold.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_displayUrl)**  

Get the display image URL of the product.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_endOfLifeDate)**  

Get the date after which a product isn’t supported, ordered, or maintained.

- 
**[id](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_id)**  

Get the ID of the product.

- 
**[isActive](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_isActive)**  

Indicates whether the product is active (true) or not (false).

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_isAssetizable)**  

Indicates whether the product instance remains a customer asset after it's purchased     (true) or not (false).

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_isComponentRequired)**  

Indicates whether the product component is required (true) or not (false).

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_isDefaultComponent)**  

Indicates whether the product component is the default component (true) or not     (false).

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_isQuantityEditable)**  

Indicates whether the product quantity is editable (true) or not (false).

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_ricpq_ProductListR_isSoldOnlyWithOtherProds)**  

Indicates whether the product can't be sold separately (true) or not (false).

- 
**[name](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_name)**  

Get the name of the product. If data translation is set up and specified in the org, the     translated name is available.

- 
**[nodeType](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_nodeType)**  

Get the type of the node, such as a product or bundled product.

- 
**[prices](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_prices)**  

Get the price details associated with the products.

- 
**[productClassification](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productClassification)**  

Get the details of the product classification that the product is based on.

- 
**[productCode](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productCode)**  

Get the universal product code that's used to track the part that’s used in the     product.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productComponentGroups)**  

Get the logical grouping of the component products in a bundle and group cardinality for     ordering the product components.

- 
**[productInformation](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productInformation)**  

Get the details of a product.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_ricpq_ProductListR_productPricingInformation)**  

Get the pricing details of a product.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productQuantity)**  

Get the quantity of a product.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_ricpq_ProductListR_productRelatedComponent)**  

Get the details of the related components of a product.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_ricpq_ProductListR_productSellingModelOptions)**  

Get the details of the product selling model options.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_ricpq_ProductListR_productSpecificationType)**  

Get the details of the product specification type.

- 
**[productType](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_productType)**  

Get the product type.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_qualificationContext)**  

Get the context details of a user, which are used for qualification rules.

- 
**[status](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_status)**  

Get or set the status of the product, such as Active or Inactive.

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_runtime_industries_cpq_ProductListRepresentation_unitOfMeasure)**  

Get details about the unit of measure for a specific set of records.

### additionalFields

Get the key-value pair of additional standard or custom fields with their
    values.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get the list of categorized attributes related to the product.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributeCategoryOutputRepresentation](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)>

### availabilityDate

Get the date when the part is used in the product or is made available for
    sale.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get the list of associated catalogs. Returns the name and id values only.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)>

### categories

Get the list of associated categories. Returns the name and id values only.

#### Signature

`public List<runtime_industries_cpq.CategoryOutputRepresentation> categories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CategoryOutputRepresentation](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CategoryOutputRepresentation)>

### childProducts

Get the hierarchy of the child products.

#### Signature

`public List<runtime_industries_cpq.ProductListRepresentation> childProducts {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductListRepresentation](#apex_class_runtime_industries_cpq_ProductListRepresentation)>

### configureDuringSale

Determines whether to allow or prevent configuration when a bundle is sold.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get the description of the product. If data translation is set up and specified in the
    org, the translated description is available.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get the date from when the part can’t be used in the product or sold.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get the display image URL of the product.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get the date after which a product isn’t supported, ordered, or maintained.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### id

Get the ID of the product.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isActive

Indicates whether the product is active (true) or not (false).

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Indicates whether the product instance remains a customer asset after it's purchased
    (true) or not (false).

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Indicates whether the product component is required (true) or not (false).

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Indicates whether the product component is the default component (true) or not
    (false).

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Indicates whether the product quantity is editable (true) or not (false).

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Indicates whether the product can't be sold separately (true) or not (false).

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the product. If data translation is set up and specified in the org, the
    translated name is available.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get the type of the node, such as a product or bundled product.

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### prices

Get the price details associated with the products.

#### Signature

`public List<runtime_industries_cpq.ProductPricesOutputRepresentation> prices {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductPricesOutputRepresentation](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation)>

### productClassification

Get the details of the product classification that the product is based on.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)

### productCode

Get the universal product code that's used to track the part that’s used in the
    product.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get the logical grouping of the component products in a bundle and group cardinality for
    ordering the product components.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupOutputRepresentation](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)>

### productInformation

Get the details of a product.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get the pricing details of a product.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get the quantity of a product.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductQuantityOutputRepresentation](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)

### productRelatedComponent

Get the details of the related components of a product.

#### Signature

`public ConnectApi.CPQProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: ConnectApi.CPQProductRelatedComponentOutputRepresentation

### productSellingModelOptions

Get the details of the product selling model options.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)>

### productSpecificationType

Get the details of the product specification type.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)

### productType

Get the product type.

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the context details of a user, which are used for qualification rules.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### status

Get or set the status of the product, such as Active or Inactive.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get details about the unit of measure for a specific set of records.

#### Signature

`public ConnectApi.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: ConnectApi.UnitOfMeasureOutputRepresentation

=== ARTICLE: apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm
title: ProductOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductOutputRepresentation Class

Get the details of a product definition.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_properties)**  

Learn more about the properties available with the ProductOutputRepresentation     class.

  

## ProductOutputRepresentation Properties

  
  
  
Learn more about the properties available with the ProductOutputRepresentation
    class.

    
      

The `ProductOutputRepresentation` class includes these
        properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_additionalFields)**  

Get the key-value pair of additional standard or custom fields with their     values.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_attributeCategories)**  

Get the list of categorized attributes related to the product.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_availabilityDate)**  

Get the date when the part is used in the product or is made available for     sale.

- 
**[catalogs](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_catalogs)**  

Get the list of associated catalogs. Returns the name and id values only.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_configureDuringSale)**  

Determines whether to allow or prevent configuration when a bundle is sold.

- 
**[description](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_description)**  

Get the description of the product. If data translation is set up and specified in the     org, the translated description is available.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_discontinuedDate)**  

Get the date from when the part can’t be used in the product or sold.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_displayUrl)**  

Get the display image URL of the product.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_endOfLifeDate)**  

Get the date after which a product isn’t supported, ordered, or maintained.

- 
**[id](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_id)**  

Get the ID of the product.

- 
**[isActive](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_isActive)**  

Indicates whether the product is active (true) or not (false).

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_isAssetizable)**  

Indicates whether the product instance remains a customer asset after it's purchased     (true) or not (false).

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_isComponentRequired)**  

Indicates whether the product component is required (true) or not (false).

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_isDefaultComponent)**  

Indicates whether the product component is the default component (true) or not     (false).

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_isQuantityEditable)**  

Indicates whether the product quantity is editable (true) or not (false).

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_isSoldOnlyWithOtherProds)**  

Indicates whether the product can't be sold separately (true) or not (false).

- 
**[name](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_name)**  

Get the name of the product. If data translation is set up and specified in the org, the     translated name is available.

- 
**[nodeType](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_nodeType)**  

Get the type of the node, such as a product or bundled product.

- 
**[productClassification](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productClassification)**  

Get the details of the product classification that the product is based on.

- 
**[productCode](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_productCode)**  

Get the universal product code that's used to track the part that’s used in the     product.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productComponentGroups)**  

Get the logical grouping of the component products in a bundle and group cardinality for     ordering the product components.

- 
**[productInformation](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_productInformation)**  

Get the details of a product.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productPricingInformation)**  

Get the pricing details of a product.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_productQuantity)**  

Get the quantity of a product.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productRelatedComponent)**  

Get the details of the related components of a product.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productSellingModelOptions)**  

Get the details of the product selling model options.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_ricpq_ProductOR_productSpecificationType)**  

Get the details of the product specification type.

- 
**[productType](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_productType)**  

Get the product type.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_qualificationContext)**  

Get the context details of a user, which are used for qualification rules.

- 
**[status](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductOutputRepresentation_status)**  

Get or set the status of the product, such as Active or Inactive.

### additionalFields

Get the key-value pair of additional standard or custom fields with their
    values.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get the list of categorized attributes related to the product.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.AttributeCategoryOutputRepresentation](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)>

### availabilityDate

Get the date when the part is used in the product or is made available for
    sale.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get the list of associated catalogs. Returns the name and id values only.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.CatalogOutputRepresentation](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)>

### configureDuringSale

Determines whether to allow or prevent configuration when a bundle is sold.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get the description of the product. If data translation is set up and specified in the
    org, the translated description is available.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get the date from when the part can’t be used in the product or sold.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get the display image URL of the product.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get the date after which a product isn’t supported, ordered, or maintained.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### id

Get the ID of the product.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isActive

Indicates whether the product is active (true) or not (false).

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Indicates whether the product instance remains a customer asset after it's purchased
    (true) or not (false).

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Indicates whether the product component is required (true) or not (false).

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Indicates whether the product component is the default component (true) or not
    (false).

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Indicates whether the product quantity is editable (true) or not (false).

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Indicates whether the product can't be sold separately (true) or not (false).

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get the name of the product. If data translation is set up and specified in the org, the
    translated name is available.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get the type of the node, such as a product or bundled product.

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### productClassification

Get the details of the product classification that the product is based on.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductClassificationOutputRepresentation](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)

### productCode

Get the universal product code that's used to track the part that’s used in the
    product.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get the logical grouping of the component products in a bundle and group cardinality for
    ordering the product components.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductComponentGroupOutputRepresentation](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)>

### productInformation

Get the details of a product.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get the pricing details of a product.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get the quantity of a product.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductQuantityOutputRepresentation](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)

### productRelatedComponent

Get the details of the related components of a product.

#### Signature

`public ConnectApi.CPQProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: ConnectApi.CPQProductRelatedComponentOutputRepresentation

### productSellingModelOptions

Get the details of the product selling model options.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<[runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)>

### productSpecificationType

Get the details of the product specification type.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)

### productType

Get the product type.

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get the context details of a user, which are used for qualification rules.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.QualificationContextOutputRepresentation](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)

### status

Get or set the status of the product, such as Active or Inactive.

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm
title: ProductPricesOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductPricesOutputRepresentation Class

Get the price details of a product.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductPricesOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_properties)**  

Learn more about the properties available with the ProductPricesOutputRepresentation     class.

  

## ProductPricesOutputRepresentation Properties

  
  
  
Learn more about the properties available with the ProductPricesOutputRepresentation
    class.

    
      

The following are properties for `ProductPricesOutputRepresentation`.

    

    
  

- 
**[currencyIsoCode](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_ricpq_ProductPricesOR_currencyIsoCode)**  

Get or set the ISO currency code for the price.

- 
**[effectiveFrom](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_effectiveFrom)**  

Get or set the date and time when this price becomes effective.

- 
**[effectiveTo](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_effectiveTo)**  

Get or set the date and time when this price expires.

- 
**[isDefault](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_isDefault)**  

Indicates whether this is the default price for the product.

- 
**[isDerived](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_isDerived)**  

Indicates whether this price is derived from another price.

- 
**[isSelected](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_isSelected)**  

Indicates whether this price is currently selected.

- 
**[price](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_price)**  

Get or set the price value for the product.

- 
**[priceBookEntryId](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_ricpq_ProductPricesOR_priceBookEntryId)**  

Get or set the ID of the price book entry.

- 
**[priceBookId](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_priceBookId)**  

Get or set the ID of the price book containing this price.

- 
**[pricingModel](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductPricesOutputRepresentation_pricingModel)**  

Get or set the pricing model associated with this price.

### currencyIsoCode

Get or set the ISO currency code for the price.

#### Signature

`public String currencyIsoCode {get; set;}`

#### Property Value

Type: String

### effectiveFrom

Get or set the date and time when this price becomes effective.

#### Signature

`public String effectiveFrom {get; set;}`

#### Property Value

Type: String

### effectiveTo

Get or set the date and time when this price expires.

#### Signature

`public String effectiveTo {get; set;}`

#### Property Value

Type: String

### isDefault

Indicates whether this is the default price for the product.

#### Signature

`public Boolean isDefault {get; set;}`

#### Property Value

Type: Boolean

### isDerived

Indicates whether this price is derived from another price.

#### Signature

`public Boolean isDerived {get; set;}`

#### Property Value

Type: Boolean

### isSelected

Indicates whether this price is currently selected.

#### Signature

`public Boolean isSelected {get; set;}`

#### Property Value

Type: Boolean

### price

Get or set the price value for the product.

#### Signature

`public Double price {get; set;}`

#### Property Value

Type: Double

### priceBookEntryId

Get or set the ID of the price book entry.

#### Signature

`public String priceBookEntryId {get; set;}`

#### Property Value

Type: String

### priceBookId

Get or set the ID of the price book containing this price.

#### Signature

`public String priceBookId {get; set;}`

#### Property Value

Type: String

### pricingModel

Get or set the pricing model associated with this price.

#### Signature

`public runtime_industries_cpq.PricingModelOutputRepresentation pricingModel {get; set;}`

#### Property Value

Type: [runtime_industries_cpq.PricingModelOutputRepresentation](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_PricingModelOutputRepresentation)

=== ARTICLE: apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm
title: ProductQuantityOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductQuantityOutputRepresentation Class

Represents the quantity constraints and current quantity for a product in the product discovery context.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductQuantityOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductQuantityOutputRepresentation_properties)**  

## ProductQuantityOutputRepresentation Properties

The following are properties for `ProductQuantityOutputRepresentation`.

- 
**[maxQuantity](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductQuantityOutputRepresentation_maxQuantity)**  

Get or set the maximum quantity allowed for the product.

- 
**[minQuantity](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductQuantityOutputRepresentation_minQuantity)**  

Get or set the minimum quantity allowed for the product.

- 
**[quantity](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductQuantityOutputRepresentation_quantity)**  

Get or set the current quantity of the product.

### maxQuantity

Get or set the maximum quantity allowed for the product.

#### Signature

`public Double maxQuantity {get; set;}`

#### Property Value

Type: Double

### minQuantity

Get or set the minimum quantity allowed for the product.

#### Signature

`public Double minQuantity {get; set;}`

#### Property Value

Type: Double

### quantity

Get or set the current quantity of the product.

#### Signature

`public Double quantity {get; set;}`

#### Property Value

Type: Double

=== ARTICLE: apex_class_runtime_industries_cpq_ProductRecommendationRule.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductRecommendationRule.htm
title: ProductRecommendationRule Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductRecommendationRule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductRecommendationRule Class

Represents a product recommendation rule that is evaluated during product configuration. Product recommendation rules suggest additional products to users based on configuration conditions.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductRecommendationRule Constructor](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_constructors)**  

Learn more about the constructor that's available with the ProductRecommendationRule     class.

- 
**[ProductRecommendationRule Properties](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_properties)**  

Contains properties to store product recommendation rule details from configuration rule evaluation.

  

## ProductRecommendationRule Constructor

  
  
  
Learn more about the constructor that's available with the ProductRecommendationRule
    class.

    
      

The `ProductRecommendationRule` class includes this
        constructor.

    

    
  

- 
**[ProductRecommendationRule(referenceId, productIds, message, recordType, target, scope)](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_ctor)**  

Constructor to create a ProductRecommendationRule instance with the specified recommendation details.

### ProductRecommendationRule(referenceId, productIds, message, recordType, target, scope)

Constructor to create a ProductRecommendationRule instance with the specified recommendation details.

#### Signature

`public ProductRecommendationRule(String referenceId, List<String> productIds, String message, String recordType, String target, String scope)`

#### Parameters

**referenceId**

: Type: String

: The reference ID of the product recommendation rule.

**productIds**

: Type: List<String>

: List of product IDs that are recommended.

**message**

: Type: String

: The message to display with the product recommendation.

**recordType**

: Type: String

: The record type associated with the recommendation.

**target**

: Type: String

: The target of the recommendation rule.

**scope**

: Type: String

: The scope of the recommendation rule.

  

## ProductRecommendationRule Properties

  
  
  
Contains properties to store product recommendation rule details from configuration rule evaluation.

    
      

The `ProductRecommendationRule` class includes these
        properties.

    

    
  

- 
**[message](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_message)**  

Get the message value.

- 
**[productIds](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_productIds)**  

Get the list of productid.

- 
**[recordType](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_recordType)**  

Get the recordtype value.

- 
**[referenceId](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_referenceId)**  

Get the ID of the reference.

- 
**[scope](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_scope)**  

Get the scope value.

- 
**[target](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_runtime_industries_cpq_ProductRecommendationRule_target)**  

Get the target value.

### message

Get the message value.

#### Signature

`public String message {get; set;}`

#### Property Value

Type: String

### productIds

Get the list of productid.

#### Signature

`public List<String> productIds {get; set;}`

#### Property Value

Type: List<String>

### recordType

Get the recordtype value.

#### Signature

`public String recordType {get; set;}`

#### Property Value

Type: String

### referenceId

Get the ID of the reference.

#### Signature

`public String referenceId {get; set;}`

#### Property Value

Type: String

### scope

Get the scope value.

#### Signature

`public String scope {get; set;}`

#### Property Value

Type: String

### target

Get the target value.

#### Signature

`public String target {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm
title: ProductSellingModelOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSellingModelOutputRepresentation Class

Represents a product selling model that defines how a product is sold, including the selling model type, pricing term, and status.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[ProductSellingModelOutputRepresentation Properties](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_ricpq_ProductSellingModelOR_properties)**  

Learn more about the properties available with the     ProductSellingModelOutputRepresentation class.

  

## ProductSellingModelOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    ProductSellingModelOutputRepresentation class.

    
      

The `ProductSellingModelOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[id](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductSellingModelOutputRepresentation_id)**  

Get or set the unique identifier of the product selling model.

- 
**[name](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductSellingModelOutputRepresentation_name)**  

Get or set the name of the product selling model.

- 
**[pricingTerm](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_ricpq_ProductSellingModelOR_pricingTerm)**  

Get or set the pricing term value, which represents the duration or quantity for the pricing term unit.

- 
**[pricingTermUnit](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_ricpq_ProductSellingModelOR_pricingTermUnit)**  

Get or set the unit for the pricing term, such as "Month", "Year", or "Day".

- 
**[sellingModelType](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_ricpq_ProductSellingModelOR_sellingModelType)**  

Get or set the type of selling model, such as "Subscription", "OneTime", or "Usage".

- 
**[status](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_runtime_industries_cpq_ProductSellingModelOutputRepresentation_status)**  

Get or set the status of the product selling model, such as "Active" or "Inactive".

### id

Get or set the unique identifier of the product selling model.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get or set the name of the product selling model.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### pricingTerm

Get or set the pricing term value, which represents the duration or quantity for the pricing term unit.

#### Signature

`public Integer pricingTerm {get; set;}`

#### Property Value

Type: Integer

### pricingTermUnit

Get or set the unit for the pricing term, such as "Month", "Year", or "Day".

#### Signature

`public String pricingTermUnit {get; set;}`

#### Property Value

Type: String

### sellingModelType

Get or set the type of selling model, such as "Subscription", "OneTime", or "Usage".

#### Signature

`public String sellingModelType {get; set;}`

#### Property Value

Type: String

### status

Get or set the status of the product selling model, such as "Active" or "Inactive".

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm
title: QocQualificationOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QocQualificationOutputRepresentation Class

Represents a quote, order, or contract qualification that determines whether a product
    can be sold based on specific business rules and conditions.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[QocQualificationOutputRepresentation Constructors](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_ricpq_QocQualificationOR_constructors)**  

- 
**[QocQualificationOutputRepresentation Properties](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_runtime_industries_cpq_QocQualificationOutputRepresentation_properties)**  

Learn more about the properties available with the QocQualificationOutputRepresentation     class.

## QocQualificationOutputRepresentation Constructors

The following are constructors for `QocQualificationOutputRepresentation`.

- 
**[QocQualificationOutputRepresentation()](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_runtime_industries_cpq_QocQualificationOutputRepresentation_ctor_2)**  

Constructs an empty QocQualificationOutputRepresentation instance.

### QocQualificationOutputRepresentation()

Constructs an empty QocQualificationOutputRepresentation instance.

#### Signature

`public QocQualificationOutputRepresentation()`

  

## QocQualificationOutputRepresentation Properties

  
  
  
Learn more about the properties available with the QocQualificationOutputRepresentation
    class.

    
      

The `QocQualificationOutputRepresentation` class includes
        these properties.

    

    
  

- 
**[productId](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_runtime_industries_cpq_QocQualificationOutputRepresentation_productId)**  

Get or set the identifier of the product being qualified.

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_ricpq_QocQualificationOR_qualificationContext)**  

Get or set the qualification context that contains the qualification result and reason.

### productId

Get or set the identifier of the product being qualified.

#### Signature

`public String productId {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get or set the qualification context that contains the qualification result and reason.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: runtime_industries_cpq.QualificationContextOutputRepresentation

=== ARTICLE: apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm
title: QualificationContextOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QualificationContextOutputRepresentation Class

Represents the context information used for product qualification, including account, opportunity, and other relevant context data for determining product eligibility.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[QualificationContextOutputRepresentation Properties](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_ricpq_QualificationContextOR_properties)**  

Learn more about the properties available with the     QualificationContextOutputRepresentation class.

  

## QualificationContextOutputRepresentation Properties

  
  
  
Learn more about the properties available with the
    QualificationContextOutputRepresentation class.

    
      

The `QualificationContextOutputRepresentation` class
        includes these properties.

    

    
  

- 
**[isQualified](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_ricpq_QualificationContextOR_isQualified)**  

Get or set whether the product is qualified based on the qualification rules.

- 
**[reason](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_runtime_industries_cpq_QualificationContextOutputRepresentation_reason)**  

Get or set the reason for the qualification result, explaining why the product is qualified or not qualified.

### isQualified

Get or set whether the product is qualified based on the qualification rules.

#### Signature

`public Boolean isQualified {get; set;}`

#### Property Value

Type: Boolean

### reason

Get or set the reason for the qualification result, explaining why the product is qualified or not qualified.

#### Signature

`public String reason {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_RelatedObjectFilter.htm ===
---
page_id: apex_class_runtime_industries_cpq_RelatedObjectFilter.htm
title: RelatedObjectFilter Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_RelatedObjectFilter.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RelatedObjectFilter Class

Represents a filter for related objects used in product search and discovery, allowing you to filter products based on related object criteria.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[RelatedObjectFilter Properties](./apex_class_runtime_industries_cpq_RelatedObjectFilter.htm.md#apex_runtime_industries_cpq_RelatedObjectFilter_properties)**  

Learn more about the properties available with the RelatedObjectFilter     class.

  

## RelatedObjectFilter Properties

  
  
  
Learn more about the properties available with the RelatedObjectFilter
    class.

    
      

The `RelatedObjectFilter` class includes these
        properties.

    

    
  

- 
**[criteria](./apex_class_runtime_industries_cpq_RelatedObjectFilter.htm.md#apex_runtime_industries_cpq_RelatedObjectFilter_criteria)**  

Get or set the list of filter criteria to apply to the related object.

- 
**[objectName](./apex_class_runtime_industries_cpq_RelatedObjectFilter.htm.md#apex_runtime_industries_cpq_RelatedObjectFilter_objectName)**  

Get or set the name of the related object to filter by, such as "Account" or "Opportunity".

### criteria

Get or set the list of filter criteria to apply to the related object.

#### Signature

`public List<runtime_industries_cpq.FilterCriteriaInputRepresentation> criteria {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.FilterCriteriaInputRepresentation>

### objectName

Get or set the name of the related object to filter by, such as "Account" or "Opportunity".

#### Signature

`public String objectName {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm
title: RelatedObjectFilterInputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RelatedObjectFilterInputRepresentation Class

Represents input criteria for filtering products based on related object information, such as account, opportunity, or contract data.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[RelatedObjectFilterInputRepresentation Properties](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md#apex_ricpq_RelatedObjectFilterIR_properties)**  

Learn more about the properties available with the     RelatedObjectFilterInputRepresentation

  

## RelatedObjectFilterInputRepresentation Properties

  
  
  
Learn more about the properties available with the
    RelatedObjectFilterInputRepresentation

    
      

The `RelatedObjectFilterInputRepresentation` class
        includes these properties.

    

    
  

- 
**[relatedObjectFilter](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md#apex_ricpq_RelatedObjectFilterIR_relatedObjectFilter)**  

Get or set the list of related object filters to apply when searching for products.

### relatedObjectFilter

Get or set the list of related object filters to apply when searching for products.

#### Signature

`public List<runtime_industries_cpq.RelatedObjectFilter> relatedObjectFilter {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.RelatedObjectFilter>

=== ARTICLE: apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm
title: SearchProductsFacetRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SearchProductsFacetRepresentation Class

Represents a search facet that provides filtering and categorization options for product search results, such as categories, attributes, or other product characteristics.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[SearchProductsFacetRepresentation Properties](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_properties)**  

Learn more about the properties available with the SearchProductsFacetRepresentation     class.

  

## SearchProductsFacetRepresentation Properties

  
  
  
Learn more about the properties available with the SearchProductsFacetRepresentation
    class.

    
      

The `SearchProductsFacetRepresentation` class includes
        these properties.

    

    
  

- 
**[attributeType](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_attributeType)**  

Get or set the type of attribute this facet represents, such as "Picklist" or "Text".

- 
**[displayName](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_displayName)**  

Get or set the display name of the search facet.

- 
**[displayRank](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_displayRank)**  

Get or set the display rank that determines the order in which this facet appears in search results.

- 
**[nameOrId](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_nameOrId)**  

Get or set the name or identifier of the attribute or category that this facet represents.

- 
**[values](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsFacetRepresentation_values)**  

Get or set the list of facet values available for filtering, each representing a distinct option within this facet.

### attributeType

Get or set the type of attribute this facet represents, such as "Picklist" or "Text".

#### Signature

`public String attributeType {get; set;}`

#### Property Value

Type: String

### displayName

Get or set the display name of the search facet.

#### Signature

`public String displayName {get; set;}`

#### Property Value

Type: String

### displayRank

Get or set the display rank that determines the order in which this facet appears in search results.

#### Signature

`public Integer displayRank {get; set;}`

#### Property Value

Type: Integer

### nameOrId

Get or set the name or identifier of the attribute or category that this facet represents.

#### Signature

`public String nameOrId {get; set;}`

#### Property Value

Type: String

### values

Get or set the list of facet values available for filtering, each representing a distinct option within this facet.

#### Signature

`public List<runtime_industries_cpq.FacetValueRepresentation> values {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.FacetValueRepresentation>

=== ARTICLE: apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm
title: SearchProductsRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SearchProductsRepresentation Class

Represents the results of a product search operation, including the list of products, search facets, pagination information, and total count of matching products.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[SearchProductsRepresentation Properties](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_properties)**  

Learn more about the properties available with the SearchProductsRepresentation     class.

  

## SearchProductsRepresentation Properties

  
  
  
Learn more about the properties available with the SearchProductsRepresentation
    class.

    
      

The `SearchProductsRepresentation` class includes these
        properties.

    

    
  

- 
**[additionalFields](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_additionalFields)**  

Get or set additional custom fields for the product in the search results.

- 
**[attributeCategories](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_attributeCategories)**  

Get or set the list of attribute categories that contain product attributes for configuration.

- 
**[availabilityDate](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_availabilityDate)**  

Get or set the date when the product becomes available for sale.

- 
**[catalogs](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_catalogs)**  

Get or set the list of catalogs that this product belongs to.

- 
**[configureDuringSale](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_configureDuringSale)**  

Get or set whether the product can be configured during the sales process.

- 
**[description](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_description)**  

Get or set the description of the product in the search results. If data translation is set up and specified in the org, the translated description is available.

- 
**[discontinuedDate](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_discontinuedDate)**  

Get or set the date when the product was discontinued.

- 
**[displayUrl](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_displayUrl)**  

Get or set the URL to display additional information about the product.

- 
**[endOfLifeDate](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_endOfLifeDate)**  

Get or set the end of life date for the product.

- 
**[id](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_id)**  

Get or set the ID of the product in the search results.

- 
**[isActive](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_isActive)**  

Get or set whether the product is active (true) or not (false) in the search results.

- 
**[isAssetizable](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_isAssetizable)**  

Get or set whether the product can be converted to an asset after sale.

- 
**[isComponentRequired](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_isComponentRequired)**  

Get or set whether this component is required in a bundle or product relationship.

- 
**[isDefaultComponent](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_isDefaultComponent)**  

Get or set whether this component is selected by default in a bundle or product relationship.

- 
**[isQuantityEditable](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_isQuantityEditable)**  

Get or set whether the quantity of this product can be edited.

- 
**[isSoldOnlyWithOtherProds](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_isSoldOnlyWithOtherProds)**  

Get or set whether this product can only be sold with other products.

- 
**[name](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_name)**  

Get or set the name of the product in the search results. If data translation is set up and specified in the org, the translated name is available.

- 
**[nodeType](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_nodeType)**  

Get or set the node type of the product, such as "Product" or "Bundle".

- 
**[prices](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_prices)**  

Get or set the list of prices available for this product.

- 
**[productClassification](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productClassification)**  

Get or set the product classification information for this product.

- 
**[productCode](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_productCode)**  

Get or set the universal product code that's used to track the part that's used in the product.

- 
**[productComponentGroups](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productComponentGroups)**  

Get or set the list of product component groups that organize related components.

- 
**[productInformation](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_productInformation)**  

Get or set additional product information details.

- 
**[productPricingInformation](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productPricingInformation)**  

Get or set the pricing information for this product, including price lists and pricing models.

- 
**[productQuantity](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_productQuantity)**  

Get or set the quantity constraints and current quantity for this product.

- 
**[productRelatedComponent](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productRelatedComponent)**  

Get or set the related component information for this product in bundle or product relationships.

- 
**[productSellingModelOptions](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productSellingModelOptions)**  

Get or set the list of selling model options available for this product.

- 
**[productSpecificationType](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_productSpecificationType)**  

Get or set the product specification type that defines the structure and attributes for configuring this product.

- 
**[productType](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_productType)**  

Get or set the type of product, such as "Product", "Service", or "Bundle".

- 
**[qualificationContext](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_ricpq_SearchProductsR_qualificationContext)**  

Get or set the qualification context that contains the qualification result and reason for this product.

- 
**[status](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_status)**  

Get or set the status of the product, such as "Active" or "Inactive".

- 
**[unitOfMeasure](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_runtime_industries_cpq_SearchProductsRepresentation_unitOfMeasure)**  

Get or set the unit of measure for the quantity of this product.

### additionalFields

Get or set additional custom fields for the product in the search results.

#### Signature

`public List<runtime_industries_cpq.AdditionalFieldsWrapper> additionalFields {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AdditionalFieldsWrapper>

### attributeCategories

Get or set the list of attribute categories that contain product attributes for configuration.

#### Signature

`public List<runtime_industries_cpq.AttributeCategoryOutputRepresentation> attributeCategories {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.AttributeCategoryOutputRepresentation>

### availabilityDate

Get or set the date when the product becomes available for sale.

#### Signature

`public Datetime availabilityDate {get; set;}`

#### Property Value

Type: Datetime

### catalogs

Get or set the list of catalogs that this product belongs to.

#### Signature

`public List<runtime_industries_cpq.CatalogOutputRepresentation> catalogs {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.CatalogOutputRepresentation>

### configureDuringSale

Get or set whether the product can be configured during the sales process.

#### Signature

`public String configureDuringSale {get; set;}`

#### Property Value

Type: String

### description

Get or set the description of the product in the search results. If data translation is set up and specified in the org, the translated description is available.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### discontinuedDate

Get or set the date when the product was discontinued.

#### Signature

`public Datetime discontinuedDate {get; set;}`

#### Property Value

Type: Datetime

### displayUrl

Get or set the URL to display additional information about the product.

#### Signature

`public String displayUrl {get; set;}`

#### Property Value

Type: String

### endOfLifeDate

Get or set the end of life date for the product.

#### Signature

`public Datetime endOfLifeDate {get; set;}`

#### Property Value

Type: Datetime

### id

Get or set the ID of the product in the search results.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### isActive

Get or set whether the product is active (true) or not (false) in the search results.

#### Signature

`public Boolean isActive {get; set;}`

#### Property Value

Type: Boolean

### isAssetizable

Get or set whether the product can be converted to an asset after sale.

#### Signature

`public Boolean isAssetizable {get; set;}`

#### Property Value

Type: Boolean

### isComponentRequired

Get or set whether this component is required in a bundle or product relationship.

#### Signature

`public Boolean isComponentRequired {get; set;}`

#### Property Value

Type: Boolean

### isDefaultComponent

Get or set whether this component is selected by default in a bundle or product relationship.

#### Signature

`public Boolean isDefaultComponent {get; set;}`

#### Property Value

Type: Boolean

### isQuantityEditable

Get or set whether the quantity of this product can be edited.

#### Signature

`public Boolean isQuantityEditable {get; set;}`

#### Property Value

Type: Boolean

### isSoldOnlyWithOtherProds

Get or set whether this product can only be sold with other products.

#### Signature

`public Boolean isSoldOnlyWithOtherProds {get; set;}`

#### Property Value

Type: Boolean

### name

Get or set the name of the product in the search results. If data translation is set up and specified in the org, the translated name is available.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### nodeType

Get or set the node type of the product, such as "Product" or "Bundle".

#### Signature

`public String nodeType {get; set;}`

#### Property Value

Type: String

### prices

Get or set the list of prices available for this product.

#### Signature

`public List<runtime_industries_cpq.ProductPricesOutputRepresentation> prices {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.ProductPricesOutputRepresentation>

### productClassification

Get or set the product classification information for this product.

#### Signature

`public runtime_industries_cpq.ProductClassificationOutputRepresentation productClassification {get; set;}`

#### Property Value

Type: runtime_industries_cpq.ProductClassificationOutputRepresentation

### productCode

Get or set the universal product code that's used to track the part that's used in the product.

#### Signature

`public String productCode {get; set;}`

#### Property Value

Type: String

### productComponentGroups

Get or set the list of product component groups that organize related components.

#### Signature

`public List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation> productComponentGroups {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.ProductComponentGroupOutputRepresentation>

### productInformation

Get or set additional product information details.

#### Signature

`public String productInformation {get; set;}`

#### Property Value

Type: String

### productPricingInformation

Get or set the pricing information for this product, including price lists and pricing models.

#### Signature

`public String productPricingInformation {get; set;}`

#### Property Value

Type: String

### productQuantity

Get or set the quantity constraints and current quantity for this product.

#### Signature

`public runtime_industries_cpq.ProductQuantityOutputRepresentation productQuantity {get; set;}`

#### Property Value

Type: runtime_industries_cpq.ProductQuantityOutputRepresentation

### productRelatedComponent

Get or set the related component information for this product in bundle or product relationships.

#### Signature

`public ConnectApi.CPQProductRelatedComponentOutputRepresentation productRelatedComponent {get; set;}`

#### Property Value

Type: ConnectApi.CPQProductRelatedComponentOutputRepresentation

### productSellingModelOptions

Get or set the list of selling model options available for this product.

#### Signature

`public List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation> productSellingModelOptions {get; set;}`

#### Property Value

Type: List<runtime_industries_cpq.ProductSellingModelOptionOutputRepresentation>

### productSpecificationType

Get or set the product specification type that defines the structure and attributes for configuring this product.

#### Signature

`public runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation productSpecificationType {get; set;}`

#### Property Value

Type: runtime_industries_cpq.ProductSpecificationTypeOutputRepresentation

### productType

Get or set the type of product, such as "Product", "Service", or "Bundle".

#### Signature

`public String productType {get; set;}`

#### Property Value

Type: String

### qualificationContext

Get or set the qualification context that contains the qualification result and reason for this product.

#### Signature

`public runtime_industries_cpq.QualificationContextOutputRepresentation qualificationContext {get; set;}`

#### Property Value

Type: runtime_industries_cpq.QualificationContextOutputRepresentation

### status

Get or set the status of the product, such as "Active" or "Inactive".

#### Signature

`public String status {get; set;}`

#### Property Value

Type: String

### unitOfMeasure

Get or set the unit of measure for the quantity of this product.

#### Signature

`public ConnectApi.UnitOfMeasureOutputRepresentation unitOfMeasure {get; set;}`

#### Property Value

Type: ConnectApi.UnitOfMeasureOutputRepresentation

=== ARTICLE: apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm ===
---
page_id: apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm
title: UnitOfMeasureOutputRepresentation Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# UnitOfMeasureOutputRepresentation Class

Represents the unit of measure for a product. This class contains information about how product quantities are measured, including the unit code, name, scale, and rounding method.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[UnitOfMeasureOutputRepresentation Constructor](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_constructors)**  

Learn more about the constructor that's available with the UnitOfMeasureOutputRepresentation     class.

- 
**[UnitOfMeasureOutputRepresentation Properties](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_properties)**  

Contains properties to include unit of measure details for products.

  

## UnitOfMeasureOutputRepresentation Constructor

  
  
  
Learn more about the constructor that's available with the UnitOfMeasureOutputRepresentation
    class.

    
      

The `UnitOfMeasureOutputRepresentation` class includes this
        constructor.

    

    
  

- 
**[UnitOfMeasureOutputRepresentation(apexObj)](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_ctor)**  

Constructor to create a UnitOfMeasureOutputRepresentation instance from a ConnectApi UnitOfMeasureOutputRepresentation object.

### UnitOfMeasureOutputRepresentation(apexObj)

Constructor to create a UnitOfMeasureOutputRepresentation instance from a ConnectApi UnitOfMeasureOutputRepresentation object.

#### Signature

`public UnitOfMeasureOutputRepresentation(ConnectApi.UnitOfMeasureOutputRepresentation apexObj)`

#### Parameters

**apexObj**

: Type: ConnectApi.UnitOfMeasureOutputRepresentation

: The ConnectApi unit of measure representation object to convert to UnitOfMeasureOutputRepresentation.

  

## UnitOfMeasureOutputRepresentation Properties

  
  
  
Contains properties to include unit of measure details for products.

    
      

The `UnitOfMeasureOutputRepresentation` class includes these
        properties.

    

    
  

- 
**[id](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_id)**  

Get the ID of the unitofmeasure.

- 
**[name](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_name)**  

Get the name of the unitofmeasure.

- 
**[roundingMethod](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_roundingMethod)**  

Get the roundingmethod value.

- 
**[scale](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_scale)**  

Get the scale value.

- 
**[unitCode](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_runtime_industries_cpq_UnitOfMeasureOutputRepresentation_unitCode)**  

Get the unitcode value.

### id

Get the ID of the unitofmeasure.

#### Signature

`public String id {get; set;}`

#### Property Value

Type: String

### name

Get the name of the unitofmeasure.

#### Signature

`public String name {get; set;}`

#### Property Value

Type: String

### roundingMethod

Get the roundingmethod value.

#### Signature

`public String roundingMethod {get; set;}`

#### Property Value

Type: String

### scale

Get the scale value.

#### Signature

`public Integer scale {get; set;}`

#### Property Value

Type: Integer

### unitCode

Get the unitcode value.

#### Signature

`public String unitCode {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_runtime_industries_cpq_VisibilityRule.htm ===
---
page_id: apex_class_runtime_industries_cpq_VisibilityRule.htm
title: VisibilityRule Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_runtime_industries_cpq_VisibilityRule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: apex_namespace_runtime_industries_cpq.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# VisibilityRule Class

Represents a visibility rule that is evaluated during product configuration. Visibility rules control the visibility of products, attributes, or other UI elements based on configuration conditions.

## Namespace

[runtime_industries_cpq](./apex_namespace_runtime_industries_cpq.htm.md)

- 
**[VisibilityRule Constructor](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_constructors)**  

Learn more about the constructor that's available with the VisibilityRule     class.

- 
**[VisibilityRule Properties](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_properties)**  

Contains properties to store visibility rule details from configuration rule evaluation.

  

## VisibilityRule Constructor

  
  
  
Learn more about the constructor that's available with the VisibilityRule
    class.

    
      

The `VisibilityRule` class includes this
        constructor.

    

    
  

- 
**[VisibilityRule(stiId, prcId, attributeId, attributePicklistValueId, target, scope, type, productIds, message)](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_ctor)**  

Constructor to create a VisibilityRule instance with the specified visibility rule details.

### VisibilityRule(stiId, prcId, attributeId, attributePicklistValueId, target, scope, type, productIds, message)

Constructor to create a VisibilityRule instance with the specified visibility rule details.

#### Signature

`public VisibilityRule(String stiId, String prcId, String attributeId, String attributePicklistValueId, String target, String scope, String type, List<String> productIds, String message)`

#### Parameters

**stiId**

: Type: String

: The ID of the Sales Transaction Item (STI) associated with this visibility rule.

**prcId**

: Type: String

: The ID of the Product Relationship Configuration (PRC) associated with this visibility rule.

**attributeId**

: Type: String

: The ID of the attribute associated with this visibility rule.

**attributePicklistValueId**

: Type: String

: The ID of the attribute picklist value associated with this visibility rule.

**target**

: Type: String

: The target of the visibility rule (for example, product, attribute, or component).

**scope**

: Type: String

: The scope of the visibility rule.

**type**

: Type: String

: The type of visibility rule (for example, Show or Hide).

**productIds**

: Type: List<String>

: List of product IDs affected by this visibility rule.

**message**

: Type: String

: The message to display when the visibility rule is applied.

  

## VisibilityRule Properties

  
  
  
Contains properties to store visibility rule details from configuration rule evaluation.

    
      

The `VisibilityRule` class includes these
        properties.

    

    
  

- 
**[attributeId](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_attributeId)**  

Get the ID of the attribute.

- 
**[attributePicklistValueId](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_attributePicklistValueId)**  

Get the ID of the attributepicklistvalue.

- 
**[message](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_message)**  

Get the message value.

- 
**[prcId](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_prcId)**  

Get the ID of the prc.

- 
**[productId](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_productId)**  

Get the ID of the product.

- 
**[scope](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_scope)**  

Get the scope value.

- 
**[stiId](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_stiId)**  

Get the ID of the sti.

- 
**[target](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_target)**  

Get the target value.

- 
**[type](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_runtime_industries_cpq_VisibilityRule_type)**  

Get the type value.

### attributeId

Get the ID of the attribute.

#### Signature

`public String attributeId {get; set;}`

#### Property Value

Type: String

### attributePicklistValueId

Get the ID of the attributepicklistvalue.

#### Signature

`public String attributePicklistValueId {get; set;}`

#### Property Value

Type: String

### message

Get the message value.

#### Signature

`public String message {get; set;}`

#### Property Value

Type: String

### prcId

Get the ID of the prc.

#### Signature

`public String prcId {get; set;}`

#### Property Value

Type: String

### productId

Get the ID of the product.

#### Signature

`public List<String> productId {get; set;}`

#### Property Value

Type: List<String>

### scope

Get the scope value.

#### Signature

`public String scope {get; set;}`

#### Property Value

Type: String

### stiId

Get the ID of the sti.

#### Signature

`public String stiId {get; set;}`

#### Property Value

Type: String

### target

Get the target value.

#### Signature

`public String target {get; set;}`

#### Property Value

Type: String

### type

Get the type value.

#### Signature

`public String type {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_namespace_runtime_industries_cpq.htm ===
---
page_id: apex_namespace_runtime_industries_cpq.htm
title: runtime_industries_cpq Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_runtime_industries_cpq.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# runtime_industries_cpq Namespace

The runtime_industries_cpq namespace provides classes and methods to search products or
    to manage products, catalogs, and categories.

The `runtime_industries_cpq` namespace includes these
        classes.

    

## Usage

      
      

You can access the `runtime_industries_cpq` classes if
        your org has the Product Discovery feature.

    

- 
**[AdditionalContextData Class](./apex_class_runtime_industries_cpq_AdditionalContextData.htm.md#apex_class_runtime_industries_cpq_AdditionalContextData)**  

Contains properties to include a list of additional context data nodes. These nodes are     used along with the context definition nodes for data hydration.

- 
**[AdditionalFields Class](./apex_class_runtime_industries_cpq_AdditionalFields.htm.md#apex_class_runtime_industries_cpq_AdditionalFields)**  

Contains properties to include a map where the key is a string and the value is an     instance of the AdditionalFieldsInput class.

- 
**[AdditionalFieldsInput Class](./apex_class_runtime_industries_cpq_AdditionalFieldsInput.htm.md#apex_class_runtime_industries_cpq_AdditionalFieldsInput)**  

Contains properties to include the additional standard or custom fields in the     request.

- 
**[ApiStatusRepresentation Class](./apex_class_runtime_industries_cpq_ApiStatusRepresentation.htm.md#apex_class_runtime_industries_cpq_ApiStatusRepresentation)**  

Stores details of the API request such as execution messages, status code, and status     message.

- 
**[AttributeCategoryOutputRepresentation Class](./apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributeCategoryOutputRepresentation)**  

Stores details of an attribute such as code, description, usage type, and so     on.

- 
**[AttributePickListOutputRepresentation Class](./apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributePickListOutputRepresentation)**  

Stores details of an attribute picklist.

- 
**[AttributePickListValueOutputRepresentation Class](./apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_AttributePickListValueOutputRepresentation)**  

Stores details of an attribute picklist value.

- 
**[BulkProductDetailsInputBody Class](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBody.htm.md#apex_class_runtime_industries_cpq_BulkProductDetailsInputBody)**  

Contains the details of the request to retrieve product details by using product ID and     product selling model ID.

- 
**[BulkProductDetailsInputBodyList Class](./apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList.htm.md#apex_class_runtime_industries_cpq_BulkProductDetailsInputBodyList)**  

Contains details of the request to retrieve a list of products.

- 
**[BulkProductDetailsRepresentation Class](./apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation.htm.md#apex_class_runtime_industries_cpq_BulkProductDetailsRepresentation)**  

Get the details of multiple product definitions in a single request. This class is used for bulk product retrieval operations in Product Discovery.

- 
**[CatalogOutputRepresentation Class](./apex_class_runtime_industries_cpq_CatalogOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CatalogOutputRepresentation)**  

Contains properties to store details of a catalog definition.

- 
**[ConfigRuleResult Class](./apex_class_runtime_industries_cpq_ConfigRuleResult.htm.md#apex_class_runtime_industries_cpq_ConfigRuleResult)**  

Contains the results of configuration rule evaluation, including message rules, product recommendation rules, and visibility rules that are applied during product configuration.

- 
**[CategoryOutputRepresentation Class](./apex_class_runtime_industries_cpq_CategoryOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_CategoryOutputRepresentation)**  

Contains properties to store details of a category.

- 
**[ContextDataInput Class](./apex_class_runtime_industries_cpq_ContextDataInput.htm.md#apex_class_runtime_industries_cpq_ContextDataInput)**  

Get details of a context.

- 
**[FacetValueRepresentation Class](./apex_class_runtime_industries_cpq_FacetValueRepresentation.htm.md#apex_class_runtime_industries_cpq_FacetValueRepresentation)**  

Get details of the facet values that are found in the search result.

- 
**[Filter Class](./apex_class_runtime_industries_cpq_Filter.htm.md#apex_class_runtime_industries_cpq_Filter)**  

Contains the criteria property to store the details of a filter criteria, which is used     to filter records.

- 
**[FilterCriteriaInputRepresentation Class](./apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation.htm.md#apex_class_runtime_industries_cpq_FilterCriteriaInputRepresentation)**  

Contains properties to store criteria details to filter records based on supported     properties.

- 
**[FilterInputRepresentation Class](./apex_class_runtime_industries_cpq_FilterInputRepresentation.htm.md#apex_class_runtime_industries_cpq_FilterInputRepresentation)**  

Contains the filter property to filters records based on supported criteria.

- 
**[GuidedSelectionRepresentation Class](./apex_class_runtime_industries_cpq_GuidedSelectionRepresentation.htm.md#apex_class_runtime_industries_cpq_GuidedSelectionRepresentation)**  

Contains properties to represent a product in a guided selection flow. This class is used in Product Discovery to provide structured product information during guided product selection processes.

- 
**[GuidedSelectionSearchTerm Class](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm.htm.md#apex_class_runtime_industries_cpq_GuidedSelectionSearchTerm)**  

Represents a search term used in guided product selection. Contains the search term text and associated tags for filtering and searching products in Product Discovery.

- 
**[GuidedSelectionSearchTermList Class](./apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList.htm.md#apex_class_runtime_industries_cpq_GuidedSelectionSearchTermList)**  

Contains a list of search terms used in guided product selection. This class is used to pass multiple search terms for filtering and searching products in Product Discovery.

- 
**[MessageRule Class](./apex_class_runtime_industries_cpq_MessageRule.htm.md#apex_class_runtime_industries_cpq_MessageRule)**  

Represents a message rule that is evaluated during product configuration. Message rules display informational, warning, or error messages to users based on configuration conditions.

- 
**[PricingModelOutputRepresentation Class](./apex_class_runtime_industries_cpq_PricingModelOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_PricingModelOutputRepresentation)**  

Contains details of a pricing model in a product configuration.

- 
**[ProductAttributeOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductAttributeOutputRepresentation)**  

Contains details about the attribute in a product configuration.

- 
**[ProductClassificationOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductClassificationOutputRepresentation)**  

Get details of the product classification in a product configuration.

- 
**[ProductComponentGroupOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupOutputRepresentation)**  

Get details of the product component group in a product classification.

- 
**[ProductComponentGroupRepresentation Class](./apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductComponentGroupRepresentation)**  

Represents a product component group used in bulk product operations. This class is similar to ProductComponentGroupOutputRepresentation but is used specifically for bulk product detail representations where components are represented as BulkProductDetailsRepresentation objects.

- 
**[ProductDetailsRepresentation Class](./apex_class_runtime_industries_cpq_ProductDetailsRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductDetailsRepresentation)**  

Get the details of a product definition.

- 
**[ProductListRepresentation Class](./apex_class_runtime_industries_cpq_ProductListRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductListRepresentation)**  

Get the list of retrieved products.

- 
**[ProductOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductOutputRepresentation)**  

Get the details of a product definition.

- 
**[ProductPricesOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductPricesOutputRepresentation)**  

Get the price details of a product.

- 
**[ProductQuantityOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductQuantityOutputRepresentation)**  

Represents the quantity constraints and current quantity for a product in the product discovery context.

- 
**[ProductRecommendationRule Class](./apex_class_runtime_industries_cpq_ProductRecommendationRule.htm.md#apex_class_runtime_industries_cpq_ProductRecommendationRule)**  

Represents a product recommendation rule that is evaluated during product configuration. Product recommendation rules suggest additional products to users based on configuration conditions.

- 
**[ProductRelatedComponentOutputRepresentation Class](./apex_class_ricpq_ProductRelatedComponentOR.htm.md#apex_class_ricpq_ProductRelatedComponentOR)**  

Represents a related component product in a bundle or product relationship, including component configuration details such as quantity constraints, required status, and relationship metadata.

- 
**[ProductSellingModelOptionOutputRepresentation Class](./apex_class_ricpq_ProductSellingModelOptionOR.htm.md#apex_class_ricpq_ProductSellingModelOptionOR)**  

Represents a selling model option available for a product, which defines how the product can be sold (such as subscription, one-time, or usage-based).

- 
**[ProductSellingModelOutputRepresentation Class](./apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_ProductSellingModelOutputRepresentation)**  

Represents a product selling model that defines how a product is sold, including the selling model type, pricing term, and status.

- 
**[ProductSpecificationRecordTypeOutputRepresentation Class](./apex_class_ricpq_ProductSpecificationRecordTypeOR.htm.md#apex_class_ricpq_ProductSpecificationRecordTypeOR)**  

Represents the record type information for a product specification, which defines the type of record used to store product specification data.

- 
**[ProductSpecificationTypeOutputRepresentation Class](./apex_class_ricpq_ProductSpecificationTypeOR.htm.md#apex_class_ricpq_ProductSpecificationTypeOR)**  

Represents a product specification type that defines the structure and attributes available for configuring a product.

- 
**[QocQualificationOutputRepresentation Class](./apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QocQualificationOutputRepresentation)**  

Represents a quote, order, or contract qualification that determines whether a product     can be sold based on specific business rules and conditions.

- 
**[QualificationContextOutputRepresentation Class](./apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_QualificationContextOutputRepresentation)**  

Represents the context information used for product qualification, including account, opportunity, and other relevant context data for determining product eligibility.

- 
**[RelatedObjectFilter Class](./apex_class_runtime_industries_cpq_RelatedObjectFilter.htm.md#apex_class_runtime_industries_cpq_RelatedObjectFilter)**  

Represents a filter for related objects used in product search and discovery, allowing you to filter products based on related object criteria.

- 
**[RelatedObjectFilterInputRepresentation Class](./apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation.htm.md#apex_class_runtime_industries_cpq_RelatedObjectFilterInputRepresentation)**  

Represents input criteria for filtering products based on related object information, such as account, opportunity, or contract data.

- 
**[SearchProductsFacetRepresentation Class](./apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation.htm.md#apex_class_runtime_industries_cpq_SearchProductsFacetRepresentation)**  

Represents a search facet that provides filtering and categorization options for product search results, such as categories, attributes, or other product characteristics.

- 
**[SearchProductsRepresentation Class](./apex_class_runtime_industries_cpq_SearchProductsRepresentation.htm.md#apex_class_runtime_industries_cpq_SearchProductsRepresentation)**  

Represents the results of a product search operation, including the list of products, search facets, pagination information, and total count of matching products.

- 
**[UnitOfMeasureOutputRepresentation Class](./apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation.htm.md#apex_class_runtime_industries_cpq_UnitOfMeasureOutputRepresentation)**  

Represents the unit of measure for a product. This class contains information about how product quantities are measured, including the unit code, name, scale, and rounding method.

- 
**[VisibilityRule Class](./apex_class_runtime_industries_cpq_VisibilityRule.htm.md#apex_class_runtime_industries_cpq_VisibilityRule)**  

Represents a visibility rule that is evaluated during product configuration. Visibility rules control the visibility of products, attributes, or other UI elements based on configuration conditions.

=== ARTICLE: connect_requests_additional_fields_input.htm ===
---
page_id: connect_requests_additional_fields_input.htm
title: Additional Fields Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_additional_fields_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Additional Fields Input

Input representation of the additional standard or custom fields to include in the
    response.

**JSON example**

: 

```
  "additionalFields" : {
    "Product2" : {
    "fields" : ["CustomField1__c","StandardField1"]
}
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fields` | String[] | List of additional standard or custom fields to include in the response. | Optional | 61.0 |

=== ARTICLE: connect_requests_bulk_product_details_input.htm ===
---
page_id: connect_requests_bulk_product_details_input.htm
title: Bulk Product Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_bulk_product_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Product Details Input

Input representation of the request to retrieve details of multiple products.

**JSON example**

: 

```
{
  "productData": [
    {
      "productId": "01txx0000006ivJAAQ",
      "productSellingModelId": "0jPxx000000009hEAA"
    },
    {
      "productId": "01txx0000006ivLAAQ",
      "productSellingModelId": "0jPxx000000009iEAABB"
    }
  ],
  "correlationId": "de9a674c-1807-438c-ac78-2c96f4655325",
  "priceBookId" : "01sxx0000005qxxAAA",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
  }
}
```

This example shows a sample request with proration policy details requested through the
              `additionalFields`
            property.

```
{
  "additionalFields": {
    "ProductSellingModelOption": {
      "additionalFields": {
        "ProrationPolicy": {
          "fields": [
            "ArePartialPeriodsAllowed",
            "ProrationPolicyType"
          ]
        }
      }
    }
  },
  "productData": [
    {
      "productId": "01txx0000006ivJAAQ",
      "productSellingModelId": "0jPxx000000009hEAA"
    },
    {
      "productId": "01txx0000006ivLAAQ",
      "productSellingModelId": "0jPxx000000009iEAABB"
    }
  ],
  "correlationId": "de9a674c-1807-438c-ac78-2c96f4655325",
  "priceBookId": "01sxx0000005qxxAAA",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes to add to the custom or default context definition. This data is appended to the context input and sent for hydration and qualification. The maximum limit of supported nodes is 10. | Optional | 61.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. The field values are returned in the response for each of the products. In API version 66.0 and later, you can request proration policy details in the response for each product selling model option through this property. | Optional | 61.0 |
| `context​Definition` | String | Name of the custom context definition that’s sent for the context creation. If unspecified, the default context definition is used. | Optional | 61.0 |
| `context​Mapping` | String | Context mapping details from the context definition. If specified, the API validates if the context mapping belongs to the specified context definition and considers the mapping for hydration. If unspecified, the default context mapping of the context definition is used. | Optional | 61.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 61.0 |
| `currency​Code` | String | Currency code to consider for pricing and filtering. | Optional | 61.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 61.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 61.0 |
| `price​BookId` | String | ID of the price book to fetch the prices from. | Optional | 61.0 |
| `pricing​Procedure` | String | Name of the custom pricing procedure to send for processing. If unspecified, the default pricing procedure is executed. | Optional | 61.0 |
| `product​Data` | [Product Data Input](./connect_requests_product_data_input.htm.md)[] | List of maps that contain product IDs and product selling model IDs. | Required | 61.0 |
| `qualification​Procedure` | String | Name of the custom qualification procedure to send for processing. If unspecified, the default qualification procedure is executed. | Optional | 61.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md)[] | User context details. For example, account ID or contact ID. | Optional | 61.0 |

=== ARTICLE: connect_requests_catalog_details_input.htm ===
---
page_id: connect_requests_catalog_details_input.htm
title: Catalog Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_catalog_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog Details Input

Input representation of the request to get the catalog details.

**JSON example**

: 

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
     "accountId": "001xx0000000001AAA",
     "contactId": "003xx00000000D7AAI"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_catalog_input.htm ===
---
page_id: connect_requests_catalog_input.htm
title: Catalog Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_catalog_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog Input

Input representation of the request to retrieve catalog records.

**JSON example**

          
: This example shows how to retrieve catalogs that contain `apple` in the catalog name.

: 

```
{
"pageSize": 100,
"offset": 0,
"language": "french",
"filter": {
"criteria": [
{
"property": "name",
"operator": "contains",
"value": "apple"
}
]
}
}
```

          
: This example shows how to retrieve catalogs with `ServiceProcess` as the catalog type.

          
: 
            

```
{
"pageSize": 100,
"offset": 0,
"sort": {
  "orders": [
   {
   "property": "name",
   "direction": "desc"
   }
  ]
 },
"filter": {
"criteria": [
{
"property": "catalogType",
"operator": "eq",
"value": "ServiceProcess"
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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `filter` | [Filter](./connect_requests_criteria.htm.md) | Criteria to filter the records. Filters are applicable to the fields of the ProductCatalog object. The supported operators are: `eq` `in` `contains` The supported properties are `name` and `catalogType`. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 60.0 |
| `page​Size` | Integer | Number of records per page. Valid values are from 1 through 100. If unspecified, defaults to 100. | Optional | 60.0 |
| `sort` | [Sort](./connect_requests_order.htm.md) | Sort order of the catalog records. The supported operators are: `asc` `desc` | Optional | 60.0 |

=== ARTICLE: connect_requests_catalog_list_input.htm ===
---
page_id: connect_requests_catalog_list_input.htm
title: Catalog List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_catalog_list_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog List Input

Input representation of the request to get a list of catalogs.

**JSON example**

: 

```

    {
    "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
    "limit": 10,
    "offset": 0,
    "orderBy": [
        "name:asc",
        "id:desc"
    ],
    "userContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    }
    }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `limit` | Integer | Number of items to include in the response. | Optional | 60.0 |
| `offset` | Integer | Offset size from which to get the catalog count. | Optional | 60.0 |
| `order​By` | String[] | Sort order for the catalogs. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_category_details_input.htm ===
---
page_id: connect_requests_category_details_input.htm
title: Category Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_category_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category Details Input

Input representation of the request to get category details.

        
          

**JSON example**

          
: 

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
  }
}
```

This example shows a sample request to get category details with eligible
            promotions.

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "usePromotions": true
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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md) | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `customFields` | String[] | List of category fields to retrieve in the response. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the categories (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains` `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |
| `usePromotions` | Boolean | Indicates whether to fetch eligible promotions from Global Promotion Management (GPM) for the requested category and its products (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |

=== ARTICLE: connect_requests_category_list_input.htm ===
---
page_id: connect_requests_category_list_input.htm
title: Category List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_category_list_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category List Input

Input representation of the request to get a list of categories.

        
          

**JSON example**

          
: 

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx000000009hGAA",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
    }
}
```

This example shows a sample request to get a list of categories with eligible
            promotions.

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx000000009hGAA",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "usePromotions": true
}
```

        
      

      
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `catalog​Id` | String | ID of the catalog. | Required | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `customFields` | String[] | List of additional custom fields to include in the response. | Optional | 60.0 |
| `depth` | Integer | Specifies the levels of subcategories to retrieve beneath the parent category. This parameter only applies when `parentCategoryId` is provided. | Optional | 61.0 |
| `enableQualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`. | Optional | 60.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria.The supported property is `isQualified`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. | Optional | 62.0 |
| `parent​CategoryId` | String | ID of the parent category whose subcategories you want to retrieve. If not specified, only root-level categories from the catalog are returned. | Optional | 61.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `usePromotions` | Boolean | Indicates whether to fetch eligible promotions from Global Promotion Management (GPM) for the requested category and its products (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_context_data_input.htm ===
---
page_id: connect_requests_context_data_input.htm
title: Context Data Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_data_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context Data Input

Input representation of the context data.

**JSON example**

: 

```

"additionalContextData":[
  {
  "nodeName": "Contract",
  "nodeData": {
    "id": "xxxxx231",
    "name": "Contract1"
    
  }
},
{
  "nodeName": "Lead",
  "nodeData": {
    "id": "lllllll31",
    "name": "Lead1"
    
  }
}]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `nodeData` | Map<String, Object> | Details of the node. | Optional | 60.0 |
| `nodeName` | String | Name of the node. | Optional | 60.0 |

=== ARTICLE: connect_requests_criteria.htm ===
---
page_id: connect_requests_criteria.htm
title: Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_criteria.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Criteria Input

Input representation of the filter criteria item request.

    
      
        
          

**JSON example**

          
: 
            

```

"criteria":
[{
   "attributeType": "ProductStandard",
   "property": "name",
   "operator": "eq",
   "value": "iPhone"
},
{
   "criteriaType": "CustomWhereCondition",
   "value": "(effectiveenddate = null OR effectiveenddate >= 2024-06-25)"
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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributeType` | String | Search attribute type of the facet for a faceted search. Valid values are: `ProductStandard` `ProductCustom` `ProductDynamicAttribute` `ProductAttributeStandard` `ProductAttributeCustom` This property is applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. | Optional | 63.0 |
| `criteriaType` | String | Type of criteria for the filter. Valid value is: `CustomWhereCondition` | Required | 60.0 |
| `operator` | String | Operator used for the filter criteria. The supported operators are: `eq` `in` `contains`—This value isn’t applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. | Required | 60.0 |
| `property` | String | Property name to use in the filter, which must be the same as the object field. | Required | 60.0 |
| `value` | Object | Value for the filter criteria. | Required | 60.0 |

=== ARTICLE: connect_requests_data_rounding_input.htm ===
---
page_id: connect_requests_data_rounding_input.htm
title: Data Rounding Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_data_rounding_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Rounding Input

Input representation of the details of the data rounding input.

**JSON example**

: 

```
{
  "dataRowInputs": [
    {
      "key": "PRC1",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "0hExx0000000001EAA"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": "987462848934739347.32232590183756545",
          "unitOfMeasureId": "0hExx000000001dEAA"
        }
      ]
    },
    {
      "key": "PRC2",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "uomId1"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "unitOfMeasureId": "Kgs Id"
        }
      ]
    },
    {
      "key": "PRC3",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 0.437584,
          "unitOfMeasureId": "uomId2"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 7364.58923,
          "unitOfMeasureId": "uomId2"
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
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 63.0 |
| `dataRow​Inputs` | [Data Row Input](./connect_requests_data_row_input.htm.md)[] | List of row inputs for rounding the data. | Required | 63.0 |

=== ARTICLE: connect_requests_data_row_input.htm ===
---
page_id: connect_requests_data_row_input.htm
title: Data Row Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_data_row_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Row Input

Input representation of the details of the input for a data rounding request.

**JSON example**

: 

```
JSON example
{
  "dataRowInputs": [
    {
      "key": "PRC1",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "0hExx0000000001EAA"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": "987462848934739347.32232590183756545",
          "unitOfMeasureId": "0hExx000000001dEAA"
        }
      ]
    },
    {
      "key": "PRC2",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "uomId1"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "unitOfMeasureId": "Kgs Id"
        }
      ]
    },
    {
      "key": "PRC3",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 0.437584,
          "unitOfMeasureId": "uomId2"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 7364.58923,
          "unitOfMeasureId": "uomId2"
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
| `fieldData​Inputs` | [Field Data Input](./connect_requests_field_data_input.htm.md)[] | List of field-level data inputs. | Required | 63.0 |
| `key` | String | Key that identifies a unique data row. | Required | 63.0 |

=== ARTICLE: connect_requests_deep_clone_input.htm ===
---
page_id: connect_requests_deep_clone_input.htm
title: Deep Clone Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_deep_clone_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone Input

Input representation of the details of the object and associated record to be
    cloned.

**JSON example**

: 

```
{
  "mainRecordId": "01tSG0000028kcSYAQ",
  "mainObjectApiName": "Product2",
  "mainRecordFieldValues": {
    "Name": "New Cloud Storage"
  }
}
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `mainObject​ApiName` | String | API name of the object. The supported object is Product2. | Required | 63.0 |
| `mainRecord​Field​Values` | Map<String, String> | Mapping of the API name of the field to its value. The values passed through this map are set for the created record. You can pass the Name field only through this map. | Optional | 63.0 |
| `mainRecord​Id` | String | ID of the record. | Required | 63.0 |

=== ARTICLE: connect_requests_field_data_input.htm ===
---
page_id: connect_requests_field_data_input.htm
title: Field Data Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_field_data_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Field Data Input

Input representation of the details of the field data input.

        
          

**JSON example**

          
: 
            

```
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 0.437584,
          "unitOfMeasureId": "uomId2"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 7364.58923,
          "unitOfMeasureId": "uomId2"
        }
      ]
```

          

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fieldApi​Name` | String | Unique API name of the field. | Required | 63.0 |
| `original​Value` | String | Original value of the fields. | Required | 63.0 |
| `unitOf​MeasureId` | String | ID of the unit of measure record that’s associated to the field. | Required | 63.0 |

=== ARTICLE: connect_requests_filter.htm ===
---
page_id: connect_requests_filter.htm
title: Filter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_filter.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Filter Input

Input representation of the filter request.

    
      
        
          

**JSON example**

          
: 
            

```

"filter": 
{
"criteria": [ {  
"property": "name",   
"operator": "eq",   
"value": "iPhone"
},
{
"criteriaType": "CustomWhereCondition",
"value": "(effectiveenddate = null OR effectiveenddate >= 2024-06-25)"
}
]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `criteria` | [Criteria](./connect_requests_criteria.htm.md)[] | Details of the filter criteria. | Required if the `filter` property is specified. | 60.0 |

=== ARTICLE: connect_requests_filter_criteria_input.htm ===
---
page_id: connect_requests_filter_criteria_input.htm
title: Filter Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_filter_criteria_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Filter Criteria Input

Input representation of the criteria to filter records based on supported
    properties.

**JSON example**

: 

```

"criteria":
 [{
   "attributeType": "ProductStandard",
   "property": "name",
   "operator": "eq",
   "value": "iPhone"
 }]
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

                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attributeType` | String | Search attribute type of the facet for a faceted search. Valid values are: `ProductStandard` `ProductCustom` `ProductDynamicAttribute` `ProductAttributeStandard` `ProductAttributeCustom` | Optional | 63.0 |
| `operator` | String | Operator used for the filter criteria. The supported operators are: `eq` `in` `contains` `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. | Required | 60.0 |
| `property` | String | Property name to use in the filter, which must be the same as the object field. The supported property is `name`. | Required | 60.0 |
| `value` | Object | Value for the filter criteria. | Required | 60.0 |

=== ARTICLE: connect_requests_filter_input.htm ===
---
page_id: connect_requests_filter_input.htm
title: Filter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_filter_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Filter Input

Input representation of the request to filter records.

**JSON example**

: 

```
"filter":
 {"criteria":
 [ {
   "attributeType": "ProductStandard",
   "property": "name",
   "operator": "eq",
   "value": "iPhone"
 }]}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `criteria` | [Filter Criteria Input](./connect_requests_filter_criteria_input.htm.md)[] | Filter criteria to filter the records. | Optional | 60.0 |

=== ARTICLE: connect_requests_guided_selection_input.htm ===
---
page_id: connect_requests_guided_selection_input.htm
title: Guided Selection Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_guided_selection_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guided Selection Input

Input representation of the guided selection details.

          

**JSON example**

          
: 
            

```
{
  "correlationId": "corrId",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "pricebookId",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "userContext": {
    "accountId": "accId"
  },
  "guidedSelectionResponseId": "ABCxx0000000001GAA",
  "searchTerms": [
    {
      "term": "IPhone",
      "tags": [
        "deviceType",
        "mobile"
      ]
    },
    {
      "term": "4GB",
      "tags": [
        "RAM"
      ]
    },
    {
      "term": "64GB",
      "tags": [
        "Storage"
      ]
    }
  ],
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": false
}
```

          

          
: This example shows a sample request to fetch eligible
            promotions.

```
{
  "correlationId": "corrId",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "pricebookId",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "userContext": {
    "accountId": "accId"
  },
  "guidedSelectionResponseId": "ABCxx0000000001GAA",
  "searchTerms": [
    {
      "term": "IPhone",
      "tags": [
        "deviceType",
        "mobile"
      ]
    },
    {
      "term": "4GB",
      "tags": [
        "RAM"
      ]
    },
    {
      "term": "64GB",
      "tags": [
        "Storage"
      ]
    }
  ],
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": false,
  "transactionContextId": "context123",
  "transactionId": "trans456",
  "usePromotions": true
}
```

          
: This example shows a sample request to run visibility
            rules.

```
{
  "catalogId": "0ZSVW000000AhdC4AS",
  "currencyCode": "USD",
  "enablePricing": true,
  "enableQualification": true,
  "executeConfigurationRules": true,
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "guidedSelectionResponseId": "0U3VW0000000a1t0AA",
  "includeCatalogDetails": true,
  "limit": 12,
  "offset": 0,
  "orderBy": [
    "name:asc"
  ],
  "priceBookId": "01sVW0000024PZlYAM",
  "transactionId": "0Q0VW000001190f0AA",
  "userContext": {
    "accountId": null
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
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 62.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 62.0 |
| `catalog​Id` | String | ID of the catalog. | Required | 62.0 |
| `category​Id` | String | ID of the category. | Optional | 62.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 62.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 62.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 62.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the `currencyCode` property is required. | Optional | 62.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 62.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 62.0 |
| `guided​Selection​ResponseId` | String | Response identifier of the guided selection. | Required if the `searchTerms` property isn’t specified. | 62.0 |
| `include​Catalog​Details` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 62.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 62.0 |
| `order​By` | String[] | Sort order of the results, which is either ascending (`asc`) or descending order (`desc`). The default sort order is ascending order. The default value is `asc`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 62.0 |
| `price​BookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Required | 62.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 62.0 |
| `product​Classification​Id` | String | ID of the product classification. | Optional | 62.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 62.0 |
| `searchTerms` | [Guided Selection Search Term Input](./connect_requests_guided_selection_search_term_input.htm.md)[] | Search terms of the guided selection. | Required if the `guided​Selection​ResponseId` property isn’t specified. | 62.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 67.0 |
| `transactionId` | String | ID of the transaction. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for the guided selection (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 62.0 |

If both the `guided​Selection​ResponseId` and
                `searchTerms` properties are specified, then the
                `searchTerms` property is considered in the input
              request.

=== ARTICLE: connect_requests_guided_selection_search_term_input.htm ===
---
page_id: connect_requests_guided_selection_search_term_input.htm
title: Guided Selection Search Term Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_guided_selection_search_term_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guided Selection Search Term Input

Input representation of the search terms of a guided selection.

**JSON example**

: 

```
  "searchTerms": [
    {
      "term": "IPhone",
      "tags": [
        "deviceType",
        "mobile"
      ]
    },
    {
      "term": "4GB",
      "tags": [
        "RAM"
      ]
    },
    {
      "term": "64GB",
      "tags": [
        "Storage"
      ]
    }
  ]
```

**Properties**

: 

                
                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                    

                  

                

                
                  
                    
                    

                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                    

                  

                

              
| Name |  | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- | --- |
| `tags` |  | String[] | Search term tags for the guided selection. | Optional | 62.0 |
| `term` |  | String | Search term for the guided selection. | Required | 62.0 |

=== ARTICLE: connect_requests_include_object_input.htm ===
---
page_id: connect_requests_include_object_input.htm
title: Include Object Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_include_object_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Include Object Input

Input representation of the object to include in the response.

**JSON example**

: 

```
"includeObjects": 
[{
"objectName": "ProductCategory"
}]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `objectName` | String | Name of the object to include in the response. The supported object is `ProductCategory`. | Required if the `options` property is specified. | 60.0 |

=== ARTICLE: connect_requests_index_configuration_collection_input.htm ===
---
page_id: connect_requests_index_configuration_collection_input.htm
title: Index Configuration Collection Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_index_configuration_collection_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configuration Collection Input

Input representation of the collection of index configurations.

**JSON example**

: 

```
{
  "correlationId": "8545b5aa-f3e6-429a-8f21-9cc4ce50b1d7",
  "indexConfigurations": [
    {
      "attributeDefinitionId": "0tjT1000000002bIAA",
      "name": "Color",
      "type": "ProductDynamicAttribute",
      "isSearchable": true
    },
    {
      "attributeFieldId": "00Nxx000001FwnABII",
      "name": "Message__c",
      "type": "Custom",
      "isSearchable": true
    },
    {
      "name": "Code",
      "type": "Standard",
      "isSearchable": true
    },
    {
      "facetDisplayRank": 1,
      "isFacetable": false,
      "isSearchable": true,
      "name": "Family",
      "type": "Standard"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 62.0 |
| `index​Configurations` | [Index Configuration Input](./connect_requests_index_configuration_input.htm.md)[] | List of index configurations. | Required | 62.0 |

=== ARTICLE: connect_requests_index_configuration_input.htm ===
---
page_id: connect_requests_index_configuration_input.htm
title: Index Configuration Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_index_configuration_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configuration Input

Input representation of the request to persist the index configuration.

        
          

**JSON example**

          
: 
            

```
  "indexConfigurations": [
    {
      "attributeDefinitionId": "0tjT1000000002bIAA",
      "name": "Color",
      "type": "ProductDynamicAttribute",
      "isSearchable": true
    },
    {
      "attributeFieldId": "00Nxx000001FwnABII",
      "name": "Message__c",
      "type": "Custom",
      "isSearchable": true
    },
    {
      "name": "Code",
      "type": "Standard",
      "isSearchable": true
    },
    {
      "facetDisplayRank": 1,
      "isFacetable": false,
      "isSearchable": true,
      "name": "Family",
      "type": "Standard"
    }
  ]
```

          

        

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `attribute​DefinitionId` | String | ID of the attribute definition. | Required if the `attribute​FieldId`property isn’t specified. | 62.0 |
| `attribute​FieldId` | String | ID of the attribute field. | Required if the `attribute​DefinitionId`property isn’t specified. | 62.0 |
| `facet​DisplayRank` | Integer | Sort order for displaying the facets at run time. | Optional | 63.0 |
| `is​Facetable ` | Boolean | Indicates whether the field is facetable (`true`) or not (`false`). | Optional | 63.0 |
| `is​Searchable` | Boolean | Indicates whether the index-configured field is searchable (`true`) or not (`false`). | Optional | 62.0 |
| `name` | String | Name of the index-configured field. | Required | 62.0 |
| `type` | String | Type of the index-configured field. | Required | 62.0 |

=== ARTICLE: connect_requests_index_setting_input.htm ===
---
page_id: connect_requests_index_setting_input.htm
title: Index Setting Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_index_setting_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Setting Input

Input representation of the index setting.

**JSON example**

: 

```
{
    "setting" : {
        "supportedLanguages" : ["en_US","ja","es","nl_NL"],
        "defaultLanguage" : "en_US",
        "productsGrouping": "GROUPING_VARIATION"
   }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `setting` | [Setting Input](./connect_requests_setting_input.htm.md)[] | Object containing the setting-related details. | Required | 63.0 |

=== ARTICLE: connect_requests_options.htm ===
---
page_id: connect_requests_options.htm
title: Options Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_options.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Options Input

Reserved for internal use.

=== ARTICLE: connect_requests_order.htm ===
---
page_id: connect_requests_order.htm
title: Order Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_order.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Order Input

Input representation of the sort order item request.

    
      
        
          

**JSON example**

          
: 
            

```
"sort":{
"orders":
[{
   "property": "name",
   "direction": "asc"
}]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `direction` | String | Direction to sort the list items, such as in ascending order or descending order. | Required | 60.0 |
| `property` | String | Property to use for the sorting of the list items. | Required | 60.0 |

=== ARTICLE: connect_requests_product_catalog_additional_fields_input.htm ===
---
page_id: connect_requests_product_catalog_additional_fields_input.htm
title: Additional Fields Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_catalog_additional_fields_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Additional Fields Input

Input representation of the additional standard or custom fields to be included in the
    response.

    
      
        
          

**JSON example**

          
: 

```
"additionalFields": {
    "Product2": {
      "fields": [
        "code__c"
      ]
    }
```

This example shows a sample request with attribute definition field
            details.

```
"additionalFields":{
  "OptOutAssetization":true
  "OptOutDecompositionAction":false
  "OptOutSupplementalAction":false
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `fields` | String[] | List of additional standard or custom fields to be included in the response. | Required | 61.0 |

=== ARTICLE: connect_requests_product_classification_details_input.htm ===
---
page_id: connect_requests_product_classification_details_input.htm
title: Product Classification Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_classification_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification Details Input

Input representation of the request to fetch details of product classification records,
    including their attributes and attribute categories.

**JSON example**

: 

```
{
  "productClassificationIds": [
    "01txx0000006iFMAAY",
    "01txx0000006iGxAAY"
  ],
  "catalogSystems": [
    "epc"
  ]
}
```

**Properties**

: 

- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalogSystems` | String[] | Name of the catalog system. Valid value is: `epc`—Enterprise Product Catalog | Optional | 66.0 |
| `product​ClassificationIds` | String[] | List of product classification IDs for which you want to retrieve product details. In the `epc` catalog system, these values are the `Product2` record IDs. | Required | 66.0 |

=== ARTICLE: connect_requests_product_classification_list_input.htm ===
---
page_id: connect_requests_product_classification_list_input.htm
title: Product Classification List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_classification_list_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification List Input

Input representation of the request to retrieve a list of product classification
    records.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "catalogSystem": "pcm",
  "searchTerm": "Mobile",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "contains",
        "value": "Mobile"
      }
    ]
  },
  "sort": {
    "orders": [
      {
        "property": "name",
        "direction": "asc"
      }
    ]
  },
  "pageSize": 25,
  "offset": 0
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
| `catalogSystem` | String | Name of the catalog system. Valid values are: `pcm`—Product Catalog Management `epc`—Enterprise Product Catalog If unspecified, the default catalog system is `pcm`. | Optional | 67.0 |
| `filter` | [Criteria Input](./connect_requests_criteria.htm.md) | Criteria to filter the product classification records. The supported property is `name`. The supported operators are: `eq` `in` `contains` If multiple criteria are specified, they're combined by using the `and` operator. Each criterion supports only the `property`, `operator`, and `value` fields. | Optional | 67.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 67.0 |
| `pageSize` | Integer | Specifies the number of records per page. Valid values are 5, 10, 25, 50, and 100. If unspecified, the default value is 100. | Optional | 67.0 |
| `searchTerm` | String | String used to search for product classifications with the product classification name containing the search term. | Optional | 67.0 |
| `sort` | [Order Input](./connect_requests_order.htm.md) | Sort order for the product classifications. If unspecified, the default sort order is by name in ascending order. | Optional | 67.0 |

=== ARTICLE: connect_requests_product_data_input.htm ===
---
page_id: connect_requests_product_data_input.htm
title: Product Data Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_data_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Data Input

Input representation of the product details such as the product ID and product selling
    model ID.

**JSON example**

: 

```
  "productData": [
    {
      "productId": "01txx0000006ivJAAQ",
      "productSellingModelId": "0jPxx000000009hEAA"
    },
    {
      "productId": "01txx0000006ivLAAQ",
      "productSellingModelId": "0jPxx000000009iEAABB"
    }
  ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `productId` | String | ID of the product. | Required | 61.0 |
| `product​Selling​ModelId` | String | ID of the product selling model. | Optional | 61.0 |

=== ARTICLE: connect_requests_product_details_input.htm ===
---
page_id: connect_requests_product_details_input.htm
title: Product Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Details Input

Input representation of the request to get product details.

**JSON example**

: 

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "01s26000002ZT71AAG",
  "productSellingModelId": "0jP1Q000000CaVFUA0",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "enablePricing": true,
  "enableQualification": true,
  "qualificationProcedure": "QualificationProcedure",
  "pricingProcedure": "Preview",
  "contextDefinition": "TestDefinition",
  "contextMapping": "TestDefinitionNode",
  "additionalFields": {
    "ProductSellingModelOption": {
      "additionalFields": {
        "ProrationPolicy": {
          "fields": [
            "ArePartialPeriodsAllowed",
            "ProrationPolicyType"
          ]
        }
      }
    },
    "Product2": {
      "fields": [
        "field1",
        "field2"
      ]
    },
    "ProductAttributeDefinition": {
      "fields": [
        "field3",
        "field4"
      ]
    }
  },
  "additionalContextData": [
    {
      "nodeName": "Contract",
      "nodeData": {
        "id": "xxxxx231",
        "name": "Contract1"
      }
    },
    {
      "nodeName": "Lead",
      "nodeData": {
        "id": "lllllll31",
        "name": "Lead1"
      }
    }
  ]
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Context​Data` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields to include in the response.The supported objects are: Product2 ProductAttributeDefinition—If the fields defined for the ProductAttributeDefinition object aren’t available for the ProductClassificationAttr object, then the API request fails. In API version 66.0 and later, you can request proration policy details in the response for each product selling model option through this property. | Optional | 61.0 |
| `catalogId` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the currencyCode property is required. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `priceBook​Id` | String | ID of the price book to fetch the prices from. If this property isn’t specified, then the prices from the standard price book are fetched. | Required | 60.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product​SellingModel​Id` | String | ID of the product selling model. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_product_input.htm ===
---
page_id: connect_requests_product_input.htm
title: Product Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Input

Input representation of a product in the catalog.

**JSON example**

          
: This example is a search request for products that contain `Bundle Product` in the product
            name.

```
{
  "catalogIds": [
    "0ZST10000004D03OAE"
  ],
  "language": "spanish",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "contains",
        "value": "Bundle Product"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": false
        }
      ],
      "additionalFields": {
        "Product2": {
          "fields": [
            "code__c"
          ]
        }
      }
    }
  ]
}
```

          
: This example is a search request for products that contain the specified search term
            in the product name and are part of a
            catalog.

```
  {
  "catalogIds": [
    "0ZSDU0000002Og54AE"
  ],
  "searchTerm": "Slack"
}
```

        
          

**Query parameters**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `product​Classification​Id` | String | ID of the product classification template that contains a collection of dynamic attributes and can be reused to create multiple products. Products that are based on a product classification inherit all the attributes of the product classification. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |

          

        

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

- 
- 
- 
- 
- 
- 
- 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Map of the object and the list of standard and custom fields to be queried along with the standard response. The supported object is Product2. | Optional | 61.0 |
| `catalog​Ids` | List<String> | List of comma-separated catalog IDs. The API returns the list of product records that are associated with the specified catalog IDs. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |
| `category​Ids` | List<String> | List of comma-separated category IDs. The API returns the list of product records that are associated with the specified category IDs. If unspecified, then returns all products that are added to at least one category. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `filter` | [Criteria Input](./connect_requests_criteria.htm.md) | Criteria to filter the records. Filters are applicable to the fields of Product2 object. The supported operators are: `eq` `in` `contains`—This value isn’t applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the criteria are combined by using the `and` operator. The supported properties are `name`, `description`, and `isActive`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then the supported property is `name` only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 60.0 |
| `pageSize` | Integer | Specifies the number of records per page. Valid values are from 1 through 200. If the value is unspecified, it defaults to 100. | Optional | 60.0 |
| `related​Object​Filters` | [Related Object Filter](./connect_requests_related_object_filters_input.htm.md)[] | Criteria for the related objects to filter the records. The supported operator is `eq`. The supported object is `ProductSpecificationRecType`. The supported values are `true` and `false`. The supported property is `IsCommercial`. | Optional | 60.0 |
| `searchTerm` | String | String used to get products with the product name containing the search term. See [Search Considerations When Using Indexed Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_considerations.htm&type=5&language=en_US). | Optional | 62.0 |
| `sort` | [Sort](./connect_requests_order.htm.md) | Sort order for the products. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 60.0 |

=== ARTICLE: connect_requests_product_list_input.htm ===
---
page_id: connect_requests_product_list_input.htm
title: Product List Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_list_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product List Input

Input representation of the request to retrieve a list of products.

        
          

**JSON example**

          
: 

```
{
  "correlationId": "eeaa1db2-f371-4227-a886-c77e2f66ce1d",
  "limit": 60,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc"
  ],
  "catalogId": "0ZSDU0000002Og74AE",
  "categoryId": "0ZGDU0000002P0H4AU",
  "priceBookId": "01sDU000000JVsVYAW",
  "productClassificationId": "11BDU0000002TCC2A2",
  "currencyCode": "USD",
  "userContext": {
    "accountId": "001DU000001o2UzYAI"
  },
  "includeCatalogDetails": true,
  "enableQualification": true,
  "enablePricing": true,
  "qualificationProcedure": "ProductQualification",
  "pricingProcedure": "pricingProcedure",
  "contextDefinition": "BrowseContextDefinitionExt",
  "contextMapping": "ProductDiscoveryMapping",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "eq",
        "value": "Laptop Pro Bundle"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": true
        }
      ]
    }
  ],
  "additionalContextData": [
    {
      "nodeName": "Account",
      "nodeData": {
        "id": "001DU000001o2UzYAI",
        "name": "Cloud Kicks"
      }
    }
  ],
  "additionalFields": {
    "Product2": {
      "fields": [
        "CanRamp",
        "DecompositionScope",
        "ProductCode"
      ]
    }
  }
}
```

If a parent category ID is specified in the request body, then the API
            returns all products associated to all child categories.

          
: This example shows a sample request to retrieve a product list with promotions.

          
: 
            

```
{
  "correlationId": "eeaa1db2-f371-4227-a886-c77e2f66ce1d",
  "limit": 60,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc"
  ],
  "catalogId": "0ZSDU0000002Og74AE",
  "categoryId": "0ZGDU0000002P0H4AU",
  "priceBookId": "01sDU000000JVsVYAW",
  "productClassificationId": "11BDU0000002TCC2A2",
  "currencyCode": "USD",
  "userContext": {
    "accountId": "001DU000001o2UzYAI"
  },
  "includeCatalogDetails": true,
  "enableQualification": true,
  "enablePricing": true,
  "qualificationProcedure": "ProductQualification",
  "pricingProcedure": "pricingProcedure",
  "contextDefinition": "BrowseContextDefinitionExt",
  "contextMapping": "ProductDiscoveryMapping",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "eq",
        "value": "Laptop Pro Bundle"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": true
        }
      ]
    }
  ],
  "additionalContextData": [
    {
      "nodeName": "Account",
      "nodeData": {
        "id": "001DU000001o2UzYAI",
        "name": "Cloud Kicks"
      }
    }
  ],
  "additionalFields": {
    "Product2": {
      "fields": [
        "CanRamp",
        "DecompositionScope",
        "ProductCode"
      ]
    }
  },
  "executeConfigurationRules": false,
  "transactionContextId": "a1b2c3d4e5f6",
  "transactionId": "trans789",
  "usePromotions": true
}
```

          

          
: This example shows a sample request to run visibility
            rules.

```
{
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": true,
  "catalogId": "0ZSVW000000AhdC4AS",
  "limit": 12,
  "offset": 0,
  "userContext": {
    "accountId": null
  },
  "priceBookId": "01sVW0000024PZlYAM",
  "currencyCode": "USD",
  "transactionId": "0Q0VW000001190f0AA",
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "orderBy": [
    "name:asc"
  ],
  "executeConfigurationRules": true
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 61.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. If the category ID isn’t specified, then the API returns the list of offers from the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the `currencyCode` property is required. | Optional | 60.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `include​Catalog​Details` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 61.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 60.0 |
| `offset` | Integer | Reserved for internal use. | Optional | 60.0 |
| `order​By` | String[] | Sort order of the results, which is either ascending (`asc`) or descending order (`desc`). The default sort order is ascending order. The default value is `asc`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 60.0 |
| `price​BookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Required | 60.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product​Classification​Id` | String | ID of the product classification. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `related​Object​Filters` | [Related Object Filter Input](./connect_requests_related_object_filter_input.htm.md)[] | Filter records based on supported criteria for related objects. The supported object is `ProductSpecificationRecType`. The supported property is `IsCommerical`. The supported operator is `eq`. The supported values are `true` and `false`. | Optional | 60.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 67.0 |
| `transactionId` | String | ID of the transaction. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for each product in the list (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_product_recommendation_input.htm ===
---
page_id: connect_requests_product_recommendation_input.htm
title: Product Recommendation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_recommendation_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Recommendation Input

Input representation of the details of a request to get product
    recommendations.

**JSON example**

: 

```
{
  "currencyCode": "USD",
  "enablePricing": true,
  "enableQualification": true,
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "isQualified",
        "operator": "eq",
        "value": true
      }
    ]
  },
  "limit": 12,
  "priceBookId": "01sSG00000DQCjhYAH",
  "transactionId": "0Q0SG0000014Ui50AE"
}
```

**Properties**

: 

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additionalContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 67.0 |
| `additionalFields` | Map<String, [AdditionalFieldsInputRepresentation](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 67.0 |
| `catalogId` | String | ID of the catalog to fetch the recommended products from. | Optional | 67.0 |
| `contextDefinition` | String | API name of the custom context definition that’s sent for context creation. If you don’t specify this property, then the default context definition is used. | Optional | 67.0 |
| `contextMapping` | String | Default context mapping of the context definition. If you specify a context mapping, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 67.0 |
| `currencyCode` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled in the org, then the `currencyCode` property is required. If you don’t specify a currency code, then the value is fetched from the account. | Optional | 67.0 |
| `cursor` | String | Unique ID to represent the position of each product in the data set. | Optional | 67.0 |
| `enablePricing` | Boolean | Indicates whether to enable pricing for products in orgs where Salesforce Pricing is enabled (`true`) or not (`false`). Set the value to `false` to skip the execution of Salesforce Pricing. In orgs where Salesforce Pricing is disabled, you can’t override this value to `true`. The default value is `true`. | Optional | 67.0 |
| `enableQualification` | Boolean | Indicates whether to enable qualification rules for products in orgs where Qualification Procedure is enabled (`true`) or not (`false`). Set the value to `false` to skip the execution of Business Rules Engine qualification rules. In orgs where Qualification Procedure is disabled, you can’t override this value to `true`. The default value is `true`. | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md)[] | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If you specify multiple criteria, then the resultant criteria are combined by using the `and` operator. | Optional | 67.0 |
| `limit` | Integer | Number of recommended products to include in the response. The default value is `10`. | Optional | 67.0 |
| `priceBookId` | String | ID of the price book to get prices from. If you don’t specify a price book ID, then prices from the standard price book are fetched. | Optional | 67.0 |
| `pricingProcedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If you don’t specify this property, then the default pricing procedure is executed. | Optional | 67.0 |
| `qualificationProcedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If you don’t specify this property, then the default qualification procedure is executed. | Optional | 67.0 |
| `transactionContextId` | String | ID of the sales transaction context instance. | Optional | 67.0 |
| `transactionId` | String | ID of the quote or order. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for the guided selection (`true`) or not (`false`). The default value is `false`. | Optional | 67.0 |
| `userContext` | [User Context Input](./connect_requests_user_context_input.htm.md)[] | User context details. For example, account ID or contact ID. | Optional | 67.0 |

=== ARTICLE: connect_requests_product_variants_input.htm ===
---
page_id: connect_requests_product_variants_input.htm
title: Product Variants Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_product_variants_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Variants Input

Input representation of the request to retrieve the variation products associated with
    parent variant products.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "9b6bc520-3c82-4d6c-a458-47590370681a",
  "parentVariantsIds": [
    "01tT1000000F0afIAC",
    "01tT1000000F0agIAC"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique ID to track and associate related events or transactions. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 67.0 |
| `parent​Variants​Ids` | String[] | List of product IDs for parent variant products whose variations you want to retrieve. If any product ID is blank, invalid, or not found, the API skips that ID and processes the remaining valid IDs. The skipped IDs appear in the `inValidProductIds` response property. If a product ID is valid but isn't a parent variant product, the API includes it in the `nonVariantParentIds` response property. | Required | 67.0 |

=== ARTICLE: connect_requests_products_detail_bulk_input.htm ===
---
page_id: connect_requests_products_detail_bulk_input.htm
title: Bulk Product Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_products_detail_bulk_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Product Details Input

Input representation of the request to retrieve the details of multiple
    products.

        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "cbfabffb-093f-45b3-8c2d-88b4acbd4867",
  "productIds": [
    "01tT1000000F0afIAC",
    "01tT1000000F0afIAC"
  ],
  "uptoLevel": 1,
  "language": "french",
  "additionalFields": {
    "Product2": {
      "fields": [
        "code__c"
      ]
    },
    "ProductAttributeDefinition": {
      "fields": [
        "scope"
      ]
    }
  }
}
```

          

          
: This example shows a sample request to fetch data from Enterprise Product
            Catalog.

```
{
  "productIds": [
    "01tLT000009vGXfYAM"
  ],
  "catalogSystems": [
    "epc"
  ],
  "additionalFields": {
    "AttributeDefinition": {
      "fields": [
        "OptOutAssetization",
        "OptOutDecompositionAction",
        "OptOutSupplementalAction"
      ]
    }
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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Map of object and list of additional standard or custom fields to be included in the response. The supported objects are: Product2 ProductAttributeDefinition—If the fields defined for the ProductAttributeDefinition object aren’t available for the ProductClassificationAttr object, then the API request fails. If the Dynamic Revenue Orchestrator permission is enabled, then this property supports AttributeDefinition as key with these supported values. `OptOutAssetization` `OptOutDecompositionAction` `OptOutSupplementalAction` | Optional | 61.0 |
| `catalogSystems` | String[] | Name of the catalog system. Valid values are: `epc`—Enterprise Product Catalog `pcm`—Product Catalog Management Although this property accepts a list, you can pass only one value. If you don’t specify a value, the default behavior is to fetch data from the `pcm` catalog. | Optional | 66.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 61.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `product​Ids` | String[] | List of product IDs that details must be returned for. If any product ID is blank, invalid, or not found, then the request is processed with valid and available product IDs. | Required | 61.0 |
| `upto​Level` | Integer | Hierarchy level to follow to return the product details. For a bundle, this property determines the number of levels of child components to be returned. You can specify up to a hierarchy level of 1. If unspecified, the default level is the full bundle hierarchy. | Optional | 61.0 |

=== ARTICLE: connect_requests_qoc_qualification_input.htm ===
---
page_id: connect_requests_qoc_qualification_input.htm
title: QOC Qualification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_qoc_qualification_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# QOC Qualification

Input representation of the qualification request.

**JSON example**

: 

```
{
  "productIds": [
    "01txx0000006i7PAAQ",
    "01txx0000006i7QAAQ",
    "01txx0000006i7IAAQ"
  ],
  "userContext": {
    "accountId": "001xx000003GZHgAAO"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `catalog​Id` | String | ID of the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `product​Ids` | String[] | List of product IDs for qualification check. | Required | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s sent for processing. If this property isn’t specified, the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_related_object_filter_input.htm ===
---
page_id: connect_requests_related_object_filter_input.htm
title: Related Object Filter Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_related_object_filter_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Object Filter Input

Input representation of the request to filter records of a related object.

**JSON example**

: 

```
"relatedObjectFilters":
 [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria":
 [{
      "property": "IsCommercial",
      "operator": "eq",
      "value": true
   }]
  }
  ]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `criteria` | [Filter Criteria Input](./connect_requests_filter_criteria_input.htm.md)[] | Criteria to filter the related objects. | Required if the relatedObjectFilters property is specified. | 60.0 |
| `object​Name` | String | Name of the object that’s related to the main object. | Required if the relatedObjectFilters property is specified. | 60.0 |

=== ARTICLE: connect_requests_related_object_filters_input.htm ===
---
page_id: connect_requests_related_object_filters_input.htm
title: Related Object Filters Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_related_object_filters_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Object Filters Input

Input representation of the request to filter related objects.

    
      
        
          

**JSON example**

          
: 
            

```
"relatedObjectFilters": 
[{
   "criteria": [
    {
    "property": "IsCommercial",
    "operator": "eq",
    "value": true
    }
  ],
   "objectName": "ProductSpecificationRecType"
 }]
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `criteria` | [Criteria](./connect_requests_criteria.htm.md)[] | Criteria to filter the related objects. | Required if the `relatedObjectFilters` property is specified. | 60.0 |
| `objectName` | String | API name of the object that’s related to the main object. | Required if the `relatedObjectFilters` property is specified. | 60.0 |

=== ARTICLE: connect_requests_related_object_node_input.htm ===
---
page_id: connect_requests_related_object_node_input.htm
title: Related Object Node Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_related_object_node_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Object Node Input

Input representation of the details of a related object node.

**JSON example**

: 

```
 "relatedObjectNodes": [
    {
      "relatedObjectAPIName": "ProductRampSegment",
      "pageSize": 20,
      "offSet": 0
    },
    {
      "relatedObjectAPIName": "ProductUsageGrant",
      "pageSize": 10,
      "offSet": 0,
      "filter": {
        "criteria": [
          {
            "property": "status",
            "operator": "eq",
            "value": "active"
          },
          {
            "property": "effectivestartdate",
            "operator": "lte",
            "value": "2024-06-25"
          },
          {
            "criteriaType": "CustomWhereCondition",
            "value": "(effectiveenddate = null OR effectiveenddate >= 2024-06-25)"
          }
        ]
      }
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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `filter` | [Criteria](./connect_requests_criteria.htm.md)[] | Criteria to filter records. The supported properties are: `StartDate` `EndDate` `Status` The supported operators are: `eq` `gte` `lte` The supported related object is ProductUsageGrant. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 62.0 |
| `offSet` | Integer | Number of records to skip. The default value is 0. | Optional | 62.0 |
| `pageSize` | Integer | Number of records per page. Valid values are from 1 through 100. If unspecified, the default value is 100. | Optional | 62.0 |
| `relatedObject​APIName` | String | API name of the related object to return the records for. The supported related objects are ProductRampSegment and ProductUsageGrant. | Required | 62.0 |

=== ARTICLE: connect_requests_related_records_input.htm ===
---
page_id: connect_requests_related_records_input.htm
title: Related Records Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_related_records_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Records Input

Input representation of the request to retrieve related ProductRampSegment or
    ProductUsageGrant records for Product2 object.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "recordIds": [
    "01txx0000006i44AAA",
    "01txx0000006i5gAAA"
  ],
  "relatedObjectNodes": [
    {
      "relatedObjectAPIName": "ProductRampSegment",
      "pageSize": 20,
      "offSet": 0
    },
    {
      "relatedObjectAPIName": "ProductUsageGrant",
      "pageSize": 10,
      "offSet": 0,
      "filter": {
        "criteria": [
          {
            "property": "status",
            "operator": "eq",
            "value": "active"
          },
          {
            "property": "effectivestartdate",
            "operator": "lte",
            "value": "2024-06-25"
          },
          {
            "criteriaType": "CustomWhereCondition",
            "value": "(effectiveenddate = null OR effectiveenddate >= 2024-06-25)"
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
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 62.0 |
| `recordIds` | String[] | List of record IDs to return the relatedObjects records for. The maximum number of record IDs supported is 20. | Required | 62.0 |
| `related​ObjectNodes` | [Related Object Node Input](./connect_requests_related_object_node_input.htm.md)[] | List of nodes for the related objects. The maximum number of related object nodes supported is two. | Required | 62.0 |

=== ARTICLE: connect_requests_runtime_catalog_snapshot_input.htm ===
---
page_id: connect_requests_runtime_catalog_snapshot_input.htm
title: Run-time Catalog Snapshot Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_runtime_catalog_snapshot_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Run-time Catalog Snapshot Input

Input representation of the details of a run-time catalog snapshot for
    deployment.

        
          

**JSON example**

          
: 
            

```
  "snapshot": {
    "activationType": "IMMEDIATE",
    "activationDate": "2024-05-06T05:12:59.000Z",
    "id": "1Avxx0000005DFe1AM"
  }
```

          

        

**Properties**

: 

- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `activationDate` | String | Activation date of the snapshot. | Optional | 62.0 |
| `activationType` | String | Activation type of the snapshot. Valid value is: `IMMEDIATE`—Snapshot is activated immediately after a successful build. | Required | 62.0 |
| `id` | String | ID of the snapshot. | Required | 62.0 |

=== ARTICLE: connect_requests_search_products_input.htm ===
---
page_id: connect_requests_search_products_input.htm
title: Products Search Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_search_products_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Products Search Input

Input representation of the request to search products.

          

**JSON example**

          
: This example shows a sample request to search products by using a
            query.

```
{
  "query": {
    "textQuery": {
      "searchPhrase": "firstproduct"
    }
  },
  "catalogId": "0ZSxx0000000001GAA",
  "categoryId": "0ZGT100000000qlOAA",
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "additionalFields": {
    "Product2": {
      "fields": [
        "CustomField1__c",
        "CustomField2__c",
        "StandardField1"
      ]
    }
  }
}
```

          
: This example shows a sample request to search products by using the `searchTerm`
            property.

```
{
  "searchTerm": "Laptop",
  "catalogId": "0ZSDU0000002Og64AE",
  "categoryId": "0ZGDU0000002P0A4AU",
  "correlationId": "d9d8f898-19f5-464a-ba2b-6a070783f6c4",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNw==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001DU000001o2V0YAI"
  }
}
```

If a parent category ID is specified in the request body, then the API
            returns all products associated to all child categories.

          
: This example shows a sample request to search products with eligible promotions. To
            fetch eligible promotions, specify a value for the `query` or `searchTerm` property, and set
            the `usePromotions` property to `true`.

```
{
  "query": {
    "textQuery": {
      "searchPhrase": "laptop"
    }
  },
  "catalogId": "0ZSxx0000000001GAA",
  "categoryId": "0ZGT100000000qlOAA",
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "additionalFields": {
    "Product2": {
      "fields": [
        "CustomField1__c",
        "CustomField2__c",
        "StandardField1"
      ]
    }
  },
  "usePromotions": true
}
```

          
: This example shows a sample request to run visibility
            rules.

```
{
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": true,
  "searchTerm": "128GB LRDIMM",
  "catalogId": "0ZSVW000000AhdC4AS",
  "limit": 12,
  "userContext": {
    "accountId": null
  },
  "priceBookId": "01sVW0000024PZlYAM",
  "currencyCode": "USD",
  "transactionId": "0Q0VW000001190f0AA",
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "orderBy": [
    "name:asc"
  ],
  "executeConfigurationRules": true
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

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Context​Data` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 61.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. If the category ID isn’t specified, then the API returns the matching query offers from the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. | Optional | 60.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains` `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `include​CatalogDetails` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 61.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 60.0 |
| `offset` | Integer | Reserved for internal use. | Optional | 60.0 |
| `orderBy` | String[] | Sort order of the results, which is either ascending or descending order. The default sort order is ascending order. The default value is `asc`. | Optional | 60.0 |
| `priceBookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Optional | 60.0 |
| `pricingProcedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product ClassificationId` | String | ID of the product classification. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `query` | Map<String, Object> | Query to search the products. | Required | 60.0 |
| `related​ObjectFilter` | [Related Object Filter Input](./connect_requests_related_object_filter_input.htm.md)[] | Filter records based on supported criteria for related objects. The supported object is `ProductSpecificationRecType`. The supported property is `IsCommerical`. The supported operator is `eq`. The supported values are `true` and `false`. | Optional | 60.0 |
| `searchTerm` | String | String used to get products with the product name containing the search term. See [Search Considerations When Using Indexed Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_considerations.htm&type=5&language=en_US). | Optional | 62.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 66.0 |
| `transactionId` | String | ID of the transaction. | Optional | 66.0 |
| `usePromotions` | Boolean | Indicates whether to retrieve eligible promotions from Global Promotion Management (GPM) for each product in the search results (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `userContext` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

=== ARTICLE: connect_requests_setting_input.htm ===
---
page_id: connect_requests_setting_input.htm
title: Setting Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_setting_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Setting Input

Input representation of the details of the index setting.

**JSON example**

: 

```
    "setting" : {
        "supportedLanguages" : ["en_US","ja","es","nl_NL"],
        "defaultLanguage" : "en_US"
   }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `default​Language` | String | Default language for the API. | Required | 63.0 |
| `supported​Languages` | String[] | List of supported language locales for indexing. | Required | 63.0 |

=== ARTICLE: connect_requests_snapshot_deployment_input.htm ===
---
page_id: connect_requests_snapshot_deployment_input.htm
title: Snapshot Deployment Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_snapshot_deployment_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Deployment Input

Input representation of the request to deploy a run-time catalog snapshot.

**JSON example**

          
: This example shows a sample request to build a new snapshot with immediate
            activation.

: 

```
{
  "snapshot": {
    "activationType": "IMMEDIATE"
  },
  "buildType": "FULL"
}
```

          
: This example shows a sample request to rebuild a snapshot in the `active` status.

          
: 
            

```
{
  "snapshot": {
    "activationType": "IMMEDIATE",
    "id": "1Avxx0000005DFe1AM"
  },
  "buildType": "FULL"
}
```

          

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `buildType` | String | Build type of the snapshot index. Valid value is: `FULL`—Specifies a full index build. `INCREMENTAL`—Specifies an incremental index build. Available from API version 63.0 and later. | Required | 62.0 |
| `snapshot` | [Run-time Catalog Snapshot Input](./connect_requests_runtime_catalog_snapshot_input.htm.md)[] | Snapshot to deploy. | Required | 62.0 |

=== ARTICLE: connect_requests_sort.htm ===
---
page_id: connect_requests_sort.htm
title: Sort Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sort.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sort Input

Input representation of the sort request.

    
      
        
          

**JSON example**

          
: 
            

```
"sort":
{
"orders": 
[{
"property": "name", 
"direction": "asc"
}] 
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `orders` | [Order](./connect_requests_order.htm.md)[] | Details of the sort order. | Required if the `sort` property is specified. | 60.0 |

=== ARTICLE: connect_requests_user_context_input.htm ===
---
page_id: connect_requests_user_context_input.htm
title: User Context Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_user_context_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# User Context Input

Input representation of the details with the user context.

**JSON example**

: 

```

    "userContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI",
        "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708"
    }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `account​Id` | String | ID of the account in a user context. | Optional | 60.0 |
| `contact​Id` | String | ID of the contact in a user context. | Optional | 60.0 |
| `context​Id` | String | ID of the context that represents the created session. | Optional | 60.0 |

=== ARTICLE: connect_resources_bulk_product_details.htm ===
---
page_id: connect_resources_bulk_product_details.htm
title: Bulk Product Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_bulk_product_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Product Details (POST)

Retrieve details for multiple products. This API is a composite API
      for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/products/bulk
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/products/bulk
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
  "productData": [
    {
      "productId": "01txx0000006ivJAAQ",
      "productSellingModelId": "0jPxx000000009hEAA"
    },
    {
      "productId": "01txx0000006ivLAAQ",
      "productSellingModelId": "0jPxx000000009iEAABB"
    }
  ],
  "correlationId": "de9a674c-1807-438c-ac78-2c96f4655325",
  "priceBookId" : "01sxx0000005qxxAAA",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
  }
}
```

This example shows a sample request with proration policy details requested through the
              `additionalFields`
            property.

```
{
  "additionalFields": {
    "ProductSellingModelOption": {
      "additionalFields": {
        "ProrationPolicy": {
          "fields": [
            "ArePartialPeriodsAllowed",
            "ProrationPolicyType"
          ]
        }
      }
    }
  },
  "productData": [
    {
      "productId": "01txx0000006ivJAAQ",
      "productSellingModelId": "0jPxx000000009hEAA"
    },
    {
      "productId": "01txx0000006ivLAAQ",
      "productSellingModelId": "0jPxx000000009iEAABB"
    }
  ],
  "correlationId": "de9a674c-1807-438c-ac78-2c96f4655325",
  "priceBookId": "01sxx0000005qxxAAA",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes to add to the custom or default context definition. This data is appended to the context input and sent for hydration and qualification. The maximum limit of supported nodes is 10. | Optional | 61.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. The field values are returned in the response for each of the products. In API version 66.0 and later, you can request proration policy details in the response for each product selling model option through this property. | Optional | 61.0 |
| `context​Definition` | String | Name of the custom context definition that’s sent for the context creation. If unspecified, the default context definition is used. | Optional | 61.0 |
| `context​Mapping` | String | Context mapping details from the context definition. If specified, the API validates if the context mapping belongs to the specified context definition and considers the mapping for hydration. If unspecified, the default context mapping of the context definition is used. | Optional | 61.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 61.0 |
| `currency​Code` | String | Currency code to consider for pricing and filtering. | Optional | 61.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 61.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 61.0 |
| `price​BookId` | String | ID of the price book to fetch the prices from. | Optional | 61.0 |
| `pricing​Procedure` | String | Name of the custom pricing procedure to send for processing. If unspecified, the default pricing procedure is executed. | Optional | 61.0 |
| `product​Data` | [Product Data Input](./connect_requests_product_data_input.htm.md)[] | List of maps that contain product IDs and product selling model IDs. | Required | 61.0 |
| `qualification​Procedure` | String | Name of the custom qualification procedure to send for processing. If unspecified, the default qualification procedure is executed. | Optional | 61.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md)[] | User context details. For example, account ID or contact ID. | Optional | 61.0 |

          

        
        
          

**Response body for POST**

          
: [Bulk Product Details](./connect_responses_cpq_base_bulk_details_output.htm.md)

=== ARTICLE: connect_resources_catalog_details.htm ===
---
page_id: connect_resources_catalog_details.htm
title: Catalog Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_catalog_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog Details (POST)

Get catalog details for a specified catalog ID. This API is a
      composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/catalogs/catalogId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/catalogs/0ZSxx000000009hGAA
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
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
     "accountId": "001xx0000000001AAA",
     "contactId": "003xx00000000D7AAI"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [CPQ Base
              Details](./connect_responses_cpq_base_details_output.htm.md)

=== ARTICLE: connect_resources_catalog_list.htm ===
---
page_id: connect_resources_catalog_list.htm
title: Catalog List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_catalog_list.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog List (POST)

Get a paginated list of catalogs. This API is a composite API for
      Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/catalogs
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/catalogs
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
    "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
    "limit": 10,
    "offset": 0,
    "orderBy": [
        "name:asc",
        "id:desc"
    ],
    "userContext": {
        "accountId": "001xx0000000001AAA",
        "contactId": "003xx00000000D7AAI"
    }
    }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `limit` | Integer | Number of items to include in the response. | Optional | 60.0 |
| `offset` | Integer | Offset size from which to get the catalog count. | Optional | 60.0 |
| `order​By` | String[] | Sort order for the catalogs. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)

=== ARTICLE: connect_resources_categories_list.htm ===
---
page_id: connect_resources_categories_list.htm
title: Categories List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_categories_list.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Categories List (POST)

Get a list of categories and subcategories of a specified catalog.
      This API is a composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/categories
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/categories
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
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx000000009hGAA",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
    }
}
```

This example shows a sample request to get a list of categories with eligible
            promotions.

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx000000009hGAA",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "usePromotions": true
}
```

        
      

          

        
        
          

**Response body for POST**

          
: [CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)

=== ARTICLE: connect_resources_category_details.htm ===
---
page_id: connect_resources_category_details.htm
title: Category Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_category_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category Details (POST)

Get details of a category for a specified category ID. This API is a
      composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/categories/categoryId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/categories/0ZGxx000000001dGAA
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
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
      "accountId": "001xx0000000001AAA",
      "contactId": "003xx00000000D7AAI"
  }
}
```

This example shows a sample request to get category details with eligible
            promotions.

```
{
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "usePromotions": true
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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md) | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `customFields` | String[] | List of category fields to retrieve in the response. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the categories (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains` `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |
| `usePromotions` | Boolean | Indicates whether to fetch eligible promotions from Global Promotion Management (GPM) for the requested category and its products (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [CPQ Base Details](./connect_responses_cpq_base_details_output.htm.md)

=== ARTICLE: connect_resources_cpq_qualification.htm ===
---
page_id: connect_resources_cpq_qualification.htm
title: Qualification (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_cpq_qualification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Qualification (POST)

Run the qualification procedure on a list of product IDs. This API
      is a composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/qualification
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/qualification
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
  "productIds": [
    "01txx0000006i7PAAQ",
    "01txx0000006i7QAAQ",
    "01txx0000006i7IAAQ"
  ],
  "userContext": {
    "accountId": "001xx000003GZHgAAO"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `catalog​Id` | String | ID of the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `product​Ids` | String[] | List of product IDs for qualification check. | Required | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s sent for processing. If this property isn’t specified, the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)

=== ARTICLE: connect_resources_deep_clone.htm ===
---
page_id: connect_resources_deep_clone.htm
title: Deep Clone (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_deep_clone.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone (POST)

Copy related records of an object along with the main product
      record.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/deep-clone
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/deep-clone
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "mainRecordId": "01tSG0000028kcSYAQ",
  "mainObjectApiName": "Product2",
  "mainRecordFieldValues": {
    "Name": "New Cloud Storage"
  }
}
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `mainObject​ApiName` | String | API name of the object. The supported object is Product2. | Required | 63.0 |
| `mainRecord​Field​Values` | Map<String, String> | Mapping of the API name of the field to its value. The values passed through this map are set for the created record. You can pass the Name field only through this map. | Optional | 63.0 |
| `mainRecord​Id` | String | ID of the record. | Required | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Deep Clone
              Response](./connect_responses_deep_clone_response.htm.md)

=== ARTICLE: connect_resources_get_catalogs.htm ===
---
page_id: connect_resources_get_catalogs.htm
title: Catalog List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_catalogs.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog List (POST)

Retrieve, search, filter, or sort catalog
    records.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/catalogs
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/catalogs
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
          
          
: POST

#### Note

The POST method is used to retrieve the catalog records instead of the GET
              method as a request payload is sent to filter the
          records.

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: This example shows how to retrieve catalogs that contain `apple` in the catalog name.

: 

```
{
"pageSize": 100,
"offset": 0,
"language": "french",
"filter": {
"criteria": [
{
"property": "name",
"operator": "contains",
"value": "apple"
}
]
}
}
```

          
: This example shows how to retrieve catalogs with `ServiceProcess` as the catalog type.

          
: 
            

```
{
"pageSize": 100,
"offset": 0,
"sort": {
  "orders": [
   {
   "property": "name",
   "direction": "desc"
   }
  ]
 },
"filter": {
"criteria": [
{
"property": "catalogType",
"operator": "eq",
"value": "ServiceProcess"
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

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `filter` | [Filter](./connect_requests_criteria.htm.md) | Criteria to filter the records. Filters are applicable to the fields of the ProductCatalog object. The supported operators are: `eq` `in` `contains` The supported properties are `name` and `catalogType`. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 60.0 |
| `page​Size` | Integer | Number of records per page. Valid values are from 1 through 100. If unspecified, defaults to 100. | Optional | 60.0 |
| `sort` | [Sort](./connect_requests_order.htm.md) | Sort order of the catalog records. The supported operators are: `asc` `desc` | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Catalogs Output](./connect_responses_catalogs_output.htm.md)

=== ARTICLE: connect_resources_get_catalogs_by_ID.htm ===
---
page_id: connect_resources_get_catalogs_by_ID.htm
title: Catalog By ID (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_catalogs_by_ID.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog By ID (GET)

Retrieve details of catalog records based on a catalog
      ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/catalogs/catalogId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/catalogs/0ZST100000000kUOAQ
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/catalogs/0ZST100000000kUOAQ?language=spanish
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `fields` | String[] | For internal use only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |

          

        
        
          

**Response body for GET**

          
: [Catalogs Output](./connect_responses_catalogs_output.htm.md)

=== ARTICLE: connect_resources_get_categories.htm ===
---
page_id: connect_resources_get_categories.htm
title: Categories List (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_categories.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Categories List (GET)

Retrieve the root-level categories of a catalog based
      on a catalog ID, or subcategories based on a parent category. You can also search, filter, or
      sort the categories.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/catalogs/catalogId/categories
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/catalogs/0ZST100000000kUOAQ/categories
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/catalogs/0ZST100000000kUOAQ/categories?language=spanish
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `depth` | Integer | Number of levels in the category hierarchy to return. The default value is 1. | Optional | 60.0 |
| `fields` | String[] | For internal use only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `parent​Category​Id` | String | ID of the category to fetch the associated hierarchy of subcategories. If unspecified, then the root-level categories are returned. | Optional | 60.0 |

          

        
        
          

**Response body for GET**

          
: [Categories Output](./connect_responses_categories_output.htm.md)

=== ARTICLE: connect_resources_get_category_by_ID.htm ===
---
page_id: connect_resources_get_category_by_ID.htm
title: Category By ID (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_category_by_ID.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category By ID (GET)

Retrieve details of individual category records based
      on a category ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/categories/categoryId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/categories/0ZGT100000000qqOAA
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/categories/0ZGT100000000qqOAA?language=spanish
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `fields` | String[] | For internal use only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |

          

        
        
          

**Response body for GET**

          
: [Categories Output](./connect_responses_categories_output.htm.md)

=== ARTICLE: connect_resources_get_index_errors.htm ===
---
page_id: connect_resources_get_index_errors.htm
title: Snapshot Index Error (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_index_errors.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Index Error (GET)

Get the count and details of the errors that occurred during the
      indexing process.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/index/error
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/error
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `indexId` | String | ID of the index. | Required | 63.0 |
| `snapshot​IndexId` | String | ID of the snapshot index. | Required | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Snapshot Index
              Error](./connect_responses_snapshot_index_error_output.htm.md)

=== ARTICLE: connect_resources_get_index_settings.htm ===
---
page_id: connect_resources_get_index_settings.htm
title: Index Setting (GET, PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_index_settings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Setting (GET, PATCH)

Fetch and update settings related to indexing and
    search.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/index/setting
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/setting
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET, PATCH

        
        
          

**Response body for GET**

          
: [Index Setting
              Results](./connect_responses_index_setting_output.htm.md)

        
        
          

**Request body for PATCH**

          
: 
            

**JSON example**

: 

```
{
    "setting" : {
        "supportedLanguages" : ["en_US","ja","es","nl_NL"],
        "defaultLanguage" : "en_US",
        "productsGrouping": "GROUPING_VARIATION"
   }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `setting` | [Setting Input](./connect_requests_setting_input.htm.md)[] | Object containing the setting-related details. | Required | 63.0 |

          

        
        
          

**Request parameters for PATCH**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `settingId` | String | ID of the setting to update the details for. | Required | 63.0 |

          

        
        
          

**Response body for PATCH**

          
: [Index Setting
              Update](./connect_responses_index_setting_patch_output.htm.md)

=== ARTICLE: connect_resources_get_product_by_ID.htm ===
---
page_id: connect_resources_get_product_by_ID.htm
title: Product Details (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_product_by_ID.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Details (GET)

Retrieve details of individual product records or a
      bundle based on a product ID.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/products/productId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products/01tT1000000F0afIAC
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products/01tT1000000F0afIAC?language=spanish
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products/01tT1000000F0afIAC/catalogSystems=epc
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: GET

          
: 

#### Note

You must invoke this API request by using GET method only. If the request is invoked by using
              POST method, the request is considered as a  [Products List](./connect_resources_get_products.htm.md) API request.

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalogSystems` | String[] | Name of the catalog system. Valid values are: `epc`—Enterprise Product Catalog `pcm`—Product Catalog Management Although this parameter accepts a list, you can pass only one value. If you don’t specify a value, the default behavior is to fetch data from the `pcm` catalog. | Optional | 66.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `fields` | String[] | For internal use only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |

          

        
        
          

**Response body for GET**

          
: [Products](./connect_responses_products_output.htm.md)

=== ARTICLE: connect_resources_get_products.htm ===
---
page_id: connect_resources_get_products.htm
title: Products List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_products.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Products List (POST)

Retrieve products. You can also search, filter, or sort
      the products.

    

        
          

**Resource**

          
: 
            

```
/connect/pcm/products
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products?productClassificationId=11BT10000004C9SMAU
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

#### Note

POST methods typically create an item, but for this resource POST is used to
              retrieve information.

        
      

        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: This example is a search request for products that contain `Bundle Product` in the product
            name.

```
{
  "catalogIds": [
    "0ZST10000004D03OAE"
  ],
  "language": "spanish",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "contains",
        "value": "Bundle Product"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": false
        }
      ],
      "additionalFields": {
        "Product2": {
          "fields": [
            "code__c"
          ]
        }
      }
    }
  ]
}
```

          
: This example is a search request for products that contain the specified search term
            in the product name and are part of a
            catalog.

```
  {
  "catalogIds": [
    "0ZSDU0000002Og54AE"
  ],
  "searchTerm": "Slack"
}
```

        
          

**Query parameters**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `product​Classification​Id` | String | ID of the product classification template that contains a collection of dynamic attributes and can be reused to create multiple products. Products that are based on a product classification inherit all the attributes of the product classification. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |

          

        

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

- 
- 
- 
- 
- 
- 
- 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Map of the object and the list of standard and custom fields to be queried along with the standard response. The supported object is Product2. | Optional | 61.0 |
| `catalog​Ids` | List<String> | List of comma-separated catalog IDs. The API returns the list of product records that are associated with the specified catalog IDs. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |
| `category​Ids` | List<String> | List of comma-separated category IDs. The API returns the list of product records that are associated with the specified category IDs. If unspecified, then returns all products that are added to at least one category. Specify either the product classification ID, list of category IDs, or list of catalog IDs to retrieve products. | Optional | 60.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 60.0 |
| `filter` | [Criteria Input](./connect_requests_criteria.htm.md) | Criteria to filter the records. Filters are applicable to the fields of Product2 object. The supported operators are: `eq` `in` `contains`—This value isn’t applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the criteria are combined by using the `and` operator. The supported properties are `name`, `description`, and `isActive`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then the supported property is `name` only. | Optional | 60.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 60.0 |
| `pageSize` | Integer | Specifies the number of records per page. Valid values are from 1 through 200. If the value is unspecified, it defaults to 100. | Optional | 60.0 |
| `related​Object​Filters` | [Related Object Filter](./connect_requests_related_object_filters_input.htm.md)[] | Criteria for the related objects to filter the records. The supported operator is `eq`. The supported object is `ProductSpecificationRecType`. The supported values are `true` and `false`. The supported property is `IsCommercial`. | Optional | 60.0 |
| `searchTerm` | String | String used to get products with the product name containing the search term. See [Search Considerations When Using Indexed Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_considerations.htm&type=5&language=en_US). | Optional | 62.0 |
| `sort` | [Sort](./connect_requests_order.htm.md) | Sort order for the products. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [Products Output](./connect_responses_products_output.htm.md)

=== ARTICLE: connect_resources_global_search.htm ===
---
page_id: connect_resources_global_search.htm
title: Global Search (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_global_search.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Global Search (POST)

Retrieves a list of products based on a search query or search term.
      This API is a composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/products/search
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/products/search
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
          

**JSON example**

          
: This example shows a sample request to search products by using a
            query.

```
{
  "query": {
    "textQuery": {
      "searchPhrase": "firstproduct"
    }
  },
  "catalogId": "0ZSxx0000000001GAA",
  "categoryId": "0ZGT100000000qlOAA",
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "additionalFields": {
    "Product2": {
      "fields": [
        "CustomField1__c",
        "CustomField2__c",
        "StandardField1"
      ]
    }
  }
}
```

          
: This example shows a sample request to search products by using the `searchTerm`
            property.

```
{
  "searchTerm": "Laptop",
  "catalogId": "0ZSDU0000002Og64AE",
  "categoryId": "0ZGDU0000002P0A4AU",
  "correlationId": "d9d8f898-19f5-464a-ba2b-6a070783f6c4",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNw==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001DU000001o2V0YAI"
  }
}
```

If a parent category ID is specified in the request body, then the API
            returns all products associated to all child categories.

          
: This example shows a sample request to search products with eligible promotions. To
            fetch eligible promotions, specify a value for the `query` or `searchTerm` property, and set
            the `usePromotions` property to `true`.

```
{
  "query": {
    "textQuery": {
      "searchPhrase": "laptop"
    }
  },
  "catalogId": "0ZSxx0000000001GAA",
  "categoryId": "0ZGT100000000qlOAA",
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc",
    "id:desc"
  ],
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "additionalFields": {
    "Product2": {
      "fields": [
        "CustomField1__c",
        "CustomField2__c",
        "StandardField1"
      ]
    }
  },
  "usePromotions": true
}
```

          
: This example shows a sample request to run visibility
            rules.

```
{
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": true,
  "searchTerm": "128GB LRDIMM",
  "catalogId": "0ZSVW000000AhdC4AS",
  "limit": 12,
  "userContext": {
    "accountId": null
  },
  "priceBookId": "01sVW0000024PZlYAM",
  "currencyCode": "USD",
  "transactionId": "0Q0VW000001190f0AA",
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "orderBy": [
    "name:asc"
  ],
  "executeConfigurationRules": true
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

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Context​Data` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 61.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. If the category ID isn’t specified, then the API returns the matching query offers from the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. | Optional | 60.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains` `gt`—Specifies a greater than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lt`—Specifies a less than criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `gte`—Specifies a greater than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. `lte`—Specifies a less than or equal to criteria. Available from API version 63.0 and later for Number, Date, and Datetime data types only. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `include​CatalogDetails` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 61.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 60.0 |
| `offset` | Integer | Reserved for internal use. | Optional | 60.0 |
| `orderBy` | String[] | Sort order of the results, which is either ascending or descending order. The default sort order is ascending order. The default value is `asc`. | Optional | 60.0 |
| `priceBookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Optional | 60.0 |
| `pricingProcedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product ClassificationId` | String | ID of the product classification. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `query` | Map<String, Object> | Query to search the products. | Required | 60.0 |
| `related​ObjectFilter` | [Related Object Filter Input](./connect_requests_related_object_filter_input.htm.md)[] | Filter records based on supported criteria for related objects. The supported object is `ProductSpecificationRecType`. The supported property is `IsCommerical`. The supported operator is `eq`. The supported values are `true` and `false`. | Optional | 60.0 |
| `searchTerm` | String | String used to get products with the product name containing the search term. See [Search Considerations When Using Indexed Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_considerations.htm&type=5&language=en_US). | Optional | 62.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 66.0 |
| `transactionId` | String | ID of the transaction. | Optional | 66.0 |
| `usePromotions` | Boolean | Indicates whether to retrieve eligible promotions from Global Promotion Management (GPM) for each product in the search results (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `userContext` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)

=== ARTICLE: connect_resources_guided_product_selection.htm ===
---
page_id: connect_resources_guided_product_selection.htm
title: Guided Selection (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_guided_product_selection.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guided Selection (POST)

Retrieve a list of products based on the response identifier or search
      terms of a guided selection. Guided selection captures user requirements to show suitable
      products.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/products/guided-selection
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/products/guided-selection
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
  "correlationId": "corrId",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "pricebookId",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "userContext": {
    "accountId": "accId"
  },
  "guidedSelectionResponseId": "ABCxx0000000001GAA",
  "searchTerms": [
    {
      "term": "IPhone",
      "tags": [
        "deviceType",
        "mobile"
      ]
    },
    {
      "term": "4GB",
      "tags": [
        "RAM"
      ]
    },
    {
      "term": "64GB",
      "tags": [
        "Storage"
      ]
    }
  ],
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": false
}
```

          

          
: This example shows a sample request to fetch eligible
            promotions.

```
{
  "correlationId": "corrId",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "pricebookId",
  "limit": 10,
  "cursor": "MTAwMDAwMDAwNg==",
  "userContext": {
    "accountId": "accId"
  },
  "guidedSelectionResponseId": "ABCxx0000000001GAA",
  "searchTerms": [
    {
      "term": "IPhone",
      "tags": [
        "deviceType",
        "mobile"
      ]
    },
    {
      "term": "4GB",
      "tags": [
        "RAM"
      ]
    },
    {
      "term": "64GB",
      "tags": [
        "Storage"
      ]
    }
  ],
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": false,
  "transactionContextId": "context123",
  "transactionId": "trans456",
  "usePromotions": true
}
```

          
: This example shows a sample request to run visibility
            rules.

```
{
  "catalogId": "0ZSVW000000AhdC4AS",
  "currencyCode": "USD",
  "enablePricing": true,
  "enableQualification": true,
  "executeConfigurationRules": true,
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "guidedSelectionResponseId": "0U3VW0000000a1t0AA",
  "includeCatalogDetails": true,
  "limit": 12,
  "offset": 0,
  "orderBy": [
    "name:asc"
  ],
  "priceBookId": "01sVW0000024PZlYAM",
  "transactionId": "0Q0VW000001190f0AA",
  "userContext": {
    "accountId": null
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
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 62.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 62.0 |
| `catalog​Id` | String | ID of the catalog. | Required | 62.0 |
| `category​Id` | String | ID of the category. | Optional | 62.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 62.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 62.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 62.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the `currencyCode` property is required. | Optional | 62.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 62.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`. | Optional | 62.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 62.0 |
| `guided​Selection​ResponseId` | String | Response identifier of the guided selection. | Required if the `searchTerms` property isn’t specified. | 62.0 |
| `include​Catalog​Details` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 62.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 62.0 |
| `order​By` | String[] | Sort order of the results, which is either ascending (`asc`) or descending order (`desc`). The default sort order is ascending order. The default value is `asc`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 62.0 |
| `price​BookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Required | 62.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 62.0 |
| `product​Classification​Id` | String | ID of the product classification. | Optional | 62.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 62.0 |
| `searchTerms` | [Guided Selection Search Term Input](./connect_requests_guided_selection_search_term_input.htm.md)[] | Search terms of the guided selection. | Required if the `guided​Selection​ResponseId` property isn’t specified. | 62.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 67.0 |
| `transactionId` | String | ID of the transaction. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for the guided selection (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 62.0 |

If both the `guided​Selection​ResponseId` and
                `searchTerms` properties are specified, then the
                `searchTerms` property is considered in the input
              request.

          

        
        
          

**Response body for POST**

          
: [Guided
              Selection](./connect_responses_guided_selection_output.htm.md)

=== ARTICLE: connect_resources_index_configuration.htm ===
---
page_id: connect_resources_index_configuration.htm
title: Index Configuration Collection (GET, PUT)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_index_configuration.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configuration Collection (GET, PUT)

Retrieve the saved index configurations. Additionally, you can persist
      the index configuration.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/index/configurations
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/configurations
```

          

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/configurations?includeMetadata=false&fieldTypes=Standard,Custom
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET, PUT

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 62.0 |
| `field​Types` | String[] | Filters and returns only the persisted index configurations, based on the index configuration type specified in the query parameters. The supported types of filters are: `STANDARD` `CUSTOM` `ProductDynamicAttribute` `ProductAttributeDefinitionStandard` `ProductAttributeDefinitionCustom` | Optional | 62.0 |
| `include​Metadata` | Boolean | Indicates whether to include metadata (`true`) or not (`false`). | Optional | 62.0 |

          

        
        
          

**Response body for GET**

          
: [Index Configuration
              Collection](./connect_responses_index_configuration_collection_output.htm.md)

        
        
          

**Request body for PUT**

          
: 
            

**JSON example**

: 

```
{
  "correlationId": "8545b5aa-f3e6-429a-8f21-9cc4ce50b1d7",
  "indexConfigurations": [
    {
      "attributeDefinitionId": "0tjT1000000002bIAA",
      "name": "Color",
      "type": "ProductDynamicAttribute",
      "isSearchable": true
    },
    {
      "attributeFieldId": "00Nxx000001FwnABII",
      "name": "Message__c",
      "type": "Custom",
      "isSearchable": true
    },
    {
      "name": "Code",
      "type": "Standard",
      "isSearchable": true
    },
    {
      "facetDisplayRank": 1,
      "isFacetable": false,
      "isSearchable": true,
      "name": "Family",
      "type": "Standard"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 62.0 |
| `index​Configurations` | [Index Configuration Input](./connect_requests_index_configuration_input.htm.md)[] | List of index configurations. | Required | 62.0 |

          

        
        
          

**Response body for PUT**

          
: [Index Configurations
              Update](./connect_responses_index_configurations_update_output.htm.md)

=== ARTICLE: connect_resources_product_catalog_bulk_product_details.htm ===
---
page_id: connect_resources_product_catalog_bulk_product_details.htm
title: Bulk Product Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_catalog_bulk_product_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Product Details (POST)

Retrieve details for multiple products.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/products/bulk
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products/bulk
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
  "correlationId": "cbfabffb-093f-45b3-8c2d-88b4acbd4867",
  "productIds": [
    "01tT1000000F0afIAC",
    "01tT1000000F0afIAC"
  ],
  "uptoLevel": 1,
  "language": "french",
  "additionalFields": {
    "Product2": {
      "fields": [
        "code__c"
      ]
    },
    "ProductAttributeDefinition": {
      "fields": [
        "scope"
      ]
    }
  }
}
```

          

          
: This example shows a sample request to fetch data from Enterprise Product
            Catalog.

```
{
  "productIds": [
    "01tLT000009vGXfYAM"
  ],
  "catalogSystems": [
    "epc"
  ],
  "additionalFields": {
    "AttributeDefinition": {
      "fields": [
        "OptOutAssetization",
        "OptOutDecompositionAction",
        "OptOutSupplementalAction"
      ]
    }
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

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Map of object and list of additional standard or custom fields to be included in the response. The supported objects are: Product2 ProductAttributeDefinition—If the fields defined for the ProductAttributeDefinition object aren’t available for the ProductClassificationAttr object, then the API request fails. If the Dynamic Revenue Orchestrator permission is enabled, then this property supports AttributeDefinition as key with these supported values. `OptOutAssetization` `OptOutDecompositionAction` `OptOutSupplementalAction` | Optional | 61.0 |
| `catalogSystems` | String[] | Name of the catalog system. Valid values are: `epc`—Enterprise Product Catalog `pcm`—Product Catalog Management Although this property accepts a list, you can pass only one value. If you don’t specify a value, the default behavior is to fetch data from the `pcm` catalog. | Optional | 66.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 61.0 |
| `language` | String | Custom language that you can specify to get translated data for the fields of an object that's enabled for translation. See [Translate Product and Product Category Data](https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&language=en_US). | Optional | 64.0 |
| `product​Ids` | String[] | List of product IDs that details must be returned for. If any product ID is blank, invalid, or not found, then the request is processed with valid and available product IDs. | Required | 61.0 |
| `upto​Level` | Integer | Hierarchy level to follow to return the product details. For a bundle, this property determines the number of levels of child components to be returned. You can specify up to a hierarchy level of 1. If unspecified, the default level is the full bundle hierarchy. | Optional | 61.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Products Output](./connect_responses_products_output.htm.md)

=== ARTICLE: connect_resources_product_classification.htm ===
---
page_id: connect_resources_product_classification.htm
title: Product Classification Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_classification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification Details (POST)

Retrieve the details for a list of product classification
      records.

    
      

This API fetches metadata, attributes, and attribute categories associated with product
        classifications across supported catalog systems.

    

    
      
        
          

**Resource**

          
: 
            

```
/revenue/product-catalog-management/product-classifications/details
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/product-catalog-management/product-classifications/details
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
  "productClassificationIds": [
    "01txx0000006iFMAAY",
    "01txx0000006iGxAAY"
  ],
  "catalogSystems": [
    "epc"
  ]
}
```

**Properties**

: 

- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `catalogSystems` | String[] | Name of the catalog system. Valid value is: `epc`—Enterprise Product Catalog | Optional | 66.0 |
| `product​ClassificationIds` | String[] | List of product classification IDs for which you want to retrieve product details. In the `epc` catalog system, these values are the `Product2` record IDs. | Required | 66.0 |

          

        
        
          

**Response body for POST**

          
: [Product Classification Details
              Collection](./connect_responses_product_classification_details_collection_output.htm.md)

=== ARTICLE: connect_resources_product_classification_list.htm ===
---
page_id: connect_resources_product_classification_list.htm
title: Product Classification List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_classification_list.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification List (POST)

Retrieve a list of product classification records. You can also
    search, filter, or sort the product classifications.

    
      

This API retrieves a paginated list of product classification records from the Product
        Catalog Management (PCM) or Enterprise Product Catalog (EPC) catalog system. You can search
        for product classifications by name, apply filters, and sort the results.

    

    
      
        
          

**Resource**

          
: 
            

```
/revenue/product-catalog-management/product-classifications/list
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/product-catalog-management/product-classifications/list
```

          

        
        
          

**Available version**

          
: 67.0

        
        
          

**HTTP methods**

          
: POST

#### Note

POST methods typically create an item, but for this resource POST is used to
              retrieve information.

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "catalogSystem": "pcm",
  "searchTerm": "Mobile",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "contains",
        "value": "Mobile"
      }
    ]
  },
  "sort": {
    "orders": [
      {
        "property": "name",
        "direction": "asc"
      }
    ]
  },
  "pageSize": 25,
  "offset": 0
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
| `catalogSystem` | String | Name of the catalog system. Valid values are: `pcm`—Product Catalog Management `epc`—Enterprise Product Catalog If unspecified, the default catalog system is `pcm`. | Optional | 67.0 |
| `filter` | [Criteria Input](./connect_requests_criteria.htm.md) | Criteria to filter the product classification records. The supported property is `name`. The supported operators are: `eq` `in` `contains` If multiple criteria are specified, they're combined by using the `and` operator. Each criterion supports only the `property`, `operator`, and `value` fields. | Optional | 67.0 |
| `offset` | Integer | Number of records to skip. The default value is 0. | Optional | 67.0 |
| `pageSize` | Integer | Specifies the number of records per page. Valid values are 5, 10, 25, 50, and 100. If unspecified, the default value is 100. | Optional | 67.0 |
| `searchTerm` | String | String used to search for product classifications with the product classification name containing the search term. | Optional | 67.0 |
| `sort` | [Order Input](./connect_requests_order.htm.md) | Sort order for the product classifications. If unspecified, the default sort order is by name in ascending order. | Optional | 67.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Product Classification List
              Collection](./connect_responses_product_classification_list_collection_output.htm.md)

=== ARTICLE: connect_resources_product_details.htm ===
---
page_id: connect_resources_product_details.htm
title: Product Details (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Details (POST)

Get product details, such as attributes, hierarchy, or cardinality,
      for a specified product ID. This API is a composite API for Product
    Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/products/productId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/products/01txx0000006j08AAA
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
  "correlationId": "9cbb9650-48c5-11ed-96d1-0afcf185843b",
  "catalogId": "0ZSxx0000000001GAA",
  "priceBookId": "01s26000002ZT71AAG",
  "productSellingModelId": "0jP1Q000000CaVFUA0",
  "userContext": {
    "accountId": "001xx0000000001AAA",
    "contactId": "003xx00000000D7AAI"
  },
  "enablePricing": true,
  "enableQualification": true,
  "qualificationProcedure": "QualificationProcedure",
  "pricingProcedure": "Preview",
  "contextDefinition": "TestDefinition",
  "contextMapping": "TestDefinitionNode",
  "additionalFields": {
    "ProductSellingModelOption": {
      "additionalFields": {
        "ProrationPolicy": {
          "fields": [
            "ArePartialPeriodsAllowed",
            "ProrationPolicyType"
          ]
        }
      }
    },
    "Product2": {
      "fields": [
        "field1",
        "field2"
      ]
    },
    "ProductAttributeDefinition": {
      "fields": [
        "field3",
        "field4"
      ]
    }
  },
  "additionalContextData": [
    {
      "nodeName": "Contract",
      "nodeData": {
        "id": "xxxxx231",
        "name": "Contract1"
      }
    },
    {
      "nodeName": "Lead",
      "nodeData": {
        "id": "lllllll31",
        "name": "Lead1"
      }
    }
  ]
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Context​Data` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields to include in the response.The supported objects are: Product2 ProductAttributeDefinition—If the fields defined for the ProductAttributeDefinition object aren’t available for the ProductClassificationAttr object, then the API request fails. In API version 66.0 and later, you can request proration policy details in the response for each product selling model option through this property. | Optional | 61.0 |
| `catalogId` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier value that’s attached to the requests and messages, and accepts references to a particular transaction or event chain. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the currencyCode property is required. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `priceBook​Id` | String | ID of the price book to fetch the prices from. If this property isn’t specified, then the prices from the standard price book are fetched. | Required | 60.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product​SellingModel​Id` | String | ID of the product selling model. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
        
          

**Response body for POST**

          
: [CPQ Base Details](./connect_responses_cpq_base_details_output.htm.md)

=== ARTICLE: connect_resources_product_recommendations.htm ===
---
page_id: connect_resources_product_recommendations.htm
title: Product Recommendations (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_recommendations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Recommendations (POST)

Get a list of recommended products based on your underlying business
      rules.

    

This API returns a list of products based on the current quote or order and applicable constraint
        rules, along with the recommendation reasons and compatibility indicators. This enables
        sales reps to define accurate and complete, quoting process, minimizing both manual effort
        and errors.

        
          

**Resource**

          
: 
            

```
/revenue/product-discovery/products/recommendations
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v67.0/revenue/product-discovery/products/recommendations
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
  "currencyCode": "USD",
  "enablePricing": true,
  "enableQualification": true,
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "isQualified",
        "operator": "eq",
        "value": true
      }
    ]
  },
  "limit": 12,
  "priceBookId": "01sSG00000DQCjhYAH",
  "transactionId": "0Q0SG0000014Ui50AE"
}
```

**Properties**

: 

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additionalContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 67.0 |
| `additionalFields` | Map<String, [AdditionalFieldsInputRepresentation](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 67.0 |
| `catalogId` | String | ID of the catalog to fetch the recommended products from. | Optional | 67.0 |
| `contextDefinition` | String | API name of the custom context definition that’s sent for context creation. If you don’t specify this property, then the default context definition is used. | Optional | 67.0 |
| `contextMapping` | String | Default context mapping of the context definition. If you specify a context mapping, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 67.0 |
| `currencyCode` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled in the org, then the `currencyCode` property is required. If you don’t specify a currency code, then the value is fetched from the account. | Optional | 67.0 |
| `cursor` | String | Unique ID to represent the position of each product in the data set. | Optional | 67.0 |
| `enablePricing` | Boolean | Indicates whether to enable pricing for products in orgs where Salesforce Pricing is enabled (`true`) or not (`false`). Set the value to `false` to skip the execution of Salesforce Pricing. In orgs where Salesforce Pricing is disabled, you can’t override this value to `true`. The default value is `true`. | Optional | 67.0 |
| `enableQualification` | Boolean | Indicates whether to enable qualification rules for products in orgs where Qualification Procedure is enabled (`true`) or not (`false`). Set the value to `false` to skip the execution of Business Rules Engine qualification rules. In orgs where Qualification Procedure is disabled, you can’t override this value to `true`. The default value is `true`. | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md)[] | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If you specify multiple criteria, then the resultant criteria are combined by using the `and` operator. | Optional | 67.0 |
| `limit` | Integer | Number of recommended products to include in the response. The default value is `10`. | Optional | 67.0 |
| `priceBookId` | String | ID of the price book to get prices from. If you don’t specify a price book ID, then prices from the standard price book are fetched. | Optional | 67.0 |
| `pricingProcedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If you don’t specify this property, then the default pricing procedure is executed. | Optional | 67.0 |
| `qualificationProcedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If you don’t specify this property, then the default qualification procedure is executed. | Optional | 67.0 |
| `transactionContextId` | String | ID of the sales transaction context instance. | Optional | 67.0 |
| `transactionId` | String | ID of the quote or order. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for the guided selection (`true`) or not (`false`). The default value is `false`. | Optional | 67.0 |
| `userContext` | [User Context Input](./connect_requests_user_context_input.htm.md)[] | User context details. For example, account ID or contact ID. | Optional | 67.0 |

          

        
        
          

**Response body for POST**

          
: [Product
              Recommendations](./connect_responses_product_recommendation_output.htm.md)

=== ARTICLE: connect_resources_product_variants.htm ===
---
page_id: connect_resources_product_variants.htm
title: Product Variants (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_product_variants.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Variants (POST)

Retrieve the variation product associated with one or more parent
      variant products.

    
      

A parent variant product is a non-purchasable product that groups related variations. Use
        this API to retrieve the mapping between parent variant product IDs and their associated
        variation product IDs.

    

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/products/variants
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/products/variants
```

          

        
        
          

**Available version**

          
: 67.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
: POST

#### Note

POST methods typically create an item, but for this resource POST is used to
              retrieve information.

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "9b6bc520-3c82-4d6c-a458-47590370681a",
  "parentVariantsIds": [
    "01tT1000000F0afIAC",
    "01tT1000000F0agIAC"
  ]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique ID to track and associate related events or transactions. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 67.0 |
| `parent​Variants​Ids` | String[] | List of product IDs for parent variant products whose variations you want to retrieve. If any product ID is blank, invalid, or not found, the API skips that ID and processes the remaining valid IDs. The skipped IDs appear in the `inValidProductIds` response property. If a product ID is valid but isn't a parent variant product, the API includes it in the `nonVariantParentIds` response property. | Required | 67.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Product
              Variants](./connect_responses_product_variants_output.htm.md)

=== ARTICLE: connect_resources_products_list.htm ===
---
page_id: connect_resources_products_list.htm
title: Products List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_products_list.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Products List (POST)

Get a list of products for a specified catalog, category, or
      subcategory. This API is a composite API for Product Discovery.

    
      
        
          

**Resource**

          
: 
            

```
/connect/cpq/products
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/cpq/products
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
  "correlationId": "eeaa1db2-f371-4227-a886-c77e2f66ce1d",
  "limit": 60,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc"
  ],
  "catalogId": "0ZSDU0000002Og74AE",
  "categoryId": "0ZGDU0000002P0H4AU",
  "priceBookId": "01sDU000000JVsVYAW",
  "productClassificationId": "11BDU0000002TCC2A2",
  "currencyCode": "USD",
  "userContext": {
    "accountId": "001DU000001o2UzYAI"
  },
  "includeCatalogDetails": true,
  "enableQualification": true,
  "enablePricing": true,
  "qualificationProcedure": "ProductQualification",
  "pricingProcedure": "pricingProcedure",
  "contextDefinition": "BrowseContextDefinitionExt",
  "contextMapping": "ProductDiscoveryMapping",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "eq",
        "value": "Laptop Pro Bundle"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": true
        }
      ]
    }
  ],
  "additionalContextData": [
    {
      "nodeName": "Account",
      "nodeData": {
        "id": "001DU000001o2UzYAI",
        "name": "Cloud Kicks"
      }
    }
  ],
  "additionalFields": {
    "Product2": {
      "fields": [
        "CanRamp",
        "DecompositionScope",
        "ProductCode"
      ]
    }
  }
}
```

If a parent category ID is specified in the request body, then the API
            returns all products associated to all child categories.

          
: This example shows a sample request to retrieve a product list with promotions.

          
: 
            

```
{
  "correlationId": "eeaa1db2-f371-4227-a886-c77e2f66ce1d",
  "limit": 60,
  "cursor": "MTAwMDAwMDAwNg==",
  "orderBy": [
    "name:asc"
  ],
  "catalogId": "0ZSDU0000002Og74AE",
  "categoryId": "0ZGDU0000002P0H4AU",
  "priceBookId": "01sDU000000JVsVYAW",
  "productClassificationId": "11BDU0000002TCC2A2",
  "currencyCode": "USD",
  "userContext": {
    "accountId": "001DU000001o2UzYAI"
  },
  "includeCatalogDetails": true,
  "enableQualification": true,
  "enablePricing": true,
  "qualificationProcedure": "ProductQualification",
  "pricingProcedure": "pricingProcedure",
  "contextDefinition": "BrowseContextDefinitionExt",
  "contextMapping": "ProductDiscoveryMapping",
  "filter": {
    "criteria": [
      {
        "property": "name",
        "operator": "eq",
        "value": "Laptop Pro Bundle"
      }
    ]
  },
  "relatedObjectFilters": [
    {
      "objectName": "ProductSpecificationRecType",
      "criteria": [
        {
          "property": "IsCommercial",
          "operator": "eq",
          "value": true
        }
      ]
    }
  ],
  "additionalContextData": [
    {
      "nodeName": "Account",
      "nodeData": {
        "id": "001DU000001o2UzYAI",
        "name": "Cloud Kicks"
      }
    }
  ],
  "additionalFields": {
    "Product2": {
      "fields": [
        "CanRamp",
        "DecompositionScope",
        "ProductCode"
      ]
    }
  },
  "executeConfigurationRules": false,
  "transactionContextId": "a1b2c3d4e5f6",
  "transactionId": "trans789",
  "usePromotions": true
}
```

          

          
: This example shows a sample request to run visibility
            rules.

```
{
  "enableQualification": true,
  "enablePricing": true,
  "includeCatalogDetails": true,
  "catalogId": "0ZSVW000000AhdC4AS",
  "limit": 12,
  "offset": 0,
  "userContext": {
    "accountId": null
  },
  "priceBookId": "01sVW0000024PZlYAM",
  "currencyCode": "USD",
  "transactionId": "0Q0VW000001190f0AA",
  "filter": {
    "criteria": [
      {
        "property": "isActive",
        "operator": "eq",
        "value": true
      },
      {
        "property": "UsedFor",
        "operator": "eq",
        "value": ""
      }
    ]
  },
  "orderBy": [
    "name:asc"
  ],
  "executeConfigurationRules": true
}
```

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `additional​ContextData` | [Context Data Input](./connect_requests_context_data_input.htm.md)[] | Additional nodes that are added to the custom or default context definition. The maximum number of supported nodes is 10. | Optional | 60.0 |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_additional_fields_input.htm.md)> | Additional standard or custom fields of the Product2 object to include in the response. If the requested fields are invalid or access to fields isn’t available, then the API throws an error. | Optional | 61.0 |
| `catalog​Id` | String | ID of the catalog. If the catalog ID is specified, then the API returns the list of offers from the catalog with the pricing details related to the catalog. | Optional | 60.0 |
| `category​Id` | String | ID of the category. If the category ID isn’t specified, then the API returns the list of offers from the catalog. | Optional | 60.0 |
| `context​Definition` | String | API name of the custom context definition that’s sent for context creation. If this property isn’t specified, then the default context definition is used. | Optional | 60.0 |
| `context​Mapping` | String | Default context mapping of the context definition. If a context mapping is specified, then the API checks whether the mapping belongs to the specified context definition to process the details for hydration. | Optional | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Optional | 60.0 |
| `currency​Code` | String | Currency code that’s considered for pricing and filtering request. If multiple currencies are enabled for the org, then the `currencyCode` property is required. | Optional | 60.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Optional | 60.0 |
| `enable​Pricing` | Boolean | Indicates whether to enable pricing for the products (`true`) or not (`false`). The default value is `true`.The **Pricing Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Pricing Procedure** toggle is disabled, then setting the `enablePricing` property to `true` has no effect and the `prices` property in the API response is returned empty. | Optional | 60.0 |
| `enable​Qualification` | Boolean | Indicates whether to enable qualification rules for the products (`true`) or not (`false`). The default value is `true`.The **Qualification Procedure** toggle from the Product Discovery Settings page from Setup overrides this property. For example, if the **Qualification Procedure** toggle is disabled, then setting the `enableQualification` property to `true` has no effect and the `qualificationContext` property in the API response isn’t returned. | Optional | 60.0 |
| `execute​ConfigurationRules` | Boolean | Indicates whether to execute configuration rules (`true`) or not (`false`). | Optional | 67.0 |
| `filter` | [Filter Input](./connect_requests_filter_input.htm.md) | Filters records based on supported criteria. The supported property is `name`. The supported operators are: `eq` `in` `contains`—This value isn't applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. If multiple criteria are specified, then the resultant criteria are combined by using the `and` operator. | Optional | 60.0 |
| `include​Catalog​Details` | Boolean | Indicates whether to include catalog details in the response (`true`) or not (`false`). | Optional | 61.0 |
| `limit` | Integer | Number of items to include in the response. The default value is 10. | Optional | 60.0 |
| `offset` | Integer | Reserved for internal use. | Optional | 60.0 |
| `order​By` | String[] | Sort order of the results, which is either ascending (`asc`) or descending order (`desc`). The default sort order is ascending order. The default value is `asc`. If the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled, then you can sort products by using name only. | Optional | 60.0 |
| `price​BookId` | String | ID of the price book to get the prices from. If this property isn’t specified, then prices from the standard price book are fetched. | Required | 60.0 |
| `pricing​Procedure` | String | API name of the custom pricing procedure that’s used for the pricing process. If this property isn’t specified, then the default pricing procedure is executed. | Optional | 60.0 |
| `product​Classification​Id` | String | ID of the product classification. | Optional | 60.0 |
| `qualification​Procedure` | String | API name of the custom qualification procedure that’s used for the product qualification process. If this property isn’t specified, then the default qualification procedure is executed. | Optional | 60.0 |
| `related​Object​Filters` | [Related Object Filter Input](./connect_requests_related_object_filter_input.htm.md)[] | Filter records based on supported criteria for related objects. The supported object is `ProductSpecificationRecType`. The supported property is `IsCommerical`. The supported operator is `eq`. The supported values are `true` and `false`. | Optional | 60.0 |
| `transaction​ContextId` | String | ID of the transaction context. | Optional | 67.0 |
| `transactionId` | String | ID of the transaction. | Optional | 67.0 |
| `usePromotions` | Boolean | Indicates whether to fetch applicable promotions from Global Promotion Management (GPM) for each product in the list (`true`) or not (`false`). If Promotion feature is enabled in the org and this property isn't specified, then the default value is `true`. If the Promotion feature isn't enabled, the default value is `false`. | Optional | 66.0 |
| `user​Context` | [User Context Input](./connect_requests_user_context_input.htm.md) | User context details. For example, account ID or contact ID. | Optional | 60.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)

=== ARTICLE: connect_resources_related_records.htm ===
---
page_id: connect_resources_related_records.htm
title: Product Related Records List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_related_records.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Related Records List (POST)

Retrieve related ProductRampSegment or ProductUsageGrant records for
      Product2 object.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/relatedRecords/entityName
```

          

          
: The supported entity or object is Product2.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/relatedRecords/product2
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

#### Note

POST methods typically create an item, but for this resource POST is used to
              retrieve information.

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            

```
{
  "recordIds": [
    "01txx0000006i44AAA",
    "01txx0000006i5gAAA"
  ],
  "relatedObjectNodes": [
    {
      "relatedObjectAPIName": "ProductRampSegment",
      "pageSize": 20,
      "offSet": 0
    },
    {
      "relatedObjectAPIName": "ProductUsageGrant",
      "pageSize": 10,
      "offSet": 0,
      "filter": {
        "criteria": [
          {
            "property": "status",
            "operator": "eq",
            "value": "active"
          },
          {
            "property": "effectivestartdate",
            "operator": "lte",
            "value": "2024-06-25"
          },
          {
            "criteriaType": "CustomWhereCondition",
            "value": "(effectiveenddate = null OR effectiveenddate >= 2024-06-25)"
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
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 62.0 |
| `recordIds` | String[] | List of record IDs to return the relatedObjects records for. The maximum number of record IDs supported is 20. | Required | 62.0 |
| `related​ObjectNodes` | [Related Object Node Input](./connect_requests_related_object_node_input.htm.md)[] | List of nodes for the related objects. The maximum number of related object nodes supported is two. | Required | 62.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Related Records
              List](./connect_responses_related_records_list_output.htm.md)

=== ARTICLE: connect_resources_snapshot_deploy.htm ===
---
page_id: connect_resources_snapshot_deploy.htm
title: Snapshot Deployment (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_snapshot_deploy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Deployment (POST)

Create indexes for a snapshot. Indexes improve search results and make
      it easier to find products at run time through search terms.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/index/deploy
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/deploy
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

          
: This example shows a sample request to build a new snapshot with immediate
            activation.

: 

```
{
  "snapshot": {
    "activationType": "IMMEDIATE"
  },
  "buildType": "FULL"
}
```

          
: This example shows a sample request to rebuild a snapshot in the `active` status.

          
: 
            

```
{
  "snapshot": {
    "activationType": "IMMEDIATE",
    "id": "1Avxx0000005DFe1AM"
  },
  "buildType": "FULL"
}
```

          

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `buildType` | String | Build type of the snapshot index. Valid value is: `FULL`—Specifies a full index build. `INCREMENTAL`—Specifies an incremental index build. Available from API version 63.0 and later. | Required | 62.0 |
| `snapshot` | [Run-time Catalog Snapshot Input](./connect_requests_runtime_catalog_snapshot_input.htm.md)[] | Snapshot to deploy. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Snapshot
              Deployment](./connect_responses_snapshot_deployment_output.htm.md)

=== ARTICLE: connect_resources_snapshot_get.htm ===
---
page_id: connect_resources_snapshot_get.htm
title: Snapshot Collection (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_snapshot_get.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Collection (GET)

Retrieve the created snapshots and snapshot indexes.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/index/snapshots
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/index/snapshots
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Query Parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `numberOf​IndexLogs` | Integer | Number of index logs to include in the response. Specify a number from 0 through 100. The default value is 25. | Optional | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Snapshot
              Collection](./connect_responses_snapshot_collection_output.htm.md)

=== ARTICLE: connect_resources_unit_of_measure_info.htm ===
---
page_id: connect_resources_unit_of_measure_info.htm
title: Unit of Measure Info (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_unit_of_measure_info.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unit of Measure Info (GET)

Get details about the unit of measure for a specific set of
      records.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/unit-of-measure/info
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/unit-of-measure/info
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Query parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 63.0 |
| `ids` | String | IDs of the unit of measure records. | Optional | 63.0 |

          

        
        
          

**Response body for GET**

          
: [Bulk Unit Of Measure
              Info](./connect_responses_bulk_unit_of_measure_info_output.htm.md)

=== ARTICLE: connect_resources_unit_of_measure_rounded_data.htm ===
---
page_id: connect_resources_unit_of_measure_rounded_data.htm
title: Unit of Measure Rounded Data (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_unit_of_measure_rounded_data.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unit of Measure Rounded Data (POST)

Round off and scale decimal data for a specific set of
    fields.

    
      
        
          

**Resource**

          
: 
            

```
/connect/pcm/unit-of-measure/rounded-data
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/pcm/unit-of-measure/rounded-data
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "dataRowInputs": [
    {
      "key": "PRC1",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "0hExx0000000001EAA"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": "987462848934739347.32232590183756545",
          "unitOfMeasureId": "0hExx000000001dEAA"
        }
      ]
    },
    {
      "key": "PRC2",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "unitOfMeasureId": "uomId1"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "unitOfMeasureId": "Kgs Id"
        }
      ]
    },
    {
      "key": "PRC3",
      "fieldDataInputs": [
        {
          "fieldApiName": "MaxQuantity",
          "originalValue": 0.437584,
          "unitOfMeasureId": "uomId2"
        },
        {
          "fieldApiName": "MinQuantity",
          "originalValue": 7364.58923,
          "unitOfMeasureId": "uomId2"
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
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Optional | 63.0 |
| `dataRow​Inputs` | [Data Row Input](./connect_requests_data_row_input.htm.md)[] | List of row inputs for rounding the data. | Required | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Data
            Rounding](./connect_responses_data_rounding_output.htm.md)

=== ARTICLE: connect_responses_api_status_output.htm ===
---
page_id: connect_responses_api_status_output.htm
title: API Status
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_api_status_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# API Status

Output representation of the API status.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `messages` | [CPQ Message](./connect_responses_cpq_message_output.htm.md)[] | Status messages of the API execution. | Small, 60.0 | 60.0 |
| `status​Code` | String | Status code of the API execution. | Small, 60.0 | 60.0 |
| `status​Message` | String | Display label for the API status. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_attribute_category_output.htm ===
---
page_id: connect_responses_attribute_category_output.htm
title: Attribute Category
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_attribute_category_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Attribute Category

Output representation of the attribute category.

      
        
          

**JSON example**

          
: 
            

```
"attributeCategory": [
        {
          "attributes": [
            {
              "additionalFields": {
                "scope": "Order"
              },
              "attributeNameOverride": "AD Text",
              "code": "AD02",
              "dataType": "Text",
              "defaultValue": "AD Text DV",
              "description": "AD Text Desc",
              "displayType": "Text",
              "helpText": "AD Text DHT",
              "id": "0tjT1000000002bIAA",
              "isHidden": false,
              "isPriceImpacting": true,
              "isReadOnly": true,
              "isRequired": true,
              "label": "AD Text Label",
              "maximumCharacterCount": "20",
              "maximumValue": "100",
              "minimumCharacterCount": "1",
              "minimumValue": "50",
              "name": "AD Text",
              "sequence": 1,
              "status": "Active",
              "valueDescription": "AD Text VD"
            }
          ],
          "code": "AC001",
          "id": "0v3T1000000000BIAQ",
          "name": "build and make"
    }
]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributes` | [Attribute Definition](./connect_responses_attribute_definition_output.htm.md)[] | List of categorized attributes associated with the product. | Small, 60.0 | 60.0 |
| `code` | String | Code of the attribute category. | Small, 60.0 | 60.0 |
| `id` | String | ID associated with the attribute category. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute category. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |

