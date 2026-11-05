# Industries Common Resources Developer Guide 264 — sección: Timeline (5 artículos)

=== ARTICLE: sforce_api_objects_timelineobjectdefinitionlocalization.htm ===
---
page_id: sforce_api_objects_timelineobjectdefinitionlocalization.htm
title: TimelineObjectDefinitionLocalization
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_objects_timelineobjectdefinitionlocalization.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Timeline
parent_page: timeline_standard_objects.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TimelineObjectDefinitionLocalization

      Represents the translated value of a timeline configuration’s master label
         when the Translation Workbench is enabled for your organization. This object is
      available in API version 60.0 and later. 

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Special Access Rules

Translation Workbench must be enabled for your
         org.

      

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
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

                  

                  
                     

                     

: 

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
| Language | **Type** picklist **Properties** Create, Filter, Group, Restricted picklist, Sort **Description** The language of the translated label. Possible values are: `af`—Afrikaans `am`—Amharic `ar`—Arabic `ar_AE`—Arabic (United Arab Emirates) `ar_BH`—Arabic (Bahrain) `ar_DZ`—Arabic (Algeria) `ar_EG`—Arabic (Egypt) `ar_IQ`—Arabic (Iraq) `ar_JO`—Arabic (Jordan) `ar_KW`—Arabic (Kuwait) `ar_LB`—Arabic (Lebanon) `ar_LY`—Arabic (Libya) `ar_MA`—Arabic (Morocco) `ar_OM`—Arabic (Oman) `ar_QA`—Arabic (Qatar) `ar_SA`—Arabic (Saudi Arabia) `ar_SD`—Arabic (Sudan) `ar_SY`—Arabic (Syria) `ar_TN`—Arabic (Tunisia) `ar_YE`—Arabic (Yemen) `bg`—Bulgarian `bn`—Bengali `bs`—Bosnian `ca`—Catalan `cac`—Chuj `cak`—Kaqchikel `cs`—Czech `cy`—Welsh `da`—Danish `de`—German `de_AT`—German (Austria) `de_BE`—German (Belgium) `de_CH`—German (Switzerland) `de_LU`—German (Luxembourg) `el`—Greek `el_CY`—Greek (Cyprus) `en_AE`—English (United Arab Emirates) `en_AU`—English (Australian) `en_BE`—English (Belgium) `en_CA`—English (Canadian) `en_CY`—English (Cyprus) `en_DE`—English (Germany) `en_GB`—English (UK) `en_HK`—English (Hong Kong) `en_IE`—English (Ireland) `en_IL`—English (Israel) `en_IN`—English (Indian) `en_IT`—English (Italy) `en_MT`—English (Malta) `en_MY`—English (Malaysian) `en_NL`—English (Netherlands) `en_NZ`—English (New Zealand) `en_PH`—English (Phillipines) `en_SG`—English (Singapore) `en_US`—English `en_ZA`—English (South Africa) `eo`—Esperanto (Pseudo) `es`—Spanish `es_AR`—Spanish (Argentina) `es_BO`—Spanish (Bolivia) `es_CL`—Spanish (Chile) `es_CO`—Spanish (Colombia) `es_CR`—Spanish (Costa Rica) `es_DO`—Spanish (Dominican Republic) `es_EC`—Spanish (Ecuador) `es_GT`—Spanish (Guatemala) `es_HN`—Spanish (Honduras) `es_MX`—Spanish (Mexico) `es_NI`—Spanish (Nicaragua) `es_PA`—Spanish (Panama) `es_PE`—Spanish (Peru) `es_PR`—Spanish (Puerto Rico) `es_PY`—Spanish (Paraguay) `es_SV`—Spanish (El Salvador) `es_US`—Spanish (United States) `es_UY`—Spanish (Uruguay) `es_VE`—Spanish (Venezuela) `et`—Estonian `eu`—Basque `fa`—Farsi `fi`—Finnish `fr`—French `fr_BE`—French (Belgium) `fr_CA`—French (Canadian) `fr_CH`—French (Switzerland) `fr_LU`—French (Luxembourg) `fr_MA`—French (Morocco) `ga`—Irish `gu`—Gujarati `haw`—Hawaiian `hi`—Hindi `hmn`—Hmong `hr`—Croatian `ht`—Haitian Creole `hu`—Hungarian `hy`—Armenian `in`—Indonesian `is`—Icelandic `it`—Italian `it_CH`—Italian (Switzerland) `iw`—Hebrew `iw_EO`—Esperanto RTL (Pseudo) `ja`—Japanese `ji`—Yiddish `ka`—Georgian `kk`—Kazakh `kl`—Greenlandic `km`—Khmer `kn`—Kannada `ko`—Korean `lb`—Luxembourgish `lt`—Lithuanian `lv`—Latvian `mi`—Te reo `mk`—Macedonian `ml`—Malayalam `mr`—Marathi `ms`—Malay `mt`—Maltese `my`—Burmese `nl_BE`—Dutch (Belgium) `nl_NL`—Dutch `no`—Norwegian `pa`—Punjabi `pl`—Polish `pt_BR`—Portuguese (Brazil) `pt_PT`—Portuguese (European) `quc`—Kiche `rm`—Romansh `ro`—Romanian `ro_MD`—Romanian (Moldova) `ru`—Russian `ru_AM`—Russian (Armenia) `ru_BY`—Russian (Belarus) `ru_KG`—Russian (Kyrgyzstan) `ru_KZ`—Russian (Kazakhstan) `ru_LT`—Russian (Lithuania) `ru_MD`—Russian (Moldova) `ru_PL`—Russian (Poland) `ru_UA`—Russian (Ukraine) `sh`—Serbian (Latin) `sh_ME`—Montenegrin `sk`—Slovak `sl`—Slovene `sm`—Samoan `sq`—Albanian `sr`—Serbian (Cyrillic) `sv`—Swedish `sw`—Swahili `ta`—Tamil `te`—Telugu `th`—Thai `tl`—Tagalog `tr`—Turkish `uk`—Ukrainian `ur`—Urdu `vi`—Vietnamese `xh`—Xhosa `zh_CN`—Chinese (Simplified) `zh_HK`—Chinese (Hong Kong) `zh_MY`—Chinese (Malaysia) `zh_SG`—Chinese (Singapore) `zh_TW`—Chinese (Traditional) `zu`—Zulu |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix that is associated with this object. Each Developer Edition org that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values. In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the org for all objects that support it, unless an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition org of the package developer. In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects that are part of an installed managed package. All other objects have no namespace prefix. |
| ParentId | **Type** reference **Properties** Create, Filter, Group, Sort **Description** The ID of the related timeline configuration. This field is a relationship field. This field is a relationship field. **Relationship Name** Parent **Relationship Type** Lookup **Refers To** TimelineObjectDefinition |
| Value | **Type** textarea **Properties** Create, Filter, Sort, Update **Description** The translated master label of the timeline configuration. |

=== ARTICLE: timeline.htm ===
---
page_id: timeline.htm
title: Timeline
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/timeline.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Timeline
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Timeline

The Timeline component shows key events relating to a person or a resource in one place,
  so your users can see information from a single source of truth.

- 
**[Timeline Standard Object](./timeline_standard_objects.htm.md)**  

Use the standard object to translate timeline labels.

- 
**[Timeline Tooling API Object](./timeline_tooling_api_object.htm.md)**  

Tooling API exposes metadata used in developer tooling that   you can access through REST or SOAP. Tooling API’s SOQL capabilities for many metadata types allow   you to retrieve smaller pieces of metadata. For more information about Tooling API objects and to   find a complete reference of all the supported objects, see **[Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)**.

#### See Also

- [*Salesforce Help*: View Events Using Timeline in Salesforce](https://help.salesforce.com/s/articleView?id=ind.timeline.htm&type=5&language=en_US)

=== ARTICLE: timeline_standard_objects.htm ===
---
page_id: timeline_standard_objects.htm
title: Timeline Standard Object
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/timeline_standard_objects.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Timeline
parent_page: timeline.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Timeline Standard Object

Use the standard object to translate timeline labels.

- 
**[TimelineObjectDefinitionLocalization](./sforce_api_objects_timelineobjectdefinitionlocalization.htm.md)**  

       Represents the translated value of a timeline configuration’s master label          when the Translation Workbench is enabled for your organization. This object is       available in API version 60.0 and later.

=== ARTICLE: timeline_tooling_api_object.htm ===
---
page_id: timeline_tooling_api_object.htm
title: Timeline Tooling API Object
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/timeline_tooling_api_object.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Timeline
parent_page: timeline.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# Timeline Tooling API Object

Tooling API exposes metadata used in developer tooling that
  you can access through REST or SOAP. Tooling API’s SOQL capabilities for many metadata types allow
  you to retrieve smaller pieces of metadata. For more information about Tooling API objects and to
  find a complete reference of all the supported objects, see **[Introducing Tooling API](https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_api_tooling.htm)**.

- 
**[TimelineObjectDefinition](./tooling_api_objects_timelineobjectdefinition.htm.md)**  

Represents the timeline configurations. This object is available       in API version 55.0 and later.

=== ARTICLE: tooling_api_objects_timelineobjectdefinition.htm ===
---
page_id: tooling_api_objects_timelineobjectdefinition.htm
title: TimelineObjectDefinition
source_url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/tooling_api_objects_timelineobjectdefinition.htm
release: 264
release_name: Winter '27
deliverable: industries_reference
section: Timeline
parent_page: timeline_tooling_api_object.htm
fetched_at: 2026-08-24
---

Note: This release is in preview. Features described here don’t become generally available until the latest general availability date that Salesforce announces for this release. Before then, and where features are noted as beta, pilot, or developer preview, we can’t guarantee general availability within any particular time frame or at all. Make your purchase decisions only on the basis of generally available products and features.

# TimelineObjectDefinition

Represents the timeline configurations. This object is available
      in API version 55.0 and later.

      
         

#### Important

Where possible, we changed noninclusive terms to align with our
            company value of Equality. We maintained certain terms to avoid any effect on customer
            implementations.

      

      

## Supported SOAP API Calls

         
         

            `create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`
         

      

      

## Supported REST API Methods

         
         

`DELETE, GET, HEAD, PATCH, POST, Query`
         

      

      

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
- 
- 
- 
- 
- 
- 
- 
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
| BaseObject | **Type** picklist **Properties** Filter, Group, Restricted picklist, Sort **Description** The object on which a timeline is based. Information displayed in a timeline comes from objects that are related to the base object. The base object can be any Salesforce object, standard or custom. |
| Definition | **Type** textarea **Properties** Create, Update **Description** The timeline definition stored in JSON format. |
| DeveloperName | **Type** string **Properties** Filter, Group, Sort **Description** The developer name of the timeline. |
| FullName | **Type** string **Properties** Create, Group, Nillable **Description** |
| IsActive | **Type** boolean **Properties** Defaulted on create, Filter, Group, Sort **Description** Indicates whether the timeline is active. The default value is `false`. |
| Language | **Type** picklist **Properties** Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort **Description** The language of the timeline object definition. Possible values are: `da`—Danish `de`—German `en_US`—English `es`—Spanish `es_MX`—Spanish (Mexico) `fi`—Finnish `fr`—French `it`—Italian `ja`—Japanese `ko`—Korean `nl_NL`—Dutch `no`—Norwegian `pt_BR`—Portuguese (Brazil) `ru`—Russian `sv`—Swedish `th`—Thai `zh_CN`—Chinese (Simplified) `zh_TW`—Chinese (Traditional) |
| ManageableState | **Type** picklist **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Possible values are: `beta`—Managed-Beta `deleted`—Managed-Proposed-Deleted `deprecated`—Managed-Proposed-Deprecated `deprecatedEditable`—SecondGen-Installed-Deprecated `installed`—Managed-Installed `installedEditable`—SecondGen-Installed-Editable `released`—Managed-Released `unmanaged`—Unmanaged |
| MasterLabel | **Type** ManageableState enumerated list **Properties** Filter, Group, Nillable, Restricted picklist, Sort **Description** Indicates the manageable state of the specified component that is contained in a package: `beta` `deleted` `deprecated` `deprecatedEditable` `installed` `installedEditable` `released` `unmanaged` |
| Metadata | **Type** TimelineObjectDefinition **Properties** Create, Nillable, Update **Description** The timeline object definition's metadata. |
| NamespacePrefix | **Type** string **Properties** Filter, Group, Nillable, Sort **Description** The namespace prefix associated with this object. Each Developer Edition organization that creates a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a component in a managed package by using the `namespacePrefix__componentName` notation. The namespace prefix can have one of the following values: In Developer Edition organizations, the namespace prefix is set to the namespace prefix of the organization for all objects that support it. There is an exception if an object is in an installed managed package. In that case, the object has the namespace prefix of the installed managed package. This field’s value is the namespace prefix of the Developer Edition organization of the package developer. In organizations that are not Developer Edition organizations, NamespacePrefix is only set for objects that are part of an installed managed package. There is no namespace prefix for all other objects. |

      

      

## Associated Objects

         
         

This
            object has the following associated objects. If the API version isn’t
            specified, they’re available in the same API versions as this object. Otherwise, they’re
            available in the specified API version and later.

         
            
               

**
[TimelineObjectDefinitionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/sforce_api_associated_objects_change_event.htm) (API version 60.0)**

               
: Change events are available for the object.

