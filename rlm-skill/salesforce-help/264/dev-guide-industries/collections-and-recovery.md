# Industries Common Resources Developer Guide 264 — sección: Collections and Recovery (8 artículos)

=== ARTICLE: collections_data_model.htm ===
---
page_id: collections_data_model.htm
title: Collections and Recovery Data Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/collections_data_model.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Collections and Recovery Data Model

Learn about the objects and relationships used for Collections and Recovery.

  

    
     
      

     

    

   
| Available in: Lightning Experience. [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.collections_editions_permissions.htm&language=en_US) |
| --- |

  

  
   
  

  

To view a larger version, right-click or Ctrl+click the image and select **Open Image
    in New Tab**.

=== ARTICLE: collections_objects.htm ===
---
page_id: collections_objects.htm
title: Collections and Recovery
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/collections_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Collections and Recovery

Use Collections data model to streamline the collection process. Create prioritized lists
                of collection plans. Create and manage promise to pay agreements for better
                management of overdue amounts.

- 
**[Collections and Recovery Data Model](./collections_data_model.htm.md)**  

Learn about the objects and relationships used for Collections and Recovery.

- 
**[Standard Objects](./collections_standard_objects.htm.md)**  

Use Collections standard objects and associated fields to create collection plan and         related records.

=== ARTICLE: collections_standard_objects.htm ===
---
page_id: collections_standard_objects.htm
title: Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/collections_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Standard Objects

Use Collections standard objects and associated fields to create collection plan and
        related records.

- 
**[CollectionPlan](./sforce_api_objects_collectionplan.htm.md)**  

       Represents details about the outstanding amounts linked to financial          accounts, billing accounts, contacts, accounts, or cases associated with individuals or an          organization. This object is available in API version 63.0 and later.

- 
**[CollectionPlanItem](./sforce_api_objects_collectionplanitem.htm.md)**  

       Represents an instance of a collection plan. This object is available in       API version 63.0 and later.

- 
**[CollectionPlanReason](./sforce_api_objects_collectionplanreason.htm.md)**  

       Represents the reason for initiating the collection process, including          non-payment of bills, bankruptcy, outstanding invoices, and deceased account holders.       This object is available in API version 63.0 and later.

- 
**[CaseProceeding](./sforce_api_objects_caseproceeding.htm.md)**  

       Represents a legal and formal demand for the enforcement of an individual’s          rights against another party in a court of justice. This object is available in API       version 64.0 and later.

- 
**[CaseProceedingParticipant](./sforce_api_objects_caseproceedingparticipant.htm.md)**  

       Represents a junction between the case proceeding and a participant, such as          an account or a contact. This object stores the details of a participant who is involved in          a case proceeding. This object is available in API version       64.0       and later.

=== ARTICLE: sforce_api_objects_caseproceeding.htm ===
---
page_id: sforce_api_objects_caseproceeding.htm
title: CaseProceeding
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_caseproceeding.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CaseProceeding

      Represents a legal and formal demand for the enforcement of an individual’s
         rights against another party in a court of justice. This object is available in API
      version 64.0 and later.

      

## Special Access Rules

This is a standard
            object and is available with Collections and Recovery permission set in API version 64.0
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

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

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
- 
- 
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| AddressId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Address of the location where the case proceeding is being conducted. This field is a relationship field. **Relationship Name** Address **Relationship Type** Lookup **Refers To** Address |
| ApplicationId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The relationship between case proceeding and a business license application or an individual application. This field is a polymorphic relationship field. **Relationship Name** Application **Relationship Type** Lookup **Refers To** BusinessLicenseApplication, IndividualApplication |
| CaseFilingDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The data and time when the case proceeding was initiated. |
| CaseId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The case associated with the case proceeding record. This field is a relationship field. **Relationship Name** Case **Relationship Type** Lookup **Refers To** Case |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** The description of the case proceeding record. |
| EndDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the case proceeding was completed. |
| ExternalCaseIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier of the related case in an external system. |
| ExternalIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier for this case proceeding. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the case proceeding record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the case proceeding record owner. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| RelatedCaseProceedingId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of a case proceeding related to this case proceeding. This field is a relationship field. **Relationship Name** RelatedCaseProceeding **Relationship Type** Lookup **Refers To** CaseProceeding |
| StartDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time from when the case proceeding began. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the status of the case proceeding. Possible values are: `Completed` `Planned` |
| SubType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The subtype of the case proceeding. Possible values are: `Appeal` `Disposition` `Review Hearing` |
| TotalLegalExpenses | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** Total legal proceeding expenses for the case associated with a collection plan. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Sort, Update **Description** The type of case proceeding. Possible values are: `Board Proceeding` `Court Action` `Mediation` `Warrant Request` |

      

      

## Associated Objects

         
            

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise, they’re available in the specified API version and later.

            
            
            
               

**[CaseProceedingFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[CaseProceedingHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[CaseProceedingOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**
[CaseProceedingShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)
               **

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_caseproceedingparticipant.htm ===
---
page_id: sforce_api_objects_caseproceedingparticipant.htm
title: CaseProceedingParticipant
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_caseproceedingparticipant.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CaseProceedingParticipant

      Represents a junction between the case proceeding and a participant, such as
         an account or a contact. This object stores the details of a participant who is involved in
         a case proceeding. This object is available in API version
      64.0
      and later. 

      

         

#### Note

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

         

When Compliant Data Sharing is enabled for the Case Proceeding object, a case proceeding
            participant represents information about a user or group of participants who have access
            to a case proceeding.

      

      

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
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| CaseProceedingId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The case proceeding associated with the case proceeding participant record. This field is a relationship field. **Relationship Name** CaseProceeding **Relationship Type** Master-detail **Refers To** CaseProceeding (the master object) |
| Comments | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The comments about why the participant has access to the case proceeding. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Specifies whether the participant's association with the case proceeding is active (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferencedDate is not null, the user accessed this record or list view indirectly. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the case proceeding participant record. |
| ParticipantId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The participant associated with the case proceeding record. This field is a polymorphic relationship field. **Relationship Name** Participant **Relationship Type** Lookup **Refers To** Account, Contact, Group, User |
| ParticipantRoleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The participant role associated with the case proceeding participant record. This field is a relationship field. **Relationship Name** ParticipantRole **Refers To** ParticipantRole |
| ParticipationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The actual type of presence of the participant during the case proceeding. Possible values are: `Absent` `Present In Person` `Virtual` |
| Role | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The role of the participant associated with the case proceeding record. Possible values are: `Attorney` `Defendant` `Judge` `Perpetrator` `Plaintiff` `Victim` `Witness` |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the status of the participant in the case proceeding. Possible values are: `Active` `Inactive` |

      

      

## Associated Objects

         
            

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise, they’re available in the specified API version and later.

            
            
            
               

**[CaseProceedingParticipantFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[CaseProceedingParticipantHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_collectionplan.htm ===
---
page_id: sforce_api_objects_collectionplan.htm
title: CollectionPlan
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_collectionplan.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CollectionPlan

      Represents details about the outstanding amounts linked to financial
         accounts, billing accounts, contacts, accounts, or cases associated with individuals or an
         organization. This object is available in API version 63.0 and later.

      

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 
: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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
- 
- 
- 

                  

               

            
| Field | Details |
| --- | --- |
| AccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The account associated with the collection plan record. This field is a relationship field. **Relationship Name** Account **Refers To** Account |
| AutoDebitRequestCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The count of the auto debit requests initiated for a collection plan. |
| ClosedDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date when the collection plan was closed. |
| CollectionAgencyAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The account of the recovery agency, which may be a third-party agency, responsible for managing the collection activities associated with this collection plan. Available in API version 65.0 and later. This field is a relationship field. **Relationship Name** CollectionAgencyAccount **Refers To** Account |
| CollectionPlanReasonId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of collection plan reason associated with the collection plan. This field is a relationship field. **Relationship Name** CollectionPlanReason **Refers To** CollectionPlanReason |
| CollectionPlanSegment | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies a predefined group associated with the collection plan record. The group is derived based on various criteria, such as collection amount and days past due. |
| ContactId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The contact associated with the collection plan record. This field is a relationship field. **Relationship Name** Contact **Refers To** Contact |
| CurrentDueAmount | **Type** currency **Properties** Create, Filter, Sort, Update **Description** The current outstanding amount for the collection plan. |
| DaysPastDue | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of days that a payment is past its scheduled or expected due date. |
| DueDate | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The date by which the organization or individuals are expected to make a payment towards the outstanding amount. |
| FirstCallDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The timestamp when the first phone call is made to notify an individual or organization about the repayment of funds. |
| FirstEmailDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The timestamp when the first email is sent to notify an individual or organization about the repayment of funds. |
| FirstSmsDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The timestamp when the first message is sent to notify an individual or organization about the due amount. |
| FinancialAccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The financial account associated with the collection plan record. This field is a relationship field. **Relationship Name** FinancialAccount **Refers To** FinancialAccount |
| InitialDueAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The initial due amount of the collection plan. |
| InteractionOutcome | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the result of the collections specialist's interaction with a customer, such as promised to pay, escalated to recovery, legal case created, no commitment, or bankruptcy. Available in API version 64.0 and later. |
| IsClosed | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if the collection plan is active (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and LastReferencedDate is not null, the user accessed this record or list view indirectly. |
| LegalRepresentativeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The contact details of the borrower's legal representative or attorney. Available in API version 64.0 and later. This field is a relationship field. **Relationship Name** LegalRepresentative **Refers To** Contact |
| MaximumPromisetoPayCount | **Type** int **Properties** Create, Defaulted on create, Filter, Group, Nillable, Sort, Update **Description** The maximum number of promises to pay allowed for a collection plan. Available in API version 64.0 and later. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the collection plan record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the collection plan record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PromiseToPayCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of commitments made by an individual or an organization to repay the amount they owe within a specified timeframe. |
| RiskScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The numerical score that is computed based on the Einstein model. This score is used to assess an individual's repayment capacity. |
| SourceSystemRecordIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The unique identifier of the collection plan in an external system. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the status of the collection plan, such as new, in progress, promise to pay registered, promise to pay broken, and closed. Possible values are: `Close` `InProgress` `New` |
| TotalFeesAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The sum of any fee amount associated with the collection plan. It includes any applicable surcharges, processing fees, penalties, and any other additional charges incurred. |
| TotalInterestAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The cumulative sum of all interest charges accrued over a specified time period. |
| TotalPaymentsReceived | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** Total amount of payments received that are associated with a collection plan. Available in API version 63.0 and later. |
| TotalTaxAmount | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The total tax amount of the collection plan. |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Name of the cloud or the function that uses the Collections feature. Possible values are: `Automotive` `Billing` `Financial Services Cloud` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CollectionPlanChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
            
               

**[CollectionPlanHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[CollectionPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[CollectionPlanShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_collectionplanitem.htm ===
---
page_id: sforce_api_objects_collectionplanitem.htm
title: CollectionPlanItem
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_collectionplanitem.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CollectionPlanItem

      Represents an instance of a collection plan. This object is available in
      API version 63.0 and later.

      

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
- 

                  

               

            
| Field | Details |
| --- | --- |
| CollectionPlanId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the parent collection plan associated with the collection plan item record. This field is a relationship field. **Relationship Name** CollectionPlan **Relationship Type** Master-detail **Refers To** CollectionPlan (the master object) |
| FinancialAccountStatementId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Financial account statement associated with the collection plan item record. This field is a relationship field. **Relationship Name** FinancialAccountStatement **Refers To** FinancialAccountStatement |
| Invoice | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The invoice associated with the collection plan item record. This field is a relationship field. **Relationship Name** Invoice **Refers To** Invoice |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and <parmname>LastReferenceDate</parmname> is not null, the user accessed this record or list view indirectly. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the collection plan item record. |
| SourceSystemRecordIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The unique identifier of the collection plan item in an external system. |
| Status | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the status of the collection plan item, such as new, pending, paid, and closed. Possible values are: `New` Paid `Pending` `Closed` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[CollectionPlanItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
            
            
               

**[CollectionPlanItemHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_collectionplanreason.htm ===
---
page_id: sforce_api_objects_collectionplanreason.htm
title: CollectionPlanReason
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_collectionplanreason.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Collections and Recovery
parent_page: collections_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# CollectionPlanReason

      Represents the reason for initiating the collection process, including
         non-payment of bills, bankruptcy, outstanding invoices, and deceased account holders.
      This object is available in API version 63.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| Code | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** A unique code that represents the collection plan reason. |
| Description | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** A description of the reason for initiating the collection. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates if the collection plan reason is active (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record indirectly, for example, through a list view or related record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, and <parmname>LastReferenceDate</parmname> is not null, the user accessed this record or list view indirectly. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The reason for initiating the collection. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the owner of the collection plan reason record. This field is a relationship field. **Relationship Name** Owner **Refers To** User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
            
               

**[CollectionPlanReasonChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
            
               

**[CollectionPlanReasonHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[CollectionPlanReasonOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[CollectionPlanReasonShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

