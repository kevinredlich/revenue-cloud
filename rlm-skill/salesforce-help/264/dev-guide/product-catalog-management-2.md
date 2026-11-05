# Revenue Management Developer Guide 264 — sección: Product Catalog Management (parte 2/2) (131 artículos)

=== ARTICLE: connect_responses_attribute_definition_output.htm ===
---
page_id: connect_responses_attribute_definition_output.htm
title: Attribute Definition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_attribute_definition_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Attribute Definition

Output representation of the attribute definition.

      
        
          

**JSON example**

          
: 
            

```
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
      "maximumCharacterCount": 20,
      "maximumValue": "100",
      "minimumCharacterCount": 1,
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
}]
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
- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Key-value pair of additional standard or custom fields to include in the response. | Small, 61.0 | 61.0 |
| `attribute​Name​Override` | String | Name to display for the attribute, which overrides the name on the attribute. For example, the Color attribute is overridden to display as Laptop Color. | Small, 60.0 | 60.0 |
| `code` | String | Unique code of the attribute definition. | Small, 60.0 | 60.0 |
| `dataType` | String | Data type of the attribute definition value. | Small, 60.0 | 60.0 |
| `default​Value` | String | Default value of the attribute. | Small, 60.0 | 60.0 |
| `description` | String | Description of the attribute. | Small, 60.0 | 60.0 |
| `display​Type` | String | Display types of the attribute. Valid values are: `Radio Button` `Checkbox` `Toggle` `Input Date` `DateTime` `Currency Symbol` `Currency Code` `Currency Name` `Percentage` `Text` `Combobox` `Radio Button` `MultiSelect` `MultiSelectCheckboxes` | Small, 60.0 | 60.0 |
| `help​Text` | String | Help text that appears at run time for the attribute. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `id` | String | ID of the attribute definition. | Small, 60.0 | 60.0 |
| `is​Configurable` | Boolean | Reserved for future use. | Small, 60.0 | 60.0 |
| `is​Hidden` | Boolean | Indicates whether to hide the attribute from the users in the order capture interface (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isPrice​Impacting` | Boolean | Indicates whether the attribute impacts the product price (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isRead​Only` | Boolean | Indicates whether the product attribute is read-only for the end users in the order capture page (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Required` | Boolean | Indicates whether a value for the attribute is required for the assigned parent object (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Value​Cloneable` | Boolean | Reserved for future use. | Small, 60.0 | 60.0 |
| `label` | String | Label of the attribute. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `maximum​Character​Count` | Integer | Maximum number of alphanumeric characters that can be entered for attributes of type number and text in run time. | Small, 60.0 | 60.0 |
| `maximum​Value` | String | Maximum value that can be entered for attributes of type number, currency, and percent in run time. | Small, 60.0 | 60.0 |
| `minimum​Character​Count` | Integer | Minimum number of alphanumeric characters that can be entered for attributes of type number and text in run time. The minimum character count must be less than or equal to the maximum character count. | Small, 60.0 | 60.0 |
| `minimum​Value` | String | Minimum value that can be entered for attributes of type number, currency, and percent in run time. The minimum value must be less than or equal to the maximum value. | Small, 60.0 | 60.0 |
| `name` | String | Name of the attribute. | Small, 60.0 | 60.0 |
| `picklist` | [Attribute Picklist](./connect_responses_attribute_picklist_output.htm.md) | ID of the attribute picklist that provides the valid values for the attribute. | Small, 60.0 | 60.0 |
| `sequence` | Integer | Order in which the attribute values appear in the attribute definition when the product is configured at run time. | Small, 60.0 | 60.0 |
| `status` | String | Lifecycle state of the attribute picklist. Valid values are: `Active` `Draft` `Inactive` | Small, 60.0 | 60.0 |
| `step​Value` | String | Reserved for future use. | Small, 60.0 | 60.0 |
| `value​Decoder` | String | Reserved for future use. | Small, 60.0 | 60.0 |
| `value​Description` | String | Description of the value assigned to the attribute. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_attribute_picklist_output.htm ===
---
page_id: connect_responses_attribute_picklist_output.htm
title: Attribute Picklist
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_attribute_picklist_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Attribute Picklist

Output representation of the attribute picklist.

      
        
          

**JSON example**

          
: 
            

```
"picklist": {
     "dataType": "Text",
     "description": "Fabric Module options",
     "id": "0v51Q000000TNDkQAO",
     "name": "Fabric Module options",
     "values": [
      {
        "abbreviation": "IFM1"
        "code": "PV0051",
        "displayValue": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "id": "0v61Q0000008OMYQA2",
        "name": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "sequence": "1",
        "value": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "status" : "Active"
      },
      {
        "abbreviation": "IFM2"
        "code": "PV0052",
        "displayValue": "100G Intelligent Fabric Module with 8x 100G QSFP28 ports",
        "id": "0v61Q0000008OMZQA2",
        "name": "100G Intelligent Fabric Module with 8x 100G QSFP28 ports",
        "sequence": "2",
        "value": "100G Intelligent Fabric Module with 8x 100G QSFP28 ports",
        "status" : "Active"
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
| `dataType` | String | Data type of the values in the picklist. Valid values are: `Boolean` `Date` `Datetime` `Number` `Text` `Currency` `Percent` | Small, 60.0 | 60.0 |
| `description` | String | Description of the picklist, such as the picklist purpose or the associated product. | Small, 60.0 | 60.0 |
| `id` | String | ID associated with the attribute picklist record. | Small, 60.0 | 60.0 |
| `name` | String | Name of the picklist value. | Small, 60.0 | 60.0 |
| `values` | [Attribute Picklist Value](./connect_responses_attribute_picklist_value_output.htm.md)[] | List of values associated with the picklist. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_attribute_picklist_value_output.htm ===
---
page_id: connect_responses_attribute_picklist_value_output.htm
title: Attribute Picklist Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_attribute_picklist_value_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Attribute Picklist Value

Output representation of the attribute picklist value.

      
        
          

**JSON example**

          
: 
            

```
"values": [
      {
        "abbreviation": "IFM1"
        "code": "PV0051",
        "displayValue": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "id": "0v61Q0000008OMYQA2",
        "name": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "sequence": "1",
        "value": "25G Intelligent Fabric Module with 8x 25G SFP28 ports",
        "status" : "Active"
      }
     ]
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `abbreviation` | String | Name of the picklist value that appears at run time. | Small, 60.0 | 60.0 |
| `code` | String | Unique code of the picklist value within the picklist. | Small, 60.0 | 60.0 |
| `display​Value` | String | Picklist value that appears at run time in the order capture page. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `id` | String | ID associated with the attribute picklist value. | Small, 60.0 | 60.0 |
| `name` | String | Name of the picklist value. | Small, 60.0 | 60.0 |
| `sequence` | String | Order in which the picklist value appears in the picklist. | Small, 60.0 | 60.0 |
| `status` | String | Status of the attribute picklist value. | Small, 62.0 | 62.0 |
| `value` | String | Value of the picklist item. Value must be unique within the picklist. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_bulk_unit_of_measure_info_output.htm ===
---
page_id: connect_responses_bulk_unit_of_measure_info_output.htm
title: Bulk Unit Of Measure Info
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_bulk_unit_of_measure_info_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Unit Of Measure Info

Output representation of the details of the unit of measure records along with error
    details.

      
        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "928ea35f-8a2f-4932-9f7e-ec6cdbcabdbe",
  "errorCodeToErrorMap": {
    "UNIT_OF_MEASURE_INFO_INVALID_UOM_IDS": {
      "errorCode": "UOM_INFO_API_003",
      "messageDetail": "Invalid uomId is passed. Please specify a valid uomId.",
      "messageTitle": "Invalid uomId is passed.",
      "recordIds": [
        "sample"
      ],
      "source": "Unit_Of_Measure_Info_Api"
    }
  },
  "status": {
    "errors": [],
    "httpStatusCode": "200",
    "message": " Successfully fetched UnitOfMeasure Info. "
  },
  "uomIdToUnitOfMeasureInfo": {
    "0hEU200000003M5MAI": {
      "id": "0hEU200000003M5MAI",
      "name": "Pounds",
      "roundingMethod": "Nearest",
      "scale": 1,
      "unitCode": "Pounds"
    },
    "0hEU200000003KTMAY": {
      "id": "0hEU200000003KTMAY",
      "name": "Grams",
      "roundingMethod": "Down",
      "scale": 5,
      "unitCode": "Grams"
    }
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 63.0 | 63.0 |
| `errorCode​ToErrorMap` | Map<String, [Unit Of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)> | Error codes mapped to their details. | Small, 63.0 | 63.0 |
| `status` | [Unit Of Measure Status](./connect_responses_unit_of_measure_status.htm.md)[] | Status of the API request. | Small, 63.0 | 63.0 |
| `uomIdToUnit​OfMeasure​Info` | Map<String, [Unit Of Measure Info](./connect_responses_unit_of_measure_info_output.htm.md)> | Unit of measure record IDs mapped to their details. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_catalog_output.htm ===
---
page_id: connect_responses_catalog_output.htm
title: Catalog Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_catalog_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog Output

Output representation of the catalog definition.

      
        
          

**JSON example**

          
: 
            

```
catalogs": [
    {
      "catalogType": "Sales",
      "code": "CAT009",
      "description": "SmartBytes B2B Catalog",
      "effectiveEndDate": "31-07-2023",
      "effectiveStartDate": "24-07-2023",
      "id": "0ZS1Q000000XbZAWA0",
      "name": "SmartBytes B2B Catalog",
      "numberOfCategories": 8
    }
]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​Type` | String | The category of an entry in the catalog, which is customizable. For example, catalog types, such as sellable products, services, parts, technical services, or technical resources. | Small, 60.0 | 60.0 |
| `code` | String | Unique ID associated with the catalog. | Small, 60.0 | 60.0 |
| `description` | String | Description of the catalog. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `effective​EndDate` | String | Date and time from when the catalog isn't available to the end users. | Small, 60.0 | 60.0 |
| `effective​Start​Date` | String | Date and time from when the catalog is available to the end users. | Small, 60.0 | 60.0 |
| `id` | String | ID of the catalog. | Small, 60.0 | 60.0 |
| `name` | String | Name of the catalog. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `numberOf​Categories` | Integer | Number of categories in the catalog. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_catalogs_output.htm ===
---
page_id: connect_responses_catalogs_output.htm
title: Catalogs Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_catalogs_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalogs Output

Output representation of the retrieved catalog result.

      
        
          

**JSON example**

          
: 
            

```
{
  "catalogs": [
    {
      "catalogType": "Sales",
      "code": "CAT009",
      "id": "0ZS1Q000000XbZAWA0",
      "name": "SmartBytes B2B Catalog",
      "numberOfCategories": 8
    }
  ],
  "correlationId": "0b7b6a30-895c-407a-91b3-e67482d339a3",
  "count": 1,
  "status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched the catalog records."
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalogs` | [Catalog Output](./connect_responses_catalog_output.htm.md)[] | List of the catalogs. | Small, 60.0 | 60.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 60.0 | 60.0 |
| `count` | Integer | Total number of the catalog records retrieved after the query execution, wherein the `pageSize` property determines the number of records returned in every page. | Small, 60.0 | 60.0 |
| `status` | [Status](./connect_responses_status.htm.md) | Status of the request. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_categories_output.htm ===
---
page_id: connect_responses_categories_output.htm
title: Categories Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_categories_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Categories Output

Output representation of the retrieved categories result.

      
        
          

**JSON example**

          
: 
            

```
{
  "categories": [
    {
      "catalogId": "0ZS1Q000000XbZAWA0",
      "code": "B2B Category",
      "description": "Products Category",
      "hasSubCategories": true,
      "id": "0ZG1Q000000XbVGWA0",
      "name": "Unified Computing",
      "numberOfProducts": 2,
      "parentCategoryId": "0ZGT100000000qlOAA",
      "sortOrder": 2,
      "subCategories": [],
      "isNavigational: false
    }
  ],
  "correlationId": "30230973-0a09-405e-b148-f085bb6dd66e",
  "status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched the category records."
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `categories` | [Category Output](./connect_responses_category_output.htm.md)[] | List of the retrieved categories. | Small, 60.0 | 60.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 60.0 | 60.0 |
| `status` | [Status](./connect_responses_status.htm.md) | Status of the request. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_category_output.htm ===
---
page_id: connect_responses_category_output.htm
title: Category Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_category_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category Output

Output representation of the category definition.

      
        
          

**JSON example**

          
: 
            

```
"categories": [
    {
      "catalogId": "0ZS1Q000000XbZAWA0",
      "code": "B2B Category",
      "description": "Products Category",
      "hasSubCategories": true,
      "id": "0ZG1Q000000XbVGWA0",
      "name": "Unified Computing",
      "numberOfProducts": 2,
      "parentCategoryId": "0ZGT100000000qlOAA",
      "sortOrder": 2,
      "subCategories": [],
      "isNavigational: false
    }
  ]
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalogId` | String | ID of the catalog that the category is associated with. | Small, 60.0 | 60.0 |
| `code` | String | Unique code of the product category. | Small, 60.0 | 60.0 |
| `description` | String | Description of the category. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `hasSub​Categories` | Boolean | Indicates whether the subcategories are available (true) or not (false). | Small, 60.0 | 60.0 |
| `id` | String | ID of the category. | Small, 60.0 | 60.0 |
| `isNavigational` | Boolean | Indicates whether the category node is navigational (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `name` | String | Name of the category. If data translation is set up and specified in the org, the translated name is available. | Small, 60.0 | 60.0 |
| `numberOf​Products` | Integer | Number of products associated with the category. | Small, 60.0 | 60.0 |
| `parent​CategoryId` | String | ID of the parent category. | Small, 60.0 | 60.0 |
| `sort​Order` | Integer | Display order of the product category relative to the siblings with the same parent category. | Small, 60.0 | 60.0 |
| `sub​Categories` | [Category Output](#)[] | List of subcategories, if available. This property is returned with the [Categories List (GET) API](./connect_resources_get_categories.htm.md) response. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_cpq_base_bulk_details_output.htm ===
---
page_id: connect_responses_cpq_base_bulk_details_output.htm
title: Bulk Product Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_cpq_base_bulk_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Bulk Product Details

Output representation of the response that contains the details of multiple
    products.

        
          

**JSON example**

          
: 
            

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "contextId": "c68c7c7e85f3ea5b0e7bcfefc0f2dba9bbd24bfe2f4240ca589af50e473e2242",
  "correlationId": "de9a674c-1807-438c-ac78-2c96f4655325",
  "result": [
    {
      "additionalFields": [],
      "attributeCategories": [],
      "attributes": [],
      "catalogs": [],
      "childProducts": [],
      "id": "01txx0000006ivJAAQ",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "iPhone12",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": false,
          "isSelected": true,
          "price": 100,
          "priceBookEntryId": "01uxx0000008zUkAAI",
          "priceBookId": "01sxx0000005qxxAAA",
          "pricingModel": {
            "id": "0jPxx000000009hEAA",
            "name": "OneTime",
            "pricingModelType": "OneTime"
          }
        },
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isSelected": false,
          "price": 15,
          "priceBookEntryId": "01uxx0000008zUmAAI",
          "priceBookId": "01sxx0000005qxxAAA",
          "pricingModel": {
            "frequency": "Months",
            "id": "0jPxx000000009iEAA",
            "name": "Monthly",
            "occurrence": 1,
            "pricingModelType": "TermDefined"
          }
        }
      ],
      "productClassification": {},
      "productCode": "iPhone12",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iOxx00000000EfEAI",
          "productId": "01txx0000006ivJAAQ",
          "productSellingModel": {
            "id": "0jPxx000000009iEAA",
            "name": "Monthly",
            "pricingTerm": 1,
            "pricingTermUnit": "Months",
            "sellingModelType": "TermDefined",
            "status": "Active"
          },
          "productSellingModelId": "0jPxx000000009iEAA"
        },
        {
          "id": "0iOxx00000000EgEAI",
          "productId": "01txx0000006ivJAAQ",
          "productSellingModel": {
            "id": "0jPxx000000009hEAA",
            "name": "OneTime",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPxx000000009hEAA"
        }
      ],
      "productSpecificationType": {
        "name": "ProdSpecRecType1",
        "productSpecificationRecordType": {}
      },
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "additionalFields": [],
      "attributeCategories": [],
      "attributes": [],
      "catalogs": [],
      "childProducts": [],
      "id": "01txx0000006ivLAAQ",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "iPhone13",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isSelected": false,
          "price": 1520,
          "priceBookEntryId": "01uxx0000008zUpAAI",
          "priceBookId": "01sxx0000005qxxAAA",
          "pricingModel": {
            "id": "0jPxx000000009hEAA",
            "name": "OneTime",
            "pricingModelType": "OneTime"
          }
        },
        {
          "currencyIsoCode": "USD",
          "isDefault": false,
          "isSelected": false,
          "price": 152,
          "priceBookEntryId": "01uxx0000008zUqAAI",
          "priceBookId": "01sxx0000005qxxAAA",
          "pricingModel": {
            "frequency": "Months",
            "id": "0jPxx000000009iEAA",
            "name": "Monthly",
            "occurrence": 1,
            "pricingModelType": "TermDefined"
          }
        }
      ],
      "productClassification": {},
      "productCode": "iPhone13",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iOxx00000000EbEAI",
          "productId": "01txx0000006ivLAAQ",
          "productSellingModel": {
            "id": "0jPxx000000009iEAA",
            "name": "Monthly",
            "pricingTerm": 1,
            "pricingTermUnit": "Months",
            "sellingModelType": "TermDefined",
            "status": "Active"
          },
          "productSellingModelId": "0jPxx000000009iEAA"
        },
        {
          "id": "0iOxx00000000EeEAI",
          "productId": "01txx0000006ivLAAQ",
          "productSellingModel": {
            "id": "0jPxx000000009hEAA",
            "name": "OneTime",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPxx000000009hEAA"
        }
      ],
      "productSpecificationType": {
        "name": "ProdSpecRecType1",
        "productSpecificationRecordType": {}
      },
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `api​Status` | [API Status](./connect_responses_api_status_output.htm.md)[] | Status of the API request. | Small, 61.0 | 61.0 |
| `context​Id` | String | ID of the context. | Small, 61.0 | 61.0 |
| `correlation​Id` | String | Unique identifier of the request. | Small, 61.0 | 61.0 |
| `result` | Any response body | Result that contains the details of products. | Small, 61.0 | 61.0 |
| `user​Context` | [User Context](./connect_responses_user_context_output.htm.md)[] | User context details. For example, account ID or contact ID. | Small, 61.0 | 61.0 |

=== ARTICLE: connect_responses_cpq_base_details_output.htm ===
---
page_id: connect_responses_cpq_base_details_output.htm
title: CPQ Base Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_cpq_base_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CPQ Base Details

Output representation of the catalog, category, or product details based on the
    request.

      
        
          

**JSON example**

          
: This example shows the sample catalog details.

          
: 
            

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "32595ed6-1922-41f7-9c2c-373c677a7d62",
  "result": {
    "catalogCode": "Mobiles",
    "catalogType": "Sales",
    "description": "Catalog for mobile phones",
    "effectiveEndDate": "2028-04-01T19:00Z",
    "effectiveStartDate": "2024-04-01T19:00Z",
    "id": "0ZSxx0000000001GAA",
    "name": "Mobiles",
    "numberOfCategories": 3
  }
}
```

          

          
: This example shows the sample category details.

          
: 
            

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "f9fb90de-36aa-44a1-9961-a9ef5fc0cad8",
  "result": {
    "catalogId": "0ZSxx0000000001GAA",
    "childCategories": [
      
    ],
    "description": "Category for Samsung phones",
    "id": "0ZGxx000000004rGAA",
    "name": "Samsung",
    "isNavigational": true,
    "sortOrder": 2
  }
}
```

          

          
: This example shows the sample product details.

          
: 

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "822a8941-7412-4883-bb80-e488f908471e",
  "result": {
    "additionalFields": {
        "CustomField1__c": "TextValue",
        "CustomField2__c": "10",
        "StandardField1": "false"
    },
    "attributeCategories": [
      
    ],
    "attributes": [
      
    ],
    "catalogs": [
      
    ],
    "childProducts": [
      
    ],
    "id": "01txx0000006i2WAAQ",
    "isActive": true,
    "isAssetizable": true,
    "isSoldOnlyWithOtherProds": false,
    "name": "iPhone15",
    "nodeType": "simpleProduct",
    "prices": [
      
    ],
    "productClassification": {
      
    },
    "productCode": "iPhone15",
    "productComponentGroups": [
      
    ],
    "productSellingModelOptions": [
      {
        "id": "0iOxx0000000003EAA",
        "productId": "01txx0000006i2WAAQ",
        "productSellingModel": {
          "id": "0jPxx0000000001EAA",
          "name": "OneTime",
          "sellingModelType": "OneTime",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx0000000001EAA"
      },
      {
        "id": "0iOxx0000000004EAA",
        "productId": "01txx0000006i2WAAQ",
        "productSellingModel": {
          "id": "0jPxx0000000002EAA",
          "name": "Monthly",
          "pricingTerm": 1,
          "pricingTermUnit": "Months",
          "sellingModelType": "TermDefined",
          "status": "Active"
        },
        "productSellingModelId": "0jPxx0000000002EAA"
      }
    ],
    "productSpecificationType": {
      "name": "ProdSpecRecType1",
      "productSpecificationRecordType": {
        
      }
    }
  }
}
```

This example shows a sample of category details with eligible
            promotions.

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "f9fb90de-36aa-44a1-9961-a9ef5fc0cad8",
  "result": {
    "catalogId": "0ZSxx0000000001GAA",
    "childCategories": [],
    "description": "Category for Samsung phones",
    "id": "0ZGxx000000004rGAA",
    "name": "Samsung",
    "isNavigational": true,
    "sortOrder": 2,
    "eligiblePromotions": [
      {
        "id": "0ZPxx0000000001AAA",
        "name": "Summer Sale 2025",
        "displayName": "Summer Electronics Sale",
        "description": "Get 20% off on all Samsung devices",
        "priority": 100,
        "startDateTime": "2025-06-01T00:00:00Z",
        "endDateTime": "2025-08-31T23:59:59Z",
        "isAutomatic": true,
        "isCategoryPromo": true,
        "isProductPromo": false,
        "couponCode": null,
        "termsAndConditions": "Valid on all Samsung products. Cannot be combined with other offers."
      },
      {
        "id": "0ZPxx0000000002AAA",
        "name": "Electronics Bundle Deal",
        "displayName": "Bundle & Save",
        "description": "Save 15% when you buy 2 or more items",
        "priority": 90,
        "startDateTime": "2025-05-15T00:00:00Z",
        "endDateTime": "2025-12-31T23:59:59Z",
        "isAutomatic": false,
        "isCategoryPromo": false,
        "isProductPromo": true,
        "couponCode": "BUNDLE15",
        "termsAndConditions": "Minimum 2 items required."
      }
    ]
  }
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `api​Status` | [API Status](./connect_responses_api_status_output.htm.md) | Status of the API request. | Small, 60.0 | 60.0 |
| `context​Id` | String | ID of the context. | Small, 60.0 | 60.0 |
| `correlation​Id` | String | Unique identifier of the request. | Small, 60.0 | 60.0 |
| `result` | Any response body | Result that contains the details of catalogs, categories, or products as per the requested resource. | Small, 60.0 | 60.0 |
| `user​Context` | [User Context](./connect_responses_user_context_output.htm.md) | User context details. For example, account ID or contact ID. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_cpq_base_list_output.htm ===
---
page_id: connect_responses_cpq_base_list_output.htm
title: CPQ Base List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_cpq_base_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CPQ Base List

Output representation of the list of catalogs, categories, or products based on the
    request.

        
          

**JSON example**

          
: This example shows a sample catalog list.

          
: 
            

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "9f417514-9587-4063-9e48-18a2cf2477c0",
  "limit": 10,
  "offSet": 0,
  "query": {
    
  },
  "result": [
    {
      "catalogCode": "Mobiles",
      "catalogType": "Sales",
      "description": "Catalog for mobile phones",
      "effectiveEndDate": "2028-04-01T19:00Z",
      "effectiveStartDate": "2024-04-01T19:00Z",
      "id": "0ZSxx0000000001GAA",
      "name": "Mobiles",
      "numberOfCategories": 3
    }
  ],
  "total": 1
}
```

          

          
: This example shows a sample category list.

          
: 
            

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "3f2a8f45-e7d2-42ec-bc4c-b981d750e912",
  "query": {
    
  },
  "result": [
    {
      "catalogId": "0ZSxx0000000001GAA",
      "childCategories": [
        
      ],
      "description": "Category for Apple phones and iPads",
      "id": "0ZGxx0000000001GAA",
      "name": "Apple",
      "sortOrder": 1,
      "isNavigational": true
    },
    {
      "catalogId": "0ZSxx0000000001GAA",
      "childCategories": [
        
      ],
      "description": "Category for Samsung phones",
      "id": "0ZGxx000000004rGAA",
      "name": "Samsung",
      "sortOrder": 2,
      "isNavigational": true
    },
    {
      "catalogId": "0ZSxx0000000001GAA",
      "childCategories": [
        
      ],
      "description": "Category for Android phones",
      "id": "0ZGxx000000006TGAQ",
      "name": "Android",
      "isNavigational": true
    }
  ],
  "total": 3
}
```

          

          
: This example shows a sample product list.

          
: 
            

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "contextId": "f36f8e73f1fc338cc4e93c61613cba07a6a0129941d97e5dd6e52a2885776ce4",
  "correlationId": "eeaa1db2-f371-4227-a886-c77e2f66ce1d",
  "cursor": "MTAwMDAwMDAwNg==",
  "query": {},
  "result": [
    {
      "additionalFields": {
        "DecompositionScope": "OrderLineItem",
        "ProductCode": "LPB001",
        "CanRamp": false
      },
      "attributeCategories": [],
      "catalogs": [
        {
          "customFields": {},
          "id": "0ZSDU0000002Og74AE",
          "name": "Service Catalog",
          "numberOfCategories": 5
        }
      ],
      "categories": [
        {
          "catalogId": "0ZSDU0000002Og74AE",
          "childCategories": [],
          "customFields": {},
          "hasSubCategories": false,
          "id": "0ZGDU0000002P0H4AU",
          "name": "Cloud Services",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "childProducts": [],
      "configureDuringSale": "Allowed",
      "description": "The laptop pro bundle includes a Laptop, mouse, warranty for 2 years, premium support and printer bundle",
      "displayUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCrGjPR1fvJqg4yP3RMyqjI0H9eL6tk1fvzw&amp;usqp=CAU",
      "id": "01tDU000000ExkZYAS",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Laptop Pro Bundle",
      "nodeType": "bundleProduct",
      "prices": [],
      "productClassification": {},
      "productCode": "LPB001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iODU0000002TBN2A2",
          "productId": "01tDU000000ExkZYAS",
          "productSellingModel": {
            "id": "0jPDU0000002OTv2AM",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPDU0000002OTv2AM"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "productType": "Bundle",
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

          

          
: This example shows a sample of the list of products retrieved based on the `Laptop` search term.

          
: 
            

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "d9d8f898-19f5-464a-ba2b-6a070783f6c4",
  "cursor": "MTAwMDAwMDAwMw==",
  "facets": [
    {
      "attributeType": "ProductStandard",
      "displayName": "Product Type",
      "displayRank": 2,
      "nameOrId": "Type",
      "values": [
        {
          "displayName": "Bundle",
          "nameOrId": "Bundle"
        }
      ]
    },
    {
      "attributeType": "ProductDynamicAttribute",
      "displayName": "Display",
      "displayRank": 3,
      "nameOrId": "0tjDU0000003K5BYAU",
      "values": [
        {
          "displayName": "1080p Built-in Display",
          "nameOrId": "1080p Built-in Display"
        },
        {
          "displayName": "2k Built-in Display",
          "nameOrId": "2k Built-in Display"
        },
        {
          "displayName": "4k Built-in Display",
          "nameOrId": "4k Built-in Display"
        }
      ]
    }
  ],
  "limit": 10,
  "query": {},
  "result": [
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [],
      "categories": [
        {
          "catalogId": "0ZSDU0000002Og64AE",
          "childCategories": [],
          "customFields": {},
          "hasSubCategories": false,
          "id": "0ZGDU0000002P0A4AU",
          "name": "Laptops",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "Battery- or AC-powered personal computer (PC) smaller than a briefcase",
      "displayUrl": "https://media.istockphoto.com/id/1023428598/photo/3d-illustration-laptop-isolated-on-white-background-laptop-with-empty-space-screen-laptop-at.jpg?s=612x612&amp;w=0&amp;k=20&amp;c=ssK6er5v1fGpSghGiqySwoD8tn5blC7xgefQJI2xU38=",
      "id": "01tDU000000ExkWYAS",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Laptop",
      "nodeType": "simpleProduct",
      "prices": [],
      "productClassification": {
        "id": "11BDU0000002TCD2A2"
      },
      "productCode": "LP001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iODU0000002TBF2A2",
          "productId": "01tDU000000ExkWYAS",
          "productSellingModel": {
            "id": "0jPDU0000002OTv2AM",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPDU0000002OTv2AM"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [],
      "categories": [
        {
          "catalogId": "0ZSDU0000002Og64AE",
          "childCategories": [],
          "customFields": {},
          "hasSubCategories": false,
          "id": "0ZGDU0000002P0A4AU",
          "name": "Laptops",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "The laptop basic bundle includes a Laptop, mouse, and warranty for 1 year.",
      "displayUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbf49JG4zZogCmZMJuXU38qOkR9X36MN4bSw&amp;usqp=CAU",
      "id": "01tDU000000ExkXYAS",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Laptop Basic Bundle",
      "nodeType": "bundleProduct",
      "prices": [],
      "productClassification": {},
      "productCode": "LB001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iODU0000002TBD2A2",
          "productId": "01tDU000000ExkXYAS",
          "productSellingModel": {
            "id": "0jPDU0000002OTv2AM",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPDU0000002OTv2AM"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "productType": "Bundle",
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [],
      "categories": [
        {
          "catalogId": "0ZSDU0000002Og64AE",
          "childCategories": [],
          "customFields": {},
          "hasSubCategories": false,
          "id": "0ZGDU0000002P0A4AU",
          "name": "Laptops",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "The laptop pro bundle includes a Laptop, mouse, warranty for 2 years, premium support and printer bundle",
      "displayUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCrGjPR1fvJqg4yP3RMyqjI0H9eL6tk1fvzw&amp;usqp=CAU",
      "id": "01tDU000000ExkZYAS",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Laptop Pro Bundle",
      "nodeType": "bundleProduct",
      "prices": [],
      "productClassification": {},
      "productCode": "LPB001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iODU0000002TBN2A2",
          "productId": "01tDU000000ExkZYAS",
          "productSellingModel": {
            "id": "0jPDU0000002OTv2AM",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPDU0000002OTv2AM"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "productType": "Bundle",
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [],
      "categories": [
        {
          "catalogId": "0ZSDU0000002Og64AE",
          "childCategories": [],
          "customFields": {},
          "hasSubCategories": false,
          "id": "0ZGDU0000002P0A4AU",
          "name": "Laptops",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "Laptop, Laptop Bag, Laptop stand, Mouse, Keyboard, USB-C Hub,External Hard Drive, Noise Cancelling Headphones, office 365",
      "displayUrl": "https://m.media-amazon.com/images/I/613Fno-NLYL._AC_SL1000_.jpg",
      "id": "01tDU000000ExlAYAS",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Laptop Productivity Bundle",
      "nodeType": "bundleProduct",
      "prices": [],
      "productClassification": {},
      "productCode": "LPB001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iODU0000002TBq2AM",
          "productId": "01tDU000000ExlAYAS",
          "productSellingModel": {
            "id": "0jPDU0000002OTv2AM",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPDU0000002OTv2AM"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "productType": "Bundle",
      "qualificationContext": {
        "isQualified": true
      }
    }
  ],
  "total": 4
}
```

          

          
: This example shows a sample of the results of a qualification procedure that’s
            executed on a list of product IDs.

          
: 
            

```
{
  "apiStatus": {
    "messages": [
      
    ],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "contextId": "e055bb18-d4e8-41c3-881e-0132b9561708",
  "correlationId": "c280c1b0-fd3f-4eac-9b08-075bdf1cbefc",
  "query": {
    
  },
  "result": [
    {
      "productId": "01txx0000006i7PAAQ",
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "productId": "01txx0000006i7QAAQ",
      "qualificationContext": {
        "isQualified": true
      }
    },
    {
      "productId": "01txx0000006i7IAAQ",
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

          

          
: This example shows a list of products with eligible promotions.

          
: 
            

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "f9fb90de-36aa-44a1-9961-a9ef5fc0cad8",
  "result": {
    "catalogId": "0ZSxx0000000001GAA",
    "childCategories": [],
    "description": "Category for Samsung phones",
    "id": "0ZGxx000000004rGAA",
    "name": "Samsung",
    "isNavigational": true,
    "sortOrder": 2,
    "eligiblePromotions": [
      {
        "id": "0ZPxx0000000001AAA",
        "name": "Summer_Sale_2025",
        "displayName": "Summer Electronics Sale",
        "description": "Get 20% off on all Samsung devices",
        "priority": 100,
        "startDateTime": "2025-06-01T00:00:00Z",
        "endDateTime": "2025-08-31T23:59:59Z",
        "isAutomatic": true,
        "isCategoryPromo": true,
        "isProductPromo": false,
        "couponCode": null,
        "termsAndConditions": "Valid on all Samsung products. Cannot be combined with other offers."
      },
      {
        "id": "0ZPxx0000000002AAA",
        "name": "Electronics_Bundle",
        "displayName": "Bundle & Save",
        "description": "Save 15% when you buy 2 or more items",
        "priority": 90,
        "startDateTime": "2025-05-15T00:00:00Z",
        "endDateTime": "2025-12-31T23:59:59Z",
        "isAutomatic": false,
        "isCategoryPromo": false,
        "isProductPromo": true,
        "couponCode": "BUNDLE15",
        "termsAndConditions": "Minimum 2 items required."
      }
    ]
  }
}
```

          

          
: This example shows a sample response with visibility rule
            details.

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "contextId": "0000000r25tp21g002517756484726523db13b6a0ce245dc98062eb32a583a69",
  "correlationId": "81e072e2-e1ae-4321-9b73-d591f75854ec",
  "cursor": "MTAwMDAwMDAwNg==",
  "facets": [],
  "limit": 12,
  "query": {},
  "result": [
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [
        {
          "customFields": {},
          "id": "0ZSVW000000AhdC4AS",
          "name": "QuantumBit Hardware",
          "numberOfCategories": 11
        }
      ],
      "categories": [
        {
          "catalogId": "0ZSVW000000AhdC4AS",
          "childCategories": [],
          "customFields": {},
          "eligiblePromotions": [],
          "id": "0ZGVW000000IUEC4A4",
          "name": "Memory"
        }
      ],
      "childVariationIds": [],
      "configurationRules": [
        {
          "details": [
            {
              "message": "32GB RDIMM disables 128GB LRDIMM"
            }
          ],
          "type": "disable"
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "128GB RDIMM",
      "displayUrl": "/resource/ram_32GB_RDIMM",
      "eligiblePromotions": [],
      "id": "01tVW000003l7v5YAA",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "128GB LRDIMM",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isDerived": false,
          "isSelected": false,
          "price": 0,
          "priceBookEntryId": "01uVW000000jzfJYAQ",
          "priceBookId": "01sVW0000024PZlYAM",
          "pricingModel": {
            "id": "0jPVW0000001fh42AA",
            "name": "One-Time",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "productClass": "Simple",
      "productClassification": {},
      "productCode": "QB-MEM 128GB",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iOVW00000049xS2AQ",
          "isDefault": true,
          "productId": "01tVW000003l7v5YAA",
          "productSellingModel": {
            "doesAutoRenewByDefault": false,
            "id": "0jPVW0000001fh42AA",
            "name": "One-Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPVW0000001fh42AA"
        }
      ],
      "productUnitOfMeasures": []
    }
  ],
  "total": 1
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `api​Status` | [API Status](./connect_responses_api_status_output.htm.md) | Status of the API request. | Small, 60.0 | 60.0 |
| `context​Id` | String | ID of the context. | Small, 60.0 | 60.0 |
| `correlation​Id` | String | Unique ID of the request. | Small, 60.0 | 60.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Small, 60.0 | 60.0 |
| `facets` | [Search Products Facet](./connect_responses_search_products_facet.htm.md) | Details of the faceted search. | Small, 63.0 | 63.0 |
| `limit` | Integer | Number of items fetched in the response. | Small, 60.0 | 60.0 |
| `offSet` | Integer | Offset size from which the item count is fetched. | Small, 60.0 | 60.0 |
| `query` | Map<String, Object> | Query that was used for the search request. | Small, 60.0 | 60.0 |
| `result` | Any response body | Result that contains the list of catalogs, categories, or products as per the requested resource. | Small, 60.0 | 60.0 |
| `total` | Integer | Number of fetched records. | Small, 60.0 | 60.0 |
| `user​Context` | [User Context](./connect_responses_user_context_output.htm.md) | User context details. For example, account ID or contact ID. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_cpq_message_output.htm ===
---
page_id: connect_responses_cpq_message_output.htm
title: CPQ Message
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_cpq_message_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CPQ Message

Output representation of the API messages.

- 
- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code specifying the type of message. Valid value is `CartValidationError`. | Small, 60.0 | 60.0 |
| `detail` | String | Required details other than the message text. | Small, 60.0 | 60.0 |
| `message` | String | Text of the API message. | Small, 60.0 | 60.0 |
| `severity` | String | Severity of the API message. Valid values are: `Error` `Info` `Warning` | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_data_rounding_output.htm ===
---
page_id: connect_responses_data_rounding_output.htm
title: Data Rounding
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_data_rounding_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Rounding

Output representation of the data rounding response.

      
        
          

**JSON example**

          
: 
            

```
{
  "keyToUomDataRowOutput": {
    "PRC1": {
      "key": "PRC1",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": true,
          "roundedValue": 1234.56,
          "unitOfMeasureId": "uomId1",
          "errorCodeToErrorMap" : []
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 643.1,
          "isRoundingApplicable": true,
          "roundedValue": 643.1,
          "unitOfMeasureId": "uomId1"
        }
      },
      "errorCodeToErrorMap" : []
    },
    "PRC2": {
      "key": "PRC2",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": true,
          "roundedValue": 1234.56,
          "unitOfMeasureId": "uomId1"
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "isRoundingApplicable": true,
          "errorCodeToErrorMap": {
            "message": "arithrmetic operation"
          },
          "unitOfMeasureId": "uomId1"
        }
      },
      "errorCodeToErrorMap": []
    },
    "PRC3": {
      "key": "PRC3",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": false,
          "unitOfMeasureId": "uomId2"
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "isRoundingApplicable": false,
          "unitOfMeasureId": "uomId2"
        }
      },
      "errorCodeToErrorMap": []
    }
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 63.0 | 63.0 |
| `errorCode​ToErrorMap` | Map<String, [Unit Of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)> | Error codes mapped to their details. | Small, 63.0 | 63.0 |
| `keyToData​RowOutput` | Map<String, [Data Row](./connect_responses_data_row_output.htm.md)> | Data row key mapped to the associated data row. | Small, 63.0 | 63.0 |
| `status` | [Unit Of Measure Status](./connect_responses_unit_of_measure_status.htm.md)[] | Status of the API request. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_data_row_output.htm ===
---
page_id: connect_responses_data_row_output.htm
title: Data Row
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_data_row_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Row

Output representation of the details of a data row.

        
          

**JSON example**

          
: 
            

```
{
  "keyToUomDataRowOutput": {
    "PRC1": {
      "key": "PRC1",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": true,
          "roundedValue": 1234.56,
          "unitOfMeasureId": "uomId1",
          "errorCodeToErrorMap" : []
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 643.1,
          "isRoundingApplicable": true,
          "roundedValue": 643.1,
          "unitOfMeasureId": "uomId1"
        }
      },
      "errorCodeToErrorMap" : []
    },
    "PRC2": {
      "key": "PRC2",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": true,
          "roundedValue": 1234.56,
          "unitOfMeasureId": "uomId1"
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "isRoundingApplicable": true,
          "errorCodeToErrorMap": {
            "message": "arithrmetic operation"
          },
          "unitOfMeasureId": "uomId1"
        }
      },
      "errorCodeToErrorMap": []
    },
    "PRC3": {
      "key": "PRC3",
      "fieldApiNameToFieldDataOutput": {
        "MaxQuantity": {
          "fieldApiName": "MaxQuantity",
          "originalValue": 1234.5678,
          "isRoundingApplicable": false,
          "unitOfMeasureId": "uomId2"
        },
        "MinQuantity": {
          "fieldApiName": "MinQuantity",
          "originalValue": 987.4628,
          "isRoundingApplicable": false,
          "unitOfMeasureId": "uomId2"
        }
      },
      "errorCodeToErrorMap": []
    }
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode​ToErrorMap` | Map<String, [Unit Of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)> | Map of error codes to their details. | Small, 63.0 | 63.0 |
| `fieldApi​NameToField​DataOutput` | Map<String, [Field Data](./connect_responses_field_data_output.htm.md)> | Map of field API name to associated field data. | Small, 63.0 | 63.0 |
| `key` | String | Unique key of the data row. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_deep_clone_error.htm ===
---
page_id: connect_responses_deep_clone_error.htm
title: Deep Clone Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_deep_clone_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone Error

Output representation of the error details related to the deep clone request.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​Code` | String | Code of the error message related to the deep clone request. | Small, 63.0 | 63.0 |
| `error​Message` | String | Details of the error message related to the deep clone request. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_deep_clone_record_response.htm ===
---
page_id: connect_responses_deep_clone_record_response.htm
title: Deep Clone Record Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_deep_clone_record_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone Record Response

Output representation of the details of the cloned related records.

        
          

**JSON example**

          
: 
            

```
  "createdRecordList": [
    {
      "createdRecordId": "01tSG0000030Yb3YAE",
      "entityApiName": "Product2",
      "entityLabel": "Product"
    },
    {
      "createdRecordId": "0iOSG0000002rMn2AI",
      "entityApiName": "ProductSellingModelOption",
      "entityLabel": "Product Selling Model Option"
    },
    {
      "createdRecordId": "0v7SG0000001ktdYAA",
      "entityApiName": "ProductAttributeDefinition",
      "entityLabel": "Product Attribute Definition"
    }
  ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `created​RecordId` | String | ID of the created related record. | Small, 63.0 | 63.0 |
| `entity​ApiName` | String | API name of the created object. | Small, 63.0 | 63.0 |
| `entity​Label` | String | Label of the created object. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_deep_clone_response.htm ===
---
page_id: connect_responses_deep_clone_response.htm
title: Deep Clone Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_deep_clone_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Deep Clone Response

Output representation of the details of the cloned record.

        
          

**JSON example**

          
: 
            

```
{
  "createdRecordList": [
    {
      "createdRecordId": "01tSG0000030Yb3YAE",
      "entityApiName": "Product2",
      "entityLabel": "Product"
    },
    {
      "createdRecordId": "0iOSG0000002rMn2AI",
      "entityApiName": "ProductSellingModelOption",
      "entityLabel": "Product Selling Model Option"
    },
    {
      "createdRecordId": "0v7SG0000001ktdYAA",
      "entityApiName": "ProductAttributeDefinition",
      "entityLabel": "Product Attribute Definition"
    }
  ],
  "createdRootRecordId": "01tSG0000030Yb3YAE",
  "errorList": [],
  "isSuccessful": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `created​RecordList` | [Deep Clone Record Response](./connect_responses_deep_clone_record_response.htm.md)[] | List of cloned related records of the main record. | Small, 63.0 | 63.0 |
| `createdRoot​RecordId` | String | ID of the created root record. | Small, 63.0 | 63.0 |
| `error​List` | [Deep Clone Error](./connect_responses_deep_clone_error.htm.md)[] | Details of errors, if any. | Small, 63.0 | 63.0 |
| `error​Message` | String | Error message if the API request fails. | Small, 63.0 | 63.0 |
| `is​Successful` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_epc_error_output.htm ===
---
page_id: connect_responses_epc_error_output.htm
title: Error Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_epc_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error
    Output

Output representation of the error details.

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​Code` | String | Code of the error message. | Small, 60.0 | 60.0 |
| `message​Detail` | String | Details of the error message. | Small, 60.0 | 60.0 |
| `message​Title` | String | Title of the error message. | Small, 60.0 | 60.0 |
| `node​ProductId` | String | ID of the product node. | Small, 61.0 | 61.0 |
| `record​Id` | String | ID of the record. | Small, 60.0 | 60.0 |
| `record​Name` | String | Name of the record. | Small, 60.0 | 60.0 |
| `related​ObjectNodes` | [Invalid Related Object Node](./connect_responses_invalid_related_object_node_output.htm.md)[] | List of related object nodes with errors. | Small, 62.0 | 62.0 |
| `source` | String | Name of the API that’s the source of the error. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_facet_value.htm ===
---
page_id: connect_responses_facet_value.htm
title: Facet Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_facet_value.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Facet Value

Output representation of the facet values found in the search result.

        
          

**JSON example**

          
: 
            

```

      "values": [
        {
          "displayName": "1080p Built-in Display",
          "nameOrId": "1080p Built-in Display"
        },
        {
          "displayName": "2k Built-in Display",
          "nameOrId": "2k Built-in Display"
        },
        {
          "displayName": "4k Built-in Display",
          "nameOrId": "4k Built-in Display"
        }
      ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `display​Name` | String | Display name of the facet value. | Small, 63.0 | 63.0 |
| `nameOr​Id` | String | ID or the internal name of the facet value. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_facet_value_output.htm ===
---
page_id: connect_responses_facet_value_output.htm
title: Facet Value
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_facet_value_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Facet Value

Output representation of the facet values found in the search result.

      
        
          

**JSON example**

          
: 
            

```

      "values": [
        {
          "displayName": "Simple",
          "nameOrId": "Simple",
          "productCount": 9
        }
      ]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `display​Name` | String | Display name of the facet value. | Small, 63.0 | 63.0 |
| `nameOr​Id` | String | Facet value name or ID. Reserved for internal use. | Small, 63.0 | 63.0 |
| `product​Count` |  | Number of products in the search result that match the facet value. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_field_data_output.htm ===
---
page_id: connect_responses_field_data_output.htm
title: Field Data
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_field_data_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Field Data

Output representation of the field data.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode​ToErrorMap` | Map<String, [Unit Of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)> | Error codes mapped to their details. | Small, 63.0 | 63.0 |
| `fieldApiName` | String | Unique API Name of the field. | Small, 63.0 | 63.0 |
| `isRounding​Applicable` | Boolean | Indicates whether data rounding is applicable to the decimal (`true`) or not (`false`). | Small, 63.0 | 63.0 |
| `original​Value` | String | Original value of the field. | Small, 63.0 | 63.0 |
| `rounded​Value` | String | Rounded field value that corresponds to the original value, if data rounding is applicable. | Small, 63.0 | 63.0 |
| `unitOf​MeasureId` | String | ID of the unit of measure record that’s associated to the field. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_fields_info_output.htm ===
---
page_id: connect_responses_fields_info_output.htm
title: Fields Info
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_fields_info_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Fields Info

Output representation of the metadata fields in an object.

        
          

**JSON example**

          
: 
            

```
        "fields": [
          {
            "dataType": "text",
            "isFacetableConfigurable": true,
            "isSearchableConfigurable": false,
            "label": "Product Name",
            "name": "Name",
            "type": "Standard"
          },
          {
            "dataType": "multilinetext",
            "isFacetableConfigurable": false,
            "isSearchableConfigurable": true,
            "label": "Product Description",
            "name": "Description",
            "type": "Standard"
          }
        ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `customField​Id` | String | ID of the custom field. | Small, 62.0 | 62.0 |
| `dataType` | String | Type of data. | Small, 62.0 | 62.0 |
| `is​Configurable` | Boolean | Reserved for internal use. | Small, 62.0 | 62.0 |
| `isFacetable​Configurable` | Boolean | Indicates whether the field is facetable (`true`) or not (`false`). | Small, 63.0 | Small, 63.0 |
| `isSearchable​Configurable` | Boolean | Indicates whether the field is searchable (`true`) or not (`false`). | Small, 63.0 | Small, 63.0 |
| `label` | String | Label of the object field. | Small, 62.0 | 62.0 |
| `name` | String | Name of the object field. | Small, 62.0 | 62.0 |
| `type` | String | Type of the object field. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_guided_selection_output.htm ===
---
page_id: connect_responses_guided_selection_output.htm
title: Guided Selection
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_guided_selection_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guided Selection

Output representation of the details of a guided selection.

        
          

**JSON example**

          
: 

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FETCHED_DETAILS_SUCCESSFULLY"
  },
  "correlationId": "corrId",
  "cursor": "MTAwMDAwMDAwNg==",
  "searchTerms": [
    {
      "term": "IPhone"
    },
    {
      "term": "4GB"
    },
    {
      "term": "64GB"
    }
  ],
  "result": [
    {
      "additionalFields": {
        "CustomField1__c": "TextValue",
        "CustomField2__c": "10",
        "StandardField1": "false"
      },
      "description": "IPhone-13",
      "id": "01txx0000006kYwAAI",
      "name": "Sample product 1",
      "prices": [
        {
          "price": 150,
          "priceBookEntryId": "12Axx0000004DF7EAM",
          "priceBookId": "01sxx0000005puLAAQ",
          "pricingModel": {
            "frequency": "Monthly",
            "id": "12Bxx000000CiCDEA0",
            "name": "IPhone-13",
            "occurrence": 6,
            "pricingModelType": "Recurring"
          }
        },
        {
          "price": 400,
          "priceBookEntryId": "12Axx0000004DGjEAM",
          "priceBookId": "01sxx0000005puLAAQ",
          "pricingModel": {
            "id": "12Bxx000000CiCCEA0",
            "name": "IPhone-13",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

This example shows a sample response with details of eligible
            promotions.

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FETCHED_DETAILS_SUCCESSFULLY"
  },
  "correlationId": "corrId",
  "cursor": "MTAwMDAwMDAwNg==",
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
  "result": [
    {
      "additionalFields": {
        "CustomField1__c": "TextValue",
        "CustomField2__c": "10",
        "StandardField1": "false"
      },
      "description": "IPhone-13",
      "id": "01txx0000006kYwAAI",
      "name": "Sample product 1",
      "prices": [
        {
          "price": 150,
          "priceBookEntryId": "12Axx0000004DF7EAM",
          "priceBookId": "01sxx0000005puLAAQ",
          "pricingModel": {
            "frequency": "Monthly",
            "id": "12Bxx000000CiCDEA0",
            "name": "IPhone-13",
            "occurrence": 6,
            "pricingModelType": "Recurring"
          }
        },
        {
          "price": 400,
          "priceBookEntryId": "12Axx0000004DGjEAM",
          "priceBookId": "01sxx0000005puLAAQ",
          "pricingModel": {
            "id": "12Bxx000000CiCCEA0",
            "name": "IPhone-13",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "qualificationContext": {
        "isQualified": true
      },
      "eligiblePromotions": [
        {
          "id": "0ZPxx0000000001AAA",
          "name": "IPhone_Promotion_2025",
          "displayName": "iPhone Special Offer",
          "description": "Get 15% off on iPhone 13",
          "priority": 100,
          "startDateTime": "2025-03-01T00:00:00Z",
          "endDateTime": "2025-03-31T23:59:59Z",
          "isAutomatic": true,
          "isCategoryPromo": false,
          "isProductPromo": true,
          "couponCode": null,
          "termsAndConditions": "Valid on iPhone 13 models only."
        },
        {
          "id": "0ZPxx0000000002AAA",
          "name": "Memory_Upgrade_Deal",
          "displayName": "Free Memory Upgrade",
          "description": "Upgrade to 128GB for the price of 64GB",
          "priority": 90,
          "startDateTime": "2025-02-01T00:00:00Z",
          "endDateTime": "2025-12-31T23:59:59Z",
          "isAutomatic": false,
          "isCategoryPromo": false,
          "isProductPromo": true,
          "couponCode": "MEMORY128",
          "termsAndConditions": "Applies to select iPhone models."
        }
      ]
    }
  ]
}
```

          
: This example shows a sample request to run visibility
            rules.

```
{
  "apiStatus": {
    "messages": [],
    "statusCode": "FetchedDetailsSuccessfully"
  },
  "correlationId": "ef4f324d-b6d9-47ca-9e78-c6ec60ca5b23",
  "cursor": "MTAwMDAwMDAwNg==",
  "offSet": 1,
  "result": [
    {
      "additionalFields": {},
      "attributeCategories": [],
      "catalogs": [
        {
          "customFields": {},
          "id": "0ZSVW000000AhdC4AS",
          "name": "QuantumBit Hardware",
          "numberOfCategories": 11
        }
      ],
      "categories": [
        {
          "catalogId": "0ZSVW000000AhdC4AS",
          "childCategories": [],
          "customFields": {},
          "eligiblePromotions": [],
          "id": "0ZGVW000000IUEC4A4",
          "name": "Memory"
        }
      ],
      "childProducts": [],
      "childVariationIds": [],
      "configurationRules": [
        {
          "details": [
            {
              "message": "32GB RDIMM disables 128GB LRDIMM"
            }
          ],
          "type": "disable"
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "128GB RDIMM",
      "displayUrl": "/resource/ram_32GB_RDIMM",
      "eligiblePromotions": [],
      "id": "01tVW000003l7v5YAA",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "128GB LRDIMM",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isDerived": false,
          "isSelected": false,
          "price": 0,
          "priceBookEntryId": "01uVW000000jzfJYAQ",
          "priceBookId": "01sVW0000024PZlYAM",
          "pricingModel": {
            "id": "0jPVW0000001fh42AA",
            "name": "One-Time",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "productClass": "Simple",
      "productClassification": {},
      "productCode": "QB-MEM 128GB",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iOVW00000049xS2AQ",
          "isDefault": true,
          "productId": "01tVW000003l7v5YAA",
          "productSellingModel": {
            "doesAutoRenewByDefault": false,
            "id": "0jPVW0000001fh42AA",
            "name": "One-Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPVW0000001fh42AA"
        }
      ],
      "productUnitOfMeasures": []
    }
  ],
  "searchTerms": [
    {
      "tags": [],
      "term": "128GB LRDIMM"
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `apiStatus` | [API Status](./connect_responses_api_status_output.htm.md) | Status of the API request. | Small, 62.0 | 62.0 |
| `correlation​Id` | String | Unique ID of the request. | Small, 62.0 | 62.0 |
| `cursor` | String | Unique ID to represent the position of each product in the dataset. | Small, 62.0 | 62.0 |
| `result` | Any response body | Result that contains the list of products as per the requested resource. | Small, 62.0 | 62.0 |
| `searchTerms` | [Guided Selection Search Term](./connect_responses_guided_selection_search_term_output.htm.md)[] | Search terms for the guided selection. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_guided_selection_search_term_output.htm ===
---
page_id: connect_responses_guided_selection_search_term_output.htm
title: Guided Selection Search Term
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_guided_selection_search_term_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Guided Selection Search Term

Output representation of the search term details for a guided selection.

        
          

**JSON example**

          
: 
            

```
{
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
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `tags` | String[] | Search term tags for the guided selection. | Small, 62.0 | 62.0 |
| `term` | String | Search term value for the guided selection. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_index_configuration_collection_output.htm ===
---
page_id: connect_responses_index_configuration_collection_output.htm
title: Index Configuration Collection
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_configuration_collection_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configuration Collection

Output representation of the collection of index configuration details.

        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "ad960cb6-392d-4d11-bac3-3824baedf67e",
  "errors": [],
  "indexConfigurations": [
    {
      "isSearchable": true,
      "name": "Name",
      "type": "Standard"
    }
  ],
  "metadata": {
    "objectInfos": [
      {
        "fields": [
          {
            "dataType": "text",
            "isFacetableConfigurable": true,
            "isSearchableConfigurable": false,
            "label": "Product Name",
            "name": "Name",
            "type": "Standard"
          },
          {
            "dataType": "multilinetext",
            "isFacetableConfigurable": false,
            "isSearchableConfigurable": true,
            "label": "Product Description",
            "name": "Description",
            "type": "Standard"
          }
        ],
        "name": "Product2"
      },
      {
        "fields": [
          {
            "dataType": "stringplusclob",
            "label": "Description",
            "name": "Description",
            "type": "ProductAttributeDefinitionStandard"
          },
          {
            "dataType": "text",
            "label": "Name",
            "name": "Name",
            "type": "ProductAttributeDefinitionStandard"
          },
        ],
        "name": "ProductAttributeDefinition"
      }
    ]
  },
  "statusCode": "200"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 62.0 | 62.0 |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 62.0 | 62.0 |
| `index​Configurations` | [Index Configuration Field](./connect_responses_index_configuration_field_output.htm.md)[] | Details of the index-configured fields. | Small, 62.0 | 62.0 |
| `metadata` | [Metadata](./connect_responses_metadata_output.htm.md)[] | Details of the metadata for objects. | Small, 62.0 | 62.0 |
| `statusCode` | String | Code that indicates the status of the request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_index_configuration_field_output.htm ===
---
page_id: connect_responses_index_configuration_field_output.htm
title: Index Configuration Field
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_configuration_field_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configuration Field

Output representation of the details of the index-configured field.

        
          

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

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attribute​DefinitionId` | String | ID of the attribute definition. | Small, 62.0 | 62.0 |
| `attribute​FieldId` | String | ID of the attribute field. | Small, 62.0 | 62.0 |
| `facetDisplay​Rank` | Integer | Sort order for displaying the facets at run time. | Small, 63.0 | 63.0 |
| `is​Facetable` | Boolean | Indicates whether the field is facetable (`true`) or not (`false`). | Small, 63.0 | 63.0 |
| `is​Searchable` | Boolean | Indicates whether the index-configured field is searchable (`true`) or not (`false`). | Small, 62.0 | 62.0 |
| `name` | String | Name of the index-configured field. | Small, 62.0 | 62.0 |
| `type` | String | Type of the index-configured field. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_index_configurations_update_output.htm ===
---
page_id: connect_responses_index_configurations_update_output.htm
title: Index Configurations Update
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_configurations_update_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Configurations Update

Output representation of the updated index configuration.

        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "8545b5aa-f3e6-429a-8f21-9cc4ce50b1d7",
  "errors": [],
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
  ],
  "statusCode": "200"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 62.0 | 62.0 |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 62.0 | 62.0 |
| `index​Configurations` | [Index Configuration Field](./connect_responses_index_configuration_field_output.htm.md)[] | Details of the index-configured fields. | Small, 62.0 | 62.0 |
| `status​Code` | String | Code that indicates the status of the request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_index_error_output.htm ===
---
page_id: connect_responses_index_error_output.htm
title: Index Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Error

Output representation of the error details related to an index.

      
        
          

**JSON example**

          
: 
            

```
  "indexErrorDetails": {
    "errorFileId": "069xx0000004C92AAE",
    "indexCreatedDate": "2024-10-03T05:24:18.000Z",
    "indexErrorsCount": 1,
    "indexLastUpdatedDate": "2024-10-03T05:27:00.000Z",
    "itemLevelErrorsCount": 1
  }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​FileId` | String | ID of the exported error file that contains the index errors. | Small, 63.0 | 63.0 |
| `indexCreated​Date` | String | Date on which the index was created. | Small, 63.0 | 63.0 |
| `index​ErrorsCount` | Integer | Number of index-level errors. | Small, 63.0 | 63.0 |
| `indexLast​UpdatedDate` | String | Date on which the index was last updated. | Small, 63.0 | 63.0 |
| `itemLevel​ErrorsCount` | Integer | Number of item-level errors. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_index_setting_output.htm ===
---
page_id: connect_responses_index_setting_output.htm
title: Index Setting
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_setting_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Setting

Output representation of the retrieved index settings.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "errors": [],
  "metadata": {
    "activeLanguages": ["en_US","ja","es","nl_NL"]
  },
  "setting": {
    "defaultLanguage": "en_US",
    "id": "1JySG0000000GUb0AM",
    "supportedLanguages": ["en_US","ja","es","nl_NL"]
  },
  "statusCode": "200"
}
```

          

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 63.0 | 63.0 |
| `metadata` | [Setting Metadata](./connect_responses_setting_metadata_output.htm.md)[] | Metadata associated with the setting. | Small, 63.0 | 63.0 |
| `setting` | [Setting](./connect_responses_setting_output.htm.md)[] | Setting that’s used in indexing and maintained for an org. | Small, 63.0 | 63.0 |
| `status​Code` | String | Code that indicates the status of the request. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_index_setting_patch_output.htm ===
---
page_id: connect_responses_index_setting_patch_output.htm
title: Index Setting Update
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_index_setting_patch_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Index Setting Update

Output representation of the details of the updated index setting.

    
      
        
          

**JSON example**

          
: 
            

```
{
   "setting" : {
        "supportedLanguages" : ["en_US","ja","es","nl_NL"],
        "id": "1JySG0000000GUb0AM",
        "defaultLanguage" : "en_US"
   },
   "errors" : [],
   "statusCode" : "200"
}
```

          

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 63.0 | 63.0 |
| `setting` | [Setting](./connect_responses_setting_output.htm.md)[] | Setting that’s used in indexing and maintained for an org. | Small, 63.0 | 63.0 |
| `statusCode` | String | Code that indicates the status of the API request. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_invalid_related_object_node_output.htm ===
---
page_id: connect_responses_invalid_related_object_node_output.htm
title: Invalid Related Object Node
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invalid_related_object_node_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invalid Related Object Node

Output representation of the invalid related object node with details of
    errors.

      
        
          

**JSON example**

          
: 
            

```
To add
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorMessages` | String[] | List of error messages. | Small, 62.0 | 62.0 |
| `related​Object​APIName` | String | API name of the related object. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_metadata_output.htm ===
---
page_id: connect_responses_metadata_output.htm
title: Metadata
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_metadata_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Metadata

Output representation of the metadata details for objects.

        
          

**JSON example**

          
: 
            

```
  "metadata": {
    "objectInfos": [
      {
        "fields": [
          {
            "dataType": "text",
            "isFacetableConfigurable": true,
            "isSearchableConfigurable": false,
            "label": "Product Name",
            "name": "Name",
            "type": "Standard"
          },
          {
            "dataType": "multilinetext",
            "isFacetableConfigurable": false,
            "isSearchableConfigurable": true,
            "label": "Product Description",
            "name": "Description",
            "type": "Standard"
          }
        ],
        "name": "Product2"
      },
      {
        "fields": [
          {
            "dataType": "stringplusclob",
            "label": "Description",
            "name": "Description",
            "type": "ProductAttributeDefinitionStandard"
          },
          {
            "dataType": "text",
            "label": "Name",
            "name": "Name",
            "type": "ProductAttributeDefinitionStandard"
          },
        ],
        "name": "ProductAttributeDefinition"
      }
    ]
  }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `objectInfos` | [Object Info](./connect_responses_object_info_output.htm.md)[] | Metadata details for objects. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_object_info_output.htm ===
---
page_id: connect_responses_object_info_output.htm
title: Object Info
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_object_info_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Object Info

Output representation of the object details along with its fields.

        
          

**JSON example**

          
: 
            

```
    "objectInfos": [
      {
        "fields": [
          {
            "dataType": "text",
            "isFacetableConfigurable": true,
            "isSearchableConfigurable": false,
            "label": "Product Name",
            "name": "Name",
            "type": "Standard"
          },
          {
            "dataType": "multilinetext",
            "isFacetableConfigurable": false,
            "isSearchableConfigurable": true,
            "label": "Product Description",
            "name": "Description",
            "type": "Standard"
          }
        ],
        "name": "Product2"
      },
      {
        "fields": [
          {
            "dataType": "stringplusclob",
            "label": "Description",
            "name": "Description",
            "type": "ProductAttributeDefinitionStandard"
          },
          {
            "dataType": "text",
            "label": "Name",
            "name": "Name",
            "type": "ProductAttributeDefinitionStandard"
          },
        ],
        "name": "ProductAttributeDefinition"
      }
    ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `fields` | [Fields Info](./connect_responses_fields_info_output.htm.md)[] | Fields of the object. | Small, 62.0 | 62.0 |
| `name` | String | Name of the object. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_p_c_m_error_output.htm ===
---
page_id: connect_responses_p_c_m_error_output.htm
title: Product Catalog Management Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_p_c_m_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Error

Output representation that contains error details, including error codes and
    messages.

        
          

**JSON example**

          
: 
            

```
{
  "errorCode": "INSUFFICIENT_ACCESS",
  "message": "Insufficient access rights on cross-reference ID"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Error code that identifies the type of error. | Small, 66.0 | 66.0 |
| `message` | String | Message that explains the reason for the error. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_pricing_model_output.htm ===
---
page_id: connect_responses_pricing_model_output.htm
title: Pricing Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_pricing_model_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Pricing Model

Output representation of the details of the pricing model.

        
          

**JSON example**

          
: 
            

```
{
  "pricingModel": {
    "id": "0jPSG000000Avcv2AC",
    "name": "One Time",
    "pricingModelType": "OneTime"
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `frequency` | String | Details about the frequency of recurrence of the pricing model. | Small, 67.0 | 67.0 |
| `id` | String | ID of the pricing model. | Small, 67.0 | 67.0 |
| `name` | String | Name of the pricing model. | Small, 67.0 | 67.0 |
| `occurrence` | Integer | Details about the number of occurrences of the pricing model. | Small, 67.0 | 67.0 |
| `pricingModelType` | String | Type of the pricing model. | Small, 67.0 | 67.0 |
| `unitOfMeasure` | String | Unit of measure for the pricing model. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_classification_details_collection_output.htm ===
---
page_id: connect_responses_product_classification_details_collection_output.htm
title: Product Classification Details Collection
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_classification_details_collection_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification Details Collection

Output representation that contains a collection of product classification details along
    with any processing errors.

        
          

**JSON example**

          
: 
            

```
{
  "success": false,
  "errors": [
    {
      "errorCode": "INSUFFICIENT_ACCESS",
      "message": "Insufficient access rights on cross-reference ID"
    }
  ],
  "productClassifications": [
    {
      "id": "dummyId",
      "name": "Dummy Product Classification",
      "code": "DUMMY_CODE",
      "attributeCategories": [
        {
          "attributes": [
            {
              "attributeNameOverride": "Dummy_Attribute__c",
              "code": "ATTR_CODE_1",
              "dataType": "String",
              "defaultValue": "default",
              "description": "A dummy attribute for demonstration.",
              "developerName": "Dummy_Attribute",
              "displayType": "Text",
              "helpText": "Help text for dummy attribute",
              "id": "attrId1",
              "isConfigurable": true,
              "isHidden": false,
              "isPriceImpacting": false,
              "isReadOnly": false,
              "isRequired": false,
              "isValueCloneable": true,
              "label": "Dummy Attribute Label",
              "maximumCharacterCount": 100,
              "maximumValue": "100",
              "minimumCharacterCount": 1,
              "minimumValue": "1",
              "name": "Dummy Attribute",
              "sequence": 1,
              "status": "Active",
              "stepValue": "1"
            }
          ],
          "code": "GENERAL",
          "id": "catId1",
          "name": "General"
        }
      ],
      "attributes": [
        {
          "attributeNameOverride": "Dummy_Attribute__c",
          "code": "ATTR_CODE_1",
          "dataType": "String",
          "defaultValue": "default",
          "description": "A dummy attribute for demonstration.",
          "developerName": "Dummy_Attribute",
          "displayType": "Text",
          "helpText": "Help text for dummy attribute",
          "id": "attrId1",
          "isConfigurable": true,
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": false,
          "isValueCloneable": true,
          "label": "Dummy Attribute Label",
          "maximumCharacterCount": 100,
          "maximumValue": "100",
          "minimumCharacterCount": 1,
          "minimumValue": "1",
          "name": "Dummy Attribute",
          "sequence": 1,
          "status": "Active",
          "stepValue": "1"
        }
      ]
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Product Catalog Management Error](./connect_responses_p_c_m_error_output.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 66.0 | 66.0 |
| `productClassifications` | [Product Classification Details](./connect_responses_product_classification_details_output.htm.md)[] | List of product classification detail records that match the requested product classification IDs. | Small, 66.0 | 66.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or has failed (`false`). | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_product_classification_details_output.htm ===
---
page_id: connect_responses_product_classification_details_output.htm
title: Product Classification Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_classification_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification Details

Output representation that contains the details of a single product classification,
    including its attributes and categories.

        
          

**JSON example**

          
: 
            

```
{
  "id": "dummyId",
  "name": "Dummy Product Classification",
  "code": "DUMMY_CODE",
  "attributeCategories": [{
          "attributes": [
            {
              "attributeNameOverride": "Dummy_Attribute__c",
              "code": "ATTR_CODE_1",
              "dataType": "String",
              "defaultValue": "default",
              "description": "A dummy attribute for demonstration.",
              "developerName": "Dummy_Attribute",
              "displayType": "Text",
              "helpText": "Help text for dummy attribute",
              "id": "attrId1",
              "isConfigurable": true,
              "isHidden": false,
              "isPriceImpacting": false,
              "isReadOnly": false,
              "isRequired": false,
              "isValueCloneable": true,
              "label": "Dummy Attribute Label",
              "maximumCharacterCount": 100,
              "maximumValue": "100",
              "minimumCharacterCount": 1,
              "minimumValue": "1",
              "name": "Dummy Attribute",
              "sequence": 1,
              "status": "Active",
              "stepValue": "1"
            }
          ],
          "code": "GENERAL",
          "id": "catId1",
          "name": "General"
        }],
  "attributes": [{
          "attributeNameOverride": "Dummy_Attribute__c",
          "code": "ATTR_CODE_1",
          "dataType": "String",
          "defaultValue": "default",
          "description": "A dummy attribute for demonstration.",
          "developerName": "Dummy_Attribute",
          "displayType": "Text",
          "helpText": "Help text for dummy attribute",
          "id": "attrId1",
          "isConfigurable": true,
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": false,
          "isValueCloneable": true,
          "label": "Dummy Attribute Label",
          "maximumCharacterCount": 100,
          "maximumValue": "100",
          "minimumCharacterCount": 1,
          "minimumValue": "1",
          "name": "Dummy Attribute",
          "sequence": 1,
          "status": "Active",
          "stepValue": "1"
        }]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              
              

              

              

              

            

            
              

              
              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attributeCategories` | [Product Classification Attribute Category](./connect_responses_attribute_category_output.htm.md)[] | List of attribute categories applicable to the product classification. | Small, 66.0 | 66.0 |
| `attributes` | [Product Classification Attribute Definition](./connect_responses_attribute_definition_output.htm.md)[] | List of uncategorized attributes applicable to the product classification. | Small, 66.0 | 66.0 |
| `code` | String | Code of the product classification. | Small, 66.0 | 66.0 |
| `id` | String | ID of the product classification. | Small, 66.0 | 66.0 |
| `name` | String | Name of the product classification. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_product_classification_list_collection_output.htm ===
---
page_id: connect_responses_product_classification_list_collection_output.htm
title: Product Classification List Collection
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_classification_list_collection_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification List Collection

Output representation that contains a collection of product classification records
    along with any processing errors.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "success": true,
  "errors": [],
  "productClassifications": [
    {
      "id": "11BT10000004C9SMAU",
      "name": "Mobile Devices",
      "code": "MOB_DEV",
      "parentProductClassificationId": "11BDU0000004JXq2AM",
      "status": "Active"
    },
    {
      "id": "11BT10000004C9TMAU",
      "name": "Mobile Accessories",
      "code": "MOB_ACC",
      "status": "Active"
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Product Catalog Management Error](./connect_responses_p_c_m_error_output.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 67.0 | 67.0 |
| `productClassifications` | [Product Classification](./connect_responses_product_classification_output.htm.md)[] | List of product classification records that match the request query. | Small, 67.0 | 67.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or has failed (`false`). | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_classification_output.htm ===
---
page_id: connect_responses_product_classification_output.htm
title: Product Classification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_classification_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification

Output representation of the product classification details.

      
        
          

**JSON example**

          
: 
            

```
{
  "productClassification": {
    "id": "11BT10000004C9SMAU",
    "name": "class",
    "code": "code",
    "parentProductClassificationId": "11BDU0000004JXq2AM",
    "status": "Active"
  }
}
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code of the product classification record. | Small, 61.0 | 61.0 |
| `id` | String | ID of the product classification record. | Small, 60.0 | 60.0 |
| `name` | String | Name of the product classification record. If data translation is set up and specified in the org, the translated description is available. | Small, 61.0 | 61.0 |
| `parentProduct​Classification​Id` | String | ID of the parent product classification. | Small, 65.0 | 65.0 |
| `status` | String | Status of the product classification record. | Small, 61.0 | 61.0 |

=== ARTICLE: connect_responses_product_component_group_output.htm ===
---
page_id: connect_responses_product_component_group_output.htm
title: Product Component Group
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_component_group_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Component Group

Output representation of the product component group.

      
        
          

**JSON example**

          
: 
            

```
"productComponentGroups":[
  {
    "childGroups":[
     {
      "childGroups":[],
    "    components":[
          {
            "additionalFields":{},
            "attributeCategory":[],
            "attributes":[],
            "catalogs":[],
            "categories":[],
            "childProducts":[],
            "id":"01txx0000006i2aAAA",
            "isActive":true,
            "isAssetizable":true,
            "isSoldOnlyWithOtherProds":true,
            "name":"GenWatt Diesel 1000kW",
            "nodeType":"simpleProduct",
            "productCode":"GC1060",
            "productComponentGroups":[],
            "productRelatedComponent":
             {
              "childProductId":"01txx0000006i2aAAA",
              "doesBundlePriceIncludeChild":true,
              "id":"0dSxx00000001P7EAI",
              "isComponentRequired":false,
              "isDefaultComponent":true,
              "isExcluded":false,
              "isQuantityEditable":false,
              "parentProductId":"01txx0000006iC8AAI",
              "productRelationshipTypeId":"0yoxx000000001dAAA",
              "quantity":1,
              "quantityScaleMethod":"Proportional"
              },
              "productSellingModelOptions":[]
              },
              {
              "additionalFields":{},
              "attributeCategory":[],
              "attributes":[],
              "catalogs":[],
              "categories":[],
              "childProducts":[],
              "id":"01txx0000006i2TAAQ",
              "isActive":true,
              "isAssetizable":true,
              "isSoldOnlyWithOtherProds":true,
              "name":"GenWatt Diesel 10kW",
              "nodeType":"simpleProduct",
              "productCode":"GC1020",
              "productComponentGroups":[],
              "productRelatedComponent":{
                  "childProductId":"01txx0000006i2TAAQ",
                  "doesBundlePriceIncludeChild":true,
                  "id":"0dSxx00000001P8EAI",
                  "isComponentRequired":false,
                  "isDefaultComponent":true,
                  "isExcluded":false,
                  "isQuantityEditable":false,
                  "parentProductId":"01txx0000006iC8AAI",
                  "productRelationshipTypeId":"0yoxx000000001dAAA",
                  "quantity":1,"quantityScaleMethod":"Proportional"
               },
              "productSellingModelOptions":[]
               },
               {
                "additionalFields":{},
                "attributeCategory":[],
                "attributes":[],
                "catalogs":[],
                "categories":[],
                "childProducts":[],
                "id":"01txx0000006i2SAAQ",
                "isActive":true,
                "isAssetizable":true,
                "isSoldOnlyWithOtherProds":true,
                "name":"GenWatt Diesel 200kW",
                "nodeType":"simpleProduct",
                "productCode":"GC1040",
                "productComponentGroups":[],
                "productRelatedComponent":
                  {
                    "childProductId":"01txx0000006i2SAAQ",
                    "doesBundlePriceIncludeChild":true,
                    "id":"0dSxx00000001P9EAI",
                    "isComponentRequired":false,
                    "isDefaultComponent":true,
                    "isExcluded":false,
                    "isQuantityEditable":false,
                    "parentProductId":"01txx0000006iC8AAI",
                    "productRelationshipTypeId":"0yoxx000000001dAAA",
                    "quantity":1,
                    "quantityScaleMethod":"Proportional"
                   },
                  "productSellingModelOptions":[]
                    }
                  ],
                  "id":"0y7xx000000015lAAA",
                  "isExcluded":false,
                  "name":"G1.1",
                  "parentGroupId":"0y7xx0000000149AAA",
                  "parentProductId":"01txx0000006iC8AAI"
                   }
                  ],
                "components":[],
                "id":"0y7xx0000000149AAA",
                "isExcluded":false,
                "name":"G1",
                "parentProductId":"01txx0000006iC8AAI"
                }
          ]
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Unique code of the product component group, which is used only during design time. | Small, 60.0 | 60.0 |
| `components` | [Product](./connect_responses_product_output.htm.md)[] | List of the product details. | Small, 60.0 | 60.0 |
| `childGroups` | [Product Component Group](#)[] | List of child product components groups. | Small, 62.0 | 62.0 |
| `description` | String | Description of the product component group. | Small, 60.0 | 60.0 |
| `id` | String | ID of the record. | Small, 60.0 | 60.0 |
| `isExcluded` | Boolean | Indicates whether the product component group is excluded from the product bundle for selection in the run time (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `max​Bundle​Components` | Integer | Maximum number of product components that can be added to a group. | Small, 60.0 | 60.0 |
| `min​Bundle​Components` | Integer | Minimum number of product components that can be added to a group. | Small, 60.0 | 60.0 |
| `name` | String | Name of the record. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `parent​Product​Id` | String | ID associated with the parent product record. | Small, 60.0 | 60.0 |
| `parent​GroupId` | String | ID of the parent group record. | Small, 62.0 | 62.0 |
| `sequence` | Integer | Order in which the groups are listed in the bundle. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_configuration_rule_details_output.htm ===
---
page_id: connect_responses_product_configuration_rule_details_output.htm
title: Product Configuration Rule Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_configuration_rule_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configuration Rule Details

Output representation of the product configuration rule details.

        
          

**JSON example**

          
: 
            

```
{
  "configurationRules": [
    {
      "details": [
        {
          "message": "recommend Mouse from monitor"
        }
      ],
      "type": "recommend"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | Message associated with the product configuration rule. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_configuration_rules_output.htm ===
---
page_id: connect_responses_product_configuration_rules_output.htm
title: Product Configuration Rules
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_configuration_rules_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Configuration Rules

Output representation of the details of the product configuration rules.

        
          

**JSON example**

          
: 
            

```
{
  "configurationRules": [
    {
      "details": [
        {
          "message": "recommend Mouse from monitor"
        }
      ],
      "type": "recommend"
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `details` | [Product Configuration Rule Details](./connect_responses_product_configuration_rule_details_output.htm.md)[] | Details of the product configuration rule. | Small, 67.0 | 67.0 |
| `type` | String | Type of the product configuration rule. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_catalog_output.htm ===
---
page_id: connect_responses_product_discovery_catalog_output.htm
title: Catalog Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_catalog_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Catalog Details

Output representation of the details of a catalog definition.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "catalogs": [
    {
      "customFields": {},
      "id": "0ZSSG000001875O4AQ",
      "name": "Hardware Catalog",
      "numberOfCategories": 4
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalogCode` | String | Unique ID associated with the catalog. | Small, 67.0 | 67.0 |
| `catalogType` | String | Category of an entry in the catalog, which is customizable. For example, catalog types, such as sellable products, services, parts, technical services, or technical resources. | Small, 67.0 | 67.0 |
| `customFields` | Map<String, Object> | Details of the custom fields associated with a catalog. | Small, 67.0 | 67.0 |
| `description` | String | Description of the catalog. | Small, 67.0 | 67.0 |
| `effectiveEndDate` | String | Date and time from when the catalog isn’t available to the end users. | Small, 67.0 | 67.0 |
| `effectiveStartDate` | String | Date and time from when the catalog is available to the end users. | Small, 67.0 | 67.0 |
| `id` | String | ID of the catalog. | Small, 67.0 | 67.0 |
| `name` | String | Name of the catalog. | Small, 67.0 | 67.0 |
| `numberOfCategories` | Integer | Number of categories in the catalog. | Small, 67.0 | 67.0 |
| `status` | String | Status of the catalog. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_category_output.htm ===
---
page_id: connect_responses_product_discovery_category_output.htm
title: Category Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_category_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Category Details

Output representation of the details of a category.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "categories": [
    {
      "catalogId": "0ZSSG000001875O4AQ",
      "childCategories": [],
      "customFields": {},
      "eligiblePromotions": [],
      "id": "0ZGSG000001DJtv4AG",
      "name": "Accessories",
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalogId` | String | ID of the catalog the requested category belong to. | Small, 67.0 | 67.0 |
| `customFields` | Map<String, Object> | Details of the custom fields associated with a catalog. | Small, 67.0 | 67.0 |
| `description` | String | Description of the category. | Small, 67.0 | 67.0 |
| `eligiblePromotions` | [Promotion Output](./connect_responses_promotion_output.htm.md)[] | List of eligible promotions for the product. | Small, 67.0 | 67.0 |
| `hasSubCategories` | Boolean | Indicates whether the subcategories are available (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `id` | String | ID of the category. | Small, 67.0 | 67.0 |
| `isNavigational` | Boolean | Indicates whether the category node is navigational (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `name` | String | Name of the category. | Small, 67.0 | 67.0 |
| `parentCategoryId` | String | ID of the parent category. | Small, 67.0 | 67.0 |
| `qualificationContext` | [Qualification Context Output](./connect_responses_qualification_context_output.htm.md)[] | Context details of a user, which are used for qualification rules. | Small, 67.0 | 67.0 |
| `sortOrder` | Integer | Display order of the product category relative to the siblings with the same parent category. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_product_classification_output.htm ===
---
page_id: connect_responses_product_discovery_product_classification_output.htm
title: Product Classification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_product_classification_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Classification

Output representation of the details of a product classification.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "productClassification": {
    "id": "11BSG00000UNijx2AD"
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code of the product classification. | Small, 67.0 | 67.0 |
| `id` | String | ID of the product classification. | Small, 67.0 | 67.0 |
| `name` | String | Name of the product classification. | Small, 67.0 | 67.0 |
| `status` | String | Status of the product classification. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_product_selling_model_option_output.htm ===
---
page_id: connect_responses_product_discovery_product_selling_model_option_output.htm
title: Product Selling Model Option
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_product_selling_model_option_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Selling Model Option

Output representation of the product selling model option component.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "productSellingModelOptions": [
    {
      "id": "0iOSG000000J64x2AC",
      "isDefault": true,
      "productId": "01tSG00000BiywkYAB",
      "productSellingModel": {
        "doesAutoRenewByDefault": false,
        "id": "0jPSG000000Avcv2AC",
        "name": "One Time",
        "sellingModelType": "OneTime",
        "status": "Active"
      },
      "productSellingModelId": "0jPSG000000Avcv2AC"
    }
  ]
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the product selling model option. | Small, 67.0 | 67.0 |
| `isDefault` | Boolean | Indicates whether this product selling model option is default (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `productId` | String | ID of the product. | Small, 67.0 | 67.0 |
| `productSellingModel` | [Product Selling Model](./connect_responses_product_discovery_product_selling_model_output.htm.md)[] | Details of the product selling model. | Small, 67.0 | 67.0 |
| `productSellingModelId` | String | ID of the product selling model. | Small, 67.0 | 67.0 |
| `prorationPolicy` | [Proration Policy](./connect_responses_proration_policy_output.htm.md)[] | Details of the proration policy. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_product_selling_model_output.htm ===
---
page_id: connect_responses_product_discovery_product_selling_model_output.htm
title: Product Selling Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_product_selling_model_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Selling Model

Product Selling Model Component output representation

    
      
        
          

**JSON example**

          
: 
            

```
{
  "productSellingModel": {
    "doesAutoRenewByDefault": false,
    "id": "0jPSG000000Avcv2AC",
    "name": "One Time",
    "sellingModelType": "OneTime",
    "status": "Active"
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `doesAutoRenewByDefault` | Boolean | Indicates whether the product is automatically renewed by default (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `id` | String | ID of the product selling model. | Small, 67.0 | 67.0 |
| `name` | String | Name of the product selling model. | Small, 67.0 | 67.0 |
| `pricingTerm` | Integer | Pricing term of the product selling model. | Small, 67.0 | 67.0 |
| `pricingTermUnit` | String | Pricing term unit of the product selling model. | Small, 67.0 | 67.0 |
| `sellingModelType` | String | Selling model type associated with the product selling model. | Small, 67.0 | 67.0 |
| `status` | String | Status of the product selling model. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_discovery_product_specification_type_output.htm ===
---
page_id: connect_responses_product_discovery_product_specification_type_output.htm
title: Product Specification Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_discovery_product_specification_type_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Specification Type

Output representation of the details of the product specification type.

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | Name of the product specification type. | Small, 67.0 | 67.0 |
| `productSpecificationRecordType` | [Product Specification Record Type](./connect_responses_product_specification_record_type_output.htm.md)[] | Details of the product specification record type. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_output.htm ===
---
page_id: connect_responses_product_output.htm
title: Product
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product

Output representation of the product definition.

      
        
          

**JSON example**

          
: This example shows a sample of the Product List (POST) API response.

          
: 
            

```
{
  "products": [
      {
      "additionalFields": {
        "code__c": "SWX445"
      },
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
              "displayType": "Text",
              "MinimumCharacterCount": "1",
              "MaximumCharacterCount": "20",
              "defaultValue": "AD Text DV",
              "description": "AD Text Desc",
              "helpText": "AD Text DHT",
              "id": "0tjT1000000002bIAA",
              "isHidden": false,
              "isPriceImpacting": true,
              "isReadOnly": true,
              "isRequired": true,
              "label": "AD Text Label",
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
      ],
      "attributes": [
        {
          "additionalFields": {
            "scope": "SWX445"
          },
          "attributeNameOverride": "AD Picklist",
          "code": "AD001",
          "dataType": "Picklist",
          "defaultValue": "Red",
          "description": "AD Picklist Description",
          "helpText": "AD Picklist DHT",
          "id": "0tjT1000000002WIAQ",
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": true,
          "label": "AD Picklist Label",
          "name": "AD Picklist",
          "picklist": {
            "dataType": "Text",
            "description": "APV Description",
            "id": "0v5T10000000001IAA",
            "name": "Color",
            "values": [
              {
                "abbreviation": "Blue Abb",
                "code": "APV03",
                "displayValue": "Blue DV",
                "id": "0v6T10000000006IAA",
                "name": "Blue",
                "sequence": "3",
                "value": "Blue b",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abb",
                "code": "APV04",
                "displayValue": "Red",
                "id": "0v6T10000000001IAA",
                "name": "Red",
                "sequence": "4",
                "value": "Red",
                "status": "Active"
              },
              {
                "abbreviation": "One Abb",
                "code": "APV02",
                "displayValue": "One DV",
                "id": "0v6T1000000000uIAA",
                "name": "One",
                "sequence": "2",
                "value": "One 1",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abbreviation",
                "code": "APV01",
                "displayValue": "Red Display Value",
                "id": "0v6T1000000001OIAQ",
                "name": "Red",
                "sequence": "1",
                "value": "red12",
                "status": "Active"
              }
            ]
          },
          "sequence": 1,
          "status": "Active",
          "valueDescription": "AD Picklist VD"
        }
      ],
      "categories": [],
      "childProducts": [
        {
          "attributeCategory": [],
          "attributes": [],
          "categories": [],
          "childProducts": [],
          "configureDuringSale": "NotAllowed",
          "id": "01tZ7000000AJkaIAG",
          "isActive": false,
          "isAssetizable": true,
          "isSoldOnlyWithOtherProds": false,
          "name": "Earphones",
          "nodeType": "bundleProduct",
          "productComponentGroups": [],
          "productRelatedComponent": {
            "childProductId": "01tZ7000000AJkaIAG",
            "doesBundlePriceIncludeChild": true,
            "id": "0dSZ700000000cdMAA",
            "isComponentRequired": false,
            "isDefaultComponent": true,
            "isExcluded": false,
            "isQuantityEditable": false,
            "parentProductId": "01tZ7000000AJXOIA4",
            "productRelationshipTypeId": "0yoZ700000000kPIAQ",
            "quantity": 1,
            "quantityScaleMethod": "Proportional"
          },
          "productSellingModelOptions": []
        }
      ],
      "description": "Keep your organization connected with seamless collaboration across distributed teams. No matter where employees are located, organizations are seeking stronger employee engagement and customer experiences to enable more productivity and greater business agility. More effective collaboration helps organizations work smarter.",
      "displayUrl": "https://dispatch.m.io/wp-content/uploads/2023/01/History-of-Webex.png",
      "id": "01t1Q000008CD2eQAG",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "SmartBytes Collaboration Suite",
      "nodeType": "bundleProduct",
      "productClassification": {
        "id": "11B1Q0000008OMGUA2"
      },
      "productCode": "P0143",
      "productComponentGroups": [
        {
          "components": [
            {
              "attributeCategory": [],
              "attributes": [],
              "categories": [],
              "childProducts": [],
              "id": "01tZ7000000AJXTIA4",
              "isActive": false,
              "isAssetizable": true,
              "isSoldOnlyWithOtherProds": false,
              "name": "Charger",
              "nodeType": "bundleProduct",
              "productComponentGroups": [],
              "productRelatedComponent": {
                "childProductId": "01tZ7000000AJXTIA4",
                "doesBundlePriceIncludeChild": true,
                "id": "0dSZ700000000YLMAY",
                "isComponentRequired": false,
                "isDefaultComponent": true,
                "isExcluded": false,
                "isQuantityEditable": false,
                "parentProductId": "01tZ7000000AJXOIA4",
                "productRelationshipTypeId": "0yoZ700000000kPIAQ",
                "quantity": 1,
                "quantityScaleMethod": "Proportional"
              },
              "productSellingModelOptions": []
            }
          ],
          "id": "0y7Z700000000TtIAI",
          "isExcluded": false,
          "name": "Box",
          "parentProductId": "01tZ7000000AJXOIA4"
        }
      ],
      "productSellingModelOptions": [
        {
          "id": "0iO1Q0000008OkeUAE",
          "productId": "01t1Q000008CD2eQAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVFUA0",
            "isDefault": true,
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "None"
      }
    }
],
  "status": {
    "code": "200",
    "correlationId": "fd158d80-d73c-4a1f-a009-9225db804d70",
    "errors": [],
    "message": "Successfully fetched product records."
  }
}
```

          

          
: This example shows a sample of the Bulk Product Details (POST) API response.

          
: 
            

```
{
  "products": [
      {
      "additionalFields": {
        "code__c": "SWX445"
      },
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
              "displayType": "Text",
              "MinimumCharacterCount": "1",
              "MaximumCharacterCount": "20",
              "defaultValue": "AD Text DV",
              "description": "AD Text Desc",
              "helpText": "AD Text DHT",
              "id": "0tjT1000000002bIAA",
              "isHidden": false,
              "isPriceImpacting": true,
              "isReadOnly": true,
              "isRequired": true,
              "label": "AD Text Label",
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
      ],
      "attributes": [
        {
          "additionalFields": {
            "scope": "SWX445"
          },
          "attributeNameOverride": "AD Picklist",
          "code": "AD001",
          "dataType": "Picklist",
          "defaultValue": "Red",
          "description": "AD Picklist Description",
          "helpText": "AD Picklist DHT",
          "id": "0tjT1000000002WIAQ",
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": true,
          "label": "AD Picklist Label",
          "name": "AD Picklist",
          "picklist": {
            "dataType": "Text",
            "description": "APV Description",
            "id": "0v5T10000000001IAA",
            "name": "Color",
            "values": [
              {
                "abbreviation": "Blue Abb",
                "code": "APV03",
                "displayValue": "Blue DV",
                "id": "0v6T10000000006IAA",
                "name": "Blue",
                "sequence": "3",
                "value": "Blue b",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abb",
                "code": "APV04",
                "displayValue": "Red",
                "id": "0v6T10000000001IAA",
                "name": "Red",
                "sequence": "4",
                "value": "Red",
                "status": "Active"
              },
              {
                "abbreviation": "One Abb",
                "code": "APV02",
                "displayValue": "One DV",
                "id": "0v6T1000000000uIAA",
                "name": "One",
                "sequence": "2",
                "value": "One 1",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abbreviation",
                "code": "APV01",
                "displayValue": "Red Display Value",
                "id": "0v6T1000000001OIAQ",
                "name": "Red",
                "sequence": "1",
                "value": "red12",
                "status": "Active"
              }
            ]
          },
          "sequence": 1,
          "status": "Active",
          "valueDescription": "AD Picklist VD"
        }
      ],
      "categories": [],
      "childProducts": [
        {
          "attributeCategory": [],
          "attributes": [],
          "categories": [],
          "childProducts": [],
          "configureDuringSale": "NotAllowed",
          "id": "01tZ7000000AJkaIAG",
          "isActive": false,
          "isAssetizable": true,
          "isSoldOnlyWithOtherProds": false,
          "name": "Earphones",
          "nodeType": "bundleProduct",
          "productComponentGroups": [],
          "productRelatedComponent": {
            "childProductId": "01tZ7000000AJkaIAG",
            "doesBundlePriceIncludeChild": true,
            "id": "0dSZ700000000cdMAA",
            "isComponentRequired": false,
            "isDefaultComponent": true,
            "isExcluded": false,
            "isQuantityEditable": false,
            "parentProductId": "01tZ7000000AJXOIA4",
            "productRelationshipTypeId": "0yoZ700000000kPIAQ",
            "quantity": 1,
            "quantityScaleMethod": "Proportional"
          },
          "productSellingModelOptions": []
        }
      ],
      "description": "Keep your organization connected with seamless collaboration across distributed teams. No matter where employees are located, organizations are seeking stronger employee engagement and customer experiences to enable more productivity and greater business agility. More effective collaboration helps organizations work smarter.",
      "displayUrl": "https://dispatch.m.io/wp-content/uploads/2023/01/History-of-Webex.png",
      "id": "01t1Q000008CD2eQAG",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "SmartBytes Collaboration Suite",
      "nodeType": "bundleProduct",
      "productClassification": {
        "id": "11B1Q0000008OMGUA2",
        "name" : "class",
        "code" : "code",
        "status" : "Active"
      },
      "productCode": "P0143",
      "productComponentGroups": [
        {
          "components": [
            {
              "attributeCategory": [],
              "attributes": [],
              "categories": [],
              "childProducts": [],
              "id": "01tZ7000000AJXTIA4",
              "isActive": false,
              "isAssetizable": true,
              "isSoldOnlyWithOtherProds": false,
              "name": "Charger",
              "nodeType": "bundleProduct",
              "productComponentGroups": [],
              "productRelatedComponent": {
                "childProductId": "01tZ7000000AJXTIA4",
                "doesBundlePriceIncludeChild": true,
                "id": "0dSZ700000000YLMAY",
                "isComponentRequired": false,
                "isDefaultComponent": true,
                "isExcluded": false,
                "isQuantityEditable": false,
                "parentProductId": "01tZ7000000AJXOIA4",
                "productRelationshipTypeId": "0yoZ700000000kPIAQ",
                "quantity": 1,
                "quantityScaleMethod": "Proportional"
              },
              "productSellingModelOptions": []
            }
          ],
          "id": "0y7Z700000000TtIAI",
          "isExcluded": false,
          "name": "Box",
          "parentProductId": "01tZ7000000AJXOIA4"
        }
      ],
      "productSellingModelOptions": [
        {
          "id": "0iO1Q0000008OkeUAE",
          "productId": "01t1Q000008CD2eQAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVFUA0",
            "isDefault": true,
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "None"
      }
    }
],
  "status": {
    "code": "200",
    "correlationId": "fd158d80-d73c-4a1f-a009-9225db804d70",
    "errors": [],
    "message": "Successfully fetched product records."
  }
}
```

          

          
: This example shows a sample of the Product By ID (GET) API response.

          
: 
            

```
{
  "products": [
    {
      "attributeCategory": [
        {
          "attributes": [
            {
              "attributeNameOverride": "AD Text",
              "code": "AD02",
              "dataType": "Text",
              "displayType": "Text",
              "MinimumCharacterCount": "1",
              "MaximumCharacterCount": "20",
              "defaultValue": "AD Text DV",
              "description": "AD Text Desc",
              "helpText": "AD Text DHT",
              "id": "0tjT1000000002bIAA",
              "isHidden": false,
              "isPriceImpacting": true,
              "isReadOnly": true,
              "isRequired": true,
              "label": "AD Text Label",
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
      ],
      "attributes": [
        {
          "attributeNameOverride": "AD Picklist",
          "code": "AD001",
          "dataType": "Picklist",
          "defaultValue": "Red",
          "description": "AD Picklist Description",
          "helpText": "AD Picklist DHT",
          "id": "0tjT1000000002WIAQ",
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": true,
          "label": "AD Picklist Label",
          "name": "AD Picklist",
          "picklist": {
            "dataType": "Text",
            "description": "APV Description",
            "id": "0v5T10000000001IAA",
            "name": "Color",
            "values": [
              {
                "abbreviation": "Blue Abb",
                "code": "APV03",
                "displayValue": "Blue DV",
                "id": "0v6T10000000006IAA",
                "name": "Blue",
                "sequence": "3",
                "value": "Blue b",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abb",
                "code": "APV04",
                "displayValue": "Red",
                "id": "0v6T10000000001IAA",
                "name": "Red",
                "sequence": "4",
                "value": "Red",
                "status": "Active"
              },
              {
                "abbreviation": "One Abb",
                "code": "APV02",
                "displayValue": "One DV",
                "id": "0v6T1000000000uIAA",
                "name": "One",
                "sequence": "2",
                "value": "One 1",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abbreviation",
                "code": "APV01",
                "displayValue": "Red Display Value",
                "id": "0v6T1000000001OIAQ",
                "name": "Red",
                "sequence": "1",
                "value": "red12",
                "status": "Active"
              }
            ]
          },
          "sequence": 1,
          "status": "Active",
          "valueDescription": "AD Picklist VD"
        }
      ],
      "availabilityDate": "2023-07-12T19:00:00.000Z",
      "categories": [],
      "childProducts": [],
      "configureDuringSale": "Allowed",
      "description": "Bundle Product Description",
      "discontinuedDate": "2023-07-27T19:00:00.000Z",
      "displayUrl": "www.google.com",
      "endOfLifeDate": "2023-07-31T19:00:00.000Z",
      "id": "01tT1000000F0afIAC",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": true,
      "name": "Bundle Product",
      "nodeType": "bundleProduct",
      "productClassification": {
        "id": "11BT10000004C9SMAU",
        "name" : "class",
        "code" : "code",
        "status" : "Active"
      },
      "productCode": "P001",
      "productComponentGroups": [
        {
          "code": "PCG002",
          "components": [
            {
              "attributeCategory": [],
              "attributes": [],
              "categories": [],
              "childProducts": [],
              "nodeType": "productClass",
              "productClassification": {
                "id": "11BT10000004C9SMAU",
                "name" : "class",
                "code" : "code",
                "status" : "Active"
              },
              "productComponentGroups": [],
              "productRelatedComponent": {
                "childSellingModelId": "0jPT10000004CAfMAM",
                "doesBundlePriceIncludeChild": true,
                "id": "0dST100000000rlMAA",
                "isComponentRequired": false,
                "isDefaultComponent": false,
                "isQuantityEditable": true,
                "maxQuantity": 5,
                "minQuantity": 1,
                "parentProductId": "01tT1000000F0afIAC",
                "productClassificationId": "11BT10000004C9SMAU",
                "productRelationshipTypeId": "0yoT10000004CBEIA2",
                "quantity": 1,
                "quantityScaleMethod": "Proportional",
                "sequence": 2,
                "isExcluded": false
              },
              "productSellingModelOptions": []
            }
          ],
          "description": "PCG002 desc",
          "id": "0y7T10000004C9IIAU",
          "maxBundleComponents": 5,
          "minBundleComponents": 1,
          "name": "PCG002",
          "parentProductId": "01tT1000000F0afIAC",
          "sequence": 2,
          "isExcluded": false
        },
        {
          "code": "PCG001",
          "components": [
            {
              "attributeCategory": [],
              "attributes": [
                {
                  "attributeNameOverride": "AD Picklist",
                  "code": "AD001",
                  "dataType": "Picklist",
                  "defaultValue": "Red",
                  "description": "AD Picklist Description",
                  "helpText": "AD Picklist DHT",
                  "id": "0tjT1000000002WIAQ",
                  "isHidden": false,
                  "isPriceImpacting": false,
                  "isReadOnly": false,
                  "isRequired": true,
                  "label": "AD Picklist Label",
                  "name": "AD Picklist",
                  "picklist": {
                    "dataType": "Text",
                    "description": "APV Description",
                    "id": "0v5T10000000001IAA",
                    "name": "Color",
                    "values": [
                      {
                        "abbreviation": "Blue Abb",
                        "code": "APV03",
                        "displayValue": "Blue DV",
                        "id": "0v6T10000000006IAA",
                        "name": "Blue",
                        "sequence": "3",
                        "value": "Blue b",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "Red Abb",
                        "code": "APV04",
                        "displayValue": "Red",
                        "id": "0v6T10000000001IAA",
                        "name": "Red",
                        "sequence": "4",
                        "value": "Red",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "One Abb",
                        "code": "APV02",
                        "displayValue": "One DV",
                        "id": "0v6T1000000000uIAA",
                        "name": "One",
                        "sequence": "2",
                        "value": "One 1",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "Red Abbreviation",
                        "code": "APV01",
                        "displayValue": "Red Display Value",
                        "id": "0v6T1000000001OIAQ",
                        "name": "Red",
                        "sequence": "1",
                        "value": "red12",
                        "status": "Active"
                      }
                    ]
                  },
                  "sequence": 1,
                  "status": "Active",
                  "valueDescription": "AD Picklist VD"
                },
                {
                  "attributeNameOverride": "AD Text",
                  "code": "AD02",
                  "dataType": "Text",
                  "displayType": "Text",
                  "MinimumCharacterCount": "1",
                  "MaximumCharacterCount": "20",
                  "defaultValue": "AD Text DV",
                  "description": "AD Text Desc",
                  "helpText": "AD Text DHT",
                  "id": "0tjT1000000002bIAA",
                  "isHidden": false,
                  "isPriceImpacting": false,
                  "isReadOnly": false,
                  "isRequired": true,
                  "label": "AD Text Label",
                  "name": "AD Text",
                  "status": "Active",
                  "valueDescription": "AD Text VD"
                }
              ],
              "availabilityDate": "2023-07-17T19:00:00.000Z",
              "categories": [],
              "childProducts": [],
              "configureDuringSale": "Allowed",
              "description": "P003 desc",
              "discontinuedDate": "2023-07-19T19:00:00.000Z",
              "displayUrl": "www.google.com",
              "endOfLifeDate": "2023-07-28T19:00:00.000Z",
              "id": "01tT1000000F0YyIAK",
              "isActive": false,
              "isAssetizable": true,
              "isSoldOnlyWithOtherProds": false,
              "name": "Child1 - Bundle with PCG",
              "nodeType": "bundleProduct",
              "productClassification": {
                "id": "11BT10000004C9SMAU",
                "name" : "class",
                "code" : "code",
                "status" : "Active"
              },
              "productCode": "P003",
              "productComponentGroups": [
                {
                  "code": "PCG2",
                  "components": [
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "categories": [],
                      "childProducts": [],
                      "id": "01tT1000000F0Z8IAK",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "Super Child2 - Bundle with PCG",
                      "nodeType": "bundleProduct",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0Z8IAK",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rWMAQ",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "sequence": 2,
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    },
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "availabilityDate": "2023-07-15T19:00:00.000Z",
                      "categories": [],
                      "childProducts": [],
                      "configureDuringSale": "Allowed",
                      "discontinuedDate": "2023-07-16T19:00:00.000Z",
                      "displayUrl": "Test",
                      "endOfLifeDate": "2023-07-17T19:00:00.000Z",
                      "id": "01tT1000000F0YzIAK",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "SuperChild1 - Bundle with PCG",
                      "nodeType": "bundleProduct",
                      "productCode": "Test",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0YzIAK",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rXMAQ",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "sequence": 1,
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    },
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "categories": [],
                      "childProducts": [],
                      "configureDuringSale": "Allowed",
                      "id": "01tT1000000F0apIAC",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "Bundle2",
                      "nodeType": "bundleProduct",
                      "productCode": "PC003",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0apIAC",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rqMAA",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    }
                  ],
                  "description": "Group for components at level 2",
                  "id": "0y7T10000004C98IAE",
                  "maxBundleComponents": 5,
                  "minBundleComponents": 1,
                  "name": "PCG2",
                  "parentProductId": "01tT1000000F0YyIAK",
                  "isExcluded": false
                }
              ],
              "productRelatedComponent": {
                "childProductId": "01tT1000000F0YyIAK",
                "childSellingModelId": "0jPT10000004CAfMAM",
                "doesBundlePriceIncludeChild": true,
                "id": "0dST100000000rgMAA",
                "isComponentRequired": false,
                "isDefaultComponent": false,
                "isQuantityEditable": true,
                "maxQuantity": 3,
                "minQuantity": 1,
                "parentProductId": "01tT1000000F0afIAC",
                "parentSellingModelId": "0jPT10000004CAfMAM",
                "productRelationshipTypeId": "0yoT1000000002WIAQ",
                "quantity": 1,
                "quantityScaleMethod": "Proportional",
                "sequence": 1,
                "isExcluded": false
              },
              "productSellingModelOptions": [
                {
                  "id": "0iOT10000004CMrMAM",
                  "productId": "01tT1000000F0YyIAK",
                  "isDefault": false,
                  "productSellingModel": {
                    "id": "0jPT10000004CAfMAM",
                    "name": "OneTimePSM",
                    "sellingModelType": "OneTime",
                    "status": "Active"
                  }
                }
              ],
              "productSpecificationType": {
                "name": "NonCommercialSpecType",
                "productSpecificationRecordType": null
              }
            }
          ],
          "description": "PCG001 Description",
          "id": "0y7T10000004C9DIAU",
          "maxBundleComponents": 5,
          "minBundleComponents": 1,
          "name": "PCG001",
          "parentProductId": "01tT1000000F0afIAC",
          "sequence": 1,
          "isExcluded": false
        }
      ],
      "productSellingModelOptions": [
        {
          "id": "0iOT10000004CMmMAM",
          "productId": "01tT1000000F0afIAC",
          "productSellingModel": {
            "id": "0jPT10000004CAfMAM",
            "name": "OneTimePSM",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "NonCommercialSpecType",
        "productSpecificationRecordType": null
      }
    },
    {
      "attributeCategory": [
        {
          "attributes": [
            {
              "attributeNameOverride": "AD Text",
              "code": "AD02",
              "dataType": "Text",
              "displayType": "Text",
              "MinimumCharacterCount": "1",
              "MaximumCharacterCount": "20",
              "defaultValue": "AD Text DV",
              "description": "AD Text Desc",
              "helpText": "AD Text DHT",
              "id": "0tjT1000000002bIAA",
              "isHidden": false,
              "isPriceImpacting": true,
              "isReadOnly": true,
              "isRequired": true,
              "label": "AD Text Label",
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
      ],
      "attributes": [
        {
          "attributeNameOverride": "AD Picklist",
          "code": "AD001",
          "dataType": "Picklist",
          "defaultValue": "Red",
          "description": "AD Picklist Description",
          "helpText": "AD Picklist DHT",
          "id": "0tjT1000000002WIAQ",
          "isHidden": false,
          "isPriceImpacting": false,
          "isReadOnly": false,
          "isRequired": true,
          "label": "AD Picklist Label",
          "name": "AD Picklist",
          "picklist": {
            "dataType": "Text",
            "description": "APV Description",
            "id": "0v5T10000000001IAA",
            "name": "Color",
            "values": [
              {
                "abbreviation": "Blue Abb",
                "code": "APV03",
                "displayValue": "Blue DV",
                "id": "0v6T10000000006IAA",
                "name": "Blue",
                "sequence": "3",
                "value": "Blue b",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abb",
                "code": "APV04",
                "displayValue": "Red",
                "id": "0v6T10000000001IAA",
                "name": "Red",
                "sequence": "4",
                "value": "Red",
                "status": "Active"
              },
              {
                "abbreviation": "One Abb",
                "code": "APV02",
                "displayValue": "One DV",
                "id": "0v6T1000000000uIAA",
                "name": "One",
                "sequence": "2",
                "value": "One 1",
                "status": "Active"
              },
              {
                "abbreviation": "Red Abbreviation",
                "code": "APV01",
                "displayValue": "Red Display Value",
                "id": "0v6T1000000001OIAQ",
                "name": "Red",
                "sequence": "1",
                "value": "red12",
                "status": "Active"
              }
            ]
          },
          "sequence": 1,
          "status": "Active",
          "valueDescription": "AD Picklist VD"
        }
      ],
      "availabilityDate": "2023-07-12T19:00:00.000Z",
      "categories": [],
      "childProducts": [],
      "configureDuringSale": "Allowed",
      "description": "Bundle Product Description",
      "discontinuedDate": "2023-07-27T19:00:00.000Z",
      "displayUrl": "www.google.com",
      "endOfLifeDate": "2023-07-31T19:00:00.000Z",
      "id": "01tT1000000F0afIAC",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": true,
      "name": "Bundle Product",
      "nodeType": "bundleProduct",
      "productClassification": {
        "id": "11BT10000004C9SMAU",
        "name" : "class",
        "code" : "code",
        "status" : "Active"
      },
      "productCode": "P001",
      "productComponentGroups": [
        {
          "code": "PCG002",
          "components": [
            {
              "attributeCategory": [],
              "attributes": [],
              "categories": [],
              "childProducts": [],
              "nodeType": "productClass",
              "productClassification": {
                "id": "11BT10000004C9SMAU",
                "name" : "class",
                "code" : "code",
                "status" : "Active"
              },
              "productComponentGroups": [],
              "productRelatedComponent": {
                "childSellingModelId": "0jPT10000004CAfMAM",
                "doesBundlePriceIncludeChild": true,
                "id": "0dST100000000rlMAA",
                "isComponentRequired": false,
                "isDefaultComponent": false,
                "isQuantityEditable": true,
                "maxQuantity": 5,
                "minQuantity": 1,
                "parentProductId": "01tT1000000F0afIAC",
                "productClassificationId": "11BT10000004C9SMAU",
                "productRelationshipTypeId": "0yoT10000004CBEIA2",
                "quantity": 1,
                "quantityScaleMethod": "Proportional",
                "sequence": 2,
                "isExcluded": false
              },
              "productSellingModelOptions": []
            }
          ],
          "description": "PCG002 desc",
          "id": "0y7T10000004C9IIAU",
          "maxBundleComponents": 5,
          "minBundleComponents": 1,
          "name": "PCG002",
          "parentProductId": "01tT1000000F0afIAC",
          "sequence": 2,
          "isExcluded": false
        },
        {
          "code": "PCG001",
          "components": [
            {
              "attributeCategory": [],
              "attributes": [
                {
                  "attributeNameOverride": "AD Picklist",
                  "code": "AD001",
                  "dataType": "Picklist",
                  "defaultValue": "Red",
                  "description": "AD Picklist Description",
                  "helpText": "AD Picklist DHT",
                  "id": "0tjT1000000002WIAQ",
                  "isHidden": false,
                  "isPriceImpacting": false,
                  "isReadOnly": false,
                  "isRequired": true,
                  "label": "AD Picklist Label",
                  "name": "AD Picklist",
                  "picklist": {
                    "dataType": "Text",
                    "description": "APV Description",
                    "id": "0v5T10000000001IAA",
                    "name": "Color",
                    "values": [
                      {
                        "abbreviation": "Blue Abb",
                        "code": "APV03",
                        "displayValue": "Blue DV",
                        "id": "0v6T10000000006IAA",
                        "name": "Blue",
                        "sequence": "3",
                        "value": "Blue b",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "Red Abb",
                        "code": "APV04",
                        "displayValue": "Red",
                        "id": "0v6T10000000001IAA",
                        "name": "Red",
                        "sequence": "4",
                        "value": "Red",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "One Abb",
                        "code": "APV02",
                        "displayValue": "One DV",
                        "id": "0v6T1000000000uIAA",
                        "name": "One",
                        "sequence": "2",
                        "value": "One 1",
                        "status": "Active"
                      },
                      {
                        "abbreviation": "Red Abbreviation",
                        "code": "APV01",
                        "displayValue": "Red Display Value",
                        "id": "0v6T1000000001OIAQ",
                        "name": "Red",
                        "sequence": "1",
                        "value": "red12",
                        "status": "Active"
                      }
                    ]
                  },
                  "sequence": 1,
                  "status": "Active",
                  "valueDescription": "AD Picklist VD"
                },
                {
                  "attributeNameOverride": "AD Text",
                  "code": "AD02",
                  "dataType": "Text",
                  "displayType": "Text",
                  "MinimumCharacterCount": "1",
                  "MaximumCharacterCount": "20",
                  "defaultValue": "AD Text DV",
                  "description": "AD Text Desc",
                  "helpText": "AD Text DHT",
                  "id": "0tjT1000000002bIAA",
                  "isHidden": false,
                  "isPriceImpacting": false,
                  "isReadOnly": false,
                  "isRequired": true,
                  "label": "AD Text Label",
                  "name": "AD Text",
                  "status": "Active",
                  "valueDescription": "AD Text VD"
                }
              ],
              "availabilityDate": "2023-07-17T19:00:00.000Z",
              "categories": [],
              "childProducts": [],
              "configureDuringSale": "Allowed",
              "description": "P003 desc",
              "discontinuedDate": "2023-07-19T19:00:00.000Z",
              "displayUrl": "www.google.com",
              "endOfLifeDate": "2023-07-28T19:00:00.000Z",
              "id": "01tT1000000F0YyIAK",
              "isActive": false,
              "isAssetizable": true,
              "isSoldOnlyWithOtherProds": false,
              "name": "Child1 - Bundle with PCG",
              "nodeType": "bundleProduct",
              "productClassification": {
                "id": "11BT10000004C9SMAU",
                "name" : "class",
                "code" : "code",
                "status" : "Active"
              },
              "productCode": "P003",
              "productComponentGroups": [
                {
                  "code": "PCG2",
                  "components": [
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "categories": [],
                      "childProducts": [],
                      "id": "01tT1000000F0Z8IAK",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "Super Child2 - Bundle with PCG",
                      "nodeType": "bundleProduct",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0Z8IAK",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rWMAQ",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "sequence": 2,
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    },
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "availabilityDate": "2023-07-15T19:00:00.000Z",
                      "categories": [],
                      "childProducts": [],
                      "configureDuringSale": "Allowed",
                      "discontinuedDate": "2023-07-16T19:00:00.000Z",
                      "displayUrl": "Test",
                      "endOfLifeDate": "2023-07-17T19:00:00.000Z",
                      "id": "01tT1000000F0YzIAK",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "SuperChild1 - Bundle with PCG",
                      "nodeType": "bundleProduct",
                      "productCode": "Test",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0YzIAK",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rXMAQ",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "sequence": 1,
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    },
                    {
                      "attributeCategory": [],
                      "attributes": [],
                      "categories": [],
                      "childProducts": [],
                      "configureDuringSale": "Allowed",
                      "id": "01tT1000000F0apIAC",
                      "isActive": false,
                      "isAssetizable": true,
                      "isSoldOnlyWithOtherProds": false,
                      "name": "Bundle2",
                      "nodeType": "bundleProduct",
                      "productCode": "PC003",
                      "productComponentGroups": [],
                      "productRelatedComponent": {
                        "childProductId": "01tT1000000F0apIAC",
                        "doesBundlePriceIncludeChild": true,
                        "id": "0dST100000000rqMAA",
                        "isComponentRequired": false,
                        "isDefaultComponent": false,
                        "isQuantityEditable": false,
                        "parentProductId": "01tT1000000F0YyIAK",
                        "productRelationshipTypeId": "0yoT1000000002WIAQ",
                        "quantity": 1,
                        "quantityScaleMethod": "Proportional",
                        "isExcluded": false
                      },
                      "productSellingModelOptions": [],
                      "productSpecificationType": {
                        "name": "NonCommercialSpecType",
                        "productSpecificationRecordType": null
                      }
                    }
                  ],
                  "description": "Group for components at level 2",
                  "id": "0y7T10000004C98IAE",
                  "maxBundleComponents": 5,
                  "minBundleComponents": 1,
                  "name": "PCG2",
                  "parentProductId": "01tT1000000F0YyIAK",
                  "isExcluded": false
                }
              ],
              "productRelatedComponent": {
                "childProductId": "01tT1000000F0YyIAK",
                "childSellingModelId": "0jPT10000004CAfMAM",
                "doesBundlePriceIncludeChild": true,
                "id": "0dST100000000rgMAA",
                "isComponentRequired": false,
                "isDefaultComponent": false,
                "isQuantityEditable": true,
                "maxQuantity": 3,
                "minQuantity": 1,
                "parentProductId": "01tT1000000F0afIAC",
                "parentSellingModelId": "0jPT10000004CAfMAM",
                "productRelationshipTypeId": "0yoT1000000002WIAQ",
                "quantity": 1,
                "quantityScaleMethod": "Proportional",
                "sequence": 1,
                "isExcluded": false
              },
              "productSellingModelOptions": [
                {
                  "id": "0iOT10000004CMrMAM",
                  "productId": "01tT1000000F0YyIAK",
                  "isDefault": false,
                  "productSellingModel": {
                    "id": "0jPT10000004CAfMAM",
                    "name": "OneTimePSM",
                    "sellingModelType": "OneTime",
                    "status": "Active"
                  }
                }
              ],
              "productSpecificationType": {
                "name": "NonCommercialSpecType",
                "productSpecificationRecordType": null
              }
            }
          ],
          "description": "PCG001 Description",
          "id": "0y7T10000004C9DIAU",
          "maxBundleComponents": 5,
          "minBundleComponents": 1,
          "name": "PCG001",
          "parentProductId": "01tT1000000F0afIAC",
          "sequence": 1,
          "isExcluded": false
        }
      ],
      "productSellingModelOptions": [
        {
          "id": "0iOT10000004CMmMAM",
          "productId": "01tT1000000F0afIAC",
          "productSellingModel": {
            "id": "0jPT10000004CAfMAM",
            "name": "OneTimePSM",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "NonCommercialSpecType",
        "productSpecificationRecordType": null
      }
    }
  ],
  "status": {
    "code": "200",
    "correlationId": "fd158d80-d73c-4a1f-a009-9225db804d70",
    "errors": [],
    "message": "Successfully fetched Product records."
  }
}
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, [Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)> | Key-value pair of additional standard or custom fields with their values. | Small, 61.0 | 61.0 |
| `attribute​Category` | [Attribute Category](./connect_responses_attribute_category_output.htm.md)[] | List of categorized attributes related to the product. | Small, 60.0 | 60.0 |
| `attributes` | [Attribute Definition](./connect_responses_attribute_definition_output.htm.md)[] | List of uncategorized attributes related to the product. | Small, 60.0 | 60.0 |
| `availability​Date` | String | Date when the part is used in the product or is made available for sale. | Small, 60.0 | 60.0 |
| `catalogs` | [Catalog](./connect_responses_catalog_output.htm.md)[] | List of the associated catalogs returned with the Product List API (POST) response. The Product By ID API (GET) returns an empty catalog list in the response. Returns the `name` and `id` values only. | Small, 61.0 | 61.0 |
| `categories` | [Category](./connect_responses_category_output.htm.md)[] | List of the associated categories returned with the Product List API (POST) response. The Product By ID API (GET) returns an empty category list in the response. Returns the `name` and `id` values only. | Small, 60.0 | 60.0 |
| `child​Products` | [Product](#)[] | Hierarchy of the child products. | Small, 60.0 | 60.0 |
| `configure​During​Sale` | String | Determines whether to allow or prevent configuration when a bundle is sold. | Small, 60.0 | 60.0 |
| `description` | String | Description of the product. If data translation is set up and specified in the org, the translated description is available. | Small, 60.0 | 60.0 |
| `discontinued​Date` | String | Date from when the part can’t be used in the product or sold. | Small, 60.0 | 60.0 |
| `display​Url` | String | Display image URL of the product. | Small, 60.0 | 60.0 |
| `endOf​Life​Date` | String | Date after which a product isn’t supported, ordered, or maintained. | Small, 60.0 | 60.0 |
| `id` | String | ID of the product. | Small, 60.0 | 60.0 |
| `isActive` | Boolean | Indicates if the product is active (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Assetizable` | Boolean | Indicates if the product instance remains a customer asset after it's purchased (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​SoldOnly​WithOther​Prods` | Boolean | Indicates whether the product can't be sold separately (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `name` | String | Name of the product. If data translation is set up and specified in the org, the translated name is available. | Small, 60.0 | 60.0 |
| `node​Type` | String | Type of the node, such as a product or bundled product. | Small, 60.0 | 60.0 |
| `product​Classification` | [Product Classification](./connect_responses_product_classification_output.htm.md) | Details of the product classification that the product is based on. | Small, 60.0 | 60.0 |
| `product​Code` | String | Universal product code that's used to track the part that’s used in the product. | Small, 60.0 | 60.0 |
| `product​Component​Groups` | [Product Component Group](./connect_responses_product_component_group_output.htm.md)[] | Logical grouping of the component products in a bundle and the group cardinality for ordering the product components. | Small, 60.0 | 60.0 |
| `product​Related​Component` | [Product Related Component](./connect_responses_product_related_component_output.htm.md) | Details of the related components of a product. | Small, 60.0 | 60.0 |
| `product​Selling​Model​Options` | [Product Selling Model Option](./connect_responses_product_selling_model_option_output.htm.md)[] | Details of the product selling model options. | Small, 60.0 | 60.0 |
| `product​Specification​Type` | [Product Specification Type](./connect_responses_product_specification_type_output.htm.md) | Details of the product specification type. | Small, 60.0 | 60.0 |
| `quantity​Scale​Method` | String | Method to scale the quantity of the child product in relation to the quantity of the parent. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_prices_output.htm ===
---
page_id: connect_responses_product_prices_output.htm
title: Product Prices
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_prices_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Prices

Output representation of the details of the product prices.

        
          

**JSON example**

          
: 
            

```
{
  "prices": [
    {
      "currencyIsoCode": "USD",
      "isDefault": true,
      "isDerived": false,
      "isSelected": false,
      "price": 7.99,
      "priceBookEntryId": "01uSG000004wTsEYAU",
      "priceBookId": "01sSG00000DQCjhYAH",
      "pricingModel": {
        "id": "0jPSG000000Avcv2AC",
        "name": "One Time",
        "pricingModelType": "OneTime"
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `currencyIsoCode` | String | Currency ISO code of the given price. | Small, 67.0 | 67.0 |
| `effectiveFrom` | String | Date from when the given price is effective. | Small, 67.0 | 67.0 |
| `effectiveTo` | String | Date until when the given price is effective. | Small, 67.0 | 67.0 |
| `isDefault` | Boolean | Indicates whether the given price is default (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isDerived` | Boolean | Indicates whether the given price is derived (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isSelected` | Boolean | Indicates whether the given price is selected (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `price` | Double | Price of the product. | Small, 67.0 | 67.0 |
| `priceBookEntryId` | String | Price book entry ID of the given price. | Small, 67.0 | 67.0 |
| `priceBookId` | String | Price book ID of the given price. | Small, 67.0 | 67.0 |
| `pricingModel` | [Pricing Model](./connect_responses_pricing_model_output.htm.md)[] | Pricing model of the given price. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_quantity_output.htm ===
---
page_id: connect_responses_product_quantity_output.htm
title: Product Quantity
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_quantity_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Quantity

Output representation of the details of the quantity constraints and current quantity for
    a product in the product discovery context.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `maxQuantity` | Double | Maximum quantity allowed for a product. | Small, 67.0 | 67.0 |
| `minQuantity` | Double | Minimum quantity allowed for a product. | Small, 67.0 | 67.0 |
| `quantity` | Double | Default or current quantity of the product. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_recommendation_errors_output.htm ===
---
page_id: connect_responses_product_recommendation_errors_output.htm
title: Product Recommendation Errors
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_recommendation_errors_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Recommendation Errors

Output representation of the details of the errors encountered during the processing of
    the Product Recommendations API request.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code that indicates the type of error. | Small, 66.0 | 66.0 |
| `message` | String | Message stating the reason for error, if any. | Small, 66.0 | 66.0 |

=== ARTICLE: connect_responses_product_recommendation_output.htm ===
---
page_id: connect_responses_product_recommendation_output.htm
title: Product Recommendations
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_recommendation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Recommendations

Output representation of the fetched product recommendations.

        
          

**JSON example**

          
: 
            

```
{
  "cursor": "MTAwMDAwMDAwNQ==",
  "errors": [],
  "products": [
    {
      "additionalFields": {},
      "catalogs": [
        {
          "customFields": {},
          "id": "0ZSSG000001875O4AQ",
          "name": "Hardware Catalog",
          "numberOfCategories": 4
        }
      ],
      "categories": [
        {
          "catalogId": "0ZSSG000001875O4AQ",
          "childCategories": [],
          "customFields": {},
          "eligiblePromotions": [],
          "id": "0ZGSG000001DJtv4AG",
          "name": "Accessories",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configurationRules": [
        {
          "details": [
            {
              "message": "recommend Mouse from monitor"
            }
          ],
          "type": "recommend"
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "HeyMicky Mouse compatible comes with choice of USB or Wireless connectivity.",
      "displayUrl": "https://5.imimg.com/data5/IS/JP/MY-58678879/computer-mouse.jpg",
      "eligiblePromotions": [],
      "id": "01tSG00000BiywkYAB",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Mouse",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isDerived": false,
          "isSelected": false,
          "price": 7.99,
          "priceBookEntryId": "01uSG000004wTsEYAU",
          "priceBookId": "01sSG00000DQCjhYAH",
          "pricingModel": {
            "id": "0jPSG000000Avcv2AC",
            "name": "One Time",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "productClassification": {
        "id": "11BSG00000UNijx2AD"
      },
      "productCode": "MOU001",
      "productSellingModelOptions": [
        {
          "id": "0iOSG000000J64x2AC",
          "isDefault": true,
          "productId": "01tSG00000BiywkYAB",
          "productSellingModel": {
            "doesAutoRenewByDefault": false,
            "id": "0jPSG000000Avcv2AC",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPSG000000Avcv2AC"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "qualificationContext": {
        "isQualified": true
      }
    }
  ],
  "success": true,
  "transactionContextId": "0000000p18dq18g002917732061529307c5e047346664b2f81ff3d4845acf2d0"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `cursor` | String | Unique ID to represent the position of each product in the data set. | Small, 67.0 | 67.0 |
| `errors` | [Product Recommendation Errors](./connect_responses_product_recommendation_errors_output.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 67.0 | 67.0 |
| `products` | [Recommended Products](./connect_responses_recommended_products_output.htm.md)[] | List of recommended products. | Small, 67.0 | 67.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `transactionContextId` | String | ID of the sales transaction context. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_related_component_output.htm ===
---
page_id: connect_responses_product_related_component_output.htm
title: Product Related Component
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_related_component_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Related Component

Output representation of the product-related component.

      
        
          

**JSON example**

          
: 
            

```
"productRelatedComponent": {
      "childProductId": "01tT1000000F0YyIAK",
      "childSellingModelId": "0jPT10000004CAfMAM",
      "doesBundlePriceIncludeChild": true,
      "id": "0dST100000000rgMAA",
      "isComponentRequired": false,
      "isDefaultComponent": false,
      "isExcluded": false,
      "isQuantityEditable": true,
      "maxQuantity": 3,
      "minQuantity": 1,
      "parentProductId": "01tT1000000F0afIAC",
      "parentSellingModelId": "0jPT10000004CAfMAM",
      "productClassificationId": "11BRO00000000222AA",
      "productRelationshipTypeId": "0yoT1000000002WIAQ",
      "quantity": 1,
      "quantityScaleMethod": "Proportional",
      "quoteVisibility": "Quote Document Only",
      "sequence": 1
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
| `child​Product​Id` | String | Lookup to the child product in the bundle. | Small, 60.0 | 60.0 |
| `child​Selling​ModelId` | String | ID of the child product selling model record. | Small, 60.0 | 60.0 |
| `does​Bundle​PriceInclude​Child` | Boolean | Indicates whether the price of the bundle includes the child product (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `id` | String | ID of the record. | Small, 60.0 | 60.0 |
| `isComponent​Required` | Boolean | Indicates whether the component is required in the bundle (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isDefault​Component` | Boolean | Indicates whether to select the component in the bundle group by default (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `isExcluded` | Boolean | Indicates whether the component is excluded in the bundle group (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `is​Quantity​Editable` | Boolean | Indicates whether to allow changes to the quantity of the component in the bundle (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `max​Quantity` | Double | Maximum quantity of the product in the opportunity, quote, or order line item. | Small, 60.0 | 60.0 |
| `min​Quantity` | Double | Minimum quantity of the product in the opportunity, quote, or order line item. | Small, 60.0 | 60.0 |
| `parent​Product​Id` | String | Lookup to the parent product. | Small, 60.0 | 60.0 |
| `parent​Selling​ModelId` | String | ID of the product selling model record. | Small, 60.0 | 60.0 |
| `product​Classification​Id` | String | ID of the product classification record. | Small, 60.0 | 60.0 |
| `productInstance​Reuse` | String | Reserved for future use. | Small, 62.0 | 62.0 |
| `product​Relationship​TypeId` | String | ID of the product relationship type record. | Small, 60.0 | 60.0 |
| `quantity` | Double | Quantity of the child products. | Small, 60.0 | 60.0 |
| `quantity​Scale​Method` | String | Method to scale the quantity of the child product in relation to the quantity of the parent. Valid values are: `Constant` `Proportional` | Small, 60.0 | 60.0 |
| `quote​Visibility` | String | Specifies whether a quote line item must be shown on the transaction line editor or quote document. Valid values are: `Always` `Transaction Line Editor Only`—Specifies whether to show a quote line item on quote editor only. `Quote Document Only`—Specifies whether to show a quote line item on quote proposal only. `Never` The API returns this property only if the CoreCPQ permission set is available. | Small, 64.0 | 64.0 |
| `sequence` | Integer | Order in which the child products are displayed. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_selling_model_option_output.htm ===
---
page_id: connect_responses_product_selling_model_option_output.htm
title: Product Selling Model Option
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_selling_model_option_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Selling Model Option

Output representation of the definition of the product selling model option.

    
      

#### Important

Where possible, we changed noninclusive terms to align with our company
        value of Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

      
        
          

**JSON example**

          
: 
            

```
"productSellingModelOptions": [
   {
    "id": "0iOT10000004CMrMAM",
    "isDefault": false,
    "productId": "01tT1000000F0YyIAK",
    "productSellingModel": {
    "id": "0jPT10000004CAfMAM",
    "name": "OneTimePSM",
    "pricingTerm": 1,
    "pricingTermUnit": "Months",
    "sellingModelType": "TermDefined",
    "status": "Active"
  }
}]
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the record. | Small, 60.0 | 60.0 |
| `isDefault` | Boolean | Indicates whether this model option is the default product selling model option (`true`) or not (`false`). | Small, 60.0 | 60.0 |
| `product​Id` | String | ID of the product. | Small, 60.0 | 60.0 |
| `product​Selling​Model` | [Product Selling Model](./connect_responses_product_selling_model_output.htm.md) | Master-detail field to the product selling model. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_selling_model_output.htm ===
---
page_id: connect_responses_product_selling_model_output.htm
title: Product Selling Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_selling_model_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Selling Model

Output representation of the definition of the product selling model.

      
        
          

**JSON example**

          
: 
            

```
"productSellingModel": 
{
  "id": "0jPT10000004CAfMAM",
  "name": "OneTimePSM",
  "pricingTerm": 1,
  "pricingTermUnit": "Months",
  "sellingModelType": "TermDefined",
  "status": "Active"
}
}]
```

          

        
      

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              
- 
- 
- 

              

              

            

            
              

              

              

              

              

            

          

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the record. | Small, 60.0 | 60.0 |
| `name` | String | Name of the record. | Small, 60.0 | 60.0 |
| `pricing​Term` | Integer | Duration of the selling model. | Small, 60.0 | 60.0 |
| `pricing​Term​Unit` | String | Units of the pricing term. | Small, 60.0 | 60.0 |
| `selling​Model​Type` | String | Different models of selling the product. Valid values are: `OneTime` `TermDefined` `Evergreen` | Small, 60.0 | 60.0 |
| `status` | String | Status of the selling model. For example, whether the selling model is active and can be used in transactions. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_specification_record_type_output.htm ===
---
page_id: connect_responses_product_specification_record_type_output.htm
title: Product Specification Record Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_specification_record_type_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Specification Record Type

Output representation of the details of the product specification record
    type.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `isCommercial` | Boolean | Indicates whether this product specification record type is commercial (`true`) or not (`false`). | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_product_specification_type_output.htm ===
---
page_id: connect_responses_product_specification_type_output.htm
title: Product Specification Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_specification_type_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Specification Type

Output representation of the product specification type.

      
        
          

**JSON example**

          
: 
            

```
"productSpecificationType": 
{
"name": "NonCommercialSpecType",
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | Name of the product specification type. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_product_variants_output.htm ===
---
page_id: connect_responses_product_variants_output.htm
title: Product Variants
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_product_variants_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Variants

Output representation of the variation products associated with the specified parent
    variant products.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "9b6bc520-3c82-4d6c-a458-47590370681a",
  "count": 2,
  "details": {
    "01tT1000000F0afIAC": [
      "01tT1000000F0ahIAC",
      "01tT1000000F0aiIAC"
    ],
    "01tT1000000F0agIAC": [
      "01tT1000000F0ajIAC"
    ]
  },
  "inValidProductIds": [],
  "nonVariantParentIds": [],
  "status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched the product variants."
  }
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique ID to track and associate related events or transactions. | Small, 67.0 | 67.0 |
| `count` | Integer | Number of parent variant products in the response that have at least one associated variation. | Small, 67.0 | 67.0 |
| `details` | Map<String, String[]> | Specifies a map where each key is a parent variant product ID and the value is a list of its associated variation product IDs. Only parent variants that have at least one variation are included in this map. | Small, 67.0 | 67.0 |
| `inValid​Product​Ids` | String[] | List of product IDs from the request that are blank, invalid, or not found in the org. The API excludes these IDs from processing but doesn’t fail the request. | Small, 67.0 | 67.0 |
| `non​Variant​Parent​Ids` | String[] | List of product IDs from the request that are valid products but don’t have the `VariationParent` product class. For example, simple products or bundle products passed in the request appear in this list. | Small, 67.0 | 67.0 |
| `status` | [Status](./connect_responses_status.htm.md) | Status of the request. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_products_output.htm ===
---
page_id: connect_responses_products_output.htm
title: Products
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_products_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Products

Output representation of the list of retrieved products.

      
        
          

**JSON example**

          
: 

```
{
  "correlationId": "9b6bc520-3c82-4d6c-a458-47590370681a",
  "facets":[
    {
      "attributeType": "ProductStandard",
      "displayName": "Product Type",
      "displayRank": 1,
      "displayType": "MultiSelect",
      "nameOrId": "Type",
      "values": [
        {
          "displayName": "Simple",
          "nameOrId": "Simple",
          "productCount": 9
        }
      ]
    },
    {
      "attributeType": "ProductStandard",
      "displayName": "Active",
      "displayRank": 2,
      "displayType": "MultiSelect",
      "nameOrId": "IsActive",
      "values": [
        {
          "displayName": "true",
          "nameOrId": "true",
          "productCount": 47
        }
      ]
    }
  ],
  "count": 3,
  "products": [
    {
      "attributeCategory": [],
      "attributes": [],
      "categories": [],
      "childProducts": [],
      "description": "Keep your organization connected with seamless collaboration across distributed teams. No matter where employees are located, organizations are seeking stronger employee engagement and customer experiences to enable more productivity and greater business agility. More effective collaboration helps organizations work smarter.",
      "displayUrl": "https://dispatch.m.io/wp-content/uploads/2023/01/History-of-Webex.png",
      "id": "01t1Q000008CD2eQAG",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "SmartBytes Collaboration Suite",
      "nodeType": "bundleProduct",
      "productClassification": {
        "id": "11B1Q0000008OMGUA2"
      },
      "productCode": "P0143",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iO1Q0000008OkeUAE",
          "productId": "01t1Q000008CD2eQAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVFUA0",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "None"
      }
    },
    {
      "attributeCategory": [],
      "attributes": [],
      "categories": [],
      "childProducts": [],
      "configureDuringSale": "Allowed",
      "displayUrl": "https://www.cisco.com/c/dam/en/us/products/collateral/wireless/small-business-300-series-wireless-access-points/datasheet-c78-732143.doc/_jcr_content/renditions/datasheet-c78-732143_1.jpg",
      "id": "01t1Q000008CD36QAG",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "SmartBytes Repeater",
      "nodeType": "simpleProduct",
      "productClassification": {
        "id": "11B1Q0000008OMMUA2"
      },
      "productCode": "BS_R001",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iO1Q0000008OlsUAE",
          "productId": "01t1Q000008CD36QAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVFUA0",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "COM_Offer"
      }
    },
    {
      "attributeCategory": [],
      "attributes": [],
      "categories": [],
      "childProducts": [],
      "configureDuringSale": "Allowed",
      "description": "A converged data center architecture that integrates computing, networking and storage resources to increase efficiency and enable centralized management. UCS products are designed and configured to work together effectively.",
      "displayUrl": "https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/sap-hana-scaleup-appliance-with-xseries-wp.docx/_jcr_content/renditions/sap-hana-scaleup-appliance-with-xseries-wp_3.png",
      "id": "01t1Q000008CD2sQAG",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "SmartBytes Unified Computing System",
      "nodeType": "bundleProduct",
      "productCode": "P0157",
      "productComponentGroups": [],
      "productSellingModelOptions": [
        {
          "id": "0iO1Q0000008OkzUAE",
          "productId": "01t1Q000008CD2sQAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVFUA0",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          }
        },
        {
          "id": "0iO1Q0000008OlWUAU",
          "productId": "01t1Q000008CD2sQAG",
          "productSellingModel": {
            "id": "0jP1Q000000CaVHUA0",
            "name": "Evergreen",
            "pricingTerm": 1,
            "pricingTermUnit": "Months",
            "sellingModelType": "Evergreen",
            "status": "Active"
          }
        }
      ],
      "productSpecificationType": {
        "name": "None"
      }
    }
  ],
  "status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched the product records."
  }
}
```

This example shows a sample response with data from Enterprise Product
            Catalog.

```
{
  "correlationId": "4cf1997d-5d86-4997-9c6b-55842442f325",
  "facets": [],
  "products": [
    {
      "additionalFields": {},
      "attributeCategory": [
        {
          "attributes": [
            {
              "additionalFields": {
                "OptOutAssetization": true,
                "OptOutDecompositionAction": false,
                "OptOutSupplementalAction": false
              },
              "attributeNameOverride": "ATTRIBUTE-ABP-INT",
              "code": "ABP-INT",
              "dataType": "Number",
              "developerName": "ABP-INT",
              "id": "ABP-INT",
              "isHidden": false,
              "isPriceImpacting": false,
              "isReadOnly": false,
              "isRequired": false,
              "name": "ATTRIBUTE-ABP-INT",
              "sequence": 3,
              "status": "Active"
            },
            {
              "additionalFields": {
                "OptOutAssetization": false,
                "OptOutDecompositionAction": false,
                "OptOutSupplementalAction": false
              },
              "attributeNameOverride": "ATTRIBUTE-ABP-CHECKBOX",
              "code": "ABP-CHECKBOX",
              "dataType": "Checkbox",
              "developerName": "ABP-CHECKBOX",
              "id": "ABP-CHECKBOX",
              "isHidden": false,
              "isPriceImpacting": false,
              "isReadOnly": false,
              "isRequired": false,
              "name": "ATTRIBUTE-ABP-CHECKBOX",
              "sequence": 2,
              "status": "Active"
            }
          ],
          "code": "CATEGORY-ABP",
          "id": "a0Zxx000000c3tNEAQ",
          "name": "ATTRIBUTE_CATEGORY-ABP"
        }
      ],
      "attributes": [],
      "catalogs": [],
      "categories": [],
      "childProducts": [],
      "id": "01txx0000006kFYAAY",
      "isActive": true,
      "isAssetizable": true,
      "name": "ARProduct",
      "nodeType": "simpleProduct",
      "productCode": "ARProduct",
      "productComponentGroups": [],
      "productSellingModelOptions": [],
      "productUnitOfMeasures": []
    }
  ],
  "status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched Product records."
  }
}
```

        
      

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 60.0 | 60.0 |
| `count` | Integer | Total count of the products matching the request query. | Small, 60.0 | 60.0 |
| `facets` | [Search Facet](./connect_responses_search_facet_output.htm.md) | Details of the faceted search. This property is applicable if the **Use Indexed Data For Product Listing and Search** toggle from the Product Discovery Settings page from Setup is enabled. | Small, 63.0 | 63.0 |
| `products` | [Product](./connect_responses_product_output.htm.md)[] | List of products matching the request query. | Small, 60.0 | 60.0 |
| `status` | [Status](./connect_responses_status.htm.md) | Status of the request. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_promotion_output.htm ===
---
page_id: connect_responses_promotion_output.htm
title: Promotion Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_promotion_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Promotion Details

Output representation of the details of applicable promotions.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `couponCode` | String | Coupon code for the promotion. | Small, 67.0 | 67.0 |
| `description` | String | Description of the promotion. | Small, 67.0 | 67.0 |
| `displayName` | String | Display name of the promotion. | Small, 67.0 | 67.0 |
| `endDateTime` | String | End date and time of the promotion. | Small, 67.0 | 67.0 |
| `id` | String | ID of the promotion. | Small, 67.0 | 67.0 |
| `isAutomatic` | Boolean | Indicates whether the promotion is automatic (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isCategoryPromo` | Boolean | Indicates whether the promotion is a category-level promotion (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isProductPromo` | Boolean | Indicates whether the promotion is a product-level promotion (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `name` | String | Name of the promotion. | Small, 67.0 | 67.0 |
| `priority` | Integer | Priority of the promotion. | Small, 67.0 | 67.0 |
| `startDateTime` | String | Start date and time of the promotion. | Small, 67.0 | 67.0 |
| `termsAndConditions` | String | Terms and conditions of the promotion. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_proration_policy_output.htm ===
---
page_id: connect_responses_proration_policy_output.htm
title: Proration Policy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_proration_policy_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Proration Policy

Output representation of the details of the proration policy component.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additionalFields` | Map<String, Object> | Fields associated with the proration policy. | Small, 67.0 | 67.0 |
| `id` | String | ID of the proration policy. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_qualification_context_output.htm ===
---
page_id: connect_responses_qualification_context_output.htm
title: Qualification Context
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_qualification_context_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Qualification Context

Output representation of the details about the product qualification.

      
        
          

**JSON example**

          
: 
            

```
{
  "qualificationContext": {
    "isQualified": true
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `isQualified` | Boolean | Indicates whether the product is qualified (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `reason` | String | Specifies the reason for product qualification or disqualification. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_recommended_products_output.htm ===
---
page_id: connect_responses_recommended_products_output.htm
title: Recommended Products
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_recommended_products_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Recommended Products

Output representation of the list of recommended products.

        
          

**JSON example**

          
: 
            

```
{
  "products": [
    {
      "additionalFields": {},
      "catalogs": [
        {
          "customFields": {},
          "id": "0ZSSG000001875O4AQ",
          "name": "Hardware Catalog",
          "numberOfCategories": 4
        }
      ],
      "categories": [
        {
          "catalogId": "0ZSSG000001875O4AQ",
          "childCategories": [],
          "customFields": {},
          "eligiblePromotions": [],
          "id": "0ZGSG000001DJtv4AG",
          "name": "Accessories",
          "qualificationContext": {
            "isQualified": true
          }
        }
      ],
      "configurationRules": [
        {
          "details": [
            {
              "message": "recommend Mouse from monitor"
            }
          ],
          "type": "recommend"
        }
      ],
      "configureDuringSale": "Allowed",
      "description": "HeyMicky Mouse compatible comes with choice of USB or Wireless connectivity.",
      "displayUrl": "https://5.imimg.com/data5/IS/JP/MY-58678879/computer-mouse.jpg",
      "eligiblePromotions": [],
      "id": "01tSG00000BiywkYAB",
      "isActive": true,
      "isAssetizable": true,
      "isSoldOnlyWithOtherProds": false,
      "name": "Mouse",
      "nodeType": "simpleProduct",
      "prices": [
        {
          "currencyIsoCode": "USD",
          "isDefault": true,
          "isDerived": false,
          "isSelected": false,
          "price": 7.99,
          "priceBookEntryId": "01uSG000004wTsEYAU",
          "priceBookId": "01sSG00000DQCjhYAH",
          "pricingModel": {
            "id": "0jPSG000000Avcv2AC",
            "name": "One Time",
            "pricingModelType": "OneTime"
          }
        }
      ],
      "productClassification": {
        "id": "11BSG00000UNijx2AD"
      },
      "productCode": "MOU001",
      "productSellingModelOptions": [
        {
          "id": "0iOSG000000J64x2AC",
          "isDefault": true,
          "productId": "01tSG00000BiywkYAB",
          "productSellingModel": {
            "doesAutoRenewByDefault": false,
            "id": "0jPSG000000Avcv2AC",
            "name": "One Time",
            "sellingModelType": "OneTime",
            "status": "Active"
          },
          "productSellingModelId": "0jPSG000000Avcv2AC"
        }
      ],
      "productSpecificationType": {
        "name": "Commercial",
        "productSpecificationRecordType": {}
      },
      "qualificationContext": {
        "isQualified": true
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additionalFields` | Map<String, Object> | Additional fields of the product. | Small, 67.0 | 67.0 |
| `availabilityDate` | String | Date when the part is used in the product or is made available for sale. | Small, 67.0 | 67.0 |
| `catalogs` | [Catalog](./connect_responses_product_discovery_catalog_output.htm.md)[] | List of the associated catalogs. This property returns the `name` and `id` values only. | Small, 67.0 | 67.0 |
| `categories` | [Category](./connect_responses_product_discovery_category_output.htm.md)[] | List of the associated categories. This property returns the `name` and `id` values only. | Small, 67.0 | 67.0 |
| `configurationRules` | [Product Configuration Rules](./connect_responses_product_configuration_rules_output.htm.md)[] | List of configuration rules of the product. | Small, 67.0 | 67.0 |
| `configureDuringSale` | String | Specifies whether to allow or prevent configuration when a bundle is sold. | Small, 67.0 | 67.0 |
| `description` | String | Description of the product. | Small, 67.0 | 67.0 |
| `discontinuedDate` | String | Date from when the part can’t be used in the product or sold. | Small, 67.0 | 67.0 |
| `displayUrl` | String | Display image URL of the product. | Small, 67.0 | 67.0 |
| `eligiblePromotions` | [Promotion Details](./connect_responses_promotion_output.htm.md)[] | List of applicable promotions of the product. | Small, 67.0 | 67.0 |
| `endOfLifeDate` | String | Date after which a product isn’t supported, ordered, or maintained. | Small, 67.0 | 67.0 |
| `id` | String | ID of the product. | Small, 67.0 | 67.0 |
| `isActive` | Boolean | Indicates whether the product is active (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isAssetizable` | Boolean | Indicates whether a product instance remains a customer asset after it’s purchased (`true`) or not (`false`). The default value is `true`. | Small, 67.0 | 67.0 |
| `isComponentRequired` | Boolean | Indicates whether a product component is required (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isDefaultComponent` | Boolean | Indicates whether a product component is a default component (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isQuantityEditable` | Boolean | Indicates whether the quantity of a product is editable (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `isSoldOnlyWithOtherProds` | Boolean | Indicates whether a product can be sold only with other products (`true`) or not (`false`). | Small, 67.0 | 67.0 |
| `name` | String | Name of the product. | Small, 67.0 | 67.0 |
| `nodeType` | String | Specifies whether a node is a product node or a product classification node. | Small, 67.0 | 67.0 |
| `prices` | [Product Prices](./connect_responses_product_prices_output.htm.md)[] | Pricing details of a product. | Small, 67.0 | 67.0 |
| `productClassification` | [Product Classification](./connect_responses_product_discovery_product_classification_output.htm.md)[] | Details of the product classification that the product is based on. | Small, 67.0 | 67.0 |
| `productCode` | String | Universal product code that’s used to track the part that’s used in the product. | Small, 67.0 | 67.0 |
| `productQuantity` | [Product Quantity](./connect_responses_product_quantity_output.htm.md)[] | Quantity details of a product. | Small, 67.0 | 67.0 |
| `productSellingModelOptions` | [Product Selling Model Option](./connect_responses_product_discovery_product_selling_model_option_output.htm.md)[] | Details of the product selling model options. | Small, 67.0 | 67.0 |
| `productSpecificationType` | [Product Specification Type](./connect_responses_product_discovery_product_specification_type_output.htm.md)[] | Details of the product specification type. | Small, 67.0 | 67.0 |
| `productType` | String | Details about the product type. | Small, 67.0 | 67.0 |
| `qualificationContext` | [Qualification Context](./connect_responses_qualification_context_output.htm.md)[] | Context details of a user, which are used for qualification rules. | Small, 67.0 | 67.0 |
| `status` | String | Status of the product, such as active or inactive. | Small, 67.0 | 67.0 |

=== ARTICLE: connect_responses_related_object_records_output.htm ===
---
page_id: connect_responses_related_object_records_output.htm
title: Related Object Records
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_related_object_records_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Object Records

Output representation of the related records for a specified record ID and related object
    API name.

        
          

**JSON example**

          
: 
            

```
      "relatedObjectRecords": [
        {
          "count": 2,
          "records": [
            {
              "SegmentType": "Yearly",
              "DurationType": "Months",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CDtGAM",
              "Name": "PPRS-000000005"
            },
            {
              "SegmentType": "FreeTrial",
              "DurationType": "Days",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CFUGA2",
              "Name": "PPRS-000000006"
            }
          ],
          "relatedObjectAPIName": "ProductRampSegment"
        },
        {
          "count": 2,
          "records": [
            {
              "UsageMetricId": "1BRxx0000004CAeGAM",
              "UsageMetricName": "Test Usage Metric 2",
              "UsageDefinitionProductId": null,
              "Label": "PUG-103",
              "Quantity": 100,
              "Id": "1BXxx0000004CCGGA2"
            },
            {
              "UsageMetricId": "1BRxx0000004CCGGA2",
              "UsageMetricName": "Test Usage Metric 3",
              "UsageDefinitionProductId": "01txx0000006i2eAAA",
              "Label": "PUG-105",
              "Quantity": 500,
              "Id": "1BXxx0000004CFUGA2"
            }
          ],
          "relatedObjectAPIName": "ProductUsageGrant"
        }
      ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `count` | Integer | Total count of the related records that are returned. | Small, 62.0 | 62.0 |
| `records` | Map<String, Object> | List of related object records. | Small, 62.0 | 62.0 |
| `relatedObject​APIName` | String | API name of the related object to return the records for. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_related_records_list_output.htm ===
---
page_id: connect_responses_related_records_list_output.htm
title: Related Records List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_related_records_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Records List

Output representation of the list of related records.

        
          

**JSON example**

          
: 
            

```
{
  "correlationId": "f4d6b42a-d9b7-49c9-8fa8-1c7bb6fe99aa",
  "relatedRecords": [
    {
      "recordId": "01txx0000006i44AAA",
      "relatedObjectRecords": [
        {
          "count": 2,
          "records": [
            {
              "SegmentType": "Yearly",
              "DurationType": "Months",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CDtGAM",
              "Name": "PPRS-000000005"
            },
            {
              "SegmentType": "FreeTrial",
              "DurationType": "Days",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CFUGA2",
              "Name": "PPRS-000000006"
            }
          ],
          "relatedObjectAPIName": "ProductRampSegment"
        },
        {
          "count": 2,
          "records": [
            {
              "UsageMetricId": "1BRxx0000004CAeGAM",
              "UsageMetricName": "Test Usage Metric 2",
              "UsageDefinitionProductId": null,
              "Label": "PUG-103",
              "Quantity": 100,
              "Id": "1BXxx0000004CCGGA2"
            },
            {
              "UsageMetricId": "1BRxx0000004CCGGA2",
              "UsageMetricName": "Test Usage Metric 3",
              "UsageDefinitionProductId": "01txx0000006i2eAAA",
              "Label": "PUG-105",
              "Quantity": 500,
              "Id": "1BXxx0000004CFUGA2"
            }
          ],
          "relatedObjectAPIName": "ProductUsageGrant"
        }
      ]
    },
    {
      "recordId": "01txx0000006i5gAAA",
      "relatedObjectRecords": [
        {
          "count": 4,
          "records": [
            {
              "SegmentType": "Yearly",
              "DurationType": "Months",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004C92GAE",
              "Name": "PPRS-000000001"
            },
            {
              "SegmentType": "Custom",
              "DurationType": "Days",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CAeGAM",
              "Name": "PPRS-000000002"
            },
            {
              "SegmentType": "FreeTrial",
              "DurationType": "Months",
              "TrialDuration": 6,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CCGGA2",
              "Name": "PPRS-000000003"
            },
            {
              "SegmentType": "Custom",
              "DurationType": null,
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CDsGAM",
              "Name": "PPRS-000000004"
            }
          ],
          "relatedObjectAPIName": "ProductRampSegment"
        },
        {
          "count": 0,
          "records": [],
          "relatedObjectAPIName": "ProductUsageGrant"
        }
      ]
    }
  ],
  "status": {
    "code": "200",
    "errors": [
    ],
    "message": ""
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 62.0 | 62.0 |
| `related​Records` | [Related Records](./connect_responses_related_records_output.htm.md)[] | List of related records. | Small, 62.0 | 62.0 |
| `status` | [Status](./connect_responses_status.htm.md)[] | Status of the API request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_related_records_output.htm ===
---
page_id: connect_responses_related_records_output.htm
title: Related Records
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_related_records_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Related Records

Output representation of the list of relatedObject records for a specified record
    ID.

        
          

**JSON example**

          
: 
            

```
  "relatedRecords": [
    {
      "recordId": "01txx0000006i44AAA",
      "relatedObjectRecords": [
        {
          "count": 2,
          "records": [
            {
              "SegmentType": "Yearly",
              "DurationType": "Months",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CDtGAM",
              "Name": "PPRS-000000005"
            },
            {
              "SegmentType": "FreeTrial",
              "DurationType": "Days",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx000000001dEAA",
              "ProductId": "01txx0000006i44AAA",
              "Id": "1FTxx0000004CFUGA2",
              "Name": "PPRS-000000006"
            }
          ],
          "relatedObjectAPIName": "ProductRampSegment"
        },
        {
          "count": 2,
          "records": [
            {
              "UsageMetricId": "1BRxx0000004CAeGAM",
              "UsageMetricName": "Test Usage Metric 2",
              "UsageDefinitionProductId": null,
              "Label": "PUG-103",
              "Quantity": 100,
              "Id": "1BXxx0000004CCGGA2"
            },
            {
              "UsageMetricId": "1BRxx0000004CCGGA2",
              "UsageMetricName": "Test Usage Metric 3",
              "UsageDefinitionProductId": "01txx0000006i2eAAA",
              "Label": "PUG-105",
              "Quantity": 500,
              "Id": "1BXxx0000004CFUGA2"
            }
          ],
          "relatedObjectAPIName": "ProductUsageGrant"
        }
      ]
    },
    {
      "recordId": "01txx0000006i5gAAA",
      "relatedObjectRecords": [
        {
          "count": 4,
          "records": [
            {
              "SegmentType": "Yearly",
              "DurationType": "Months",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004C92GAE",
              "Name": "PPRS-000000001"
            },
            {
              "SegmentType": "Custom",
              "DurationType": "Days",
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CAeGAM",
              "Name": "PPRS-000000002"
            },
            {
              "SegmentType": "FreeTrial",
              "DurationType": "Months",
              "TrialDuration": 6,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CCGGA2",
              "Name": "PPRS-000000003"
            },
            {
              "SegmentType": "Custom",
              "DurationType": null,
              "TrialDuration": null,
              "ProductSellingModelId": "0jPxx0000000001EAA",
              "ProductId": "01txx0000006i5gAAA",
              "Id": "1FTxx0000004CDsGAM",
              "Name": "PPRS-000000004"
            }
          ],
          "relatedObjectAPIName": "ProductRampSegment"
        },
        {
          "count": 0,
          "records": [],
          "relatedObjectAPIName": "ProductUsageGrant"
        }
      ]
    }
  ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `recordId` | String | ID of the record. | Small, 62.0 | 62.0 |
| `relatedObject​Records` | [Related Object Records](./connect_responses_related_object_records_output.htm.md)[] | List of related object records. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_search_facet_output.htm ===
---
page_id: connect_responses_search_facet_output.htm
title: Search Facet
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_search_facet_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Search Facet

Output representation of the details of the faceted search.

      
        
          

**JSON example**

          
: 
            

```

  "facets":[
    {
      "attributeType": "ProductStandard",
      "displayName": "Product Type",
      "displayRank": 1,
      "displayType": "MultiSelect",
      "nameOrId": "Type",
      "values": [
        {
          "displayName": "Simple",
          "nameOrId": "Simple",
          "productCount": 9
        }
      ]
    },
    {
      "attributeType": "ProductStandard",
      "displayName": "Active",
      "displayRank": 2,
      "displayType": "MultiSelect",
      "nameOrId": "IsActive",
      "values": [
        {
          "displayName": "true",
          "nameOrId": "true",
          "productCount": 47
        }
      ]
    }
  ]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attribute​Type` | String | Search attribute type of the facet. | Small, 63.0 | 63.0 |
| `display​Name` | String | Display name of the facet. | Small, 63.0 | 63.0 |
| `display​Rank` | Integer | Display rank of the facet. | Small, 63.0 | 63.0 |
| `display​Type` | String | Display type of the face. | Small, 63.0 | 63.0 |
| `nameOr​Id` | String | Facet name or ID. Reserved for internal use. | Small, 63.0 | 63.0 |
| `values` | [Facet Value](./connect_responses_facet_value_output.htm.md)[] | Values of the facet found in the search result. Sorted by display name in alphabetical order. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_search_products_facet.htm ===
---
page_id: connect_responses_search_products_facet.htm
title: Search Products Facet
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_search_products_facet.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Search Products Facet

Output representation of the details of the faceted search.

        
          

**JSON example**

          
: 
            

```
  "facets": [
    {
      "attributeType": "ProductStandard",
      "displayName": "Product Type",
      "displayRank": 2,
      "nameOrId": "Type",
      "values": [
        {
          "displayName": "Bundle",
          "nameOrId": "Bundle"
        }
      ]
    },
    {
      "attributeType": "ProductDynamicAttribute",
      "displayName": "Display",
      "displayRank": 3,
      "nameOrId": "0tjDU0000003K5BYAU",
      "values": [
        {
          "displayName": "1080p Built-in Display",
          "nameOrId": "1080p Built-in Display"
        },
        {
          "displayName": "2k Built-in Display",
          "nameOrId": "2k Built-in Display"
        },
        {
          "displayName": "4k Built-in Display",
          "nameOrId": "4k Built-in Display"
        }
      ]
    }
  ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `attribute​Type` | String | Search attribute type of the facet. | Small, 63.0 | 63.0 |
| `display​Name` | String | Display name of the facet. | Small, 63.0 | 63.0 |
| `display​Rank` | Integer | Display rank for the facet. | Small, 63.0 | 63.0 |
| `nameOr​Id` | String | ID or the internal name of the facet. | Small, 63.0 | 63.0 |
| `values` | [Facet Value](./connect_responses_facet_value.htm.md)[] | Values of the facet found in the search result. Sorted by display name in alphabetical order. | Medium, 63.0 | 63.0 |

=== ARTICLE: connect_responses_setting_metadata_output.htm ===
---
page_id: connect_responses_setting_metadata_output.htm
title: Setting Metadata
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_setting_metadata_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Setting Metadata

Output representation of the metadata associated with a setting.

    
      
        
          

**JSON example**

          
: 
            

```

  "metadata": {
    "activeLanguages": [
      "en_US"
    ]
  }
```

          

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `active​Languages` | String[] | List of active languages in an org. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_setting_output.htm ===
---
page_id: connect_responses_setting_output.htm
title: Setting
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_setting_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Setting

Output representation of the setting that’s used in indexing.

    
      
        
          

**JSON example**

          
: 
            

```

  "setting": {
    "defaultLanguage": "en_US",
    "id": "1JySG0000000GUb0AM",
    "supportedLanguages": ["en_US","ja","es","nl_NL"]
  }
```

          

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `default​Language` | String | Default language for the API. | Small, 63.0 | 63.0 |
| `id` | String | ID of the setting. | Small, 63.0 | 63.0 |
| `supported​Languages` | String[] | List of supported language locales for indexing. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_snapshot_collection_output.htm ===
---
page_id: connect_responses_snapshot_collection_output.htm
title: Snapshot Collection
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_collection_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Collection

Output representation of the retrieved snapshot collection.

      
        
          

**JSON example**

          
: 
            

```
{
  "errors": [],
  "snapshots": [
    {
      "activationDate": "2024-11-06T06:58:02.000Z",
      "activationStatus": "ACTIVE",
      "activationType": "IMMEDIATE",
      "id": "1Avxx0000004C92CAE",
      "snapshotIndexes": [
        {
          "createdDate": "2024-11-06T06:56:49.000Z",
          "id": "1D6xx0000004C92CAE",
          "indexBuildType": "FULL",
          "indexInfos": [
            {
              "buildType": "FULL",
              "id": "0axxx00000000T3AAI",
              "isIncrementable": true,
              "usageType": "LIVE"
            }
          ],
          "indexLogs": [
            {
              "catalogSnapshotTime": "2024-11-06T16:14:30.000Z",
              "completionTime": "2024-11-06T16:16:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "FULL",
              "indexId": "0axxx00000000T3AAI",
              "numberOfChanges": 7
            },
            {
              "catalogSnapshotTime": "2024-11-06T15:03:32.000Z",
              "completionTime": "2024-11-06T15:05:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 3
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:35:34.000Z",
              "completionTime": "2024-11-06T12:35:34.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "There are no changes for the partial update.",
              "numberOfChanges": 0
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:07:32.000Z",
              "completionTime": "2024-11-06T12:09:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "FULL",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 1
            }
          ],
          "indexType": "PRODUCT",
          "lastBuildStatus": "IN_PROGRESS",
          "venueId": "1D6xx0000004C92CAE"
        }
      ]
    }
  ],
  "statusCode": "200"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 62.0 | 62.0 |
| `snapshots` | [Snapshot](./connect_responses_snapshot_output.htm.md)[] | List of active snapshots. | Small, 62.0 | 62.0 |
| `statusCode` | String | Code indicating the status of the request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_snapshot_deployment_output.htm ===
---
page_id: connect_responses_snapshot_deployment_output.htm
title: Snapshot Deployment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_deployment_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Deployment

Output representation of the snapshot deployment.

        
          

**JSON example**

          
: This example shows a sample response to the request to build a new snapshot with
            immediate activation.

          
: 
            

```
{
  "errors": [],
  "snapshot": {
    "activationStatus": "NONE",
    "activationType": "IMMEDIATE",
    "id": "1Avxx0000004CFU",
    "snapshotIndexes": [
      {
        "createdDate": "2024-07-24T21:10:48.000Z",
        "id": "1D6xx0000004CFU",
        "indexBuildType": "FULL",
        "indexType": "PRODUCT",
        "lastBuildStatus": "IN_PROGRESS"
      }
    ]
  },
  "statusCode": "200"
}
```

          

          
: This example shows a sample response of the request to rebuild a snapshot in the
              `active` status.

          
: 
            

```
{
  "errors": [],
  "snapshot": {
    "activationStatus": "NONE",
    "activationType": "IMMEDIATE",
    "id": "1Avxx0000004CH6",
    "snapshotIndexes": [
      {
        "createdDate": "2024-07-24T21:13:05.000Z",
        "id": "1D6xx0000004CH6",
        "indexBuildType": "FULL",
        "indexType": "PRODUCT",
        "lastBuildStatus": "IN_PROGRESS"
      }
    ]
  },
  "statusCode": "200"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors, if any. | Small, 62.0 | 62.0 |
| `snapshot` | [Snapshot](./connect_responses_snapshot_output.htm.md)[] | Run-time catalog snapshot associated with the created index. | Small, 62.0 | 62.0 |
| `statusCode` | String | Code indicating the status of the request. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_snapshot_index_error_output.htm ===
---
page_id: connect_responses_snapshot_index_error_output.htm
title: Snapshot Index Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_index_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Index Error

Output representation of the error details related to a snapshot index.

      
        
          

**JSON example**

          
: 
            

```
{
  "errors": [],
  "indexErrorDetails": {
    "errorFileId": "069xx0000004C92AAE",
    "indexCreatedDate": "2024-10-03T05:24:18.000Z",
    "indexErrorsCount": 1,
    "indexLastUpdatedDate": "2024-10-03T05:27:00.000Z",
    "itemLevelErrorsCount": 1
  },
  "statusCode": "200"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Output](./connect_responses_epc_error_output.htm.md)[] | List of errors encountered during the processing of the API request. | Small, 63.0 | 63.0 |
| `indexError​Details` | [Index Error](./connect_responses_index_error_output.htm.md)[] | Count and details of errors that occurred during indexing. | Small, 63.0 | 63.0 |
| `status​Code` | String | Code that indicates the status of the API request. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_snapshot_index_info_output.htm ===
---
page_id: connect_responses_snapshot_index_info_output.htm
title: Snapshot Index Info
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_index_info_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Index Info

Output representation of the details of a snapshot index.

      
        
          

**JSON example**

          
: 
            

```
 "indexInfos": [
            {
              "buildType": "FULL",
              "id": "0axxx00000000T3AAI",
              "isIncrementable": true,
              "usageType": "LIVE"
            }
          ]
```

          

        
      

- 
- 

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `buildType` | String | Build type of the index. Valid values are: `FULL`—Specifies a full index build. `INCREMENTAL`—Specifies an incremental index build. Available in API version 63.0 and later. | Small, 63.0 | 63.0 |
| `id` | String | ID of the index information record. | Small, 63.0 | 63.0 |
| `isIncrementable` | Boolean | Indicates whether a partial build is enabled (`true`) or disabled (`false`). | Small, 63.0 | 63.0 |
| `usageType` | String | Usage type of the index. Valid values are: `LIVE`—Index usage type is live. `OUT_OF_USE`—Index usage type is out of use. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_snapshot_index_log_output.htm ===
---
page_id: connect_responses_snapshot_index_log_output.htm
title: Snapshot Index Log
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_index_log_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Index Log

Output representation of a snapshot index log.

      
        
          

**JSON example**

          
: 
            

```
          "indexLogs": [
            {
              "catalogSnapshotTime": "2024-11-06T16:14:30.000Z",
              "completionTime": "2024-11-06T16:16:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "FULL",
              "indexId": "0axxx00000000T3AAI",
              "numberOfChanges": 7
            },
            {
              "catalogSnapshotTime": "2024-11-06T15:03:32.000Z",
              "completionTime": "2024-11-06T15:05:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 3
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:35:34.000Z",
              "completionTime": "2024-11-06T12:35:34.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "There are no changes for the partial update.",
              "numberOfChanges": 0
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:07:32.000Z",
              "completionTime": "2024-11-06T12:09:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "FULL",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 1
            }
          ]
```

          

        
      

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `catalog​SnapshotTime` | String | Catalog snapshot time of the index. | Small, 63.0 | 63.0 |
| `completion​Time` | String | Completion time of the index. | Small, 63.0 | 63.0 |
| `createdBy​Id` | String | ID of the user that initiated the index build. | Small, 63.0 | 63.0 |
| `indexBuild​Status` | String | Status of the index build. | Small, 63.0 | 63.0 |
| `indexBuild​Type` | String | Type of the index build. Valid values are: `FULL`—Specifies a full index build. `INCREMENTAL`—Specifies an incremental index build. Available in API version 63.0 and later. | Small, 63.0 | 63.0 |
| `index​Id` | String | ID of the index. | Small, 63.0 | 63.0 |
| `message` | String | Message for the index status. | Small, 63.0 | 63.0 |
| `numberOf​Changes` | Integer | Number of new or changed products included in the index. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_snapshot_index_output.htm ===
---
page_id: connect_responses_snapshot_index_output.htm
title: Snapshot Index
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_index_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot Index

Output representation of the snapshot index of a run-time catalog.

      
        
          

**JSON example**

          
: 
            

```
      "snapshotIndexes": [
        {
          "createdDate": "2024-11-06T06:56:49.000Z",
          "id": "1D6xx0000004C92CAE",
          "indexBuildType": "FULL",
          "indexInfos": [
            {
              "buildType": "FULL",
              "id": "0axxx00000000T3AAI",
              "isIncrementable": true,
              "usageType": "LIVE"
            }
          ],
          "indexLogs": [
            {
              "catalogSnapshotTime": "2024-11-06T16:14:30.000Z",
              "completionTime": "2024-11-06T16:16:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "FULL",
              "indexId": "0axxx00000000T3AAI",
              "numberOfChanges": 7
            },
            {
              "catalogSnapshotTime": "2024-11-06T15:03:32.000Z",
              "completionTime": "2024-11-06T15:05:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 3
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:35:34.000Z",
              "completionTime": "2024-11-06T12:35:34.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "There are no changes for the partial update.",
              "numberOfChanges": 0
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:07:32.000Z",
              "completionTime": "2024-11-06T12:09:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "FULL",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 1
            }
          ],
          "indexType": "PRODUCT",
          "lastBuildStatus": "IN_PROGRESS",
          "venueId": "1D6xx0000004C92CAE"
        }
      ]
```

          

        
      

- 
- 

            
              

              

              

              

              

            

            
              

              

              

              

              

            

- 

- 
- 
- 

            
              

              

              

              

              

            

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `completed​Date` | String | Completed date of the snapshot index. | Small, 62.0 | 62.0 |
| `created​Date` | String | Created date of the snapshot index. | Small, 62.0 | 62.0 |
| `id` | String | ID of the snapshot index. | Small, 62.0 | 62.0 |
| `indexBuild​Type` | String | Build type of the snapshot index. Valid value is: `FULL`—Specifies a full index build. `INCREMENTAL`—Specifies an incremental index build. Available in API version 63.0 and later. | Small, 62.0 | 62.0 |
| `indexInfos` | [Index Info](./connect_responses_snapshot_index_info_output.htm.md) | Index information records associated with the snapshot index. | Small, 63.0 | 63.0 |
| `indexLogs` | [Index Logs](./connect_responses_snapshot_index_log_output.htm.md)[] | Index logs associated with the snapshot index. | Small, 63.0 | 63.0 |
| `indexType` | String | Index type of the snapshot index. Valid value is: `PRODUCT`—Snapshot index is of product type. | Small, 62.0 | 62.0 |
| `lastBuild​Status` | String | Last build status of the snapshot index. Valid values are: `IN_PROGRESS`—Snapshot index build is in progress. `FAILED`—Snapshot index build failed. `COMPLETED`—Snapshot index build completed successfully. | Small, 62.0 | 62.0 |
| `numberOf​Records` | Integer | Number of indexed records. | Small, 62.0 | 62.0 |
| `venueId` | String | Venue ID of the snapshot index. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_snapshot_output.htm ===
---
page_id: connect_responses_snapshot_output.htm
title: Snapshot
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_snapshot_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Snapshot

Output representation of the list of active snapshots.

      
        
          

**JSON example**

          
: 
            

```
  "snapshots": [
    {
      "activationDate": "2024-11-06T06:58:02.000Z",
      "activationStatus": "ACTIVE",
      "activationType": "IMMEDIATE",
      "id": "1Avxx0000004C92CAE",
      "snapshotIndexes": [
        {
          "createdDate": "2024-11-06T06:56:49.000Z",
          "id": "1D6xx0000004C92CAE",
          "indexBuildType": "FULL",
          "indexInfos": [
            {
              "buildType": "FULL",
              "id": "0axxx00000000T3AAI",
              "isIncrementable": true,
              "usageType": "LIVE"
            }
          ],
          "indexLogs": [
            {
              "catalogSnapshotTime": "2024-11-06T16:14:30.000Z",
              "completionTime": "2024-11-06T16:16:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "FULL",
              "indexId": "0axxx00000000T3AAI",
              "numberOfChanges": 7
            },
            {
              "catalogSnapshotTime": "2024-11-06T15:03:32.000Z",
              "completionTime": "2024-11-06T15:05:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 3
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:35:34.000Z",
              "completionTime": "2024-11-06T12:35:34.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED",
              "indexBuildType": "INCREMENTAL",
              "indexId": "0axxx00000000RRAAY",
              "message": "There are no changes for the partial update.",
              "numberOfChanges": 0
            },
            {
              "catalogSnapshotTime": "2024-11-06T12:07:32.000Z",
              "completionTime": "2024-11-06T12:09:02.000Z",
              "createdById": "005xx000001X7x7AAC",
              "indexBuildStatus": "COMPLETED_WITH_ERRORS",
              "indexBuildType": "FULL",
              "message": "Warning: Product errors found.",
              "numberOfChanges": 1
            }
          ],
          "indexType": "PRODUCT",
          "lastBuildStatus": "IN_PROGRESS",
          "venueId": "1D6xx0000004C92CAE"
        }
      ]
    }
  ]
```

          

        
      

- 
- 
- 

- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `activation​Date` | String | Activation date of the snapshot. | Small, 62.0 | 62.0 |
| `activation​Status` | String | Activation status of the snapshot. Valid values are: `NONE` `ACTIVE`—Snapshot is in active status. `EXPIRED`—Snapshot is in expired status. | Small, 62.0 | 62.0 |
| `activation​Type` | String | Activation type of the snapshot. Valid values are: `IMMEDIATE`—Snapshot is activated immediately after a successful build. | Small, 62.0 | 62.0 |
| `id` | String | ID of the snapshot. | Small, 61.0 | 61.0 |
| `snapshot​Indexes` | [Snapshot Index](./connect_responses_snapshot_index_output.htm.md)[] | List of indexes created in the snapshot. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_status.htm ===
---
page_id: connect_responses_status.htm
title: Status
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_status.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Status

Output representation of the status of the request.

    
      
        
          

**JSON example**

          
: 
            

```
"status": {
    "code": "200",
    "errors": [],
    "message": "Successfully fetched the catalog records."
  }
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Code of the error message. | Small, 60.0 | 60.0 |
| `errors` | [Error](./connect_responses_epc_error_output.htm.md)[] | Details of the error. | Small, 60.0 | 60.0 |
| `message` | String | Error message. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_unit_of_measure_error_output.htm ===
---
page_id: connect_responses_unit_of_measure_error_output.htm
title: Unit of Measure Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_unit_of_measure_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unit of Measure Error

Output representation of the details of errors encountered during the processing of the
    Unit of Measure API request.

      
        
          

**JSON example**

          
: 
            

```
  "errorCodeToErrorMap": {
    "UNIT_OF_MEASURE_INFO_INVALID_UOM_IDS": {
      "errorCode": "UOM_INFO_API_003",
      "messageDetail": "Invalid uomId is passed. Please specify a valid uomId.",
      "messageTitle": "Invalid uomId is passed.",
      "recordIds": [
        "sample"
      ],
      "source": "Unit_Of_Measure_Info_Api"
    }
  }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Localized error code. | Small, 63.0 | 63.0 |
| `messageDetail` | String | Localized details of the error message. | Small, 63.0 | 63.0 |
| `messageTitle` | String | Localized title of the error message. | Small, 63.0 | 63.0 |
| `recordIds` | String[] | List of erroneous record IDs. | Small, 63.0 | 63.0 |
| `source` | String | Localized source of the error. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_unit_of_measure_info_output.htm ===
---
page_id: connect_responses_unit_of_measure_info_output.htm
title: Unit of Measure Info
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_unit_of_measure_info_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unit of Measure Info

Output representation of the details of a unit of measure record.

      
        
          

**JSON example**

          
: 
            

```
  "uomIdToUnitOfMeasureInfo": {
    "0hEU200000003M5MAI": {
      "id": "0hEU200000003M5MAI",
      "name": "Pounds",
      "roundingMethod": "Nearest",
      "scale": 1,
      "unitCode": "Pounds"
    },
    "0hEU200000003KTMAY": {
      "id": "0hEU200000003KTMAY",
      "name": "Grams",
      "roundingMethod": "Down",
      "scale": 5,
      "unitCode": "Grams"
    }
  }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the unit of measure record. | Small, 63.0 | 63.0 |
| `name` | String | Name of the unit of measure record. | Small, 63.0 | 63.0 |
| `roundingMethod` | String | Data rounding method of the unit of measure record. | Small, 63.0 | 63.0 |
| `scale` | Integer | Scale of the unit of measure record. | Small, 63.0 | 63.0 |
| `unitCode` | String | Code of the unit of measure record. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_unit_of_measure_status.htm ===
---
page_id: connect_responses_unit_of_measure_status.htm
title: Unit of Measure Status
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_unit_of_measure_status.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unit of Measure Status

Output representation of the status of the Unit of Measure API request.

      
        
          

**JSON example**

          
: 
            

```
  "status": {
    "errors": [],
    "httpStatusCode": "200",
    "message": " Successfully fetched UnitOfMeasure Info. "
  }
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Unit Of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)[] | Errors encountered during the processing of the API request. | Small, 63.0 | 63.0 |
| `httpStatus​Code` | String | HTTP status code of the API request. | Small, 63.0 | 63.0 |
| `message` | String | Localized response message. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_user_context_output.htm ===
---
page_id: connect_responses_user_context_output.htm
title: User Context
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_user_context_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# User Context

Output representation of the user context details.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `context​Id` | String | ID of the context. | Small, 60.0 | 60.0 |

=== ARTICLE: meta_productcatalogmanagementsettings.htm ===
---
page_id: meta_productcatalogmanagementsettings.htm
title: ProductCatalogManagementSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productcatalogmanagementsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductCatalogManagementSettings

Represents the settings for Product Catalog
			Management.

	
		

## Parent Type and Manifest Access

			
			

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

			

In the package manifest, all the settings metadata types for the org are accessed
				using the “Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

		

		

## File Suffix and Directory Location

			
			

ProductCatalogManagementSettings values are stored in the
					ProductCatalogManagementSettings.settings file in the
					settings folder. The .settings files
				are different from other named components, because there is only one settings file
				for each settings component.

		

	

## Version

		
		

ProductCatalogManagementSettings components are available in API version 64.0 and later.

	

	

## Special Access Rules

		
			

These settings are available when Product Catalog Management is enabled.

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| productDeepCloneContextDefOrgValue | **Field Type** string **Description** Name of the context definition that you want to use to deep clone the product. |
| productDeepCloneExpressionSetOrgValue | **Field Type** string **Description** Expression set that contains the rules that you want to apply to deep clone the product. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a ProductCatalogManagementSettings component.

			

```
<ProductCatalogManagementSettings xmlns="http://soap.sforce.com/2006/04/metadata">
<productDeepCloneContextDefOrgValue>ProductDeepCloneContextDefinition</productDeepCloneContextDefOrgValue>
<productDeepCloneExpressionSetOrgValue>ProductDeepCloneExpressionSet</productDeepCloneExpressionSetOrgValue>
</ProductCatalogManagementSettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>ProductCatalogManagement</members>
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

=== ARTICLE: meta_productdiscoverysettings.htm ===
---
page_id: meta_productdiscoverysettings.htm
title: ProductDiscoverySettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productdiscoverysettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductDiscoverySettings

Represents the settings for Product
		Discovery.

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

ProductDiscoverySettings values are stored in the
					ProductDiscoverySettings.settings file in the
					settings folder. The .settings files
				are different from other named components, because there is only one settings file
				for each settings component.

	

	

## Version

		
		

ProductDiscoverySettings components are available in API version 62.0 and later.

	

	

	

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

				

				

			
| Field Name | Description |
| --- | --- |
| enableGuidedSelling | **Field Type** boolean **Description** Indicates whether guided product selection is enabled (`true`) or not (`false`). Using guided product selection, you can manage dynamic forms that assess user requirements and show relevant products. The default value is `false`. Available in API version 63.0 and later. |
| enableProdDiscConstraintRules | **Field Type** boolean **Description** Indicates whether to enable the Constraint Rules Engine within Product Discovery (`true`) or not (`false`). The default value is `false`.If set to `true`, this setting activates constraint-based configuration rules so that the Constraint Rules Engine evaluates product selections during configuration. This step determines valid combinations based on defined constraints. Available in API version 67.0 and later. |
| discoverProductsFlowNameOrgValue | **Field Type** string **Description** Name of the custom flow for browsing and adding products. If this field isn’t specified, the Discover Products flow is used for browsing and adding products. Available in API version 63.0 and later. |
| prodDiscBrowseContextDefOrgValue | **Field Type** string **Description** Context definition that gets updated based on the user-selected options and provides summary data. |
| prodDiscDefaultCatalogOrgValue | **Field Type** string **Description** Default catalog that determines the products to be displayed on the product list page. Available in API version 64.0 and later. |
| prodDiscPricingEnabledOrgValue | **Field Type** string **Description** Indicates whether pricing is enabled (`true`) or not (`false`). The default value is `false`. |
| prodDiscProcedureOrgValue | **Field Type** string **Description** Pricing procedure that calculates the list price. |
| prodDiscQualEnabledOrgValue | **Field Type** string **Description** Indicates whether product qualification is enabled (`true`) or not (`false`). The default value is `false`. |
| prodDiscQualificationOrgValue | **Field Type** string **Description** Qualification procedure that determines product eligibility. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a ProductDiscoverySettings component.

			

```
<ProductDiscoverySettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <enableGuidedSelling>true</enableGuidedSelling>
    <discoverProductsFlowNameOrgValue>revenue_products__DiscoverProducts</discoverProductsFlowNameOrgValue>
    <prodDiscPricingEnabledOrgValue>true</prodDiscPricingEnabledOrgValue>
    <prodDiscQualEnabledOrgValue>true</prodDiscQualEnabledOrgValue>
    <prodDiscProcedureOrgValue>PricingProcedure</prodDiscProcedureOrgValue>
    <prodDiscQualificationOrgValue>QualificationProcedure</prodDiscQualificationOrgValue>
    <prodDiscBrowseContextDefOrgValue>BrowseContextDefinition</prodDiscBrowseContextDefOrgValue>
</ProductDiscoverySettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>ProductDiscovery</members>
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

=== ARTICLE: meta_productspecificationrectype.htm ===
---
page_id: meta_productspecificationrectype.htm
title: ProductSpecificationRecType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productspecificationrectype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationRecType

Represents the association of a product
			specification type with record types defined on the Product object. The product
			specification record type also determines if the product specification is sold
			commercially or not.

	
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

	

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type
			and inherits its fullName field. 

	

## File Suffix and Directory Location

		
		

ProductSpecificationRecType components have the suffix .productSpecificationRecType and are stored in the productSpecificationRecTypes folder.

	

	

## Version

		
		

ProductSpecificationRecType components are available in API version 60.0 and later.

	

	

## Special Access Rules

Ensure Product Catalog Management is enabled to
				access this metadata type.

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

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
| isCommercial | **Field Type** boolean **Description** Required. Indicates whether the product is sold commercially (`true`) or not (`false`). The default value is `true`. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for the product specification record type, which is defined when the metadata component is created. |
| productSpecificationType | **Field Type** string **Description** Required. Product specification type that's associated with the record type. This field is unique within your organization. |
| recordType | **Field Type** string **Description** Required. Custom record type of Product2 object. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a ProductSpecificationRecType component.

			

```

<ProductSpecificationRecType xmlns="http://soap.sforce.com/2006/04/metadata">
    <masterLabel>sample</masterLabel>
   <recordType>Product2.Offer</recordType>
   <productSpecificationType>Placeholder</productSpecificationType>
   <isCommercial>true</isCommercial>
</ProductSpecificationRecType>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```

<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>ProductSpecificationRecType</name>
    </types>
    <types>
        <members>*</members>
        <name>ProductSpecificationType</name>
    </types>
    <types>
        <members>Product2.Offer</members>
        <name>RecordType</name>
    </types>
    <version>68.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: meta_productspecificationtype.htm ===
---
page_id: meta_productspecificationtype.htm
title: ProductSpecificationType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productspecificationtype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationType

Represents the specification types in your org that define products
			with unique terminology specific to the industry.

	
			

#### Important

 Where possible, we changed noninclusive terms to align with our
				company value of Equality. We maintained certain terms to avoid any effect on
				customer implementations. 

		

	

## Parent Type

			 This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type
			and inherits its fullName field. 

	

## File Suffix and Directory Location

		
		

ProductSpecificationType components have the suffix .productSpecificationType and are stored in the productSpecificationTypes folder.

	

	

## Version

		
		

ProductSpecificationType components are available in API version 60.0 and later.

	

	

## Special Access Rules

		
		

Ensure Product Catalog Management is enabled to access this metadata type.

	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** Required. Description of the product specification type. |
| masterLabel | **Field Type** string **Description** Required. A user-friendly name for the product specification record type, which is defined when the metadata component is created. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a ProductSpecificationType component.

			

```

<ProductSpecificationType xmlns="http://soap.sforce.com/2006/04/metadata">
    <masterLabel>sample</masterLabel>
    <description>Sample Description</description>
</ProductSpecificationType>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```

<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>ProductSpecificationType</name>
    </types>
    <version>68.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*`
				(asterisk) in the package.xml manifest file. For information
				about using the manifest file, see [Deploying and Retrieving Metadata with the Zip File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

=== ARTICLE: pcm_metadata_api_parent.htm ===
---
page_id: pcm_metadata_api_parent.htm
title: Product Catalog Management Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pcm_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[ProductCatalogManagementSettings](./meta_productcatalogmanagementsettings.htm.md)**  

Represents the settings for Product Catalog 			Management.

- 
**[ProductSpecificationType](./meta_productspecificationtype.htm.md)**  

Represents the specification types in your org that define products 			with unique terminology specific to the industry.

- 
**[ProductSpecificationRecType](./meta_productspecificationrectype.htm.md)**  

Represents the association of a product 			specification type with record types defined on the Product object. The product 			specification record type also determines if the product specification is sold 			commercially or not.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: pcm_overview.htm ===
---
page_id: pcm_overview.htm
title: Product Catalog Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pcm_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management

Manage an entire product portfolio with components such as attributes, product
  classifications, simple and bundled products, and rules.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Management |

  

 

- 
**[Product Catalog Management Standard Objects](./pcm_std_objects_parent.htm.md)**  

The Product Catalog Management data model provides objects and fields to manage   products, rules, and catalogs.

- 
**[Product Catalog Management Fields on Standard Objects](./product_catalog_management_fields_on_standard_objects.htm.md)**  

Product Catalog Management adds standard and custom fields to some          standard Salesforce objects. These fields are available only in orgs where Product Catalog          Management is enabled. This object is available in API version 60.0 and       later.

- 
**[Product Catalog Management Business APIs](./product_catalog_management_business_api.htm.md)**  

Use primitive APIs of Product Catalog Management that serve catalog definitions to         users or applications.

- 
**[Product Catalog Management Metadata API Types](./pcm_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Product Catalog Management Tooling API Objects](./pcm_tooling_api_parent.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata.

#### See Also

- [*Salesforce Help*: Product Catalog Management Permission Set
       Licenses](https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_catalog_management_permission_set_licenses.htm&type=5&language=en_US)

- [*Salesforce Help*: User Permissions for Product Catalog Management](https://help.salesforce.com/s/articleView?id=sf.product_catalog_user_permissions_for_product_catalog_management.htm&language=en_US)

=== ARTICLE: pcm_parent.htm ===
---
page_id: pcm_parent.htm
title: Product Catalog Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pcm_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management

Create and manage a product catalog with components, such as attributes, product
  classifications, simple and bundled products, and rules.

- 
**[Product Catalog Management](./pcm_overview.htm.md)**  

Manage an entire product portfolio with components such as attributes, product   classifications, simple and bundled products, and rules.

- 
**[Product Discovery](./product_discovery_overview.htm.md)**  

Product Discovery provides a hierarchical catalog browsing experience to identify   suitable products with text-based and faceted search.

=== ARTICLE: pcm_std_objects_parent.htm ===
---
page_id: pcm_std_objects_parent.htm
title: Product Catalog Management Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pcm_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Standard Objects

The Product Catalog Management data model provides objects and fields to manage
  products, rules, and catalogs.

- 
**[AttributeCategory](./sforce_api_objects_attributecategory.htm.md)**  

       Represents a logical grouping of attributes that can be reused while defining          products. Attribute Categories are used for searching and managing product attributes. For          example, the "Mobile Handset Properties" category has color, storage and make model, and          size attributes. This object is available in API version 60.0 and later. 

- 
**[AttributeCategoryAttribute](./sforce_api_objects_attributecategoryattribute.htm.md)**  

       Represents a relationship between an attribute category and the attribute          definition. This object is available in API version 60.0 and later. 

- 
**[AttrPicklistExcludedValue](./sforce_api_objects_attrpicklistexcludedvalue.htm.md)**  

       Represents the excluded picklist values for a product classification          attribute or a product attribute definition. This object is available in API version       61.0 and later.

- 
**[ProductAttributeDefinition](./sforce_api_objects_productattributedefinition.htm.md)**  

       Represents the relationship between a product and its attributes. This       object is available in API version 60.0 and later. 

- 
**[ProductCategoryDisqual](./sforce_api_objects_productcategorydisqual.htm.md)**  

       Represents disqualification rules for product categories. The rules determine          when the product category doesn’t qualify to be displayed to users. This object is       available in API version 60.0 and later. 

- 
**[ProductCategoryQualification](./sforce_api_objects_productcategoryqualification.htm.md)**  

       Represents qualification rules for product categories. The rules determine          when the product category qualifies to be displayed to users. This object is available       in API version 60.0 and later. 

- 
**[ProductClassification](./sforce_api_objects_productclassification.htm.md)**  

       Represents a template that holds a collection of dynamic attributes. Product          classification is used to quickly define and create multiple products that are similar yet          different. This object is available in API version 60.0 and later. 

- 
**[ProductClassificationAttr](./sforce_api_objects_productclassificationattr.htm.md)**  

Represents the relationship between a product classification and its          attributes. This is the default configuration for products based on the product          classification. This object is available in API version 60.0 and later.

- 
**[ProductComponentGrpOverride](./sforce_api_objects_productcomponentgrpoverride.htm.md)**  

       Represents override information for a Product Component Group. The          cardinality of the product component group can be overridden in the context of a product          bundle. This object is available in API version 60.0 and later. 

- 
**[ProductDisqualification](./sforce_api_objects_productdisqualification.htm.md)**  

       Represents disqualification rules for products. The rules determine when the          product doesn’t qualify to be displayed to users. The rules are based on user context.       This object is available in API version 60.0 and later. 

- 
**[ProductQualification](./sforce_api_objects_productqualification.htm.md)**  

       Represents qualification rules for products. The rules determine when the          product qualifies to be displayed to users. The rules are based on user context. This       object is available in API version 60.0 and later. 

- 
**[ProductRampSegment](./sforce_api_objects_productrampsegment.htm.md)**  

       Represents the ramp period within a ramp deal where terms, volumes, and other          commitments change over time. This object is available in API version 62.0 and       later.

- 
**[ProductRelComponentOverride](./sforce_api_objects_productrelcomponentoverride.htm.md)**  

       Represents the cardinality overrides for product components in a bundle.       This object is available in API version 60.0 and later. 

- 
**[ProductSpecificationRecType](./sforce_api_objects_productspecificationrectype.htm.md)**  

       Represents the relationship between industry-specific product specifications          and the product record type. This object is available in API version 60.0 and later. 

- 
**[ProductSpecificationType](./sforce_api_objects_productspecificationtype.htm.md)**  

       Represents the type of product specification provided by the user to make the          product terminology unique to an industry. A product specification type is associated with          a product specification record type. This object is available in API version 60.0 and       later. 

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: pcm_tooling_api_parent.htm ===
---
page_id: pcm_tooling_api_parent.htm
title: Product Catalog Management Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pcm_tooling_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata.

- 
**[ProductSpecificationType](./tooling_api_objects_productspecificationtype.htm.md)**  

       Represents the specification types in your org that define products with          unique terminology specific to the industry. This object is available in API version       60.0 and later.

- 
**[ProductSpecificationRecType](./tooling_api_objects_productspecificationrectype.htm.md)**  

       Represents the association of a product specification type with record types          defined on the Product object. The product specification record type also determines if the          product specification is sold commercially or not. This object is available in API       version 60.0 and later.

#### See Also

- [*Tooling API Developer Guide*: Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)

=== ARTICLE: product_catalog_management_api_requests.htm ===
---
page_id: product_catalog_management_api_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_api_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_business_api.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available Product Catalog Management API request
    bodies.

- 
**[Additional Fields Input](./connect_requests_product_catalog_additional_fields_input.htm.md)**  

Input representation of the additional standard or custom fields to be included in the     response.

- 
**[Bulk Product Details Input](./connect_requests_products_detail_bulk_input.htm.md)**  

Input representation of the request to retrieve the details of multiple     products.

- 
**[Catalog Input](./connect_requests_catalog_input.htm.md)**  

Input representation of the request to retrieve catalog records.

- 
**[Criteria Input](./connect_requests_criteria.htm.md)**  

Input representation of the filter criteria item request.

- 
**[Data Rounding Input](./connect_requests_data_rounding_input.htm.md)**  

Input representation of the details of the data rounding input.

- 
**[Data Row Input](./connect_requests_data_row_input.htm.md)**  

Input representation of the details of the input for a data rounding request.

- 
**[Deep Clone Input](./connect_requests_deep_clone_input.htm.md)**  

Input representation of the details of the object and associated record to be     cloned.

- 
**[Field Data Input](./connect_requests_field_data_input.htm.md)**  

Input representation of the details of the field data input.

- 
**[Filter Input](./connect_requests_filter.htm.md)**  

Input representation of the filter request.

- 
**[Include Object Input](./connect_requests_include_object_input.htm.md)**  

Input representation of the object to include in the response.

- 
**[Index Configuration Collection Input](./connect_requests_index_configuration_collection_input.htm.md)**  

Input representation of the collection of index configurations.

- 
**[Index Configuration Input](./connect_requests_index_configuration_input.htm.md)**  

Input representation of the request to persist the index configuration.

- 
**[Index Setting Input](./connect_requests_index_setting_input.htm.md)**  

Input representation of the index setting.

- 
**[Options Input](./connect_requests_options.htm.md)**  

Reserved for internal use.

- 
**[Order Input](./connect_requests_order.htm.md)**  

Input representation of the sort order item request.

- 
**[Product Classification Details Input](./connect_requests_product_classification_details_input.htm.md)**  

Input representation of the request to fetch details of product classification records,     including their attributes and attribute categories.

- 
**[Product Classification List Input](./connect_requests_product_classification_list_input.htm.md)**  

Input representation of the request to retrieve a list of product classification     records.

- 
**[Product Input](./connect_requests_product_input.htm.md)**  

Input representation of a product in the catalog.

- 
**[Product Variants Input](./connect_requests_product_variants_input.htm.md)**  

Input representation of the request to retrieve the variation products associated with     parent variant products.

- 
**[Related Object Filters Input](./connect_requests_related_object_filters_input.htm.md)**  

Input representation of the request to filter related objects.

- 
**[Related Object Node Input](./connect_requests_related_object_node_input.htm.md)**  

Input representation of the details of a related object node.

- 
**[Related Records Input](./connect_requests_related_records_input.htm.md)**  

Input representation of the request to retrieve related ProductRampSegment or     ProductUsageGrant records for Product2 object.

- 
**[Run-time Catalog Snapshot Input](./connect_requests_runtime_catalog_snapshot_input.htm.md)**  

Input representation of the details of a run-time catalog snapshot for     deployment.

- 
**[Setting Input](./connect_requests_setting_input.htm.md)**  

Input representation of the details of the index setting.

- 
**[Snapshot Deployment Input](./connect_requests_snapshot_deployment_input.htm.md)**  

Input representation of the request to deploy a run-time catalog snapshot.

- 
**[Sort Input](./connect_requests_sort.htm.md)**  

Input representation of the sort request.

=== ARTICLE: product_catalog_management_api_resources.htm ===
---
page_id: product_catalog_management_api_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_api_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_business_api.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Product Catalog Management API resources.

- 
**[Bulk Product Details (POST)](./connect_resources_product_catalog_bulk_product_details.htm.md)**  

Retrieve details for multiple products.

- 
**[Catalog List (POST)](./connect_resources_get_catalogs.htm.md)**  

Retrieve, search, filter, or sort catalog     records.

- 
**[Catalog By ID (GET)](./connect_resources_get_catalogs_by_ID.htm.md)**  

Retrieve details of catalog records based on a catalog       ID.

- 
**[Categories List (GET)](./connect_resources_get_categories.htm.md)**  

Retrieve the root-level categories of a catalog based       on a catalog ID, or subcategories based on a parent category. You can also search, filter, or       sort the categories.

- 
**[Category By ID (GET)](./connect_resources_get_category_by_ID.htm.md)**  

Retrieve details of individual category records based       on a category ID.

- 
**[Deep Clone (POST)](./connect_resources_deep_clone.htm.md)**  

Copy related records of an object along with the main product       record.

- 
**[Index Configuration Collection (GET, PUT)](./connect_resources_index_configuration.htm.md)**  

Retrieve the saved index configurations. Additionally, you can persist       the index configuration.

- 
**[Index Setting (GET, PATCH)](./connect_resources_get_index_settings.htm.md)**  

Fetch and update settings related to indexing and     search.

- 
**[Product Classification Details (POST)](./connect_resources_product_classification.htm.md)**  

Retrieve the details for a list of product classification       records.

- 
**[Product Classification List (POST)](./connect_resources_product_classification_list.htm.md)**  

Retrieve a list of product classification records. You can also     search, filter, or sort the product classifications.

- 
**[Product Details (GET)](./connect_resources_get_product_by_ID.htm.md)**  

Retrieve details of individual product records or a       bundle based on a product ID.

- 
**[Product Related Records List (POST)](./connect_resources_related_records.htm.md)**  

Retrieve related ProductRampSegment or ProductUsageGrant records for       Product2 object.

- 
**[Products List (POST)](./connect_resources_get_products.htm.md)**  

Retrieve products. You can also search, filter, or sort       the products.

- 
**[Product Variants (POST)](./connect_resources_product_variants.htm.md)**  

Retrieve the variation product associated with one or more parent       variant products.

- 
**[Snapshot Collection (GET)](./connect_resources_snapshot_get.htm.md)**  

Retrieve the created snapshots and snapshot indexes.

- 
**[Snapshot Deployment (POST)](./connect_resources_snapshot_deploy.htm.md)**  

Create indexes for a snapshot. Indexes improve search results and make       it easier to find products at run time through search terms.

- 
**[Snapshot Index Error (GET)](./connect_resources_get_index_errors.htm.md)**  

Get the count and details of the errors that occurred during the       indexing process.

- 
**[Unit of Measure Info (GET)](./connect_resources_unit_of_measure_info.htm.md)**  

Get details about the unit of measure for a specific set of       records.

- 
**[Unit of Measure Rounded Data (POST)](./connect_resources_unit_of_measure_rounded_data.htm.md)**  

Round off and scale decimal data for a specific set of     fields.

=== ARTICLE: product_catalog_management_api_responses.htm ===
---
page_id: product_catalog_management_api_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_api_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_business_api.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available Product Catalog Management API response
    bodies.

- 
**[Attribute Category](./connect_responses_attribute_category_output.htm.md)**  

Output representation of the attribute category.

- 
**[Attribute Definition](./connect_responses_attribute_definition_output.htm.md)**  

Output representation of the attribute definition.

- 
**[Attribute Picklist](./connect_responses_attribute_picklist_output.htm.md)**  

Output representation of the attribute picklist.

- 
**[Attribute Picklist Value](./connect_responses_attribute_picklist_value_output.htm.md)**  

Output representation of the attribute picklist value.

- 
**[Bulk Unit Of Measure Info](./connect_responses_bulk_unit_of_measure_info_output.htm.md)**  

Output representation of the details of the unit of measure records along with error     details.

- 
**[Data Rounding](./connect_responses_data_rounding_output.htm.md)**  

Output representation of the data rounding response.

- 
**[Data Row](./connect_responses_data_row_output.htm.md)**  

Output representation of the details of a data row.

- 
**[Catalog Output](./connect_responses_catalog_output.htm.md)**  

Output representation of the catalog definition.

- 
**[Catalogs Output](./connect_responses_catalogs_output.htm.md)**  

Output representation of the retrieved catalog result.

- 
**[Categories Output](./connect_responses_categories_output.htm.md)**  

Output representation of the retrieved categories result.

- 
**[Category Output](./connect_responses_category_output.htm.md)**  

Output representation of the category definition.

- 
**[Deep Clone Error](./connect_responses_deep_clone_error.htm.md)**  

Output representation of the error details related to the deep clone request.

- 
**[Deep Clone Record Response](./connect_responses_deep_clone_record_response.htm.md)**  

Output representation of the details of the cloned related records.

- 
**[Deep Clone Response](./connect_responses_deep_clone_response.htm.md)**  

Output representation of the details of the cloned record.

- 
**[Error Output](./connect_responses_epc_error_output.htm.md)**  

Output representation of the error details.

- 
**[Facet Value](./connect_responses_facet_value_output.htm.md)**  

Output representation of the facet values found in the search result.

- 
**[Field Data](./connect_responses_field_data_output.htm.md)**  

Output representation of the field data.

- 
**[Fields Info](./connect_responses_fields_info_output.htm.md)**  

Output representation of the metadata fields in an object.

- 
**[Index Configuration Collection](./connect_responses_index_configuration_collection_output.htm.md)**  

Output representation of the collection of index configuration details.

- 
**[Index Configuration Field](./connect_responses_index_configuration_field_output.htm.md)**  

Output representation of the details of the index-configured field.

- 
**[Index Configurations Update](./connect_responses_index_configurations_update_output.htm.md)**  

Output representation of the updated index configuration.

- 
**[Index Error](./connect_responses_index_error_output.htm.md)**  

Output representation of the error details related to an index.

- 
**[Index Setting](./connect_responses_index_setting_output.htm.md)**  

Output representation of the retrieved index settings.

- 
**[Index Setting Update](./connect_responses_index_setting_patch_output.htm.md)**  

Output representation of the details of the updated index setting.

- 
**[Invalid Related Object Node](./connect_responses_invalid_related_object_node_output.htm.md)**  

Output representation of the invalid related object node with details of     errors.

- 
**[Metadata](./connect_responses_metadata_output.htm.md)**  

Output representation of the metadata details for objects.

- 
**[Object Info](./connect_responses_object_info_output.htm.md)**  

Output representation of the object details along with its fields.

- 
**[Product Catalog Management Error](./connect_responses_p_c_m_error_output.htm.md)**  

Output representation that contains error details, including error codes and     messages.

- 
**[Product Classification](./connect_responses_product_classification_output.htm.md)**  

Output representation of the product classification details.

- 
**[Product Classification Details](./connect_responses_product_classification_details_output.htm.md)**  

Output representation that contains the details of a single product classification,     including its attributes and categories.

- 
**[Product Classification Details Collection](./connect_responses_product_classification_details_collection_output.htm.md)**  

Output representation that contains a collection of product classification details along     with any processing errors.

- 
**[Product Classification List Collection](./connect_responses_product_classification_list_collection_output.htm.md)**  

Output representation that contains a collection of product classification records     along with any processing errors.

- 
**[Product Component Group](./connect_responses_product_component_group_output.htm.md)**  

Output representation of the product component group.

- 
**[Product](./connect_responses_product_output.htm.md)**  

Output representation of the product definition.

- 
**[Product Related Component](./connect_responses_product_related_component_output.htm.md)**  

Output representation of the product-related component.

- 
**[Product Selling Model](./connect_responses_product_selling_model_output.htm.md)**  

Output representation of the definition of the product selling model.

- 
**[Product Selling Model Option](./connect_responses_product_selling_model_option_output.htm.md)**  

Output representation of the definition of the product selling model option.

- 
**[Product Specification Type](./connect_responses_product_specification_type_output.htm.md)**  

Output representation of the product specification type.

- 
**[Products](./connect_responses_products_output.htm.md)**  

Output representation of the list of retrieved products.

- 
**[Product Variants](./connect_responses_product_variants_output.htm.md)**  

Output representation of the variation products associated with the specified parent     variant products.

- 
**[Related Object Records](./connect_responses_related_object_records_output.htm.md)**  

Output representation of the related records for a specified record ID and related object     API name.

- 
**[Related Records](./connect_responses_related_records_output.htm.md)**  

Output representation of the list of relatedObject records for a specified record     ID.

- 
**[Related Records List](./connect_responses_related_records_list_output.htm.md)**  

Output representation of the list of related records.

- 
**[Search Facet](./connect_responses_search_facet_output.htm.md)**  

Output representation of the details of the faceted search.

- 
**[Setting](./connect_responses_setting_output.htm.md)**  

Output representation of the setting that’s used in indexing.

- 
**[Setting Metadata](./connect_responses_setting_metadata_output.htm.md)**  

Output representation of the metadata associated with a setting.

- 
**[Snapshot](./connect_responses_snapshot_output.htm.md)**  

Output representation of the list of active snapshots.

- 
**[Snapshot Collection](./connect_responses_snapshot_collection_output.htm.md)**  

Output representation of the retrieved snapshot collection.

- 
**[Snapshot Deployment](./connect_responses_snapshot_deployment_output.htm.md)**  

Output representation of the snapshot deployment.

- 
**[Snapshot Index](./connect_responses_snapshot_index_output.htm.md)**  

Output representation of the snapshot index of a run-time catalog.

- 
**[Snapshot Index Error](./connect_responses_snapshot_index_error_output.htm.md)**  

Output representation of the error details related to a snapshot index.

- 
**[Snapshot Index Info](./connect_responses_snapshot_index_info_output.htm.md)**  

Output representation of the details of a snapshot index.

- 
**[Snapshot Index Log](./connect_responses_snapshot_index_log_output.htm.md)**  

Output representation of a snapshot index log.

- 
**[Status](./connect_responses_status.htm.md)**  

Output representation of the status of the request.

- 
**[Unit of Measure Error](./connect_responses_unit_of_measure_error_output.htm.md)**  

Output representation of the details of errors encountered during the processing of the     Unit of Measure API request.

- 
**[Unit of Measure Info](./connect_responses_unit_of_measure_info_output.htm.md)**  

Output representation of the details of a unit of measure record.

- 
**[Unit of Measure Status](./connect_responses_unit_of_measure_status.htm.md)**  

Output representation of the status of the Unit of Measure API request.

=== ARTICLE: product_catalog_management_business_api.htm ===
---
page_id: product_catalog_management_business_api.htm
title: Product Catalog Management Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_business_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Business APIs

Use primitive APIs of Product Catalog Management that serve catalog definitions to
        users or applications.

        
            

This table lists the available Product Catalog Management resources.

            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                        
                            

                            

                        

                    

                
| Resource | Description |
| --- | --- |
| [`/connect/pcm/catalogs`](./connect_resources_get_catalogs.htm.md) (POST) | Retrieve, search, filter, or sort catalog records. |
| [`/connect/pcm/catalogs/catalogId`](./connect_resources_get_catalogs_by_ID.htm.md) (GET) | Retrieve details of catalog records based on a catalog ID. |
| [`/connect/pcm/catalogs/catalogId/categories`](./connect_resources_get_categories.htm.md) (GET) | Retrieve the root-level categories of a catalog based on a catalog ID, or subcategories based on a parent category. You can also search, filter, or sort the categories. |
| [`/connect/pcm/categories/categoryId`](./connect_resources_get_category_by_ID.htm.md) (GET) | Retrieve details of individual category records based on a category ID. |
| [`/connect/pcm/products`](./connect_resources_get_products.htm.md) (POST) | Retrieve products. You can also search, filter, or sort the products. |
| [`/connect/pcm/products/productId`](./connect_resources_get_product_by_ID.htm.md) (GET) | Retrieve details of individual product records or a bundle based on a product ID. |
| [`/revenue/product-catalog-management/product-classifications/details`](./connect_resources_product_classification.htm.md) (POST) | Retrieve the details for a list of product classification records. |
| [`/revenue/product-discovery/products/recommendations`](./connect_resources_product_recommendations.htm.md) (POST) | Get a list of recommended products based on your underlying business rules. |
| [`/revenue/product-configurator/rules/actions/execute`](./connect_resources_config_rules.htm.md) (POST) | This API is used in Product Catalog Management to disable rules, get product recommendations, and get message rules. |
| [`/connect/pcm/products/bulk`](./connect_resources_product_catalog_bulk_product_details.htm.md) (POST) | Retrieve details for multiple products. |
| [`/connect/pcm/products/variants`](./connect_resources_product_variants.htm.md) (POST) | Retrieve the variation product associated with one or more parent variant products. |
| `[/connect/pcm/index/configurations](./connect_resources_index_configuration.htm.md)` (GET, PUT) | Retrieve the saved index configurations. Additionally, you can persist the index configuration. |
| [`/connect/pcm/relatedRecords/entityName`](./connect_resources_related_records.htm.md) (POST) | Retrieve related ProductRampSegment or ProductUsageGrant records for Product2 object. |
| [`/connect/pcm/index/snapshots`](./connect_resources_snapshot_get.htm.md) (GET) | Retrieve the created snapshots and snapshot indexes. |
| [`/connect/pcm/index/deploy`](./connect_resources_snapshot_deploy.htm.md) (POST) | Create indexes for a snapshot. Indexes improve search results and make it easier to find products at run time through search terms. |
| [`/connect/pcm/index/setting`](./connect_resources_get_index_settings.htm.md) (GET, PATCH) | Fetch and update settings related to indexing and search. |
| [`/connect/pcm/index/error`](./connect_resources_get_index_errors.htm.md) (GET) | Get the count and details of the errors that occurred during the indexing process. |
| [`/connect/pcm/deep-clone`](./connect_resources_deep_clone.htm.md) (POST) | Copy related records of an object along with the main product record. |
| [`/connect/pcm/unit-of-measure/info`](./connect_resources_unit_of_measure_info.htm.md) (GET) | Get details about the unit of measure for a specific set of records. |
| [`/connect/pcm/unit-of-measure/rounded-data`](./connect_resources_unit_of_measure_rounded_data.htm.md) (POST) | Round off and scale decimal data for a specific set of fields. |

        

    

- 
**[Resources](./product_catalog_management_api_resources.htm.md)**  

Learn more about the available Product Catalog Management API resources.

- 
**[Request Bodies](./product_catalog_management_api_requests.htm.md)**  

Learn more about the available Product Catalog Management API request     bodies.

- 
**[Response Bodies](./product_catalog_management_api_responses.htm.md)**  

Learn more about the available Product Catalog Management API response     bodies.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: product_catalog_management_fields_on_attributedefinition.htm ===
---
page_id: product_catalog_management_fields_on_attributedefinition.htm
title: Product Catalog Management Fields on Attribute Definition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_attributedefinition.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Attribute Definition

 Standard and custom fields extend the standard Attribute Definition
         object for use in Product Catalog Management.

      

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

                  

                  
               

            
| Field | Details |
| --- | --- |
| DataType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort **Description** The data type of the attribute definition. Valid values are: `Checkbox` `Currency`—Available in API version 61.0 and later `Date` `Datetime` `Number` `Percent`—Available in API version 61.0 and later `Picklist` `Text` |

      

      
   

#### See Also

- [Attribute Definition](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_attributedefinition.htm)

=== ARTICLE: product_catalog_management_fields_on_product2.htm ===
---
page_id: product_catalog_management_fields_on_product2.htm
title: Product Catalog Management Fields on Product2
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product2.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product2

Standard and custom fields extend the standard Product2 object for
         use in Product Catalog Management to represent information about products.

      

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
| Based On | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the product classification from which this product inherits. This field is a relationship field. **Relationship Name** BasedOn **Relationship Type** Lookup **Refers To** ProductClassification |
| Help Text | **Type** textarea **Properties** Create, Nillable, Update **Description** The help text that appears at runtime for the product. The maximum size is 32,000 alphanumeric characters. The help text can include these special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”. |
| Availability Date | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the product is available. |
| CanRamp | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the product’s terms, volumes, and other commitments can be ramped (true) at run time or not (false) The default value is `false`. |
| Discontinued Date | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the product is discontinued. |
| End Of Life Date | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time after which a product isn’t supported, ordered, or maintained. |
| Specification Type | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The type of product specification that’s being created. |
| DecompositionScope | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The number of fulfillment order line items that must be generated. Available in API version 61.0 and later. Valid values are: `Account` `Bundle` `Order` `OrderLineItem` |
| FulfillmentQtyCalcMethod | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Determines whether the quantity of fulfillment order line items must always be one or must be aggregated from the source line items. Available in API version 61.0 and later. Valid values are: `Aggregate` `AlwaysOne` |
| UsageModelType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of usage model for a product or service. Anchor is the main subscription product or service. Pack is the add-on product or service that grants additional usage resources for consumption. Available in API version 62.0 and later. Valid values are: `Anchor` `Pack` |

      

   

#### See Also

- [Product2](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_product2.htm)

=== ARTICLE: product_catalog_management_fields_on_product_catalog.htm ===
---
page_id: product_catalog_management_fields_on_product_catalog.htm
title: Product Catalog Management Fields on Product Catalog
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_catalog.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Catalog 

Standard and custom fields extend the standard Product Catalog object
         for use in Product Catalog Management. This object is available in API version 60.0
      and later.

      

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

: 

                  

               

            
| Field | Details |
| --- | --- |
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** A unique ID associated with the catalog. The maximum size is 80 alphanumeric characters. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the catalog that's used during design time. The maximum size is 255 alphanumeric characters. |
| EffectiveEndDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date after which the product catalog is unavailable to end users. |
| EffectiveStartDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date on which the product catalog is available to end users. |
| CatalogType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The category of an entry in the catalog. Possible values are: `Sales` `ServiceProcess`—Service Process The default value is `Sales`. |

      

      
   

#### See Also

- [Product Catalog](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productcatalog.htm)

=== ARTICLE: product_catalog_management_fields_on_product_category.htm ===
---
page_id: product_catalog_management_fields_on_product_category.htm
title: Product Catalog Management Fields on Product Category
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_category.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Category

Standard and custom fields extend the standard Product Category
         object for use in Product Catalog Management.

      

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
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** A unique ID associated with the catalog. The maximum size is 80 alphanumeric characters. |
| IsNavigational | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the category or subcategory is shown in the menu as a navigational breadcrumb (`true`) or not (`false`). Available in API version 62.0 and later. The default value is `false`. |

      

   

#### See Also

- [Product Category](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productcategory.htm)

=== ARTICLE: product_catalog_management_fields_on_product_component_group.htm ===
---
page_id: product_catalog_management_fields_on_product_component_group.htm
title: Product Catalog Management Fields on Product Component Group
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_component_group.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Component Group

      Standard and custom fields extend the standard Product Component Group object
         for use in Product Catalog Management.

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ParentGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The parent product component group in a nested group hierarchy for the same parent product. Available in API version 62.0 and later. This field is a relationship field. **Relationship Name** ParentGroup **Refers To** ProductComponentGroup |

      

   

#### See Also

- [Product Component Group](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productcomponentgroup.htm)

=== ARTICLE: product_catalog_management_fields_on_product_related_component.htm ===
---
page_id: product_catalog_management_fields_on_product_related_component.htm
title: Product Catalog Management Fields on Product Related Component
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_related_component.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Related Component

      Standard and custom fields extend the standard Product Related Component
         object for use in Product Catalog Management.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ChildProductClassificationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The child product classification that's associated with a product. This field is a relationship field. **Relationship Name** ChildProductClassification **Refers To** ProductClassification |
| QuoteVisibility | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the product-related component to display as a quote line item in the Transaction Line Editor and the quote document. The default value is Always. Possible values are: Always Transaction Line Editor Only Quote Document Only Never |

      

   

#### See Also

- [Product Related Component](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productrelatedcomponent.htm)

=== ARTICLE: product_catalog_management_fields_on_product_relationship_type.htm ===
---
page_id: product_catalog_management_fields_on_product_relationship_type.htm
title: Product Catalog Management Fields on Product Relationship Type
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_relationship_type.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Relationship Type

      Standard and custom fields extend the standard Product Relationship Type
         object for use in Product Catalog Management.

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AssociatedProductRoleCat | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The role that the associated component plays in the relationship. Valid values are: `BundleComponent`— The associated product is part of a bundle. `ClassificationComponent`— The associated component is a product classification. Available in API version 61.0 and later |

      

   

#### See Also

- [Product Relationship Type](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productrelationshiptype.htm)

=== ARTICLE: product_catalog_management_fields_on_product_selling_model_option.htm ===
---
page_id: product_catalog_management_fields_on_product_selling_model_option.htm
title: Product Catalog Management Fields on Product Selling Model Option
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_product_selling_model_option.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_catalog_management_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Product Selling Model Option

Standard and custom fields extend the standard Product Selling Model
         Option object for use in Product Catalog Management. This object is available in API
      version 60.0 and later.

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

                  

               

            
| Field | Details |
| --- | --- |
| IsDefault | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates the default product selling model for a product. Setting a product selling model as default is optional. A product can only have one default product selling model. The default value is `false`. |

      

      
   

#### See Also

- [Product Selling Model Option](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_productsellingmodeloption.htm)

=== ARTICLE: product_catalog_management_fields_on_standard_objects.htm ===
---
page_id: product_catalog_management_fields_on_standard_objects.htm
title: Product Catalog Management Fields on Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_catalog_management_fields_on_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Catalog Management Fields on Standard Objects

Product Catalog Management adds standard and custom fields to some
         standard Salesforce objects. These fields are available only in orgs where Product Catalog
         Management is enabled. This object is available in API version 60.0 and
      later.

- 
**[Product Catalog Management Fields on Attribute Definition](./product_catalog_management_fields_on_attributedefinition.htm.md)**  

 Standard and custom fields extend the standard Attribute Definition          object for use in Product Catalog Management.

- 
**[Product Catalog Management Fields on Product2](./product_catalog_management_fields_on_product2.htm.md)**  

Standard and custom fields extend the standard Product2 object for          use in Product Catalog Management to represent information about products.

- 
**[Product Catalog Management Fields on Product Catalog](./product_catalog_management_fields_on_product_catalog.htm.md)**  

Standard and custom fields extend the standard Product Catalog object          for use in Product Catalog Management. This object is available in API version 60.0       and later.

- 
**[Product Catalog Management Fields on Product Category](./product_catalog_management_fields_on_product_category.htm.md)**  

Standard and custom fields extend the standard Product Category          object for use in Product Catalog Management.

- 
**[Product Catalog Management Fields on Product Component Group](./product_catalog_management_fields_on_product_component_group.htm.md)**  

       Standard and custom fields extend the standard Product Component Group object          for use in Product Catalog Management.

- 
**[Product Catalog Management Fields on Product Related Component](./product_catalog_management_fields_on_product_related_component.htm.md)**  

       Standard and custom fields extend the standard Product Related Component          object for use in Product Catalog Management.

- 
**[Product Catalog Management Fields on Product Relationship Type](./product_catalog_management_fields_on_product_relationship_type.htm.md)**  

       Standard and custom fields extend the standard Product Relationship Type          object for use in Product Catalog Management.

- 
**[Product Catalog Management Fields on Product Selling Model Option](./product_catalog_management_fields_on_product_selling_model_option.htm.md)**  

Standard and custom fields extend the standard Product Selling Model          Option object for use in Product Catalog Management. This object is available in API       version 60.0 and later.

=== ARTICLE: product_discovery_apex_reference.htm ===
---
page_id: product_discovery_apex_reference.htm
title: Product Discovery Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Discovery Apex Reference

Use built-in Apex classes and interfaces grouped by namespace.

- 
**[runtime_industries_cpq Namespace](./apex_namespace_runtime_industries_cpq.htm.md)**  

The runtime_industries_cpq namespace provides classes and methods to search products or     to manage products, catalogs, and categories.

=== ARTICLE: product_discovery_api_requests.htm ===
---
page_id: product_discovery_api_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_api_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available Product Discovery API request bodies.

- 
**[Additional Fields Input](./connect_requests_additional_fields_input.htm.md)**  

Input representation of the additional standard or custom fields to include in the     response.

- 
**[Bulk Product Details Input](./connect_requests_bulk_product_details_input.htm.md)**  

Input representation of the request to retrieve details of multiple products.

- 
**[Catalog Details Input](./connect_requests_catalog_details_input.htm.md)**  

Input representation of the request to get the catalog details.

- 
**[Catalog List Input](./connect_requests_catalog_list_input.htm.md)**  

Input representation of the request to get a list of catalogs.

- 
**[Category Details Input](./connect_requests_category_details_input.htm.md)**  

Input representation of the request to get category details.

- 
**[Category List Input](./connect_requests_category_list_input.htm.md)**  

Input representation of the request to get a list of categories.

- 
**[Context Data Input](./connect_requests_context_data_input.htm.md)**  

Input representation of the context data.

- 
**[Guided Selection Input](./connect_requests_guided_selection_input.htm.md)**  

Input representation of the guided selection details.

- 
**[Guided Selection Search Term Input](./connect_requests_guided_selection_search_term_input.htm.md)**  

Input representation of the search terms of a guided selection.

- 
**[Filter Criteria Input](./connect_requests_filter_criteria_input.htm.md)**  

Input representation of the criteria to filter records based on supported     properties.

- 
**[Filter Input](./connect_requests_filter_input.htm.md)**  

Input representation of the request to filter records.

- 
**[Product Details Input](./connect_requests_product_details_input.htm.md)**  

Input representation of the request to get product details.

- 
**[Product Data Input](./connect_requests_product_data_input.htm.md)**  

Input representation of the product details such as the product ID and product selling     model ID.

- 
**[Product List Input](./connect_requests_product_list_input.htm.md)**  

Input representation of the request to retrieve a list of products.

- 
**[Product Recommendation Input](./connect_requests_product_recommendation_input.htm.md)**  

Input representation of the details of a request to get product     recommendations.

- 
**[Products Search Input](./connect_requests_search_products_input.htm.md)**  

Input representation of the request to search products.

- 
**[QOC Qualification](./connect_requests_qoc_qualification_input.htm.md)**  

Input representation of the qualification request.

- 
**[Related Object Filter Input](./connect_requests_related_object_filter_input.htm.md)**  

Input representation of the request to filter records of a related object.

- 
**[User Context Input](./connect_requests_user_context_input.htm.md)**  

Input representation of the details with the user context.

=== ARTICLE: product_discovery_api_resources.htm ===
---
page_id: product_discovery_api_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_api_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Product Discovery API resources.

- 
**[Catalog Details (POST)](./connect_resources_catalog_details.htm.md)**  

Get catalog details for a specified catalog ID. This API is a       composite API for Product Discovery.

- 
**[Catalog List (POST)](./connect_resources_catalog_list.htm.md)**  

Get a paginated list of catalogs. This API is a composite API for       Product Discovery.

- 
**[Categories List (POST)](./connect_resources_categories_list.htm.md)**  

Get a list of categories and subcategories of a specified catalog.       This API is a composite API for Product Discovery.

- 
**[Category Details (POST)](./connect_resources_category_details.htm.md)**  

Get details of a category for a specified category ID. This API is a       composite API for Product Discovery.

- 
**[Bulk Product Details (POST)](./connect_resources_bulk_product_details.htm.md)**  

Retrieve details for multiple products. This API is a composite API       for Product Discovery.

- 
**[Global Search (POST)](./connect_resources_global_search.htm.md)**  

Retrieves a list of products based on a search query or search term.       This API is a composite API for Product Discovery.

- 
**[Guided Selection (POST)](./connect_resources_guided_product_selection.htm.md)**  

Retrieve a list of products based on the response identifier or search       terms of a guided selection. Guided selection captures user requirements to show suitable       products.

- 
**[Product Details (POST)](./connect_resources_product_details.htm.md)**  

Get product details, such as attributes, hierarchy, or cardinality,       for a specified product ID. This API is a composite API for Product     Discovery.

- 
**[Product Recommendations (POST)](./connect_resources_product_recommendations.htm.md)**  

Get a list of recommended products based on your underlying business       rules.

- 
**[Products List (POST)](./connect_resources_products_list.htm.md)**  

Get a list of products for a specified catalog, category, or       subcategory. This API is a composite API for Product Discovery.

- 
**[Qualification (POST)](./connect_resources_cpq_qualification.htm.md)**  

Run the qualification procedure on a list of product IDs. This API       is a composite API for Product Discovery.

=== ARTICLE: product_discovery_api_responses.htm ===
---
page_id: product_discovery_api_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_api_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available Product Discovery API response bodies.

- 
**[API Status](./connect_responses_api_status_output.htm.md)**  

Output representation of the API status.

- 
**[Catalog Details](./connect_responses_product_discovery_catalog_output.htm.md)**  

Output representation of the details of a catalog definition.

- 
**[Category Details](./connect_responses_product_discovery_category_output.htm.md)**  

Output representation of the details of a category.

- 
**[Bulk Product Details](./connect_responses_cpq_base_bulk_details_output.htm.md)**  

Output representation of the response that contains the details of multiple     products.

- 
**[CPQ Base Details](./connect_responses_cpq_base_details_output.htm.md)**  

Output representation of the catalog, category, or product details based on the     request.

- 
**[CPQ Base List](./connect_responses_cpq_base_list_output.htm.md)**  

Output representation of the list of catalogs, categories, or products based on the     request.

- 
**[CPQ Message](./connect_responses_cpq_message_output.htm.md)**  

Output representation of the API messages.

- 
**[Facet Value](./connect_responses_facet_value.htm.md)**  

Output representation of the facet values found in the search result.

- 
**[Guided Selection](./connect_responses_guided_selection_output.htm.md)**  

Output representation of the details of a guided selection.

- 
**[Guided Selection Search Term](./connect_responses_guided_selection_search_term_output.htm.md)**  

Output representation of the search term details for a guided selection.

- 
**[Pricing Model](./connect_responses_pricing_model_output.htm.md)**  

Output representation of the details of the pricing model.

- 
**[Product Classification](./connect_responses_product_discovery_product_classification_output.htm.md)**  

Output representation of the details of a product classification.

- 
**[Product Configuration Rule Details](./connect_responses_product_configuration_rule_details_output.htm.md)**  

Output representation of the product configuration rule details.

- 
**[Product Configuration Rules](./connect_responses_product_configuration_rules_output.htm.md)**  

Output representation of the details of the product configuration rules.

- 
**[Product Prices](./connect_responses_product_prices_output.htm.md)**  

Output representation of the details of the product prices.

- 
**[Product Quantity](./connect_responses_product_quantity_output.htm.md)**  

Output representation of the details of the quantity constraints and current quantity for     a product in the product discovery context.

- 
**[Product Recommendation Errors](./connect_responses_product_recommendation_errors_output.htm.md)**  

Output representation of the details of the errors encountered during the processing of     the Product Recommendations API request.

- 
**[Product Recommendations](./connect_responses_product_recommendation_output.htm.md)**  

Output representation of the fetched product recommendations.

- 
**[Product Selling Model Option](./connect_responses_product_discovery_product_selling_model_option_output.htm.md)**  

Output representation of the product selling model option component.

- 
**[Product Selling Model](./connect_responses_product_discovery_product_selling_model_output.htm.md)**  

Product Selling Model Component output representation

- 
**[Product Specification Record Type](./connect_responses_product_specification_record_type_output.htm.md)**  

Output representation of the details of the product specification record     type.

- 
**[Product Specification Type](./connect_responses_product_discovery_product_specification_type_output.htm.md)**  

Output representation of the details of the product specification type.

- 
**[Promotion Details](./connect_responses_promotion_output.htm.md)**  

Output representation of the details of applicable promotions.

- 
**[Proration Policy](./connect_responses_proration_policy_output.htm.md)**  

Output representation of the details of the proration policy component.

- 
**[Qualification Context](./connect_responses_qualification_context_output.htm.md)**  

Output representation of the details about the product qualification.

- 
**[Recommended Products](./connect_responses_recommended_products_output.htm.md)**  

Output representation of the list of recommended products.

- 
**[Search Products Facet](./connect_responses_search_products_facet.htm.md)**  

Output representation of the details of the faceted search.

- 
**[User Context](./connect_responses_user_context_output.htm.md)**  

Output representation of the user context details.

=== ARTICLE: product_discovery_business_apis.htm ===
---
page_id: product_discovery_business_apis.htm
title: Product Discovery Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_business_apis.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Discovery Business APIs

Use the Product Discovery Business APIs, which are composite APIs, to search products
        or to discover catalogs, products, and categories during the product browsing
        experience.

        

This table lists the available Product Discovery resources.

        

                
                
                
                    
                        

                        

                    

                

                
                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                    
                        

                        

                    

                

            
| Resource | Description |
| --- | --- |
| [`/connect/cpq/catalogs/catalogId`](./connect_resources_catalog_details.htm.md) (POST) | Get catalog details for a specified catalog ID. This API is a composite API for Product Discovery. |
| [`/connect/cpq/catalogs`](./connect_resources_catalog_list.htm.md) (POST) | Get a paginated list of catalogs. This API is a composite API for Product Discovery. |
| [`/connect/cpq/categories`](./connect_resources_categories_list.htm.md) (POST) | Get a list of categories and subcategories of a specified catalog. This API is a composite API for Product Discovery. |
| [`/connect/cpq/categories/categoryId`](./connect_resources_category_details.htm.md) (POST) | Get details of a category for a specified category ID. This API is a composite API for Product Discovery. |
| [`/connect/cpq/qualification`](./connect_resources_cpq_qualification.htm.md) (POST) | Run the qualification procedure on a list of product IDs. This API is a composite API for Product Discovery. |
| [`/connect/cpq/products/search`](./connect_resources_global_search.htm.md) (POST) | Retrieves a list of products based on a search query or search term. This API is a composite API for Product Discovery. |
| [`/connect/cpq/products/productId`](./connect_resources_product_details.htm.md) (POST) | Get product details, such as attributes, hierarchy, or cardinality, for a specified product ID. This API is a composite API for Product Discovery. |
| [`/connect/cpq/products`](./connect_resources_products_list.htm.md) (POST) | Get a list of products for a specified catalog, category, or subcategory. This API is a composite API for Product Discovery. |
| [`/connect/cpq/products/bulk`](./connect_resources_bulk_product_details.htm.md) (POST) | Retrieve details for multiple products. This API is a composite API for Product Discovery. |
| [`/connect/cpq/products/guided-selection`](./connect_resources_guided_product_selection.htm.md) (POST) | Retrieve a list of products based on the response identifier or search terms of a guided selection. Guided selection captures user requirements to show suitable products. |
| [`/revenue/product-discovery/products/recommendations`](./connect_resources_product_recommendations.htm.md) (POST) | Get a list of recommended products based on your underlying business rules. |

    

- 
**[Resources](./product_discovery_api_resources.htm.md)**  

Learn more about the available Product Discovery API resources.

- 
**[Request Bodies](./product_discovery_api_requests.htm.md)**  

Learn more about the available Product Discovery API request bodies.

- 
**[Response Bodies](./product_discovery_api_responses.htm.md)**  

Learn more about the available Product Discovery API response bodies.

=== ARTICLE: product_discovery_flow_metadata_api.htm ===
---
page_id: product_discovery_flow_metadata_api.htm
title: Flow for Product Discovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Product Discovery

Represents the metadata associated with a flow. With Flow, you can create an
    application that takes users through a series of pages to query and update the records in the
    database. You can also run logic and provide branching capability based on user input to build
    dynamic applications.

    

## FlowActionCall

      
      

Product Discovery exposes additional actionType values for the FlowActionCall metadata
        type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
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
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values for Product Discovery are: `findProducts`—Search for the products from a catalog, category, or subcategory by using the specified search term. `GetProducts`—Get products from the specified catalog, category, or subcategory, including product qualification and pricing details. `GetProductDetails`—Get details such as attributes, hierarchy, and cardinality for the specified product. `executeQualificationProcedure`—Execute a qualification procedure, which returns the qualification status for the specified products. `getCatalogDetails`—Get details of a catalog record. `getCatalogs`—Get a list of catalog records. `getCategories`—Get the list of categories associated with a catalog record. `getCategoryDetails`—Get details of a category record. `getMultipleProductDetails`—Get product details for a list of products. `searchPrdctWithGuidedSelection`—Use guided product selection to search for products. `getRecommendedProducts`—Retrieve a list of recommended products for a quote or order by using the Constraint Rule Engine. |

=== ARTICLE: product_discovery_invocable_actions_parent.htm ===
---
page_id: product_discovery_invocable_actions_parent.htm
title: Product Discovery Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Discovery Standard Invocable Actions

Use the standard invocable actions available with Product Discovery to find and retrieve
  product, category, and catalog details. Additionally, execute a qualification procedure, and
  search products with guided selection.

- 
**[Find Products Action](./actions_obj_find_products.htm.md)**  

Search for the products from a catalog, category, or subcategory by 			using the specified search term.

- 
**[Execute Qualification Procedure Action](./actions_obj_execute_qualification_procedure.htm.md)**  

Execute a qualification procedure, which returns the qualification             status for the specified products.

- 
**[Get Catalogs Action](./actions_obj_get_catalogs.htm.md)**  

Get a list of catalog records.

- 
**[Get Catalog Details Action](./actions_obj_get_catalog_details.htm.md)**  

Get details of a catalog record.

- 
**[Get Categories Action](./actions_obj_get_categories.htm.md)**  

Get the list of categories associated with a catalog         record.

- 
**[Get Category Details Action](./actions_obj_get_category_details.htm.md)**  

Get details of a category record.

- 
**[Get Multiple Product Details Action](./actions_obj_get_multiple_product_details.htm.md)**  

Get product details for a list of products.

- 
**[Get Products Action](./actions_obj_get_products.htm.md)**  

Get products from the specified catalog, category, or subcategory, 			including product qualification and pricing details.

- 
**[Get Product Details Action](./actions_obj_get_product_details.htm.md)**  

Get details such as attributes, hierarchy, and cardinality for the 			specified product.

- 
**[Search Product with Guided Selection Action](./actions_obj_search_products_with_guided_selection.htm.md)**  

Use guided product selection to search for         products.

- 
**[Get Product Recommendations Action](./actions_obj_get_recommendation_products.htm.md)**  

Retrieve a list of recommended products for a quote or order by using 			the Constraint Rule Engine.

=== ARTICLE: product_discovery_metadata_api_parent.htm ===
---
page_id: product_discovery_metadata_api_parent.htm
title: Product Discovery Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: product_discovery_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Discovery Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Product Discovery](./product_discovery_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that takes users through a series of pages to query and update the records in the     database. You can also run logic and provide branching capability based on user input to build     dynamic applications.

- 
**[ProductDiscoverySettings](./meta_productdiscoverysettings.htm.md)**  

Represents the settings for Product 		Discovery.

=== ARTICLE: product_discovery_overview.htm ===
---
page_id: product_discovery_overview.htm
title: Product Discovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Product Discovery

Product Discovery provides a hierarchical catalog browsing experience to identify
  suitable products with text-based and faceted search.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Management |

  

 

- 
**[Product Discovery Business APIs](./product_discovery_business_apis.htm.md)**  

Use the Product Discovery Business APIs, which are composite APIs, to search products         or to discover catalogs, products, and categories during the product browsing         experience.

- 
**[Product Discovery Standard Invocable Actions](./product_discovery_invocable_actions_parent.htm.md)**  

Use the standard invocable actions available with Product Discovery to find and retrieve   product, category, and catalog details. Additionally, execute a qualification procedure, and   search products with guided selection.

- 
**[Product Discovery Apex Reference](./product_discovery_apex_reference.htm.md)**  

Use built-in Apex classes and interfaces grouped by namespace.

- 
**[Product Discovery Metadata API Types](./product_discovery_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

#### See Also

- [*Salesforce Help*: Configure Product Discovery Settings](https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_product_discovery.htm&type=5&language=en_US)

- [*Salesforce Help*: Invoke Qualification Procedures During Product
       Discovery](https://help.salesforce.com/s/articleView?id=sf.product_catalog_invoke_qualification_procedures_during_product_discovery.htm&language=en_US)

=== ARTICLE: sforce_api_objects_attributecategory.htm ===
---
page_id: sforce_api_objects_attributecategory.htm
title: AttributeCategory
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_attributecategory.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttributeCategory

      Represents a logical grouping of attributes that can be reused while defining
         products. Attribute Categories are used for searching and managing product attributes. For
         example, the "Mobile Handset Properties" category has color, storage and make model, and
         size attributes. This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The unique code for the attribute category. The maximum size is 80 alphanumeric characters. The code can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the attribute category that's used only during design time. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the attribute category was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the attribute category was last viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The unique name of the attribute category. The maximum length is 80 characters (of any type). |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the attribute category. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[AttributeCategoryFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[AttributeCategoryHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[AttributeCategoryShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_attributecategoryattribute.htm ===
---
page_id: sforce_api_objects_attributecategoryattribute.htm
title: AttributeCategoryAttribute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_attributecategoryattribute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttributeCategoryAttribute

      Represents a relationship between an attribute category and the attribute
         definition. This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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
| AttributeCategoryId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the attribute category that the attribute is associated with. The ID is unique within the organization. This field is a relationship field. **Relationship Name** AttributeCategory **Relationship Type** Lookup **Refers To** AttributeCategory |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the attribute definition associated with the attribute category. The ID is unique within the organization. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the attribute category attribute was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the attribute category attribute was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** A unique name for the attribute. The maximum length is 80 characters (of any type). |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the attribute category attribute. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[AttributeCategoryAttributeFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[AttributeCategoryAttributeHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[AttributeCategoryAttributeShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_attrpicklistexcludedvalue.htm ===
---
page_id: sforce_api_objects_attrpicklistexcludedvalue.htm
title: AttrPicklistExcludedValue
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_attrpicklistexcludedvalue.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AttrPicklistExcludedValue

      Represents the excluded picklist values for a product classification
         attribute or a product attribute definition. This object is available in API version
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
      

      

      

## Special Access Rules

Product Catalog Management must be enabled to
            access this object.

      

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
| AttributeId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the product classification attribute or the product attribute definition of the picklist data type. This field is a polymorphic relationship field. **Relationship Name** Attribute **Relationship Type** Lookup **Refers To** ProductAttributeDefinition, ProductClassificationAttr |
| AttributePicklistValueId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the attribute picklist value that’s excluded in the product classification attribute or product attribute definition. This field is a relationship field. **Relationship Name** AttributePicklistValue **Relationship Type** Lookup **Refers To** AttributePicklistValue |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the excluded attribute picklist value was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the excluded attribute picklist value was last viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the excluded attribute picklist value. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the excluded attribute picklist value. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[AttrPicklistExcludedValueFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[AttrPicklistExcludedValueHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[AttrPicklistExcludedValueShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productattributedefinition.htm ===
---
page_id: sforce_api_objects_productattributedefinition.htm
title: ProductAttributeDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productattributedefinition.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductAttributeDefinition

      Represents the relationship between a product and its attributes. This
      object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| AttributeCategoryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The ID of the attribute category assigned to the parent object. This field is a relationship field. **Relationship Name** AttributeCategory **Relationship Type** Lookup **Refers To** AttributeCategory |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the attribute associated with the product. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| AttributeNameOverride | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name to display for the attribute when shown for this object. This display name overrides the name on the attribute. For example, the attribute "Color" is overridden to display as "Laptop Color." The maximum size is 255 alphanumeric characters. The name can include these special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”. |
| DefaultValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The default value for the product attribute. The attribute value can be changed. This default overrides the default value set for a picklist for the attribute. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** A description of the attribute definition. The maximum size is 32,000 alphanumeric characters. The description can include these special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”. |
| DisplayType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type to display data for the selected data type. Possible values are: `CheckBox`—Checkbox `ComboBox`—Combobox `Date` `Datetime`—Date Time `Number` `RadioButton`—Radio Button `Slider`—Available in API version 61.0 and later `Text` `Toggle` |
| HelpText | **Type** textarea **Properties** Create, Nillable, Update **Description** The help text to display when end users are configuring this attribute. This field overrides the help text defined for the attribute itself. |
| IsHidden | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if this product attribute is hidden from end users in the run time (`true`) or not (`false`). The default value is `false`. |
| IsPriceImpacting | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this attribute dictates the price of a product (`true`) or not (`false`). The default value is `false`. |
| IsReadOnly | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the attribute is read-only for users in the run time (`true`) or not (`false`). The default value is `false`. |
| IsRequired | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this attribute requires a value when assigned to a parent object (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product attribute was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product attribute was last viewed. |
| MaximumCharacterCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of characters that can be entered for an attribute value. |
| MaximumValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum value that can be entered as an attribute value. |
| MinimumCharacterCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The minimum number of characters that can be entered for an attribute value. |
| MinimumValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The minimum value that can be entered as an attribute value. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the product attribute. |
| OverriddenProductAttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The ID associated with the overridden product attribute definition. This field is a relationship field. **Relationship Name** OverriddenProductAttributeDefinition **Relationship Type** Lookup **Refers To** ProductAttributeDefinition |
| OverrideContextId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The ID associated with the root product record in a bundle. This field is a polymorphic relationship field. **Relationship Name** OverrideContext **Relationship Type** Lookup **Refers To** Product2 |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the product attribute definition. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| Product2Id | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The product ID associated with the product attribute definition. This field is a relationship field. **Relationship Name** Product2 **Relationship Type** Lookup **Refers To** Product2 |
| ProductClassificationAttributeId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the attribute assigned to the product classification. This field is a relationship field. **Relationship Name** ProductClassificationAttribute **Relationship Type** Lookup **Refers To** ProductClassificationAttr |
| Sequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The display sequence of the attribute when configuring the product during run time. |
| Status | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The lifecycle state of the product attribute definition. Valid values are: `Active` `Draft` `Inactive` The default value is `Draft`. |
| StepValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The increment or decrement by which a slider's value changes as the user adjusts the product attribute value. Available in API version 61.0 and later. |
| ValueDescription | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the value assigned to this attribute. This field takes on the value description from the attribute definition. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductAttributeDefinitionFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductAttributeDefinitionHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductAttributeDefinitionShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productcategorydisqual.htm ===
---
page_id: sforce_api_objects_productcategorydisqual.htm
title: ProductCategoryDisqual
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productcategorydisqual.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductCategoryDisqual

      Represents disqualification rules for product categories. The rules determine
         when the product category doesn’t qualify to be displayed to users. This object is
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
         `search()`, 
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Product Catalog Management must be enabled to access this object.

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| CategoryId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The product category associated with the product disqualification record. This field is a relationship field. **Relationship Name** Category **Relationship Type** Lookup **Refers To** ProductCategory |
| EffectiveFromDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date from which the disqualification rule for the product category comes into effect. |
| EffectiveToDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date to which the disqualification rule for the product category ceases to be in effect. |
| IsDisqualified | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the product category is disqualified (`true`) or not (`false`) based on the disqualification rules. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product category disqualification record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product category disqualification record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product category disqualification record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product category disqualification record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| Reason | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The reason to disqualify the product category. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductCategoryDisqualFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductCategoryDisqualHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductCategoryDisqualShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productcategoryqualification.htm ===
---
page_id: sforce_api_objects_productcategoryqualification.htm
title: ProductCategoryQualification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productcategoryqualification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductCategoryQualification

      Represents qualification rules for product categories. The rules determine
         when the product category qualifies to be displayed to users. This object is available
      in API version 60.0 and later. 

      

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

         
         

Product Catalog Management must be enabled to access this object.

      

      

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
| CategoryId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The product category associated with the category qualification record. This field is a relationship field. **Relationship Name** Category **Relationship Type** Lookup **Refers To** ProductCategory |
| EffectiveFromDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date from which the qualification rule for the product category comes into effect. |
| EffectiveToDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date to which the qualification rule for the product category ceases to be in effect. |
| IsQualified | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the product category is qualified (`true`) or not (`false`) based on the qualification rules. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product category qualification record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product category qualification record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product category qualification record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product category qualification record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductCategoryQualificationFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductCategoryQualificationHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductCategoryQualificationShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productclassification.htm ===
---
page_id: sforce_api_objects_productclassification.htm
title: ProductClassification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productclassification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductClassification

      Represents a template that holds a collection of dynamic attributes. Product
         classification is used to quickly define and create multiple products that are similar yet
         different. This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| Code | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** A unique code for the product classification. The maximum size is 80 alphanumeric characters. The code can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product classification record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product classification record was last viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the product classification. The maximum length is 80 characters (of any type). |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the product classification. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| Status | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The lifecycle status of the product classification. Possible values are: `Active` `Draft` `Inactive` The default value is `Draft`. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductClassificationFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductClassificationHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               
               
: Sharing rules are available for the object.

            
            
               

**[ProductClassificationShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productclassificationattr.htm ===
---
page_id: sforce_api_objects_productclassificationattr.htm
title: ProductClassificationAttr
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productclassificationattr.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductClassificationAttr

Represents the relationship between a product classification and its
         attributes. This is the default configuration for products based on the product
         classification. This object is available in API version 60.0 and later.

      

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

Product Catalog Management must be enabled to
            access this object.

      

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

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

                  

            

            
| Field | Details |
| --- | --- |
| AttributeCategoryId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The ID of the attribute category assigned to the parent object. This field is a relationship field. **Relationship Name** AttributeCategory **Relationship Type** Lookup **Refers To** AttributeCategory |
| AttributeDefinitionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the attribute assigned to the parent object. This field is a relationship field. **Relationship Name** AttributeDefinition **Relationship Type** Lookup **Refers To** AttributeDefinition |
| AttributeNameOverride | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The overridden attribute name to display for the attribute when shown for this object. For example, "Color" overridden to "Laptop Color." |
| DefaultValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The default value of the attribute for a product based on the product classification. This value can be changed. |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of this product classification attribute definition. |
| DisplayType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type to display data for the selected data type. Valid values are: `CheckBox`—Checkbox `ComboBox`—Combobox `Date` `Datetime`—Date Time `Number` `RadioButton`—Radio Button `Slider`—Available in API version 61.0 and later `Text` `Toggle` |
| ExcludedPicklistValues | **Type** textarea **Properties** Create, Nillable, Update **Description** The picklist values excluded from the attribute picklist. This field ensures that the product classification attribute only has valid values. |
| HelpText | **Type** textarea **Properties** Create, Nillable, Update **Description** The help text to display when end users are configuring this attribute. This field overrides the help text defined for the attribute itself. |
| IsHidden | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if this product attribute is hidden from end users in the run time (`true`) or not (`false`). The default value is `false`. |
| IsPriceImpacting | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this attribute dictates the price of a product (`true`) or not (`false`). The default value is `false`. |
| IsReadOnly | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the attribute is read-only for users in the run time (`true`) or not (`false`). The default value is `false`. |
| IsRequired | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this attribute requires a value when assigned to a parent object (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product classification attribute was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product classification attribute was last viewed. |
| MaximumCharacterCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of characters that can be entered for an attribute value. |
| MaximumValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum value that can be entered as an attribute value. |
| MinimumCharacterCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The minimum number of characters that can be entered for an attribute value. |
| MinimumValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The minimum value that can be entered as an attribute value. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the product classification attribute. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the product classification attribute owner. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProductClassificationId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the product classification that the attribute is associated with. This field is unique within your organization. This field is a relationship field. **Relationship Name** ProductClassification **Relationship Type** Lookup **Refers To** ProductClassification |
| Sequence | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The display sequence of the attribute when configuring the product during run time. |
| Status | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The lifecycle status of the product classification attribute. Valid values are: `Active` `Draft` `Inactive` The default value is `Draft`. |
| StepValue | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The increment or decrement by which a slider's value changes as the user adjusts the product classification attribute value. Available in API version 61.0 and later. |
| ValueDescription | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the value assigned to this attribute. This field takes on the value description from the attribute definition. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductClassificationAttrFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductClassificationAttrHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               
               
: Sharing rules are available for the object.

            
            
               

**[ProductClassificationAttrShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productcomponentgrpoverride.htm ===
---
page_id: sforce_api_objects_productcomponentgrpoverride.htm
title: ProductComponentGrpOverride
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productcomponentgrpoverride.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductComponentGrpOverride

      Represents override information for a Product Component Group. The
         cardinality of the product component group can be overridden in the context of a product
         bundle. This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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
| IsExcluded | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the product component group is excluded from the product bundle in the runtime. Excluding a group automatically excludes all child components of the group. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product component override record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product component override record was last viewed. |
| MaxBundleComponents | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of components that can be added to a group. |
| MinBundleComponents | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The minimum number of components that must be added to a group. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the overridden product component group. |
| OverrideContextId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The root bundle product in whose context the group cardinality is overridden. This field is a polymorphic relationship field. **Relationship Name** OverrideContext **Relationship Type** Lookup **Refers To** Product2 |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the product component group override record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProductComponentGroupId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the product component group record. This field is a relationship field. **Relationship Name** ProductComponentGroup **Relationship Type** Lookup **Refers To** ProductComponentGroup |

=== ARTICLE: sforce_api_objects_productdisqualification.htm ===
---
page_id: sforce_api_objects_productdisqualification.htm
title: ProductDisqualification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productdisqualification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductDisqualification

      Represents disqualification rules for products. The rules determine when the
         product doesn’t qualify to be displayed to users. The rules are based on user context.
      This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| EffectiveFromDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date from which the disqualification rule for the product comes into effect. |
| EffectiveToDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date to which the disqualification rule for the product ceases to be in effect. |
| IsDisqualified | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the product is disqualified based on the disqualification rules (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product disqualification record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product disqualification record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product disqualification record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the product disqualification record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ParentProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the immediate parent product in the product bundle hierarchy. This field is a relationship field. **Relationship Name** ParentProduct **Relationship Type** Lookup **Refers To** Product2 |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The product for which the disqualification rule is defined. This field is a relationship field. **Relationship Name** Product **Relationship Type** Lookup **Refers To** Product2 |
| Reason | **Type** textarea **Properties** Create, Nillable, Update **Description** The reason to disqualify the product. |
| RootProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the root product in the product bundle hierarchy. This field is a relationship field. **Relationship Name** RootProduct **Relationship Type** Lookup **Refers To** Product2 |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductDisqualificationFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductDisqualificationHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductDisqualificationShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productqualification.htm ===
---
page_id: sforce_api_objects_productqualification.htm
title: ProductQualification
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productqualification.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductQualification

      Represents qualification rules for products. The rules determine when the
         product qualifies to be displayed to users. The rules are based on user context. This
      object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
            access this object.

      

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

                  

            

            
| Field | Details |
| --- | --- |
| EffectiveFromDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date from which the qualification rule for the product comes into effect. |
| EffectiveToDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** The date to which the qualification rule for the product ceases to be in effect. |
| IsQualified | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the product is qualified based on the qualification rules (`true`) or not (`false`). For a product to qualify, this field should be true. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product qualification record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product qualification record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product qualification record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner of the product qualification record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ParentProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the immediate parent product in the product bundle hierarchy. This field is a relationship field. **Relationship Name** ParentProduct **Relationship Type** Lookup **Refers To** Product2 |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The product for which the qualification rule is defined. This field is a relationship field. **Relationship Name** Product **Relationship Type** Lookup **Refers To** Product2 |
| RootProductId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the root product in the product bundle hierarchy. This field is a relationship field. **Relationship Name** RootProduct **Relationship Type** Lookup **Refers To** Product2 |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductQualificationFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductQualificationHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductQualificationShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productrampsegment.htm ===
---
page_id: sforce_api_objects_productrampsegment.htm
title: ProductRampSegment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productrampsegment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductRampSegment

      Represents the ramp period within a ramp deal where terms, volumes, and other
         commitments change over time. This object is available in API version 62.0 and
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

Product Catalog Management must be enabled to
            access this object.

      

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
- 
- 
- 

: 

                  

                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| DurationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit of time within which users can try the product for free. Valid values are: `Days` `Months` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product ramp segment was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product ramp segment was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product ramp segment. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the product ramp segment. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ProductId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the product associated with the product ramp segment. This field is a relationship field. **Relationship Name** Product **Refers To** Product2 |
| ProductSellingModelId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the product selling model associated with the product ramp segment. This field is a relationship field. **Relationship Name** ProductSellingModel **Refers To** ProductSellingModel |
| SegmentType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** The time duration within the ramp deal where specific terms, volumes, and commitments are applied to the subscription product. Valid values are: `Custom` `FreeTrial` `Yearly` The default value is `Yearly`. |
| TrialDuration | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The duration within which users can try the product for free. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductRampSegmentFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductRampSegmentHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductRampSegmentShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productrelcomponentoverride.htm ===
---
page_id: sforce_api_objects_productrelcomponentoverride.htm
title: ProductRelComponentOverride
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productrelcomponentoverride.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductRelComponentOverride

      Represents the cardinality overrides for product components in a bundle.
      This object is available in API version 60.0 and later. 

      

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

Product Catalog Management must be enabled to
         access this object.

      

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
- 
- 

: 

                  

            

            
| Field | Details |
| --- | --- |
| DoesBundlePriceIncludeChild | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the bundle price includes the associated child component's price (`true`) or not (`false`). The default value is `false`. |
| IsComponentRequired | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the component is a required component in the product bundle. The default value is `false`. |
| IsDefaultComponent | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether this component is included in the product component group by default. The default value is `false`. |
| IsExcluded | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the bundle excludes the component (`true`) or not (`false`). The default value is `false`. |
| IsQuantityEditable | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the product component quantity can be edited (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product related component override record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the product related component override record was last viewed. |
| MaxQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The maximum quantity for the product component in the product bundle. |
| MinQuantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The minimum quantity for the product component in the product bundle |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the product related component override. The maximum length is 255 characters (of any type). |
| OverrideContextId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID associated with the root product in a bundle. This field is a polymorphic relationship field. **Relationship Name** OverrideContext **Relationship Type** Lookup **Refers To** Product2 |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The owner ID of the product related component override record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProductRelatedComponentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID associated with the product related component record. This field is a relationship field. **Relationship Name** ProductRelatedComponent **Relationship Type** Lookup **Refers To** ProductRelatedComponent |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The default number of child product related components. |
| QuantityScaleMethod | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The scaling method that determines how the child product quantity changes as the quantity of the parent product changes in the runtime cart. Possible values are: `Constant` `Proportional` The default value is `Proportional`. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[ProductRelComponentOverrideFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[ProductRelComponentOverrideHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
            
               

**[ProductRelComponentOverrideShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_productspecificationrectype.htm ===
---
page_id: sforce_api_objects_productspecificationrectype.htm
title: ProductSpecificationRecType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productspecificationrectype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationRecType

      Represents the relationship between industry-specific product specifications
         and the product record type. This object is available in API version 60.0 and later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Product Catalog Management must be enabled to access this object.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
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

                  

                  
                     

                     

: 

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
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the ProductSpecificationRecType object in the API. The name: must be 40 characters or fewer. can contain only underscores and alphanumeric characters. must begin with a letter. can contain only underscores and alphanumeric characters. can’t include spaces can’t end with an underscore can’t contain 2 consecutive underscores |
| IsCommercial | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the product is sold commercially (`true`) or not (`false`) |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The combined language and locale ISO code, which controls the language of the Product Specification Record Type. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label for this Product Specification Record Type value. This display value is the internal label that doesn't get translated. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix_componentName`The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| ProductSpecificationType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The product specification type that's associated with the record type. |
| RecordTypeId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The ID of the record type that's associated with the product specification type. This field is a relationship field. **Relationship Name** RecordType **Relationship Type** Lookup **Refers To** RecordType |

=== ARTICLE: sforce_api_objects_productspecificationtype.htm ===
---
page_id: sforce_api_objects_productspecificationtype.htm
title: ProductSpecificationType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_productspecificationtype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationType

      Represents the type of product specification provided by the user to make the
         product terminology unique to an industry. A product specification type is associated with
         a product specification record type. This object is available in API version 60.0 and
      later. 

      

## Supported Calls

      
      

         `create()`, 
         `delete()`, 
         `describeSObjects()`, 
         `query()`, 
         `retrieve()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

Product Catalog Management must be enabled to access this object.

      

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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
- 
- 
- 
- 
- 
- 
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

                  

            

            
| Field | Details |
| --- | --- |
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the Product Specification Type. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the Product Specification Type object in the API. The name: must be 40 characters or fewer. can contain only underscores and alphanumeric characters. must begin with a letter. can contain only underscores and alphanumeric characters. can’t include spaces can’t end with an underscore can’t contain 2 consecutive underscores In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The combined language and locale ISO code, which controls the language of the Product Specification Type. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label for this Product Specification Type value. This display value is the internal label that doesn't get translated. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix_componentName`The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |

=== ARTICLE: tooling_api_objects_productspecificationrectype.htm ===
---
page_id: tooling_api_objects_productspecificationrectype.htm
title: ProductSpecificationRecType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/tooling_api_objects_productspecificationrectype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationRecType

      Represents the association of a product specification type with record types
         defined on the Product object. The product specification record type also determines if the
         product specification is sold commercially or not. This object is available in API
      version 60.0 and later.

      
         

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
		

      

      

## Special Access Rules

Ensure Product Catalog Management is enabled to
            access this object.

      

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

: 

: 
: 

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. |
| IsCommercial | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the product is sold commercially (`true`) or not (`false`). The default value is `true`. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Language of the product specification record type instance. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label assigned to the ProductSpecificationRecType object. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |
| ProductSpecificationType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Product specification type that's associated with the record type. This field is unique within your organization. The picklist values that are available to you depend on your industry solution and permission sets. |
| RecordType | **Type** sObject **Properties** Nillable **Description** Custom record type of Product2 object. |
| RecordTypeId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. ID of the product record type associated with the product specification type. This field is unique within your organization. This field is a relationship field. **Relationship Name** RecordType **Relationship Type** Lookup **Refers To** RecordType |

=== ARTICLE: tooling_api_objects_productspecificationtype.htm ===
---
page_id: tooling_api_objects_productspecificationtype.htm
title: ProductSpecificationType
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/tooling_api_objects_productspecificationtype.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Product Catalog Management
parent_page: pcm_tooling_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ProductSpecificationType

      Represents the specification types in your org that define products with
         unique terminology specific to the industry. This object is available in API version
      60.0 and later.

      
         

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
		

      

      

## Special Access Rules

Ensure Product Catalog Management is enabled to
            access this object.

      

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
| Description | **Type** textarea **Properties** Create, Nillable, Update **Description** Description of the product specification type. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Label is **Record Type Name**. |
| Language | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Language of the product specification type instance. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Label assigned to the ProductSpecificationType object. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |

