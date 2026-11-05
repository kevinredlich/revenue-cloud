# Industries Common Resources Developer Guide 264 — sección: Data Processing Engine, Batch Management, and Monitor Workflow Services (37 artículos)

=== ARTICLE: actions_obj_submit_failed_records_batchjob.htm ===
---
page_id: actions_obj_submit_failed_records_batchjob.htm
title: Submit Failed Records Batch Job
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_submit_failed_records_batchjob.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_mgt_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Submit Failed Records Batch Job

Run to resubmit an existing batch job with failed records for
   processing. This action executes the batch job asynchronously.

  
   

This object is available in API version 52.0 and later.

  

  

## Special Access Rules

To know the products and user permissions needed to
    access this action, See [Supported Editions and Permissions for Batch
    Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

  

## Supported REST HTTP Methods

   
   
    
     

**URI**

     
: ``/services/data/vXX.X/`actions/standard/submitFailedRecordsBatchJob`

    
    
     

**Formats**

     
: JSON

    
    
     

**HTTP Methods**

     
: GET, POST

    
    
     

**Authentication**

     
: `Authorization: Bearer token`

    
   

  

  

## Inputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

      
       

       

: 

: 

      

     

    
| Input | Details |
| --- | --- |
| failedRecordIds | **Type** array **Description** The IDs of failed records in a batch job. |
| parentBatchJobId | **Type** string **Description** Required. The ID of a batch job with failed records. |

  

  

## Outputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

      
       

       

: 

: 

      

     

    
| Output | Details |
| --- | --- |
| batchJobId | **Type** string **Description** The ID of a batch job generated after the request is successful. This batch job ID is used to track the progress of the batch job in Monitor Workflow Services in the org. |
| status | **Type** string **Description** Indicates whether a batch job succeeded or failed. |

  

  

## Usage

   
   

**JSON Sample Request**

   
    

```
{
   "inputs": [{
      "parentBatchJobId": "0mdRM0000004DXrYAM",
      "failedRecordIds": [
         "001RM000005AG0bYAG", "001RM000005AERZYA4", "001RM000005AG0WYAW"
      ]
   }]
}
```

   

   

**JSON Sample Response**

   

```
[ {
   "actionName" : "submitFailedRecordsBatchJob",
   "errors" : null,
   "isSuccess" : true,
   "outputValues" : {
      "batchJobId" : "0mdRM0000004DZ9YAM"
   }
} ]
```

=== ARTICLE: batch.htm ===
---
page_id: batch.htm
title: Data Processing Engine, Batch Management, and Monitor Workflow Services
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine, Batch Management, and Monitor Workflow Services

Data Processing Engine and Batch Management help automate your business processes. Use
  objects, APIs, Platform Events, and invocable actions to define, run, and review Data Processing
  Engine definitions and Batch Management jobs.

  

    
     
      

     

     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability for Data Processing Engine.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |
| Available in: [View product and edition availability for Batch Management.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

  

Here's how both these features can automate your business processes:

  
   
- Data Processing Engine: Transform data that's available in your Salesforce org and write back
    the transformation results as new or updated records. You can transform the data for standard
    and custom objects.

   
- Batch Management: Automate the processing of records in scheduled flows. You can process a
    high volume of standard and custom object records.

  

  

Once a Data Processing Engine definition is run or a Batch Management job is run, you can view
   the progress of the run and the results of the run using Monitor Workflow Services.

 

- 
**[Data Model](./batch_data_model.htm.md)**  

Data    Processing Engine, Batch Management, and Monitor Workflow Servics share a data model. Let's learn    about the objects and relationships in this shared data model.

- 
**[Common Tooling API Object](./batch_common_setup_objects.htm.md)**  

BatchJobDefinition is a common Tooling API object that is shared between Data       Processing Engine and Batch Management.

- 
**[Common Platform Event](./batch_management_platform_event.htm.md)**  

Batch Management jobs and Data Processing Engine definitions are run using invocable    actions in Flows. Use the BatchJobStatusChanged event to notify subscribers after a Batch    Management job or a Data Processing Engine definition is processed in a flow.

- 
**[Common Business APIs](./batch_management_apis.htm.md)**  

Common Business APIs are RESTful APIs that are sometimes available as Apex classes and     methods.

- 
**[Data Processing Engine](./data_processing_engine_dev_overview.htm.md)**  

Transform data that's available in your Salesforce org and write back the transformation   results as new or updated records. You can transform the data for standard and custom objects.   Data Processing Engine consists of a Tooling API object, a standard object, a Metadata API, and an   invocable action. You can use these to view, create, edit, and run Data Processing Engine   definitions.

- 
**[Batch Management](./batch_management_dev_overview.htm.md)**  

Automate the processing of records in scheduled flows. You can process a high volume of   standard and custom object records. Batch Management consists of three Tooling API objects, a   standard object, a Metadata API, and an invocable action. You can use these resources to view,   create, edit, and run Batch Management jobs.

- 
**[Monitor Workflow Services](./monitor_workflow_services_dev_overview.htm.md)**  

The Monitor Workflow Services standard objects can be used to track the run of Data   Processing Engine definitions and Batch Management jobs. During a run, you can view details about   each part that the run is broken down into. After the run is complete, you can view its status and   the records which weren't processed during the run.

=== ARTICLE: batch_common_setup_objects.htm ===
---
page_id: batch_common_setup_objects.htm
title: Common Tooling API Object
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_common_setup_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Common Tooling API Object

BatchJobDefinition is a common Tooling API object that is shared between Data
      Processing Engine and Batch Management.

  

    
     
      

     

     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability for Data Processing Engine.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |
| Available in: [View product and edition availability for Batch Management.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

  

Tooling API objects let you interact with metadata for declarative development. For example,
   you can create your own version of Setup.

 

- 
**[BatchJobDefinition](./tooling_api_objects_batchjobdefinition.htm.md)**  

     Represents the definition of a batch job. This object is available in API     version 51.0 and later.

=== ARTICLE: batch_data_model.htm ===
---
page_id: batch_data_model.htm
title: Data Model
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_data_model.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Model

Data
   Processing Engine, Batch Management, and Monitor Workflow Servics share a data model. Let's learn
   about the objects and relationships in this shared data model.

  

    
     
      

     

     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability for Data Processing Engine.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |
| Available in: [View product and edition availability for Batch Management.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

  

Here's the data model:

=== ARTICLE: batch_management_apis.htm ===
---
page_id: batch_management_apis.htm
title: Common Business APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Common Business APIs

Common Business APIs are RESTful APIs that are sometimes available as Apex classes and
    methods.

- 
**[REST Reference](./batch_management_apis_rest_references.htm.md)**  

You can access Common Business APIs using REST endpoints. These REST APIs follow     similar conventions as Connect REST APIs.

=== ARTICLE: batch_management_apis_resources.htm ===
---
page_id: batch_management_apis_resources.htm
title: Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Resources

Here’s a list of Common Business API resources.

- 
**[Batch Job Cancel](./connect_resources_batch_job_cancel.htm.md)**  

Cancel a batch job of type data processing engine (calc job) and batch       management. A batch job with only the status Submitted or In Progress can be     canceled.

=== ARTICLE: batch_management_apis_responses.htm ===
---
page_id: batch_management_apis_responses.htm
title: Response Bodies
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_apis_rest_references.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Response Bodies

Here’s a list of Common Business API response bodies.

- 
**[Batch Job Cancel Output](./connect_responses_batch_job_cancel.htm.md)**  

Output representation of the batch job cancel     request.

=== ARTICLE: batch_management_apis_rest_references.htm ===
---
page_id: batch_management_apis_rest_references.htm
title: REST Reference
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_apis_rest_references.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# REST Reference

You can access Common Business APIs using REST endpoints. These REST APIs follow
    similar conventions as Connect REST APIs.

    

To understand the architecture, authentication, rate limits, and how the requests and
      responses work, see
        [Connect REST API Developer
        Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/).

  

- 
**[Resources](./batch_management_apis_resources.htm.md)**  

Here’s a list of Common Business API resources.

- 
**[Response Bodies](./batch_management_apis_responses.htm.md)**  

Here’s a list of Common Business API response bodies.

#### See Also

- [Connect REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.chatterapi.meta/chatterapi/)

=== ARTICLE: batch_management_dev_overview.htm ===
---
page_id: batch_management_dev_overview.htm
title: Batch Management
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_dev_overview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Management

Automate the processing of records in scheduled flows. You can process a high volume of
  standard and custom object records. Batch Management consists of three Tooling API objects, a
  standard object, a Metadata API, and an invocable action. You can use these resources to view,
  create, edit, and run Batch Management jobs.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

 

- 
**[Batch Management Tooling API Objects](./batch_management_setup_object.htm.md)**  

You can use the Batch Management Tooling API object to view the settings of Batch    Management jobs.

- 
**[Batch Management Standard Objects](./batch_management_standard_object.htm.md)**  

Batch Management contains a standard BatchProcessJobDefinitionView object, which you    can use to view all the batch jobs available in your Salesforce org, including file-based    jobs.

- 
**[Batch Management Metadata API](./batch_metadata.htm.md)**  

Use a Metadata API to create, update, and activate Batch Management jobs.

- 
**[Batch Management Invocable Actions](./batch_mgt_actions_parent.htm.md)**  

Run an active Batch Management job definition. For more     information on custom invocable actions, see **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

=== ARTICLE: batch_management_platform_event.htm ===
---
page_id: batch_management_platform_event.htm
title: Common Platform Event
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_platform_event.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Common Platform Event

Batch Management jobs and Data Processing Engine definitions are run using invocable
   actions in Flows. Use the BatchJobStatusChanged event to notify subscribers after a Batch
   Management job or a Data Processing Engine definition is processed in a flow.

  

    
     
      

     

     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability for Data Processing Engine.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |
| Available in: [View product and edition availability for Batch Management.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

 

- 
**[BatchJobStatusChangedEvent](./sforce_api_objects_batchjobstatuschangedevent.htm.md)**  

Notifies subscribers of when a batch job is completed in a 			flow. This object is available in API version 51.0 and later.

=== ARTICLE: batch_management_setup_object.htm ===
---
page_id: batch_management_setup_object.htm
title: Batch Management Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_setup_object.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Management Tooling API Objects

You can use the Batch Management Tooling API object to view the settings of Batch
   Management jobs.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

  

Tooling API objects let you interact with metadata for declarative development. For example,
   you can create your own version of Setup.

 

- 
**[BatchDataSource](./tooling_api_objects_batchdatasource.htm.md)**  

       Represents the source of information from which a batch job retrieves records          for processing. This object is available in API version 66.0 and later.

- 
**[BatchDataSrcFilterCriteria](./tooling_api_objects_batchdatasrcfiltercriteria.htm.md)**  

       Represents the details of a condition in the filter criteria used to retrieve          records from the data source of a batch job. This object is available in API version       66.0 and later. 

- 
**[BatchProcessJobDefinition](./tooling_api_objects_batchprocessjobdefinition.htm.md)**  

     Represents the details of a Batch Management job. This object is available     in API version 51.0 and later.

=== ARTICLE: batch_management_standard_object.htm ===
---
page_id: batch_management_standard_object.htm
title: Batch Management Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_management_standard_object.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Management Standard Objects

Batch Management contains a standard BatchProcessJobDefinitionView object, which you
   can use to view all the batch jobs available in your Salesforce org, including file-based
   jobs.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

 

- 
**[BatchProcessJobDefView](./sforce_api_objects_batchprocessjobdefview.htm.md)**  

     Represents the details of a Batch Job definition. The definition can also be       file-based definitions that are available in your Salesforce org. This object is     available in API version 51.0 and later.

=== ARTICLE: batch_metadata.htm ===
---
page_id: batch_metadata.htm
title: Batch Management Metadata API
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_metadata.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Management Metadata API

Use a Metadata API to create, update, and activate Batch Management jobs.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US) |

  

 

- 
**[BatchProcessJobDefinition](./meta_batchprocessjobdefinition.htm.md)**  

Represents the details of a Batch Management job       definition.

=== ARTICLE: batch_mgt_actions_batch_job.htm ===
---
page_id: batch_mgt_actions_batch_job.htm
title: Batch Job Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_mgt_actions_batch_job.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_mgt_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Job Actions

Run an active Batch Management job definition. This action executes a
   defined Batch Management job asynchronously.

  
   

A Batch Management job processes a flow in manageable parts. For more information about
    running an active Batch Management jobs, see [Schedule a Batch Job](https://help.salesforce.com/articleView?id=task_schedule_batch_flow.htm&language=en_US) in Salesforce Help.

   

This object is available in API version 51.0 and later.

  

  

## Special Access Rules

To know the products and
    user permissions needed to access this action, See [Supported Editions and Permissions for Batch
    Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

  

## Supported REST HTTP Methods

   
   
    
     

**URI**

     
: ``/services/data/vXX.X/`actions/custom/batchJobAction`

    
    
     

**Formats**

     
: JSON

    
    
     

**HTTP Methods**

     
: GET, POST

    
    
     

**Authentication**

     
: `Authorization: Bearer token`

    
   

  

  

## Inputs

   
   

The batch job action uses the batch job definition ID and input variables to execute the job
    and generate a batch job ID. The input values vary according to the input variables in that
    flow.

  

  

## Outputs

   
   

     
     
     
      
       

       

      

     

     
      
       

       

: 

: 

      

     

    
| Output | Details |
| --- | --- |
| batchJobId | **Type** string **Description** ID of the batch job generated after the request is successful. This batch job ID is used to track the progress of the batch job in Monitor Workflow Services. |

  

  

## Usage

A request body is always required. The input values vary according
    to the input variables in that flow. If your batch job doesn't require any input variables, you
    still must send an empty JSON body.

    

```
{
  "inputs": [{}]
}
```

   

**JSON Sample Request**

    

```
{
   "noOfEmployees" : 900,
   "accountIndustry" : "Technology"
}
```

   

**JSON Sample Response**

    

```
{
   "batchJobId": "0lMxx0000A000001EAA"
   "accepted": "true"
}
```

=== ARTICLE: batch_mgt_actions_parent.htm ===
---
page_id: batch_mgt_actions_parent.htm
title: Batch Management Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/batch_mgt_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Management Invocable Actions

Run an active Batch Management job definition. For more
    information on custom invocable actions, see **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

- 
**[Batch Job Actions](./batch_mgt_actions_batch_job.htm.md)**  

Run an active Batch Management job definition. This action executes a    defined Batch Management job asynchronously.

- 
**[Submit Failed Records Batch Job](./actions_obj_submit_failed_records_batchjob.htm.md)**  

Run to resubmit an existing batch job with failed records for    processing. This action executes the batch job asynchronously.

=== ARTICLE: connect_resources_batch_job_cancel.htm ===
---
page_id: connect_resources_batch_job_cancel.htm
title: Batch Job Cancel
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_batch_job_cancel.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Job Cancel

Cancel a batch job of type data processing engine (calc job) and batch
      management. A batch job with only the status Submitted or In Progress can be
    canceled.

        
          

**Special Access Rules**

          
: To know the permissions needed to access this resource, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

        
        
          

**Resource**

          
: 
            

```
/connect/batch-job/batchJobId/cancel-job
```

          

        
        
          

**Resource example**

          
: 
            

```
/connect/batch-job/0mdxx00000000fxAAA/cancel-job
```

          

        
        
          

**Available version**

          
: 52.0

        
        
          

**Requires Chatter**

          
: No

        
        
          

**HTTP methods**

          
          
: POST

#### Note

POST doesn’t take
              request
              parameters or a request body.

        
        
          

**Response body for POST**

          
: Returns HTTP 201 on success.

          
: See [Batch Job Cancel Output](./connect_responses_batch_job_cancel.htm.md) for HTTP code descriptions that are
            unique to this resource in case of failure of the batch job cancel request.

=== ARTICLE: connect_responses_batch_job_cancel.htm ===
---
page_id: connect_responses_batch_job_cancel.htm
title: Batch Job Cancel Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_batch_job_cancel.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Batch Job Cancel Output

Output representation of the batch job cancel
    request.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `message` | String | Details about why the batch job cancel request failed. | Small, 52.0 | 52.0 |

      

This table lists HTTP response code descriptions that are unique to this resource.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| HTTP Response Code | Error Code | Description |
| --- | --- | --- |
| 400 | `INVALID_STATUS` | We can't cancel the batch job that doesn't have an active run. Specify the ID of a batch job with an active run and try again. |
| 400 | `INVALID_STATUS` | We can't cancel the batch job that is already canceled or completed. Specify the ID of a valid batch job with the status InProgress or Submitted and try again. |
| 400 | `DELETE_FAILED` | We can’t cancel the batch job of which the results are already being written back. |
| 400 | `DELETE_FAILED` | We can’t cancel the batch job because of an error in processing your org’s data. Run the Data Processing Engine definition and try again. |
| 403 | `FORBIDDEN` | You don’t have the permission to cancel a batch job. Ask your Salesforce admin for help. |
| 404 | `RESOURCE_NOT_FOUND` | Specify the ID of a valid batch job and try again. |
| 500 | `INTERNAL_SERVER_ERROR` | Something went wrong when we tried to cancel the batch job. Try again or ask your Salesforce admin for help. |

=== ARTICLE: data_processing_engine_dev_overview.htm ===
---
page_id: data_processing_engine_dev_overview.htm
title: Data Processing Engine
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/data_processing_engine_dev_overview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine

Transform data that's available in your Salesforce org and write back the transformation
  results as new or updated records. You can transform the data for standard and custom objects.
  Data Processing Engine consists of a Tooling API object, a standard object, a Metadata API, and an
  invocable action. You can use these to view, create, edit, and run Data Processing Engine
  definitions.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |

  

 

- 
**[Data Processing Engine Tooling API Objects](./data_processing_engine_setup_object.htm.md)**  

Data Processing Engine consists of one Tooling API object, BatchCalcJobDefinition. Use   this object to create and edit a Data Processing Engine definition.

- 
**[Data Processing Engine Standard Object](./data_processing_engine_standard_object.htm.md)**  

Data Processing Engine contains one standard object, BatchCalcJobDefinitionView. Use   this object to view all the Data Processing Engine definitions available in your Salesforce org,   including file-based definitions.

- 
**[Data Processing Engine Metadata API](./dpe_metadata.htm.md)**  

Use a Metadata API to create, update, and activate Data Processing Engine   definitions.

- 
**[Data Processing Engine Invocable Actions](./dpe_actions_parent.htm.md)**  

Run an active Data Processing Engine definition. For more     information on custom invocable actions, see **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

=== ARTICLE: data_processing_engine_setup_object.htm ===
---
page_id: data_processing_engine_setup_object.htm
title: Data Processing Engine Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/data_processing_engine_setup_object.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine Tooling API Objects

Data Processing Engine consists of one Tooling API object, BatchCalcJobDefinition. Use
  this object to create and edit a Data Processing Engine definition.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |

  

  

Tooling API objects let you interact with metadata for declarative development. For example,
   you can create your own version of Setup.

 

- 
**[BatchCalcJobDefinition](./tooling_api_objects_batchcalcjobdefinition.htm.md)**  

Represents a Data Processing Engine (DPE) definition. This object     is available in API version 51.0 and later.

=== ARTICLE: data_processing_engine_standard_object.htm ===
---
page_id: data_processing_engine_standard_object.htm
title: Data Processing Engine Standard Object
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/data_processing_engine_standard_object.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine Standard Object

Data Processing Engine contains one standard object, BatchCalcJobDefinitionView. Use
  this object to view all the Data Processing Engine definitions available in your Salesforce org,
  including file-based definitions.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |

  

 

- 
**[BatchCalcJobDefinitionView](./sforce_api_objects_batchcalcjobdefinitionview.htm.md)**  

Represents the details of a Data Processing Engine definition. The       definition can also be a file-based definition that is available in your Salesforce org.     This object is available in API version 51.0 and later.

=== ARTICLE: dpe_actions_parent.htm ===
---
page_id: dpe_actions_parent.htm
title: Data Processing Engine Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dpe_actions_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine Invocable Actions

Run an active Data Processing Engine definition. For more
    information on custom invocable actions, see **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_intro.htm)**.

- 
**[Data Processing Engine Actions](./dpe_actions_run_data_processing_engine.htm.md)**  

Run an active Data Processing Engine definition. This action executes       a Data Processing Engine definition asynchronously.

=== ARTICLE: dpe_actions_run_data_processing_engine.htm ===
---
page_id: dpe_actions_run_data_processing_engine.htm
title: Data Processing Engine Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dpe_actions_run_data_processing_engine.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: dpe_actions_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine Actions

Run an active Data Processing Engine definition. This action executes
      a Data Processing Engine definition asynchronously.

    
      

A Data Processing Engine definition transforms data from your Salesforce org and writes
        back the results to your org. For more information about running Data Processing Engine
        definitions, see [Run a Data Processing Engine Definition](https://help.salesforce.com/articleView?id=task_data_processing_engine_run.htm&language=en_US) in
        Salesforce Help.

      

This object is available in API version 51.0 and later.

    

    

## Special Access Rules

To know the products and user permissions needed to access this action, See [product availability](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) and [user permissions](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) for Data Processing Engine.

    

## Supported REST HTTP Methods

      
      
        
          

**URI**

          
: ``/services/data/vXX.X/`actions/custom/dataProcessingEngineAction`

        
        
          

**Formats**

          
: JSON

        
        
          

**HTTP Methods**

          
: GET, POST

        
        
          

**Authentication**

          
: `Authorization: Bearer token`

        
      

    

    

## Inputs

      
      

Use the GET method to retrieve input variables of a Data Processing Engine definition. The
        input variables of each Data Processing Engine definition are unique. The Data Processing
        Engine action uses the input variables to execute the Data Processing Engine definition and
        generate a batch job ID. 

      

#### Note

You can't use this action to start two simultaneous runs of a definition with the same
        input variables.

    

    

## Outputs

      
      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

            

          

        
| Output | Details |
| --- | --- |
| batchJobId | **Type** string **Description** ID of the batch job generated after the request is successful. This ID is used to track the progress of the batch job in Monitor Workflow Services. |

    

    

## Usage

      
      

**JSON Sample Request to execute PointsAccrual DPE Definition**

      
        

```
{
   "PointsAccrual" : {
      "memberTier" : "Gold",
      "minimumPointBalanceRequired" : "50000",
      "pointType" : "non-qualifying"
   }
}
```

      

      

**JSON Sample Response**

      
        

```
{
   "actionName":"PointsAccrual",
      "errors":null,
      "isSuccess":true,
      "outputValues":{ 
        "batchJobId":"0lMxx0000A000001EAA"
      }
}
```

      

    

    

## Example

      
      
        
          

**GET**

          
: 
            This example shows how to retrieve input variables of a Data Processing Engine action
              type.

```
curl --include --request GET \
--header "Authorization: Authorization: Bearer 00DR...xyz" \
--header "Content-Type: application/json" \
"https://instance.salesforce.com/services/data/v60.0/actions/custom/dataProcessingEngineAction/newinputvardefn"
```

          

        
        
          

**POST**

          
: 
            Here’s a request to retrieve DPE definition

```
{
  "inputs": [
    {
      "start_date": "26-09-2023",
      "end_date": "12-12-2023",
      "randomkey": "069SM0000001SgbYAE"
    }
  ]
}
```

            Here’s a response for this action.

```
[
  {
    "actionName": "newinputvardefn",
    "errors": null,
    "invocationID": null,
    "isSuccess": true,
    "outputValues": {
      "batchJobId": "0mdSM0000006EJdYAM",
      "accepted": true
    },
    "version": 1
  }
]
```

=== ARTICLE: dpe_metadata.htm ===
---
page_id: dpe_metadata.htm
title: Data Processing Engine Metadata API
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dpe_metadata.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Data Processing Engine Metadata API

Use a Metadata API to create, update, and activate Data Processing Engine
  definitions.

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: [View product and edition availability.](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) |

  

 

- 
**[BatchCalcJobDefinition](./meta_batchcalcjobdefinition.htm.md)**  

Represents a Data Processing Engine definition.

=== ARTICLE: meta_batchcalcjobdefinition.htm ===
---
page_id: meta_batchcalcjobdefinition.htm
title: BatchCalcJobDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_batchcalcjobdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: dpe_metadata.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchCalcJobDefinition

Represents a Data Processing Engine definition.
  

    
    

## Parent Type

       This type extends the Metadata metadata type and inherits its fullName
      field.

    

## File Suffix and Directory Location

      
      

BatchCalcJobDefinition components have the suffix
          .batchCalcJobDefinition and are stored in the
          batchCalcJobDefinitions folder.

    

    

## Version

      
      

BatchCalcJobDefinition components are available in API version 51.0 and later.

    

    

## Special Access Rules

To know the products and user permissions needed to access this type, See [product availability](https://help.salesforce.com/s/articleView?id=ind.dpe_editions.htm&language=en_US) and [user permissions](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) for Data Processing Engine.

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              
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

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| aggregates | [BatchCalcJob​​​Aggregate](#bcjaggregateID)[] | Collection of aggregate nodes in a data processing engine. |
| appends | [BatchCalcJobUnion](#bcjunionID)[] | Collection of append nodes in a data processing engine. |
| atomicWritebacks | [BatchCalcJobAtomicWriteBack](#BatchCalcJobAtomicWriteback)[] | Collection of composite writeback nodes in a data processing engine definition. Available in API version 62.0 and later. |
| customNodes | [BatchCalcJobCustomNode](#bcjcustomnodeID)[] | Collection of custom nodes in a data processing engine. Available in API version 57.0 and later. |
| currencyConversion | string | Specifies the currency conversion type for the data processing engine definition.Available in API version 67.0 and later. |
| dataSpaceApiName | string | Stores the Data Space API Name from Data 360. Available in API version 60.0 and later. |
| datasources | [BatchCalcJob​Datasource](#bcjdatasourceID)[] | Collection of data source nodes in a data processing engine. |
| definitionRunMode | BatchCalcJobDefRunMode(enumeration of type string) | Specifies the execution mode in a data processing engine. Valid values are: `Batch` `OnDemand` |
| description | string | Description of a data processing engine definition. |
| doesGenAllFailedRecords | boolean | Indicates whether the error file includes a complete list of all failed writeback records (`true`) or not (`false`). The default value is `false`, and only the first instance of a failure is recorded in the error file. If set to `true`, all failed records are recorded in the error file for the writeback node.Available in API version 65.0 and later. |
| executionPlatformObjectType | ExecutionPlatformObjectType(enumeration of type string) | The execution platform object type that's used during the read, transform, and writeback process for the Data Processing Engine definition. Possible values are: `CalculatedInsightsObject` `DataLakeObject` `DataModelObject` `None` Available in API version 65.0 and later. |
| executionPlatformType | ExecutionPlatformType(enumeration of type string) | The platform that's used to run the Data Processing Engine definition. Valid values are: `CRMA` `CDP` `CORE` Available in API version 59.0 and later. |
| filters | [BatchCalcJobFilter](#bcjfilterID)[] | Collection of filter nodes in a data processing engine. definition. |
| forecasts | [BatchCalcJobForecast](#bcjforecastID)[] | Collection of forecast nodes in a data processing engine. definition.Available in API version 58.0 and later. |
| hierarchyPaths | [BatchCalcJobHierarchyPath](#bcjhierarchypathID)[] | Collection of hierarchy path nodes in a data processing engine definition. |
| isTemplate | boolean | Indicates whether it’s a template data processing engine definition. |
| joins | [BatchCalcJobSource​Join](#bcjsourcejoinID)[] | Collection of join nodes in a data processing engine. |
| label | string | The label of a data processing engine definition. |
| parameters | [BatchCalcJobParameter](#bcjparameterID)[] | Collection of input variables in a data processing engine. |
| processType | BatchCalcProcessType (enumeration of type string) | The process type of a data processing engine. These process types may be available to you depending on your industry solution and permission sets. Valid values are: `AccountingPeriodClosure` `AccountingSubledger`—This value is reserved for internal use. `AccrualsAndPayoutEngine` `ActionableList` `AdvancedAccountForecast` `AutomotiveFoundation` `BenefitManagement` `BillingSchedulesforInvoiceGeneration` `CDPEnrichment` `ChannelInventoryManagement`—Available in API version 63.0 and later. `CollectionPlan`—Available in API version 65.0 and later. `ContextService`—Available in API version 67.0 and later. `CriteriaBsdSearchAndFilter` `DataProcessingEngine` `DecisionMatrixDataUpload` `Decisiontable` `Education` `EmployeeService`—Available in API version 63.0 and later. `EnergyUtilitiesSales` `FinancialSummaryRollup` `FlexibleHierarchy` `ForeignExchangeGainLossCalculations`—Available in API version 65.0 and later. `FSCHierarchyRollUp` `Fundraising`—Available in API version 64.0 and later. `FundraisingRollups`—Available in API version 63.0 and later. `GeneralLedgerAccountBalancesSummary`—Available in API version 65.0 and later. `InventoryBatchSearch`—Available in API version 65.0 and later. `InventorySearch`—Available in API version 65.0 and later. `InvoiceGeneration` `Loyalty` `LegalEntityAccountingPeriodClosureAdvanced`—Available in API version 63.0 and later. `LifeSciencbatchcalesCommercialTerritoryAlignment`—Available in API version 63.0 and later. `LifeSciencesCustomerEngagement`—Available in API version 64.0 and later. `LoyaltyPartnerManagement` `LoyaltyPointsAggregation` `MediaAdSales` `NextGenForecasting`—Available in API version 64.0 and earlier. `NetZero` `PatientServicesProgram`—Available in API version 64.0 and later. `PlanningAndForecasting` `PnmRosterFileUpload` `PriceProtection` `ProductCatalogManagement` `ProgramBasedBusiness` `ProviderSearch`—This value is reserved for internal use. `Rebates` `RebateAndAccrualManagementAdvanced` `Recruitment` `RevenueTransactionManagement`—Available in API version 63.0 and later. `SalesAgreement`—Available in API version 63.0 and later. `TestAtomicWritebackScale`—Available in API version 64.0 and later. `TestProcessType` `UsageManagement` |
| status | BatchJobDefinition​Status (enumeration of type string) | Status of a data processing engine definition. Valid values are: `Active` `Inactive` |
| targetCurrencyIsoCode | string | ISO code of the target currency for currency conversion in the data processing engine definition.Available in API version 67.0 and later. |
| transforms | [BatchCalcJobTransform](#bcjtransformID)[] | Collection of data transformation nodes in a data processing engine. |
| writebacks | [BatchCalcJobWriteback​Object](#bcjwritebackobjectID)[] | Collection of writeback objects in which the results of the data processing engine are written back. |

    

    

## BatchCalcJob​​​Aggregate

      
    

    
      

Represents a collection of fields relating to an aggregate node in a data processing
          engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | Description of an aggregate node. |
| fields | [BatchCalcJob​AggregateField](#bcjaggregatefieldID)[] | Required. Collection of aggregation fields. |
| groupBy | string[] | Required. Collections of fields used to group data in an aggregate node. |
| label | string | Required. Label of an aggregate node. |
| name | string | Required. Name of an aggregate node. |
| sourceName | string | Required. Name of the source node. |

    

    

## BatchCalcJob​AggregateField

      
    

    
      

Represents a collection of fields relating to an aggregation field in an aggregate node
          of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

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
| aggregateFunction | BatchCalcJobAggregateFunction (enumeration of type string) | Required. Function used for aggregation. Valid values are: `Unique`—A count of unique values. `Sum`—The sum of all values. `Max`—The largest value. `Min`—The smallest value. `Avg`—The average value, calculated as the mean. `Std`—The standard deviation. `Stdp`—A standard deviation with population variance. `Var`—The variance. `VarP`—The variance with population. `Count`—The total count of values. |
| alias | string | Required. Name that subsequent nodes within the data processing engine use to refer to the aggregate field. |
| sourceFieldName | string | Required. Source node field on which the aggregate is calculated. |

    

    

## BatchCalcJobAtomicWriteback

      
      

Represents a node in a DPE definition that stores the details about the relationship
        between the writeback nodes and the composite writeback operations between the nodes.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | Description of the composite writeback object. |
| label | string | Required. Name of the composite writeback object. |
| name | string | Required. API name of the composite writeback object. |
| writebackObject​Relationships | [BatchCalcJobAtomicWritebackRelationship](#BatchCalcJobAtomicWritebackRelationship)[] | Specifies the relationship between the writeback objects that are involved in the writeback operation. |
| writebackSequence | int | Sequence in which the data processing engine executes the composite write back node. |

    

    

## BatchCalcJobAtomicWritebackRelationship

      
      

Represents the relationships between the writeback objects that are involved in a composite
        writeback operation. It captures the relationships between these objects and the sequence in
        which they should be processed.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| childWriteback​ObjectField | string | Field name that's associated with the child writeback object in a composite writeback relationship. Available in API version 63.0 and later. |
| childWriteback​ObjectName | string | Name of the child writeback object that's associated with the writeback relationship. |
| parentWriteback​ObjectField | string | Field name that's associated with the parent writeback object in a composite writeback relationship. Available in API version 63.0 and later. |
| parentWriteback​ObjectName | string | Required. Name of the parent writeback object that's associated with the writeback relationship. |
| relationshipName | string | Describes the relationship between the child and parent writeback objects in a composite writeback node. Available in API version 64.0 and later. |
| sequenceNumber | int | Sequence number of the writeback node that's associated with its parent node in the relationship. |

    

    

## BatchCalcJob​​​CustomNode

      
    

    
      

Represents a collection of custom nodes in a data processing engine. Use a custom node
          to add a custom action.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | Description of a custom node. |
| extensionName | string | Required. Name of an extension node. |
| extensionNamespace | string | Required. Namespace of an extension node. |
| label | string | Required. Label of a custom node. |
| name | string | Required. Name of a custom node. |
| parameters | [BatchCalcJob​​​CustomNodeParameter](#bcjcustomnodeparameterID)[] | The field mappings of an extension node. |
| sources | string[] | Sources of an extension node. |

    

    

## BatchCalcJob​​​CustomNodeParameter

      
    

    
      

Represents the field mappings of an extension node.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| name | string | Required. Name of a parameter. |
| value | string | Required. Value of a parameter. |

    

    

## BatchCalcJob​Datasource

      
    

    
      

Represents a collection of fields relating to a data source node in a data processing
          engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

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
| CSVDelimiter | ​BatchCalcJobCSVDelimiter (enumeration of type string) | Specifies the field separator to read fields from a CSV file record. Possible values are: `COMMA` `BACKQUOTE` `CARET` `PIPE` `SEMICOLON` `TAB` The default value is `COMMA`. The same delimiter value used for the CSV file can’t be used within any of the column values in the file. If you mistakenly use the same delimiter value in column values, it can cause data parsing issues. |
| description | string | Description of a data source node. |
| fields | [BatchCalcJob​DatasourceField](#bcjdatasourcefieldID)[] | Required. Collection of data source fields. |
| fileIdentifier | string | Specifies the source of the file or file storage system. |
| filePath | string | The file path for the specified file. |
| fileSource | BatchCalcJobFileSource (enumeration of type string) | Specifies the source of the file or file storage system.Possible value is: `ContentManagement` |
| label | string | Required. Label of a data source node. |
| name | string | Required. Name of a data source node. |
| parentDataSource | string | Name of the parent data source node.Available in API version 67.0 and later. |
| sourceName | string | Required. Name of a standard or custom object from which the data source node extracts data. |
| type | BatchCalcJobDataSource​Type (enumeration of type string) | Required. Type of object for the source object field. Supported values are: `Analytics` `CalculatedInsightsObject` `Context`—Available in API version 67.0 and later. `CRMObject` `CSV` `DataLakeObject` `DataModelObject` `StandardObject` . |

    

    

## BatchCalcJob​DatasourceField

      
    

    
      

Represents a collection of fields relating to a source object field that are selected
          in the data source node of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

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
| alias | string | Name that subsequent nodes within the data processing engine use to refer to the data source field. Required when the field name is lookup. |
| dataType | BatchCalcJobDataType (enumeration of type string) | Specifies the data type of the input field when using a CSV file as a data source.Possible values are: `Boolean`—Available in API version 65.0 and later. `Date` `DateTime` `MultiValue` `Numeric` `Text` |
| isPrimaryKey | boolean | Indicates whether a column name is the primary key (`true`) or not (`false`) for the Data Cloud CSV file. |
| name | string | Required. Name of the field. Can be either of the following: Name of the source field selected in the associated data source object. Name from a nested lookup object with three child levels. |

    

    

## BatchCalcJobFilter

      
    

    
      

Represents a collection of fields relating to a filter node in a data processing
          engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| criteria | [BatchCalcJobFilter​Criteria](#bcjfiltercriteriaID)[] | Collection of filter criteria in a filter node. The field is required when `isDynamicFilter` is set to `False`. |
| description | string | Description of the batch calculation job filter. |
| filterCondition | string | Logic that is specified to apply the filter conditions. The field is required when `isDynamicFilter` is set to `False`. |
| filterParameterName | string | Name of the parameter of type filter. |
| isDynamicFilter | boolean | Indicates whether the filter criteria is dynamic. If value is set to `True`, filter criteria is passed in runtime with `filterParameterName`. |
| label | string | Required. Label of the filter node. |
| name | string | Required. Name of the filter node. |
| sourceName | string | Required. Name of the source node. |

    

    

## BatchCalcJobForecast

      
    

    
      

Represents a collection of fields relating to a forecast node in a data processing
          engine. Available in API version 58.0 and later.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

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

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| accuracyPercent | BatchCalcJobFrcstAccuracy (enumeration of type string) | The interval percentage to account for errors in forecasts. Possible values are: `Eighty` `NinetyFive` `None` The default value is `None`. |
| aggregationFields | [BtchCalcJobFrcstAggrFld[]](#BtchCalcJobFrcstAggrFld) | The list of fields to forecast. |
| dateFieldName | string | Required.The date field from the source node used to forecast values for the specified forecast length. |
| description | string | The description of the forecast node. |
| forecastModelType | BatchCalcJobFrcstModel (enumeration of type string) | The model used to forecast data.Possible values are: `Additive` `Auto` `Multiplicative` The default value is `Auto`. |
| forecastPeriodCount | int | The number of time periods to generate forecast data. For example, if you select Year-Month as the forecast period type, and 4 as the forecast period count, the forecast results are generated for the next 4 months. The minimum and the default count is 1, and the maximum is 100. |
| forecastPeriodType | BatchCalcJobFrcstPeriodType (enumeration of type string) | Required.The type of forecast period to group date field values in the forecast results. Possible values are: `FiscalYear` `FiscalYearMonth` `FiscalYearQuarter` `FiscalYearWeek` `Year` `YearMonth` `YearMonthDay` `YearQuarter` `YearWeek` |
| groupFields | [BatchCalcJobFrcstGrpFld[]](#BatchCalcJobFrcstGrpFld) | The source fields for grouping the data to be processed by the forecast node. |
| label | string | Required.The name of the forecast node in the UI. |
| name | string | Required. A unique name for the forecast node. |
| periodStartDateName | string | Required.The start date of the forecast period. |
| seasonality | BatchCalcJobFrcstSeasonality (enumeration of type string) | Represents the periodic fluctuations that occur around the same time every year. Possible values are: `Two` `Three` `Four` `Five` `Six` `Seven` `Eight` `Nine` `Ten` `Eleven` `Twelve` `Thirteen` `Fourteen` `Fifteen` `Sixteen` `Seventeen` `Eighteen` `Nineteen` `Twenty` `TwentyOne` `TwentyTwo` `TwentyThree` `TwentyFour` `Auto` `None` The default value is `None`. |
| shouldExcludeLastPeriod | boolean | Indicates whether to ignore the last period in the source node when it has incomplete data (`true`) or not (`false`).The default value is `false`. |
| sourceName | string | Required. The name of the source node. A source can be any node other than the datasink and register node. |

    

    

## BtchCalcJobFrcstAggrFld

      
      

Represents a list of fields to forecast in a forecast node.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

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
| aggregateFunction | BatchCalcJobAggregateFunction (enumeration of type string) | Required.The function of the aggregate field. Possible values are: `Avg` `Count` `Max` `Min` `Std` `StdP` `Sum` `Unique` `Var` `VarP` |
| aggregationResultLabel | string | Required.The name of the aggregation result generated from the aggregation function that’s applied to the source node field. |
| fieldName | string | Required.The name of the source field. |

    

    

## BatchCalcJobFrcstGrpFld

      
      

Represents source fields for grouping the data to be processed by the forecast node.

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

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
| fieldName | string | Required.The name of the source field to group the data to be processed by the forecast node. |
| groupBy | string | A comma-separated list of values to group data by. Required when the source field type is Date or DateTime. Possible values are: `Second` `Second Epoch` `Minute` `Hour` `Day` `Day Epoch` `Week` `Month` `Quarter` `Year` |

    

    

## BatchCalcJobHierarchyPath

      
    

    
      

Represents a collection of hierarchy path nodes in a data processing engine
          definition.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| aggregateFields | [BatchCalcJobHierarchyPath​AggregateField](#bcjhierarchypathaggfieldID)[] | Collection of aggregate fields for the hierarchy path node.Available in API version 67.0 and later. |
| description | string | Description of the hierarchy path node. |
| hierarchyFieldName | string | Required. Field name that contains the hierarchy path. |
| isAggregationRequired | boolean | Indicates whether aggregation is required for the hierarchy path node (`true`) or not (`false`).Available in API version 67.0 and later. |
| isSelfFieldValueIncluded | boolean | Indicates whether the self value is included in the calculated hierarchy path (`True`) or not (`False`). |
| label | string | Required. Label of the hierarchy path node. |
| name | string | Required. Name of the hierarchy path node. |
| parentFieldName | string | Required. Parent field name to calculate hierarchy path. |
| rollupPercentageFieldName | string | Field name used for rollup percentage calculation in the hierarchy path.Available in API version 67.0 and later. |
| selfFieldName | string | Required. Self field name to calculate hierarchy path. |
| sourceName | string | Required. Name of the source node. |

    

    

## BatchCalcJobHierarchyPath​AggregateField

      
    

    
      

Represents a collection of fields relating to an aggregation field in a hierarchy path
          node of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

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
| aggregateFunction | BatchCalcJobAggregateFunction (enumeration of type string) | Required. Function used for aggregation in the hierarchy path. Valid values are: `Unique` `Sum` `Max` `Min` `Avg` `Std` `Stdp` `Var` `VarP` `Count` Available in API version 67.0 and later. |
| alias | string | Required. Name that subsequent nodes within the data processing engine use to refer to the aggregate field.Available in API version 67.0 and later. |
| sourceFieldName | string | Required. Source node field on which the aggregate is calculated.Available in API version 67.0 and later. |

    

    

## BatchCalcJobFilter​Criteria

      
    

    
      

Represents a collection of fields relating to a filter condition in a filter node in a
          data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

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
| inputVariable | string | Name of the input variable used as a filter. |
| operator | BatchCalcJobFilter​Operator (enumeration of type string) | Required. Operator that is specified in the filter condition. Valid values are: `Equals` `NotEquals` `GreaterThan` `GreaterThanOrEqual` `LessThan` `LessThanOrEqual` `StartsWith` `EndsWith` `Contains` `DoesNotContain` `IsNull` `IsNotNull` `In` `NotIn` |
| sequence | integer | Required. Sequence number used to refer the criteria in a filter node. |
| sourceFieldName | string | Required. Name of the field from the source node to apply the filter. |
| value | string | Value used to filter data from the source node. |

    

    

## BatchCalcJobParameter

      
    

    
      

Represents a collection of fields relating to an input variable in a data processing
          engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              
- 
- 
- 
- 
- 
- 
- 

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| dataType | BatchCalcJobParameter​DataType (enumeration of type string) | Required. Data type of the parameter. Valid values are: `Date` `DateTime` `Expression` `FileIdentifier` `Filter` `Numeric` `Text` |
| defaultValue | string | Default value of the parameter. |
| description | string | Description of the batch calculation job parameter. |
| isMultiValue | boolean | Indicates whether the parameter has different values (`True`) or not (`False`). This field is supported only for the `Text` data type. |
| label | string | Required. Label of the batch calculation job parameter. |
| name | string | Required. Name of the batch calculation job parameter. |

    

    

## BatchCalcJobSource​Join

      
    

    
      

Represents a collection of fields relating to a join node in a data processing
          engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              
- 
- 
- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | Description of the join node. |
| fields | [BatchCalcJobJoin​ResultField](#bcjjoinresultfieldID)[] | Collection of fields in a join node. |
| hasLookUpMultipleValues | boolean | Indicates whether the lookup join returns multiple values (`true`) or not (`false`).Available in API version 67.0 and later. |
| joinKeys | [BatchCalcJobJoin​Key](#bcjjoinkeyID)[] | Collection of mapping of fields from the primary source node and the second source node in a join node. |
| label | string | Required. Label of the join node. |
| name | string | Required. Name of the join node. |
| primarySourceName | string | Required. Name associated with the node as the primary source node. |
| secondarySourceName | string | Required. Name associated with the node as the secondary source node. |
| type | BatchCalcJobSource​JoinType (enumeration of type string) | Required. Type of join specified between the primary source node and secondary source node. Valid values are: `LeftOuter` `RightOuter` `Inner` `Outer` `Lookup` |

    

    

## BatchCalcJobJoin​Key

      
    

    
      

Represents a collection of fields relating to a mapping of fields from the first source
          node and second source node in a join node of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| primarySourceFieldName | string | Required. Mapped field name of the primary source node. |
| secondarySourceFieldName | string | Required. Mapped field name of the secondary source node. |

    

    

## BatchCalcJobJoin​ResultField

      
    

    
      

Represents a collection of fields relating to a set of resultant fields in a join node
          of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| alias | string | Required. Name that subsequent nodes within the data processing engine definition use to refer to the resultant field. |
| sourceFieldName | string | Required. Name of field from the primary or secondary data source. |
| sourceName | string | Required. Source node of the primary or secondary data source. |

    

    

## BatchCalcJobTransform

      
    

    
      

Represents a collection of fields relating to a data transformation in a data
          processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

- 
- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | The description of the batch calculation job transform. |
| droppedFields | [BatchCalcJobTransform​DroppedField](#bcjtransformdroppedfieldID)[] | The collection of dropped fields in a data transformation. Available when the transformation type is `Slice`. |
| expressionFields | [BatchCalcJobTransform​AddedField](#bcjtransformaddedfieldID)[] | The collection of formula fields in a data transformation. Available when the transformation type is `Expression`. |
| label | string | Required. The label of the batch calculation job transform. |
| name | string | Required. The name of the batch calculation job transform. |
| orderBy | [BatchCalcJobOrderByField](#bcjorderbyfieldID)[] | A collection of fields that’s used to sort the records within each partition group. |
| partitionBy | string[] | A group of fields that’s used to partition the source data into partition groups. |
| sourceName | string | Required. Name of the source node. |
| transformType | BatchCalcJobTransform​Type (enumeration of type string) | Required. The type of transformation. Valid values are: `ComputeRelative—`This transformation calculates values based on values of the same partition group. `Expression`—This transformation calculates values based on existing values of fields in the same record. `Slice`—This transformation removes fields from the source node. |

    

    

## BatchCalcJobTransform​DroppedField

      
    

    
      

Represents a collection of fields relating to a dropped field in a data transformation
          of a data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| sourceFieldName | string | Required. Name of the field that is dropped. |

    

    

## BatchCalcJobTransform​AddedField

      
    

    
      

Represents a collection of fields relating to a formula in a data transformation of a
          data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

- 
- 
- 
- 
- 
- 

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| alias | string | Required. Name that subsequent nodes within the data processing engine use to the transform node. |
| dataType | BatchCalcJobDataType (enumeration of type string) | Required. Data type of the formula. Valid values are: `Boolean`—Available in API version 65.0 and later. `Date` `DateTime` `MultiValue` `Numeric` `Text` |
| decimalPlaces | integer | Number of digits to the right of a decimal point in the value. Required for the `Numeric` data type. |
| expression | string | Required. Formula defined by the user. |
| length | integer | Total length of the value including the decimal places. Required for data types: `Text` and `Numeric`. |

    

    

## BatchCalcJobOrderByField

      
    

    
      

Represents a collection of fields that are used to sort the partitioned data.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

- 
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| name | string | Required. Name of the field that is used to sort data. |
| orderType | BatchCalcJobOrderType(enumeration of type string) | Order in which the data is sorted. Valid values are: Ascending Descending |

    

    

## BatchCalcJobUnion

      
    

    
      

Represents a collection of fields relating to the union of data from two nodes in a
          data processing engine.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| description | string | Description of the batch calculation job union. |
| isDisjointedSchema | boolean | Indicates whether the union is of two disjointed datasets (`true`) or not (`false`). Set to `True` to allow joining of two datasets having no common fields. |
| label | string | Required. Label of the batch calculation job union. |
| name | string | Required. Name of the batch calculation job union. |
| sources | string[] | Names of the source nodes. |

    

    

## BatchCalcJobWriteback​Object

      
    

    
      

Represents a collection of fields relating to the object in which the results of the
          data processing engine are written back.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

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
| canWrtbckToNonEditableFields | boolean | Indicates whether the non-editable fields are included in field mapping when the action type is upsert. The default value is `false`.Available in API version 64.0 and later. |
| description | string | Descriptions of the batch calculation job writeback object. |
| externalId​FieldName | string | Unique external field ID for the target object name. Available in API version 60.0 and later. |
| fields | [BatchCalcJobWriteback​Mapping](#bcjwritebackmappingID)[] | Collection of the writeback fields. |
| filterCondition | string | The condition that filters the records from a writeback dataset for a user. Examples of a filter condition include a user ID, stage name, and a security policy that returns only the records that a user owns.Available in API version 57.0 and later. |
| folderName | string | The folder where the writeback dataset is saved. Available in API version 57.0 and later. |
| groupBy | string | Reserved for future use. |
| isChangedRow | boolean | Indicates whether a row in the write back object is changed. Set to `True` to write back the changed rows. |
| isExistingDataset | boolean | Indicates whether a CRM Application (CRMA) dataset or a Data 360 Data Lake object is present (`true`) or will be created (`false`). Available in API version 62.0 and later. |
| jsonStructureType | string | JSON structure type for the writeback object.Available in API version 67.0 and later. |
| label | string | Required. Name of the write back object. |
| name | string | Required. Name of the batch calculation job write back object. |
| operationType | BatchCalcJobWriteback​Opn (enumeration of type string) | Type of operation specified. Valid values are: `Delete`—This value is available in API version 56.0 and later. `Insert` `Overwrite`—Available only when storageType is `DataLakeObject`. This value is available in API version 60.0 and later. `Update` `Upsert` |
| sharingInheritanceObjectName | string | The name of the source object from which the row-level sharing inheritance settings are applied. Available in API version 57.0 and later. |
| shouldCreateTargetObject | boolean | Indicates whether target Data Lake Object or Salesforce Object is created in Salesforce (`true`) or not (`false`). Available in API version 65.0 and later. |
| shouldMngRow​LockFor​GroupedRec | boolean | Reserved for future use. |
| sourceName | string | Required. Name of the source node associated with the write back object. |
| storageType | BatchCalcJobWriteback​Type (enumeration of type string) | Specifies where you want to use the data stored in the source node. Available in API version 57.0 and later.Valid values are: `Analytics` `DataLakeObject` `sObject` The default value is `sObject`. |
| targetObjectName | string | Required. Object that is inserted or upserted by the data processing engine. |
| targetObjectCategory | string | Category of the target object for the writeback operation.Available in API version 67.0 and later. |
| writebackSequence | integer | Sequence in which the target object is updated by the data processing engine. |
| writebackUser | string | ID of the user whose permissions decide which objects and fields of the target object can be updated. |

    

    

## BatchCalcJobWriteback​Mapping

      
    

    
      

Represents a collection of fields relating to the mapping between results and the
          fields in the target object.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              
- 
- 
- 
- 
- 

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| fieldType | string | Target field type on the writeback object. Valid values are: `EventTimeField`—Available in API version 67.0 and later. `ParentRecordIdentifierField`—Available in API version 67.0 and later. `PrimaryKey` `QualifierKey` `RecordIdentifierField`—Available in API version 67.0 and later. Available in API version 64.0 and later. |
| isAutogenerated | boolean | Indicates whether the target field value on the writeback object is autogenerated (`true`) or not (`false`).Available in API version 64.0 and later. |
| parentName | string | Name of the lookup object. Required only when the `relationshipName` field is defined. |
| relationshipName | string | Name of the lookup relationship. |
| runtimeParameter | boolean | Indicates whether the source field from runtime parameter is `true` or `false`. The default value is `false`.Available in API version 59.0 and later. |
| sourceFieldName | string | Required. Name of the field in the source node that is written back. |
| targetFieldName | string | Name of the sObject field to which the results are written back. |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of a BatchCalcJobDefinition component.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<BatchCalcJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">
    <aggregates>
        <description>Aggregate Description</description>
        <fields>
            <aggregateFunction>Count</aggregateFunction>
            <alias>NameCount</alias>
            <sourceFieldName>Name</sourceFieldName>
        </fields>
        <groupBy>ContactId</groupBy>
        <groupBy>Name</groupBy>
        <label>AggregateOpportunities</label>
        <name>AggregateOpportunities</name>
        <sourceName>Opportunity</sourceName>
    </aggregates>
    <forecasts>
        <description>ForecastNode Description</description>
        <label>ContactForecast</label>
        <name>ContactForecast</name>
        <sourceName>Contact</sourceName>
        <dateFieldName>CreatedDate</dateFieldName>
        <forecastPeriodType>YearMonth</forecastPeriodType>
        <shouldExcludeLastPeriod>false</shouldExcludeLastPeriod>
        <forecastPeriodCount>12</forecastPeriodCount>
        <periodStartDateName>CreatedDateYM</periodStartDateName>
        <forecastModelType>Auto</forecastModelType>
        <seasonality>None</seasonality>
        <accuracyPercent>None</accuracyPercent>
        <aggregationFields>
            <aggregateFunction>Count</aggregateFunction>
            <aggregationResultLabel>CountOfLastName</aggregationResultLabel>
            <fieldName>LastName</fieldName>
        </aggregationFields>
        <groupFields>
            <fieldName>LastModifiedDate</fieldName>
            <groupBy>Week</groupBy>
        </groupFields>
    </forecasts>
    <appends>
        <description>Append desc</description>
        <isDisjointedSchema>true</isDisjointedSchema>
        <label>AppendAllAccounts</label>
        <name>AppendAllAccounts</name>
        <sources>AccountsOfManufacturingIndustry</sources>
        <sources>ComputeRelativeManufacturingIndustry</sources>
    </appends>
    <datasources>
        <description>Desc Contact</description>
        <fields>
            <alias>Id</alias>
            <name>Id</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Text</dataType>
        </fields>
        <fields>
            <alias>LastName</alias>
            <name>LastName</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Text</dataType>
        </fields>
        <fields>
            <alias>CreatedDate</alias>
            <name>CreatedDate</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Date</dataType>
        </fields>
        <fields>
            <alias>LastModifiedDate</alias>
            <name>LastModifiedDate</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Date</dataType>
        </fields>
        <label>Contact</label>
        <name>Contact</name>
        <sourceName>Contact</sourceName>
        <type>StandardObject</type>
        <fileSource>ContentManagement</fileSource>
        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>
        <CSVDelimiter>COMMA</CSVDelimiter>
        <filePath>parentFolder/childFolder</filePath>
    </datasources>
    <datasources>
        <fields>
            <alias>Name</alias>
            <name>Name</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Text</dataType>
        </fields>
        <fields>
            <alias>ContactId</alias>
            <name>ContactId</name>
            <isPrimaryKey>false</isPrimaryKey>
            <dataType>Text</dataType>
        </fields>
        <label>Opportunity</label>
        <name>Opportunity</name>
        <sourceName>Opportunity</sourceName>
        <type>StandardObject</type>
        <fileSource>ContentManagement</fileSource>
        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>
        <CSVDelimiter>COMMA</CSVDelimiter>
        <filePath>parentFolder/childFolder</filePath>
    </datasources>
    <description>Calculates and creates transaction journal records based on the orders placed by the loyalty program members. The transaction journals are used to accrue points to the member.</description>
    <filters>
        <criteria>
            <operator>Equals</operator>
            <sequence>1</sequence>
            <sourceFieldName>LastName</sourceFieldName>
            <value>Salesforce</value>
        </criteria>
        <description>Filter Desc</description>
        <filterCondition>1</filterCondition>
        <isDynamicFilter>false</isDynamicFilter>
        <label>AccountsOfManufacturingIndustry</label>
        <name>AccountsOfManufacturingIndustry</name>
        <sourceName>AccountOpportunities</sourceName>
    </filters>
    <hierarchyPaths>
        <description>Hierarchy Path Node</description>
        <hierarchyFieldName>Hierarchy_Path</hierarchyFieldName>
        <isAggregationRequired>true</isAggregationRequired>
        <isSelfFieldValueIncluded>true</isSelfFieldValueIncluded>
        <label>Get Hierarchy</label>
        <name>Get_Hierarchy</name>
        <parentFieldName>ContactId</parentFieldName>
        <selfFieldName>LastName</selfFieldName>
        <sourceName>AppendAllAccounts</sourceName>
        <aggregateFields>
            <aggregateFunction>Count</aggregateFunction>
            <aggregationFieldName>*</aggregationFieldName>
            <aggregateFieldAliasName>CountOfLastName</aggregateFieldAliasName>
        </aggregateFields>
    </hierarchyPaths>
    <isTemplate>false</isTemplate>
    <executionPlatformObjectType>None</executionPlatformObjectType>
    <joins>
        <description>Left Outer Join</description>
        <fields>
            <alias>ContactId</alias>
            <sourceFieldName>Id</sourceFieldName>
            <sourceName>Contact</sourceName>
        </fields>
        <fields>
            <alias>LastName</alias>
            <sourceFieldName>LastName</sourceFieldName>
            <sourceName>Contact</sourceName>
        </fields>
        <fields>
            <alias>NameCount</alias>
            <sourceFieldName>NameCount</sourceFieldName>
            <sourceName>AggregateOpportunities</sourceName>
        </fields>
        <fields>
            <alias>OpportunityName</alias>
            <sourceFieldName>Name</sourceFieldName>
            <sourceName>AggregateOpportunities</sourceName>
        </fields>
        <joinKeys>
            <primarySourceFieldName>Id</primarySourceFieldName>
            <secondarySourceFieldName>ContactId</secondarySourceFieldName>
        </joinKeys>
        <label>AccountOpportunities</label>
        <name>AccountOpportunities</name>
        <primarySourceName>Contact</primarySourceName>
        <secondarySourceName>AggregateOpportunities</secondarySourceName>
        <type>LeftOuter</type>
    </joins>
    <label>Create Transaction Journals Based on Orders</label>
    <parameters>
        <dataType>Date</dataType>
        <defaultValue>2020-01-01</defaultValue>
        <description>Desc TextParameter</description>
        <isMultiValue>false</isMultiValue>
        <label>DateParameter</label>
        <name>DateParameter</name>
    </parameters>
    <parameters>
        <dataType>Filter</dataType>
        <defaultValue>{&quot;filterCondition&quot;: &quot;1 AND 2&quot;, &quot;criteria&quot;: [{&quot;sourceFieldName&quot;: &quot;NameCount&quot;,&quot;operator&quot;: &quot;GreaterThan&quot;,&quot;value&quot;: &quot;20&quot;,&quot;sequence&quot;: &quot;1&quot;}, {&quot;sourceFieldName&quot;: &quot;Name&quot;,&quot;operator&quot;: &quot;Equals&quot;,&quot;value&quot;: &quot;Salesforce&quot;,&quot;sequence&quot;: &quot;2&quot;}]}</defaultValue>
        <isMultiValue>false</isMultiValue>
        <label>FilterParameter</label>
        <name>FilterParameter</name>
    </parameters>
    <parameters>
        <dataType>Numeric</dataType>
        <defaultValue>5000</defaultValue>
        <description>Desc TextParameter</description>
        <isMultiValue>false</isMultiValue>
        <label>NumericParameter</label>
        <name>NumericParameter</name>
    </parameters>
    <parameters>
        <dataType>Text</dataType>
        <defaultValue>@salesforce.com</defaultValue>
        <description>Desc TextParameter</description>
        <isMultiValue>false</isMultiValue>
        <label>TextParameter</label>
        <name>TextParameter</name>
    </parameters>
    <processType>Rebates</processType>
    <definitionRunMode>Batch</definitionRunMode>
    <status>Inactive</status>
    <transforms>
        <description>transforms Desc</description>
        <expressionFields>
            <alias>NewLastName</alias>
            <dataType>Text</dataType>
            <expression>TODAY()</expression>
            <length>80</length>
        </expressionFields>
        <label>ManufacturingIndustry</label>
        <name>ManufacturingIndustry</name>
        <sourceName>AccountsOfManufacturingIndustry</sourceName>
        <transformationType>Expression</transformationType>
    </transforms>
    <transforms>
        <droppedFields>
            <sourceFieldName>NewLastName</sourceFieldName>
        </droppedFields>
        <label>MediaIndustry</label>
        <name>MediaIndustry</name>
        <sourceName>ManufacturingIndustry</sourceName>
        <transformationType>Slice</transformationType>
    </transforms>
    <transforms>
        <description>compute relative transforms Desc</description>
        <expressionFields>
            <alias>NewLastName</alias>
            <dataType>Text</dataType>
            <expression>rank()</expression>
            <length>80</length>
        </expressionFields>
        <label>ComputeRelativeManufacturingIndustry</label>
        <name>ComputeRelativeManufacturingIndustry</name>
        <orderBy>
            <name>LastName</name>
            <orderType>Ascending</orderType>
        </orderBy>
        <partitionBy>LastName</partitionBy>
        <sourceName>MediaIndustry</sourceName>
        <transformationType>ComputeRelative</transformationType>
    </transforms>
    <customNodes>
        <name>RebatesCustomNode</name>
        <label>Rebates Custom Node</label>
        <description>customNodes Desc</description>
        <sources>Get_Hierarchy</sources>
        <extensionName>RebatesExpression</extensionName>
        <extensionNamespace>industries_mfg</extensionNamespace>
        <parameters>
            <name>inputColumn</name>
            <value>LastName</value>
        </parameters>
        <parameters>
            <name>isFilterCriteria</name>
            <value>true</value>
        </parameters>
        <parameters>
            <name>outputColumn</name>
            <value>GenName</value>
        </parameters>
    </customNodes>
    <writebacks>
        <fields>
            <sourceFieldName>GenName</sourceFieldName>
            <targetFieldName>LastName</targetFieldName>
        </fields>
        <isChangedRow>false</isChangedRow>
        <label>exportToContact</label>
        <name>exportToContact</name>
        <description>Export To Contact</description>
        <operationType>Insert</operationType>
        <sourceName>RebatesCustomNode</sourceName>
        <targetObjectName>Contact</targetObjectName>
        <writebackSequence>1</writebackSequence>
        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>
    </writebacks>
    <writebacks>
        <fields>
            <sourceFieldName>CreatedDateYM</sourceFieldName>
            <targetFieldName>CreatedDate</targetFieldName>
        </fields>
        <isChangedRow>false</isChangedRow>
        <isExistingDataset>false</isExistingDataset>
        <label>exportToContactFC</label>
        <name>exportToContactFC</name>
        <description>Export To Contact</description>
        <operationType>Insert</operationType>
        <sourceName>ContactForecast</sourceName>
        <targetObjectName>Contact</targetObjectName>
        <writebackSequence>2</writebackSequence>
        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>
    </writebacks>
</BatchCalcJobDefinition>
```

      

The following is an example `package.xml` that
        references the previous definition.

      

```
<?xml version="1.0" encoding="UTF-8"?>
<!--
   ~ Copyright 2020 Salesforce, Inc.
   ~ All Rights Reserved
   ~ Company Confidential
-->
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
   <types>
      <members>*</members>
      <name>BatchCalcJobDefinition</name>
   </types>
   <version>60.0</version>
</Package>
```

    

    

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

=== ARTICLE: meta_batchprocessjobdefinition.htm ===
---
page_id: meta_batchprocessjobdefinition.htm
title: BatchProcessJobDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_batchprocessjobdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_metadata.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchProcessJobDefinition

Represents the details of a Batch Management job
      definition.
  

    
      

This type extends the Metadata metadata type and inherits its
            fullName field.

      

#### Important

Where possible, we changed noninclusive terms to align with our company
        value of Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## File Suffix and Directory Location

      
      

BatchProcessJobDefinition components have the suffix
          .batchProcessJobDefinition and are stored in the
          batchProcessJobDefinitions folder.

    

    

## Version

      
      

BatchProcessJobDefinition components are available in API version 51.0 and later.

    

    

## Special Access Rules

To know the products and user permissions needed to access this type, See [Supported Editions and Permissions for Batch
          Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              
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

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| batchSize | integer | Required. Number of records that each Batch Management job can process. Flow type Batch Management jobs can process up to 2000 records and Loyalty Program Process type Batch Management jobs can process up to 250 records. |
| dataSource | [BatchDataSource](#batchdatasourceID)[] | Required. Source of information whose records must be processed by the Batch Management job. |
| description | string | Description of the Batch Management job, up to 255 characters. |
| executionProcessApiName | string | API name of process that must be executed by the Batch Management job. This field is available in API version 55.0 and later. If the batch job’s type is Flow, enter the API name of an active flow that the batch job must execute. If the batch job’s type is Loyalty Program Process, enter: Transaction_Journals if you want the batch job to process Transaction Journal records by applying the applicable active loyalty program process of the type TransactionJournal. API name of an active loyalty process of the type TierProcessing if you want the batch job to run the loyalty program process to assess the tier of eligible members. The API name consists of the name of the process, the process type, and the name of the loyalty program separated by two consecutive underscores. For example, the process API name is `Update Member Tier__TierProcessing__Inner Circle` if the process name is Update Member Tier, the process type is TierProcessing, and the loyalty program name is Inner Circle. You can use database-based APEX classes that let you use flex queues in the Batch Management job, allowing to place more than 5 jobs in a queue. This functionality is applicable to all Industry Clouds that use managed packages. See [Apex Flex Queue](https://help.salesforce.com/s/articleView?id=platform.code_apex_flex_queue.htm&type=5&language=en_US). |
| flowApiName | string | API name of an active flow process that must be executed by the Batch Management job.You can either specify the flow API name in the `executionProcessApiName` field or in the `flowApiName` field. |
| flowInputVariable | string | Input variable of associated flow that is used by the batch job to uniquely identify records. |
| masterLabel | string | Required. Name of the Batch Management job, up to 80 characters. |
| processGroup | string | Required. Name of the group for which the Batch Management job processes records. |
| retryCount | integer | Required. Number of times this Batch Management job must be rerun in case it fails. The maximum retry count is 3. Valid values are 1–3. |
| retryInterval | integer | Required. Number of milliseconds after which the Batch Management job must be rerun in case it fails. Valid values are 1,000–10,000. |
| status | string | Indicates the status of the Batch Management job. Valid values are `Active` and `Inactive`. |
| type | string (enumeration of type string) | The type of process that the Batch Management job must execute. This field is available in API version 55.0 and later. Valid values are: `BulkUpdate` `Calc`—Data Processing Engine `ConsumptionOveragesCalculation` `DecisionTableRefresh` `DeepCloneSalesAgreement` `FlattenAccountIOUHierarchyBatchJob` `Flow` `EnergyUseRecordCreationBatchJob` `EntitlementCreationBatchJob` `HighScaleBreProcess` `IndustriesLSCommercial` `InvoiceDTPRunBatchJob` `InvoiceRecoveryRunBatchJob` `InvoiceRunBatchJob` `LifeSciProviderActivityGoalSharingBatchJob` `LoyaltyProgramProcess` `NetUnitRateCalculation` `NextGenCommitmentBatchProcessingJob` `ManagerProvisioning` `PbbToOptyConversion` `ProductCatalogCacheRefresh` `PromotionChannelPropagationBatchJob` `RatableSummaryCreation` `ServiceProcess` `StoreAssortmentPropagationBatchJob` `SummaryCreation` `WorkDotComToHRManagerProvisioning` |

    

    

## BatchDataSource

      
    

    
      

Represents the source of information whose records must be processed by the Batch
        Management job.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              
- 
- 

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

- 
- 

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| condition | string | Required. Criteria defined to filter the records. |
| criteria | string | Type of filter criteria that’s used to filter records for processing. |
| dataSourceType | string | Type of data source that's used to create the batch job definition. Valid values are: SingleSobject MultiSobject Available in API version 64.0 and later. |
| filters | [BatchDataSrcFilterCriteria](#batchdatasrcfiltercriteriaID)[] | Filter criterion that decides which records must be processed by the Batch Management job. |
| orderFields | [BatchDataSourceOrderField](#BatchDataSourceOrderField) | Fields that are used to order the records before the records are added to a batch in a job. |
| sourceObject | string | Required. API name of an object whose records must be processed by the batch job. If the batch job type is Loyalty Program Process, the source object must be: TransactionJournal if the batch job is used to process transaction journals by applying the applicable loyalty program process. An object that stores the details of loyalty program members whose tier must be assessed by the loyalty program process specified in the executionProcessApiName field. |
| sourceObjectField | string | API name of the source object field that uniquely identifies records for which the batch job is executed. This field is available in API version 57.0 and later.This field is only applicable when the batch job’s type is Loyalty Program Process and a TierProcess type active loyalty program process is specified in the executionProcessApiName field. Specify the API name of a field that is a lookup to the LoyaltyProgramMember object and uniquely identifies the members whose tier must be assessed. |

    

    

## BatchDataSrcFilterCriteria

      
    

    
      

Represents the filter conditions that decide which records must be processed by the Batch
        Management job.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

            
              

              

              
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
| domainObjectName | string | Name of the object the field is associated with. Available in API version 64.0 and later. |
| dynamicValueType | string | Data type of the input variable used as a filter. |
| fieldName | string | Required. Name of the field that must be used to filter records. |
| fieldPath | string | Stores the path to a field in the object. Available in API version 64.0 and later. |
| fieldValue | string | Required. Value of the field that must be filtered. Specify the field if `isDynamicValue` is set to `False`. |
| isDynamicValue | boolean | Required. Indicates whether the filter criteria is dynamic. |
| operator | string (enumeration of type string) | Required. Operator that is specified in the filter criteria. Valid values are: `equals` `excludes` `greaterThan` `greaterThanOrEqualTo` `in` `includes` `lessThan` `LessThanOrEqualTo` `GreaterOrEqual` `like` `notEquals` `notIn` |
| sequenceNo | integer | Required. Sequence number used to refer the criteria in a filter. |

    

    

## BatchDataSourceOrderField

      
    

    
      

Represents the fields that are used to group data.

    

    

## Fields

      
      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              

            

            
              

              

              

            

            
              

              

              

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| domainObjectName | string | Required. Name of the object the field is associated with. Available in API version 64.0 and later. |
| fieldName | string | Required. Name of the field that must be used to filter records. Available in API version 64.0 and later. |
| fieldPath | string | Required. Stores the path to a field in the object. Available in API version 64.0 and later. |

    

    

## Declarative Metadata Sample Definition

      
      

The following is an example of a BatchProcessJobDefinition component.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<BatchProcessJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">
   <batchSize>10</batchSize>
   <dataSource>
      <condition>1</condition>
      <criteria>all</criteria>
      <filters>
         <dynamicValue>false</dynamicValue>
         <dynamicValueType>string</dynamicValueType>
         <fieldName>Name</fieldName>
         <fieldValue>abcd</fieldValue>
         <operator>equals</operator>
         <sequenceNo>1</sequenceNo>
      </filters>
      <sourceObject>Account</sourceObject>
   </dataSource>
   <flowApiName>Flow1</flowApiName>
   <flowInputVariable>recordId</flowInputVariable>
   <masterLabel>BatchJob1</masterLabel>
   <processGroup>Loyalty</processGroup>
   <retryCount>2</retryCount>
   <retryInterval>1000</retryInterval>
   <status>Inactive</status>
   <description>test</description>
   <type>Flow</type>
   <executionProcessApiName>testFlow</executionProcessApiName>
</BatchProcessJobDefinition>
```

      

The following is an example of a Flow object used in Metadata API.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<!--
   ~ Copyright 2020 Salesforce, Inc.
   ~ All Rights Reserved
   ~ Company Confidential
-->
<Flow xmlns="http://soap.sforce.com/2006/04/metadata">
   <apiVersion>51.0</apiVersion>
   <interviewLabel>Flow1 {!$Flow.CurrentDateTime}</interviewLabel>
   <label>Flow1</label>
   <processMetadataValues>
      <name>BuilderType</name>
      <value>
         <stringValue>LightningFlowBuilder</stringValue>
      </value>
   </processMetadataValues>
   <processMetadataValues>
      <name>OriginBuilderType</name>
      <value>
         <stringValue>LightningFlowBuilder</stringValue>
      </value>
   </processMetadataValues>
   <processType>AutoLaunchedFlow</processType>
   <recordLookups>
      <name>getAcc</name>
      <label>getAcc</label>
      <locationX>614</locationX>
      <locationY>465</locationY>
      <assignNullValuesIfNoRecordsFound>false</assignNullValuesIfNoRecordsFound>
      <filterLogic>and</filterLogic>
      <filters>
         <field>Id</field>
         <operator>EqualTo</operator>
         <value>
            <elementReference>recordId</elementReference>
         </value>
      </filters>
      <getFirstRecordOnly>true</getFirstRecordOnly>
      <object>Account</object>
      <storeOutputAutomatically>true</storeOutputAutomatically>
   </recordLookups>
   <start>
      <locationX>73</locationX>
      <locationY>213</locationY>
      <connector>
         <targetReference>getAcc</targetReference>
      </connector>
   </start>
   <status>Draft</status>
   <variables>
      <name>recordId</name>
      <dataType>String</dataType>
      <isCollection>false</isCollection>
      <isInput>true</isInput>
      <isOutput>false</isOutput>
   </variables>
</Flow>
```

      

The following is an example `package.xml` that
        references the previous definition.

      

```

<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
   <types>
      <members>*</members>
      <name>BatchProcessJobDefinition</name>
   </types>
   <types>
      <members>Flow1</members>
      <name>Flow</name>
   </types>
   <version>51.0</version>
</Package>
```

    

    

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

=== ARTICLE: monitor_workflow_services_dev_overview.htm ===
---
page_id: monitor_workflow_services_dev_overview.htm
title: Monitor Workflow Services
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/monitor_workflow_services_dev_overview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Monitor Workflow Services

The Monitor Workflow Services standard objects can be used to track the run of Data
  Processing Engine definitions and Batch Management jobs. During a run, you can view details about
  each part that the run is broken down into. After the run is complete, you can view its status and
  the records which weren't processed during the run. 

  

    
     
      

     

     
      

     

    

   
| Available in: Lightning Experience |
| --- |
| Available in: Monitor Workflow Services is available with Enterprise, Unlimited, and Performance Editions where Data Processing Engine or Batch Management is available |

  

  

The objects of Monitor Workflow Services aren't available in Object Manager of your Salesforce
   org.

 

- 
**[BatchJob](./sforce_api_objects_batchjob.htm.md)**  

     Represents an instance of a batch job that is either running and has been       run. This object is available in API version 51.0 and later. 

- 
**[BatchJobPart](./sforce_api_objects_batchjobpart.htm.md)**  

     Represents one part of a batch job. This object is available in API     version 51.0 and later. 

- 
**[BatchJobPartFailedRecord](./sforce_api_objects_batchjobpartfailedrecord.htm.md)**  

     Represents records that a batch job part couldn't successfully process.     This object is available in API version 51.0 and later.

=== ARTICLE: sforce_api_objects_batchcalcjobdefinitionview.htm ===
---
page_id: sforce_api_objects_batchcalcjobdefinitionview.htm
title: BatchCalcJobDefinitionView
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchcalcjobdefinitionview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_standard_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchCalcJobDefinitionView

Represents the details of a Data Processing Engine definition. The
      definition can also be a file-based definition that is available in your Salesforce org.
    This object is available in API version 51.0 and later.

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## Supported Calls

      
      

`describeSObjects()`, `query()`

    

    

## Special Access Rules

      
      

To know the permissions needed to access this view, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US).

    

    

## Fields

      
      

          
          
          
            
              

              

            

          

          
            
              

              

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

            

          

        
| Field | Details |
| --- | --- |
| CurrencyConversion | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies whether currency values must be converted when the definition is run. Possible values are: `Enabled` `Disabled` `None` |
| DataSpaceApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Stores the data space API name from Data Cloud. |
| DefinitionRunMode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The execution mode of the Data Processing Engine definition. Possible values are: `Batch` `OnDemand`—On Demand The default value is `Batch`. |
| Description | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The description of a Data Processing Engine definition. |
| DurableId | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier for the field. Always retrieve this value before using it, as the value isn’t guaranteed to stay the same from one release to the next. Simplify queries by using this field instead of making multiple queries. |
| ExecutionPlatformObjectType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the execution platform object type used to read, transform, and write back processes during the execution of a Data Processing Engine definition. This field is available in API version 65.0 and later. Possible values are: `CalculatedInsightsObject`—Calculated Insights Object `DataLakeObject`—Data Lake Object `DataModelObject`—Data Model Object `None` |
| ExecutionPlatformType | **Type** Picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies the platform that's used to run the Data Processing Engine definition. Possible values: `CDP`—Data Cloud `CRMA`—CRM Analytics |
| InstalledPackageName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the package used to add the definition to the org. |
| IsActive | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the definition is active. |
| IsTemplate | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the definition is a template. You can make a copy of a template definition and update it based on your requirements. |
| LastModifiedBy | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the user who modified the definition last. |
| LastModifiedDate | **Type** datetime **Properties** Filter, Sort **Description** The date and time when the definition was last modified. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the definition if it’s contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The label of the Data Processing Engine definition. |
| Name | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the Data Processing Engine definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the namespacePrefix__componentName notation.The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There’s an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that aren’t Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There’s no namespace prefix for all other objects. |
| ProcessType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The process type of the definition. Possible values are: `AccountingPeriodClosure`—Legal Entity Accounting Period Closure—Available in API version 62.0 and later. `AccrualsAndPayoutEngine` `ActionableList` `AdvancedAccountForecast` `AutomotiveFoundation` `BenefitManagement`—Available in API version 61.0 and later. `BillingSchedulesforInvoiceGeneration`—Billing Schedules for Invoice Generation—Available in API version 62.0 and later. `CDPEnrichment` `ChannelInventoryManagement`—Available in API version 63.0 and later. `CollectionsAndRecovery` `ContextService—Available in API version 67.0 and later.` `CriteriaBsdSearchAndFilter - Criteria-Based Search And Filter` `DataProcessingEngine - Standard` `DecisionMatrixDataUpload`-This value is available only if you have Business Rules Engine enabled. `Decisiontable`—Decision table activation—Available in API version 62.0 and later. `Education` `EmployeeService`—Available in API version 63.0 and later. `EnergyUtilitiesSales` `FinancialSummaryRollup`—Available in API version 63.0 and later. `FlexibleHierarchy` `ForeignExchangeGainLossCalculations` `FSCHierarchyRollUp` `Fundraising` `FundraisingRollups`—Available in API version 63.0 and later. `GeneralLedgerAccountBalancesSummary` `InventoryBatchSearch` `InventorySearch` `InvoiceGeneration`—Available in API version 62.0 and later. `LegalEntityAccountingPeriodClosureAdvanced`—Available in API version 63.0 and later. `LifeSciencesCommercialTerritoryAlignment`—Available in API version 63.0 and later. `LifeSciencesCustomerEngagement` `Loyalty` `LoyaltyPartnerManagement` `LoyaltyPointsAggregation` `MediaAdSales` `NetZero` `NextGenForecasting`—Available in API version 62.0 and later. `PatientServicesProgram` `PlanningAndForecasting` `PnmRosterFileUpload`—Available in API version 62.0 and later. `PriceProtection`—Available in API version 62.0 and later. `ProductCatalogManagement`—Available in API version 63.0 and later. `ProgramBasedBusiness` `ProgramManagementRollups` `Rebates` `RebateAndAccrualManagementAdvanced` `RecordAggregation` `RevenueTransactionManagement`—Available in API version 63.0 and later. `AccountingSubledger`—This value is reserved for internal use. `ProviderSearch`—This value is reserved for internal use. `Recruitment`—Available in API version 62.0 and later. `SalesAgreement`—Available in API version 63.0 and later. `StockRotation` `UsageManagement`—Available in API version 62.0 and later. When Data Processing Engine is enabled for a Salesforce org, the default value is 'Standard’. Other process types may be available to you depending on your industry solution and permission sets. |
| TargetCurrencyIsoCode | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies the ISO code of the target currency used to convert currency values when the definition is run. |

=== ARTICLE: sforce_api_objects_batchjob.htm ===
---
page_id: sforce_api_objects_batchjob.htm
title: BatchJob
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchjob.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: monitor_workflow_services_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchJob

    Represents an instance of a batch job that is either running and has been
      run. This object is available in API version 51.0 and later. 

    

## Supported Calls

      
      

        `delete()`, `describeLayout()`, `describeSObjects()`,
          `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
          `undelete()`
      

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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

: 
: 

            

            
              

              

: 

: 

: 
: 
: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 
: 

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

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
| AdditionalInformation | **Type** textarea **Properties** Create, Nillable, Update **Description** A JSON that contains additional context about the batch jon. |
| ApiVersion | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The Salesforce API version in which this definition was created. |
| BatchJobDefinitionId | **Type** reference **Properties** Filter, Group, Sort **Description** The unique identifier of the associated batch job definition. This is a relationship field. **Relationship Name** BatchJobDefinition **Relationship Type** Lookup **Refers To** BatchJobDefinition |
| BatchJobDefinitionName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the associated batch job definition. |
| DefinitionType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of batch calculation job definition that was used to create this batch job. Possible values are: `Calcservice` |
| EndTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the batch job run was completed. |
| ErrorDescription | **Type** string **Properties** Filter, Nillable, Sort **Description** The error message in case the batch job run failed. |
| ExecutionStage | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the stage at which the batch job's run failed. This field is available in API version 66.0 and later. Possible values are: `Datasync` `Execution` `Preprocessing` `Writeback` |
| ExternalReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the process that's running or has run the batch job. |
| IsDebugOn | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether debug mode was turned on (true) or not (false) when a definition was run. The default value is `false`. |
| IsDebugRecipeDeleted | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether debug recipes and datasets were deleted (true) or not (false). When the IsDebugOn is set to True, and the definition is run, after 7 days IsDebugRecipeDeleted is automatically set to True, and debug recipes and datasets are deleted. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed the batch job. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this item. |
| Name | **Type** string **Properties** Filter, Group, idLookup, Sort **Description** The name of the batch job. |
| OwnerId | **Type** reference **Properties** Filter, Group, Sort **Description** Unique identifier of the user who initiated the batch job run. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ProcessGroup | **Type** string **Properties** Filter, Group, Sort **Description** The group or team for which the batch job is run. |
| QueuingRetryCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The number of times the scheduler attempted to queue the batch job before succeeding. |
| RetryCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of times the batch job run is automatically rerun in case it fails. |
| RunByUser | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the user who initiated the batch job execution. |
| RuntimeParameter | **Type** textarea **Properties** Nillable **Description** The values of the input variables that are used as filter criteria in a Batch Management job. |
| StartTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the batch job run was started. |
| Status | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The status of the batch job run. Possible values are: `Canceled` `Canceling` `Completed` `CompletedWithFailures` `Failed` `InProgress` `Queued` `QueueingInProgress` `Submitted` |
| TotalInputRecordCount | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The total number of records that were provided as input to the batch job. This field is available in API version 66.0 and later. |
| TotalProcessedRecordCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The total number of records that were processed by all the batch job parts associated with the batch job. This field is available in API version 66.0 and later. |
| TriggerType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the mode with which this batch job is triggered. Possible values are: `API` `RunNow` `Schedule` |
| Type | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** The type of batch job that is run. Possible values are: `BulkUpdate` `Calc`—Data Processing Engine `ConsumptionOveragesCalculation` `DecisionTableRefresh` `DeepCloneSalesAgreement` `FlattenAccountIOUHierarchyBatchJob` `Flow` `EnergyUseRecordCreationBatchJob` `EntitlementCreationBatchJob` `HighScaleBreProcess` `IndustriesLSCommercial` `InvoiceDTPRunBatchJob` `InvoiceRecoveryRunBatchJob` `InvoiceRunBatchJob` `LifeSciProviderActivityGoalSharingBatchJob` `LoyaltyProgramProcess` `NetUnitRateCalculation` `NextGenCommitmentBatchProcessingJob` `ManagerProvisioning` `PbbToOptyConversion` `ProductCatalogCacheRefresh` `PromotionChannelPropagationBatchJob` `RatableSummaryCreation` `ServiceProcess` `StoreAssortmentPropagationBatchJob` `SummaryCreation` `WorkDotComToHRManagerProvisioning` The process types available to you vary depending on the licenses available in your org. |
| UtilisedExecutionLimit | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The CRM Analytics or Data 360 execution capacity utilized by Data Processing Engine batch jobs before the current run started. This field is available in API version 66.0 and later. |
| UtilisedWritebackLimit | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The CRM Analytics or Data 360 writeback capacity utilized by Data Processing Engine batch jobs before the current run started. This field is available in API version 66.0 and later. |

    

    

## Associated Objects

      
      

This object has the following associated objects. If the API version isn’t specified,
        they’re available in the same API versions as this object. Otherwise, they’re available in
        the specified API version and later.

      
        
          

**BatchJobFeed**

          
: Feed tracking is available for the object.

        
        
          

**BatchJobHistory**

          
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_batchjobpart.htm ===
---
page_id: sforce_api_objects_batchjobpart.htm
title: BatchJobPart
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchjobpart.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: monitor_workflow_services_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchJobPart

    Represents one part of a batch job. This object is available in API
    version 51.0 and later. 

    
      

When a batch job is run, it is divided in to multiple parts. Each part is used to process a
        specific number of records.

    

    

## Supported Calls

      
      

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
          `retrieve()`

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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
- 
- 

            

            
              

              

: 

: 

: 

            

          

        
| Field | Details |
| --- | --- |
| AdditionalInformation | **Type** string **Properties** Filter, Nillable, Sort **Description** Contains additional information on the batch job part. |
| BatchJobId | **Type** reference **Properties** Filter, Group, Sort **Description** The unique identifier of the associated batch job. This is a relationship field. **Relationship Name** BatchJob **Relationship Type** Lookup **Refers To** BatchJob |
| EndTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the batch job part was processed. |
| ErrorDescription | **Type** string **Properties** Filter, Nillable, Sort **Description** The error message in case the batch job part failed. |
| FailedRecFileBody | **Type** base64 **Properties** Nillable **Description** Contains the details of the records that the batch job part failed to process. |
| FailedRecFileContentType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Shows the type of data that the batch job part failed to process. For example, `application/html` or `text/csv` or `text/vcard`. |
| FailedRecFileLength | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The character length of the failed record file. |
| FailedRecFileName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the file that contains the details of the failed records. |
| FailedRecordCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of records that the batch job part couldn't process. |
| FailedRowCount | **Type** long **Properties** Filter, Group, Nillable, Sort **Description** The number of records that were processed but the batch job part failed to write back for a Data Processing Engine definition run. This field is available in API version 66.0 and later. |
| InputRecordCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of records that the batch job part must process. |
| InputRowCount | **Type** long **Properties** Filter, Group, Nillable, Sort **Description** The number of records that were submitted to the batch job part for a Data Processing Engine definition run. This field is available in API version 66.0 and later. |
| Name | **Type** string **Properties** Filter, Group, idLookup, Sort **Description** The name of the batch job part. |
| OutputRecordCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of records the batch job part has processed. |
| OutputRowCount | **Type** long **Properties** Filter, Group, Nillable, Sort **Description** The number of records that were processed by the batch job part for a Data Processing Engine definition run. This field is available in API version 66.0 and later. |
| ParentBatchJobPartId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the part batch job part associated with the batch job part. This is a relationship field. **Relationship Name** ParentBatchJobPart **Relationship Type** Lookup **Refers To** BatchJobPart |
| RecordFileBody | **Type** base64 **Properties** Nillable **Description** Contains the details of the records that the batch job part processed. |
| RecordFileContentType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Shows the type of data that the batch job part processed. For example, `application/html` or `text/csv` or `text/vcard`. |
| RecordFileLength | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The character length of the file that contains the records that the batch job part processed. |
| RecordFileName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the file that contains the details of the records that the batch job part processed. |
| RetryCount | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The number of times the batch job part is automatically rerun in case it fails. |
| StartTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the batch job part's run was started. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** The status of the batch job part. Possible values are: `Canceled` `Completed` `CompletedWithFailures` `Failed` `InProgress` `New` `Waiting` |
| Type | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of node in case the associated batch job is of the type Calc (Data Processing Engine). Possible values are: `Aggregate` `Analysis` `Append` `AtomicWriteback` `Compute` `CsvIngestion` `Custom` `Datasync` `Execution` `Filter` `Forecast` `Hierarchy` `Join` `OutputRecordsNode` `Register` `Slice` `Source` `Summary` `Transform` `Writeback` |
| UserReference | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The ID of the user who is assigned as the writeback user in the Writeback Object node of the Data Processign Engine definition for which the batch job part has written back results. This field is available in API version 66.0 and later. |

    

    

## Associated Objects

      
      

This object has the following associated objects. If the API version isn’t specified,
        they’re available in the same API versions as this object. Otherwise, they’re available in
        the specified API version and later.

      
        
          

**BatchJobPartFeed**

          
: Feed tracking is available for the object.

        
        
          

**BatchJobPartHistory**

          
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_batchjobpartfailedrecord.htm ===
---
page_id: sforce_api_objects_batchjobpartfailedrecord.htm
title: BatchJobPartFailedRecord
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchjobpartfailedrecord.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: monitor_workflow_services_dev_overview.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchJobPartFailedRecord

    Represents records that a batch job part couldn't successfully process.
    This object is available in API version 51.0 and later. 

    

## Supported Calls

      
      

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
          `retrieve()`

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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
- 
- 

: 

            

          

        
| Field | Details |
| --- | --- |
| BatchJobId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the associated batch job. This is a relationship field. **Relationship Name** BatchJob **Relationship Type** Lookup **Refers To** BatchJob |
| BatchJobPartId | **Type** reference **Properties** Filter, Group, Sort **Description** The unique identifier of the associated batch job part. This is a relationship field. **Relationship Name** BatchJobPart **Relationship Type** Lookup **Refers To** BatchJobPart |
| ErrorDescription | **Type** string **Properties** Filter, Nillable, Sort **Description** The error message that indicates why the batch job part couldn't process the records. |
| Name | **Type** string **Properties** Filter, Group, idLookup, Sort **Description** The name of the batch job part failed record. |
| ProcessingGroupKey | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Length** 100 **Description** The field used for creating batch job parts. It can be a Group By field selected from the UI or a Partition Key from the API. |
| Record | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the batch record that processed the failed records. |
| RecordName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the record that's associated with the batch job part failed record. |
| ResubmittedBatchJobId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The batch job used to submit failed records. This field is available in API version 52.0 and later. This is a relationship field. **Relationship Name** ResubmittedBatchJob **Relationship Type** Lookup **Refers To** BatchJob |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the status of the failed records. This field is available in API version 52.0 and later. Possible values are: `Failed` `Resubmitted` The default value is 'Failed'. |

    

    

## Associated Objects

      
      

This object has the following associated objects. If the API version isn’t specified,
        they’re available in the same API versions as this object. Otherwise, they’re available in
        the specified API version and later.

      
        
          

**BatchJobPartFailedRecordFeed**

          
: Feed tracking is available for the object.

        
        
          

**BatchJobPartFailedRecordHistory**

          
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_batchjobstatuschangedevent.htm ===
---
page_id: sforce_api_objects_batchjobstatuschangedevent.htm
title: BatchJobStatusChangedEvent
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchjobstatuschangedevent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_platform_event.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchJobStatusChangedEvent

Notifies subscribers of when a batch job is completed in a
			flow. This object is available in API version 51.0 and later.

		

## Supported Calls

			
			

`describeSObjects()`

		

		

## Supported Subscribers

			
			

					
					
					
						
							

							

						

					

					
						
							

							

						

					

				
| Subscriber | Supported? |
| --- | --- |
| Flows |  |

		

		

## Special Access Rules

			
			

To know the permissions needed to access this event, See [User Permissions for Data Processing
					Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

		

		

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

						

					

				
| Field | Details |
| --- | --- |
| BatchJob | **Type** string **Description** The unique identifier of the batch job. |
| BatchJobDefinition | **Type** string **Properties** Nillable **Description** The unique identifier of the batch job's definition. |
| EndDateTime | **Type** dateTime **Properties** Nillable **Description** The timestamp for when the batch job execution is complete. |
| EventUuid | **Type** string **Properties** Nillable **Description** A universally unique identifier (UUID) that identifies a platform event message. This field is available in API version 52.0 and later. |
| ReplayId | **Type** string **Properties** Nillable **Description** Represents an ID value that is populated by the system and refers to the position of the event in the event stream. Replay ID values aren’t guaranteed to be contiguous for consecutive events. A subscriber can store a replay ID value and use it on resubscription to retrieve missed events that are within the retention window. |
| StartDateTime | **Type** dateTime **Properties** Nillable **Description** The timestamp for when the batch job execution is started. |
| Status | **Type** picklist **Properties** Restricted picklist **Description** The status of the batch job. Possible values are: `Canceled`—Canceled `Failure` `Success` |

=== ARTICLE: sforce_api_objects_batchprocessjobdefview.htm ===
---
page_id: sforce_api_objects_batchprocessjobdefview.htm
title: BatchProcessJobDefView
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_batchprocessjobdefview.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_standard_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchProcessJobDefView

    Represents the details of a Batch Job definition. The definition can also be
      file-based definitions that are available in your Salesforce org. This object is
    available in API version 51.0 and later.

    

## Supported Calls

      
      

`describeSObjects()`, `query()`

    

    

## Special Access Rules

      
      

To know the permissions needed to access this view, See [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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

            

            
              

              

: 

: 

: 

            

            
              

              

: 

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
| DurableId | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier for the field. Always retrieve this value before using it, as the value isn’t guaranteed to stay the same from one release to the next. Simplify queries by using this field instead of making multiple queries. |
| IsActive | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the definition is active. |
| Label | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The label of the Batch Job definition. |
| Name | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the Batch Job definition. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the namespacePrefix__componentName notation.The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |
| ProcessDefinition | **Type** textarea **Properties** Nillable **Description** The name of the process group for the batch process job definition. |
| ProcessGroup | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The team or group for which the definition processes records. |
| SourceObjectName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The API name of the object whose records are processed. |
| Type | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The type of process for which the Batch Management job processes records. Possible values are: `Flow` `LoyaltyProgramProcess` This field is available in API version 55.0 and later. |
| TypeInstance | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The API name of the process that's processed by the Batch Job definition. |

=== ARTICLE: tooling_api_objects_batchcalcjobdefinition.htm ===
---
page_id: tooling_api_objects_batchcalcjobdefinition.htm
title: BatchCalcJobDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_batchcalcjobdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: data_processing_engine_setup_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchCalcJobDefinition

Represents a Data Processing Engine (DPE) definition. This object
    is available in API version 51.0 and later.

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## Supported SOAP API Calls

      
      

        `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`,
          `update()`, `upsert()`
      

    

    

## Supported REST API Methods

      
      

`DELETE, GET, HEAD, PATCH, POST, Query`
      

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US).

    

    

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

            

          

        
| Field | Details |
| --- | --- |
| ApiVersion | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The Salesforce API version in which this definition was created. |
| BatchJobDefinitionId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the associated batch job definition. This is a relationship field. **Relationship Name** BatchJobDefinition **Relationship Type** Lookup **Refers To** BatchJobDefinition |
| CurrencyConversion | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies whether currency values must be converted when the definition is run. Possible values are: `Enabled` `Disabled` `None` |
| DataSpaceApiName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The Data Space API name from Data Cloud. |
| DefinitionRunMode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The execution mode of the Data Processing Engine definition. Possible values are: `Batch` `OnDemand`—This value is reserved for internal use. The default value is `Batch`. |
| DefinitionType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of batch calculation job definition that was used to create this batch job. Possible values are: `Calcservice` |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the Data Processing Engine definition. |
| DoesGenAllFailedRecords | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the error file includes a complete list of all failed writeback records (`true`) or not (`false`). The default value is `false`, and only the first instance of a failure is recorded in the error file. If set to `true`, all failed records are recorded in the error file for the writeback node.Available in API version 65.0 and later. |
| ExecutionPlatformObjectType | **Type** Picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Required. The execution platform object type that's used during the read, transform, and writeback process for the Data Processing Engine definition. Possible values are: `CalculatedInsightsObject` `DataLakeObject` `DataModelObject` `None` Available in API version 65.0 and later. |
| ExecutionPlatformType | **Type** Picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies the platform that's used to run the Data Processing Engine definition. Possible values: `CDP`—Data Cloud `CORE`—This value is reserved for internal use. `CRMA`—CRM Analytics |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** The name of the Data Processing Engine definition. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| IsTemplate | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether this is a template Data Processing Engine definition. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which this Data Processing Engine definition is created. |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the Data Processing Engine definition. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** Data Processing Engine definition's metadata. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation.The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There’s an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that aren’t Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There’s no namespace prefix for all other objects. |
| ProcessType | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Required. The process type for which the Data Processing Engine definition is created. Possible values are: `AccountingPeriodClosure`—Legal Entity Accounting Period Closure—Available in API version 62.0 and later. `AccrualsAndPayoutEngine` `ActionableList` `AdvancedAccountForecast` `AutomotiveFoundation` `BenefitManagement`—Available in API version 61.0 and later. `BillingSchedulesforInvoiceGeneration`—Billing Schedules for Invoice Generation—Available in API version 62.0 and later. `CDPEnrichment` `ChannelInventoryManagement`—Available in API version 63.0 and later. `CollectionsAndRecovery` `ContextService—Available in API version 67.0 and later.` `CriteriaBsdSearchAndFilter - Criteria-Based Search And Filter` `DataProcessingEngine - Standard` `DecisionMatrixDataUpload`-This value is available only if you have Business Rules Engine enabled. `Decisiontable`—Decision table activation—Available in API version 62.0 and later. `Education` `EmployeeService`—Available in API version 63.0 and later. `EnergyUtilitiesSales` `FinancialSummaryRollup`—Available in API version 63.0 and later. `FlexibleHierarchy` `ForeignExchangeGainLossCalculations` `FSCHierarchyRollUp` `Fundraising` `FundraisingRollups`—Available in API version 63.0 and later. `GeneralLedgerAccountBalancesSummary` `InventoryBatchSearch` `InventorySearch` `InvoiceGeneration`—Available in API version 62.0 and later. `LegalEntityAccountingPeriodClosureAdvanced`—Available in API version 63.0 and later. `LifeSciencesCommercialTerritoryAlignment`—Available in API version 63.0 and later. `LifeSciencesCustomerEngagement` `Loyalty` `LoyaltyPartnerManagement` `LoyaltyPointsAggregation` `MediaAdSales` `NetZero` `NextGenForecasting`—Available in API version 62.0 and later. `PatientServicesProgram` `PlanningAndForecasting` `PnmRosterFileUpload`—Available in API version 62.0 and later. `PriceProtection`—Available in API version 62.0 and later. `ProductCatalogManagement`—Available in API version 63.0 and later. `ProgramBasedBusiness` `ProgramManagementRollups` `Rebates` `RebateAndAccrualManagementAdvanced` `RecordAggregation` `RevenueTransactionManagement`—Available in API version 63.0 and later. `AccountingSubledger`—This value is reserved for internal use. `ProviderSearch`—This value is reserved for internal use. `Recruitment`—Available in API version 62.0 and later. `SalesAgreement`—Available in API version 63.0 and later. `StockRotation` `UsageManagement`—Available in API version 62.0 and later. When Data Processing Engine is enabled for a Salesforce org, the default value is 'Standard’. Other process types may be available to you depending on the licenses available in your org. |
| TargetCurrencyIsoCode | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort, Not-Nillable **Description** Specifies the ISO code of the target currency used to convert currency values when the definition is run. |

=== ARTICLE: tooling_api_objects_batchdatasource.htm ===
---
page_id: tooling_api_objects_batchdatasource.htm
title: BatchDataSource
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_batchdatasource.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_setup_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchDataSource

      Represents the source of information from which a batch job retrieves records
         for processing. This object is available in API version 66.0 and later.

      

## Supported Calls

         
         

            `describeSObjects()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

         
         

To know the permissions needed to access this object, See [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

      

      

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
| BatchJobDefinitionId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the batch job definition associated with batch data source. This field is a relationship field. **Relationship Name** BatchJobDefinition **Relationship Type** Master-detail **Refers To** BatchJobDefinition (the master object) |
| CriteriaJoinCondition | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The logic that's used to decide how data source records are filtered. |
| CriteriaJoinType | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Specifies the criteria type used to filter data source records. Possible values are: `all`—All conditions are met (AND) `any`—Any condition is met (OR) `custom`—Customize the logic `none`—No conditions are met The default value is `all`. |
| DataSourceType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the type of data source. Possible values are: `MultipleSobjects` `SingleSobject` `File` |
| RelatedSobjects | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The list of objects that are used as data sources for the batch job definition. |
| SourceFieldName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The field from the source object that's used to run the batch job. |
| SourceTableName | **Type** string **Properties** Filter, Group, Sort **Description** The name of the object from which records are processed by the batch job. |

=== ARTICLE: tooling_api_objects_batchdatasrcfiltercriteria.htm ===
---
page_id: tooling_api_objects_batchdatasrcfiltercriteria.htm
title: BatchDataSrcFilterCriteria
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_batchdatasrcfiltercriteria.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_setup_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchDataSrcFilterCriteria

      Represents the details of a condition in the filter criteria used to retrieve
         records from the data source of a batch job. This object is available in API version
      66.0 and later. 

      

## Supported Calls

         
         

            `describeSObjects()`, `query()`, `retrieve()`
         

      

      

## Special Access Rules

         
         

To know the permissions needed to access this object, See [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

      

      

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
| BatchDataSourceId | **Type** reference **Properties** Filter, Group, Sort **Description** The ID of the batch data source associated with the batch data source filter criteria. This field is a relationship field. **Relationship Name** BatchDataSource **Relationship Type** Master-detail **Refers To** BatchDataSource (the master object) |
| DomainObjectName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the object that contains the field that's used in the filter criteria condition. |
| DynamicValueType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the data type of the input variable that's used in the filter criteria condition. Possible values are: `boolean` `currency` `date` `datetime` `double` `integer` `long` `number` `picklist` `reference` `string` |
| FieldName | **Type** string **Properties** Filter, Group, Sort **Description** The name of the field that's used in the filter criteria condition. |
| FieldPath | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The patch of the related object field that's used in the filter criteria condition. |
| FieldValue | **Type** string **Properties** Filter, Group, Sort **Description** The value of the specified field used to filter records of the data source. |
| FilterCriteriaSequence | **Type** int **Properties** Filter, Group, Sort **Description** The sequence number of the condition in the filter criteria. |
| IsDynamicValue | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the value of the filter criteria condition is provided by an input variable. The default value is `false`. |
| Operator | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Specifies the operator used in the filter criteria condition. Possible values are: `equals`—Equals `excludes`—Excludes `greaterThan`—Greater Than `greaterThanOrEqualTo`—Greater Than Or Equal To `in`—In `includes`—Includes `isNotNull`—Is Not Null `isNull`—Is Null `lessThan`—Less Than `lessThanOrEqualTo`—Less Than Or Equal To `like`—Like `notEquals`—Not Equals `notIn`—Not In |

=== ARTICLE: tooling_api_objects_batchjobdefinition.htm ===
---
page_id: tooling_api_objects_batchjobdefinition.htm
title: BatchJobDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_batchjobdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_common_setup_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchJobDefinition

    Represents the definition of a batch job. This object is available in API
    version 51.0 and later. 

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    

## Supported SOAP API Calls

      
      

`describeSObjects()`, `query()`, `retrieve()`

    

    

## Supported REST API Methods

      
      

`GET, HEAD, Query`
      

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_setup.htm&language=en_US) or [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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

            

          

        
| Field | Details |
| --- | --- |
| Description | **Type** textarea **Properties** Filter, Group, Nillable, Sort **Description** The description of the batch job definition. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the batch job. |
| Language | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The language in which the batch job is created. Possible values are: `af`—Afrikaans `am`—Amharic `ar`—Arabic `ar_AE`—Arabic (United Arab Emirates) `ar_BH`—Arabic (Bahrain) `ar_DZ`—Arabic (Algeria) `ar_EG`—Arabic (Egypt) `ar_IQ`—Arabic (Iraq) `ar_JO`—Arabic (Jordan) `ar_KW`—Arabic (Kuwait) `ar_LB`—Arabic (Lebanon) `ar_LY`—Arabic (Libya) `ar_MA`—Arabic (Morocco) `ar_OM`—Arabic (Oman) `ar_QA`—Arabic (Qatar) `ar_SA`—Arabic (Saudi Arabia) `ar_SD`—Arabic (Sudan) `ar_SY`—Arabic (Syria) `ar_TN`—Arabic (Tunisia) `ar_YE`—Arabic (Yemen) `bg`—Bulgarian `bn`—Bengali `bs`—Bosnian `ca`—Catalan `cs`—Czech `cy`—Welsh `da`—Danish `de`—German `de_AT`—German (Austria) `de_BE`—German (Belgium) `de_CH`—German (Switzerland) `de_LU`—German (Luxembourg) `el`—Greek `en_AU`—English (Australian) `en_CA`—English (Canadian) `en_GB`—English (UK) `en_HK`—English (Hong Kong) `en_IE`—English (Ireland) `en_IN`—English (Indian) `en_MY`—English (Malaysian) `en_NZ`—English (New Zealand) `en_PH`—English (Phillipines) `en_SG`—English (Singapore) `en_US`—English `en_ZA`—English (South Africa) `eo`—Esperanto (Pseudo) `es`—Spanish `es_AR`—Spanish (Argentina) `es_BO`—Spanish (Bolivia) `es_CL`—Spanish (Chile) `es_CO`—Spanish (Colombia) `es_CR`—Spanish (Costa Rica) `es_DO`—Spanish (Dominican Republic) `es_EC`—Spanish (Ecuador) `es_GT`—Spanish (Guatemala) `es_HN`—Spanish (Honduras) `es_MX`—Spanish (Mexico) `es_NI`—Spanish (Nicaragua) `es_PA`—Spanish (Panama) `es_PE`—Spanish (Peru) `es_PR`—Spanish (Puerto Rico) `es_PY`—Spanish (Paraguay) `es_SV`—Spanish (El Salvador) `es_US`—Spanish (United States) `es_UY`—Spanish (Uruguay) `es_VE`—Spanish (Venezuela) `et`—Estonian `eu`—Basque `fa`—Farsi `fi`—Finnish `fr`—French `fr_BE`—French (Belgium) `fr_CA`—French (Canadian) `fr_CH`—French (Switzerland) `fr_LU`—French (Luxembourg) `ga`—Irish `gu`—Gujarati `hi`—Hindi `hr`—Croatian `hu`—Hungarian `hy`—Armenian `in`—Indonesian `is`—Icelandic `it`—Italian `it_CH`—Italian (Switzerland) `iw`—Hebrew `iw_EO`—Esperanto RTL (Pseudo) `ja`—Japanese `ka`—Georgian `km`—Khmer `kn`—Kannada `ko`—Korean `lb`—Luxembourgish `lt`—Lithuanian `lv`—Latvian `mi`—Te reo `mk`—Macedonian `ml`—Malayalam `mr`—Marathi `ms`—Malay `mt`—Maltese `my`—Burmese `nl_BE`—Dutch (Belgium) `nl_NL`—Dutch `no`—Norwegian `pl`—Polish `pt_BR`—Portuguese (Brazil) `pt_PT`—Portuguese (European) `rm`—Romansh `ro`—Romanian `ro_MD`—Romanian (Moldova) `ru`—Russian `sh`—Serbian (Latin) `sh_ME`—Montenegrin `sk`—Slovak `sl`—Slovene `sq`—Albanian `sr`—Serbian (Cyrillic) `sv`—Swedish `sw`—Swahili `ta`—Tamil `te`—Telugu `th`—Thai `tl`—Tagalog `tr`—Turkish `uk`—Ukrainian `ur`—Urdu `vi`—Vietnamese `xh`—Xhosa `zh_CN`—Chinese (Simplified) `zh_HK`—Chinese (Hong Kong) `zh_SG`—Chinese (Singapore) `zh_TW`—Chinese (Traditional) `zu`—Zulu |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the batch job. |
| ProcessGroup | **Type** string **Properties** Filter, Group, Sort **Description** The group or team that's using the batch job. This field is only applicable to Batch Management jobs. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** The status of the batch job. Possible values are: `Active` `Inactive` |
| Type | **Type** picklist **Properties** Defaulted on create, Filter, Group, Restricted picklist, Sort **Description** Specifies the type of batch job. Possible values are: `BulkUpdate` `Calc`—Data Processing Engine `ConsumptionOveragesCalculation` `DecisionTableRefresh` `DeepCloneSalesAgreement` `FlattenAccountIOUHierarchyBatchJob` `Flow` `EnergyUseRecordCreationBatchJob` `EntitlementCreationBatchJob` `HighScaleBreProcess` `IndustriesLSCommercial` `InvoiceDTPRunBatchJob` `InvoiceRecoveryRunBatchJob` `InvoiceRunBatchJob` `LifeSciProviderActivityGoalSharingBatchJob` `LoyaltyProgramProcess` `NetUnitRateCalculation` `NextGenCommitmentBatchProcessingJob` `ManagerProvisioning` `PbbToOptyConversion` `ProductCatalogCacheRefresh` `PromotionChannelPropagationBatchJob` `RatableSummaryCreation` `ServiceProcess` `StoreAssortmentPropagationBatchJob` `SummaryCreation` `WorkDotComToHRManagerProvisioning` When Data Processing Engine or Batch Management is available in a Salesforce org, the default values are Calc or Flow respectively. Other types may be available to you depending on the licenses available in your org. |

=== ARTICLE: tooling_api_objects_batchprocessjobdefinition.htm ===
---
page_id: tooling_api_objects_batchprocessjobdefinition.htm
title: BatchProcessJobDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_batchprocessjobdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Data Processing Engine, Batch Management, and Monitor Workflow Services
parent_page: batch_management_setup_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# BatchProcessJobDefinition

    Represents the details of a Batch Management job. This object is available
    in API version 51.0 and later. 

    
      

#### Note

Where possible, we changed noninclusive terms to align with our company value of
        Equality. We maintained certain terms to avoid any effect on customer
        implementations.

    

    
      

Data and processes in your org are impacted if you update or delete a
        BatchProcessJobDefinition record. Update or delete a Batch Management job using the [Metadata API](./batch_metadata.htm.md).

    

    

## Supported SOAP API Calls

      
      

`describeSObjects()`, `query()`, `retrieve()`

    

    

## Supported REST API Methods

      
      

`DELETE, GET, HEAD, PATCH, POST, Query`

    

    

## Special Access Rules

      
      

To know the permissions needed to access this object, See [User Permissions for Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management_editions.htm&language=en_US).

    

    

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

            

            
              

              

: 

: 

: 

            

            
              

              

: 

: 

: 

            

            
              

              

: 

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

            

          

        
| Field | Details |
| --- | --- |
| BatchJobDefinitionId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier of the associated batch job definition. This is a relationship field. **Relationship Name** BatchJobDefinition **Relationship Type** Lookup **Refers To** BatchJobDefinition |
| BatchJobDefinitionName | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The name of the associated batch job definition. |
| BatchSize | **Type** int **Properties** Filter, Group, Sort **Description** Required. The number of records that each Batch Management job part can process. The maximum number of transaction journal records that a batch management job can process for flow or loyalty program process is 2000. |
| Description | **Type** textarea **Properties** Filter, Group, Nillable, Sort **Description** The description of the Batch Management job. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the Batch Management job. |
| FlowDefinitionId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The input variable of the associated flow that uniquely identifies each record that the Batch Management job processes. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** The name of the Batch Management job. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language in which the batch job is created. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** The label of the Batch Management job. |
| Metadata | **Type** complexvalue **Properties** Create, Nillable, Update **Description** The Batch Management job's metadata. Query this field only if the query result contains no more than one record. Otherwise, an error is returned. If more than one record exists, use multiple queries to retrieve the records. This limit protects performance. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| ProcessGroup | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The group or team for which the Batch Management job processes records. |
| RecordIdVariable | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The unique identifier that identifies each record that must be processed by the Batch Management job. |
| RetryCount | **Type** int **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. The number of times this Batch Management job must be rerun in case it fails. |
| RetryInterval | **Type** int **Properties** Defaulted on create, Filter, Group, Sort **Description** Required. The number of milliseconds after which the Batch Management job must be rerun in case it fails. A retry interval can be 1,000–10,000 milliseconds. |
| Status | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The status of the Batch Management job. Possible values are: `Active` `Inactive` |
| Type | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The type of process for which the Batch Management job processes records. Possible values are: `Flow` `BulkUpdate` `ConsumptionOveragesCalculation` `DecisionTableRefresh` `DeepCloneSalesAgreement` `EntitlementCreationBatchJob` `HighScaleBreProcess` `IndustriesLSCommercial` `LoyaltyProgramProcess` `ManagerProvisioning` `NetUnitRateCalculation` `PbbToOptyConversion` `ProductCatalogCacheRefresh` `RatableSummaryCreation` `SummaryCreation` The default value is `Flow`. Other types may be available to you depending on the licenses available in your org. This field is available in API version 55.0 and later. |
| TypeInstance | **Type** string **Properties** Filter, Group, Sort **Description** Required. The API name of the process that the Batch Management job must execute. |

