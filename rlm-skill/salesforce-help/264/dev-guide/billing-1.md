# Revenue Management Developer Guide 264 — sección: Billing (parte 1/3) (163 artículos)

=== ARTICLE: actions_obj_apply_rules.htm ===
---
page_id: actions_obj_apply_rules.htm
title: Apply Payments and Credits by Rules Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_apply_rules.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apply Payments and Credits by Rules Action

Apply payments and credits to posted invoices by adhering to the specified
        rules.

        

This action uses predefined logic to allocate payments and credits, reducing any
                manual intervention and errors.

This action is available in API version 66.0
                and later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/applyPaymentsAndCreditsByRules`

                
                
                    

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
| accountId | **Type** reference **Description** Required. The ID of the account to perform the settlement of payments and credits against invoices in adherence with the applied rules. |
| targetDate | **Type** date **Description** Optional. The date used to select invoices and invoice lines with a posted date equal to or later than the target date to apply payments and credits. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| rulesApplicationResponse | **Type** Apex-defined **Description** The Apex [RulesApplicationResponse](./apex_class_RulesAppln_RulesApplicationResponse.htm.md) record that contains the results of rules application including the list of applied rules, application details, and any errors. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Apply Payments and Credits by Rules
                            action.

                        

```
{
  "inputs": [
    {
      "accountId": "001AAC0001NmajhYBB",
      "targetDate": "2025-08-27"
    }
  ]
}
```

                    

                    
: 

Here's a sample success response for the Apply Payments and Credits by
                            Rules action.

```
[
  {
    "actionName": "applyPaymentsAndCreditsByRules",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "rulesApplicationResponse": {
        "rulesApplicationSummary": {
          "totalPaymentApplications": 1,
          "totalCreditMemoApplications": 1,
          "fetchedPaymentsCount": 1,
          "fetchedCreditMemosCount": 1,
          "areAllInvoicesConsidered": true
        },
        "isSuccess": true,
        "errors": null,
        "appliedRules": [
          "Match Balance",
          "Prioritize Highest Balance Invoices"
        ]
      }
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

                    
: 
                        

Here's a sample error response for the Apply Payments and Credits by
                            Rules action.

                        

```
[
  {
    "actionName": "applyPaymentsAndCreditsByRules",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "rulesApplicationResponse": {
        "rulesApplicationSummary": null,
        "isSuccess": false,
        "errors": [
          {
            "message": "We couldn't find eligible invoices to apply rules-based credits and payments. ",
            "errorCode": null
          }
        ],
        "appliedRules": null
      }
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_automate_refund.htm ===
---
page_id: actions_obj_automate_refund.htm
title: Automate Refund Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_automate_refund.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Automate Refund Action

Initiate refund orchestration for a credit memo
            generated from a subscription cancellation or negative amendment.

        
            

When you cancel a subscription or make a change that lowers the price (a negative
                amendment), a credit memo is generated. A credit memo is a record that represents
                the amount to be returned. Use this action to process the refund for that credit
                memo.

            

During an invoice batch run, Revenue Cloud Billing uses these two org preferences to
                run the refund orchestration.

            
                
- Conversion of negative invoice lines to credit memo and credit memo
                    lines—When turned on, this org preference creates a credit memo from the
                    negative invoice lines of a cancellation or a negative amendment, and then emits
                    a credit memo event.

                
- Issue refunds and settle balances — Listens to the credit memo event and starts
                    the refund orchestration for the converted credit memo.

            

            

Turn off these org preferences to call this action directly and choose which credit
                memo receives a refund.

            

In both modes, the orchestration runs these steps in order.

            
                
- Remove payments from the original invoice. Partial removal isn’t supported, so
                    each selected payment is removed in full. For example, if an invoice has two
                    payments P1 ($20) and P2 ($15) and the refund amount is $30, the orchestration
                    removes both P1 and P2 in full for a total of $35.

                
- Apply back any extra amount to the invoice. In the example above, $35 was
                    removed but only $30 is needed for the refund. The orchestration applies the
                    extra $5 from P2 back to the original invoice.

                
- Apply the credit memo to the original invoice to record the credit.

                
- Send a refund request to the payment gateway. The payment gateway is the service
                    that processes the customer's payment method. For example, a credit card
                    processor. In the example above, the orchestration sends two separate refund
                    requests, one for P1 ($20) and one for P2 ($10, the portion not applied
                    back).

                
- Record each refund against its original payment.

            

            

The orchestration selects the fewest payments to unapply so that the total unapplied
                amount is at least equal to the refund amount.

            

This action is available in API version 67.0 and later.

            

For
                more information about automated refunds in Subscription Management, see [Automate a refund
                    (Subscription Management reference)](https://developer.salesforce.com/docs/revenue/subscription-management/references/payments?meta=Automate%2Ba%2Brefund).

        

        

## Special Access Rules

            
            

The Automate Refund action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Cloud.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/automateRefund`

                
                
                    

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
| credit​MemoId | **Type** ID **Description** Required. ID of the credit memo to generate a refund. |
| invoiceId | **Type** ID **Description** ID of the invoice that the credit memo converts from. This ID matches the value in the Reference Entity field of the credit memo object. When you omit this input, the action reads the invoice ID from the Reference Entity field. When you provide this input, the value must match the Reference Entity field. If the values don’t match, the action returns a validation error.. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| status​Url | **Type** string **Description** URL to poll for the `RefundAsyncOperation` status. Use this URL to access the tracking record for the credit memo and check the current orchestration run status. |

        

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Automate Refund action.

                        

```
{
  "inputs": [
    {
      "creditMemoId": "3ttxx0000000001AAA",
      "invoiceId": "3ttxx0000000002BBB"
    }
  ]
}
```

                    

                    
: 
                        

This sample response shows a successful invocation with a status URL.

                        

```
[
  {
    "actionName": "automateRefund",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "statusUrl": "/services/data/v67.0/async-operations/00Dxx0000000000EAA/status"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

                    

                    
: 
                        

This sample shows an error response for an invalid credit memo ID.

                        

```
[
  {
    "actionName": "automateRefund",
    "errors": [
      {
        "statusCode": "INVALID_INPUT",
        "message": "The value \"INVALID\" for the creditMemoId parameter is invalid.",
        "fields": []
      }
    ],
    "invocationId": null,
    "isSuccess": false,
    "outcome": null,
    "outputValues": null,
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_blng_dspt_issue_credit_memo.htm ===
---
page_id: actions_obj_blng_dspt_issue_credit_memo.htm
title: Issue Credit Memo Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_blng_dspt_issue_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Issue Credit Memo Action

Issue credit memos for disputed invoices to resolve billing
            disputes.

        
            

Specify the credit request list to automate the creation of credit memos during the
                dispute resolution process. The credit request list includes the invoice ID, the
                total credit amount, an optional description, and a detailed list of specific
                invoice lines with their corresponding credit amounts.

            

This action is available in API version 66.0 and later.

        

        

## Special Access Rules

            
            

The Issue Credit Memo Action is available in Enterprise, Developer, and Unlimited
                Editions where Dispute Management is enabled in Billing.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/blngDsptIssueCreditMemo`

                
                
                    

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
| creditRequest​List | **Type** Apex-defined **Description** List of Apex-defined creditRequestInputRepresentations objects that contains the invoice ID, credit amount, description, and a list of creditLineRequestInputRepresentations objects. The creditLineRequestInputRepresentations objects include the invoice line ID, credit line amount, and a description. See [CreditLineRequestInputRepresentations](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md) Apex class. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 
: 

                        

                    

                
| Output | Details |
| --- | --- |
| creditResponse | **Type** Apex-defined **Description** An Apex-defined creditResponseOutputRepresentations object that contains the status and any additional information. See [CreditResponseOutputRepresentations](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md) Apex class. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Issue Credit Memo action.

                        

```
{
  "inputs": [
    {
      "creditRequestList": [
        {
          "invoiceId": "801xx000003GYexAAG",
          "creditAmount": 100,
          "description": "Credit for disputed charges",
          "creditLineRequestInputRepresentations": [
            {
              "invoiceLineId": "801xx000003GYeyAAG",
              "creditLineAmount": 50,
              "description": "Line-level credit"
            }
          ]
        }
      ]
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Issue Credit Memo action.

                        

```
[
  {
    "actionName": "blngDsptIssueCreditMemo",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "creditResponse": {
        "success": true,
        "message": "Credit memo issued successfully"
      }
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_blng_send_dunning_email.htm ===
---
page_id: actions_obj_blng_send_dunning_email.htm
title: Send Dunning Email Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_blng_send_dunning_email.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Send Dunning Email Action

Run an orchestration that sends dunning
            process emails for collection plans to recover overdue revenue and notify customers
            about amounts still due.

        
            

Specify the collection plan for the dunning emails. Optionally, specify the email
                template by name or by ID. The action triggers an orchestration that sends dunning
                process emails for a collection plan based on your configured timeline.

            

This action is available in API version 67.0 and later.

        

        

## Special Access Rules

            
            

The Send Dunning Email action is available in Enterprise, Unlimited, and
                Developer Editions of Revenue Cloud.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/blngSendDunningEmail`

                
                
                    

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
| collection​PlanId | **Type** string **Description** Required. ID of the collection plan record for dunning emails. |
| emailTemplate​NameOrId | **Type** string **Description** Email template name or ID to use for the reminder email. If not specified, the default email template is used. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| isDunning​EmailSent | **Type** boolean **Description** Indicates whether the dunning email related to the collection plan was sent (`true`) or not (`false`). |
| additional​Information | **Type** string **Description** Additional information to be passed on with the response. |

        

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Send Dunning Email action.

                        

```
{
  "inputs": [
    {
      "collectionPlanId": "0PLxxxxxxxxxxxxxxx",
      "emailTemplateNameOrId": "Dunning_Reminder_Template"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Send Dunning Email action.

                        

```
[
  {
    "actionName": "blngSendDunningEmail",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "isDunningEmailSent": true,
      "additionalInformation": null
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_blng_svc_inv_extend_due_date.htm ===
---
page_id: actions_obj_blng_svc_inv_extend_due_date.htm
title: Extend Invoice Due Date Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_blng_svc_inv_extend_due_date.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Extend Invoice Due Date Action

Update the due date on an invoice to accommodate payment extensions
            or resolve billing disputes.

        
            

Specify the invoice ID and the revised due date to adjust the payment timeline. Use
                this action to extend or change the due date on an invoice.

            

This action is available in API version 66.0 and later.

        

        

## Special Access Rules

            
            

The Extend Invoice Due Date Action is available in Enterprise, Developer, and
                Unlimited Editions where Dispute Management is enabled in Billing.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/blngSvcExtendInvoiceDueDate`

                
                
                    

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
| invoiceId | **Type** string **Description** ID of the invoice whose due date must be revised. |
| revisedDue​DateTime | **Type** date **Description** Date and time that’s to be updated as the new due date on the invoice. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| additional​Information | **Type** string **Description** Any additional information to be included in the response. |
| isSuccess | **Type** boolean **Description** Indicates whether the due date is updated on the invoice record (`true`) or not (`false`). |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Extend Invoice Due Date action.

                        

```
{
  "inputs": [
    {
      "invoiceID": "801xx000003GYexAAG",
      "revisedDueDate": "2025-03-31"
    }
  ]
}

```

                    

                    
: 
                        

This sample response is for the Extend Invoice Due Date action.

                        

```
[
  {
    "actionName": "blngSvcExtendInvoiceDueDate",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "isSuccess": true,
      "additionalInformation": "{\"status\":\"Due date updated successfully\"}"
    },
    "sortOrder": -1,
    "version": 1
  }
]

```

=== ARTICLE: actions_obj_blng_svc_suspend_billing.htm ===
---
page_id: actions_obj_blng_svc_suspend_billing.htm
title: Suspend Billing Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_blng_svc_suspend_billing.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Suspend Billing Action

Suspend or resume the billing of an account to handle billing
            disputes.

        
            

Specify the account ID and a date when billing must be suspended. Optionally, specify
                the date when billing must be resumed. The action suspends billing for the account
                from the suspension date and, if provided, resumes billing on the resumption
                date.

            

This action is available in API version 66.0 and later.

        

        

## Special Access Rules

            
            

The Suspend Billing Action is available in Enterprise, Developer, and Unlimited
                Editions where Dispute Management is enabled in Billing.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/blngSvcSuspendBilling`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| accountId | **Type** string **Description** ID of the account for which billing must be suspended. |
| resumptionDate | **Type** date **Description** Date when the billing must be resumed. |
| suspensionDate | **Type** date **Description** Date when the billing must be suspended. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| additional​Information | **Type** string **Description** Any additional information to be included in the response. |
| isSuccess | **Type** boolean **Description** Indicates whether the billing related to the specified account was suspended (`true`) or not (`false`). The default value is `false`. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Suspend Billing action.

                        

```
{
  "inputs": [
    {
      "accountId": "001xx000003GYexAAG",
      "suspensionDate": "2025-03-01",
      "resumptionDate": "2025-03-15"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Suspend Billing action.

                        

```
[
  {
    "actionName": "blngSvcSuspendBilling",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "isSuccess": true,
      "additionalInformation": "{\"status\":\"Billing suspended successfully\"}"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_blng_svc_update_bill_to_contact.htm ===
---
page_id: actions_obj_blng_svc_update_bill_to_contact.htm
title: Update Bill To Contact Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_blng_svc_update_bill_to_contact.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Update Bill To Contact Action

Update the Bill to Contact detail on an invoice to ensure accurate
            billing communication and routing.

        
            

Specify the invoice ID and the new Bill to Contact detail. Optionally, indicate
                whether the new contact must be set as the default for future invoices. Use this
                action to change the contact to be billed on an invoice, for example, when handling
                a billing dispute.

            

This action is available in API version 66.0 and later.

        

        

## Special Access Rules

            
            

The Update Bill To Contact Action is available in Enterprise, Developer, and
                Unlimited Editions where Dispute Management is enabled in Billing.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/blngSvcUpdateBillToContact`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| invoiceId | **Type** string **Description** ID of the invoice whose Bill to Contact detail must be updated. |
| newBill​ToContactId | **Type** string **Description** ID of the Bill to Contact record to be updated on the invoice. |
| setAs​Default | **Type** boolean **Description** Indicates whether the new Bill to Contact detail must be set as default for future invoices (`true`) or not (`false`). The default value is `false`. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| additional​Information | **Type** string **Description** Any additional information to be included in the response. |
| isSuccess | **Type** boolean **Description** Indicates whether the Bill to Contact detail is updated on the invoice record (`true`) or not (`false`). |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Update Bill To Contact action.

                        

```
{
  "inputs": [
    {
      "invoiceID": "3ttxx0000000001AAA",
      "newBillToContactid": "003xx000004XYZPAA4",
      "setAsDefault": true
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Update Bill To Contact action.

                        

```
[
  {
    "actionName": "blngSvcUpdateBillToContact",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "isSuccess": true,
      "additionalInformation": "{\"status\":\"Success\",\"notes\":\"Default billing contact updated.\"}"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_create_billing_schedule_from_billing_transaction.htm ===
---
page_id: actions_obj_create_billing_schedule_from_billing_transaction.htm
title: Create Billing Schedules From Billing Transaction Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_billing_schedule_from_billing_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Billing Schedules From Billing Transaction Action

Create one or more billing schedules for a specified billing
			transaction ID.

		
			

This action calls the [Create Billing Schedules
					for Orders (POST) API](./connect_resources_create_billing_schedules.htm.md) to retrieve the billing transaction items
				associated with the billing transaction ID. The API generates the corresponding
				billing schedules for each of the billing transaction items for operations such as
				transaction modifications, renewals, cancellations, and new sales.

			

This action is available in API version 62.0 and later.

		

		

## Special Access Rules

			
			

The Create Billing Schedules From Billing Transaction action is available in Enterprise,
				Unlimited, and Developer Editions where Billing is enabled. To use this action, you
				need the Create Billing Schedules From Billing Transactions API permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/createBillingSchedulesFromBillingTransaction`

				
				
					

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
| billingTransactionId | **Type** string **Description** Required. ID of the billing transaction record to create one or more billing schedules for. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** Universally Unique Identifier (UUID) that’s used to track the status of the asynchronous action. |
| statusUrl | **Type** string **Description** URL that’s used to check the status of the API request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Create Billing Schedules From Billing
							Transaction action.

						

```
{
  "inputs": [
    {
      "billingTransactionId": "801xx000003JztvAAC"
    }
  ]
}
```

						

This example shows a sample response for the Create Billing Schedules
							From Billing Transaction action.

						

```
{
  "actionName": "createBillingSchedulesFromBillingTransaction",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "requestId": "4sFDU00000000652AA",
    "statusUrl": "/services/data/v62.0/sobjects/AsyncOperationTracker/16Pxx0000004NhAEAU"
  },
  "sortOrder": -1,
  "version": 1
}
```

					

				
			

		

	

#### See Also

- [*Revenue Cloud Developer Guide*: Context-Aware Billing
                            Schedule API](./connect_resources_create_billing_schedules.htm.md)

=== ARTICLE: actions_obj_create_billing_schedules_from_transaction.htm ===
---
page_id: actions_obj_create_billing_schedules_from_transaction.htm
title: Create Standalone Billing Schedules Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_create_billing_schedules_from_transaction.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Create Standalone Billing Schedules Action

Creates billing schedules for internal or external transaction
            records by calling the Create Standalone Billing Schedules API.

        

This action is available in API version 64.0 and later.

See [Create Standalone Billing
                    Schedules (POST) API](./connect_resources_create_billing_schedules_from_any_transaction.htm.md) to know more about the mandatory and optional tags,
                sample transaction details, and sample payloads for various types of
                transactions.

        

## Special Access Rules

This action is available in Enterprise, Unlimited, and Developer Editions with the Revenue Cloud
                Billing license. To use this action, you need the Billing Operations permission
                set.

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/createBillingSchedulesFromTrxn`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| contextDefinitionName | **Type** string **Description** Required. Name of the context definition that contains the mappings for the transaction record and billing schedules. |
| readContextMappingName | **Type** string **Description** Required. Name of the context mapping with the mapping for the transaction. |
| saveContextMappingName | **Type** string **Description** Required. Name of the context mapping with the mapping for the billing schedule and billing schedule group. The save context mapping is used to save the billing schedule. |
| transactionDetails | **Type** string **Description** Required. A JSON string containing the ID of the transaction record that the billing schedule is created for and other additional transaction details. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** Unique request identifier that you can use to poll the asynchronous request. |
| statusUrl | **Type** string **Description** Status URL that’s used to track the operation. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Create Billing Schedules From Transaction
                            action.

                        

```
{
  "inputs": [
    {
      "transactionDetails": "{\"Transaction\":[{\"id\":\"sampleA1\",\"ParentTransactionId\":\"sample\",\"TransactionId\":\"sampleA1\",\"RelatedTransactionId\":\"ter1\",\"StartDate\":\"2025-04-01\",\"UnitPrice\":10,\"Quantity\":1,\"TotalPrice\":90,\"BillingActionType\":\"Amend\"},{\"id\":\"sampleA2\",\"ParentTransactionId\":\"sample\",\"TransactionId\":\"sampleA2\",\"RelatedTransactionId\":\"ter1\",\"StartDate\":\"2025-03-01\",\"UnitPrice\":10,\"Quantity\":-2,\"TotalPrice\":-200,\"BillingActionType\":\"Amend\"},{\"id\":\"sampleA3\",\"ParentTransactionId\":\"sample\",\"TransactionId\":\"sampleA3\",\"RelatedTransactionId\":\"ter1\",\"StartDate\":\"2025-03-01\",\"UnitPrice\":10,\"Quantity\":-1,\"TotalPrice\":-100,\"BillingActionType\":\"Amend\"}]}",
      "contextDefinitionName": "StandaloneBillingContext__stdctx",
      "readContextMappingName": "TransactionMapping",
      "saveContextMappingName": "BSGEntitiesMapping"
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Create Billing Schedules From
                            Transaction action.

                        

```
{
  "actionName": "createBillingSchedulesFromTrxn",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "requestId": "16PZ6000000CnKRMA0",
    "statusUrl": "/services/data/v64.0/sobjects/AsyncOperationTracker/16PZ6000000CnKRMA0"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_generate_batch_invoice_documents.htm ===
---
page_id: actions_obj_generate_batch_invoice_documents.htm
title: Generate Invoice Documents Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_generate_batch_invoice_documents.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Generate Invoice Documents Action

Asynchronously generate PDF documents for the invoices associated with
			an invoice batch run record that are in the `Draft`
			or `Posted` status.

		
			

This action uses the ID of the invoice batch run record to find the draft or posted invoices
				from the batch and to generate the PDF documents for its invoices that are in the
					`Draft` or `Posted` status. This action creates a DocGenerationBatchProcess record
				that contains the Document Generation Process and Invoice Document records for each
				of the invoices. This action is available in API version 63.0 and later with Revenue
				Cloud Billing.

		

		

## Special Access Rules

			
			

The Generate Invoice Documents action is available in Enterprise, Unlimited, and Developer
				Editions where Revenue Cloud Billing is enabled. The org must have Billing Docgen
				enabled and an active Invoice Document Template to generate PDF documents. To use
				this action, you need either the Billing Operations User or the Billing Admin
				permission set, along with the Docgen Designer and Docgen Designer Standard User
				permission sets.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/generateInvoiceDocuments`

				
				
					

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
| invoiceBatchRunId | **Type** string **Description** Required. ID of the invoice batch run record that created the draft or posted invoices. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| requestId | **Type** string **Description** An alphanumeric string to track the status of the document generation request. |
| requestStatus | **Type** boolean **Description** Indicates whether the operation is successful (`true`) or not (`false`). |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Generate Invoice Documents
							action.

						

```
{
  "inputs": [
    {
      "invoiceBatchRunId": "5IRSG000001Az014AC"
    }
  ]
}
```

						

This example shows a sample response for the Generate Invoice Documents
							action.

						

```
{
  "actionName": "generateInvoiceDocuments",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "requestId": "4sFDU00000000652AA",
    "requestStatus": true
  }
}
```

=== ARTICLE: actions_obj_generate_statement_of_account.htm ===
---
page_id: actions_obj_generate_statement_of_account.htm
title: Generate Account Statement
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_generate_statement_of_account.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Generate Account Statement

Generates a comprehensive account statement for a specified account
            with transaction history and balance information.

        
            

An account statement includes these details.

            
        
- Transaction History—List of all financial transactions, such as invoices, credit
          memos, debit memos, payments, and refunds, within a specified date range.

        
- Open Balances—Non-zero balances for invoices and other transactions.

        
- Account Summary—Aggregated totals including beginning balance, total charges,
          total payments, and ending balance.

        
- Multi-currency Support—Transactions across multiple currencies.

      

            

This action is available in API version 66.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/generateAccountStatement`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| accountId | **Type** string **Description** Required. ID of the account for which to generate the statement of account. |
| associatedAccountIds | **Type** string **Description** List of associated account IDs from hierarchy to include in the statement. You can specify a maximum of 50 accounts. |
| correlationId | **Type** string **Description** Correlation ID that tracks messages related to the request. These messages are logged in Splunk by the different services involved in the request. If this ID isn’t specified, a random Universally Unique Identifier (UUID) is created. |
| customFields | **Type** string **Description** JSON string specifying custom fields to include in the statement. As a best practice, we recommend that you limit the number of custom fields up to 30 fields. Valid objects to specify the associated fields are: Invoice CreditMemo Payment DebitMemo Refund Account Here's the expected format.{"Invoice": ["field1", "field2"], "Account": {"base": ["field1"], "associated": ["field2"]}} Available in API version 67.0 and later. |
| documentTemplateId | **Type** string **Description** Document template ID to use for PDF generation. If you don’t specify a value, the default account statement template is used. |
| shouldShowOpenBalancesOnly | **Type** boolean **Description** Indicates whether to show only accounts with non-zero balances (`true`) or complete transaction history within date range (`false`). |
| sortBy | **Type** string **Description** Required. Criteria for sorting transactions. The default and valid value is `Date`. |
| sortingOrder | **Type** string **Description** Sort order for transactions. Valid values are: `Ascending` `Descending` The default value is `Desc`. |
| startDate | **Type** date **Description** Required. The date from when the transaction history is to be considered in YYYY MM DD format. This parameter value is required when the `shouldShowOpenBalancesOnly` parameter value is `false`. The date must be within the last 90 days and can't be in the future. |
| transactionTypes | **Type** string **Description** List of transaction types to include in the statement. If you don’t specify a value or if it’s empty, all transaction types are included. Valid values are: `All` `Invoice` `CreditMemo` `Payment` `DebitMemo` `Refund` |

        

        

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
| accountId | **Type** string **Description** ID of the account for which to generate the account statement. |
| requestIdentifier | **Type** string **Description** Unique request identifier for tracking the async operation. |
| statusUrl | **Type** string **Description** URL that tracks the status of the request and retrieves the generated document. |
| templateId | **Type** string **Description** Document template ID that’s used for PDF generation. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This example shows a sample request for the Generate Account Statement
                            action.

                        

```
{
  "inputs": [
    {
      "accountId": "001000000000001AAA",
      "shouldShowOpenBalancesOnly": false,
      "startDate": "2025-01-01",
      "transactionTypes": [
        "All"
      ],
      "sortBy": "Date",
      "sortingOrder": "Descending",
      "associatedAccountIds": [
        "001000000000002AAA",
        "001000000000003AAA"
      ],
      "documentTemplateId": "a0T000000000001AAA",
      "customFields": "{\"Invoice\": [\"TotalAmountWithTax\"], \"Account\": {\"base\": [\"Phone\", \"Fax\"], \"associated\": [\"Website\"]}}}"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample response for the Generate Account Statement
                            action.

                        

```
{
  "accountId": "001AAC0001O5W9pYBF",
  "errors": [],
  "requestIdentifier": "3267407f-0c96-4b8a-a8e0-bb7a71c91a2f",
  "statusUrl": "16PAAC000008AIM",
  "success": true,
  "templateId": "2dtAAC000002oiIYBQ"
}
```

=== ARTICLE: actions_obj_post_draft_credit_memo.htm ===
---
page_id: actions_obj_post_draft_credit_memo.htm
title: Post Draft Credit Memo Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_post_draft_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Post Draft Credit Memo Action

Post a draft credit memo to a credit memo record for review and
            approval.

        
            

This action is available in API version 65.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/postDraftCreditMemo`

                
                
                    

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
| correlationId | **Type** string **Description** Splunk correlation ID to use to track messages that are related to the request and logged in Splunk by the different services involved in the request. If not specified, the service creates a random Universally Unique Identifier (UUID). |
| creditMemoId | **Type** string **Description** Required. ID of the credit memo record in `Draft` status to be posted. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| requestIdentifier | **Type** string **Description** The UUID that's used to track the status of the asynchronous action. |
| statusUrl | **Type** string **Description** The URL to use to check the status of the request. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This example shows a sample request that contains the ID of the credit
                            memo to be posted.

                        

```
{
  "inputs": [
    {
      "creditMemoId": "50gDU00000001MdYAI"
    }
  ]
}
```

                    

                    
: 
                        

This example shows a sample successful response.

                        

```
[
  {
    "actionName": "postDraftCreditMemo",
    "errors": [],
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "statusUrl": "/services/data/v68.0/sobjects/AsyncOperationTracker/16PDU000000A4nw2AC",
      "requestIdentifier": "d3a9d9ce-2a83-4a08-bcf3-df0348a0008c"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_post_draft_invoice.htm ===
---
page_id: actions_obj_post_draft_invoice.htm
title: Post Draft Invoice Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_post_draft_invoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Post Draft Invoice Action

Update the status of an invoice from `Draft` to `Posted` for a credit memo
			application.

		
			

This action uses the ID of the draft invoice and triggers an asynchronous process to post the
				invoice. This action is available in API version 62.0 and later.

		

		

## Special Access Rules

			
			

The Post Draft Invoice action is available in Enterprise, Unlimited, and Developer Editions
				where Billing is enabled. To use this action, you need the Billing Operations User
				permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/postDraftInvoice`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| correlationId | **Type** string **Description** Splunk correlation ID to track the messages that are related to the request and are logged in Splunk by the different services involved in the request. If the ID isn’t specified, the service creates a random Universally Unique Identifier (UUID). |
| invoiceId | **Type** string **Description** Required. ID of the `Draft` invoice to be posted. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| requestIdentifier | **Type** string **Description** UUID that’s used to track the status of the asynchronous action. |
| statusUrl | **Type** string **Description** URL that’s used to check the status of the API request. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Post Draft Invoice
							action.

						

```
{
  "inputs": [
    {
      "invoiceId": "3ttDU00000000iZYAQ"
    }
  ]
}
```

						

This example shows a sample response for the Post Draft Invoice
							action.

						

```
{
  "actionName": "postDraftInvoice",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "requestIdentifier": "4sFDU00000000652AA",
    "statusUrl": "/services/data/v62.0/sobjects/AsyncOperationTracker/16Pxx0000004NhAEAU"
  }
}
```

=== ARTICLE: actions_obj_post_draft_invoice_batch_run.htm ===
---
page_id: actions_obj_post_draft_invoice_batch_run.htm
title: Post Draft Invoice Batch Run Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_post_draft_invoice_batch_run.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Post Draft Invoice Batch Run Action

Update the status of a batch of invoices from `Draft` to `Posted`
			for a credit memo application.

		
			

This action uses the ID of the invoice batch run record to find draft invoices from the batch
				and to post the draft invoices to an invoice record. This action is available in API
				version 62.0 and later.

		

		

## Special Access Rules

			
			

The Post Draft Invoice Batch Run action is available in Enterprise, Unlimited, and Developer
				Editions where Billing is enabled. To use this action, you need the Billing
				Operations User permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/postDraftInvoiceBatchRun`

				
				
					

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
| invoiceBatchRunId | **Type** string **Description** Required. ID of the invoice batch run record that created the draft invoices. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| invBatchDraftToPostedRunId | **Type** string **Description** ID of the record that’s created to track the batch process of posting draft invoices. These draft invoices are associated with the parent invoice batch run record. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Post Draft Invoice Batch Run
							action.

						

```
{
  "inputs": [
    {
      "invoiceBatchRunId": "5IRSG000001Az014AC"
    }
  ]
}
```

						

This example shows a sample response for the Post Draft Invoice Batch Run
							action.

						

```
{
  "actionName": "postDraftInvoiceBatchRun",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "invBatchDraftToPostedRunId": "4sFDU00000000652AA"
  }
}
```

=== ARTICLE: actions_obj_recover_billing_schedule.htm ===
---
page_id: actions_obj_recover_billing_schedule.htm
title: Recover Billing Schedules Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_recover_billing_schedule.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Recover Billing Schedules Action

Recover one or more billing schedules in the `Error` or `Processing` status.

		

This action uses the ID of the billing schedule record in the `Error` or `Processing` status to
				retrieve the latest generated invoice. This action also retrieves any other billing
				schedules in the `Error` or `Processing` status associated with that invoice.

This action is available in API version 62.0 and later.

		

## Special Access Rules

			
			

The Recover Billing Schedules action is available in Enterprise, Unlimited, and
				Developer Editions where Billing is enabled. To use this action, you need the Manage
				Errors Using Invoice Error Recovery API permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/recoverBillingSchedules`

				
				
					

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
| billingScheduleId | **Type** string **Description** Required. ID of the billing schedule record in the `Error` or `Processing` status. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| successBillingScheduleIds | **Type** string **Description** Comma-separated list of IDs associated with the parent billing schedule record in the `Error` or `Processing` status. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Recover Billing Schedules
							action.

						

```
{
  "inputs": [
    {
      "billingScheduleId": "801xx000003JztvAAC"
    }
  ]
}
```

						

This example shows a sample response for the Recover Billing Schedules
							action.

						

```
{
  "actionName": "recoverBillingSchedules",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "successBillingScheduleIds": ["4sFDU00000000652AA", 16Pxx0000004NhAEAU]
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_run_apply_credit.htm ===
---
page_id: actions_obj_run_apply_credit.htm
title: Apply Credit Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_run_apply_credit.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Apply Credit Action

Apply a credit memo or credit memo line to an invoice or invoice
			line, respectively. 

		
			

This action credits the amount of the credit memo or credit memo line to the
				corresponding invoice or invoice line, reducing both their balances.

			

This action is available in API version 62.0 and later.

		

		

## Special Access Rules

			
			

The Apply Credit action is available in Enterprise, Developer, and Unlimited Editions
				where Billing is enabled. To use this action, you need the Credit Memo Operations
				User permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/applyCredit`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| appliedCreditAmount | **Type** double **Description** Required. Credit amount applied to an invoice or invoice line. |
| creditSourceRecordId | **Type** string **Description** Required. ID of the credit memo or credit memo line that’s applied to an invoice or invoice line. |
| creditTargetRecordId | **Type** string **Description** Required. ID of the invoice or invoice line record that the credit is applied to. |
| description | **Type** string **Description** Additional details about the credit memo or credit memo line to be applied to an invoice or invoice line. |
| effectiveDate | **Type** string **Description** Date to use for applying the credit memo to an invoice or invoice line. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| recordId | **Type** string **Description** ID of the credit memo invoice application or credit memo line invoice line record of type `Applied` that the action created. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Apply Credit action.

						

```
{
  "inputs": [
    {
      "appliedCreditAmount": 20,
      "creditTargetRecordId": "3ttDU00000000iZYAQ",
      "creditSourceRecordId": "50gDU000000007NYAQ",
      "description": "Applied credit memo to an invoice",
      "effectiveDate": "2024-08-27"
    }
  ]
}
```

						

This example shows a sample response for the Apply Credit action.

						

```
{
  "actionName": "applyCredit",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outputValues": {
    "recordId": "4sFDU00000000652AA"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_run_unapply_credit.htm ===
---
page_id: actions_obj_run_unapply_credit.htm
title: Unapply Credit Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_run_unapply_credit.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unapply Credit Action

Unapply a credit memo or credit memo line from an invoice or invoice
			line, respectively.

		

This action unapplies the credit from an invoice or invoice line. This process
				involves crediting the applied amount of the credit memo invoice application or
				credit memo line invoice line record to the related credit memo or credit memo line
				and invoice or invoice line.

This action is available in API version 62.0 and
				later.

		

## Special Access Rules

			
			

The Apply Credit action is available in Enterprise, Developer, and Unlimited Editions where
				Billing is enabled. To use this action, you need the Credit Memo Operations User
				permission set.

		

		

## Supported REST HTTP Methods

			
			
				
					

**URI**

					
: `/services/data/v68.0/actions/standard/unapplyCredit`

				
				
					

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

						

					

				
| Input | Details |
| --- | --- |
| effectiveDate | **Type** string **Description** Date when the credit is unapplied from an invoice or invoice line. |
| description | **Type** string **Description** Additional details about the credit memo invoice application or credit memo line invoice line record of type `Applied` that’s processed. |
| recordId | **Type** string **Description** Required. ID of the credit memo invoice application or credit memo line invoice line record of type `Applied` that’s processed to unapply the credit. |

		

		

## Outputs

			
			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

					

				
| Output | Details |
| --- | --- |
| recordId | **Type** string **Description** ID of the credit memo invoice application or credit memo line invoice line record of type `Unapplied` that the action created. |

		

		

## Example

			
			
				
					

**POST**

					
: 
						

This example shows a sample request for the Unapply Credit action.

						

```
{
  "inputs": [
    {
      "recordId": "4sFDU000000005g2AA",
      "description": "Unapplied credit memo from an invoice",
      "effectiveDate": "2024-08-27"
    }
  ]
}
```

						

This example shows a sample response for the Unapply Credit action.

						

```
  {
    "actionName": "unapplyCredit",
    "errors": null,
    "invocationId": null,
    "isSuccess": true,
    "outputValues": {
      "recordId": "4sFDU00000000602AA"
    },
    "sortOrder": -1,
    "version": 1
  }
```

=== ARTICLE: actions_obj_unapply_payment.htm ===
---
page_id: actions_obj_unapply_payment.htm
title: Unapply Payment Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_unapply_payment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Unapply Payment Action

Unapplies a payment that's already been applied to an invoice or
            invoice line by crediting the amount back to the payment and the invoice or invoice
            line.

        
            

If the **Apply Payments to Invoices** setting is enabled, payments
                can be applied to invoices, which creates the PaymentLineInvoice records of type
                    `Applied`. If the **Apply Payments
                    to Invoices feature** setting is disabled, payments can be applied to
                invoice lines, which creates the PaymentLineInvoiceLine records of type `Applied`.

            

When payments are unapplied, the PaymentLineInvoice or PaymentLineInvoiceLine records
                of type `Applied` has the associated
                PaymentLineInvoice or PaymentLineInvoiceLine records of type `Unapplied`.

            

This action is available in API version 64.0 and later.

        

        

## Special Access Rules

This action is available in Enterprise,
                Unlimited, and Developer Editions where Billing is enabled. To use this action, you
                need the Payment Ops permission set.

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/unapplyPayment`

                
                
                    

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

                        

                    

                
| Input | Details |
| --- | --- |
| description | **Type** string **Description** Additional details about the payment line invoice or payment line invoice line that's processed to unapply the payment. |
| effectiveDateTime | **Type** datetime **Description** Date and time to use for unapplying the payment from an invoice or invoice line. |
| recordId | **Type** id **Description** Required ID of the payment line invoice or payment line invoice line record of type `Applied` that’s processed to unapply the payment. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| recordId | **Type** id **Description** ID of the payment line invoice or payment line invoice line record of type `Unapplied` that the action created. |
| unappliedDateTime | **Type** datetime **Description** Date and time when the payment was unapplied. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

This sample request is for the Unapply Payment action.

                        

```
{
  "inputs": [
    {
      "description": "Unapply payment",
      "effectiveDateTime": "2024-08-11T07:53:15.000Z",
      "recordId": "1PLR000000000dDOAQ"
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Unapply Payment action.

                        

```
{
  "actionName": "unapplyPayment",
  "errors": null,
  "isSuccess": true,
  "outputValues": {
    "recordId": "1PLR000000000dDOAQ",
    "unappliedDateTime": "2024-08-11T08:09:01.000Z"
  },
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_void_posted_credit_memo.htm ===
---
page_id: actions_obj_void_posted_credit_memo.htm
title: Void Posted Credit Memo Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_void_posted_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Void Posted Credit Memo Action

Invoke the Void Posted Credit Memo API by providing a credit memo ID.

        
            

This action is available in API version 66.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/voidPostedCreditMemo`

                
                
                    

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
| creditMemoId | **Type** string **Description** Required. ID of the credit memo record in posted status to be voided. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| debitMemoId | **Type** string **Description** ID of the created debit memo record. |
| statusUrl | **Type** string **Description** URL to use to check the status of the request. |

        

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Void Posted Credit Memo action.

                        

```
{
  "inputs": [
    {
      "creditMemoId": "50gSG0000001y5NYAQ"
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Void Posted Credit Memo action.

                        

```
[
  {
    "actionName": "voidPostedCreditMemo",
    "errors": [],
    "invocationId": null,
    "isSuccess": true,
    "outcome": null,
    "outputValues": {
      "debitMemoId": "4DmSG000001YcIP0A0",
      "statusUrl": "/services/data/v68.0/sobjects/AsyncOperationTracker/16PSG000001qlyL2AQ"
    },
    "sortOrder": -1,
    "version": 1
  }
]
```

=== ARTICLE: actions_obj_write_off_invoices.htm ===
---
page_id: actions_obj_write_off_invoices.htm
title: Write Off Invoices Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_write_off_invoices.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Write Off Invoices Action

Write off partially paid or unpaid invoices to manage pending debts
            and to maintain accurate financial records. This action calls the Posted Invoice List
            Write-Off (POST) API.

        
            

This action is available in API version 64.0 and later.

        

        

## Special Access Rules

            
            

The Write Off Invoices action is available in Enterprise, Developer, and Unlimited
                Editions where Billing is enabled. To use this action, you need the Billing
                Operations User and Credit Memo Operations User permission sets.

        

        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/writeOffInvoices`

                
                
                    

**Formats**

                    
: JSON, XML

                
                
                    

**HTTP Methods**

                    
: GET

                
                
                    

**Authentication**

                    
: `Authorization:
                            Bearertoken`

                
                
                    

**Notes**

                    
: You can also call the associated Connect REST API endpoint or
                        InvoiceWriteOff Apex methods. See [Posted Invoice List Write-Off
                            (POST)](./connect_resources_write_off_invoices.htm.md) API or [InvoiceWriteOff Namespace](./apex_namespace_InvoiceWriteOff.htm.md).

                
            

        

        

## Inputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| writeOffInvoiceInputList | **Type** Apex-defined **Description** Required. A collection of Apex input records that contain details about the invoices to be written off. See [InvoiceWriteOff Namespace](./apex_namespace_InvoiceWriteOff.htm.md) for the list of input parameters. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| writeOffInvoiceResponseList | **Type** Apex-defined **Description** A collection of Apex output records that contain details about the invoices that were written off. See [InvoiceWriteOff Namespace](./apex_namespace_InvoiceWriteOff.htm.md) for the list of output parameters. |

        

        
        

## Example

            
            
                
                    

**GET**

                    
: 
                        

This sample request is for the Write Off Invoices action.

                        

```
{
  "inputs": [
    {
      "apexClass": "InvoiceWriteOff__WriteOffInvoiceInputList",
      "bytelength": 0,
      "configuration": false,
      "defaultValue": null,
      "description": "A collection of Apex WriteOffInvoiceInputList records that contain details about the invoices to be written-off.",
      "label": "WriteOffInvoiceInputList",
      "maxOccurs": 1,
      "name": "writeOffInvoiceInputList",
      "picklistValues": null,
      "placeholderText": null,
      "required": true,
      "sObjectType": null,
      "setupReferenceType": null,
      "toolingType": null,
      "type": null
    }
  ]
}
```

                    

                    
: 
                        

This sample response is for the Write Off Invoices action.

                        

```
{
  "outputs": [
    {
      "additionalAttributes": null,
      "apexClass": "InvoiceWriteOff__WriteOffInvoiceResponseList",
      "description": "A collection Apex WriteOffInvoiceResponseList records that contain details about the invoices that were written off.",
      "label": "WriteOffInvoiceResponseList",
      "maxOccurs": 1,
      "name": "writeOffInvoiceResponseList",
      "picklistValues": null,
      "sobjectType": null,
      "type": null
    }
  ]
}
```

=== ARTICLE: apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm ===
---
page_id: apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm
title: BatchInvoiceApplication Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# BatchInvoiceApplication Class

 
 
 
Update a batch of invoices from Draft to Posted status for a credit memo application. by
  using the BatchInvoiceApplication class.

  

## Namespace

   
   

ConnectApi

  

 

 

## BatchInvoiceApplication Methods

 These methods are for `BatchInvoiceApplication`.
  All methods are static.

 

- 
**[triggerInvoiceBatchDraftToPosted(invoiceBatchRunId)](./apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm.md#apex_ConnectAPI_BatchInvoiceApplication_triggerInvoiceBatchDraftToPosted_1)**  

Update a batch of invoices from Draft to Posted status for a credit memo     application.

### triggerInvoiceBatchDraftToPosted(invoiceBatchRunId)

Update a batch of invoices from Draft to Posted status for a credit memo
    application.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.InvoiceBatchDraftToPostedResult
          triggerInvoiceBatchDraftToPosted(String invoiceBatchRunId)`

#### Parameters

**invoiceBatchRunId**

: Type: String

          
: ID of the invoice batch run record that creates the draft invoices.

#### Return Value

Type: [`ConnectApi.InvoiceBatchDraftToPostedResult`](./apex_connectapi_output_invoice_batch_draft_to_posted_output.htm.md)

#### Usage

You need the Billing Operations User permission set to use this
        method.

This method posts the draft invoices and changes the status of the invoices
        from `Draft` to `Posted`.

=== ARTICLE: apex_ConnectAPI_Billing_static_methods.htm ===
---
page_id: apex_ConnectAPI_Billing_static_methods.htm
title: Billing Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_Billing_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# Billing Class

 
 
 
Manage billing scenarios by using the Billing class. You can convert negative invoice
  lines, create and apply a credit memo to an invoice, generate invoices, and recover billing
  schedules.

  

## Namespace

   
   

ConnectApi

  

 

 

## Billing Methods

 These methods are for `Billing`. All methods are
  static.

 

- 
**[convertNegativeInvoiceLines(ConvertNegativeInvoiceLinesInput, invoiceId)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_convertNegativeInvoiceLines)**  

Convert a list of invoice lines with a negative amount into a posted credit memo. This     conversion is applicable for a single invoice at a time.

- 
**[createCreditMemos(CreditMemoInputRequest)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_createCreditMemos_1)**  

Create a credit memo without applying it to an invoice. You can credit the invoice at a     later date.

- 
**[creditInvoice(CreditInvoiceInput, invoiceId)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_creditInvoice_1)**  

Create a credit memo and apply it to an invoice. The credit memo can fully or partially     credit the invoice.

- 
**[generateInvoices(inputRequest)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_generateInvoices_1)**  

Create an invoice from a billing schedule.

- 
**[recoverBillingSchedules(inputRequest)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_recoverBillingSchedules_1)**  

Recover the latest generated invoice associated with the billing schedules in the Error     or Processing status.

- 
**[voidPostedCreditMemo(VoidPostedCreditMemoInput, creditMemoId)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_voidPostedCreditMemo_1)**  

Invoke the Void Posted Credit Memo API by providing a credit memo ID.

- 
**[voidPostedInvoice(invoiceId)](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_voidPostedInvoice_1)**  

Void a posted invoice to rebill the customer, if necessary.

  

### convertNegativeInvoiceLines(ConvertNegativeInvoiceLinesInput, invoiceId)

  
  
  
Convert a list of invoice lines with a negative amount into a posted credit memo. This
    conversion is applicable for a single invoice at a time.

    

#### API Version

      
      

62.0

    

    

#### Requires Chatter

      
      

No

    

    

#### Signature

      
      

`public static ConnectApi.ConvertNegativeInvoiceLinesResult
          convertNegativeInvoiceLines(ConnectApi.ConvertNegativeInvoiceLinesInputRequest
          ConvertNegativeInvoiceLinesInput, String invoiceId)`

      

```
ConnectApi.Billing, convertNegativeInvoiceLines, [ConnectApi.ConvertNegativeInvoiceLinesInputRequest, String], ConnectApi.ConvertNegativeInvoiceLinesResult
```

    

    

#### Parameters

      
      
        
          

**ConvertNegativeInvoiceLinesInput**

          
: Type: [ConnectApi.ConvertNegativeInvoiceLinesInputRequest](./apex_connectapi_input_convert_negative_invoice_lines.htm.md)

          
: 
            

Input parameters to convert a negative invoice line to a credit.

          

        
        
          

**invoiceId**

          
: Type: String

          
: ID of the invoice whose negative invoice lines must be converted.

        
      

    

    

#### Return Value

      
      

Type: [ConnectApi.ConvertNegativeInvoiceLinesResult](./apex_connectapi_output_convert_negative_invoice_lines_output.htm.md)

    

    

#### Usage

You need the Credit Memo Operations User permission set to use this method.

Keep these considerations in mind when you use this method.

        
- All invoice lines must be related to the same invoice.

        
- The invoice line must have a negative amount.

        
- The invoice line must not be a previously converted credit memo.

        
- The invoice must have the `Posted` status.

        
- The invoice must not have any active settlements such as credit applications.

      

    
  

### createCreditMemos(CreditMemoInputRequest)

Create a credit memo without applying it to an invoice. You can credit the invoice at a
    later date.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RevenueAsyncRepresentation createCreditMemos(ConnectApi.StandaloneCreditMemoInputRequest CreditMemoInputRequest)`

#### Parameters

**CreditMemoInputRequest**

: Type: [`ConnectApi.StandaloneCreditMemoInputRequest`](./apex_connectapi_input_standalone_credit_memo.htm.md)

: Input representation of the details required to create a standalone credit memo.

#### Return Value

Type: [`ConnectApi.RevenueAsyncRepresentation`](./apex_connectapi_output_revenue_async.htm.md)

#### Usage

You need the Credit Memo Operations User permission set to use this
        method.

Specify the credit memo header information, charge parameters, adjustment
        parameters, and tax parameters. A credit memo requires at least one credit memo line. The
        credit memo line can be a charge or an adjustment.

Specify the credit memo lines that
        you want as lists of charges and adjustments. Each credit memo line must be related to a
        product.

### creditInvoice(CreditInvoiceInput, invoiceId)

Create a credit memo and apply it to an invoice. The credit memo can fully or partially
    credit the invoice.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RevenueAsyncLineLevelOutputResponse creditInvoice(ConnectApi.CreditInvoiceInputRequest CreditInvoiceInput, String invoiceId)`

```
ConnectApi.Billing, creditInvoice, [ConnectApi.CreditInvoiceInputRequest, String], ConnectApi.RevenueAsyncLineLevelOutputResponse
```

#### Parameters

**CreditInvoiceInput**

: Type: [`ConnectApi.CreditInvoiceInputRequest`](./apex_connectapi_input_credit_invoice.htm.md)

: Input representation of the details of the request to create a credit memo.

**invoiceId**

: Type: String

: ID of the invoice to be credited partially or fully. The status of the invoice must be `Posted`.

#### Return Value

Type: [`ConnectApi.RevenueAsyncLineLevelOutputResponse`](./apex_connectapi_output_revenue_async_line_level.htm.md)

#### Usage

      
    

    
      

Use this method to adjust an outstanding invoice balance or rectify errors in an invoice.
        Pass a list of invoice lines to credit. Keep these considerations in mind when you use this
        API.

      
        
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

      

      

This method creates and posts a credit memo. The credit memo has one credit memo line for
        each invoice line passed in the API request. The invoice’s balance is then reduced by a
        value equal to the credit memo’s balance. This API modifies the balance of a posted invoice
        or invoice line based on the specified credit application level for your org. See [Apply Credits to Posted Invoices or
          Invoice Lines](https://help.salesforce.com/s/articleView?id=sf.billing_setup_credit_application_level.htm&language=en_US).

    

### generateInvoices(inputRequest)

Create an invoice from a billing schedule.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RevenueAsyncRepresentation generateInvoices(ConnectApi.InvoiceInputRepresentation inputRequest)`

```
ConnectApi.Billing, generateInvoices, [ConnectApi.InvoiceInputRepresentation], ConnectApi.RevenueAsyncRepresentation
```

#### Parameters

**inputRequest**

: Type: [ConnectApi.InvoiceInputRepresentation](./apex_connectapi_input_invoice.htm.md)

: Input representation of the details of the billing schedule.

#### Return Value

Type: [ConnectApi.RevenueAsyncRepresentation](./apex_connectapi_output_revenue_async.htm.md)

#### Usage

You need the Generate Invoices From Billing Schedule API permission
        set to use this method.

This method creates one billing period item for each unbilled
        period between the billing schedule's next billing date and the invoice's target date.
        Additionally, one invoice line is created for each billing period item. This method creates
        up to six billing periods per request.

### recoverBillingSchedules(inputRequest)

Recover the latest generated invoice associated with the billing schedules in the Error
    or Processing status.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.BillingScheduleRecoveryResults recoverBillingSchedules(ConnectApi.BillingScheduleRecoveryInputRequest inputRequest)`

```
ConnectApi.Billing, recoverBillingSchedules, [ConnectApi.BillingScheduleRecoveryInputRequest], ConnectApi.BillingScheduleRecoveryResults
```

#### Parameters

**inputRequest**

: Type: [ConnectApi.BillingScheduleRecoveryInputRequest](./apex_connectapi_input_billing_schedule_recovery.htm.md)

: Input representation of the details of the billing schedules to recover the associated
            invoice.

#### Return Value

Type: [ConnectApi.BillingScheduleRecoveryResults](./apex_connectapi_output_billing_schedule_recovery_list_output.htm.md)

#### Usage

      
      

You need the Manage Errors Using Invoice Error Recovery API permission set to use this
        method.

      

Billing schedules include critical details such as the amount to be billed, next billing
        date, and status. An invoice can be associated with one or more billing schedules. When an
        invoice is generated or posted, the billing schedules are updated to reflect the accurate
        state of the invoice. The billing schedules associated with an invoice are marked in the
          `Error` status if any of the invoicing processes have
        errors. Use this method to recover the invoice associated with the billing schedules in the
          `Error` or `Processing` status.

    

### voidPostedCreditMemo(VoidPostedCreditMemoInput, creditMemoId)

Invoke the Void Posted Credit Memo API by providing a credit memo ID.

#### API Version

66.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.VoidPostedCreditMemoOutputRepresentation voidPostedCreditMemo(ConnectApi.VoidPostedCreditMemoInputRepresentation VoidPostedCreditMemoInput, String creditMemoId)`

```
ConnectApi.Billing, voidPostedCreditMemo, [ConnectApi.VoidPostedCreditMemoInputRepresentation, String], ConnectApi.VoidPostedCreditMemoOutputRepresentation
```

#### Parameters

**VoidPostedCreditMemoInput**

: Type: [`ConnectApi.VoidPostedCreditMemoInputRepresentation`](./apex_connectapi_input_void_posted_credit_memo.htm.md)

: Input representation of the details of a credit memo to be voided.

**creditMemoId**

: Type: String

: Required. ID of the credit memo record in posted status to be voided.

#### Return Value

Type: [`ConnectApi.VoidPostedCreditMemoOutputRepresentation`](./apex_connectapi_output_void_posted_credit_memo_output.htm.md)

### voidPostedInvoice(invoiceId)

Void a posted invoice to rebill the customer, if necessary.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RevenueAsyncRepresentation
          voidPostedInvoice(String invoiceId)`

#### Parameters

**invoiceId**

: Type: String

: ID of the posted invoice to be voided.

#### Return Value

Type: [`ConnectApi.RevenueAsyncRepresentation`](./apex_connectapi_output_revenue_async.htm.md)

#### Usage

You need the Void a Posted Invoice API permission set to use this
        method.

This method changes the invoice status from `Posted` to `Void In Progress`. The invoice
        remains in the `Void In Progress` status until the credit
        is applied and financial fields are recalculated on the invoice’s related billing period
        items and billing schedule. The invoice status changes to `Voided` after all recalculations are completed.

Keep these considerations
        in mind when you use this method.

      
        
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

=== ARTICLE: apex_ConnectAPI_CreditMemoApply_static_methods.htm ===
---
page_id: apex_ConnectAPI_CreditMemoApply_static_methods.htm
title: CreditMemoApply Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_CreditMemoApply_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# CreditMemoApply Class

 
 
 
Manage credit memo applications by using the CreditMemoApply class.

  

## Namespace

   
   

ConnectApi

  

 

 

## CreditMemoApply Methods

 These methods are for `CreditMemoApply`. All
  methods are static.

 

- 
**[applyCreditMemos(CreditMemoApplyInput, creditMemoId)](./apex_ConnectAPI_CreditMemoApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoApply_applyCreditMemos_1)**  

Adjust or correct already issued invoices by applying an existing credit memo to an     invoice.

- 
**[unapplyCreditMemos(CreditMemoUnapplyInput, creditMemoInvApplicationId)](./apex_ConnectAPI_CreditMemoApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoApply_unapplyCreditMemos_1)**  

Unapply a credit memo from an invoice and return the invoice and the credit memo to their     pre-application states.

### applyCreditMemos(CreditMemoApplyInput, creditMemoId)

Adjust or correct already issued invoices by applying an existing credit memo to an
    invoice.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.ApplyCreditResults applyCreditMemos(ConnectApi.CreditMemoApplyInputRequest CreditMemoApplyInput, String creditMemoId)`

#### Parameters

**CreditMemoApplyInput**

: Type: [ConnectApi.CreditMemoApplyInputRequest](./apex_connectapi_input_credit_memo_apply.htm.md)

: Input representation of the request to apply a credit memo to an invoice.

**creditMemoId**

: Type: String

: ID of the credit memo record.

#### Return Value

Type: [ConnectApi.ApplyCreditResults](./apex_connectapi_output_credit_memo_apply_list_output.htm.md)

#### Usage

      
      

Specify the credit memo ID and the amounts to be applied, with the total of all applied
        amounts not exceeding the credit memo's balance.

      

The credit amount for each invoice can’t surpass the original charge or adjustment amount,
        and the overall credit amount must not exceed the invoice's outstanding balance. The
        exceptions include any taxes calculated by an external service.

      

For example, your organization sold 10 tablets at US$500 each, totaling $5000, to a vendor
        who later reported that 6 tablets were defective. Using this method, your accounts
        receivable team creates a $3000 credit memo and applies this credit to the original
        invoice.

    

### unapplyCreditMemos(CreditMemoUnapplyInput, creditMemoInvApplicationId)

Unapply a credit memo from an invoice and return the invoice and the credit memo to their
    pre-application states.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.UnapplyCreditResult unapplyCreditMemos(ConnectApi.CreditMemoUnapplyInputRequest CreditMemoUnapplyInput, String creditMemoInvApplicationId)`

#### Parameters

**CreditMemoUnapplyInput**

: Type: [ConnectApi.CreditMemoUnapplyInputRequest](./apex_connectapi_input_credit_memo_unapply.htm.md)

: Input representation of the request to unapply a credit memo from an invoice.

**creditMemoInvApplicationId**

: Type: String

: ID of the credit memo invoice application.

#### Return Value

Type: [ConnectApi.UnapplyCreditResult](./apex_connectapi_output_credit_memo_unapply_output.htm.md)

#### Usage

      

Use this method if an error occurred when a credit is issued. For example, if an incorrect
        credit memo is applied to an invoice, or if a credit memo is created for an incorrect
        amount, use this method to unapply the credit memo.

=== ARTICLE: apex_ConnectAPI_CreditMemoLineApply_static_methods.htm ===
---
page_id: apex_ConnectAPI_CreditMemoLineApply_static_methods.htm
title: CreditMemoLineApply Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_CreditMemoLineApply_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# CreditMemoLineApply Class

 
 
 
Manage credit memo line applications by using the CreditMemoLineApply class.

  

## Namespace

   
   

ConnectApi

  

 

 

## CreditMemoLineApply Methods

 These methods are for `CreditMemoLineApply`. All
  methods are static.

 

- 
**[applyCreditMemoLines(CreditMemoLineApplyInput, creditMemoLineId)](./apex_ConnectAPI_CreditMemoLineApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoLineApply_applyCreditMemoLines_1)**  

Adjust or correct already issued invoices by applying an existing credit memo line to an     invoice line.

- 
**[unapplyCreditMemoLines(CreditMemoLineUnapplyInput, creditMemoLineInvoiceLineId)](./apex_ConnectAPI_CreditMemoLineApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoLineApply_unapplyCreditMemoLines_1)**  

Unapply a credit memo line from an invoice line and return the invoice line and the     credit memo line to their pre-application states.

### applyCreditMemoLines(CreditMemoLineApplyInput, creditMemoLineId)

Adjust or correct already issued invoices by applying an existing credit memo line to an
    invoice line.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.CreditMemoLineAppliedResponse applyCreditMemoLines(ConnectApi.CreditMemoLineApplyInput CreditMemoLineApplyInput, String creditMemoLineId)`

#### Parameters

**CreditMemoLineApplyInput**

: Type: [ConnectApi.CreditMemoLineApplyInput](./apex_connectapi_input_credit_memo_line_apply.htm.md)

: Input representation of the details of the request to apply a credit memo line to an invoice
            line.

**creditMemoLineId**

: Type: String

: ID of the credit memo line record.

#### Return Value

Type: [ConnectApi.CreditMemoLineAppliedResponse](./apex_connectapi_output_credit_memo_line_applied.htm.md)

#### Usage

You need the Credit Memo Operations User permission set to use this method.

### unapplyCreditMemoLines(CreditMemoLineUnapplyInput, creditMemoLineInvoiceLineId)

Unapply a credit memo line from an invoice line and return the invoice line and the
    credit memo line to their pre-application states.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.CreditMemoLineUnappliedResponse unapplyCreditMemoLines(ConnectApi.CreditMemoLineUnapplyInput CreditMemoLineUnapplyInput, String creditMemoLineInvoiceLineId)`

#### Parameters

**CreditMemoLineUnapplyInput**

: Type: [ConnectApi.CreditMemoLineUnapplyInput](./apex_connectapi_input_credit_memo_line_unapply.htm.md)

: Input representation of the details of the request to unapply a credit memo line from an invoice
            line.

**creditMemoLineInvoiceLineId**

: Type: String

: ID of the credit memo line invoice line record.

#### Return Value

Type: [ConnectApi.CreditMemoLineUnappliedResponse](./apex_connectapi_output_credit_memo_line_unapplied.htm.md)

#### Usage

You need the Credit Memo Operations User permission set to use this method.

=== ARTICLE: apex_ConnectAPI_HarmonizeBilling_static_methods.htm ===
---
page_id: apex_ConnectAPI_HarmonizeBilling_static_methods.htm
title: HarmonizeBilling Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_HarmonizeBilling_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# HarmonizeBilling Class

 
 
 
Update the status of the invoice from Draft to Posted by using the HarmonizeBilling
  class.

  

## Namespace

   
   

ConnectApi

  

 

 

## HarmonizeBilling Methods

 These methods are for `HarmonizeBilling`. All
  methods are static.

 

- 
**[postDraftInvoices(inputRequest)](./apex_ConnectAPI_HarmonizeBilling_static_methods.htm.md#apex_ConnectAPI_HarmonizeBilling_postDraftInvoices_1)**  

Update the status of the invoice from Draft to Posted.

### postDraftInvoices(inputRequest)

Update the status of the invoice from Draft to Posted.

#### API Version

62.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RevenueAsyncRepresentation postDraftInvoices(ConnectApi.InvoiceDraftToPostedInputRequest inputRequest)`

#### Parameters

**inputRequest**

: Type: [`ConnectApi.InvoiceDraftToPostedInputRequest`](./apex_connectapi_input_invoice_draft_to_posted.htm.md)

: Input representation of the details of the draft invoice that’s posted.

#### Return Value

Type: [`ConnectApi.RevenueAsyncRepresentation`](./apex_connectapi_output_revenue_async.htm.md)

#### Usage

You need the Billing Operations User permission set to use this
        method.

This method calls an external tax engine to calculate taxes for the draft
        invoice, posts the invoice, and updates the related billing schedules and billing
        periods.

=== ARTICLE: apex_ConnectAPI_PaymentsBilling_static_methods.htm ===
---
page_id: apex_ConnectAPI_PaymentsBilling_static_methods.htm
title: PaymentsBilling Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_PaymentsBilling_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# PaymentsBilling Class

 
 
 
Use the PaymentsBilling class to allocate the balance of a payment to reduce the balance
  of an invoice. Additionally, revert the application of a payment line from an invoice.

  

## Namespace

   
   

ConnectApi

  

 

 

## PaymentsBilling Methods

 These methods are for `PaymentsBilling`. All
  methods are static.

 

- 
**[applyPaymentLine(PaymentLineApplyInput, paymentId)](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_applyPaymentLine_1)**  

Allocate the balance of a payment to reduce the balance of an invoice. The response     includes an ID of the payment line invoice that represents the payment balance allocated against     the invoice.

- 
**[applyRefundLine(RefundLineApplyInput, refundId)](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_applyRefundLine_1)**  

Make a refund transaction against a payment.

- 
**[unapplyPaymentLine(PaymentLineUnapplyInput, paymentId, paymentLineId)](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_unapplyPaymentLine_1)**  

Revert the application of a payment line from an invoice, and return the payment and     invoices to their pre-application state. Use this method if you need to correct an input during     the payment application process.

- 
**[unapplyPaymentLine(PaymentLineUnapplyInput, paymentLineId)](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_unapplyPaymentLine_2)**  

Revert the application of a payment line from an invoice, and return the payment and     invoices to their pre-application state. Use this method if you need to correct an input during     the payment application process.

### applyPaymentLine(PaymentLineApplyInput, paymentId)

Allocate the balance of a payment to reduce the balance of an invoice. The response
    includes an ID of the payment line invoice that represents the payment balance allocated against
    the invoice.

#### API Version

64.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.PaymentLineApplyResponse applyPaymentLine(ConnectApi.PaymentLineApplyRequest PaymentLineApplyInput, String paymentId)`

#### Parameters

**PaymentLineApplyInput**

: Type: [`ConnectApi.PaymentLineApplyRequest`](./apex_connectapi_input_payment_line_apply.htm.md)

: Input representation of the payment line details.

**paymentId**

: Type: String

: 

ID of the payment record.

#### Return Value

Type: [`ConnectApi.PaymentLineApplyResponse`](./apex_connectapi_output_payment_line_apply_output.htm.md)

#### Usage

Use the Commerce Payments APIs to send your payment and
        refund details to external payment gateways for processing against a customer's bank. See
          [Commerce Payments resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm)
        to check the APIs for payment gateways, payment captures, and payment authorizations.

### applyRefundLine(RefundLineApplyInput, refundId)

Make a refund transaction against a payment.

#### API Version

64.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.RefundLineApplyResponse applyRefundLine(ConnectApi.RefundLineApplyRequest RefundLineApplyInput, String refundId)`

#### Parameters

**RefundLineApplyInput**

: Type: [`ConnectApi.RefundLineApplyRequest`](./apex_connectapi_input_refund_line_apply.htm.md)

: Input representation of the details of a transaction refund request. This representation
            outlines the properties of a refund, including the refund amount and ID of the payment
            or credit memo record that the refund is applied to.

**refundId**

: Type: String

: ID of the refund record.

#### Return Value

Type: [`ConnectApi.RefundLineApplyResponse`](./apex_connectapi_output_refund_line_apply_output.htm.md)

### unapplyPaymentLine(PaymentLineUnapplyInput, paymentId, paymentLineId)

Revert the application of a payment line from an invoice, and return the payment and
    invoices to their pre-application state. Use this method if you need to correct an input during
    the payment application process.

#### API Version

64.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.PaymentLineUnapplyResponse unapplyPaymentLine(ConnectApi.PaymentLineUnapplyRequest PaymentLineUnapplyInput, String paymentId, String paymentLineId)`

#### Parameters

**PaymentLineUnapplyInput**

: Type: [`ConnectApi.PaymentLineUnapplyRequest`](./apex_connectapi_input_payment_line_unapply.htm.md)

: Input representation of the payment line details.

**paymentId**

: Type: String

: 

ID of the payment record.

**paymentLineId**

: Type: String

: 

ID of the payment line record.

#### Return Value

Type: [`ConnectApi.PaymentLineUnapplyResponse`](./apex_connectapi_output_payment_line_unapply_output.htm.md)

#### Usage

      

Use the Commerce Payments APIs to send your payment and
        refund details to external payment gateways for processing against a customer's bank. See
          [Commerce Payments resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm)
        to check the APIs for payment gateways, payment captures, and payment authorizations.

### unapplyPaymentLine(PaymentLineUnapplyInput, paymentLineId)

Revert the application of a payment line from an invoice, and return the payment and
    invoices to their pre-application state. Use this method if you need to correct an input during
    the payment application process.

#### API Version

64.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.PaymentLineUnapplyResponse unapplyPaymentLine(ConnectApi.PaymentLineUnapplyRequest PaymentLineUnapplyInput, String paymentLineId)`

#### Parameters

**PaymentLineUnapplyInput**

: Type: [`ConnectApi.PaymentLineUnapplyRequest`](./apex_connectapi_input_payment_line_unapply.htm.md)

          
: Input representation of the payment line details.

**paymentLineId**

: Type: String

: 

ID of the payment line record.

#### Return Value

Type: [`ConnectApi.PaymentLineUnapplyResponse`](./apex_connectapi_output_payment_line_unapply_output.htm.md)

#### Usage

      

Use the Commerce Payments APIs to send your payment and
        refund details to external payment gateways for processing against a customer's bank. See
          [Commerce Payments resources](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/connect_resources_payments.htm)
        to check the APIs for payment gateways, payment captures, and payment authorizations.

=== ARTICLE: apex_ConnectAPI_SequencingWithoutAura_static_methods.htm ===
---
page_id: apex_ConnectAPI_SequencingWithoutAura_static_methods.htm
title: SequencingWithoutAura Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_ConnectAPI_SequencingWithoutAura_static_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

 

# SequencingWithoutAura Class

 
 
 
Manage invoice sequencing processes by using the SequencingWithoutAura
  class.

  

## Namespace

   
   

ConnectApi

  

 

 

## SequencingWithoutAura Methods

 These methods are for `SequencingWithoutAura`. All
  methods are static.

 

- 
**[reconcileSequences(sequenceGapReconciliationInputRepresentation)](./apex_ConnectAPI_SequencingWithoutAura_static_methods.htm.md#apex_ConnectAPI_SequencingWithoutAura_reconcileSequences_1)**  

Restore a missing sequence value identified by using this API in gapless-enabled     sequences. This sequence value can be used later in the subsequent sequence policy numbering,     ensuring there are no gaps.

- 
**[sequenceAssignment(sequencesAssignmentInputRepresentation)](./apex_ConnectAPI_SequencingWithoutAura_static_methods.htm.md#apex_ConnectAPI_SequencingWithoutAura_sequenceAssignment_1)**  

Assign sequence pattern values to objects based on the configured sequence     policy.

### reconcileSequences(sequenceGapReconciliationInputRepresentation)

Restore a missing sequence value identified by using this API in gapless-enabled
    sequences. This sequence value can be used later in the subsequent sequence policy numbering,
    ensuring there are no gaps.

#### API Version

65.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.sequenceGapReconciliationOutputRepresentation reconcileSequences(ConnectApi.sequenceGapReconciliationInputRepresentation sequenceGapReconciliationInputRepresentation)`

#### Parameters

**sequenceGapReconciliationInputRepresentation**

: Type: [`ConnectApi.SequenceGapReconciliationInputRepresentation`](./apex_connectapi_input_sequence_gap_reconciliation.htm.md)

: The details of the input used to identify and reconcile gaps in sequence values based on the
            sequence policy or target object.

#### Return Value

Type: [`ConnectApi.SequenceGapReconciliationOutputRepresentation`](./apex_connectapi_output_sequence_gap_reconciliation_output.htm.md)

#### Usage

You need the Billing Admin permission set to use this method.

### sequenceAssignment(sequencesAssignmentInputRepresentation)

Assign sequence pattern values to objects based on the configured sequence
    policy.

#### API Version

65.0

#### Requires Chatter

No

#### Signature

`public static ConnectApi.SequencesAssignmentOutputRepresentation sequenceAssignment(ConnectApi.SequencesAssignmentInputRepresentation sequencesAssignmentInputRepresentation)`

#### Parameters

**sequencesAssignmentInputRepresentation**

: Type: [`ConnectApi.SequencesAssignmentInputRepresentation`](./apex_connectapi_input_sequences_assignment.htm.md)

: The details of the target objects to which the sequence pattern values are assigned.

#### Return Value

Type: [`ConnectApi.SequencesAssignmentOutputRepresentation`](./apex_connectapi_output_sequences_assignment_output.htm.md)

#### Usage

You need the Billing Admin permission set to use this method.

=== ARTICLE: apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm ===
---
page_id: apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm
title: WriteOffInvoiceInput Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_InvoiceWriteOff.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# WriteOffInvoiceInput Class

Contains invoice details that are used for the request to write off an
    invoice.

## Namespace

[InvoiceWriteOff](./apex_namespace_InvoiceWriteOff.htm.md)

- 
**[WriteOffInvoiceInput Constructors](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_constructors)**  

Learn more about the constructors available with the WriteOffInvoiceInput     class.

- 
**[WriteOffInvoiceInput Properties](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_properties)**  

Learn more about the properties available with the WriteOffInvoiceInput     class.

  

## WriteOffInvoiceInput Constructors

  
  
  
Learn more about the constructors available with the WriteOffInvoiceInput
    class.

    
      

The `WriteOffInvoiceInput` class includes these
        constructors.

    

- 
**[WriteOffInvoiceInput(invoiceId, reasonCode, reason)](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_ctor)**  

Initializes the WriteOffInvoiceInput class that stores the invoice details and reason for     writing off invoices.

- 
**[WriteOffInvoiceInput()](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_ctor_2)**  

Initializes the WriteOffInvoiceInput class.

### WriteOffInvoiceInput(invoiceId, reasonCode, reason)

Initializes the WriteOffInvoiceInput class that stores the invoice details and reason for
    writing off invoices.

#### Signature

`public WriteOffInvoiceInput(String invoiceId, String reasonCode, String reason)`

#### Parameters

**invoiceId**

: Type: String

: 

ID of the invoice record that you want to write off.

**reasonCode**

: Type: String

: 

Code that categorizes the write-off reason. For example, if the reason for the
                        invoice write-off is a disputed amount, the reason code can be Disputed
                        Amount (DA).

**reason**

: Type: String

: 

Reason for writing off invoices.

### WriteOffInvoiceInput()

Initializes the WriteOffInvoiceInput class.

#### Signature

`public WriteOffInvoiceInput()`

  

## WriteOffInvoiceInput Properties

  
  
  
Learn more about the properties available with the WriteOffInvoiceInput
    class.

    
      

The `WriteOffInvoiceInput` class includes these
        properties.

    

- 
**[invoiceId](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_invoiceId)**  

Sets the ID of the invoice record that must be written off.

- 
**[reason](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_reason)**  

Sets the reason for writing off invoices.

- 
**[reasonCode](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInput_reasonCode)**  

Sets the code that categorizes the write-off reason.

### invoiceId

Sets the ID of the invoice record that must be written off.

#### Signature

`public String invoiceId {get; set;}`

#### Property Value

Type: String

### reason

Sets the reason for writing off invoices.

#### Signature

`public String reason {get; set;}`

#### Property Value

Type: String

### reasonCode

Sets the code that categorizes the write-off reason.

#### Signature

`public String reasonCode {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm ===
---
page_id: apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm
title: WriteOffInvoiceInputList Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_InvoiceWriteOff.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# WriteOffInvoiceInputList Class

Contains invoice details to write off a list of posted invoices.

## Namespace

[InvoiceWriteOff](./apex_namespace_InvoiceWriteOff.htm.md)

- 
**[WriteOffInvoiceInputList Constructors](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInputList_constructors)**  

Learn more about the constructors available with the WriteOffInvoiceInputList     class.

- 
**[WriteOffInvoiceInputList Properties](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInputList_properties)**  

Learn more about the properties available with the WriteOffInvoiceInputList     class.

  

## WriteOffInvoiceInputList Constructors

  
  
  
Learn more about the constructors available with the WriteOffInvoiceInputList
    class.

    
      

The `WriteOffInvoiceInputList` class includes these
        constructors.

    

- 
**[WriteOffInvoiceInputList(writeOffInvoiceInputList)](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInputList_ctor)**  

Initializes the WriteOffInvoiceInputList class that stores the details of invoices that     you want to write off.

- 
**[WriteOffInvoiceInputList()](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInputList_ctor_2)**  

Initializes the WriteOffInvoiceInputList class.

### WriteOffInvoiceInputList(writeOffInvoiceInputList)

Initializes the WriteOffInvoiceInputList class that stores the details of invoices that
    you want to write off.

#### Signature

`public WriteOffInvoiceInputList(List<InvoiceWriteOff.WriteOffInvoiceInput> writeOffInvoiceInputList)`

#### Parameters

**writeOffInvoiceInputList**

: Type: List<I[nvoiceWriteOff.WriteOffInvoiceInput](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceInput)>

: Input representation of the request to write off a list of posted invoices.

### WriteOffInvoiceInputList()

Initializes the WriteOffInvoiceInputList class.

#### Signature

`public WriteOffInvoiceInputList()`

  

## WriteOffInvoiceInputList Properties

  
  
  
Learn more about the properties available with the WriteOffInvoiceInputList
    class.

    
      

The `WriteOffInvoiceInputList` class includes these
        properties.

    

- 
**[writeOffInvoiceInputList](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceInputList_writeOffInvoiceInputList)**  

Input representation of the request to write off a list of posted invoices.

### writeOffInvoiceInputList

Input representation of the request to write off a list of posted invoices.

#### Signature

`public List<InvoiceWriteOff.WriteOffInvoiceInput> writeOffInvoiceInputList {get; set;}`

#### Property Value

Type: List<[nvoiceWriteOff.WriteOffInvoiceInput](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceInput)>

=== ARTICLE: apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm ===
---
page_id: apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm
title: WriteOffInvoiceResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_InvoiceWriteOff.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# WriteOffInvoiceResponse Class

Contains properties to store the response details to the request to write off a posted
    invoice.

## Namespace

[InvoiceWriteOff](./apex_namespace_InvoiceWriteOff.htm.md)

- 
**[WriteOffInvoiceResponse Constructors](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_constructors)**  

Learn more about the constructors available with the WriteOffInvoiceResponse     class.

- 
**[WriteOffInvoiceResponse Properties](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_properties)**  

Learn more about the properties available with the WriteOffInvoiceResponse     class.

  

## WriteOffInvoiceResponse Constructors

  
  
  
Learn more about the constructors available with the WriteOffInvoiceResponse
    class.

    
      

The `WriteOffInvoiceResponse` class includes these
        constructors.

    

- 
**[WriteOffInvoiceResponse(errors, invoiceId, requestIdentifier, success)](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_ctor)**  

Initializes the WriteOffInvoiceResponse class that stores the response details to the     request to write off a posted invoice.

### WriteOffInvoiceResponse(errors, invoiceId, requestIdentifier, success)

Initializes the WriteOffInvoiceResponse class that stores the response details to the
    request to write off a posted invoice.

#### Signature

`public WriteOffInvoiceResponse(InvoiceWriteOff.WriteOffInvoiceResponseError errors, String invoiceId, String requestIdentifier, Boolean success)`

#### Parameters

**errors**

: Type: [InvoiceWriteOff.WriteOffInvoiceResponseError](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError)

: 

If the request fails, this property contains a list of
                  errors.

**invoiceId**

: Type: String

: 

ID of the invoice record that's written off.

**requestIdentifier**

: Type: String

: 

If the request is successful, this property contains an asynchronous API
                  request identifier for an invoice ID.

**success**

: Type: Boolean

: 

Indicates whether the invoice write-off request was successful
                    (`true`) or not (`false`).

  

## WriteOffInvoiceResponse Properties

  
  
  
Learn more about the properties available with the WriteOffInvoiceResponse
    class.

    
      

The `WriteOffInvoiceResponse` class includes these
        properties.

    

- 
**[errors](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_errors)**  

Get the list of errors if the request to write off posted invoices fails.

- 
**[invoiceId](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_invoiceId)**  

Get the ID of the invoice record that's written off.

- 
**[requestIdentifier](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_requestIdentifier)**  

Get the identifier of the asynchronous API request for an invoice ID if the request is     successful.

- 
**[success](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponse_success)**  

Get the request status of the invoice write-off request.

### errors

Get the list of errors if the request to write off posted invoices fails.

#### Signature

`public InvoiceWriteOff.WriteOffInvoiceResponseError errors {get; set;}`

#### Property Value

Type: [InvoiceWriteOff.WriteOffInvoiceResponseError](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError)

### invoiceId

  
Get the ID of the invoice record that's written off.

#### Signature

`public String invoiceId {get; set;}`

#### Property Value

Type: String

### requestIdentifier

Get the identifier of the asynchronous API request for an invoice ID if the request is
    successful.

#### Signature

`public String requestIdentifier {get; set;}`

#### Property Value

Type: String

### success

Get the request status of the invoice write-off request.

#### Signature

`public Boolean success {get; set;}`

#### Property Value

Type: Boolean

=== ARTICLE: apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm ===
---
page_id: apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm
title: WriteOffInvoiceResponseError Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_InvoiceWriteOff.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# WriteOffInvoiceResponseError Class

Contains properties to store the error response that's associated with a request to write
    off a posted invoice.

## Namespace

[InvoiceWriteOff](./apex_namespace_InvoiceWriteOff.htm.md)

- 
**[WriteOffInvoiceResponseError Constructors](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseError_constructors)**  

Learn more about the constructors available with the WriteOffInvoiceResponseError     class.

- 
**[WriteOffInvoiceResponseError Properties](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseError_properties)**  

Learn more about the properties available with the WriteOffInvoiceResponseError     class.

  

## WriteOffInvoiceResponseError Constructors

  
  
  
Learn more about the constructors available with the WriteOffInvoiceResponseError
    class.

    
      

The `WriteOffInvoiceResponseError` class includes these
        constructors.

    

- 
**[WriteOffInvoiceResponseError(errorCode, errorMessage)](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseError_ctor)**  

Initializes the WriteOffInvoiceResponseError class that stores the error response that's     associated with a request to write off a posted invoice.

### WriteOffInvoiceResponseError(errorCode, errorMessage)

Initializes the WriteOffInvoiceResponseError class that stores the error response that's
    associated with a request to write off a posted invoice.

#### Signature

`public WriteOffInvoiceResponseError(String errorCode, String errorMessage)`

#### Parameters

**errorCode**

: Type: String

: 

Code that represents the error.

**errorMessage**

: Type: String

: 

Message that describes the error.

## WriteOffInvoiceResponseError Properties

  
Learn more about the properties available with the WriteOffInvoiceResponseError
    class.

    
      

The `WriteOffInvoiceResponseError` class includes these
        properties.

    

- 
**[errorCode](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseError_errorCode)**  

Get the error code details.

- 
**[errorMessage](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseError_errorMessage)**  

Get the error message details.

### errorCode

Get the error code details.

#### Signature

`public String errorCode {get; set;}`

#### Property Value

Type: String

### errorMessage

Get the error message details.

#### Signature

`public String errorMessage {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm ===
---
page_id: apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm
title: WriteOffInvoiceResponseList Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_InvoiceWriteOff.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# WriteOffInvoiceResponseList Class

Contains properties to store the response details of the list of invoices that are
    written off.

## Namespace

[InvoiceWriteOff](./apex_namespace_InvoiceWriteOff.htm.md)

- 
**[WriteOffInvoiceResponseList Constructors](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseList_constructors)**  

Learn more about the constructors available with the WriteOffInvoiceResponseList     class.

- 
**[WriteOffInvoiceResponseList Properties](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseList_properties)**  

Learn more about the properties available with the WriteOffInvoiceResponseList     class.

  

## WriteOffInvoiceResponseList Constructors

  
  
  
Learn more about the constructors available with the WriteOffInvoiceResponseList
    class.

    
      

The `WriteOffInvoiceResponseList` class includes these
        constructors.

    

- 
**[WriteOffInvoiceResponseList(writeOffInvoiceResponseList)](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseList_ctor)**  

Initializes the WriteOffInvoiceResponseList class that stores the response details of the     list of invoices that are written off.

- 
**[WriteOffInvoiceResponseList()](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseList_ctor_2)**  

Initializes the WriteOffInvoiceResponseList class.

### WriteOffInvoiceResponseList(writeOffInvoiceResponseList)

Initializes the WriteOffInvoiceResponseList class that stores the response details of the
    list of invoices that are written off.

#### Signature

`public WriteOffInvoiceResponseList(List<InvoiceWriteOff.WriteOffInvoiceResponse> writeOffInvoiceResponseList)`

#### Parameters

**writeOffInvoiceResponseList**

: Type: List<[InvoiceWriteOff.WriteOffInvoiceResponse](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponse)>

: 

Details of the invoices for which the write-off process is initiated.

### WriteOffInvoiceResponseList()

Initializes the WriteOffInvoiceResponseList class.

#### Signature

`public WriteOffInvoiceResponseList()`

  

## WriteOffInvoiceResponseList Properties

  
  
  
Learn more about the properties available with the WriteOffInvoiceResponseList
    class.

    
      

The `WriteOffInvoiceResponseList` class includes these
        properties.

    

- 
**[writeOffInvoiceResponseList](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_InvoiceWriteOff_WriteOffInvoiceResponseList_writeOffInvoiceResponseList)**  

Get the details of the invoices for which the write-off posted invoice process is     initiated.

### writeOffInvoiceResponseList

Get the details of the invoices for which the write-off posted invoice process is
    initiated.

#### Signature

`public List<InvoiceWriteOff.WriteOffInvoiceResponse> writeOffInvoiceResponseList {get; set;}`

#### Property Value

Type: List<[InvoiceWriteOff.WriteOffInvoiceResponse](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponse)>

=== ARTICLE: apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm ===
---
page_id: apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm
title: CreditLineRequestInputRepresentations Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_IssueCreditMemo.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditLineRequestInputRepresentations Class

Represents a single line-level credit request. Specifies the invoice line to credit, the amount to apply, and an optional description.

## Namespace

[IssueCreditMemo](./apex_namespace_IssueCreditMemo.htm.md)

- 
**[CreditLineRequestInputRepresentations Constructors](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_constructors)**  

- 
**[CreditLineRequestInputRepresentations Properties](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_properties)**  

  

## CreditLineRequestInputRepresentations Constructors

  
  
    
      

The `CreditLineRequestInputRepresentations` class includes
        these constructors.

    

    
  

- 
**[CreditLineRequestInputRepresentations(invoiceLineId, creditLineAmount, description)](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_ctor)**  

Creates a credit line request for the specified invoice line, amount, and description.

- 
**[CreditLineRequestInputRepresentations()](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_ctor_2)**  

Creates an empty credit line request.

### CreditLineRequestInputRepresentations(invoiceLineId, creditLineAmount, description)

Creates a credit line request for the specified invoice line, amount, and description.

#### Signature

`public CreditLineRequestInputRepresentations(String invoiceLineId, Double creditLineAmount, String description)`

#### Parameters

**invoiceLineId**

: Type: String

: The ID of the invoice line to which the credit applies.

**creditLineAmount**

: Type: Double

: The monetary amount to credit for this invoice line.

**description**

: Type: String

: Optional description or reason for the credit line.

### CreditLineRequestInputRepresentations()

Creates an empty credit line request.

#### Signature

`public CreditLineRequestInputRepresentations()`

  

## CreditLineRequestInputRepresentations Properties

  
  
    
      

The `CreditLineRequestInputRepresentations` class includes
        these properties.

    

    
  

- 
**[creditLineAmount](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_creditLineAmount)**  

The monetary amount to credit for this invoice line.

- 
**[description](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_description)**  

Optional description or reason for the credit line.

- 
**[invoiceLineId](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditLineRequestInputRepresentations_invoiceLineId)**  

The ID of the invoice line to which the credit applies.

### creditLineAmount

The monetary amount to credit for this invoice line.

#### Signature

`public Double creditLineAmount {get; set;}`

#### Property Value

Type: Double

### description

Optional description or reason for the credit line.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### invoiceLineId

The ID of the invoice line to which the credit applies.

#### Signature

`public String invoiceLineId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm ===
---
page_id: apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm
title: CreditRequestInputRepresentations Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_IssueCreditMemo.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditRequestInputRepresentations Class

Represents a credit request for an invoice. Contains invoice and dispute identifiers, total credit amount, category, and line-level credit details for issuing a credit memo.

## Namespace

[IssueCreditMemo](./apex_namespace_IssueCreditMemo.htm.md)

- 
**[CreditRequestInputRepresentations Constructors](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_constructors)**  

- 
**[CreditRequestInputRepresentations Properties](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_properties)**  

  

## CreditRequestInputRepresentations Constructors

  
  
    
      

The `CreditRequestInputRepresentations` class includes
        these constructors.

    

    
  

- 
**[CreditRequestInputRepresentations(invoiceId, creditAmount, description, disputeId, category, creditLineRequestInputRepresentations)](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_ctor)**  

Creates a credit request with the given invoice, amount, description, dispute, category, and line-level credit details.

- 
**[CreditRequestInputRepresentations(invoiceId, creditAmount, description, creditLineRequestInputRepresentations)](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_ctor_2)**  

Creates a credit request with the given invoice, amount, description, and line-level credit details.

- 
**[CreditRequestInputRepresentations()](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_ctor_3)**  

Creates an empty credit request.

### CreditRequestInputRepresentations(invoiceId, creditAmount, description, disputeId, category, creditLineRequestInputRepresentations)

Creates a credit request with the given invoice, amount, description, dispute, category, and line-level credit details.

#### Signature

`public CreditRequestInputRepresentations(String invoiceId, Double creditAmount, String description, String disputeId, String category, List<IssueCreditMemo.CreditLineRequestInputRepresentations> creditLineRequestInputRepresentations)`

#### Parameters

**invoiceId**

: Type: String

: ID of the invoice to credit.

**creditAmount**

: Type: Double

: Total credit amount to apply to the invoice.

**description**

: Type: String

: Optional description for the credit request.

**disputeId**

: Type: String

: ID of the billing dispute associated with this credit request.

**category**

: Type: String

: Category of the credit memo.

**creditLineRequestInputRepresentations**

: Type: List<[IssueCreditMemo.CreditLineRequestInputRepresentations](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations)>

: List of line-level credit requests for this invoice.

### CreditRequestInputRepresentations(invoiceId, creditAmount, description, creditLineRequestInputRepresentations)

Creates a credit request with the given invoice, amount, description, and line-level credit details.

#### Signature

`public CreditRequestInputRepresentations(String invoiceId, Double creditAmount, String description, List<IssueCreditMemo.CreditLineRequestInputRepresentations> creditLineRequestInputRepresentations)`

#### Parameters

**invoiceId**

: Type: String

: ID of the invoice to credit.

**creditAmount**

: Type: Double

: Total credit amount to apply to the invoice.

**description**

: Type: String

: Optional description for the credit request.

**creditLineRequestInputRepresentations**

: Type: List<[IssueCreditMemo.CreditLineRequestInputRepresentations](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations)>

: List of line-level credit requests for this invoice.

### CreditRequestInputRepresentations()

Creates an empty credit request.

#### Signature

`public CreditRequestInputRepresentations()`

  

## CreditRequestInputRepresentations Properties

  
  
    
      

The `CreditRequestInputRepresentations` class includes
        these properties.

    

    
  

- 
**[category](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_category)**  

The credit memo category.

- 
**[creditAmount](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_creditAmount)**  

The total credit amount to apply to the invoice.

- 
**[creditLineRequestInputRepresentations](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestIRs_creditLineRequestInputRepresentations)**  

List of line-level credit requests for this invoice.

- 
**[description](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_description)**  

Optional description for the credit request.

- 
**[disputeId](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_disputeId)**  

The ID of the billing dispute associated with this credit request.

- 
**[invoiceId](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_IssueCreditMemo_CreditRequestInputRepresentations_invoiceId)**  

The ID of the invoice to credit.

### category

The credit memo category.

#### Signature

`public String category {get; set;}`

#### Property Value

Type: String

### creditAmount

The total credit amount to apply to the invoice.

#### Signature

`public Double creditAmount {get; set;}`

#### Property Value

Type: Double

### creditLineRequestInputRepresentations

List of line-level credit requests for this invoice.

#### Signature

`public List<IssueCreditMemo.CreditLineRequestInputRepresentations> creditLineRequestInputRepresentations {get; set;}`

#### Property Value

Type: List<[IssueCreditMemo.CreditLineRequestInputRepresentations](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations)>

### description

Optional description for the credit request.

#### Signature

`public String description {get; set;}`

#### Property Value

Type: String

### disputeId

The ID of the billing dispute associated with this credit request.

#### Signature

`public String disputeId {get; set;}`

#### Property Value

Type: String

### invoiceId

The ID of the invoice to credit.

#### Signature

`public String invoiceId {get; set;}`

#### Property Value

Type: String

=== ARTICLE: apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm ===
---
page_id: apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm
title: CreditResponseOutputRepresentations Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_IssueCreditMemo.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CreditResponseOutputRepresentations Class

Represents the result of a credit memo operation. Indicates success or failure and any additional information or message.

## Namespace

[IssueCreditMemo](./apex_namespace_IssueCreditMemo.htm.md)

## Usage

## Example

- 
**[CreditResponseOutputRepresentations Constructors](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_IssueCreditMemo_CreditResponseOutputRepresentations_constructors)**  

- 
**[CreditResponseOutputRepresentations Properties](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_IssueCreditMemo_CreditResponseOutputRepresentations_properties)**  

  

## CreditResponseOutputRepresentations Constructors

  
  
    
      

The `CreditResponseOutputRepresentations` class includes
        these constructors.

    

    
  

- 
**[CreditResponseOutputRepresentations(success, additionalInformation)](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_IssueCreditMemo_CreditResponseOutputRepresentations_ctor)**  

Creates a response with the given success flag and additional information.

### CreditResponseOutputRepresentations(success, additionalInformation)

Creates a response with the given success flag and additional information.

#### Signature

`public CreditResponseOutputRepresentations(Boolean success, String additionalInformation)`

#### Parameters

**success**

: Type: Boolean

: Indicates whether the credit memo is issued successfully (`true`) or not (`false`).

**additionalInformation**

: Type: String

: Additional information or message, such as error details or confirmation.

  

## CreditResponseOutputRepresentations Properties

  
  
    
      

The `CreditResponseOutputRepresentations` class includes
        these properties.

    

    
  

- 
**[additionalInformation](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_IssueCreditMemo_CreditResponseORs_additionalInformation)**  

Additional information or message, such as error details or confirmation.

- 
**[success](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_IssueCreditMemo_CreditResponseOutputRepresentations_success)**  

Indicates whether the credit memo is issued successfully (true) or not     (false).

### additionalInformation

Additional information or message, such as error details or confirmation.

#### Signature

`public String additionalInformation {get; set;}`

#### Property Value

Type: String

### success

Indicates whether the credit memo is issued successfully (true) or not
    (false).

#### Signature

`public Boolean success {get; set;}`

#### Property Value

Type: Boolean

=== ARTICLE: apex_class_RulesAppln_RulesApplicationErrorResponse.htm ===
---
page_id: apex_class_RulesAppln_RulesApplicationErrorResponse.htm
title: RulesApplicationErrorResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationErrorResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_RulesAppln.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RulesApplicationErrorResponse Class

Contains properties to store error details that occurred during the rules application.

## Namespace

[RulesAppln](./apex_namespace_RulesAppln.htm.md)

- 
**[RulesApplicationErrorResponse Constructors](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_constructors)**  

Learn more about the constructors available with the RulesApplicationErrorResponse     class.

- 
**[RulesApplicationErrorResponse Properties](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_properties)**  

Learn more about the properties available with the RulesApplicationErrorResponse     class.

  

## RulesApplicationErrorResponse Constructors

  
  
  
Learn more about the constructors available with the RulesApplicationErrorResponse
    class.

    
      

The `RulesApplicationErrorResponse` class includes these
        constructors.

    

    
  

- 
**[RulesApplicationErrorResponse(errorCode, message)](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_ctor)**  

Initializes the RulesApplicationErrorResponse class that stores error details that occurred during the rules application.

- 
**[RulesApplicationErrorResponse()](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_ctor_2)**  

Initializes an empty instance of the RulesApplicationErrorResponse class.

### RulesApplicationErrorResponse(errorCode, message)

Initializes the RulesApplicationErrorResponse class that stores error details that occurred during the rules application.

#### Signature

`public RulesApplicationErrorResponse(String errorCode, String message)`

```
RulesAppln.RulesApplicationErrorResponse, newinstance, [String, String], RulesAppln.RulesApplicationErrorResponse
```

#### Parameters

**errorCode**

: Type: String

: 

Error code that identifies the type of error that occurred during the rules application.

**message**

: Type: String

: 

Error message that describes the error that occurred during the rules application.

### RulesApplicationErrorResponse()

Initializes an empty instance of the RulesApplicationErrorResponse class.

#### Signature

`public RulesApplicationErrorResponse()`

```
RulesAppln.RulesApplicationErrorResponse, newinstance, [], RulesAppln.RulesApplicationErrorResponse
```

  

## RulesApplicationErrorResponse Properties

  
  
  
Learn more about the properties available with the RulesApplicationErrorResponse
    class.

    
      

The `RulesApplicationErrorResponse` class includes these
        properties.

    

    
  

- 
**[errorCode](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_errorCode)**  

Get the error code that identifies the type of error that occurred during the rules     application.

- 
**[message](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_RulesAppln_RulesApplicationErrorResponse_message)**  

Get the error message that describes the error that occurred during the rules     application.

### errorCode

Get the error code that identifies the type of error that occurred during the rules
    application.

#### Signature

`public String errorCode {get; set;}`

```
RulesAppln.RulesApplicationErrorResponse, errorCode
```

#### Property Value

Type: String

### message

Get the error message that describes the error that occurred during the rules
    application.

#### Signature

`public String message {get; set;}`

```
RulesAppln.RulesApplicationErrorResponse, message
```

#### Property Value

Type: String

=== ARTICLE: apex_class_RulesAppln_RulesApplicationResponse.htm ===
---
page_id: apex_class_RulesAppln_RulesApplicationResponse.htm
title: RulesApplicationResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_RulesAppln.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RulesApplicationResponse Class

Contains properties to store the response details for the rules application request.

## Namespace

[RulesAppln](./apex_namespace_RulesAppln.htm.md)

- 
**[RulesApplicationResponse Constructors](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_constructors)**  

Learn more about the constructors available with the RulesApplicationResponse     class.

- 
**[RulesApplicationResponse Properties](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_properties)**  

Learn more about the properties available with the RulesApplicationResponse     class.

  

## RulesApplicationResponse Constructors

  
  
  
Learn more about the constructors available with the RulesApplicationResponse
    class.

    
      

The `RulesApplicationResponse` class includes these
        constructors.

    

    
  

- 
**[RulesApplicationResponse(isSuccess, appliedRules, rulesApplicationSummary, errors)](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_ctor)**  

Initializes the RulesApplicationResponse class that stores the response details for the rules application request.

- 
**[RulesApplicationResponse()](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_ctor_2)**  

Initializes an empty instance of the RulesApplicationResponse class.

### RulesApplicationResponse(isSuccess, appliedRules, rulesApplicationSummary, errors)

Initializes the RulesApplicationResponse class that stores the response details for the rules application request.

#### Signature

`public RulesApplicationResponse(Boolean isSuccess, List<String> appliedRules, RulesAppln.RulesApplicationSummaryResponse rulesApplicationSummary, List<RulesAppln.RulesApplicationErrorResponse> errors)`

```
RulesAppln.RulesApplicationResponse, newinstance, [Boolean, List<String>, RulesAppln.RulesApplicationSummaryResponse, List<RulesAppln.RulesApplicationErrorResponse>], RulesAppln.RulesApplicationResponse
```

#### Parameters

**isSuccess**

: Type: Boolean

: 

Indicates whether the rules are applied (`true`) or not
                (`false`).

**appliedRules**

: Type: List<String>

: 

Comma-delimited list of applied rules.

**rulesApplicationSummary**

: Type: [RulesAppln.RulesApplicationSummaryResponse](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_class_RulesAppln_RulesApplicationSummaryResponse)

: 

Details of the rules application that includes these details.

            
              
- Payment and credit memo count for the account

              
- Payment and credit memo count that's applied to invoices or invoice lines

              
- Details of rules

            

**errors**

: Type: List<[RulesAppln.RulesApplicationErrorResponse](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_class_RulesAppln_RulesApplicationErrorResponse)>

: 

List of error responses that occurred during the rules application.

### RulesApplicationResponse()

Initializes an empty instance of the RulesApplicationResponse class.

#### Signature

`public RulesApplicationResponse()`

```
RulesAppln.RulesApplicationResponse, newinstance, [], RulesAppln.RulesApplicationResponse
```

  

## RulesApplicationResponse Properties

  
  
  
Learn more about the properties available with the RulesApplicationResponse
    class.

    
      

The `RulesApplicationResponse` class includes these
        properties.

    

    
  

- 
**[appliedRules](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_appliedRules)**  

Get the comma-delimited list of rules that were applied.

- 
**[errors](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_errors)**  

Get the list of error responses that occurred during the rules application.

- 
**[isSuccess](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_isSuccess)**  

Get the boolean value that indicates whether the rules were applied (true) or not     (false).

- 
**[rulesApplicationSummary](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_RulesAppln_RulesApplicationResponse_rulesApplicationSummary)**  

Get the details of the rules application that includes payment and credit memo count for     the account, payment and credit memo count that's applied to invoices or invoice lines, and     whether the exact amount rule is applied.

### appliedRules

Get the comma-delimited list of rules that were applied.

#### Signature

`public List<String> appliedRules {get; set;}`

```
RulesAppln.RulesApplicationResponse, appliedRules
```

#### Property Value

Type: List<String>

### errors

Get the list of error responses that occurred during the rules application.

#### Signature

`public List<RulesAppln.RulesApplicationErrorResponse> errors {get; set;}`

```
RulesAppln.RulesApplicationResponse, errors
```

#### Property Value

Type: List<[RulesAppln.RulesApplicationErrorResponse](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_class_RulesAppln_RulesApplicationErrorResponse)>

### isSuccess

Get the boolean value that indicates whether the rules were applied (true) or not
    (false).

#### Signature

`public Boolean isSuccess {get; set;}`

```
RulesAppln.RulesApplicationResponse, isSuccess
```

#### Property Value

Type: Boolean

### rulesApplicationSummary

Get the details of the rules application that includes payment and credit memo count for
    the account, payment and credit memo count that's applied to invoices or invoice lines, and
    whether the exact amount rule is applied.

#### Signature

`public RulesAppln.RulesApplicationSummaryResponse rulesApplicationSummary {get; set;}`

```
RulesAppln.RulesApplicationResponse, rulesApplicationSummary
```

#### Property Value

Type: [RulesAppln.RulesApplicationSummaryResponse](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_class_RulesAppln_RulesApplicationSummaryResponse)

=== ARTICLE: apex_class_RulesAppln_RulesApplicationSummaryResponse.htm ===
---
page_id: apex_class_RulesAppln_RulesApplicationSummaryResponse.htm
title: RulesApplicationSummaryResponse Class
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationSummaryResponse.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_namespace_RulesAppln.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RulesApplicationSummaryResponse Class

Contains properties to store the summary details of the rules application, including payment and credit memo counts and application statistics.

## Namespace

[RulesAppln](./apex_namespace_RulesAppln.htm.md)

- 
**[RulesApplicationSummaryResponse Constructors](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_constructors)**  

Learn more about the constructors available with the RulesApplicationSummaryResponse     class.

- 
**[RulesApplicationSummaryResponse Properties](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_properties)**  

Learn more about the properties available with the RulesApplicationSummaryResponse     class.

  

## RulesApplicationSummaryResponse Constructors

  
  
  
Learn more about the constructors available with the RulesApplicationSummaryResponse
    class.

    
      

The `RulesApplicationSummaryResponse` class includes these
        constructors.

    

    
  

- 
**[RulesApplicationSummaryResponse(fetchedPaymentsCount, fetchedCreditMemosCount, totalPaymentApplications, totalCreditMemoApplications, areAllInvoicesConsidered)](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_ctor)**  

Initializes the RulesApplicationSummaryResponse class that stores the summary details of the rules application.

- 
**[RulesApplicationSummaryResponse()](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_ctor_2)**  

Initializes an empty instance of the RulesApplicationSummaryResponse class.

### RulesApplicationSummaryResponse(fetchedPaymentsCount, fetchedCreditMemosCount, totalPaymentApplications, totalCreditMemoApplications, areAllInvoicesConsidered)

Initializes the RulesApplicationSummaryResponse class that stores the summary details of the rules application.

#### Signature

`public RulesApplicationSummaryResponse(Integer fetchedPaymentsCount, Integer fetchedCreditMemosCount, Integer totalPaymentApplications, Integer totalCreditMemoApplications, Boolean areAllInvoicesConsidered)`

```
RulesAppln.RulesApplicationSummaryResponse, newinstance, [Integer, Integer, Integer, Integer, Boolean], RulesAppln.RulesApplicationSummaryResponse
```

#### Parameters

**fetchedPaymentsCount**

: Type: Integer

: 

Number of payment records retrieved for an account.

**fetchedCreditMemosCount**

: Type: Integer

: 

Number of credit memo or credit memo line records retrieved for an account.

**totalPaymentApplications**

: Type: Integer

: 

Number of payments that are applied to invoices and invoice lines.

**totalCreditMemoApplications**

: Type: Integer

: 

Number of credit memos that are applied to the invoice or invoice lines.

**areAllInvoicesConsidered**

: Type: Boolean

: 

Indicates whether all invoices are considered (`true`) or not
                (`false`).

### RulesApplicationSummaryResponse()

Initializes an empty instance of the RulesApplicationSummaryResponse class.

#### Signature

`public RulesApplicationSummaryResponse()`

```
RulesAppln.RulesApplicationSummaryResponse, newinstance, [], RulesAppln.RulesApplicationSummaryResponse
```

  

## RulesApplicationSummaryResponse Properties

  
  
  
Learn more about the properties available with the RulesApplicationSummaryResponse
    class.

    
      

The `RulesApplicationSummaryResponse` class includes these
        properties.

    

    
  

- 
**[areAllInvoicesConsidered](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_areAllInvoicesConsidered)**  

Indicates whether all invoices are considered (true) or not (false).

- 
**[fetchedCreditMemosCount](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_fetchedCreditMemosCount)**  

Get the number of credit memo or credit memo line records retrieved for an     account.

- 
**[fetchedPaymentsCount](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_fetchedPaymentsCount)**  

Get the number of payment records retrieved for an account.

- 
**[totalCreditMemoApplications](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_totalCreditMemoApplications)**  

Get the number of credit memos that are applied to the invoice or invoice     lines.

- 
**[totalPaymentApplications](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_RulesAppln_RulesApplicationSummaryResponse_totalPaymentApplications)**  

Get the number of payments that are applied to invoices and invoice lines.

### areAllInvoicesConsidered

Indicates whether all invoices are considered (true) or not (false).

#### Signature

`public Boolean areAllInvoicesConsidered {get; set;}`

```
RulesAppln.RulesApplicationSummaryResponse, areAllInvoicesConsidered
```

#### Property Value

Type: Boolean

### fetchedCreditMemosCount

Get the number of credit memo or credit memo line records retrieved for an
    account.

#### Signature

`public Integer fetchedCreditMemosCount {get; set;}`

```
RulesAppln.RulesApplicationSummaryResponse, fetchedCreditMemosCount
```

#### Property Value

Type: Integer

### fetchedPaymentsCount

Get the number of payment records retrieved for an account.

#### Signature

`public Integer fetchedPaymentsCount {get; set;}`

```
RulesAppln.RulesApplicationSummaryResponse, fetchedPaymentsCount
```

#### Property Value

Type: Integer

### totalCreditMemoApplications

Get the number of credit memos that are applied to the invoice or invoice
    lines.

#### Signature

`public Integer totalCreditMemoApplications {get; set;}`

```
RulesAppln.RulesApplicationSummaryResponse, totalCreditMemoApplications
```

#### Property Value

Type: Integer

### totalPaymentApplications

Get the number of payments that are applied to invoices and invoice lines.

#### Signature

`public Integer totalPaymentApplications {get; set;}`

```
RulesAppln.RulesApplicationSummaryResponse, totalPaymentApplications
```

#### Property Value

Type: Integer

=== ARTICLE: apex_commercetax_TaxEngineAdapter_methods.htm ===
---
page_id: apex_commercetax_TaxEngineAdapter_methods.htm
title: TaxEngineAdapter Methods
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_commercetax_TaxEngineAdapter_methods.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_tax_engine_adapter_interface_for_standard_tax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxEngineAdapter Methods

Learn more about the available methods with the `TaxEngineAdapter` class.

    
      

The `TaxEngineAdapter` class includes these
        methods.

    

    
  

- 
**[processRequest(requestType)](./apex_commercetax_TaxEngineAdapter_processRequest.htm.md)**  

The `processRequest` method takes       an instance of `TaxEngineContext` class and returns a       response with the calculated tax details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

=== ARTICLE: apex_commercetax_TaxEngineAdapter_processRequest.htm ===
---
page_id: apex_commercetax_TaxEngineAdapter_processRequest.htm
title: processRequest(requestType)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_commercetax_TaxEngineAdapter_processRequest.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: apex_commercetax_TaxEngineAdapter_methods.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# processRequest(requestType)

The `processRequest` method takes
      an instance of `TaxEngineContext` class and returns a
      response with the calculated tax details through the `TaxDetailsResponse` class or an error response through the `ErrorResponse` class.

    

## Signature

`global commercetax.TaxEngineResponse
          processRequest(commercetax.TaxEngineContext var1)`

    

## Parameters

        
- 
**var1**:

Type: [TaxEngineContext](./apex_class_commercetax_TaxEngineContext.htm.md#apex_class_commercetax_TaxEngineContext)

Wrapper class that stores information about

the type of a tax calculation
            request.

      

    

## Return Value

Type:
        TaxEngineResponse

Generic interface representing a response from a tax engine.

=== ARTICLE: apex_connectapi_input_address.htm ===
---
page_id: apex_connectapi_input_address.htm
title: ConnectApi.BillingAddressRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_address.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.BillingAddressRequest

Input representation of the details of an address.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `city` | String | Address city. | Optional | 62.0 |
| `country` | String | Address country. | Optional | 62.0 |
| `latitude` | Double | Latitude for the address. | Optional | 62.0 |
| `locationCode` | String | Location code for the address. | Optional | 62.0 |
| `longitude` | Double | Longitude for the address. | Optional | 62.0 |
| `postalCode` | String | Postal code for the address. | Optional | 62.0 |
| `state` | String | Address state. | Optional | 62.0 |
| `street` | String | Address street. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_billing_schedule_recovery.htm ===
---
page_id: apex_connectapi_input_billing_schedule_recovery.htm
title: ConnectApi.BillingScheduleRecoveryInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_billing_schedule_recovery.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.BillingScheduleRecoveryInputRepresentation

Input representation of the details of the billing schedules to recover the associated
    invoice.

    
      

          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Schedule​Ids` | List<`String`> | IDs of the billing schedules to recover the invoice for. You can recover one billing schedule per API request. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_convert_negative_invoice_lines.htm ===
---
page_id: apex_connectapi_input_convert_negative_invoice_lines.htm
title: ConnectApi.ConvertNegativeInvoiceLinesInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_convert_negative_invoice_lines.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ConvertNegativeInvoiceLinesInputRequest

Input representation of the request details to convert a negative invoice line into a
    credit.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Description stamped on the credit memo that’s created after the negative invoice line conversion. | Optional | 62.0 |
| `effectiveDate` | String | Date stamped on the credit memo that’s created after the negative invoice line conversion. | Required | 62.0 |
| `invoiceId` | String | ID of the invoice whose negative invoice lines must be converted into a posted credit memo. | Required | 62.0 |
| `invoiceLines` | List<`String`> | Complete list of the negative invoice lines along with the associated invoice line taxes. The specified negative invoice lines are converted into a posted credit memo. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_invoice.htm ===
---
page_id: apex_connectapi_input_credit_invoice.htm
title: ConnectApi.CreditInvoiceInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_invoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditInvoiceInputRequest

Input representation of the details of the request to create a credit memo.

- 
- 
- 
- 

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Description for the credit memo to be created. | Optional | 62.0 |
| `effective​Date` | String | Date when the credit memo takes effect. | Optional | 62.0 |
| `invoice​Lines` | List<[ConnectApi.CreditInvoiceInvoiceLine](./apex_connectapi_input_credit_invoice_invoice_line.htm.md)> | List of the invoice lines to be credited. The invoice line IDs must be related to the invoice ID specified in the API request. If invoice lines aren’t specified, the API request results in an error. | Required | 62.0 |
| `taxEffective​Date` | String | Date when the tax takes effect to recalculate the taxes. | Optional | 62.0 |
| `tax​Strategy` | `ConnectApi.TaxStrategyEnum` | Tax strategy to be applied across invoice lines. You can override the tax strategy at the individual invoice line level or at the tax line level. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `ManualOverride`—Specifies that the provided tax values must be considered for taxes. `CopyFromInvoiceLine`—Specifies that tax values must be copied from the invoice line. `Calculate`—Specifies that tax must be calculated by using the API. | Required | 62.0 |
| `type` | `ConnectApi.CreditMemoTypeEnum` | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_invoice_invoice_line.htm ===
---
page_id: apex_connectapi_input_credit_invoice_invoice_line.htm
title: ConnectApi.CreditInvoiceInvoiceLine
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_invoice_invoice_line.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditInvoiceInvoiceLine

Input representation of the details of the invoice lines to be credited.

- 
- 
- 
- 

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [ConnectApi.CreditMemoAddressesInputRequest](./apex_connectapi_input_credit_memo_addresses.htm.md) | Addresses to be created manually for this invoice line and the overridden tax lines. These addresses are only applicable if this invoice line is using the `ManualOverride` tax strategy. | Optional | 62.0 |
| `amountToCredit` | Double | Amount to be credited from this invoice line. | Required | 62.0 |
| `invoiceLineId` | String | ID of the invoice line record to be credited. The invoice line ID must be related to the invoice ID specified in the API request. | Required | 62.0 |
| `isTaxOnlyCredit` | Boolean | Indicates whether the applicable tax amount is credited for the charge or adjustment amount (`true`), or the applicable tax amount is credited along with the charge or adjustment amount (`false`). The default value is `false`. | Optional | 62.0 |
| `taxEffectiveDate` | String | Date when the tax takes effect and the invoice line is credited. | Optional | 62.0 |
| `taxStrategy` | `ConnectApi.TaxStrategyEnum` | Tax strategy for crediting the invoice line. This tax strategy takes precedence over the `taxStrategy` property value specified in the [Credit Invoice Input](./connect_requests_credit_invoice_input.htm.md). Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `ManualOverride`—Specifies that the provided tax values must be considered for taxes. `CopyFromInvoiceLine`—Specifies that tax values must be copied from the invoice line. `Calculate`—Specifies that tax must be calculated by using the API. | Optional | 62.0 |
| `taxes` | List<[ConnectApi.CreditInvoiceInvoiceLineTax](./apex_connectapi_input_credit_invoice_invoice_line_tax.htm.md)> | List of tax lines to be created manually for this invoice line. | Required if the `taxStrategy` property value is `ManualOverride`. | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_invoice_invoice_line_tax.htm ===
---
page_id: apex_connectapi_input_credit_invoice_invoice_line_tax.htm
title: ConnectApi.CreditInvoiceInvoiceLineTax
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_invoice_invoice_line_tax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditInvoiceInvoiceLineTax

Input representation of the details of the tax lines to be created manually for the
    invoice line.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `taxAmount` | Double | Amount of tax to be applied related to this invoice line. | Required | 62.0 |
| `taxCode` | String | Tax code to be applied related to this invoice line to create the tax line. | Optional | 62.0 |
| `taxName` | String | Name of tax to be applied related to this invoice line. | Optional | 62.0 |
| `taxRate` | Double | Tax rate used to create the tax line. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_addresses.htm ===
---
page_id: apex_connectapi_input_credit_memo_addresses.htm
title: ConnectApi.CreditMemoAddressesInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_addresses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoAddressesInputRequest

Input representation of the details of the billing and shipping addresses.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billingAddress` | [ConnectApi.BillingAddressRequest](./apex_connectapi_input_address.htm.md) | Billing address for charge or adjustment line. | Optional | 62.0 |
| `shippingAddress` | [ConnectApi.BillingAddressRequest](./apex_connectapi_input_address.htm.md) | Shipping address for charge or adjustment line. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_apply.htm ===
---
page_id: apex_connectapi_input_credit_memo_apply.htm
title: ConnectApi.CreditMemoApplyInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoApplyInputRequest

Input representation of the request to apply a credit memo to an invoice.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `applications` | List<[ConnectApi.ApplicationsRequest](./apex_connectapi_input_credit_memo_apply_application.htm.md)> | List of one or more applications to apply the credit memo for. Each application represents an invoice that’s credited by using the balance of the specified credit memo. | Required | 62.0 |
| `creditMemoId` | String | ID of the credit memo record. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_apply_application.htm ===
---
page_id: apex_connectapi_input_credit_memo_apply_application.htm
title: ConnectApi.ApplicationsRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_apply_application.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ApplicationsRequest

Connect API representation of an application item input request for credit memo apply api

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Credit amount to be applied to the invoice. | Required | 62.0 |
| `appliedToId` | String | ID of the invoice record to apply the credit for. | Required | 62.0 |
| `description` | String | Explanation or reason for applying the credit memo. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_line_application.htm ===
---
page_id: apex_connectapi_input_credit_memo_line_application.htm
title: ConnectApi.CreditDetailsApplyInput
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_line_application.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditDetailsApplyInput

Input representation of the request to specify one or more applications to apply a credit
    memo line for, with each application representing an invoice line.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `appliedAmount` | Double | Credit amount to be applied to the invoice line. | Required | 62.0 |
| `description` | String | Explanation or reason for applying the credit memo line. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo line. | Optional | 62.0 |
| `invoiceLineId` | String | ID of the invoice line record to apply the credit for. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_line_apply.htm ===
---
page_id: apex_connectapi_input_credit_memo_line_apply.htm
title: ConnectApi.CreditMemoLineApplyInput
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_line_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoLineApplyInput

Input representation of the details of the request to apply a credit memo line to an
    invoice line.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `applyCreditDetails` | List<[`ConnectApi.CreditDetailsApplyInput`](./apex_connectapi_input_credit_memo_line_application.htm.md)> | List of one or more applications to apply the credit memo line for. Each application represents an invoice line that’s credited by using the balance of the specified credit memo line. | Required | 62.0 |
| `creditMemoLineId` | String | ID of the credit memo line record. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_line_unapply.htm ===
---
page_id: apex_connectapi_input_credit_memo_line_unapply.htm
title: ConnectApi.CreditMemoLineUnapplyInput
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_line_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoLineUnapplyInput

Input representation of the details of the request to unapply a credit memo line from an
    invoice line.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemoLineInvoiceLineId` | String | ID of the credit memo line invoice line record. | Required | 62.0 |
| `description` | String | Explanation or reason for unapplying the credit memo line. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo line. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_credit_memo_unapply.htm ===
---
page_id: apex_connectapi_input_credit_memo_unapply.htm
title: ConnectApi.CreditMemoUnapplyInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_credit_memo_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoUnapplyInputRequest

Input representation of the request to unapply a credit memo from an invoice.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemoInvApplicationId` | String | ID of the credit memo invoice application. | Required | 62.0 |
| `description` | String | Explanation or reason for unapplying the credit memo. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_invoice.htm ===
---
page_id: apex_connectapi_input_invoice.htm
title: ConnectApi.InvoiceInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_invoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.InvoiceInputRepresentation

Input representation of the details of the billing schedule.

- 
- 

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `action` | `ConnectApi.InvoiceAction` | Type of invoice to be created. Valid values are: `Draft` `Posted` | Required | 62.0 |
| `billing​ScheduleIds` | List<`String`> | List of billing schedule IDs that’s used to create the invoices. You can specify a maximum of 200 billing schedules. | Required | 62.0 |
| `correlation​Id` | String | Property that’s tagged against the published `InvoiceProcessedEvent` event, if specified. | Optional | 62.0 |
| `invoice​Date` | String | Stamping date of the invoice in ISO 8601 format. | Required | 62.0 |
| `target​Date` | String | Date in ISO 8601 format used to decide the billing periods that are included to create invoices. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_invoice_draft_to_posted.htm ===
---
page_id: apex_connectapi_input_invoice_draft_to_posted.htm
title: ConnectApi.InvoiceDraftToPostedInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_invoice_draft_to_posted.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.InvoiceDraftToPostedInputRequest

Input representation of the details of the draft invoice that’s posted.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Splunk correlation ID to track the messages that are related to the request and are logged in Splunk by the different services involved in the request. If the ID isn’t specified, the service creates a random Universally Unique Identifier (UUID). | Optional | 62.0 |
| `invoiceIds` | List<`String`> | IDs of the invoice records in `Draft` status to be posted. You can post one draft invoice per API request. | Required | 62.0 |

=== ARTICLE: apex_connectapi_input_payment_line_apply.htm ===
---
page_id: apex_connectapi_input_payment_line_apply.htm
title: ConnectApi.PaymentLineApplyRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_payment_line_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.PaymentLineApplyRequest

Input representation of the payment line details. This representation covers details on
    allocation of a payment to a specific invoice line. It also provides additional context through
    optional fields, such as associated account and effective date.

- 
- 

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount that's applied. The amount must be less than the invoice line and payment balance. | Required | 64.0 |
| `applied​ToId` | String | ID of the invoice line that this payment is applied to. Specify the IDs for these records. Invoice Invoice Line | Required | 64.0 |
| `associated​AccountId` | String | ID of the associated account. | Optional | 64.0 |
| `comments` | String | Comments that you can add to the payment line application. | Optional | 64.0 |
| `effective​Date` | Datetime | Date from which the payment line application takes effect. | Optional | 64.0 |

=== ARTICLE: apex_connectapi_input_payment_line_unapply.htm ===
---
page_id: apex_connectapi_input_payment_line_unapply.htm
title: ConnectApi.PaymentLineUnapplyRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_payment_line_unapply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.PaymentLineUnapplyRequest

Input representation of the payment line details. This representation covers fields that
    you can specify to revert a payment line application.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `comments` | String | Comments that you can add when you revert a payment line application. | Optional | 64.0 |
| `effective​Date` | Datetime | Date from when the reversal of the payment line application is in effect. | Optional | 64.0 |

=== ARTICLE: apex_connectapi_input_refund_line_apply.htm ===
---
page_id: apex_connectapi_input_refund_line_apply.htm
title: ConnectApi.RefundLineApplyRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_refund_line_apply.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.RefundLineApplyRequest

Input representation of the details of a transaction refund request. This representation
    outlines the properties of a refund, including the refund amount and ID of the payment or credit
    memo record that the refund is applied to.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Amount to refund. | Required | 64.0 |
| `appliedToId` | String | ID of a payment or credit memo record. The refund is applied to this object. | Required | 64.0 |
| `comments` | String | Additional details of the refund request. | Optional | 64.0 |
| `effectiveDate` | Datetime | Date from when the refund is in effect. | Optional | 64.0 |

=== ARTICLE: apex_connectapi_input_sequence_gap_reconciliation.htm ===
---
page_id: apex_connectapi_input_sequence_gap_reconciliation.htm
title: ConnectApi.SequenceGapReconciliationInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_sequence_gap_reconciliation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequenceGapReconciliationInputRepresentation

The details of the input used to identify and reconcile gaps in sequence values based on the sequence policy or target object.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequencePolicyIds` | List<`String`> | List of IDs of the sequence policies. | Required if the `targetObjects` property isn't specified. You must not specify both properties. | 65.0 |
| `targetObjects` | List<`String`> | List of objects to which the policies are applied. | Required if the `sequencePolicyIds` property isn't specified. You must not specify both properties. | 65.0 |

=== ARTICLE: apex_connectapi_input_sequences_assignment.htm ===
---
page_id: apex_connectapi_input_sequences_assignment.htm
title: ConnectApi.SequencesAssignmentInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_sequences_assignment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequencesAssignmentInputRepresentation

The details of the target objects to which the sequence pattern values are assigned.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `sequencePolicyId` | String | ID of the sequence policy. | Optional | 65.0 |
| `shouldPublishPlatformEvent` | Boolean | Indicates whether to publish a platform event when a sequence is assigned to a target record (`true`) or not (`false`). | Optional | 65.0 |
| `targetObjectIds` | List<`String`> | List of records to which the sequence pattern values are assigned. | Required | 65.0 |

=== ARTICLE: apex_connectapi_input_standalone_credit_memo.htm ===
---
page_id: apex_connectapi_input_standalone_credit_memo.htm
title: ConnectApi.StandaloneCreditMemoInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_standalone_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.StandaloneCreditMemoInputRequest

Input representation of the details required to create a standalone credit
    memo.

- 
- 
- 

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billToContactId` | String | Contact related to the credit memo. | Optional | 62.0 |
| `billingAccountId` | String | ID of the account that the credit is issued to. | Required | 62.0 |
| `charges` | List<[`ConnectApi.StandaloneCreditMemoChargeInputRequest`](./apex_connectapi_input_standalone_credit_memo_charge.htm.md)> | Charge lines of the credit memo. Requires at least one charge line. | Required | 62.0 |
| `currencyIsoCode` | String | ISO code currency of the new credit that’s issued. | Optional | 62.0 |
| `description` | String | Description for the new credit that’s issued. | Optional | 62.0 |
| `effectiveDate` | String | Effective date of the credit memo. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `externalReference` | String | ID of the external reference for the credit memo. | Optional | 62.0 |
| `externalReferenceDataSource` | String | Source of the external reference for the credit memo. | Optional | 62.0 |
| `taxEffectiveDate` | String | Effective date of the credit memo tax. If the value isn’t specified, then it’s null. | Optional | 62.0 |
| `taxStrategy` | `ConnectApi.StandaloneTaxStrategyEnum` | Specifies how tax lines must be created for the standalone credit memos. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. | Required | 62.0 |
| `type` | `ConnectApi.CreditMemoTypeEnum` | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_standalone_credit_memo_charge.htm ===
---
page_id: apex_connectapi_input_standalone_credit_memo_charge.htm
title: ConnectApi.StandaloneCreditMemoChargeInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_standalone_credit_memo_charge.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.StandaloneCreditMemoChargeInputRequest

Input representation of the details of the charge lines of a credit memo.

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

- 
- 
- 

              

              

            

            
              

              

              

              

              

            

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [Credit Memo Addresses Input](./apex_connectapi_input_credit_memo_addresses.htm.md) | Details of the billing and shipping addresses. | Optional | 62.0 |
| `chargeAmount` | Double | Charge amount for the credit memo. | Required | 62.0 |
| `description` | String | Description of the created credit memo charge line. | Optional | 62.0 |
| `endDate` | String | End date of the credit memo charge line. | Optional | 62.0 |
| `isTaxOnlyCredit` | Boolean | Indicates whether the credit is for tax only (`true`) or not (`false`). | Optional | 62.0 |
| `productId` | String | ID of the product record that the credit memo is issued on. | Optional | 62.0 |
| `productName` | String | Name of the product that the credit memo is issued on. | Optional | 62.0 |
| `startDate` | String | Start date of the credit memo charge line. | Optional | 62.0 |
| `taxEffectiveDate` | String | Date from when the tax is applicable. | Optional | 62.0 |
| `taxes` | List[ConnectApi.StandaloneCreditMemoTaxInputRequest](./apex_connectapi_input_standalone_credit_memo_tax.htm.md) | List of credit memo tax lines. | Optional | 62.0 |
| `taxStrategy` | `ConnectApi.StandaloneTaxStrategyEnum` | Tax strategy to be applied to this credit memo charge line, child treatment lines, and tax lines. You can override the tax strategy at the individual credit memo lines or tax lines level. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. | Optional | 62.0 |
| `treatmentId` | String | ID of the tax treatment record that’s used to calculate tax. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_standalone_credit_memo_tax.htm ===
---
page_id: apex_connectapi_input_standalone_credit_memo_tax.htm
title: ConnectApi.StandaloneCreditMemoTaxInputRequest
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_standalone_credit_memo_tax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.StandaloneCreditMemoTaxInputRequest

Connect API representation of Tax input request

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `taxAmount` | Double | Amount of tax to be applied. | Required | 62.0 |
| `taxCode` | String | Tax code to be used to create the tax line. | Optional | 62.0 |
| `taxName` | String | Name of tax to be applied. | Optional | 62.0 |
| `taxRate` | Double | Tax rate to be used to create the tax line. | Optional | 62.0 |

=== ARTICLE: apex_connectapi_input_void_posted_credit_memo.htm ===
---
page_id: apex_connectapi_input_void_posted_credit_memo.htm
title: ConnectApi.VoidPostedCreditMemoInputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_input_void_posted_credit_memo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_input_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.VoidPostedCreditMemoInputRepresentation

Input representation of the details of a credit memo to be voided.

| Property | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `creditMemoId` | String | ID of the posted credit memo to be voided. | Required | 66.0 |

=== ARTICLE: apex_connectapi_output_billing_schedule_recovery_list_output.htm ===
---
page_id: apex_connectapi_output_billing_schedule_recovery_list_output.htm
title: ConnectApi.BillingScheduleRecoveryResults
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_billing_schedule_recovery_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.BillingScheduleRecoveryResults

Output representation of the recovered details of the billing schedules and associated
    invoice.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `recovery​Results` | List<[ConnectApi.InvoiceRecoveryResult](./apex_connectapi_output_invoice_recovery_output.htm.md)> | Details of the recovered invoice and billing schedules. | 62.0 |

=== ARTICLE: apex_connectapi_output_billing_schedule_recovery_output.htm ===
---
page_id: apex_connectapi_output_billing_schedule_recovery_output.htm
title: ConnectApi.BillingScheduleRecoveryResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_billing_schedule_recovery_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.BillingScheduleRecoveryResult

Output representation of the details of the recovered billing schedules.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `billing​ScheduleId` | String | ID of the billing schedule. | 62.0 |
| `billing​Schedule​Status` | String | Flag that indicates the billing schedule status. | 62.0 |

=== ARTICLE: apex_connectapi_output_convert_negative_invoice_lines_output.htm ===
---
page_id: apex_connectapi_output_convert_negative_invoice_lines_output.htm
title: ConnectApi.ConvertNegativeInvoiceLinesResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_convert_negative_invoice_lines_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ConvertNegativeInvoiceLinesResult

Output representation of the details of the credit memo along with the status of the
    request.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the processing of the API request. | 62.0 |
| `id` | String | ID of the credit memo that’s created after the conversion of the negative invoice lines. | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_apply_list_output.htm ===
---
page_id: apex_connectapi_output_credit_memo_apply_list_output.htm
title: ConnectApi.ApplyCreditResults
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_apply_list_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ApplyCreditResults

Output representation of the list of applied credit memo results.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `applyCreditResults` | List<[ConnectApi.ApplyCreditResult](./apex_connectapi_output_credit_memo_apply_output.htm.md)> | Output list of the applied credit memo results. | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_apply_output.htm ===
---
page_id: apex_connectapi_output_credit_memo_apply_output.htm
title: ConnectApi.ApplyCreditResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ApplyCreditResult

Connect API representation of credit memo apply output result

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `appliedToId` | String | ID of the invoice record that the credit is applied to. | 62.0 |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the processing of the API request. | 62.0 |
| `id` | String | ID of the credit memo invoice application. | 62.0 |
| `success` | Boolean | Indicates whether the credit memo is successfully applied (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_line_applied.htm ===
---
page_id: apex_connectapi_output_credit_memo_line_applied.htm
title: ConnectApi.CreditMemoLineAppliedResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_line_applied.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoLineAppliedResponse

Output representation of the list of applied credit memo line results.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `appliedCreditResponses` | List<[`ConnectApi.AppliedCreditResponse`](./apex_connectapi_output_credit_memo_line_applied_response.htm.md)> | Output list for the applied credit memo line results. | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_line_applied_response.htm ===
---
page_id: apex_connectapi_output_credit_memo_line_applied_response.htm
title: ConnectApi.AppliedCreditResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_line_applied_response.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.AppliedCreditResponse

Output representation of the list of applied credit memo line results.

    
      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `creditMemoLineInvoiceLineId` | String | ID of the credit memo line invoice line ID. | 62.0 |
| `errors` | List<[`ConnectApi.ErrorResponse`](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the processing of the API request. | 62.0 |
| `invoiceLineId` | String | ID of the invoice line record that the credit is applied to. | 62.0 |
| `success` | Boolean | Indicates whether the credit memo line is successfully applied (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_line_unapplied.htm ===
---
page_id: apex_connectapi_output_credit_memo_line_unapplied.htm
title: ConnectApi.CreditMemoLineUnappliedResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_line_unapplied.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.CreditMemoLineUnappliedResponse

Output representation of the details of the credit memo line invoice line record with the
    status of the request.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `creditMemoLineInvoiceLineId` | String | ID of the credit memo line invoice line record. | 62.0 |
| `errors` | List<[`ConnectApi.ErrorResponse`](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the processing of the API request. | 62.0 |
| `success` | Boolean | Indicates whether the credit memo line is successfully unapplied (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_credit_memo_unapply_output.htm ===
---
page_id: apex_connectapi_output_credit_memo_unapply_output.htm
title: ConnectApi.UnapplyCreditResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_credit_memo_unapply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.UnapplyCreditResult

Output representation of the details of the credit memo invoice application record with
    the status of the request.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the processing of the API request. | 62.0 |
| `id` | String | ID of the credit memo invoice application record. | 62.0 |
| `success` | Boolean | Indicates whether the credit memo is successfully unapplied (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_invoice_batch_draft_to_posted_output.htm ===
---
page_id: apex_connectapi_output_invoice_batch_draft_to_posted_output.htm
title: ConnectApi.InvoiceBatchDraftToPostedResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_invoice_batch_draft_to_posted_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.InvoiceBatchDraftToPostedResult

Output representation of the batch update details of the invoices from `Draft` to `Posted`
      status.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `invoiceBatchDraftToPostedId` | String | ID of the invoice batch draft to posted run record that’s created to track the batch process of posting the draft invoices that are associated with the parent invoice batch run record. | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_invoice_recovery_output.htm ===
---
page_id: apex_connectapi_output_invoice_recovery_output.htm
title: ConnectApi.InvoiceRecoveryResult
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_invoice_recovery_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.InvoiceRecoveryResult

Output representation of the details of the recovered invoice and billing
    schedules.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `billing​Schedules` | List<[ConnectApi.BillingScheduleRecoveryResult](./apex_connectapi_output_billing_schedule_recovery_output.htm.md)> | Billing schedules associated with this invoice. | 62.0 |
| `invoice​Errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors encountered during the invoice recovery. | 62.0 |
| `invoice​Id` | String | ID of the recovered invoice. | 62.0 |
| `invoice​Status` | String | Flag that indicates the invoice status. | 62.0 |
| `success` | Boolean | Indicates whether the overall transaction was successful or not (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_payment_line_apply_output.htm ===
---
page_id: apex_connectapi_output_payment_line_apply_output.htm
title: ConnectApi.PaymentLineApplyResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_payment_line_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.PaymentLineApplyResponse

Output representation of the details of the applied payment line. The details include the
    ID of the payment record and date when the payment line was applied.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `applied​Date` | Datetime | Date when the payment line was applied. | 64.0 |
| `id` | String | ID of the payment line record. | 64.0 |

=== ARTICLE: apex_connectapi_output_payment_line_unapply_output.htm ===
---
page_id: apex_connectapi_output_payment_line_unapply_output.htm
title: ConnectApi.PaymentLineUnapplyResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_payment_line_unapply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.PaymentLineUnapplyResponse

Output representation of the details of the reversed payment line application. The
    details include the ID of the payment line record and date when the payment line application was
    reversed.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `id` | String | ID of the payment line record. | 64.0 |
| `unapplied​Date` | Datetime | Date when the payment line application was reversed. | 64.0 |

=== ARTICLE: apex_connectapi_output_reference_line_error.htm ===
---
page_id: apex_connectapi_output_reference_line_error.htm
title: ConnectApi.ReferenceLineError
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_reference_line_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.ReferenceLineError

Output representation of the details of the line level errors.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors with error code and error message for the specified invoice line ID. | 62.0 |
| `reference​LineId` | String | ID of the invoice line specified in the API request that has an issue, causing the API request to fail. | 62.0 |

=== ARTICLE: apex_connectapi_output_refund_line_apply_output.htm ===
---
page_id: apex_connectapi_output_refund_line_apply_output.htm
title: ConnectApi.RefundLineApplyResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_refund_line_apply_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.RefundLineApplyResponse

Output representation of the details of an applied refund. This representation includes
    the properties of a refund line, such as the date when the refund is applied against a payment
    and ID of the refund line record.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `appliedDate` | Datetime | Date when the refund is applied against a payment. | 64.0 |
| `id` | String | ID of the refund line record. | 64.0 |

=== ARTICLE: apex_connectapi_output_revenue_async.htm ===
---
page_id: apex_connectapi_output_revenue_async.htm
title: ConnectApi.RevenueAsyncRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_revenue_async.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.RevenueAsyncRepresentation

Output representation of the result of the API request with the request
    identifier.

    
      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | Details of errors, if any. | 62.0 |
| `request​​Identifier` | String | Unique identifier of the request. | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_revenue_async_line_level.htm ===
---
page_id: apex_connectapi_output_revenue_async_line_level.htm
title: ConnectApi.RevenueAsyncLineLevelOutputResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_revenue_async_line_level.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.RevenueAsyncLineLevelOutputResponse

Output representation of the result of the API request for the async line level
    operations.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[ConnectApi.ErrorResponse](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | Details of errors, if any. | 62.0 |
| `referenceLineErrorResults` | List<[ConnectApi.ReferenceLineError](./apex_connectapi_output_reference_line_error.htm.md)> | List of errors grouped by the invoice line IDs if the API request fails. | 62.0 |
| `referenceLineType` | String | Reference type for the reference line entity in the `referenceLineErrorResults` property. | 62.0 |
| `requestIdentifier` | String | Unique identifier of the request. | 62.0 |
| `statusURL` | String | URL to track the status of the operation. | 62.0 |
| `success` | Boolean | Indicates whether the API request is successful (`true`) or not (`false`). | 62.0 |

=== ARTICLE: apex_connectapi_output_sequence_error_output.htm ===
---
page_id: apex_connectapi_output_sequence_error_output.htm
title: ConnectApi.SequenceErrorOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_sequence_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequenceErrorOutputRepresentation

Output representation of the error response that's associated with a request to create or
    update a sequence policy, or assign sequences.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | 65.0 |
| `message` | String | Error message for the resultant error. | 65.0 |

=== ARTICLE: apex_connectapi_output_sequence_gap_reconciliation_error_output.htm ===
---
page_id: apex_connectapi_output_sequence_gap_reconciliation_error_output.htm
title: ConnectApi.SequenceGapReconciliationErrorOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_sequence_gap_reconciliation_error_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequenceGapReconciliationErrorOutputRepresentation

List of errors encountered during the processing of the API request.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errorCode` | String | Code for the resultant error. | 65.0 |
| `errorMessage` | String | Error message for the resultant error. | 65.0 |

=== ARTICLE: apex_connectapi_output_sequence_gap_reconciliation_output.htm ===
---
page_id: apex_connectapi_output_sequence_gap_reconciliation_output.htm
title: ConnectApi.SequenceGapReconciliationOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_sequence_gap_reconciliation_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequenceGapReconciliationOutputRepresentation

Output representation of the details of the sequence gap reconciliation.

- 
- 

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `error` | [`ConnectApi.SequenceGapReconciliationErrorOutputRepresentation`](./apex_connectapi_output_sequence_gap_reconciliation_error_output.htm.md) | List of errors encountered during the processing of the API request. | 65.0 |
| `jobId` | String | Unique identifier assigned to sequence gap reconciliation asynchronous process. | 65.0 |
| `sequencePolicyIds` | List<`String`> | List of IDs of the sequence policies. | 65.0 |
| `status` | `StatusEnum` | The status of sequence reconciliation API request. Valid values are: `Submitted` `NotSubmitted` | 65.0 |
| `submittedAt` | String | Date and time when the reconciliation request was submitted to the async job. | 65.0 |
| `targetObjects` | List<`String`> | List of objects to which the policies are applied. | 65.0 |

=== ARTICLE: apex_connectapi_output_sequences_assignment_output.htm ===
---
page_id: apex_connectapi_output_sequences_assignment_output.htm
title: ConnectApi.SequencesAssignmentOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_sequences_assignment_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequencesAssignmentOutputRepresentation

Output representation showing the status of the assigned sequence pattern values.

- 
- 
- 

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<[`ConnectApi.SequenceErrorOutputRepresentation`](./apex_connectapi_output_sequence_error_output.htm.md)> | Error encountered during the processing of the API request. | 65.0 |
| `sequencesAssignment` | List<[`ConnectApi.SequencesAssignmentResultOutputRepresentation`](./apex_connectapi_output_sequences_assignment_result_output.htm.md)> | Details of the sequence pattern values assignment. | 65.0 |
| `status` | `SequenceResponseStatusEnum` | Status of the sequence policy assignment. Valid values are: `PartialSuccess` `Success` `Failed` | 65.0 |

=== ARTICLE: apex_connectapi_output_sequences_assignment_result_output.htm ===
---
page_id: apex_connectapi_output_sequences_assignment_result_output.htm
title: ConnectApi.SequencesAssignmentResultOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_sequences_assignment_result_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.SequencesAssignmentResultOutputRepresentation

Output representation of the details of the assigned sequence values to target
    objects.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `errors` | List<`ConnectApi.SequenceErrorOutputRepresentation`> | Error encountered during the processing of the API request. | 65.0 |
| `isSuccess` | Boolean | Indicates whether the sequence pattern value was assigned (`true`) or not (`false`). | 65.0 |
| `sequencePatternValue` | String | Sequence pattern value assigned to the target object. | 65.0 |
| `sequencePolicyId` | String | ID of the sequence policy assigned to the target object. | 65.0 |
| `targetObjectId` | String | Record to which the sequence pattern value is assigned. | 65.0 |

=== ARTICLE: apex_connectapi_output_void_posted_credit_memo_output.htm ===
---
page_id: apex_connectapi_output_void_posted_credit_memo_output.htm
title: ConnectApi.VoidPostedCreditMemoOutputRepresentation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_connectapi_output_void_posted_credit_memo_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_output_classes.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi.VoidPostedCreditMemoOutputRepresentation

Output representation of the request to void a posted credit memo.

| Property Name | Type | Description | Available Version |
| --- | --- | --- | --- |
| `debitMemoId` | String | ID of the created debit memo. | 66.0 |
| `errors` | List<[`ConnectApi.ErrorResponse`](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_connectapi_output_error_response.htm)> | List of errors specific to this API request that were encountered during voiding the credit memo. | 66.0 |
| `isSuccess` | Boolean | Indicates whether the API request was successful (`true`) or not (`false`). | 66.0 |
| `statusURL` | String | Status URL for tracking this operation. | 66.0 |

=== ARTICLE: apex_namespace_InvoiceWriteOff.htm ===
---
page_id: apex_namespace_InvoiceWriteOff.htm
title: InvoiceWriteOff Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_InvoiceWriteOff.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# InvoiceWriteOff Namespace

Create credit memos with the total charge amount on the invoice as the write-off amount
    and close the invoice.

The `InvoiceWriteOff` namespace includes these classes.

    

## Usage

      
      

You need the Billing Operations User or Credit Memo Operations User permission set to
        access this namespace.

    

- 
**[WriteOffInvoiceInput Class](./apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceInput)**  

Contains invoice details that are used for the request to write off an     invoice.

- 
**[WriteOffInvoiceInputList Class](./apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceInputList)**  

Contains invoice details to write off a list of posted invoices.

- 
**[WriteOffInvoiceResponse Class](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponse)**  

Contains properties to store the response details to the request to write off a posted     invoice.

- 
**[WriteOffInvoiceResponseError Class](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError)**  

Contains properties to store the error response that's associated with a request to write     off a posted invoice.

- 
**[WriteOffInvoiceResponseList Class](./apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm.md#apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList)**  

Contains properties to store the response details of the list of invoices that are     written off.

=== ARTICLE: apex_namespace_IssueCreditMemo.htm ===
---
page_id: apex_namespace_IssueCreditMemo.htm
title: IssueCreditMemo Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_IssueCreditMemo.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# IssueCreditMemo Namespace

Issue credit memos from disputed invoices. Use this namespace to create and apply credit
    memos against invoices or invoice lines based on dispute adjustments.

You can access this namespace if Dispute Management is enabled in Billing.

The
          `IssueCreditMemo` namespace includes these
      classes.

- 
**[CreditLineRequestInputRepresentations Class](./apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations)**  

Represents a single line-level credit request. Specifies the invoice line to credit, the amount to apply, and an optional description.

- 
**[CreditRequestInputRepresentations Class](./apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditRequestInputRepresentations)**  

Represents a credit request for an invoice. Contains invoice and dispute identifiers, total credit amount, category, and line-level credit details for issuing a credit memo.

- 
**[CreditResponseOutputRepresentations Class](./apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm.md#apex_class_IssueCreditMemo_CreditResponseOutputRepresentations)**  

Represents the result of a credit memo operation. Indicates success or failure and any additional information or message.

=== ARTICLE: apex_namespace_RulesAppln.htm ===
---
page_id: apex_namespace_RulesAppln.htm
title: RulesAppln Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_RulesAppln.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# RulesAppln Namespace

Apply payments and credits to posted invoices by adhering to the specified rules.

The `RulesAppln` namespace includes these classes.

    

- 
**[RulesApplicationErrorResponse Class](./apex_class_RulesAppln_RulesApplicationErrorResponse.htm.md#apex_class_RulesAppln_RulesApplicationErrorResponse)**  

Contains properties to store error details that occurred during the rules application.

- 
**[RulesApplicationResponse Class](./apex_class_RulesAppln_RulesApplicationResponse.htm.md#apex_class_RulesAppln_RulesApplicationResponse)**  

Contains properties to store the response details for the rules application request.

- 
**[RulesApplicationSummaryResponse Class](./apex_class_RulesAppln_RulesApplicationSummaryResponse.htm.md#apex_class_RulesAppln_RulesApplicationSummaryResponse)**  

Contains properties to store the summary details of the rules application, including payment and credit memo counts and application statistics.

=== ARTICLE: billing_apex_input_classes.htm ===
---
page_id: billing_apex_input_classes.htm
title: ConnectApi Input Classes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_apex_input_classes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi Input Classes

Billing includes these Apex input classes.

- 
**[ConnectApi.ApplicationsRequest](./apex_connectapi_input_credit_memo_apply_application.htm.md)**  

Connect API representation of an application item input request for credit memo apply api

- 
**[ConnectApi.BillingAddressRequest](./apex_connectapi_input_address.htm.md)**  

Input representation of the details of an address.

- 
**[ConnectApi.BillingScheduleRecoveryInputRepresentation](./apex_connectapi_input_billing_schedule_recovery.htm.md)**  

Input representation of the details of the billing schedules to recover the associated     invoice.

- 
**[ConnectApi.ConvertNegativeInvoiceLinesInputRequest](./apex_connectapi_input_convert_negative_invoice_lines.htm.md)**  

Input representation of the request details to convert a negative invoice line into a     credit.

- 
**[ConnectApi.CreditDetailsApplyInput](./apex_connectapi_input_credit_memo_line_application.htm.md)**  

Input representation of the request to specify one or more applications to apply a credit     memo line for, with each application representing an invoice line.

- 
**[ConnectApi.CreditInvoiceInputRequest](./apex_connectapi_input_credit_invoice.htm.md)**  

Input representation of the details of the request to create a credit memo.

- 
**[ConnectApi.CreditInvoiceInvoiceLine](./apex_connectapi_input_credit_invoice_invoice_line.htm.md)**  

Input representation of the details of the invoice lines to be credited.

- 
**[ConnectApi.CreditInvoiceInvoiceLineTax](./apex_connectapi_input_credit_invoice_invoice_line_tax.htm.md)**  

Input representation of the details of the tax lines to be created manually for the     invoice line.

- 
**[ConnectApi.CreditMemoAddressesInputRequest](./apex_connectapi_input_credit_memo_addresses.htm.md)**  

Input representation of the details of the billing and shipping addresses.

- 
**[ConnectApi.CreditMemoApplyInputRequest](./apex_connectapi_input_credit_memo_apply.htm.md)**  

Input representation of the request to apply a credit memo to an invoice.

- 
**[ConnectApi.CreditMemoLineApplyInput](./apex_connectapi_input_credit_memo_line_apply.htm.md)**  

Input representation of the details of the request to apply a credit memo line to an     invoice line.

- 
**[ConnectApi.CreditMemoLineUnapplyInput](./apex_connectapi_input_credit_memo_line_unapply.htm.md)**  

Input representation of the details of the request to unapply a credit memo line from an     invoice line.

- 
**[ConnectApi.CreditMemoUnapplyInputRequest](./apex_connectapi_input_credit_memo_unapply.htm.md)**  

Input representation of the request to unapply a credit memo from an invoice.

- 
**[ConnectApi.InvoiceDraftToPostedInputRequest](./apex_connectapi_input_invoice_draft_to_posted.htm.md)**  

Input representation of the details of the draft invoice that’s posted.

- 
**[ConnectApi.InvoiceInputRepresentation](./apex_connectapi_input_invoice.htm.md)**  

Input representation of the details of the billing schedule.

- 
**[ConnectApi.PaymentLineApplyRequest](./apex_connectapi_input_payment_line_apply.htm.md)**  

Input representation of the payment line details. This representation covers details on     allocation of a payment to a specific invoice line. It also provides additional context through     optional fields, such as associated account and effective date.

- 
**[ConnectApi.PaymentLineUnapplyRequest](./apex_connectapi_input_payment_line_unapply.htm.md)**  

Input representation of the payment line details. This representation covers fields that     you can specify to revert a payment line application.

- 
**[ConnectApi.RefundLineApplyRequest](./apex_connectapi_input_refund_line_apply.htm.md)**  

Input representation of the details of a transaction refund request. This representation     outlines the properties of a refund, including the refund amount and ID of the payment or credit     memo record that the refund is applied to.

- 
**[ConnectApi.SequenceGapReconciliationInputRepresentation](./apex_connectapi_input_sequence_gap_reconciliation.htm.md)**  

The details of the input used to identify and reconcile gaps in sequence values based on the sequence policy or target object.

- 
**[ConnectApi.SequencesAssignmentInputRepresentation](./apex_connectapi_input_sequences_assignment.htm.md)**  

The details of the target objects to which the sequence pattern values are assigned.

- 
**[ConnectApi.StandaloneCreditMemoChargeInputRequest](./apex_connectapi_input_standalone_credit_memo_charge.htm.md)**  

Input representation of the details of the charge lines of a credit memo.

- 
**[ConnectApi.StandaloneCreditMemoInputRequest](./apex_connectapi_input_standalone_credit_memo.htm.md)**  

Input representation of the details required to create a standalone credit     memo.

- 
**[ConnectApi.StandaloneCreditMemoTaxInputRequest](./apex_connectapi_input_standalone_credit_memo_tax.htm.md)**  

Connect API representation of Tax input request

- 
**[ConnectApi.VoidPostedCreditMemoInputRepresentation](./apex_connectapi_input_void_posted_credit_memo.htm.md)**  

Input representation of the details of a credit memo to be voided.

=== ARTICLE: billing_apex_interface_TaxEngineAdapter_Example.htm ===
---
page_id: billing_apex_interface_TaxEngineAdapter_Example.htm
title: TaxEngineAdapter Example Implementation
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_apex_interface_TaxEngineAdapter_Example.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_tax_engine_adapter_interface_for_standard_tax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxEngineAdapter Example Implementation

Refer to the example implementation of the `TaxEngineAdapter` interface to accept information from a tax engine and
        evaluate the information to define tax details.

        

## Namespace

            
            

See [commercetax](./apex_namespace_commercetax.htm.md)
                namespace to view the list of available classes.

        

        

## Usage

            
            

The `TaxEngineAdapter` interface accepts information
                from the tax engine through the `TaxEngineContext`
                class. The interface evaluates the information to define tax in the response with
                details, such as tax amount and addresses. The response is used to update and create
                entities in the Salesforce org.

        

        

## Considerations

From Winter ’26, the available state and country
                values from orgs that are configured with [State and Country/Territory Picklists](https://help.salesforce.com/s/articleView?id=xcloud.admin_state_country_picklists_configure.htm&language=en_US) are
                also supported.

        

## Example

            

Use these steps to build a sample tax adapter implementation. Each tax adapter
                implementation varies based on your implementation requirements. Customize this
                example to suit your business requirements. 

            

See [Tax Engine Reference
                    Gateway Adapter](https://github.com/salesforce-misc/salesforce-tax-engine-reference-gateway-adapters) for reference implementations of a tax engine
                adapter.

            
                
- 

Get the tax rates from the created custom object. See [TaxEngineAdapter
                            Interface](./billing_tax_engine_adapter_interface_for_standard_tax.htm.md).

                
- 
                    

The custom adapter class implements the `TaxEngineAdapter` interface. The `processRequest` method takes an instance of `TaxEngineContext` class and returns a response
                        with the calculated tax details through the `TaxDetailsResponse` class or an error response through the
                            `ErrorResponse` class.

                    

```
global virtual class StandardTaxAdapter implements commercetax.TaxEngineAdapter {
    global commercetax.TaxEngineResponse processRequest(commercetax.TaxEngineContext taxEngineContext) {
        commercetax.RequestType requestType = taxEngineContext.getRequestType();

        // Map of tax field name to the value of the corresponding entity field (EntityFieldName) at header level
        Map<String, Object> customTaxAttributeHeaderLevelMap = new Map<String, Object>();
        // Map of tax field name to the value of the corresponding entity field (EntityFieldName) at line level
        Map<String, Object> customTaxAttributeLineLevelMap = new Map<String, Object>();
        // Map of tax field name to the value of the corresponding entity field (EntityFieldName) at line tax level
        Map<String, Object> customTaxAttributeLineTaxLevelMap = new Map<String, Object>();

        commercetax.CustomTaxAttributesResponse customTaxAttributeHeaderLevelResponse = new commercetax.CustomTaxAttributesResponse();
        commercetax.CustomTaxAttributesResponse customTaxAttributeLineLevelResponse = new commercetax.CustomTaxAttributesResponse();
        commercetax.CustomTaxAttributesResponse customTaxAttributeLineTaxLevelResponse = new commercetax.CustomTaxAttributesResponse();

        customTaxAttributeHeaderLevelResponse.setData(customTaxAttributeHeaderLevelMap);
        customTaxAttributeLineLevelResponse.setData(customTaxAttributeLineLevelMap);
        customTaxAttributeLineTaxLevelResponse.setData(customTaxAttributeLineTaxLevelMap);

        commercetax.CalculateTaxRequest request = (commercetax.CalculateTaxRequest) taxEngineContext.getRequest();
        if (request.documentCode == null) {
            return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '404', 'documentCode  is mandatory');
        }
        if (request.documentCode == 'TaxEngineError') {
            return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '504', 'documentCode  - not supported');
        }
        if (request.documentCode == 'simulateUnhandledExceptionInAdapter') {
            Integer foo = 5 / 0;
        }
        if (request.documentCode == 'simulateValidationFailureInAdapter') {
            return new commercetax.ErrorResponse(
                commercetax.resultcode.TaxEngineError,
                '400',
                'validations for documentCode failed in adapter'
            );
        }
        if (request.documentCode == 'simulateMalformedErrorInAdapter') {
            return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, null, 'malformed adapter error response');
        }
        if (request.documentCode == 'simulateTaxEngineProcessFailure') {
            return new commercetax.ErrorResponse(commercetax.resultcode.TaxEngineError, '500', 'Tax Engine couldnt process your request');
        }
        if (request.documentCode == 'simulateReferenceDocumentCodeMissing') {
            return new commercetax.ErrorResponse(commercetax.resultcode.ReferenceDocumentCodeMissing, '400', 'Ref Document Code not found');
        }

        if (requestType == commercetax.RequestType.CalculateTax) {
            commercetax.calculatetaxtype type = request.taxtype;
            String docCode = '';
            if (request.DocumentCode == 'simulateEmptyDocumentCode')
                docCode = '';
            else if (request.DocumentCode != null)
                docCode = request.DocumentCode;
            else if (request.ReferenceEntityId != null)
                docCode = request.ReferenceEntityId;
            else
                docCode = String.valueOf(getRandomInteger(0, 2147483647));
            commercetax.CalculateTaxResponse response = new commercetax.CalculateTaxResponse();
            response.setCustomTaxAttributes(customTaxAttributeHeaderLevelResponse);
            if (request.isCommit == true) {
                response.setStatus(commercetax.TaxTransactionStatus.Committed);
            } else {
                response.setStatus(commercetax.TaxTransactionStatus.Uncommitted);
            }

            if (request.shouldVoidTax) {
                if (request.documentCode.startsWith('simulateCalculateWhenRefDocIsLocked')) {
                    response.setDocumentCode(docCode);
                    response.setReferenceDocumentCode(request.referenceDocumentCode);
                    if (request.taxTransactionType == null) {
                        response.setTaxTransactionType(commercetax.TaxTransactionType.Debit);
                    } else {
                        response.setTaxTransactionType(request.taxTransactionType);
                    }
                } else if (request.documentCode.startsWith('simulateRandomRefDocumentCode')) {
                    response.setDocumentCode(docCode);
                    response.setReferenceDocumentCode('simulateRandomRefDocumentCode2');
                    response.setTaxTransactionType(request.taxTransactionType);
                } else if (request.documentCode.startsWith('simulateRandomCode')) {
                    response.setDocumentCode('simulateRandomCode2');
                    response.setReferenceDocumentCode(null);
                    response.setTaxTransactionType(commercetax.TaxTransactionType.Void);
                } else {
                    response.setDocumentCode(request.referenceDocumentCode);
                    response.setReferenceDocumentCode(null);
                    response.setTaxTransactionType(commercetax.TaxTransactionType.Void);
                }
            } else {
                response.setDocumentCode(docCode);
                response.setReferenceDocumentCode(request.referenceDocumentCode);

                if (request.taxTransactionType == null) {
                    response.setTaxTransactionType(commercetax.TaxTransactionType.Debit);
                } else {
                    response.setTaxTransactionType(request.taxTransactionType);
                }
            }

            response.setTaxType(type);
            response.setStatusDescription('statusDescription');
            if (request.sellerDetails.code == 'testSellerCode') {
                response.setDescription('SellerCode fetched from TaxEngine entity');
            } else {
                response.setDescription('description');
            }
            response.setEffectiveDate(system.now());
            if (request.transactionDate == null) {
                response.setTransactionDate(system.now());
            } else {
                response.setTransactionDate(request.transactionDate);
            }

            if (request.currencyIsoCode == null || request.currencyIsoCode == '') {
                response.setCurrencyIsoCode('USD');
            } else {
                response.setCurrencyIsoCode(request.currencyIsoCode);
            }
            response.setReferenceEntityId(request.ReferenceEntityId);
            Double totalTax = 0.0;
            Double totalAmount = 0.0;
            Map<String, Double> countryTaxRateMap = getTaxes(request.lineItems);
            List<commercetax.LineItemResponse> lineItemResponses = new List<commercetax.LineItemResponse>();
            for (Commercetax.TaxLineItemRequest lineItem : request.lineItems) {
                String country = getCountryFromLineItem(lineItem);
                if (country == null) {
                    return new commercetax.ErrorResponse(
                        commercetax.resultcode.TaxEngineError,
                        '400',
                        'Country is mandatory for each line item'
                    );
                }

                Double taxRate = countryTaxRateMap.get(country);
                if (taxRate == null) {
                    return new commercetax.ErrorResponse(
                        commercetax.resultcode.TaxEngineError,
                        '404',
                        'No tax rate found for the specified country: ' + country
                    );
                }
                commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();
                if (request.DocumentCode == 'SetsNullForResponseWithoutException') {
                    addressesRes.setShipFrom(null);
                    addressesRes.setShipTO(null);
                    addressesRes.setSoldTo(null);
                } else {
                    setAddresses(addressesRes, lineItem);
                    //System.debug('Line item addresses: ' + addressesRes);
                }
                //System.debug('ProductSKU: ' + lineItem.productSKU);
                //System.debug('ReferenceDocumentCode: ' + lineItem.referenceDocumentCode);
                commercetax.LineItemResponse lineItemResponse = new commercetax.LineItemResponse();
                lineItemResponse.setCustomTaxAttributes(customTaxAttributeLineLevelResponse);
                Double totalLineTax = 0;
                List<commercetax.TaxDetailsResponse> taxDetailsResponses = new List<commercetax.TaxDetailsResponse>();
                for (integer i = 0; i < 1; i++) {
                    Integer rate = 1;
                    Double taxableAmount = lineItem.amount;
                    commercetax.TaxDetailsResponse taxDetailsResponse = new commercetax.TaxDetailsResponse();
                    taxDetailsResponse.setRate(Double.valueOf(rate));
                    taxDetailsResponse.setTaxableAmount(taxableAmount);
                    Double tax = taxableAmount * rate;
                    totalLineTax += tax;
                    taxDetailsResponse.setTax(taxableAmount * rate);
                    taxDetailsResponse.setExemptAmount(0);
                    taxDetailsResponse.setExemptReason('exemptReason');
                    taxDetailsResponse.setTaxRegionId('taxRegionId');
                    taxDetailsResponse.setTaxId(String.valueOf(getRandomInteger(0, 2323233)));
                    taxDetailsResponse.setSerCode('serCode');
                    taxDetailsResponse.setCustomTaxAttributes(customTaxAttributeLineTaxLevelResponse);
                    taxDetailsResponse.setTaxAuthorityTypeId('taxAuthorityTypeId');
                    if (request.DocumentCode == 'SetsNullForResponseWithoutException') {
                        taxDetailsResponse.setImposition(null);
                    } else {
                        commercetax.ImpositionResponse imposition = new commercetax.ImpositionResponse();
                        imposition.setSubType('subtype');
                        imposition.setType('type');
                        taxDetailsResponse.setImposition(imposition);
                    }

                    if (request.DocumentCode == 'SetsNullForResponseWithoutException') {
                        taxDetailsResponse.setJurisdiction(null);
                    } else {
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
                totalTax += totalLineTax;
                totalAmount += lineItem.amount;

                if (request.DocumentCode == 'SetsNullForResponseWithException') {
                    lineItemResponse.setAmountDetails(null);
                } else {
                    commercetax.AmountDetailsResponse amountResponse = new commercetax.AmountDetailsResponse();
                    amountResponse.setTotalAmountWithTax(totalTax + totalAmount);
                    amountResponse.setExemptAmount(0);
                    amountResponse.setTotalAmount(totalAmount);
                    amountResponse.setTaxAmount(totalTax);
                    lineItemResponse.setAmountDetails(amountResponse);
                }
                lineItemResponse.setEffectiveDate(system.now());
                lineItemResponse.setTaxCode(lineItem.taxCode);
                lineItemResponse.setProductCode(lineItem.ProductCode);
                lineItemResponse.setLineNumber(lineItem.linenumber);
                lineItemResponse.setIsTaxable(true);
                lineItemResponse.setQuantity(lineItem.quantity);
                if (request.DocumentCode == 'SetsNullForResponseWithoutException') {
                    lineItemResponse.setAddresses(null);
                } else {
                    lineItemResponse.setAddresses(addressesRes);
                }
                lineItemResponses.add(lineItemResponse);
            }
            if (request.DocumentCode == 'SetsNullForResponseWithException') {
                lineItemResponses.add(null);
            }
            if (request.documentCode == 'nolines') {
                // logic to skip adding lines to response
            } else {
                response.setLineItems(lineItemResponses);
            }
            if (request.DocumentCode == 'SetsNullForResponseWithException') {
                response.setAmountDetails(null);
            } else {
                commercetax.AmountDetailsResponse headerAmountResponse = new commercetax.AmountDetailsResponse();
                headerAmountResponse.setTotalAmountWithTax(totalTax + totalAmount);
                headerAmountResponse.setExemptAmount(0);
                headerAmountResponse.setTotalAmount(totalAmount);
                headerAmountResponse.setTaxAmount(totalTax);
                response.setAmountDetails(headerAmountResponse);
            }
            commercetax.AddressesResponse addressesRes = new commercetax.AddressesResponse();
            commercetax.AddressResponse addRes = new commercetax.AddressResponse();
            addRes.setLocationCode('street, city, state, country, postalCode');
            addressesRes.setShipFrom(addRes);
            addressesRes.setShipTO(addRes);
            addressesRes.setSoldTo(addRes);
            response.setAddresses(addressesRes);
            return response;
        } else
            return null;
    }

    public static Integer getRandomInteger(Integer min, Integer max) {
        return min + (Integer.valueOf(Math.random()) * (max - min));
    }

    // Method to get the tax rates for the line items based on the address country codes
    private Map<String, Double> getTaxes(List<commercetax.TaxLineItemRequest> lineItems) {
        Set<String> countryCodes = new Set<String>();
        // Collecting all unique the country codes
        for (commercetax.TaxLineItemRequest lineItem : lineItems) {
            String country = getCountryFromLineItem(lineItem);
            if (country != null) {
                countryCodes.add(country);
            }
        }
        // Query tax rates for the unique country codes and store it in a map
        Map<String, Double> countryTaxRateMap = new Map<String, Double>();
        if (!countryCodes.isEmpty()) {
            // Query the tax rate from the custom object based on the country code
            List<CountryTaxRate__c> taxRates = [
                SELECT Country_Code__c, Tax_Rate__c
                FROM CountryTaxRate__c
                WHERE Country_Code__c IN :countryCodes
            ];
            for (CountryTaxRate__c taxRate : taxRates) {
                countryTaxRateMap.put(taxRate.Country_Code__c, taxRate.Tax_Rate__c);
            }
        }
        return countryTaxRateMap;
    }
    // Method to retrieve the country for the line item
    private String getCountryFromLineItem(commercetax.TaxLineItemRequest lineItem) {
        if (lineItem.addresses != null) {
            commercetax.TaxAddressRequest addressRequest = lineItem.addresses.shipTo;
            if (addressRequest != null && addressRequest.country != null) {
                return addressRequest.country;
            }
        }
        return null;
    }

    // Method to set addresses in the line item response
    private void setAddresses(commercetax.AddressesResponse addressesRes, Commercetax.TaxLineItemRequest lineItem) {
        commercetax.LineTaxAddressesRequest addressesReq = lineItem.addresses;
        if (addressesReq == null) {
            return;
        }
        addressesRes.setShipFrom(getShipFromAddressRes(addressesReq));
        addressesRes.setShipTo(getShipToAddressRes(addressesReq));
        addressesRes.setSoldTo(getSoldToAddressRes(addressesReq));
    }

    private commercetax.AddressResponse getShipFromAddressRes(commercetax.LineTaxAddressesRequest addressesReq) {
        return getAddressRes(addressesReq.shipFrom);
    }

    private commercetax.AddressResponse getShipToAddressRes(commercetax.LineTaxAddressesRequest addressesReq) {
        return getAddressRes(addressesReq.shipTo);
    }

    private commercetax.AddressResponse getSoldToAddressRes(commercetax.LineTaxAddressesRequest addressesReq) {
        if (addressesReq.soldTo != null) {
            return getAddressRes(addressesReq.soldTo);
        } else {
            return getAddressRes(addressesReq.billTo);
        }
    }

    private commercetax.AddressResponse getAddressRes(commercetax.TaxAddressRequest addressReq) {
        if (addressReq == null) {
            return null;
        }

        commercetax.AddressResponse addressRes = new commercetax.AddressResponse();

        List<String> addressEle = new List<String>();
        if (addressReq.street != null)
            addressEle.add(addressReq.street);
        if (addressReq.city != null)
            addressEle.add(addressReq.city);
        if (addressReq.state != null)
            addressEle.add(addressReq.state);
        if (addressReq.country != null)
            addressEle.add(addressReq.country);
        if (addressReq.postalCode != null)
            addressEle.add(addressReq.postalCode);

        addressRes.setLocationCode(String.join(addressEle, ', '));
        return addressRes;
    }
}
```

                

                
- Select `StandardTaxAdapter` as the provider
                    when you create a tax engine record in your org.

=== ARTICLE: billing_apex_output_classes.htm ===
---
page_id: billing_apex_output_classes.htm
title: ConnectApi Output Classes
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_apex_output_classes.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi Output Classes

Billing includes these Apex output classes.

- 
**[ConnectApi.AppliedCreditResponse](./apex_connectapi_output_credit_memo_line_applied_response.htm.md)**  

Output representation of the list of applied credit memo line results.

- 
**[ConnectApi.ApplyCreditResults](./apex_connectapi_output_credit_memo_apply_list_output.htm.md)**  

Output representation of the list of applied credit memo results.

- 
**[ConnectApi.ApplyCreditResult](./apex_connectapi_output_credit_memo_apply_output.htm.md)**  

Connect API representation of credit memo apply output result

- 
**[ConnectApi.BillingScheduleRecoveryResult](./apex_connectapi_output_billing_schedule_recovery_output.htm.md)**  

Output representation of the details of the recovered billing schedules.

- 
**[ConnectApi.BillingScheduleRecoveryResults](./apex_connectapi_output_billing_schedule_recovery_list_output.htm.md)**  

Output representation of the recovered details of the billing schedules and associated     invoice.

- 
**[ConnectApi.CreditMemoLineAppliedResponse](./apex_connectapi_output_credit_memo_line_applied.htm.md)**  

Output representation of the list of applied credit memo line results.

- 
**[ConnectApi.CreditMemoLineUnappliedResponse](./apex_connectapi_output_credit_memo_line_unapplied.htm.md)**  

Output representation of the details of the credit memo line invoice line record with the     status of the request.

- 
**[ConnectApi.ConvertNegativeInvoiceLinesResult](./apex_connectapi_output_convert_negative_invoice_lines_output.htm.md)**  

Output representation of the details of the credit memo along with the status of the     request.

- 
**[ConnectApi.InvoiceBatchDraftToPostedResult](./apex_connectapi_output_invoice_batch_draft_to_posted_output.htm.md)**  

Output representation of the batch update details of the invoices from `Draft` to `Posted`       status.

- 
**[ConnectApi.InvoiceRecoveryResult](./apex_connectapi_output_invoice_recovery_output.htm.md)**  

Output representation of the details of the recovered invoice and billing     schedules.

- 
**[ConnectApi.PaymentLineApplyResponse](./apex_connectapi_output_payment_line_apply_output.htm.md)**  

Output representation of the details of the applied payment line. The details include the     ID of the payment record and date when the payment line was applied.

- 
**[ConnectApi.PaymentLineUnapplyResponse](./apex_connectapi_output_payment_line_unapply_output.htm.md)**  

Output representation of the details of the reversed payment line application. The     details include the ID of the payment line record and date when the payment line application was     reversed.

- 
**[ConnectApi.ReferenceLineError](./apex_connectapi_output_reference_line_error.htm.md)**  

Output representation of the details of the line level errors.

- 
**[ConnectApi.RefundLineApplyResponse](./apex_connectapi_output_refund_line_apply_output.htm.md)**  

Output representation of the details of an applied refund. This representation includes     the properties of a refund line, such as the date when the refund is applied against a payment     and ID of the refund line record.

- 
**[ConnectApi.RevenueAsyncLineLevelOutputResponse](./apex_connectapi_output_revenue_async_line_level.htm.md)**  

Output representation of the result of the API request for the async line level     operations.

- 
**[ConnectApi.RevenueAsyncRepresentation](./apex_connectapi_output_revenue_async.htm.md)**  

Output representation of the result of the API request with the request     identifier.

- 
**[ConnectApi.SequenceErrorOutputRepresentation](./apex_connectapi_output_sequence_error_output.htm.md)**  

Output representation of the error response that's associated with a request to create or     update a sequence policy, or assign sequences.

- 
**[ConnectApi.SequenceGapReconciliationOutputRepresentation](./apex_connectapi_output_sequence_gap_reconciliation_output.htm.md)**  

Output representation of the details of the sequence gap reconciliation.

- 
**[ConnectApi.SequenceGapReconciliationErrorOutputRepresentation](./apex_connectapi_output_sequence_gap_reconciliation_error_output.htm.md)**  

List of errors encountered during the processing of the API request.

- 
**[ConnectApi.SequencesAssignmentOutputRepresentation](./apex_connectapi_output_sequences_assignment_output.htm.md)**  

Output representation showing the status of the assigned sequence pattern values.

- 
**[ConnectApi.SequencesAssignmentResultOutputRepresentation](./apex_connectapi_output_sequences_assignment_result_output.htm.md)**  

Output representation of the details of the assigned sequence values to target     objects.

- 
**[ConnectApi.UnapplyCreditResult](./apex_connectapi_output_credit_memo_unapply_output.htm.md)**  

Output representation of the details of the credit memo invoice application record with     the status of the request.

- 
**[ConnectApi.VoidPostedCreditMemoOutputRepresentation](./apex_connectapi_output_void_posted_credit_memo_output.htm.md)**  

Output representation of the request to void a posted credit memo.

=== ARTICLE: billing_apex_reference.htm ===
---
page_id: billing_apex_reference.htm
title: Billing Apex Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_apex_reference.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Apex Reference

Billing provides the `ConnectApi`
      namespace (also called Connect in Apex) that contains classes for accessing the same
      capabilities that are available in the Billing Business APIs. Additionally, you can use other
      built-in Apex classes and interfaces grouped by namespace.

    

This table lists the available Billing Apex methods with the associated Connect REST API.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

          
            

            

          

        

      
| Apex Method | Connect REST API |
| --- | --- |
| [`convertNegativeInvoiceLines(ConvertNegativeInvoiceLinesInput, invoiceId)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_convertNegativeInvoiceLines) | [`Negative Invoice Lines to Credit Conversion (POST)`](./connect_resources_convert_negative_invoice_lines_to_credit.htm.md) |
| [`generateInvoices(inputRequest)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_generateInvoices_1) | [`Invoices By Using Billing Schedules (POST)`](./connect_resources_create_invoices_from_billing_schedules.htm.md) |
| [`recoverBillingSchedules(inputRequest)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_recoverBillingSchedules_1) | [`Billing Schedule Recovery List (POST)`](./connect_resources_recover_billing_schedules.htm.md) |
| [`creditInvoice(CreditInvoiceInput, invoiceId)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_creditInvoice_1) | [`Credit Memo Create and Apply (POST)`](./connect_resources_create_and_apply_a_credit_memo.htm.md) |
| [`applyCreditMemos(CreditMemoApplyInput, creditMemoId)`](./apex_ConnectAPI_CreditMemoApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoApply_applyCreditMemos_1) | [`Credit Memo Apply List(POST)`](./connect_resources_credit_memo_apply.htm.md) |
| [`unapplyCreditMemos(CreditMemoUnapplyInput, creditMemoInvApplicationId)`](./apex_ConnectAPI_CreditMemoApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoApply_unapplyCreditMemos_1) | [`Credit Memo Unapply (POST)`](./connect_resources_credit_memo_invoice_application_unapply.htm.md) |
| [`applyCreditMemoLines(CreditMemoLineApplyInput, creditMemoLineId)`](./apex_ConnectAPI_CreditMemoLineApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoLineApply_applyCreditMemoLines_1) | [`Credit Memo Line Apply (POST)`](./connect_resources_credit_memo_line_level_apply.htm.md) |
| [`unapplyCreditMemoLines(CreditMemoLineUnapplyInput, creditMemoLineInvoiceLineId)`](./apex_ConnectAPI_CreditMemoLineApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoLineApply_unapplyCreditMemoLines_1) | [`Credit Memo Line Unapply (POST)`](./connect_resources_credit_memo_line_level_unapply.htm.md) |
| [`triggerInvoiceBatchDraftToPosted(invoiceBatchRunId)`](./apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm.md#apex_ConnectAPI_BatchInvoiceApplication_triggerInvoiceBatchDraftToPosted_1) | [`Invoices Batch Draft to Posted Status (POST)`](./connect_resources_batch_draft_invoices_to_posted.htm.md) |
| [`postDraftInvoices(inputRequest)`](./apex_ConnectAPI_HarmonizeBilling_static_methods.htm.md#apex_ConnectAPI_HarmonizeBilling_postDraftInvoices_1) | [`Invoice Draft to Posted Status (POST)`](./connect_resources_draft_to_posted_invoice.htm.md) |
| [`createCreditMemos(CreditMemoInputRequest)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_createCreditMemos_1) | [`Credit Memo Create and Apply (POST)`](./connect_resources_create_and_apply_a_credit_memo.htm.md) |
| [`voidPostedInvoice(invoiceId)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_voidPostedInvoice_1) | [`Posted Invoice Voidance (POST)`](./connect_resources_void_a_posted_invoice.htm.md) |
| [`calculateTax(calculateTax)`](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_ConnectAPI_TaxPlatform_static_methods.htm) | [`Tax Calculation (POST)`](./connect_resources_calculate_taxes.htm.md) |
| [`applyPaymentLine(PaymentLineApplyInput, paymentId)`](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_applyPaymentLine_1) | [`Payment Line Apply (POST)`](./connect_resources_payment_line_apply.htm.md) |
| [`unapplyPaymentLine(PaymentLineUnapplyInput, paymentId, paymentLineId)`](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_unapplyPaymentLine_1) | [`Payment Line Unapply (POST)`](./connect_resources_payment_line_unapply.htm.md) |
| [`applyRefundLine(RefundLineApplyInput, refundId)`](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_applyRefundLine_1) | [`Refund Line Apply (POST)`](./connect_resources_apply_refund_to_payment.htm.md) |
| [`reconcileSequences(sequenceGapReconciliationInputRepresentation)`](./apex_ConnectAPI_SequencingWithoutAura_static_methods.htm.md#apex_ConnectAPI_SequencingWithoutAura_reconcileSequences_1) | [`Sequence Gap Reconciliation (POST)`](./connect_resources_sequences_gap_reconciliation.htm.md) |
| [`sequenceAssignment(sequencesAssignmentInputRepresentation)`](./apex_ConnectAPI_SequencingWithoutAura_static_methods.htm.md#apex_ConnectAPI_SequencingWithoutAura_sequenceAssignment_1) | [`Sequence Assignment (POST)`](./connect_resources_sequences_assignment.htm.md) |
| [`voidPostedCreditMemo(VoidPostedCreditMemoInput, creditMemoId)`](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_voidPostedCreditMemo_1) | [`Void Posted Credit Memo (POST)`](./connect_resources_void_posted_credit_memo.htm.md) |

    

For more information about Apex classes that are available for Commerce Payments, see [CommercePayments Namespace](https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_commercepayments.htm).

  

- 
**[ConnectApi Namespace](./billing_connect_api_namespace.htm.md)**  

The `ConnectApi` namespace (also called Connect in         Apex) provides classes to manage credit applications and billing scenarios.

- 
**[InvoiceWriteOff Namespace](./apex_namespace_InvoiceWriteOff.htm.md)**  

Create credit memos with the total charge amount on the invoice as the write-off amount     and close the invoice.

- 
**[IssueCreditMemo Namespace](./apex_namespace_IssueCreditMemo.htm.md)**  

Issue credit memos from disputed invoices. Use this namespace to create and apply credit     memos against invoices or invoice lines based on dispute adjustments.

- 
**[RulesAppln Namespace](./apex_namespace_RulesAppln.htm.md)**  

Apply payments and credits to posted invoices by adhering to the specified rules.

- 
**[TaxEngineAdapter Interface](./billing_tax_engine_adapter_interface_for_standard_tax.htm.md)**  

Retrieves and evaluates the details from a tax engine to define tax         details.

=== ARTICLE: billing_business_api_overview.htm ===
---
page_id: billing_business_api_overview.htm
title: Billing Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_business_api_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Business APIs

Use the Billing Business APIs to manage credit application and to handle billing
    scenarios.

    
      

These sections list the available resources.

    

    

## Credits

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/invoicing/credit-memos/creditMemoId/actions/apply`](./connect_resources_credit_memo_apply.htm.md) (POST) | Adjust or correct already issued invoices by applying an existing credit memo to an invoice. |
| [`/commerce/invoicing/credit-memo-inv-applications/creditMemoInvApplicationId/actions/unapply`](./connect_resources_credit_memo_invoice_application_unapply.htm.md) (POST) | Unapply a credit memo from an invoice and return the invoice and the credit memo to their pre-application states. |
| [`/commerce/invoicing/credit-memo-lines/creditMemoLineId/actions/apply`](./connect_resources_credit_memo_line_level_apply.htm.md) (POST) | Adjust or correct already issued invoices by applying an existing credit memo line to an invoice line. |
| [`/commerce/invoicing/credit-memo-line-invoice-line/creditMemoLineInvoiceLineId/actions/unapply`](./connect_resources_credit_memo_line_level_unapply.htm.md) (POST) | Unapply a credit memo line from an invoice line and return the invoice line and the credit memo line to their pre-application states. |
| [`/commerce/invoicing/credit-memos/actions/generate`](./connect_resources_create_a_standalone_credit_memo.htm.md) (POST) | Create a credit memo without applying it to an invoice. You can credit the invoice at a later date. |
| [`/commerce/invoicing/invoices/invoiceId/actions/void`](./connect_resources_void_a_posted_invoice.htm.md) (POST) | Void a posted invoice to rebill the customer, if necessary. |
| [`/commerce/invoicing/invoices/invoiceId/actions/convert-to-credit`](./connect_resources_convert_negative_invoice_lines_to_credit.htm.md) (POST) | Convert a list of invoice lines with a negative amount into a posted credit memo. This conversion is applicable for a single invoice at a time. |
| [`/commerce/invoicing/invoices/invoiceId/actions/credit`](./connect_resources_create_and_apply_a_credit_memo.htm.md) (POST) | Create a credit memo and apply it to an invoice. The credit memo can fully or partially credit the invoice. |
| [`/commerce/invoicing/credit/collection/actions/post`](./connect_resources_post_draft_credit_memo.htm.md) (POST) | Post a draft credit memo to a credit memo record for review and approval. |
| [`/commerce/billing/credit-memos/creditMemoId/actions/void`](./connect_resources_void_posted_credit_memo.htm.md) (POST) | Void a credit memo in posted state. |

    

    

## Billing Schedules

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/invoicing/billing-schedules/actions/create`](./connect_resources_create_billing_schedules.htm.md) (POST) | Generate billing schedules for orders by using context service. |
| [`/commerce/invoicing/standalone/billing-schedules/actions/create`](./connect_resources_create_billing_schedules_from_any_transaction.htm.md) (POST) | Generate billing schedules from any internal or external transaction by using context service. |
| [`/commerce/invoicing/billing-schedules/collection/actions/recover`](./connect_resources_recover_billing_schedules.htm.md) (POST) | Recover the latest generated invoice associated with the billing schedules in the `Error` or `Processing` status. |
| [`/commerce/invoicing/actions/suspend-billing`](./connect_resources_suspend_billing.htm.md) (POST) | Suspend billing for billing schedule groups or an account for a predefined period. |
| [`/commerce/invoicing/actions/resume-billing`](./connect_resources_resume_billing.htm.md) (POST) | Resume billing for billing schedule groups or an account that’s currently on hold. |

    

    

## Invoices

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/invoicing/invoices/collection/actions/post`](./connect_resources_draft_to_posted_invoice.htm.md) (POST) | Update the status of the invoice from Draft to Posted. |
| [`/commerce/invoicing/invoice-batch-runs/invoiceBatchRunId/actions/draft-to-posted`](./connect_resources_batch_draft_invoices_to_posted.htm.md) (POST) | Update a batch of invoices from `Draft` to `Posted` status for a credit memo application. |
| [`/commerce/invoicing/invoices/collection/actions/preview`](./connect_resources_preview_invoices.htm.md) (POST) | Generate preview invoices, which includes the estimated tax amounts, for a billing transaction for the next two billing periods. |
| [`/commerce/invoicing/invoices/collection/actions/ingest`](./connect_resources_invoices_ingestion.htm.md) (POST) | Ingest or generate an invoice from an internal or external billing transaction data. |
| [`/commerce/billing/invoices/invoice-batch-docgen/invoiceBatchRunId/actions/actionName`](./connect_resources_invoice_batch_docgen.htm.md) (POST) | Asynchronously generate PDF documents for the invoices that are in the `Draft` or `Posted` status and are associated with an invoice batch run record. |
| [`/commerce/billing/invoices/invoice-batch-docgen/invoiceBatchRunId/actions/actionName`](./connect_resources_invoice_batch_docgen_retry.htm.md) (POST) | Asynchronously regenerate PDF documents for the invoices that are in the `Draft` or `Posted` status and failed in an earlier invoice batch run. |
| [`/commerce/invoicing/invoices/actions/write-off`](./connect_resources_write_off_invoices.htm.md) (POST) | Create credit memos with the total charge amount on the invoice as the write-off amount and close the invoice. |
| [`/commerce/invoicing/invoice-batch-runs/actions/send-email`](./connect_resources_send_email_for_invoice_batch_run.htm.md) (POST) | Send emails for the posted invoices of a specified invoice batch run ID. |
| [`/commerce/invoicing/invoices/collection/actions/generate`](./connect_resources_create_invoices_from_billing_schedules.htm.md) (POST) | Create an invoice for an account, order, or a list of billing schedules. |
| [`/revenue/billing/transactions/actions/apply`](./connect_resources_rules_application.htm.md) (POST) | Apply payments and credits to an account's invoices based on specified rules defined on the Billing Settings page. |
| [`/revenue/billing/document/actions/generate`](./connect_resources_generate_documents.htm.md) (POST) | Generate an invoice document for a record, and update any junction object record. |

    

    

## Invoice Scheduler

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/invoicing/invoice-schedulers`](./connect_resources_create_an_invoice_scheduler.htm.md) (POST) | Create or update an invoice scheduler to automatically generate invoices. Use the criteria and filters of the invoice scheduler to set up the invoice run schedules based on your requirements. |
| [`/commerce/invoicing/invoice-batch-runs/invoiceBatchRunId/actions/recover`](./connect_resources_recover_errored_invoices_batch_run.htm.md) (POST) | Recover records associated with a failed invoice run. Recovery is required only when billing schedules remain in the `Processing`, `Void In Progress`, or `Error` status. |

    

    

## Invoice Sequencing

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/connect/sequences/policy`](./connect_resources_create_sequence_policy.htm.md) (POST) | Create a sequence policy to configure a unique, sequential number for posted invoices or credit memos. |
| [`/connect/sequences/policy/sequencePolicyId`](./connect_resources_update_sequence_policies.htm.md) (PATCH) | Update the settings of a sequence policy that defines how unique, sequential numbers are generated by using specific patterns, values, and filters. |
| [`/connect/sequences/actions/assign`](./connect_resources_sequences_assignment.htm.md) (POST) | Assign sequence pattern values to objects based on the configured sequence policy. |
| [`/connect/sequences/gap-reconciliation`](./connect_resources_sequences_gap_reconciliation.htm.md) (POST) | Restore a missing sequence value identified by using this API in gapless-enabled sequences. This sequence value can be used later in the subsequent sequence policy numbering, ensuring there are no gaps. |

    

    

## Account Statement

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/revenue/billing/accounts/accountId/statement`](./connect_resources_generate_account_statement.htm.md) (POST) | Generate comprehensive account statement with transaction history and balance information. |

    

    

## Payments

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/billing/payments/paymentId/actions/apply`](./connect_resources_payment_line_apply.htm.md) (POST) | Allocate the balance of a payment to reduce the balance of an invoice. The response includes an ID of the payment line invoice or payment line invoice line that represents the payment balance allocated against the invoice. |
| [`/commerce/billing/payments/paymentId/paymentlines/paymentLineId/actions/unapply`](./connect_resources_payment_line_unapply.htm.md) (POST) | Revert the application of a payment line from an invoice, and return the payment and invoices to their preapplication state. Use this API to correct an input during the payment application process. |
| [`/commerce/billing/refunds/refundId/actions/apply`](./connect_resources_apply_refund_to_payment.htm.md) (POST) | Make a refund transaction against a payment. |

    

    

## Tax Calculation

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/taxes/actions/calculate`](./connect_resources_calculate_taxes.htm.md) (POST) | Calculate tax for a transaction. |
| [`/commerce/invoicing/invoices/collection/actions/calculate-estimated-tax`](./connect_resources_calculate_estimated_tax.htm.md) (POST) | Calculate estimated tax for invoices with invoice lines that have the `TaxProcessingStatus` as either `Pending` or `Estimated`. |

    

    

## Salesforce Commerce Payments API

      
      

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/commerce/payments/payment-methods`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=tokenizePaymentMethod) (POST) | Tokenize a payment method. |
| [`/commerce/payments/sales`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=salePayment) (POST) | Make a payment sale. |
| [`/commerce/payments/payments/paymentId/refunds`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=createPaymentRefund) (POST) | Create a refund for a payment. |
| [`/commerce/payments/authorizations`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=authorizePayment) (POST) | Authorize a payment. |
| [`/commerce/payments/authorizations/authorizationId/reversals`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=reverseAuthorization) (POST) | Reverse an authorized payment. |
| [`/commerce/payments/authorizations/authorizationId/captures`](https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/comm-ccs-payments-ref?meta=capturePayment) (POST) | Capture an authorized payment. |

    

  

- 
**[Billing Business API Limits](./billing_business_apis_limits.htm.md)**  

Learn about the default limits on the usage of the Billing business APIs.

- 
**[Resources](./billing_business_apis_resources.htm.md)**  

Learn more about the available Billing API resources.

- 
**[Request Bodies](./billing_business_apis_requests.htm.md)**  

Learn more about the available request bodies of Billing APIs.

- 
**[Response Bodies](./billing_business_apis_responses.htm.md)**  

Learn more about the available response bodies of Billing APIs.

#### See Also

- [*Connect REST API Developer Guide*: Introduction](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm)

=== ARTICLE: billing_business_apis_limits.htm ===
---
page_id: billing_business_apis_limits.htm
title: Billing Business API Limits
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_business_apis_limits.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Business API Limits

Learn about the default limits on the usage of the Billing business APIs.

    

        
          
            

          

          
            

          

        

      
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions |

  

    Refer to these default API limits and applicable recommendations to scale beyond these
      default limits.

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Limit | Value | Scale Recommendations |
| --- | --- | --- |
| The number of billing schedules that can be processed by the [Create Invoices By Using Billing Schedules API](./connect_resources_create_invoices_from_billing_schedules.htm.md). | 200 | Use Invoice Scheduler to scale up to 2000 invoice lines. See [Invoice Scheduler](https://help.salesforce.com/s/articleView?id=ind.billing_guided_setup_invoice.htm&language=en_US) or [Batch Invoice Scheduler (POST) API](./connect_resources_create_an_invoice_scheduler.htm.md). |
| The number of invoice lines that can be generated by the [Create Invoices By Using Billing Schedules API](./connect_resources_create_invoices_from_billing_schedules.htm.md). | 200 | Use Invoice Scheduler to scale up to 2000 invoice lines. See [Invoice Scheduler](https://help.salesforce.com/s/articleView?id=ind.billing_guided_setup_invoice.htm&language=en_US) or [Batch Invoice Scheduler (POST) API](./connect_resources_create_an_invoice_scheduler.htm.md). |
| The number of billing schedules that can be processed by the [Recover Billing Schedule List API](./connect_resources_recover_billing_schedules.htm.md). | 200 | Use this API to follow the default API limits. |
| The number of invoices that can be processed by the [Apply Credit Memos API](./connect_resources_credit_memo_apply.htm.md). | 300 | Use this API recursively to apply left-over credits after 300 invoice lines. |
| The number of invoice lines that can be processed by the [Apply Credit Memo Lines API](./connect_resources_credit_memo_line_level_apply.htm.md). | 300 | Use this API iteratively for every 300 invoice lines to support more than 300 invoice lines. |
| The number of invoices that can be processed by the [Create and Apply Credit Memos API](./connect_resources_create_and_apply_a_credit_memo.htm.md). | 300 | Use this API to follow the default API limits. The limits include the count for both charge and tax lines. |
| The number of credit memo lines of type Charge that can be created by the [Create a Standalone Credit Memo API](./connect_resources_create_a_standalone_credit_memo.htm.md). | 300 | Use this API to follow the default API limits. The limits include the count for both charge and tax lines. |
| The number of invoice lines that can be processed by the [Convert Negative Invoice Lines to Credits API](./connect_resources_convert_negative_invoice_lines_to_credit.htm.md), which excludes the number of associated invoice line taxes. | 300 | Use this API to follow the default API limits. The limits include the count for invoice charge lines only. |
| The number of billing transaction items that can be processed by the [Create Billing Schedules for Orders API](./connect_resources_create_billing_schedules.htm.md). | 1000 | This API supports creation of 1000 order lines as billing schedules. |
| The number of reference IDs that can be processed by the [Suspend Billing API](./connect_resources_suspend_billing.htm.md) and the [Resume Billing API](./connect_resources_resume_billing.htm.md). | 200 | Use this API to follow the default API limits. |
| The number of invoice lines that's supported by the [Invoice Draft to Posted Status API](./connect_resources_draft_to_posted_invoice.htm.md). | 200 | Use this API to follow the default API limits. |
| The number of records that can be processed by the [Invoice Ingestion API](./connect_resources_invoices_ingestion.htm.md). | 500 | Use this API to follow the default API limits. The limits include the count for all invoices, invoice lines, taxes, and address group records. |
| The number of invoice lines or billing schedules that can be processed by the [Invoice Preview API](./connect_resources_preview_invoices.htm.md). | 200 | Use this API to follow the default API limits. |
| The number of invoice lines that can be processed by the [Void a Posted Invoice API](./connect_resources_void_a_posted_invoice.htm.md). | 2000 | Use this API to follow the default API limits. |
| The number of invoices that can be processed by the [Posted Invoice List Write-Off API](./connect_resources_write_off_invoices.htm.md). | 300 | Use this API to follow the default API limits. |
| The number of invoice lines that can be generated on an invoice by the [Batch Invoice Scheduler (POST) API](./connect_resources_create_an_invoice_scheduler.htm.md). The number of records that can be recovered from a failed invoice run by the [Batch Invoice Run Recovery (POST) API](./connect_resources_recover_errored_invoices_batch_run.htm.md). | 2000 | Use this API to support the creation or recovery of up to 2,000 invoice lines on a single invoice. |
| The number of invoice lines that's supported by the [Batch Invoices Draft to Posted Status (POST) API](./connect_resources_batch_draft_invoices_to_posted.htm.md). | 2000 | Use this API to support 2000 invoice lines with no limit on the number of supported invoices. |
| The number of invoices that's supported by the [Tax Calculation API](./connect_resources_void_a_posted_invoice.htm.md). | 1 | Use this API to follow the default API limits. |
| The number of invoice lines that's supported by the [Tax Calculation API](./connect_resources_void_a_posted_invoice.htm.md). | 500 | The request can include 500 invoice lines. To avoid limit-related issues, test your TaxEngineAdapter Apex interface’s implementation to make sure that it adheres to the [Apex limit for total heap size](https://developer.salesforce.com/docs/atlas.en-us.264.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm). |
| The number of invoice lines that's supported by the Tax Calculation API interface when used with the [Invoice Creation API](./connect_resources_create_invoices_from_billing_schedules.htm.md). | 200 | The request can include 200 invoice lines. To avoid limit-related issues, test your TaxEngineAdapter Apex interface’s implementation to make sure that it adheres to the [Apex limit for total heap size](https://developer.salesforce.com/docs/atlas.en-us.264.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm). |
| The number of invoice lines that's supported by the Tax Calculation API interface when used with the [Invoice Batch Run API](./connect_resources_batch_draft_invoices_to_posted.htm.md). | 2000 | The request can include 2000 invoice lines. To avoid limit-related issues, test your TaxEngineAdapter Apex interface’s implementation to make sure that it adheres to the [Apex limit for total heap size](https://developer.salesforce.com/docs/atlas.en-us.264.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm). |
| The number of records that's supported by the [Payment Line Apply API](./connect_resources_void_a_posted_invoice.htm.md). | 1 | Payment supports application for either an Invoice or InvoiceLine record based on the settlement-level preferences. |
| The number of records that's supported by the [Payment Line Unapply API](./connect_resources_payment_line_unapply.htm.md). | 1 | Payment supports unapplication for either a PaymentLineInvoice or PaymentLineInvoiceLine record based on the settlement-level preferences. |

=== ARTICLE: billing_business_apis_requests.htm ===
---
page_id: billing_business_apis_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_business_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available request bodies of Billing APIs.

- 
**[Address Input](./connect_requests_address_input.htm.md)**  

Input representation of the details of an address.

- 
**[Addresses Input](./connect_requests_addresses_input.htm.md)**  

Input representation of the details of the addresses for calculating tax.

- 
**[Batch Invoice Filter Criteria Input](./connect_requests_batch_invoice_filter_criteria_input.htm.md)**  

Input representation of the filter criteria for an invoice batch run.

- 
**[Batch Invoice Scheduler Input](./connect_requests_batch_invoice_scheduler_input.htm.md)**  

Input representation of the details of the request to create an invoice     scheduler.

- 
**[Billing Schedule Recovery Input](./connect_requests_billing_schedule_recovery_input.htm.md)**  

Input representation of the details of the billing schedules to recover the associated     invoice.

- 
**[Context-Aware Billing Schedule](./connect_requests_context_aware_billing_schedule_input.htm.md)**  

Input representation of the billing transaction details.

- 
**[Standalone Billing Schedule Input](./connect_requests_context_aware_standalone_billing_schedule_input.htm.md)**  

Input representation of the request to create a billing schedule based on transaction     details. This representation includes the transaction and context service details.

- 
**[Standalone Billing Schedule Metadata Input](./connect_requests_context_aware_standalone_billing_schedule_metadata_input.htm.md)**  

Input representation of the metadata details to create a billing schedule. This     representation includes the name of the context definition and context mapping along with the     mapping details of the transaction, billing schedule, and billing schedule group.

- 
**[Convert Negative Invoice Lines Input](./connect_requests_convert_negative_invoice_lines_input.htm.md)**  

Input representation of the details of the request to convert a list of negative invoice     lines into a credit.

- 
**[Credit Invoice Input](./connect_requests_credit_invoice_input.htm.md)**  

Input representation of the details of the request to create a credit memo.

- 
**[Credit Invoice Line Input](./connect_requests_credit_invoice_line_input.htm.md)**  

Input representation of the details of the invoice lines to be credited.

- 
**[Credit Invoice Line Tax Input](./connect_requests_credit_invoice_line_tax_input.htm.md)**  

Input representation of the details of the tax lines to be created manually for the     invoice line.

- 
**[Credit Memo Addresses Input](./connect_requests_credit_memo_addresses_input.htm.md)**  

Input representation of the details of the billing and shipping addresses.

- 
**[Credit Memo Apply Input](./connect_requests_credit_memo_apply_input.htm.md)**  

Input representation of the request to apply a credit memo to an invoice.

- 
**[Credit Memo Apply Application Input](./connect_requests_credit_memo_apply_application_input.htm.md)**  

Input representation of the request to specify one or more applications to apply a credit     memo for, with each application representing an invoice.

- 
**[Credit Memo Draft to Posted Input](./connect_requests_credit_memo_draft_to_posted_input.htm.md)**  

Input representation of the request to post a draft credit memo.

- 
**[Credit Memo Unapply Input](./connect_requests_credit_memo_unapply_input.htm.md)**  

Input representation of the request to unapply a credit memo from an invoice.

- 
**[Credit Memo Line Apply Input](./connect_requests_credit_memo_line_apply_input.htm.md)**  

Input representation of the details of the request to apply a credit memo line to an     invoice line.

- 
**[Credit Memo Line Application Input](./connect_requests_credit_memo_line_application_input.htm.md)**  

Input representation of the request to specify one or more applications to apply a credit     memo line for, with each application representing an invoice line.

- 
**[Credit Memo Line Unapply Input](./connect_requests_credit_memo_line_unapply_input.htm.md)**  

Input representation of the details of the request to unapply a credit memo line from     an invoice line.

- 
**[Customer Details Input](./connect_requests_customer_details_input.htm.md)**  

Input representation of the customer details for tax calculation.

- 
**[Frequency Cadence Options](./connect_requests_frequency_cadence_options.htm.md)**  

Input representation of the frequency cadence options for an invoice     scheduler.

- 
**[Graph Record for Invoice Ingestion](./connect_requests_graph_record_input.htm.md)**  

A Graph record is an object that’s a part of the graph structure,       representing both the fields and relationships among different objects. Each record in the       graph can contain attributes, which are fields of the object, and references to other related       records.

- 
**[Invoice Draft To Posted Input](./connect_requests_draft_to_posted_invoice_input.htm.md)**  

Input representation of the details of the draft invoice that’s posted.

- 
**[Invoice Estimated Tax Calculation Input](./connect_requests_invoice_estimated_tax_calculation_input.htm.md)**  

Details of the invoice for which the estimated tadsfsefx must be calculated.

- 
**[Invoice Ingestion Input](./connect_requests_invoice_ingestion_input.htm.md)**  

Input representation of the details of the invoice to be processed. The details include     the tax processing status, user preferences for tax callouts, and associated object graph     representation.

- 
**[Invoice Input for Ingestion](./connect_requests_invoice_input_for_ingestion.htm.md)**  

Input representation of the details of the invoice that must be generated for or     ingested into Billing.

- 
**[Invoice Input](./connect_requests_invoice_input.htm.md)**  

Input representation of the details of the billing     schedule.

- 
**[Invoice Preview Input](./connect_requests_invoice_preview_input.htm.md)**  

Input representation of the details of the billing transaction that the preview invoices     are generated for.

- 
**[Line Item Input](./connect_requests_line_item_input.htm.md)**  

Input representation of the details of the line item for tax calculation.

- 
**[On-Demand Document Generation Input](./connect_requests_on_demand_doc_gen_input.htm.md)**  

Input representation of the details to generate a comprehensive on-demand document for     specified record types.

- 
**[Payment Line Apply Input](./connect_requests_payment_line_apply_input.htm.md)**  

Input representation of the payment line details. This representation       covers details on allocation of a payment to a specific invoice line. It also provides       additional context through optional fields such as associated account and effective     date.

- 
**[Payment Line Unapply Input](./connect_requests_payment_line_unapply_input.htm.md)**  

Input representation of the payment line details. This representation covers fields that     you can specify to revert a payment line application to their preapplication state.

- 
**[Payment Run Batch Filter Criteria Input](./connect_requests_payment_run_batch_filter_criteria_input.htm.md)**  

Input representation of the filter criteria for an invoice batch run. This representation     covers the criteria and sequence for filtering payment run details. It specifies the field and     object names, comparison operations, and values to be used for filtering.

- 
**[Payment Batch Scheduler Input](./connect_requests_payment_scheduler_input.htm.md)**  

Input representation of the details of the request to create a payment scheduler. This     representation sets the rules and timing for a payment scheduler, including match types, dates,     frequency, and filter criteria.

- 
**[Payment Scheduler Update Input](./connect_requests_payment_scheduler_update_input.htm.md)**  

Input representation of the details of the request to update the status of a payment     scheduler. This representation defines the status of a payment scheduler, which can be set to     Active, Canceled, Draft, or Inactive.

- 
**[Posted Invoice List Write-Off Input](./connect_requests_write_off_posted_invoice_list_input.htm.md)**  

Input representation of the request to write off a list of posted invoices. This     representation includes the details of invoices that you want to write off.

- 
**[Posted Invoice Write-Off Input](./connect_requests_write_off_posted_invoice_input.htm.md)**  

Input representation of the details of the request to write off a posted invoice. This     representation includes invoice details such as invoice ID and reason for writing off     invoices.

- 
**[Refund Line Apply Input](./connect_requests_refund_line_apply_input.htm.md)**  

Input representation of the details of a transaction refund request. This representation     outlines the properties of a refund, including the refund amount and ID of the payment or credit     memo record that the refund is applied to.

- 
**[Resume Billing Input](./connect_requests_resume_billing_input.htm.md)**  

Input representation of the details of the request to resume the billing operation for an     account or a billing schedule group.

- 
**[Resume Billing Object Input](./connect_requests_resume_billing_entity_input.htm.md)**  

Input representation of the details such as the ID of the account or billing schedule     group along with the effective date. These details are used to start the billing     operation.

- 
**[Rules Application Input](./connect_requests_rules_application_input.htm.md)**  

Input representation for applying payments and credits to invoices based on rules.

- 
**[Selection Condition Input](./connect_requests_selection_condition_input.htm.md)**  

Input representation of the criteria that's used to determine which sequencing policy is     applied to a record. The criteria stores the conditions based on any standard or custom fields     of the record.

- 
**[Seller Details Input](./connect_requests_seller_details_input.htm.md)**  

Input representation of the seller details for tax calculation.

- 
**[Send Email Input](./connect_requests_send_email_for_invoice_batch_run_input.htm.md)**  

Input representation of the request to send an email for an invoice batch     run.

- 
**[Sequence Policy Input](./connect_requests_sequence_policy_input.htm.md)**  

Input representation of the configured rules and properties to generate unique,     sequential numbers for objects.

- 
**[Sequence Gap Reconciliation Input](./connect_requests_sequence_gap_reconciliation_input.htm.md)**  

Input representation of the details that are used to identify and reconcile gaps in     sequence values based on the sequence policy or target object.

- 
**[Sequences Assignment Input](./connect_requests_sequences_assignment_input.htm.md)**  

Input representation of the details of the target objects to which the sequence pattern     values are assigned.

- 
**[Standalone Credit Memo Charge Input](./connect_requests_standalone_credit_memo_charge_input.htm.md)**  

Input representation of the details of the charge lines of a credit memo.

- 
**[Standalone Credit Memo Input](./connect_requests_standalone_credit_memo_input.htm.md)**  

Input representation of the details required to create a standalone credit     memo.

- 
**[Standalone Credit Memo Tax Input](./connect_requests_standalone_credit_memo_tax_input.htm.md)**  

Input representation of the details of the tax request.

- 
**[Account Statement Input](./connect_requests_statement_of_account_input.htm.md)**  

Input representation of the details required to generate a comprehensive account     statement with transaction history and balance information.

- 
**[Suspend Billing Input](./connect_requests_suspend_billing_input.htm.md)**  

Input representation of the details of the request to suspend the billing operation for     an account or a billing schedule group.

- 
**[Suspend Billing Object Input](./connect_requests_suspend_billing_entity_input.htm.md)**  

Input representation of the details such as the ID of the account or billing schedule     group along with the effective dates. These details are used to suspend the billing     operation.

- 
**[Tax Calculation Input](./connect_requests_calculate_tax_input.htm.md)**  

Input representation of the details of the request to calculate tax.

- 
**[Void Posted Credit Memo Input](./connect_requests_void_posted_credit_memo_input.htm.md)**  

Input representation of the details of a credit memo to be voided.

- 
**[Void Posted Invoice Input](./connect_requests_void_posted_invoice_input.htm.md)**  

Input representation of the details of the invoice to be voided.

=== ARTICLE: billing_business_apis_resources.htm ===
---
page_id: billing_business_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_business_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Billing API resources.

- 
**[Sequence Gap Reconciliation (POST)](./connect_resources_sequences_gap_reconciliation.htm.md)**  

Restore a missing sequence value identified by using this API in       gapless-enabled sequences. This sequence value can be used later in the subsequent sequence       policy numbering, ensuring there are no gaps.

- 
**[Sequence Assignment (POST)](./connect_resources_sequences_assignment.htm.md)**  

Assign sequence pattern values to objects based on the configured       sequence policy.

- 
**[Batch Invoices Document Generation (POST)](./connect_resources_invoice_batch_docgen.htm.md)**  

Asynchronously generate PDF documents for the invoices that are in the         `Draft` or `Posted`       status and are associated with an invoice batch run record.

- 
**[Batch Invoices Document Generation Retry (POST)](./connect_resources_invoice_batch_docgen_retry.htm.md)**  

Asynchronously regenerate PDF documents for the invoices that are in       the `Draft` or `Posted`       status and failed in an earlier invoice batch run.

- 
**[Batch Invoices Draft to Posted Status (POST)](./connect_resources_batch_draft_invoices_to_posted.htm.md)**  

Update a batch of invoices from `Draft` to `Posted` status for a credit memo       application.

- 
**[Batch Invoice Scheduler (POST, PUT)](./connect_resources_create_an_invoice_scheduler.htm.md)**  

Create or update an invoice scheduler to automatically generate       invoices. Use the criteria and filters of the invoice scheduler to set up the invoice run       schedules based on your requirements.

- 
**[Batch Payment Scheduler (POST)](./connect_resources_create_payment_scheduler.htm.md)**  

Create a payment scheduler to automate and process payment runs on a       recurring basis.

- 
**[Billing Arrangement (GET)](./connect_resources_get_billing_arrangement.htm.md)**  

Retrieve a billing arrangement and its associated billing arrangement     lines.

- 
**[Billing Schedule Recovery List (POST)](./connect_resources_recover_billing_schedules.htm.md)**  

Recover the latest generated invoice associated with the billing       schedules in the `Error` or `Processing` status.

- 
**[Create Billing Schedules for Orders (POST)](./connect_resources_create_billing_schedules.htm.md)**  

Generate billing schedules for orders by using context     service.

- 
**[Create Sequence Policy (POST)](./connect_resources_create_sequence_policy.htm.md)**  

Create a sequence policy to configure a unique, sequential number for       posted invoices or credit memos.

- 
**[Create Standalone Billing Schedules (POST)](./connect_resources_create_billing_schedules_from_any_transaction.htm.md)**  

Generate billing schedules from any internal or external transaction       by using context service.

- 
**[Create and Apply Credit Memo (POST)](./connect_resources_create_and_apply_a_credit_memo.htm.md)**  

Create a credit memo and apply it to an invoice. The credit memo can       fully or partially credit the invoice.

- 
**[Apply Credit Memo (POST)](./connect_resources_credit_memo_apply.htm.md)**  

Adjust or correct already issued invoices by applying an existing       credit memo to an invoice.

- 
**[Unapply Credit Memo (POST)](./connect_resources_credit_memo_invoice_application_unapply.htm.md)**  

Unapply a credit memo from an invoice and return the invoice and the       credit memo to their pre-application states.

- 
**[Apply Credit Memo Line (POST)](./connect_resources_credit_memo_line_level_apply.htm.md)**  

Adjust or correct already issued invoices by applying an existing       credit memo line to an invoice line.

- 
**[Unapply Credit Memo Line (POST)](./connect_resources_credit_memo_line_level_unapply.htm.md)**  

Unapply a credit memo line from an invoice line and return the invoice       line and the credit memo line to their pre-application states.

- 
**[Generate On-Demand Invoice Document (POST)](./connect_resources_generate_documents.htm.md)**  

Generate an invoice document for a record, and update any junction       object record.

- 
**[Generate Account Statement (POST)](./connect_resources_generate_account_statement.htm.md)**  

Generate comprehensive account statement with transaction history and       balance information.

- 
**[Invoice Creation (POST)](./connect_resources_create_invoices_from_billing_schedules.htm.md)**  

Create an invoice for an account, order, or a list of billing       schedules.

- 
**[Invoice Draft to Posted Status (POST)](./connect_resources_draft_to_posted_invoice.htm.md)**  

Update the status of the invoice from Draft to     Posted.

- 
**[Invoice Ingestion (POST)](./connect_resources_invoices_ingestion.htm.md)**  

Ingest or generate an invoice from an internal or external billing       transaction data.

- 
**[Invoice Estimated Tax Calculation (POST)](./connect_resources_calculate_estimated_tax.htm.md)**  

Calculate estimated tax for invoices with invoice lines that have the         `TaxProcessingStatus` as either `Pending` or `Estimated`.

- 
**[Invoice Preview (POST)](./connect_resources_preview_invoices.htm.md)**  

Generate preview invoices, which includes the estimated tax amounts,       for a billing transaction for the next two billing periods.

- 
**[Invoice Run Recovery (POST)](./connect_resources_recover_errored_invoices_batch_run.htm.md)**  

Recover records associated with a failed invoice run. Recovery is       required only when billing schedules remain in the `Processing`, `Void In Progress`, or `Error` status.

- 
**[Negative Invoice Lines to Credit Conversion (POST)](./connect_resources_convert_negative_invoice_lines_to_credit.htm.md)**  

Convert a list of invoice lines with a negative amount into a posted       credit memo. This conversion is applicable for a single invoice at a time.

- 
**[Payment Line Apply (POST)](./connect_resources_payment_line_apply.htm.md)**  

Allocate the balance of a payment to reduce the balance of an invoice.       The response includes an ID of the payment line invoice or payment line invoice line that       represents the payment balance allocated against the invoice.

- 
**[Payment Line Unapply (POST)](./connect_resources_payment_line_unapply.htm.md)**  

Revert the application of a payment line from an invoice, and return the       payment and invoices to their preapplication state. Use this API to correct an input during       the payment application process.

- 
**[Payment Scheduler Update (PATCH)](./connect_resources_update_payment_scheduler.htm.md)**  

Activate or deactivate a payment scheduler. You can set the status of       a payment scheduler to `Active`, `Canceled`, `Draft`, or         `Inactive`.

- 
**[Post a Draft Memo (POST)](./connect_resources_post_draft_credit_memo.htm.md)**  

Post a draft credit memo to a credit memo record for review and       approval.

- 
**[Rules Application (POST)](./connect_resources_rules_application.htm.md)**  

Apply payments and credits to an account's invoices based on specified       rules defined on the Billing Settings page.

- 
**[Posted Invoice List Write-Off (POST)](./connect_resources_write_off_invoices.htm.md)**  

Create credit memos with the total charge amount on the invoice as the       write-off amount and close the invoice.

- 
**[Void a Posted Invoice (POST)](./connect_resources_void_a_posted_invoice.htm.md)**  

Void a posted invoice to rebill the customer, if     necessary.

- 
**[Refund Line Apply (POST)](./connect_resources_apply_refund_to_payment.htm.md)**  

Make a refund transaction against a payment.

- 
**[Send Emails for Posted Invoices (POST)](./connect_resources_send_email_for_invoice_batch_run.htm.md)**  

Send emails for the posted invoices of a specified invoice batch run       ID.

- 
**[Resume Billing (POST)](./connect_resources_resume_billing.htm.md)**  

Resume billing for billing schedule groups or an account that’s       currently on hold.

- 
**[Suspend Billing (POST)](./connect_resources_suspend_billing.htm.md)**  

Suspend billing for billing schedule groups or an account for a       predefined period.

- 
**[Standalone Credit Memo (POST)](./connect_resources_create_a_standalone_credit_memo.htm.md)**  

Create a credit memo without applying it to an invoice. You can credit       the invoice at a later date.

- 
**[Tax Calculation (POST)](./connect_resources_calculate_taxes.htm.md)**  

Calculate tax for a transaction.

- 
**[Update Sequence Policy (PATCH)](./connect_resources_update_sequence_policies.htm.md)**  

Update the settings of a sequence policy that defines how unique,       sequential numbers are generated by using specific patterns, values, and     filters.

- 
**[Void Posted Credit Memo (POST)](./connect_resources_void_posted_credit_memo.htm.md)**  

Void a credit memo in posted state.

=== ARTICLE: billing_business_apis_responses.htm ===
---
page_id: billing_business_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_business_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_api_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available response bodies of Billing APIs.

- 
**[Addresses](./connect_responses_addresses_output.htm.md)**  

Output representation of the details of the addresses that are used for calculating     tax.

- 
**[Address](./connect_responses_address_output.htm.md)**  

Output representation of the location code associated with an address.

- 
**[Batch Invoice Document Generation](./connect_responses_batch_invoice_doc_gen_output.htm.md)**  

Output representation of the request to generate or regenerate the PDF documents for       the invoices that are in the `Draft` or `Posted` status.

- 
**[Error Response](./connect_responses_error_response.htm.md)**  

Output representation of the error details encountered during the API     request.

- 
**[Error Response for Batch Invoice Document Generation](./connect_responses_batch_invoice_doc_gen_error.htm.md)**  

Output representation of the error details associated with the Batch Invoice Document     Generation API.

- 
**[Batch Invoice Scheduler](./connect_responses_batch_invoice_scheduler_output.htm.md)**  

Output representation of the details of an invoice scheduler.

- 
**[Batch Payment Scheduler](./connect_responses_payment_scheduler_output.htm.md)**  

Output representation of the details of a payment scheduler.

- 
**[Billing Arrangement](./connect_responses_billing_arrangement_output.htm.md)**  

Output representation that contains the details of a billing arrangement, including its     status, configuration settings, and associated lines.

- 
**[Billing Arrangement Line](./connect_responses_billing_arrangement_line.htm.md)**  

Output representation that contains the details of a specific line item within a billing     arrangement, defining how charges are split for an account.

- 
**[Billing Batch Scheduler](./connect_responses_billing_batch_scheduler.htm.md)**  

Output representation of the details of a created invoice or payment     scheduler.

- 
**[Billing Schedule Recovery List](./connect_responses_billing_schedule_recovery_list_output.htm.md)**  

Output representation of the recovered details of the billing schedules and associated     invoice.

- 
**[Billing Schedule Recovery](./connect_responses_billing_schedule_recovery_output.htm.md)**  

Output representation of the details of the recovered billing schedules.

- 
**[Context-Aware Billing Schedule](./connect_responses_context_aware_billing_schedule_output.htm.md)**  

Output representation of the context-aware billing schedule.

- 
**[Context-Aware Billing Schedule Error](./connect_responses_context_aware_billing_schedule_error.htm.md)**  

Output representation of the error response related to the generation of the billing     schedule.

- 
**[Convert Negative Invoice Lines](./connect_responses_convert_negative_invoice_lines_output.htm.md)**  

Output representation of the details of the created memo along with the status of the     request.

- 
**[Credit Memo Apply](./connect_responses_credit_memo_apply_output.htm.md)**  

Output representation of the list of applied credit memo results.

- 
**[Credit Memo Apply List](./connect_responses_credit_memo_apply_list_output.htm.md)**  

Output representation of the list of applied credit memo results.

- 
**[Credit Memo Post](./connect_responses_credit_memo_post_output.htm.md)**  

Output representation of the request to post a credit memo.

- 
**[Credit Memo Unapply](./connect_responses_credit_memo_unapply_output.htm.md)**  

Output representation of the details of the credit memo invoice application record with     the status of the request.

- 
**[Credit Memo Line Applied](./connect_responses_credit_memo_line_applied.htm.md)**  

Output representation of the list of applied credit memo line results.

- 
**[Credit Memo Line Applied Response](./connect_responses_credit_memo_line_applied_response.htm.md)**  

Output representation of the list of applied credit memo line results.

- 
**[Credit Memo Line Unapplied](./connect_responses_credit_memo_line_unapplied.htm.md)**  

Output representation of the details of the credit memo line invoice line record with     the status of the request.

- 
**[Document Details](./connect_responses_document_details_output.htm.md)**  

Output representation of the details of the generated document.

- 
**[Invoice Batch Draft To Posted](./connect_responses_invoice_batch_draft_to_posted_output.htm.md)**  

Output representation of the batch update details of the invoices from `Draft` to `Posted`       status.

- 
**[Invoice Batch Run Recovery](./connect_responses_invoice_batch_run_recovery_output.htm.md)**  

Output representation of the details of the invoice batch run recovery     record.

- 
**[Invoice Ingestion](./connect_responses_invoices_ingestion_output.htm.md)**  

Output representation of the details of the generated invoices.

- 
**[Invoice Ingestion Details](./connect_responses_invoice_ingestion_output.htm.md)**  

Output representation of the details of a generated invoice.

- 
**[Invoice Ingestion Output Error](./connect_responses_invoice_ingestion_output_error.htm.md)**  

Output representation of the details of an invoice generation error.

- 
**[Invoice Line Preview](./connect_responses_prev_inv_line_output.htm.md)**  

Output representation of the invoice line preview result.

- 
**[Invoice Preview](./connect_responses_prev_inv_output.htm.md)**  

Output representation of the invoice preview result.

- 
**[Invoice Preview Result](./connect_responses_invoice_preview_output.htm.md)**  

Output representation of the list of preview invoices that are generated for the billing transaction.

- 
**[Invoice Recovery](./connect_responses_invoice_recovery_output.htm.md)**  

Output representation of the details of the recovered invoice and billing     schedules.

- 
**[Line Item](./connect_responses_line_item_output.htm.md)**  

Output representation of the details of the line item.

- 
**[On-Demand Document Generation Response](./connect_responses_on_demand_doc_gen_output.htm.md)**  

Output representation of the details of the generated document along with error     response.

- 
**[Payment Line Apply](./connect_responses_payment_line_apply_output.htm.md)**  

Output representation of the details of the applied payment line. The details include the     ID of the payment record and date when the payment line was applied.

- 
**[Payment Line Unapply](./connect_responses_payment_line_unapply_output.htm.md)**  

Output representation of the details of the reversed payment line application. The     details include the ID of the payment line record and date when the payment line application was     reversed.

- 
**[Payment Scheduler Update](./connect_responses_payment_scheduler_update_output.htm.md)**  

Output representation of the details of the updated payment scheduler. This     representation covers the updated status value of the specified payment scheduler.

- 
**[Posted Invoice List Write-Off](./connect_responses_write_off_posted_invoice_list_output.htm.md)**  

Output representation of the list of invoices that are written off.

- 
**[Posted Invoice Write-Off](./connect_responses_write_off_posted_invoice_output.htm.md)**  

Output representation of the details of a posted invoice that's written off.

- 
**[Posted Invoice Write-Off Error](./connect_responses_write_off_posted_invoice_output_error.htm.md)**  

Output representation of the error response that's associated with a request to write off     a posted invoice.

- 
**[Reference Line Error](./connect_responses_reference_line_error.htm.md)**  

Output representation of the details of the line level errors.

- 
**[Refund Line Applied Response](./connect_responses_refund_line_apply_output.htm.md)**  

Output representation of the details of an applied refund. This representation includes     the properties of a refund line, such as the date when the refund is applied against a payment     and ID of the refund line record.

- 
**[Revenue Async Line Level](./connect_responses_revenue_async_line_level.htm.md)**  

Output representation of the result of the API request for the async line level     operations.

- 
**[Revenue Async Response](./connect_responses_revenue_async_output.htm.md)**  

Output representation of the result of the API request with the request     identifier.

- 
**[Rules Application](./connect_responses_rules_application_output.htm.md)**  

Output representation of the details of rules application.

- 
**[Rules Application Error](./connect_responses_rules_application_error_output.htm.md)**  

Output representation of the error details for rules application failure.

- 
**[Rules Application Summary](./connect_responses_rules_application_summary_output.htm.md)**  

Output representation of the summary of the application rule. This includes the number of     payments and credit memos for the account, the total number of payments and credit memos that's     applied to invoices, and whether all invoices for an account are considered (true) or not     (false).

- 
**[Send Email Error](./connect_responses_send_email_for_invoice_batch_run_error.htm.md)**  

Output representation of the error response of the API request to send emails for     posted invoices.

- 
**[Send Email Response](./connect_responses_send_email_for_invoice_batch_run_output.htm.md)**  

Output representation of the API request to send emails for posted     invoices.

- 
**[Sequence Error](./connect_responses_sequence_error_output.htm.md)**  

Output representation of the error response that's associated with a request to create or     update a sequence policy, or assign sequences.

- 
**[Sequence Gap Reconciliation Error](./connect_responses_sequence_gap_reconciliation_error_output.htm.md)**  

Output representation of the errors encountered during the processing of the API     request.

- 
**[Sequence Gap Reconciliation](./connect_responses_sequence_gap_reconciliation_output.htm.md)**  

Output representation of the details of the sequence gap reconciliation.

- 
**[Sequence Policy](./connect_responses_sequence_policy_output.htm.md)**  

Output representation that shows the status of the assigned sequence pattern     values.

- 
**[Sequences Assignment](./connect_responses_sequences_assignment_output.htm.md)**  

Output representation with the status of the assigned sequence pattern     values.

- 
**[Sequences Assignment Result](./connect_responses_sequences_assignment_result_output.htm.md)**  

Output representation of the details of the assigned sequence values to target     objects.

- 
**[Statement of Account](./connect_responses_statement_of_account_output.htm.md)**  

Output representation of the details of the generated account statement with async     tracking details.

- 
**[Suspend Resume Billing](./connect_responses_suspend_resume_billing_output.htm.md)**  

Output representation of the list of accounts and billing schedule groups, which are     suspended or resumed for billing operations.

- 
**[Suspend Resume Billing Object](./connect_responses_suspend_resume_billing_entity_output.htm.md)**  

Output representation of the details of accounts and billing schedule groups, which are     suspended or resumed for billing operations, along with the status of the API     request.

- 
**[Tax Amount Details](./connect_responses_tax_amount_details_output.htm.md)**  

Output representation of the details of the tax amount.

- 
**[Tax Calculation](./connect_responses_calculate_tax_output.htm.md)**  

Output representation of the details of the calculated tax.

- 
**[Tax Details](./connect_responses_tax_details_output.htm.md)**  

Output representation of the tax details for each line item.

- 
**[Tax Engine Log](./connect_responses_tax_engine_log_output.htm.md)**  

Output representation of the logs that the tax engine generates.

- 
**[Tax Imposition](./connect_responses_tax_imposition_output.htm.md)**  

Output representation of the details of the imposed tax.

- 
**[Tax Jurisdiction](./connect_responses_tax_jurisdiction_output.htm.md)**  

Output representation of the details of the tax jurisdiction for the tax     line.

- 
**[Void Posted Credit Memo](./connect_responses_void_posted_credit_memo_output.htm.md)**  

Output representation of the request to void a posted credit memo.

=== ARTICLE: billing_connectAPI_enums.htm ===
---
page_id: billing_connectAPI_enums.htm
title: ConnectApi Enums
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_connectAPI_enums.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_connect_api_namespace.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ConnectApi Enums

Enums specific to the `ConnectApi`
    namespace.

    
      

`ConnectApi` enums inherit all properties and methods
        of Apex enums.

      

Enums are not versioned. Enum values are returned in all API
          versions.

      
        

            
            
            
              
                

                

              

            

            
              
                

                

- 
- 

              

              
                

                

- 
- 
- 
- 

              

              
                

                

              

              
                

                

- 
- 
- 

              

              
                

                

- 
- 
- 

              

              
                

                

- 
- 

              

            

          
| Enum | Description |
| --- | --- |
| `ConnectApi.InvoiceAction` | Type of invoice to be created. Valid values are: `Draft` `Posted` |
| `ConnectApi.TaxStrategyEnum` | Tax strategy to be applied across invoice lines. You can override the tax strategy at the individual invoice line level or at the tax line level. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `ManualOverride`—Specifies that the provided tax values must be considered for taxes. `CopyFromInvoiceLine`—Specifies that tax values must be copied from the invoice line. `Calculate`—Specifies that tax must be calculated by using the API. |
| `ConnectApi.CreditMemoTypeEnum` | Type of credit memo to be created. Valid values are `Posted` and `Draft`. Specify `Draft` as a value in your request to create draft credit memos. |
| `ConnectApi.StandaloneTaxStrategyEnum` | Specifies how tax lines must be created for the standalone credit memos. Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `Manual Override`—Specifies that the provided tax values must be considered for taxes. `Calculate`—Specifies that tax must be calculated by using the API. |
| `ConnectApi.SequenceResponseStatusEnum` | Status of the sequence policy assignment. Valid values are: `PartialSuccess` `Success` `Failed` |
| `ConnectApi.StatusEnum` | The status of sequence reconciliation API request. Valid values are: `Submitted` `NotSubmitted` |

=== ARTICLE: billing_connect_api_namespace.htm ===
---
page_id: billing_connect_api_namespace.htm
title: ConnectApi Namespace
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_connect_api_namespace.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# 
ConnectApi Namespace

The `ConnectApi` namespace (also called Connect in
        Apex) provides classes to manage credit applications and billing scenarios.

        
            

These classes are available in the `ConnectApi`
                namespace.

        

    

- 
**[BatchInvoiceApplication Class](./apex_ConnectAPI_BatchInvoiceApplication_static_methods.htm.md#apex_ConnectAPI_BatchInvoiceApplication_static_methods)**  

Update a batch of invoices from Draft to Posted status for a credit memo application. by   using the BatchInvoiceApplication class.

- 
**[Billing Class](./apex_ConnectAPI_Billing_static_methods.htm.md#apex_ConnectAPI_Billing_static_methods)**  

Manage billing scenarios by using the Billing class. You can convert negative invoice   lines, create and apply a credit memo to an invoice, generate invoices, and recover billing   schedules.

- 
**[CreditMemoApply Class](./apex_ConnectAPI_CreditMemoApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoApply_static_methods)**  

Manage credit memo applications by using the CreditMemoApply class.

- 
**[CreditMemoLineApply Class](./apex_ConnectAPI_CreditMemoLineApply_static_methods.htm.md#apex_ConnectAPI_CreditMemoLineApply_static_methods)**  

Manage credit memo line applications by using the CreditMemoLineApply class.

- 
**[HarmonizeBilling Class](./apex_ConnectAPI_HarmonizeBilling_static_methods.htm.md#apex_ConnectAPI_HarmonizeBilling_static_methods)**  

Update the status of the invoice from Draft to Posted by using the HarmonizeBilling   class.

- 
**[PaymentsBilling Class](./apex_ConnectAPI_PaymentsBilling_static_methods.htm.md#apex_ConnectAPI_PaymentsBilling_static_methods)**  

Use the PaymentsBilling class to allocate the balance of a payment to reduce the balance   of an invoice. Additionally, revert the application of a payment line from an invoice.

- 
**[SequencingWithoutAura Class](./apex_ConnectAPI_SequencingWithoutAura_static_methods.htm.md#apex_ConnectAPI_SequencingWithoutAura_static_methods)**  

Manage invoice sequencing processes by using the SequencingWithoutAura   class.

- 
**[ConnectApi Input Classes](./billing_apex_input_classes.htm.md)**  

Billing includes these Apex input classes.

- 
**[ConnectApi Output Classes](./billing_apex_output_classes.htm.md)**  

Billing includes these Apex output classes.

- 
**[ConnectApi Enums](./billing_connectAPI_enums.htm.md)**  

Enums specific to the `ConnectApi`     namespace.

=== ARTICLE: billing_extended_standard_object_fields.htm ===
---
page_id: billing_extended_standard_object_fields.htm
title: Billing Fields on Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_extended_standard_object_fields.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on Standard Objects

Billing adds standard fields to some standard Salesforce objects of other features to
        represent information specific to Billing. These fields are available only in orgs where
        Billing is enabled.

- 
**[Billing Fields on AccountBillingAccount](./billling_sforce_api_objects_accountbillingaccount.htm.md)**  

Standard fields extend the AccountBillingAccount object for use in          Billing to represent information about default billing accounts. This object is       available in API version 63.0 and later.

- 
**[Billing Fields on AssetActionSource](./billing_sforce_api_objects_assetactionsource.htm.md)**  

       Standard fields extend the AssetActionSource object for use in Billing to          represent information about the billing term.

- 
**[Billing Fields on BillingAccount](./billling_sforce_api_objects_billingaccount.htm.md)**  

Standard fields extend the BillingAccount object for use in Billing          to represent information about the billing suspension date and the billing resumption          date. This object is available in API version 63.0 and later.

- 
**[Billing Fields on CollectionPlan](./billing_sforce_api_objects_collectionplan.htm.md)**  

       Standard fields extend the CollectionPlan object for use in Billing to          represent information about the total invoice balance. This object is available in API       version 64.0 and later.

- 
**[Billing Fields on CollectionPlanItem](./billing_sforce_api_objects_collectionplanitem.htm.md)**  

       Standard fields extend the CollectionPlanItem object for use in Billing to          represent information about the invoice balance. This object is available in API       version 64.0 and later.

- 
**[Billing Fields on ExpressionSet](./billing_sforce_api_objects_expressionset.htm.md)**  

Standard fields extend the ExpressionSet object for use in Billing.          These fields represent information about an expression set that performs a series of          calculations by using lookups and user-defined variables and constants to calculate          taxes. This object is available in API version 66.0 and later.

- 
**[Billing Fields on Dispute](./billing_sforce_api_objects_dispute.htm.md)**  

       Represents the details of a billing dispute that involves one invoice and one          or more disputed invoice lines. The details include the disputed amount, the approved          amount, and the dispute type, subtype and status. This object is available in API       version 66.0 and later.

- 
**[Billing Fields on DisputeItem](./billing_sforce_api_objects_disputeitem.htm.md)**  

       Represents a specific invoice line or charge that’s being disputed. The          details include the total transaction amount, transaction date, disputed amount, reason,          and status of the dispute. This object is available in API version 66.0 and       later.

- 
**[Billing Fields on OrderItem](./billing_sforce_api_objects_orderitem.htm.md)**  

       Standard fields extend the OrderItem object for use in Billing to represent          information about the billing term.

- 
**[Billing Fields on Payment](./billing_sforce_api_objects_payment.htm.md)**  

       Standard fields extend the Payment object for use in Billing to represent          information about corporate currency, transaction amounts in corporate currency, and          accounting periods for legal entities. This object is available in API version 64.0       and later.

- 
**[Billing Fields on PaymentLineInvoice](./billing_sforce_api_objects_paymentlineinvoice.htm.md)**  

Standard fields extend the PaymentLineInvoice object for use in          Billing to represent information about legal entities and legal entity accounting          periods. This object is available in API version 64.0 and later.

- 
**[Billing Fields on QuoteLineItem](./billing_sforce_api_objects_quotelineitem.htm.md)**  

       Standard fields extend the QuoteLineItem object for use in Billing to          represent information about the billing term.

- 
**[Billing Fields on Refund](./billing_sforce_api_objects_refund.htm.md)**  

Standard fields extend the Refund object for use in Billing to          represent information about corporate currency, transaction amounts in corporate currency,          and accounting periods for legal entities. This object is available in API version       64.0 and later.

- 
**[Billing Fields on RefundLinePayment](./billing_sforce_api_objects_refund_line_payment.htm.md)**  

Standard fields extend the Refund Line Payment object for use in          Billing to represent information about accounting periods for legal entities. This       object is available in API version 64.0 and later.

- 
**[Billing Fields on TaxRate](./billing_sforce_api_objects_taxrate.htm.md)**  

       Standard fields extend the TaxRate object for use in Billing. These fields          represent information about the tax rate for a transaction that's determined by the          applicable tax code and country. This object is available in API version 66.0 and       later.

- 
**[Billing Fields on TransactionJournal](./billing_sforce_api_objects_transactionjournal.htm.md)**  

Standard fields extend the TransactionJournal object for use in          Billing to represent information about the general ledger accounts for billing          transactions. This object is available in API version 63.0 and later.

=== ARTICLE: billing_flow_metadata_api.htm ===
---
page_id: billing_flow_metadata_api.htm
title: Flow for Billing
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Billing

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Billing exposes additional actionType values for the FlowActionCall Metadata type.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
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
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Billing include: `applyCredit`—Apply a credit memo or credit memo line to an invoice or invoice line, respectively. `unapplyCredit`—Unapply a credit memo or credit memo line from an invoice or invoice line, respectively. `postDraftInvoice`—Update the status of an invoice from `Draft` to `Posted` for a credit memo application. `postDraftInvoiceBatchRun`—Update the status of a batch of invoices from `Draft` to `Posted` for a credit memo application. `createBillingSchedulesFromBillingTransaction`—Create one or more billing schedules for a specified billing transaction ID. `recoverBillingSchedules`—Recover one or more billing schedules in the `Error` or `Processing` status. `generateInvoiceDocuments`—Asynchronously generate PDF documents for the invoices associated with an invoice batch run record that are in the `Draft` or `Posted` status. `createBillingSchedulesFromTrxn`—Creates billing schedules for internal or external transaction records by calling the Create Standalone Billing Schedules API. `unapplyPayment`—Unapplies a payment that's already been applied to an invoice or invoice line by crediting the amount back to the payment and the invoice or invoice line. `writeOffInvoices`—Write off partially paid or unpaid invoices to manage pending debts and to maintain accurate financial records. This action calls the Posted Invoice List Write-Off (POST) API. `assignSequences`—Assigns sequence pattern values to target invoice records based on the specified sequence policy. `postDraftCreditMemo`—Post a draft credit memo to a credit memo record for review and approval. `generateAccountStatement`—Generates a comprehensive account statement for a specified account with transaction history and balance information. `blngDsptIssueCreditMemo`—Issue credit memos for disputed invoices to resolve billing disputes. `blngSvcExtendInvoiceDueDate`—Update the due date on an invoice to accommodate payment extensions or resolve billing disputes. `blngSvcSuspendBilling`—Suspend or resume the billing of an account to handle billing disputes. `blngSvcUpdateBillToContact`—Update the Bill to Contact detail on an invoice to ensure accurate billing communication and routing. `blngSendDunningEmail`—Run an orchestration that sends dunning process emails for collection plans to recover overdue revenue and notify customers about amounts still due. `automateRefund`—Initiate refund orchestration for a credit memo generated from a subscription cancellation or negative amendment. |

=== ARTICLE: billing_invocable_actions_parent.htm ===
---
page_id: billing_invocable_actions_parent.htm
title: Billing Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Standard Invocable Actions

Use standard invocable actions to automate processes such as credit application,
    billing schedules creation, and invoice management.

    

## Commerce Payments Invocable Actions

This table provides a list of the
        invocable actions of Commerce Payments, which can be used for Billing.

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

          

        
| Resource | Description |
| --- | --- |
| [`/services/data/v68.0/actions/standard/applyPayment`](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_obj_payment_apply.htm) (POST) | Apply a payment record to an invoice header by creating a PaymentLineInvoice record with `Applied` type. |
| [`/services/data/v68.0/actions/standard/paymentSale`](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_obj_payment_sale.htm) (POST) | Capture a payment without any prior authorization, and create a payment record. |

    
      

Billing provides these invocable actions.

      
    

  

- 
**[Apply Credit Action](./actions_obj_run_apply_credit.htm.md)**  

Apply a credit memo or credit memo line to an invoice or invoice 			line, respectively. 

- 
**[Apply Payments and Credits by Rules Action](./actions_obj_apply_rules.htm.md)**  

Apply payments and credits to posted invoices by adhering to the specified         rules.

- 
**[Automate Refund Action](./actions_obj_automate_refund.htm.md)**  

Initiate refund orchestration for a credit memo             generated from a subscription cancellation or negative amendment.

- 
**[Create Billing Schedules From Billing Transaction Action](./actions_obj_create_billing_schedule_from_billing_transaction.htm.md)**  

Create one or more billing schedules for a specified billing 			transaction ID.

- 
**[Create Standalone Billing Schedules Action](./actions_obj_create_billing_schedules_from_transaction.htm.md)**  

Creates billing schedules for internal or external transaction             records by calling the Create Standalone Billing Schedules API.

- 
**[Extend Invoice Due Date Action](./actions_obj_blng_svc_inv_extend_due_date.htm.md)**  

Update the due date on an invoice to accommodate payment extensions             or resolve billing disputes.

- 
**[Generate Account Statement](./actions_obj_generate_statement_of_account.htm.md)**  

Generates a comprehensive account statement for a specified account             with transaction history and balance information.

- 
**[Generate Invoice Documents Action](./actions_obj_generate_batch_invoice_documents.htm.md)**  

Asynchronously generate PDF documents for the invoices associated with 			an invoice batch run record that are in the `Draft` 			or `Posted` status.

- 
**[Issue Credit Memo Action](./actions_obj_blng_dspt_issue_credit_memo.htm.md)**  

Issue credit memos for disputed invoices to resolve billing             disputes.

- 
**[Post Draft Credit Memo Action](./actions_obj_post_draft_credit_memo.htm.md)**  

Post a draft credit memo to a credit memo record for review and             approval.

- 
**[Post Draft Invoice Action](./actions_obj_post_draft_invoice.htm.md)**  

Update the status of an invoice from `Draft` to `Posted` for a credit memo 			application.

- 
**[Post Draft Invoice Batch Run Action](./actions_obj_post_draft_invoice_batch_run.htm.md)**  

Update the status of a batch of invoices from `Draft` to `Posted` 			for a credit memo application.

- 
**[Recover Billing Schedules Action](./actions_obj_recover_billing_schedule.htm.md)**  

Recover one or more billing schedules in the `Error` or `Processing` status.

- 
**[Send Dunning Email Action](./actions_obj_blng_send_dunning_email.htm.md)**  

Run an orchestration that sends dunning             process emails for collection plans to recover overdue revenue and notify customers             about amounts still due.

- 
**[Suspend Billing Action](./actions_obj_blng_svc_suspend_billing.htm.md)**  

Suspend or resume the billing of an account to handle billing             disputes.

- 
**[Update Bill To Contact Action](./actions_obj_blng_svc_update_bill_to_contact.htm.md)**  

Update the Bill to Contact detail on an invoice to ensure accurate             billing communication and routing.

- 
**[Unapply Credit Action](./actions_obj_run_unapply_credit.htm.md)**  

Unapply a credit memo or credit memo line from an invoice or invoice 			line, respectively.

- 
**[Unapply Payment Action](./actions_obj_unapply_payment.htm.md)**  

Unapplies a payment that's already been applied to an invoice or             invoice line by crediting the amount back to the payment and the invoice or invoice             line.

- 
**[Void Posted Credit Memo Action](./actions_obj_void_posted_credit_memo.htm.md)**  

Invoke the Void Posted Credit Memo API by providing a credit memo ID.

- 
**[Write Off Invoices Action](./actions_obj_write_off_invoices.htm.md)**  

Write off partially paid or unpaid invoices to manage pending debts             and to maintain accurate financial records. This action calls the Posted Invoice List             Write-Off (POST) API.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

=== ARTICLE: billing_metadata_api_parent.htm ===
---
page_id: billing_metadata_api_parent.htm
title: Billing Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[BillingSettings](./meta_billingsettings.htm.md)**  

Represents the settings for Salesforce 		Billing.

- 
**[Flow for Billing](./billing_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

- 
**[PaymentsSharingSettings](./meta_paymentssharingsettings.htm.md)**  

Represents the settings to enable account-based sharing 			to view details related to Revenue Cloud Billing on the objects for Payments and 			Refunds.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: billing_overview.htm ===
---
page_id: billing_overview.htm
title: Billing
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing

Automate processes related to billing, credit application, and invoice generation.
  Generate billing schedules by using context service, and create invoices from a billing
  schedule.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions |

  

 

- 
**[Billing Standard Objects](./billing_std_objects_parent.htm.md)**  

The Billing data model provides objects and fields to manage billing and tax   configurations, credit memos, and invoices, and accounting periods for legal entities.

- 
**[Billing Fields on Standard Objects](./billing_extended_standard_object_fields.htm.md)**  

Billing adds standard fields to some standard Salesforce objects of other features to         represent information specific to Billing. These fields are available only in orgs where         Billing is enabled.

- 
**[Salesforce Payments Objects in Billing](./billing_payments_objects.htm.md)**  

Billing provides access to some standard Salesforce Payments objects                   that you can use to authorize payments, connect to an external payment gateway,                   group all the payment transactions that are processed for a particular                   transaction, and store payment methods. You can access these objects with the                   Revenue Cloud Billing license.

- 
**[Billing Platform Events](./billing_pfrm_evnt_parent.htm.md)**  

Salesforce publishes standard platform events in response to an action that occurred in   the org or to report errors. For example, the InvoiceProcessedEvent platform event sends   notification to the customer when the billing invoice activity is complete. You can subscribe to a   standard platform event by using the subscription mechanism that the event supports.

- 
**[Billing Standard Invocable Actions](./billing_invocable_actions_parent.htm.md)**  

Use standard invocable actions to automate processes such as credit application,     billing schedules creation, and invoice management.

- 
**[Billing Business APIs](./billing_business_api_overview.htm.md)**  

Use the Billing Business APIs to manage credit application and to handle billing     scenarios.

- 
**[Billing Apex Reference](./billing_apex_reference.htm.md)**  

Billing provides the `ConnectApi`       namespace (also called Connect in Apex) that contains classes for accessing the same       capabilities that are available in the Billing Business APIs. Additionally, you can use other       built-in Apex classes and interfaces grouped by namespace.

- 
**[Billing Metadata API Types](./billing_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

#### See Also

- [*Salesforce Help*: Assign Permissions to Access Billing Features](https://help.salesforce.com/s/articleView?id=ind.billing_permission_sets.htm&type=5&language=en_US)

=== ARTICLE: billing_payments_objects.htm ===
---
page_id: billing_payments_objects.htm
title: Salesforce Payments Objects in Billing
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_payments_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Salesforce Payments Objects in Billing

Billing provides access to some standard Salesforce Payments objects
                  that you can use to authorize payments, connect to an external payment gateway,
                  group all the payment transactions that are processed for a particular
                  transaction, and store payment methods. You can access these objects with the
                  Revenue Cloud Billing license.

      
         

For more information about these Salesforce Payments objects, refer to these
                        resources.

         
            
- [PaymentAuthAdjustment](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentauthadjustment.htm)

            
- [PaymentAuthorization](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentauthorization.htm)

            
- [PaymentGateway](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentgateway.htm)

            
- [PaymentGatewayLog](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewaylog.htm)

            
- [PaymentGatewayProvider](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewayprovider.htm)

            
- [PaymentGroup](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentgroup.htm)

            
- [PaymentMethod](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentmethod.htm)

=== ARTICLE: billing_pfrm_evnt_parent.htm ===
---
page_id: billing_pfrm_evnt_parent.htm
title: Billing Platform Events
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_pfrm_evnt_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Platform Events

Salesforce publishes standard platform events in response to an action that occurred in
  the org or to report errors. For example, the InvoiceProcessedEvent platform event sends
  notification to the customer when the billing invoice activity is complete. You can subscribe to a
  standard platform event by using the subscription mechanism that the event supports.

- 
**[BillingScheduleCreatedEvent](./sforce_api_objects_billingschedulecreatedevent.htm.md)**  

Notifies subscribers when the `/commerce/invoicing/billing-schedules/actions/create` request is complete.       This object is available in API version 63.0 and later.

- 
**[CreditInvoiceProcessedEvent](./sforce_api_objects_creditinvoiceprocessedevent.htm.md)**  

Represents the notification to the customers after the process          initiated by the `/commerce/invoicing/invoices/{invoiceId}/actions/credit` request is          complete. This object is available in API version 62.0 and later.

- 
**[CreditMemoProcessedEvent](./sforce_api_objects_creditmemoprocessedevent.htm.md)**  

       Represents the notification to the customers after the process initiated by          the `/commerce/invoicing/credit-memos` request is          complete. This object is available in API version 62.0 and later.

- 
**[InvoiceProcessedEvent](./sforce_api_objects_invoiceprocessedevent.htm.md)**  

Represents the notification to the customers after the process          started by the `/commerce/billing/invoices` request is          complete. The process groups billing schedules by grouping keys and creates one invoice per          grouping key. The `InvoiceProcessedEvent` platform event          is a top-level object that contains a list of `InvoiceProcessedDetailEvents` platform events, where each detail event          represents an attempt to create one invoice. This object is available in API version       62.0 and later.

- 
**[NegInvcLineProcessedEvent](./sforce_api_objects_neginvclineprocessedevent.htm.md)**  

Represents the notification to the customers when a negative invoice          line is converted to a credit memo This object is available in API version 62.0 and       later.

- 
**[SequenceAssignedEvent](./sforce_api_objects_sequenceassignedevent.htm.md)**  

       Represents the notification to customers about the assignment of a sequence          to a target record. This process is initiated by the `/sequences/actions/assign` request. This object is available in API       version 65.0 and later.

- 
**[VoidInvoiceProcessedEvent](./sforce_api_objects_voidinvoiceprocessedevent.htm.md)**  

Represents the notification to the customers after the process          started by the `/commerce/invoicing/invoices/{invoiceId}/actions/void` request is complete. The          request attempts to void an invoice by crediting an invoice and changing its status to             `Voided`, which prevents further changes. This       object is available in API version 62.0 and later.

=== ARTICLE: billing_sforce_api_objects_assetactionsource.htm ===
---
page_id: billing_sforce_api_objects_assetactionsource.htm
title: Billing Fields on AssetActionSource
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_assetactionsource.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on AssetActionSource

      Standard fields extend the AssetActionSource object for use in Billing to
         represent information about the billing term.

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Admin permission set or the
            Billing Operations User permission set to access this object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| BillingTerm | **Type** int **Properties** Defaulted on create, Filter, Group, Nillable, Sort **Description** The number of billing frequency units to combine into a billing period item. Available in API version 68.0 and later. |

=== ARTICLE: billing_sforce_api_objects_collectionplan.htm ===
---
page_id: billing_sforce_api_objects_collectionplan.htm
title: Billing Fields on CollectionPlan
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_collectionplan.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on CollectionPlan

      Standard fields extend the CollectionPlan object for use in Billing to
         represent information about the total invoice balance. This object is available in API
      version 64.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Collections and Recovery
            Specialist permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| TotalInvoiceBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The sum of all invoice balances for collection plan items associated with the collection plan. |
| OverdueRiskIndicator | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Indicates the overdue risk level for the collection plan. Available in API version 67.0 and later. Valid values are: `Low` `Medium` `High` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CollectionPlanChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
               

**[CollectionPlanFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[CollectionPlanHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
            
               

**[CollectionPlanShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

            
         

      

   

#### See Also

- [*Industries Common Resources Developer Guide*: CollectionPlan](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/sforce_api_objects_collectionplan.htm)

=== ARTICLE: billing_sforce_api_objects_collectionplanitem.htm ===
---
page_id: billing_sforce_api_objects_collectionplanitem.htm
title: Billing Fields on CollectionPlanItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_collectionplanitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on CollectionPlanItem

      Standard fields extend the CollectionPlanItem object for use in Billing to
         represent information about the invoice balance. This object is available in API
      version 64.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Collections and Recovery
            Specialist permission set to access this object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| InvoiceBalance | **Type** currency **Properties** Filter, Nillable, Sort **Description** The balance amount of the invoice associated with the collection plan item. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CollectionPlanItemChangeEvent](./sforce_api_associated_objects_change_event.htm.md)**

               
: Change events are available for the object.

            
            
               

**[CollectionPlanItemFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
            
               

**[CollectionPlanItemHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object

            
         

      

   

#### See Also

- [*Industries Common Resources Developer Guide*: CollectionPlanItem](https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/sforce_api_objects_collectionplanitem.htm)

=== ARTICLE: billing_sforce_api_objects_dispute.htm ===
---
page_id: billing_sforce_api_objects_dispute.htm
title: Billing Fields on Dispute
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_dispute.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on Dispute

      Represents the details of a billing dispute that involves one invoice and one
         or more disputed invoice lines. The details include the disputed amount, the approved
         amount, and the dispute type, subtype and status. This object is available in API
      version 66.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Operations User or the
            Billing Customer Service User permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| InvoiceId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The invoice ID associated with the dispute. This field is a relationship field. **Relationship Name** Invoice **Refers To** Invoice |
| RevisedDueDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The revised due date for the invoice. |
| BillingSuspensionDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when billing for the account is suspended. |
| BillingResumptionDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when billing for the account is resumed. |
| RevisedBillToContact | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The revised billing contact for the invoice. This field is a relationship field. **Relationship Name** Contact **Refers To** Contact |
| ResolutionAction | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The action taken to resolve the dispute. Valid values are: `Resolve with No Action` `Issue Credit Memo` |
| ResolutionActionStatus | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of the resolution action. Valid values are: `In Progress` `Closed` `Error` |
| MaySetContactAsDefault | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the revised billing contact is set as default for future invoices (`true`) or not (`false`). The default value is `false`. |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the name of the cloud or function that uses the Dispute object. Valid value is `Billing`. |

      

   

#### See Also

- [*Financial Services Cloud Developer Guide*: Dispute](https://developer.salesforce.com/docs/atlas.en-us.264.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/sforce_api_objects_dispute.htm)

=== ARTICLE: billing_sforce_api_objects_disputeitem.htm ===
---
page_id: billing_sforce_api_objects_disputeitem.htm
title: Billing Fields on DisputeItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_disputeitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on DisputeItem

      Represents a specific invoice line or charge that’s being disputed. The
         details include the total transaction amount, transaction date, disputed amount, reason,
         and status of the dispute. This object is available in API version 66.0 and
      later.

      

## Supported Calls

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Operations User or the
            Billing Customer Service User permission set to access this object.

      

      

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
| ApprovedAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The amount that’s approved to be credited to the customer. |
| InvoiceLineId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The invoice line ID associated with the dispute. This field is a relationship field. **Relationship Name** Invoice Line **Refers To** Invoice Line |

      

   

#### See Also

- [*Financial Services Cloud Developer Guide*: DisputeItem](https://developer.salesforce.com/docs/atlas.en-us.264.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/sforce_api_objects_disputeitem.htm)

=== ARTICLE: billing_sforce_api_objects_expressionset.htm ===
---
page_id: billing_sforce_api_objects_expressionset.htm
title: Billing Fields on ExpressionSet
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_expressionset.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on ExpressionSet

Standard fields extend the ExpressionSet object for use in Billing.
         These fields represent information about an expression set that performs a series of
         calculations by using lookups and user-defined variables and constants to calculate
         taxes. This object is available in API version 66.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| UsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The Revenue Standard Tax Calculation value that’s using the expression set to calculate taxes. |

=== ARTICLE: billing_sforce_api_objects_orderitem.htm ===
---
page_id: billing_sforce_api_objects_orderitem.htm
title: Billing Fields on OrderItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_orderitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on OrderItem

      Standard fields extend the OrderItem object for use in Billing to represent
         information about the billing term.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Admin permission set or the
            Billing Operations User permission set to access this object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| BillingTerm | **Type** int **Properties** Defaulted on create, Filter, Group, Nillable, Sort **Description** The number of billing frequency units to combine into a billing period item. Available in API version 68.0 and later. |
| NetUnitPrice | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The net unit price of the related order item. Available in API version 64.0 and later. |

=== ARTICLE: billing_sforce_api_objects_payment.htm ===
---
page_id: billing_sforce_api_objects_payment.htm
title: Billing Fields on Payment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_payment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on Payment

      Standard fields extend the Payment object for use in Billing to represent
         information about corporate currency, transaction amounts in corporate currency, and
         accounting periods for legal entities. This object is available in API version 64.0
      and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Payment Admin permission set or the
            Payment Operations User permission set to access this object.

      

      

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
| CorporateCurrencyCnvAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The payment amount in corporate currency. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the payment amount is converted into corporate currency. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the payment amount into corporate currency. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. |
| FunctionalCurrencyCnvAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the amount value is converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the amount value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period related to the payment. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntityAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity related to the payment. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[PaymentFeed](./sforce_api_associated_objects_feed.htm.md)**

               
: Feed tracking is available for the object.

            
         

      

   

#### See Also

- [*Object Reference for the platform*: Payment](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_payment.htm)

=== ARTICLE: billing_sforce_api_objects_paymentlineinvoice.htm ===
---
page_id: billing_sforce_api_objects_paymentlineinvoice.htm
title: Billing Fields on PaymentLineInvoice
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_paymentlineinvoice.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on PaymentLineInvoice

Standard fields extend the PaymentLineInvoice object for use in
         Billing to represent information about legal entities and legal entity accounting
         periods. This object is available in API version 64.0 and later.

      

## Supported Calls

         
         

            `create()`, `describeLayout()`, `describeSObjects()`,
               `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Payment Admin permission set or the
            Payment Operations User permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period related to the payment line invoice. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntyAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity related to the payment line invoice. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[PaymentLineInvoiceHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

            
         

      

   

#### See Also

- [*Object Reference for the platform*: PaymentLineInvoice](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_paymentlineinvoice.htm)

=== ARTICLE: billing_sforce_api_objects_quotelineitem.htm ===
---
page_id: billing_sforce_api_objects_quotelineitem.htm
title: Billing Fields on QuoteLineItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_quotelineitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on QuoteLineItem

      Standard fields extend the QuoteLineItem object for use in Billing to
         represent information about the billing term.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Billing Admin permission set or the
            Billing Operations User permission set to access this object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| BillingTerm | **Type** int **Properties** Create, Defaulted on create, Filter, Group, Nillable, Sort, Update **Description** The number of billing frequency units to combine into a billing period item. Available in API version 68.0 and later. |

=== ARTICLE: billing_sforce_api_objects_refund.htm ===
---
page_id: billing_sforce_api_objects_refund.htm
title: Billing Fields on Refund
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_refund.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on Refund

Standard fields extend the Refund object for use in Billing to
         represent information about corporate currency, transaction amounts in corporate currency,
         and accounting periods for legal entities. This object is available in API version
      64.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Payment Admin permission set or the
            Payment Operations User permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| CorporateCurrencyCnvAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The refund amount in corporate currency. |
| CorporateCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the refund amount is converted into corporate currency. |
| CorporateCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the refund amount into corporate currency. |
| CorporateCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The currency ISO code of the corporate currency. |
| FunctionalCurrencyCnvAmount | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The amount value in functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnDate | **Type** date **Properties** Filter, Group, Nillable, Sort, Update **Description** The date on which the amount value is converted into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyCvsnRate | **Type** double **Properties** Filter, Nillable, Sort, Update **Description** The exchange rate that's used to convert the amount value into functional currency. Available in API version 66.0 and later. |
| FunctionalCurrencyIsoCode | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The ISO code of the functional currency. Available in API version 66.0 and later. |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period related to the refund. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntityAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity related to the refund. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| ReasonCode | **Type** picklist **Properties** Filter, Group, Nillable, Sort **Description** Specifies a unique code that identifies the primary reason for a refund. Available in API version 68.0 and later. |
| ReferenceRecordId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the record that this refund was issued against. For example, an invoice, credit memo, or payment. Available in API version 68.0 and later. This field is a polymorphic relationship field. **Relationship Name** ReferenceRecord **Refers To** CreditMemo |

      

   

#### See Also

- [*Object Reference for the platform*: Refund](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_refund.htm)

=== ARTICLE: billing_sforce_api_objects_refund_line_payment.htm ===
---
page_id: billing_sforce_api_objects_refund_line_payment.htm
title: Billing Fields on RefundLinePayment
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_refund_line_payment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on RefundLinePayment

Standard fields extend the Refund Line Payment object for use in
         Billing to represent information about accounting periods for legal entities. This
      object is available in API version 64.0 and later.

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license, and the Payment Admin permission set or the
            Payment Operations User permission set to access this object.

      

      

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

                  

               

            
| Field | Details |
| --- | --- |
| LegalEntityAccountingPeriodId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity accounting period related to the refund. This field is a relationship field. **Relationship Name** LegalEntityAccountingPeriod **Refers To** LegalEntityAccountingPeriod |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity related to the refund. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[RefundLinePaymentHistory](./sforce_api_associated_objects_history.htm.md)**

               
: History is available for tracked fields of the object.

=== ARTICLE: billing_sforce_api_objects_taxrate.htm ===
---
page_id: billing_sforce_api_objects_taxrate.htm
title: Billing Fields on TaxRate
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_taxrate.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on TaxRate

      Standard fields extend the TaxRate object for use in Billing. These fields
         represent information about the tax rate for a transaction that's determined by the
         applicable tax code and country. This object is available in API version 66.0 and
      later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set or Tax Admin permission set access to this
            object.

      

      

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

                  

                  
                     

                     

: 

: 

: 
: 

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

                  

               

            
| Field | Details |
| --- | --- |
| ApplicationBasis | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies whether the tax rate is applied on the net or gross amount. Valid values are: `Gross` `Net` The default value is `Gross`. |
| City | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The city to which the tax rate applies. |
| Country | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The country name that’s derived from the GeoCountry field value. This field is a calculated field. |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The currency ISO code that’s applicable to the tax rate. |
| EndDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date until when the tax rate is valid. |
| FlatTaxAmount | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The flat tax amount that’s applied to the transaction. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed a tax rate record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a tax rate record. If this value is null, it’s possible that the user only accessed the debit memo line tax record or a related list view (LastReferencedDate), but not viewed the debit memo line tax record itself. |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort **Description** The legal entity to which the tax rate applies. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The name of the invoice line. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Required. The ID of the user who owns a TaxRate record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ProductCode | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The code of the product for which the tax rate applies. |
| RateUsageType | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies whether the tax rate is created for Commerce or Revenue Cloud. Valid values are: `Commerce` `RevCloud` The default value is `Commerce`. |
| StartDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date from when the tax rate is valid. |
| State | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The state name that’s derived from the GeoState field value. This field is a calculated field. |
| ZipCode | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The postal or ZIP code to which the tax rate applies. |

=== ARTICLE: billing_sforce_api_objects_transactionjournal.htm ===
---
page_id: billing_sforce_api_objects_transactionjournal.htm
title: Billing Fields on TransactionJournal
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_sforce_api_objects_transactionjournal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on TransactionJournal

Standard fields extend the TransactionJournal object for use in
         Billing to represent information about the general ledger accounts for billing
         transactions. This object is available in API version 63.0 and later.

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

         
         

You need the Revenue Cloud Billing license and the Accounts Receivables Admin permission
            set to access this object.

      

      

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

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

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
- 

                  

               

            
| Field | Details |
| --- | --- |
| ActivityDate | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time when a billing transaction record is posted or processed. |
| Credit | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The transaction record amount when a credit general ledger account is specified. |
| CreditGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the general ledger account for a debit transaction that's related to the transaction journal. This field is a relationship field. **Relationship Name** CreditGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| Debit | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The transaction record amount when a debit general ledger account is specified. |
| DebitGeneralLedgerAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the General Ledger (GL) Treatment based on which transaction journals must be generated for the billing transaction. This field is a relationship field. **Relationship Name** DebitGeneralLedgerAccount **Refers To** GeneralLedgerAccount |
| ForeignExchangeGainOrLossType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of foreign exchange gain or loss for the transaction journal. This field is available in API version 65.0 and later. Valid values are: `Realized` `Unrealized` `UnrealizedReversal` |
| GeneralLedgerAcctAsgntRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The general ledger account assignment rule used to assign general ledger accounts to transaction journals that’s created for billing transactions. This field is a relationship field. **Relationship Name** GeneralLedgerAcctAsgntRule **Refers To** GeneralLedgerAcctAsgntRule |
| GenlLdgrJournalEntryRuleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The general ledger journal entry rule used to assign general ledger accounts to transaction journals created for billing transactions. This field is available in API version 65.0 and later. This field is a relationship field. **Relationship Name** GenlLdgrJournalEntryRule **Refers To** GeneralLedgerJrnlEntryRule |
| LegalEntityId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The legal entity that's related to the transaction journal. This field is a relationship field. **Relationship Name** LegalEntity **Refers To** LegalEntity |
| ReferenceTransactionRecordId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The transaction record for which the transaction journal is created. This field is a polymorphic relationship field. **Relationship Name** ReferenceTransactionRecord **Refers To** CreditMemo, CreditMemoInvApplication, CreditMemoLine, CreditMemoLineInvoiceLine, CreditMemoLineTax, Invoice, InvoiceLine, InvoiceLineTax, Payment, PaymentLineInvoice, PaymentLineInvoiceLine, Refund |
| TransactionType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The transaction type that's related to the transaction journal. Valid values are: `CreditMemo` `CreditMemoInvApplication` `CreditMemoLine` `CreditMemoLineTax` `CreditMemoLineInvoiceLine` `DebitMemoLine`—Available in API version 65.0 and later. `Invoice` `InvoiceLine` `InvoiceLineTax` `Payment`—Available in API version 64.0 and later. `PaymentLineInvoice`—Available in API version 64.0 and later. `PaymentLineInvoiceLine`—Available in API version 64.0 and later. `Refund`—Available in API version 64.0 and later. `RefundLine`—Available in API version 64.0 and later. |
| UniqueIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** An auto-generated identifier for the transaction journal when the usage type is Billing. The identifier is a combination of the reference transaction record ID, the general ledger account assignment rule ID, and other internal-only fields. |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of usage. Valid value is: `Billing` |

      

      
   

#### See Also

- [*Loyalty Management Developer Guide*: TransactionJournal](https://developer.salesforce.com/docs/atlas.en-us.264.0.loyalty.meta/loyalty/sforce_api_objects_transactionjournal.htm)

=== ARTICLE: billing_std_objects_parent.htm ===
---
page_id: billing_std_objects_parent.htm
title: Billing Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_std_objects_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Standard Objects

The Billing data model provides objects and fields to manage billing and tax
  configurations, credit memos, and invoices, and accounting periods for legal entities.

- 
**[AccountingPeriod](./sforce_api_objects_accountingperiod.htm.md)**  

Represents information about a time period for which businesses          prepare reports and analyze performance. Each billing transaction is associated with an          accounting period. This object is available in API version 62.0 and later.

- 
**[BillingArrangement](./sforce_api_objects_billingarrangement.htm.md)**  

       Represents the arrangement for invoicing a transaction’s billing amount to          one or more accounts. The arrangement specifies whether the total amount must be invoiced          to the owning account or a different billing account, or whether the invoices must be split          among multiple billing accounts. This object is available in API version 66.0 and       later.

- 
**[BillingArrangementLine](./sforce_api_objects_billingarrangementline.htm.md)**  

       Represents the billing account, billing profile, and the percentage of          billing amount to be invoiced. Each billing arrangement line results in a separate invoice          addressed to the selected billing account. This object is available in API version       66.0 and later.

- 
**[BillingBatchScheduler](./sforce_api_objects_billingbatchscheduler.htm.md)**  

Represents a scheduled processing job that triggers recurring invoice          batch runs. This object is available in API version 62.0 and later.

- 
**[BillingBatchFilterCriteria](./sforce_api_objects_billingbatchfiltercriteria.htm.md)**  

       Represents the filter that all eligible billing schedules must satisfy in          order to be picked up by an invoice run. This object is available in API version 62.0       and later.

- 
**[BillingForecast](./sforce_api_objects_billingforecast.htm.md)**  

       Represents forecasted invoice lines generated from billing schedules before actual invoicing occurs. This object is available in API version 68.0 and later.    

- 
**[BillingMilestonePlan](./sforce_api_objects_billingmilestoneplan.htm.md)**  

Represents a structured approach to invoicing where invoices are          scheduled based on predefined milestones. This object is available in API version 63.0       and later.

- 
**[BillingMilestonePlanItem](./sforce_api_objects_billingmilestoneplanitem.htm.md)**  

Represents a specific billing milestone within the billing milestone          plan that’s used to manage and track billing based on the completion of certain          deliverables or stages. This object is available in API version 63.0 and later. 

- 
**[BillingPeriodItem](./sforce_api_objects_billingperioditem.htm.md)**  

Represents a payment period for an invoice. The billing period item          is used to pass billing information to an invoice line. This object is available in       API version 62.0 and later.

- 
**[BillingPolicy](./sforce_api_objects_billingpolicy.htm.md)**  

Represents information about a set of billing treatments that define          the rules to invoice a customer for an order item. This object is available in API       version 62.0 and later.

- 
**[BillingSchedule](./sforce_api_objects_billingschedule.htm.md)**  

Represents information about the order item that's used in the invoicing          process. This object is available in API version 62.0 and later.

- 
**[BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)**  

Represents a consolidated view of all the billing schedules related          to the order items generated from one asset, including new orders and amendment          orders. This object is available in API version 62.0 and later.

- 
**[BillingTreatment](./sforce_api_objects_billingtreatment.htm.md)**  

Represents information about the billing of an order item. This       object is available in API version 62.0 and later.

- 
**[BillingTreatmentItem](./sforce_api_objects_billingtreatmentitem.htm.md)**  

Represents information about allocation of the total amount of an          order item to billing schedules throughout the order item's lifecycle. This object is       available in API version 62.0 and later.

- 
**[BsgRelationship](./sforce_api_objects_bsgrelationship.htm.md)**  

Represents a relationship between billing schedule groups to support          bundles where one parent billing schedule group has multiple child billing schedule          groups. This object is available in API version 62.0 and later.

- 
**[CaseServiceProcessExtension](./sforce_api_objects_caseserviceprocessextension.htm.md)**  

Represents additional information for a case record based on the type of service          process for which the case was raised. This object is available in API version 67.0       and later.

- 
**[CreditMemo](./sforce_api_objects_creditmemo.htm.md)**  

Represents a document that’s used to reduce the amount that a buyer          owes a seller under the terms of an earlier invoice. This object is available in API       version 62.0 and later.

- 
**[CreditMemoAddressGroup](./sforce_api_objects_creditmemoaddressgroup.htm.md)**  

Represents the storage of the buyer's address information, which is          used to determine the tax credit amount for a buyer when a credit memo is issued. This       object is available in API version 62.0 and later.

- 
**[CreditMemoInvApplication](./sforce_api_objects_creditmemoinvapplication.htm.md)**  

Represents information about the application of a credit memo to an          invoice. This object is available in API version 62.0 and later.

- 
**[CreditMemoLine](./sforce_api_objects_creditmemoline.htm.md)**  

Represents the product, service, adjustment, or tax line items          included in a credit memo. This object is available in API version 62.0 and       later.

- 
**[CreditMemoLineInvoiceLine](./sforce_api_objects_creditmemolineinvoiceline.htm.md)**  

Represents a junction between a credit memo line and an invoice          line. This object is available in API version 62.0 and later.

- 
**[CreditMemoLineTax](./sforce_api_objects_creditmemolinetax.htm.md)**  

Represents tax information of a credit memo line of type `Tax`. This object is available in API version 62.0 and       later.

- 
**[DebitMemo](./sforce_api_objects_debitmemo.htm.md)**  

       Represents the document used to charge an additional amount to a buyer by a          seller. An invoice is generated for the debit memo in the next invoice run. This       object is available in API version 65.0 and later.

- 
**[DebitMemoAddress](./sforce_api_objects_debitmemoaddress.htm.md)**  

Represents the buyer's address information, which is used to          determine the tax amount for a buyer when a debit memo is issued. This object is       available in API version 65.0 and later.

- 
**[DebitMemoLine](./sforce_api_objects_debitmemoline.htm.md)**  

Represents the additional charge amount that the buyer must pay for          the product, service, or debit memo line tax that’s related to the debit memo. This       object is available in API version 65.0 and later.

- 
**[DebitMemoLineTax](./sforce_api_objects_debitmemolinetax.htm.md)**  

Represents the tax information for a debit memo line. This       object is available in API version 66.0 and later.

- 
**[GeneralLedgerAccount](./sforce_api_objects_generalledgeraccount.htm.md)**  

Represents information about the accounting codes, types, and names that are used          to store and organize financial transactions. This object is available in API version       63.0 and later.

- 
**[GeneralLedgerAcctAsgntRule](./sforce_api_objects_generalledgeracctasgntrule.htm.md)**  

Represents information about the rule based on which general ledger accounts are          assigned to transaction journals that are created for billing transactions. This       object is available in API version 63.0 and later.

- 
**[GeneralLdgrAcctPrdSummary](./sforce_api_objects_generalldgracctprdsummary.htm.md)**  

Represents a junction between a general ledger account and a legal          entity accounting period. Stores information about the total credit amount, total debit          amount, opening balance, and closing balance of a general ledger account for a specific          legal entity accounting period. This object is available in API version 65.0 and       later.

- 
**[GeneralLedgerJrnlEntryRule](./sforce_api_objects_generalledgerjrnlentryrule.htm.md)**  

       Represents information about the transaction journal entry rule, based on          which transaction journals are created for the selected credit and debit general ledger          accounts, transaction amount field, and percentage. This object is available in API       version 65.0 and later.

- 
**[InvBatchDraftToPostedRun](./sforce_api_objects_invbatchdrafttopostedrun.htm.md)**  

Represents information about the batch job that posts all invoices          with the status as `Draft` that are generated by the          invoice batch run associated with the billing schedule. This object is available in       API version 62.0 and later.

- 
**[Invoice](./sforce_api_objects_invoice.htm.md)**  

Represents information about a financial document describing the          total amount a buyer must pay for provided products or services. This object is       available in API version 62.0 and later.

- 
**[InvoiceAddressGroup](./sforce_api_objects_invoiceaddressgroup.htm.md)**  

Represents the storage of the buyer's address information. This       object is available in API version 62.0 and later.

- 
**[InvoiceBatchRun](./sforce_api_objects_invoicebatchrun.htm.md)**  

Represents a batch processing job in Billing. During an invoice batch          run, all billing schedules that meet the specified criteria are processed, resulting in the          generation of invoices. This object is available in API version 62.0 and       later.

- 
**[InvoiceBatchRunCriteria](./sforce_api_objects_invoicebatchruncriteria.htm.md)**  

Represents a batch processing job and its required criteria in          Billing. During an invoice batch run, all billing schedules that meet the specified          criteria are processed, resulting in the generation of invoices. This object is       available in API version 62.0 and later.

- 
**[InvoiceBatchRunRecovery](./sforce_api_objects_invoicebatchrunrecovery.htm.md)**  

Represents information about the recovery procedure of an invoice          batch run. This object is available in API version 62.0 and later.

- 
**[InvoiceDocument](./sforce_api_objects_invoicedocument.htm.md)**  

       Represents the PDF document generated for an invoice. This object is       available in API version 63.0 and later.

- 
**[InvoiceLine](./sforce_api_objects_invoiceline.htm.md)**  

Represents the amount that a buyer must pay for a product, service,          or fee. Invoice lines are created based on the amount of an order line. This object is       available in API version 62.0 and later.

- 
**[InvoiceLineRelationship](./sforce_api_objects_invoicelinerelationship.htm.md)**  

Represents a relationship between invoice line items to support          bundles where one parent invoice line has multiple child invoice lines. This object is       available in API version 62.0 and later. 

- 
**[InvoiceLineTax](./sforce_api_objects_invoicelinetax.htm.md)**  

Represents tax information of an invoice line of type `Tax`. This object is available in API version 62.0 and       later.

- 
**[LegalEntity](./sforce_api_objects_legalentity.htm.md)**  

Represents the way an organization is structured. An organization can          be a single legal entity or it can comprise more than one legal entity. This object is       available in API version 62.0 and later.

- 
**[LegalEntyAccountingPeriod](./sforce_api_objects_legalentyaccountingperiod.htm.md)**  

Represents a junction between a legal entity and an accounting          period. This object is available in API version 62.0 and later.

- 
**[PaymentAdviceInvoiceRecile](./sforce_api_objects_paymentadviceinvoicerecile.htm.md)**  

       Represents an invoice match with a payment advice line, linking a payment advice line to an open invoice. This object is available in API version 68.0 and later.    

- 
**[PaymentAdviceReconciliation](./sforce_api_objects_paymentadvicereconciliation.htm.md)**  

       Represents the reconciliation of a payment advice with a bank transaction and a resolved account, including match confidence and the reviewer’s decision. This object is available in API version 68.0 and later.    

- 
**[PaymentBatchRun](./sforce_api_objects_paymentbatchrun.htm.md)**  

       Represents a batch processing job that processes payments in Billing. During          a payment batch run, all the payment schedules that meet the specified criteria are          processed and the corresponding Payment records are created. These payments are then          applied to invoices or invoice lines. This object is available in API version 64.0 and       later.

- 
**[PaymentLineInvoiceLine](./sforce_api_objects_paymentlineinvoiceline.htm.md)**  

Represents information about a payment line that's applied to or          unapplied from an invoice line. This object is available in API version 64.0 and       later.

- 
**[PaymentRetryRule](./sforce_api_objects_paymentretryrule.htm.md)**  

Represents the specific payment retry rule for a failed payment          schedule item. Each rule defines actionable parameters such as the maximum number of          retries for the failed records and time intervals between subsequent retry attempts.       This object is available in API version 66.0 and later.

- 
**[PaymentRetryRuleSet](./sforce_api_objects_paymentretryruleset.htm.md)**  

Represents the payment retry rule definition that defines how failed          payments are retried based on the error codes across various retry categories. This       object is available in API version 66.0 and later.

- 
**[PaymentSchedule](./sforce_api_objects_paymentschedule.htm.md)**  

Represents information about a set of payments that a customer wants          to collect at different times for a certain record. A schedule contains one or more payment          schedule items, where each item represents one payment to be processed. Each of a          schedule’s items can have different payment configuration fields, such as payment methods,          payment dates, and payment accounts. When a payment scheduler launches a payment run, the          run evaluates active payment schedule items, and picks them up for payment processing if          they match the scheduler’s payment criteria. This object is available in API version       64.0 and later.

- 
**[PaymentSchedulePolicy](./sforce_api_objects_paymentschedulepolicy.htm.md)**  

       Represents information about the configuration for the payment schedule.       This object is available in API version 64.0 and later.

- 
**[PaymentScheduleTreatment](./sforce_api_objects_paymentscheduletreatment.htm.md)**  

       Represents information about the processing of payment schedules including          the payment method and the payment amount for the payment schedule. This object is       available in API version 64.0 and later.

- 
**[PaymentScheduleTreatmentDtl](./sforce_api_objects_paymentscheduletreatmentdtl.htm.md)**  

       Represents information about the processing of payment schedules after the          corresponding invoices are posted. This object is available in API version 64.0 and       later.

- 
**[PymtSchdDistributionMethod](./sforce_api_objects_pymtschddistributionmethod.htm.md)**  

Represents information about the partial payments that the total          payment is divided into. This object is available in API version 64.0 and       later.

- 
**[PaymentScheduleItem](./sforce_api_objects_paymentscheduleitem.htm.md)**  

Represents information about a payment to be processed. Each schedule          item can have different payment configuration fields, such as payment methods, payment          dates, and payment accounts. When a payment scheduler launches a payment run, the run          evaluates active payment schedule items, and picks them up for payment processing if they          match the scheduler’s payment criteria. This object is available in API version 64.0       and later.

- 
**[PaymentTerm](./sforce_api_objects_paymentterm.htm.md)**  

Represents an agreement between a buyer and a seller about when          payment is due for an invoice. This object is available in API version 62.0 and       later.

- 
**[PaymentTermItem](./sforce_api_objects_paymenttermitem.htm.md)**  

Represents configuration of a payment term. This object is       available in API version 62.0 and later.

- 
**[RefundLineCreditMemo](./sforce_api_objects_refundlinecreditmemo.htm.md)**  

       Represents a junction between a refund and a credit memo. This object is available in API version 68.0 and later.    

- 
**[RefundLineCreditMemoLine](./sforce_api_objects_refundlinecreditmemoline.htm.md)**  

       Represents a junction between a refund and a credit memo line. This object is available in API version 68.0 and later.    

- 
**[RevenueTransactionErrorLog](./sforce_api_objects_revenuetransactionerrorlog.htm.md)**  

       Represents the details of errors that occurred during the processing of a          request. The error record persists until a new error with the same category, primary          record, and, if necessary, related record occurs. This object is available in API       version 62.0 and later.

- 
**[SeqPolicySelectionCondition](./sforce_api_objects_seqpolicyselectioncondition.htm.md)**  

Represents the condition used to determine which sequence policy is          applied to a record. This object is available in API version 65.0 and       later.

- 
**[SequenceGapReconciliation](./sforce_api_objects_sequencegapreconciliation.htm.md)**  

Represents a missing sequence value identified during reconciliation,          which can be used later to ensure there are no gaps in the sequence policy numbers.       This object is available in API version 65.0 and later.

- 
**[SequencePolicy](./sforce_api_objects_sequencepolicy.htm.md)**  

Represents the configuration of rules and parameters for generating          unique, sequential numbers for records. Stores settings such as numbering patterns,          prefixes, suffixes, sequence start numbers, increment values, and filter criteria to ensure          accurate and compliant numbering. This object is available in API version 65.0 and       later.

- 
**[TaxEngine](./sforce_api_objects_taxengine.htm.md)**  

Represents information about an instance of a tax engine provider as          well as the merchant credentials for that specific instance. This object is available       in API version 62.0 and later.

- 
**[TaxEngineInteractionLog](./sforce_api_objects_taxengineinteractionlog.htm.md)**  

       Represents a record of a communication with an external tax engine following          a tax calculation request.  This object is available in API version 62.0 and later. 

- 
**[TaxEngineProvider](./sforce_api_objects_taxengineprovider.htm.md)**  

Represents general information about a service that manages a tax          engine. Tax engine providers have a one-to-many relationship with tax engines, where the          tax engine record represents a specific configuration of a tax engine that can be assigned          to multiple order items. This object is available in API version 62.0 and       later.

- 
**[TaxPolicy](./sforce_api_objects_taxpolicy.htm.md)**  

Represents information about a group of tax treatments, where each          treatment represents parameters to determine how a particular product is taxed for a          transaction line item. Tax policies are related to products, which pass the policy on to          the resulting order items and in turn the billing schedules. This object is available       in API version 62.0 and later.

- 
**[TaxTreatment](./sforce_api_objects_taxtreatment.htm.md)**  

Represents information about tax calculation by external          engines. Each product requires a tax policy to determine whether to apply tax. Each tax          policy requires at least one tax treatment. The tax treatments determine how taxable          products are taxed. This object is available in API version 62.0 and       later.

- 
**[Tax Treatment Item](./sforce_api_objects_taxtreatmentitem.htm.md)**  

Represents tax code information that’s used to calculate tax for a          product by a specific tax engine. This object is available in API version 66.0 and       later.

#### See Also

- [*Object Reference for the platform*: Overview of Salesforce Objects
       and Fields](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)

- [*SOAP API Developer Guide*: Introduction to SOAP API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_quickstart_intro.htm)

=== ARTICLE: billing_tax_contract_mappings_for_invoices_and_credits.htm ===
---
page_id: billing_tax_contract_mappings_for_invoices_and_credits.htm
title: Tax Mappings for Invoices and Credits
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_tax_contract_mappings_for_invoices_and_credits.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_tax_engine_adapter_interface_for_standard_tax.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Mappings for Invoices and Credits

You can extend and customize the existing tax interface by using custom metadata types
    and tax mappings. These customizations help you with unique business requirements such as the
    inclusion of specific data for accurate calculations and audits.

    
      

Here are some prerequisites before you work with the tax mappings for invoices and
        credits.

      
        
- See [custom metadata types](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_overview.htm&language=en_US) to
          specify all your tax mapping definitions.

        
- See [details on extension of your tax
            contract](https://help.salesforce.com/s/articleView?id=ind.billing_custom_metadata_types_configure.htm&language=en_US) with custom fields.

        
- Tax callout extensions are supported for the Invoice, Invoice Line, Invoice Line Tax,
          Credit Memo, Credit Memo Line, and Credit Memo Line Tax objects.

      

    

    

## Request Mappings for Header Attributes

      
      

This table defines the request mappings between the header attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Header Attributes | Invoice Mapping | Negative Invoice Mapping | Credit Mapping |
| --- | --- | --- | --- |
| currencyIsoCode | Invoice.CurrencyISOCode | Invoice.CurrencyISOCode | CreditMemo.CurrencyISOCode |
| isCommit | If status is `DRAFT` then this value is `False`. If status is `POSTED`, then this value is `True`. | If status is `DRAFT` then this value is `False`. If status is POSTED, then this value is `True`. | This value is `True` until Summer ’25. From Winter ’26, if status is `DRAFT`, then this value is `False`. If status is `POSTED`, then this value is `True`. |
| referenceEntityId | Invoice.ID | Invoice.ID | CreditMemo.ID |
| taxEngineId | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID |
| transactionDate | SystemDate | SystemDate | SystemDate |
| **sellerDetails** |  |  |  |
| code | TaxEngine.SellerCode | TaxEngine.SellerCode | TaxEngine.SellerCode |
| **customerDetails** |  |  |  |
| accountId | Invoice.BillingAccount.ID | Invoice.BillingAccount.ID | CreditMemo.BillingAccount.ID |
| code | NULL | NULL | NULL |
| exemptionNo | Invoice.BillingAccount.TaxExemptionNumber. Available from Spring ’26. | Invoice.BillingAccount.TaxExemptionNumberAvailable from Spring ’26. | CreditMemo.BillingAccount.TaxExemptionNumberAvailable from Spring ’26. |
| exemptionReason | NULL | NULL | NULL |
| exemptionStatus | Invoice.BillingAccount.TaxExemptionStatusAvailable from Spring ’26. | Invoice.BillingAccount.TaxExemptionStatusAvailable from Spring ’26. | CreditMemo.BillingAccount.TaxExemptionStatusAvailable from Spring ’26. |
| exemptionExpirationDate | Invoice.BillingAccount.TaxExemptionExpirationDateAvailable from Spring ’26. | Invoice.BillingAccount.TaxExemptionExpirationDateAvailable from Spring ’26. | CreditMemo.BillingAccount.TaxExemptionExpirationDateAvailable from Spring ’26. |
| deliveryTerms | Invoice.BillingAccount.DeliveryTermsAvailable from Spring ’26. | Invoice.BillingAccount.DeliveryTermsAvailable from Spring ’26. | CreditMemo.BillingAccount.DeliveryTermsAvailable from Spring ’26. |
| billingProfileId | Invoice.BillingAccount.IDAvailable from Spring ’26. | Invoice.BillingAccount.IDAvailable from Spring ’26. | CreditMemo.BillingAccount.IDAvailable from Spring ’26. |
| additionalTaxIdentificationDetails | Invoice.BillingAccount.AddTaxIdentificationDetailsAvailable from Spring ’26. | Invoice.BillingAccount.AddTaxIdentificationDetailsAvailable from Spring ’26. | CreditMemo.BillingAccount.AddTaxIdentificationDetailsAvailable from Spring ’26. |
| taxIdentificationNumber | Invoice.BillingAccount.TaxIdentificationNumberAvailable from Spring ’26. | Invoice.BillingAccount.TaxIdentificationNumberAvailable from Spring ’26. | CreditMemo.BillingAccount.TaxIdentificationNumberAvailable from Spring ’26. |
| taxType | If status is `DRAFT`, then this value is `Estimated`. If status is `POSTED`, then this value is `Actual`. | If status is `DRAFT`, then this value is `Estimated`. If status is `POSTED`, then this value is `Actual`. | This value is `Actual` until Summer ’25. From Winter ’26, if status is `DRAFT`, then this value is `Estimated`. If status is POSTED, then this value is `Actual`. |
| taxTransactionType | Debit | Credit | Credit |
| effectiveDate | invoice.InvoiceDate | If you're creating from negative lines, then this value is the original `Invoice.InvoiceDate` value. | If you're using standalone credit memo, then this value is the `CreditMemo.CreditDate` value. |
| **addresses** |  |  |  |
| billTo | NULL | NULL | NULL |
| shipTo | NULL | NULL | NULL |
| shipFrom | NULL | NULL | NULL |
| soldTo | NULL | NULL | NULL |
| taxEngineAddress | TaxEngine.Address | TaxEngine.Address | TaxEngine.Address |
| referenceDocumentCode | NULL | If you're converting from negative lines, then this value is the original document code `Invoice.ID & "Debit" & TaxEngine.ID`. | If you're using standalone credit memo, then this value is NULL. Otherwise, this value is the `documentCode` value of the original invoice. |
| description | Invoice.Description | Invoice.Description | Invoice.Description |
| documentCode | `Invoice.ID & "_Debit_" & TaxEngine.ID` | `Invoice.ID & "_Credit_" & TaxEngine.ID` | `CreditMemo.ID & "_Credit_" & TaxEngine.ID` |
| shouldVoid | FALSE | From Winter ’26, if the request is to void a posted invoice, then this value is TRUE. Else, it is FALSE. | FALSE |
| lineItems | Refer to the next line attributes section. | Refer to the next line attributes section. | Refer to the next line attributes section. |

    

    

## Request Mappings for Line Attributes

      
      

This table defines the request mappings between the line attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Line Attributes | Invoice Mapping | Negative Invoices | Credit Mapping |
| --- | --- | --- | --- |
| taxCode | TaxTreatment.TaxCode | TaxTreatment.TaxCode | TaxTreatment.TaxCode |
| productCode | TaxTreatment.ProductCode | TaxTreatment.ProductCode | TaxTreatment.ProductCode |
| productId | InvoiceLine.ProductId | InvoiceLine.ProductId | ProductId |
| amount | InvoiceLine.ChargeAmount | InvoiceLine.ChargeAmount | CreditMemoLine.ChargeAmount |
| effectiveDate | InvoiceLine.Invoice.InvoiceDate | If you're creating from negative lines, then this value is the original `Invoice.InvoiceDate` value. | CreditMemoLine.CreditMemo.CreditDate |
| lineNumber | InvoiceLine.ID | InvoiceLine.ID | CreditMemoLine.ID |
| description | InvoiceLine.Description | InvoiceLine.Description | CreditMemoLine.Description |
| quantity | InvoiceLine.Quantity | InvoiceLine.Quantity | NULL |
| **addresses** |  |  |  |
| billTo | InvoiceLine.BillingAddress.Address | InvoiceLine.BillingAddress.Address | CreditMemoLine.BillingAddress.Address |
| shipTo | InvoiceLine.ShippingAddress.Address | InvoiceLine.ShippingAddress.Address | CreditMemoLine.ShippingAddress.Address |
| shipFrom | InvoiceLine.ShippingFrom.Address | InvoiceLine.ShippingFrom.Address | CreditMemoLine.ShippingFrom.Address |
| soldTo | NULL | NULL | NULL |
| productsku | InvoiceLine.Product.productCode | InvoiceLine.Product.productCode | CreditMemoLine.Product.productCode |
| referenceDocumentCode | NULL | If you're converting from negative lines, then this value is the original `Document Code - "Invoice.ID" & "Debit" & TaxEngine.ID`. | If you're using standalone credit memo, then this value is NULL. Otherwise, this value is the `documentCode` value of the original invoice. |

    

    

## Response Mappings for Header Attributes

      
      

This table defines the response mappings between the header attributes of a tax callout and
        fields of applicable objects. This response structure is used to create the InvoiceLineTax
        records.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Header Attributes | Invoice Mapping | Negative Invoice Mapping | Credit Mapping |
| --- | --- | --- | --- |
| currencyIsoCode | Invoice.CurrencyISOCode | Invoice.CurrencyISOCode | CreditMemo.CurrencyISOCode |
| isCommit | Not persisted. | Not persisted. | Not persisted. |
| referenceEntityId | Invoice.ID | Invoice.ID | CreditMemo.ID |
| taxEngineId | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID | TaxTreatment.TaxEngine.ID |
| transactionDate | SystemDate | SystemDate | SystemDate |
| **sellerDetails** |  |  |  |
| code | TaxEngine.SellerCode | TaxEngine.SellerCode | TaxEngine.SellerCode |
| **customerDetails** |  |  |  |
| accountId | Invoice.BillingAccount.ID | Invoice.BillingAccount.ID | Invoice.BillingAccount.ID |
| code | Not persisted. | Not persisted. | Not persisted. |
| exemptionNo | Not persisted. | Not persisted. | Not persisted. |
| exemptionReason | Not persisted. | Not persisted. | Not persisted. |
| taxType | If status is `DRAFT`, then this value is `Estimated`. If status is `POSTED`, then this value is `Actual`. | If status is `DRAFT`, then this value is `Estimated`. If status is `POSTED`, then this value is `Actual`. | Actual |
| taxTransactionType | Debit | Credit | Credit |
| effectiveDate | invoice.InvoiceDate | If you're creating from negative lines, then this value is the original `Invoice.InvoiceDate` value. | If you're using standalone credit memo, then this value is the `CreditMemo.CreditDate` value. If you're creating from negative lines, then this value is the original `Invoice.InvoiceDate` value. |
| **addresses** |  |  |  |
| billTo | Not persisted. | Not persisted. | Not persisted. |
| shipTo | Not persisted. | Not persisted. | Not persisted. |
| shipFrom | Not persisted. | Not persisted. | Not persisted. |
| soldTo | Not persisted. | Not persisted. | Not persisted. |
| taxEngineAddress | Not persisted. | Not persisted. | Not persisted. |
| referenceDocumentCode | Not persisted. | Not persisted. | Not persisted. |
| description | Not persisted. | Not persisted. | Not persisted. |
| documentCode | Invoice.ID & "_Debit_" & TaxEngine.ID | Invoice.ID & "_Credit_" & TaxEngine.ID | CreditMemo.ID & "_Credit_" & TaxEngine.ID |
| status | Committed |  |  |
| **taxEngineLogs** |  |  |  |
| resultCode | TaxEngineInteractionLog.ResultCode | TaxEngineInteractionLog.ResultCode | TaxEngineInteractionLog.ResultCode |
| createddate | Not persisted. | Not persisted. | Not persisted. |
| Id | Not persisted. | Not persisted. | Not persisted. |
| transactionDate | Not persisted. | Not persisted. | Not persisted. |
| **amountDetails** |  |  |  |
| exemptAmount | Not persisted. | Not persisted. | Not persisted. |
| taxAmount | If header tax is enabled, then this value is `Invoice.TotalTaxesCapturedAtHeader`. | If header tax is enabled, then this value is `Invoice.TotalTaxesCapturedAtHeader`. | If header tax is enabled, then this value is `CreditMemo.TotalTaxesCapturedAtHeader`. |
| totalAmount | Not persisted. | Not persisted. | Not persisted. |
| totalAmountWithTax | Not persisted. | Not persisted. | Not persisted. |
| lineItems | Refer to the next line attributes section. | Refer to the next line attributes section. | Refer to the next line attributes section. |

    

    

## Response Mappings for Line Attributes

      
      

This table defines the response mappings between the line attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Line Attributes | Invoice Mapping | Negative Invoices | Credit Mapping |
| --- | --- | --- | --- |
| taxCode | InvoiceLineTax.taxCode | InvoiceLineTax.taxCode | InvoiceLineTax.taxCode |
| productCode | Not persisted. | Not persisted. | Not persisted. |
| productId | Not persisted. | Not persisted. | Not persisted. |
| **amountDetails** |  |  |  |
| exemptAmount | Not persisted. | Not persisted. | Not persisted. |
| taxAmount | Not persisted. | Not persisted. | Not persisted. |
| totalAmount | Not persisted. | Not persisted. | Not persisted. |
| totalAmountWithTax | Not persisted. | Not persisted. | Not persisted. |
| effectiveDate | InvoiceLineTax.taxEffectiveDate | InvoiceLineTax.taxEffectiveDate | CreditMemoLineTax.taxEffectiveDate |
| lineNumber | InvoiceLineTax.InvoiceLine | InvoiceLineTax.InvoiceLine | CreditMemoLineTax.CreditMemoLine |
| description | Not persisted. | Not persisted. | Not persisted. |
| quantity | Not persisted. | Not persisted. | Not persisted. |
| **addresses** |  |  |  |
| billTo | Not persisted. | Not persisted. | Not persisted. |
| shipTo | Not persisted. | Not persisted. | Not persisted. |
| shipFrom | Not persisted. | Not persisted. | Not persisted. |
| soldTo | Not persisted. | Not persisted. | Not persisted. |
| productsku | Not persisted. | Not persisted. | Not persisted. |
| referenceDocumentCode | Not persisted. | Not persisted. | Not persisted. |
| taxes | Refer to the next tax attributes section. | Refer to the next tax attributes section. | Refer to the next tax attributes section. |

    

    

## Response Mappings for Tax Attributes

      
      

This table defines the response mappings between the tax attributes of a tax callout and
        fields of applicable objects.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Line Attributes | Invoice Mapping | Negative Invoices | Credit Mapping |
| --- | --- | --- | --- |
| exemptAmount | InvoiceLineTax.taxExemptAmount | InvoiceLineTax.taxExemptAmount | Not persisted. |
| exemptReason | Not persisted. | Not persisted. | Not persisted. |
| **imposition** |  |  |  |
| type | Not persisted. | Not persisted. | Not persisted. |
| Name | InvoiceLineTax.TaxName | InvoiceLineTax.TaxName | CreditMemoLineTax.TaxName |
| **jurisdiction** |  |  |  |
| country | Not persisted. | Not persisted. | Not persisted. |
| id | Not persisted. | Not persisted. | Not persisted. |
| level | Not persisted. | Not persisted. | Not persisted. |
| name | Not persisted. | Not persisted. | Not persisted. |
| region | Not persisted. | Not persisted. | Not persisted. |
| stateAssignedNo | Not persisted. | Not persisted. | Not persisted. |
| rate | InvoiceLineTax.taxRate | InvoiceLineTax.taxRate | CreditMemoLineTax.TaxRate |
| tax | InvoiceLineTax.taxAmount | InvoiceLineTax.taxAmount | CreditMemoLineTax.TaxAmount |
| taxId | InvoiceLineTax.TaxTransactionNumber | InvoiceLineTax.TaxTransactionNumber | CreditMemoLineTax.TaxTransactionNumber |
| taxableAmount | Not persisted. | Not persisted. | Not persisted. |

=== ARTICLE: billing_tax_engine_adapter_interface_for_standard_tax.htm ===
---
page_id: billing_tax_engine_adapter_interface_for_standard_tax.htm
title: TaxEngineAdapter Interface
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_tax_engine_adapter_interface_for_standard_tax.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_apex_reference.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TaxEngineAdapter Interface

Retrieves and evaluates the details from a tax engine to define tax
        details.

        

You can extend the TaxEngineAdapter interface to define a custom tax adapter based on
            your requirements. Use the custom tax adapter with Billing services to implement
            standard tax.

        

Create a custom object and associated fields to store tax details, such as tax rate for a
            country. For example, create a custom object named CountryTaxRate with Country_Code and
            Tax_Rate fields. Create records to define the details for these fields.

    

- 
**[TaxEngineAdapter Methods](./apex_commercetax_TaxEngineAdapter_methods.htm.md)**  

Learn more about the available methods with the `TaxEngineAdapter` class.

- 
**[TaxEngineAdapter Example Implementation](./billing_apex_interface_TaxEngineAdapter_Example.htm.md)**  

Refer to the example implementation of the `TaxEngineAdapter` interface to accept information from a tax engine and         evaluate the information to define tax details.

- 
**[Tax Mappings for Invoices and Credits](./billing_tax_contract_mappings_for_invoices_and_credits.htm.md)**  

You can extend and customize the existing tax interface by using custom metadata types     and tax mappings. These customizations help you with unique business requirements such as the     inclusion of specific data for accurate calculations and audits.

#### See Also

- [*Salesforce Help*: Tax Calculation for Invoices](https://help.salesforce.com/s/articleView?id=ind.billing_tax_configuration.htm&language=en_US)

- [*Billing Business APIs*: Tax Calculation (POST)](./connect_resources_calculate_taxes.htm.md)

- [*Billing Standard Objects*: TaxEngineProvider, TaxEngine, TaxPolicy, and
       TaxTreatment](./billing_std_objects_parent.htm.md)

- [Tax Engine Reference Gateway Adapter](https://github.com/salesforce-misc/salesforce-tax-engine-reference-gateway-adapters)

=== ARTICLE: billling_sforce_api_objects_accountbillingaccount.htm ===
---
page_id: billling_sforce_api_objects_accountbillingaccount.htm
title: Billing Fields on AccountBillingAccount
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billling_sforce_api_objects_accountbillingaccount.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on AccountBillingAccount

Standard fields extend the AccountBillingAccount object for use in
         Billing to represent information about default billing accounts. This object is
      available in API version 63.0 and later.

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

         
         

You need the Billing Admin permission set, Billing Operations User permission set, or
            Billing Customer Service User permission set access to this object.

      

      

## Fields

         
         

               
               
               
                  
                     

                     

                  

               

               
                  
                     

                     

: 

: 

: 
: 

                  

               

            
| Field | Details |
| --- | --- |
| IsDefaultBillingAccount | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the account is the default billing account (`true`) or not (`false`). The default value is `false`. |

      

      
   

#### See Also

- [*Energy and Utilities Cloud Developer Guide*: AccountBillingAccount](https://developer.salesforce.com/docs/atlas.en-us.264.0.eu_developer_guide.meta/eu_developer_guide/sforce_api_objects_accountbillingaccount.htm)

=== ARTICLE: billling_sforce_api_objects_billingaccount.htm ===
---
page_id: billling_sforce_api_objects_billingaccount.htm
title: Billing Fields on BillingAccount
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billling_sforce_api_objects_billingaccount.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_extended_standard_object_fields.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Fields on BillingAccount

Standard fields extend the BillingAccount object for use in Billing
         to represent information about the billing suspension date and the billing resumption
         date. This object is available in API version 63.0 and later.

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `search()`
         

      

      

## Special Access Rules

You need the Billing Admin permission set, Billing Operations User permission set, or Billing
            Customer Service User permission set access to this object.

      

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
- 
- 
- 
- 
- 
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

                  

               

            
| Field | Details |
| --- | --- |
| AccountID | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the account that's related to the billing account. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| AddTaxIdentificationDetails | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The additional tax identification details, such as a Peppol ID. Available in API version 66.0 and later. |
| BillDayOfMonth | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A number from 1 to 31 that indicates the billing date. Available in API version 64.0 and later. |
| BillToContactId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The contact associated with the billing account. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** BillToContact **Refers To** Contact |
| BillingResumptionDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when billing for the account is resumed. |
| BillingSuspensionDate | **Type** date **Properties** Filter, Group, Nillable, Sort **Description** The date when billing for the account is suspended. |
| DeliveryTerms | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The standard code in internal trades used to define shipping responsibilities. Valid values are: `CFR` `CIF` `CIO` `CPT` `CUS` `DAF` `DAP` `DDP` `DDU` `DEQ` `DES` `DPU` `EXW` `FAS` `FCA` `FOB` `SUP` The default value is `USD`. Available in API version 66.0 and later. |
| DoesSkipAutomaticPayments | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether to skip the automatic creation of payment schedules and payment schedule items for posted invoices related to billing accounts (`true`) or not (`false`). This boolean value is considered when the automatic creation of payment schedules and payment schedule items is turned on. Available in API version 65.0 and later. |
| EmailTemplateId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The template used for sending billing account emails. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** EmailTemplate **Refers To** Email template |
| InvoiceDocumentTemplateId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The document template that’s used to generate PDF documents for the invoices that are related to the billing account. Available in API version 66.0 and later. This field is a relationship field. **Relationship Name** InvoiceDocumentTemplate **Refers To** DocumentTemplate |
| IsDefaultBillingProfile | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the billing account is the default billing profile (`true`) or not (`false`). Available in API version 65.0 and later. |
| PaymentTermId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The payment term associated with the billing account. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** PaymentTerm **Refers To** PaymentTerm |
| SavedPaymentMethodId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The saved payment method that’s used to collect payments for the default billing profile of an account when the automatic creation of payment schedules and payment schedule items is turned on. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** SavedPaymentMethod **Refers To** SavedPaymentMethod |
| ShippingAddress | **Type** address **Properties** Filter, Nillable **Description** The shipping address of the billing account. Available in API version 64.0 and later. |
| ShouldAttachInvoiceDocToEmail | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether to attach the invoice PDF document to the email that’s sent to the billing account. Available in API version 65.0 and later. The default value is false. |
| TaxExemptionExpirationDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date until which the tax exemption is valid. Available in API version 66.0 and later. |
| TaxExemptionNumber | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A unique identifier used to indicate that a transaction is tax exempt. Available in API version 66.0 and later. |
| TaxExemptionStatus | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The status of the tax exemption with values defined by the user. Available in API version 66.0 and later. |
| TaxIdentificationNumber | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The tax identification number such as a VAT ID. Available in API version 66.0 and later. |

      

      
   

#### See Also

- [*Energy and Utilities Cloud Developer Guide*: BillingAccount](https://developer.salesforce.com/docs/atlas.en-us.264.0.eu_developer_guide.meta/eu_developer_guide/sforce_api_objects_billingaccount.htm)

=== ARTICLE: connect_requests_address_input.htm ===
---
page_id: connect_requests_address_input.htm
title: Address Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_address_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Address Input

Input representation of the details of an address.

**JSON example**

: 

              
                

**JSON example**

                
: 
                  

```
  "billingAddress": {
    "street": "1 Market St #300",
    "city": "San Francisco",
    "state": "CA",
    "country": "US",
    "postalCode": "94105",
    "latitude": "37.789901",
    "longitude": "-122.396923"
  }
```

                

              
            

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `city` | String | Address city. | Optional | 62.0 |
| `country` | String | Address country. | Optional | 62.0 |
| `latitude` | Double | Latitude for the address. | Optional | 62.0 |
| `locationCode` | String | Location code for the address. | Optional | 62.0 |
| `longitude` | Double | Longitude for the address. | Optional | 62.0 |
| `postalCode` | String | Postal code for the address. | Optional | 62.0 |
| `state` | String | Address state. | Optional | 62.0 |
| `street` | String | Address street. | Optional | 62.0 |

=== ARTICLE: connect_requests_addresses_input.htm ===
---
page_id: connect_requests_addresses_input.htm
title: Addresses Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_addresses_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Addresses Input

Input representation of the details of the addresses for calculating tax.

**JSON example**

: 

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
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billTo` | [Address Input](./connect_requests_address_input.htm.md) | Billing address of the item. | Optional | 62.0 |
| `shipFrom` | [Address Input](./connect_requests_address_input.htm.md) | Address that the item is shipped from. | Optional | 62.0 |
| `shipTo` | [Address Input](./connect_requests_address_input.htm.md) | Address that the item is shipped to. | Required | 62.0 |
| `soldTo` | [Address Input](./connect_requests_address_input.htm.md) | Address of the entity that the item is sold to. | Optional | 62.0 |

=== ARTICLE: connect_requests_batch_invoice_filter_criteria_input.htm ===
---
page_id: connect_requests_batch_invoice_filter_criteria_input.htm
title: Batch Invoice Filter Criteria Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_batch_invoice_filter_criteria_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoice Filter Criteria Input

Input representation of the filter criteria for an invoice batch run.

**JSON example**

: 

```
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
| `field​Name` | String | Name of the field that this filter is applicable for. Valid values are: `Currency_Iso_code`—If multiple currencies are enabled for the org, then this value is required. `InvoiceRunMatchingValue` `BillingAccount` `LegalEntity` `BillingTermUnit` | Required | 62.0 |
| `object​Name` | Object | Name of the object that the filter is applicable for. Valid values are: `BillingSchedule` `BillingScheduleGroup` | Required | 62.0 |
| `operation` | String | Operation to be performed for comparison. Valid values are: `Equals` `InList`—This value supports only the `InvoiceRunMatchingValue` and `BillingTermUnit` fields with API version 62.0 and later. In addition, this value supports the `CurrencyIsoCode` field with API version 63.0 and later. `NotEquals` | Required | 62.0 |
| `value` | String | Value for the filter criteria. | Required | 62.0 |

=== ARTICLE: connect_requests_batch_invoice_scheduler_input.htm ===
---
page_id: connect_requests_batch_invoice_scheduler_input.htm
title: Batch Invoice Scheduler Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_batch_invoice_scheduler_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Invoice Scheduler Input

Input representation of the details of the request to create an invoice
    scheduler.

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

=== ARTICLE: connect_requests_billing_schedule_input_for_amendment.htm ===
---
page_id: connect_requests_billing_schedule_input_for_amendment.htm
title: Amended Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_amendment.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Amended Transaction

Learn how amendments update quantity, price, and end date in billing schedules along
    with delta-only price transactions and billing-frequency changes at the billing schedule
    level.

## Considerations

      
      

Keep these important considerations in mind when providing the details for amended
        transactions.

      
        
- The `BillingActionType__std ` value for any amended
          transaction must be `Amend`.

        
- When you provide a negative quantity, make sure that it’s less than the total quantity
          of the related transaction.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the `transactionDetails` property value. All the
          other transaction details are automatically fetched from the sObject record if those
          details are mapped in the context definition.

      

    

    

## Amendment Payload Types

The Create Standalone Billing Schedules API
        accepts two amendment payload types in the `transactionDetails` node. Use the type that matches the level of detail you want
        to provide in the request.

Simplified amendment payloads support these scenarios.

        
- Negative amendment to reduce quantity

        
- Positive amendment to add quantity

        
- Price amendment to change net or unit price from an effective date

        
- End date change to extend or shorten the subscription term

        
- Delta price change to pass a price delta as a single adjustment

        
- Billing frequency update at the billing schedule group level

      

Detailed amendment payloads cover the same business outcomes when you specify all
      transaction details and financial fields.
        
          

**Simplified amendment payload**

          
: 
            

Set `BillingActionType__std` to `Amend`. Set `BillingSubActionType__std` to `QuantityAmend`, `PriceAmend`, `EndDateChange`, `DeltaPriceAmend`, or `BillingFrequencyChange` depending on the scenario. Include `TransactionId__std` and `StartDate__std`. Identify the source with either `RelatedTransactionId__std` (one billing schedule) or
                `BillingScheduleGroupId__std` (a billing schedule
              group). The examples in the scenario-specific sections in this topic use `RelatedTransactionId__std`. For amendments by using a
              billing schedule group as source, use `BillingScheduleGroupId__std` instead.

            
              
                

**Negative amendment (QuantityAmend)**

                
: 

Reduce quantity from a start date by specifying the reduction quantity as a
                    negative number along with the start date.

If you specify a related
                    transaction, the reduction is applied against that transaction’s billing
                    schedules. If you specify a billing schedule group ID, the API applies
                    reductions in Last In, First Out (LIFO) order within that billing schedule
                    group.

The API determines which billing schedules to reduce, validates
                    that sufficient net quantity exists, and checks whether price can be derived
                    through proration or whether `TotalPrice` can
                    be accepted when specified.

This sample includes a negative `Quantity__std` for the quantity to remove from the
                    effective date.

```
{
  "Transaction": [
    {
      "TransactionId__std": "a2",
      "RelatedTransactionId__std": "a1",
      "StartDate__std": "2025-05-01",
      "Quantity__std": -2,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "QuantityAmend"
    }
  ]
}
```

This sample shows the request payload for the same negative
                    quantity amendment.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"a2\",\"RelatedTransactionId__std\":\"a1\",\"StartDate__std\":\"2025-05-01\",\"Quantity__std\":-2,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"QuantityAmend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This sample shows the transaction data that references a billing
                    schedule group.

```
{
  "Transaction": [
    {
      "TransactionId__std": "a2",
      "BillingScheduleGroupId__std": "9Ws00000AXB00AAI",
      "StartDate__std": "2025-05-01",
      "Quantity__std": -2,
      "BillingActionType__std": "Amend",
     "BillingSubActionType__std": "QuantityAmendment"
    }
  ]
}
```

This sample shows the request payload when billing schedule
                    group is used as a
                  reference.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"a2\",\"BillingScheduleGroupId__std\":\"9Ws00000AXB00AAI\",\"StartDate__std\":\"2025-05-01\",\"Quantity__std\":-2,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"QuantityAmendment\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

              
              
                

**Positive amendment (QuantityAmend)**

                
: 

Add quantity from a start date. Specify minimal information in the payload.
                    The API derives the billing schedule to amend and, if not specified, the unit
                    price and total price. Use a positive `Quantity__std` for the quantity to add from the effective
                    date.

```
{
  "Transaction": [
    {
      "TransactionId__std": "a2",
      "RelatedTransactionId__std": "a1",
      "StartDate__std": "2025-05-01",
      "Quantity__std": 2,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "QuantityAmend"
    }
  ]
}
```

This sample shows the request payload for the same positive
                    quantity amendment.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"a2\",\"RelatedTransactionId__std\":\"a1\",\"StartDate__std\":\"2025-05-01\",\"Quantity__std\":2,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"QuantityAmend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This sample shows the transaction data that references a billing
                    schedule group.

```
{
  "Transaction": [
    {
      "TransactionId__std": "a2",
      "BillingScheduleGroupId__std": "9Ws00000AXB00AAI",
      "StartDate__std": "2025-05-01",
      "Quantity__std": 2,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "QuantityAmendment"
    }
  ]
}
```

This sample shows the request payload when billing schedule
                    group is used as a
                  reference.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"a2\",\"BillingScheduleGroupId__std\":\"9Ws00000AXB00AAI\",\"StartDate__std\":\"2025-05-01\",\"Quantity__std\":2,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"QuantityAmendment\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

              
              
                

**Price amendment (PriceAmend)**

                
: 

Change the price from a given start date. For example, apply a new net unit
                    price or unit price. The API cancels the existing billing schedule(s) from that
                    date and creates new positive amendment billing schedule with the updated price
                    . Specify the new `NetUnitPrice__std` or
                      `UnitPrice__std` effective on `StartDate__std`. This sample uses net unit
                    price.

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter3",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2026-04-01",
      "NetUnitPrice__std": 20,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "PriceAmend"
    }
  ]
}
```

This sample shows the request payload for the same price
                    amendment.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter3\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2026-04-01\",\"NetUnitPrice__std\":20,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"PriceAmend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This sample shows the transaction data that references a billing
                    schedule group with delta quantity to amend price on an entire billing schedule
                    group.

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter4",
      "BillingScheduleGroupId__std": "9Wsxx000000026fCAA",
      "StartDate__std": "2026-06-01",
      "NetUnitPrice__std": 30,
      "Quantity__std": 1,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "PriceAmend"
    }
  ]
}
```

This sample shows the request payload when billing schedule
                    group is used as a
                  reference.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter4\",\"BillingScheduleGroupId__std\":\"9Wsxx000000026fCAA\",\"StartDate__std\":\"2026-06-01\",\"NetUnitPrice__std\":30,\"Quantity__std\":1,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"PriceAmend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

              
              
                

**End date change (EndDateChange)**

                
: 

Change the end date of the subscription or of a specific billing schedule
                    under a billing schedule group from a specified start date. The API cancels the
                    existing billing schedule(s) from that start date and creates a new positive
                    amendment billing schedule from the start date to the new end
                    date.

Specify `StartDate__std` to
                    specify when the change is effective and `EndDate__std` for the new end of the
                    term.

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter3",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2026-05-01",
      "EndDate__std": "2026-09-01",
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "EndDateChange"
    }
  ]
}
```

This sample shows the request payload for the same end date
                    change on one billing schedule by using related transaction
                    ID.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter3\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2026-05-01\",\"EndDate__std\":\"2026-09-01\",\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"EndDateChange\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This sample shows the transaction data that references a billing
                    schedule group for end date change on one billing schedule
                    group.

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter3",
      "BillingScheduleGroupId__std": "9Wsxx000000026fCAA",
      "StartDate__std": "2026-05-01",
      "EndDate__std": "2026-09-01",
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "ChangeEndDate"
    }
  ]
}
```

This sample shows the request payload when billing schedule
                    group is used as a
                  reference.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter3\",\"BillingScheduleGroupId__std\":\"9Wsxx000000026fCAA\",\"StartDate__std\":\"2026-05-01\",\"EndDate__std\":\"2026-09-01\",\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"ChangeEndDate\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

              
              
                

**Delta price change (DeltaPriceAmend)**

                
: 

Change a subscription's price mid-term. For example, manage modifications
                    such as add or remove features, or apply special discounts and price
                    uplifts.

Send `Quantity__std` as
                      `0` with `TotalPrice__std` set to the delta amount, or send a non-zero quantity
                    with `NetUnitPrice__std` as the delta net
                    unit price. This sample shows the zero-quantity delta total price
                    pattern.

```
{
  "Transaction": [
    {
      "TransactionId__std": "amendmentSampleId1",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2025-07-01",
      "TotalPrice__std": 600,
      "Quantity__std": 0,
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "DeltaPriceAmend"
    }
  ]
}
```

This sample shows the request payload for the same delta price
                    change.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"amendmentSampleId1\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2025-07-01\",\"TotalPrice__std\":600,\"Quantity__std\":0,\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"DeltaPriceAmend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

              
              
                

**Billing frequency update at billing schedule group (BillingFrequencyChange)**

                
: 
                  

Change how often the subscription bills for all billing schedules in a billing
                    schedule group. Set `BillingSubActionType__std` to `BillingFrequencyChange`, identify the group with `BillingScheduleGroupId__std`, set `BillingTermUnit__std` to the new term unit (for
                    example, `Quarter`), and set `StartDate__std` when the new frequency is
                    effective. Include `TransactionId__std`.
                    Optionally, include `BillingStartMonth__std`
                    when the billing selling model requires it for that term unit.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "bfTer1",
      "BillingScheduleGroupId__std": "9Ws00000AXB00AAI",
      "StartDate__std": "2025-05-01",
      "BillingTermUnit__std": "Quarter",
      "BillingActionType__std": "Amend",
      "BillingSubActionType__std": "BillingFrequencyChange"
    }
  ]
}
```

                  

This sample shows the request payload for the same billing frequency
                    update.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"bfTer1\",\"BillingScheduleGroupId__std\":\"9Ws00000AXB00AAI\",\"StartDate__std\":\"2025-05-01\",\"BillingTermUnit__std\":\"Quarter\",\"BillingActionType__std\":\"Amend\",\"BillingSubActionType__std\":\"BillingFrequencyChange\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
            

          

        
        
          

**Detailed amendment payload**

          
: 
            

Send each amendment as its own transaction with `BillingActionType__std` set to `Amend`.
              Include identifiers, `RelatedTransactionId__std`,
              and the financial fields for each line. Use this payload type when you already
              computed quantities, unit prices, and total prices. This sample includes one positive
              amendment and two negative amendments for the same related transaction.

            

This sample includes the transaction data for an amendment.

            

```
{
  "Transaction": [
    {
      "id": "sampleA1",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sampleA1",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2025-04-01",
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 90,
      "BillingActionType__std": "Amend"
    },
    {
      "id": "sampleA2",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sampleA2",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2025-03-01",
      "UnitPrice__std": 10,
      "Quantity__std": -2,
      "TotalPrice__std": -200,
      "BillingActionType__std": "Amend"
    },
    {
      "id": "sampleA3",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sampleA3",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2025-03-01",
      "UnitPrice__std": 10,
      "Quantity__std": -1,
      "TotalPrice__std": -100,
      "BillingActionType__std": "Amend"
    }
  ]
}
```

            

This sample shows the request payload to create a billing schedule for an
              amendment.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"sampleA1\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sampleA1\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2025-04-01\",\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":90,\"BillingActionType__std\":\"Amend\"},{\"id\":\"sampleA2\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sampleA2\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2025-03-01\",\"UnitPrice__std\":10,\"Quantity__std\":-2,\"TotalPrice__std\":-200,\"BillingActionType__std\":\"Amend\"},{\"id\":\"sampleA3\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sampleA3\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2025-03-01\",\"UnitPrice__std\":10,\"Quantity__std\":-1,\"TotalPrice__std\":-100,\"BillingActionType__std\":\"Amend\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    
      

When you're creating a billing schedule for an amended transaction, make sure that you
        specify the mandatory values in the transactionDetails property value.

    

        
        
        
        
        
          
            

            

            

            

          

        

        
          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

- 
- 
- 
- 

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

        

      
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `TransactionId__std` | The unique identifier reference to apply to the billing schedule with amendment or updated billing frequency. The Reference and ReferenceItem field on a billing schedule has this value appended with a unique ID generated string. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `BillingStartMonth__std` | The month when billing begins for an annual subscription. This value can be any number from `1` through `12`. For example, if billing starts in January, the value is `1`. If billing starts in June, the value is `6`. | BillingStartMonth field on the BillingScheduleGroup object | Optional. Required if the billing term unit is Quarter, Semi-Annual, or Annual. |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Optional. Required in case of an end date change of a subscription. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Optional |
| `RelatedTransactionId__std` | The ID of the related transaction that must be referenced for an amendment. | This value isn't populated on any BillingSchedule or BillingScheduleGroup field. | Required |
| `BillingScheduleGroupId__std` | ID of the billing schedule group that must be referenced for an amendment. | Not applicable. | Specify either `RelatedTransactionId__std` or `BillingScheduleGroupId__std` in your request if you’re sending a simplified payload. |
| `BillingActionType__std` | The action that you want to perform for the transaction. Specify `Amend` as the BillingActionType for amended transactions. | Category field on the BillingSchedule object is populated as AmendQuantity. | Required |
| `BillingSubActionType__std` | The sub-action that you want to perform for the transaction. Specify `PriceAmend`, `QuantityAmend`, or `DeltaPriceAmend` as the BillingActionType to specify minimal details in the payload for a price, quantity, or delta price amendment respectively. Specify `EndDateChange` as the BillingActionType to change the end date of a subscription. Specify `BillingFrequencyChange` as the BillingActionType to update the billing frequency at the billing schedule group level. Available in API version 67.0 and later. | SubCategory field on the BillingSchedule object | Optional |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |
| `NetUnitPrice__std` | The net unit price of the transaction. | NetUnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |

=== ARTICLE: connect_requests_billing_schedule_input_for_bundled_products_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_bundled_products_new_sale.htm
title: New Sale Transaction With Bundled Products
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_bundled_products_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# New Sale Transaction With Bundled Products

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with bundled products.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with bundled products.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- For new sale transactions with bundled products, the `MainTransactionId__std` value is required for all the child transactions.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the `LegalEntityId__std` value for the transaction, the default
            TaxTreatmentId, BillingTreatmentId, and
            LegalEntityId of your Salesforce org is considered. If your org
          doesn't have any default values, an error occurs.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the `transactionDetails` property value. All the
          other transaction details are automatically fetched from the sObject record if those
          details are mapped in the context definition.

        
- To understand the requirements for the various selling model types, see these resources.
            
  - [One-Time New Sale
              Transaction](./connect_requests_billing_schedule_input_for_one_time_new_sale.htm.md)

            
  - [Term-Defined New Sale
                Transaction](./connect_requests_billing_schedule_input_for_termed_new_sale.htm.md)

            
  - [Evergreen New Sale
              Transaction](./connect_requests_billing_schedule_input_for_evergreen_new_sale.htm.md)

          

      

    

    
      
        
          

**JSON example**

          
: 
            

This sample is for a new sale transaction for bundled products with two levels of
              nesting and with these selling model types.

            
              
- The main root product's selling model type is `OneTime`.

              
- The second root product's selling model type is `OneTime`.

              
- The child products' selling model types are `TermDefined` and `Evergreen`.

            

            

```
{
  "Transaction": [
    {
      "id": "sample1",
      "SellingModelType__std": "OneTime",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sample1",
      "ProductName__std": "OneTimeProduct",
      "StartDate__std": "2025-02-20",
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 10,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillToContactId__std": "003LT0000038bALYAY",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD"
    },
    {
      "id": "sample2",
      "SellingModelType__std": "OneTime",
      "ParentTransactionId__std": "abc",
      "TransactionId__std": "sample2",
      "ProductName__std": "OneTimeProduct",
      "StartDate__std": "2025-02-20",
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 10,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillToContactId__std": "003LT0000038bALYAY",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "AssociatedTransactionPricing__std": "IncludedInBundlePrice",
      "MainTransactionRole__std": "Bundle",
      "AssociatedTransactionRole__std": "BundleComponent",
      "MainTransactionId__std": "sample1"
    },
    {
      "id": "sample3",
      "SellingModelType__std": "TermDefined",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sample3",
      "ProductName__std": "TermedQuarterlyProduct",
      "StartDate__std": "2025-01-01",
      "EndDate__std": "2025-12-31",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "BillingStartMonth__std": 2,
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 120,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillToContactId__std": "003LT0000038bALYAY",
      "BillingTermUnit__std": "Quarter",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "AssociatedTransactionPricing__std": "IncludedInBundlePrice",
      "MainTransactionRole__std": "Bundle",
      "AssociatedTransactionRole__std": "BundleComponent",
      "MainTransactionId__std": "sample2"
    },
    {
      "id": "sample4",
      "SellingModelType__std": "Evergreen",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "sample4",
      "ProductName__std": "EvergreenSemiAnnualProduct",
      "StartDate__std": "2025-01-01",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "BillingStartMonth__std": 3,
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 10,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillToContactId__std": "003LT0000038bALYAY",
      "BillingTermUnit__std": "Semi-Annual",
      "BillingActionType__std": "Add",
      "BillingPostalCode__std": "94105",
      "CurrencyIsoCode__std": "USD",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "AssociatedTransactionPricing__std": "IncludedInBundlePrice",
      "MainTransactionRole__std": "Bundle",
      "AssociatedTransactionRole__std": "BundleComponent",
      "MainTransactionId__std": "sample2"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction for bundled products.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"sample1\",\"SellingModelType__std\":\"OneTime\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sample1\",\"ProductName__std\":\"OneTimeProduct\",\"StartDate__std\":\"2025-02-20\",\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":10,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillToContactId__std\":\"003LT0000038bALYAY\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\"},{\"id\":\"sample2\",\"SellingModelType__std\":\"OneTime\",\"ParentTransactionId__std\":\"abc\",\"TransactionId__std\":\"sample2\",\"ProductName__std\":\"OneTimeProduct\",\"StartDate__std\":\"2025-02-20\",\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":10,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillToContactId__std\":\"003LT0000038bALYAY\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"AssociatedTransactionPricing__std\":\"IncludedInBundlePrice\",\"MainTransactionRole__std\":\"Bundle\",\"AssociatedTransactionRole__std\":\"BundleComponent\",\"MainTransactionId__std\":\"sample1\"},{\"id\":\"sample3\",\"SellingModelType__std\":\"TermDefined\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sample3\",\"ProductName__std\":\"TermedQuarterlyProduct\",\"StartDate__std\":\"2025-01-01\",\"EndDate__std\":\"2025-12-31\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"BillingStartMonth__std\":2,\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":120,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillToContactId__std\":\"003LT0000038bALYAY\",\"BillingTermUnit__std\":\"Quarter\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"AssociatedTransactionPricing__std\":\"IncludedInBundlePrice\",\"MainTransactionRole__std\":\"Bundle\",\"AssociatedTransactionRole__std\":\"BundleComponent\",\"MainTransactionId__std\":\"sample2\"},{\"id\":\"sample4\",\"SellingModelType__std\":\"Evergreen\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"sample4\",\"ProductName__std\":\"EvergreenSemiAnnualProduct\",\"StartDate__std\":\"2025-01-01\",\"PeriodBoundary__std\":\"DayOfPeriod__std\",\"BillingDayOfMonth__std\":1,\"BillingStartMonth__std\":3,\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":10,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillToContactId__std\":\"003LT0000038bALYAY\",\"BillingTermUnit__std\":\"Semi-Annual\",\"BillingActionType__std\":\"Add\",\"BillingPostalCode__std\":\"94105\",\"CurrencyIsoCode__std\":\"USD\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"AssociatedTransactionPricing__std\":\"IncludedInBundlePrice\",\"MainTransactionRole__std\":\"Bundle\",\"AssociatedTransactionRole__std\":\"BundleComponent\",\"MainTransactionId__std\":\"sample2\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you're creating a billing schedule for a new sale transaction with bundled products,
        make sure that you specify the mandatory values in the `transactionDetails` property value.

    

        
        
        
        
        
          
            

            

            

            

          

        

        

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            
- 
- 
- 
- 

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            
- 
- 
- 
- 

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            
- 
- 
- 

            

            

          

          
            

            
- 
- 
- 

            

            

          

          
            

            
- 
- 

            

            

          

          

      
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `BillToContactId__std` | The ID of the Contact record that's related to the transaction. | BillToContactId field on the BillingScheduleGroup object | Required |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `BillingPostalCode__std` | The postal code in the billing address of the transaction. | BillingPostalCode field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `OneTime` as the SellingModelType for the transaction that's related to a product that's sold once. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductName__std` | The name of the product that's related to the transaction that you want to create a billing schedule for. | ProductName field on the BillingScheduleGroup object | Either the ProductName or the ProductId value is required |
| `PeriodBoundary__std` | The period boundary determines the start and end date of the billing period. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` | PeriodBoundary field on the BillingScheduleGroup object | Required for child products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingDayOfMonth__std` | The day of the month on which a recurring billing process is scheduled to occur for the transaction. | BillDayOfMonth field on the BillingScheduleGroup object | Required for child products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingStartMonth__std` | The month when billing begins for an annual subscription. This value can be any number from `1` through `12`. For example, if billing starts in January, the value is `1`. If billing starts in June, the value is `6`. | BillingStartMonth field on the BillingScheduleGroup object | Required for child products with the `Evergreen` selling model type. |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required for child products with the `TermDefined` selling model type. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `TaxTreatmentId__std` | The ID of the tax treatment that's used to calculate tax for the transaction. If you don't specify a TaxTreatmentId, the org-default TaxTreatmentId is considered. | TaxTreatmentId field on the BillingScheduleGroup object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Required for child products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingTreatmentId__std` | The ID of the billing treatment that's used to create the billing schedule for the transaction. If you don't specify a BillingTreatmentId, the org-default BillingTreatmentId is considered. | BillingTreatmentId field on the BillingScheduleGroup object | Required |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for [Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US). |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |
| `MainTransactionId__std` | When your transaction is part of a bundle, this value is the ID of the main transaction record for all the child transactions. | MainBsgId field on the BsgRelationship object | Required for all the child products. |
| `MainTransactionRole__std` | When your transaction is part of a bundle, this value is the role of the primary transaction in the bundle relationship. Valid values are: `AddOn` `Bundle` `Set` | MainBsgRole field on the BsgRelationship object | Required for all the child products. |
| `AssociatedTransactionRole__std` | When your transaction is part of a bundle, this value is the role of the child transaction in the bundle relationship. Valid values are: `BundleComponent` `ClassificationComponent` | AssociatedBsgRole field on the BsgRelationship object | Required for all the child products. |
| `AssociatedTransactionPricing__std` | When your transaction is part of a bundle, this value describes how the child transaction is priced in relation to the primary transaction. Valid values are: `IncludedInBundlePrice` `NotIncludedInBundlePrice` | AssociatedBsgPricing field on the BsgRelationship object | Required for all the child products. |

  

#### See Also

- [BillingSchedule](./sforce_api_objects_billingschedule.htm.md)

- [BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)

- [BsgRelationship](./sforce_api_objects_bsgrelationship.htm.md)

=== ARTICLE: connect_requests_billing_schedule_input_for_cancellation.htm ===
---
page_id: connect_requests_billing_schedule_input_for_cancellation.htm
title: Canceled Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_cancellation.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Canceled Transaction

Cancel an entire billing schedule from a specified date. Specify only the cancellation
    date and billing schedule group identifier. The API computes the logic to split the cancellation
    across overlapping billing schedules and creates one cancel transaction per segment.

    

## Considerations

      
      

Keep these important considerations in mind when you provide the details for canceled
        transactions.

      
        
- The `BillingActionType__std` value for any amended
          transaction must be `Cancel`.

        
- If you provide a quantity, make sure that it matches the total quantity of the related
          transaction.

        
- If there are multiple canceled transactions associated with the same related
          transaction, specify the same start date for all of these transactions.

        
- Specify the canceled transaction details for all the billing schedules that are
          associated with the same billing schedule group.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the `transactionDetails` property value. All the
          other transaction details are automatically fetched from the sObject record if those
          details are mapped in the context definition.

      

    

    

## Cancellation Payload Types

      
      

The Create Standalone Billing Schedules API accepts two cancellation payload types in
          `transactionDetails` node. Use the type that matches
        the level of details you want to provide in the request.

      
        
          

**Simplified cancellation payload**

          
: 

Send a single transaction in the `Transaction` array. Set `BillingActionType__std` to `Cancel` and
                `BillingSubActionType__std` to `SimplifiedCancel`. Identify the source to cancel with
                `RelatedTransactionId__std` (one billing
              schedule) or `BillingScheduleGroupId__std` (a
              billing schedule group), and include `TransactionId__std` and `StartDate__std`
              for the effective cancellation date.

This sample shows the transaction data with
                `BillingScheduleGroupId__std` to cancel a billing
              schedule group.

```
{
  "Transaction": [
    {
      "TransactionId__std": "cTer5",
      "BillingScheduleGroupId__std": "9Wsxx000000009hCAA",
      "StartDate__std": "2026-08-01",
      "BillingActionType__std": "Cancel",
      "BillingSubActionType__std": "SimplifiedCancel"
    }
  ]
}
```

This sample shows a simplified cancellation
              request.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"cTer5\",\"BillingScheduleGroupId__std\":\"9Wsxx000000009hCAA\",\"StartDate__std\":\"2026-08-01\",\"BillingActionType__std\":\"Cancel\",\"BillingSubActionType__std\":\"SimplifiedCancel\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This sample shows the transaction data with `RelatedTransactionId__std` to cancel a billing
              schedule.

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter4",
      "RelatedTransactionId__std": "evg1",
      "StartDate__std": "2026-02-01",
      "BillingActionType__std": "Cancel",
      "BillingSubActionType__std": "SimplifiedCancel"
    }
  ]
}
```

This sample shows a simplified cancellation
            request.

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter4\",\"RelatedTransactionId__std\": \"evg1\",\"StartDate__std\":\"2026-02-01\",\"BillingActionType__std\": \"Cancel\",\"BillingSubActionType__std\":\"SimplifiedCancel\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

        
        
          

**Detailed cancellation payload**

          
: 
            

Send one cancel transaction for each positive billing schedule that you want to end.
              Each transaction uses `BillingActionType__std` set
              to `Cancel`. You specify `RelatedTransactionId__std` and the financial fields,
              such as quantity, unit price, and total price, for each line. Use this sample
              structure when you already computed the cancel lines and amounts yourself.

            

This sample shows a detailed cancellation for a single billing schedule. It uses a
              compact set of fields and does not use `SimplifiedCancel` sub-action type. For a detailed cancellation with
              multiple transactions, see the following sample.

            

This sample includes the transaction data for a cancellation.

            

```
{
  "Transaction": [
    {
      "id": "termedCancel1",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "termedCancel1",
      "RelatedTransactionId__std": "ot1",
      "StartDate__std": "2025-03-01",
      "UnitPrice__std": 10,
      "TotalPrice__std": -50,
      "BillingActionType__std": "Cancel"
    }
  ]
}
```

            

This sample shows the request payload to create a billing schedule for a
              cancellation.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"termedCancel1\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"termedCancel1\",\"RelatedTransactionId__std\":\"ot1\",\"StartDate__std\":\"2025-03-01\",\"UnitPrice__std\":10,\"TotalPrice__std\":-50,\"BillingActionType__std\":\"Cancel\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you're creating a billing schedule for a canceled transaction, make sure that you
        specify the mandatory values in the `transactionDetails`
        property value.

    

    

        
        
        
        
        
          
            

            

            

            

          

        

        
          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

          
            

            

            

            

          

        

      
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `TransactionId__std` | The unique identifier reference to apply to the canceled billing schedule. The Reference and ReferenceItem field on a billing schedule has this value appended with a unique ID generated string. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Optional if you’re sending a simplified payload. If you don’t specify this value, the API creates unique transaction IDs. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `RelatedTransactionId__std` | The ID of the related transaction that must be referenced to cancel one billing schedule. | This value isn't populated on any BillingSchedule or BillingScheduleGroup field. | Required |
| `BillingScheduleGroupId__std` | ID of the billing schedule group that must be referenced ‌to cancel the billing schedule group. | Not applicable. | Specify either `RelatedTransactionId__std` or `BillingScheduleGroupId__std` in your request if you’re sending a simplified payload. |
| `BillingActionType__std` | The action that you want to perform for the transaction. Specify `Cancel` as the BillingActionType for canceled transactions. | Category field on the BillingSchedule object is populated as Cancellation. | Required |
| `BillingSubActionType__std` | The sub-action that you want to perform for the transaction. Specify `SimplifiedCancel` as the BillingActionType to specify minimal details in the payload for canceled transactions. Available in API version 67.0 and later. | SubCategory field on the BillingSchedule object | Optional |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |
| `NetUnitPrice__std` | The net unit price of the transaction. | NetUnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |

=== ARTICLE: connect_requests_billing_schedule_input_for_early_renewal.htm ===
---
page_id: connect_requests_billing_schedule_input_for_early_renewal.htm
title: Early Renewal Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_early_renewal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Early Renewal Transaction

Early Renewal ends the current term at an effective date and starts a renewed term to a
    new end date, creating two billing schedules in one request. The request creates a negative
    segment for the remaining original term and a positive segment for the renewal term.

## Considerations

      
      

Keep these important considerations in mind when you specify the details for early renewal
        transactions.

      
        
- The `BillingActionType__std` value for early renewal
          transactions must be `Renew`.

        
- 
          

When you're creating billing schedules for early renewal transactions, your input
            payload must have details for two transactions.

          
            
  - A transaction to cancel the existing new-sale transaction. The details of this
              transaction must include a negative quantity to cancel billing for the remaining
              period. The quantity for this transaction must be the negative equivalent of the total
              quantity of all the existing billing schedules associated with the same billing
              schedule group.

            
  - Another transaction that specifies the early renewal details, which must have a
              positive quantity.

            
  - The `BillingActionType__std` value for both these
              transactions must be `Renew`.

          

        

        
- 
          

The start date of the early renewal transaction must be:

          
            
  - Before the end date of the related transaction.

            
  - Before the maximum end date of all the existing billing schedules associated with
              the billing schedule group of the related transaction.

            
  - The same as the start date of all the existing billing schedules associated with the
              same billing schedule group or after it.

          

        

        
- The end date for the early renewal transaction must be after the maximum end date of all
          the existing transactions associated with the billing schedule group of the related
          transaction.

        
- For early renewal transactions, the `TaxTreatmentId__std` value, the `BillingTreatmentId__std` value, and the `LegalEntityId__std` value of the related transaction are considered.

      

    

    

## Early Renewal Payload Types

      
      

The Create Standalone Billing Schedules API accepts two early renewal payload types in the
          `transactionDetails` node. Use the type that matches
        the level of detail you want to provide in the request.

      

Simplified early renewal payloads support these scenarios.

      
        
- Early renewal by related transaction by using `SimplifiedRenewal` sub-action type with an effective start date before the
          current term end and a new end date.

        
- Early renewal by billing schedule group by using `SimplifiedRenewal` sub-action type with the same date rules at the group
          level

        
- Early as-is renewal by using `AsIsRenewal` sub-action
          type when each underlying billing schedule should renew at its own quantity and net unit
          price from an effective date before the group end.

      

      

For renewal that begins after the prior term or billing schedule group ends, see [Renewal Transaction](./connect_requests_billing_schedule_input_for_renewal.htm.md).

      

Detailed early renewal payloads use separate cancel and renewal rows when you supply full
        transaction and financial fields yourself.

      
        
          

**Simplified early renewal payload**

          
: 
            

Set `BillingActionType__std` to `Renew`. Set `BillingSubActionType__std` to `SimplifiedRenewal` for a blended early renewal, or to `AsIsRenewal` for an early as-is renewal. Include `TransactionId__std`, `StartDate__std` (before the related transaction or group end), and `EndDate__std` for the new term. Identify the source with
              either `RelatedTransactionId__std` (one billing
              schedule) or `BillingScheduleGroupId__std` (a
              billing schedule group). The API can derive quantity and pricing when you omit those
              fields.

            
              
                

**Early renewal by related transaction (SimplifiedRenewal)**

                
: 
                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "earlyRen1",
      "RelatedTransactionId__std": "ter1",
      "StartDate__std": "2025-12-15",
      "EndDate__std": "2026-12-14",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "SimplifiedRenewal"
    }
  ]
}
```

                  

This sample shows the request payload for the same simplified early renewal by
                    using related transaction ID.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"earlyRen1\",\"RelatedTransactionId__std\":\"ter1\",\"StartDate__std\":\"2025-12-15\",\"EndDate__std\":\"2026-12-14\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"SimplifiedRenewal\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
              
                

**Early renewal by billing schedule group (SimplifiedRenewal)**

                
: 
                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "earlyRen2",
      "BillingScheduleGroupId__std": "9Wsxx00000001ovCAA",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "SimplifiedRenewal",
      "Quantity__std": 5,
      "UnitPrice__std": 10,
      "StartDate__std": "2025-12-15",
      "EndDate__std": "2026-12-14"
    }
  ]
}
```

                  

This sample shows the request payload for the same simplified early renewal by
                    using billing schedule group.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"earlyRen2\",\"BillingScheduleGroupId__std\":\"9Wsxx00000001ovCAA\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"SimplifiedRenewal\",\"Quantity__std\":5,\"UnitPrice__std\":10,\"StartDate__std\":\"2025-12-15\",\"EndDate__std\":\"2026-12-14\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
              
                

**Early as-is renewal (AsIsRenewal)**

                
: 
                  

Use this pattern when the billing schedule group has multiple billing schedules
                    with different quantities or net unit prices and the renewal effective date is
                    before the group end.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "asIsEarly1",
      "BillingScheduleGroupId__std": "9Wsxx00000001ovCAA",
      "StartDate__std": "2025-12-15",
      "EndDate__std": "2026-12-14",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "AsIsRenewal"
    }
  ]
}
```

                  

This sample shows the request payload for the same early as-is renewal.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"asIsEarly1\",\"BillingScheduleGroupId\":\"9Wsxx00000001ovCAA\",\"StartDate__std\":\"2025-12-15\",\"EndDate__std\":\"2026-12-14\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"AsIsRenewal\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
            

          

        
        
          

**Detailed early renewal payload**

          
: 
            

Send two transactions with `BillingActionType__std` set to `Renew`
              for each row. The first transaction ends billing for the remainder of the current term
              with a negative quantity. The second transaction starts the new term with a positive
              quantity. Include identifiers, related transaction, dates, unit price, and total price
              for each row.

            

This sample includes the transaction data for an early renewal.

            

```
{
  "Transaction": [
    {
      "id": "temp71",
      "TotalPrice__std": -10,
      "Quantity__std": -1,
      "UnitPrice__std": 10,
      "StartDate__std": "2026-12-31",
      "EndDate__std": "2027-12-31",
      "TransactionId__std": "temp71",
      "BillingActionType__std": "Renew",
      "RelatedTransactionId__std": "test21"
    },
    {
      "id": "temp72",
      "TotalPrice__std": 10,
      "Quantity__std": 1,
      "UnitPrice__std": 10,
      "StartDate__std": "2026-12-31",
      "EndDate__std": "2027-12-31",
      "TransactionId__std": "temp72",
      "BillingActionType__std": "Renew",
      "RelatedTransactionId__std": "test21"
    }
  ]
}
```

            

This sample shows the request payload to create a billing schedule for an early
              renewal.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"temp71\",\"TotalPrice__std\":-10,\"Quantity__std\":-1,\"UnitPrice__std\":10,\"StartDate__std\":\"2026-12-31\",\"EndDate__std\":\"2027-12-31\",\"TransactionId__std\":\"temp71\",\"BillingActionType__std\":\"Renew\",\"RelatedTransactionId__std\":\"test21\"},{\"id\":\"temp72\",\"TotalPrice__std\":10,\"Quantity__std\":1,\"UnitPrice__std\":10,\"StartDate__std\":\"2026-12-31\",\"EndDate__std\":\"2027-12-31\",\"TransactionId__std\":\"temp72\",\"BillingActionType__std\":\"Renew\",\"RelatedTransactionId__std\":\"test21\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you renew a new-sale transaction before its end date, those transactions are called
        early renewal transactions. For example, a new-sale transaction starts on 01/01/2025 and
        ends on 12/31/2025, and you renew it to start on 12/01/2025 and end on 12/31/2026.

      

When a billing schedule is created for an early renewal transaction, it results in these
        updates.

      
        
- The cancellation date on the original billing schedule is populated.

        
- A billing schedule with a negative quantity is created and can be used for a
          refund.

        
- A billing schedule with a positive quantity is created for the early renewal
          transaction.

      

      

When you're creating a billing schedule for an early renewal transaction, make sure that
        you provide the mandatory values in the `transactionDetails` property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `TransactionId__std` | The unique identifier reference to apply to the renewal billing schedule. The Reference and ReferenceItem field on a billing schedule has this value appended with a unique ID generated string. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required for a positive transaction. Optional for a negative transaction. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `RelatedTransactionId__std` | The ID of the transaction against which you're doing an early renewal. This transaction must have a positive quantity. | This value isn't populated on any BillingSchedule or BillingScheduleGroup field. | Required |
| `BillingScheduleGroupId__std` | ID of the billing schedule group that must be referenced ‌to renew each billing schedule in the billing schedule group early. | Not applicable. | Specify either `RelatedTransactionId__std` or `BillingScheduleGroupId__std` in your request if you’re sending a simplified payload. |
| `BillingScheduleGroupId__std` | ID of the billing schedule group that must be referenced ‌to renew each billing schedule in the billing schedule group early. | Not applicable. | Specify either `RelatedTransactionId__std` or `BillingScheduleGroupId__std` in your request if you’re sending a simplified payload. |
| `BillingActionType__std` | The action that you want to perform for the transaction. Specify `Renew` as the BillingActionType for early renewal transactions. | Category field on the BillingSchedule object is populated as Renewal. | Required |
| `BillingSubActionType__std` | The sub-action that you want to perform for the transaction. Specify `AsIsRenewal` as the BillingActionType to specify minimal details in the payload for an as-is renewal. Specify `SimplifiedRenewal` as the BillingActionType to specify minimal details in the payload for a renewal or an early renewal. Available in API version 67.0 and later. | SubCategory field on the BillingSchedule object | Optional |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |

=== ARTICLE: connect_requests_billing_schedule_input_for_evergreen_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_evergreen_new_sale.htm
title: Evergreen New Sale Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_evergreen_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Evergreen New Sale Transaction

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with the Evergreen selling model type.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with the Evergreen selling model type.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- When a new sale transaction is for the Evergreen selling model type, the
          SellingModelType value must be `Evergreen`.

        
- When a new sale transaction is for the Evergreen selling model type, the BillingTermUnit
          and PeriodBoundary values are required.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the `LegalEntityId__std` value for the transaction, the default
            `TaxTreatmentId`, `BillingTreatmentId`, and `LegalEntityId` of
          your Salesforce org is considered. If your org doesn't have any default values, an error
          occurs.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the transactionDetails property value. All the other transaction details are
          automatically fetched from the sObject record if those details are mapped in the context
          definition.

      

    

    
      
        
          

**JSON example**

          
: 
            

This example includes the transaction data for a new sale transaction with the
              Evergreen selling model type.

            

```
{
  "Transaction": [
    {
      "id": "evg1",
      "SellingModelType__std": "Evergreen",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "evg1",
      "ProductName__std": "EvergreenSemiAnnualProduct",
      "StartDate__std": "2025-01-01",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "BillingStartMonth__std": 3,
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 10,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingTermUnit__std": "Semi-Annual",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction with the Evergreen selling model type.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"evg1\",\"SellingModelType__std\":\"Evergreen\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"evg1\",\"ProductName__std\":\"EvergreenSemiAnnualProduct\",\"StartDate__std\":\"2025-01-01\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"BillingStartMonth__std\":3,\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":10,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingTermUnit__std\":\"Semi-Annual\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    

When you're creating a billing schedule for a new sale transaction with the
        Evergreen selling model type, make sure that you specify the mandatory values in the `transactionDetails` property value.

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingProfileId__std` | The ID of the billing profile (Billing Account record) that's related to the transaction. See [Billing Profile](https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&language=en_US) requirements. | BillingAccountId field on the BillingSchedule object | Optional |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `Evergreen` as the SellingModelType for the transaction that's related to a product that's sold for an indefinite term. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductName__std` | The name of the product that's related to the transaction that you want to create a billing schedule for. | ProductName field on the BillingScheduleGroup object | Either the ProductName or the ProductId is required |
| `PeriodBoundary__std` | The period boundary determines the start and end date of the billing period. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` | PeriodBoundary field on the BillingScheduleGroup object | Required |
| `BillingDayOfMonth__std` | The day of the month on which a recurring billing process is scheduled to occur for the transaction. | BillDayOfMonth field on the BillingScheduleGroup object | Required |
| `BillingStartMonth__std` | The month when billing begins for an annual subscription. This value can be any number from `1` through `12`. For example, if billing starts in January, the value is `1`. If billing starts in June, the value is `6`. | BillingStartMonth field on the BillingScheduleGroup object | Required |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `TaxTreatmentId__std` | The ID of the tax treatment that's used to calculate tax for the transaction. If you don't specify a TaxTreatmentId, the org-default TaxTreatmentId is considered. | TaxTreatmentId field on the BillingScheduleGroup object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Required |
| `BillingTreatmentId__std` | The ID of the billing treatment that's used to create the billing schedule for the transaction. If you don't specify a BillingTreatmentId, the org-default BillingTreatmentId is considered. | BillingTreatmentId field on the BillingScheduleGroup object | Required |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for[Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US) |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total cost to the customer for the transaction for each billing period, such as month, quarter, or year, based on the billing frequency. | TotalAmount field on the BillingSchedule object | Required |

  

#### See Also

- [BillingSchedule](./sforce_api_objects_billingschedule.htm.md)

- [BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)

- [BsgRelationship](./sforce_api_objects_bsgrelationship.htm.md)

=== ARTICLE: connect_requests_billing_schedule_input_for_one_time_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_one_time_new_sale.htm
title: One-Time New Sale Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_one_time_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# One-Time New Sale Transaction

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with the OneTime selling model type.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with the OneTime selling model type.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- When a new sale transaction is for the OneTime selling model type, the SellingModelType
          value must be `OneTime`.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the `LegalEntityId__std` value, the default `TaxTreatmentId` for the transaction, `BillingTreatmentId`, and `LegalEntityId` of your Salesforce org is considered. If your org doesn't have
          any default values, an error occurs.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the `transactionDetails` property value. All the
          other transaction details are automatically fetched from the sObject record if those
          details are mapped in the context definition.

      

    

    
      
        
          

**JSON example**

          
: 
            

This example includes the transaction data for a new sale transaction with the
              OneTime selling model type.

            

```
{
  "Transaction": [
    {
      "id": "ot1",
      "SellingModelType__std": "OneTime",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "ot1",
      "ProductName__std": "OneTimeProduct",
      "StartDate__std": "2025-02-20",
      "UnitPrice__std": 10,
      "Quantity__std": 5,
      "TotalPrice__std": 50,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction with the OneTime selling model type.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"ot1\",\"SellingModelType__std\":\"OneTime\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"ot1\",\"ProductName__std\":\"OneTimeProduct\",\"StartDate__std\":\"2025-02-20\",\"UnitPrice__std\":10,\"Quantity__std\":5,\"TotalPrice__std\":50,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you're creating a billing schedule for a new sale transaction with the OneTime selling
        model type, make sure that you specify the required values in the `transactionDetails` property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingProfileId__std` | The ID of the billing profile that’s related to the transaction, which is used to resolve billing configurations if not specified at transaction level. See [Billing Profile](https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&language=en_US) requirements. | Not applicable. | Optional |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `OneTime` as the SellingModelType for the transaction that's related to a product that's sold once. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductName__std` | The name of the product that's related to the transaction that you want to create a billing schedule for. | ProductName field on the BillingScheduleGroup object | Either the ProductName or the ProductId is required |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `TaxTreatmentId__std` | The ID of the tax treatment that's used to calculate tax for the transaction. If you don't specify a TaxTreatmentId, the org-default TaxTreatmentId is considered. | TaxTreatmentId field on the BillingScheduleGroup object | Required |
| `BillingTreatmentId__std` | The ID of the billing treatment that's used to create the billing schedule for the transaction. If you don't specify a BillingTreatmentId, the org-default BillingTreatmentId is considered. | BillingTreatmentId field on the BillingScheduleGroup object | Required |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for[Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US) |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |

    

  

#### See Also

- [BillingSchedule](./sforce_api_objects_billingschedule.htm.md)

- [BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)

- [BsgRelationship](./sforce_api_objects_bsgrelationship.htm.md)

=== ARTICLE: connect_requests_billing_schedule_input_for_ramps_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_ramps_new_sale.htm
title: New Sale Transaction With Ramped Products
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_ramps_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# New Sale Transaction With Ramped Products

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with ramped products.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with ramped products.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- For new sale transactions with a ramped product, the `RampIdentifier__std` value is required.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the` LegalEntityId__std` value for the transaction, the default
            `TaxTreatmentId`, `BillingTreatmentId`, and `LegalEntityId` of
          your Salesforce org is considered. If your org doesn't have any default values, an error
          occurs.

        
- The billing schedules for transactions with the same `RampIdentifier__std` value are created for the same billing schedule
          group.

        
- To understand the requirements for the various selling model types, see these resources.
            
  - [One-Time New Sale
              Transaction](./connect_requests_billing_schedule_input_for_one_time_new_sale.htm.md)

            
  - [Term-Defined New Sale
                Transaction](./connect_requests_billing_schedule_input_for_termed_new_sale.htm.md)

            
  - [Evergreen New Sale
              Transaction](./connect_requests_billing_schedule_input_for_evergreen_new_sale.htm.md)

          

      

    

    
      
        
          

**JSON example**

          
: 
            

This example includes the transaction data for a new sale transaction with ramped
              products and a `TermDefined` selling model.

            

```
{
  "Transaction": [
    {
      "id": "ter1",
      "SellingModelType__std": "TermDefined",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "ter1",
      "ProductName__std": "TermedQuarterlyProduct",
      "StartDate__std": "2025-01-01",
      "EndDate__std": "2026-12-31",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "UnitPrice__std": 10,
      "Quantity__std": 5,
      "TotalPrice__std": 120,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingTermUnit__std": "Month",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD",
      "RampIdentifier__std": "ramp1"
    },
    {
      "id": "ter2",
      "SellingModelType__std": "TermDefined",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "ter2",
      "ProductName__std": "TermedQuarterlyProduct",
      "StartDate__std": "2025-01-01",
      "EndDate__std": "2026-12-31",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "UnitPrice__std": 10,
      "Quantity__std": 5,
      "TotalPrice__std": 120,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingTermUnit__std": "Month",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD",
      "RampIdentifier__std": "ramp1"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction with ramped products and a `TermDefined` selling model.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"ter1\",\"SellingModelType__std\":\"TermDefined\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"ter1\",\"ProductName__std\":\"TermedQuarterlyProduct\",\"StartDate__std\":\"2025-01-01\",\"EndDate__std\":\"2026-12-31\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"UnitPrice__std\":10,\"Quantity__std\":5,\"TotalPrice__std\":120,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingTermUnit__std\":\"Month\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\",\"RampIdentifier__std\":\"ramp1\"},{\"id\":\"ter2\",\"SellingModelType__std\":\"TermDefined\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"ter2\",\"ProductName__std\":\"TermedQuarterlyProduct\",\"StartDate__std\":\"2025-01-01\",\"EndDate__std\":\"2026-12-31\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"UnitPrice__std\":10,\"Quantity__std\":5,\"TotalPrice__std\":120,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingTermUnit__std\":\"Month\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\",\"RampIdentifier__std\":\"ramp1\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you're creating a billing schedule for a new sale transaction with ramped products,
        make sure that you specify the mandatory values in the `transactionDetails` property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              
- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              
- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Name | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingProfileId__std` | The ID of the billing profile (Billing Account record) that's related to the transaction. See [Billing Profile](https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&language=en_US) requirements. | BillingAccountId field on the BillingSchedule object | Optional |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `OneTime` as the SellingModelType for the transaction that's related to a product that's sold once. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductName__std` | The name of the product that's related to the transaction that you want to create a billing schedule for. | ProductName field on the BillingScheduleGroup object | Either the ProductName or the ProductId is required |
| `PeriodBoundary__std` | The period boundary determines the start and end date of the billing period. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` | PeriodBoundary field on the BillingScheduleGroup object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingDayOfMonth__std` | The day of the month on which a recurring billing process is scheduled to occur for the transaction. | BillDayOfMonth field on the BillingScheduleGroup object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required for products with the `TermDefined` selling model type. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `TaxTreatmentId__std` | The ID of the tax treatment that's used to calculate tax for the transaction. If you don't specify a TaxTreatmentId, the org-default TaxTreatmentId is considered. | TaxTreatmentId field on the BillingScheduleGroup object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingTreatmentId__std` | The ID of the billing treatment that's used to create the billing schedule for the transaction. If you don't specify a BillingTreatmentId, the org-default BillingTreatmentId is considered. | BillingTreatmentId field on the BillingScheduleGroup object | Required |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for [Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US). |
| `RampIdentifier__std` | When the transaction is part of a ramp deal, the RampIdentifier value is a unique identifier for that ramp. All the transactions with the same RampIdentifier value are grouped to have billing schedules for the same billing schedule group. | This value isn't populated on any BillingSchedule or BillingScheduleGroup field. | Required |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |

=== ARTICLE: connect_requests_billing_schedule_input_for_renewal.htm ===
---
page_id: connect_requests_billing_schedule_input_for_renewal.htm
title: Renewal Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_renewal.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Renewal Transaction

Create a renewal billing schedule for termed subscriptions that continues without a
    gap, starting the day after the current billing schedule group ends and running for the same
    term length.

## Considerations

      
      

Keep these important considerations in mind when you specify the details for renewal
        transactions.

      
        
- The `BillingActionType__std` value for renewal
          transactions must be `Renew`.

        
- The quantity for renewal transactions must be a nonzero positive number.

        
- The start date of the renewal transaction must be before the maximum end date of all the
          existing billing schedules associated with the billing schedule group.

        
- The end date of the renewal transaction must be after the maximum end date of all the
          existing transactions associated with the billing schedule group of the related
          transaction.

        
- Specify a `RelatedTransactionId__std` value with a
          positive quantity.

        
- For a particular RelatedTransactionId, you can create a billing schedule only for a
          single renewal transaction.

        
- For renewal transactions, the `TaxTreatmentId__std`
          value, the `BillingTreatmentId__std` value, and the
            `LegalEntityId__std` value of the related transaction
          are considered.

      

    

    

## Renewal Payload Types

      
      

The Create Standalone Billing Schedules API accepts two renewal payload types in the
          `transactionDetails` node. Use the type that matches
        the level of detail you want to provide in the request.

      

Simplified renewal payloads support these scenarios.

      
        
- Renewal to start a new term after the related transaction or billing schedule group
          reaches its end

        
- As-is renewal to renew each existing billing schedule at its own quantity and net unit
          price

      

      

Detailed renewal payloads cover the same outcomes when you specify all transaction details
        and financial fields.

      
        
          

**Simplified renewal payload**

          
: 
            

Set `BillingActionType__std` to `Renew`. Set `BillingSubActionType__std` to `SimplifiedRenewal` for a standard renewal, or to `AsIsRenewal` for an as-is renewal. Include `TransactionId__std`. Identify the source with either
                `RelatedTransactionId__std` (one billing
              schedule) or `BillingScheduleGroupId__std` (a
              billing schedule group). For a standard renewal, you can omit dates and pricing. The
              API can derive start date, end date, quantity, and price from the related transaction
              record or billing schedule group. You can add optional dates or pricing when you want
              to override derived values. The examples in this topic use `RelatedTransactionId__std`. For renewals with billing schedule group as
              source, use `BillingScheduleGroupId__std`
              instead.

            
              
                

**Renewal (SimplifiedRenewal)**

                
: 
                  

Use this payload structure when the new term begins after the prior term ends.
                    This sample shows the minimum fields. Keep these considerations in mind when you
                    specify a simplified payload.

                  
                    
- If you specify a billing schedule group ID, start date is required. If you
                      omit the start date and specify a related transaction ID, the API sets the
                      start date to a day after the end date of the related billing schedule.

                    
- If you specify a billing schedule group ID, end date is required. If you
                      omit the end date and specify a related transaction ID, the API sets the end
                      date by adding one full billing schedule term to that billing schedule’s end
                      date (plus one day).

                    
- If you specify a billing schedule group ID, unit price and net unit price
                      are required. If you omit the unit price and net unit price, and specify a
                      related transaction ID, the API sets the unit price and net unit price values
                      from the related billing schedule.

                    
- If you specify a billing schedule group ID, quantity is required. If you
                      omit the quantity and specify a related transaction ID, the API sets the
                      renewal quantity from the related billing schedule.

                  

                  

This sample shows the transaction data for the simplified renewal with related
                    transaction ID as a reference.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "ren1",
      "RelatedTransactionId__std": "ter1",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "SimplifiedRenewal"
    }
  ]
}
```

                  

This sample shows the request payload for the simplified renewal with related
                    transaction ID as a reference.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ren1\",\"RelatedTransactionId__std\":\"ter1\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"SimplifiedRenewal\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                  

This sample shows the transaction data for the simplified renewal with billing
                    schedule group ID as a reference.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "ter3",
      "BillingScheduleGroupId__std": "9Ws00000AXB00AAI",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "SimplifiedRenewal",
      "Quantity__std": 5,
      "UnitPrice__std": 10,
      "StartDate__std": "2025-12-15",
      "EndDate__std": "2026-12-14"
    }
  ]
}
```

                  

This sample shows the request payload for the simplified renewal with billing
                    schedule group ID as a reference.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"ter3\",\"BillingScheduleGroupId__std\":\"9Ws00000AXB00AAI\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"SimplifiedRenewal\",\"Quantity__std\":5,\"UnitPrice__std\":10,\"StartDate__std\":\"2025-12-15\",\"EndDate__std\":\"2026-12-14\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
              
                

**As-is renewal (AsIsRenewal)**

                
: 
                  

Use this payload structure when multiple billing schedules under the reference
                    have different quantities or net unit prices and you want one renewal billing
                    schedule per source schedule.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "asIsRen1",
      "RelatedTransactionId__std": "ter1",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "AsIsRenewal"
    }
  ]
}
```

                  

This sample shows the request payload for the same as-is renewal.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"asIsRen1\",\"RelatedTransactionId__std\":\"ter1\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"AsIsRenewal\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                  

This sample shows the request payload for the as-is renewal with billing
                    schedule group ID as a reference.

                  

```
{
  "Transaction": [
    {
      "TransactionId__std": "asIsRenew2",
      "BillingScheduleGroupId__std": "9Ws00000AXB00AAI",
      "BillingActionType__std": "Renew",
      "BillingSubActionType__std": "AsIsRenewal"
    }
  ]
}
```

                  

This sample shows the request payload for the as-is renewal with billing
                    schedule group ID as a reference.

                  

```
{
  "transactionDetails": "{\"Transaction\":[{\"TransactionId__std\":\"asIsRenew2\",\"BillingScheduleGroupId__std\":\"9Ws00000AXB00AAI\",\"BillingActionType__std\":\"Renew\",\"BillingSubActionType__std\":\"AsIsRenewal\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

                

              
            

          

        
        
          

**Detailed renewal payload**

          
: 
            

Send each renewal row with `BillingActionType__std` set to `Renew`
              and include identifiers, related transaction, dates, quantity, unit price, and total
              price. Use this payload type when you already computed the renewal lines yourself.

            

This sample includes the transaction data for a standard renewal after the end
              date.

            

```
{
  "Transaction": [
    {
      "id": "temp1001",
      "TotalPrice__std": 10,
      "Quantity__std": 1,
      "UnitPrice__std": 10,
      "StartDate__std": "2026-03-01",
      "EndDate__std": "2027-12-31",
      "TransactionId__std": "temp1001",
      "BillingActionType__std": "Renew",
      "RelatedTransactionId__std": "temp1"
    }
  ]
}
```

            

This sample shows the request payload to create a billing schedule for a renewal.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"temp1001\",\"TotalPrice__std\":10,\"Quantity__std\":1,\"UnitPrice__std\":10,\"StartDate__std\":\"2026-03-01\",\"EndDate__std\":\"2027-12-31\",\"TransactionId__std\":\"temp1001\",\"BillingActionType__std\":\"Renew\",\"RelatedTransactionId__std\":\"temp1\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you renew a new-sale transaction after its end date, those transactions are called
        renewal transactions. For example, a new-sale transaction starts on 01/01/2025 and ends on
        12/31/2025, and you renew it to start on 03/01/2026 and end on 12/31/2026. 

      

When you're creating a billing schedule for a renewal transaction, make sure that you
        provide the mandatory values in the `transactionDetails`
        property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `TransactionId__std` | The unique identifier reference to apply to the renewal billing schedule. The Reference and ReferenceItem field on a billing schedule has this value appended with a unique ID generated string. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `RelatedTransactionId__std` | The ID of the original transaction that's related to the renewal transaction. | This value isn't populated on any BillingSchedule or BillingScheduleGroup field. | Required |
| `BillingScheduleGroupId__std` | ID of the billing schedule group that must be referenced ‌to renew the billing schedule group. | Not applicable. | Specify either `RelatedTransactionId__std` or `BillingScheduleGroupId__std` in your request if you’re sending a simplified payload. |
| `BillingActionType__std` | The action that you want to perform for the transaction. Specify `Renew` as the BillingActionType for renewal transactions. | Category field on the BillingSchedule object is populated as Renewal. | Required |
| `BillingSubActionType__std` | The sub-action that you want to perform for the transaction. Specify `AsIsRenewal` as the BillingActionType to specify minimal details in the payload for an as-is renewal. Specify `SimplifiedRenewal` as the BillingActionType to specify minimal details in the payload for a renewal or an early renewal. Available in API version 67.0 and later. | SubCategory field on the BillingSchedule object | Optional |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |

=== ARTICLE: connect_requests_billing_schedule_input_for_termed_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_termed_new_sale.htm
title: Term-Defined New Sale Transaction
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_termed_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Term-Defined New Sale Transaction

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with the TermDefined selling model type.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with the TermDefined selling model type.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- When a new sale transaction is for the TermDefined selling model type, the
          SellingModelType value must be `TermDefined`.

        
- When a new sale transaction is for the TermDefined selling model type, the `BillingTermUnit__std` and `PeriodBoundary__std` values are required.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the `LegalEntityId__std` value for the transaction, the default
            `TaxTreatmentId`, `BillingTreatmentId`, and `LegalEntityId` of
          your Salesforce org is considered. If your org doesn't have any default values, an error
          occurs.

        
- If your transaction is for an sObject record, only specify the record ID as the id value
          in the transactionDetails property value. All the other transaction details are
          automatically fetched from the sObject record if those details are mapped in the context
          definition.

      

    

    
      
        
          

**JSON example**

          
: 
            

This example includes the transaction data for a new sale transaction with the
              TermDefined selling model type.

            

```
{
  "Transaction": [
    {
      "id": "ter1",
      "SellingModelType__std": "TermDefined",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "ter1",
      "ProductName__std": "TermedQuarterlyProduct",
      "StartDate__std": "2025-01-01",
      "EndDate__std": "2025-12-31",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "UnitPrice__std": 10,
      "Quantity__std": 5,
      "TotalPrice__std": 120,
      "TaxTreatmentId__std": "1ttLT000000EV7DYAW",
      "BillingTreatmentId__std": "1BTLT00000008yT4AQ",
      "AccountId__std": "001LT00000dPVrlYAG",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingCity__std": "HYD",
      "ShippingCity__std": "VSKP",
      "BillingTermUnit__std": "Month",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction with the TermDefined selling model type.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"ter1\",\"SellingModelType__std\":\"TermDefined\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"ter1\",\"ProductName__std\":\"TermedQuarterlyProduct\",\"StartDate__std\":\"2025-01-01\",\"EndDate__std\":\"2025-12-31\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":120,\"TaxTreatmentId__std\":\"1ttLT000000EV7DYAW\",\"BillingTreatmentId__std\":\"1BTLT00000008yT4AQ\",\"AccountId__std\":\"001LT00000dPVrlYAG\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingCity__std\":\"HYD\",\"ShippingCity__std\":\"VSKP\",\"BillingTermUnit__std\":\"Month\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

When you're creating a billing schedule for a new sale transaction with the TermDefined
        selling model type, make sure that you specify the mandatory values in the `transactionDetails` property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Required |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingProfileId__std` | The ID of the billing profile (Billing Account record) that's related to the transaction. See [Billing Profile](https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&language=en_US) requirements. | BillingAccountId field on the BillingSchedule object | Optional |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `TermDefined` as the SellingModelType for the transaction that's related to a product that's sold for a specific term. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductName__std` | The name of the product that's related to the transaction that you want to create a billing schedule for. | ProductName field on the BillingScheduleGroup object | Either the ProductName or the ProductId is required |
| `PeriodBoundary__std` | The period boundary determines the start and end date of the billing period. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` | PeriodBoundary field on the BillingScheduleGroup object | Required |
| `BillingDayOfMonth__std` | The day of the month on which a recurring billing process is scheduled to occur for the transaction. | BillDayOfMonth field on the BillingScheduleGroup object | Required |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `TaxTreatmentId__std` | The ID of the tax treatment that's used to calculate tax for the transaction. If you don't specify a TaxTreatmentId, the org-default TaxTreatmentId is considered. | TaxTreatmentId field on the BillingScheduleGroup object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Required |
| `BillingTreatmentId__std` | The ID of the billing treatment that's used to create the billing schedule for the transaction. If you don't specify a BillingTreatmentId, the org-default BillingTreatmentId is considered. | BillingTreatmentId field on the BillingScheduleGroup object | Required |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for[Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US) |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total cost to the customer for the transaction, from the start date to the end date. | TotalAmount field on the BillingSchedule object | Required |

    

  

#### See Also

- [BillingSchedule](./sforce_api_objects_billingschedule.htm.md)

- [BillingScheduleGroup](./sforce_api_objects_billingschedulegroup.htm.md)

- [BsgRelationship](./sforce_api_objects_bsgrelationship.htm.md)

=== ARTICLE: connect_requests_billing_schedule_input_for_usage_new_sale.htm ===
---
page_id: connect_requests_billing_schedule_input_for_usage_new_sale.htm
title: New Sale Transaction With Usage Products
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_input_for_usage_new_sale.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: connect_requests_context_aware_standalone_billing_schedule_input.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# New Sale Transaction With Usage Products

Understand the required values and key considerations before you create a billing
    schedule for a new sale transaction with usage-based products.

## Considerations

      
      

Keep these important considerations in mind when you provide the details for new sale
        transactions with a usage-based product.

      
        
- The `BillingActionType__std` value for any new sale
          transaction must be `Add`.

        
- For new sale transactions with a usage-based product, the `ProductUsageModelType__std` and `BindingInstance__std` values are required.

        
- If you don't provide the `TaxTreatmentId__std` value,
          the `BillingTreatmentId__std` value, or the `LegalEntityId__std` value for the transaction, the default
            `TaxTreatmentId`, `BillingTreatmentId`, and `LegalEntityId` of
          your Salesforce org is considered. If your org doesn't have any default values, an error
          occurs.

        
- To understand the requirements for the various selling model types, see these resources.
            
  - [One-Time New Sale
              Transaction](./connect_requests_billing_schedule_input_for_one_time_new_sale.htm.md)

            
  - [Term-Defined New Sale
                Transaction](./connect_requests_billing_schedule_input_for_termed_new_sale.htm.md)

            
  - [Evergreen New Sale
              Transaction](./connect_requests_billing_schedule_input_for_evergreen_new_sale.htm.md)

          

      

    

    
      
        
          

**JSON example**

          
: 
            

This sample is for a new sale transaction for a usage-based product with a `TermDefined` selling model.

            

```
{
  "Transaction": [
    {
      "id": "termDefined",
      "SellingModelType__std": "TermDefined",
      "ParentTransactionId__std": "sample",
      "TransactionId__std": "onetimeUsage2",
      "StartDate__std": "2025-01-01",
      "EndDate__std": "2025-12-31",
      "PeriodBoundary__std": "DayOfPeriod",
      "BillingDayOfMonth__std": 1,
      "BillingTermUnit__std": "Month",
      "UnitPrice__std": 10,
      "Quantity__std": 1,
      "TotalPrice__std": 120,
      "AccountId__std": "001xx000003GgEJAA0",
      "BillingProfileId__std": "001LT00000dPVrlYAG",
      "BillingActionType__std": "Add",
      "CurrencyIsoCode__std": "USD",
      "BillingCity__std": "Hyderabad",
      "ShippingCity__std": "SFO",
      "ProductUsageModelType__std": "Anchor",
      "BindingInstance__std": "001xx000003GgChAAK",
      "ProductId__std": "01txx0000006i3DAAQ"
    }
  ]
}
```

            

This example shows the request payload to create a billing schedule for a new sale
              transaction for usage-based products with a `TermDefined` selling model.

            

```
{
  "transactionDetails": "{\"Transaction\":[{\"id\":\"termDefined\",\"SellingModelType__std\":\"TermDefined\",\"ParentTransactionId__std\":\"sample\",\"TransactionId__std\":\"onetimeUsage2\",\"StartDate__std\":\"2025-01-01\",\"EndDate__std\":\"2025-12-31\",\"PeriodBoundary__std\":\"DayOfPeriod\",\"BillingDayOfMonth__std\":1,\"BillingTermUnit__std\":\"Month\",\"UnitPrice__std\":10,\"Quantity__std\":1,\"TotalPrice__std\":120,\"AccountId__std\":\"001xx000003GgEJAA0\",\"BillingProfileId__std\":\"001LT00000dPVrlYAG\",\"BillingActionType__std\":\"Add\",\"CurrencyIsoCode__std\":\"USD\",\"BillingCity__std\":\"Hyderabad\",\"ShippingCity__std\":\"SFO\",\"ProductUsageModelType__std\":\"Anchor\",\"BindingInstance__std\":\"001xx000003GgChAAK\",\"ProductId__std\":\"01txx0000006i3DAAQ\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext__stdctx",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "TransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

          

        
      

    

    
      

Before using the Create Standalone Billing Schedules API for usage-based products, [Create a Usage Product Grant Binding
          Policy record](https://help.salesforce.com/s/articleView?id=ind.um_create_a_usage_product_grant_binding_policy.htm&language=en_US) with the grant binding type as `Target`.

      

When you're creating a billing schedule for a new sale transaction with a usage-based
        product, make sure that you specify the mandatory values in the `transactionDetails` property value.

      

          
          
          
          
          
            
              

              

              

              

            

          

          
            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              
- 
- 
- 
- 

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

              

              

            

            
              

              

- 
- 

              

              

            

            
              

              

              

              

            

          

        
| Context Tag in the Transaction Node of the StandaloneBillingContext Context Definition | Description | Mapped Field | Required or Optional |
| --- | --- | --- | --- |
| `ParentTransactionId__std` | The ID of the parent transaction record. For example, if the transaction is at a level similar to that of an Order Item record, the parent transaction will be at a level similar to that of an Order record. | If the transaction is a child Order or Quote record, the ReferenceEntityId field on the BillingScheduleobject is populated. For other sObject records or external records, the Reference field on the BillingSchedule object is populated. | Optional |
| `AccountId__std` | The ID of the Account record that's related to the transaction. | BillingAccountId field on the BillingScheduleGroup object | Required |
| `BillingProfileId__std` | The ID of the billing profile (Billing Account record) that's related to the transaction. See [Billing Profile](https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&language=en_US) requirements. | BillingAccountId field on the BillingSchedule object | Optional |
| `BillingCity__std` | The city in the billing address of the transaction. | BillingCity field on the BillingScheduleGroup object | Any one of the billing address fields is required. |
| `ShippingCity__std` | The city in the shipping address of the transaction. | ShippingCity field on the BillingScheduleGroup object | Any one of the shipping address fields is required. |
| `SellingModelType__std` | The selling model type indicates whether the transaction is for a one-time product, a term-defined product, or an evergreen product. Specify `OneTime` as the SellingModelType for the transaction that's related to a product that's sold once. | BillingMethod on the BillingSchedule object is populated as OrderAmount. | Required |
| `TransactionId__std` | The ID of the transaction that you want to create a billing schedule for. | If the transaction is an OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, QuoteLineDetail, or QuoteLineItem record, the ReferenceEntityItemId field on the BillingScheduleobject is populated. For other sObject records or external records, the ReferenceItem field on the BillingSchedule object is populated. | Required |
| `ProductId__std` | The ID of the product that's related to the transaction that you want to create a billing schedule for. | Product2Id field on the BillingScheduleGroup object | Either the ProductName or the ProductId is required |
| `PeriodBoundary__std` | The period boundary determines the start and end date of the billing period. Valid values are: `AlignToCalendar` `Anniversary` `DayOfPeriod` `LastDayOfPeriod` | PeriodBoundary field on the BillingScheduleGroup object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `BillingDayOfMonth__std` | The day of the month on which a recurring billing process is scheduled to occur for the transaction. | BillDayOfMonth field on the BillingScheduleGroup object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `EndDate__std` | The end date of the transaction. | BillingScheduleEndDate field on the BillingSchedule object | Required for products with the `TermDefined` selling model type. |
| `StartDate__std` | The start date of the transaction. | BillingScheduleStartDate field on the BillingSchedule object | Required |
| `Quantity__std` | The quantity of the transaction. | Quantity field on the BillingSchedule object | Required |
| `BillingTermUnit__std` | The unit of measurement of the billing term. Valid values are: `Month` `Quarter` `Semi-Annual` `Year` | BillingTermUnit field on the BillingSchedule object | Required for products with the `TermDefined` or `Evergreen` selling model types. |
| `CurrencyIsoCode__std` | The currency code of the transaction amount if your Salesforce org has multi-currency enabled. | CurrencyIsoCode field on the BillingScheduleGroup object | Required for[Salesforce orgs with multiple currencies enabled](https://help.salesforce.com/s/articleView?id=sales.admin_enable_multicurrency.htm&language=en_US). |
| `BillingActionType__std` | The action that you want to perform for the transaction. Valid value is `Add`. | Category field on the BillingSchedule object is populated as Original. | Required |
| `UnitPrice__std` | The unit price of the transaction. | UnitPrice field on the BillingSchedule object | Either the UnitPrice or the NetUnitPrice value is required |
| `TotalPrice__std` | The total price of the transaction. | TotalAmount field on the BillingSchedule object | Required |
| `ProductUsageModelType__std` | The type of usage model for the transaction product or service. Valid values are: `Anchor`—Anchor is the main subscription product or service. `Pack`—Pack is the add-on product or service that grants additional usage resources for consumption. | BillingMethod value field on the BillingSchedule object is populated as OrderAmount. | Required |
| `BindingInstance__std` | The ID of the Asset record or custom object record that's related to the transaction. | BindingInstanceId on the BillingScheduleGroup object | Required |

=== ARTICLE: connect_requests_billing_schedule_recovery_input.htm ===
---
page_id: connect_requests_billing_schedule_recovery_input.htm
title: Billing Schedule Recovery Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_billing_schedule_recovery_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Billing Schedule Recovery Input

Input representation of the details of the billing schedules to recover the associated
    invoice.

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

=== ARTICLE: connect_requests_calculate_tax_input.htm ===
---
page_id: connect_requests_calculate_tax_input.htm
title: Tax Calculation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_calculate_tax_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Tax Calculation Input

Input representation of the details of the request to calculate tax.

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

=== ARTICLE: connect_requests_context_aware_billing_schedule_input.htm ===
---
page_id: connect_requests_context_aware_billing_schedule_input.htm
title: Context-Aware Billing Schedule
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_aware_billing_schedule_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Context-Aware Billing Schedule

Input representation of the billing transaction details.

    
      
        
          

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

=== ARTICLE: connect_requests_context_aware_standalone_billing_schedule_input.htm ===
---
page_id: connect_requests_context_aware_standalone_billing_schedule_input.htm
title: Standalone Billing Schedule Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_aware_standalone_billing_schedule_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Billing Schedule Input

Input representation of the request to create a billing schedule based on transaction
    details. This representation includes the transaction and context service details.

    

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

- 
**[One-Time New Sale Transaction](./connect_requests_billing_schedule_input_for_one_time_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with the OneTime selling model type.

- 
**[Term-Defined New Sale Transaction](./connect_requests_billing_schedule_input_for_termed_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with the TermDefined selling model type.

- 
**[Evergreen New Sale Transaction](./connect_requests_billing_schedule_input_for_evergreen_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with the Evergreen selling model type.

- 
**[New Sale Transaction With Bundled Products](./connect_requests_billing_schedule_input_for_bundled_products_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with bundled products.

- 
**[New Sale Transaction With Ramped Products](./connect_requests_billing_schedule_input_for_ramps_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with ramped products.

- 
**[New Sale Transaction With Usage Products](./connect_requests_billing_schedule_input_for_usage_new_sale.htm.md)**  

Understand the required values and key considerations before you create a billing     schedule for a new sale transaction with usage-based products.

- 
**[Amended Transaction](./connect_requests_billing_schedule_input_for_amendment.htm.md)**  

Learn how amendments update quantity, price, and end date in billing schedules along     with delta-only price transactions and billing-frequency changes at the billing schedule     level.

- 
**[Renewal Transaction](./connect_requests_billing_schedule_input_for_renewal.htm.md)**  

Create a renewal billing schedule for termed subscriptions that continues without a     gap, starting the day after the current billing schedule group ends and running for the same     term length.

- 
**[Early Renewal Transaction](./connect_requests_billing_schedule_input_for_early_renewal.htm.md)**  

Early Renewal ends the current term at an effective date and starts a renewed term to a     new end date, creating two billing schedules in one request. The request creates a negative     segment for the remaining original term and a positive segment for the renewal term.

- 
**[Canceled Transaction](./connect_requests_billing_schedule_input_for_cancellation.htm.md)**  

Cancel an entire billing schedule from a specified date. Specify only the cancellation     date and billing schedule group identifier. The API computes the logic to split the cancellation     across overlapping billing schedules and creates one cancel transaction per segment.

=== ARTICLE: connect_requests_context_aware_standalone_billing_schedule_metadata_input.htm ===
---
page_id: connect_requests_context_aware_standalone_billing_schedule_metadata_input.htm
title: Standalone Billing Schedule Metadata Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_context_aware_standalone_billing_schedule_metadata_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standalone Billing Schedule Metadata Input

Input representation of the metadata details to create a billing schedule. This
    representation includes the name of the context definition and context mapping along with the
    mapping details of the transaction, billing schedule, and billing schedule group.

          

**JSON example**

          
: 

```
{
  "transactionDetails": "{\"nodeName\": [{\"id\":\"001SG000004FvlGYAS\", \"businessSobjectType\": \"Account\", \"Quantity\":\"4\" , \"Name\": \"TestAccount\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "StandaloneBillingContext",
    "intraContextCustomMappingName": "CustomContextMapping",
    "readContextMappingName": "OrderTransactionMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

This example shows a sample request to generate billing schedules from order
            items by specifying the BillingContext standard context definition as the context
            definition name.

```
{
  "transactionDetails": "{\"nodeName\": [{\"id\":\"001SG000004FvlGYAS\", \"businessSobjectType\": \"Account\", \"Quantity\":\"4\" , \"Name\": \"TestAccount\"}]}",
  "transactionContextDetails": {
    "contextDefinitionName": "BillingContext__stdctx",
    "readContextMappingName": "OrderEntitiesMapping",
    "saveContextMappingName": "BSGEntitiesMapping"
  }
}
```

        

**Properties**

: 

                  
                    

                    

                    

                    

                    

                  

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `context​Definition​Name` | String | Name of the context definition that’s used to hydrate the context to generate the billing schedule. To generate billing schedules from order items, specify the BillingContext standard context definition as the context definition name. Applicable from API version 66.0 and later. | Required | 64.0 |
| `intraContext​CustomMapping​Name` | String | Name of the cross-context custom mapping that's used to map Billing fields to Transaction fields. Use this mapping to populate the Billing fields with the values stored in custom transaction fields. | Optional | 65.0 |
| `readContext​Mapping​Name` | String | Name of the context mapping with the mapping for the transaction. | Required | 64.0 |
| `saveContext​Mapping​Name` | String | Name of the context mapping with the mapping for the billing schedule and billing schedule group. | Required | 64.0 |

=== ARTICLE: connect_requests_convert_negative_invoice_lines_input.htm ===
---
page_id: connect_requests_convert_negative_invoice_lines_input.htm
title: Convert Negative Invoice Lines Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_convert_negative_invoice_lines_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Convert Negative Invoice Lines Input

Input representation of the details of the request to convert a list of negative invoice
    lines into a credit.

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

=== ARTICLE: connect_requests_credit_invoice_input.htm ===
---
page_id: connect_requests_credit_invoice_input.htm
title: Credit Invoice Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_invoice_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Invoice Input

Input representation of the details of the request to create a credit memo.

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

=== ARTICLE: connect_requests_credit_invoice_line_input.htm ===
---
page_id: connect_requests_credit_invoice_line_input.htm
title: Credit Invoice Line Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_invoice_line_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Invoice Line Input

Input representation of the details of the invoice lines to be credited.

    
      
        
          

**JSON example**

          
: 
            

```
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
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 
- 
- 

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `addresses` | [Credit Memo Addresses Input](./connect_requests_credit_memo_addresses_input.htm.md)[] | Addresses to be created manually for this invoice line and the overridden tax lines. These addresses are only applicable if this invoice line is using the `ManualOverride` tax strategy. | Optional | 62.0 |
| `amountTo​Credit` | Double | Amount to be credited from this invoice line. | Required | 62.0 |
| `invoice​LineId` | String | ID of the invoice line record to be credited. The invoice line ID must be related to the invoice ID specified in the API request. | Required | 62.0 |
| `isTaxOnly​Credit` | Boolean | Indicates whether the applicable tax amount is credited for the charge or adjustment amount (`true`), or the applicable tax amount is credited along with the charge or adjustment amount (`false`). The default value is `false`. | Optional | 62.0 |
| `taxEffective​Date` | String | Date when the tax takes effect and the invoice line is credited. | Optional | 62.0 |
| `tax​Strategy` | String | Tax strategy for crediting the invoice line. This tax strategy takes precedence over the `taxStrategy` property value specified in the [Credit Invoice Input](./connect_requests_credit_invoice_input.htm.md). Valid values are: `Ignore`—Specifies that the creation of tax lines must be ignored. `ManualOverride`—Specifies that the provided tax values must be considered for taxes. `CopyFromInvoiceLine`—Specifies that tax values must be copied from the invoice line. `Calculate`—Specifies that tax must be calculated by using the API. | Optional | 62.0 |
| `taxes` | [Credit Invoice Line Tax Input](./connect_requests_credit_invoice_line_tax_input.htm.md)[] | List of tax lines to be created manually for this invoice line. | Required if the `taxStrategy` property value is `ManualOverride`. | 62.0 |

=== ARTICLE: connect_requests_credit_invoice_line_tax_input.htm ===
---
page_id: connect_requests_credit_invoice_line_tax_input.htm
title: Credit Invoice Line Tax Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_invoice_line_tax_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Invoice Line Tax Input

Input representation of the details of the tax lines to be created manually for the
    invoice line.

    
      
        
          

**JSON example**

          
: 
            

```
      "taxes": [
        {
          "taxAmount": 15,
          "taxName": "abc",
          "taxCode": "taxCode",
          "taxRate": 7
        }
      ]
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `taxAmount` | Double | Amount of tax to be applied related to this invoice line. | Required | 62.0 |
| `taxCode` | String | Tax code to be applied related to this invoice line to create the tax line. | Optional | 62.0 |
| `taxName` | String | Name of tax to be applied related to this invoice line. | Optional | 62.0 |
| `taxRate` | Double | Tax rate used to create the tax line. | Optional | 62.0 |

=== ARTICLE: connect_requests_credit_memo_addresses_input.htm ===
---
page_id: connect_requests_credit_memo_addresses_input.htm
title: Credit Memo Addresses Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_addresses_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Addresses Input

Input representation of the details of the billing and shipping addresses.

**JSON example**

: 

```
{
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
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `billing​Address` | [Address Input](./connect_requests_address_input.htm.md)[] | Billing address for charge or adjustment line. | Optional | 62.0 |
| `shipping​Address` | [Address Input](./connect_requests_address_input.htm.md)[] | Shipping address for charge or adjustment line. | Optional | 62.0 |

=== ARTICLE: connect_requests_credit_memo_apply_application_input.htm ===
---
page_id: connect_requests_credit_memo_apply_application_input.htm
title: Credit Memo Apply Application Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_apply_application_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Apply Application Input

Input representation of the request to specify one or more applications to apply a credit
    memo for, with each application representing an invoice.

**JSON example**

: 

```
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
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `amount` | Double | Credit amount to be applied to the invoice. | Required | 62.0 |
| `appliedToId` | String | ID of the invoice record to apply the credit for. | Required | 62.0 |
| `description` | String | Explanation or reason for applying the credit memo. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo. | Optional | 62.0 |

=== ARTICLE: connect_requests_credit_memo_apply_input.htm ===
---
page_id: connect_requests_credit_memo_apply_input.htm
title: Credit Memo Apply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_apply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Apply Input

Input representation of the request to apply a credit memo to an invoice.

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

=== ARTICLE: connect_requests_credit_memo_draft_to_posted_input.htm ===
---
page_id: connect_requests_credit_memo_draft_to_posted_input.htm
title: Credit Memo Draft to Posted Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_draft_to_posted_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Draft to Posted Input

Input representation of the request to post a draft credit memo.

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

=== ARTICLE: connect_requests_credit_memo_line_application_input.htm ===
---
page_id: connect_requests_credit_memo_line_application_input.htm
title: Credit Memo Line Application Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_line_application_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Application Input

Input representation of the request to specify one or more applications to apply a credit
    memo line for, with each application representing an invoice line.

        
          

**JSON example**

          
: 
            

```

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
```

          

        

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `appliedAmount` | Double | Credit amount to be applied to the invoice line. | Required | 62.0 |
| `description` | String | Explanation or reason for applying the credit memo line. | Optional | 62.0 |
| `effectiveDate` | String | Effective date for the credit memo line. | Optional | 62.0 |
| `invoiceLineId` | String | ID of the invoice line record to apply the credit for. | Required | 62.0 |

=== ARTICLE: connect_requests_credit_memo_line_apply_input.htm ===
---
page_id: connect_requests_credit_memo_line_apply_input.htm
title: Credit Memo Line Apply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_line_apply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Apply Input

Input representation of the details of the request to apply a credit memo line to an
    invoice line.

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

=== ARTICLE: connect_requests_credit_memo_line_unapply_input.htm ===
---
page_id: connect_requests_credit_memo_line_unapply_input.htm
title: Credit Memo Line Unapply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_line_unapply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Line Unapply Input

Input representation of the details of the request to unapply a credit memo line from
    an invoice line.

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

=== ARTICLE: connect_requests_credit_memo_unapply_input.htm ===
---
page_id: connect_requests_credit_memo_unapply_input.htm
title: Credit Memo Unapply Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_credit_memo_unapply_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Credit Memo Unapply Input

Input representation of the request to unapply a credit memo from an invoice.

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

=== ARTICLE: connect_requests_customer_details_input.htm ===
---
page_id: connect_requests_customer_details_input.htm
title: Customer Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_customer_details_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Customer Details Input

Input representation of the customer details for tax calculation.

**JSON example**

: 

```
{
    "accountId": "001R000000000zSMAQ"
}

```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `accountId` | String | Salesforce account ID of the customer. | Optional | 62.0 |

=== ARTICLE: connect_requests_draft_to_posted_invoice_input.htm ===
---
page_id: connect_requests_draft_to_posted_invoice_input.htm
title: Invoice Draft To Posted Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_draft_to_posted_invoice_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Draft To Posted Input

Input representation of the details of the draft invoice that’s posted.

    
      
        
          

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

=== ARTICLE: connect_requests_frequency_cadence_options.htm ===
---
page_id: connect_requests_frequency_cadence_options.htm
title: Frequency Cadence Options
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_frequency_cadence_options.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Frequency Cadence Options

Input representation of the frequency cadence options for an invoice
    scheduler.

**JSON example**

: 

```
  "frequencyCadenceOptions": {
        "recurringSubType" : "Every",
        "recursOn" : "First",
        "recursOnDay" : "Sunday",
        "shouldExcludeWkendAndHldy": true
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
| `recurring​Sub​Type` | String | Subtype of the recurring frequency for the invoice run. Valid values are: `Every`—Specifies if the invoice scheduler must generate the invoices on a recurring frequency on a specific cadence. Use this value to generate invoices on a specific day of the month. For example, you can specify that the invoice scheduler must generate the invoices every first Monday of the month. `SpecificDate`—Specifies if the invoice scheduler must generate the invoices on a recurring frequency on a specific date. Use this value to generate invoices on a monthly basis on a specific date. | Required if the `frequency​Cadence` property is set to `Monthly`. | 62.0 |
| `recurs​On` | String | Cadence that specifies when the invoice scheduler must generate the invoices on a recurring frequency. For example, you can specify that the invoice scheduler must generate the invoices every first Monday of the month. Valid values are: `First` `Second` `Third` `Fourth` `Last` | Required if the `frequency​Cadence` property is set to `Monthly`. | 62.0 |
| `recursOn​Date` | String | Date when the invoice scheduler must generate the invoices on a specific date. The supported values are: 1 through 28—Specify any date from 1 through 28. `L`—Specifies that the invoice scheduler must generate the invoices on the last day of the month. `L-1`—Specifies that the invoice scheduler must generate the invoices on the second to last day of the month. `L-2`—Specifies that the invoice scheduler must generate the invoices on the third to last day of the month. | Required if the `recurring​Sub​Type` property is set to `SpecificDate`. | 62.0 |
| `recursOn​Day` | String | Day of the week when the invoice scheduler must generate the invoices on a recurring frequency. For example, you can specify that the invoice scheduler must generate the invoices every Monday or every first Monday of a month. Valid values are: `Sunday` `Monday` `Tuesday` `Wednesday` `Thursday` `Friday` `Saturday` | Required if the `frequency​Cadence` property is set to `Weekly` or `Monthly`. | 62.0 |
| `should​Exclude​Wkend​AndHldy` | Boolean | Indicates whether to exclude weekends and holidays from the billing schedule (`true`) or not (`false`). | Required if the `frequency​Cadence` property is set to `Monthly`. | 62.0 |

=== ARTICLE: connect_requests_graph_record_input.htm ===
---
page_id: connect_requests_graph_record_input.htm
title: Graph Record for Invoice Ingestion
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_graph_record_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Graph Record for Invoice Ingestion

A Graph record is an object that’s a part of the graph structure,
      representing both the fields and relationships among different objects. Each record in the
      graph can contain attributes, which are fields of the object, and references to other related
      records.

    

Invoice ingestion supports a Graph record count of 500. The supported Graph
        attribute types for  invoice ingestion are Account, Contact, Invoice, InvoiceLine,
        InvoiceLineTax, and InvoiceAddressGroup.

A Graph record has these properties and associated fields.

          
          
          
            
              

              

            

          

          
            
              

              

            

            
              

              

            

            
              

              

            

            
              

              

            

          

        
| Field | Description |
| --- | --- |
| `referenceId` | Unique identifier of the record that’s used to reference the record in the graph. |
| `record` | Object containing the actual data for the record. |
| `record.attributes.type` | Standard object of the referenced record. In this scenario, this field indicates an `InvoiceAddressGroup` attribute type. |
| `record.attributes.method` | Method that defines the operation on the record. For example, POST to create a record, PUT to update a record, or GET to get record data. |

        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refBillingAddress",
  "record": {
    "attributes": {
      "type": "InvoiceAddressGroup",
      "method": "POST"
    },
    //Contains the actual data
  }
}
```

          

        
      

    

## Account Record

      
      

Keep these considerations in mind when you specify an Account record as the Graph attribute
        type.

      
        
- The supported Graph attribute method is GET only.

        
- The supported record count that you can specify for each account is one only.

        
- The id field on attributes is the value of the externalId field API Name in [Account](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_account.htm). Use this field to
          resolve the Salesforce Account ID from the custom external ID field. See [Use an 'External ID' to set the values for audit
            fields](https://help.salesforce.com/s/articleView?id=000383278&type=1&language=en_US).

      

      
        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refAccount", 
  "record": {
    "attributes": {
      "type": "Account",
      "method": "GET",
      "id": "AccountId__c/7661eaaf-f527-4dcf-beb3-301f3eddcd9e"
    }
  }
}
```

          

        
      

    

    

## Contact Record

      
      

Keep these considerations in mind when you specify a Contact record as the Graph attribute
        type.

      
        
- The supported Graph attribute method is GET only.

        
- The supported record count that you can specify for Contact is one only.

        
- The id field on attributes is the value of the externalId field API Name in [Contact](https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_contact.htm). Use this field to resolve the Salesforce Contact ID from the custom
          external ID field. See [Use an 'External ID' to set the values for audit
            fields](https://help.salesforce.com/s/articleView?id=000383278&type=1&language=en_US).

      

      
        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refContact", 
  "record": {
    "attributes": {
      "type": "Contact",
      "method": "GET",
      "id": "ContactId__c/7661eaaf-f527-4dcf-beb3-301f3eddcd9e"
    }
  }
}
```

          

        
      

    

    

## Invoice Record

      
      

Keep these considerations in mind when you specify an Invoice record as the Graph attribute
        type.

      
        
- The supported Graph attribute method is POST only.

        
- The supported record count that you can specify for Invoice is one only.

        
- An invoice with `Draft` status can’t have a posted
          date.

        
- You can’t use an invoice with `Draft` status when the
            `taxCalculationStatus` property value is `Posted`. The `taxCalculationStatus` property must be `Estimated` or `Pending`.

        
- You can’t use an invoice with `Posted` status when
          the `shouldCalculateTax` property is `true`.

        
- An invoice with `Posted` status can’t include the
            `Estimated` or `Pending` as the `taxCalculationStatus`
          property values. The tax processing status must be `Posted`.

        
- An invoice with `Posted` status with an invoice line
          marked as `taxable` must include an `invoiceLineTax` for that invoice line.

        
- An invoice with `Posted` status with an invoice line
          marked as `nontaxable` must not include an `invoiceLineTax` for that invoice line.

        
- The `invoice.CreationMode` field value is `External`. This field differentiates the invoices created
          from a billing schedule or an invoice ingestion. For invoices created from a billing
          schedule, the value is Salesforce. For invoices created from an invoice ingestion, the
          value is `External`.

        
- The due date of an invoice graph is in the future or with a valid payment term, or your
          Salesforce org has a default payment term set.

      

      
        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refInvoice",
  "record": {
    "attributes": {
      "type": "Invoice",
      "method": "POST"
    },
    "invoiceDate": "2024-01-01",
    "billingAccountId": "001xx000003Dzo9AAC",
    "billToContactId": "003xx000004TzFoAAI",
    "paymentTermId": "2OXxx0000004CFUGA2",
    "referenceEntityId": "801xx000003GeQQAA0",
    "status": "Draft",
    "currencyIsoCode": "USD",
    "dueDate": "2024-02-01",
    "postedDate": "2024-01-02",
    "invoiceNumber": "INV-12345",
    "uniqueIdentifier": "1a9380c1-8042-422d-bcc5-70c3f51c2588",
    "description": "Consulting Services"
  }
}
```

          

          
: 
            

Table 1. Properties
                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

- 
- 

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| NAME | Standard Object Field | Description | Required or Optional |
| --- | --- | --- | --- |
| `invoiceDate` | Invoice.invoiceDate | Date when the invoice was created or issued. | Required |
| `billingAccountId` | Invoice.billingAccountId | Billing account associated with this invoice, which you can resolve with the externalId field by using the GET method. | Required |
| `billToContactId` | Invoice.billToContactId | Contact to whom the invoice is billed, which you can resolve with the externalId field by using the GET method. | Required |
| `paymentTermId` | Invoice.paymentTermId | Payment term associated with the invoice. If a value isn’t specified, then the default payment term ID is used. | Optional |
| `referenceEntityId` | Invoice.referenceEntityId | Reference to a related object, if applicable. To generate invoices from debit memos, specify the debit memo ID as the property value. Make sure that the debit memo is in `Posted` status. Available in API version 66.0 and later. The invoice is generated in `Draft` status. | Optional |
| `status` | Invoice.status | Status of the invoice. Valid values are: `Draft` `Posted`. The default value is `Draft`. | Optional |
| `currencyIsoCode` | Invoice.currencyIsoCode | ISO code representing the currency of the invoice. This property must be specified if multi-currency is enabled in the organization. | Optional |
| `dueDate` | Invoice.dueDate | Due date for the invoice payment. If a value isn’t specified, then this value is set based on the payment term. | Optional |
| `postedDate` | Invoice.postedDate | Date the invoice was posted to the system. Until API version 64.0, the default value is the current date irrespective of the value that’s specified in the input payload. In API version 65.0 and later, the posted date specified in the input payload is considered. | Required in API version 65.0 and later. |
| `invoiceNumber` | Invoice.invoiceNumber | Unique identifier for the invoice. | Optional |
| `uniqueIdentifier` | Invoice.uniqueIdentifier | Unique identifier for the invoice. This property is used as the idempotency key to avoid duplicate invoice generation. | Optional |
| `description` | Invoice.description | Short description of the invoice or the billed items. | Optional |

          

        
      

    

    

## Invoice Line Record

      
      

Keep these considerations in mind when you specify an Invoice Line record as the Graph
        attribute type.

      
        
- The supported Graph attribute method is POST only.

        
- The Graph must include at least one Graph record with the InvoiceLine attribute
          type.

        
- The invoice line end date must be greater than or equal to the invoice line start
          date.

      

      
        
          

**JSON example**

          
: 
            

```
{
  "referenceId": "refInvoiceLine",
  "record": {
    "attributes": {
      "type": "InvoiceLine",
      "method": "POST"
    },
    "name": "Parle G",
    "invoiceLineStartDate": "2024-01-01",
    "invoiceLineEndDate": "2024-01-31",
    "quantity": 10,
    "unitPrice": 25,
    "chargeAmount": 250,
    "invoiceId": "@{refInvoice.id}",
    "shippingAddressId": "@{refShippingAddress.id}",
    "billingAddressId": "@{refBillingAddress.id}",
    "referenceEntityItemId": "802xx000001neB9AAI",
    "taxTreatmentId": "1ttxx0000000BOTAA2",
    "legalEntityId": "0fwxx0000000001AAA",
    "legalEntityAccountingPeriodId": "1HLxx0000004C92GAE",
    "product2Id": "01txx0000006ic4AAA",
    "usageProductId": "01txx0000006ic5AAA",
    "isUsageBasedInvoiceLine": false,
    "usageOverageQuantity": 5,
    "unitOfMeasureId": "0hExx0000000001EAA",
    "description": "Sample product description"
  }
}
```

          

          
: 
            

Table 2. Properties
                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| NAME | Standard Object Field | Description | Required or Optional |
| --- | --- | --- | --- |
| `name` | InvoiceLine.name | Name or description of the invoice line item. | Required |
| `invoiceLineStartDate` | InvoiceLine.invoiceLineStartDate | Start date for the invoice line period. For example, the date when the product or service is provided. | Required |
| `invoiceLineEndDate` | InvoiceLine.invoiceLineEndDate | End date for the invoice line period. For example, the date when the product or service ends. | Required |
| `quantity` | InvoiceLine.quantity | Quantity of the product or billed service in this invoice line. | Required |
| `unitPrice` | InvoiceLine.unitPrice | Price per unit of the product or billed service. | Required |
| `chargeAmount` | InvoiceLine.chargeAmount | Total charge amount for this invoice line, which is calculated as quantity * unit price. | Required |
| `invoiceId` | InvoiceLine.invoiceId | Reference to the invoice that this invoice line is associated with. | Required |
| `shippingAddressId` | InvoiceLine.shippingAddressId | Shipping address associated with this invoice line. | Required |
| `billingAddressId` | InvoiceLine.billingAddressId | Billing address associated with this invoice line. | Required |
| `referenceEntityItemId` | InvoiceLine.referenceEntityItemId | Reference to a related object record for this invoice line. | Optional |
| `taxTreatmentId` | InvoiceLine.taxTreatmentId | Tax treatment applied to this invoice line such as taxable or nontaxable. If the `TaxTreatmentId` property isn’t specified in the request, it’s retrieved from the [organization's default values](https://help.salesforce.com/s/articleView?language=en_US&id=ind.guided_setup_for_billing.htm&type=5). If the organization's defaults aren’t set, an error is thrown. | Optional |
| `legalEntityId` | InvoiceLine.legalEntityId | Legal entity that this invoice line belongs to. If the `LegalEntityId` property isn’t specified in the request, it’s retrieved from the [organization's default values](https://help.salesforce.com/s/articleView?id=ind.guided_setup_for_billing.htm&type=5&language=en_US). If the organization's defaults aren’t set, an error is thrown. | Optional |
| `legalEntityAccountingPeriodId` | InvoiceLine.legalEntityAccountingPeriodId | Accounting period for the legal entity that this invoice line belongs to. | Optional |
| `product2Id` | InvoiceLine.product2Id | Identifier for the product that’s billed in this invoice line. | Optional |
| `usageProductId` | InvoiceLine.usageProductId | Identifier for the usage-based product if this invoice line is for usage-based billing. | Optional |
| `isUsageBasedInvoiceLine` | InvoiceLine.isUsageBasedInvoiceLine | Boolean value that indicates whether this invoice line is for a usage-based product (`true`) or not (`false`). | Optional |
| `usageOverageQuantity` | InvoiceLine.usageOverageQuantity | Quantity of usage overage for this invoice line, if applicable. | Optional |
| `unitOfMeasureId` | InvoiceLine.unitOfMeasureId | Identifier for the unit of measure for the product or service, such as each, kg, or lb. | Optional |
| `description` | InvoiceLine.description | Description of the invoice line item with additional details. | Optional |

          

        
      

    

    

## Tax Record

      
      

Keep these considerations in mind when you specify a Tax record as the Graph attribute
        type.

      
        
- The supported Graph attribute method is POST only.

        
- The associated standard object is InvoiceLineTax.

        
- The invoiceLineTax graph record must not include the `taxCalculationStatus` property value as `Pending`.

      

      
        
          

**JSON example**

          
: 
            

```
{
    "referenceId": "refInvoiceLineTax",
    "record": {
        "attributes": {
            "type": "InvoiceLineTax",
            "method": "POST"
        },
        "taxTransactionNumber": "TX123456789",
        "taxAmount": 15.00,
        "taxRate": 0.08,
        "taxName": "Sales Tax",
        "taxCode": "TX-SALES",
        "taxEffectiveDate": "2024-01-01",
        "invoiceLine": "@{refInvoiceLine.id}",
        "taxDocumentNumber": "TAXDOC987654",
        "taxExemptAmount": 0.00,
        "description": "Exempt from VAT"
    }
}
```

          

          
: 
            

Table 3. Properties
                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| NAME | Standard Object Field | Description | Required or Optional |
| --- | --- | --- | --- |
| `taxTransactionNumber` | InvoiceLineTax.taxTransactionNumber | Unique identifier of the tax transaction related to this invoice line tax. | Required |
| `taxAmount` | InvoiceLineTax.taxAmount | Total tax amount applied to the invoice line. | Required |
| `taxRate` | InvoiceLineTax.taxRate | Rate at which the tax is applied on the invoice line. | Required |
| `taxName` | InvoiceLineTax.taxName | Name of the tax applied on the invoice line, such as Sales Tax or Value Added Tax (VAT). | Required |
| `taxCode` | InvoiceLineTax.taxCode | Tax code that corresponds to the applied tax rate. | Required |
| `taxEffectiveDate` | InvoiceLineTax.taxEffectiveDate | Effective date from which the tax rate applies. | Required |
| `invoiceLine` | InvoiceLineTax.invoiceLine | Reference to the invoice line this tax record is associated with. | Required |
| `taxDocumentNumber` | InvoiceLineTax.taxDocumentNumber | Document number associated with the tax transaction, such as tax return document or government filing number. | Required |
| `taxExemptAmount` | InvoiceLine.billingAddressId | Billing address associated with this invoice line. | Required |
| `description` | InvoiceLineTax.description | Additional details about the tax. | Optional |

          

        
      

    

    

## Shipping Address Record

      
      

Keep these considerations in mind when you specify a Shipping Address record as the Graph
        attribute type.

      
        
- The supported Graph attribute method is POST only.

        
- The associated standard object is InvoiceAddressGroup.

      

      
        
          

**JSON example**

          
: 
            

```
{
    "referenceId": "refShippingAddress",
    "record": {
        "attributes": {
            "type": "InvoiceAddressGroup",
            "method": "POST"
        },
        "street": "456 Elm St",
        "city": "Springfield",
        "postalCode": "62701",
        "state": "IL",
        "country": "USA",
        "longitude": "-89.6501",
        "latitude": "39.7817",
        "invoiceId": "@{refInvoice.id}"
    }
}
```

          

          
: 
            

Table 4. Properties
                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| NAME | Standard Object Field | Description | Required or Optional |
| --- | --- | --- | --- |
| `invoiceId` | InvoiceAddressGroup.invoice | Unique identifier of the invoice associated with this shipping address. | Required |
| `street` | InvoiceAddressGroup.street | Street address where the goods or services are shipped to. | Required |
| `city` | InvoiceAddressGroup.city | City where the shipment is delivered. | Required |
| `postalCode` | InvoiceAddressGroup.postalCode | Postal or ZIP code for the shipping address. | Required |
| `state` | InvoiceAddressGroup.state | State or province of the delivery location. | Required |
| `country` | InvoiceAddressGroup.country | Country where the shipment is delivered. | Required |
| `longitude` | InvoiceAddressGroup.longitude | Geographic longitude of the shipping address location for mapping purposes. | Optional |
| `latitude` | InvoiceAddressGroup.latitude | Geographic latitude of the shipping address location for mapping purposes. | Optional |

          

        
      

    

    

## Billing Address Record

      
      

Keep these considerations in mind when you specify a Billing Address record as the Graph
        attribute type.

      
        
- The supported Graph attribute method is POST only.

        
- The associated standard object is InvoiceAddressGroup.

      

      
        
          

**JSON example**

          
: 
            

```
{
    "referenceId": "refBillingAddress",
    "record": {
        "attributes": {
            "type": "InvoiceAddressGroup",
            "method": "POST"
        },
        "street": "789 Oak St",
        "city": "Los Angeles",
        "postalCode": "90001",
        "state": "CA",
        "country": "USA",
        "longitude": "-118.2437",
        "latitude": "34.0522",
        "invoiceId": "@{refInvoice.id}"
    }
}
```

          

          
: 
            

Table 5. Properties
                
                
                
                
                
                  
                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                  

                

              
| NAME | Standard Object Field | Description | Required or Optional |
| --- | --- | --- | --- |
| `invoiceId` | InvoiceAddressGroup.invoice | Unique identifier of the invoice associated with this billing address. | Required |
| `street` | InvoiceAddressGroup.street | Street address for billing purposes. | Required |
| `city` | InvoiceAddressGroup.city | City for billing address. | Required |
| `postalCode` | InvoiceAddressGroup.postalCode | Postal or ZIP code for the billing address. | Required |
| `state` | InvoiceAddressGroup.state | State or province for the billing address. | Required |
| `country` | InvoiceAddressGroup.country | Country for the billing address. | Required |
| `longitude` | InvoiceAddressGroup.longitude | Geographic longitude of the billing address location for mapping purposes. | Optional |
| `latitude` | InvoiceAddressGroup.latitude | Geographic latitude of the billing address location for mapping purposes. | Optional |

=== ARTICLE: connect_requests_invoice_estimated_tax_calculation_input.htm ===
---
page_id: connect_requests_invoice_estimated_tax_calculation_input.htm
title: Invoice Estimated Tax Calculation Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_invoice_estimated_tax_calculation_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Billing
parent_page: billing_business_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Invoice Estimated Tax Calculation Input

Details of the invoice for which the estimated tadsfsefx must be calculated.

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

