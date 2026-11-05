# Revenue Management Developer Guide 264 — sección: Advanced Approvals (23 artículos)

=== ARTICLE: actions_obj_cancel_approval_submission.htm ===
---
page_id: actions_obj_cancel_approval_submission.htm
title: Cancel Approval Submission Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_cancel_approval_submission.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Cancel Approval Submission Action

Cancels an approval submission and all child approval work items
            that haven't been completed. You can also add comments about why the approval admin made
            the cancellation.

        

This action also validates if a user has required permissions to cancel an approval submission.
                Keep these considerations in mind when you use this invocable action.

            
                
- The user must have the Approval Admin user permission.

                
- The status of the approval submission must be in `In
                        progress` or `Suspended`
                    status.

            

This action is available in API version 62.0 and later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/cancelApprovalSubmission`

                
                
                    

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
| approvalSubmissionId | **Type** string **Description** Required. ID of the Approval Submission to be canceled. |
| comments | **Type** string **Description** Comments entered by the approval admin about why they canceled the Approval Submission. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Cancel Approval Submission action.

                        

```
{
  "inputs": [
    {
      "approvalSubmissionId": "9iPxx00000001lhEBA",
      "comments": "Cancellation comments."
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Cancel Approval Submission action.

                        

```
{
  "actionName": "cancelApprovalSubmission",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": null,
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_get_previous_rela_rec_details.htm ===
---
page_id: actions_obj_get_previous_rela_rec_details.htm
title: Get Previous Related Record Details Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_get_previous_rela_rec_details.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Previous Related Record Details Action

Get the related record details submitted for approval before the
            current approval submission. The details are required for approval steps that use custom
            logic for auto-approvals.

        
            

This Apex action is available in API version 66.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/getPreviousRelaRecDetails`

                
                
                    

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
| flowOrchestrationInstanceId | **Type** string **Description** Required. The ID of the flow orchestration instance associated with the approval submission. |
| stepApiNamesList | **Type** string **Description** Required. The comma-delimited list of step API names to retrieve previous related record details for. |

        

        

## Outputs

            
            

                    
                    
                    
                        
                            

                            

                        

                    

                    
                        
                            

                            

: 

: 

                        

                    

                
| Output | Details |
| --- | --- |
| previousRelatedRecordDetails | **Type** sObject **Description** The collection of previous related record details for approval steps that use custom logic for auto-approvals. |

        

        

## Usage

To use this Apex action in approval workflows, see [Define Rules and
                    Conditions for Auto-Approval Resubmissions](https://help.salesforce.com/s/articleView?id=ind.approvals_define_custom_logic_auto_approvals.htm&language=en_US).

        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Get Previous Related Record Details
                            action.

                        

```
{
  "flowOrchestrationInstanceId": "0jEDU0000001zeN",
  "stepApiNameList": [
    "ManagerApprovalStep",
    "FinancialApprovalStep"
  ]
}
```

=== ARTICLE: actions_obj_override_approval_work_item.htm ===
---
page_id: actions_obj_override_approval_work_item.htm
title: Override Approval Work Item Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_override_approval_work_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Override Approval Work Item Action

Update an approval work item status with the approval admin decision
            and any comments that the approval admin added.

        

This action also validates if a user has required permissions to override an approval work item
                and update its status. Keep these considerations in mind when you use this invocable
                action.

            
                
- The user must have the Approval Admin user permission.

                
- This action enables approval admins to interject the approval decision for any
                    assignee.

                
- The status of the approval work item must be in `Assigned` status.

            

This action is available in API version 62.0 and later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/overrideApprovalWorkItem`

                
                
                    

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

- 
- 
- 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| approvalDecision | **Type** string **Description** Required. Action that the overriding approval admin made for the unreviewed approval work item. Valid values are: `approve` `reject` |
| approvalWorkItemId | **Type** string **Description** Required. ID of the unreviewed approval work item to be reviewed by an approval admin. |
| channelType | **Type** picklist **Description** Type of channel where the request to review the approval work item originated. Valid values are: `InvocableAction` `Slack` `ApprovalRecord` The default value is `InvocableAction`. Available in API version 65.0 and later. |
| comments | **Type** string **Description** Comments entered by the approval admin about their decision to approve or reject an unreviewed approval work item. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Override Approval Work Item action.

                        

```
{
  "inputs": [
    {
      "approvalWorkItemId": "9jRxx00000001lhEAA",
      "approvalDecision": "Reject",
      "channelType": "InvocableAction",
      "comments": "Needs to be reviewed."
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Override Approval Work Item action.

                        

```
{
  "actionName": "overrideApprovalWorkItem",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": null,
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_reassign_approval_work_item.htm ===
---
page_id: actions_obj_reassign_approval_work_item.htm
title: Reassign Approval Work Item Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_reassign_approval_work_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Reassign Approval Work Item Action

Reassign an approval work item that hasn't been completed. You can
            also add comments about why the approval admin reassigned the approval work
        item.

        

This action also validates if a user has required permissions to reassign an approval work item
                and update the assignee. Keep these considerations in mind when you use this
                invocable action.

            
                
- The user must have the Approval Admin user permission.

                
- The status of the approval work item must be in `Assigned` status.

            

This action is available in API version 62.0 and later.

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/reassignApprovalWorkItem`

                
                
                    

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
| approvalWorkItemId | **Type** string **Description** Required. ID of the approval work item to be reassigned. |
| assigneeId | **Type** string **Description** Required. ID of the user, group, or queue to reassign the approval work item to. |
| comments | **Type** string **Description** Comments entered by the approval admin about why they reassigned the approval work item. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Reassign Approval Work Item action.

                        

```
{
  "inputs": [
    {
      "approvalWorkItemId": "9jRDU00000015C22AI",
      "assigneeId": "005DU000000I3zHYAS",
      "comments": "Needs to be reviewed."
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Reassign Approval Work Item action.

                        

```
{
  "actionName": "reassignApprovalWorkItem",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": null,
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_recall_approval_submission.htm ===
---
page_id: actions_obj_recall_approval_submission.htm
title: Recall Approval Submission Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_recall_approval_submission.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Recall Approval Submission Action

Recall an approval submission that isn't completed. You can also add
            comments that the submitter or approval admin made the recall.

        
            

This action also validates if a user has required permissions to recall an approval
                submission. Keep these considerations in mind when you use this invocable
                action.

            
                
- The user must have the Approval Admin user permission.

                
- The user must also be a submitter of this approval submission.

                
- The status of the approval submission must be in `In
                        progress` or `Suspended`
                    status.

            

            

This action is available in API version 62.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/recallApprovalSubmission`

                
                
                    

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
| approvalSubmissionId | **Type** string **Description** Required. ID of the approval submission to be recalled. |
| comments | **Type** string **Description** Comments entered by the approval admin or approval submitter about why they recalled the approval submission. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Recall Approval Submission action.

                        

```
{
  "inputs": [
    {
      "approvalSubmissionId": "9iPxx00000001lhEBA",
      "comments": "Recall comments."
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Recall Approval Submission action.

                        

```
{
  "actionName": "recallApprovalSubmission",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": null,
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: actions_obj_review_approval_work_item.htm ===
---
page_id: actions_obj_review_approval_work_item.htm
title: Review Approval Work Item Action
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_review_approval_work_item.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_invocable_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Review Approval Work Item Action

Update an approval work item status with the assignee or reviewer's
            decision and any comments that the assignee or reviewer added.

        
            

Keep these considerations in mind when you use this invocable action.

            
                
- The user must be an assignee of the approval work item or be a member of a group
                    or queue if the approval work item is assigned to the group or queue.
                    Additionally, a user has access to Approval Submissions if they're a delegate of
                    the assignee or has a role higher than the assignee.

                
- The status of the approval work item must be in `Assigned` status.

                
- The user can also use this action if inherited access to group or queue
                    membership, nested group membership, roles hierarchy, or delegates is available.
                    See [Public Group
                        Considerations](https://help.salesforce.com/s/articleView?id=platform.user_groups_considerations.htm&language=en_US).

            

            

This action is available in API version 62.0 and later.

        

        
        

## Supported REST HTTP Methods

            
            
                
                    

**URI**

                    
: `/services/data/v68.0/actions/standard/reviewApprovalWorkItem`

                
                
                    

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

                        

                        
                            

                            

: 

: 

                        

                        
                            

                            

: 

: 

- 
- 
- 

                        

                        
                            

                            

: 

: 

                        

                    

                
| Input | Details |
| --- | --- |
| approvalDecision | **Type** string **Description** Required. Action that the assigned approver made for the approval work item. Valid values are: `approve` `reject` |
| approvalWorkItemId | **Type** string **Description** Required. ID of the approval work item to be reviewed by the assigned approver. |
| channelType | **Type** picklist **Description** Type of channel where the request to review the approval work item originated. Valid values are: `InvocableAction` `Slack` `ApprovalRecord` The default value is `InvocableAction`. Available in API version 65.0 and later. |
| comments | **Type** string **Description** Approval comments for the decision. |

        

        

## Outputs

None.

        
        

## Example

            
            
                
                    

**POST**

                    
: 
                        

Here's a sample request for the Review Approval Work Item action.

                        

```
{
  "inputs": [
    {
      "approvalWorkItemId": "9jRxx00000001lhEAA",
      "approvalDecision": "Approve",
      "channelType": "InvocableAction",
      "comments": "Looks good."
    }
  ]
}
```

                    

                    
: 
                        

Here's a sample response for the Review Approval Work Item action.

                        

```
{
  "actionName": "reviewApprovalWorkItem",
  "errors": null,
  "invocationId": null,
  "isSuccess": true,
  "outcome": null,
  "outputValues": null,
  "sortOrder": -1,
  "version": 1
}
```

=== ARTICLE: adv_approvals_capture_fields_on_approvalworkitem.htm ===
---
page_id: adv_approvals_capture_fields_on_approvalworkitem.htm
title: Advanced Approvals Fields on Approval Work Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/adv_approvals_capture_fields_on_approvalworkitem.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approval_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals Fields on Approval Work Item

Standard and custom fields extend the standard Approval Work Item
         object for use in Advanced Approvals.
   

      

## Supported Calls

         
         

            `describeLayout()`, `describeSObjects()`, `getDeleted()`,
               `getUpdated()`, `query()`, `retrieve()`, `update()`
         

      

      

## Special Access Rules

         
         

This object is available in Enterprise, Performance, Unlimited, and Developer Editions
            for users with access to the Approval Submission object.

      

      

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
| ApprovalChainName | **Type** string **Properties** Filter, Group, Nillable, Sort, Update **Description** The name of the related approval chain. This field is populated when there are multiple approval chains that are run in parallel. This field is only available with Advanced Approvals enabled. |
| CurrencyIsoCode | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Available only for organizations with the multicurrency feature enabled. Contains the ISO code for any currency allowed by the organization. Valid values are: `AED`—UAE Dirham `AUD`—Australian Dollar `BRL`—Brazilian Real `CAD`—Canadian Dollar `EUR`—Euro `GBP`—British Pound `INR`—Indian Rupee `JPY`—Japanese Yen `SEK`—Swedish Krona `USD`—U.S. Dollar The default value is `USD`. |
| IsAutoReviewed | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the approval work item is eligible for smart approval (true) or not (false). The default value is `false`. |
| IsEligibleForSmartApproval | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the approval work item is eligible for smart approval (`true`) or not (`false`). The default value is `false`. |
| SmartApprovalBasisWorkItemId | **Type** reference **Properties** Filter, Group, Nillable, Sort, Update **Description** The previous approval work item used as a reference for the auto-approval evaluation. This field is a relationship field. **Relationship Name** SmartApprovalBasisWorkItem **Refers To** ApprovalWorkItem |

=== ARTICLE: advanced_approval_fields_on_standard_objects.htm ===
---
page_id: advanced_approval_fields_on_standard_objects.htm
title: Advanced Approvals Fields on Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approval_fields_on_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals Fields on Standard Objects 

Advanced Approvals adds standard and custom fields to some standard Salesforce objects.
    These fields are available only in Revenue Management orgs where Advanced Approvals is
    enabled.

- 
**[ApprovalSubmission](./sforce_api_objects_approvalsubmission.htm.md)**  

       Represents the instance of an approval request that's submitted for a record          of the related object. This object is available in API version 62.0 and       later.

- 
**[Advanced Approvals Fields on Approval Work Item](./adv_approvals_capture_fields_on_approvalworkitem.htm.md)**  

Standard and custom fields extend the standard Approval Work Item          object for use in Advanced Approvals.

=== ARTICLE: advanced_approvals_api_requests.htm ===
---
page_id: advanced_approvals_api_requests.htm
title: Request Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_api_requests.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Request Bodies

Learn more about the available request bodies.

- 
**[Preview Approval Input](./connect_requests_preview_approval_input.htm.md)**  

Input representation of the details of the request to preview an approval.

=== ARTICLE: advanced_approvals_api_responses.htm ===
---
page_id: advanced_approvals_api_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_api_responses.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Learn more about the available response bodies.

- 
**[Preview Approval](./connect_responses_preview_approval_output.htm.md)**  

Output representation of the details of a preview approval request.

- 
**[Preview Approval Chain Item](./connect_responses_preview_approval_chain_item_output.htm.md)**  

Output representation of the details of an approval chain item for a specific     group.

- 
**[Preview Approval Error](./connect_responses_preview_approval_error.htm.md)**  

Output representation of the error details associated with the Preview Approval     API.

- 
**[Preview Approval Item](./connect_responses_preview_approval_item_output.htm.md)**  

Output representation of the details of a specific approval item with an approval     chain.

=== ARTICLE: advanced_approvals_business_apis.htm ===
---
page_id: advanced_approvals_business_apis.htm
title: Advanced Approvals Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_business_apis.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals Business APIs

Use the Advanced Approvals Business APIs to preview approval levels and related
    details before you submit a record for approval.

    

This table lists the available Advanced Approvals resources.

    

        
        
        
          
            

            

          

        

        
          
            

            

          

        

      
| Resource | Description |
| --- | --- |
| [`/connect/advanced-approvals/approval-submission/preview`](./connect_resources_preview_approvals.htm.md) (POST) | Preview the approval levels of a record and associated level details, approval chains, approvers, and conditions before you submit the record for an approval. |

  

- 
**[Resources](./advanced_approvals_business_apis_rest_references.htm.md)**  

Learn more about the available Advanced Approvals resources.

- 
**[Request Bodies](./advanced_approvals_api_requests.htm.md)**  

Learn more about the available request bodies.

- 
**[Response Bodies](./advanced_approvals_api_responses.htm.md)**  

Learn more about the available response bodies.

=== ARTICLE: advanced_approvals_business_apis_rest_references.htm ===
---
page_id: advanced_approvals_business_apis_rest_references.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_business_apis_rest_references.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_business_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Learn more about the available Advanced Approvals resources.

- 
**[Preview Approval (POST)](./connect_resources_preview_approvals.htm.md)**  

Preview the approval levels of a record and associated level details,       approval chains, approvers, and conditions before you submit the record for an     approval.

=== ARTICLE: advanced_approvals_flow_metadata_api.htm ===
---
page_id: advanced_approvals_flow_metadata_api.htm
title: Flow for Advanced Approvals
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Advanced Approvals

The flow for Advanced Approvals represents the metadata associated with a flow. With
    Flow, you can create an application that takes users through a series of pages to query and
    update the records in the database. You can also run logic and provide branching capability
    based on user input to build dynamic applications.

    

## FlowActionCall

Advanced Approvals exposes additional actionType values
        for the FlowActionCall metadata type.

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

- 
- 
- 
- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values for Advanced Approvals are: `cancelApprovalSubmission`—Cancels an approval submission and all child approval work items that haven't been completed. You can also add comments about why the approval admin made the cancellation. Added in API version 62.0 and later. `overrideApprovalWorkItem`—Update an approval work item status with the approval admin decision and any comments that the approval admin added. Added in API version 62.0 and later. `reassignApprovalWorkItem`—Reassign an approval work item that hasn't been completed. You can also add comments about why the approval admin reassigned the approval work item. Added in API version 62.0 and later. `recallApprovalSubmission`—Recall an approval submission that isn't completed. You can also add comments that the submitter or approval admin made the recall. Added in API version 62.0 and later. `reviewApprovalWorkItem`—Update an approval work item status with the assignee or reviewer's decision and any comments that the assignee or reviewer added. Added in API version 62.0 and later. `getPreviousRelaRecDetails`—Get the related record details submitted for approval before the current approval submission. The details are required for approval steps that use custom logic for auto-approvals. Added in API version 66.0 and later. |

/

=== ARTICLE: advanced_approvals_invocable_actions_parent.htm ===
---
page_id: advanced_approvals_invocable_actions_parent.htm
title: Advanced Approvals Standard Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_invocable_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals Standard Invocable Actions

Learn more about the standard invocable actions available with Advanced
    Approvals.

- 
**[Cancel Approval Submission Action](./actions_obj_cancel_approval_submission.htm.md)**  

Cancels an approval submission and all child approval work items             that haven't been completed. You can also add comments about why the approval admin made             the cancellation.

- 
**[Get Previous Related Record Details Action](./actions_obj_get_previous_rela_rec_details.htm.md)**  

Get the related record details submitted for approval before the             current approval submission. The details are required for approval steps that use custom             logic for auto-approvals.

- 
**[Override Approval Work Item Action](./actions_obj_override_approval_work_item.htm.md)**  

Update an approval work item status with the approval admin decision             and any comments that the approval admin added.

- 
**[Reassign Approval Work Item Action](./actions_obj_reassign_approval_work_item.htm.md)**  

Reassign an approval work item that hasn't been completed. You can             also add comments about why the approval admin reassigned the approval work         item.

- 
**[Recall Approval Submission Action](./actions_obj_recall_approval_submission.htm.md)**  

Recall an approval submission that isn't completed. You can also add             comments that the submitter or approval admin made the recall.

- 
**[Review Approval Work Item Action](./actions_obj_review_approval_work_item.htm.md)**  

Update an approval work item status with the assignee or reviewer's             decision and any comments that the assignee or reviewer added.

#### See Also

- [*Actions Developer Guide*: Overview](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro_overview.htm)

- [*REST API Developer Guide*: Invocable Actions Standard](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)

=== ARTICLE: advanced_approvals_metadata_api_parent.htm ===
---
page_id: advanced_approvals_metadata_api_parent.htm
title: Advanced Approvals Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

- 
**[Flow for Advanced Approvals](./advanced_approvals_flow_metadata_api.htm.md)**  

The flow for Advanced Approvals represents the metadata associated with a flow. With     Flow, you can create an application that takes users through a series of pages to query and     update the records in the database. You can also run logic and provide branching capability     based on user input to build dynamic applications.

#### See Also

- [*Metadata API Developer Guide*: Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_intro.htm)

=== ARTICLE: advanced_approvals_overview.htm ===
---
page_id: advanced_approvals_overview.htm
title: Advanced Approvals
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/advanced_approvals_overview.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Advanced Approvals

Advanced Approvals feature provides invocable actions to streamline complex business
  processes. These actions automate and manage intricate parallel or sequential approval chains with
  detailed audit trails.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: **Enterprise**, **Unlimited**, and **Developer** Editions of Revenue Management where Advanced Approvals is enabled |

  

 

- 
**[Advanced Approvals Fields on Standard Objects](./advanced_approval_fields_on_standard_objects.htm.md)**  

Advanced Approvals adds standard and custom fields to some standard Salesforce objects.     These fields are available only in Revenue Management orgs where Advanced Approvals is     enabled.

- 
**[Advanced Approvals Standard Invocable Actions](./advanced_approvals_invocable_actions_parent.htm.md)**  

Learn more about the standard invocable actions available with Advanced     Approvals.

- 
**[Advanced Approvals Business APIs](./advanced_approvals_business_apis.htm.md)**  

Use the Advanced Approvals Business APIs to preview approval levels and related     details before you submit a record for approval.

- 
**[Advanced Approvals Metadata API Types](./advanced_approvals_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

#### See Also

- [*Salesforce Help*: Advanced Approvals](https://help.salesforce.com/s/articleView?id=ind.approvals_advanced_approvals.htm&language=en_US)

=== ARTICLE: connect_requests_preview_approval_input.htm ===
---
page_id: connect_requests_preview_approval_input.htm
title: Preview Approval Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_requests_preview_approval_input.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_api_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval Input

Input representation of the details of the request to preview an approval.

**JSON example**

: 

```
{
  "flowApiName": "QuoteApprovals",
  "objectApiName": "Quote",
  "recordId": "0Q0DU0000005HZC0A2",
  "inputParameters": {
    "approverComments": "Submitted for approval",
    "requestType": "Standard"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `flowApiName` | String | API name of the auto-launched flow. | Required | 65.0 |
| `objectApiName` | String | API name of the object to preview the approvals for. | Required | 65.0 |
| `recordId` | String | ID of the record to preview the approvals for. | Required | 65.0 |
| `inputParameters` | Map<String, Object> | List of input parameters to preview. | Optional | 67.0 |

=== ARTICLE: connect_resources_preview_approvals.htm ===
---
page_id: connect_resources_preview_approvals.htm
title: Preview Approval (POST)
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_preview_approvals.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_business_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval (POST)

Preview the approval levels of a record and associated level details,
      approval chains, approvers, and conditions before you submit the record for an
    approval.

    

For example, a sales rep working on a quote can preview the approval levels for a
        quote before submitting the quote for approval.

        
          

**Resource**

          
: 
            

```
/connect/advanced-approvals/approval-submission/preview
```

          

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v68.0/connect/advanced-approvals/approval-submission/preview
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
  "flowApiName": "QuoteApprovals",
  "objectApiName": "Quote",
  "recordId": "0Q0DU0000005HZC0A2",
  "inputParameters": {
    "approverComments": "Submitted for approval",
    "requestType": "Standard"
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `flowApiName` | String | API name of the auto-launched flow. | Required | 65.0 |
| `objectApiName` | String | API name of the object to preview the approvals for. | Required | 65.0 |
| `recordId` | String | ID of the record to preview the approvals for. | Required | 65.0 |
| `inputParameters` | Map<String, Object> | List of input parameters to preview. | Optional | 67.0 |

          

        
        
          

**Response body for POST**

          
: [Preview
              Approval](./connect_responses_preview_approval_output.htm.md)

=== ARTICLE: connect_responses_preview_approval_chain_item_output.htm ===
---
page_id: connect_responses_preview_approval_chain_item_output.htm
title: Preview Approval Chain Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_preview_approval_chain_item_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval Chain Item

Output representation of the details of an approval chain item for a specific
    group.

        
          

**JSON example**

          
: 
            

```
{
  "approvalChainItems": [
    {
      "approvalChainName": "FINANCE",
      "approvalItems": [
        {
          "stepApiName": "CPIFC",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "005XX000001ABCQYA4",
          "assigneeType": "User",
          "assigneeDetails": {
            "id": "005XX000001ABCQYA4",
            "name": "Sam Smith",
            "type": "User",
            "apiName": "",
            "email": "sam.smith@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "Approved",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [],
          "parents": [],
          "level": 1,
          "additionalFields": {
            "reviewedBy": "005CVxhW4MBIUbPYUX",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        },
        {
          "stepApiName": "CPIFC2",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "00GXX000001XYZA2A4",
          "assigneeType": "Group",
          "assigneeDetails": {
            "id": "00GXX000001XYZA2A4",
            "name": "Admin Group",
            "type": "Group",
            "apiName": "Admin_Group",
            "email": "admin.group@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "In Progress",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [
            "CPIFC"
          ],
          "parents": [
            "CPIFC"
          ],
          "level": 2,
          "additionalFields": {
            "reviewedBy": "00GvUUtUVGmTDUHU34",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        }
      ]
    }
  ],
  "flowOrchestrationDefinitionVersionId": "0jEDU0000001nZm",
  "status": "Success"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `approvalChain​Name` | String | Name of the approval chain. | Small, 65.0 | 65.0 |
| `approval​Items` | [Preview Approval Item](./connect_responses_preview_approval_item_output.htm.md)[] | Details of the approval items. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_preview_approval_error.htm ===
---
page_id: connect_responses_preview_approval_error.htm
title: Preview Approval Error
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_preview_approval_error.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval Error

Output representation of the error details associated with the Preview Approval
    API.

        
          

**JSON example**

          
: This example shows a sample error
            scenario.

```
{
  "approvalChainItems": [],
  "error": {
    "correlationId": "0Q0DU0000005HZC0A2",
    "errorCode": "[xmlrpc=-1, statusCode=INVALID_API_INPUT, exceptionCode=null, scope=PublicApi, http=400]",
    "errorMessage": "Looks like the flow associated with this approval workflow for the current record isn't active. Activate the flow and try again.",
    "source": "PreviewApprovalDataProcessingException"
  },
  "status": "Failure"
}
```

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `correlationId` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 65.0 | 65.0 |
| `errorCode` | String | Code for the resultant error. | Small, 65.0 | 65.0 |
| `errorMessage` | String | Error message for the resultant error. | Small, 65.0 | 65.0 |
| `source` | String | Details about the source of the error. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_preview_approval_item_output.htm ===
---
page_id: connect_responses_preview_approval_item_output.htm
title: Preview Approval Item
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_preview_approval_item_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval Item

Output representation of the details of a specific approval item with an approval
    chain.

      
        
          

**JSON example**

          
: 
            

```
{
  "approvalChainItems": [
    {
      "approvalChainName": "FINANCE",
      "approvalItems": [
        {
          "stepApiName": "CPIFC",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "005XX000001ABCQYA4",
          "assigneeType": "User",
          "assigneeDetails": {
            "id": "005XX000001ABCQYA4",
            "name": "Sam Smith",
            "type": "User",
            "apiName": "",
            "email": "sam.smith@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "Approved",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [],
          "parents": [],
          "level": 1,
          "additionalFields": {
            "reviewedBy": "005CVxhW4MBIUbPYUX",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        },
        {
          "stepApiName": "CPIFC2",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "00GXX000001XYZA2A4",
          "assigneeType": "Group",
          "assigneeDetails": {
            "id": "00GXX000001XYZA2A4",
            "name": "Admin Group",
            "type": "Group",
            "apiName": "Admin_Group",
            "email": "admin.group@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "In Progress",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [
            "CPIFC"
          ],
          "parents": [
            "CPIFC"
          ],
          "level": 2,
          "additionalFields": {
            "reviewedBy": "00GvUUtUVGmTDUHU34",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        }
      ]
    }
  ],
  "flowOrchestrationDefinitionVersionId": "0jEDU0000001nZm",
  "status": "Success"
}
```

          

        
      

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additional​Fields` | Map<String, String> | Details of any additional fields in the approval workflow. | Small, 65.0 | 65.0 |
| `approval​ConditionName` | String | Details of the configured conditions in the approval workflow. | Small, 65.0 | 65.0 |
| `assignedTo` | String | Name of the assignee that the approval request is assigned to. | Small, 65.0 | 65.0 |
| `assigneeType` | String | Type of assignee. | Small, 65.0 | 65.0 |
| `assigneeDetails` | Map<String, Object> | Includes the details of an assignee, such as ID, name, type, API name, and email. | Small, 65.0 | 65.0 |
| `dependencies` | String[] | Specifies dependencies among approval steps, which are entry conditions based on the status of a previous step within the same stage. | Small, 65.0 | 65.0 |
| `level` | Integer | Hierarchy level of the approval item. | Small, 65.0 | 65.0 |
| `object​ApiName` | String | API name of the object to preview the approval for. | Small, 65.0 | 65.0 |
| `objectId` | String | ID of the object to preview the approval for. | Small, 65.0 | 65.0 |
| `parents` | String[] | Details of the parent step. | Small, 65.0 | 65.0 |
| `stage` | Map<String, String> | Includes the API name and label. | Small, 65.0 | 65.0 |
| `status` | String | Status of the approval request. | Small, 65.0 | 65.0 |
| `stepApi​Name` | String | API name of the step. | Small, 65.0 | 65.0 |

=== ARTICLE: connect_responses_preview_approval_output.htm ===
---
page_id: connect_responses_preview_approval_output.htm
title: Preview Approval
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_responses_preview_approval_output.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approvals_api_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Preview Approval

Output representation of the details of a preview approval request.

        
          

**JSON example**

          
: 
            

```
{
  "approvalChainItems": [
    {
      "approvalChainName": "FINANCE",
      "approvalItems": [
        {
          "stepApiName": "CPIFC",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "005XX000001ABCQYA4",
          "assigneeType": "User",
          "assigneeDetails": {
            "id": "005XX000001ABCQYA4",
            "name": "Sam Smith",
            "type": "User",
            "apiName": "",
            "email": "sam.smith@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "Approved",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [],
          "parents": [],
          "level": 1,
          "additionalFields": {
            "reviewedBy": "005CVxhW4MBIUbPYUX",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        },
        {
          "stepApiName": "CPIFC2",
          "approvalConditionName": "Payment Term Greater Than 90 Days",
          "assignedTo": "00GXX000001XYZA2A4",
          "assigneeType": "Group",
          "assigneeDetails": {
            "id": "00GXX000001XYZA2A4",
            "name": "Admin Group",
            "type": "Group",
            "apiName": "Admin_Group",
            "email": "admin.group@example.com"
          },
          "objectId": "0Q0bsOgSBEhlexWC3Q",
          "objectApiName": "Quote",
          "status": "In Progress",
          "stage": {
            "apiName": "stage101",
            "label": "Stage 101"
          },
          "dependencies": [
            "CPIFC"
          ],
          "parents": [
            "CPIFC"
          ],
          "level": 2,
          "additionalFields": {
            "reviewedBy": "00GvUUtUVGmTDUHU34",
            "isEligibleForSmartApproval": true,
            "smartApprovalBasisWI": "000000000000000",
            "isAutoReviewed": false
          }
        }
      ]
    }
  ],
  "flowOrchestrationDefinitionVersionId": "0jEDU0000001nZm",
  "status": "Success"
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `approvalChain​Items` | [Preview Approval Chain Item](./connect_responses_preview_approval_chain_item_output.htm.md)[] | Details of the approval items of an approval chain. | Small, 65.0 | 65.0 |
| `correlation​Id` | String | Unique token to track and associate related events or transactions across different components of the application. If unspecified, a Universally Unique Identifier (UUID) is generated. | Small, 65.0 | 65.0 |
| `error` | [Preview Approval Error](./connect_responses_preview_approval_error.htm.md)[] | Details of the error encountered during the processing of the API request. | Small, 65.0 | 65.0 |
| `flowOrchestration​DefinitionVersion​Id` | String | ID of the flow orchestration definition version. | Small, 65.0 | 65.0 |
| `status` | String | Status of the API request. | Small, 65.0 | 65.0 |

=== ARTICLE: sforce_api_objects_approvalsubmission.htm ===
---
page_id: sforce_api_objects_approvalsubmission.htm
title: ApprovalSubmission
source_url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_approvalsubmission.htm
release: 264
release_name: Winter '27
deliverable: revenue_lifecycle_management_dev_guide
section: Advanced Approvals
parent_page: advanced_approval_fields_on_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ApprovalSubmission

      Represents the instance of an approval request that's submitted for a record
         of the related object. This object is available in API version 62.0 and
      later.

      

## Supported Calls

      
      

         `describeLayout()`, 
         `describeSObjects()`, 
         `getDeleted()`,
         `getUpdated()`,
         `query()`, 
         `retrieve()`
      

      

      

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

                  

            

            
| Field | Details |
| --- | --- |
| Comments | **Type** textarea **Properties** Nillable **Description** The comments about the request that's submitted for approval. |
| DoesSendApprovalEmail | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. Indicates whether approval request emails are sent to approvers and delegates (`true`) or not (`false`). The default value is `false`. |
| FlowOrchestrationInstanceId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the flow orchestration instance record that's associated with the approval. This field is a relationship field. **Relationship Name** FlowOrchestrationInstance **Refers To** FlowOrchestrationInstance |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The auto-generated name for the approval submission. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the user or the group that owns the approval submission record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RelatedRecordId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** Required. The ID of the related record that's submitted for approval. This field is a polymorphic relationship field. **Relationship Name** RelatedRecord **Refers To** Account, AdAvailabilityViewConfig, Address, AnalyticsUserAttrFuncTkn, ApprovalSubmission, ApprovalSubmissionDetail, ApprovalWorkItem, Asset, AssetAction, AssetActionSource, AssetContractRelationship, AssetRateAdjustment, AssetRateCardEntry, AssetRelationship, AssetStatePeriod, AssociatedLocation, AsyncOperationTracker, AttrPicklistExcludedValue, AttributeAdjustmentCondition, AttributeBasedAdjRule, AttributeBasedAdjustment, AttributeCategory, AttributeCategoryAttribute, AttributeDefinition, AttributePicklist, AttributePicklistValue, AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse, AuthorizationFormText, BatchJob, BatchJobPart, BatchJobPartFailedRecord, BundleBasedAdjustment, BusinessBrand, Case, CaseComment, ChannelProgram, ChannelProgramLevel, ChannelProgramMember, CollaborationGroup, CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming, Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone, ContactPointTypeConsent, ContactRequest, ContextDefinitionSync, Contract, ContractItemPrice, ContractItemPriceAdjTier, CostBook, CostBookEntry, Customer, DTRecordsetReplica, DataUseLegalBasis, DataUsePurpose, DecisionTblFileImportData, DelegatedAccount, DocGenerationQueryResult, DocTemplateSectionCondition, DocumentEnvelope, DocumentGenerationProcess, DocumentRecipient, DocumentTemplate, DocumentTemplateContentDoc, DocumentTemplateSection, DocumentTemplateToken, DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType, ExpressionSetConstraintObj, ExternalEventMapping, FlowOrchestrationInstance, FulfillmentOrder, FulfillmentOrderItemAdjustment, FulfillmentOrderItemTax, FulfillmentOrderLineItem, GeneratedDocument, GeneratedDocumentSection, Idea, Image, Individual, IntegrationProviderDcsnRqmt, IntegrationProviderExecution, Lead, Location, LocationTrustMeasure, ManagedContentVariant, ObjectStateDefinition, ObjectStateTransition, ObjectStateValue, Obligation, Opportunity, OpportunityRelatedDeleteLog, Order, OrderAction, OrderAdjustmentGroup, OrderDeliveryGroup, OrderDeliveryMethod, OrderItem, OrderItemAdjustmentLineItem, OrderItemDetail, OrderItemRateAdjustment, OrderItemRateCardEntry, OrderItemRecipient, OrderItemRelationship, OrderItemTaxLineItem, OrgMetricScanResult, OrgMetricScanSummary, Organization, PartnerFundAllocation, PartnerFundClaim, PartnerFundRequest, PartnerMarketingBudget, PartyConsent, PriceBookEntryDerivedPrice, PriceBookRateCard, PricingAdjBatchJob, PricingAdjBatchJobLog, PricingApiExecution, PricingProcessExecution, ProcessException, Product2, ProductAttributeDefinition, ProductCatalog, ProductCategory, ProductCategoryDisqual, ProductCategoryProduct, ProductCategoryQualification, ProductClassification, ProductClassificationAttr, ProductComponentGroup, ProductComponentGrpOverride, ProductConfigFlowAssignment, ProductConfigurationFlow, ProductConfigurationRule, ProductDisqualification, ProductPriceHistoryLog, ProductPriceRange, ProductQualification, ProductRampSegment, ProductRelComponentOverride, ProductUsageGrant, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction, PromptError, QuickText, QuickTextUsage, Quote, QuoteLineDetail, QuoteLineItem, QuoteLineItemRecipient, QuoteLineRateAdjustment, QuoteLineRateCardEntry, RateAdjustmentByAttribute, RateAdjustmentByTier, RateCard, RateCardEntry, RatingFrequencyPolicy, SalesTransactionType, Seller, Shipment, ShipmentItem, Site, SocialPersona, SocialPost, Solution, StreamingChannel, TableauHostMapping, Topic, UnitOfMeasure, UnitOfMeasureClass, UsageGrantRenewalPolicy, UsageGrantRolloverPolicy, UsageResource, UsageResourceBillingPolicy, User, UserEsignVendorIdentifier, UserLicense, UserLocalWebServerIdentity, UserProvisioningRequest, WorkBadge, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkThanks |
| RelatedRecordObjectName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Required. The type of record that was submitted for approval. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The status of the approval. Valid values are: `Approved` `Canceled` `Errored` `InProgress` `Recalled` `Rejected` `Suspended` |
| SubmittedById | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** Required. The ID of the user who submitted the record for approval. This field is a relationship field. **Relationship Name** SubmittedBy **Refers To** User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[ApprovalSubmissionOwnerSharingRule](./sforce_api_associated_objects_ownersharingrule.htm.md)**

               
: Sharing rules are available for the object.

            
            
               

**[ApprovalSubmissionShare](./sforce_api_associated_objects_share.htm.md)**

               
: Sharing is available for the object.

