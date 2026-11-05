# Revenue Management Developer Guide 264 — sección: Billing (parte 2/3) (175 artículos)

=== ARTICLE: connect_requests_invoice_ingestion_input.htm ===
---
page_id: connect_requests_invoice_ingestion_input.htm
title: Invoice Ingestion Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_invoice_ingestion_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Ingestion Input

Input representation of the details of the invoice to be processed. The details include
    the tax processing status, user preferences for tax callouts, and associated object graph
    representation.

        
          

**JSON example to ingest a draft invoice with a tax callout**

          
: 
            

```
{
  "invoices": [
    {
      "shouldCalculateTax": true,
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "CreateInvoice",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refContact",
            "record": {
              "attributes": {
                "type": "Contact",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "@{refAccount.Id}",
              "billToContactId": "@{refContact.Id}",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "Sample Invoice",
              "uniqueIdentifier": "5873af8f-f007-4aa0-9e3d-53a08c3f59de"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": 7.25,
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "kl",
              "description": "Associated tax line.",
              "invoiceLineId": "@{refInvoiceLine1.id}"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine2.id}",
              "description": "Associated tax line."
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

- 
- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlation​Id` | String | Splunk correlation ID to track the messages that are related to the request and are logged in Splunk by the different services involved in the request. If the ID isn’t specified, the service creates a random Universally Unique Identifier (UUID). | Optional | 63.0 |
| `graph` | [Object Graph Input](./connect_requests_object_graph_input.htm.md) | Graph that represents the invoice structure for invoice ingestion or generation. The supported Graph attribute types for invoice ingestion are Account, Contact, Invoice, InvoiceLine, InvoiceLineTax, and InvoiceAddressGroup. See [Graph Record for Invoice Ingestion](./connect_requests_graph_record_input.htm.md). | Required | 63.0 |
| `should​CalculateTax` | Boolean | Indicates whether the estimated tax must be calculated for the ingested invoice (`true`) or not (`false`). The default value is `false`. | Optional | 63.0 |
| `taxCalculation​Status` | String | Status of the tax calculation, which is saved on the invoice line. Valid values are: `Estimated` `Pending` `Posted` The default value is `Pending`. | Optional | 63.0 |

=== ARTICLE: connect_requests_invoice_input.htm ===
---
page_id: connect_requests_invoice_input.htm
title: Invoice Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_invoice_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Input

Input representation of the details of the billing
    schedule.

**JSON example**

: 

```
{
  "accountId": "001SG00000mYtRWYA0",
  "action": "Posted",
  "billingScheduleIds": [
    "44bSG000000CVeMYAW"
  ],
  "billingTransactionId": "801SG00000mYtaXYAS",
  "correlationId": null,
  "invoiceDate": "2024-01-12",
  "targetDate": "2024-01-12"
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account record to create the invoices for. | Required if the `billing​ScheduleIds` or `billing​TransactionId` property isn’t specified. | 63.0 |
| `action` | String | Type of invoice to be created. Valid values are: `Draft` `Posted` | Required | 62.0 |
| `billing​ScheduleIds` | String[] | List of billing schedule IDs that’s used to create the invoices. You can specify a maximum of 200 billing schedules. | Required if the `accountId` or `billing​TransactionId` property isn’t specified. | 62.0 |
| `billing​TransactionId` | String | ID of the billing transaction record, which is the order ID, to create the invoices for. | Required if the `accountId` or `billing​ScheduleIds` property isn’t specified. | 63.0 |
| `correlation​Id` | String | Property that’s tagged against the published `InvoiceProcessedEvent` event, if specified. | Optional | 62.0 |
| `invoice​Date` | String | Stamping date of the invoice in ISO 8601 format. | Required | 62.0 |
| `target​Date` | String | Date in ISO 8601 format used to decide the billing periods that are included to create invoices. | Required | 62.0 |

=== ARTICLE: connect_requests_invoice_input_for_ingestion.htm ===
---
page_id: connect_requests_invoice_input_for_ingestion.htm
title: Invoice Input for Ingestion
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_invoice_input_for_ingestion.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Input for Ingestion

Input representation of the details of the invoice that must be generated for or
    ingested into Billing.

    
      
        
          

**
JSON example to ingest a draft invoice with a tax callout**

          
: 
            

```
{
  "invoices": [
    {
      "shouldCalculateTax": true,
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "CreateInvoice",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refContact",
            "record": {
              "attributes": {
                "type": "Contact",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "@{refAccount.Id}",
              "billToContactId": "@{refContact.Id}",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "Sample Invoice",
              "uniqueIdentifier": "5873af8f-f007-4aa0-9e3d-53a08c3f59de"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": 7.25,
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "kl",
              "description": "Associated tax line.",
              "invoiceLineId": "@{refInvoiceLine1.id}"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine2.id}",
              "description": "Associated tax line."
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to ingest a draft invoice without a tax callout**

          
: 
            

```
{
  "invoices": [
    {
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "123",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "TestExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "@{refAccount.Id}",
              "billToContactId": "003xx000004Wk8qAAC",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "testInvoice",
              "uniqueIdentifier": "c76011a1-e113-49d9-9c54-3b5c68950ada"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": 7.25,
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "kl",
              "description": "description for tax Line",
              "invoiceLineId": "@{refInvoiceLine1.id}"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine2.id}",
              "description": "description for tax Line"
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to ingest posted invoices**

          
: 
            

```
{
  "invoices": [
    {
      "taxCalculationStatus": "Posted",
      "graph": {
        "graphId": "123",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "001SG00000njpF3YAI",
              "billToContactId": "003xx000004Wk8qAAC",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Posted",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "Sample Invoice",
              "uniqueIdentifier": "9994b2c4-c0c3-47c3-806f-ae6e1f16bac3"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine1.id}",
              "description": "Associated tax line."
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to generate invoices from debit memos**

          
: 
            

```
{
  "invoices": [
    {
      "shouldCalculateTax": true,
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "CreateInvoice",
        "records": [
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "accountId": "001SB00001V3RxNYAV",
              "billToContactId": "003xx000004WhUQAA0",
              "referenceEntityId": "4DmAAC000008UP70BM",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "dueDate": "2024-12-19",
              "description": "Sample Invoice"
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
| `invoices` | [Invoice Ingestion Input](./connect_requests_invoice_ingestion_input.htm.md)[] | List of invoices to be generated or ingested, enabling the submission and processing of multiple invoices in a single request. This API supports one invoice per request. To send 25 requests at a time, see the [Composite Batch request](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/requests_composite_batch.htm). | Required | 63.0 |

=== ARTICLE: connect_requests_invoice_preview_input.htm ===
---
page_id: connect_requests_invoice_preview_input.htm
title: Invoice Preview Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_invoice_preview_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Preview Input

Input representation of the details of the billing transaction that the preview invoices
    are generated for.

**JSON example**

: 

```
{
    "billingTransactionId": "801Z600000004LoIAI",
    "numberOfBillingPeriods": 2,
    "previewDate": "2024-12-04"
}
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​TransactionId` | String | ID of the record to generate the preview invoices for. | Required | 63.0 |
| `numberOf​BillingPeriods` | Integer | Number of billing periods that the invoice preview is generated for. If unspecified, the default value is `2`. | Optional | 64.0 |
| `preview​Date` | String | The date on which the preview invoice is generated. For the first invoice, the preview date is the target date for generating the invoice. For the second invoice, the target date is calculated based on the preview date and the minimum billing frequency of the transactions. The default value is the current date. | Optional | 63.0 |

=== ARTICLE: connect_requests_line_item_input.htm ===
---
page_id: connect_requests_line_item_input.htm
title: Line Item Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_line_item_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Line Item Input

Input representation of the details of the line item for tax calculation.

**JSON example**

: 

```
{
  "lineItems": [
    {
      "quantity": 1,
      "amount": 100,
      "taxCode": "TX0001",
      "productCode": "Y0001",
      "productSKU": "PRES-RX-12896745",
      "description": "New Product",
      "effectiveDate": "2022-03-09T10:30:41.000Z",
      "lineNumber": "5TVxx0000004C92GAE",
      "addresses": {
        "shipFrom": {
          "street": "123 Alaskan Way",
          "city": "Seattle",
          "state": "WA",
          "country": "US",
          "postalCode": "98101",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "shipTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "soldTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "billTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        }
      }
    }
  ]
}
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [Addresses Input](./connect_requests_addresses_input.htm.md) | Address types that specify different locations associated with the transaction of the line item. | Optional | 62.0 |
| `amount` | Double | Total amount for the line item. | Required | 62.0 |
| `description` | String | Description of the line item. | Optional | 62.0 |
| `effectiveDate` | String | Date that tax rules are applicable from. This property value overrides the global effective date. | Optional | 62.0 |
| `legalEntity` | String | Legal entity that's related to the tax treatment. | Optional | 63.0 |
| `lineNumber` | String | Unique identifier for the line item. | Required | 62.0 |
| `productCode` | String | Product code of the line item according to the tax treatment rules of the tax engine. | Optional | 62.0 |
| `productId` | String | ID of the product. | Optional | 63.0 |
| `productSKU` | String | Unique identifier of a product that can be used to identify products that are exempted from tax. | Optional | 64.0 |
| `quantity` | Double | Quantity of the line item. | Required | 62.0 |
| `taxCode` | String | Tax code of the line item according to the tax treatment rules of the tax engine. | Optional | 62.0 |
| `unitPrice` | Double | Unit price of the product. | Optional | 63.0 |

=== ARTICLE: connect_requests_on_demand_doc_gen_input.htm ===
---
page_id: connect_requests_on_demand_doc_gen_input.htm
title: On-Demand Document Generation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_on_demand_doc_gen_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# On-Demand Document Generation Input

Input representation of the details to generate a comprehensive on-demand document for
    specified record types.

**JSON example**

: 

```
{
  "recordId": "3ttasd98776266777",
  "shouldForceRegenerate": true,
  "documentTemplateId": "0694x000000XyzABC",
  "documentTitle": "DOC-00000012",
  "tokenData": "{\"InvoiceLines\":{\"StartDate\":\"02/21/2025\",\"IsUsageBasedInvoiceLine\":false,\"UnitPrice\":\"$7.99\",\"ProductName\":\"Mouse\",\"UsageProductId\":\"01tSG00000BHFPSYA5\",\"Subtotal\":\"$7.99\",\"Quantity\":\"1\",\"Tax\":\"$0.00\",\"Id\":\"5TVSG000000DU3V4AW\",\"CurrencyIsoCode\":\"USD\",\"EndDate\":\"02/21/2025\"},\"NetCreditsApplied\":\"$0.00\",\"CompanyEmail\":\"rsamantaray@salesforce.com\",\"CompanyState\":\"CA\",\"DocumentNumber\":\"DOC-000000001\",\"SubTotal\":\"$7.99\",\"CompanyStreet\":\"1 Market St\",\"CompanyName\":\"260.1\",\"TotalAmnt\":\"$7.99\",\"TotalTax\":\"$0.00\",\"InvoiceDueDate\":\"10/08/2025\",\"CompanyPostalCode\":\"94105\",\"InvoiceDate\":\"09/08/2025\",\"CompanyCity\":\"San Francisco\",\"CompanyCountry\":\"US\",\"AccountName\":\"Sonia BAT Account\"}"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `documentTemplateId` | String | Document template ID to use for PDF generation. The document template must be active with UsageType as `INVOICE` If you don't specify this value, the system auto-resolves by using the default template. | Optional | 66.0 |
| `documentTitle` | String | Custom title for the generated document. If you don't specify a value, the value is auto-generated. | Optional | 66.0 |
| `recordId` | String | Record ID of the object the document is generated for. You can specify invoice ID only. | Required | 66.0 |
| `shouldForceRegenerate` | Boolean | Indicates whether to regenerate the document (`true`) or not (`false`). If set to `true`, this API generates a document, replacing any existing ones. If set to `false`, this API skips the generation of document if invoice already has an associated document. The default value is `false`. | Optional | 66.0 |
| `tokenData` | String | Token data to generate the document. | Optional | 66.0 |

=== ARTICLE: connect_requests_payment_line_apply_input.htm ===
---
page_id: connect_requests_payment_line_apply_input.htm
title: Payment Line Apply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_payment_line_apply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Apply Input

Input representation of the payment line details. This representation
      covers details on allocation of a payment to a specific invoice line. It also provides
      additional context through optional fields such as associated account and effective
    date.

**JSON example**

: 

```
{
  "appliedToId": "3ttR000000001IkIAI",
  "amount": 10,
  "effectiveDate": "2020-08-11T07:53:15.000Z",
  "comments": "Apply payment",
  "associatedAccountId": "001R00000060AyuIAE"
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount that's applied. The amount must be less than the invoice line and payment balance. | Required | 64.0 |
| `applied​ToId` | String | ID of the invoice line that this payment is applied to. Specify the IDs for these records. Invoice Invoice Line | Required | 64.0 |
| `associated​AccountId` | String | ID of the associated account. | Optional | 64.0 |
| `comments` | String | Comments that you can add to the payment line application. | Optional | 64.0 |
| `effective​Date` | String | Date from which the payment line application takes effect. | Optional | 64.0 |

=== ARTICLE: connect_requests_payment_line_unapply_input.htm ===
---
page_id: connect_requests_payment_line_unapply_input.htm
title: Payment Line Unapply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_payment_line_unapply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Unapply Input

Input representation of the payment line details. This representation covers fields that
    you can specify to revert a payment line application to their preapplication state.

**JSON example**

: 

```
{
  "effectiveDate": "2025-05-22T11:30:25.000Z",
  "comments": "Unapply payment"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `comments` | String | Comments that you can add when you revert a payment line application. | Optional | 64.0 |
| `effective​Date` | String | Date from when the reversal of the payment line application is in effect. | Optional | 64.0 |

=== ARTICLE: connect_requests_payment_run_batch_filter_criteria_input.htm ===
---
page_id: connect_requests_payment_run_batch_filter_criteria_input.htm
title: Payment Run Batch Filter Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_payment_run_batch_filter_criteria_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Run Batch Filter Criteria Input

Input representation of the filter criteria for an invoice batch run. This representation
    covers the criteria and sequence for filtering payment run details. It specifies the field and
    object names, comparison operations, and values to be used for filtering.

**JSON example**

: 
            

```

  "filterCriteria": [
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "1",
      "criteriaSequence": 1
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "2",
      "criteriaSequence": 2
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "3",
      "criteriaSequence": 3
    }
  ]
```

          

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `criteriaSequence` | Integer | Sequence that's used to filter the payment run details. | Required | 64.0 |
| `fieldName` | String | Name of the field that this filter is applicable for. Valid value is `PaymentRunMatchingValue`. | Required | 64.0 |
| `objectName` | Object | Name of the object that the filter is applicable for. Valid value is `PaymentScheduleItem`. | Required | 64.0 |
| `operation` | String | Operation that's used for comparison. Valid values are: `Equals` `InList` `NotEquals` | Required | 64.0 |
| `value` | String | Value that's used for the filter criteria. | Required | 64.0 |

=== ARTICLE: connect_requests_payment_scheduler_input.htm ===
---
page_id: connect_requests_payment_scheduler_input.htm
title: Payment Batch Scheduler Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_payment_scheduler_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Batch Scheduler Input

Input representation of the details of the request to create a payment scheduler. This
    representation sets the rules and timing for a payment scheduler, including match types, dates,
    frequency, and filter criteria.

    
      
        
          

**JSON example**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
  "schedulerName": "Payment Scheduler",
  "startDate": "2022-01-01",
  "endDate": "2022-12-31",
  "preferredTime": "02:05:00.000",
  "frequencyCadence": "Monthly",
  "recursEveryMonthOnDay": "28",
  "criteriaMatchType": "MatchAny",
  "status": "Active",
  "filterCriteria": [
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "1",
      "criteriaSequence": 1
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "2",
      "criteriaSequence": 2
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "3",
      "criteriaSequence": 3
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
| `criteria​MatchType` | String | Match type for the criteria of the payment scheduler. Valid values are: `Match Any` `Match None` | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `endDate` | String | End date of the payment scheduler. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `frequency​Cadence` | String | Frequency cadence of the payment scheduler. Valid values are: `Once` `Daily` `Weekly` `Monthly` | Required | 64.0 |
| `filter​Criteria` | [Payment Run Batch Filter Criteria Input](./connect_requests_payment_run_batch_filter_criteria_input.htm.md) | List of criteria that are used to filter the payment run details. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `preferredTime` | String | Preferred time for the payment scheduler run. | Required | 64.0 |
| `recursEvery​MonthOnDay` | String | Date when the payment scheduler recurs. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `scheduler​Name` | String | Name of the payment scheduler. | Required | 64.0 |
| `startDate` | String | Start date of the payment scheduler. | Required | 64.0 |
| `status` | String | Status of the payment scheduler. Valid values are: `Active` `Canceled` `Draft` `Inactive` | Required | 64.0 |

=== ARTICLE: connect_requests_payment_scheduler_update_input.htm ===
---
page_id: connect_requests_payment_scheduler_update_input.htm
title: Payment Scheduler Update Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_payment_scheduler_update_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Scheduler Update Input

Input representation of the details of the request to update the status of a payment
    scheduler. This representation defines the status of a payment scheduler, which can be set to
    Active, Canceled, Draft, or Inactive.

    
      
        
          

**JSON example**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
  "status": "Active"
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
| `status` | String | Status that must be set to activate or deactivate a payment scheduler. Valid values are: `Active` `Canceled` `Draft` `Inactive` | Required | 64.0 |

=== ARTICLE: connect_requests_refund_line_apply_input.htm ===
---
page_id: connect_requests_refund_line_apply_input.htm
title: Refund Line Apply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_refund_line_apply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Refund Line Apply Input

Input representation of the details of a transaction refund request. This representation
    outlines the properties of a refund, including the refund amount and ID of the payment or credit
    memo record that the refund is applied to.

**JSON example**

: 

```
{
  "appliedToId": "0aQR00000004ZkKMAU",
  "amount": 10,
  "effectiveDate": "2020-08-11T07:53:15.000Z",
  "comments": "Payment application."
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount to refund. | Required | 64.0 |
| `appliedToId` | String | ID of a payment or credit memo record. The refund is applied to this object. | Required | 64.0 |
| `comments` | String | Additional details of the refund request. | Optional | 64.0 |
| `effectiveDate` | String | Date from when the refund is in effect. | Optional | 64.0 |

=== ARTICLE: connect_requests_resume_billing_entity_input.htm ===
---
page_id: connect_requests_resume_billing_entity_input.htm
title: Resume Billing Object Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_resume_billing_entity_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resume Billing Object Input

Input representation of the details such as the ID of the account or billing schedule
    group along with the effective date. These details are used to start the billing
    operation.

**JSON example**

: 

```
{
    "referenceIds":
    [
        {
          "referenceId": "001DU000001o2UwYAI",
          "resumeDate": "2024-11-27"
        }
    ]
 
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceId` | String | ID of the account or billing schedule group to resume the billing operation for. | Required | 63.0 |
| `resumeDate` | String | Date when the billing operation is resumed. If a date isn’t specified, the default value is today’s date. The billing operation starts immediately and any future suspension dates aren’t applicable. | Required | 63.0 |

=== ARTICLE: connect_requests_resume_billing_input.htm ===
---
page_id: connect_requests_resume_billing_input.htm
title: Resume Billing Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_resume_billing_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resume Billing Input

Input representation of the details of the request to resume the billing operation for an
    account or a billing schedule group.

**JSON example**

: 

```
{
    "referenceIds":
    [
        {
          "referenceId": "001DU000001o2UwYAI",
          "resumeDate": "2024-11-27"
        }
    ]
 
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceIds` | [Resume Billing Object Input](./connect_requests_resume_billing_entity_input.htm.md)[] | Input representation of the account or billing schedule group IDs to resume the billing operation for. | Required | 63.0 |

=== ARTICLE: connect_requests_rules_application_input.htm ===
---
page_id: connect_requests_rules_application_input.htm
title: Rules Application Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_rules_application_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rules Application Input

Input representation for applying payments and credits to invoices based on rules.

**JSON example**

: 

```
{
  "accountId": "001xx000003DGbQAAW",
  "targetDate": "2024-01-15"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account to perform the settlement of payments and credits against invoices in adherence with the applied rules. | Required | 66.0 |
| `targetDate` | String | The date used to select invoices and invoice lines with a posted date equal to or later than the target date to apply payments and credits. | Optional | 66.0 |

=== ARTICLE: connect_requests_selection_condition_input.htm ===
---
page_id: connect_requests_selection_condition_input.htm
title: Selection Condition Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_selection_condition_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Selection Condition Input

Input representation of the criteria that's used to determine which sequencing policy is
    applied to a record. The criteria stores the conditions based on any standard or custom fields
    of the record.

**JSON example**

: 

```
{
  "selectionCondition": [
    {
      "filterField": "AppType",
      "operator": "Equals",
      "filterValue": "RLM",
      "conditionNumber": 1
    },
    {
      "filterField": "Status",
      "operator": "Equals",
      "filterValue": "Posted",
      "conditionNumber": 2
    },
    {
      "filterField": "LegalEntity",
      "operator": "Equals",
      "filterValue": "US",
      "conditionNumber": 3
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
| `condition​Number` | Integer | Unique number that's assigned to a condition in a sequence policy. | Required | 65.0 |
| `filterField` | String | Field used in the filter condition. | Required | 65.0 |
| `filterValue` | String | Value in the filter condition. | Required | 65.0 |
| `operator` | String | Relational operator that's used to compare the filter field with the filter value. Valid values are: `Equals` `NotEquals` | Required | 65.0 |

=== ARTICLE: connect_requests_seller_details_input.htm ===
---
page_id: connect_requests_seller_details_input.htm
title: Seller Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_seller_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Seller Details Input

Input representation of the seller details for tax calculation.

**JSON example**

: 

```
{
  "code": "ADIDAS"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `code` | String | Seller code as specified in the tax engine. | Required | 62.0 |

=== ARTICLE: connect_requests_send_email_for_invoice_batch_run_input.htm ===
---
page_id: connect_requests_send_email_for_invoice_batch_run_input.htm
title: Send Email Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_send_email_for_invoice_batch_run_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Send Email Input

Input representation of the request to send an email for an invoice batch
    run.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "invoiceBatchRunId": "5IRLT000001SIJB4A4"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceBatchRunId` | String | ID of the invoice batch run record to send emails for the posted invoices of an invoice batch run. | Required | 65.0 |

=== ARTICLE: connect_requests_sequence_gap_reconciliation_input.htm ===
---
page_id: connect_requests_sequence_gap_reconciliation_input.htm
title: Sequence Gap Reconciliation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sequence_gap_reconciliation_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Gap Reconciliation Input

Input representation of the details that are used to identify and reconcile gaps in
    sequence values based on the sequence policy or target object.

**JSON example**

: This example shows a sample request that specifies the list of sequence policies for gap
            reconciliation.

```
{
  "sequencePolicyIds": [
    "1vdxx0000000abc",
    "1vdxx0000000def"
  ]
}
```

          
: This example shows a sample request that specifies the target invoice object for gap
            reconciliation.

```
{
  "targetObjects": [
    "Invoice"
  ]
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequence​PolicyIds` | String[] | List of IDs of the sequence policies. | Required if the `targetObjects` property isn't specified. You must not specify both properties. | 65.0 |
| `target​Objects` | String[] | List of objects to which the policies are applied. Valid values are: `Invoice` `CreditMemo`—Available in API version 66.0 and later. | Required if the `sequencePolicyIds` property isn't specified. You must not specify both properties. | 65.0 |

=== ARTICLE: connect_requests_sequence_policy_input.htm ===
---
page_id: connect_requests_sequence_policy_input.htm
title: Sequence Policy Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sequence_policy_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Policy Input

Input representation of the configured rules and properties to generate unique,
    sequential numbers for objects.

**JSON example**

: This example shows a sample request to create a sequence
            policy.

```
{
  "name": "Sample Sequence Policy",
  "description": "This is a sample sequence policy.",
  "effectiveFromDateTime": "2025-08-10",
  "expirationDateTime": "2025-09-20",
  "isActive": true,
  "sequenceMode": "Basic",
  "targetObject": "Invoice",
  "dateStampFormat": "Yyyy",
  "sequenceStartNumber": 1,
  "incrementNumber": 1,
  "maximumSequenceNumber": 1000,
  "minimumSequenceNumberWidth": 2,
  "filterCriteria": "Custom",
  "selectionLogic": "selectionLogic",
  "sequencePattern": "INV-{SequenceValue}-abc",
  "selectionCondition": [
    {
      "filterField": "AppType",
      "operator": "Equals",
      "filterValue": "RLM",
      "conditionNumber": 1
    },
    {
      "filterField": "Status",
      "operator": "Equals",
      "filterValue": "Posted",
      "conditionNumber": 2
    },
    {
      "filterField": "LegalEntity",
      "operator": "Equals",
      "filterValue": "US",
      "conditionNumber": 3
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
| `dateStamp​Format` | String | Format of the stamp date that's appended to the sequence number. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `description` | String | Additional details about the sequence policy. | Optional | 65.0 |
| `effectiveFrom​DateTime` | String | Date and time when the policy becomes effective. The default value is the current date. | Required | 65.0 |
| `expiration​DateTime` | String | Date and time when the policy expires. | Optional | 65.0 |
| `filter​Criteria` | String | Criteria to filter the target objects. | Required | 65.0 |
| `increment​Number` | Integer | Value by which the sequence number increases until it reaches the maximum number. This value must be greater than or equal to `1`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `isActive` | Boolean | Indicates whether the policy is active (`true`) or not (`false`). The default value is `false`. | Required | 65.0 |
| `maximumSequence​Number` | Integer | Maximum number the sequence number can reach. | Optional | 65.0 |
| `minimumSequence​NumberWidth` | Integer | Minimum number of digits a sequence number must have. You can't edit this property by using the Update Sequence Policy API. | Optional | 65.0 |
| `name` | String | Name of the sequence policy. | Required | 65.0 |
| `selection​Condition` | [Selection Condition Input](./connect_requests_selection_condition_input.htm.md)[] | Criteria to determine which sequence policy is applied to a record. This property includes conditions based on any standard or custom fields of the record. | Optional | 65.0 |
| `selection​Logic` | String | Logic that determines the objects that the sequence policy applies to. | Optional | 65.0 |
| `sequence​Mode` | String | Specifies how sequence numbers are generated. Valid values are: `Basic`—Assigns sequential numbers without gap reconciliation. `Gapless`—Assigns sequential numbers with gap reconciliation. The usage of this value ensures that the posted invoices or credit memos don't have any numbering gaps for audits and compliance. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `sequence​Pattern` | String | Pattern structure that’s followed for the sequence. | Required | 65.0 |
| `sequenceStart​Number` | Integer | Starting value of the sequence number, which must be greater than or equal to `0`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `target​Object` | String | Object that the policy is applied to. Valid values are: `Invoice` `CreditMemo`—Available in API version 66.0 and later. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `timeZone` | String | Time zone that’s applicable for the sequence policy. | Optional | 65.0 |

=== ARTICLE: connect_requests_sequences_assignment_input.htm ===
---
page_id: connect_requests_sequences_assignment_input.htm
title: Sequences Assignment Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_sequences_assignment_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequences Assignment Input

Input representation of the details of the target objects to which the sequence pattern
    values are assigned.

**JSON example**

: 

```
{
  "targetObjectIds": [
    "3ttxx00000005nhAAA",
    "3ttxx00000006bhAAA"
  ],
  "sequencePolicyId": "1Vdxx0000004CFU"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequence​PolicyId` | String | ID of the sequence policy. | Optional | 65.0 |
| `shouldPublish​Platform​Event` | Boolean | Indicates whether to publish a platform event when a sequence is assigned to a target record (`true`) or not (`false`). | Optional | 65.0 |
| `target​ObjectIds` | String[] | List of records to which the sequence pattern values are assigned. | Required | 65.0 |

=== ARTICLE: connect_requests_standalone_credit_memo_charge_input.htm ===
---
page_id: connect_requests_standalone_credit_memo_charge_input.htm
title: Standalone Credit Memo Charge Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_standalone_credit_memo_charge_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Credit Memo Charge Input

Input representation of the details of the charge lines of a credit memo.

**JSON example**

: 

```
  "charges": [
    {
      "chargeAmount": 100,
      "productId": "01tR0000000njDiIAI"
    }
  ]
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [Credit Memo Addresses Input](./connect_requests_credit_memo_addresses_input.htm.md) | Details of the billing and shipping addresses. | Optional | 62.0 |
| `charge​Amount` | Double | Charge amount for the credit memo. | Required | 62.0 |
| `description` | String | Description of the created credit memo charge line. | Optional | 62.0 |
| `endDate` | String | End date of the credit memo charge line. | Optional | 62.0 |
| `isTax​OnlyCredit` | Boolean | Indicates whether the credit is for tax only (`true`) or not (`false`). | Optional | 62.0 |
| `product​Id` | String | ID of the product record that the credit memo is issued on. | Optional | 62.0 |
| `product​Name` | String | Name of the product that the credit memo is issued on. | Optional | 62.0 |
| `startDate` | String | Start date of the credit memo charge line. | Optional | 62.0 |
| `taxEffective​Date` | String | Date from when the tax is applicable. | Optional | 62.0 |
| `taxes` | [Standalone Credit Memo Tax Input](./connect_requests_standalone_credit_memo_tax_input.htm.md)[] | List of credit memo tax lines. | Optional | 62.0 |
| `taxStrategy` | String | Tax strategy to be applied to this credit memo charge line, child treatment lines, and tax lines. You can override the tax strategy at the individual credit memo lines or tax lines level. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. | Optional | 62.0 |
| `treatment​Id` | String | ID of the tax treatment record that’s used to calculate tax. | Optional | 62.0 |

=== ARTICLE: connect_requests_standalone_credit_memo_input.htm ===
---
page_id: connect_requests_standalone_credit_memo_input.htm
title: Standalone Credit Memo Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_standalone_credit_memo_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Credit Memo Input

Input representation of the details required to create a standalone credit
    memo.

**JSON example**

: This example shows a sample request with the `Ignore` tax
            strategy.

```
{
  "billingAccountId": "001j000000WCFB800x",
  "type": "Posted",
  "description": "Standalone credit memo with ignored tax.",
  "currencyIsoCode": "USD",
  "taxStrategy": "Ignore",
  "charges": [
    {
      "chargeAmount": 100,
      "productId": "01tR0000000njDiIAI"
    }
  ]
}
```

          
: This example shows a sample request with the `ManualOverride` tax
            strategy.

```
{
  "billingAccountId": "001DU000001nhoPYAQ",
  "description": "creditmemo-1",
  "currencyIsoCode": "USD",
  "taxStrategy": "ManualOverride",
  "charges": [
    {
      "productId": "01tDU000000EpKkYAK",
      "chargeAmount": 1000,
      "taxes": [
        {
          "taxAmount": 7.25,
          "taxCode": "CA-94121",
          "taxName": "CALIFORNIA",
          "taxRate": 0.25
        }
      ]
    }
  ]
}
```

          
: This example shows a sample request with the `Calculate` tax strategy for a charge
            line.

```
{
  "billingAccountId": "001DU000001nhoPYAQ",
  "description": "Standalone Credit Memo",
  "type": "Posted",
  "currencyIsoCode": "USD",
  "taxStrategy": "Ignore",
  "charges": [
    {
      "productId": "01tR0000000njDiIAI",
      "chargeAmount": 10,
      "taxStrategy": "Calculate",
      "treatmentId": "1ttxx00000001VZAAY"
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
| `billTo​ContactId` | String | Contact related to the credit memo. | Optional | 62.0 |
| `billing​AccountId` | String | ID of the account that the credit is issued to. | Required | 62.0 |
| `charges` | [Standalone Credit Memo Charge Input](./connect_requests_standalone_credit_memo_charge_input.htm.md)[] | Charge lines of the credit memo. Requires at least one charge line. | Required | 62.0 |
| `currency​IsoCode` | String | ISO code currency of the new credit that’s issued. | Optional | 62.0 |
| `description` | String | Description for the new credit that’s issued. | Optional | 62.0 |
| `effective​Date` | String | Effective date of the credit memo. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `external​Reference` | String | ID of the external reference for the credit memo. | Optional | 62.0 |
| `externalReference​Data​Source` | String | Source of the external reference for the credit memo. | Optional | 62.0 |
| `taxEffective​Date` | String | Effective date of the credit memo tax. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `tax​Strategy` | String | Specifies how tax lines must be created for the standalone credit memos. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. | Required | 62.0 |
| `type` | String | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. | Optional | 62.0 |

=== ARTICLE: connect_requests_standalone_credit_memo_tax_input.htm ===
---
page_id: connect_requests_standalone_credit_memo_tax_input.htm
title: Standalone Credit Memo Tax Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_standalone_credit_memo_tax_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Credit Memo Tax Input

Input representation of the details of the tax request.

**JSON example**

: 

```
[
  {
    "taxAmount": 200,
    "taxName": "Federal Tax",
    "taxRate": 1
  },
  {
    "taxAmount": 500,
    "taxName": "State Tax",
    "taxRate": 1
  }
]
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `taxAmount` | Double | Amount of tax to be applied. | Required | 62.0 |
| `taxCode` | String | Tax code to be used to create the tax line. | Optional | 62.0 |
| `taxName` | String | Name of tax to be applied. | Optional | 62.0 |
| `taxRate` | Double | Tax rate to be used to create the tax line. | Optional | 62.0 |

=== ARTICLE: connect_requests_statement_of_account_input.htm ===
---
page_id: connect_requests_statement_of_account_input.htm
title: Account Statement Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_statement_of_account_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Account Statement Input

Input representation of the details required to generate a comprehensive account
    statement with transaction history and balance information.

**JSON example**

: 

```
{
  "shouldShowOpenBalancesOnly": false,
  "startDate": "2025-09-01",
  "transactionTypes": {
    "transactionTypes": [
      "Invoice"
    ]
  },
  "sortBy": "DueDate",
  "sortingOrder": "Ascending",
  "associatedAccountIds": {
    "associatedAccountIds": [
      "001xx000003DGb5AAG",
      "001xx000003DGb6AAG"
    ]
  },
  "documentTemplateId": "0TRxx000000002YGAQ",
  "correlationId": "monthly-statement-sept-2025",
  "customFields": "{\"Invoice\": [\"TotalAmountWithTax\"], \"Account\": {\"base\": [\"Phone\", \"Fax\"], \"associated\": [\"Website\"]}}}"
}
```

**Properties**

: 

                  
                    

                    

                    

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

```

```

                    

                    

                  

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
| `associatedAccountIds` | String[] | List of associated account IDs from hierarchy to include in the statement. You can specify up to 50 accounts. | Optional | 66.0 |
| `correlationId` | String | Correlation ID for tracking the request across systems. | Optional | 66.0 |
| `customFields` | String | JSON string specifying custom fields to include in the statement. As a best practice, we recommend that you limit the number of custom fields up to 30 fields. Valid objects to specify the associated fields are: Invoice CreditMemo Payment DebitMemo Refund Account Here's the expected format.{"Invoice": ["field1", "field2"], "Account": {"base": ["field1"], "associated": ["field2"]}} | Optional | 67.0 |
| `documentTemplateId` | String | Document template ID to use for PDF generation. If you don’t specify a value, the system auto-resolves by using the default template. | Optional | 66.0 |
| `shouldShowOpenBalancesOnly` | Boolean | Indicates whether to show open balances only (`true`) or not (`false`). If set to `true`, the API shows only accounts with non-zero balances. If set to `false`, this API shows complete transaction history within the date range from the start date. | Optional | 66.0 |
| `sortBy` | String | Criteria for sorting transactions. The default and valid value is `Date`. | Optional | 66.0 |
| `sortingOrder` | String | Sort order for transactions. Valid values are: `Ascending` `Descending` The default value is `Descending`. | Optional | 66.0 |
| `startDate` | String | Start date for the transaction history. The required format is `YYYY-MM-DD`. The system processes records up to 90 days from this date. | Required | 66.0 |
| `transactionTypes` | String[] | List of transaction types to include in the statement. If you don’t specify a value or the value is empty, all transaction types are included. Valid values are: `All` `CreditMemo` `DebitMemo` `Invoice` `Payment` `Refund` | Optional | 66.0 |

=== ARTICLE: connect_requests_suspend_billing_entity_input.htm ===
---
page_id: connect_requests_suspend_billing_entity_input.htm
title: Suspend Billing Object Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_suspend_billing_entity_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Billing Object Input

Input representation of the details such as the ID of the account or billing schedule
    group along with the effective dates. These details are used to suspend the billing
    operation.

**JSON example**

: 
            

```
{
    "referenceIds": 
    [
        {
            "referenceId": "001DU000001o2UwYAI",
            "suspendDate": "2024-11-27",
            "resumeDate": "2024-12-27"
        }
    ]
}
```

          

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceId` | String | ID of the account or billing schedule group to suspend the billing operation for. | Required | 63.0 |
| `resumeDate` | String | Date until when the account or billing schedule group is suspended for billing. | Required | 63.0 |
| `suspendDate` | String | Date when the account or billing schedule group is suspended for billing. | Required | 63.0 |

=== ARTICLE: connect_requests_suspend_billing_input.htm ===
---
page_id: connect_requests_suspend_billing_input.htm
title: Suspend Billing Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_suspend_billing_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Billing Input

Input representation of the details of the request to suspend the billing operation for
    an account or a billing schedule group.

**JSON example**

: 

```
{
    "referenceIds": 
    [
        {
            "referenceId": "001DU000001o2UwYAI",
            "suspendDate": "2024-11-27",
            "resumeDate": "2024-12-27"
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceIds` | [Suspend Billing Object Input](./connect_requests_suspend_billing_entity_input.htm.md)[] | Input representation of the account or billing schedule group IDs to suspend the billing operation for. | Required | 63.0 |

=== ARTICLE: connect_requests_void_posted_credit_memo_input.htm ===
---
page_id: connect_requests_void_posted_credit_memo_input.htm
title: Void Posted Credit Memo Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_void_posted_credit_memo_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void Posted Credit Memo Input

Input representation of the details of a credit memo to be voided.

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemoId` | String | ID of the posted credit memo to be voided. | Required | 66.0 |

=== ARTICLE: connect_requests_void_posted_invoice_input.htm ===
---
page_id: connect_requests_void_posted_invoice_input.htm
title: Void Posted Invoice Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_void_posted_invoice_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void
    Posted Invoice Input

Input representation of the details of the invoice to be voided.

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceId` | String | ID of the posted invoice to be voided. | Required | 62.0 |

=== ARTICLE: connect_requests_write_off_posted_invoice_input.htm ===
---
page_id: connect_requests_write_off_posted_invoice_input.htm
title: Posted Invoice Write-Off Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_write_off_posted_invoice_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice Write-Off Input

Input representation of the details of the request to write off a posted invoice. This
    representation includes invoice details such as invoice ID and reason for writing off
    invoices.

**JSON example**

: 

```
{
  "invoices": [
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Bad Debt",
      "description": "Bad Debt"
    },
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Concession",
      "description": "Concession"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceId` | String | ID of the invoice record that you want to write off. | Required | 64.0 |
| `reason` | String | Reason for writing off invoices. | Optional | 64.0 |
| `reason​Code` | String | Code that categorizes the write-off reason. For example, if the reason for the invoice write-off is a disputed amount, the reason code can be Disputed Amount (DA). | Required | 64.0 |

=== ARTICLE: connect_requests_write_off_posted_invoice_list_input.htm ===
---
page_id: connect_requests_write_off_posted_invoice_list_input.htm
title: Posted Invoice List Write-Off Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_write_off_posted_invoice_list_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice List Write-Off Input

Input representation of the request to write off a list of posted invoices. This
    representation includes the details of invoices that you want to write off.

**JSON example**

: 

```
{
  "invoices": [
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Bad Debt",
      "description": "Bad Debt"
    },
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Concession",
      "description": "Concession"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoices` | [Posted Invoice Write-Off Input](./connect_requests_write_off_posted_invoice_input.htm.md)[] | Details of the invoices that you want to write off. | Required | 64.0 |

=== ARTICLE: connect_resources_apply_refund_to_payment.htm ===
---
page_id: connect_resources_apply_refund_to_payment.htm
title: Refund Line Apply (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_apply_refund_to_payment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Refund Line Apply (POST)

Make a refund transaction against a payment.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/billing/refunds/refundId/actions/apply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/refunds/0cbVc0000000G4nIAE/actions/apply
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `refundId` | String | ID of the refund record. | Required | 64.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "appliedToId": "0aQR00000004ZkKMAU",
  "amount": 10,
  "effectiveDate": "2020-08-11T07:53:15.000Z",
  "comments": "Payment application."
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount to refund. | Required | 64.0 |
| `appliedToId` | String | ID of a payment or credit memo record. The refund is applied to this object. | Required | 64.0 |
| `comments` | String | Additional details of the refund request. | Optional | 64.0 |
| `effectiveDate` | String | Date from when the refund is in effect. | Optional | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Refund Line
              Apply](./connect_responses_refund_line_apply_output.htm.md)

=== ARTICLE: connect_resources_batch_draft_invoices_to_posted.htm ===
---
page_id: connect_resources_batch_draft_invoices_to_posted.htm
title: Batch Invoices Draft to Posted Status (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_batch_draft_invoices_to_posted.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch
    Invoices
    Draft to
    Posted Status (POST)

Update a batch of invoices from `Draft` to `Posted` status for a credit memo
      application.

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the Billing Operations User permission set.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoice-batch-runs/invoiceBatchRunId/actions/draft-to-posted
```

          

          
: This API posts the draft invoices and changes the status of the invoices from `Draft` to `Posted`.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoice-batch-runs/5IRNZ0000000cA94AI/actions/draft-to-posted
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoice​Batch​RunId` | String | ID of the invoice batch run record that creates the draft invoices. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Invoice Batch Draft
              To Posted](./connect_responses_invoice_batch_draft_to_posted_output.htm.md)

=== ARTICLE: connect_resources_calculate_estimated_tax.htm ===
---
page_id: connect_resources_calculate_estimated_tax.htm
title: Invoice Estimated Tax Calculation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_calculate_estimated_tax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Estimated Tax Calculation (POST)

Calculate estimated tax for invoices with invoice lines that have the
        `TaxProcessingStatus` as either `Pending` or `Estimated`.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/collection/actions/calculate-estimated-tax
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/collection/actions/calculate-estimated-tax
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
  "invoiceIds": ["3ttxx0000004CIjAAM"]
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Splunk correlation ID to track the messages that are related to the request and are logged in Splunk by the different services involved in the request. If the ID isn’t specified, the service creates a random Universally Unique Identifier (UUID). | Optional | 63.0 |
| `invoiceIds` | String[] | IDs of the invoices for which the estimated tax must be calculated. You can specify one invoice per API request. | Required | 63.0 |

          

          

        
        
          

**Response body for POST**

          
: [Revenue Async Response](./connect_responses_revenue_async_output.htm.md)

=== ARTICLE: connect_resources_calculate_taxes.htm ===
---
page_id: connect_resources_calculate_taxes.htm
title: Tax Calculation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_calculate_taxes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Calculation (POST)

Calculate tax for a transaction.

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the CalculateTaxes  API permission set.

        
        
          

**Resource**

          
: 
            

```
/commerce/taxes/actions/calculate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/taxes/actions/calculate
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: This example shows a tax request for a specified invoice as the reference
            entity.

```
{
  "addresses": {
    "billTo": {
      "street": "123 Main Street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    },
    "soldTo": {
      "street": "123 Main Street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    },
    "shipFrom": {
      "street": "123 Alaskan Way",
      "city": "Seattle",
      "state": "WA",
      "country": "US",
      "postalCode": "98101"
    },
    "shipTo": {
      "street": "123 Main street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    }
  },
  "currencyIsoCode": "USD",
  "customerDetails": {
    "accountId": "001xx000003HYD5AAO"
  },
  "description": "Monthly invoice for account 001xx000003HYEhAAO",
  "documentCode": "3ttxx0000000C7d_Debit-4wAxx00000000ODEAY",
  "effectiveDate": "2022-03-09T10:30:41.000Z",
  "isCommit": true,
  "lineItems": [
    {
      "quantity": 1,
      "amount": 100,
      "taxCode": "TX0001",
      "productCode": "Y0001",
      "productSKU": "PRES-RX-12896745",
      "description": "New Product",
      "effectiveDate": "2022-03-09T10:30:41.000Z",
      "lineNumber": "5TVxx0000004C92GAE",
      "addresses": {
        "shipFrom": {
          "street": "123 Alaskan Way",
          "city": "Seattle",
          "state": "WA",
          "country": "US",
          "postalCode": "98101",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "shipTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "soldTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "billTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        }
      }
    }
  ],
  "referenceDocumentCode" = null,
  "referenceEntityId": "3ttxx0000000C7d",
  "shouldVoidTax": false,
  "taxEngineId": "4wAxx0000000g8v",
  "taxType": "Actual",
  "taxTransactionType": "Debit",
  "transactionDate": "2022-03-09T10:30:41.000Z"
}
```

          
: This example shows a tax request for a specified credit memo as the reference
            entity.

```
{
  "addresses": {
    "billTo": {
      "street": "123 Main Street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    },
    "soldTo": {
      "street": "123 Main Street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    },
    "shipFrom": {
      "street": "123 Alaskan Way",
      "city": "Seattle",
      "state": "WA",
      "country": "US",
      "postalCode": "98101"
    },
    "shipTo": {
      "street": "123 Main street",
      "city": "Bainbridge Island",
      "state": "WA",
      "postalCode": "98110",
      "country": "US"
    }
  },
  "currencyIsoCode": "USD",
  "customerDetails": {
    "accountId": "001xx000003HYD5AAO"
  },
  "description": "Monthly credit memo for account 001xx000003HYEhAAO",
  "documentCode": "50gxx000000g27KAAQ-4wAxx00000000ODEAY",
  "effectiveDate": "2022-03-09T10:30:41.000Z",
  "isCommit": true,
  "lineItems": [
    {
      "quantity": 1,
      "amount": 100,
      "taxCode": "TX0001",
      "productCode": "Y0001",
      "productSKU": "PRES-RX-12896745",
      "description": "New Product",
      "effectiveDate": "2022-03-09T10:30:41.000Z",
      "lineNumber": "5TVxx0000004C92GAE",
      "addresses": {
        "shipFrom": {
          "street": "123 Alaskan Way",
          "city": "Seattle",
          "state": "WA",
          "country": "US",
          "postalCode": "98101",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "shipTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "soldTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        },
        "billTo": {
          "street": "123 Auburn Blvd",
          "city": "Sacramento",
          "state": "CA",
          "country": "US",
          "postalCode": "95841",
          "latitude": 45.12,
          "longitude": 45.12
        }
      }
    }
  ],
  "referenceDocumentCode" = null,
  "referenceEntityId": "50gxx000000g27K",
  "shouldVoidTax": false,
  "taxEngineId": "4wAxx0000000g8v",
  "taxType": "Actual",
  "taxTransactionType": "Debit",
  "transactionDate": "2022-03-09T10:30:41.000Z"
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
| `addresses` | [Addresses](./connect_requests_addresses_input.htm.md) | Address details for tax calculation. | Optional | 62.0 |
| `currencyIsoCode` | String | Currency ISO code that’s used for tax calculation. | Optional | 62.0 |
| `customerDetails` | [Customer Details](./connect_requests_customer_details_input.htm.md) | Customer details for determining the applicable tax. | Optional | 62.0 |
| `description` | String | Description of the tax transaction. | Optional | 62.0 |
| `documentCode` | String | Unique identifier for the tax document. If the `documentCode` property isn't specified, the tax engine auto-generates it. | Optional | 62.0 |
| `effectiveDate` | String | Date when the tax rules are applied. If a tax rate changes on a specific date, the `effectiveDate` property ensures the correct rate is applied based on the transaction's timing. For credit-based tax callouts, specify the original invoice date. | Optional | 62.0 |
| `isCommit` | Boolean | Indicates whether to submit the transaction to the tax engine for reporting (`true`) or not (`false`).This property value is `true` for invoices and credit memos with the `Posted` status. | Optional | 62.0 |
| `lineItems` | [Line Item Input](./connect_requests_line_item_input.htm.md) [] | Details of the line items for calculating the applicable tax. | Required | 62.0 |
| `reference​DocumentCode` | String | Reference document code. For subsequent transactions such as a credit tax, this property value specifies the original document code. For credit-based tax callouts, specify the original invoice ID. | Optional | 62.0 |
| `reference​EntityId` | String | ID of the related quote, invoice, and other transaction documents. | Optional | 62.0 |
| `sellerDetails` | [Seller Details Input](./connect_requests_seller_details_input.htm.md) | Seller details for tax calculation. | Optional | 62.0 |
| `shouldVoidTax` | Boolean | Indicates whether to void the tax transaction associated with a document that's mentioned as the `referenceDocumentCode` property value with `taxType` property value as `Actual` and `isCommit` property value set to `true`. Keep these considerations in mind when you use this property. If the `shouldVoidTax` property value is set to `true`, then the operation returns a response with `documentCode` property value updated to `referenceDocumentCode` property value that was originally sent in the request payload. The response also includes the `taxTransactionType` property value as `Void`. This indicates that the document specified in the `referenceDocumentCode` property value is voided. If document is locked or you can't void the tax transaction for any reason, then you can use the Tax Calculation request to perform another transaction such as a Credit Tax request. In this scenario, the response includes the `documentCode` property value that was sent in the request payload. If the document that's mentioned in the `referenceDocumentCode` property value isn't available in the tax engine, then an error response occurs with [ResultCode](./apex_enum_commercetax_ResultCode.htm.md) value as `ReferenceDocumentCodeMissing`. | Optional | 65.0 |
| `taxEngineId` | String | ID of the tax engine that’s used to calculate tax. | Required | 62.0 |
| `tax​TransactionType` | String | Type of the tax transaction. Valid values are: `Debit`—Increases tax liability for the seller, requiring the seller to pay tax on the transaction. `Credit`—Decreases tax liability for the seller, resulting in a tax refund for the seller. `Void`—Reserved for internal use. The default value is `Debit`. | Optional | 62.0 |
| `taxType` | String | Type of the tax. Valid values are: `Actual`—Exact tax amount that’s calculated based on actual sales. `Estimated`— Estimated tax amount, which is adjusted later to match actual tax calculations. For draft invoices and quote records, the tax type is marked as `Estimated`. After draft invoices are posted and the status changes to `Posted`, the tax type is updated to `Actual`. Similarly, when a quote record is finalized and converted into an actual order, the tax type is also updated to `Actual`. | Required | 62.0 |
| `transactionDate` | String | Date of the transaction that appears on the invoice, order, and other transaction documents. | Required | 62.0 |

          

        

          

        
        
          

**Response body for POST**

          
: [Tax Calculation](./connect_responses_calculate_tax_output.htm.md)

=== ARTICLE: connect_resources_convert_negative_invoice_lines_to_credit.htm ===
---
page_id: connect_resources_convert_negative_invoice_lines_to_credit.htm
title: Negative Invoice Lines to Credit Conversion (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_convert_negative_invoice_lines_to_credit.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Negative Invoice Lines to Credit Conversion (POST)

Convert a list of invoice lines with a negative amount into a posted
      credit memo. This conversion is applicable for a single invoice at a time.

    
      

Keep these considerations in mind when you use this API.

      
        
- All invoice lines must be related to the same invoice.

        
- The invoice line must have a negative amount.

        
- The invoice line must not be a previously converted credit memo.

        
- The invoice must have the `Posted` status.

        
- The invoice must not have any active settlements such as credit applications.

      

    

    
      
        
          

**Special Access Rules**

          
: 

You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/invoiceId/actions/convert-to-credit
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/3ttxx00000000XtAAI/actions/convert-to-credit
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceId` | String | ID of the invoice whose negative invoice lines must be converted into a posted credit memo. | Required | 62.0 |

      
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
  {
  "invoiceLines": ["5TVxx0000004C92GAE", "5TVxx0000004C93GAE"],
  "description": "Convert negative invoice lines into credit",
  "effectiveDate":"2022-05-18"
  }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Description stamped on the credit memo that’s created after the negative invoice line conversion. | Optional | 62.0 |
| `effectiveDate` | String | Date stamped on the credit memo that’s created after the negative invoice line conversion. | Required | 62.0 |
| `invoiceLines` | String[] | Complete list of the negative invoice lines along with the associated invoice line taxes. The specified negative invoice lines are converted into a posted credit memo. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Convert Negative
              Invoice Lines](./connect_responses_convert_negative_invoice_lines_output.htm.md)

=== ARTICLE: connect_resources_create_a_standalone_credit_memo.htm ===
---
page_id: connect_resources_create_a_standalone_credit_memo.htm
title: Standalone Credit Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_a_standalone_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Credit Memo (POST)

Create a credit memo without applying it to an invoice. You can credit
      the invoice at a later date.

    

In the API request, specify the credit memo header information, charge parameters,
        adjustment parameters, and tax parameters. A credit memo requires at least one credit memo
        line. The credit memo line can be a charge or an adjustment.

Specify the credit memo
        lines that you want as lists of charges and adjustments. Each credit memo line must be
        related to a product.

    
      
        
          

**Special Access Rules**

          
: 

You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit-memos/actions/generate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/credit-memos/actions/generate
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: This example shows a sample request with the `Ignore` tax
            strategy.

```
{
  "billingAccountId": "001j000000WCFB800x",
  "type": "Posted",
  "description": "Standalone credit memo with ignored tax.",
  "currencyIsoCode": "USD",
  "taxStrategy": "Ignore",
  "charges": [
    {
      "chargeAmount": 100,
      "productId": "01tR0000000njDiIAI"
    }
  ]
}
```

          
: This example shows a sample request with the `ManualOverride` tax
            strategy.

```
{
  "billingAccountId": "001DU000001nhoPYAQ",
  "description": "creditmemo-1",
  "currencyIsoCode": "USD",
  "taxStrategy": "ManualOverride",
  "charges": [
    {
      "productId": "01tDU000000EpKkYAK",
      "chargeAmount": 1000,
      "taxes": [
        {
          "taxAmount": 7.25,
          "taxCode": "CA-94121",
          "taxName": "CALIFORNIA",
          "taxRate": 0.25
        }
      ]
    }
  ]
}
```

          
: This example shows a sample request with the `Calculate` tax strategy for a charge
            line.

```
{
  "billingAccountId": "001DU000001nhoPYAQ",
  "description": "Standalone Credit Memo",
  "type": "Posted",
  "currencyIsoCode": "USD",
  "taxStrategy": "Ignore",
  "charges": [
    {
      "productId": "01tR0000000njDiIAI",
      "chargeAmount": 10,
      "taxStrategy": "Calculate",
      "treatmentId": "1ttxx00000001VZAAY"
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
| `billTo​ContactId` | String | Contact related to the credit memo. | Optional | 62.0 |
| `billing​AccountId` | String | ID of the account that the credit is issued to. | Required | 62.0 |
| `charges` | [Standalone Credit Memo Charge Input](./connect_requests_standalone_credit_memo_charge_input.htm.md)[] | Charge lines of the credit memo. Requires at least one charge line. | Required | 62.0 |
| `currency​IsoCode` | String | ISO code currency of the new credit that’s issued. | Optional | 62.0 |
| `description` | String | Description for the new credit that’s issued. | Optional | 62.0 |
| `effective​Date` | String | Effective date of the credit memo. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `external​Reference` | String | ID of the external reference for the credit memo. | Optional | 62.0 |
| `externalReference​Data​Source` | String | Source of the external reference for the credit memo. | Optional | 62.0 |
| `taxEffective​Date` | String | Effective date of the credit memo tax. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `tax​Strategy` | String | Specifies how tax lines must be created for the standalone credit memos. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. | Required | 62.0 |
| `type` | String | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Revenue Async
              Response](./connect_responses_revenue_async_output.htm.md)

=== ARTICLE: connect_resources_create_an_invoice_scheduler.htm ===
---
page_id: connect_resources_create_an_invoice_scheduler.htm
title: Batch Invoice Scheduler (POST, PUT)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_an_invoice_scheduler.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoice Scheduler (POST, PUT)

Create or update an invoice scheduler to automatically generate
      invoices. Use the criteria and filters of the invoice scheduler to set up the invoice run
      schedules based on your requirements.

    
      
        
          

**Special Access Rules**

          
: You need the Billing Operations User and Data Pipelines Base User permission sets to
            use this API. See [Data Pipelines](https://help.salesforce.com/s/articleView?id=sf.reference_data_processing_engine_requirements.htm&language=en_US).

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoice-schedulers
```

            

```
/commerce/invoicing/invoice-schedulers/billingBatchSchedulerId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoice-schedulers
```

            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoice-schedulers/5BSxx0000004TwGGAU
```

            
          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST, PUT

          
: PUT is supported in version 63.0 and later for invoice schedulers with `Draft` or `Inactive`
            status.

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

                    
: This example shows a sample request to create an invoice scheduler that
            generates invoices once. 

```
{
  "schedulerName": "InvoiceScheduler",
  "startDate": "2024-05-06",
  "invoiceStatus": "POSTED",
  "preferredTime": "00:45",
  "targetDate": "2024-05-22",
  "invoiceDate": "2024-05-22",
  "frequencyCadence": "Once",
  "frequencyCadenceOptions": {},
  "timezone": "Asia/Kolkata",
  "status": "Active",
  "filterCriteria": [
    {
      "operation": "InList",
      "value": "Batch 2,Batch 3,Batch 4",
      "criteriaSequence": 1,
      "objectName": "BillingSchedule",
      "fieldName": "InvoiceRunMatchingValue"
    },
    {
      "operation": "Equals",
      "value": "001xx000003GZG5AAO",
      "criteriaSequence": 2,
      "objectName": "BillingSchedule",
      "fieldName": "BillingAccount"
    },
    {
      "operation": "Equals",
      "value": "0fwxx0000000001AAA",
      "criteriaSequence": 3,
      "objectName": "BillingScheduleGroup",
      "fieldName": "LegalEntity"
    },
    {
      "operation": "InList",
      "value": "OneTime,Recurring",
      "criteriaSequence": 4,
      "objectName": "BillingSchedule",
      "fieldName": "BillingTermUnit"
    },
    {
      "operation": "Equals",
      "value": "USD",
      "criteriaSequence": 5,
      "objectName": "BillingSchedule",
      "fieldName": "Currency_Iso_code"
    }
  ]
}
```

: This example shows a sample request to create an invoice scheduler that generates invoices
            daily. 

```
{
  "schedulerName": "InvoiceScheduler",
  "startDate": "2024-05-06",
  "endDate": "2026-05-06",
  "invoiceStatus": "POSTED",
  "preferredTime": "00:45",
  "targetDateOffset": 0,
  "invoiceDateOffset": 0,
  "isInvoiceDateFromRunDate": true,
  "frequencyCadence": "Daily",
  "frequencyCadenceOptions": {},
  "timezone": "Asia/Kolkata",
  "status": "Active",
  "filterCriteria": [
    {
      "operation": "InList",
      "value": "Batch 2,Batch 3,Batch 4",
      "criteriaSequence": 1,
      "objectName": "BillingSchedule",
      "fieldName": "InvoiceRunMatchingValue"
    },
    {
      "operation": "Equals",
      "value": "001xx000003GZG5AAO",
      "criteriaSequence": 2,
      "objectName": "BillingSchedule",
      "fieldName": "BillingAccount"
    },
    {
      "operation": "Equals",
      "value": "0fwxx0000000001AAA",
      "criteriaSequence": 3,
      "objectName": "BillingScheduleGroup",
      "fieldName": "LegalEntity"
    },
    {
      "operation": "InList",
      "value": "OneTime,Recurring",
      "criteriaSequence": 4,
      "objectName": "BillingSchedule",
      "fieldName": "BillingTermUnit"
    },
    {
      "operation": "InList",
      "value": "USD",
      "criteriaSequence": 5,
      "objectName": "BillingSchedule",
      "fieldName": "Currency_Iso_code"
    }
  ]
}
```

                    
: This example shows a sample request to create an invoice scheduler that
            generates invoices weekly. 

```
{
  "schedulerName": "InvoiceScheduler",
  "startDate": "2024-05-06",
  "endDate": "2026-05-06",
  "invoiceStatus": "POSTED",
  "preferredTime": "00:45",
  "targetDateOffset": 0,
  "invoiceDateOffset": 0,
  "isInvoiceDateFromRunDate": false,
  "frequencyCadence": "Weekly",
  "frequencyCadenceOptions": {
    "recursOnDay": "Sunday"
  },
  "timezone": "Asia/Kolkata",
  "status": "Active",
  "filterCriteria": [
    {
      "operation": "InList",
      "value": "Batch 2,Batch 3,Batch 4",
      "criteriaSequence": 1,
      "objectName": "BillingSchedule",
      "fieldName": "InvoiceRunMatchingValue"
    },
    {
      "operation": "Equals",
      "value": "001xx000003GZG5AAO",
      "criteriaSequence": 2,
      "objectName": "BillingSchedule",
      "fieldName": "BillingAccount"
    },
    {
      "operation": "Equals",
      "value": "0fwxx0000000001AAA",
      "criteriaSequence": 3,
      "objectName": "BillingScheduleGroup",
      "fieldName": "LegalEntity"
    },
    {
      "operation": "InList",
      "value": "OneTime,Recurring",
      "criteriaSequence": 4,
      "objectName": "BillingSchedule",
      "fieldName": "BillingTermUnit"
    },
    {
      "operation": "Equals",
      "value": "USD",
      "criteriaSequence": 5,
      "objectName": "BillingSchedule",
      "fieldName": "Currency_Iso_code"
    }
  ]
}
```

                    
: This example shows a sample request to create an invoice scheduler that
            generates invoices monthly on a specific date.
            

```
{
  "schedulerName": "InvoiceScheduler",
  "startDate": "2024-05-06",
  "endDate": "2026-05-06",
  "invoiceStatus": "POSTED",
  "preferredTime": "00:45",
  "targetDateOffset": 0,
  "invoiceDateOffset": 0,
  "isInvoiceDateFromRunDate": false,
  "frequencyCadence": "Monthly",
  "frequencyCadenceOptions": {
    "recurringSubType": "SpecificDate",
    "recursOnDate": "L-1",
    "shouldExcludeWkendAndHldy": true
  },
  "timezone": "Asia/Kolkata",
  "status": "Active",
  "filterCriteria": [
    {
      "operation": "InList",
      "value": "Batch 2,Batch 3,Batch 4",
      "criteriaSequence": 1,
      "objectName": "BillingSchedule",
      "fieldName": "InvoiceRunMatchingValue"
    },
    {
      "operation": "Equals",
      "value": "001xx000003GZG5AAO",
      "criteriaSequence": 2,
      "objectName": "BillingSchedule",
      "fieldName": "BillingAccount"
    },
    {
      "operation": "Equals",
      "value": "0fwxx0000000001AAA",
      "criteriaSequence": 3,
      "objectName": "BillingScheduleGroup",
      "fieldName": "LegalEntity"
    },
    {
      "operation": "InList",
      "value": "OneTime,Recurring",
      "criteriaSequence": 4,
      "objectName": "BillingSchedule",
      "fieldName": "BillingTermUnit"
    },
    {
      "operation": "Equals",
      "value": "USD",
      "criteriaSequence": 5,
      "objectName": "BillingSchedule",
      "fieldName": "Currency_Iso_code"
    }
  ]
}
```

          
: This example shows a sample request to create an invoice scheduler that runs
            immediately. 

```
{
    "schedulerName": "InvoiceScheduler",
    "status": "Draft",
    "invoiceStatus": "Posted",
    "frequencyCadenceOptions": {
        "shouldStartRunImmediately": true
    },
    "frequencyCadence": "Once",
    "targetDate": "2024-08-28",
    "invoiceDate": "2024-08-28",
    "filterCriteria": [
        {
            "operation": "InList",
            "value": "Batch 2,Batch 3,Batch 4",
            "criteriaSequence": 1,
            "objectName": "BillingSchedule",
            "fieldName": "InvoiceRunMatchingValue"
        },
        {
            "operation": "Equals",
            "value": "001xx000003GZG5AAO",
            "criteriaSequence": 2,
            "objectName": "BillingSchedule",
            "fieldName": "BillingAccount"
        },
        {
            "operation": "Equals",
            "value": "0fwxx0000000001AAA",
            "criteriaSequence": 3,
            "objectName": "BillingScheduleGroup",
            "fieldName": "LegalEntity"
        },
        {
            "operation": "InList",
            "value": "OneTime,Recurring",
            "criteriaSequence": 4,
            "objectName": "BillingSchedule",
            "fieldName": "BillingTermUnit"
        },
        {
            "operation": "Equals",
            "value": "USD",
            "criteriaSequence": 5,
            "objectName": "BillingSchedule",
            "fieldName": "Currency_Iso_code"
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
| `endDate` | String | End date of the invoice scheduler. | Optional | 63.0 |
| `filter​Criteria` | [Batch Invoice Filter Criteria Input](./connect_requests_batch_invoice_filter_criteria_input.htm.md)[] | List of line items of the filter criteria. | Optional | 62.0 |
| `frequency​Cadence` | String | Frequency to run the invoice scheduler. Valid values are: `Once` `Daily` `Weekly` `Monthly` | Required | 62.0 |
| `frequency​Cadence​Options` | [Frequency Cadence Options](./connect_requests_frequency_cadence_options.htm.md) | Frequency cadence options for the invoice scheduler. | Required | 62.0 |
| `invoice​Date` | String | Date shown on the invoice. This date is also used for tax calculations. | Required if the `frequency​Cadence` property is set to `Once`. | 62.0 |
| `invoiceDate​Offset` | Integer | Offset applied to the target date, which is the number of days added to or subtracted from the invoice date, to calculate the updated invoice date. | Required if the `frequency​Cadence` property is set to `Daily`, `Weekly`, or `Monthly`. | 62.0 |
| `invoice​Status` | String | Status of the invoice that specifies the expected invoice status from an invoice batch run. Valid values are: `Draft` `Posted` | Required | 62.0 |
| `isInvoice​DateFrom​RunDate` | Boolean | Indicates whether the invoice date is applicable from the date when the invoice scheduler is run (`true`) or not (`false`). | Optional | 63.0 |
| `preferred​Time` | String | Preferred time for the invoice batch run. | Required | 62.0 |
| `scheduler​Name` | String | Name of the invoice scheduler, which must be unique in your org. | Required | 62.0 |
| `startDate` | String | Start date of the invoice scheduler. | Required | 62.0 |
| `status` | String | Status of the invoice scheduler. Valid values are: `Draft` `Active` `Inactive` | Required | 62.0 |
| `target​Date` | String | Target date of the invoice batch run. Billing schedules having the next billing date before this date are picked up for invoicing. The target date must be less than or equal to the maximum allowed target date for the org. | Required if the `frequency​Cadence` property is set to `Once`. | 62.0 |
| `target​DateOffset` | Integer | Target date offset applied to the next invoice run date to calculate the target date. The offset is the number of days added to or subtracted from the next billing date. | Required if the `frequency​Cadence` property is set to `Daily`, `Weekly`, or `Monthly`. | 62.0 |
| `timezone` | String | Time zone that’s applicable for the invoice scheduler. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Batch Invoice Scheduler](./connect_responses_batch_invoice_scheduler_output.htm.md)

=== ARTICLE: connect_resources_create_and_apply_a_credit_memo.htm ===
---
page_id: connect_resources_create_and_apply_a_credit_memo.htm
title: Create and Apply Credit Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_and_apply_a_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create and Apply Credit Memo (POST)

Create a credit memo and apply it to an invoice. The credit memo can
      fully or partially credit the invoice.

    

Use this API to adjust an outstanding invoice balance or rectify errors in an
        invoice. In the API request, pass a list of invoice lines to credit. Keep these
        considerations in mind when you use this API.

        
- The request must contain at least one invoice line. Each invoice line must have the
          invoice line’s ID, the amount to credit, and any optional tax details. The invoice lines
          must be a part of the invoice passed in the resource.

        
- The amount to credit must not exceed the charge or adjustment amount of an individual
          invoice line.

        
- The request body's credit amount inclusive of taxes must not exceed the target invoice
          line's amount inclusive of taxes, except for taxes calculated through an external tax
          service.

        
- The request body's total credit amount inclusive of taxes calculated through an external
          tax service must not exceed the outstanding invoice balance, which is also inclusive of
          taxes.

      

This API creates and posts a credit memo. The credit memo has one credit memo line for each
        invoice line passed in the API request. The invoice balance reduces by a value equal to the
        credit memo’s balance. This API modifies the balance of a posted invoice or invoice line
        based on the specified credit application level for your org. See [Apply Credits to Posted Invoices or
          Invoice Lines](https://help.salesforce.com/s/articleView?id=sf.billing_setup_credit_application_level.htm&language=en_US).

    
      
        
          

**Special Access Rules**

          
: You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/invoiceId/actions/credit
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/3ttR000000008NEIAY/actions/credit
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoice​Id` | String | ID of the invoice to be credited partially or fully. The status of the invoice must be `Posted`. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: This example shows a sample request with the `Calculate` tax
            strategy.

```
{
  "type": "POSTED",
  "taxStrategy": "Calculate",
  "taxEffectiveDate": "2024-07-20",
  "effectiveDate": "2024-07-20",
  "description": "Credit Invoice",
  "invoiceLines": [
    {
      "invoiceLineId": "5TVR00000004SiqOBE",
      "amountToCredit": 5
    }
  ]
}
```

          
: This example shows a sample request with the `CopyFromInvoiceLine` tax
            strategy.

```
{
  "type": "POSTED",
  "taxStrategy": "CopyFromInvoiceLine",
  "effectiveDate": "2020-05-22",
  "description": "Credit Invoice",
  "invoiceLines": [
    {
      "invoiceLineId": "5TVR00000004SiqOBE",
      "amountToCredit": "5",
      "taxStrategy": "CopyFromInvoiceLine"
    }
  ]
}
```

          
: This example shows a sample request with the `ManualOverride` and `CopyFromInvoiceLine`
            tax strategies.

```
{
  "type": "POSTED",
  "taxStrategy": "ManualOverride",
  "taxEffectiveDate": "2021-08-01",
  "effectiveDate": "2021-08-01",
  "description": "Credit issued because product was malfunctioning.",
  "invoiceLines": [
    {
      "invoiceLineId": "5TVR00000004SiqOBE",
      "amountToCredit": 100,
      "taxStrategy": "ManualOverride",
      "taxEffectiveDate": "2021-08-01T21:22:41.000Z",
      "taxes": [
        {
          "taxAmount": 15,
          "taxName": "abc",
          "taxCode": "taxCode",
          "taxRate": 7
        }
      ],
      "addresses": {
        "billingAddress": {
          "street": "1 Market St #300",
          "city": "San Francisco",
          "state": "CA",
          "country": "US",
          "postalCode": "94105",
          "latitude": "37.789901",
          "longitude": "-122.396923"
        },
        "shippingAddress": {
          "street": "415 Mission St",
          "city": "San Francisco",
          "state": "CA",
          "country": "US",
          "postalCode": "94105",
          "latitude": "37.789901",
          "longitude": "-122.396923"
        }
      }
    },
    {
      "invoiceLineId": "5TVR00000004SiqOAE",
      "amountToCredit": 200,
      "taxStrategy": "CopyFromInvoiceLine"
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
| `description` | String | Description for the credit memo to be created. | Optional | 62.0 |
| `effective​Date` | String | Date when the credit memo takes effect. | Optional | 62.0 |
| `invoice​Lines` | [Credit Invoice Line Input](./connect_requests_credit_invoice_line_input.htm.md)[] | List of the invoice lines to be credited. The invoice line IDs must be related to the invoice ID specified in the API request. If invoice lines aren’t specified, the API request results in an error. | Required | 62.0 |
| `taxEffective​Date` | String | Date when the tax takes effect to recalculate the taxes. | Optional | 62.0 |
| `tax​Strategy` | String | Tax strategy to be applied across invoice lines. You can override the tax strategy at the individual invoice line level or at the tax line level. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `ManualOverride`—Specifies that the provided tax values must be considered for taxes. `CopyFromInvoiceLine`—Specifies that tax values must be copied from the invoice line. `Calculate`—Specifies that tax must be calculated by using the API. | Required | 62.0 |
| `type` | String | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Revenue Async Line
              Level](./connect_responses_revenue_async_line_level.htm.md)

=== ARTICLE: connect_resources_create_billing_schedules.htm ===
---
page_id: connect_resources_create_billing_schedules.htm
title: Create Billing Schedules for Orders (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_billing_schedules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Billing Schedules for Orders (POST)

Generate billing schedules for orders by using context
    service.

    
      
        
          

**Special Access Rules**

          
: 

The org must have the standard billing context definition with the target mapping.
              This context definition is available in orgs with Billing enabled. Additionally, you
              need the Create Billing Schedules From Billing Transactions API permission set and the
              Context Service Runtime permission set to use this API.

See these [requirements](https://help.salesforce.com/s/articleView?id=ind.billing_schedules_create.htm&language=en_US) to learn
              more about the configuration prerequisites.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/billing-schedules/actions/create
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/billing-schedules/actions/create
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
    "billingTransactionIds": [ "801xx000003H1H9AAK"]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Transaction​Ids` | String[] | ID of the billing transaction. This property value is the ID of the order if the source of the billing request is for the Order object. If the order product associated with the specified order ID doesn't have an associated billing treatment ID, the API considers the default billing treatment ID. The generated billing schedule group has the default billing treatment ID. The API supports only one billing transaction ID in the input. | Required | 62.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Context-Aware Billing
              Schedule](./connect_responses_context_aware_billing_schedule_output.htm.md)

=== ARTICLE: connect_resources_create_billing_schedules_from_any_transaction.htm ===
---
page_id: connect_resources_create_billing_schedules_from_any_transaction.htm
title: Create Standalone Billing Schedules (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_billing_schedules_from_any_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Standalone Billing Schedules (POST)

Generate billing schedules from any internal or external transaction
      by using context service.

    
      

You can create a billing schedule from any sObject such as WorkOrder, Cart, Order,
        Opportunity, and insurance policy. Or, you can also generate billing schedules from order
        items.

    

    

The Create Standalone Billing Schedules (POST) API uses the StandaloneBillingContext context
                definition to hydrate the context of the transaction. The context definition
                includes these mappings.

        
- The TransactionMapping maps the fields of the transaction to the attributes of the
                    Transaction node.

        
- The BSGEntitiesMapping maps the attributes of the Billing Schedule node, the Billing
          Schedule Group node, and Billing Schedule Group Relationship node to the fields of the
          corresponding Salesforce objects.

      

For the StandaloneBillingContext context definition to hydrate all the required data, transaction
                data for the mandatory context tags are required. Here are the topics that mention
                the mandatory and optional tags, sample transaction details, and sample payloads for
                various types of transactions.

        
- [One-Time New Sale Transaction](./connect_requests_billing_schedule_input_for_one_time_new_sale.htm.md)

        
- [Term-Defined New Sale
          Transaction](./connect_requests_billing_schedule_input_for_termed_new_sale.htm.md)

        
- [Evergreen New Sale Transaction](./connect_requests_billing_schedule_input_for_evergreen_new_sale.htm.md)

        
- [New Sale Transaction With
                        Bundled Products](./connect_requests_billing_schedule_input_for_bundled_products_new_sale.htm.md)

                
- [New Sale Transaction With
                        Ramped Products](./connect_requests_billing_schedule_input_for_ramps_new_sale.htm.md)

        
- [New Sale Transaction With Usage
                        Products](./connect_requests_billing_schedule_input_for_usage_new_sale.htm.md)

                
- [Amended Transaction](./connect_requests_billing_schedule_input_for_amendment.htm.md)

                
- [Renewal Transaction](./connect_requests_billing_schedule_input_for_renewal.htm.md)

                
- [Early Renewal
                        Transaction](./connect_requests_billing_schedule_input_for_early_renewal.htm.md)

                
- [Canceled
                    Transaction](./connect_requests_billing_schedule_input_for_cancellation.htm.md)

      

    

        
          

**Special Access Rules**

          
: This API is available with the Revenue Cloud Billing license.

        
      

        
          

**Resource**

          
: 
            

```
/commerce/invoicing/standalone/billing-schedules/actions/create
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/standalone/billing-schedules/actions/create
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "transactionDetails": "{\"nodeName\": [{\"id\":\"801Az00000aynKZIAY\", \"businessSobjectType\": \"Order\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "OrderTransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `transaction​ContextDetails` | [Standalone Billing Schedule Metadata Input](./connect_requests_context_aware_standalone_billing_schedule_metadata_input.htm.md)[] | Details of the context definition and its mappings that are used to hydrate the transaction data and save it in the appropriate Billing fields. | Required | 64.0 |
| `transaction​Details` | String | Input JSON data that includes the ID of the transaction record for which the billing schedule must be created and other additional transaction details. The API request supports a single mapping ID. You can send separate requests for line items and line details by using their respective mapping IDs. However, this approach can result in duplicate billing schedules for the same line items and line details. | Required | 64.0 |

          

        
      

    
      
        
          

**Response body for POST**

          
: [Context-Aware Billing
              Schedule](./connect_responses_context_aware_billing_schedule_output.htm.md)

        
      

    

  

#### See Also

- [Salesforce Help: Context Service](https://help.salesforce.com/s/articleView?id=ind.context_service_context_definitions.htm&language=en_US)

- [Industries Common Resources Developer Guide: Context Service](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/context_service_overview.htm)

- [BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)

=== ARTICLE: connect_resources_create_invoices_from_billing_schedules.htm ===
---
page_id: connect_resources_create_invoices_from_billing_schedules.htm
title: Invoice Creation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_invoices_from_billing_schedules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Creation (POST)

Create an invoice for an account, order, or a list of billing
      schedules.

    

This API request creates billing period items for the matching billing schedules.
        The billing period items are created for the period between the next charge date of the
        billing schedule and the specified target date. Invoice lines are created by processing
        these billing period items. These invoice lines are then grouped into invoices based on the
        defined grouping criteria on the billing schedule.

This API also applies any available
        credits on an account to settle an invoice and to reduce it's balance. To apply available
        credits, ensure the **Apply Credits to Posted Invoices** setting from
        Billing Settings is turned on.

    
      
        
          

**Special Access Rules**

          
: 

You need the Generate Invoices From Billing Schedule API, Billing Operations User, or Billing
              Customer Service permission set to use this API.

            

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/collection/actions/generate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/collection/actions/generate
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

#### Note

The `billing​TransactionId` property
              takes precedence over the `accountId` property followed by
              the `billing​ScheduleIds` property when
              values for these properties are specified in the input request.

          

          
: 
            

**JSON example**

: 

```
{
  "accountId": "001SG00000mYtRWYA0",
  "action": "Posted",
  "billingScheduleIds": [
    "44bSG000000CVeMYAW"
  ],
  "billingTransactionId": "801SG00000mYtaXYAS",
  "correlationId": null,
  "invoiceDate": "2024-01-12",
  "targetDate": "2024-01-12"
}
```

**Properties**

: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account record to create the invoices for. | Required if the `billing​ScheduleIds` or `billing​TransactionId` property isn’t specified. | 63.0 |
| `action` | String | Type of invoice to be created. Valid values are: `Draft` `Posted` | Required | 62.0 |
| `billing​ScheduleIds` | String[] | List of billing schedule IDs that’s used to create the invoices. You can specify a maximum of 200 billing schedules. | Required if the `accountId` or `billing​TransactionId` property isn’t specified. | 62.0 |
| `billing​TransactionId` | String | ID of the billing transaction record, which is the order ID, to create the invoices for. | Required if the `accountId` or `billing​ScheduleIds` property isn’t specified. | 63.0 |
| `correlation​Id` | String | Property that’s tagged against the published `InvoiceProcessedEvent` event, if specified. | Optional | 62.0 |
| `invoice​Date` | String | Stamping date of the invoice in ISO 8601 format. | Required | 62.0 |
| `target​Date` | String | Date in ISO 8601 format used to decide the billing periods that are included to create invoices. | Required | 62.0 |

          

          

        
        
          

**Response body for POST**

          
: [Revenue Async
              Response](./connect_responses_revenue_async_output.htm.md)

=== ARTICLE: connect_resources_create_payment_scheduler.htm ===
---
page_id: connect_resources_create_payment_scheduler.htm
title: Batch Payment Scheduler (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_payment_scheduler.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Payment Scheduler (POST)

Create a payment scheduler to automate and process payment runs on a
      recurring basis.

    
      
        
          

**Special Access Rules**

          
: You need the Payment Ops permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/payments/payment-schedulers/
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/payments/payment-schedulers/
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**JSON example**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
  "schedulerName": "Payment Scheduler",
  "startDate": "2022-01-01",
  "endDate": "2022-12-31",
  "preferredTime": "02:05:00.000",
  "frequencyCadence": "Monthly",
  "recursEveryMonthOnDay": "28",
  "criteriaMatchType": "MatchAny",
  "status": "Active",
  "filterCriteria": [
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "1",
      "criteriaSequence": 1
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "2",
      "criteriaSequence": 2
    },
    {
      "objectName": "PaymentScheduleItem",
      "fieldName": "PaymentRunMatchingValue",
      "operation": "Equals",
      "value": "3",
      "criteriaSequence": 3
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
| `criteria​MatchType` | String | Match type for the criteria of the payment scheduler. Valid values are: `Match Any` `Match None` | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `endDate` | String | End date of the payment scheduler. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `frequency​Cadence` | String | Frequency cadence of the payment scheduler. Valid values are: `Once` `Daily` `Weekly` `Monthly` | Required | 64.0 |
| `filter​Criteria` | [Payment Run Batch Filter Criteria Input](./connect_requests_payment_run_batch_filter_criteria_input.htm.md) | List of criteria that are used to filter the payment run details. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `preferredTime` | String | Preferred time for the payment scheduler run. | Required | 64.0 |
| `recursEvery​MonthOnDay` | String | Date when the payment scheduler recurs. | Required if the `frequencyCadence` property is set to `Monthly`. | 64.0 |
| `scheduler​Name` | String | Name of the payment scheduler. | Required | 64.0 |
| `startDate` | String | Start date of the payment scheduler. | Required | 64.0 |
| `status` | String | Status of the payment scheduler. Valid values are: `Active` `Canceled` `Draft` `Inactive` | Required | 64.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Batch Payments
              Scheduler](./connect_responses_payment_scheduler_output.htm.md)

=== ARTICLE: connect_resources_create_sequence_policy.htm ===
---
page_id: connect_resources_create_sequence_policy.htm
title: Create Sequence Policy (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_sequence_policy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Sequence Policy (POST)

Create a sequence policy to configure a unique, sequential number for
      posted invoices or credit memos.

    
      

A sequence policy ensures unique identification and systematic tracking of financial
        transactions, supporting regulatory compliance and preventing fraud. You can create a
        sequence policy for invoices or credit memos only.

    

    

## Special Access Rules

      
      

You need the Billing Admin permission set to use this API.

    

    
      
        
          

**Resource**

          
: 
            

```
/connect/sequences/policy
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/sequences/policy
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: This example shows a sample request to create a sequence
            policy.

```
{
  "name": "Sample Sequence Policy",
  "description": "This is a sample sequence policy.",
  "effectiveFromDateTime": "2025-08-10",
  "expirationDateTime": "2025-09-20",
  "isActive": true,
  "sequenceMode": "Basic",
  "targetObject": "Invoice",
  "dateStampFormat": "Yyyy",
  "sequenceStartNumber": 1,
  "incrementNumber": 1,
  "maximumSequenceNumber": 1000,
  "minimumSequenceNumberWidth": 2,
  "filterCriteria": "Custom",
  "selectionLogic": "selectionLogic",
  "sequencePattern": "INV-{SequenceValue}-abc",
  "selectionCondition": [
    {
      "filterField": "AppType",
      "operator": "Equals",
      "filterValue": "RLM",
      "conditionNumber": 1
    },
    {
      "filterField": "Status",
      "operator": "Equals",
      "filterValue": "Posted",
      "conditionNumber": 2
    },
    {
      "filterField": "LegalEntity",
      "operator": "Equals",
      "filterValue": "US",
      "conditionNumber": 3
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
| `dateStamp​Format` | String | Format of the stamp date that's appended to the sequence number. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `description` | String | Additional details about the sequence policy. | Optional | 65.0 |
| `effectiveFrom​DateTime` | String | Date and time when the policy becomes effective. The default value is the current date. | Required | 65.0 |
| `expiration​DateTime` | String | Date and time when the policy expires. | Optional | 65.0 |
| `filter​Criteria` | String | Criteria to filter the target objects. | Required | 65.0 |
| `increment​Number` | Integer | Value by which the sequence number increases until it reaches the maximum number. This value must be greater than or equal to `1`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `isActive` | Boolean | Indicates whether the policy is active (`true`) or not (`false`). The default value is `false`. | Required | 65.0 |
| `maximumSequence​Number` | Integer | Maximum number the sequence number can reach. | Optional | 65.0 |
| `minimumSequence​NumberWidth` | Integer | Minimum number of digits a sequence number must have. You can't edit this property by using the Update Sequence Policy API. | Optional | 65.0 |
| `name` | String | Name of the sequence policy. | Required | 65.0 |
| `selection​Condition` | [Selection Condition Input](./connect_requests_selection_condition_input.htm.md)[] | Criteria to determine which sequence policy is applied to a record. This property includes conditions based on any standard or custom fields of the record. | Optional | 65.0 |
| `selection​Logic` | String | Logic that determines the objects that the sequence policy applies to. | Optional | 65.0 |
| `sequence​Mode` | String | Specifies how sequence numbers are generated. Valid values are: `Basic`—Assigns sequential numbers without gap reconciliation. `Gapless`—Assigns sequential numbers with gap reconciliation. The usage of this value ensures that the posted invoices or credit memos don't have any numbering gaps for audits and compliance. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `sequence​Pattern` | String | Pattern structure that’s followed for the sequence. | Required | 65.0 |
| `sequenceStart​Number` | Integer | Starting value of the sequence number, which must be greater than or equal to `0`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `target​Object` | String | Object that the policy is applied to. Valid values are: `Invoice` `CreditMemo`—Available in API version 66.0 and later. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `timeZone` | String | Time zone that’s applicable for the sequence policy. | Optional | 65.0 |

          

        
        
          

**Response body for POST**

          
: [Sequence
              Policy](./connect_responses_sequence_policy_output.htm.md)

=== ARTICLE: connect_resources_credit_memo_apply.htm ===
---
page_id: connect_resources_credit_memo_apply.htm
title: Apply Credit Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_credit_memo_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apply Credit Memo (POST)

Adjust or correct already issued invoices by applying an existing
      credit memo to an invoice.

    

Specify the credit memo ID and the amounts to be applied, with the total of all
        applied amounts not exceeding the credit memo's balance.

The credit amount for each
        invoice can’t surpass the original charge or adjustment amount, and the overall credit
        amount must not exceed the invoice's outstanding balance. The exceptions include any taxes
        calculated by an external service.

For example, your organization sold 10 tablets at
        US$500 each, totaling $5000, to a vendor who later reported that 6 tablets were defective.
        Your accounts receivable team creates a $3000 credit memo by using the standalone Credit
        Memo API. Additionally, the team applies this credit to the original invoice by using the
        Apply Credit Memo API.

When the [credit application level is Invoice
          Line](https://help.salesforce.com/s/articleView?id=ind.billing_setup_credit_memo_features_enable.htm&language=en_US), this API applies the credit memo amount to all invoice lines starting from
        the highest amount until the full credit is applied or all lines are settled.

    
      
        
          

**Special Access Rules**

          
: You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit-memos/creditMemoId/actions/apply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/credit-memos/50gSG0000000XATYA2/actions/apply
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​Id` | String | ID of the credit memo record. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "applications": [
    {
      "appliedToId": "3ttxx000000003FAAQ",
      "amount": 10,
      "description": "Apply to invoice for refund",
      "effectiveDate": "2024-07-01"
    },
    {
      "appliedToId": "3ttxx0000000001AAA",
      "amount": 100
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `applications` | [Credit Memo Apply Application Input](./connect_requests_credit_memo_apply_application_input.htm.md)[] | List of one or more applications to apply the credit memo for. Each application represents an invoice that’s credited by using the balance of the specified credit memo. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Credit Memo Apply
              List](./connect_responses_credit_memo_apply_list_output.htm.md)

=== ARTICLE: connect_resources_credit_memo_invoice_application_unapply.htm ===
---
page_id: connect_resources_credit_memo_invoice_application_unapply.htm
title: Unapply Credit Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_credit_memo_invoice_application_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unapply Credit Memo (POST)

Unapply a credit memo from an invoice and return the invoice and the
      credit memo to their pre-application states.

    

Use this resource if an error occurred when a credit is issued. For example, if an incorrect
        credit memo is applied to an invoice, or if a credit memo is created for an incorrect
        amount, use this resource to unapply the credit memo.

    
      
        
          

**Special Access Rules**

          
: You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit-memo-inv-applications/creditMemoInvApplicationId/actions/unapply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/credit-memo-inv-applications/4sFSG000002nxPB2AY/actions/unapply
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​InvApplication​Id` | String | ID of the credit memo invoice application. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
    {
      "description": "Unapply credit memo from invoice to revert an error",
      "effectiveDate": "2024-07-01"
    }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Explanation or reason for unapplying the credit memo. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Credit Memo
              Unapply](./connect_responses_credit_memo_unapply_output.htm.md)

=== ARTICLE: connect_resources_credit_memo_line_level_apply.htm ===
---
page_id: connect_resources_credit_memo_line_level_apply.htm
title: Apply Credit Memo Line (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_credit_memo_line_level_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apply Credit Memo Line (POST)

Adjust or correct already issued invoices by applying an existing
      credit memo line to an invoice line.

    
      
        
          

**Special Access Rules**

          
: You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit-memo-lines/creditMemoLineId/actions/apply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/credit-memo-lines/9yxSG0000000LUHYA2/actions/apply
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​LineId` | String | ID of the credit memo line record. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```

{
 "applyCreditDetails": [
 {
 "invoiceLineId": "5TVSG0000002ZJR4A2",
 "appliedAmount": 5,
 "description": "Apply to invoice line 1",
 "effectiveDate": "2024-07-01"
 },
 {
 "invoiceLineId": "5TVSG0000002ZJS4A2",
 "appliedAmount": 10,
 "description": "Apply to invoice line 2",
 "effectiveDate": "2024-07-01"
 }
 ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `applyCredit​Details` | [Credit Memo Line Application Input](./connect_requests_credit_memo_line_application_input.htm.md)[] | List of one or more applications to apply the credit memo line for. Each application represents an invoice line that’s credited by using the balance of the specified credit memo line. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Credit Memo Line
              Applied](./connect_responses_credit_memo_line_applied.htm.md)

=== ARTICLE: connect_resources_credit_memo_line_level_unapply.htm ===
---
page_id: connect_resources_credit_memo_line_level_unapply.htm
title: Unapply Credit Memo Line (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_credit_memo_line_level_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unapply Credit Memo Line (POST)

Unapply a credit memo line from an invoice line and return the invoice
      line and the credit memo line to their pre-application states.

    
      
        
          

**Special Access Rules**

          
: You need the Credit Memo Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit-memo-line-invoice-line/creditMemoLineInvoiceLineId/actions/unapply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/credit-memo-line-invoice-line/4sGSG0000002kQ92AI/actions/unapply
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​LineInvoice​LineId` | String | ID of the credit memo line invoice line record. | Required | 62.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
 "description": "Unapply a credit memo line from invoice line 1",
 "effectiveDate": "2024-07-01"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Explanation or reason for unapplying the credit memo line. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo line. | Optional | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Credit Memo Line
              Unapplied](./connect_responses_credit_memo_line_unapplied.htm.md)

=== ARTICLE: connect_resources_draft_to_posted_invoice.htm ===
---
page_id: connect_resources_draft_to_posted_invoice.htm
title: Invoice Draft to Posted Status (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_draft_to_posted_invoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Draft to Posted Status (POST)

Update the status of the invoice from Draft to
    Posted.

    

This API calls an external tax engine or provides information to your tax adapter implementation
        to calculate taxes for the draft invoice, post the invoice, and update the related billing
        schedules and billing periods.

        
          

**Special Access Rules**

          
: You need the Billing Operations User permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/collection/actions/post
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/collection/actions/post
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
  "invoiceIds": ["3ttxx0000004CIjAAM"]
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Splunk correlation ID to track the messages that are related to the request and are logged in Splunk by the different services involved in the request. If the ID isn’t specified, the service creates a random Universally Unique Identifier (UUID). | Optional | 62.0 |
| `invoiceIds` | String[] | IDs of the invoice records in `Draft` status to be posted. You can post one draft invoice per API request. | Required | 62.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Revenue Async Response](./connect_responses_revenue_async_output.htm.md)

=== ARTICLE: connect_resources_generate_account_statement.htm ===
---
page_id: connect_resources_generate_account_statement.htm
title: Generate Account Statement (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_generate_account_statement.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Generate Account Statement (POST)

Generate comprehensive account statement with transaction history and
      balance information.

    

An account statement includes these details.

        
- Transaction History—List of all financial transactions, such as invoices, credit
          memos, debit memos, payments, and refunds, within a specified date range.

        
- Open Balances—Non-zero balances for invoices and other transactions.

        
- Account Summary—Aggregated totals including beginning balance, total charges,
          total payments, and ending balance.

        
- Multi-currency Support—Transactions across multiple currencies.

      

        
          

**Resource**

          
: 
            

```
/revenue/billing/accounts/accountId/statement
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/billing/accounts/accountId/statement
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
  "shouldShowOpenBalancesOnly": false,
  "startDate": "2025-09-01",
  "transactionTypes": {
    "transactionTypes": [
      "Invoice"
    ]
  },
  "sortBy": "DueDate",
  "sortingOrder": "Ascending",
  "associatedAccountIds": {
    "associatedAccountIds": [
      "001xx000003DGb5AAG",
      "001xx000003DGb6AAG"
    ]
  },
  "documentTemplateId": "0TRxx000000002YGAQ",
  "correlationId": "monthly-statement-sept-2025",
  "customFields": "{\"Invoice\": [\"TotalAmountWithTax\"], \"Account\": {\"base\": [\"Phone\", \"Fax\"], \"associated\": [\"Website\"]}}}"
}
```

**Properties**

: 

                  
                    

                    

                    

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

```

```

                    

                    

                  

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
| `associatedAccountIds` | String[] | List of associated account IDs from hierarchy to include in the statement. You can specify up to 50 accounts. | Optional | 66.0 |
| `correlationId` | String | Correlation ID for tracking the request across systems. | Optional | 66.0 |
| `customFields` | String | JSON string specifying custom fields to include in the statement. As a best practice, we recommend that you limit the number of custom fields up to 30 fields. Valid objects to specify the associated fields are: Invoice CreditMemo Payment DebitMemo Refund Account Here's the expected format.{"Invoice": ["field1", "field2"], "Account": {"base": ["field1"], "associated": ["field2"]}} | Optional | 67.0 |
| `documentTemplateId` | String | Document template ID to use for PDF generation. If you don’t specify a value, the system auto-resolves by using the default template. | Optional | 66.0 |
| `shouldShowOpenBalancesOnly` | Boolean | Indicates whether to show open balances only (`true`) or not (`false`). If set to `true`, the API shows only accounts with non-zero balances. If set to `false`, this API shows complete transaction history within the date range from the start date. | Optional | 66.0 |
| `sortBy` | String | Criteria for sorting transactions. The default and valid value is `Date`. | Optional | 66.0 |
| `sortingOrder` | String | Sort order for transactions. Valid values are: `Ascending` `Descending` The default value is `Descending`. | Optional | 66.0 |
| `startDate` | String | Start date for the transaction history. The required format is `YYYY-MM-DD`. The system processes records up to 90 days from this date. | Required | 66.0 |
| `transactionTypes` | String[] | List of transaction types to include in the statement. If you don’t specify a value or the value is empty, all transaction types are included. Valid values are: `All` `CreditMemo` `DebitMemo` `Invoice` `Payment` `Refund` | Optional | 66.0 |

          

        
        
          

**Response body for POST**

          
: [Account Statement
              Response](./connect_responses_statement_of_account_output.htm.md)

=== ARTICLE: connect_resources_generate_documents.htm ===
---
page_id: connect_resources_generate_documents.htm
title: Generate On-Demand Invoice Document (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_generate_documents.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Generate On-Demand Invoice Document (POST)

Generate an invoice document for a record, and update any junction
      object record.

    
      
        
          

**Resource**

          
: 
            

```
/revenue/billing/document/actions/generate
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/billing/document/actions/generate
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
  "recordId": "3ttasd98776266777",
  "shouldForceRegenerate": true,
  "documentTemplateId": "0694x000000XyzABC",
  "documentTitle": "DOC-00000012",
  "tokenData": "{\"InvoiceLines\":{\"StartDate\":\"02/21/2025\",\"IsUsageBasedInvoiceLine\":false,\"UnitPrice\":\"$7.99\",\"ProductName\":\"Mouse\",\"UsageProductId\":\"01tSG00000BHFPSYA5\",\"Subtotal\":\"$7.99\",\"Quantity\":\"1\",\"Tax\":\"$0.00\",\"Id\":\"5TVSG000000DU3V4AW\",\"CurrencyIsoCode\":\"USD\",\"EndDate\":\"02/21/2025\"},\"NetCreditsApplied\":\"$0.00\",\"CompanyEmail\":\"rsamantaray@salesforce.com\",\"CompanyState\":\"CA\",\"DocumentNumber\":\"DOC-000000001\",\"SubTotal\":\"$7.99\",\"CompanyStreet\":\"1 Market St\",\"CompanyName\":\"260.1\",\"TotalAmnt\":\"$7.99\",\"TotalTax\":\"$0.00\",\"InvoiceDueDate\":\"10/08/2025\",\"CompanyPostalCode\":\"94105\",\"InvoiceDate\":\"09/08/2025\",\"CompanyCity\":\"San Francisco\",\"CompanyCountry\":\"US\",\"AccountName\":\"Sonia BAT Account\"}"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `documentTemplateId` | String | Document template ID to use for PDF generation. The document template must be active with UsageType as `INVOICE` If you don't specify this value, the system auto-resolves by using the default template. | Optional | 66.0 |
| `documentTitle` | String | Custom title for the generated document. If you don't specify a value, the value is auto-generated. | Optional | 66.0 |
| `recordId` | String | Record ID of the object the document is generated for. You can specify invoice ID only. | Required | 66.0 |
| `shouldForceRegenerate` | Boolean | Indicates whether to regenerate the document (`true`) or not (`false`). If set to `true`, this API generates a document, replacing any existing ones. If set to `false`, this API skips the generation of document if invoice already has an associated document. The default value is `false`. | Optional | 66.0 |
| `tokenData` | String | Token data to generate the document. | Optional | 66.0 |

          

        
        
          

**Response body for POST**

          
: [On-Demand Document
              Generation Response](./connect_responses_on_demand_doc_gen_output.htm.md)

=== ARTICLE: connect_resources_get_billing_arrangement.htm ===
---
page_id: connect_resources_get_billing_arrangement.htm
title: Billing Arrangement (GET)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_get_billing_arrangement.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Arrangement (GET)

Retrieve a billing arrangement and its associated billing arrangement
    lines.

    
      

This API fetches billing information, including the split percentage allocation for
        accounts, the remainder percentage, and whether adjustments are applied to the owning
        account.

    

    
      
        
          

**Resource**

          
: 
            

```
/revenue/billing/billing-arrangement/billingArrangementId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/billing/billing-arrangement//revenue/billing/billing-arrangement/1bdxx000000004rAAA
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameter for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​ArrangementId` | String | Unique ID of the billing arrangement to retrieve. | Required | 66.0 |

          

        
        
          

**Response body for GET**

          
: [Billing Arrangement](./connect_responses_billing_arrangement_output.htm.md)

=== ARTICLE: connect_resources_invoice_batch_docgen.htm ===
---
page_id: connect_resources_invoice_batch_docgen.htm
title: Batch Invoices Document Generation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_invoice_batch_docgen.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoices Document Generation (POST)

Asynchronously generate PDF documents for the invoices that are in the
        `Draft` or `Posted`
      status and are associated with an invoice batch run record.

    
      
        
          

**Special Access Rules**

          
: This API is available with Revenue Cloud Billing. To use this API, enable Document
            Generation for Billing. Additionally, you need either the Billing Operations User
            permission set or the Billing Admin permission set, along with the Docgen Designer
            permission set and Docgen Designer Standard User permission set.

        
        
          

**Resource**

          
: 
            

```
/commerce/billing/invoices/invoice-batch-docgen/invoiceBatchRunId/actions/actionName
```

          

          
: 
            
              
- The invoiceBatchRunId parameter is the ID of the invoice batch
                run record that created the `Draft` or `Posted` invoices.

              
- The actionName parameter is the name of the action you want to
                perform on the specified invoice batch run record.

            

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/invoices/invoice-batch-docgen/5KPxx0025063GSmSAX/actions/run
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Response body for POST**

          
: [Batch Invoice
              Document Generation](./connect_responses_batch_invoice_doc_gen_output.htm.md)

=== ARTICLE: connect_resources_invoice_batch_docgen_retry.htm ===
---
page_id: connect_resources_invoice_batch_docgen_retry.htm
title: Batch Invoices Document Generation Retry (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_invoice_batch_docgen_retry.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoices Document Generation Retry (POST)

Asynchronously regenerate PDF documents for the invoices that are in
      the `Draft` or `Posted`
      status and failed in an earlier invoice batch run.

    
      
        
          

**Special Access Rules**

          
: This API is available with Revenue Cloud Billing. To use this API, enable Document
            Generation for Billing. Additionally, you need either the Billing Operations User
            permission set or the Billing Admin permission set, along with the Docgen Designer
            permission set and Docgen Designer Standard User permission set.

        
        
          

**Resource**

          
: 
            

```
/commerce/billing/invoices/invoice-batch-docgen/invoiceBatchRunId/actions/actionName
```

          

          
: 
            
              
- The invoiceBatchRunId parameter is the ID of the invoice batch
                run record that created the `Draft` or `Posted` invoices.

              
- The actionName parameter is the name of the action you want to
                perform on the specified invoice batch run record. In this case, the action is to
                retry generating the `Draft` or `Posted` invoices that failed earlier.

            

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/invoices/invoice-batch-docgen/5IRxx0000004GSmGAM/actions/retry
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Response body for POST**

          
: [Batch Invoice
              Document Generation](./connect_responses_batch_invoice_doc_gen_output.htm.md)

=== ARTICLE: connect_resources_invoices_ingestion.htm ===
---
page_id: connect_resources_invoices_ingestion.htm
title: Invoice Ingestion (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_invoices_ingestion.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Ingestion (POST)

Ingest or generate an invoice from an internal or external billing
      transaction data.

Create invoices from any external or internal transaction. For example, create invoices by using
        external orders, policies, quotes, or internal data, such as assets or quotes.

You can also perform these additional tasks.

      
        
- Ingest invoices from any external system into Billing to manage invoice operations such
          as issuing credits against an invoice or voiding an invoice.

        
- Generate invoices from debit memos from API version 66.0 and later.

      

Keep these considerations in mind when you use this API.

        
- If the Convert Negative Invoice Lines to Credit Memo Lines feature isn’t enabled, use
          the [Negative Invoice Lines to Credit
            Conversion API](./connect_resources_convert_negative_invoice_lines_to_credit.htm.md) to create a credit memo against an ingested negative invoice
          line.

        
- Use the [Apply Credit Action](./actions_obj_run_apply_credit.htm.md) to
          apply a credit memo to an invoice.

        
- To ingest legacy invoices, create at least one invoice line.

        
- To generate invoices from debit memos, specify the debit memo ID as the `referenceEntityId` property value in the request body of
          this API. Make sure that the debit memo is in `Posted`
          status and is ready for invoice generation. The invoice is generated in `Draft` status.

      

        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/collection/actions/ingest
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/collection/actions/ingest
```

          

        
        
          

**Available version**

          
: 63.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            
        
          

**
JSON example to ingest a draft invoice with a tax callout**

          
: 
            

```
{
  "invoices": [
    {
      "shouldCalculateTax": true,
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "CreateInvoice",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refContact",
            "record": {
              "attributes": {
                "type": "Contact",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "@{refAccount.Id}",
              "billToContactId": "@{refContact.Id}",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "Sample Invoice",
              "uniqueIdentifier": "5873af8f-f007-4aa0-9e3d-53a08c3f59de"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": 7.25,
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "kl",
              "description": "Associated tax line.",
              "invoiceLineId": "@{refInvoiceLine1.id}"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine2.id}",
              "description": "Associated tax line."
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to ingest a draft invoice without a tax callout**

          
: 
            

```
{
  "invoices": [
    {
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "123",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "TestExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "@{refAccount.Id}",
              "billToContactId": "003xx000004Wk8qAAC",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "testInvoice",
              "uniqueIdentifier": "c76011a1-e113-49d9-9c54-3b5c68950ada"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": 7.25,
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "kl",
              "description": "description for tax Line",
              "invoiceLineId": "@{refInvoiceLine1.id}"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine2.id}",
              "description": "description for tax Line"
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to ingest posted invoices**

          
: 
            

```
{
  "invoices": [
    {
      "taxCalculationStatus": "Posted",
      "graph": {
        "graphId": "123",
        "records": [
          {
            "referenceId": "refAccount",
            "record": {
              "attributes": {
                "type": "Account",
                "method": "GET",
                "id": "ExternalId__c/123"
              }
            }
          },
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "billingAccountId": "001SG00000njpF3YAI",
              "billToContactId": "003xx000004Wk8qAAC",
              "paymentTermId": "2OXxx0000004CFUGA2",
              "referenceEntityId": "801xx000003GeQQAA0",
              "status": "Posted",
              "invoiceDate": "2024-12-19",
              "currencyIsoCode": "USD",
              "dueDate": "2024-12-19",
              "invoiceNumber": "DOC-10",
              "description": "Sample Invoice",
              "uniqueIdentifier": "9994b2c4-c0c3-47c3-806f-ae6e1f16bac3"
            }
          },
          {
            "referenceId": "refBillingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShippingAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "123 Main St",
              "city": "NewYork",
              "postalCode": "10001",
              "state": "New York",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refShipFromAddress",
            "record": {
              "attributes": {
                "type": "InvoiceAddressGroup",
                "method": "POST"
              },
              "street": "1 Market Street",
              "city": "San Francisco",
              "postalCode": "94105",
              "state": "CA",
              "country": "US",
              "longitude": "123.456",
              "latitude": "78.910",
              "invoiceId": "@{refInvoice.id}"
            }
          },
          {
            "referenceId": "refInvoiceLine1",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName1",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-13",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx0000000BOTAA2",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLine2",
            "record": {
              "attributes": {
                "type": "InvoiceLine",
                "method": "POST"
              },
              "name": "productName2",
              "product2Id": "01txx0000006ic4AAA",
              "invoiceLineStartDate": "2024-11-10",
              "invoiceLineEndDate": "2024-11-15",
              "quantity": "10",
              "unitPrice": "10",
              "chargeAmount": "100",
              "invoiceId": "@{refInvoice.id}",
              "referenceEntityItemId": "802xx000001neB9AAI",
              "billingAddressId": "@{refBillingAddress.id}",
              "shippingAddressId": "@{refShippingAddress.id}",
              "shipFromAddressId": "@{refShipFromAddress.id}",
              "taxTreatmentId": "1ttxx00000001DpAAI",
              "legalEntityId": "0fwxx0000000001AAA",
              "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE"
            }
          },
          {
            "referenceId": "refInvoiceLineTax1",
            "record": {
              "attributes": {
                "type": "InvoiceLineTax",
                "method": "POST"
              },
              "taxAmount": "10",
              "taxCode": "CA-94121",
              "taxName": "CALIFORNIA",
              "taxRate": 0.25,
              "taxEffectiveDate": "2024-11-10",
              "taxDocumentNumber": "123",
              "taxExemptAmount": 0,
              "taxTransactionNumber": "125",
              "invoiceLineId": "@{refInvoiceLine1.id}",
              "description": "Associated tax line."
            }
          }
        ]
      }
    }
  ]
}
```

          

        
        
          

**JSON example to generate invoices from debit memos**

          
: 
            

```
{
  "invoices": [
    {
      "shouldCalculateTax": true,
      "taxCalculationStatus": "Estimated",
      "graph": {
        "graphId": "CreateInvoice",
        "records": [
          {
            "referenceId": "refInvoice",
            "record": {
              "attributes": {
                "type": "Invoice",
                "method": "POST"
              },
              "accountId": "001SB00001V3RxNYAV",
              "billToContactId": "003xx000004WhUQAA0",
              "referenceEntityId": "4DmAAC000008UP70BM",
              "status": "Draft",
              "invoiceDate": "2024-12-19",
              "dueDate": "2024-12-19",
              "description": "Sample Invoice"
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
| `invoices` | [Invoice Ingestion Input](./connect_requests_invoice_ingestion_input.htm.md)[] | List of invoices to be generated or ingested, enabling the submission and processing of multiple invoices in a single request. This API supports one invoice per request. To send 25 requests at a time, see the [Composite Batch request](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/requests_composite_batch.htm). | Required | 63.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Invoice
              Ingestion](./connect_responses_invoices_ingestion_output.htm.md)

=== ARTICLE: connect_resources_payment_line_apply.htm ===
---
page_id: connect_resources_payment_line_apply.htm
title: Payment Line Apply (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_payment_line_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Apply (POST)

Allocate the balance of a payment to reduce the balance of an invoice.
      The response includes an ID of the payment line invoice or payment line invoice line that
      represents the payment balance allocated against the invoice.

      

Use the Commerce Payments APIs to send your payment and
        refund details to external payment gateways for processing against a customer's bank. See
          [Commerce Payments resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm)
        to check the APIs for payment gateways, payment captures, and payment authorizations.

**Resource**

: 

```
/commerce/billing/payments/paymentId/actions/apply
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/payments/1PLR000000000dDOAQ/actions/apply
```

**Available version**

: 64.0

**HTTP methods**

: POST

        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `paymentId` | String | ID of the payment record. | Required | 64.0 |

          

        

**Request body for POST**

: 

**JSON example**

: 

```
{
  "appliedToId": "3ttR000000001IkIAI",
  "amount": 10,
  "effectiveDate": "2020-08-11T07:53:15.000Z",
  "comments": "Apply payment",
  "associatedAccountId": "001R00000060AyuIAE"
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount that's applied. The amount must be less than the invoice line and payment balance. | Required | 64.0 |
| `applied​ToId` | String | ID of the invoice line that this payment is applied to. Specify the IDs for these records. Invoice Invoice Line | Required | 64.0 |
| `associated​AccountId` | String | ID of the associated account. | Optional | 64.0 |
| `comments` | String | Comments that you can add to the payment line application. | Optional | 64.0 |
| `effective​Date` | String | Date from which the payment line application takes effect. | Optional | 64.0 |

**Response body for POST**

: [Payment Line Apply](./connect_responses_payment_line_apply_output.htm.md)

=== ARTICLE: connect_resources_payment_line_unapply.htm ===
---
page_id: connect_resources_payment_line_unapply.htm
title: Payment Line Unapply (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_payment_line_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Unapply (POST)

Revert the application of a payment line from an invoice, and return the
      payment and invoices to their preapplication state. Use this API to correct an input during
      the payment application process.

For example, you can use this API to revert an incorrect payment that's applied to an
        invoice, or to rectify an incorrect amount.

      

Use the Commerce Payments APIs to send your payment and
        refund details to external payment gateways for processing against a customer's bank. See
          [Commerce Payments resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm)
        to check the APIs for payment gateways, payment captures, and payment authorizations.

        
          

**Resource**

          
: 
            

```
/commerce/billing/payments/paymentId/paymentlines/paymentLineId/actions/unapply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/payments/0aQ1j000000001O/paymentlines/1PLR000000000dDOAQ/actions/unapply
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameters for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `paymentId` | String | ID of the payment record. | Required | 64.0 |
| `payment​LineId` | String | ID of the payment line record. | Required | 64.0 |

          

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "effectiveDate": "2025-05-22T11:30:25.000Z",
  "comments": "Unapply payment"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `comments` | String | Comments that you can add when you revert a payment line application. | Optional | 64.0 |
| `effective​Date` | String | Date from when the reversal of the payment line application is in effect. | Optional | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Payment Line
              Unapply](./connect_responses_payment_line_unapply_output.htm.md)

=== ARTICLE: connect_resources_post_draft_credit_memo.htm ===
---
page_id: connect_resources_post_draft_credit_memo.htm
title: Post a Draft Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_post_draft_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Post a Draft Memo (POST)

Post a draft credit memo to a credit memo record for review and
      approval.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/credit/collection/actions/post
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v65.0/commerce/invoicing/credit/collection/actions/post
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
"creditMemoIds": ["50gDU00000001MnYAI"]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Splunk correlation ID to use to track messages that are related to the request and logged in Splunk by the different services involved in the request. If not specified, the service creates a random Universally Unique Identifier (UUID). | Optional | 65.0 |
| `creditMemoIds` | String[] | ID of the credit memo record in `Draft` status to be posted. You can post one draft credit memo per API request. | Required | 65.0 |

          

        
        
          

**Response body for POST**

          
: [Credit Memo
              Post](./connect_responses_credit_memo_post_output.htm.md)

=== ARTICLE: connect_resources_preview_invoices.htm ===
---
page_id: connect_resources_preview_invoices.htm
title: Invoice Preview (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_preview_invoices.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Preview (POST)

Generate preview invoices, which includes the estimated tax amounts,
      for a billing transaction for the next two billing periods.

    

Invoice preview provides details of the upcoming invoices for orders or quotes within the
        system.

        
          

**Special Access Rules**

          
: 

You need the Billing Operations User or Billing Customer Service permission set to
              use this API.

See these [requirements](https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_procedure_plan_create.htm&language=en_US) to learn
              more about the configuration prerequisites.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/collection/actions/preview
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/collection/actions/preview
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
    "billingTransactionId": "801Z600000004LoIAI",
    "numberOfBillingPeriods": 2,
    "previewDate": "2024-12-04"
}
```

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​TransactionId` | String | ID of the record to generate the preview invoices for. | Required | 63.0 |
| `numberOf​BillingPeriods` | Integer | Number of billing periods that the invoice preview is generated for. If unspecified, the default value is `2`. | Optional | 64.0 |
| `preview​Date` | String | The date on which the preview invoice is generated. For the first invoice, the preview date is the target date for generating the invoice. For the second invoice, the target date is calculated based on the preview date and the minimum billing frequency of the transactions. The default value is the current date. | Optional | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Invoice
              Preview](./connect_responses_invoice_preview_output.htm.md)

=== ARTICLE: connect_resources_recover_billing_schedules.htm ===
---
page_id: connect_resources_recover_billing_schedules.htm
title: Billing Schedule Recovery List (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_recover_billing_schedules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Schedule Recovery List (POST)

Recover the latest generated invoice associated with the billing
      schedules in the `Error` or `Processing` status.

    

Billing schedules include critical details such as the amount to be billed, next billing date,
        and status. An invoice can be associated with one or more billing schedules. When an invoice
        is generated or posted, the billing schedules are updated to reflect the accurate state of
        the invoice. The billing schedules associated with an invoice are marked in the `Error` status if any of the invoicing processes have errors.
        Use this API to recover the invoice associated with the billing schedules in the `Error` or `Processing`
        status.

    
      
        
          

**Special Access Rules**

          
: You need the Manage Errors Using Invoice Error Recovery API permission set to use this
            API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/billing-schedules/collection/actions/recover
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/billing-schedules/collection/actions/recover
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
    "billingScheduleIds": ["44bDU00000000XXYAY"]
  }
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Schedule​Ids` | String[] | IDs of the billing schedules to recover the invoice for. You can recover one billing schedule per API request. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Billing Schedule
              Recovery List](./connect_responses_billing_schedule_recovery_list_output.htm.md)

=== ARTICLE: connect_resources_recover_errored_invoices_batch_run.htm ===
---
page_id: connect_resources_recover_errored_invoices_batch_run.htm
title: Invoice Run Recovery (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_recover_errored_invoices_batch_run.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Run Recovery (POST)

Recover records associated with a failed invoice run. Recovery is
      required only when billing schedules remain in the `Processing`, `Void In Progress`, or `Error` status.

    
      
        
          

**Special Access Rules**

          
: To use this API, you need the Invoice Scheduler API permission set.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoice-batch-runs/invoiceBatchRunId/actions/recover
```

          

          
: The invoiceBatchRunId parameter is the ID of the failed invoice
            batch run record whose details you want to retrieve.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoice-batch-runs/5IRxx0000004TwGGAU/actions/recover
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Response body for POST**

          
: [Invoice Batch Run Recovery](./connect_responses_invoice_batch_run_recovery_output.htm.md)

=== ARTICLE: connect_resources_resume_billing.htm ===
---
page_id: connect_resources_resume_billing.htm
title: Resume Billing (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_resume_billing.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resume Billing (POST)

Resume billing for billing schedule groups or an account that’s
      currently on hold.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/actions/resume-billing
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/actions/resume-billing
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
    "referenceIds":
    [
        {
          "referenceId": "001DU000001o2UwYAI",
          "resumeDate": "2024-11-27"
        }
    ]
 
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceIds` | [Resume Billing Object Input](./connect_requests_resume_billing_entity_input.htm.md)[] | Input representation of the account or billing schedule group IDs to resume the billing operation for. | Required | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Suspend Resume
              Billing](./connect_responses_suspend_resume_billing_output.htm.md)

=== ARTICLE: connect_resources_rules_application.htm ===
---
page_id: connect_resources_rules_application.htm
title: Rules Application (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_rules_application.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rules Application (POST)

Apply payments and credits to an account's invoices based on specified
      rules defined on the Billing Settings page.

This API uses predefined logic to allocate payments and credits, reducing any manual
        intervention and errors.

        
          

**Resource**

          
: 
            

```
/revenue/billing/transactions/actions/apply
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/revenue/billing/transactions/actions/apply
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
  "accountId": "001xx000003DGbQAAW",
  "targetDate": "2024-01-15"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account to perform the settlement of payments and credits against invoices in adherence with the applied rules. | Required | 66.0 |
| `targetDate` | String | The date used to select invoices and invoice lines with a posted date equal to or later than the target date to apply payments and credits. | Optional | 66.0 |

          

        
        
          

**Response body for POST**

          
: [Rules
              Application](./connect_responses_rules_application_output.htm.md)

=== ARTICLE: connect_resources_send_email_for_invoice_batch_run.htm ===
---
page_id: connect_resources_send_email_for_invoice_batch_run.htm
title: Send Emails for Posted Invoices (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_send_email_for_invoice_batch_run.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Send Emails for Posted Invoices (POST)

Send emails for the posted invoices of a specified invoice batch run
      ID.

    
      

Each email includes a custom message template in the email body and an attachment of the
        Invoice Document PDF. The email template is based on the user preferences defined on the
        Billing Profile, Legal Entity, or Billing Settings page.

    

    

## Special Access Rules

      
      

Enable the **Configure Email Delivery Settings** toggle from the Billing
        Settings page from Setup.

    

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoice-batch-runs/actions/send-email
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoice-batch-runs/actions/send-email
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
  "invoiceBatchRunId": "5IRLT000001SIJB4A4"
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceBatchRunId` | String | ID of the invoice batch run record to send emails for the posted invoices of an invoice batch run. | Required | 65.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Send Email
              Response](./connect_responses_send_email_for_invoice_batch_run_output.htm.md)

=== ARTICLE: connect_resources_sequences_assignment.htm ===
---
page_id: connect_resources_sequences_assignment.htm
title: Sequence Assignment (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_sequences_assignment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Assignment (POST)

Assign sequence pattern values to objects based on the configured
      sequence policy.

    

## Special Access Rules

      
      

You need the Billing Admin permission set to use this API.

    

**Resource**

: 

```
/connect/sequences/actions/assign
```

**Resource example**

: 

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/sequences/actions/assign
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
  "targetObjectIds": [
    "3ttxx00000005nhAAA",
    "3ttxx00000006bhAAA"
  ],
  "sequencePolicyId": "1Vdxx0000004CFU"
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequence​PolicyId` | String | ID of the sequence policy. | Optional | 65.0 |
| `shouldPublish​Platform​Event` | Boolean | Indicates whether to publish a platform event when a sequence is assigned to a target record (`true`) or not (`false`). | Optional | 65.0 |
| `target​ObjectIds` | String[] | List of records to which the sequence pattern values are assigned. | Required | 65.0 |

**Response body for POST**

: [Sequences Assignment](./connect_responses_sequences_assignment_output.htm.md)

=== ARTICLE: connect_resources_sequences_gap_reconciliation.htm ===
---
page_id: connect_resources_sequences_gap_reconciliation.htm
title: Sequence Gap Reconciliation (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_sequences_gap_reconciliation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Gap Reconciliation (POST)

Restore a missing sequence value identified by using this API in
      gapless-enabled sequences. This sequence value can be used later in the subsequent sequence
      policy numbering, ensuring there are no gaps.

    

## Special Access Rules

      
      

You need the Billing Admin permission set to use this API.

    

    
      
        
          

**Resource**

          
: 
            

```
/connect/sequences/gap-reconciliation
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/sequences/gap-reconciliation
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: This example shows a sample request that specifies the list of sequence policies for gap
            reconciliation.

```
{
  "sequencePolicyIds": [
    "1vdxx0000000abc",
    "1vdxx0000000def"
  ]
}
```

          
: This example shows a sample request that specifies the target invoice object for gap
            reconciliation.

```
{
  "targetObjects": [
    "Invoice"
  ]
}
```

**Properties**

: 

- 
- 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequence​PolicyIds` | String[] | List of IDs of the sequence policies. | Required if the `targetObjects` property isn't specified. You must not specify both properties. | 65.0 |
| `target​Objects` | String[] | List of objects to which the policies are applied. Valid values are: `Invoice` `CreditMemo`—Available in API version 66.0 and later. | Required if the `sequencePolicyIds` property isn't specified. You must not specify both properties. | 65.0 |

          

        
        
          

**Response body for POST**

          
: [Sequence Gap Reconciliation](./connect_responses_sequence_gap_reconciliation_output.htm.md)

=== ARTICLE: connect_resources_suspend_billing.htm ===
---
page_id: connect_resources_suspend_billing.htm
title: Suspend Billing (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_suspend_billing.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Billing (POST)

Suspend billing for billing schedule groups or an account for a
      predefined period.

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/actions/suspend-billing
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/actions/suspend-billing
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
    "referenceIds": 
    [
        {
            "referenceId": "001DU000001o2UwYAI",
            "suspendDate": "2024-11-27",
            "resumeDate": "2024-12-27"
        }
    ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceIds` | [Suspend Billing Object Input](./connect_requests_suspend_billing_entity_input.htm.md)[] | Input representation of the account or billing schedule group IDs to suspend the billing operation for. | Required | 63.0 |

          

        
        
          

**Response body for POST**

          
: [Suspend Resume
              Billing](./connect_responses_suspend_resume_billing_output.htm.md)

=== ARTICLE: connect_resources_update_payment_scheduler.htm ===
---
page_id: connect_resources_update_payment_scheduler.htm
title: Payment Scheduler Update (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_update_payment_scheduler.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Scheduler Update (PATCH)

Activate or deactivate a payment scheduler. You can set the status of
      a payment scheduler to `Active`, `Canceled`, `Draft`, or
        `Inactive`.

    
      
        
          

**Special Access Rules**

          
: You need the Payment Ops permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/payments/payment-schedulers/billingBatchSchedulerId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/payments/payment-schedulers/5BSxx0000004TwGGAU
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: PATCH

        
        
          

**Path parameter for POST**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billingBatch​SchedulerId` | String | ID of the payment scheduler record. | Required | 64.0 |

          

        
        
          

**Request body for PATCH**

          
: 
            
        
          

**JSON example**

          
: 
            
              
                

**JSON example**

                
: 
                  

```
{
  "status": "Active"
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
| `status` | String | Status that must be set to activate or deactivate a payment scheduler. Valid values are: `Active` `Canceled` `Draft` `Inactive` | Required | 64.0 |

          

        
      

          

        
        
          

**Response body for PATCH**

          
: [Payments Scheduler
              Update](./connect_responses_payment_scheduler_update_output.htm.md)

=== ARTICLE: connect_resources_update_sequence_policies.htm ===
---
page_id: connect_resources_update_sequence_policies.htm
title: Update Sequence Policy (PATCH)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_update_sequence_policies.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Update Sequence Policy (PATCH)

Update the settings of a sequence policy that defines how unique,
      sequential numbers are generated by using specific patterns, values, and
    filters.

    

## Special Access Rules

      
      

You need the Billing Admin permission set to use this API.

    

    
      
        
          

**Resource**

          
: 
            

```
/connect/sequences/policy/sequencePolicyId
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/sequences/policy/1Vdxx0000000GRNAA2
```

          

        
        
          

**Available version**

          
: 65.0

        
        
          

**HTTP methods**

          
: PATCH

        
        
          

**Request body for PATCH**

          
: 
            

**JSON example**

: This example shows a sample request to create a sequence
            policy.

```
{
  "name": "Sample Sequence Policy",
  "description": "This is a sample sequence policy.",
  "effectiveFromDateTime": "2025-08-10",
  "expirationDateTime": "2025-09-20",
  "isActive": true,
  "sequenceMode": "Basic",
  "targetObject": "Invoice",
  "dateStampFormat": "Yyyy",
  "sequenceStartNumber": 1,
  "incrementNumber": 1,
  "maximumSequenceNumber": 1000,
  "minimumSequenceNumberWidth": 2,
  "filterCriteria": "Custom",
  "selectionLogic": "selectionLogic",
  "sequencePattern": "INV-{SequenceValue}-abc",
  "selectionCondition": [
    {
      "filterField": "AppType",
      "operator": "Equals",
      "filterValue": "RLM",
      "conditionNumber": 1
    },
    {
      "filterField": "Status",
      "operator": "Equals",
      "filterValue": "Posted",
      "conditionNumber": 2
    },
    {
      "filterField": "LegalEntity",
      "operator": "Equals",
      "filterValue": "US",
      "conditionNumber": 3
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
| `dateStamp​Format` | String | Format of the stamp date that's appended to the sequence number. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `description` | String | Additional details about the sequence policy. | Optional | 65.0 |
| `effectiveFrom​DateTime` | String | Date and time when the policy becomes effective. The default value is the current date. | Required | 65.0 |
| `expiration​DateTime` | String | Date and time when the policy expires. | Optional | 65.0 |
| `filter​Criteria` | String | Criteria to filter the target objects. | Required | 65.0 |
| `increment​Number` | Integer | Value by which the sequence number increases until it reaches the maximum number. This value must be greater than or equal to `1`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `isActive` | Boolean | Indicates whether the policy is active (`true`) or not (`false`). The default value is `false`. | Required | 65.0 |
| `maximumSequence​Number` | Integer | Maximum number the sequence number can reach. | Optional | 65.0 |
| `minimumSequence​NumberWidth` | Integer | Minimum number of digits a sequence number must have. You can't edit this property by using the Update Sequence Policy API. | Optional | 65.0 |
| `name` | String | Name of the sequence policy. | Required | 65.0 |
| `selection​Condition` | [Selection Condition Input](./connect_requests_selection_condition_input.htm.md)[] | Criteria to determine which sequence policy is applied to a record. This property includes conditions based on any standard or custom fields of the record. | Optional | 65.0 |
| `selection​Logic` | String | Logic that determines the objects that the sequence policy applies to. | Optional | 65.0 |
| `sequence​Mode` | String | Specifies how sequence numbers are generated. Valid values are: `Basic`—Assigns sequential numbers without gap reconciliation. `Gapless`—Assigns sequential numbers with gap reconciliation. The usage of this value ensures that the posted invoices or credit memos don't have any numbering gaps for audits and compliance. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `sequence​Pattern` | String | Pattern structure that’s followed for the sequence. | Required | 65.0 |
| `sequenceStart​Number` | Integer | Starting value of the sequence number, which must be greater than or equal to `0`. The default value is `1`. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `target​Object` | String | Object that the policy is applied to. Valid values are: `Invoice` `CreditMemo`—Available in API version 66.0 and later. You can't edit this property by using the Update Sequence Policy API. | Required | 65.0 |
| `timeZone` | String | Time zone that’s applicable for the sequence policy. | Optional | 65.0 |

          

        
        
          

**Response body for PATCH**

          
: [Sequence
              Policy](./connect_responses_sequence_policy_output.htm.md)

=== ARTICLE: connect_resources_void_a_posted_invoice.htm ===
---
page_id: connect_resources_void_a_posted_invoice.htm
title: Void a Posted Invoice (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_void_a_posted_invoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void a Posted Invoice (POST)

Void a posted invoice to rebill the customer, if
    necessary.

    

This API request changes the invoice status from `Posted` to `Void In Progress`. The invoice
        remains in the `Void In Progress` status until the credit
        is applied and financial fields are recalculated on the invoice’s related billing period
        items and billing schedule. The invoice status changes to `Voided` after all recalculations are completed.

Keep these considerations in mind when you use this API.

        
- The balance and total amount on the invoice must be equal. If these amounts aren’t equal
          due to payments or credits, the API request fails.

        
- You can’t call other APIs on an invoice with the `Void In
            Progress` status. You also can’t update the invoice fields.

        
- You can void only the most recently posted invoice on a billing schedule.

        
- To void an invoice that has payments or credits, use the [Credit Memo
            Unapply (POST)](./connect_resources_credit_memo_invoice_application_unapply.htm.md) API.

      

    
      
        
          

**Credit Memos**

          
: The void process creates a credit memo, which contains one credit memo line for each
            invoice line, including tax lines. For example, if the invoice line has a balance of
            US$20, the related credit memo line has a balance of $20. The credit memo’s balance is
            then allocated to the invoice header’s balance, reducing it to zero. A credit memo
            invoice application is created to record the details of the void process.

        
        
          

**Negative Invoice Lines**

          
: If an invoice has negative invoice lines that aren’t converted to a credit memo, you
            can use this endpoint to void the posted invoice.

        
        
          

**Special Access Rules**

          
: You need the Void a Posted Invoice API permission set to use this API.

        
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/invoiceId/actions/void
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/3ttxx00000000XtAAI/actions/void
```

          

        
        
          

**Available version**

          
: 62.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceId` | String | ID of the posted invoice to be voided. | Required | 62.0 |

          

        
        
          

**Response body for POST**

          
: [Revenue Async
              Response](./connect_responses_revenue_async_output.htm.md)

=== ARTICLE: connect_resources_void_posted_credit_memo.htm ===
---
page_id: connect_resources_void_posted_credit_memo.htm
title: Void Posted Credit Memo (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_void_posted_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void Posted Credit Memo (POST)

Void a credit memo in posted state.

The API response returns a unique identifier. In case of any asynchronous errors, a
        RevenueTransactionErrorLog record is created.

        
          

**Resource**

          
: 
            

```
/commerce/billing/credit-memos/creditMemoId/actions/void
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/billing/credit-memos/50gVB0000003khRYAQ/actions/void
```

          

        
        
          

**Available version**

          
: 66.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Path parameter for POST**

          
: 
            

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemoId` | String | ID of the posted credit memo to be voided. | Required | 66.0 |

          

        
        
          

**Request body for POST**

          
: As this API accepts a credit memo ID as a path parameter in the URL, specify an empty
            request body.

        
        
          

**Response body for POST**

          
: [Void Posted Credit
              Memo](./connect_responses_void_posted_credit_memo_output.htm.md)

=== ARTICLE: connect_resources_write_off_invoices.htm ===
---
page_id: connect_resources_write_off_invoices.htm
title: Posted Invoice List Write-Off (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_write_off_invoices.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice List Write-Off (POST)

Create credit memos with the total charge amount on the invoice as the
      write-off amount and close the invoice.

    
      

You can write off invoices to maintain accurate financial records and to prioritize
        invoices with a higher probability of payment, which is essential for compliance with
        accounting standards.

    

    

## Special Access Rules

      
      

To use this API, you need the Billing Operations User or Credit Memo Operations User
        permission set.

    

    
      
        
          

**Resource**

          
: 
            

```
/commerce/invoicing/invoices/actions/write-off
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/commerce/invoicing/invoices/actions/write-off
```

          

        
        
          

**Available version**

          
: 64.0

        
        
          

**HTTP methods**

          
: POST

        
        
          

**Request body for POST**

          
: 
            

**JSON example**

: 

```
{
  "invoices": [
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Bad Debt",
      "description": "Bad Debt"
    },
    {
      "invoiceId": "3ttxx00000000cjAAA",
      "reasonCode": "Concession",
      "description": "Concession"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `invoices` | [Posted Invoice Write-Off Input](./connect_requests_write_off_posted_invoice_input.htm.md)[] | Details of the invoices that you want to write off. | Required | 64.0 |

          

        
        
          

**Response body for POST**

          
: [Posted Invoice List
              Write-Off](./connect_responses_write_off_posted_invoice_list_output.htm.md)

=== ARTICLE: connect_responses_address_output.htm ===
---
page_id: connect_responses_address_output.htm
title: Address
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_address_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Address

Output representation of the location code associated with an address.

        
          

**JSON example**

          
: 
            

```
{
    "locationCode": "123456789"
}

```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `locationCode` | String | Unique location code of the address. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_addresses_output.htm ===
---
page_id: connect_responses_addresses_output.htm
title: Addresses
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_addresses_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Addresses

Output representation of the details of the addresses that are used for calculating
    tax.

    

        
          

**JSON example**

          
: 
            

```
{
  "addresses": {
    "shipFrom": {
      "locationCode": "67890"
    },
    "shipTo": {
      "locationCode": "12345"
    },
    "soldTo": {
      "locationCode": "12345"
    }
  }
}

```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `shipFrom` | [Address](./connect_responses_address_output.htm.md) | Address that the item is shipped from. | Big, 62.0 | 62.0 |
| `shipTo` | [Address](./connect_responses_address_output.htm.md) | Address that the item is shipped to. | Big, 62.0 | 62.0 |
| `soldTo` | [Address](./connect_responses_address_output.htm.md) | Address that the item is sold to. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_batch_invoice_doc_gen_error.htm ===
---
page_id: connect_responses_batch_invoice_doc_gen_error.htm
title: Error Response for Batch Invoice Document Generation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_batch_invoice_doc_gen_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Response for Batch Invoice Document Generation 

Output representation of the error details associated with the Batch Invoice Document
    Generation API.

    
      
        
          

**JSON example**

          
: 
            

```

  "errors": {
    "errorCode": "API_DISABLED_FOR_ORG",
    "message": "Document Generation is not enabled for this org!"
  }

```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | Big, 63.0 | 63.0 |
| `errorMessage` | String | Error message for the resultant error. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_batch_invoice_doc_gen_output.htm ===
---
page_id: connect_responses_batch_invoice_doc_gen_output.htm
title: Batch Invoice Document Generation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_batch_invoice_doc_gen_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoice Document Generation

Output representation of the request to generate or regenerate the PDF documents for
      the invoices that are in the `Draft` or `Posted` status.

        
          

**JSON example**

          
: 
            

```
{
  "errors": [
    {
      "errorCode": "API_DISABLED_FOR_ORG",
      "errorMessage": "Document Generation is not enabled for this org!"
    },
    {
      "errorCode": "INVALID_API_INPUT",
      "errorMessage": "Invalid Invoice Batch Run Id"
    }
  ],
  "requestIdentifier": "5IRDU000000009i4AA",
  "success": false
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Batch Invoice Document Generation Error []](./connect_responses_batch_invoice_doc_gen_error.htm.md) | Details of the error if the operation fails. | Big, 63.0 | 63.0 |
| `requestIdentifier` | String | Unique ID that’s associated with the specific error, and is used for tracking and referencing the request. | Big, 63.0 | 63.0 |
| `success` | Boolean | Indicates whether the operation is successful (`true`) or not (`false`). | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_batch_invoice_scheduler_output.htm ===
---
page_id: connect_responses_batch_invoice_scheduler_output.htm
title: Batch Invoice Scheduler
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_batch_invoice_scheduler_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoice Scheduler

Output representation of the details of an invoice scheduler.

        
          

**JSON example**

          
: 
            

```
{
    "billingBatchScheduler": {
        "id": "5BSxx0000004TwGGAU"
    }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Batch​Scheduler` | [Billing Batch Scheduler](./connect_responses_billing_batch_scheduler.htm.md)[] | Details of the created invoice scheduler. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_billing_arrangement_line.htm ===
---
page_id: connect_responses_billing_arrangement_line.htm
title: Billing Arrangement Line
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_arrangement_line.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Arrangement Line

Output representation that contains the details of a specific line item within a billing
    arrangement, defining how charges are split for an account.

        
          

**JSON example**

          
: 
            

```
{
  "billingArrangementLineId": "1blxx000000006TAAQ",
  "accountId": "accId1",
  "billingAccountId": "bAccId1",
  "isRemainderAdjustmentAccount": false,
  "percentage": 60.00
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | ID of the account associated with the billing line. | Big, 66.0 | 66.0 |
| `billing​AccountId` | String | ID of the billing account responsible for this portion of the bill. | Big, 66.0 | 66.0 |
| `billingArrangement​LineId` | String | Unique ID of the billing arrangement line. | Big, 66.0 | 66.0 |
| `isRemainder​AdjustmentAccount` | Boolean | Indicates whether the specific line is designated as the adjustment account for any remainder (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `percentage` | Double | Percentage of the charge allocated to this line. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_billing_arrangement_output.htm ===
---
page_id: connect_responses_billing_arrangement_output.htm
title: Billing Arrangement
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_arrangement_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Arrangement

Output representation that contains the details of a billing arrangement, including its
    status, configuration settings, and associated lines.

        
          

**JSON example**

          
: 
            

```
{
  "billingArrangementId": "1bdxx000000004rAAA",
  "name": "Acme Shared Billing Definition",
  "isAdjustmentToOwnAccount": true,
  "remainderPercentage": 15,
  "versionNumber": 1,
  "numOfAssociatedBSGs": 5,
  "status": "Active",
  "billingArrangementLines": [
    {
      "billingArrangementLineId": "1blxx000000006TAAQ",
      "accountId": "accId1",
      "billingAccountId": "bAccId1",
      "isRemainderAdjustmentAccount": false,
      "percentage": 60
    },
    {
      "billingArrangementLineId": "1blxx000000001dAAA",
      "accountId": "accId2",
      "billingAccountId": "bAccId2",
      "isRemainderAdjustmentAccount": false,
      "percentage": 25
    }
  ],
  "isSuccess": true,
  "error": null
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              
- 
- 
- 

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billing​ArrangementId` | String | Unique ID of the billing arrangement. | Big, 66.0 | 66.0 |
| `billing​ArrangementLines` | [Billing Arrangement Line](./connect_responses_billing_arrangement_line.htm.md)[] | List of billing arrangement lines associated with the latest version of the billing arrangement. | Big, 66.0 | 66.0 |
| `error` | [Error Response Output](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | Error details if the request was unsuccessful. | Big, 66.0 | 66.0 |
| `isAdjustment​ToOwnAccount` | Boolean | Indicates whether the remainder of the bill is adjusted to the owning account (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `isSuccess` | Boolean | Indicates whether the request was successfully processed (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `name` | String | Name of the billing arrangement. | Big, 66.0 | 66.0 |
| `numOf​AssociatedBSGs` | Integer | Total number of billing schedule groups associated with the billing arrangement. | Big, 66.0 | 66.0 |
| `remainderPercentage` | Double | Remaining percentage of the bill after all line allocations are calculated. | Big, 66.0 | 66.0 |
| `status` | String | Status of the billing arrangement. Valid values are: `Draft` `Active` `Inactive` | Big, 66.0 | 66.0 |
| `versionNumber` | Integer | Current version number of the billing arrangement. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_billing_batch_scheduler.htm ===
---
page_id: connect_responses_billing_batch_scheduler.htm
title: Billing Batch Scheduler
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_batch_scheduler.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Batch Scheduler

Output representation of the details of a created invoice or payment
    scheduler.

        
          

**JSON example**

          
: 
            

```
    "billingBatchScheduler": {
        "id": "5BSxx0000004TwGGAU"
    }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the invoice or payment scheduler. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_billing_schedule_recovery_list_output.htm ===
---
page_id: connect_responses_billing_schedule_recovery_list_output.htm
title: Billing Schedule Recovery List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_schedule_recovery_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Schedule Recovery List

Output representation of the recovered details of the billing schedules and associated
    invoice.

        
          

**JSON example**

          
: 
            

```
{
  "recoveryResults": [
    {
      "billingSchedules": [
        {
          "billingScheduleId": "44bDU00000000XX",
          "billingScheduleStatus": "ReadyForInvoicing"
        }
      ],
      "invoiceErrors": [],
      "invoiceId": null,
      "success": true
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `recovery​Results` | [Invoice Recovery](./connect_responses_invoice_recovery_output.htm.md)[] | Details of the recovered invoice and billing schedules. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_billing_schedule_recovery_output.htm ===
---
page_id: connect_responses_billing_schedule_recovery_output.htm
title: Billing Schedule Recovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_billing_schedule_recovery_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Schedule Recovery

Output representation of the details of the recovered billing schedules.

        
          

**JSON example**

          
: 
            

```
    "billingSchedules": [
        {
          "billingScheduleId": "44bDU00000000XX",
          "billingScheduleStatus": "ReadyForInvoicing"
        }
    ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Schedule​Id` | String | ID of the billing schedule. | Big, 62.0 | 62.0 |
| `billing​Schedule​Status` | String | Flag that indicates the billing schedule status. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_calculate_tax_output.htm ===
---
page_id: connect_responses_calculate_tax_output.htm
title: Tax Calculation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_calculate_tax_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Calculation

Output representation of the details of the calculated tax.

    

        
          

**JSON example**

          
: 
            

```
{
    "referenceEntityId": "001xx000003HYEhAAO",
    "status": "Committed",
    "taxEngineLogs": [
        {
            "createdDate": "2022-03-09T10:55:38.000Z",
            "id": "3l1xx00000000PpAAI",
            "resultCode": "Success"
        }
    ],
    "taxTransactionType": "Debit",
    "taxType": "Actual",
    "transactionDate": "2022-03-09T10:30:41.000Z",
    "addresses": {
        "shipFrom": {
            "locationCode": "67890"
        },
        "shipTo": {
            "locationCode": "23456"
        },
        "soldTo": {
            "locationCode": "23456"
        }
    },
    "amountDetails": {
        "exemptAmount": 0.0,
        "taxAmount": 12.5,
        "totalAmount": 100.0,
        "totalAmountWithTax": 112.5
    },
    "currencyIsoCode": "USD",
    "description": "Monthly invoice for account 001xx000003HYEhAAO",
    "documentCode": "INV-003",
    "effectiveDate": "2022-03-09T10:55:38.410Z",
    "lineItems": [
        {
            "addresses": {
                "shipFrom": {
                    "locationCode": "67890"
                },
                "shipTo": {
                    "locationCode": "12345"
                },
                "soldTo": {
                    "locationCode": "12345"
                }
            },
            "amountDetails": {
                "exemptAmount": 0.0,
                "taxAmount": 12.5,
                "totalAmount": 100.0,
                "totalAmountWithTax": 112.5
            },
            "effectiveDate": "2022-03-09T10:55:38.416Z",
            "lineNumber": "001xx000003HYEiAAO",
            "productCode": "Y0001",
            "quantity": 1.0,
            "taxCode": "TX0001",
            "taxes": [
                {
                    "exemptAmount": 0.0,
                    "exemptReason": "NoExemption",
                    "imposition": {
                        "type": "General"
                    },
                    "jurisdiction": {
                        "country": "US",
                        "id": "63000",
                        "level": "CIT",
                        "name": "SEATTLE",
                        "region": "WA",
                        "stateAssignedNo": "1726"
                    },
                    "rate": 12.5,
                    "tax": 12.5,
                    "taxId": "11000378132466",
                    "taxableAmount": 100.0
                }
            ]
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
| `adapterError` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | Details of the adapter error. | Big, 62.0 | 62.0 |
| `addresses` | [Addresses](./connect_responses_addresses_output.htm.md) | Addresses that are used for calculating tax. | Big, 62.0 | 62.0 |
| `amountDetails` | [Tax Amount Details](./connect_responses_tax_amount_details_output.htm.md) | Details of the transaction amount and taxes. | Big, 62.0 | 62.0 |
| `currencyIsoCode` | String | Currency ISO code that’s used for tax calculation. | Big, 62.0 | 62.0 |
| `description` | String | Description of the transaction status. | Big, 62.0 | 62.0 |
| `documentCode` | String | Unique identifier for the tax document. If the `documentCode` property isn't specified, the tax engine auto-generates it. | Big, 62.0 | 62.0 |
| `effectiveDate` | String | Date when the tax rules are applied. | Big, 62.0 | 62.0 |
| `lineItems` | [Line Item](./connect_responses_line_item_output.htm.md) [] | Line items that the taxes are calculated for. | Big, 62.0 | 62.0 |
| `reference​DocumentCode` | String | Reference document code. For subsequent transactions such as a credit tax, the `referenceDocumentCode` property value refers to the original document code. | Big, 62.0 | 62.0 |
| `reference​EntityId` | String | ID of the related quote, invoice, or other transaction documents. | Big, 62.0 | 62.0 |
| `status` | String | Commit status of the tax transaction. Valid values are: `Committed`—Committed transaction, which is marked for tax reporting. `Uncommitted`— Uncommitted transaction, which isn’t marked for tax reporting. | Big, 62.0 | 62.0 |
| `taxEngineLogs` | [Tax Engine Log](./connect_responses_tax_engine_log_output.htm.md) [] | Records that the tax engine generates while calculating taxes for the transaction. | Big, 62.0 | 62.0 |
| `tax​TransactionId` | String | Unique ID for the tax transaction. | Big, 62.0 | 62.0 |
| `transactionDate` | String | Date of the transaction that appears on the invoice, order, and other transaction documents. | Big, 62.0 | 62.0 |
| `taxTransaction​Type` | String | Tax transaction type. Valid values are: `Debit`—Increases tax liability for the user, requiring the user to pay tax on the transaction. `Credit`—Decreases tax liability for the user, resulting in a tax refund for the user. `Void`—Specifies that the tax engine has voided the document that's mentioned as the `referenceDocumentCode` property value. | Big, 62.0 | 62.0 |
| `taxType` | String | Type of calculated tax. Valid values are: `Actual`—Exact tax amount that’s calculated based on the actual sales. `Estimated`— Estimated tax amount, which is adjusted later to match the actual tax calculations. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_aware_billing_schedule_error.htm ===
---
page_id: connect_responses_context_aware_billing_schedule_error.htm
title: Context-Aware Billing Schedule Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_context_aware_billing_schedule_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context-Aware Billing Schedule Error

Output representation of the error response related to the generation of the billing
    schedule.

      

```
    "errors": [ 
        { 
            "errorCode": "REQUIRED_FIELD_MISSING",
            "errorMessage": "Required fields are missing: billToContact", 
            "referenceId": "802xx000001nmb5"
        } 
    ]
```

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | Big, 62.0 | 62.0 |
| `errorMessage` | String | Error message for the resultant error. | Big, 62.0 | 62.0 |
| `referenceId` | String | Reference ID of the source item that resulted in the error. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_context_aware_billing_schedule_output.htm ===
---
page_id: connect_responses_context_aware_billing_schedule_output.htm
title: Context-Aware Billing Schedule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_context_aware_billing_schedule_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context-Aware Billing Schedule

Output representation of the context-aware billing schedule.

        
          

**JSON example**

          
: This request shows a sample success response.

          
: 
            

```
{ 
    "errors": null, 
    "requestIdentifier": "16Pxx0000004CaS", 
    "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16Pxx0000004CaSEAU", 
    "success": true 
}
```

          

          
: This request shows a sample error response.

          
: 
            

```
{ 
    "errors": [ 
        { 
            "errorCode": "REQUIRED_FIELD_MISSING",
            "errorMessage": "Required fields are missing: billToContact", 
            "referenceId": "802xx000001nmb5"
        } 
    ],
    "requestIdentifier": "16Pxx0000004CYq", 
    "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16Pxx0000004CYqEAM", 
    "success": false 
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Context Aware Billing Schedule Error](./connect_responses_context_aware_billing_schedule_error.htm.md)[] | Error response if the generation of the billing schedule fails. | Big, 62.0 | 62.0 |
| `request​Identifier` | String | Unique request identifier that you can use to poll the asynchronous request. | Big, 62.0 | 62.0 |
| `statusURL` | String | Status URL to track the operation. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the processing of the billing schedule is successful (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_convert_negative_invoice_lines_output.htm ===
---
page_id: connect_responses_convert_negative_invoice_lines_output.htm
title: Convert Negative Invoice Lines
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_convert_negative_invoice_lines_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Convert
    Negative Invoice Lines

Output representation of the details of the created memo along with the status of the
    request.

        
          

**JSON example**

          
: 
            

```
  {
  "id": "50gxx000000g0WwAAI",
  "success": true,
  "errors": []
  }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.252.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the processing of the API request. | Big, 62.0 | 62.0 |
| `id` | String | ID of the credit memo that’s created after the conversion of the negative invoice lines. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_apply_list_output.htm ===
---
page_id: connect_responses_credit_memo_apply_list_output.htm
title: Credit Memo Apply List
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_apply_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Apply List

Output representation of the list of applied credit memo results.

        
          

**JSON example**

          
: 
            

```
{
  "applyCreditResults" : [ {
    "appliedToId" : "3ttxx000000003FAAQ",
    "errors" : null,
    "id" : "4sFxx00000002ppEAA",
    "success" : true
  }, {
    "appliedToId" : "3ttxx0000000001AAA",
    "errors" : null,
    "id" : "4sFxx00000002pqEAA",
    "success" : true
  } ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `applyCredit​Results` | [Credit Memo Apply](./connect_responses_credit_memo_apply_output.htm.md)[] | Output list of the applied credit memo results. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_apply_output.htm ===
---
page_id: connect_responses_credit_memo_apply_output.htm
title: Credit Memo Apply
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Apply

Output representation of the list of applied credit memo results.

        
          

**JSON example**

          
: 
            

```
  "applyCreditResults" : [ {
    "appliedToId" : "3ttxx000000003FAAQ",
    "errors" : null,
    "id" : "4sFxx00000002ppEAA",
    "success" : true
  }, {
    "appliedToId" : "3ttxx0000000001AAA",
    "errors" : null,
    "id" : "4sFxx00000002pqEAA",
    "success" : true
  } ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `appliedToId` | String | ID of the invoice record that the credit is applied to. | Big, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the processing of the API request. | Big, 62.0 | 62.0 |
| `id` | String | ID of the credit memo invoice application. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the credit memo is successfully applied (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_line_applied.htm ===
---
page_id: connect_responses_credit_memo_line_applied.htm
title: Credit Memo Line Applied
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_line_applied.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Applied

Output representation of the list of applied credit memo line results.

        
          

**JSON example**

          
: 
            

```
  {
  "appliedCreditResponses": [
   {
    "creditMemoLineInvoiceLineId": "4sGSG0000002pMb2AI",
    "errors": null,
    "invoiceLineId": "5TVSG0000003CuH4AU",
    "success": true
   }
  ]
 }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `applied​CreditResponses` | [Credit Memo Line Applied Response](./connect_responses_credit_memo_line_applied_response.htm.md)[] | Output list for the applied credit memo line results. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_line_applied_response.htm ===
---
page_id: connect_responses_credit_memo_line_applied_response.htm
title: Credit Memo Line Applied Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_line_applied_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Applied Response

Output representation of the list of applied credit memo line results.

        
          

**JSON example**

          
: 
            

```
  "appliedCreditResponses": [
   {
    "creditMemoLineInvoiceLineId": "4sGSG0000002pMb2AI",
    "errors": null,
    "invoiceLineId": "5TVSG0000003CuH4AU",
    "success": true
   }
  ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​LineInvoice​LineId` | String | ID of the credit memo line invoice line ID. | Big, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the processing of the API request. | Big, 62.0 | 62.0 |
| `invoice​LineId` | String | ID of the invoice line record that the credit is applied to. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the credit memo line is successfully applied (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_line_unapplied.htm ===
---
page_id: connect_responses_credit_memo_line_unapplied.htm
title: Credit Memo Line Unapplied
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_line_unapplied.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Unapplied

Output representation of the details of the credit memo line invoice line record with
    the status of the request.

        
          

**JSON example**

          
: 
            

```
  {
  "creditMemoLineInvoiceLineId": "4sGSG0000002pOD2AY",
  "errors": [],
  "success": true
 }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemo​LineInvoice​LineId` | String | ID of the credit memo line invoice line record. | Small, 62.0 | 62.0 |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the processing of the API request. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the credit memo line is successfully unapplied (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_credit_memo_post_output.htm ===
---
page_id: connect_responses_credit_memo_post_output.htm
title: Credit Memo Post
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_post_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Post

Output representation of the request to post a credit memo.

        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "errors": [],
  "requestIdentifier": "d3a9d9ce-2a83-4a08-bcf3-df0348a0008c",
  "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16PDU000000A4oz2AC",
  "success": true
}
```

          
: This example shows a sample error
            response.

```
{
  "errors": [
    {
      "errorCode": "BAD_REQUEST",
      "message": "You can post up to 1 credit memo at a time."
    }
  ],
  "requestIdentifier": "9065b043-dcc3-4dcf-b5a1-55fdf5a79f7b",
  "statusURL": "",
  "success": false
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` |  | List of errors encountered during the processing of the API request. | Big, 65.0 | 65.0 |
| `requestIdentifier` | String | Unique request identifier for the request. | Big, 65.0 | 65.0 |
| `statusURL` | String | Status URL for tracking this operation. | Big, 65.0 | 65.0 |
| `success` | Boolean | Indicates whether the API request was successful (`true`) or not (`false`). | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_credit_memo_unapply_output.htm ===
---
page_id: connect_responses_credit_memo_unapply_output.htm
title: Credit Memo Unapply
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_credit_memo_unapply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Unapply

Output representation of the details of the credit memo invoice application record with
    the status of the request.

        
          

**JSON example**

          
: 
            

```
{
    "errors": [],
    "id": "4sFxx00000002ppEAA",
    "success": true
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the processing of the API request. | Big, 62.0 | 62.0 |
| `id` | String | ID of the credit memo invoice application record. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the credit memo is successfully unapplied (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_document_details_output.htm ===
---
page_id: connect_responses_document_details_output.htm
title: Document Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_document_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Document Details

Output representation of the details of the generated document.

        
          

**JSON example**

          
: 
            

```
{
  "details": {
    "documentEntityId": "1BBSM00000003KT4AY",
    "documentGenerationProcessId": "0nnSM00000009jFYAQ",
    "documentTitle": "DOC-000000197",
    "existingDocumentId": "069SM000002PYQLYA4",
    "recordId": "3ttSM0000000o58YAA",
    "documentTemplateId": "0694x000000XyzABC"
  }
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `documentEntityId` | String | Identifier of the related object record that manages the relationship between the source record and the generated document. For example, InvoiceDocument for Invoice records. | Big, 66.0 | 66.0 |
| `documentGenerationProcessId` | String | Identifier of the document generation process record that's created to track this document generation request. | Big, 66.0 | 66.0 |
| `documentTemplateId` | String | Identifier of the document template that’s used to generate the PDF. | Big, 66.0 | 66.0 |
| `documentTitle` | String | Document title or name of the generated document. | Big, 66.0 | 66.0 |
| `existingDocumentId` | String | Identifier of the existing content document if a document is already generated and is available to view. | Big, 66.0 | 66.0 |
| `recordId` | String | Identifier of the source record the document is generated for. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_error_response.htm ===
---
page_id: connect_responses_error_response.htm
title: Error Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_error_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Error Response

Output representation of the error details encountered during the API
    request.

      
        
          

**JSON example**

          
: This example shows a sample error
            response.

```
{
  "errors": [
    {
      "errorCode": "INVALID_STATUS",
      "message": "CreditMemo 50gxx00000000XtAAI is not in the Posted status."
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code that indicates the type of error. | Big, 66.0 | 66.0 |
| `message` | String | Message stating the reason for error, if any. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_invoice_batch_draft_to_posted_output.htm ===
---
page_id: connect_responses_invoice_batch_draft_to_posted_output.htm
title: Invoice Batch Draft To Posted
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_batch_draft_to_posted_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Batch Draft To Posted

Output representation of the batch update details of the invoices from `Draft` to `Posted`
      status.

    

        
          

**JSON example**

          
: 
            

```
{
  "invoiceBatchDraftToPostedId": "4sFDU00000000652AA",
  "success": true
}
```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceBatch​DraftToPostedId` | String | ID of the invoice batch draft to posted run record that’s created to track the batch process of posting the draft invoices that are associated with the parent invoice batch run record. | Small, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_invoice_batch_run_recovery_output.htm ===
---
page_id: connect_responses_invoice_batch_run_recovery_output.htm
title: Invoice Batch Run Recovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_batch_run_recovery_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Batch Run Recovery

Output representation of the details of the invoice batch run recovery
    record.

        
          

**JSON example**

          
: 
            

```
{
  "invoiceBatchRunRecoveryId": ["0wBxx0000004TtwGAU"]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `invoiceBatchRun​RecoveryId` | String | ID of the invoice batch run recovery record for the specified invoice batch run. This record represents the background recovery process. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_invoice_ingestion_output.htm ===
---
page_id: connect_responses_invoice_ingestion_output.htm
title: Invoice Ingestion Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_ingestion_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Ingestion Details

Output representation of the details of a generated invoice.

        
          

**JSON example**

          
: 
            

```
{
  "invoices": [
    {
      "errors": null,
      "invoiceId": "3ttxx0000000GRNAA2",
      "requestIdentifier": "16e80fbc-e7b3-4462-9439-745647fcf0a8",
      "statusURL": "/services/data/v63.0/sobjects/AsyncOperationTracker/16Pxx0000004Gz2EAE",
      "success": true
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Invoice Ingestion Output Error](./connect_responses_invoice_ingestion_output_error.htm.md)[] | Details of the errors if the request was unsuccessful. | Small, 63.0 | 63.0 |
| `invoice​Id` | String | ID of the Invoice record that’s created in Salesforce. | Small, 63.0 | 63.0 |
| `request​Identifier` | String | Unique request identifier that can be used to poll the async request. | Small, 63.0 | 63.0 |
| `status​URL` | String | Status URL for tracking the estimated tax callout operation. | Big, 63.0 | 63.0 |
| `success` | Boolean | Indicates whether the API request was successful (`true`) or not (`false`). | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_invoice_ingestion_output_error.htm ===
---
page_id: connect_responses_invoice_ingestion_output_error.htm
title: Invoice Ingestion Output Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_ingestion_output_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Ingestion Output Error

Output representation of the details of an invoice generation error.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code that indicates the type of error. | Small, 63.0 | 63.0 |
| `message` | String | Message that states the reason for error, if any. | Small, 63.0 | 63.0 |
| `reference​Id` | String | Reference ID that maps to the subrequest’s response and can be used to reference the response in later subrequests. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_invoice_preview_output.htm ===
---
page_id: connect_responses_invoice_preview_output.htm
title: Invoice Preview Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_preview_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Preview Result

Output representation of the list of preview invoices that are generated for the billing transaction.

      
        
          

**JSON example**

          
: 
            

```
{
  "invoiceDetailList": [
    {
      "accountId": "001Z6000005aQj8",
      "currencyIsoCode": "USD",
      "dueDate": "2025-01-03",
      "invoiceDate": "2024-12-04",
      "invoiceLineDetailList": [
        {
          "billingFrequency": "OneTime",
          "chargeAmount": "1990.00",
          "endDate": "2024-07-18",
          "lineAmount": "2189.00",
          "productName": "Laptop",
          "quantity": "10.0",
          "startDate": "2024-07-18",
          "taxAmount": "199.0",
          "unitPrice": "199.0"
        }
      ],
      "totalAmount": "1990.00",
      "totalAmountWithTax": "2189.00",
      "totalTaxAmount": "199.0"
    }
  ]
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `invoice​Detail​List` | [Invoice Preview](./connect_responses_prev_inv_output.htm.md)[] | Details of the invoices that are generated for the billing transaction. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_invoice_recovery_output.htm ===
---
page_id: connect_responses_invoice_recovery_output.htm
title: Invoice Recovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoice_recovery_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Recovery

Output representation of the details of the recovered invoice and billing
    schedules.

        
          

**JSON example**

          
: 
            

```
{
  "recoveryResults": [
    {
      "billingSchedules": [
        {
          "billingScheduleId": "44bDU00000000XX",
          "billingScheduleStatus": "ReadyForInvoicing"
        }
      ],
      "invoiceErrors": [],
      "invoiceId": null,
      "success": true
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Schedules` | [Billing Schedule Recovery](./connect_responses_billing_schedule_recovery_output.htm.md)[] | Billing schedules associated with this invoice. | Big, 62.0 | 62.0 |
| `invoice​Errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors encountered during the invoice recovery. | Big, 62.0 | 62.0 |
| `invoice​Id` | String | ID of the recovered invoice. | Big, 62.0 | 62.0 |
| `invoice​Status` | String | Flag that indicates the invoice status. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the overall transaction was successful or not (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_invoices_ingestion_output.htm ===
---
page_id: connect_responses_invoices_ingestion_output.htm
title: Invoice Ingestion
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_invoices_ingestion_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Ingestion

Output representation of the details of the generated invoices.

        
          

**JSON example**

          
: 
            

```
{
  "invoices": [
    {
      "errors": null,
      "invoiceId": "3ttxx0000000GRNAA2",
      "requestIdentifier": "16e80fbc-e7b3-4462-9439-745647fcf0a8",
      "statusURL": "/services/data/v63.0/sobjects/AsyncOperationTracker/16Pxx0000004Gz2EAE",
      "success": true
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `invoices` | [Invoice Ingestion](./connect_responses_invoice_ingestion_output.htm.md)[] | Result that contains the details for each generated invoice. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_line_item_output.htm ===
---
page_id: connect_responses_line_item_output.htm
title: Line Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_line_item_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Line Item

Output representation of the details of the line item.

    

        
          

**JSON example**

          
: 
            

```
{
  "lineItems": [
    {
      "addresses": {
        "shipFrom": {
          "locationCode": "67890"
        },
        "shipTo": {
          "locationCode": "12345"
        },
        "soldTo": {
          "locationCode": "12345"
        }
      },
      "amountDetails": {
        "exemptAmount": 0,
        "taxAmount": 12.5,
        "totalAmount": 100,
        "totalAmountWithTax": 112.5
      },
      "effectiveDate": "2022-03-09T10:55:38.416Z",
      "lineNumber": "001xx000003HYEiAAO",
      "productCode": "Y0001",
      "quantity": 1,
      "taxCode": "TX0001",
      "taxes": [
        {
          "exemptAmount": 0,
          "exemptReason": "NoExemption",
          "imposition": {
            "type": "General"
          },
          "jurisdiction": {
            "country": "US",
            "id": "63000",
            "level": "CIT",
            "name": "SEATTLE",
            "region": "WA",
            "stateAssignedNo": "1726"
          },
          "rate": 12.5,
          "tax": 12.5,
          "taxId": "11000378132466",
          "taxableAmount": 100
        }
      ]
    }
  ]
}

```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [Addresses](./connect_responses_addresses_output.htm.md) | Different types of addresses that are used for the transaction of the line item. | Big, 62.0 | 62.0 |
| `amountDetails` | [Tax Amount Details](./connect_responses_tax_amount_details_output.htm.md) | Details of the transaction amount and the taxes applicable for the line item. | Big, 62.0 | 62.0 |
| `effectiveDate` | String | Date when the tax rules are applied on the line item. | Big, 62.0 | 62.0 |
| `lineNumber` | String | Unique identifier of the line item. | Big, 62.0 | 62.0 |
| `productCode` | String | Product code of the line item as defined by the tax engine. | Big, 62.0 | 62.0 |
| `quantity` | Double | Quantity of the line item. | Big, 62.0 | 62.0 |
| `taxCode` | String | Tax code of the line item according to the tax engine. | Big, 62.0 | 62.0 |
| `taxes` | [Tax Details](./connect_responses_tax_details_output.htm.md) [] | Tax details of the line item. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_on_demand_doc_gen_output.htm ===
---
page_id: connect_responses_on_demand_doc_gen_output.htm
title: On-Demand Document Generation Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_on_demand_doc_gen_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# On-Demand Document Generation Response

Output representation of the details of the generated document along with error
    response.

        
          

**JSON example**

          
: 
            

```
{
  "requestIdentifier": "aad8ee2d-d94d-4760-8759-a2c5d63ce6db",
  "isSuccess": true,
  "details": {
    "documentEntityId": "1BBSM00000003KT4AY",
    "documentGenerationProcessId": "0nnSM00000009jFYAQ",
    "documentTitle": "DOC-000000197",
    "existingDocumentId": "069SM000002PYQLYA4",
    "recordId": "3ttSM0000000o58YAA",
    "documentTemplateId": "0694x000000XyzABC"
  },
  "errors": []
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `details` | [Document Details](./connect_responses_document_details_output.htm.md)[] | Details of the generated document. | Big, 66.0 | 66.0 |
| `errors` | [Error Response](./connect_responses_error_response.htm.md)[] | Error details of any issues encountered during the enqueue operation. | Big, 66.0 | 66.0 |
| `isSuccess` | Boolean | Status of the enqueuing PDF generation task. | Big, 66.0 | 66.0 |
| `requestIdentifier` | String | Unique request identifier that's used to poll the asynchronous request. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_payment_line_apply_output.htm ===
---
page_id: connect_responses_payment_line_apply_output.htm
title: Payment Line Apply
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_payment_line_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Apply

Output representation of the details of the applied payment line. The details include the
    ID of the payment record and date when the payment line was applied.

      
        
          

**JSON example**

          
: 
            

```
{
  "appliedDate": "2020-08-11T08:09:01.000Z",
  "id": "1PLR000000000dDOAQ"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `applied​Date` | String | Date when the payment line was applied. | Big, 64.0 | 64.0 |
| `id` | String | ID of the payment line record. | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_payment_line_unapply_output.htm ===
---
page_id: connect_responses_payment_line_unapply_output.htm
title: Payment Line Unapply
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_payment_line_unapply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Line Unapply

Output representation of the details of the reversed payment line application. The
    details include the ID of the payment line record and date when the payment line application was
    reversed.

      
        
          

**JSON example**

          
: 
            

```
{
  "unappliedDate": "2020-08-11T08:09:01.000Z",
  "id": "1PLR000000000dDOAQ"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `id` | String | ID of the payment line record. | Big, 64.0 | 64.0 |
| `unapplied​Date` | String | Date when the payment line application was reversed. | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_payment_scheduler_output.htm ===
---
page_id: connect_responses_payment_scheduler_output.htm
title: Batch Payment Scheduler
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_payment_scheduler_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Payment Scheduler

Output representation of the details of a payment scheduler.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "billingBatchScheduler": {
    "id": "5BSxx0000004TwGGAU"
  }
}

```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billingBatch​Scheduler` | [Billing Batch Scheduler](./connect_responses_billing_batch_scheduler.htm.md) | Details of the payment scheduler. | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_payment_scheduler_update_output.htm ===
---
page_id: connect_responses_payment_scheduler_update_output.htm
title: Payment Scheduler Update
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_payment_scheduler_update_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Payment Scheduler Update

Output representation of the details of the updated payment scheduler. This
    representation covers the updated status value of the specified payment scheduler.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "status": "Active"
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `status` | String | Updated status value of the specified payment scheduler. Valid values are: `Active` `Canceled` `Draft` `Inactive` | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_prev_inv_line_output.htm ===
---
page_id: connect_responses_prev_inv_line_output.htm
title: Invoice Line Preview
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_prev_inv_line_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Line Preview

Output representation of the invoice line preview result.

      
        
          

**JSON example**

          
: 
            

```
  "invoiceLineDetailList": [
        {
          "billingFrequency": "OneTime",
          "chargeAmount": "1990.00",
          "endDate": "2024-07-18",
          "lineAmount": "2189.00",
          "productName": "Laptop",
          "quantity": "10.0",
          "startDate": "2024-07-18",
          "taxAmount": "199.0",
          "unitPrice": "199.0"
        }
      ]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Frequency` | String | The frequency at which the invoice line is created for the billing transaction. | Big, 63.0 | 63.0 |
| `endDate` | String | The end date of the billing for the service for invoice lines made from a time-based service. | Big, 63.0 | 63.0 |
| `line​Amount` | String | The amount of the invoice line. | Big, 63.0 | 63.0 |
| `product​Name` | String | The name of the product that was charged or ordered to create the invoice line. | Big, 63.0 | 63.0 |
| `quantity` | String | The number of units of the order product that created the invoice line. | Big, 63.0 | 63.0 |
| `startDate` | String | The first date of the billing for the service for invoice lines made from a time-based service. | Big, 63.0 | 63.0 |
| `taxAmount` | String | The tax amount for the invoice line. | Big, 63.0 | 63.0 |
| `unitPrice` | String | The price for one unit of the item on the invoice line. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_prev_inv_output.htm ===
---
page_id: connect_responses_prev_inv_output.htm
title: Invoice Preview
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_prev_inv_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Preview

Output representation of the invoice preview result.

      
        
          

**JSON example**

          
: 
            

```
  "invoiceDetailList": [
    {
      "accountId": "001Z6000005aQj8",
      "currencyIsoCode": "USD",
      "dueDate": "2025-01-03",
      "invoiceDate": "2024-12-04",
      "invoiceLineDetailList": [
        {
          "billingFrequency": "OneTime",
          "chargeAmount": "1990.00",
          "endDate": "2024-07-18",
          "lineAmount": "2189.00",
          "productName": "Laptop",
          "quantity": "10.0",
          "startDate": "2024-07-18",
          "taxAmount": "199.0",
          "unitPrice": "199.0"
        }
      ],
      "totalAmount": "1990.00",
      "totalAmountWithTax": "2189.00",
      "totalTaxAmount": "199.0"
    }
  ]
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | The account ID of the billing transaction. | Big, 63.0 | 63.0 |
| `currency​Code` | String | The currency code for the amount fields. | Big, 63.0 | 63.0 |
| `dueDate` | String | The date by when the customer must pay an invoice that’s generated for the billing transaction. | Big, 63.0 | 63.0 |
| `invoiceDate` | String | The date when an invoice that’s generated for the billing transaction is posted. | Big, 63.0 | 63.0 |
| `invoiceLines` | [Invoice Line Preview](./connect_responses_prev_inv_line_output.htm.md)[] | The details of the invoice lines related to the invoices that are generated for the billing transaction. | Big, 63.0 | 63.0 |
| `totalAmount` | String | The sum of the total amount on the invoice lines of an invoice that’s generated for the billing transaction. | Big, 63.0 | 63.0 |
| `total​Amount​WithTax` | String | The sum of the total amount including tax on the invoice lines of an invoice that’s generated for the billing transaction. | Big, 63.0 | 63.0 |
| `totalTax​Amount` | String | The sum of the tax amount on the invoice lines of an invoice that’s generated for the billing transaction. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_reference_line_error.htm ===
---
page_id: connect_responses_reference_line_error.htm
title: Reference Line Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_reference_line_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Reference Line Error

Output representation of the details of the line level errors.

        
          

**JSON example**

          
: If the API request fails, the `referenceLineErrorResults` property contains a list of errors grouped by the
            invoice line IDs.

```
[
  {
    "referenceLineId": "5TV9A000007x2gz",
    "errors": [
      {
        "errorCode": "INVALID_INPUT",
        "message": "Invalid invoice line id"
      }
    ]
  }
]
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | List of errors with error code and error message for the specified invoice line ID. | Big, 62.0 | 62.0 |
| `reference​LineId` | String | ID of the invoice line specified in the API request that has an issue, causing the API request to fail. | Small, 62.0 | 62.0 |

=== ARTICLE: connect_responses_refund_line_apply_output.htm ===
---
page_id: connect_responses_refund_line_apply_output.htm
title: Refund Line Applied Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_refund_line_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Refund Line Applied Response

Output representation of the details of an applied refund. This representation includes
    the properties of a refund line, such as the date when the refund is applied against a payment
    and ID of the refund line record.

      
        
          

**JSON example**

          
: 
            

```
{
  "appliedDate": "2020-08-11T08:09:01.000Z",
  "id": "0dRR000000000CsMAI"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `appliedDate` | String | Date when the refund is applied against a payment. | Big, 64.0 | 64.0 |
| `id` | String | ID of the refund line record. | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_revenue_async_line_level.htm ===
---
page_id: connect_responses_revenue_async_line_level.htm
title: Revenue Async Line Level
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_revenue_async_line_level.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Revenue Async Line Level

Output representation of the result of the API request for the async line level
    operations.

      
        
          

**JSON example**

          
: 
            

```
  {
  "success": true,
  "requestIdentifier": "237e9877-e79b-12d4-a765-321741963000",
  "errors":[]
}
```

          

          
: If the API request fails, the `referenceLineErrorResults` property contains a list of errors grouped by the
            invoice line IDs.

```
[
  {
    "referenceLineId": "5TV9A000007x2gz",
    "errors": [
      {
        "errorCode": "INVALID_INPUT",
        "message": "Invalid invoice line id"
      }
    ]
  }
]
```

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | Details of errors, if any. | Big, 62.0 | 62.0 |
| `referenceLine​Error​Results` | [Reference Line Error](./connect_responses_reference_line_error.htm.md)[] | List of errors grouped by the invoice line IDs if the API request fails. | Big, 62.0 | 62.0 |
| `reference​Line​Type` | String | Reference type for the reference line entity in the `referenceLineErrorResults` property. | Big, 62.0 | 62.0 |
| `request​Identifier` | String | Unique identifier of the request. | Big, 62.0 | 62.0 |
| `status​URL` | String | URL to track the status of the operation. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_revenue_async_output.htm ===
---
page_id: connect_responses_revenue_async_output.htm
title: Revenue Async Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_revenue_async_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Revenue Async Response

Output representation of the result of the API request with the request
    identifier.

    
      
        
          

**JSON example**

          
: 
            

```
  {
    "errors": null,
    "requestIdentifier": "ae6f23bc-f056-44b7-aa4d-c7f6fc5e0cf4",
    "success": true
}
```

          

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Error Response](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_responses_error_response.htm) | Details of errors, if any. | Big, 62.0 | 62.0 |
| `request​Identifier` | String | Unique identifier of the request. | Big, 62.0 | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_rules_application_error_output.htm ===
---
page_id: connect_responses_rules_application_error_output.htm
title: Rules Application Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rules_application_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rules Application Error

Output representation of the error details for rules application failure.

      
        
          

**JSON example**

          
: This example shows the rules application error.

```
{
  "errors": [
    {
      "errorCode": "INVALID_ACCOUNT",
      "message": "The specified account does not exist or is not accessible."
    }
  ]
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code that indicates the type of error. | Big, 66.0 | 66.0 |
| `message` | String | Message that states the reason for error, if any. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_rules_application_output.htm ===
---
page_id: connect_responses_rules_application_output.htm
title: Rules Application
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rules_application_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rules Application

Output representation of the details of rules application.

      
        
          

**JSON example**

          
: This example shows the rules application
            response.

```
{
  "isSuccess": true,
  "rulesApplicationSummary": {
    "fetchedPaymentsCount": 250,
    "fetchedCreditMemosCount": 250,
    "totalPaymentApplications": 250,
    "totalCreditMemoApplications": 200,
    "areAllInvoicesConsidered": true
  },
  "appliedRules": [
    "Match ID",
    "Match Balance"
  ],
  "errors": []
}
```

        
      

- 
- 
- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `isSuccess` | Boolean | Indicates whether the rules are applied (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `rulesApplication​Summary` | [Rules Application Summary](./connect_responses_rules_application_summary_output.htm.md) | Summary of the application rule. This includes the number of payments and credit memos for the account, the total number of payments and credit memos that are applied to invoices, and whether all invoices for an account are considered (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `applied​Rules` | String[] | Rules that were applied. Valid values are: `Match ID` `Match Balance` `Prioritize Highest Balance Invoices` `Prioritize Oldest Invoices` | Big, 66.0 | 66.0 |
| `errors` | [Rules Application Error](./connect_responses_rules_application_error_output.htm.md)[] | Details of the errors if the API request was unsuccessful. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_rules_application_summary_output.htm ===
---
page_id: connect_responses_rules_application_summary_output.htm
title: Rules Application Summary
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_rules_application_summary_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Rules Application Summary

Output representation of the summary of the application rule. This includes the number of
    payments and credit memos for the account, the total number of payments and credit memos that's
    applied to invoices, and whether all invoices for an account are considered (true) or not
    (false).

      
        
          

**JSON example**

          
: This example shows the rules application summary.

```
{
  "rulesApplicationSummary": {
    "fetchedPaymentsCount": 5,
    "fetchedCreditMemosCount": 2,
    "totalPaymentApplications": 3,
    "totalCreditMemoApplications": 1,
    "areAllInvoicesConsidered": true
  }
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `fetched​Payments​Count` | Integer | Total number of payments related to the account. | Big, 66.0 | 66.0 |
| `fetchedCredit​Memos​Count` | Integer | Total number of credit memos or credit memo lines related to the account. | Big, 66.0 | 66.0 |
| `totalPayment​Applications` | Integer | Total number of payments that are applied to the invoices or invoice lines. | Big, 66.0 | 66.0 |
| `totalCredit​Memo​Applications` | Integer | Total number of credit memos that are applied to the invoice or invoice lines. | Big, 66.0 | 66.0 |
| `areAll​Invoices​Considered` | Boolean | Indicates whether all invoices are considered (`true`) or not (`false`). | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_send_email_for_invoice_batch_run_error.htm ===
---
page_id: connect_responses_send_email_for_invoice_batch_run_error.htm
title: Send Email Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_send_email_for_invoice_batch_run_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Send Email Error

Output representation of the error response of the API request to send emails for
    posted invoices.

    
      
        
          

**JSON example**

          
: This example shows a sample response with an error
            scenario.

```
{
  "errors": [
    {
      "errorCode": "INVALID_API_INPUT",
      "errorMessage": "Specify a valid invoiceBatchRunId."
    }
  ],
  "requestIdentifier": "5IRxx0000004CKKGA2",
  "success": false
}
```

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Unique code for the error. | Big, 65.0 | 65.0 |
| `errorMessage` | String | Descriptive message for the error. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_send_email_for_invoice_batch_run_output.htm ===
---
page_id: connect_responses_send_email_for_invoice_batch_run_output.htm
title: Send Email Response
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_send_email_for_invoice_batch_run_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Send Email Response

Output representation of the API request to send emails for posted
    invoices.

    
      
        
          

**JSON example**

          
: This example shows a sample response when the request is
            successful.

```
{
  "errors": [],
  "requestIdentifier": "5IRLT000001SIJB4A4",
  "success": true
}
```

          
: This example shows a sample response with an error
            scenario.

```
{
  "errors": [
    {
      "errorCode": "INVALID_API_INPUT",
      "errorMessage": "Specify a valid invoiceBatchRunId."
    }
  ],
  "requestIdentifier": "5IRxx0000004CKKGA2",
  "success": false
}
```

        
      

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

- 
- 
- 

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Send Email Error](./connect_responses_send_email_for_invoice_batch_run_error.htm.md)[] | List of errors that occurred while trying to enqueue the request. In case of errors while sending emails, you can check the Revenue Transaction Error Logs of the InvoiceBatchRun record and associated Invoice record. An error occurs for these scenarios. The contact email or user isn't configured. The configured email template isn't valid. Email is sent through a contact email, and the contact doesn't have an associated user. In this scenario, the emails are counted against the general email limits. An error is thrown if you exceed the email limits. | Big, 65.0 | 65.0 |
| `requestIdentifier` | String | Unique identifier for the request, which corresponds to the invoice batch run ID. | Big, 65.0 | 65.0 |
| `success` | Boolean | Indicates whether the request to start the email sending process was successfully enqueued (`true`) or not (`false`). | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequence_error_output.htm ===
---
page_id: connect_responses_sequence_error_output.htm
title: Sequence Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequence_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Error

Output representation of the error response that's associated with a request to create or
    update a sequence policy, or assign sequences.

        
          

**JSON example**

          
: This example shows a sample error
            response.

```
{
  "error": {
    "errorCode": "INVALID_INPUT",
    "message": "Specify a valid selectionLogic."
  },
  "isSuccess": false,
  "sequencePolicyId": null
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | Big, 65.0 | 65.0 |
| `message` | String | Error message for the resultant error. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequence_gap_reconciliation_error_output.htm ===
---
page_id: connect_responses_sequence_gap_reconciliation_error_output.htm
title: Sequence Gap Reconciliation Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequence_gap_reconciliation_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Gap Reconciliation Error

Output representation of the errors encountered during the processing of the API
    request.

      
        
          

**JSON example**

          
: This example shows a sample error
            response.

```
{
  "jobId": "",
  "sequencePolicyIds": [
    "1vdxx0000000abc",
    "1vdxx0000000def"
  ],
  "targetObjects": [
    "Invoice"
  ],
  "status": "NotSubmitted",
  "submittedAt": "",
  "error": {
    "errorCode": "INVALID_INPUT",
    "message": "Specify a value for either sequencePolicyIds or targetObjects."
  }
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error​Code` | String | Code for the resultant error. | Big, 65.0 | 65.0 |
| `error​Message` | String | Error message for the resultant error. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequence_gap_reconciliation_output.htm ===
---
page_id: connect_responses_sequence_gap_reconciliation_output.htm
title: Sequence Gap Reconciliation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequence_gap_reconciliation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Gap Reconciliation

Output representation of the details of the sequence gap reconciliation.

      
        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "jobId": "0B1xx0000006P12",
  "sequencePolicyIds": [
    "1vdxx0000000uyr",
    "1vdxx0000000lrf"
  ],
  "targetObjects": [
    "Invoice"
  ],
  "status": "Submitted",
  "submittedAt": "2025-06-05T09:12:28Z",
  "error": {}
}
```

          
: This example shows a sample error response for an invalid
            input.

```
{
  "jobId": "",
  "sequencePolicyIds": [
    "1vdxx0000000abc",
    "1vdxx0000000def"
  ],
  "targetObjects": [
    "Invoice"
  ],
  "status": "NotSubmitted",
  "submittedAt": "",
  "error": {
    "errorCode": "INVALID_INPUT",
    "message": "Missing required field in the request."
  }
}
```

        
      

- 
- 

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Sequence Gap Reconciliation Error](./connect_responses_sequence_gap_reconciliation_error_output.htm.md)[] | List of errors encountered during the processing of the API request. | Big, 65.0 | 65.0 |
| `jobId` | String | Unique identifier assigned to the sequence gap reconciliation asynchronous process. | Big, 65.0 | 65.0 |
| `sequence​PolicyIds` | String[] | List of IDs of the sequence policies. | Big, 65.0 | 65.0 |
| `status` | String | Status of the sequence gap reconciliation API request. Valid values are: `Submitted` `NotSubmitted` | Big, 65.0 | 65.0 |
| `submitted​At` | String | Date and time when the reconciliation request was submitted to the async job. | Big, 65.0 | 65.0 |
| `target​Objects` | String[] | List of objects to which the policies are applied. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequence_policy_output.htm ===
---
page_id: connect_responses_sequence_policy_output.htm
title: Sequence Policy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequence_policy_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequence Policy

Output representation that shows the status of the assigned sequence pattern
    values.

        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "error": null,
  "isSuccess": true,
  "sequencePolicyId": "1Vdxx0000000GRNAA2"
}
```

          
: This example shows a sample error
            response.

```
{
  "error": {
    "errorCode": "INVALID_INPUT",
    "message": "Specify a valid selectionLogic."
  },
  "isSuccess": false,
  "sequencePolicyId": null
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `error` | [Sequence Error](./connect_responses_sequence_error_output.htm.md)[] | Details of any error that encountered during the processing of the API request. | Big, 65.0 | 65.0 |
| `isSuccess` | Boolean | Indicates whether the sequence policy is generated (`true`) or not (`false`). | Big, 65.0 | 65.0 |
| `sequencePolicyId` | String | ID of the sequence policy. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequences_assignment_output.htm ===
---
page_id: connect_responses_sequences_assignment_output.htm
title: Sequences Assignment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequences_assignment_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequences Assignment

Output representation with the status of the assigned sequence pattern
    values.

    
      
        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "errors": null,
  "sequencesAssignment": [
    {
      "errors": null,
      "isSuccess": true,
      "sequencePatternValue": "INV-1234-2025-04-12-001",
      "targetObjectId": "3ttxx000000085dAAA"
    }
  ],
  "status": "Success"
}
```

        
      

    

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Sequence Error](./connect_responses_sequence_error_output.htm.md)[] | Error encountered during the processing of the API request. | Big, 65.0 | 65.0 |
| `sequencesAssignment` | [Sequences Assignment Result](./connect_responses_sequences_assignment_result_output.htm.md)[] | Details of the sequence pattern values assignment. | Big, 65.0 | 65.0 |
| `status` | String | Status of the sequence policy assignment. Valid values are: `PartialSuccess` `Success` `Failed` | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_sequences_assignment_result_output.htm ===
---
page_id: connect_responses_sequences_assignment_result_output.htm
title: Sequences Assignment Result
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_sequences_assignment_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Sequences Assignment Result

Output representation of the details of the assigned sequence values to target
    objects.

    
      
        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "errors": null,
  "sequencesAssignment": [
    {
      "errors": null,
      "isSuccess": true,
      "sequencePatternValue": "INV-1234-2025-04-12-001",
      "targetObjectId": "3ttxx000000085dAAA"
    }
  ],
  "status": "Success"
}
```

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Sequence Error](./connect_responses_sequence_error_output.htm.md)[] | Error encountered during the processing of the API request. | Big, 65.0 | 65.0 |
| `isSuccess` | Boolean | Indicates whether the sequence pattern value is assigned (`true`) or not (`false`). | Big, 65.0 | 65.0 |
| `sequencePatternValue` | String | Sequence pattern value assigned to the target object. | Big, 65.0 | 65.0 |
| `sequencePolicyId` | String | ID of the sequence policy assigned to the target object. | Big, 65.0 | 65.0 |
| `targetObjectId` | String | Record to which the sequence pattern value is assigned. | Big, 65.0 | 65.0 |

=== ARTICLE: connect_responses_statement_of_account_output.htm ===
---
page_id: connect_responses_statement_of_account_output.htm
title: Statement of Account
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_statement_of_account_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Statement of Account

Output representation of the details of the generated account statement with async
    tracking details.

        
          

**JSON example**

          
: This example shows a sample successful
            response.

```
{
  "requestIdentifier": "a0Bxx000000001ZEAQ",
  "statusURL": "/services/data/v60.0/commerce/billing/document-generation-process/a0Bxx000000001ZEAQ/status",
  "success": true,
  "accountId": "001xx000003DGb2AAG",
  "templateId": "0TRxx000000001XGAQ",
  "errors": null
}
```

          
: This example shows a sample error
            response.

```
{
  "success": false,
  "errors": [
    {
      "code": "ACCOUNT_NOT_FOUND",
      "message": "Account with ID 001XX000004DKy5YAG not found",
      "field": "accountId"
    }
  ]
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | Primary account ID the statement is generated for. | Big, 66.0 | 66.0 |
| `errors` | [Error Response](./connect_responses_error_response.htm.md)[] | List of errors encountered during the processing of the API request. | Big, 66.0 | 66.0 |
| `requestIdentifier` | String | Unique identifier for the request. | Big, 66.0 | 66.0 |
| `statusURL` | String | Status URL to track the operation. | Big, 66.0 | 66.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `templateId` | String | Document template ID that's used to generate the PDF. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_suspend_resume_billing_entity_output.htm ===
---
page_id: connect_responses_suspend_resume_billing_entity_output.htm
title: Suspend Resume Billing Object
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_suspend_resume_billing_entity_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Resume Billing Object

Output representation of the details of accounts and billing schedule groups, which are
    suspended or resumed for billing operations, along with the status of the API
    request.

    
            
                
                    

**JSON example**

                    
: 
                        

```
{
    "result":{
        {
        "referenceId": "1",
        "isSuccess": true,
        "errorcode": null,
        "errorMessage":null
        }
    }
}
```

                    

                
            

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code indicating the type of error. | Big, 63.0 | 63.0 |
| `errorMessage` | String | Message stating the reason for the error, if any. | Big, 63.0 | 63.0 |
| `isSuccess` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | Big, 63.0 | 63.0 |
| `referenceId` | String | ID of the account or billing schedule group that the suspend or resume billing request is initiated for. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_suspend_resume_billing_output.htm ===
---
page_id: connect_responses_suspend_resume_billing_output.htm
title: Suspend Resume Billing
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_suspend_resume_billing_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Resume Billing

Output representation of the list of accounts and billing schedule groups, which are
    suspended or resumed for billing operations.

    
      
        
          

**JSON example**

          
: 
            

```
{
    "result":{
        {
            "referenceId": "001DU000001o2UwYAI",
            "success": true,
            "errorcode": null,
            "errorMessage":null
        },
        {
            "referenceId": "001DU000001o2UuYAI",
            "success": false,
            "errorcode": "INVALID_API_INPUT",
            "errorMessage":"Billing is already suspended for 9Wsxx000000006TCAQ."
        }
    }
}
```

          

        
      

    

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `result` | [Suspend Resume Billing Object](./connect_responses_suspend_resume_billing_entity_output.htm.md)[] | Details of the accounts or billing schedule groups that the suspend or resume billing request is initiated for. | Big, 63.0 | 63.0 |

=== ARTICLE: connect_responses_tax_amount_details_output.htm ===
---
page_id: connect_responses_tax_amount_details_output.htm
title: Tax Amount Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_tax_amount_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Amount Details

Output representation of the details of the tax amount.

        
          

**JSON example**

          
: 
            

```
{
    "exemptAmount": 0.0,
    "taxAmount": 12.5,
    "totalAmount": 100.0,
    "totalAmountWithTax": 112.5
}

```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `exemptAmount` | Double | Amount exempted from taxation. | Big, 62.0 | 62.0 |
| `taxAmount` | Double | Tax amount applicable to the transaction. | Big, 62.0 | 62.0 |
| `totalAmount` | Double | Total amount without tax. | Big, 62.0 | 62.0 |
| `totalAmount​WithTax` | Double | Total amount with tax. The `totalAmountWithTax` property value is the sum of the `taxAmount` and `totalAmount` property values. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_tax_details_output.htm ===
---
page_id: connect_responses_tax_details_output.htm
title: Tax Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_tax_details_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Details

Output representation of the tax details for each line item.

    

        
          

**JSON example**

          
: 
            

```
{
  "taxes": [
    {
      "exemptAmount": 0,
      "exemptReason": "NoExemption",
      "imposition": {
        "type": "General"
      },
      "jurisdiction": {
        "country": "US",
        "id": "63000",
        "level": "CIT",
        "name": "SEATTLE",
        "region": "WA",
        "stateAssignedNo": "1726"
      },
      "rate": 12.5,
      "tax": 12.5,
      "taxId": "11000378132466",
      "taxableAmount": 100
    }
  ]
}
```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `exemptAmount` | Double | Amount exempted from taxation for the line item. | Big, 62.0 | 62.0 |
| `exemptReason` | String | Reason for the tax exemption. | Big, 62.0 | 62.0 |
| `imposition` | [Tax Imposition](./connect_responses_tax_imposition_output.htm.md) | Tax imposition details applicable to the line item. | Big, 62.0 | 62.0 |
| `jurisdiction` | [Tax Jurisdiction](./connect_responses_tax_jurisdiction_output.htm.md) | Details of the tax jurisdiction. | Big, 62.0 | 62.0 |
| `rate` | Double | Tax rate applied to the taxable amount to calculate the tax. | Big, 62.0 | 62.0 |
| `tax` | Double | Actual amount of tax that’s applicable to the line item. | Big, 62.0 | 62.0 |
| `taxId` | String | Unique identifier such as a code or a number that’s assigned to a specific tax. This value helps users identify which type of tax is applied. | Big, 62.0 | 62.0 |
| `taxableAmount` | Double | Total amount of the line item that’s eligible for taxation. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_tax_engine_log_output.htm ===
---
page_id: connect_responses_tax_engine_log_output.htm
title: Tax Engine Log
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_tax_engine_log_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Engine Log

Output representation of the logs that the tax engine generates.

    

        
          

**JSON example**

          
: 
            

```
{
  "taxEngineLogs": [
    {
      "createdDate": "2022-03-09T10:55:38.000Z",
      "id": "3l1xx00000000PpAAI",
      "resultCode": "Success"
    }
  ]
}

```

          

        
      

    
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `createdDate` | String | Date when the tax engine creates the log. | Big, 62.0 | 62.0 |
| `id` | String | ID of the tax engine log record. | Big, 62.0 | 62.0 |
| `resultCode` | String | Result code associated with the created log. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_tax_imposition_output.htm ===
---
page_id: connect_responses_tax_imposition_output.htm
title: Tax Imposition
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_tax_imposition_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Imposition

Output representation of the details of the imposed tax.

        
          

**JSON example**

          
: 
            

```
{
  "type": "Parish",
  "name": "Burbank"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `name` | String | Name of the tax imposition. | Big, 62.0 | 62.0 |
| `type` | String | Type of the tax imposition. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_tax_jurisdiction_output.htm ===
---
page_id: connect_responses_tax_jurisdiction_output.htm
title: Tax Jurisdiction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_tax_jurisdiction_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Jurisdiction 

Output representation of the details of the tax jurisdiction for the tax
    line.

        
          

**JSON example**

          
: 
            

```
{
    "country": "US",
    "id": "63000",
    "level": "CIT",
    "name": "SEATTLE",
    "region": "WA",
    "stateAssignedNo": "1726"
}

```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `country` | String | Country of the tax jurisdiction. | Big, 62.0 | 62.0 |
| `id` | String | ID of the tax jurisdiction. | Big, 62.0 | 62.0 |
| `level` | String | Level of the tax jurisdiction, for example, `State` and `Federal`. | Big, 62.0 | 62.0 |
| `name` | String | Name of the tax jurisdiction authority. | Big, 62.0 | 62.0 |
| `region` | String | Parent region of the tax jurisdiction. | Big, 62.0 | 62.0 |
| `stateAssigned​No` | String | Number of the assigned state. | Big, 62.0 | 62.0 |

=== ARTICLE: connect_responses_void_posted_credit_memo_output.htm ===
---
page_id: connect_responses_void_posted_credit_memo_output.htm
title: Void Posted Credit Memo
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_void_posted_credit_memo_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void Posted Credit Memo

Output representation of the request to void a posted credit memo.

      
        
          

**JSON example**

          
: This example shows a sample success
            response.

```
{
  "errors": null,
  "statusURL": "/services/data/v68.0/sobjects/AsyncOperationTracker/16Pxx0000004LdkEAE",
  "debitMemoId": "4Dmxx00000000XtAAK",
  "success": true
}
```

This example shows a sample error
            response.

```
{
  "errors": [
    {
      "errorCode": "INVALID_STATUS",
      "message": "CreditMemo 50gxx00000000XtAAI is not in the Posted status."
    }
  ],
  "debitMemoId": "",
  "success": false
}
```

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `debitMemoId` | String | ID of the created debit memo. | Big, 66.0 | 66.0 |
| `errors` | [Error Response](./connect_responses_error_response.htm.md)[] | List of errors specific to this API request that were encountered during voiding the credit memo. | Big, 66.0 | 66.0 |
| `isSuccess` | Boolean | Indicates whether the API request was successful (`true`) or not (`false`). | Big, 66.0 | 66.0 |
| `statusURL` | String | Status URL for tracking this operation. | Big, 66.0 | 66.0 |

=== ARTICLE: connect_responses_write_off_posted_invoice_list_output.htm ===
---
page_id: connect_responses_write_off_posted_invoice_list_output.htm
title: Posted Invoice List Write-Off
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_write_off_posted_invoice_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice List Write-Off 

Output representation of the list of invoices that are written off.

        
          

**JSON example**

          
: 
            

```
{
  "result": [
    {
      "requestIdentifier": null,
      "invoiceId": "3t00000000CwAGI",
      "success": false,
      "errors": {
        "errorcode": "INVALID_API_INPUT",
        "errorMessage": "Reason is missing."
      }
    },
    {
      "requestIdentifier": 37612787,
      "invoiceId": "3t00000000CwAAI",
      "success": true,
      "errors": {
        "errorcode": null,
        "errorMessage": null
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `result` | [Posted Invoice Write-Off](./connect_responses_write_off_posted_invoice_output.htm.md)[] | Details of the invoices for which the write-off process is initiated. | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_write_off_posted_invoice_output.htm ===
---
page_id: connect_responses_write_off_posted_invoice_output.htm
title: Posted Invoice Write-Off
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_write_off_posted_invoice_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice Write-Off

Output representation of the details of a posted invoice that's written off.

        
          

**JSON example**

          
: 
            

```
{
  "result": [
    {
      "requestIdentifier": null,
      "invoiceId": "3t00000000CwAGI",
      "success": false,
      "errors": {
        "errorcode": "INVALID_API_INPUT",
        "errorMessage": "Reason is missing"
      }
    },
    {
      "requestIdentifier": 37612787,
      "invoiceId": "3t00000000CwAAI",
      "success": true,
      "errors": {
        "errorcode": null,
        "errorMessage": null
      }
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errors` | [Posted Invoice Write-Off Error](./connect_responses_write_off_posted_invoice_output_error.htm.md)[] | If the request fails, this property contains a list of errors. | Small, 64.0 | 64.0 |
| `invoiceId` | String | ID of the invoice record that's written off. | Big, 64.0 | 64.0 |
| `request​Identifier` | String | If the request is successful, this property contains an asynchronous API request identifier for an invoice ID. | Big, 64.0 | 64.0 |
| `success` | Boolean | Indicates whether the invoice write-off request was successful (`true`) or not (`false`). | Big, 64.0 | 64.0 |

=== ARTICLE: connect_responses_write_off_posted_invoice_output_error.htm ===
---
page_id: connect_responses_write_off_posted_invoice_output_error.htm
title: Posted Invoice Write-Off Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_write_off_posted_invoice_output_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Posted Invoice Write-Off Error 

Output representation of the error response that's associated with a request to write off
    a posted invoice.

      
        
          

**JSON example**

          
: 
            

```
{
  "errors": {
    "errorcode": "INVALID_API_INPUT",
    "errorMessage": "Reason is missing"
  }
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `errorCode` | String | Code that represents the error. | Small, 64.0 | 64.0 |
| `error​Message` | String | Message that describes the error. | Small, 64.0 | 64.0 |

=== ARTICLE: meta_billingsettings.htm ===
---
page_id: meta_billingsettings.htm
title: BillingSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_billingsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingSettings

Represents the settings for Salesforce
		Billing.

	

	

## Parent Type and Manifest	Access

		
		

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

		

In the package manifest, all the settings metadata types for the org are accessed using the
				“Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

	

	

## File Suffix and Directory Location

		
		

The BillingSettings values are stored in the
					BillingSettings.settings file in the
					settings folder. The .settings files
				are different from other named components, because there’s only one settings file
				for each settings component.

	

	

## Version

		
		

BillingSettings components are available in API version 62.0 and later.

	

	

## Special Access Rules

		
		

These settings are available when Billing is enabled.

	

	

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
- 
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

						

				

			
| Field Name | Description |
| --- | --- |
| acctRecGlAccount | **Field Type** string **Description** General ledger account to record the credit amount for unrealized or realized losses and the debit amount for unrealized or realized gains in transaction journals. Available in API version 64.0 and later. |
| billingContextDefinition | **Field Type** string **Description** Name of the context definition that the [Create Billing Schedules for Orders API](./connect_resources_create_billing_schedules.htm.md) uses to understand your order data. Available in API version 64.0 and later. |
| billingContextSourceMapping | **Field Type** string **Description** Name of the context mapping that links Order fields to billing transaction context nodes. Available in API version 64.0 and later. |
| billingIntraCtxtSrcMapping | **Field Type** string **Description** Name of the custom context mapping that maps your custom or standard Order fields to billing transaction context nodes. Available in API version 64.0 and later. |
| defaultAPClosureDPEDefnName | **Field Type** string **Description** Org-wide default value to specify the Data Processing Engine (DPE) definition to close legal entity accounting periods. Available in API version 64.0 and later. |
| defaultApplyCreditMemoFlow | **Field Type** string **Description** Default flow that’s used to apply the credit memo to invoices. Available in API version 64.0 and later. |
| defaultBillingTreatment | **Field Type** string **Description** Org-wide default value to specify the name of the billing treatment. Available in API version 64.0 and later. |
| defaultEmailTemplate | **Field Type** string **Description** Default email template to send the generated invoice PDFs. Available in API version 64.0 and later. |
| defaultInvPreviewTemplate | **Field Type** string **Description** Default template to generate PDFs of invoice previews. Available in API version 64.0 and later. |
| defaultInvoiceDocTemplate | **Field Type** string **Description** Default template to generate PDFs of invoices. Available in API version 64.0 and later. |
| defaultLegalEntity | **Field Type** string **Description** Org-wide default value to specify the name of the legal entity. Available in API version 64.0 and later. |
| defaultTaxTreatment | **Field Type** string **Description** Org-wide default value to specify the name of the tax treatment. Available in API version 64.0 and later. |
| enableBillingDisputeManagement | **Field Type** boolean **Description** Indicates whether to enable Dispute Management (`true`) or not (`false`). The default value is `false`. Available in API version 66.0 and later. |
| enableBillingSetup | **Field Type** boolean **Description** Indicates whether to enable Billing setting (`true`) or not (`false`). The default value is `false`. |
| enableCreditMemoSequenceService | **Field Type** boolean **Description** Indicates whether to mandate the application of sequence policy for credit memos (`true`) or not (`false`). The default value is `false`.Available in API version 66.0 and later with Revenue Cloud Billing. |
| enableCrMemoApplicationToPostedInvoices | **Field Type** boolean **Description** Indicates whether to enable Apply Credits to Posted Invoices setting (`true`) or not (`false`). The default value is `false`. This setting automates settlement of invoices through application of credits to posted invoices. The credit application level determines whether credits are automatically applied to invoices or invoice lines. |
| enableFailedPaymentsRetry | **Field Type** boolean **Description** Indicates whether to retry failed payment schedule items automatically based on the defined payment retry rules (`true`) or not (`false`). The default value is `false`. Available in API version 66.0 and later. |
| enableForeignExchangeTrxnJrnlCreation | **Field Type** boolean **Description** Indicates whether to create Transaction Journal records for invoices that hold balance amounts (partially settled and not fully settled posted invoices) to record foreign exchange unrealized gains or losses during the closure activity of a legal entity accounting period. The default value is `false`. Available in API version 65.0 and later with Revenue Cloud Billing. |
| enableInvoiceEmailDelivery | **Field Type** boolean **Description** Indicates whether to enable Configure Email Delivery Settings (`true`) or not (`false`). The default value is `false`. Available in API version 63.0 and later with Revenue Cloud Billing. |
| enableInvoicePdfGeneration | **Field Type** boolean **Description** Indicates whether to enable Document Generation setting (`true`) or not (`false`). The default value is `false`. Available in API version 63.0 and later with Revenue Cloud Billing. |
| enableInvoiceSequenceService | **Field Type** boolean **Description** Indicates whether to mandate the application of sequence policy for posted invoices (`true`) or not (`false`). The default value is `false`. If enabled, each posted invoice is assigned an invoice number. Available in API version 65.0 and later with Revenue Cloud Billing. |
| enableNegInvoiceLnConversionToCrMemoLn | **Field Type** boolean **Description** Indicates whether to enable Convert Negative Invoice Lines to Credit Memo Lines setting (`true`) or not (`false`). The default value is `false`. |
| enablePaymentSchedulesAndItemsCreation | **Field Type** boolean **Description** Indicates whether to create a default payment schedule policy and payment schedule treatment (`true`) or not (`false`). The default value is `false`. If enabled, payment schedules and payment schedule items are created during financial transactions such as posting of invoices. Available in API version 64.0 and later with Revenue Cloud Billing. |
| enableRefundIssuingAndBalanceSettlement | **Field Type** boolean **Description** Indicates whether to issue refunds and settle balances (`true`) or not (`false`). The default value is `false`. If enabled, refunds are issued and credit memos are applied to any remaining invoice balance when customers amend or cancel an order. Available in API version 67.0 and later. |
| enableTransactionJournalCreation | **Field Type** boolean **Description** Indicates whether to create Transaction Journal records based on the defined general ledger account assignment rules for the billing entities when billing transaction records are created or updated (`true`) or not (`false`). The default value is `false`. Available in API version 63.0 and later with Revenue Cloud Billing. Billing transaction records include these transaction types. Invoice Invoice Line Invoice Line Tax Credit Memo Credit Memo Line Credit Memo Line Tax Payment Refund Payment Line Invoice Payment Line Invoice Line Credit Memo Inv Application Credit Memo Line Invoice Line |
| enableTransactionsApplicationToInvoices | **Field Type** boolean **Description** Indicates whether to enable Credit Application Level setting (`true`) or not (`false`). The default value is `false`. **Revenue Cloud Advanced** This setting applies balances of credit memos to invoices or balances of credit memo lines to invoice lines. For the latter, amounts and balances on the invoices are rolled-up from the related invoice lines. **Revenue Cloud Billing** This setting applies balances of credit memos and payments to invoices or balances of credit memo lines and payments lines to invoice lines. For the latter, amounts and balances on the invoices are rolled-up from the related invoice lines. |
| enableTrxnAmountsStorageInCorpCurrency | **Field Type** boolean **Description** Indicates whether to allow conversion of amounts of the Invoice, Invoice Line, Credit Memo, and Credit Memo Line records to your corporate currency (`true`) or not (`false`). The default value is `false`. Available in API version 63.0 and later. Store the converted amounts in corporate currency-specific amount fields. |
| realisedGainGlAccount | **Field Type** string **Description** Name of the general ledger account to record realized gains in transaction journals. Available in API version 64.0 and later. |
| realisedLossGlAccount | **Field Type** string **Description** Name of the general ledger account to record realized losses in transaction journals. Available in API version 64.0 and later. |
| ruleBasedCrAndPymtAppln | **Field Type** string **Description** Automates the settlement of the posted invoices by applying payments and credits that meet the specified application rules. The rules application level determines whether payments or credits are applied first to the invoices. The ruleset displays a list of selectable rules. Available in API version 66.0 and later. |
| unrealisedGainGlAccount | **Field Type** string **Description** Name of the general ledger account to record unrealized gains in transaction journals. Available in API version 64.0 and later. |
| unrealisedLossGlAccount | **Field Type** string **Description** Name of the general ledger account to record unrealized losses in transaction journals. Available in API version 64.0 and later. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a BillingSettings component.

			

```
<BillingSettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <enableBillingSetup>true</enableBillingSetup>
    <enableForeignExchangeTrxnJrnlCreation>true</enableForeignExchangeTrxnJrnlCreation>
    <enableInvoicePdfGeneration>true</enableInvoicePdfGeneration>
    <enableTransactionsApplicationToInvoices>true</enableTransactionsApplicationToInvoices>
    <enableCrMemoApplicationToPostedInvoices>true</enableCrMemoApplicationToPostedInvoices>
    <enableInvoiceEmailDelivery>true</enableInvoiceEmailDelivery>
    <enableInvoiceSequenceService>true</enableInvoiceSequenceService>
    <enableTransactionJournalCreation>true</enableTransactionJournalCreation>
    <enableTrxnAmountsStorageInCorpCurrency>true</enableTrxnAmountsStorageInCorpCurrency>
    <enablePaymentSchedulesAndItemsCreation>true</enablePaymentSchedulesAndItemsCreation>
</BillingSettings>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>Billing</members>
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

=== ARTICLE: meta_paymentssharingsettings.htm ===
---
page_id: meta_paymentssharingsettings.htm
title: PaymentsSharingSettings
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_paymentssharingsettings.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# PaymentsSharingSettings

Represents the settings to enable account-based sharing
			to view details related to Revenue Cloud Billing on the objects for Payments and
			Refunds.

		

Use account-based sharing to view Revenue Cloud Billing details on these
				objects.

				
- Payment

				
- Payment Authorization

				
- Payment Authorization Adjustment

				
- Refund

				
- Saved Payment Method

			

		

## Parent Type and Manifest Access

			

This type extends the [Metadata](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/metadata.htm) metadata type and inherits its fullName
				field.

In the package manifest, all the settings metadata types for the org
				are accessed using the “Settings” name. See [Settings](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_settings.htm) for more details.

		

## File Suffix and Directory Location

			
			

The PaymentsSharingSettings values are stored in the
					PaymentsSharing.settings file in the
					settings folder. The .settings files
				are different from other named components, because there’s only one settings file
				for each settings component.

		

		

## Version

			
			

PaymentsSharingSettings components are available in API version 64.0 and later.

		

		

## Special Access Rules

If you don’t have the View All Records
				permission to the Payments and Refunds objects, then you can:

				
- View the records only when the records have a value for the
						Account field and a shared Account ID.

				
- Use Payment Sale API and Payment Authorization API irrespective of whether the
					Account ID is null or shared.

				
- Use Payment Capture API, Authorization Reversal API, Create Payment Refund
					Billing API, and Apply Refunds to Payments API only when the corresponding
					Authorization or Payment record has a shared Account ID.

			

See [Commerce Payments
					resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm).

		

## Fields

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

- 
- 
- 
- 
- 

						

					

				
| Field Name | Description |
| --- | --- |
| delegatePaymentSharingToAccount | **Field Type** boolean **Description** Indicates whether sharing for these objects must be delegated to the corresponding Account record (`true`) or not (`false`). Payment Payment Authorization Payment Authorization Adjustment Refund Saved Payment Method The default value is `false`. If this field's value is set to `true`, you get access to these objects based on the access you have for the Account object. For example, if you have Read access to the Account object, you get Read access to the objects for Payments and Refunds. For saved payment method, the sharing is delegated to merchant account instead of account if the user has Manage Saved Payment Methods user permission. |

		

		

## Declarative Metadata Sample Definition

			
			

The
				following
				is an example of a PaymentsSharingSettings component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<PaymentsSharingSettings xmlns="http://soap.sforce.com/2006/04/metadata">
    <delegatePaymentSharingToAccount>true</delegatePaymentSharingToAccount>
</PaymentsSharingSettings>

```

			

The following is an example `package.xml` that
				references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>PaymentsSharing</members>
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

=== ARTICLE: sforce_api_objects_accountingperiod.htm ===
---
page_id: sforce_api_objects_accountingperiod.htm
title: AccountingPeriod
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_accountingperiod.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AccountingPeriod

Represents information about a time period for which businesses
         prepare reports and analyze performance. Each billing transaction is associated with an
         accounting period. This object is available in API version 62.0 and later.

      

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

You need the Accounts Receivables Admin permission set to access this object.

      

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

: 

                  

                  
                     

                     

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
| EndDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** Required. The end date of an accounting period. |
| FinancialYear | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The financial year in which an accounting period falls. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed an accounting period indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed an accounting period. If this value is null, it’s possible that the user only accessed the accounting period or a related list view (LastReferencedDate), but not viewed the accounting period itself. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The auto-generated name of an accounting period. The name is a combination of the accounting period's start date, start month, end date, and end month. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. The user who owns an Accounting Period record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| StartDate | **Type** date **Properties** Create, Filter, Group, Sort, Update **Description** Required. The start date of an accounting period. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of an accounting period. Valid values are: `Closed` `Open` |
| TotalAssetsAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of all the assets from legal entity accounting periods associated with the accounting period. This field is available in API version 65.0 and later. |
| TotalEquitiesAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of all the equities from legal entity accounting periods associated with the accounting period. This field is available in API version 65.0 and later. |
| TotalExpensesAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of all the expenses from legal entity accounting periods associated with the accounting period. This field is available in API version 65.0 and later. |
| TotalLiabilitiesAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of all the liabilities from legal entity accounting periods associated with the accounting period. This field is available in API version 65.0 and later. |
| TotalRevenueAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of all the revenue from legal entity accounting periods associated with the accounting period. This field is available in API version 65.0 and later. |

      

      

## Associated Objects

This object has the following associated objects.
            If the API version isn’t specified, they’re available in the same API versions as this
            object. Otherwise, they’re available in the specified API version and later.

            
               

**[AccountingPeriodShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

            
         

            
               

**[AccountingPeriodFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[AccountingPeriodHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_billingarrangement.htm ===
---
page_id: sforce_api_objects_billingarrangement.htm
title: BillingArrangement
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingarrangement.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingArrangement

      Represents the arrangement for invoicing a transaction’s billing amount to
         one or more accounts. The arrangement specifies whether the total amount must be invoiced
         to the owning account or a different billing account, or whether the invoices must be split
         among multiple billing accounts. This object is available in API version 66.0 and
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
- 
- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

            

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the billing arrangement record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date the billing arrangement record was last viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. A user-defined name for the billing arrangement. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the billing arrangement record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RemainderBillingPercentage | **Type** double **Properties** Filter, Sort **Description** Required. The percentage of the billing amount that isn’t assigned to any of the billing accounts. |
| ShouldBillRemainderToAccount | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether to bill the remainder billing percentage to the owning account (`true`) or not (`false`). |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies the status of the billing arrangement. Valid values are: `Active` `Draft` `Inactive` |
| VersionNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** A numerical value indicating the current version of the billing arrangement record. The version number increases when new billing arrangement line records are added or existing billing arrangement line records are updated. |

=== ARTICLE: sforce_api_objects_billingarrangementline.htm ===
---
page_id: sforce_api_objects_billingarrangementline.htm
title: BillingArrangementLine
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingarrangementline.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingArrangementLine

      Represents the billing account, billing profile, and the percentage of
         billing amount to be invoiced. Each billing arrangement line results in a separate invoice
         addressed to the selected billing account. This object is available in API version
      66.0 and later.

      
         

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

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the account that's related to the billing arrangement line. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| BillingAccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the billing account record that's related to the billing arrangement line. This field is a relationship field. **Relationship Name** BillingAccount **Refers To** BillingAccount |
| BillingArrangementId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Required. The ID of the billing arrangement record that's related to the billing arrangement line. This field is a relationship field. **Relationship Name** BillingArrangement **Relationship Type** Master-detail **Refers To** BillingArrangement (the master object) |
| BillingArrangementLineName | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort |
| BillingPercentage | **Type** double **Properties** Create, Defaulted on create, Filter, Sort, Update **Description** Required. The percentage of the billing amount to be assigned to the billing account of the billing arrangement line. |
| ShouldBillRemainder | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the remainder percentage must be billed to the billing account of the billing arrangement line (`true`) or not (`false`). The default value is `false`. |
| VersionNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** A numerical value indicating the current version of the billing arrangement record. The version number increases when new billing arrangement line records are added or existing billing arrangement line records are updated. |

=== ARTICLE: sforce_api_objects_billingbatchfiltercriteria.htm ===
---
page_id: sforce_api_objects_billingbatchfiltercriteria.htm
title: BillingBatchFilterCriteria
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchfiltercriteria.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingBatchFilterCriteria

      Represents the filter that all eligible billing schedules must satisfy in
         order to be picked up by an invoice run. This object is available in API version 62.0
      and later.

      

## Supported Calls

      
      

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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
- 
- 
- 
- 
- 
- 
- 
- 
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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

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
| BatchCriteriaId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the batch criteria record. This field is a polymorphic relationship field. **Relationship Name** BatchCriteria **Refers To** InvoiceBatchRunCriteria |
| BillingBatchFilterCriteriaNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the billing batch filter criteria. |
| ColumnEnum | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The column or field to which the filter criteria are applied. |
| CriteriaFieldType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The data type of the custom or standard criteria field. Valid values are: `CustomBoolean` `CustomCurrency` `CustomDate` `CustomLookup` `CustomNumber` `CustomPercent` `CustomText` Available in API version 63.0 and later. |
| CriteriaSequence | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The order in which the filter criteria are applied on the billing batch. |
| CustomCriteriaFieldName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The API name of the custom field on the object specified in the ObjectName field. The filter criteria is applied on the custom field. This object is available in API version 65.0 and later. |
| InvoiceRunMatchingValue | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** A value to match during an invoice run. This field is useful for filtering the invoices based on specific criteria during the billing process. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferenceDate is not null, the user accessed this record or list view indirectly. |
| ObjectName | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The object on which the filter criteria are applied. Valid values are: `AccountBillingAccount` — Available in API version 63.0 and later. `BillingAccount` — Available in API version 63.0 and later. `BillingSchedule` `BillingScheduleGroup` `CreditMemo` — Available in API version 63.0 and later. `CreditMemoInvApplication` — Available in API version 63.0 and later. `CreditMemoLine` — Available in API version 63.0 and later. `CreditMemoLineInvoiceLine` — Available in API version 63.0 and later. `CreditMemoLineTax` — Available in API version 63.0 and later. `DebitMemoLine` — Available in API version 65.0 and later. `Invoice` — Available in API version 63.0 and later. `InvoiceLine` — Available in API version 63.0 and later. `InvoiceLineTax` — Available in API version 63.0 and later. `Payment` — Available in API version 64.0 and later. `PaymentGateway` — Available in API version 64.0 and later. `PaymentLineInvoice` — Available in API version 64.0 and later. `PaymentLineInvoiceLine` — Available in API version 64.0 and later. `PaymentSchedule` — Available in API version 64.0 and later. `PaymentScheduleItem` — Available in API version 64.0 and later. `Refund` — Available in API version 64.0 and later. `RefundLinePayment` — Available in API version 64.0 and later. |
| Operation | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The type of comparison or logical operation to be performed on the specified column or field. Valid values are: `Contains` — Available in API version 63.0 and later. `Equals` `GreaterThan` — Available in API version 63.0 and later. `GreaterThanOrEqualTo` — Available in API version 63.0 and later. `InList` `LessThan` — Available in API version 63.0 and later. `LessThanOrEqualTo` `NotEquals` — Available in API version 63.0 and later. `OfType` `StartsWith` — Available in API version 63.0 and later. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the user who created the billing batch filter criteria. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PaymentRunMatchingValue | **Type** picklist **Properties** Filter, Group, Nillable, Sort **Description** A value to match during a payment run. This field is useful for filtering the payments based on specific criteria during the billing process. This field is visible but isn't used in API version 62.0. |
| StandardCriteriaField | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the standard field for the object specified in the ObjectName field. The filter criteria is applied on the standard field. Available in API version 63.0 and later. |
| Value | **Type** string **Properties** Filter, Group, Sort **Description** Required. The value to be used in the filter criteria. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
            
               

**[BillingBatchFilterCriteriaHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_billingbatchscheduler.htm ===
---
page_id: sforce_api_objects_billingbatchscheduler.htm
title: BillingBatchScheduler
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingbatchscheduler.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingBatchScheduler

Represents a scheduled processing job that triggers recurring invoice
         batch runs. This object is available in API version 62.0 and later.

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`
      

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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
- 
- 
- 
- 
- 

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

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
| BillingSchedulerName | **Type** string **Properties** Filter, Group, idLookup, Sort **Description** Required. The name of the scheduler. |
| Comments | **Type** textarea **Properties** Filter, Nillable, Sort **Description** Additional details about the billing batch scheduler. |
| CronExpression | **Type** string **Properties** Filter, Group, Sort **Description** Required. This field determines how often the scheduler recurs. |
| EndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when the scheduler stops triggering batch processing jobs. |
| FrequencyCadence | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The frequency of the scheduler triggering the invoice batch run. Valid values are: `Daily`— The scheduled job recurs every day. `Monthly`— The scheduled job recurs every month. `Once`— The scheduled job occurs one time and doesn’t recur. `Weekly`— The scheduled job recurs every week. |
| FrequencyOptions | **Type** textarea **Properties** Nillable **Description** This field is a derived field that stores the scheduler configuration. |
| JobType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The type of batch processing job that the scheduler triggers. Valid value is `Invoice` for which the scheduler starts a batch invoice run. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing batch scheduler record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing batch scheduler record. If this value is null, it’s possible that the user only accessed the billing batch scheduler record or a related list view (LastReferencedDate), but not viewed the billing batch scheduler record itself. |
| NextRunTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and timestamp of the next scheduled batch invoice run in the user's time zone. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the user who created the scheduler. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RecurringSubType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The frequency at which the batch processing job recurs when the FrequencyCadence field value is set to `Monthly`. Valid values are: `Every`— The processing job recurs at every instance of the frequency of the value. For example, if the RecurringSubType field value is `Every` and the FrequencyCadence field value is `Weekly`, then the batch processing job recurs every week. `SpecificDate`— The scheduler triggers the batch processing job on the selected date. For example, if the selected date is 5, and the FrequencyCadence field value is `Monthly`, then the job recurs on the fifth day of each month. |
| RecurringType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The frequency at which the batch processing job is repeated when the FrequencyCadence field value is set to `Weekly`. Valid value is `Every`. |
| RecursOn | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The interval at which the scheduler triggers a batch processing job. If the FrequencyCadence field value is `Monthly`, you must select either the specific date or the interval when the schedule triggers the job. Valid values are: `First` `Fourth` `Last` `Second` `Third` **Example:** To configure the scheduler to trigger the job on the first Monday of the month, set the following fields: FrequencyCadence=`Monthly` RecursOn=`First` RecursOnDay= `Monday` |
| RecursOnDate | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The date on which the scheduler triggers a batch processing job. **Example:** To configure the scheduler to trigger the job on the fifth day of the month, set the following fields: FrequencyCadence=`Monthly` RecursOnDate= 5 **Example:** To configure the scheduler to trigger the job on the second to last day of the month, set the following fields: FrequencyCadence=`Monthly` RecursOnDate=`SecondToLast` If you select `Last`, `SecondToLast`, or `ThirdToLast`, the date of the batch processing job varies depending on the number of days in the month. For example, consider `SecondToLast` is selected. If the month has 30 days, such as June, then the batch processing job occurs on the 28th day. If the month has 31 days, such as July, then the batch processing job occurs on the 29th day. |
| RecursOnDay | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The day on which the scheduler triggers a batch processing job. If the FrequencyCadence field value is set to `Weekly`, then you must select the day when the scheduler runs. The scheduler recurs every week on the selected day; for example, weekly on Monday. Valid values are: `Sunday` `Monday` `Tuesday` `Wednesday` `Thursday` `Friday` `Saturday` |
| RunCriteriaId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the filter criteria that’s defined for the invoice batch run or the payment batch run. This field is a polymorphic relationship field. **Relationship Name** RunCriteria **Refers To** InvoiceBatchRunCriteria |
| ShouldExcludeWkendAndHldy | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. Indicates whether weekends and holidays are excluded from the billing schedule (`true`) or not (`false`). The default value is `false`. |
| ShouldGenerateInvoiceDocuments | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. Indicates whether the invoice scheduler generates invoice documents (`true`) or not (`false`). This field is available in API version 68.0 and later. The default value is `false`. |
| ShouldStartRunImmediately | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. Indicates whether the invoice scheduler must start the run immediately (`true`) or not (`false`). The default value is `false`. Available in API version 63.0 and later. |
| StartDate | **Type** date **Properties** Filter, Group, Sort **Description** Required. The date when the scheduler triggers its first batch processing job. |
| StartTime | **Type** time **Properties** Filter, Sort **Description** Required. The time when the scheduler triggers the batch processing job. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The status of the scheduler. Only active schedulers can trigger batch processing jobs. Valid values are: `Active` `Canceled` `Draft` `Inactive` |
| TimeZone | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The time zone is either the value selected when the run was configured, or it's the user's time zone. The time zone is shown in Greenwich Mean Time (GMT). |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BillingBatchSchedulerShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_billingforecast.htm ===
---
page_id: sforce_api_objects_billingforecast.htm
title: BillingForecast
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingforecast.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingForecast

      Represents forecasted invoice lines generated from billing schedules before actual invoicing occurs. This object is available in API version 68.0 and later.
   

      
         

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

         
         

You need the Revenue Cloud Billing license, and the Billing Admin permission set to
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

                  

            

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the account associated with the billing forecast. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| BillingAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the billing account associated with the billing forecast. This field is a relationship field. **Relationship Name** BillingAccount **Refers To** BillingAccount |
| BillingArrangementId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the billing arrangement associated with the billing forecast. This field is a relationship field. **Relationship Name** BillingArrangement **Refers To** BillingArrangement |
| BillingMethod | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of billing used for the billing forecast. Valid values are: `Evergreen` `OrderAmount` `Usage` |
| BillingPeriodEndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The end date of the billing period for the billing forecast. |
| BillingPeriodStartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The start date of the billing period for the billing forecast. |
| BillingScheduleGroupId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the billing schedule group associated with the billing forecast. This field is a relationship field. **Relationship Name** BillingScheduleGroup **Refers To** BillingScheduleGroup |
| BillingScheduleId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the billing schedule associated with the billing forecast. This field is a relationship field. **Relationship Name** BillingSchedule **Refers To** BillingSchedule |
| BillingTermUnit | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies the unit of the billing term for the billing forecast. Valid values are: `BillingMilestonePlan` `Day` `Month` `OneTime` `Quarter` `Semi-Annual` `Week` `Year` |
| Category | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies the category of the billing forecast. Valid values are: `AmendQuantity` `Amendment` `Cancellation` `Original` `Renewal` |
| ChargeAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** Required. The charge amount for the billing forecast. |
| InvoiceBatchRunId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the invoice batch run associated with the billing forecast. This field is a relationship field. **Relationship Name** InvoiceBatchRun **Refers To** InvoiceBatchRun |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferencedDate isn’t null, the user accessed this record or list view indirectly. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity accounting period associated with the billing forecast. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity associated with the billing forecast. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number assigned to the billing forecast. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. The ID of the owner of this record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PaymentTermId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the payment term associated with the billing forecast. This field is a relationship field. **Relationship Name** PaymentTerm **Refers To** PaymentTerm |
| Quantity | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The quantity of the product or service for the billing forecast. |
| ReferenceEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the reference entity associated with the billing forecast. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntity **Refers To** Order, Quote |
| ReferenceEntityItemId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the reference entity line item associated with the billing forecast. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntityItem **Refers To** DebitMemoLine, OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, QuoteLineItem |
| UnitPrice | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The unit price of the product or service for the billing forecast. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BillingForecastShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_billingmilestoneplan.htm ===
---
page_id: sforce_api_objects_billingmilestoneplan.htm
title: BillingMilestonePlan
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingmilestoneplan.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingMilestonePlan

Represents a structured approach to invoicing where invoices are
         scheduled based on predefined milestones. This object is available in API version 63.0
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
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and the Billing Admin permission set to access
            this object.

      

      

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
- 

                  

               

            
| Field | Details |
| --- | --- |
| BillingTreatmentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Required. The billing treatment associated with the billing milestone plan. This field is a relationship field. **Relationship Name** BillingTreatment **Refers To** BillingTreatment |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Additional details about the billing milestone plan. |
| ExternalReference | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The external reference item that links a billing milestone plan item to the original transaction item. Available in API version 65.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing milestone plan record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing milestone plan record. If this value is null, it’s possible that the user only accessed the billing milestone plan record or a related list view (`LastReferencedDate`), but not viewed the billing milestone plan record itself. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the billing milestone plan. |
| ReferenceItemAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The total reference item amount to be billed. |
| ReferenceItemId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the reference item that links a billing milestone plan item to the original order item. This field is a polymorphic relationship field. **Relationship Name** ReferenceItem **Refers To** BillingSchedule, OrderItem |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the billing milestone plan. Valid values are: `Active` `Cancelled` `Completely Billed` `Draft` |

=== ARTICLE: sforce_api_objects_billingmilestoneplanitem.htm ===
---
page_id: sforce_api_objects_billingmilestoneplanitem.htm
title: BillingMilestonePlanItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingmilestoneplanitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingMilestonePlanItem

Represents a specific billing milestone within the billing milestone
         plan that’s used to manage and track billing based on the completion of certain
         deliverables or stages. This object is available in API version 63.0 and later. 

      
         

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
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and the Billing Admin permission set to access
            this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 
: 
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

                  

            

            
| Field | Details |
| --- | --- |
| BillingMilestonePlanId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The billing milestone plan associated with the billing milestone plan item. This field is a relationship field. **Relationship Name** BillingMilestonePlan **Relationship Type** Master-detail **Refers To** BillingMilestonePlan (the master object) |
| BillingScheduleGroupId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The billing schedule group that's related to the billing milestone plan item. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** BillingScheduleGroup **Refers To** BillingScheduleGroup |
| CommencementDate | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The action that triggers the start of the billing milestone plan for a date-based milestone. Valid value is: `OrderProductActivation` |
| CommencementDateOffset | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The offset applied to the commencement date to determine the milestone achievement date for a date-based milestone. |
| CommencementDateOffsetUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit of time for the commencement date offset. Valid values are: `Days` `Months` `Years` |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Additional details about the billing milestone plan item. |
| FlatAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The amount in terms of units of currency, such as $10 or $21.52, to invoice from the order item. Used only when Type field has a value of `FlatAmount`. |
| IsMilestoneAccomplished | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. Indicates whether the billing treatment is for milestone billing (`true`) or not (`false`). |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing milestone plan item record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing milestone plan item record. If this value is null, it’s possible that the user only accessed the billing milestone plan item record or a related list view (LastReferencedDate), but not viewed the billing milestone plan item record itself. |
| MilestoneAccomplishmentDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date the milestone is achieved for date-based milestones. For event-based milestones, this field indicates the date when the milestone is manually marked as completed. |
| MilestoneAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount that’s billed when the milestone is reached or completed. |
| MilestoneType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The milestone type for the billing treatment item. Valid values are: `Date` `Event` |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the billing milestone plan item. |
| Percentage | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percentage,such as 10% or 12.5%, to invoice from the order item. Used only when Type field has a value of `Percentage`. |
| ServicePeriodEnd | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The end date of the service associated with the milestone. Valid value is: `Order Product End Date` |
| ServicePeriodStart | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The start date of the service associated with the milestone. Valid value is: `Order Product Start Date` |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the billing milestone plan item. Valid values are: `Cancelled` `Draft` `Error` `Invoiced` `Ready for Invoicing` `Waiting for Milestone Accomplishment` |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies whether billing schedules created from this billing treatment item are based on a flat amount or a percentage of the order item's total amount. Valid values are: `FlatAmount` `Percentage` `Remainder` |

=== ARTICLE: sforce_api_objects_billingperioditem.htm ===
---
page_id: sforce_api_objects_billingperioditem.htm
title: BillingPeriodItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingperioditem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingPeriodItem

Represents a payment period for an invoice. The billing period item
         is used to pass billing information to an invoice line. This object is available in
      API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`
      

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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
| Amount | **Type** currency **Properties** Filter, Sort **Description** Required. The price for the billing period item. This field is used to calculate the invoice line's amount. |
| BillingPeriodEndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The end date of a billing period that’s used to calculate the invoice line’s end date. |
| BillingPeriodItemNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number identifying the billing period item. |
| BillingPeriodStartDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The start date of a billing period item that’s used to calculate the invoice line's start date. |
| BillingScheduleGroupId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the parent billing schedule group record that's related to the billing period item. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** BillingScheduleGroup **Refers To** BillingScheduleGroup |
| BillingScheduleId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the parent billing schedule record of the billing period item. This field is a relationship field. **Relationship Name** BillingSchedule **Relationship Type** Master-detail **Refers To** BillingSchedule (the master object) |
| InvoiceBatchRunId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the parent invoice batch run record of the billing period item. This field is a relationship field. **Relationship Name** InvoiceBatchRun **Refers To** InvoiceBatchRun |
| InvoiceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the parent Invoice record of the Invoice Line record that's generated from the billing period item. This field is a relationship field. **Relationship Name** Invoice **Refers To** Invoice |
| InvoiceLineId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the Invoice Line record that's generated from the billing period item. This field is populated only when a billing period item is generated by an invoice batch run. Otherwise, this field is empty. This field is a relationship field. **Relationship Name** InvoiceLine **Refers To** InvoiceLine |
| InvoiceStatus | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The status of the invoice that contains the invoice line created from the billing period item. Valid values are: `Canceled`— The invoice for this billing period item was canceled. `Draft`— The invoice has been created but hasn’t been posted. `DraftInProgress`— The invoice hasn’t been created yet. When the invoice is created, the InvoiceStatus field value is changed to `Draft`. If the invoice generation process fails, the InvoiceStatus field value shows `DraftInProgress`. `Error`— The invoice for this billing period item was generated in error. `Pending`— The invoice for this billing period item is being generated. `Posted`— An invoice line based on this billing period has been created and added successfully to the invoice. `PostingInProgress`— An invoice line based on this billing period has been created and is in the process of being added to the invoice. `Voided`— An invoice line based on this billing period was voided. `VoidInProgress`— An invoice line based on this billing period is in the process of being voided. |
| OverageQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The quantity of the usage overage that has exceeded the initial grant. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| RelatedMilestonePlanItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing milestone plan item that creates the billing period item. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a relationship field. **Relationship Name** RelatedMilestonePlanItem **Refers To** BillingMilestonePlanItem |
| RelatedUsageBillPeriodItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The method for retrieving billing information for usage-based products. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a relationship field. **Relationship Name** RelatedUsageBillPeriodItem **Refers To** UsageBillingPeriodItem |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The status of the billing period item. Draft billing period items aren't evaluated for invoice line creation. Valid values are: `Canceled` `CatchUpProcessed`. Available in API version 68.0 and later. `Draft` `Reviewed` |
| TotalUsedQuantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The total quantity of the usage resource consumed during the billing period. This includes granted entitlements, excess consumption, or consumption below the granted entitlements. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| UnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The units used to measure the overage. For example, bytes or minutes. Available in API version 63.0 and later. This field is a relationship field. **Relationship Name** UnitOfMeasure **Refers To** UnitOfMeasure |

=== ARTICLE: sforce_api_objects_billingpolicy.htm ===
---
page_id: sforce_api_objects_billingpolicy.htm
title: BillingPolicy
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingpolicy.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingPolicy

Represents information about a set of billing treatments that define
         the rules to invoice a customer for an order item. This object is available in API
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
         `undelete()`, 
         `update()`, 
         `upsert()`
      

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| BillingTreatmentSelection | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Defines how billing treatments are assigned to order items and assets that are related to the billing policy. Valid values are: `Default` `LegalEntity` `Manual` |
| DefaultBillingTreatmentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** When BillingTreatmentSelection has a value of `Default`, the selected billing treatment is used for all the order items and assets that are related to the billing policy. This field is a relationship field. **Relationship Name** DefaultBillingTreatment **Refers To** BillingTreatment |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** Additional details about the billing policy. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing policy indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing policy. If this value is null, it’s possible that the user only accessed the billing policy or a related list view (LastReferencedDate), but not viewed the accounting period itself. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the billing policy. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the billing policy. Valid values are: `Active` `Draft` `Inactive` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BillingPolicyHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_billingschedule.htm ===
---
page_id: sforce_api_objects_billingschedule.htm
title: BillingSchedule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingSchedule

Represents information about the order item that's used in the invoicing
         process. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

`describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

                  
                     

                     

: 

: 

: 
: 

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

                  

               

            
| Field | Details |
| --- | --- |
| BillDayOfMonth | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The day of the month on which a recurring billing process is scheduled to occur. |
| BilledAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount (excluding tax) that has been invoiced from the billing schedule. This field is a calculated field. |
| BillingAccountId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the account that's related to the billing schedule. This field is a relationship field. **Relationship Name** BillingAccount **Refers To** Account |
| BillingMethod | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of billing used for the source item. Valid values are: `Evergreen` `OrderAmount` `Usage—`Available in API version 63.0 and later with Revenue Cloud Billing license. |
| BillingMilestonePlanId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing milestone plan associated with the billing schedule. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a relationship field. **Relationship Name** BillingMilestonePlan **Refers To** BillingMilestonePlan |
| BillingPeriodAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount to be invoiced each billing period. For example, if the billing period is monthly, this field shows the monthly amount that appears on the invoice line. |
| BillingScheduleEndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The last date that the billing schedule is available for invoicing. This value is inherited from the EndDate field on the order item. |
| BillingScheduleGroupId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The billing schedule group that contains the billing schedule. Billing schedules are grouped when they have the same source order item. The source order item is the original order item that a customer bought. Afterwards, if the customer amends, cancels, or renews the order item, a new billing schedule is created with the BillingScheduleGroupId for the original order item. This field is a relationship field. **Relationship Name** BillingScheduleGroup **Relationship Type** Master-detail **Refers To** BillingScheduleGroup (the master object) |
| BillingScheduleNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the billing schedule. |
| BillingScheduleStartDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when the billing schedule is available for invoicing. This value is inherited from the ServiceDate field on the order item. |
| BillingTerm | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The duration for which the customer is invoiced. |
| BillingTermUnit | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The unit of measurement of the billing term. Valid values are: `BillingMilestonePlan`—Available in API version 63.0 and later with Revenue Cloud Billing license. `Day` `Month` `OneTime` `Quarter` `Semi-Annual` `Year` |
| BillingTreatmentId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the billing treatment record associated with the billing schedule. Available in API version 67.0 and later. This field is a relationship field. **Relationship Name** BillingTreatment **Refers To** BillingTreatment |
| BillingTreatmentItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing treatment item that's used to configure invoiceable amounts on the billing schedule. This field is a relationship field. **Relationship Name** BillingTreatmentItem **Refers To** BillingTreatmentItem |
| BillingType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The timing of invoicing for a product or service relative to its delivery to the customer. Valid values are: `Advance`— Invoices a product or service before its delivery. `Arrears` — Invoices a product or service after its delivery. |
| CancellationDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date from when the user can no longer access the service. For example, if a service ends on August 31, the cancellation date is September 1 because that’s the date from when the user can no longer use the service. Billing schedules past their cancellation date aren't invoiced. |
| Category | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The category of the billing schedule. Valid values are: `Amendment`— A billing schedule for an order that was amended. Available in API version 67.0 and later. `AmendQuantity`— A billing schedule for an order that changes the quantity. `Cancellation` — A billing schedule for an order that was canceled. `Original` — A billing schedule for the initial order. `Renewal` — A billing schedule for an order that was renewed. |
| CustomInvoiceGroupKey | **Type** string **Properties** Filter, Group, Restricted picklist, Sort **Description** The group identifier for which an invoice must be generated when the invoice group type is `Custom`. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| ForecastBatchRunId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the invoice batch run associated with this billing schedule that’s used for forecasting. This field is available in API version 68.0 and later. This field is a relationship field. **Relationship Name** ForecastBatchRun **Refers To** InvoiceBatchRun |
| ForecastStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the lifecycle of the billing schedule in a forecast run. This field is available in API version 68.0 and later. Valid values are: `Error` `Forecasted` `PendingForecast` `Processing` |
| InvBatchDraftToPostedRunId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The batch job that posts all invoices with a status as `Draft` that are generated by the invoice batch run associated with the billing schedule. This field is a relationship field. **Relationship Name** InvBatchDraftToPostedRun **Refers To** InvBatchDraftToPostedRun |
| InvoiceBatchRunId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The invoice batch run that evaluated the billing schedule and its billing period items to generate an invoice. This field is a relationship field. **Relationship Name** InvoiceBatchRun **Refers To** InvoiceBatchRun |
| InvoiceGroupType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether to generate an invoice for a billing schedule, a custom group, or the default group of account, bill-to-contact, payment term, currency, and tax engine. Valid values are: `Billing Schedule` `Custom` `Default` This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| InvoiceRunMatchingValue | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The batch value used by the invoice run that evaluated the billing schedule. During an invoice run, billing schedules with the same batch value, including null, are grouped to the same invoice run. |
| LastForecastRunTargetDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The target date used by the recent forecast batch run that processed this billing schedule. This field is available in API version 68.0 and later. |
| LineAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount associated with a specific line item in the billing schedule. Available in API version 63.0 and later. |
| NetUnitPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** The net unit price of the order item for which the billing schedule was created. Available in API version 64.0 and later. |
| NextBillingDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date that the next billing period starts for the invoice. This date is used to calculate which invoice lines are included on an invoice. When an invoice scheduler or API evaluates an order for invoicing, billing schedules with a next billing date on or before the invoice's target date are included in the invoice. |
| NextChargeFromDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date that the billing schedule is invoiced in the upcoming billing period. For example, if you invoiced a customer for a billing period of 01/01/24 through 01/31/24, the billing schedule's NextChargeFromDate is 02/01/22. |
| OriginalBillingScheduleId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** If the billing schedule is an amended or canceled billing schedule, then this field shows the original billing schedule. Otherwise, this field is null. This field is a relationship field. **Relationship Name** OriginalBillingSchedule **Refers To** BillingSchedule |
| PendingAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount from the current billing term that hasn't been billed yet. For example, the unbilled amount for a month, quarter, or year, depending on this billing schedule's billing term. |
| PricingTermUnit | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The unit of time for which the pricing of the product applies. Valid values are: `Months` `Quarterly` `Semi-Annual` `Annual` Available in API version 66.0 and later. |
| ProcessingOrder | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** Specifies the order in which billing transactions are applied. Available in API version 67.0 and later. This field is an autogenerated field. |
| Quantity | **Type** double **Properties** Filter, Nillable, Sort **Description** The quantity of the order item that created the billing schedule. |
| RampIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the ramp deal that groups billing schedules belonging to the same ramped product. This field is available in API version 68.0 and later. |
| Reference | **Type** reference **Properties** Filter, Group, idLookup, Sort **Description** Required. The ID of the parent record of the reference item for which the billing schedule is created. Available in API version 61.0 and later. |
| ReferenceEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The parent order of the order item that created the billing schedule. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntity **Refers To** Order |
| ReferenceEntityItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The order item or asset that created the billing schedule. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntityItem **Refers To** OrderItem, OrderItemAdjustmentLineItem |
| ReferenceItem | **Type** reference **Properties** Filter, Group, idLookup, Sort **Description** The ID of the transaction line item record for which the billing schedule is created. Available in API version 61.0 and later. |
| SubCategory | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The subcategory of the billing schedule. Available in API version 67.0 and later. Valid values are: `AsIsRenewal` `BillingFrequencyAmendment` `ChangeEndDate` `DeltaPriceAmend` `PriceAmend` `QuantityAmendment` `SimplifiedCancel` `SimplifiedRenewal` |
| SegmentIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the ramp segment in which the billing schedule is grouped. This field is available in API version 68.0 and later. |
| SegmentName | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The name of the ramp segment. This field is available in API version 68.0 and later. |
| SegmentType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of the ramp segment. This field is available in API version 68.0 and later. Valid values are: `Custom` `FreeTrial` `Prorated` `Yearly` The default value is `Yearly`. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the order item that the billing schedule represents. Valid values are: `WaitingForMilestoneEventAccomplishment`—Available in API version 63.0 and later with Revenue Cloud Billing license. `CompletelyBilled` `Error` `Processing` `ReadyForInvoicing` |
| TaxTreatmentId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the treatment that's used to calculate tax for the billing schedule. This value is defined based on the order item's tax policy. This field is a relationship field. **Relationship Name** TaxTreatment **Refers To** TaxTreatment |
| TotalAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of the order item represented by the billing schedule. |
| Type | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The type of the billing schedule. Valid values are: `LineItemAdjustedCharge` `LineItemAdjustment` `LineItemCharge` |
| UnitOfMeasureId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the unit of measure for the billing schedule. Available in API version 63.0 and later. This field is a relationship field. **Relationship Name** UnitOfMeasure **Refers To** UnitOfMeasure |
| UnitPrice | **Type** currency **Properties** Filter, Nillable, Sort **Description** The price for an individual unit of the billing schedule's parent order item, including charges, adjustments, and discounts. This value is inherited from the order item's UnitPrice field. |
| UsageResourceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The usage resource associated with the billing schedule. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a relationship field. **Relationship Name** UsageResource **Refers To** UsageResource |

=== ARTICLE: sforce_api_objects_billingschedulecreatedevent.htm ===
---
page_id: sforce_api_objects_billingschedulecreatedevent.htm
title: BillingScheduleCreatedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulecreatedevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_pfrm_evnt_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingScheduleCreatedEvent

Notifies subscribers when the `/commerce/invoicing/billing-schedules/actions/create` request is complete.
      This object is available in API version 63.0 and later.

      

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

         
         

`/event/billingschedulecreatedevent`

      

      

## Event Delivery Allocation Enforced

         
         

No

      

      

## Special Access Rules

         
         

This object is available when Billing is enabled.

      

      

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
| BillingScheduleCreatedEventDetail | **Type** [BillSchdCreatedEventDetail](./sforce_api_objects_billschdcreatedeventdetail.htm.md) **Properties** Nillable **Description** One `BillingScheduleCreatedEventDetail` entry is created for each order item in the `BillingScheduleCreatedEvent` request. One `BillSchdCreatedEventDetail` entry is created for each error that occurred. |
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** ID returned in the `CreateBillingScheduleFromOrderItem` response. Use this ID to identify the `BillingScheduleCreatedEvent` for a specific request. |

      

   

- 
**[BillSchdCreatedEventDetail](./sforce_api_objects_billschdcreatedeventdetail.htm.md)**  

Contains details about each order item in the `/commerce/invoicing/billing-schedules/actions/create` request and any errors          that occurred while processing the request. This object is included in an `BillingScheduleCreatedEvent` message. You can't subscribe to          the `BillSchdCreatedEventDetail` platform event          directly. This object is available in API version 63.0 and later.

=== ARTICLE: sforce_api_objects_billingschedulegroup.htm ===
---
page_id: sforce_api_objects_billingschedulegroup.htm
title: BillingScheduleGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingschedulegroup.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingScheduleGroup

Represents a consolidated view of all the billing schedules related
         to the order items generated from one asset, including new orders and amendment
         orders. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

            `delete()`, `describeLayout()`, `describeSObjects()`,
               `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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

: 

: 

                  

                  
                     

                     

: 

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
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AnchorProdtBillingSchdGrpId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing schedule group for the anchor product in a usage-based product. The anchor product contains the grants for the usage-based product. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a relationship field. **Relationship Name** AnchorProdtBillingSchdGrp **Refers To** BillingScheduleGroup |
| BillDayOfMonth | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The day of the month on which a recurring billing process is scheduled to occur. |
| BillToContactId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the contact related to the billing schedule group.﻿ This field can’t be modified when related billing schedules are in processing. This field is a relationship field. **Relationship Name** BillToContact **Refers To** Contact |
| BillingAccountId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the account that's related to the billing schedule group. This field is a relationship field. **Relationship Name** BillingAccount **Refers To** Account |
| BillingAddress | **Type** address **Properties** Filter, Nillable **Description** The compound form of the billing address. Read only. See [Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/compound_fields_address.htm) for details on compound address fields. |
| BillingArrangementId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the billing arrangement that’s related to the billing schedule group. Available in API version 66.0 and later. This field is a relationship field. **Relationship Name** BillingArrangement **Refers To** BillingArrangement |
| BillingMethod | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The type of billing used for the source item. Valid values are: `Evergreen` `OrderAmount` `Usage` |
| BillingResumptionDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when billing for the asset related to the billing schedule group is resumed. Available in API version 63.0 and later. |
| BillingScheduleGroupNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the billing schedule group. |
| BillingStartMonth | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** This is a read-only field used with annual billing. The field shows the numbers from 1 through 12, which indicate the month when billing begins for an annual subscription. For example, if billing starts in January, the value is 1; if billing starts in June, the value is 6. |
| BillingSuspensionDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when billing for the asset related to the billing schedule group is suspended. Available in API version 63.0 and later. |
| BillingTerm | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** This field is used with BillingTermUnitfield to define a billing cycle. For example, bill every 20 days or every two months. In this example, the BillingTerm field value is 20 and the BillingTermUnit field value is `Day`. |
| BillingTermUnit | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The unit of measurement of the billing term. Valid values are: `BillingMilestonePlan`—Available in API version 63.0 and later with Revenue Cloud Billing license. `Day` `Month` `OneTime` `Quarter` `Semi-Annual` `Year` |
| BillingTreatmentId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing treatment item that's used to configure invoiceable amounts on the billing schedule group. This field is a relationship field. **Relationship Name** BillingTreatment **Refers To** BillingTreatment |
| BillingType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The timing of invoicing for a product or service relative to its delivery to the customer. Valid values are: `Advance`— Invoices a product or service before its delivery. `Arrears`— Invoices a product or service after its delivery. |
| BindingInstanceId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The asset or custom object record associated with the billing schedule group. This field is available in API version 63.0 and later with Revenue Cloud Billing license. This field is a polymorphic relationship field. **Relationship Name** BindingInstance **Refers To** Asset |
| CancellationDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date from when the user can no longer access the service. For example, if a service ends on August 31, the cancellation date is September 1 because that’s the date from when the user can no longer use the service. Billing schedules past their cancellation date aren't invoiced. |
| Controller | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. During the invoicing process, this field determines which date is used when the billing schedule group and billing schedule have a related field with conflicting values. For example, when Controller has a value of `BillingScheduleGroup`, if the billing schedule's billing day of month is 5 while the billing schedule group's billing day of month is 10, the invoice is sent on the 10th day of the month. Valid values are: `BillingScheduleGroup` `None` |
| EffectiveNextBillingDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The earliest NextBillingDate from all billing schedules in the billing schedule group. This field is a reference field that isn't used for any features or calculations. This field is a calculated field. |
| EndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The end date of the billing schedule group. |
| ExternalBindingInstance | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The custom target associated with the entitlements that are granted with the sellable product. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| ExternalRefRecordIdentifier | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The identifier of the external record for which the billing schedule group was created. Available in API version 64.0 and later. |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the legal entity that's related to the billing schedule group. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| NextBillingDateOverride | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The next billing date for all the billing schedules related to the billing schedule group. If specified, this date overrides the next billing dates of the billing schedules. Available in API version 63.0 and later. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. The ID of the user who created the billing schedule group. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PaymentTermId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the payment term used in this billing schedule group. ﻿This field can’t be modified when related billing schedules are in processing. This field is a relationship field. **Relationship Name** PaymentTerm **Refers To** PaymentTerm |
| PeriodBoundary | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** This field is inherited from the order item's parent quote line item or sales transaction item. The period boundary determines the start and end date of the billing periods. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` |
| Product2Id | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The product that was charged or ordered to create the billing schedule group. This field is a relationship field. **Relationship Name** Product2 **Refers To** Product2 |
| ProductName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the product for the order item that's represented by each billing schedule in the billing schedule group. |
| ProrationPolicyId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the proration policy that applies to this billing schedule group. The proration policy defines how time periods are calculated for orders. For example, whether partial periods are allowed. This field is inherited from the shared proration policy for each billing schedule in the billing schedule group. This field is a relationship field. **Relationship Name** ProrationPolicy **Refers To** ProrationPolicy |
| ReferenceEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The asset used to create the billing schedules in the billing schedule group. This field is a relationship field. **Relationship Name** ReferenceEntity **Refers To** Asset |
| ReferenceRecordId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the Salesforce record for which the billing schedule group was created. Available in API version 64.0 and later. This field is a polymorphic relationship field. **Relationship Name** BillingScheduleGroups |
| SavedPaymentMethodId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the SavedPaymentMethod record that's used to collect payment for the billing schedule group. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** BillingScheduleGroups **Refers To** SavedPaymentMethod |
| ShipFromAddress | **Type** address **Properties** Filter, Nillable **Description** The address from which the product in the billing schedule group is shipped. Available in API version 64.0 and later. |
| ShippingAddress | **Type** address **Properties** Filter, Nillable **Description** The compound form of the shipping address. See [Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/compound_fields_address.htm) for details on compound address fields. This field is a read-only field. |
| StartDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The earliest start date from all billing schedules in the billing schedule group. |
| TaxTreatmentId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the tax treatment record that's used to calculate tax for the billing schedule group. This value is defined based on the order item's tax policy. This field is a relationship field. **Relationship Name** TaxTreatment **Refers To** TaxTreatment |
| TotalBilledAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount that has been invoiced for the billing schedules within the billing schedule group. This field is a calculated field. |
| TotalPendingAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount that hasn't yet been invoiced for the billing schedules within the billing schedule group. This field is a calculated field. |
| UsageType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The usage type for the billing schedule group. Valid values are: `Revenue Cloud` `Commerce Cloud` `Insurance Cloud` Available in API version 66.0 and later. |

=== ARTICLE: sforce_api_objects_billingtreatment.htm ===
---
page_id: sforce_api_objects_billingtreatment.htm
title: BillingTreatment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingTreatment

Represents information about the billing of an order item. This
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
            `undelete()`, 
            `update()`, 
            `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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
| BillingPolicyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The billing policy that's related to the billing treatment. This field is a relationship field. **Relationship Name** BillingPolicy **Refers To** BillingPolicy |
| CanChangeBillingFrequency | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the billing frequency can be changed for the billing treatment (`true`) or not (`false`). The default value is `false`. |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** Additional details about the billing treatment. |
| ExcludeFromBilling | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies whether any order items assigned to the treatment are excluded from billing. Valid values are: `No` `Yes` |
| IsMilestoneBilling | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. Indicates whether the billing treatment is for milestone billing (`true`) or not (`false`). The default value is `false`. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing treatment indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing treatment. If this value is null, it’s possible that the user only accessed the billing treatment or a related list view (LastReferencedDate), but not viewed the billing treatment itself. |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity that's used to assign the treatment to order items when the parent billing policy's BillingTreatmentSelection field value is `LegalEntity`. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the billing treatment. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the billing treatment. Valid values are: `Active` `Draft` `Inactive` Draft or inactive billing treatments can't be assigned to order items. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BillingTreatmentHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_billingtreatmentitem.htm ===
---
page_id: sforce_api_objects_billingtreatmentitem.htm
title: BillingTreatmentItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billingtreatmentitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillingTreatmentItem

Represents information about allocation of the total amount of an
         order item to billing schedules throughout the order item's lifecycle. This object is
      available in API version 62.0 and later.

      
         

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

         
         

You need the Billing Admin permission set to access this object.

      

      

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
: 
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
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| BillingTreatmentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Required. The parent billing treatment for the billing treatment item. This field is a relationship field. **Relationship Name** BillingTreatment **Relationship Type** Master-detail **Refers To** BillingTreatment (the master object) |
| BillingType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The timing of invoicing for a product or service relative to its delivery to the customer. Advance billing invoices a product or service before its delivery, whereas arrears billing invoices it after delivery. The billing system assesses the billing type to determine the next billing date for an order product. Valid values are: `Advance`—If the order item is billed in advance, the order’s billing day of month is evaluated to choose the nearest date on or before the order product’s start date. For example, if a monthly order product’s start date is January 1, and the order’s billing day of month is 15, the next billing date is December 15. `Arrears`—If the order item is billed in arrears, the order’s billing day of month is evaluated to choose the nearest date after the order product’s start date. For example, if a monthly order product’s start date is January 1, and the order’s billing day of month is 15, the order product’s next billing date is January 15. `None` |
| Controller | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. During the invoicing process, this field determines which value is used when the billing schedule group and billing schedule have a shared field with different values. For example, when Controller has a value of `BillingScheduleGroup`, if the billing schedule's billing day of month is 5 while the billing schedule group's billing day of month is 10, the value of 10 is used. Valid values are: `BillingScheduleGroup` `None` |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** Additional details about the billing treatment item. |
| FlatAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The amount in terms of units of currency (such as $10 or $21.52) to invoice from the order item. Used only when Type has a value of `FlatAmount`. |
| Handling0Amount | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies how invoices are generated for billing period items that have an amount of $0. Valid values are: `CreateInvoice` `None` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing treatment item indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing treatment item. If this value is null, it’s possible that the user only accessed the billing treatment item or a related list view (`LastReferencedDate`), but not viewed the billing treatment item itself. |
| MilestoneStartDate | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The occurrence whose date is used to calculate the milestone accomplishment date for the associated billing milestone plan item based on the provided offset details. Valid value is: `OrderProductActivation` This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| MilestoneStartDateOffset | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The calculated value that determines the time difference from the start of a milestone. This value is calculated from the milestone start date record. This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| MilestoneStartDateOffsetUnit | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The unit type to use with the milestone start date offset, which defines the milestone date. Valid values are: `Days` `Months` `Years` This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| MilestoneType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The milestone type for the billing treatment item. Valid values are: `Date` `Event` This field is available in API version 63.0 and later with Revenue Cloud Billing license. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the billing treatment item. |
| Percentage | **Type** percent **Properties** Create, Filter, Nillable, Sort, Update **Description** The percentage (such as 10% or 12.5%) to invoice from the order item. Used only when Type field has a value of `Percentage`. |
| ProcessingOrder | **Type** int **Properties** Create, Filter, Group, Sort, Update **Description** Required. The order in which billing schedules are created based on each billing treatment item. Lower numbers are evaluated first. For example, if your billing treatment has a billing treatment item that invoices at 25 percentage and a `ProcessingOrder` of 1, and another item that invoices at 75 percentage and a `ProcessingOrder` of 2, your first billing schedule will be for 25% of the order item's total amount, and your second billing schedule will be for 75% of the order item's total amount. |
| Sequencing | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The number used to start invoice numbers on invoices generated from this billing treatment item. Valid values are: `Manual` `None` |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the billing treatment item. Valid values are: `Active` `Draft`– Draft billing treatment items aren't evaluated for creating billing schedules. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. Specifies whether billing schedules created from this billing treatment item are based on a flat amount or a percentage of the order item's total amount. Valid values are: `FlatAmount` `Percentage` `Remainder` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[BillingTreatmentItemHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_billschdcreatedeventdetail.htm ===
---
page_id: sforce_api_objects_billschdcreatedeventdetail.htm
title: BillSchdCreatedEventDetail
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_billschdcreatedeventdetail.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: sforce_api_objects_billingschedulecreatedevent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BillSchdCreatedEventDetail

Contains details about each order item in the `/commerce/invoicing/billing-schedules/actions/create` request and any errors
         that occurred while processing the request. This object is included in an `BillingScheduleCreatedEvent` message. You can't subscribe to
         the `BillSchdCreatedEventDetail` platform event
         directly. This object is available in API version 63.0 and later.

      

## Supported Calls

      
      

         `describeSObjects()`
      

      

      

## Special Access Rules

This object is available when Billing is enabled in your org.

      

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
| BillingScheduleId | **Type** reference **Properties** Nillable **Description** If the request was successful, this field contains the ID of the billing schedule for the order item. This field is a relationship field. **Relationship Name** BillingSchedule **Refers To** BillingSchedule |
| ErrorCode | **Type** string **Properties** Nillable **Description** If the request wasn’t successful, this field contains the error code. |
| ErrorMessage | **Type** string **Properties** Nillable **Description** If the request wasn’t successful, this field contains the error message. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| IsSuccess | **Type** boolean **Properties** Defaulted on create **Description** Indicates whether the request to create a billing schedule for the order item is successful (`true`) or not (`false`). The default value is `false`. |
| OrderItemId | **Type** reference **Properties** **Description** The ID of the order item used in the ` /actions/standardCreateBillingScheduleFromOrderItem` REST request. This field is a relationship field. **Relationship Name** OrderItem **Refers To** OrderItem |

=== ARTICLE: sforce_api_objects_bsgrelationship.htm ===
---
page_id: sforce_api_objects_bsgrelationship.htm
title: BsgRelationship
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_bsgrelationship.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BsgRelationship

Represents a relationship between billing schedule groups to support
         bundles where one parent billing schedule group has multiple child billing schedule
         groups. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`
      

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set to access this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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

                  

            

            
| Field | Details |
| --- | --- |
| AssociatedBsgId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the related billing schedule group. In a bundle relationship, this billing schedule group is the child. This field is a relationship field. **Relationship Name** AssociatedBsg **Refers To** BillingScheduleGroup |
| AssociatedBsgPricing | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. This field describes how the related billing schedule group is priced relative to the primary billing schedule group. Valid values are: `IncludedInBundlePrice` `NotIncludedInBundlePrice` |
| AssociatedBsgRole | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. This field describes the role of the related billing schedule group in the relationship. Valid values are: `AddOnComponent` `BundleComponent` `ClassificationComponent` `SetComponent` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a billing schedule group record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a billing schedule group relationship record. If this value is null, it’s possible that the user only accessed the billing schedule group relationship record or a related list view (LastReferencedDate), but not viewed the billing schedule group relationship record itself. |
| MainBsgId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the primary billing schedule group. In a bundle relationship, this billing schedule group is the parent. This field is a relationship field. **Relationship Name** MainBsg **Relationship Type** Master-detail **Refers To** BillingScheduleGroup (the master object) |
| MainBsgRole | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. This field describes the role of the primary billing schedule group in the relationship. Valid values are: `AddOn` `Bundle` `Set` |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the billing schedule relationship. |
| ProductRelationshipTypeId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the relationship type between the main and associated billing schedule group. This field is a relationship field. **Relationship Name** ProductRelationshipType **Refers To** ProductRelationshipType |

=== ARTICLE: sforce_api_objects_caseserviceprocessextension.htm ===
---
page_id: sforce_api_objects_caseserviceprocessextension.htm
title: CaseServiceProcessExtension
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_caseserviceprocessextension.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CaseServiceProcessExtension

Represents additional information for a case record based on the type of service
         process for which the case was raised. This object is available in API version 67.0
      and later.

      

         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

      

      

## Special Access Rules

         
         

You need the Billing Admin, Billing Operations User, or Billing Customer Service User
                permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| CaseId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The case record related to the invoice. **Relationship Name** Case **Relationship Type** Master-detail **Refers To** Case |
| CaseServiceProcessExtensionNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The autogenerated number of the case. |
| CustomServiceProcess | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the name of the service process when the type of service process is `Custom`. |
| IntakeMethod | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Update **Description** Specifies whether the case was raised internally within the org or by using the self-service Billing portal. Valid values are: `Internal` `External` |
| ReferenceRecordId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The record ID associated with the case record such as an invoice record. This field is a polymorphic relationship field. **Relationship Name** CaseServiceProcessExtensionsByReference |
| ServiceProcess | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the type of service process that created the case. Valid values are: `Extend Invoice Due Date` `Invoice Charge Correction` `Suspend Billing` `Update Bill-To Contact` `Other Billing Inquiries` `Custom` |
| ReferenceRecordId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The record ID associated with the case record such as an invoice record. This field is a polymorphic relationship field. **Relationship Name** CaseServiceProcessExtensionsByReference |
| UsageType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the name of the cloud or function that uses the CaseServiceProcessExtension object. Valid value is `Billing`. |

      

      

## Usage

         
         

This section covers a sample Apex class to support backward compatibility for cases
                created before the availability of the `CaseServiceProcessExtension` object. The class finds billing cases that
                don't yet have extension records, maps service process values from service catalog
                extended attributes for supported templates. This class also populates required
                extension fields such as service process, reference record ID, usage type, and
                intake method. For other billing queries where template entries aren’t available in
                extended attributes, the class optionally accepts product IDs to identify and
                process those cases. The implementation runs as batch Apex for large data volumes
                and reports processing results in logs.

         

This example shows a sample Apex class. You can modify this class as per your
                requirements.

         /**
 * Batchable Apex class to backfill CaseServiceProcessExtension records
 * for billing cases that were created in API version 66.0 and earlier.
 *
 * Identifies billing cases with no CaseServiceProcessExtension and populates the extension record.
 *
 * Additionally, accepts a set of Product IDs to identify billing cases and populates the extension record
 * for other billing inquiries.
 *
 * Usage:
 *   Set<Id> productIds = new Set<Id>{'01tXX0000000001', '01tXX0000000002'};
 *   Database.executeBatch(new BillingCaseServiceProcessExtensionBatch(productIds), 200);
 *
 */
public class BillingCaseServiceProcessExtensionBatch implements Database.Batchable<SObject>, Database.Stateful {

    private static final Map<String, String> TEXT_VALUE_TO_SERVICE_PROCESS = new Map<String, String>{
        'billing_svc_update_billToContact' => 'UpdateBillToContact',
        'billing_svc_due_date_extension' => 'ExtendInvoiceDueDate',
        'billing_svc_incorrect_invoice_charges' => 'InvoiceChargeDispute',
        'billing_svc_suspend_billing' => 'SuspendBilling'
    };

    private static final Map<String, String> PRODUCT_NAME_KEYWORD_TO_SERVICE_PROCESS = new Map<String, String>{
        'bill to contact' => 'UpdateBillToContact',
        'due date' => 'ExtendInvoiceDueDate',
        'invoice charge' => 'InvoiceChargeDispute',
        'suspend billing' => 'SuspendBilling',
        'other billing' => 'OtherBillingInquiry'
    };

    private final Set<Id> productIds;
    private Integer totalProcessed = 0;
    private Integer totalCreated = 0;
    private Integer totalErrors = 0;

    public BillingCaseServiceProcessExtensionBatch(Set<Id> productIds) {
        this.productIds = productIds != null ? productIds : new Set<Id>();
    }

    public Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator([
            SELECT Id, SourceId
            FROM Case
            WHERE SourceId != NULL
              AND Id NOT IN (SELECT CaseId FROM CaseServiceProcessExtension)
        ]);
    }

    public void execute(Database.BatchableContext bc, List<Case> scope) {
        totalProcessed += scope.size();

        // Build CaseId -> SourceId map and collect unique SourceIds for bulk query
        // Filter for ServiceCatalogRequest IDs (prefix '946')
        Map<Id, Id> caseIdToSourceId = new Map<Id, Id>();
        Set<Id> sourceIds = new Set<Id>();
        for (Case c : scope) {
            if (c.SourceId != null && String.valueOf(c.SourceId).startsWith('946')) {
                caseIdToSourceId.put(c.Id, c.SourceId);
                sourceIds.add(c.SourceId);
            }
        }

        // Single merged query: billing text values + 3tt reference records
        List<SvcCatalogReqExtdAttrVal> attrVals = [
            SELECT SvcCatalogRequestId, TextValue
            FROM SvcCatalogReqExtdAttrVal
            WHERE SvcCatalogRequestId IN :sourceIds
              AND (TextValue IN :TEXT_VALUE_TO_SERVICE_PROCESS.keySet()
                   OR TextValue LIKE '3tt%')
        ];

        // Step 1: Identify billing ServiceCatalogRequestIds and their ServiceProcess
        Map<Id, String> sourceIdToServiceProcess = new Map<Id, String>();
        for (SvcCatalogReqExtdAttrVal attr : attrVals) {
            if (TEXT_VALUE_TO_SERVICE_PROCESS.containsKey(attr.TextValue)) {
                sourceIdToServiceProcess.put(
                    attr.SvcCatalogRequestId,
                    TEXT_VALUE_TO_SERVICE_PROCESS.get(attr.TextValue)
                );
            }
        }

        // Step 2: Identify remaining billing cases via ProductId on ServiceCatalogRequest
        Map<Id, String> sourceIdToCustomServiceProcess = new Map<Id, String>();
        if (!this.productIds.isEmpty()) {
            Set<Id> unmatchedSourceIds = new Set<Id>();
            for (Id sid : sourceIds) {
                if (!sourceIdToServiceProcess.containsKey(sid)) {
                    unmatchedSourceIds.add(sid);
                }
            }

            if (!unmatchedSourceIds.isEmpty()) {
                List<SvcCatalogRequest> catalogRequests = [
                    SELECT Id, ProductId, Product.Name
                    FROM SvcCatalogRequest
                    WHERE Id IN :unmatchedSourceIds
                      AND ProductId IN :productIds
                ];

                for (SvcCatalogRequest scr : catalogRequests) {
                    String serviceProcess = deriveServiceProcessFromProductName(scr.Product.Name);
                    sourceIdToServiceProcess.put(scr.Id, serviceProcess);
                    if (serviceProcess == 'Custom' && scr.Product.Name != null) {
                        sourceIdToCustomServiceProcess.put(scr.Id, scr.Product.Name);
                    }
                }
            }
        }

        // Step 3: Extract Invoice ReferenceRecord values for all confirmed billing cases
        Map<Id, Id> sourceIdToReferenceRecord = new Map<Id, Id>();
        for (SvcCatalogReqExtdAttrVal attr : attrVals) {
            if (attr.TextValue != null
                && attr.TextValue.startsWith('3tt')
                && sourceIdToServiceProcess.containsKey(attr.SvcCatalogRequestId)) {
                sourceIdToReferenceRecord.put(attr.SvcCatalogRequestId, (Id) attr.TextValue);
            }
        }

        // Step 4: For invoice charge dispute and other billing enquiries, check for dispute records
        // and prefer the dispute invoice ID over the text value-based invoice ID.
        Set<Id> disputeServiceProcessCaseIds = new Set<Id>();
        Map<Id, Id> disputeCaseIdToSourceId = new Map<Id, Id>();
        for (Case c : scope) {
            Id sourceId = caseIdToSourceId.get(c.Id);
            if (sourceId != null && sourceIdToServiceProcess.containsKey(sourceId)) {
                String serviceProcess = sourceIdToServiceProcess.get(sourceId);
                if (serviceProcess == 'InvoiceChargeDispute' || serviceProcess == 'OtherBillingInquiry') {
                    disputeServiceProcessCaseIds.add(c.Id);
                    disputeCaseIdToSourceId.put(c.Id, sourceId);
                }
            }
        }

        if (!disputeServiceProcessCaseIds.isEmpty()) {
            List<Dispute> disputes = [
                SELECT Id, CaseId, InvoiceId
                FROM Dispute
                WHERE CaseId IN :disputeServiceProcessCaseIds
                  AND InvoiceId != NULL
            ];

            for (Dispute dispute : disputes) {
                // Override with Dispute's InvoiceId (this takes precedence over TextValue)
                Id sourceId = disputeCaseIdToSourceId.get(dispute.CaseId);
                if (sourceId != null) {
                    sourceIdToReferenceRecord.put(sourceId, dispute.InvoiceId);
                }
            }
        }

        // Build CaseServiceProcessExtension records
        List<CaseServiceProcessExtension> extensions = new List<CaseServiceProcessExtension>();
        for (Case c : scope) {
            Id sourceId = caseIdToSourceId.get(c.Id);
            if (sourceIdToServiceProcess.containsKey(sourceId)) {
                CaseServiceProcessExtension ext = new CaseServiceProcessExtension();
                ext.CaseId = c.Id;
                ext.ServiceProcess = sourceIdToServiceProcess.get(sourceId);
                ext.UsageType = 'Billing';
                ext.IntakeMethod = 'External';
                if (sourceIdToReferenceRecord.containsKey(sourceId)) {
                    ext.ReferenceRecordId = sourceIdToReferenceRecord.get(sourceId);
                }
                if (sourceIdToCustomServiceProcess.containsKey(sourceId)) {
                    ext.CustomServiceProcess = sourceIdToCustomServiceProcess.get(sourceId);
                }
                extensions.add(ext);
            }
        }

        if (!extensions.isEmpty()) {
            List<Database.SaveResult> results = Database.insert(extensions, false);
            for (Database.SaveResult sr : results) {
                if (sr.isSuccess()) {
                    totalCreated++;
                } else {
                    totalErrors++;
                    for (Database.Error err : sr.getErrors()) {
                        System.debug(
                            LoggingLevel.ERROR,
                            'BillingCaseServiceProcessExtensionBatch insert error: ' + err.getMessage()
                        );
                    }
                }
            }
        }
    }

    public void finish(Database.BatchableContext bc) {
        System.debug(
            LoggingLevel.INFO,
            'BillingCaseServiceProcessExtensionBatch complete. ' +
            'Cases processed: ' + totalProcessed +
            ', Extensions created: ' + totalCreated +
            ', Errors: ' + totalErrors
        );
    }

    private static String deriveServiceProcessFromProductName(String productName) {
        if (String.isBlank(productName)) {
            return 'Custom';
        }
        String lowerName = productName.toLowerCase();
        for (String keyword : PRODUCT_NAME_KEYWORD_TO_SERVICE_PROCESS.keySet()) {
            if (lowerName.contains(keyword)) {
                return PRODUCT_NAME_KEYWORD_TO_SERVICE_PROCESS.get(keyword);
            }
        }
        return 'Custom';
    }
}
```

=== ARTICLE: sforce_api_objects_creditinvoiceprocessedevent.htm ===
---
page_id: sforce_api_objects_creditinvoiceprocessedevent.htm
title: CreditInvoiceProcessedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditinvoiceprocessedevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_pfrm_evnt_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditInvoiceProcessedEvent

Represents the notification to the customers after the process
         initiated by the `/commerce/invoicing/invoices/{invoiceId}/actions/credit` request is
         complete. This object is available in API version 62.0 and later.

      

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

         
         

`/event/CreditInvoiceProcessedEvent`

      

      

## Event Delivery Allocation Enforced

         
         

No

      

      

## Special Access Rules

         
         

This object is available when Billing is enabled.

      

      

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
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| CrMemoProcessErrDtlEvents | **Type** [CrMemoProcessErrDtlEvent[]](./sforce_api_objects_crmemoprocesserrdtlevent.htm.md) **Properties** Nillable **Description** A compilation of error messages and error codes for a failed request. See the ErrorDetails field for error messages and error codes. |
| CreditMemoId | **Type** reference **Properties** Nillable **Description** The credit memo created as the result of a successful request. This field is a relationship field. **Relationship Name** CreditMemo **Refers To** CreditMemo |
| ErrorDetails | **Type** string **Properties** Nillable **Description** If the request fails, this field shows error messages, error codes, and the ID of the record on which the errors occurred. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| InvoiceId | **Type** reference **Properties** Nillable **Description** The invoice credited as the result of a successful request. This field is a relationship field. **Relationship Name** Invoice **Refers To** Invoice |
| IsSuccess | **Type** boolean **Properties** Defaulted on create **Description** Required. Indicates whether the request was successful (`true`) or not (`false`). The default value is `false`. |
| ReplayId | **Type** string **Properties** Nillable **Description** An ID value that’s populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** The unique ID returned in the response. Use this ID to identify the event for a specific request. |

      

      
   

- 
**[CrMemoProcessErrDtlEvent](./sforce_api_objects_crmemoprocesserrdtlevent.htm.md)**  

Represents the information about errors that occurred while creating          or applying a credit memo as part of a request. This object is included in a `CreditInvoiceProcessedEvent`, `CreditMemoProcessedEvent,` `NegInvcLineProcessedEvent`, or `VoidInvoiceProcessedEvent` platform event message. You can't subscribe             to `CrMemoProcessErrDtlEvent` platform event          directly. This object is available in API version 62.0 and later.

=== ARTICLE: sforce_api_objects_creditmemo.htm ===
---
page_id: sforce_api_objects_creditmemo.htm
title: CreditMemo
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemo

Represents a document that’s used to reduce the amount that a buyer
         owes a seller under the terms of an earlier invoice. This object is available in API
      version 62.0 and later.

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Credit Memo Operations User permission set to access this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

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

                  

               

            
| Field | Details |
| --- | --- |
| Balance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount of the credit memo that's available for allocation. |
| BillToContactId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** This field is inherited from the account’s Bill to Account field. This field is a relationship field. **Relationship Name** BillToContact **Refers To** Contact |
| BillingAccountId | **Type** reference **Properties** Filter, Group, Sort, Update **Description** Required. The ID of the customer account associated with this credit memo. This field is a relationship field. **Relationship Name** BillingAccount **Refers To** Account |
| Category | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the credit memo is created due to writing off an invoice, converting negative invoice lines, or referencing an existing record. Valid values are: `InvoiceWriteOff` `Referenced` `Standalone` This field is available in API version 64.0 and later. |
| CorpCrcyCnvTotAmtWithTax | **Type** double **Properties** Filter, Nillable, Sort **Description** The sum of the total amount with tax on the credit memo in corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date on which the credit memo amounts are converted to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort **Description** The exchange rate that's used to convert credit memo amounts to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The currency ISO code of the corporate currency. Available in API version 63.0 and later. |
| CreationMode | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the credit memo originated in Salesforce or an external system. Valid values are: `External` `Salesforce` |
| CreditDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when the credit memo was posted. |
| CreditMemoLockedDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time when the credit memo was locked. This field is available in API version 68.0 and later. |
| CreditMemoNumber | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The number of the credit memo. |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** Additional details about the credit memo. |
| DocumentNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the credit memo. |
| EffectiveDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The effective date of the credit memo. If this field is empty, the credit date is used. For reporting purposes only; this field drives no other logic. |
| ExternalReference | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** An external system’s ID for the credit memo. |
| ExternalReferenceDataSource | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The name of the external system that also contains the credit memo. |
| FuncCrcyCnvTotAmtWithTax | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total amount with tax value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the total amount with tax value is converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the total amount with tax value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| IsCreditMemoLocked | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. Indicates whether the credit memo is locked for editing (`true`) or not (`false`). This field is available in API version 68.0 and later. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a credit memo record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a credit memo record. If this value is null, it’s possible that the user only accessed the credit memo record or a related list view (LastReferencedDate), but not viewed the credit memo record itself. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period record that’s related to the credit memo. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity record that’s related to the credit memo. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| NetCreditsApplied | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total difference between the credit applied to and credit unapplied from the invoice. This field is a calculated field. |
| NetRefundsApplied | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total refund amount applied to the credit memo after subtracting the total unapplied refund amount. This field is available in API version 68.0 and later. This field is a calculated field. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort, Update **Description** Required. The ID of the user who owns a credit memo record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ReasonCode | **Type** picklist **Properties** Filter, Group, Nillable, Sort **Description** The reason code for the credit memo's category. For example, BD can be the reason code when the credit memo's category is `InvoiceWriteOff` and the reason for the invoice write-off is bad debt. This field is available in API version 64.0 and later. |
| ReferenceEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the record that this credit memo was generated from. For example, the order, order summary, or invoice. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntity **Refers To** Invoice, Order |
| SavedPaymentMethodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the Saved Payment Method record that’s used for the credit memo. This field is available in API version 68.0 and later. This field is a relationship field. **Relationship Name** SavedPaymentMethod **Refers To** SavedPaymentMethod |
| SettlementLevel | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the credit memo amount was applied to an invoice or an invoice line. |
| SourceAction | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies which Salesforce API created the credit memo. Valid values are: `Invoice` `NegativeInvoiceLineConversion` `Standalone` `VoidPostedInvoice` `WriteOffPostedInvoice`—Available in API version 64.0 and later. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the credit memo. Valid values are: `Canceled` `Draft` `Error` `Pending` `Posted` `Void In Progress`—Available in API version 64.0 and later. `Voided` |
| TotalAdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the TotalAmount field values for the credit memo’s adjustment lines. This field is a calculated field. |
| TotalAdjustmentAmountWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the credit memo’s adjustment line amounts, including tax. Available in API versions 62.0 and 63.0. |
| TotalAdjustmentTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the credit memo’s adjustment line tax. Adjustment line balances are excluded. Available in API versions 62.0 and 63.0. |
| TotalAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the credit memo’s TotalLineAmount and TotalAdjustmentAmount field values. This field is a calculated field. |
| TotalAmountWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total credit memo amount, with tax included. This field is a calculated field. |
| TotalChargeAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the TotalAmount field values for the credit memo’s charge lines. This field is a calculated field. |
| TotalChargeAmountWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the credit memo’s charge line amounts, including tax. Available in API versions 62.0 and 63.0. |
| TotalChargeTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the credit memo’s charge tax amount. Available in API versions 62.0 and 63.0. |
| TotalTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the TotalAmount field values for the credit memo’s tax lines. This field is a calculated field. |
| TotalTaxesCapturedAtHeader | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The total tax calculated at the transaction header level. Available in API version 66.0 and later. |

=== ARTICLE: sforce_api_objects_creditmemoaddressgroup.htm ===
---
page_id: sforce_api_objects_creditmemoaddressgroup.htm
title: CreditMemoAddressGroup
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoAddressGroup

Represents the storage of the buyer's address information, which is
         used to determine the tax credit amount for a buyer when a credit memo is issued. This
      object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `delete()`, 
         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`, 
         `undelete()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Credit Memo Operations User permission set to access this object.

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| Address | **Type** address **Properties** Filter, Nillable **Description** The buyer's address. |
| CreditMemoAddressGroupNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated reference number for the credit memo address group. |
| CreditMemoId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the credit memo associated with the address group. This field is a relationship field. **Relationship Name** CreditMemo **Relationship Type** Master-detail **Refers To** CreditMemo (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a credit memo address group record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a credit memo address group record. If this value is null, it’s possible that the user only accessed the credit memo address group record or a related list view (LastReferencedDate), but not viewed the credit memo address group record itself. |

=== ARTICLE: sforce_api_objects_creditmemoinvapplication.htm ===
---
page_id: sforce_api_objects_creditmemoinvapplication.htm
title: CreditMemoInvApplication
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoInvApplication

Represents information about the application of a credit memo to an
         invoice. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Credit Memo Operations User permission set to access this object.

      

      

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
- 
- 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| Amount | **Type** currency **Properties** Filter, Sort **Description** Required. The amount of the credit memo that was applied to or unapplied from the invoice. |
| AppliedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the credit memo was applied. If the credit memo invoice application's type is `Unapplied`, this value is inherited from the `Applied` date of the credit memo referenced in the AssociatedLineId field. |
| AssociatedLineId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** ID of the original credit memo invoice application for a credit memo invoice application that represents an unapplied credit memo. This field is a relationship field. **Relationship Name** AssociatedLine **Refers To** CreditMemoInvApplication |
| CreditMemoBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The balance of a credit memo after it's applied or unapplied. This field is a snapshot of the credit memo's balance after the action. This field isn't updated after further changes to the credit memo balance. |
| CreditMemoId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The credit memo that was applied or unapplied. This field is a relationship field. **Relationship Name** CreditMemo **Refers To** CreditMemo |
| CreditMemoInvoiceNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number identifying the credit memo invoice application. |
| Date | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the credit memo amount was applied to the invoice. |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** Additional details about the credit memo applied to an invoice. |
| EffectiveDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The effective date of the application or unapplication of credit. You can provide this value when applying or unapplying the credit memo. This field is optional and provided only for reporting purposes. It doesn't affect the credit memo invoice application's other fields. |
| HasBeenUnapplied | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether this credit memo application has been unapplied from the target invoice. Valid values are: `NA` `No` `Yes` |
| ImpactAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The net adjustment to the invoice's balance after a credit memo is applied or unapplied. If a credit memo was applied, this value is the negative version of the credit memo invoice application's Amount field. If a credit memo was unapplied, this value is the positive version of the credit memo invoice application's Amount field. This field is a calculated field. |
| InvoiceBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The balance of the credit memo after a credit memo is applied or unapplied. This field is a snapshot of the credit memo's balance after the action. This field isn't updated after further changes to the credit memo balance. |
| InvoiceId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The invoice to which the credit memo is applied. This field is a relationship field. **Relationship Name** Invoice **Relationship Type** Master-detail **Refers To** Invoice (the master object) |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period record that’s related to the credit memo invoice application. This field is available in API version 67.0 and later. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity record that’s related to the credit memo invoice application. This field is available in API version 67.0 and later. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Type | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. Specifies whether the credit memo line application was generated because of an apply action (application) or an unapply action (unapplication). Valid values are: `Applied` `Unapplied` |
| UnappliedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when this application was unapplied from the target invoice. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CreditMemoInvApplicationFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[CreditMemoInvApplicationHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_creditmemoline.htm ===
---
page_id: sforce_api_objects_creditmemoline.htm
title: CreditMemoLine
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoLine

Represents the product, service, adjustment, or tax line items
         included in a credit memo. This object is available in API version 62.0 and
      later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `search()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Credit Memo Operations User permission set to access this object.

      

      

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| AdjustmentAmount | **Type** currency **Properties** Filter, Nillable, Sort, Update **Description** The amount of this credit memo line item if its type is Adjustment. |
| AdjustmentAmountWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the adjustment amount and the adjustment tax amount. Available in API versions 62.0 and 63.0. |
| AdjustmentTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount of the tax related to the adjustment amount. Available in API versions 62.0 and 63.0. |
| Balance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount of the credit memo line available for allocation. |
| BillingAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the billing address related to this credit memo line. This field is a relationship field. **Relationship Name** BillingAddress **Refers To** CreditMemoAddressGroup |
| ChargeAmount | **Type** currency **Properties** Filter, Nillable, Sort, Update **Description** The amount of this credit memo line item if its type is Charge. |
| ChargeAmountWithTax | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the charge amount and the charge tax amount. Available in API versions 62.0 and 63.0. |
| ChargeTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount of the tax related to the charge amount. Available in API versions 62.0 and 63.0. |
| CorpCurrencyCnvChargeAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The amount of the credit memo line item if its type is `Charge` in corporate currency. Available in API version 63.0 and later. |
| CorpCurrencyCnvTotalTaxAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The sum of the total amount with the tax on the credit memo line in corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the credit memo line amounts are converted to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the credit memo line amounts to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. Available in API version 63.0 and later. |
| CreditMemoId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the parent credit memo. This field is a relationship field. **Relationship Name** CreditMemo **Relationship Type** Master-detail **Refers To** CreditMemo (the master object) |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** Additional details about the credit memo line. |
| EndDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The description of the credit memo line. |
| FuncCrcyCnvTotalTaxAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total tax amount value in functional currency. Available in API version 66.0 and later. |
| FuncCurrencyCnvChargeAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The charge amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the credit memo line amounts are converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert credit memo line amounts into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity accounting period record of the credit memo line. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity record related to the credit memo line. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| LineAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The amount of the credit memo line. This field is a calculated field. |
| Name | **Type** string **Properties** Filter, Group, idLookup, Sort, Update **Description** Required. The name of the credit memo line. |
| NetCreditsApplied | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount applied to invoice lines from the credit memo. This amount is calculated by subtracting the total unapplied credit amount from the total applied credit amount. This field is a calculated field. |
| Product2Id | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the product or service being credited in the credit memo line. This field is a relationship field. **Relationship Name** Product2 **Refers To** Product2 |
| ReferenceEntityItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The order product or invoice line corresponding to this credit memo line. This field is a polymorphic relationship field. **Relationship Name** ReferenceEntityItem **Refers To** InvoiceLine, OrderItem |
| ReferenceEntityItemType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of transaction that generated the credit memo line. Valid values are: `Delivery Charge` `Fee` `Order Product` |
| ReferenceEntityItemTypeCode | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of object that generated the credit memo line. Valid values are: `Charge` `Product` |
| ShipFromAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The address from which the product in the credit memo line is shipped. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** ShipFromAddress **Refers To** CreditMemoAddressGroup |
| ShippingAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the shipping address. This field is a relationship field. **Relationship Name** ShippingAddress **Refers To** CreditMemoAddressGroup |
| StartDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The first date of the billing for the service for credit memo lines generated from a time-based service. |
| Status | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The status of the credit memo line. This field is inherited from the credit memo. |
| TaxAmount | **Type** currency **Properties** Filter, Nillable, Sort, Update **Description** The total tax amount for the credit memo. |
| TaxTreatmentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the tax treatment record for the credit memo line. This field is a relationship field. **Relationship Name** TaxTreatment **Refers To** TaxTreatment |

=== ARTICLE: sforce_api_objects_creditmemolineinvoiceline.htm ===
---
page_id: sforce_api_objects_creditmemolineinvoiceline.htm
title: CreditMemoLineInvoiceLine
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemolineinvoiceline.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoLineInvoiceLine

Represents a junction between a credit memo line and an invoice
         line. This object is available in API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Credit Memo Operations User permission set to access this object.

      

      

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
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| Amount | **Type** currency **Properties** Filter, Sort **Description** Required. The amount that's been applied to or unapplied from the invoice line. |
| AppliedDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time when the credit memo line was applied to the invoice line. |
| CreditMemoLineBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The balance of the credit memo line after it's applied to or unapplied from the invoice line. |
| CreditMemoLineId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the credit memo line record that's applied to or unapplied from the invoice line. This field is a relationship field. **Relationship Name** CreditMemoLine **Refers To** CreditMemoLine |
| CreditMemoLineInvoiceLineNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number identifying the credit memo line invoice line. |
| Description | **Type** textarea **Properties** Filter, Group, Nillable, Sort, Update **Description** Additional details about the credit memo line invoice line. |
| EffectiveDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time when the credit memo line's application to or unapplication from the invoice line becomes effective. |
| ImpactAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The credit memo line invoice line’s financial impact against the customer’s accounts receivable. If the credit memo line invoice line's type is `Applied`, the impact amount is the negative equivalent of the credit memo line invoice line's amount. Otherwise, the impact amount is equal to the credit memo line invoice line's amount. This field is a calculated field. |
| InvoiceLineBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The balance of the invoice line after the credit memo line was applied or unapplied. |
| InvoiceLineId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the invoice line record to which the credit memo line has been applied or unapplied. This field is a relationship field. **Relationship Name** InvoiceLine **Relationship Type** Master-detail **Refers To** InvoiceLine (the master object) |
| InvoiceLineTaxId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The invoice line tax record to which the credit memo line was applied or unapplied. This field is available in API version 68.0 and later. This field is a relationship field. **Relationship Name** InvoiceLineTax **Refers To** InvoiceLineTax |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity accounting period record related to the credit memo line invoice line. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity record related to the credit memo line invoice line. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| RelatedCrMemoLineInvcLineId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the related credit memo line invoice line record of the type `Applied` when the credit memo line invoice line's type is `Unapplied`. This field is a relationship field. **Relationship Name** RelatedCrMemoLineInvcLine **Refers To** CreditMemoLineInvoiceLine |
| SettlementType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the type of amount settled by the credit memo line that’s applied to the invoice line. This field is available in API version 68.0 and later. Valid values are: `Balance` `Charge` `Tax` |
| Type | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. Specifies whether the credit memo line has been applied to or unapplied from the invoice line. Valid values are: `Applied` `Unapplied` |
| UnappliedDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date and time when the credit memo line was unapplied from the invoice line. |
| UnappliedStatus | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. Specifies whether the credit memo line has been unapplied from the invoice line. Valid values are: `NA` `No` `Yes` |

=== ARTICLE: sforce_api_objects_creditmemolinetax.htm ===
---
page_id: sforce_api_objects_creditmemolinetax.htm
title: CreditMemoLineTax
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemolinetax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoLineTax

Represents tax information of a credit memo line of type `Tax`. This object is available in API version 62.0 and
      later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`

      

      

## Special Access Rules

         
         

You need the Tax Admin permission set to access this object.

      

      

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

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

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
| BillingAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing address of the parent credit memo line. This field is a relationship field. **Relationship Name** BillingAddress **Refers To** CreditMemoAddressGroup |
| CalculationStatus | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of the tax calculation. Valid values are: `Complete` `Error` `None` The default value is `None`. |
| CorpCrcyCnvTaxAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total tax amount of the credit memo line tax in corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the credit memo line tax amounts are converted to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the credit memo line tax amounts to the corporate currency. Available in API version 63.0 and later. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. Available in API version 63.0 and later. |
| CreditMemoLineId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the parent charge or adjustment credit memo line record that a credit memo line tax is related to. This field is a relationship field. **Relationship Name** CreditMemoLine **Relationship Type** Master-detail **Refers To** CreditMemoLine (the master object) |
| CreditMemoLineTaxNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number identifying a credit memo line tax. |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** Additional details about the credit memo line tax. |
| EndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The end date of a credit memo line tax. |
| FuncCrcyCnvTaxAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The tax amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the tax amount value is converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the tax amount value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the legal entity accounting period record that's related to a credit memo line tax. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The ID of the legal entity record that's related to a credit memo line tax. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Product2Id | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The product or service being credited in the parent credit memo line. Available in API version 62.0 only. This field is a relationship field. **Relationship Name** Product2 **Refers To** Product2 |
| ReferenceEntityItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The invoice line tax corresponding to a credit memo line tax. This field is a relationship field. **Relationship Name** ReferenceEntityItem **Refers To** InvoiceLineTax |
| ShipFromAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ship from address specified in the parent credit memo line. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** ShipFromAddress **Refers To** CreditMemoAddressGroup |
| ShippingAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The shipping address of the parent credit memo line. This field is a relationship field. **Relationship Name** ShippingAddress **Refers To** CreditMemoAddressGroup |
| StartDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The start date of a credit memo line tax. |
| TaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of a credit memo line tax. |
| TaxCode | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The code that's used to calculate the tax rate for the parent credit memo line. |
| TaxDocumentNumber | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The document number that's used to calculate the tax rate for the parent credit memo line. |
| TaxEffectiveDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date used to calculate the tax amount. |
| TaxName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The user-defined name for a credit memo line tax. |
| TaxRate | **Type** percent **Properties** Filter, Nillable, Sort **Description** The percentage that's used to calculate tax. |
| TaxTransactionNumber | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The number of the transaction in the external tax engine that calculated tax for the parent credit memo line. |
| TaxTreatmentId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the tax treatment record that's related to a credit memo line tax. This field is a relationship field. **Relationship Name** TaxTreatment **Refers To** TaxTreatment |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CreditMemoLineTaxFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[CreditMemoLineTaxHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_creditmemoprocessedevent.htm ===
---
page_id: sforce_api_objects_creditmemoprocessedevent.htm
title: CreditMemoProcessedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoprocessedevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_pfrm_evnt_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditMemoProcessedEvent

      Represents the notification to the customers after the process initiated by
         the `/commerce/invoicing/credit-memos` request is
         complete. This object is available in API version 62.0 and later.

      

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

         
         

`/event/CreditMemoProcessedEvent`

      

      

## Event Delivery Allocation Enforced

         
         

No

      

      

## Special Access Rules

         
         

This object is available when Billing is enabled.

      

      

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
| CorrelationIdentifier | **Type** string **Properties** Nillable **Description** Reserved for future use. |
| CrMemoProcessErrDtlEvents | **Type** [CrMemoProcessErrDtlEvent[]](./sforce_api_objects_crmemoprocesserrdtlevent.htm.md) **Properties** Nillable **Description** A compilation of error messages and error codes for a failed request. See the ErrorDetails field for error messages and error codes. |
| CreditMemoId | **Type** reference **Properties** Nillable **Description** The credit memo created as the result of a successful request. This field is a relationship field. **Relationship Name** CreditMemo **Refers To** CreditMemo |
| ErrorDetails | **Type** string **Properties** Nillable **Description** If the request fails, this field shows error messages, error codes, and the ID of the record on which the errors occurred. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |
| IsSuccess | **Type** boolean **Properties** Defaulted on create **Description** Required. Indicates whether the request was successful (`true`) or not (`false`). The default value is `false`. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that’s populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| RequestIdentifier | **Type** string **Properties** Nillable **Description** The unique ID returned in the response. Use this ID to identify the event for a specific request. |

=== ARTICLE: sforce_api_objects_crmemoprocesserrdtlevent.htm ===
---
page_id: sforce_api_objects_crmemoprocesserrdtlevent.htm
title: CrMemoProcessErrDtlEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_crmemoprocesserrdtlevent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: sforce_api_objects_creditinvoiceprocessedevent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CrMemoProcessErrDtlEvent

Represents the information about errors that occurred while creating
         or applying a credit memo as part of a request. This object is included in a `CreditInvoiceProcessedEvent`, `CreditMemoProcessedEvent,` `NegInvcLineProcessedEvent`, or `VoidInvoiceProcessedEvent` platform event message. You can't subscribe
            to `CrMemoProcessErrDtlEvent` platform event
         directly. This object is available in API version 62.0 and later.

      

## Supported Calls

         
         

            `describeSObjects()`
         

      

      

## Special Access Rules

         
         

This object is available when Billing is enabled.

      

      

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
| ErrorCode | **Type** string **Properties** Nillable **Description** Reference code for the type of error that occurred. |
| ErrorMessage | **Type** string **Properties** Nillable **Description** Information about the error that occurred during processing. |
| ErrorSourceId | **Type** reference **Properties** Nillable **Description** The ID of the record on which the error occurred during the credit memo creation process and the application process. This field is a polymorphic relationship field. **Relationship Name** ErrorSource **Refers To** CreditMemo, CreditMemoLine, Invoice, InvoiceLine |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. |

=== ARTICLE: sforce_api_objects_debitmemo.htm ===
---
page_id: sforce_api_objects_debitmemo.htm
title: DebitMemo
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_debitmemo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DebitMemo

      Represents the document used to charge an additional amount to a buyer by a
         seller. An invoice is generated for the debit memo in the next invoice run. This
      object is available in API version 65.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and one of these permission sets to access this
            object.

         
            
- Billing Admin permission set

            
- Billing Operations User permission set

            
- Payments Admin permission set

            
- Payments Operation User permission set

            
- Credit Memo Operations User permission set

         

      

      

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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The account that’s related to the debit memo record. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| CorpCrcyCnvTotChargeAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total charge amount of the debit memo in corporate currency. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The exchange date that’s used to convert the debit memo amounts into corporate currency. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that’s used to convert the debit memo amounts into corporate currency. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the debit memo. |
| DocumentNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** An autogenerated number assigned to the debit memo record. |
| FuncCrcyCnvTotChargeAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total charge amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The exchange date that’s used to convert the total charge amount value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that’s used to convert the total charge amount value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| InvoiceGenerationStatus | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of invoice generation for the debit memo. Valid values are: `Draft Invoice Generated` `None` `Posted Invoice Generated` `Processing` `Ready for Invoice Generation` `Not Applicable`—Available in API version 66.0 and later. |
| InvoiceMatchingRefKeyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Indicates the product or Asset ID. This key, combined with the account, currency, and legal entity, is used to find a matching invoice. The invoice lines converted from debit memo lines are then added to this matched invoice. This field is a polymorphic relationship field. **Relationship Name** InvoiceMatchingRefKey **Refers To** Asset, Product2 |
| InvoiceMatchingRefName | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Indicates the product's name. This text, combined with the account, currency, and legal entity, is used to find a matching invoice. The invoice lines converted from debit memo lines are then added to this matched invoice. |
| IsManuallyProcessed | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the debit memo lines of the debit memo are converted to invoice lines manually (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a debit memo address group record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a debit memo address record. If this value is null, it’s possible that the user only accessed the debit memo address record or a related list view (LastReferencedDate), but not viewed the debit memo address record itself. |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity record that's related to the debit memo. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| NextBillingDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date indicates when the next billing period begins for the debit memo. This date is used to determine when invoices are created for the debit memos. When the invoice scheduler or API evaluates debit memos to generate invoices, those with a next billing date on or before the user-specified target date are included in the invoice batch run. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of this object. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PostedDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when the debit memo is posted. |
| ReasonCode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies a dynamic picklist of reasons for generating debit memos. |
| ReferenceRecord | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record ID associated with the debit memo record. The record ID is a credit memo record. Available in API version 66.0 and later. This field is a polymorphic relationship field. **Relationship Name** InvoiceMatchingRefKey **Refers To** Credit Memo |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the debit memo. Valid values are: `Canceled` `Draft` `Posted` `Void` `Pending`—Available in API version 66.0 and later. `Error`—Available in API version 66.0 and later. |
| TotalAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the debit memo’s TotalLineAmount and TotalAdjustmentAmount field values. Available in API version 66.0 and later. This field is a calculated field. |
| TotalChargeAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the charge amount field values of the debit memo lines. This field is a calculated field. |
| TotalTaxAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of the TotalAmount field values for the debit memo’s tax lines. Available in API version 66.0 and later. This field is a calculated field. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[DebitMemoFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[DebitMemoHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[DebitMemoOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[DebitMemoShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_debitmemoaddress.htm ===
---
page_id: sforce_api_objects_debitmemoaddress.htm
title: DebitMemoAddress
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_debitmemoaddress.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DebitMemoAddress

Represents the buyer's address information, which is used to
         determine the tax amount for a buyer when a debit memo is issued. This object is
      available in API version 65.0 and later.

      

         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and one of these permission sets to access this
            object.

         
            
- Billing Admin permission set

            
- Billing Operations User permission set

            
- Payments Admin permission set

            
- Payments Operation User permission set

            
- Credit Memo Operations User permission set

         

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| Address | **Type** address **Properties** Filter **Description** The billing or shipping address of the debit memo. |
| DebitMemoAddressNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated reference number for the debit memo address. |
| DebitMemoId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the debit memo associated with the address. This field is a relationship field. **Relationship Name** DebitMemo **Relationship Type** Master-detail **Refers To** DebitMemo (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a debit memo address record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a debit memo address record. If this value is null, it’s possible that the user only accessed the debit memo address record or a related list view (LastReferencedDate), but not viewed the debit memo address record itself. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[DebitMemoAddressHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_debitmemoline.htm ===
---
page_id: sforce_api_objects_debitmemoline.htm
title: DebitMemoLine
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_debitmemoline.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DebitMemoLine

Represents the additional charge amount that the buyer must pay for
         the product, service, or debit memo line tax that’s related to the debit memo. This
      object is available in API version 65.0 and later.

      

         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `describeLayout()`, `describeSObjects()`,
               `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and one of these permission sets to access this
            object.

         
            
- Billing Admin permission set

            
- Billing Operations User permission set

            
- Payments Admin permission set

            
- Payments Operation User permission set

            
- Credit Memo Operations User permission set

         

      

      

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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

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
| BillingAddressId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The billing address record that’s related to the debit memo line. This field is a relationship field. **Relationship Name** BillingAddress **Refers To** DebitMemoAddress |
| ChargeAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The amount of the debit memo line item. |
| CorpCurrencyCnvChargeAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The charge amount of the debit memo line in corporate currency. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the debit memo line amounts are converted into corporate currency. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that’s used to convert debit memo line amounts into corporate currency. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. |
| DebitMemoId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The parent debit memo record that’s related to the debit memo line record. This field is a relationship field. **Relationship Name** DebitMemo **Relationship Type** Master-detail **Refers To** DebitMemo (the master object) |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The description of the debit memo line. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The end date of the debit memo line that determines which billing cycle it must be associated with. |
| FuncCrcyCnvTotalTaxAmt | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The total tax amount value in functional currency. Available in API version 66.0 and later. |
| FuncCrcyCnvChargeAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The charge amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the debit memo line amounts is converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the debit memo line amounts into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a debit memo address record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a debit memo address record. If this value is null, it’s possible that the user only accessed the debit memo address record or a related list view (LastReferencedDate), but not viewed the debit memo address record itself. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period record that’s related to the debit memo line. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity record that’s related to the debit memo line. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** An auto-generated name assigned to the debit memo line. |
| Product2Id | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the product or service being debited in the debit memo line. This field is a relationship field. **Relationship Name** Product2 **Refers To** Product2 |
| ReferenceRecordId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record ID associated with the debit memo line record. The record ID is an asset, invoice line, contract, or refund record. This field is a polymorphic relationship field. **Relationship Name** ReferenceRecord **Refers To** Asset, Contract, InvoiceLine, Refund, Credit Memo Line |
| ShippingAddressId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The shipping address record that’s related to the debit memo line. This field is a relationship field. **Relationship Name** ShippingAddress **Refers To** DebitMemoAddress |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The start date of the debit memo line that determines which billing cycle it must be associated with. |
| TaxTreatmentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the tax treatment record that’s related to the debit memo line. This field is a relationship field. **Relationship Name** TaxTreatment **Refers To** TaxTreatment |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[DebitMemoLineFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[DebitMemoLineHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_debitmemolinetax.htm ===
---
page_id: sforce_api_objects_debitmemolinetax.htm
title: DebitMemoLineTax
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_debitmemolinetax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DebitMemoLineTax

Represents the tax information for a debit memo line. This
      object is available in API version 66.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and the Tax Admin permission set to access this
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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

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
| BillingAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The billing address specified in the parent debit memo line. This field is a relationship field. **Relationship Name** BillingAddress **Refers To** DebitMemoAddress |
| CurrencyIsoCode | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Required. The currency ISO code of the corporate currency. |
| DebitMemoLineId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The parent debit memo line that the debit memo tax line is related to. This field is a relationship field. **Relationship Name** DebitMemoLine **Relationship Type** Master-detail **Refers To** DebitMemoLine (the master object) |
| DebitMemoLineTaxNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. An auto-generated number that identifies a debit memo line tax. |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The description of the debit memo line tax. |
| EndDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The end date of the debit memo line tax that determines which billing cycle it's associated with. |
| JurisdictionTaxCode | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The code of the jurisdiction that's used to calculate the tax rate for the parent debit memo line. |
| JurisdictionTaxName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The user-defined name for the debit memo line tax. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a debit memo line tax record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a debit memo line tax record. If this value is null, it’s possible that the user only accessed the debit memo line tax record or a related list view (LastReferencedDate), but not viewed the debit memo line tax record itself. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The legal entity accounting period record associated with the debit memo line. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The legal entity record associated with the debit memo line. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| ShipFromAddressId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The shipping address specified in the parent debit memo line. This field is a relationship field. **Relationship Name** ShipFromAddress **Refers To** DebitMemoAddress |
| StartDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The start date of the debit memo line tax that determines which billing cycle it's associated with. |
| TaxAmount | **Type** currency **Properties** Filter, Sort **Description** Required. The total amount of the debit memo line tax. |
| TaxRate | **Type** percent **Properties** Filter, Nillable, Sort **Description** The percentage that's used to calculate tax amount based on the charge amount. |
| TaxTransactionNumber | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The transaction number in the external tax engine that calculated the tax for the parent debit memo line. |

=== ARTICLE: sforce_api_objects_generalldgracctprdsummary.htm ===
---
page_id: sforce_api_objects_generalldgracctprdsummary.htm
title: GeneralLdgrAcctPrdSummary
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_generalldgracctprdsummary.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GeneralLdgrAcctPrdSummary

Represents a junction between a general ledger account and a legal
         entity accounting period. Stores information about the total credit amount, total debit
         amount, opening balance, and closing balance of a general ledger account for a specific
         legal entity accounting period. This object is available in API version 65.0 and
      later.

      

         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and the Accounts Receivables Admin permission set
            to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| ClosingBalanceAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The closing balance amount for a general ledger accounting period summary is calculated based on the general ledger account's type. For asset and expense type general ledger accounts, it’s the opening balance amount plus total debit amount minus total credit amount. For liability, equity, and revenue type general ledger accounts, it’s the opening balance amount plus total credit amount minus total debit amount. |
| GeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The general ledger account that’s related to the general ledger accounting period summary. This field is a relationship field. **Relationship Name** GeneralLedgerAccount **Relationship Type** Master-detail **Refers To** GeneralLedgerAccount (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed general ledger accounting period summary record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed general ledger accounting period summary record or list view. If this value is null, and LastReferenceDate is not null, the user accessed this record or list view indirectly. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The legal entity accounting period that’s related to the general ledger account. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| OpeningBalanceAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The opening balance is the same as the closing balance of the previous general ledger account period summary. |
| TotalCreditAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The sum of the credit fields from all transaction journals of the general ledger account for a specific legal entity accounting period. |
| TotalDebitAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The sum of the debit fields from all transaction journals of the general ledger account for a specific legal entity accounting period. |

=== ARTICLE: sforce_api_objects_generalledgeraccount.htm ===
---
page_id: sforce_api_objects_generalledgeraccount.htm
title: GeneralLedgerAccount
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_generalledgeraccount.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GeneralLedgerAccount

Represents information about the accounting codes, types, and names that are used
         to store and organize financial transactions. This object is available in API version
      63.0 and later.

      

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

         
         

You need Revenue Cloud Billing license and the Accounts Receivables Admin permission set
            to access this object.

      

      

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
- 
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| AccountingCode | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The code that's used to organize information about the general ledger account. |
| AccountingName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The user-specified name for the general ledger account. |
| AccountingType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The accounting type for the general ledger account. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Additional details about the general ledger account. |
| FinancialStatement | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The financial statement that's created by using the information from the general ledger account. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferenceDate is not null, the user accessed this record or list view indirectly. |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity that's related to the general ledger account. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Filter, Group, idLookup, Sort **Description** An auto-generated name identifying the general ledger account, which is a combination of the accounting code and the account name. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of this object or ID of the creator of this object. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Type | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the accounting type for the general ledger account. This field is available in API version 65.0 and later. Valid values are: `Asset` `Liability` `Equity` `Revenue` `Expense` `Others` |

=== ARTICLE: sforce_api_objects_generalledgeracctasgntrule.htm ===
---
page_id: sforce_api_objects_generalledgeracctasgntrule.htm
title: GeneralLedgerAcctAsgntRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_generalledgeracctasgntrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GeneralLedgerAcctAsgntRule

Represents information about the rule based on which general ledger accounts are
         assigned to transaction journals that are created for billing transactions. This
      object is available in API version 63.0 and later.

      

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

         
         

You need Revenue Cloud Billing license and the Accounts Receivables Admin permission set
            to access this object.

      

      

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

                  

                  
                     

                     

: 

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

                  

               

            
| Field | Details |
| --- | --- |
| CreditGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The general ledger account for a credit transaction that's related to the general ledger account assignment rule. This field is a relationship field. **Relationship Name** CreditGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The currency code of the general ledger account assignment rule for Salesforce orgs with multicurrency enabled. Valid values are: `AUD`—Australian Dollar `EUR`—Euro `SGD`—Singapore Dollar `USD`—U.S. Dollar The default value is `USD`. |
| DebitGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The general ledger account for a debit transaction that's related to the general ledger account assignment rule. This field is a relationship field. **Relationship Name** DebitGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| FilterCriteria | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The filter criteria for the general ledger account assignment rule. Valid values are: `All` `Any` `Custom` |
| FilterLogic | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The filter logic for the general ledger account assignment rule when the filter criteria is `Custom`. Transaction journals are created for the transactions of the selected type that meet the defined filter logic. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferenceDate is not null, the user accessed this record or list view indirectly. |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity that's related to the general ledger account assignment rule. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** A user-defined name for the general ledger account assignment rule. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the general ledger account assignment rule record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| Priority | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The priority of the general ledger account assignment rule when there are multiple general ledger account assignment rules defined for a transaction type. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The status of the general ledger account assignment rule. Valid values are: `Active` `Inactive` |
| TransactionAmountField | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The amount field on the transaction type that's used to record the credit or debit amount in the transaction journals that are generated for that specific transaction type. This field is available in API version 64.0 and later. |
| TransactionType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** The transaction type that's related to the general ledger account assignment rule. Valid values are: `CreditMemo` `CreditMemoInvApplication` `CreditMemoLine` `CreditMemoLineInvoiceLine` `CreditMemoLineTax` `DebitMemoLine`—Available in API version 65.0 and later. `Invoice` `InvoiceLine` `InvoiceLineTax` `Payment`—Available in API version 64.0 and later. `PaymentLineInvoice`—Available in API version 64.0 and later. `PaymentLineInvoiceLine`—Available in API version 64.0 and later. `Refund`—Available in API version 64.0 and later. `RefundLinePayment`—Available in API version 64.0 and later. |

=== ARTICLE: sforce_api_objects_generalledgerjrnlentryrule.htm ===
---
page_id: sforce_api_objects_generalledgerjrnlentryrule.htm
title: GeneralLedgerJrnlEntryRule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_generalledgerjrnlentryrule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# GeneralLedgerJrnlEntryRule

      Represents information about the transaction journal entry rule, based on
         which transaction journals are created for the selected credit and debit general ledger
         accounts, transaction amount field, and percentage. This object is available in API
      version 65.0 and later.

      

         

#### Important

Where possible, we changed noninclusive terms
            to align with our company value of Equality. We maintained certain terms to avoid any
            effect on customer implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need Revenue Cloud Billing license and the Accounts Receivables Admin permission set
            to access this object.

      

      

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
| CreditGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The general ledger account for a credit transaction. This field is a relationship field. **Relationship Name** CreditGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| DebitGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The general ledger account for a debit transaction. This field is a relationship field. **Relationship Name** DebitGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| GeneralLedgerAcctAsgntRuleId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The general ledger account assignment rule that’s related to the general ledger journal entry rule. This field is a relationship field. **Relationship Name** GeneralLedgerAcctAsgntRule **Relationship Type** Master-detail **Refers To** GeneralLedgerAcctAsgntRule (the master object) |
| Percentage | **Type** percent **Properties** Create, Filter, Sort, Update **Description** The percentage of the amount field value that’s used to record the credit or debit amount in the transaction journals generated for the general ledger journal entry rule. |
| TransactionAmountField | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The amount field on the transaction type that’s used to record the credit or debit amount in the transaction journals generated for that specific transaction type. |

=== ARTICLE: sforce_api_objects_invbatchdrafttopostedrun.htm ===
---
page_id: sforce_api_objects_invbatchdrafttopostedrun.htm
title: InvBatchDraftToPostedRun
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invbatchdrafttopostedrun.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_std_objects_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# InvBatchDraftToPostedRun

Represents information about the batch job that posts all invoices
         with the status as `Draft` that are generated by the
         invoice batch run associated with the billing schedule. This object is available in
      API version 62.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`, 
         `update()`
      

      

      

## Special Access Rules

         
         

You need the Billing Operations User permission set to access this object.

      

      

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

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

            

            
| Field | Details |
| --- | --- |
| BatchJobId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The batch management job that's used to track the progress of the invoice batch run. This field is a relationship field. **Relationship Name** BatchJob **Refers To** BatchJob |
| Comments | **Type** textarea **Properties** Filter, Nillable, Sort, Update **Description** Additional notes or comments for the invoice batch draft to posted run record. |
| CompletionDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The completion date and time of this invoice batch draft to posted run process. |
| CreditApplicationStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of a credit application to the invoices that are posted by the invoice batch draft to posted run process. Valid values are: `Completed` `Failed` `NotApplicable` |
| InvBatchDraftToPostedRunNumber | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The auto-generated number of the invoice batch draft to posted run record. |
| InvoiceBatchRunId | **Type** reference **Properties** Filter, Group, Sort **Description** Required. The ID of the invoice batch run record associated with the invoice batch draft to posted run record. This field is a relationship field. **Relationship Name** InvoiceBatchRun **Relationship Type** Master-detail **Refers To** InvoiceBatchRun (the master object) |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed an invoice batch draft to posted run record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed an invoice batch draft to posted run record. If this value is null, it’s possible that the user only accessed the invoice batch draft to posted run record or a related list view (LastReferencedDate), but not viewed the invoice batch draft to posted run record itself. |
| StartDateTime | **Type** dateTime **Properties** Filter, Sort **Description** Required. The start date and time of the invoice batch draft to posted run process. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Required. The status of the invoice batch draft to posted run record. Valid values are: `Completed` `CompletedWithErrors` `Failed` `Started` The default value is `Started`. |
| TotalDraftInvoicesSelected | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The total number of invoices that are selected to be processed by the invoice batch draft to posted run process. |
| TotalInvoiceAmount | **Type** currency **Properties** Filter, Nillable, Sort **Description** The total amount of all the invoices posted by the invoice batch draft to posted run process. |
| TotalInvoicesFailed | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The total number of invoices that the invoice batch draft to posted run process failed to post. |
| TotalPostedInvoices | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The total number of invoices posted by the invoice batch draft to posted run process. |

