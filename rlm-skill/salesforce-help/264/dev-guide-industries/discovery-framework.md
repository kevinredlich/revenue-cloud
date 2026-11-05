# Industries Common Resources Developer Guide 264 — sección: Discovery Framework (57 artículos)

=== ARTICLE: actions_obj_get_assessment_response_summary.htm ===
---
page_id: actions_obj_get_assessment_response_summary.htm
title: Get Assessment Response Summary
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/actions_obj_get_assessment_response_summary.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_actions.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Get Assessment Response Summary

Get Assessment Response Summary makes it easy to use a flow to trigger
      server-side document generation using Document Generation.

    
      

In the Discovery Framework, the responses from an assessment are stored in the
        AssessmentQuestionResponse object and the form metadata stays in the OmniScript. You can use
        this invocable action to pass assessment summary data to downstream processes. This
        invocable action provides summary JSON code that can be consumed in Document Generation
        workflows to generate documents.

      

The Get Assessment Response Summary invocable action takes an assessment ID as input to get
        the OmniScript (OmniProcess) ID, which is used to retrieve the OmniScript. The assessment ID
        also retrieves the assessment response and merges the response with the OmniScript to create
        an assessment summary response in the summary JSON code.

      

This object is available in API version 56.0 and later.

    

    

## Supported REST HTTP Methods

      
      
        
          

**URI**

          
: `/services/data/v56.0/actions/standard/getAssessmentResponseSummary`

        
        
          

**Formats**

          
: JSON

        
        
          

**HTTP Methods**

          
: POST

        
        
          

**Authentication**

          
: `Authorization: Bearer token`

        
      

    

    

## Inputs

      
      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

            

          

        
| Input | Details |
| --- | --- |
| assessmentId | **Type** ID **Description** Required. The ID of the assessment record for which to summarize responses. |

    

    

## Outputs

      
      

          
          
          
            
              

              

            

          

          
            
              

              

: 

: 

            

          

        
| Output | Details |
| --- | --- |
| assessmentResponseSummary | **Type** string **Description** A JSON string containing the summary assessment question texts and responses for the specified assessment record. The response summary structure follows the structure of the OmniScript. |

    

    

## Usage

      
      
        
          

**Sample Input**

          
: 
            

When exposing the Get Assessment Response Summary invocable action in a REST API, you
              can use the following format to pass input, which includes the assessmentId and its
              value. 

            

```
{
  "inputs" : [ {"assessmentId" : "0U3RO00000005FN0AY"} ]
}
```

          

        
        
          

**Sample Output**

          
: 
            

In this example, the first line indicates the OmniScript type, subtype, and language.
              For each step, there are multiple questions that appear in the OmniScript. You can use
              this information in a downstream process, such as PDF file rendering using Document
              Generation. 

            

```
  "KYC_Individual_English": {
    "Step1": {
      "label": "Identity Details",
      "value": {
        "LC_Survey_Question_2": {
          "label": "Full Name",
          "value": "Joe Smith"
        },
        "DateofBirth_m": {
          "label": "Date of Birth",
          "value": "Thu Jul 27 00:00:00 GMT 2000"
        },
        "Gender_m": {
          "label": "Gender",
          "value": "Female"
        },
        "EmailAddress_m": {
          "label": "Email Address",
          "value": "Joe.Smith@company.com"
        },
        "PAN": {
          "label": "PAN",
          "value": "QWEASDZXC"
        }
      }
    },
    "Step2": {
      "label": "Address Details",
      "value": {
        "Address_CorrespondenceAdd_Corporate": {
          "label": "Address of Correspondence",
          "value": "100 Some St, San Francisco, CA 12345, United States"
        },
        "Address_ContactDetails_Corporate": {
          "label": "Telephone/Mobile",
          "value": "1616111233"
        },
        "Alternate_Contact": {
          "label": "Alternate Mobile Number",
          "value": "1911212123"
        }
      }
    },
    "Step3": {
      "label": "Account Declaration",
      "value": {
        "Account_declaration": {
          "label": "I declare that I have following deposit accounts with your/
other bank's branches :",
          "value": [
            {
              "Bank": {
                "label": "Bank",
                "value": "Acme1"
              },
              "Branch": {
                "label": "Branch",
                "value": "Mission St"
              },
              "Type_of_Account": {
                "label": "Type of Account",
                "value": "Checking"
              },
              "Account_Number": {
                "label": "Account Number",
                "value": "12345678"
              }
            },
            {
              "Bank": {
                "label": "Bank",
                "value": "Acme2"
              },
              "Branch": {
                "label": "Branch",
                "value": "Mission St"
              },
              "Type_of_Account": {
                "label": "Type of Account",
                "value": "Savings"
              },
              "Account_Number": {
                "label": "Account Number",
                "value": "1234567890"
              }
            }
          ]
        }
      }
    },
    "Step4": {
      "label": "Declaration",
      "value": {
        "Declaration_m": {
          "label": "The customer declares and certifies that the information in this 
form is true and correct. Any pre-filled sections of this form must be reviewed prior
 to signing and submitting, to ensure the information accurately conveys the new 
account details.",
          "value": "true"
        }
      }
    }
  }
}
```

=== ARTICLE: connect_requests_assessment_links_input.htm ===
---
page_id: connect_requests_assessment_links_input.htm
title: Assessment Links Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_assessment_links_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Links Input

Associated assessments including id, category, reason and
      sequence.

    
      
        
          

**Root XML tag**

          
: `<assessmentLinks>`

        
        
          

**JSON example**

          
: 
            

```

  {
    "id": "0U3SG00000068Cb0AI",
    "category": "0iPSG0000024n0z2AA",
    "reason": "0iPSG0000024n0z2AA",
    "sequence": 333
  }
]
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required | Available Version |
| --- | --- | --- | --- | --- |
| `category` | String | The category that the supporting content belongs to. | No | 63.0 |
| `id` | String | The assessment used as the supporting content. | Yes | 55.0 |
| `reason` | String | The reason why the supporting content is required. | No | 63.0 |
| `sequence` | String | The sequence number of the content when multiple contents are available. | No | 63.0 |

=== ARTICLE: connect_requests_assessment_responses_assessment_details_input.htm ===
---
page_id: connect_requests_assessment_responses_assessment_details_input.htm
title: Assessment Details Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_assessment_responses_assessment_details_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Details Input

Input representation of the assessment details of Assessment Response request. 

        
            
                
                    

**JSON example**

                    
: 
                        

```
{
    "assessmentDetails": {
        "assessmentReasons": [
            {
                "referenceRecord": "0jySG0000000qRdxxI"
            },
            {
                "referenceRecord": "0SqSG00000005HRxxY"
            },
            {
                "referenceRecord": "0kmSG0000000n7BxxQ",
                "referenceValue": "Medication Request sample"
            },
            {
                "referenceValue": "Reference Record not present"
            }
        ],
        "assessmentQuestionsResponseDetails": {
            "First_Name": {
                "originType": "Auto",
                "reviewerRole": "0hsSG0000002t8TxxQ",
                "reviewer": "003SG00000BTzxpxxD"
            },
            "Last_Name": {
                "originType": "Auto",
                "reviewerRole": "0hsSG0000002t8TxxQ",
                "reviewer": "003SG00000BTzxpxxD"
            },
            "Email": {
                "originType": "Auto",
                "reviewerRole": "0hsSG0000002t8TxxQ",
                "reviewer": "003SG00000BTzxpxxD"
            },
            "Phone": {
                "originType": "Auto",
                "reviewerRole": "0hsSG0000002t8TxxQ",
                "reviewer": "003SG00000BTzxpxxD"
            },
            "Multi_Select": {
                "originType": "Auto",
                "reviewerRole": "0hsSG0000002t8TxxQ",
                "reviewer": "003SG00000BTzxpxxD"
            }
        }
    }
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assessmentQuestionsResponseDetails` | Map<String, Object> | The details of the assessment questions response. Only available for Health Cloud users. | Optional | 63.0 |
| `assessmentReasons` | [List<AssessmentReasonInputRepresentation>](./connect_requests_assessment_responses_assessment_reason_input.htm.md) | Details of the assessment. | Optional | 63.0 |

=== ARTICLE: connect_requests_assessment_responses_assessment_reason_input.htm ===
---
page_id: connect_requests_assessment_responses_assessment_reason_input.htm
title: Assessment Reasons Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_assessment_responses_assessment_reason_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Reasons Input

Input representation of the assessment reason in Assessment Response request. 

        
            
                
                    

**JSON example**

                    
: 
                        

```
{
        "assessmentReasons": [
            {
                "referenceRecord": "0jySG0000000qRdxxI"
            },
            {
                "referenceRecord": "0SqSG00000005HRxxY"
            },
            {
                "referenceRecord": "0kmSG0000000n7BxxQ",
                "referenceValue": "Medication Request sample"
            },
            {
                "referenceValue": "Reference Record not present"
            }
        ]
        }
    }
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `referenceRecord` | String | Reason for the assessment. | Optional | 63.0 |
| `referenceValue` | String | The supporting information when there is no Salesforce record to be added as the reference record. | Optional | 63.0 |

=== ARTICLE: connect_requests_assessment_responses_assessment_values_input.htm ===
---
page_id: connect_requests_assessment_responses_assessment_values_input.htm
title: Assessment Values Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_assessment_responses_assessment_values_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Values Input

Input representation of the assessment value of Assessment Response request. 

        
            
                
                    

**JSON example**

                    
: 
                        

```
{
    "assessmentValues": {
        "Assessment.AssessmentStatus": "Completed",
        "completedDateTime": "2024-10-23T14:45:29.123+05:30",
        "assessor": "001SG00000laIWPYA2",
        "identifier": "Test identifier",
        "assessmentDetails": {
            "assessmentReasons": [
                {
                    "referenceRecord": "0jySG0000000qRdYAI"
                },
                {
                    "referenceRecord": "0SqSG00000005HR0AY"
                },
                {
                    "referenceRecord": "0kmSG0000000n7BYAQ",
                    "referenceValue": "Medication Request sample"
                },
                {
                    "referenceValue": "Reference Record not present"
                }
            ],
            "assessmentQuestionsResponseDetails": {
                "First_Name": {
                    "originType": "Auto",
                    "reviewerRole": "0hsSG0000002t8TYAQ",
                    "reviewer": "003SG00000BTzxpYAD"
                },
                "Last_Name": {
                    "originType": "Auto",
                    "reviewerRole": "0hsSG0000002t8TYAQ",
                    "reviewer": "003SG00000BTzxpYAD"
                },
                "Email": {
                    "originType": "Auto",
                    "reviewerRole": "0hsSG0000002t8TYAQ",
                    "reviewer": "003SG00000BTzxpYAD"
                },
                "Phone": {
                    "originType": "Auto",
                    "reviewerRole": "0hsSG0000002t8TYAQ",
                    "reviewer": "003SG00000BTzxpYAD"
                },
                "Multi_Select": {
                    "originType": "Auto",
                    "reviewerRole": "0hsSG0000002t8TYAQ",
                    "reviewer": "003SG00000BTzxpYAD"
                }
            }
        }
    }
}
```

                    

                
                
                    

**Properties**

                    
: 
                        

                                
                                
                                
                                
                                
                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                                
                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                    
                                        

                                        

                                        

                                        

                                        

                                    

                                

                            
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `Assessment.AssessmentStatus` | String | Status of the assessment. | Optional | 60.0 |
| `assessmentDetails` | [AssessmentDetailsInputRepresentation](./connect_requests_assessment_responses_assessment_details_input.htm.md) | Metadata of the Assessment Questions. | Optional | 63.0 |
| `assessor` | String | Person who carried out the assessment and recorded the responses. | Optional | 63.0 |
| `completedDateTime` | Integer | The date and time when the assessment was completed. | Optional | 63.0 |
| `identifier` | String | Unique identifier of a completed or partially completed assessment in the source system. | Optional | 63.0 |

=== ARTICLE: connect_requests_assessment_responses_input.htm ===
---
page_id: connect_requests_assessment_responses_input.htm
title: Assessment Responses Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_assessment_responses_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Responses Input

Input for assessment responses.

    
      
        
          

**JSON example**

          
: 
            

```
{
  "inputs": {
    "questionResponses": {
      "ootb__DF_API_MSelect1": "Y;N",
      "ootb__DF_API_MSelect2": "1;2;3",
      "ootb__DF_API_RG1": {
        "ootb__DF_API_Radio1": "Y",
        "ootb__DF_API_Radio2": "N",
        "ootb__DF_API_Radio3": "M"
      },
      "ootb__DF_API_Text": "TestingDF",
      "ootb__DF_API_Select1": "1",
      "ootb__DF_API_Select2": "w",
      "ootb__DF_API_EditBlock2": {
        "ootb__DF_API_Int": 5
      },
      "ootb__DF_API_Boolean": true,
      "ootb__DF_API_Formula": true
    }
  },
  "contextId": "0U3B00000004IhWKAU",
  "assessmentValues": {
    "Assessment.AssessmentStatus": "Completed"
  },
  "completedDateTime": "2024-10-23T14:45:29.123+05:30",
  "assessor": "001SG00000laIWPYA2",
  "identifier": "Test identifier",
  "assessmentDetails": {
    "assessmentReasons": [
      {
        "referenceRecord": "0jySG0000000qRdYAI"
      },
      {
        "referenceRecord": "0SqSG00000005HR0AY"
      },
      {
        "referenceRecord": "0kmSG0000000n7BYAQ",
        "referenceValue": "Medication Request sample"
      },
      {
        "referenceValue": "Reference Record not present"
      }
    ],
    "assessmentQuestionsResponseDetails": {
      "First_Name": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Last_Name": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Email": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Phone": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Multi_Select": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      }
    }
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assessment​Values` | [Assessment Values Input>](./connect_requests_assessment_responses_assessment_values_input.htm.md)[] | Values of Assessment fields. | Optional | 60.0 |
| `contextId` | String | Context record for the OmniScript. | Optional | 60.0 |
| `inputs` | [Question Responses Input](./connect_requests_question_responses_input.htm.md)[] | Responses for Assessment Questions. | Optional | 60.0 |

=== ARTICLE: connect_requests_document_decision_input.htm ===
---
page_id: connect_requests_document_decision_input.htm
title: Document Decision Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_document_decision_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Document Decision Input

Input representation of the Document Decision request.

**JSON example**

: 

```
{
  "inputs": [
    {
      "Country": "USA",
      "State": "CA"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | List<Map<String, Object>> | List of inputs passed to Decision Table. Each key is a Decision Table field name, and each value is valid for that field. | Required | 59.0 |

=== ARTICLE: connect_requests_question_responses_input.htm ===
---
page_id: connect_requests_question_responses_input.htm
title: Question Responses Input
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_requests_question_responses_input.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_requests.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Question Responses Input

Input for assessment question responses.

**JSON example**

: 

The properties under `questionResponses` are in the following
              format:

```
{
  "questionResponses": {
    "Element_APIName or AssessmentQuestion uniqueIndex 1": "value",
    "Element_APIName or AssessmentQuestion uniqueIndex 2": {
      "Child_element_APIName or Question uniqueIndex 1": "value",
      "Child_element_APIName or Question uniqueIndex 2": "value",
     ...
    }
  }
}
```

For
            example:

```
{
  "questionResponses": {
    "ootb__DF_API_MSelect1": "Y;N",
    "ootb__DF_API_MSelect2": "1;2;3",
    "ootb__DF_API_RG1": {
      "ootb__DF_API_Radio1": "Y",
      "ootb__DF_API_Radio2": "N",
      "ootb__DF_API_Radio3": "M"
    },
    "ootb__DF_API_Text": "TestingDF",
    "ootb__DF_API_Select1": "1",
    "ootb__DF_API_Select2": "w",
    "ootb__DF_API_EditBlock2": {
      "ootb__DF_API_Int": 5
    },
    "ootb__DF_API_Boolean": true,
    "ootb__DF_API_Formula": true
  }
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `question​Responses` | Map<String, Object> | Responses map for Assessment Questions. | Optional | 60.0 |

=== ARTICLE: connect_resources_document_decision.htm ===
---
page_id: connect_resources_document_decision.htm
title: Document Decision
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_document_decision.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Document Decision

Invoke a Decision Table, accept key-value pairs that match the Decision Table keys, and
    return either Document Types or Document Categories and the Document Types associated with
    them.

    

For example, one use case is applying for a driver's license. Based on questions about where the
        applicant lives, a Decision Table can list the documents to be uploaded for proof of
        identity.

The Decision Table must be active and have DocumentDecisionRequirement, a platform object, as its
        Source Object. This platform object stores the Decision Table's inputs, outputs, and
        business rules.

      

One of the Decision Table outputs must be DocumentReferenceObjectId, which references a
        Document Type or Document Category object. An optional output is isUploadRequired, which
        sets the default for the Document Categories property isRequired. These two outputs don’t
        appear in the connect API’s outputs.

    
      
        
          

**Resource**

          
: 
            

```
/connect/document-matrix/document-decision/decisionTableId
```

          

        
        
          

**Available version**

          
: 59.0

        
        
          

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
  "inputs": [
    {
      "Country": "USA",
      "State": "CA"
    }
  ]
}
```

**Properties**

: 

| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `inputs` | List<Map<String, Object>> | List of inputs passed to Decision Table. Each key is a Decision Table field name, and each value is valid for that field. | Required | 59.0 |

          

        
        
          

**Response body for POST**

          
: [Document Decision Response](./connect_responses_document_decision_response.htm.md)

=== ARTICLE: connect_resources_save_assessment_responses.htm ===
---
page_id: connect_resources_save_assessment_responses.htm
title: Assessment Responses
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_save_assessment_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Responses

Save assessment responses from an OmniScript built with the Assessment Questions
    app.

This feature requires OmniStudio and Discovery Framework licenses. To build an
        OmniScript using the Assessment Questions app, see [Create a Form](https://help.salesforce.com/s/articleView?id=ind.fsc_admin_create_a_form.htm&type=5&language=en_US). 

In in Health Cloud, this API captures supporting information for a Prior Authorization (PA) by
        recording responses from the Documentation Template and Rules Questionnaire. It associates
        these responses with a specific PA request and is triggered as part of the `$submit` API from Mulesoft.

        
          

**Resource**

          
: 
            

```
/connect/discovery-framework/assessment-responses/omniScriptId
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
  "inputs": {
    "questionResponses": {
      "ootb__DF_API_MSelect1": "Y;N",
      "ootb__DF_API_MSelect2": "1;2;3",
      "ootb__DF_API_RG1": {
        "ootb__DF_API_Radio1": "Y",
        "ootb__DF_API_Radio2": "N",
        "ootb__DF_API_Radio3": "M"
      },
      "ootb__DF_API_Text": "TestingDF",
      "ootb__DF_API_Select1": "1",
      "ootb__DF_API_Select2": "w",
      "ootb__DF_API_EditBlock2": {
        "ootb__DF_API_Int": 5
      },
      "ootb__DF_API_Boolean": true,
      "ootb__DF_API_Formula": true
    }
  },
  "contextId": "0U3B00000004IhWKAU",
  "assessmentValues": {
    "Assessment.AssessmentStatus": "Completed"
  },
  "completedDateTime": "2024-10-23T14:45:29.123+05:30",
  "assessor": "001SG00000laIWPYA2",
  "identifier": "Test identifier",
  "assessmentDetails": {
    "assessmentReasons": [
      {
        "referenceRecord": "0jySG0000000qRdYAI"
      },
      {
        "referenceRecord": "0SqSG00000005HR0AY"
      },
      {
        "referenceRecord": "0kmSG0000000n7BYAQ",
        "referenceValue": "Medication Request sample"
      },
      {
        "referenceValue": "Reference Record not present"
      }
    ],
    "assessmentQuestionsResponseDetails": {
      "First_Name": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Last_Name": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Email": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Phone": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      },
      "Multi_Select": {
        "originType": "Auto",
        "reviewerRole": "0hsSG0000002t8TYAQ",
        "reviewer": "003SG00000BTzxpYAD"
      }
    }
  }
}
```

          

        
        
          

**Properties**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                  
                    

                    

                    

                    

                    

                  

                

              
| Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `assessment​Values` | [Assessment Values Input>](./connect_requests_assessment_responses_assessment_values_input.htm.md)[] | Values of Assessment fields. | Optional | 60.0 |
| `contextId` | String | Context record for the OmniScript. | Optional | 60.0 |
| `inputs` | [Question Responses Input](./connect_requests_question_responses_input.htm.md)[] | Responses for Assessment Questions. | Optional | 60.0 |

          

        
      

          

        
        
          

**Response body for POST**

          
: [Assessment Responses Output](./connect_responses_assessment_responses_output.htm.md)

=== ARTICLE: connect_resources_store_discovery_framework_structure.htm ===
---
page_id: connect_resources_store_discovery_framework_structure.htm
title: Omniscript
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_store_discovery_framework_structure.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_resources.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omniscript

Get the discovery framework structure stored as OmniProcess.

    

Use this API to get the assessment form layout and submit the assessment data through any
        custom-built UI. You can show the questionnaire form, capture assessment responses, and save
        the assessment.

    
      
        
          

**Resource**

          
: 

```
/connect/omniscript/omniScriptId
```

The
              `omniScriptId` property is the ID of the Omniscript
            to get the discovery framework structure stored as an OmniProcess.

        
        
          

**Resource example**

          
: 
            

```
https://yourInstance.salesforce.com/services/data/v60.0/connect/omniscript/CreditCard_DisputeTransaction_English_1?customType=DiscoveryFramework
```

          

        
        
          

**Available version**

          
: 60.0

        
        
          

**HTTP methods**

          
: GET

        
        
          

**Request parameters for GET**

          
: 
            

                
                
                
                
                
                
                  
                    

                    

                    

                    

                    

                  

                

                
                  
                    

                    

                    

                    

                    

                  

                

              
| Parameter Name | Type | Description | Required or Optional | Available Version |
| --- | --- | --- | --- | --- |
| `customType` | String | Custom type of Omniscript. For example, Discovery Framework. | Required | 60.0 |

          

        
        
          

**Response body for GET**

          
: [Omniscript Output](./connect_responses_omniscript_output.htm.md)

=== ARTICLE: connect_responses_additional_attributes.htm ===
---
page_id: connect_responses_additional_attributes.htm
title: Additional Attributes Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_additional_attributes.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Additional Attributes Output

Output representation of the Additional Attributes.

        
            

                    
                    
                    
                    
                    
                    
                        
                            

                            

                            

                            

                            

                        

                    

                    
                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            
- 
- 
- 

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            
- 
- 
- 

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                        
                            

                            

                            

                            

                            

                        

                    

                
| Attribute Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `approvalDateTime` | String | Date and time when the assessment was approved by the publisher. | Small, 63.0 | 63.0 |
| `displayType` | String | Specifies the display format for questions in the assessment for the end-user. Possible values are: `Sequential` `Prior-edit` `Random`. | Small, 63.0 | 63.0 |
| `effectiveFromDate` | String | The date when the assessment takes effect. | Small, 63.0 | 63.0 |
| `effectiveToDate` | String | The date until the assessment is in effect. | Small, 63.0 | 63.0 |
| `lastRevisedDateTime` | String | The date and time when the assessment was last revised. | Small, 63.0 | 63.0 |
| `performerType` | String | Specifies the type of performer that can record responses to the assessment. Possible values are: `Patient` `Practioner` `Related Person`. | Small, 63.0 | 63.0 |
| `purpose` | String | The purpose of the assessment. | Small, 63.0 | 63.0 |
| `publisher` | String | The organization or individual that published the assessment. | Small, 63.0 | 63.0 |

=== ARTICLE: connect_responses_assessment_responses_output.htm ===
---
page_id: connect_responses_assessment_responses_output.htm
title: Assessment Responses Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_assessment_responses_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment Responses Output

Output of assessment responses.

| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `assessmentId` | String | ID of created Assessment. | Small, 60.0 | 60.0 |
| `message` | String | Message explaining why the request failed. | Small, 60.0 | 60.0 |
| `status` | String | Specifies whether the request succeeded (`true`) or failed (`false`). | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_custom_type_details.htm ===
---
page_id: connect_responses_custom_type_details.htm
title: Custom Type Details
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_custom_type_details.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Custom Type Details

Output representation of the custom type details of the Omniscript elements.

        
          

**JSON example**

          
: 
            

```
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Can you provide more details about the transaction"
            }
          }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `discovery​Framework` | [OS Element Discovery Framework](./connect_responses_os_element_discovery_framework_output.htm.md)[] | Custom type details for the Omniscript element for Discovery framework. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_decision_table_document_decision.htm ===
---
page_id: connect_responses_decision_table_document_decision.htm
title: Decision Table Document Decision Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_decision_table_document_decision.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Decision Table Document Decision Output

Decision Table output.

#### Important

Where possible, we changed noninclusive terms
        to align with our company value of Equality. We maintained certain terms to avoid any effect
        on customer implementations.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Attribute Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `defaultMaximum​FileSizeAllowed` | Integer | Default maximum file size if `maximumFile​SizeAllowed` is null for a Document Type. | Small, 59.0 | 59.0 |
| `defaultMaximum​FileUploads​Allowed` | Integer | Default maximum file uploads if `maximumFile​UploadsAllowed` is null for a Document Type. | Small, 59.0 | 59.0 |
| `document​CategoryId` | String | ID of the Document Category. | Small, 59.0 | 59.0 |
| `document​CategoryLabel` | String | Master label of the Document Category. | Small, 59.0 | 59.0 |
| `documentTypes` | [Document Types Output](./connect_responses_document_types.htm.md)[] | List of document types and their properties. | Big, 59.0 | 59.0 |
| `helpText` | String | Help text for files in this Document Category. | Small, 59.0 | 59.0 |
| `isRequired` | Boolean | Indicates whether uploading a file in this Document Category is required. If `isRequired` isn't set, the `isUploadRequired` value is used. If neither `isRequired` nor `isUploadRequired` is set, the default is `false`. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_document_decision_response.htm ===
---
page_id: connect_responses_document_decision_response.htm
title: Document Decision Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_document_decision_response.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Document Decision Output

Output representation of the Document Decision response, including Decision Table
    output.

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `decisionTable​Document​Decisions` | [Decision Table Document Decision Output](./connect_responses_decision_table_document_decision.htm.md) | Decision Table output. | Big, 59.0 | 59.0 |
| `message` | String | Message with information about the success or failure of the request. A success message includes the number of results. | Small, 59.0 | 59.0 |
| `status` | String | Indicates whether the request succeeded (`true`), or failed (`false`). | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_document_types.htm ===
---
page_id: connect_responses_document_types.htm
title: Document Types Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_document_types.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Document Types Output

Output representation of the Document Type.

#### Important

Where possible, we changed noninclusive terms
        to align with our company value of Equality. We maintained certain terms to avoid any effect
        on customer implementations.

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Attribute Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `documentTypeId` | String | ID of the Document Type. | Small, 59.0 | 59.0 |
| `document​TypeLabel` | String | Master label of the Document Type. | Small, 59.0 | 59.0 |
| `maximumFile​SizeAllowed` | Integer | Maximum file size allowed for this Document Type, if any. | Small, 59.0 | 59.0 |
| `maximumFile​UploadsAllowed` | Integer | Maximum file uploads allowed for this Document Type, if any. | Small, 59.0 | 59.0 |

=== ARTICLE: connect_responses_omniscript_elements_list.htm ===
---
page_id: connect_responses_omniscript_elements_list.htm
title: Omniscript Elements List
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_omniscript_elements_list.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omniscript Elements List

Output representation of the details of the Omniscript elements.

    

        
          

**JSON example**

          
: 
            

```
  "elements": [
    {
      "DiscoveryFrameworkUsageType": "Default",
      "DesignerCustomizationType": "Discovery Framework",
      "Type": "Step",
      "PropertySetConfig": {
        "label": "Card Details",
        "show": null,
        "conditionType": "Hide if False"
      },
      "ParentElementType": null,
      "ParentElementName": null,
      "SequenceNumber": 0,
      "OmniProcessVersionNumber": 1,
      "Level": 0,
      "Description": null,
      "Name": "Step1",
      "elements": [
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Was the card in your possession at the time of the disputed transactions?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 0,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_CardRelatedQ1",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Was the card in your possession at the time of the disputed transactions?"
            }
          }
        },
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Was the card lost or stolen at the time of the disputed transactions?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": {
              "group": {
                "operator": "AND",
                "rules": [
                  {
                    "data": "Yes",
                    "condition": "=",
                    "field": "FSC_DM_v1_CardRelatedQ1"
                  }
                ]
              }
            },
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 1,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_CardRelatedQ2",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Was the card lost or stolen at the time of the disputed transactions?"
            }
          }
        },
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Did you provide your card details on any unfamiliar or suspicious websites?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 2,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_FraudRelatedQ4",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Did you provide your card details on any unfamiliar or suspicious websites?"
            }
          }
        }
      ]
    },
    {
      "DiscoveryFrameworkUsageType": "Default",
      "DesignerCustomizationType": "Discovery Framework",
      "Type": "Step",
      "PropertySetConfig": {
        "label": "Additional Details",
        "show": null,
        "conditionType": "Hide if False"
      },
      "ParentElementType": null,
      "ParentElementName": null,
      "SequenceNumber": 2,
      "OmniProcessVersionNumber": 1,
      "Level": 0,
      "Description": null,
      "Name": "Step2",
      "elements": [
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Text Area",
          "PropertySetConfig": {
            "label": "Can you provide more details about the transaction",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step2",
          "SequenceNumber": 2,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_AdditionalQ2",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Can you provide more details about the transaction"
            }
          }
        }
      ]
    }
  ]
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `custom​Type​Details` | [Custom Type Details](./connect_responses_custom_type_details.htm.md)[] | Custom type details for the Omniscript element. | Small, 60.0 | 60.0 |
| `description` | String | Description of the Omniscript element. | Small, 60.0 | 60.0 |
| `designer​Customization​Type` | String | The customization type of the Omniscript element. | Small, 60.0 | 60.0 |
| `discovery​Framework​UsageType` | String | Discovery framework usage type of the Omniscript element. | Small, 60.0 | 60.0 |
| `elements` | [Omniscript Elements List](#)[] | Elements within the Omniscript element. | Small, 60.0 | 60.0 |
| `level` | String | Level of the Omniscript element. | Small, 60.0 | 60.0 |
| `name` | String | Name of the Omniscript element. | Small, 60.0 | 60.0 |
| `omniProcess​Version​Number` | String | OmniProcess version number of the Omniscript element. | Small, 60.0 | 60.0 |
| `parent​Element​Name` | String | Parent element name of the Omniscript element. | Small, 60.0 | 60.0 |
| `parent​Element​Type` | String | Parent element type of the Omniscript element. | Small, 60.0 | 60.0 |
| `property​Set​Config` | [OS Element Property Set](./connect_responses_os_element_property_set_output.htm.md)[] | Property set configuration of the Omniscript element. | Small, 60.0 | 60.0 |
| `sequence​Number` | String | Sequence number of the Omniscript element. | Small, 60.0 | 60.0 |
| `type` | String | Type of the Omniscript element. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_omniscript_output.htm ===
---
page_id: connect_responses_omniscript_output.htm
title: Omniscript Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_omniscript_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omniscript Output

Output representation of the details of the Omniscript.

    

        
          

**JSON example**

          
: 
            

```
{
  "DiscoveryFrameworkUsageType": "Default",
  "DesignerCustomizationType": "Discovery Framework",
  "VersionNumber": 1,
  "Type": "DiscoveryFramework",
  "Language": "English",
  "IsActive": false,
  "Description": null,
  "Name": "Dispute",
  "elements": [
    {
      "DiscoveryFrameworkUsageType": "Default",
      "DesignerCustomizationType": "Discovery Framework",
      "Type": "Step",
      "PropertySetConfig": {
        "label": "Card Details",
        "show": null,
        "conditionType": "Hide if False"
      },
      "ParentElementType": null,
      "ParentElementName": null,
      "SequenceNumber": 0,
      "OmniProcessVersionNumber": 1,
      "Level": 0,
      "Description": null,
      "Name": "Step1",
      "elements": [
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Was the card in your possession at the time of the disputed transactions?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 0,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_CardRelatedQ1",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Was the card in your possession at the time of the disputed transactions?"
            }
          }
        },
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Was the card lost or stolen at the time of the disputed transactions?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": {
              "group": {
                "operator": "AND",
                "rules": [
                  {
                    "data": "Yes",
                    "condition": "=",
                    "field": "FSC_DM_v1_CardRelatedQ1"
                  }
                ]
              }
            },
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 1,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_CardRelatedQ2",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Was the card lost or stolen at the time of the disputed transactions?"
            }
          }
        },
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Radio",
          "PropertySetConfig": {
            "label": "Did you provide your card details on any unfamiliar or suspicious websites?",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "options": [
              {
                "name": "Yes",
                "developerName": "Yes",
                "value": "Yes",
                "setAll": false
              },
              {
                "name": "No",
                "developerName": "No",
                "value": "No",
                "setAll": false
              }
            ],
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step1",
          "SequenceNumber": 2,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_FraudRelatedQ4",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Did you provide your card details on any unfamiliar or suspicious websites?"
            }
          }
        }
      ]
    },
    {
      "DiscoveryFrameworkUsageType": "Default",
      "DesignerCustomizationType": "Discovery Framework",
      "Type": "Step",
      "PropertySetConfig": {
        "label": "Additional Details",
        "show": null,
        "conditionType": "Hide if False"
      },
      "ParentElementType": null,
      "ParentElementName": null,
      "SequenceNumber": 2,
      "OmniProcessVersionNumber": 1,
      "Level": 0,
      "Description": null,
      "Name": "Step2",
      "elements": [
        {
          "DiscoveryFrameworkUsageType": "Default",
          "DesignerCustomizationType": "Discovery Framework",
          "Type": "Text Area",
          "PropertySetConfig": {
            "label": "Can you provide more details about the transaction",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "show": null,
            "conditionType": "Hide if False"
          },
          "ParentElementType": "Step",
          "ParentElementName": "Step2",
          "SequenceNumber": 2,
          "OmniProcessVersionNumber": 1,
          "Level": 1,
          "Description": null,
          "Name": "FSC_DM_v1_AdditionalQ2",
          "elements": [],
          "customTypeDetails" : {
            "discoveryFramework": {
                "questionText": "Can you provide more details about the transaction"
            }
          }
        }
      ]
    }
  ]
}
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `additionalAttributes` | [additionalAttributes Output](./connect_responses_additional_attributes.htm.md)[] | Additional attributes of the Omniscript. | Small, 63.0 | 63.0 |
| `description` | String | Description of the Omniscript. | Small, 60.0 | 60.0 |
| `designer​Customization​Type` | String | Custom type of the Omniscript. | Small, 60.0 | 60.0 |
| `discovery​FrameworkUsage​Type` | String | Usage type of the Omniscript. | Small, 60.0 | 60.0 |
| `elements` | [Omniscript Elements List](./connect_responses_omniscript_elements_list.htm.md)[] | Element node of the Omniscript. | Small, 60.0 | 60.0 |
| `isActive` | Boolean | Indicates if the Omniscript assessment is active `(true)` or not `(false)`. | Small, 60.0 | 60.0 |
| `language` | String | Language of the Omniscript. | Small, 60.0 | 60.0 |
| `lastModifiedDate` | String | Date when the Omniscript was modified. | Small, 60.0 | 60.0 |
| `name` | String | Name of the Omniscript. | Small, 60.0 | 60.0 |
| `omniprocessId` | String | ID of the Omniscript associated with the assessment record. | Small, 60.0 | 60.0 |
| `subType` | String | Subtype of the Omniscript. | Small, 60.0 | 60.0 |
| `type` | String | Type of the Omniscript. | Small, 60.0 | 60.0 |
| `version​Number` | String | Version of the Omniscript. | Small, 60.0 | 60.0 |
| `uniqueName` | String | Unique name for the Omniscript. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_os_element_discovery_framework_output.htm ===
---
page_id: connect_responses_os_element_discovery_framework_output.htm
title: Omniscript Element Discovery Framework Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_os_element_discovery_framework_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omniscript Element Discovery Framework Output

Output representation of the custom type details of the Omniscript elements for
    Discovery Framework.

    

        
          

**JSON example**

          
: 
            

```
      "discoveryFramework": {
       "questionText": "Can you provide more details about the transaction"
    }
```

          

        
      

      

#### Note

        

When you receive a GET response, HTML replaces reserved characters with their
          corresponding entities. For example, "What's your address" will appear as "What&#39; s
          your address."

      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `description` | String | Description of the question for the Discovery Framework question type element. | Small, 63.0 | 63.0 |
| `displayTextCategory` | String | The category of the display text when the data type is Text Block. This field valued is returned for Health Cloud customers only. | Small, 63.0 | 63.0 |
| `question​Category` | String | Category of the question for the Discovery Framework question type element. | Small, 60.0 | 60.0 |
| `question​DataType` | String | Data type of the question for the Discovery Framework question type element. | Small, 60.0 | 60.0 |
| `question​Developer​Name` | String | Developer name of the question for the Discovery Framework question type element. | Small, 60.0 | 60.0 |
| `question​Namespace` | String | Namespace of the question for the Discovery Framework question type element. | Small, 60.0 | 60.0 |
| `question​Text` | String | Text of the question for the Discovery Framework question type element. | Small, 60.0 | 60.0 |

=== ARTICLE: connect_responses_os_element_property_set_output.htm ===
---
page_id: connect_responses_os_element_property_set_output.htm
title: Omniscript Element Property Set Output
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_responses_os_element_property_set_output.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_apis_responses.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Omniscript Element Property Set Output

Output representation of the property set configuration of the Omniscript
    elements.

    

        
          

**JSON example**

          
: 
            

```
     "PropertySetConfig": {
            "label": "Can you provide more details about the transaction",
            "defaultValue": null,
            "help": false,
            "helpText": "",
            "show": null,
            "conditionType": "Hide if False"
          }
```

          

        
      

          
          
          
          
          
          
            
              

              

              

              

              

            

          

          
            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

            
              

              

              

              

              

            

          

        
| Property Name | Type | Description | Filter Group and Version | Available Version |
| --- | --- | --- | --- | --- |
| `checkLabel` | String | Label of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `conditionType` | String | Condition type of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `dataType` | String | Data type of the formula for the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `dateFormat` | String | Date format of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `expression` | String | Formula expression of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `help` | String | Help details of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `helpText` | String | Help text of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `label` | String | Label of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `options` | List<Map<String, Object>> | Options of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `radioLabels` | List<Map<String, Object>> | Radio labels of the Omniscript element from the property set configuration for the radio group child questions. | Small, 60.0 | 60.0 |
| `required` | String | Specifies whether the Omniscript element is required to submit the form. | Small, 60.0 | 60.0 |
| `show` | Map<String, Object> | Display field details for the conditional rendering of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `text` | String | Text of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |
| `type` | String | Type of the Omniscript element from the property set configuration. | Small, 60.0 | 60.0 |

=== ARTICLE: dfdt_apis_requests.htm ===
---
page_id: dfdt_apis_requests.htm
title: Discovery Framework API Requests
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dfdt_apis_requests.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework API Requests

Here’s the list of the Discovery Framework Document Decision API request
    bodies.

- 
**[Assessment Details Input](./connect_requests_assessment_responses_assessment_details_input.htm.md)**  

Input representation of the assessment details of Assessment Response request. 

- 
**[Assessment Links Input](./connect_requests_assessment_links_input.htm.md)**  

Associated assessments including id, category, reason and       sequence.

- 
**[Assessment Reasons Input](./connect_requests_assessment_responses_assessment_reason_input.htm.md)**  

Input representation of the assessment reason in Assessment Response request. 

- 
**[Assessment Responses Input](./connect_requests_assessment_responses_input.htm.md)**  

Input for assessment responses.

- 
**[Assessment Values Input](./connect_requests_assessment_responses_assessment_values_input.htm.md)**  

Input representation of the assessment value of Assessment Response request. 

- 
**[Document Decision Input](./connect_requests_document_decision_input.htm.md)**  

Input representation of the Document Decision request.

- 
**[Question Responses Input](./connect_requests_question_responses_input.htm.md)**  

Input for assessment question responses.

=== ARTICLE: dfdt_apis_resources.htm ===
---
page_id: dfdt_apis_resources.htm
title: Discovery Framework API Resources
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dfdt_apis_resources.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework API Resources

Here’s the list of the Discovery Framework Document Decision API
                resources.

- 
**[Assessment Responses](./connect_resources_save_assessment_responses.htm.md)**  

Save assessment responses from an OmniScript built with the Assessment Questions     app.

- 
**[Document Decision](./connect_resources_document_decision.htm.md)**  

Invoke a Decision Table, accept key-value pairs that match the Decision Table keys, and     return either Document Types or Document Categories and the Document Types associated with     them.

- 
**[Omniscript](./connect_resources_store_discovery_framework_structure.htm.md)**  

Get the discovery framework structure stored as OmniProcess.

=== ARTICLE: dfdt_apis_responses.htm ===
---
page_id: dfdt_apis_responses.htm
title: Discovery Framework API Responses
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dfdt_apis_responses.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: dfdt_connect_apis.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework API Responses

Here’s the list of the Discovery Framework Document Decision API response
                bodies.

- 
**[Additional Attributes Output](./connect_responses_additional_attributes.htm.md)**  

Output representation of the Additional Attributes.

- 
**[Assessment Responses Output](./connect_responses_assessment_responses_output.htm.md)**  

Output of assessment responses.

- 
**[Custom Type Details](./connect_responses_custom_type_details.htm.md)**  

Output representation of the custom type details of the Omniscript elements.

- 
**[Decision Table Document Decision Output](./connect_responses_decision_table_document_decision.htm.md)**  

Decision Table output.

- 
**[Document Decision Output](./connect_responses_document_decision_response.htm.md)**  

Output representation of the Document Decision response, including Decision Table     output.

- 
**[Document Types Output](./connect_responses_document_types.htm.md)**  

Output representation of the Document Type.

- 
**[Omniscript Elements List](./connect_responses_omniscript_elements_list.htm.md)**  

Output representation of the details of the Omniscript elements.

- 
**[Omniscript Output](./connect_responses_omniscript_output.htm.md)**  

Output representation of the details of the Omniscript.

- 
**[Omniscript Element Discovery Framework Output](./connect_responses_os_element_discovery_framework_output.htm.md)**  

Output representation of the custom type details of the Omniscript elements for     Discovery Framework.

- 
**[Omniscript Element Property Set Output](./connect_responses_os_element_property_set_output.htm.md)**  

Output representation of the property set configuration of the Omniscript     elements.

=== ARTICLE: dfdt_connect_apis.htm ===
---
page_id: dfdt_connect_apis.htm
title: Discovery Framework Connect APIs
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/dfdt_connect_apis.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework Connect APIs

Use the Discovery Framework Document Decision Connect APIs to invoke a Decision Table,
    accept key-value pairs that match the Decision Table keys, and return either Document Types or
    Document Categories.

- 
**[Discovery Framework API Resources](./dfdt_apis_resources.htm.md)**  

Here’s the list of the Discovery Framework Document Decision API                 resources.

- 
**[Discovery Framework API Requests](./dfdt_apis_requests.htm.md)**  

Here’s the list of the Discovery Framework Document Decision API request     bodies.

- 
**[Discovery Framework API Responses](./dfdt_apis_responses.htm.md)**  

Here’s the list of the Discovery Framework Document Decision API response                 bodies.

=== ARTICLE: discovery_framework.htm ===
---
page_id: discovery_framework.htm
title: Discovery Framework
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework

The Discovery Framework data model helps manage every aspect of questionnaire-driven
  information collection use cases. By using this data model, your users can collect and validate
  their customers’ information in a compliant manner. For example, financial needs analysis, digital
  onboarding, and more.

| Available in: Discovery Framework is available in Lightning Experience and included in Financial Services Cloud, Health Cloud, Public Sector Solutions, and Consumer Goods Cloud. |
| --- |

  

- 
**[Discovery Framework Standard Objects](./discovery_framework_standard_objects.htm.md)**  

This section lists the standard objects associated with Discovery Framework with their   standard fields. Use the standard objects to create assessment questions and forms.

- 
**[Discovery Framework Metadata API Types](./discovery_framework_metadata_api_parent.htm.md)**  

Metadata API enables you to access some types and feature settings that you can     customize in the user interface.

- 
**[Discovery Framework Invocable Actions](./discovery_framework_actions.htm.md)**  

Use actions to invoke Discovery Framework actions in a flow.

- 
**[Discovery Framework Tooling API Objects](./discovery_framework_tooling_api_objects.htm.md)**  

Tooling API exposes metadata used in developer tooling that you can access through REST   or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller   pieces of metadata. For more information about Tooling API objects and to find a complete   reference of all the supported objects, see **[Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)**.

- 
**[Discovery Framework Connect APIs](./dfdt_connect_apis.htm.md)**  

Use the Discovery Framework Document Decision Connect APIs to invoke a Decision Table,     accept key-value pairs that match the Decision Table keys, and return either Document Types or     Document Categories.

- 
**[DiscoveryFramework_Prefill Integration Procedure](./discoveryframework_prefill_integration_procedure.htm.md)**  

The DiscoveryFramework_Prefill Integration Procedure calls a   Omnistudio   Data Mapper and an Apex class. To customize the prefill flow, edit the steps of   the DiscoveryFramework_Prefill Integration Procedure. Open the OmniStudio app, go to the   Integration Procedures page, expand the DiscoveryFramework/Prefill Integration Procedure, and open   the highest version.

=== ARTICLE: discovery_framework_actions.htm ===
---
page_id: discovery_framework_actions.htm
title: Discovery Framework Invocable Actions
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_actions.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework Invocable Actions

Use actions to invoke Discovery Framework actions in a flow.

- 
**[Get Assessment Response Summary](./actions_obj_get_assessment_response_summary.htm.md)**  

Get Assessment Response Summary makes it easy to use a flow to trigger       server-side document generation using Document Generation.

=== ARTICLE: discovery_framework_channels.htm ===
---
page_id: discovery_framework_channels.htm
title: Supported Metadata Channels
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_channels.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Supported Metadata Channels

In Discovery Framework, you can create questions and question sets to categorize
    questions, and you can move such a dataset across multiple orgs. A metadata wrapper is
    automatically created for these objects.

    
      Metadata APIs provide ways to package those datasets and move them across orgs. There are
        multiple ways to export or import datasets from one org to another. Each way is a metadata
        channel that provides some specific features with the import or export. The public metadata
        API is the basic way in which metadata is serialized so that clients can read, edit, and
        deploy the data into the same or another organization. Exposure in the public metadata API
        is a prerequisite for these channels.
          
            

**[Second-Generation Managed
                Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)**

            
: 
              

Managed packages are used by Salesforce partners to distribute and sell
                applications to customers. 

            

          
          
            

**[Unlocked Packaging](https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_before.htm)**

            
: 
              

Unlocked packages are especially suited for internal business apps. You can use
                unlocked packages to organize your existing metadata, package an app, extend an app
                that you’ve purchased from AppExchange, or package new metadata.

            

          
        

      
        
          

**[Unmanaged Package](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)**

          
: 
            

Unmanaged packages are typically used to distribute open-source projects or
              application templates to provide developers with the basic building blocks for an
              application.

          

        
        
          

**[Change Sets](https://help.salesforce.com/s/articleView?id=platform.changesets.htm&type=5&language=en_US)**

          
: 
            

Use change sets to send customizations from one Salesforce org to another. For
              example, you can create and test a new object in a sandbox org, then send it to your
              production org using a change set.

          

        
        
          

**[Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_rest_deploy_enable_cli.htm)**

          
: 
            

Salesforce CLI is the client-side tool at the center of the modern Salesforce
              developer experience. It’s a command-line interface that simplifies development and
              build automation when working with Salesforce orgs. Use it to create and manage orgs,
              synchronize metadata to and from orgs, create and install packages, and more.

          

        
        
          

**[Source Control
              Integration/Source-Driven Development](https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm)**

          
: 
            

A scratch org is a source-driven and disposable deployment of Salesforce code and
              metadata. A scratch org is fully configurable, allowing developers to emulate
              different Salesforce editions with different features and preferences.

          

        
      

    

    

## Usage

      
      

When importing or exporting the Discovery Framework metadata APIs types across the
        supported channels, we recommend that you review these considerations:

      
        
- When you deploy metadata with a managed package, the namespace is inserted in setup and
          platform objects.

        
- When a dataset is deployed using a change set, the created setup object record has the
          namespace of the target org only. The created platform object record has the Null
          namespace.

        
- When deploying a beta or released version of the managed package in a target org, the
          installation creates both setup and platform objects for AssessmentQuestion and
          AssessmentQuestionSets. The setup object and developerName of the platform object for
          AssessmentQuestion and AssessmentQuestionSets are not editable in a target org. Assessment
          questions in Beta packages are also not editable.

        
- You can update or upgrade a released version of the managed package. Setup and platform
          objects for AssessmentQuestion and AssessmentQuestionSets are updated if there are changes
          in the upgraded version. 

        
- Uninstalling the beta version of the managed package deletes the metadata from the
          target org. Setup objects are deleted for AssessmentQuestion and
          AssessmentQuestionSets.

        
- When using a scratch org,
            
  - Create the scratch org definition
              with:

```
{
  "orgName": "Sample Org",
  "edition": "developer",
  "features": [
    "ASSESSMENTS"
  ],
  "settings": {
    "industriesSettings": {
      "enableIndustriesAssessment": true,
      "enableDiscoveryFrameworkMetadata": true
    }
  }
}
```

            
  - Enabling Discovery Framework (ASSESSMENTS) enables both AssessmentQuestion and
              AssessmentQuestionSet and enabling enableDiscoveryFrameworkMetadata enables the
              metadata for both AssessmentQuestion and AssessmentQuestionSet.

            
  - Add the Assessment to the page layout. See [Page Layouts](https://help.salesforce.com/s/articleView?id=platform.customize_layout.htm&type=5&language=en_US) in Salesforce Help for
              more information.

          

        
- Deploying or retrieving the OmniScript metadata API for Discovery Framework is supported
          only in Change Sets, Salesforce CLI, Source Control Integration/Source-Driven Development,
          and public metadata API channels only.

        
- To avoid deployment errors, do not combine Setup objects and non-setup objects in a
          single transaction. For example, deploy Apex Class and Platform BPOs, such as
          AssessmentQuestion and ExpressionSets separately. See [Deploying OmniStudio Components with Other Objects Causes an
            Exception](https://help.salesforce.com/s/articleView?id=002890891&type=1&language=en_US)

=== ARTICLE: discovery_framework_flow_metadata_api.htm ===
---
page_id: discovery_framework_flow_metadata_api.htm
title: Flow for Discovery Framework
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_flow_metadata_api.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Flow for Discovery Framework

Represents the metadata associated with a flow. With Flow, you can create an
    application that navigates users through a series of screens to query and update records in the
    database. You can also execute logic and provide branching capability based on user input to
    build dynamic applications.

    

## FlowActionCall

      
      

Discovery Framework exposes additional actionType values for the FlowActionCall Metadata
        type. For more information on Flow and FlowActionCall metadata types, see [Flow](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_visual_workflow.htm).

      

          
          
          
          
            
              

              

              

            

          

          
            
              

              

              
- 

            

          

        
| Field Name | Field Type | Description |
| --- | --- | --- |
| actionType | InvocableActionType (enumeration of type string) | Required. The action type. Additional valid values only for Discovery Framework include: `getAssessmentResponseSummary`—Invoke the Get Assessment Response Summary action. This value is available in API version 57.0 and later. |

=== ARTICLE: discovery_framework_metadata_api_parent.htm ===
---
page_id: discovery_framework_metadata_api_parent.htm
title: Discovery Framework Metadata API Types
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_metadata_api_parent.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework Metadata API Types

Metadata API enables you to access some types and feature settings that you can
    customize in the user interface.

    
      

For more information about Metadata API and to find a complete reference of existing
        metadata types, see **[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/)**.

    

  

- 
**[AssessmentQuestion](./meta_assessmentquestion.htm.md)**  

 		Represents the container object that stores the questions 			required for an assessment.

- 
**[AssessmentQuestionSet](./meta_assessmentquestionset.htm.md)**  

Represents the container object for Assessment 			Questions. 	

- 
**[DocumentCategory](./meta_documentcategory.htm.md)**  

Represents a document category.

- 
**[DocumentCategoryDocumentType](./meta_documentcategorydocumenttype.htm.md)**  

Represents the junction between a DocumentCategory and a DocumentType. Puts a 		DocumentType in a DocumentCategory.

- 
**[DocumentType](./meta_documenttype.htm.md)**  

Represents a document type.

- 
**[OmniScript](./meta_omniscript.htm.md)**  

Represents an OmniScript for the Discovery Framework, which 			guides users through sales, service, and other business processes. For Discovery 			Framework, the customization type is `discoveryframework`. 	

- 
**[Supported Metadata Channels](./discovery_framework_channels.htm.md)**  

In Discovery Framework, you can create questions and question sets to categorize     questions, and you can move such a dataset across multiple orgs. A metadata wrapper is     automatically created for these objects.

- 
**[Flow for Discovery Framework](./discovery_framework_flow_metadata_api.htm.md)**  

Represents the metadata associated with a flow. With Flow, you can create an     application that navigates users through a series of screens to query and update records in the     database. You can also execute logic and provide branching capability based on user input to     build dynamic applications.

=== ARTICLE: discovery_framework_standard_objects.htm ===
---
page_id: discovery_framework_standard_objects.htm
title: Discovery Framework Standard Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework Standard Objects

This section lists the standard objects associated with Discovery Framework with their
  standard fields. Use the standard objects to create assessment questions and forms.

| Available in: Discovery Framework is available in Lightning Experience and included in Financial Services Cloud, Health Cloud, Public Sector Solutions, and Consumer Goods Cloud. |
| --- |

  

- 
**[Assessment](./sforce_api_objects_assessment.htm.md)**  

Stores the header data for an assessment. This object is       available in API version 55.0 and later.

- 
**[AssessmentDefinition](./sforce_api_objects_assessmentdefinition.htm.md)**  

       Represents the definition of an assessment including details such as the last          revised date and purpose. This object is available in API version 63.0 and later. 

- 
**[AssessmentQuestion](./sforce_api_objects_assessmentquestion.htm.md)**  

Stores the questions required for an assessment. This object is       available in API version 55.0 and later.

- 
**[AssessmentQuestionAssignment](./sforce_api_objects_assessmentquestionassignment.htm.md)**  

Represents a junction between an assessment question set and an          assessment question. This object is available in API version 55.0 and       later.

- 
**[AssessmentQuestionResponse](./sforce_api_objects_assessmentquestionresponse.htm.md)**  

Stores the responses submitted to an assessment. This object is       available in API version 55.0 and later.

- 
**[AssessmentQuestionSet](./sforce_api_objects_assessmentquestionset.htm.md)**  

Container object for assessment questions. This object is       available in API version 55.0 and later.

- 
**[AssessmentQuestionVersion](./sforce_api_objects_assessmentquestionversion.htm.md)**  

Stores the question versions for the assessment questions. This       object is available in API version 55.0 and later.

- 
**[AssessmentQstnVerChoice2](./sforce_api_objects_assessmentqstnverchoice2.htm.md)**  

       Represents a choice a user can select for an assessment question          version. This object is available in API version 63.0 and later. 

- 
**[AssessmentReason](./sforce_api_objects_assessmentreason.htm.md)**  

       Represents the reasons for an assessment such as the associated coverage          information. This object is available in API version 63.0 and later. 

- 
**[AssessmentSavedSession](./sforce_api_objects_assessmentsavedsession.htm.md)**  

       Represents a session of an assessment that's saved to resume for later.       This object is available in API version 62.0 and later.

- 
**[AssessmentSignature](./sforce_api_objects_assessmentsignature.htm.md)**  

       Stores the respondent’s signature during an assessment. This object is       available in API version 57.0 and later. 

- 
**[AssessmentStagedData](./sforce_api_objects_assessmentstageddata.htm.md)**  

       Represents the responses to assessment questions when a user captures and          submits information with the Discovery Framework Data Capture Flow on a mobile device. The          information is used to create assessment and related records. This object is available       in API version 63.0 and later. 

- 
**[DocumentDecisionRequirement](./sforce_api_objects_documentdecisionrequirement.htm.md)**  

       Represents the decision criteria that will be used to determine applicable          documents. This object is available in API version 59.0 and later. 

- 
**[ExternalAssessmentDefinition](./sforce_api_objects_externalassessmentdefinition.htm.md)**  

       Stores information about external assessments. This object is available       in API version 60.0 and later. 

- 
**[OmniProcessAsmtQuestionVer](./sforce_api_objects_omniprocessasmtquestionver.htm.md)**  

Represents a junction between an OmniScript process and an assessment          question version. This object is available in API version 55.0 and later.

- 
**[SuggestedAssessmentDef](./sforce_api_objects_suggestedassessmentdef.htm.md)**  

       Stores information about suggested assessments. This object is available       in API version 60.0 and later.

- 
**[SuggestedAssessmentReason](./sforce_api_objects_suggestedassessmentreason.htm.md)**  

       Stores the reasons for a suggested assessment. This object is available       in API version 60.0 and later.

=== ARTICLE: discovery_framework_tooling_api_objects.htm ===
---
page_id: discovery_framework_tooling_api_objects.htm
title: Discovery Framework Tooling API Objects
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discovery_framework_tooling_api_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Discovery Framework Tooling API Objects

Tooling API exposes metadata used in developer tooling that you can access through REST
  or SOAP. Tooling API’s SOQL capabilities for many metadata types allow you to retrieve smaller
  pieces of metadata. For more information about Tooling API objects and to find a complete
  reference of all the supported objects, see **[Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)**.

- 
**[AssessmentQuestionConfig](./tooling_api_objects_assessmentquestionconfig.htm.md)**  

Represents the assessment question record metadata          configuration. This object is available in API version 56.0 and later.

- 
**[AssessmentQuestionSetConfig](./tooling_api_objects_assessmentquestionsetconfig.htm.md)**  

Reqpresents the assessment question set record metadata          configuration. This object is available in API version 56.0 and later.

#### See Also

- [Tooling API Developer Guide: SOAP Calls](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_soap_overview.htm)

=== ARTICLE: discoveryframework_prefill_integration_procedure.htm ===
---
page_id: discoveryframework_prefill_integration_procedure.htm
title: DiscoveryFramework_Prefill Integration Procedure
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/discoveryframework_prefill_integration_procedure.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DiscoveryFramework_Prefill Integration Procedure

The DiscoveryFramework_Prefill Integration Procedure calls a
  Omnistudio
  Data Mapper and an Apex class. To customize the prefill flow, edit the steps of
  the DiscoveryFramework_Prefill Integration Procedure. Open the OmniStudio app, go to the
  Integration Procedures page, expand the DiscoveryFramework/Prefill Integration Procedure, and open
  the highest version.

  

    
     
      

     

    

   
| Available in: Lightning Experience in **Enterprise**, **Professional**, and **Unlimited** editions where a Financial Services Cloud Growth license is enabled or in **Enterprise** and **Unlimited** editions where the Health Cloud license is enabled. |
| --- |

  

  

#### Note

To ensure access to this Integration Procedure, see [Security for
     Omnistudio
     Data Mappers and Integration Procedures](https://help.salesforce.com/s/articleView?id=xcloud.os_security_for_dataraptors_and_integration_procedures_56519.htm&type=5&language=en_US).

  

## Steps

   
   
    

      
      
      
      
      
       
        

        

        

        

       

      

      
       
        

        

        

        

       

       
        

        

        

        

       

       
        

        

        

        

       

      

     
| Component Name | Type | What it does | What it calls |
| --- | --- | --- | --- |
| GetAssessmentId | Omnistudio Data Mapper Extract Action | Fetches the Id of the most recent Assessment record related to the specified ContextId, which is an AccountId. | GetAssessmentId Omnistudio Data Mapper Extract |
| GetAssessmentData | Remote Action | Fetches the Assessment record object. | DiscoveryFrmwrk.PreFillAssessment Apex class |
| AssessmentData | Response Action | Returns the Assessment record data to the entity that called this Integration Procedure. | Nothing |

   

  

  

## GetAssessmentId
    Omnistudio
    Data Mapper

   
   

The GetAssessmentId
    Omnistudio
    Data Mapper Extract fetches the ID of the most recent Assessment record
    related to the specified ContextId, which is an AccountId.

   
    
     

**Settings**

     
: 
      
       

         
         
         
         
          
           

           

           

          

         

         
          
           

           

           

          

          
           

           

           

          

          
           

           

           

          

          
           

           

           

          

          
           

           

           

          

         

        
| Tab | Setting | Value |
| --- | --- | --- |
| Extract | Object | Assessment |
| Extract | Extract Output Path | Assessment |
| Extract | Filter | AccountId = ContextId ORDER BY LastModifiedDate DESC LIMIT 1 |
| Output | Extract JSON Path | Assessment:Id |
| Output | Output JSON Path | RemoteActionAssessmentId |

      

     

    
   

  

  

## PreFillAssessment Apex Class

   
   

Use the PreFillAssessment class to fetch question and response data related to an Assessment
    object.

   
    
     

**Namespace**

     
: DiscoveryFrmwrk

    
    
     

**Usage**

     
: The PreFillAssessment class has two methods that do the same thing. The call method is
      necessary for the class to implement System.Callable.

    
    
     

**Methods**

     
: 
      
       
- call(action, args)

       
- omniScriptPreFill(input, output) 

      

      

call(action, args)

     

    
   

  

  

## call(action, args)

   
   

The call method accepts an Assessment Id and passes question and response data to the
    AssessmentDataReturned output variable. It follows the syntax required for a class that
    implements System.Callable. 

   
    
     

**API Version**

     
: 57.0

    
    
     

**Required Chatter**

     
: No

    
    
     

**Signature**

     
: `public static PreFillAssessment call(String action,
       Map<String,Object> args)`

    
    
     

**Parameters**

     
: **action**

     
: Type: `string`

     
: Set the action value to omniScriptPreFill

     
: **args**

     
: Type: `Map<String,Object>`

     
: The first two names in the name-value pairs must be input and output. The input must
      specify an Assessment Id. The output must be null. For example: `{“input”: “0U3RO0000000Aai0AE”, “output”: null}`

    
    
     

**Return Value**

     
: null

    
    
     

**Usage**

     
: See the omniScriptPreFill method usage

    
   

  

  

## omniScriptPreFill(input, output)

   
   

The omniScriptPreFill method accepts an Assessment Id and passes question and response data to
    the AssessmentDataReturned output variable.

   
    
     

**API Version**

     
: 57.0

    
    
     

**Required Chatter**

     
: No

    
    
     

**Signature**

     
: `public static PreFillAssessment
       omniScriptPreFill(Map<String,Object> input, Map<String,Object> output)`

    
    
     

**Parameters**

     
: **input**

     
: Type: `Map<String,Object>`

     
: Set the input parameter to {“input”: “idString”}, where the idString is the Id of an
      Assessment object. For example: `{“input”:
       “0U3RO0000000Aai0AE”}`

     
: **output**

     
: Type: `Map<String,Object>`

     
: In the input, set the output parameter to `{“output”:
       null}`.

    
    
     

**Return Value**

     
: null

    
    
     

**Usage**

     
: The data passed to the AssessmentDataReturned variable includes questions and their
      responses. The key for each question is the developer name of the question. For
      example:

```
{
  "AssessmentDataReturned": {
    "RespondentName": "Arthur, King of the Britons.",
    "RespondentGoal": "To seek the Holy Grail.",
    "SwallowAirspeed": "An African or European swallow?"
  }
}

```

=== ARTICLE: meta_assessmentquestion.htm ===
---
page_id: meta_assessmentquestion.htm
title: AssessmentQuestion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_assessmentquestion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestion

		Represents the container object that stores the questions
			required for an assessment.

		
		

## Parent Type

			This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

AssessmentQuestion components have the suffix
					.AssessmentQuestion and are stored in the
					AssessmentQuestions folder.

		

		

## Version

			
			

AssessmentQuestion components are available in API version 55.0 and later.

		

		
		

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

						

					

				
| Field Name | Description |
| --- | --- |
| assessmentQuestionVersion | **Field Type** [AssessmentQuestionVersion](#AssesQVer) **Description** The object that stores the question versions for the assessment questions. |
| dataType | **Field Type** string **Description** Required. The data type of the assessment question. |
| developerName | **Field Type** string **Description** Required. The developer name of the assessment question. Can contain only underscores and alphanumeric characters and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. |
| displayTextCategory | **Field Type** string **Description** Specifies the category of the display text when the data type is Text Block. |
| formulaResponseDataType | **Field Type** string **Description** Specifies the data type of the question response calculated by a formula. |
| name | **Field Type** string **Description** Required. The name of the record. |
| questionCategory | **Field Type** string **Description** Required. Stores the question category. |
| relatedQuestion | **Field Type** string **Description** Specifies the related question. Used to define a question hierarchy. |

		

		

## AssessmentQuestionVersion​​

			
			

Stores the question versions for the assessment questions.

			

					
					
					
						
							

							

						

					

					
						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 

						

						
							

							

: 

: 
: 
: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 
: 

						

						
							

							

: 

: 
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
| additionalInformation | **Field Type** string **Description** The additional details for a UI element, such as the disclosure text. |
| description | **Field Type** string **Description** The description for the assessment question. This text isn’t rendered on the assessment. |
| guidanceInformation | **Field Type** string **Description** The guidance for the assessment question. |
| helpText | **Field Type** string **Description** The text that's added as an info bubble in the UI element related to the assessment question. |
| isActive | **Field Type** boolean **Description** Required. Indicates whether the current version of the assessment question is set to active (`true`) or not (`false`). The default value is `false`. |
| name | **Field Type** string **Description** Required. Name of the assessment question version record. |
| optionSourceResponseValue | **Field Type** boolean **Description** Indicates whether the response value source for an assessment question is configured as custom (`true`) or sObject in the OmniStudio designer (`false`). The default value is `false`. |
| questionText | **Field Type** string **Description** Required. The assessment question text. Contains the label for the assessment question that appears on the assessment. |
| responseValues | **Field Type** string **Description** Holds the values to be defined in the picklist, multiselect picklist, or radio buttons. |
| status | **Field Type** string **Description** Required. Status of the assessment question version. Possible values are Draft, Active, or Archived. |
| versionNumber | **Field Type** int **Description** Required. The assessment question version number. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an AssessmentQuestion component.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<AssessmentQuestion
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<assessmentQuestionVersion>
		<additionalInformation>ParentQuestionDevName AI</additionalInformation>
		<description>ParentQuestionDevName Desc</description>
		<helpText>ParentQuestionDevName HT</helpText>
		<isActive>true</isActive>
		<name>ParentQuestionDevName</name>
		<optionSourceResponseValue>true</optionSourceResponseValue>
		<questionText>ParentQuestionDevName Text</questionText>
		<status>Active</status>
		<versionNumber>1</versionNumber>
	</assessmentQuestionVersion>
	<dataType>DateTime</dataType>
	<developerName>ParentQuestionDevName</developerName>
	<name>ParentQuestionDevName</name>
	<questionCategory>Demographic</questionCategory>
</AssessmentQuestion>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>AssessmentQuestion</name>
	</types>
	<version>55.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
        File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

    

		

## Usage

			
			Before you retrieve assessment questions, we recommend that you review these considerations.
					
- When you retrieve an assessment question, you also get the related
						assessment question version with the status Active..

#### Note

If an active
							assessment question version doesn’t exist for the assessment question,
							then the latest assessment question version with Status as Draft is
							retrieved.

					
- The value for the `<status>` tag in
						the XML definition must match the status of the related assessment question
						version.

					
- If an assessment question has a related assessment question (parent
						question), the XML definition must include the developer name of the related
						assessment question.

					
- If the fields of an assessment question contain values, the XML definition
						must contain tags with those values when retrieving it.

				

			Before you deploy assessment questions, we recommend that you review these considerations.
					
- If the Related Question isn’t available in the target org, deploying the
						assessment question fails.

					
- If an assessment question with the same developer name exists in the target
						org, deploying the assessment question updates the values of the other
						fields in the target org.

					
- If the `<versionNumber>` tag is
						present in the XML definition of an assessment question, deploying creates a
						version for that question in the target org.

					
- If the Related Questions aren’t available in target org but available in the
						package, then deploying the questions inserts the Related Questions in the
						correct order.

					
- If the assessment questions are associated with flows of type Discovery
						Framework Data Capture Flow, then deploy the assessment questions first.
						After deploying the assessment questions, deploy the flows.

=== ARTICLE: meta_assessmentquestionset.htm ===
---
page_id: meta_assessmentquestionset.htm
title: AssessmentQuestionSet
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_assessmentquestionset.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionSet

Represents the container object for Assessment
			Questions.
	

		
		

## Parent Type

			This type extends the Metadata metadata type and inherits its
				fullName field. 

		

## File Suffix and Directory Location

			
			

AssessmentQuestionSet components have the suffix
					.AssessmentQuestionSet and are stored in the
					AssessmentQuestionSets folder.

		

		

## Version

			
			

AssessmentQuestionSet components are available in API version 55.0 and later.

		

		
		

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
| assessmentQuestionDeveloperNames | **Field Type** string[] **Description** The developer names for the assessment question. Can contain only underscores and alphanumeric characters and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. |
| developerName | **Field Type** string **Description** Required. The developer name for the assessment question set. Can contain only underscores and alphanumeric characters and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. |
| name | **Field Type** string **Description** Required. The question set name. |

		

		

## Declarative Metadata Sample Definition

			
			

The following is an example of an AssessmentQuestionSet component.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<AssessmentQuestionSet
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<developerName>QuestionSetDevName</developerName>
	<name>QuestionSetName</name>
	<assessmentQuestionDeveloperNames>QuestionDevName</assessmentQuestionDeveloperNames>
</AssessmentQuestionSet>
```

			

The following is an example `package.xml` that
				references the previous definition.

			

```

<?xml version="1.0" encoding="UTF-8"?>
<Package
	xmlns="http://soap.sforce.com/2006/04/metadata">
	<types>
		<members>*</members>
		<name>AssessmentQuestion</name>
	</types>
	<types>
		<members>*</members>
		<name>AssessmentQuestionSet</name>
	</types>
	<version>55.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

      
      

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest
        file. For information about using the manifest file, see [Deploying and Retrieving Metadata with the Zip
        File](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/file_based_zip_file.htm).

    

		

## Usage

			
			Before you retrieve assessment question sets, we recommend that you review these considerations.
					
- When retrieving an assessment question set, if its fields contain values,
						then the XML definition must contain tags with those values.

					
- When retrieving an assessment question set, if that set is associated with
						multiple questions, then the XML definition must contain developer names of
						all the associated questions.

				

			Before you deploy assessment question sets, we recommend that you review these considerations.
					
- When deploying an assessment question set, if an assessment question set
						with the same developer name doesn't exist in the target org, deploying
						creates one with that name.

					
- If an assessment question set with the same developer name exists in the
						target org, then deploying the question set updates the values of the other
						fields in the target org.

					
- If the questions associated with the assessment question set don't exist in
						the target org, deploying the assessment question set fails.

					
- If the questions associated with the assessment question set don’t exist in
						the target org but are available in the package, then deploying the
						assessment question sets inserts the questions in the correct order.

=== ARTICLE: meta_documentcategory.htm ===
---
page_id: meta_documentcategory.htm
title: DocumentCategory
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_documentcategory.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DocumentCategory

Represents a document category.

	

	

## Parent Type

		
		This type extends the Metadata metadata type and inherits its fullName field.
	

	

## File Suffix and Directory Location

		
		

DocumentCategory components have the suffix .documentCategory and are stored in the documentCategory folder.

	

	

## Version

		
		

DocumentCategory components are available in API version 59.0 and later.

	

	

## Special Access Rules

		
			
	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** A description of the DocumentCategory. |
| isProtected | **Field Type** boolean **Description** An auto-generated value that doesn’t impact the behavior of the metadata type. The default value is `false`. |
| masterLabel | **Field Type** string **Description** Required. The master label of the DocumentCategory. This internal label doesn’t get translated. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a DocumentCategory component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<DocumentCategory xmlns="http://soap.sforce.com/2006/04/metadata">
    <masterLabel>Address_Proof</masterLabel>
</DocumentCategory>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>DocumentCategory</name>
    </types>
    <version>59.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

=== ARTICLE: meta_documentcategorydocumenttype.htm ===
---
page_id: meta_documentcategorydocumenttype.htm
title: DocumentCategoryDocumentType
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_documentcategorydocumenttype.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DocumentCategoryDocumentType

Represents the junction between a DocumentCategory and a DocumentType. Puts a
		DocumentType in a DocumentCategory.

	

	

## Parent Type

		
		This type extends the Metadata metadata type and inherits its fullName field.
	

	

## File Suffix and Directory Location

		
		

DocumentCategoryDocumentType components have the suffix .documentCategoryDocumentType and are stored in the documentCategoryDocumentTypes folder.

	

	

## Version

		
		

DocumentCategoryDocumentType components are available in API version 59.0  and later.

	

	

## Special Access Rules

		
		
	

	

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
| documentCategory | **Field Type** string **Description** Required. The master label of the related DocumentCategory. |
| documentType | **Field Type** string **Description** Required. The master label of the related DocumentType. |
| isProtected | **Field Type** boolean **Description** An auto-generated value that doesn’t impact the behavior of the metadata type. The default value is `false`. |
| masterLabel | **Field Type** string **Description** Required. The master label of the DocumentCategoryDocumentType. This internal label doesn’t get translated. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a DocumentCategoryDocumentType component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<DocumentCategoryDocumentType xmlns="http://soap.sforce.com/2006/04/metadata">
    <documentCategory>Address_Proof</documentCategory>
    <documentType>Utility_Bill</documentType>
    <masterLabel>junction1</masterLabel>
</DocumentCategoryDocumentType>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>DocumentCategory</name>
    </types>
    <types>
        <members>*</members>
        <name>DocumentCategoryDocumentType</name>
    </types>
    <types>
        <members>*</members>
        <name>DocumentType</name>
    </types>
    <version>59.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

=== ARTICLE: meta_documenttype.htm ===
---
page_id: meta_documenttype.htm
title: DocumentType
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_documenttype.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_metadata_api_parent.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DocumentType

Represents a document type.

	

	

## Parent Type

		
		This type extends the Metadata metadata type and inherits its fullName field.
	

	

## File Suffix and Directory Location

		
		

DocumentType components have the suffix .documentType and are stored in the documentTypes folder.

	

	

## Version

		
		

DocumentType components are available in API version 59.0 and later.

	

	

## Special Access Rules

		
			
	

	

## Fields

		

		

			
			
			
				
					

					

				

			

			

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				
					

				

: 

: 

				

				

			
| Field Name | Description |
| --- | --- |
| description | **Field Type** string **Description** A description of the DocumentType. |
| isActive | **Field Type** boolean **Description** Required. Specifies whether the DocumentType is active. |
| masterLabel | **Field Type** string **Description** Required. The master label of the DocumentType. This internal label doesn’t get translated. |

	

		

## Declarative Metadata Sample Definition

		
			

The following is an example of a DocumentType component.

			

```
<?xml version="1.0" encoding="UTF-8"?>
<DocumentType xmlns="http://soap.sforce.com/2006/04/metadata">
    <description>Utility_Bill</description>
    <isActive>true</isActive>
    <masterLabel>Utility_Bill</masterLabel>
</DocumentType>
```

			

The following is an example `package.xml` that
			references the previous definition.

			

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>*</members>
        <name>DocumentType</name>
    </types>
    <version>59.0</version>
</Package>
```

		

		

## Wildcard Support in the Manifest File

			
			

This metadata type supports the wildcard character `*` (asterisk) in the package.xml manifest file.
				For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

=== ARTICLE: sforce_api_objects_assessment.htm ===
---
page_id: sforce_api_objects_assessment.htm
title: Assessment
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessment.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Assessment

Stores the header data for an assessment. This object is
      available in API version 55.0 and later.

      

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
| AccountId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the account for which the assessment was taken. This is a relationship field. **Relationship Name** Account **Relationship Type** Lookup **Refers To** Account |
| AssessedParticipantId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the agent or rep associated with the assessment. This field is available in API version 67.0 and later. This field is a polymorphic relationship field. **Relationship Name** AssessedParticipant **Refers To** BotDefinition, ExternalConversationBotDef, User |
| AssessmentChannelId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the associated voice, messaging, or case conversations being assessed. This field is available in API version 67.0 and later. This field is a polymorphic relationship field. **Relationship Name** AssessmentChannel **Refers To** Case, MessagingSession, VoiceCall |
| ApplicantId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The applicant for whom the assessment was carried out. This field is available only if you have enabled Integrated Onboarding for Financial Services Cloud. This field is a relationship field. |
| AssessmentMode | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Possible values for assessment mode: `Automated` `Manual` `Overridden` This field is available in API version 67.0 and later. |
| AssessmentRating | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The overall rating for the assessment. Possible values are: `High` `Low` `Medium` |
| AssessmentStagedDataId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The Assessment Staged Data that's associated with this assessment. This field is a relationship field. **Relationship Name** AssessmentStagedData **Refers To** AssessmentStagedData |
| AssessmentStatus | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The status of the assessment. Possible values are: `Canceled` `Completed` `In Progress` |
| AssessmentSummary | **Type** textarea **Properties** Create, Nillable, Update **Description** The summary of the evaluated assessment. This field is available in API version 68.0 and later. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization. |
| AssessorId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The person who carried out the assessment and recorded the responses. This field is a polymorphic relationship field. **Relationship Name** Assessor **Refers To** Account, Contact, HealthcareProvider, User |
| CareProgramSiteId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** Stores the derived Care Program Site Identifier when the site assessment is done in the context of care program sites. This field is available in API version 63.0 when Site Management is enabled. This is a relationship field. **Relationship Name** CareProgramSite **Refers To** CareProgramSite |
| CaseId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the case associated with the assessment. This is a relationship field. **Relationship Name** Case **Relationship Type** Lookup **Refers To** Case |
| ChannelLastInteractionDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time of the last interaction with the agent or rep being assessed. This field is available in API version 67.0 and later. |
| ChannelType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The type of channel for the conversation being assessed. This field is available in API version 67.0 and later. Possible values are: `Case` `MessagingSession` `VoiceCall` |
| CompletedDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the assessment was completed. |
| ConfidenceScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The relative confidence score of the assessment insight, expressed as a value between 0.0 and 1.0. Higher values (closer to 1.0) indicate greater confidence. This field is available in API version 68.0 and later. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization. |
| ContactId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the contact associated with the assessment. This is a relationship field. **Relationship Name** Contact **Relationship Type** Lookup **Refers To** Contact |
| EffectiveDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The timestamp from when the assessment is effective. |
| ExpirationDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The timestamp from when the assessment lapses. |
| ExternalAssessmentDefId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The associated external assessment definition. This field is a relationship field. **Relationship Name** ExternalAssessmentDef **Relationship Type** Lookup **Refers To** ExternalAssessmentDefinition |
| Identifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier of a completed or partially completed assessment in the source system. |
| IsSavedForLater | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the assessment is saved as a draft (true) or not (false). The default value is false. This field is available in API version 60.0 and later. |
| IsSuggestedAssessment | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the assessment is a suggested assessment (true) or not (false). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| MaximumScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The total score derived from all applicable questions, used as the denominator in percentage calculations. This field is available in API version 67.0 and later. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the assessment. |
| OmniProcessId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The OmniScript associated with the assessment record. This field is available in API version 56.0 and later. This field is a relationship field. **Relationship Name** OmniProcess **Relationship Type** Lookup **Refers To** OmniProcess |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the related assessment, if any. This is a relationship field. **Relationship Name** Parent **Relationship Type** Lookup **Refers To** Assessment |
| PartyProfileId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Represents information about the profile of a party, such as a contact, account, or lead. This field is available only if you’ve enabled the Know Your Customer setting in your Salesforce org. **Relationship Name** PartyProfile **Relationship Type** Lookup **Refers To** PartyProfile |
| ResponseContextId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The record in which context the response was taken. This field is available in API version 56.0 and later where Public Sector Solutions is enabled. This field is a polymorphic relationship field. **Relationship Name** ResponseContext **Relationship Type** Lookup **Refers To** ApplicationFormEvaluation - Available in API version 62.0 and later BusinessLicenseApplication CarePlan IndividualApplication PublicComplaint VettingEvaluation - Available in API version 62.0 and later Visit |
| StatusReason | **Type** textarea **Properties** Create, Nillable, Update **Description** The reason why an assessment was incomplete or unsuccessful.This field is available in API version 68.0 and later. |
| Type | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the type of assessment. This field is available only if you have enabled Integrated Onboarding for Financial Services Cloud. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentdefinition.htm ===
---
page_id: sforce_api_objects_assessmentdefinition.htm
title: AssessmentDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentDefinition

      Represents the definition of an assessment including details such as the last
         revised date and purpose. This object is available in API version 63.0 and later. 

      

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

                  

            

            
| Field | Details |
| --- | --- |
| ApprovalDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the assessment was approved by the publisher. |
| DisplayType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the display format for questions in the assessment for the end-user. |
| EffectiveFromDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date when the assessment takes effect. |
| EffectiveToDate | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date until the assessment is in effect. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the record was last referenced. |
| LastRevisedDateTime | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The date and time when the assessment was last revised. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The user who owns the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| PerformerType | **Type** multipicklist **Properties** Create, Filter, Nillable, Update **Description** Specifies the type of performer that can record responses to the assessment. |
| PublisherId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The organization or individual that published the assessment. This field is a polymorphic relationship field. **Relationship Name** Publisher **Refers To** Account, Contact, User |
| Purpose | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The purpose of the assessment. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentDefinitionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentDefinitionHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentDefinitionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[AssessmentDefinitionShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentqstnverchoice2.htm ===
---
page_id: sforce_api_objects_assessmentqstnverchoice2.htm
title: AssessmentQstnVerChoice2
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentqstnverchoice2.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQstnVerChoice2

      Represents a choice a user can select for an assessment question
         version. This object is available in API version 63.0 and later. 

      

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
      

      

      

## Supported Calls

Only users with the Education Cloud Full Access
            permission set can access this object.

      

      

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

: 

: 
: 

                  

               

            
| Field | Details |
| --- | --- |
| AssessmentQuestionVersionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The assessment question version related to the assessment question version choice. This field is a relationship field. **Relationship Name** AssessmentQuestionVersion **Relationship Type** Master-detail **Refers To** AssessmentQuestionVersion (the master object) |
| ChoiceDescription | **Type** textarea **Properties** Create, Nillable, Update **Description** The description of the criteria that determine when the assessment question version choice is valid for evaluation. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization.This field is available in API version 67.0 and later. |
| ChoiceScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The score assigned for evaluating the assessment question version. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization.This field is available in API version 67.0 and later. |
| CurrencyIsoCode | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** The ISO code for the currency related to the assessment question version choice. Possible values are: `GBP`—British Pound `USD`—U.S. Dollar The default value is `USD`. |
| DisplayOrder | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The order in which the question choices is displayed for an assessment question version. |
| Icon | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The name of the icon presented as a question choice when the assessment question is of the icon type. |
| IsExcludedFromScoring | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the specific choice is excluded when calculating the total score (`true`) or not (`false`). The default value is `false`. This field is available in API version 68.0 and later. |
| Key | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** A unique code or identifier for a question choice that's mapped to an assessment question version. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last accessed this record, a record related to this record, or a list view. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp when the current user last viewed this record or list view. If this value is null, the user might have only accessed this record or list view (LastReferencedDate) but not viewed it. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the assessment question version choice. |
| UniqueIndex | **Type** string **Properties** Filter, Group, idLookup, Nillable, Sort **Description** The unique index for the AssessmentQuestionVersionId and Key pair. This field is a calculated field. |

=== ARTICLE: sforce_api_objects_assessmentquestion.htm ===
---
page_id: sforce_api_objects_assessmentquestion.htm
title: AssessmentQuestion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentquestion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestion

Stores the questions required for an assessment. This object is
      available in API version 55.0 and later.

      

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

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
- 

                  

            

            
| Field | Details |
| --- | --- |
| ActiveVersionId | **Type** reference **Properties** Filter, Group, Nillable, Sort **Description** The ID of the active version of the assessment question. This is a relationship field. **Relationship Name** ActiveVersion **Relationship Type** Lookup **Refers To** AssessmentQuestionVersion |
| DataType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Required. The data type of the assessment question. Possible values are: `Checkbox` `Currency` `Date` `DateTime` `Decimal` `Disclosure` `EditBlock`—Edit Block `Email` `File` `Formula` `Integer` `Multiselect`—Multi-select `Radio` `RadioGroup`—Radio Group `Select` `Telephone` `Text` `TextArea`—Text Area `TextBlock`—Text Block `Time` `URL` |
| Description | **Type** textarea **Properties** Filter, Nillable, Sort **Description** The description for the assessment question. This text is not rendered on the assessment. |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. |
| DisplayTextCategory | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the category of the display text when the data type is Text Block. Possible values are: `Instruction` `Legal` `Security` |
| FormulaResponseDataType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the data type of the question response calculated by a formula. Possible values are: `Boolean` `Currency` `Date` `Decimal` `Integer` `Text` |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| QuestionCategory | **Type** picklist **Properties** Create, Filter, Group, Sort, Update **Description** Required. Stores the question category. Possible values are: `Demographic` `Financial` |
| QuestionText | **Type** textarea **Properties** Filter, Nillable, Sort **Description** Required. The label for the assessment question that appears on the assessment. |
| RelatedQuestionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Identifies the ID of the related question. Used to define a question hierarchy. This is a relationship field. **Relationship Name** RelatedQuestion **Relationship Type** Lookup **Refers To** AssessmentQuestion |
| ShouldExcludeFromMetadata | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort **Description** Indicates whether the assessment question record should be excluded from metadata (true) or not (false). The default value is `false`. |
| ShouldHideInDesigner | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort **Description** Indicates whether the assesment question record should be hidden in OmniScript designer (true) or not (false). The default value is `false`. |
| SourceSystemName | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the source system name from where the content of the assessment question was retrieved. Possible values are: `MCG` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentQuestionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentQuestionFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentQuestionHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentQuestionShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentquestionassignment.htm ===
---
page_id: sforce_api_objects_assessmentquestionassignment.htm
title: AssessmentQuestionAssignment
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentquestionassignment.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionAssignment

Represents a junction between an assessment question set and an
         assessment question. This object is available in API version 55.0 and
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
| AssessmentQuestionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the assessment question associated with this record. This is a relationship field. **Relationship Name** AssessmentQuestion **Relationship Type** Lookup **Refers To** AssessmentQuestion |
| AssessmentQuestionSetId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the assessment question set associated with this record. This is a relationship field. **Relationship Name** AssessmentQuestionSet **Relationship Type** Lookup **Refers To** AssessmentQuestionSet |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| SequenceNumber | **Type** int **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The sequence number for an assessment question in an assessment question set. Available in API version 64.0 and later. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentQuestionAssignmentChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentQuestionAssignmentFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentQuestionAssignmentHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentQuestionAssignmentShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentquestionresponse.htm ===
---
page_id: sforce_api_objects_assessmentquestionresponse.htm
title: AssessmentQuestionResponse
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentquestionresponse.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionResponse

Stores the responses submitted to an assessment. This object is
      available in API version 55.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AssessmentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Required. The ID of the assessment associated with this record. This is a relationship field. **Relationship Name** Assessment **Relationship Type** Master-detail **Refers To** Assessment (the master object) |
| AssessmentQuestionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the assessment question associated with this record. This is a relationship field. **Relationship Name** AssessmentQuestion **Relationship Type** Lookup **Refers To** AssessmentQuestionVersion |
| ChoiceValue | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** The response value when the question's data type is choice. |
| CurrencyValue | **Type** currency **Properties** Create, Filter, Nillable, Sort, Update **Description** The response value when the question's data type is currency. |
| DateTimeValue | **Type** dateTime **Properties** Create, Filter, Nillable, Sort, Update **Description** The response value when the question's data type is date time. |
| DateValue | **Type** date **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The response value when the question's data type is date. |
| DecimalResponseValue | **Type** double **Properties** Create, Filter, idLookup, Nillable, Sort, Update **Description** The response value when the question's data type is decimal. |
| ExtlAssessmentQuestionText | **Type** textarea **Properties** Create, Nillable, Update **Description** Stores the external assessment question text. |
| ExtlResponseValueIdentifier | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The unique identifier of a response to a question in an external assessment. |
| IntegerResponseValue | **Type** int **Properties** Create, Filter, Group, idLookup, Nillable, Sort, Update **Description** The response value when the associated assessment question's data type is integer. |
| IsTrueOrFalseValue | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The response value when the question's data type is boolean. The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of this record. |
| OriginType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the origin of the assessment question response. Possible values are: `Auto` `Manual` `Override` |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| ParentAsmtQuestionVersionId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the related assessment question version associated with the assessment question response. This is a relationship field. **Relationship Name** ParentAsmtQuestionVersion **Relationship Type** Lookup **Refers To** AssessmentQuestionVersion |
| RespondentTimezone | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The auto-generated timezone of the respondent submitting the assessment response. |
| ResponseComment | **Type** textarea **Properties** Create, Nillable, Update **Description** The notes for evaluating the assessment question. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization. This field is available in API version 67.0 and later. |
| ResponseText | **Type** textarea **Properties** Create, Nillable, Update **Description** The response value when the question's data type is text. |
| ResponseType | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The data type of the response value submitted. |
| ResponseValue | **Type** textarea **Properties** Nillable **Description** The response value to the assessment question. |
| ResponseValueScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** The score of the assessment question response value. |
| ReviewerId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The person who reviewed and edited the response. This field is a polymorphic relationship field. **Relationship Name** Reviewer **Refers To** Account, Contact, HealthcareProvider, User |
| ReviewerRoleId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The role of the person who reviewed and edited the response. This field is a polymorphic relationship field. **Relationship Name** ReviewerRole **Refers To** CodeSet, CodeSetBundle |
| TimeValue | **Type** time **Properties** Create, Filter, idLookup, Nillable, Sort, Update **Description** The response value when the question's data type is time. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentQuestionResponseChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentQuestionResponseFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentQuestionResponseHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentQuestionResponseShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentquestionset.htm ===
---
page_id: sforce_api_objects_assessmentquestionset.htm
title: AssessmentQuestionSet
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentquestionset.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionSet

Container object for assessment questions. This object is
      available in API version 55.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| DeveloperName | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Required. The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The question set name. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentQuestionSetChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentQuestionSetFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentQuestionSetHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentQuestionSetShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentquestionversion.htm ===
---
page_id: sforce_api_objects_assessmentquestionversion.htm
title: AssessmentQuestionVersion
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentquestionversion.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionVersion

Stores the question versions for the assessment questions. This
      object is available in API version 55.0 and later.

      

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
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

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 
: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

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

                  

                  
                     

                     

: 

: 

: 

                  

                  
                     

                     

: 

: 

: 

                  

               

            
| Field | Details |
| --- | --- |
| ActivationDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the assessment question version was set to active. |
| AdditionalInformation | **Type** textarea **Properties** Create, Nillable, Update **Description** The additional details for an UI element, such as the disclosure text. |
| AssessmentQuestionId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** Required. The ID of the assessment question associated with this record. This is a relationship field. **Relationship Name** AssessmentQuestion **Relationship Type** Lookup **Refers To** AssessmentQuestion |
| AssessmentQuestionSourceDocId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The ID of the assessment question source document that's associated with the assessment question version. This field is a relationship field. **Relationship Name** AssessmentQuestionSourceDoc **Relationship Type** Lookup **Refers To** AssessmentQuestionSourceDoc This field is available in API version 61.0 and later for users with the Generative AI Assessment Questions user license. |
| DataType | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** The data type of the assessment question associated with this record. Possible values are: `Checkbox` `Currency` `Date` `DateTime` `Decimal` `Disclosure` `EditBlock`—Edit Block `Email` `File` `Formula` `Integer` `Multiselect`—Multi-select `Radio` `RadioGroup`—Radio Group `Select` `Telephone` `Text` `TextArea`—Text Area `TextBlock`—Text Block `Time` `URL` |
| DeactivationDateTime | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the assessment question version was set to inactive. |
| Description | **Type** textarea **Properties** Create, Filter, Nillable, Sort, Update **Description** The description for the assessment question. This text is not rendered on the assessment. |
| DisplayTextCategory | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Specifies the category of the display text when the data type is Text Block. Possible values are: `Instruction` `Legal` `Security` |
| HelpText | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The text that's added as an infobubble in the UI element related to the assessment question. |
| IsActive | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the current version of the assessment question is set to active (`true`) or not (`false`). The default value is `false`. |
| IsOptionSourceResponseValue | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the response value source for an assessment question is configured as custom or SObject in the OmniStudio designer (`true`) or not (`false`). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| MaximumScore | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** Maximum score derived from all applicable response choices for a question, used as the denominator in percentage calculations. This field is visible only if you have the QualityManagementEnabled permission enabled for your organization.This field is available in API version 67.0 and later. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** Required. The name of the assessment question version record. |
| QuestionCreationType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies how the assessment question is created from the assessment question source document. Possible values are: `GenAI` This field is available in API version 61.0 and later for users with the Generative AI Assessment Questions user license. |
| QuestionText | **Type** textarea **Properties** Create, Filter, Sort, Update **Description** Required. The assessment question text. Holds the label for the assessment question that appears on the assessment. |
| ResponseValues | **Type** textarea **Properties** Create, Nillable, Update **Description** Specifies the values to be defined in the picklist, multiselect picklist, or radio buttons. |
| Status | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The status of the assessment question version. |
| VersionNumber | **Type** int **Properties** Filter, Group, Nillable, Sort **Description** The assessment question version number. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentQuestionVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentQuestionVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentQuestionVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentQuestionVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[AssessmentQuestionVersionShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentreason.htm ===
---
page_id: sforce_api_objects_assessmentreason.htm
title: AssessmentReason
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentreason.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentReason

      Represents the reasons for an assessment such as the associated coverage
         information. This object is available in API version 63.0 and later. 

      

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

                  

            

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the record was last referenced. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The date when the record was last viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| ParentAssessmentId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The parent assessment record that this assessment record belongs to. This field is a relationship field. **Relationship Name** ParentAssessment **Relationship Type** Master-detail **Refers To** Assessment (the master object) |
| ReferenceRecordId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The reason for the assessment. This field is a polymorphic relationship field. **Relationship Name** ReferenceRecord **Refers To** ClinicalServiceRequest, MedicationRequest |
| ReferenceValue | **Type** textarea **Properties** Create, Nillable, Update **Description** The assessment reason in JSON format when there is no Salesforce record to be added as the reference record. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentReasonChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentReasonFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentReasonHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: sforce_api_objects_assessmentsavedsession.htm ===
---
page_id: sforce_api_objects_assessmentsavedsession.htm
title: AssessmentSavedSession
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentsavedsession.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentSavedSession

      Represents a session of an assessment that's saved to resume for later.
      This object is available in API version 62.0 and later.

      

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
- 

                  

            

            
| Field | Details |
| --- | --- |
| AssessmentId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The assessment record for which the session is saved. This field is a relationship field. **Relationship Name** Assessment **Relationship Type** Master-detail **Refers To** Assessment |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user referenced the record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user viewed the record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the assessment saved session record. |
| UsageType | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the use case of the saved assessment session. Possible values are: `HealthCloud` |

=== ARTICLE: sforce_api_objects_assessmentsignature.htm ===
---
page_id: sforce_api_objects_assessmentsignature.htm
title: AssessmentSignature
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentsignature.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentSignature

      Stores the respondent’s signature during an assessment. This object is
      available in API version 57.0 and later. 

      

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

                  

            

            
| Field | Details |
| --- | --- |
| AssessmentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The assessment that's associated with the signature. This field is a relationship field. **Relationship Name** Assessment **Relationship Type** Lookup **Refers To** Assessment |
| DateTime | **Type** dateTime **Properties** Create, Filter, Sort, Update **Description** The date and time of signature. |
| DigitalSignatureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The digital signature that's associated with the assessment signature record. This field is a relationship field. **Relationship Name** DigitalSignature **Relationship Type** Lookup **Refers To** DigitalSignature |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of this assessment signature record. |
| OmniscriptIdentifier | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** Identifier of signature instance in OmniScript Form. |
| Place | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The location at the time of signature. |
| SignedBy | **Type** string **Properties** Create, Filter, Group, Sort, Update **Description** The name of the individual who signed the assessment. |
| SignedInitial | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The initial used when signing the assessment. |
| SigneeId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The user or contact who signed the assessment. This field is a polymorphic relationship field. **Relationship Name** Signee **Relationship Type** Lookup **Refers To** Contact, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentSignatureChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentSignatureFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentSignatureHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentSignatureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[AssessmentSignatureShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_assessmentstageddata.htm ===
---
page_id: sforce_api_objects_assessmentstageddata.htm
title: AssessmentStagedData
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_assessmentstageddata.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentStagedData

      Represents the responses to assessment questions when a user captures and
         submits information with the Discovery Framework Data Capture Flow on a mobile device. The
         information is used to create assessment and related records. This object is available
      in API version 63.0 and later. 

      
         

         
         

      

      

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

: 

                  

            

            
| Field | Details |
| --- | --- |
| DynamicDataCaptureId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The Dynamic Data Capture associated with the assessment staged data. This field is a relationship field. **Relationship Name** DynamicDataCapture **Refers To** DynamicDataCapture |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Auto-assigned number that identifies the assessment staged data record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who owns the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Refers To** Group, User |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The parent associated with the assessment staged data record. This field is a relationship field. **Relationship Name** Parent **Refers To** AssessmentStagedData |
| Response | **Type** textarea **Properties** Create, Nillable, Update **Description** The response to assessment questions as submitted by users, in JSON format. |
| ResponseProcessingError | **Type** textarea **Properties** Filter, Nillable, Sort **Description** The error encountered while processing the question responses for creating assessment and related records. |
| ResponseProcessingStatus | **Type** picklist **Properties** Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the status of the processing of question responses, and the creation of the assessment and its related records. Possible values are: `Completed` `Failed` `Pending` The default value is `Pending`. |

      

      

## Associated Objects

         
         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[AssessmentStagedDataChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[AssessmentStagedDataFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[AssessmentStagedDataHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[AssessmentStagedDataOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[AssessmentStagedDataShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_documentdecisionrequirement.htm ===
---
page_id: sforce_api_objects_documentdecisionrequirement.htm
title: DocumentDecisionRequirement
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_documentdecisionrequirement.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# DocumentDecisionRequirement

      Represents the decision criteria that will be used to determine applicable
         documents. This object is available in API version 59.0 and later. 

      

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

                  

            

            
| Field | Details |
| --- | --- |
| Context | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context that's used to determine the applicable documents to be uploaded. |
| DocumentReferenceObjectId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The document category or the document type related to the document decision. This field is a polymorphic relationship field. **Relationship Name** DocumentReferenceObject **Relationship Type** Lookup **Refers To** DocumentCategory, DocumentType |
| HelpText | **Type** string **Properties** Create, Filter, Nillable, Sort, Update **Description** The help information to show to memebers when uploading the document. |
| IsUploadRequired | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether a document upload for a document category is required (true) or not (false). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[DocumentDecisionRequirementChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[DocumentDecisionRequirementFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[DocumentDecisionRequirementHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[DocumentDecisionRequirementOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[DocumentDecisionRequirementShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_externalassessmentdefinition.htm ===
---
page_id: sforce_api_objects_externalassessmentdefinition.htm
title: ExternalAssessmentDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_externalassessmentdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# ExternalAssessmentDefinition

      Stores information about external assessments. This object is available
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
- 

                  

            

            
| Field | Details |
| --- | --- |
| AssessmentCategory | **Type** picklist **Properties** Create, Filter, Group, Nillable, Restricted picklist, Sort, Update **Description** Specifies the guideline category the external assessment belongs to. Possible values are: `CCG` `TC` |
| AssessmentContentVersion | **Type** string **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The version number of the external assessment's content. |
| CustomAssessmentDisclaimer | **Type** textarea **Properties** Create, Nillable, Update **Description** A disclaimer for custom assessments sent by the external API. |
| ExternalIdentifier | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The unique identifier of the external assessment. |
| IsCustomAssessment | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the external assessment is a custom assessment authored by the user (true) or an out-of-the-box assessment (false). The default value is `false`. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user viewed this record. |
| Name | **Type** string **Properties** Create, Filter, Group, idLookup, Sort, Update **Description** The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| SourceSystemName | **Type** picklist **Properties** Create, Filter, Group, Sort, Update **Description** The source system from which the record was retrieved. Possible values are: `MCG` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[ExternalAssessmentDefinitionFeed](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[ExternalAssessmentDefinitionHistory](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[ExternalAssessmentDefinitionShare](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_omniprocessasmtquestionver.htm ===
---
page_id: sforce_api_objects_omniprocessasmtquestionver.htm
title: OmniProcessAsmtQuestionVer
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_omniprocessasmtquestionver.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# OmniProcessAsmtQuestionVer

Represents a junction between an OmniScript process and an assessment
         question version. This object is available in API version 55.0 and later.

      

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

                  

               

            
| Field | Details |
| --- | --- |
| AssessmentQuestionVersionId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of assessment question version associated with the Omni Process assessment question version record. This is a relationship field. **Relationship Name** AssessmentQuestionVersion **Relationship Type** Lookup **Refers To** AssessmentQuestionVersion |
| IsImportant | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the assessment question version is important (`true`) or not (`false`). The default value is `false`. Available in API version 59.0 and later. |
| IsPrefill | **Type** boolean **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** Indicates whether the assessment question version is prefilled (`true`) or not (`false`). The default value is `false`. Available in API version 60.0 and later. |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed a record related to this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The timestamp for when the current user last viewed this record. If this value is null, it’s possible that this record was referenced (LastReferencedDate) and not viewed. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** Required. The name of the Omni Process assessment question version record. |
| OmniProcessElementId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the Omni Process element associated with the Omni Process assessment question version record. This is a relationship field. **Relationship Name** OmniProcessElement **Relationship Type** Lookup **Refers To** OmniProcessElement |
| OmniProcessId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** Required. The ID of the Omni Process associated with the Omni Process assessment question version record. This is a relationship field. **Relationship Name** OmniProcess **Relationship Type** Lookup **Refers To** OmniProcess |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the relationship record. This is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| QuestionWeight | **Type** double **Properties** Create, Filter, Nillable, Sort, Update **Description** A non-negative weight assigned to the question in the Omni process. Higher values give the question more weight. This field is available in API version 67.0 and later. |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[OmniProcessAsmtQuestionVerChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm)**

               
: Change events are available for the object.

            
            
               

**[OmniProcessAsmtQuestionVerFeed](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[OmniProcessAsmtQuestionVerHistory](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[OmniProcessAsmtQuestionVerOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

               
: Sharing rules are available for the object.

            
            
               

**[OmniProcessAsmtQuestionVerShare](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_suggestedassessmentdef.htm ===
---
page_id: sforce_api_objects_suggestedassessmentdef.htm
title: SuggestedAssessmentDef
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_suggestedassessmentdef.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SuggestedAssessmentDef

      Stores information about suggested assessments. This object is available
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
- 
- 

                  

            

            
| Field | Details |
| --- | --- |
| AssessmentDefinitionRefId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The reference record of the object associated with the suggested assessment. This field is a polymorphic relationship field. **Relationship Name** AssessmentDefinitionRef **Relationship Type** Lookup **Refers To** ExternalAssessmentDefinition, OmniProcess |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| OwnerId | **Type** reference **Properties** Create, Defaulted on create, Filter, Group, Sort, Update **Description** The ID of the user who created the record. This field is a polymorphic relationship field. **Relationship Name** Owner **Relationship Type** Lookup **Refers To** Group, User |
| PartyId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The party for whom the assessment is suggested. This field is a polymorphic relationship field. **Relationship Name** Party **Relationship Type** Lookup **Refers To** Account |
| SourceContextId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The context from which the suggested assessment definition record was created. This field is a polymorphic relationship field. **Relationship Name** SourceContext **Relationship Type** Lookup **Refers To** Case, ClinicalServiceRequest |
| Status | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort, Update **Description** Specifies the status of the suggested assessment. Possible values are: `Completed` `Ignored` `InProgress`—In Progress `Suggested` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[SuggestedAssessmentDefFeed](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[SuggestedAssessmentDefHistory](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

            
            
               

**[SuggestedAssessmentDefShare](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

               
: Sharing is available for the object.

=== ARTICLE: sforce_api_objects_suggestedassessmentreason.htm ===
---
page_id: sforce_api_objects_suggestedassessmentreason.htm
title: SuggestedAssessmentReason
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_suggestedassessmentreason.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# SuggestedAssessmentReason

      Stores the reasons for a suggested assessment. This object is available
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

                  

            

            
| Field | Details |
| --- | --- |
| LastReferencedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user referenced this record. |
| LastViewedDate | **Type** dateTime **Properties** Filter, Nillable, Sort **Description** The most recent date on which a user viewed this record. |
| Name | **Type** string **Properties** Autonumber, Defaulted on create, Filter, idLookup, Sort **Description** The name of the record. |
| PrimaryAsmtQuestionResponseId | **Type** reference **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** The response value in the primary assessment that triggered the suggested assessment. This field is a relationship field. **Relationship Name** PrimaryAsmtQuestionResponse **Relationship Type** Lookup **Refers To** AssessmentQuestionResponse |
| PrimaryAssessmentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The primary assessment from which a suggested assessment was triggered. This field is a relationship field. **Relationship Name** PrimaryAssessment **Relationship Type** Lookup **Refers To** Assessment |
| SuggestedAssessmentDefId | **Type** reference **Properties** Create, Filter, Group, Sort, Update **Description** The suggested assessment associated with the suggested assessment reason. This field is a relationship field. **Relationship Name** SuggestedAssessmentDef **Relationship Type** Lookup **Refers To** SuggestedAssessmentDef |
| SuggestionSourceType | **Type** picklist **Properties** Create, Filter, Group, Nillable, Sort, Update **Description** Specifies the source of the logic by which an assessment was suggested. Possible values are: `Business Rule` `MCG` |

      

      

## Associated Objects

         
         

This object has the following associated objects. If the API version isn’t specified,
            they’re available in the same API versions as this object. Otherwise, they’re available
            in the specified API version and later.

         
            
               

**[SuggestedAssessmentReasonFeed](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

               
: Feed tracking is available for the object.

            
            
               

**[b](https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

               
: History is available for tracked fields of the object.

=== ARTICLE: tooling_api_objects_assessmentquestionconfig.htm ===
---
page_id: tooling_api_objects_assessmentquestionconfig.htm
title: AssessmentQuestionConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_assessmentquestionconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_tooling_api_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionConfig

Represents the assessment question record metadata
         configuration. This object is available in API version 56.0 and later.

      
      

## Supported SOAP API Calls

      
      

            `describeSObjects()`, `query()`, `retrieve()`

      

      

## Supported REST API Methods

               

`GET, HEAD, Query`

      

      

## Special Access Rules

To use this tooling API object, you must enable
         the Discovery Framework feature in your Salesforce org.

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance slows down while Salesforce generates one for each record. |
| Language | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Language of the assessment question. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** Label of the assessment question. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |

=== ARTICLE: tooling_api_objects_assessmentquestionsetconfig.htm ===
---
page_id: tooling_api_objects_assessmentquestionsetconfig.htm
title: AssessmentQuestionSetConfig
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_assessmentquestionsetconfig.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Discovery Framework
parent_page: discovery_framework_tooling_api_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# AssessmentQuestionSetConfig

Reqpresents the assessment question set record metadata
         configuration. This object is available in API version 56.0 and later.

      
      

## Supported SOAP API Calls

      
      

            `describeSObjects()`, `query()`, `retrieve()`

      

      

## Supported REST API Methods

               

`GET, HEAD, Query`

      

      

## Special Access Rules

To use this tooling API object, you must enable
         the Discovery Framework feature in your Salesforce org.

      

## Fields

         
         

               
               
            
               
                  

                  

               

            

            
                  
                     

                     

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
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The unique name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. Note When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance slows down while Salesforce generates one for each record. |
| Language | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** Language of the assessment question set. |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package. Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** string **Properties** Filter, Group, Sort **Description** Label of the assessment question set. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** Namespace prefix associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. |

